# Software Architecture Patterns & The Course Tech Stack

A reference guide for architecture and design students. No programming experience assumed.

---

## 1. What Is Software Architecture?

Software architecture is the organizational plan for a digital system -- just like a floor plan is the organizational plan for a building.

When an architect draws a floor plan, they decide:
- Which rooms exist
- What each room is for
- How rooms connect to each other
- Where people enter and exit

A software architect makes the same decisions, but for code:
- Which components exist (a database, a user interface, a file storage system)
- What each component is responsible for
- How components communicate with each other
- Where data enters and leaves the system

### Why It Matters

| Good Architecture | Bad Architecture |
|---|---|
| Easy to add new features | Every change breaks something else |
| Teams can work independently on separate parts | Everyone is stepping on each other's toes |
| When something breaks, you know where to look | A bug could be hiding anywhere |
| You can swap out one piece without affecting others | Everything is tangled together |

**Key insight:** Architecture is decided *before* building begins. The plan comes first, just like in real construction.

---

## 2. The Client-Server Model

Almost all modern web applications follow a pattern called the **client-server model**. The simplest way to understand it is the restaurant analogy.

### The Restaurant Analogy

| Restaurant | Software Term | What It Does |
|---|---|---|
| Dining room (what customers see) | **Frontend** | The user interface -- buttons, 3D viewer, forms, dashboards |
| Kitchen (hidden from customers) | **Server / Backend** | Where the actual work happens -- running checks, processing data, crunching numbers |
| Waiter (carries orders back and forth) | **API** | The messenger between frontend and backend |
| Menu (what you can order) | **API Documentation** | Lists what requests you can make and what responses you'll get |
| Order slip (structured format) | **Request / Response** | Data sent in a specific, agreed-upon format |

### How It Works

1. The **customer** (user) sits in the **dining room** (frontend) and looks at the **menu** (API documentation)
2. They tell the **waiter** (API) what they want
3. The waiter carries the **order slip** (request) to the **kitchen** (backend)
4. The kitchen prepares the food (processes the data)
5. The waiter brings the **plate** (response) back to the customer

The customer never enters the kitchen. The cook never enters the dining room. They communicate only through the waiter and the order slip. This separation is intentional and powerful.

---

## 3. What Is an API?

**API** stands for **Application Programming Interface**. It is a set of rules for how one piece of software talks to another piece of software.

### The Government Office Analogy

Think of a large government office building with many service counters:

- **Counter 1:** Passport applications
- **Counter 2:** Tax filings
- **Counter 3:** Building permits

Each counter:
- Has a **specific purpose** (handles one type of request)
- Expects **specific paperwork** (you bring the right form filled out correctly)
- Gives back a **specific response** (your processed application, a receipt, or a rejection notice)

You would not hand your tax return to the passport counter -- they would not know what to do with it. And you would not shout your request from across the lobby -- you walk up to the right counter with the right form.

### APIs Work the Same Way

In our compliance checking system:
- One API "counter" (called an **endpoint**) handles: "Run checks on this building file"
- Another endpoint handles: "Show me the latest check results"
- Another endpoint handles: "Upload a new IFC file"

Each endpoint has a specific address (URL), expects a specific type of input, and returns a specific type of output.

**Example:** You send an IFC file to the address `/api/checks/run`. The system processes it and sends back a list of pass/fail results. That address is the endpoint. The IFC file is the input. The results list is the output.

---

## 4. What Is REST?

**REST** is a set of conventions for how to structure API requests. Think of it as the agreed-upon format for filling out those government forms. Everyone follows the same rules so that the system works smoothly.

### HTTP Methods (The "Verbs" of the Web)

REST uses standard actions called HTTP methods. There are only a few you need to know:

| Method | Plain English | Example in Our System |
|---|---|---|
| **GET** | "Show me this" | Get the list of check results |
| **POST** | "Here's something new, process it" | Upload an IFC file and run checks on it |
| **PUT** | "Update this existing thing" | Change a check rule's threshold from 9m2 to 12m2 |
| **DELETE** | "Remove this" | Delete old check results you no longer need |

### Anatomy of a REST Request

Every REST request has up to three parts:

