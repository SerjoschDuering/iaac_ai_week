# Prototype Learnings & Pitfalls

Notes from building the IFC Compliance Checker prototype (Gradio + ifcopenshell + trimesh).

## Python Version Matters

**Problem:** Gradio 4.44.1 crashes on Python 3.9 with `TypeError: argument of type 'bool' is not iterable` in `gradio_client/utils.py:863`. The `gr.Model3D` component's JSON schema contains `additionalProperties: true` (a boolean), but the `get_type()` function expects a dict and tries `"const" in schema` on it.

**Fix applied:** Downgraded to Gradio 4.31.0 AND monkey-patched `gradio_client/utils.py` — added `if not isinstance(schema, dict): return schema` guard in `get_type()` and `_json_schema_to_python_type()`.

**Lesson:** Use Python 3.10+ for Gradio. For the course, students should use a recent Python. The conda base env (3.9) is too old.

## IFC Property Sets Are Vendor-Specific

**Problem:** Standard IFC quantity names like `Qto_SpaceBaseQuantities.NetFloorArea` return `None` for many real-world IFC files. Revit exports use `PSet_Revit_Dimensions.Area`, ArchiCAD uses different names, etc.

**Fix:** Chain of fallbacks in `get_property_value()`:
1. Try exact pset + prop name
2. Try alternative pset names (Revit, GSA, BaseQuantities)
3. Case-insensitive search across all psets

**Lesson:** Never assume a single property path. Real IFC files are messy. Students should explore psets with `ifcopenshell.util.element.get_psets(element)` before writing checks.

## GLB Geometry Needs World Coordinates

**Problem:** First attempt at IFC→GLB conversion produced a distorted/exploded model. Elements were placed at their local origins, not their world positions.

**Fix:** `settings.set(settings.USE_WORLD_COORDS, True)` in ifcopenshell geometry settings. This applies the full IfcLocalPlacement chain before returning vertices.

**Lesson:** Always use `USE_WORLD_COORDS` when extracting geometry for visualization. Without it, each element sits at its own local origin.

## PBR Materials vs Face Colors

**Problem:** Using `mesh.visual.face_colors = [r, g, b, a]` produces flat/unlit-looking models in three.js viewers. The GLB exports as unlit material.

**Fix:** Use `trimesh.visual.TextureVisuals(material=PBRMaterial(...))` with explicit `baseColorFactor`, `metallicFactor`, `roughnessFactor`. For transparency, set `alphaMode="BLEND"` on the material.

**Lesson:** For any web-based 3D viewer, use PBR materials. Face colors are fine for debugging but look bad in production.

## Gradio Model3D Limitations

The built-in `gr.Model3D` viewer is basic three.js:
- No clipping planes
- No element picking/selection
- No measurement tools
- No section cuts
- Limited lighting control (only `clear_color` for background)
- No BIM-specific features (storey filtering, element info on hover)

**For the course:** Gradio is fine for a prototype/demo. For the final product, consider:
- **That Open Engine** (IFC-native web viewer with Highlighter/Classifier)
- **xeokit** (BIM-specific SDK with section planes, measurements)
- Custom three.js viewer embedded via `gr.HTML`

## Gradio `/info` Endpoint

**Problem:** Even with `show_api=False`, the Gradio frontend hits `/info` on load. If this endpoint crashes (Python 3.9 bug), the entire app shows "API not found" despite the HTML loading fine.

**Lesson:** The `/info` endpoint must work even if you don't want to expose an API. The `show_api=False` flag only hides the API docs page, it doesn't disable the internal API that the frontend depends on.

## IFC Element Types to Skip

When iterating `IfcProduct` for 3D export, skip these:
- `IfcSite` — ground/terrain, usually huge
- `IfcBuilding` — bounding volume, not real geometry
- `IfcBuildingStorey` — floor plane, overlaps real geometry
- `IfcSpace` — room volumes, occlude everything
- `IfcOpeningElement` — void cutouts, not visible

## File Sizes

For the Duplex Apartment (2.3MB IFC):
- 113 compliance check elements
- 215 mesh elements in GLB
- ~330KB GLB output
- ~3.3s for geometry extraction
- ~0.2s for compliance checks

Larger models (13MB Office Building) will be significantly slower. Consider progress indicators for the course.

## Dependencies

Minimum working set:
```
ifcopenshell>=0.8.4   # ARM64 wheels available since Dec 2025
trimesh
numpy
gradio>=4.20,<4.44    # avoid 4.44+ on Python 3.9
```

ifcopenshell has native aarch64 wheels since v0.8.4, so ARM servers (Hetzner CAX) work fine.
