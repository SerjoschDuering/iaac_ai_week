# Understanding IFC Files -- Structure, Entities, Properties, and How to Work With Them

## What This Document Covers

This reference guide explains the IFC file format for architecture and design students who use Revit or ArchiCAD but have never worked with IFC data programmatically. It covers the structure of IFC files, the types of entities inside them, how properties and relationships work, the notorious "vendor problem," and how compliance checks actually read and use this data.

---

## 1. What Is IFC?

IFC stands for **Industry Foundation Classes**. It is the open, universal file format for describing buildings digitally.

### Key Facts

- IFC is **not owned by any single company**. It is maintained by buildingSMART International, a neutral industry organization.
- Revit files (.rvt) only work in Revit. ArchiCAD files (.pln) only work in ArchiCAD. IFC files work across all of them.
- IFC is to building data what HTML is to web pages: an open standard that any tool can read and write.
- When you hit "Export to IFC" in Revit, **all** the building data -- geometry, properties, relationships, spatial organization -- goes into one .ifc file.

### Why IFC Matters

The core purpose of IFC is **interoperability**: moving building data between different software tools without losing information. It is the closest thing the architecture, engineering, and construction industry has to a common language.

Software that can read and write IFC includes Revit, ArchiCAD, Tekla, Allplan, Vectorworks, and dozens of others.

---

## 2. What Is Actually Inside an IFC File?

Here is something that surprises most people: **an IFC file is a plain text file**. You can open it in Notepad on Windows or TextEdit on Mac.

### The STEP Format

IFC files use the STEP format (ISO 10303), an engineering data exchange standard. Each line in the file describes one piece of the building. A typical line looks something like this:

```
#42= IFCDOOR('2O2Fr$t4X7Zf8FXbfg3SIB', ..., 'Main Entrance', ..., 0.9, 2.1);
```

That single line describes a door: its unique identifier, its name ("Main Entrance"), and its dimensions.

### Think of It as an Inventory List

An IFC file is like a massive, highly organized inventory list of everything in the building:

- Every wall, door, window, room, column, beam, slab
- Their dimensions, materials, and positions in 3D space
- How they relate to each other (which door is in which wall, which wall is on which floor, which walls form the boundary of which room)

A small building might have a few hundred lines. A large hospital or airport project can have tens of thousands.

---

## 3. IFC Entity Types -- The Building Blocks

IFC defines specific entity types for different categories of building elements. The names are intuitive once you get past the "Ifc" prefix.

### Physical Building Elements

| Entity Type | What It Represents | Key Properties | You Will Use It For |
|---|---|---|---|
| IfcWall | Walls | Thickness, material, height | Wall thickness checks |
| IfcDoor | Doors | Width, height, type | Door width and accessibility checks |
| IfcWindow | Windows | Width, height, glazing type | Window-per-room checks |
| IfcSpace | Rooms and spaces | Area, volume, name (e.g., "Kitchen") | Room area checks |
| IfcSlab | Floors and roofs | Thickness, material | Structural checks |
| IfcColumn | Columns | Dimensions, material | Structural checks |
| IfcBeam | Beams | Span, cross-section | Structural checks |
| IfcOpeningElement | Holes cut through walls | Dimensions | Understanding where doors and windows sit |

### Hierarchy Entities (Organizational Containers)

These entities do not represent physical objects you can touch. They organize the building into a logical structure.

| Entity Type | What It Represents | What It Contains |
|---|---|---|
| IfcProject | The entire project | Sites |
| IfcSite | The land or terrain | Buildings |
| IfcBuilding | One building | Storeys (floors) |
| IfcBuildingStorey | One floor or level | Rooms, walls, doors, everything on that floor |
| IfcSpace | One room or area | Contained within a storey |

**Important note for 3D visualization:** IfcSite, IfcBuilding, IfcBuildingStorey, and IfcSpace should be **skipped** when creating 3D views. They are organizational containers whose bounding-box geometry would obscure the actual building elements beneath them. IfcOpeningElement should also be skipped -- it represents the void (the hole), not the door or window that fills it.

---

## 4. The Spatial Hierarchy -- How the Building Is Organized

Every element in an IFC file "lives" somewhere in a tree-like structure. Think of it like a postal address, where each level narrows down the location.

### The Address Analogy

| Level | IFC Entity | Postal Analogy |
|---|---|---|
| Top level | IfcProject | The country |
| Land | IfcSite | The city |
| Structure | IfcBuilding | The street address |
| Floor | IfcBuildingStorey | The floor number |
| Room | IfcSpace | The apartment or room |