1. **The method** -- What action you want (GET, POST, PUT, DELETE)
2. **The endpoint URL** -- Where you're sending the request (e.g., `/api/checks/run`)
3. **The body** (optional) -- The data you're sending along (e.g., the IFC file itself)

The server receives this request, does its work, and sends back a **response** containing the results (or an error message if something went wrong).

---

## 5. The Course Tech Stack

### Important Distinction

There are two states of the system you need to keep separate in your mind:

- **What exists NOW** = the prototype you start with on Day 1
- **What you will BUILD** = the full platform you work toward by Day 4

The specific technologies listed below are **examples** of what a system like this typically uses. You may end up choosing different tools during the course -- the important thing is understanding **what role each component plays**, not memorizing specific product names.

### What Exists Now (The Prototype -- Day 1 Starting Point)

The prototype is a single Gradio application written in Python. Here is what it includes:

| Feature | Description |
|---|---|
| **4 compliance checks** | Room area, wall thickness, door width, window-per-room |
| **File upload** | Drag and drop an IFC building model file |
| **Run Checks button** | Triggers all four checks on the uploaded file |
| **Load Demo button** | Loads a sample building for quick testing |
| **Results panel** | Shows pass/fail counts and a scrollable list of individual results |
| **3D viewer** | Displays the building model (red = failed elements, gray = passed) |

**What the prototype does NOT have:**
- No database (results disappear when you close the app)
- No cloud deployment (only works on your laptop)
- No login system (anyone with your laptop can use it)
- No separate API (checks only run inside the Gradio app)
- No advanced 3D features (no clicking on elements, no floor filtering, no measurements)

**Under the hood:**
- **IfcOpenShell** reads and interprets the IFC building data
- **Trimesh** converts IFC geometry into GLB format for the 3D viewer
- IFC property sets vary by software vendor (Revit, ArchiCAD, Allplan store data differently), so the prototype uses fallback chains -- it tries one property name, then another, then another until it finds the data

### What You Will Build Toward (The Full Platform -- By Day 4)

A production system like this typically needs the following types of components. Here are examples of what each might look like:

| Role | Example Tool | Analogy | What It Does |
|---|---|---|---|
| **Prototyping** | Python + Gradio | Your workshop / lab | Where you build and test checks quickly. Already exists. |
| **Web API** | e.g. FastAPI | The service counter | Exposes your Python checks so other systems can call them over the internet. |
| **User Interface** | e.g. JavaScript frontend | The showroom | 3D building viewer + dashboard with results. |
| **Data Storage** | e.g. PostgreSQL, SQLite, or a cloud database | Filing cabinet | Stores all check results so the frontend can display them. |
| **Large File Storage** | e.g. S3, Cloudflare R2, or shared drive | Warehouse | Stores IFC building models (too large for a regular database). |
| **Authentication** | e.g. a login service or auth library | Security desk | Controls who can access the system. |

The exact tools will be decided during the course. What matters is understanding the **roles** -- every production system needs these building blocks, regardless of which specific products fill them.

---

## 6. How Data Flows Through the System

Here is an **example** of how a compliance check might flow through a full system, step by step. The specific tools may vary, but the pattern is always similar.

### Step-by-Step Flow (Example)

| Step | What Happens | Where It Happens |
|---|---|---|
| 1 | User opens the website in their browser | **Frontend** |
| 2 | User uploads an IFC building model file | **Frontend** |
| 3 | The file gets stored in large-file storage (the warehouse) | **File Storage** |
| 4 | Frontend sends a request to the API: "Run checks on this file" | **Frontend -> API** |
| 5 | The API server receives the request and calls the Python check scripts | **Backend API** |
| 6 | Check scripts use IfcOpenShell to read the IFC file and run the rules | **Python Scripts** |
| 7 | Check results are produced in the shared format (element ID, rule, passed/failed, measurements) | **Python Scripts** |
| 8 | Results get saved to the database (the filing cabinet) | **Database** |
| 9 | The API sends the results back to the frontend | **API -> Frontend** |
| 10 | Frontend reads the results and updates the dashboard | **Frontend** |
| 11 | The 3D viewer highlights failing elements in red, passing elements in gray | **Frontend (3D Viewer)** |

