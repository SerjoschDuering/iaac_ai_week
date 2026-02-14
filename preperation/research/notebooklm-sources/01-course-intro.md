# Course Introduction: The Startup Simulation

## Welcome -- What This Week Is About

This is a one-week intensive course at IAAC Barcelona. Around 29 students will spend four working days building a real software product together, followed by final presentations on Friday.

### The Basics at a Glance

| Detail | Info |
|--------|------|
| Location | IAAC, Barcelona |
| Duration | 5 days (4 building days + 1 presentation day) |
| Students | ~29 total |
| Daily schedule | ~6 hours, split into 2 blocks of ~3 hours each |
| Theme | Using AI to build software for the architecture industry |

### What Makes This Different

This is not a lecture series. There are no exams. There is no homework you hand in and forget about. Instead, you will build a working product as a team -- a real piece of software that solves a real problem in the architecture industry. By Friday, it needs to work well enough to present to a panel of reviewers.

The daily rhythm follows a consistent pattern:

1. **Morning all-hands** -- the whole group gathers briefly to share progress and plans
2. **Sprint block 1** -- focused building time (~3 hours)
3. **Captain standup** -- team leads sync up with each other
4. **Sprint block 2** -- more focused building time (~3 hours)
5. **Board meeting / demo** -- end-of-day presentations to the "client"

This rhythm keeps the energy high, the feedback constant, and the momentum going.


---

## The Startup Simulation

### You Are a Company

From the moment the week begins, the class operates as a startup company. On Day 1, students pick a company name. This is not just a fun gimmick -- the entire course is structured around this idea. You have roles, responsibilities, deadlines, and a demanding client.

### The Contract

Your startup has just landed its first contract. A Spanish real estate developer wants an automated platform that checks digital building models against construction regulations. They want to upload a building file, press a button, and get back a clear report showing what passes and what fails. Your job is to build that platform in four days.

### Company Roles

Everyone in the class has a defined role, just like in a real company.

| Role | Who fills it | What they do |
|------|-------------|--------------|
| CEO / Board | The instructor | Sets deadlines, drops new requirements mid-week, plays the role of an impatient client |
| Tech Leads (Captains) | 7 experienced students | Own their team's delivery, attend cross-team standups, make technical decisions |
| Engineers | ~22 remaining students | Build features within their assigned team |

The **7 Captains** are students who already have experience with coding or AI-assisted development. They act like senior engineers at a real company: they do not do all the work themselves, but they unblock their teammates, review work, and help the team stay on track.

### Board Meetings

At the end of each day, the "board" (the instructor playing the client) watches a demo of what teams have built. Sometimes they are impressed. Sometimes they say, "Great work, but the client also wants this new feature by tomorrow." These board meetings drive the course forward organically. New requirements appear, and the company has to adapt -- just like a real startup.


---

## No Prior Coding Required (But You Will Learn)

### The Honest Truth

You do not need to know how to code before this week starts. Not a single line. The course is designed around AI coding assistants -- tools that can write code when you describe what you want in plain English.

However, you **will** learn to:

- Read Python code and understand what it does
- Debug problems when something does not work as expected
- Describe what you want clearly enough that an AI assistant can build it
- Test your code against known correct answers

These are practical skills that professionals use every day in 2025. You are learning to work the way the industry actually works now.

### The Support Structure

You are not alone in this process:

- **Your Captain** is your first point of contact when you are stuck
- **Your AI coding assistant** can write code from plain English descriptions
- **The prototype** gives you working examples to learn from
- **The IFC-Bench dataset** lets you verify your code produces correct answers

### AI Coding Tools You Can Use

Students are free to use any AI coding assistant they prefer. Common options include:

- **Claude Code** -- Anthropic's command-line coding assistant
- **Cursor** -- an AI-powered code editor
- **Windsurf** -- another AI-powered code editor
- **GitHub Copilot** -- AI code suggestions inside popular editors
- **Codex** -- OpenAI's coding assistant

The AI writes code fast, but you still need to understand what it wrote, test it, and verify it does the right thing. The AI is a tool, not a replacement for your thinking.


---

## What Is IFC?

### The Simple Explanation

IFC stands for **Industry Foundation Classes**. You can forget the full name immediately. What matters is what it does.

An IFC file is a **digital description of an entire building**. Not a pretty picture. Not a rendering. It is a structured, computer-readable file that contains every detail about a building's elements:

- Every wall, with its thickness and material
- Every door, with its width and height
- Every room, with its area and name
- Every window, with its position and dimensions
- Every floor, every staircase, every column

Think of it this way: if a blueprint is a photograph of a building, an IFC file is more like the building's DNA -- every measurement and relationship encoded in a format that software can read and analyze.

### Why IFC Matters

IFC is an **open standard**. That means no single company owns it. It works across all major architecture software:

