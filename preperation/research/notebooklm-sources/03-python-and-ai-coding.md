# Python and AI-Assisted Coding Fundamentals

A reference guide for architecture and design students with zero programming experience. Every technical term is explained in plain English. This document covers the core building blocks of Python, the tools you will use to write code, and how AI coding assistants change the learning experience entirely.

---

## 1. What Is Programming?

A program is a set of step-by-step instructions for a computer. Nothing more, nothing less.

Think of it like writing a recipe:

| Recipe concept | Programming equivalent |
|---------------|----------------------|
| Ingredients | Inputs (the data you start with) |
| Steps ("chop onions, heat pan...") | Code (the instructions) |
| Finished dish | Output (the result) |

The critical thing to understand is that a computer follows instructions **exactly and literally**. It will never guess what you meant. If you tell it to "bake for 25 hours" instead of "25 minutes," it will dutifully do exactly that. It will not use common sense. It will not improvise. It does precisely what you write, nothing more and nothing less.

The good news: unlike a real kitchen, you can always undo your mistakes and try again.

**Python** is the programming language you will use in this course. It is one of the most popular languages in the world, widely used in engineering, data science, and AI. It was designed to be readable, which means Python code often looks close to plain English compared to other languages.

---

## 2. What Is an IDE?

IDE stands for **Integrated Development Environment**. It is your workspace for writing code, the same way an architect's drafting desk has all tools organized in one place.

An IDE combines several tools into a single window:

| IDE Feature | What it does | Analogy |
|------------|-------------|---------|
| Text editor | Where you write your code | The drafting paper |
| File browser | Navigate and organize your project files | The drawer organizer |
| Terminal | Run commands and talk to your computer via text | The intercom to your computer |
| Debugger | Step through code line by line to find problems | The magnifying glass |

### Common IDEs

- **VS Code** -- Free, made by Microsoft, extremely popular, huge library of extensions.
- **Cursor** -- Built on VS Code but with especially strong AI assistance built in. Great for beginners.

During this course you can use whichever IDE you prefer. They all serve the same fundamental purpose: an organized workspace where everything you need lives in one window.

---

## 3. Core Python Concepts

### Variables

A variable is a **labeled container** that holds a value. You give it a name and put something inside.

```python
door_width = 900       # a box labeled "door_width" containing 900
room_name = "Kitchen"  # a box labeled "room_name" containing "Kitchen"
```

You can change what is inside at any time:

```python
door_width = 850       # same label, new value
```

**Naming tip:** Use descriptive names. `room_area` is clear. `x` tells you nothing. Good variable names make code readable without extra explanation.

### Data Types

Every value in Python has a **type** -- what kind of thing it is. This matters because you cannot do math on a piece of text, and you cannot spell-check a number.

| Type | What it holds | Example | When you use it |
|------|-------------|---------|-----------------|
| Integer (`int`) | Whole numbers | `42`, `800`, `-3` | Counting things, element IDs |
| Float (`float`) | Decimal numbers | `3.14`, `9.5`, `0.8` | Measurements, areas, percentages |
| String (`str`) | Text | `"Door #42"`, `"IfcWall"` | Names, labels, descriptions |
| Boolean (`bool`) | True or False | `True`, `False` | Pass/fail results, yes/no questions |
| None | "Nothing" / "No data" | `None` | When data is missing or unavailable |

### Lists

A list is an **ordered collection** of items, like a shopping list.

```python
rooms = ["Kitchen", "Bedroom", "Bathroom"]
```

Key things to know about lists:

- Items are numbered starting from **0**, not 1. So `rooms[0]` is "Kitchen" and `rooms[1]` is "Bedroom."
- You can add items, remove items, and loop through them one by one.
- The order matters. Lists remember the sequence you put things in.

### Dictionaries

A dictionary is a collection of **key-value pairs**. Think of it like a lookup table or an address book: you look something up by name, not by position.

```python
door = {
    "name": "Door #42",
    "width": 800,
    "passed": False
}
```

You look up values by their key:

```python
door["width"]   # gives you 800
door["name"]    # gives you "Door #42"
```

Dictionaries are everywhere in programming. The **shared result format** you will use in this course is a dictionary. Every compliance check result is stored as a dictionary with specific keys like `element_id`, `rule`, `requirement`, `actual`, and `passed`.

---

## 4. Functions

A function is a **reusable block of code** with a name. It takes inputs (called **parameters**), does something with them, and produces an output (called a **return value**).