### The Standardized Result Format

Every check result -- whether it is about a door, a wall, a room, or a window -- follows the same structure:

| Field | What It Contains | Example |
|---|---|---|
| `element_id` | Unique identifier for the building element | `2O2Fr$t4X7Z8f...` |
| `element_type` | What kind of IFC element it is | `IfcDoor` |
| `element_name` | Human-readable name | `Door 42` |
| `rule` | Which rule was checked | `Door Width` |
| `requirement` | What the threshold is | `>= 800 mm` |
| `actual_value` | What was actually measured | `700 mm` |
| `passed` | Did it pass or fail? | `false` (failed) |

This shared format is called a **schema** or **contract**. It is the agreement between all parts of the system about what the data looks like. The backend produces results in this format. The frontend expects results in this format. As long as both sides follow the contract, they can be built independently by different teams.

---

## 7. Why Separate Services? (Modularity)

### The Core Principle

Each component does **one thing** and does it well. This is called **separation of concerns** or **modularity**.

### Why This Matters for Teamwork

During the course, different teams will work on different parts of the system:

| Team | Works On | Does NOT Need to Understand |
|---|---|---|
| Check writers | Python compliance scripts | How the 3D viewer renders models |
| Frontend team | User interface and 3D viewer | How IfcOpenShell parses IFC files |
| Infrastructure team | Database, deployment, file storage | The details of any individual check |

### The Company Analogy

Think of departments in a company:
- **Accounting** does not need to know how **Marketing** designs advertisements
- **Marketing** does not need to understand how **Accounting** files taxes
- Each department has its own tools, expertise, and processes
- They communicate through **well-defined channels** (reports, memos, meetings)

If Marketing rebrands the company's look, they do not need to modify the accounting software. The departments are independent.

### Benefits of Modularity

| Benefit | What It Means |
|---|---|
| **Independent work** | The frontend team can redesign the dashboard without touching the Python checks |
| **Easier debugging** | If the 3D viewer is broken, you know it is a frontend problem -- no need to dig through check scripts |
| **Swappable parts** | You can replace the 3D viewer with a better one without changing anything in the backend |
| **Scalability** | Add new checks without redesigning the frontend |
| **The contract holds it together** | The shared result schema is the "handshake" between all parts |

---

## 8. The Gradio Prototype (What You Start With)

### What Gradio Is

**Gradio** is a Python library (a pre-built toolkit) that creates simple web interfaces from Python code with very little effort. You write a function, Gradio gives you buttons and input fields automatically.

### Prototype Features

| Feature | Description |
|---|---|
| **File upload** | Drag-and-drop area for IFC files |
| **Run Checks button** | Triggers all four compliance checks |
| **Load Demo button** | Loads a built-in sample building for quick testing |
| **Results summary** | Shows total pass/fail counts at a glance |
| **Results list** | Scrollable list of every individual check result |
| **3D viewer** | Interactive 3D model of the building with color-coded results |

### What the Gradio 3D Viewer Can Do

- Rotate the building model
- Zoom in and out
- Show failing elements in red, passing elements in gray

### What the Gradio 3D Viewer Cannot Do

- Click on individual elements to see their details
- Filter by floor or building level
- Use clipping planes to cut through the model
- Take measurements
- Show rich BIM (Building Information Modeling) data

These limitations are exactly why the **frontend team's job** (starting around Day 3) is to build a proper, full-featured viewer to **replace** the basic Gradio one.

### Why Start with Gradio?

Gradio is perfect for prototyping because:
- You can go from Python function to working interface in minutes
- No web development knowledge required
- Great for testing and iterating on check logic
- The feedback loop is fast: change code, click button, see result

---

## 9. Deployment (Getting Your App Online)

### Local vs. Cloud

| | Running Locally | Deployed to the Cloud |
|---|---|---|
| **Who can use it** | Only you, on your laptop | Anyone with the web address |
| **Analogy** | Cooking dinner at home | Opening a restaurant |
| **Always available?** | No -- only when your laptop is on | Yes -- the server runs 24/7 |
| **Installation needed?** | Yes -- everything must be set up on your machine | No -- users just open a web browser |