| Software | Can export to IFC? |
|----------|-------------------|
| Autodesk Revit | Yes |
| ArchiCAD | Yes |
| Tekla Structures | Yes |
| Many others | Yes |

When you export a building model from any of these programs to IFC, all the building data comes with it. This makes IFC the common language that different software tools can share.


---

## What Is Compliance Checking?

### The Problem

Before any building gets constructed, inspectors review the design to make sure it follows the rules. These rules cover things like minimum room sizes, door widths for accessibility, wall thicknesses for safety, and much more.

Traditionally, a human inspector checks these things by hand -- measuring dimensions on drawings, cross-referencing against regulation books, writing reports. This is slow, tedious, and easy to get wrong.

### The Solution

Automated compliance checking means a computer reads the IFC file and checks the rules automatically. Instead of a person measuring every door width by hand, software scans the entire building in seconds and produces a clear report.

### Examples of Automated Checks

Here are the four checks that come built into your starting prototype:

| Check | Rule | What it looks for |
|-------|------|-------------------|
| Minimum room area | Every room must be at least 9 m² | Flags any room smaller than 9 square meters |
| Minimum wall thickness | Every wall must be at least 100 mm thick | Flags any wall thinner than 100 millimeters |
| Minimum door width | Every door must be at least 800 mm wide | Flags any door narrower than 800 millimeters (accessibility requirement) |
| Window per room | Every room must have at least one window | Flags any room that has no window at all |

These are simple examples, but the same approach scales to much more complex regulations.


---

## The Prototype: Your Day 1 Starting Point

### What You Get on Day 1

You will not start from an empty screen. There is already a working application waiting for you. This is your prototype -- the foundation you will build on all week.

### What the Prototype Includes

- **Built with Python + Gradio** -- Python is the programming language; Gradio is a tool that makes it easy to create simple web interfaces without much code
- **4 working compliance checks** -- the room area, wall thickness, door width, and window-per-room checks described above
- **A 3D viewer** -- you can see the building model right in the browser; elements that fail a check turn red, elements that pass turn gray
- **Upload and check** -- you upload an IFC file, click "Run Checks," and see results instantly

### Your First Exercise

On Day 1, your first task is straightforward:

1. Run the prototype yourself
2. Understand how the existing checks work
3. Write 1-2 new check functions following the same pattern

This is not as hard as it sounds. The existing checks serve as templates. If you can describe a new rule in a sentence -- like "every corridor must be at least 1.2 meters wide" -- your AI assistant can help you turn that sentence into working code that follows the same pattern as the existing checks.


---

## The IFC-Bench Dataset

### What It Is

IFC-Bench is a collection of real building projects specifically designed for testing and practice. Think of it as a library of practice problems combined with a set of test buildings.

### What It Contains

| Component | Details |
|-----------|---------|
| Building projects | 21 real projects |
| IFC files | 37 files total |
| Question-answer pairs | 1,027 verified Q&A pairs |
| Difficulty levels | 4 levels (explained below) |

### The Four Difficulty Levels

1. **Simple lookups** -- straightforward questions like "How many doors are in this building?"
2. **Calculations** -- questions that require math, like "What is the total floor area of the second level?"
3. **Spatial reasoning** -- questions about how elements relate to each other, like "Which rooms are adjacent to the staircase?"
4. **Handling missing data** -- questions where the IFC file is incomplete and your code needs to handle that gracefully

### Why It Matters

The dataset serves two purposes:

- **Practice material** -- you can test your code against questions with known correct answers, like a textbook with answers in the back
- **Test buildings** -- the IFC files themselves are real building models you can run your compliance checks against

If your compliance check says a building has 5 doors narrower than 800 mm, and the verified answer says 5, you know your code works. If your code says 3, you know something is wrong and you can debug it.

The dataset is hosted on Hugging Face (a platform for sharing AI datasets and models) at: `https://huggingface.co/datasets/sylvainHellin/ifc-bench`


---

## How the Week Evolves

### The Day-by-Day Arc

| Day | Theme | What Happens |
|-----|-------|--------------|
| **Day 1** | "Make it work" | Learn IFC basics, explore the prototype, write your first compliance checks |
| **Day 2** | "Make it talk" | Add AI-powered checks, wrap your scripts as callable tools (small building blocks that other software can use) |
| **Day 3** | "Make it smart" | Teams specialize (e.g., a frontend team forms), build AI agents (programs that can decide which checks to run and when) |
| **Day 4** | "Make it real" | Integrate everything, deploy to the cloud (make it accessible online), polish the product |
| **Day 5** | Presentations | Final demos to "investors" / jury panel |

### The Pivot Point: Day 3

Days 1 and 2 are egalitarian -- every team does the same kind of work, writing compliance checks, learning the tools, building confidence. Everyone starts on equal footing.

Then Day 3 changes everything. The "board meeting" at the end of Day 2 introduces new requirements. The client wants more: a proper web interface, a database to store results, an API (a set of connection points that let different software systems talk to each other), support for multiple projects at once.