Think of it like a recipe card:

| Recipe card part | Function equivalent |
|-----------------|-------------------|
| Name at the top | Function name (e.g., `check_door_width`) |
| List of ingredients | Parameters (e.g., `model`, `min_width`) |
| The cooking steps | The code inside the function |
| The finished dish | The return value (e.g., a list of results) |

**Example from the course:** A function called `check_door_width` takes a building model and a minimum width as inputs. Inside, it goes through every door in the model, measures its width, compares it to the minimum, and returns a list of results telling you which doors passed and which failed.

You write a function **once**, then **call** it as many times as you need -- on different building models, with different minimum widths, without rewriting a single line.

### Default Values

Parameters can have default values. If you do not provide a specific value, the function uses the default automatically.

```python
check_room_area(model, min_area=9.0)
```

- Call `check_room_area(my_model)` and it uses 9.0 as the minimum.
- Call `check_room_area(my_model, min_area=12.0)` and it uses 12.0 instead.

This is like a recipe that says "add salt to taste, about a teaspoon." You get a sensible default, but you are free to adjust.

---

## 5. Importing Libraries

A library (also called a package) is a collection of **pre-written code tools** that someone else built. Instead of building everything from scratch, you "import" what you need. It is like hiring a specialist.

```python
import ifcopenshell   # now you can use ifcopenshell's tools
import trimesh        # now you can use trimesh's tools
```

### Key Libraries in This Course

| Library | What it does | Analogy |
|---------|-------------|---------|
| `ifcopenshell` | Reads and interprets IFC building model files | Your IFC file expert |
| `trimesh` | Handles 3D geometry and mesh operations | Your 3D geometry specialist |
| `gradio` | Creates simple web interfaces for your tools | Your web designer |
| `json` | Reads and writes JSON data files | Your data translator |

The Python ecosystem is a massive talent marketplace. Need to do math? Import `numpy`. Need to handle dates? Import `datetime`. Need to talk to a web service? Import `requests`. Someone has almost certainly already built what you need.

---

## 6. JSON -- The Universal Data Format

JSON stands for **JavaScript Object Notation**. Despite the name, it has nothing to do with JavaScript for our purposes. JSON is simply a text format for structured data that virtually every software system on earth can read and write.

JSON looks almost identical to Python dictionaries:

```json
{
    "element_id": "3x4F...",
    "element_type": "IfcDoor",
    "element_name": "Door #42",
    "rule": "Door Width",
    "requirement": ">= 800 mm",
    "actual": "700 mm",
    "passed": false
}
```

### Where You Will Encounter JSON

- **Check results** -- Every compliance check produces results in JSON format.
- **API requests and responses** -- When your code talks to an AI service or a web service, the data travels as JSON.
- **Configuration files** -- Settings and preferences are often stored as JSON.
- **The shared result schema** -- The standard format every team's check must follow is defined as JSON.

### Python vs. JSON Spelling

One small gotcha: Python and JSON spell a few values differently.

| Concept | Python spelling | JSON spelling |
|---------|----------------|--------------|
| True | `True` | `true` |
| False | `False` | `false` |
| No value | `None` | `null` |

Same meaning, slightly different capitalization. Python's built-in `json` library handles the conversion automatically.

---

## 7. Reading and Writing Files

Programs read data from files and write results back to files. This is one of the most common things code does.

The general pattern:

1. **Open** a file
2. **Read** its contents into your program
3. **Process** the data (run checks, do calculations)
4. **Write** the results to a new file

### File Types You Will Work With

| File type | How you open it | What it contains |
|-----------|----------------|-----------------|
| `.ifc` | `ifcopenshell.open("model.ifc")` | Building model data |
| `.json` | Python's built-in `json` library | Structured data (results, configs) |
| `.py` | Your IDE text editor | Your Python code |

### File Paths

A file path is the **address** of a file on your computer. It tells the program exactly where to find a file.

Example: `/Users/you/project/model.ifc`

If you give the wrong path, you get a `FileNotFoundError`. Always double-check that the path is correct and the file actually exists at that location.

---

## 8. What Is a Terminal / Command Line?

The terminal is a **text-based way to talk to your computer**. Instead of clicking on icons and buttons, you type short commands and press Enter.

It sounds old-fashioned, but it is incredibly powerful and you will use it every day during this course. Your IDE has a terminal built right into it (usually at the bottom of the window).

### Essential Commands