### What "The Cloud" Actually Means

"The cloud" is not a mysterious, floating thing. It is just **computers in a data center** that are:
- Always powered on
- Always connected to the internet
- Always ready to accept requests

When you "deploy to the cloud," you are copying your code to one of these always-on computers and giving it a web address (URL) so others can reach it.

### Deployment in This Course

- **Days 1-3:** You build and test everything locally on your laptop (the workshop phase)
- **Day 4:** The goal is to have the full platform deployed and accessible online via a URL
- **The moment of deployment** is when your tool goes from being a private experiment to a real, accessible product

---

## 10. How the Pieces Connect (Example Architecture Diagram)

Here is an example of how all the components might relate in a full system. The specific tools may differ, but the roles and connections follow this general pattern:

```
USER (Browser)
    |
    v
[FRONTEND]  <-- The showroom (what users see)
    |
    v
[AUTH]  <-- Security desk (checks who you are)
    |
    v
[API SERVER]  <-- Service counter (receives requests, returns results)
    |         |
    v         v
[DATABASE]  [FILE STORAGE]
(results)   (IFC files)
    ^
    |
[PYTHON CHECK SCRIPTS]  <-- The actual compliance logic
    |
    v
[IfcOpenShell]  <-- Reads and interprets IFC building data
```

**Remember:** In the prototype (Day 1), only the bottom portion exists -- Python check scripts running inside a Gradio interface. Everything above the scripts is what you build during the week.

---

## 11. Key Concepts Glossary

| Term | Plain English Definition |
|---|---|
| **Server** | A computer that is always running, always connected, waiting for requests |
| **Client** | The user's browser or app that sends requests to a server |
| **API** | A set of connection points where one piece of software talks to another |
| **Endpoint** | One specific address that handles one type of request (e.g., `/api/checks/run`) |
| **REST** | A widely used convention for how to format API requests and responses |
| **HTTP** | The protocol (set of communication rules) that web browsers and servers use to talk |
| **JSON** | A text format for structured data that looks like `{"key": "value"}` -- the universal data language of the web |
| **Deploy** | Put your code on a server so other people can access it via a URL |
| **Frontend** | What users see and interact with -- the website, the buttons, the 3D viewer |
| **Backend** | The behind-the-scenes logic: data processing, storage, and computation |
| **Database** | Where structured data (like check results) is stored and retrieved |
| **S3** | A storage service designed for large files (like IFC building models) |
| **Framework** | A pre-built toolkit that provides structure and shortcuts for building software (Gradio, FastAPI are frameworks) |
| **Schema / Contract** | An agreed-upon format for how data should be structured so different systems can understand each other |
| **IFC** | Industry Foundation Classes -- the standard file format for building information models |
| **IfcOpenShell** | A Python library (toolkit) that reads and interprets IFC files |
| **Library** | A collection of pre-written code you can use in your own program (like a reference book you pull off the shelf) |
| **Property Set** | A group of properties (name, value pairs) attached to a building element in an IFC file -- varies by software vendor |
| **Fallback Chain** | A strategy where the code tries multiple ways to find a piece of data, moving to the next if the first fails |
| **GLB** | A 3D file format that web browsers can display -- the prototype converts IFC geometry into GLB for the viewer |

---

## 12. Quick Reference: Prototype vs. Full Platform

| Aspect | Prototype (Day 1) | Full Platform (Day 4 Target) |
|---|---|---|
| **Interface** | Gradio (Python-generated) | Custom frontend (e.g. JavaScript-based) |
| **3D Viewer** | Basic Gradio viewer (rotate/zoom only) | Full BIM viewer (click elements, filter floors, clipping) |
| **Where checks run** | Locally inside Gradio | On a server via API endpoints |
| **Data storage** | None -- results vanish when you close the app | A database stores all results permanently |
| **File storage** | Local hard drive | Cloud file storage (e.g. S3, R2) |
| **Access** | Only on your laptop | Anyone with the URL |
| **Security** | None | Login / authentication system |
| **Who can use it** | Just you | Your whole team and beyond |
