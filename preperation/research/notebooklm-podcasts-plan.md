# NotebookLM Podcast Onboarding Plan

## Intention

Generate **4 AI-generated podcasts** via Google NotebookLM that students listen to **before the course starts** (or on Day 0). This gives them a baseline understanding across all key topics without requiring reading. NotebookLM turns uploaded source documents into conversational podcast-style audio -- so the quality depends entirely on what we feed it.

Each podcast targets ~15-20 min and covers one theme. Together they form a complete onboarding package.

---

## Podcast 1: Course Introduction & The Startup Simulation

**Goal:** Get students excited, explain the format, set expectations.

### Sources to prepare:
- [ ] **Course overview document** -- adapted from `overview.md`, written as a narrative (not bullet points). NotebookLM works best with prose.
  - What the week looks like day-by-day
  - The "startup simulation" framing (you ARE a company, instructor is CEO, captains are tech leads)
  - What the final deliverable is (compliance checking platform)
  - Team structure and how it evolves (Day 1-2 equal teams -> Day 3 specialization)
- [ ] **IFC / AEC context primer** -- 1-2 pages explaining:
  - What is IFC (Industry Foundation Classes) in plain language
  - Why compliance checking matters in construction
  - What the IFC-Bench dataset is and why it's useful
  - The shared result schema concept (the "contract")
- [ ] **Expectations & logistics** -- what students should have installed, what tools are supported, daily rhythm

### Tone: Energizing, practical, "here's what you're walking into"

---

## Podcast 2: AI Agents -- Concepts & Glossary

**Goal:** Demystify AI agent terminology. Students arrive knowing what an "agent" actually is, what tools/MCP/orchestration mean, so Day 2-3 lectures can go deeper.

### Sources to prepare:
- [ ] **AI Agents glossary** -- (Joo has an existing one, locate and adapt). Key terms:
  - Agent, Tool, Tool Use / Function Calling
  - MCP (Model Context Protocol)
  - Structured Outputs
  - Orchestration / Agentic workflows
  - RAG (Retrieval Augmented Generation)
  - Prompt engineering basics
  - Context window, tokens
  - Multi-agent systems
  - Human-in-the-loop
- [ ] **"Why agents matter for AEC" narrative** -- 1-2 pages connecting agent concepts to the course project:
  - An agent that checks building compliance = real use case
  - Tools = IFC parsing scripts the students will write
  - Orchestration = combining multiple checks into one workflow
- [ ] **Current state of AI agents (2025)** -- brief landscape overview:
  - Claude, GPT, Gemini -- capabilities relevant to coding
  - Coding assistants: Claude Code, Cursor, Windsurf, Copilot, Codex
  - What these tools can and can't do

### Tone: Educational, grounded, avoids hype

---

## Podcast 3: Software Architecture & The Tech Stack

**Goal:** Give students mental models for how software systems are structured, steered toward the stack they'll actually use.

### Sources to prepare:
- [ ] **Architecture patterns primer** -- written for beginners, covering:
  - Client-server basics (frontend vs backend)
  - API patterns: REST, webhooks, what is an endpoint
  - Microservices vs monolith (light touch -- just enough to understand why checks are separate services)
  - Data flow: how results move from check scripts -> database -> frontend
  - Deployment basics: what "deploying to the cloud" actually means
- [ ] **Stack-specific guide** (TBD -- finalize stack first):
  - **Frontend:** What viewer library (That Open Engine / xeokit / three.js)?
  - **Backend:** Python services, how they expose endpoints
  - **Database:** Where check results are stored (Cloudflare D1? PostgreSQL?)
  - **Deployment:** Cloudflare Workers/Pages or alternative
  - **IFC tooling:** ifcopenshell, trimesh, the conversion pipeline
- [ ] **AGENTS.md / governance concept** -- explain how shared rules work across different AI coding tools
  - What is AGENTS.md and why every team follows it
  - Agent Skills as reusable instructions

### Tone: Practical, visual (describe diagrams even though it's audio), "here's how the pieces connect"

### DECISION NEEDED: Finalize the tech stack before writing this source material.

---

## Podcast 4: Python & AI-Assisted Coding Skills

**Goal:** Level-set on Python basics and teach students how to effectively work with AI coding assistants.

### Sources to prepare:
- [ ] **Python essentials for the course** -- focused on what they'll actually use:
  - Functions, dictionaries, lists
  - Reading/writing JSON
  - Basic file I/O
  - Using libraries (pip install, imports)
  - Type hints and Pydantic models (leads into structured outputs)
  - Error handling basics
- [ ] **Working with AI coding assistants** -- practical guide:
  - How to write good prompts for code generation
  - When to trust AI output vs when to verify
  - How to iterate: "this doesn't work" -> provide error -> refine
  - Reading and understanding AI-generated code (don't just copy-paste blindly)
  - Using context files (AGENTS.md, CLAUDE.md) to steer AI behavior
- [ ] **Latest AI coding patterns (2025)** -- brief overview:
  - Structured outputs with Pydantic
  - Tool use / function calling patterns
  - PydanticAI for agent orchestration
  - MCP (Model Context Protocol) -- what it is, why it matters

### Tone: Encouraging, practical, "you don't need to be an expert, here's how to be effective"

---

## Research TODOs

### Locate existing materials
- [ ] Find Joo's existing AI agents glossary
- [ ] Review prototype code for accurate stack description
- [ ] Check if any IFC/AEC intro materials already exist

### Decisions blocking content
- [ ] Finalize tech stack (frontend viewer, backend framework, database, deployment)
- [ ] Decide on real CTE excerpts vs dummy regulations (affects how we describe the project)
- [ ] Confirm PydanticAI as the orchestration framework

### Content to write
- [ ] Podcast 1 sources: course narrative + IFC primer + logistics
- [ ] Podcast 2 sources: glossary doc + AEC connection narrative + landscape overview
- [ ] Podcast 3 sources: architecture primer + stack guide + governance explainer
- [ ] Podcast 4 sources: Python essentials + AI coding guide + latest patterns

### Production
- [ ] Upload each podcast's sources to a separate NotebookLM notebook
- [ ] Generate audio, review for accuracy
- [ ] Share with students via course platform/link before Day 1

---

## Notes

- NotebookLM works best with **well-written prose documents**, not bullet lists or code. Convert technical content into readable narratives before uploading.
- Each notebook can take multiple source documents -- aim for 2-4 focused docs per podcast rather than one giant dump.
- Consider having the 7 experienced students ("captains") listen first and flag anything confusing.
