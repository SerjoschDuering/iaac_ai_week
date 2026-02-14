"""Dummy IFC compliance checks for teaching prototype."""

import ifcopenshell
import ifcopenshell.util.element as util_element


def get_property_value(element, pset_name, prop_name):
    """Extract a property value from an element's property sets."""
    psets = util_element.get_psets(element)
    if pset_name in psets and prop_name in psets[pset_name]:
        return psets[pset_name][prop_name]
    # Search all psets for the property name (case-insensitive)
    prop_lower = prop_name.lower()
    for pset, props in psets.items():
        if prop_name in props:
            return props[prop_name]
        for key, val in props.items():
            if key.lower() == prop_lower:
                return val
    return None


def check_min_room_area(model, min_area=9.0):
    """Check that all rooms (IfcSpace) have area >= min_area m²."""
    results = []
    spaces = model.by_type("IfcSpace")
    for space in spaces:
        # Try standard IFC quantity names first, then Revit/vendor-specific
        area = get_property_value(space, "Qto_SpaceBaseQuantities", "NetFloorArea")
        if area is None:
            area = get_property_value(space, "Qto_SpaceBaseQuantities", "GrossFloorArea")
        if area is None:
            area = get_property_value(space, "PSet_Revit_Dimensions", "Area")
        if area is None:
            area = get_property_value(space, "GSA Space Areas", "GSA BIM Area")
        if area is None:
            area = get_property_value(space, "BaseQuantities", "Area")

        name = space.Name or space.LongName or f"Space #{space.id()}"
        if area is not None:
            passed = area >= min_area
            results.append({
                "element_id": space.GlobalId,
                "element_type": "IfcSpace",
                "element_name": name,
                "rule": "Minimum Room Area",
                "requirement": f">= {min_area} m²",
                "actual": f"{area:.1f} m²",
                "passed": passed,
            })
        else:
            results.append({
                "element_id": space.GlobalId,
                "element_type": "IfcSpace",
                "element_name": name,
                "rule": "Minimum Room Area",
                "requirement": f">= {min_area} m²",
                "actual": "N/A (no area data)",
                "passed": None,
            })
    return results


def check_wall_thickness(model, min_thickness=0.1):
    """Check that all walls are at least min_thickness meters thick."""
    results = []
    walls = model.by_type("IfcWall")
    for wall in walls:
        width = get_property_value(wall, "Qto_WallBaseQuantities", "Width")
        if width is None:
            width = get_property_value(wall, "BaseQuantities", "Width")
        if width is None:
            # Try to get from type
            wall_type = util_element.get_type(wall)
            if wall_type:
                width = get_property_value(wall_type, "Pset_WallCommon", "Width")

        name = wall.Name or f"Wall #{wall.id()}"
        if width is not None:
            passed = width >= min_thickness
            results.append({
                "element_id": wall.GlobalId,
                "element_type": "IfcWall",
                "element_name": name,
                "rule": "Wall Thickness",
                "requirement": f">= {min_thickness*1000:.0f} mm",
                "actual": f"{width*1000:.0f} mm" if width < 10 else f"{width:.0f} mm",
                "passed": passed,
            })
    return results


def check_door_width(model, min_width=0.8):
    """Check that doors are at least min_width meters wide (accessibility)."""
    results = []
    doors = model.by_type("IfcDoor")
    for door in doors:
        width = door.OverallWidth
        if width is None:
            width = get_property_value(door, "Qto_DoorBaseQuantities", "Width")

        name = door.Name or f"Door #{door.id()}"
        if width is not None:
            # Width might be in mm in some files
            w = width / 1000.0 if width > 10 else width
            passed = w >= min_width
            results.append({
                "element_id": door.GlobalId,
                "element_type": "IfcDoor",
                "element_name": name,
                "rule": "Door Width (Accessibility)",
                "requirement": f">= {min_width*1000:.0f} mm",
                "actual": f"{w*1000:.0f} mm",
                "passed": passed,
            })
    return results


def check_window_per_space(model):
    """Check that each room has at least one window."""
    results = []
    spaces = model.by_type("IfcSpace")
    windows = model.by_type("IfcWindow")

    # Build set of spaces that contain or are near windows
    spaces_with_windows = set()
    for window in windows:
        # Check spatial containment via IfcRelContainedInSpatialStructure
        for rel in model.by_type("IfcRelContainedInSpatialStructure"):
            if window in rel.RelatedElements:
                container = rel.RelatingStructure
                spaces_with_windows.add(container.GlobalId)

        # Also check via IfcRelFillsElement -> IfcRelVoidsElement
        for rel in getattr(window, "FillsVoids", []) or []:
            opening = rel.RelatingOpeningElement
            for void_rel in getattr(opening, "VoidsElements", []) or []:
                host = void_rel.RelatingBuildingElement
                # Find which space the host wall belongs to
                for space_rel in model.by_type("IfcRelSpaceBoundary"):
                    if getattr(space_rel, "RelatedBuildingElement", None) == host:
                        spaces_with_windows.add(space_rel.RelatingSpace.GlobalId)

    for space in spaces:
        name = space.Name or space.LongName or f"Space #{space.id()}"
        has_window = space.GlobalId in spaces_with_windows
        results.append({
            "element_id": space.GlobalId,
            "element_type": "IfcSpace",
            "element_name": name,
            "rule": "Window per Room",
            "requirement": "At least 1 window",
            "actual": "Yes" if has_window else "No",
            "passed": has_window,
        })
    return results


def run_all_checks(ifc_path):
    """Run all compliance checks and return combined results."""
    model = ifcopenshell.open(ifc_path)

    all_results = []
    all_results.extend(check_min_room_area(model))
    all_results.extend(check_wall_thickness(model))
    all_results.extend(check_door_width(model))
    all_results.extend(check_window_per_space(model))

    # Summary
    total = len(all_results)
    passed = sum(1 for r in all_results if r["passed"] is True)
    failed = sum(1 for r in all_results if r["passed"] is False)
    unknown = sum(1 for r in all_results if r["passed"] is None)

    failed_ids = [r["element_id"] for r in all_results if r["passed"] is False]

    return {
        "results": all_results,
        "summary": {"total": total, "passed": passed, "failed": failed, "unknown": unknown},
        "failed_ids": set(failed_ids),
        "model": model,
    }