| Command | What it does | Example |
|---------|-------------|---------|
| `cd` (change directory) | Navigate to a folder | `cd my_project` |
| `ls` (list) | Show files in current folder | `ls` |
| `python script.py` | Run a Python script | `python check_doors.py` |
| `pip install` | Install a Python library | `pip install ifcopenshell` |

That is genuinely most of what you need. You navigate to a folder, check what is there, run your scripts, and install tools. Everything else is a bonus.

---

## 9. AI Coding Assistants -- Your Pair Programming Partner

This is where the learning experience has changed dramatically. An AI coding assistant sits next to you and helps you write code. It reads your code, understands what you are trying to do, and suggests solutions -- all in real time.

Imagine having a senior developer sitting right beside you who has read millions of lines of code, understands hundreds of programming languages, and is endlessly patient. That is what these tools offer.

### Available Tools

You can use whichever tool you prefer during this course:

| Tool | What it is |
|------|-----------|
| Claude Code | Anthropic's command-line AI coding assistant |
| Cursor | VS Code-based editor with built-in AI assistance |
| Windsurf | Another AI-powered code editor |
| GitHub Copilot | GitHub's AI assistant that works inside VS Code |
| Codex | OpenAI's coding-focused AI |

### Important Reality Check

AI assistants are incredibly helpful, but they are **not magic**. They can and do make mistakes.

Think of an AI assistant as a very knowledgeable colleague who occasionally misremembers details or suggests an approach that works in theory but not for your specific case. Always:

- **Run the code** and check the output.
- **Verify** that it actually does what you intended.
- **Test** with real data, not just in your head.

The AI handles syntax and boilerplate (the repetitive structural code that every program needs). You bring the domain knowledge and the judgment about what matters.

---

## 10. How to Talk to AI Assistants Effectively

Communicating with an AI coding assistant is a skill worth practicing. The quality of your prompt directly affects the quality of the answer.

### Prompting Best Practices

| Do this | Not this | Why |
|---------|---------|-----|
| "Write a function that checks if IfcDoor width >= 800mm using ifcopenshell" | "Write a check" | Be specific about WHAT to check, HOW, and which tools to use |
| "I got this error: FileNotFoundError on line 12. Here's my code: ..." | "It doesn't work" | Share the actual error message and your code |
| "The function returns None but I expected a list of results" | "Fix it" | Explain what you expected vs. what actually happened |
| "Use the same result format as check_door_width" | "Make it match" | Reference existing patterns by name |

### The Iteration Loop

If the first answer does not work, that is completely normal. The process is:

1. Ask the AI for help.
2. Run the code it gives you.
3. If it fails, copy the **error message** and send it back to the AI.
4. The AI adjusts. Run again.
5. Repeat until it works.

This back-and-forth conversation is how even experienced developers work with AI assistants. It is not a sign that something is wrong.

### AGENTS.md -- Shared Context for AI

Many teams use a special file called `AGENTS.md` that contains shared rules and context about the project: naming conventions, file structures, the result format, common patterns. AI assistants can read this file automatically, so they stay aligned with your team's approach without you repeating yourself every time.

---

## 11. Reading Error Messages

Error messages are the computer telling you **exactly what went wrong**. They are not punishment. They are diagnosis. Learning to read them is one of the most valuable skills you can develop.

### The Golden Rule

Read error messages **from the bottom up**. The very last line is the actual error. Everything above it is the trail of breadcrumbs showing how the program got to that point (called a "stack trace").

### Common Errors and Their Fixes

| Error | What it means | How to fix it |
|-------|-------------|--------------|
| `FileNotFoundError` | The file path is wrong or the file does not exist | Check the path, check spelling, make sure the file is where you think it is |
| `ModuleNotFoundError` | A library is not installed | Run `pip install library_name` in your terminal |
| `TypeError` | You gave the wrong type of data (text where a number was expected, etc.) | Check what the function expects and what you are actually passing |
| `KeyError` | You asked for a dictionary key that does not exist | Check the key name and spelling -- capitalization matters |
| `IndentationError` | Your code spacing is wrong | Fix the indentation. Python uses spaces to understand code structure, so spacing is not optional |

### The Debugging Mindset

Debugging is not about genius. It is about:

1. Reading the error message carefully.
2. Forming a theory about what went wrong.
3. Testing that theory one step at a time.

This is the same process you use when a building design does not meet requirements: identify the problem, form a hypothesis, test a solution.