Suddenly, the company cannot have everyone doing the same thing anymore. Teams reorganize and specialize:

- Some people focus on the **frontend** (what users see on screen)
- Some people focus on the **backend** (the behind-the-scenes logic and data storage)
- Some people continue deepening the **compliance checks** themselves
- Some people work on **AI agents** that orchestrate the whole system

This mirrors exactly how real startups work. Early on, everyone is a generalist doing a bit of everything. As the product matures and requirements grow, people specialize. The company reorganizes around new needs.


---

## The Shared Result Schema: The Contract Between Teams

### Why It Exists

When seven different teams are all writing compliance checks, there is one critical question: how do all those checks produce results that the rest of the system can understand?

The answer is the **shared result schema** -- a fixed format that every single check must follow when reporting its results. Think of it as a contract between teams. No matter who wrote the check, no matter how simple or complex it is, the output always looks the same.

### The Format

Every check result contains these fields:

| Field | What it is | Example |
|-------|-----------|---------|
| `element_id` | A unique identifier for the building element being checked | `"3x4F..."` |
| `element_type` | What kind of building element it is | `"IfcDoor"` |
| `element_name` | A human-readable name | `"Door #42"` |
| `rule` | Which check was run | `"Door Width"` |
| `requirement` | What the regulation demands | `">= 800 mm"` |
| `actual` | What was actually found in the model | `"700 mm"` |
| `passed` | Did the element pass the check? | `true`, `false`, or `null` (if data is missing) |

### Why This Matters

This schema is locked on Day 1, before any team starts building. That way:

- The **frontend team** knows exactly what data format to expect and can build the interface accordingly
- The **compliance checking teams** know exactly what their code needs to output
- **New checks** written on Day 4 work with the same interface that was built on Day 2
- **Everything plugs together** without anyone having to rewrite or translate anything

If the schema is the glue that holds the platform together, respecting it is not optional. It is the most important engineering discipline the startup will practice.


---

## AGENTS.md: The Company Handbook

### What It Is

Every real company has engineering standards -- documents that say things like "this is how we name files," "this is how we structure code," and "this is the process for submitting work for review." At your startup, all of these standards live in a single file called **AGENTS.md**.

This file sits at the root of your code repository (the shared folder where all the code lives). It is the company handbook.

### What It Contains

- Naming conventions (how to name files, functions, and variables)
- The shared result schema (described above)
- Coding standards and patterns to follow
- Rules that all teams must respect

### The Special Power of AGENTS.md

Here is what makes AGENTS.md different from a normal handbook: **your AI coding assistant reads it automatically**.

When you ask your AI assistant to write a new compliance check, the assistant reads AGENTS.md first. It learns the company's standards, the expected output format, the naming conventions, and the coding patterns everyone else is using. This means that even if 29 different people are writing code in 29 different corners of the room, the code all follows the same patterns and conventions.

### How It Stays Up to Date

1. When the Captains agree on a new standard, it gets added to AGENTS.md
2. Everyone pulls the update from the shared repository
3. Every AI assistant immediately picks up the new rules
4. All new code automatically follows the updated standards

This solves one of the biggest problems in group projects: inconsistency. Without a shared handbook, five people writing five different things in five different styles means someone has to spend hours stitching it all together at the end. With AGENTS.md, consistency is baked into the process from the start, enforced not just by human reviewers but by the AI assistants themselves.


---

## Why This Matters Beyond the Course

### The Industry Is Changing

The construction and architecture industry is going through a digital transformation. Building Information Modeling (BIM) -- the broader category that IFC files belong to -- is becoming mandatory in more and more countries. Automated compliance checking is actively being developed by companies and governments worldwide. This is not a futuristic concept. It is happening now.

### Skills You Will Build This Week

| Skill | Why it matters |
|-------|---------------|
| Working with IFC / digital building models | BIM is becoming the standard in architecture worldwide |
| Writing and understanding automated checks | Compliance automation is a growing field with real demand |
| Using AI coding assistants effectively | This is how professional software development works in 2025 |
| Reading and debugging code | Even non-programmers increasingly need to understand what code does |
| Collaborating in cross-functional teams | Every technology project involves people with different specializations working together |
| Working under startup-style pressure | Deadlines, pivots, and teamwork under constraint are universal professional skills |

### The Bigger Picture

You are not just building a course project. You are practicing the exact workflow that modern software teams use: define a problem, break it into pieces, assign teams, agree on standards, build in parallel, integrate, test, and ship. The fact that you are doing it with AI assistance and building models makes it directly relevant to where the architecture profession is heading.

The course is designed to be challenging but not overwhelming, practical but not shallow. By Friday, you will have built something real, learned skills you did not have on Monday, and experienced what it feels like to ship a product as a team. That experience -- the rhythm of building, the pressure of deadlines, the satisfaction of seeing your work come together -- is something no lecture can replicate.