### Why This Matters

This hierarchy is how you ask location-based questions about a building:

- "Give me all doors on the 2nd floor" -- navigate to the right IfcBuildingStorey, then find all IfcDoor elements contained within it.
- "What is the total area of all bedrooms in Building A?" -- find the right IfcBuilding, go through its storeys, find all IfcSpace elements with "Bedroom" in their name, and add up their areas.

If you use Revit, this hierarchy maps directly to what you see in the Project Browser: the project contains levels, and each level contains the elements placed on it.

---

## 5. Property Sets -- Where the Real Data Lives

Geometry tells you **where** an element is and **what shape** it has. Properties tell you **everything else**: dimensions, materials, fire ratings, classifications, acoustic values, and more.

### How Properties Are Organized

Properties are grouped into named bundles called **property sets** (abbreviated as Psets). Each property set contains a collection of key-value pairs.

Think of it this way: if an IFC entity is like a person's ID card (name and photo), then the property sets are the full file of records -- medical history, employment records, tax information, everything that makes them more than a name.

### Common Property Set Prefixes

| Prefix | What It Means | Example |
|---|---|---|
| Qto_ (Quantity Take-Off) | Measurable dimensions and quantities | Qto_DoorBaseQuantities contains Width, Height, Area |
| Pset_ (Property Set) | General descriptive properties | Pset_WallCommon contains FireRating, IsExternal |
| PSet_Revit_ | Revit-specific properties (added by Revit during export) | PSet_Revit_Dimensions contains Area |

### Standard vs. Vendor-Specific Property Sets

The IFC specification defines standard property sets. For example, the standard place to find a room's floor area is:

> Qto_SpaceBaseQuantities.NetFloorArea

But in practice, different software puts the same data in different places. This leads us to the single most important lesson about working with IFC files.

---

## 6. The Vendor Problem -- The Most Important Lesson

**Different software exports the same information under different property names.** This is the number-one source of confusion when working with IFC files, and understanding it early will save you hours of frustration.

### The Problem Illustrated

| Information You Want | IFC Standard Name | Revit Might Export As | Other Software Might Use |
|---|---|---|---|
| Room floor area | Qto_SpaceBaseQuantities.NetFloorArea | PSet_Revit_Dimensions.Area | BaseQuantities.Area, GSA BIM Area |
| Wall thickness | Qto_WallBaseQuantities.Width | Stored on the wall type, not the wall instance | BaseQuantities.Width |
| Door width | door.OverallWidth or Qto_DoorBaseQuantities.Width | Varies by Revit version and export settings | Varies by software |

### The Date Format Analogy

This is like date formats around the world. If someone writes **01/02/2025**, what date is that?

- In the United States: January 2nd
- In Europe: February 1st
- In Japan: the convention would be 2025/02/01

Same data. Different packaging. If you assume one format when the file uses another, you get the wrong answer. IFC property sets have exactly the same problem.

### How the Prototype Solves This: Fallback Chains

The course prototype does not look in one place and give up. It uses a **fallback chain** -- a list of places to look, tried in order:

1. **Try the IFC standard property name first.** This is the "correct" location according to the specification.
2. **If not found, try vendor-specific names.** Check the Revit property sets, then ArchiCAD property sets, and so on.
3. **If still not found, do a broad search.** Scan across all property sets on the element, looking for anything that matches the concept (e.g., any property containing "width" or "area").
4. **If nothing works, report "N/A."** The data is genuinely missing from the file.

This is like asking for directions in a foreign city. You try English first. If that does not work, you try the local language. If that fails, you point at a map and use gestures. You keep trying until you find the information or confirm it is not available.

### The Golden Rule

**"Never assume a single property path. Real IFC files are messy."**

This is not a scary obstacle. It is a solvable puzzle, and once you accept it, working with IFC files becomes detective work -- genuinely interesting detective work.

---

## 7. IFC Relationships -- How Elements Connect

Elements in IFC are not floating in isolation. The file explicitly records **how elements are connected to each other** through special relationship entities.

### Key Relationship Types

| Relationship Entity | What It Means | Example |
|---|---|---|
| IfcRelContainedInSpatialStructure | "This element is inside this room/floor" | "Door #42 is on Floor 2" |
| IfcRelVoidsElement | "This opening cuts through this wall" | "Opening #7 punches a hole through Wall #3" |
| IfcRelFillsElement | "This door/window fills this opening" | "Door #42 sits inside Opening #7" |
| IfcRelSpaceBoundary | "This element forms a boundary of this room" | "Wall #3 is one of the walls around the Kitchen" |