---

## 12. Type Hints and Pydantic

### Type Hints

Type hints are **annotations** that tell you (and the AI) what type of data a function expects and returns.

```python
def check_door_width(model: str, min_width: float = 800.0) -> list:
```

This line says: "This function takes a `model` (text/string) and a `min_width` (decimal number, default 800.0), and it returns a list."

Type hints are like labels on boxes: "this box contains integers only." They help you, your teammates, and AI assistants understand what the code expects without reading through every line.

### Pydantic -- Strict Data Contracts

If type hints are gentle labels, **Pydantic** is a strict quality inspector.

A Pydantic model says: "This data MUST have exactly these fields, with exactly these types, or I reject it outright."

The shared result schema in this course is essentially a Pydantic model:

| Field | Type | Description |
|-------|------|------------|
| `element_id` | string | The unique ID of the building element |
| `element_type` | string | What kind of element (e.g., "IfcDoor") |
| `element_name` | string | Human-readable name (e.g., "Door #42") |
| `rule` | string | What rule was checked |
| `requirement` | string | What the rule demands (e.g., ">= 800 mm") |
| `actual` | string | What was actually found (e.g., "700 mm") |
| `passed` | boolean or null | Whether it passed, failed, or could not be checked |

If your check tries to return something that does not match this contract -- say, a missing field or a wrong type -- Pydantic catches the mistake immediately, before it causes problems downstream.

### Connection to Structured AI Outputs

When you ask an AI to generate data, you can give it a Pydantic model as a template. The AI then returns data **guaranteed to match** that structure. This means no manual cleanup, no surprise formats. The AI fills in the blanks of a strict form rather than writing freeform text.

---

## 13. A Short Time Travel: How Coding Changed in Just One Year

To understand the moment you are entering, it helps to see how fast things have moved. Here is a brief timeline of what happened in the world of AI-assisted coding between February 2025 and February 2026 -- just twelve months.

### February 2025: The Starting Gun

- Andrej Karpathy (co-founder of OpenAI, former head of AI at Tesla) coined the term **"vibe coding"** in a viral post: "you fully give in to the vibes, embrace exponentials, and forget that the code even exists." The post was viewed 4.5 million times.
- At this point, AI coding tools were mostly **autocomplete** -- they suggested the next line, and you decided whether to accept it. The developer was still typing most of the code.

### Mid-2025: The Agents Arrive

- AI coding tools evolved from autocomplete into **agents** -- tools that can plan, write, test, and fix code across multiple files on their own, while you supervise.
- **Claude Code** (Anthropic) reached general availability in May 2025 -- a terminal-based tool that understands entire codebases and executes through natural language.
- **Cursor** crossed 1 million daily active developers and introduced **Background Agents** that work independently while you focus on something else.
- **GitHub Copilot** launched Agent Mode: you assign a GitHub Issue to Copilot, it writes the code, creates a pull request, and you review.
- **Amazon launched Kiro**, a new IDE where you describe requirements in plain language and the AI generates a full technical plan plus implementation.
- The term "vibe coding" was named **Word of the Year** by Collins English Dictionary.

### The Numbers Tell the Story

| Metric | Early 2025 | Early 2026 |
|--------|-----------|-----------|
| Developers using AI coding tools | ~76% | ~85% |
| Percentage of new code that is AI-generated | ~15-20% | ~41% |
| AI code at top tech companies (Microsoft, Google) | "Some" | 25-30% of all code |
| AI code at Anthropic (maker of Claude) | "A lot" | ~90% of Claude Code's own codebase |
| Non-programmers building software | Experimental | Lovable hit $100M revenue in 8 months -- fastest software company ever |

### Late 2025 -- Early 2026: The Paradigm Shift

- **November 2025**: Anthropic released Claude Opus 4.5, capable of autonomous coding sessions lasting 30+ hours.
- **December 2025**: MCP (Model Context Protocol) -- the standard that lets AI tools connect to external data and services -- was donated to the Linux Foundation, making it a vendor-neutral industry standard now backed by Anthropic, OpenAI, Google, and Microsoft.
- **January 2026**: MIT Technology Review named **"Generative Coding"** one of its 10 Breakthrough Technologies of 2026.
- **January 2026**: Anthropic launched **Cowork**, bringing coding-assistant capabilities to non-developers -- you point it at a folder and describe what you want in plain language.
- **February 5, 2026**: Claude Opus 4.6 launched with **Agent Teams** -- a single orchestrator spawns multiple AI agents working on the same codebase in parallel. This is the model powering the tools you will use this week.
- **February 12, 2026**: OpenAI released GPT-5.3-Codex, the first major AI model running on non-NVIDIA hardware.
- **Today, February 13, 2026**: GPT-4o (the model that dominated 2024) is officially shut down. Replaced by models that are 10-50x more capable.