### Why Relationships Matter for Compliance Checks

Some compliance questions cannot be answered by looking at individual elements. They require **following a chain of relationships**.

**Example: "Does every room have at least one window?"**

To answer this, you need to trace a path:

1. Start with a **Room** (IfcSpace)
2. Find which **walls** bound that room (via IfcRelSpaceBoundary)
3. Find which **openings** cut through those walls (via IfcRelVoidsElement)
4. Find which **windows** fill those openings (via IfcRelFillsElement)
5. Also check which elements are **directly contained** in the room (via IfcRelContainedInSpatialStructure)

If any window is found through this chain, the room passes. If no window is found, it fails.

This is exactly how the window-per-space check works in the course prototype. It is a chain of connections, like following links in a web.

---

## 8. The Type vs. Occurrence Pattern

IFC separates **types** (templates) from **occurrences** (actual installed items). This distinction matters when you are looking for properties.

### The Concept

| Concept | Analogy | Example |
|---|---|---|
| Type | A product catalog entry | "Interior Door Type A: 800mm wide, oak finish" |
| Occurrence | An actual installed item | "Door #42 in Room 3, using Type A" |

A building might have 50 individual doors (occurrences) but only 3 door types (templates). Dimensions like width and height are often stored on the **type**, not on the individual door instance.

### Why This Matters

When checking a door's width, you might look at the door itself and find nothing. The width is stored on the door's type definition instead. Your code needs to check **both** the occurrence and its type.

The course prototype handles this automatically. If it cannot find a property on the element itself, it looks at the element's type. This is another form of fallback -- similar to the vendor problem, but within the IFC structure itself.

---

## 9. Working with IFC in Python Using ifcopenshell

**ifcopenshell** is the Python library that reads and interprets IFC files. Think of it as your IFC translator. You cannot easily read the raw STEP format yourself, but ifcopenshell turns it into Python objects you can work with.

### Key Operations in Plain Language

| What You Want to Do | What ifcopenshell Does |
|---|---|
| Open an IFC file | Reads the entire file and creates a model object you can query |
| Get all doors in the building | Returns every IfcDoor element as a Python object |
| Get a door's name | Lets you access the Name attribute directly (e.g., "Main Entrance") |
| Get a door's unique identifier | Lets you access the GlobalId (a permanent string like "2O2Fr$t4X7Zf8FXbfg3SIB") |
| Get ALL properties on an element | A utility function returns every property set attached to any element |
| Get one specific property | You look up a value by property set name and property name |

### The Bilingual Guide Analogy

ifcopenshell is like having a bilingual guide in a foreign country. You cannot read the signs on the street yourself, but your guide can read them, translate them, and help you find exactly what you are looking for. ifcopenshell does not change the IFC file -- it just makes the data accessible to you as a Python programmer.

---

## 10. The IFC-Bench Dataset

IFC-Bench is a curated collection of real IFC files designed for learning and testing. It is the practice ground for building confidence before tackling your own projects.

### Dataset Summary

| Metric | Value |
|---|---|
| Number of real building projects | 21 |
| Total IFC files | 37 |
| Question-answer pairs (with known correct answers) | 1,027 |

### Question Complexity Categories

| Category | Difficulty | Example Question |
|---|---|---|
| Direct retrieval | Easy | "What is the width of Door #42?" |
| Aggregation | Medium | "What is the total area of all bedrooms?" |
| Spatial reasoning | Hard | "Which rooms on Floor 2 have exterior walls?" |
| Incomplete information | Expert | "What is the fire rating of Wall #7?" (the data might be missing!) |

### How to Use It

Think of IFC-Bench as a textbook with the answers printed in the back. You write your compliance check code, run it against the files, and compare your results to the known correct answers. If your answers do not match, something in your logic or property lookup needs fixing. It gives you a safe environment to practice before working on real project files.

---

## 11. Common Gotchas When Working with IFC

These are the traps that catch almost everyone at least once. Knowing about them ahead of time will save you significant debugging time.

### Units Inconsistency

Door width might be stored as **0.8** (meters) or **800** (millimeters). If you read 800 and assume it is meters, you will think the door is 800 meters wide.

**How to handle it:** Check whether values seem reasonable. A door width of 0.8 is probably meters. A door width of 800 is probably millimeters. The prototype's door check handles both cases by checking the magnitude of the value and converting accordingly.

### Missing Properties

Not every element has every property filled in. The modeler might have left fields blank, or the export process might have dropped certain properties.

**How to handle it:** Never let your code crash on missing data. Report the result as "N/A" (not applicable) and move on. This is why compliance check results have three possible outcomes: pass, fail, or N/A.

### Generic Element Names

Elements might be labeled "Wall #42" instead of "Exterior North Wall." This depends entirely on how carefully the original model was built.

**How to handle it:** Do not rely on element names for logic. Use entity types, property values, and relationships instead. Names are useful for human-readable reports, but they are unreliable for automated checks.

### Vendor Property Names

The same information stored under different property set names by different software (see Section 6 in detail).

**How to handle it:** Use fallback chains. Try the standard name first, then vendor-specific alternatives, then broad search.

### World vs. Local Coordinates

3D positions in IFC can be expressed in local coordinate systems rather than global building coordinates. An element might appear to be at position (0, 0, 0) in its local space but actually be 50 meters east of the building origin.

**How to handle it:** When extracting geometry for 3D visualization, use the "world coordinates" setting. This converts local positions into the global building coordinate system so everything lines up correctly.

### Large File Sizes

A complex building can contain tens of thousands of elements. Processing them all takes time.

**How to handle it:** Expect delays for large models. A small test file might load in under a second. A real-world hospital project might take significantly longer. Use progress indicators when processing large files so users know the system has not frozen.

---

## 12. What a Compliance Check Actually Does -- Step by Step

This is the core workflow that the course prototype implements. Understanding these steps demystifies the entire process.

### The Sequence

1. **Open the IFC file** using ifcopenshell. This creates a model object you can query.
2. **Query for a specific element type.** For example, ask for all IfcDoor elements in the building.
3. **For each element, read the relevant property.** For a door width check, read the door's width. For a room area check, read the space's floor area.
4. **Handle the vendor problem.** Try the standard property name first, then vendor-specific fallbacks, then broad search.
5. **Compare the actual value against the regulation threshold.** Is the door at least 800mm wide? Is the room at least 9 square meters?
6. **Produce a result:** Pass (meets the requirement), Fail (does not meet it), or N/A (data was missing and no determination could be made).
7. **Collect all results** into a structured format -- one result record per element checked.
8. **Return the results** for the frontend to display as a compliance report.

### The Four Prototype Checks

The course prototype implements exactly four compliance checks, each demonstrating different aspects of IFC data access:

| Check | What It Queries | Key Challenge |
|---|---|---|
| Minimum room area | IfcSpace elements, reads floor area property | Vendor problem -- area stored in different property sets |
| Wall thickness | IfcWall elements, reads thickness property | Type vs. occurrence -- thickness may be on the wall type, not the wall itself |
| Door width | IfcDoor elements, reads width property | Unit handling -- width might be in meters or millimeters |
| Window per space | IfcSpace + relationship chain to IfcWindow | Relationship traversal -- must follow containment, void, fill, and boundary relationships |

---

## 13. From Revit to IFC -- Bridging What You Know

If you have used Revit or ArchiCAD, you already understand most of what IFC describes. The concepts map directly.

### Concept Mapping

| What You Know in Revit | What It Becomes in IFC |
|---|---|
| Levels in the Project Browser | IfcBuildingStorey entities |
| Rooms (with area, name, number) | IfcSpace entities with property sets |
| Wall types and wall instances | IfcWallType (type) and IfcWall (occurrence) |
| Family types and family instances | Type entities and occurrence entities |
| Instance properties and type properties | Properties on the occurrence vs. properties on the type |
| The Properties palette | Property sets (Psets) attached to each element |
| Schedule/Quantities | Qto_ property sets containing measured values |

### The Key Difference

In Revit, you click on a wall and read its properties in a panel. With IFC and Python, you write a few lines of code that read those same properties -- but for every wall in the entire building at once, checking each one against a rule automatically. That is the shift from manual inspection to automated compliance checking.

---

## Summary: The Mental Model

An IFC file is a structured, text-based description of a building. It contains:

- **Entities** -- the building elements (walls, doors, windows, rooms, etc.)
- **A spatial hierarchy** -- how elements are organized (project, site, building, storey, space)
- **Property sets** -- the detailed data attached to each element (dimensions, materials, ratings)
- **Relationships** -- explicit connections between elements (containment, voids, fills, boundaries)

The main challenge is the **vendor problem**: different software puts the same data in different places. The solution is **fallback chains** that check multiple locations.

The tool for reading IFC files in Python is **ifcopenshell**. The dataset for practicing is **IFC-Bench** (21 projects, 37 files, 1,027 question-answer pairs).

Every compliance check follows the same pattern: open the file, query elements, read properties with fallbacks, compare against thresholds, and produce pass/fail/N/A results.