### Open Source Changed Everything Too

- **January 2025**: Chinese lab DeepSeek released R1, an open-source model matching the best proprietary models -- trained for just $5.6 million (compared to hundreds of millions for competitors). The announcement triggered a $600 billion single-day drop in NVIDIA's market value.
- **2025**: Meta released Llama 4 with a 10-million-token context window. Alibaba released Qwen3-Coder. Mistral (France) released competitive models. AI coding is no longer a US-only story.

### What This Means for You

The field you are entering is one where the most valuable skill is no longer typing syntax. It is:

| Old skill (still useful, but less central) | New skill (what matters most now) |
|-------------------------------------------|----------------------------------|
| Memorizing programming syntax | Clearly describing what you want |
| Typing code quickly | Reviewing and verifying AI-generated code |
| Knowing every library by heart | Knowing which library to ask for |
| Writing everything from scratch | Directing AI agents and assembling results |
| Working alone on a codebase | Orchestrating human + AI teams |

As architecture students, you already have a superpower: you know how to describe complex systems clearly, you understand building regulations, and you can evaluate whether a result makes sense in the real world. That is exactly what AI-assisted coding needs.

---

## 14. Comprehensive Glossary

### Programming Basics

Core concepts you will encounter every day when writing or reading code.

| Term | Plain English |
|------|-------------|
| Variable | A named container that holds a value |
| Function | A reusable block of code with a name, inputs, and an output |
| Parameter | An input that a function accepts |
| Return value | The output a function produces |
| Class | A blueprint for creating objects that bundle data and behavior together |
| Library / Package | Pre-built code tools made by someone else that you can use |
| Import | Bringing a library into your code so you can use it |
| Module | A single Python file that contains code you can import |

### Data and Files

The formats and structures used to store and exchange information.

| Term | Plain English |
|------|-------------|
| JSON | A text format for structured data: `{"key": "value"}` |
| Dictionary | A Python collection of key-value pairs |
| List | A Python ordered collection of items |
| String | A piece of text in code |
| Boolean | A true/false value |
| None / null | Represents "no value" or "missing data" |
| File path | The address of a file on your computer |

### Tools and Environment

The software and systems you use to write, run, and manage code.

| Term | Plain English |
|------|-------------|
| IDE | Your coding workspace (text editor + file browser + terminal in one window) |
| Terminal | Text-based interface for running commands on your computer |
| Git | A version control system that tracks every change to your code |
| Commit | A saved snapshot of your code at a point in time |
| Repository (repo) | A folder tracked by git, containing your project's code and history |
| pip | Python's package installer for adding libraries |

### Web and APIs

How software communicates with other software over the internet.

| Term | Plain English |
|------|-------------|
| API | A set of rules for how software talks to other software |
| Endpoint | A specific address where software listens for requests |
| Server | A computer that is always running, waiting for and responding to requests |
| Request | A message sent to a server asking it to do something |
| Response | The server's answer to a request |
| Deploy | Put your code on a server so others can access it over the internet |

### Code Quality

Practices and tools that help you write correct, reliable code.

| Term | Plain English |
|------|-------------|
| Type hint | An annotation saying what type of data a variable or function expects |
| Pydantic | A library that enforces strict data structure rules |
| Debugging | Finding and fixing errors in your code |
| Syntax | The grammar rules of a programming language |
| Indentation | Spacing at the start of lines (Python uses this to understand code structure) |
| Error / Exception | The computer's way of telling you something went wrong |
| Stack trace | The error report showing the chain of events that led to a crash |

---

## 15. Final Note

Programming is not about memorizing syntax. It is about thinking clearly, breaking big problems into small steps, and being patient enough to read what the computer tells you. You already do all of that when you design a building. Now you are doing it in a new medium -- and you have an AI partner ready to help every step of the way.

You bring something to the table that pure software developers do not: you understand buildings. You know what a door width requirement means for accessibility. You know why natural light in a room matters. You know the difference between net floor area and gross floor area. The coding is the medium. Your domain knowledge is what makes the work meaningful.
