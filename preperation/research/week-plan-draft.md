# IAAC AI Week -- Merged Schedule Draft (v1)

**Feb 16-20, 2026 | 4 working days + Friday presentations**
**Daily: 10:30-13:30 (morning) + 14:30-17:30 (afternoon) = 6h/day**

---

## OPEN DECISIONS (must resolve before Day 1)

| # | Decision | Options | Impact |
|---|----------|---------|--------|
| 1 | **Do students write code manually or only via AI agents?** | A) Colab first, then AI agents. B) AI agents from the start -- students write PRDs, agents implement. C) Hybrid -- simple functions by hand Day 1, AI agents from Day 2. | Determines the entire teaching approach |
| 2 | **Which AI coding tool?** | Claude Code, Cursor, Codex CLI, or let them choose? Need skills/AGENTS.md support. | Must be decided so we can prepare setup instructions |
| 3 | **What does the final product look like?** | Need a demo/mockup to show Day 1 morning. The prototype exists but is it enough? | Students need a north star |
| 4 | **Checkpoint expectations** | What's the minimum bar at each checkpoint? | Needs to be defined per day |
| 5 | **Shared repo structure** | One monorepo? One repo per team? Shared repo with folders? | Affects GitHub setup on Tuesday |
| 6 | **Who lectures what?** | Split between Serjoscha and colleague | Need to assign before Monday |

---

## THE PLAN

### Monday Feb 16 -- "Make It Work"
*Goal: Students understand the project, see the final vision, get set up, write their first IFC check.*

#### Morning (10:30-13:30)

| Time | What | Who | Format |
|------|------|-----|--------|
| 10:30-10:45 | **Welcome + show final product vision** -- demo the prototype, show where we're heading. "This is what you'll build by Thursday." | Serjoscha? | Demo |
| 10:45-11:00 | **Startup simulation intro** -- you are a company, roles, how the week works, board meetings | Serjoscha? | Talk |
| 11:00-12:00 | **LLM fundamentals lecture** (~45min + Q&A) -- what are LLMs, what can they do, prompt basics | Colleague? | Lecture |
| 12:00-12:15 | Break | | |
| 12:15-13:00 | **IFC files deep dive** -- what's inside an IFC file, how to parse them, ifcopenshell, the vendor property problem | Serjoscha? | Lecture + live demo |
| 13:00-13:30 | **Discussion** -- what did students find in pre-course material, initial feature ideas, group formation starts | Both | Open discussion |

#### Afternoon (14:30-17:30)

| Time | What | Who | Format |
|------|------|-----|--------|
| 14:30-15:00 | **Tool setup** -- install VS Code (or Cursor), GitHub Desktop, AI coding agent, verify Python works | Both | Hands-on |
| 15:00-15:15 | **Quick intro to IDE + terminal** -- what is VS Code, what is the terminal, how to run a script | ? | Demo |
| 15:15-16:30 | **Exercise: write your first IFC check tool** (~75min) -- each team writes 1-2 check functions following the prototype pattern. Use AI coding assistant. | Both support | Hands-on exercise |
| 16:30-16:45 | Break | | |
| 16:45-17:15 | **Teams present what they built** -- quick demos of new checks | Students | Demo round |
| 17:15-17:30 | **"Board meeting" #1** -- lock the shared result schema, assign teams, preview Day 2 | Serjoscha | Wrap-up |

**Monday checkpoint:** Every team has 1+ working check function that produces results in the shared format.

---

### Tuesday Feb 17 -- "Make It Talk"
*Goal: Students understand git, build an agent with tools, learn about APIs and more advanced AI concepts.*

*Note: Colleague has lunch date ~14:00-15:00*

#### Morning (10:30-13:30)

| Time | What | Who | Format |
|------|------|-----|--------|
| 10:30-11:30 | **Git & GitHub explained** (~45min + setup) -- what is version control, branches, commits, PRs. Set up repos for each group. | Colleague? | Lecture + hands-on |
| 11:30-11:45 | Break | | |
| 11:45-13:00 | **Exercise: build an Agent with several tools** -- using the check functions from Monday as tools, build an agent that can answer questions like "Is this building accessible?" | Both | Hands-on exercise |
| 13:00-13:30 | Buffer / continued work | | |

#### Afternoon (14:30-17:30)

| Time | What | Who | Format |
|------|------|-----|--------|
| 14:30-15:30 | **Lecture: AI tools & advanced concepts** -- structured outputs, tool use, RAG, MCP overview, APIs & requests | Colleague? | Lecture |
| 15:30-15:45 | Break | | |
| 15:45-17:00 | **Group work** -- teams refine checks, wrap as proper tools, start thinking about integration | Both support | Sprint |
| 17:00-17:30 | **"Board meeting" #2** -- teams demo their agents, new requirements dropped: "the client wants a web interface" | Serjoscha | Demo + wrap-up |

**Tuesday checkpoint:** Every team has an agent that uses their check tools and can answer compliance questions.

---

### Wednesday Feb 18 -- "Make It Smart"
*Goal: Frontend work begins, teams specialize, integration starts.*

#### Morning (10:30-13:30)

| Time | What | Who | Format |
|------|------|-----|--------|
| 10:30-11:30 | **Exercise: 3D web viewer** -- how to display a building model in a browser, connecting it to check results | ? | Lecture + hands-on |
| 11:30-11:45 | Break | | |
| 11:45-13:30 | **Group work** -- teams specialize. Frontend team starts building the viewer. Check teams add more checks, improve agents. | Both support | Sprint |

#### Afternoon (14:30-17:30)

| Time | What | Who | Format |
|------|------|-----|--------|
| 14:30-15:00 | **CHECKPOINT** -- every team shows what they have, blockers are identified | Both | Demo round |
| 15:00-15:15 | Break | | |
| 15:15-17:00 | **Group work** -- continue building, integrate pieces, connect frontend to backend | Both support | Sprint |
| 17:00-17:30 | **"Board meeting" #3** -- status check, final push planning for Thursday | Serjoscha | Wrap-up |

**Wednesday checkpoint:** A frontend exists (even basic). Check results can flow from backend to frontend. Integration is underway.

---

### Thursday Feb 19 -- "Make It Real"
*Goal: Integration, polish, deployment, rehearse presentation.*

*Note: Sprint Recap & Planning meeting 11:00-13:00 (Serjoscha conflict)*

#### Morning (10:30-13:30)

| Time | What | Who | Format |
|------|------|-----|--------|
| 10:30-11:00 | **Mini-lecture (if needed)** -- deployment basics, or topic based on what students are struggling with | ? | Lecture |
| 11:00-13:30 | **Group work + integration sprint** -- connect all pieces, deploy if possible, fix bugs | Both (Serjoscha may be in/out due to Sprint meeting) | Sprint |

#### Afternoon (14:30-17:30)

| Time | What | Who | Format |
|------|------|-----|--------|
| 14:30-16:30 | **Final integration sprint** -- everything must work together | Both support | Sprint |
| 16:30-17:00 | **Presentation prep** -- each team prepares their Friday demo (3-5 min each) | Students | Prep |
| 17:00-17:30 | **Dress rehearsal** -- quick run-through of all presentations | Both | Rehearsal |

**Thursday checkpoint:** The platform works end-to-end. Each team can demo their contribution.

---

### Friday Feb 20 -- Presentations

| Time | What |
|------|------|
| 11:00 | (Serjoscha has "blocker" 11-12) |
| TBD | **Final Presentations** -- each team demos to "investors"/jury |

*Note: Serjoscha has goNEON Tech Workshop in Zurich at 15:30. Presentations must finish before that or Serjoscha joins remotely.*

---

## WHAT STUDENTS NEED BEFORE DAY 1

| Item | Status |
|------|--------|
| Listen to 5 pre-course podcasts | Podcasts being prepared |
| Python 3.10+ installed | Need setup instructions |
| VS Code or Cursor installed | Need setup instructions |
| AI coding tool set up (Claude Code / Cursor / ...) | **DECISION NEEDED** |
| GitHub account | Need to communicate |
| IFC sample files downloaded | Need to prepare download link |

## LECTURE / EXERCISE MATERIAL NEEDED

| Item | Who prepares? | Status |
|------|--------------|--------|
| LLM fundamentals lecture (Mon AM) | ? | ? |
| IFC deep dive (Mon AM) | ? | ? |
| Tool setup instructions | ? | Not started |
| First check exercise brief | ? | Prototype exists |
| Git & GitHub lecture (Tue AM) | ? | ? |
| Agent-building exercise (Tue AM) | ? | ? |
| AI tools & advanced concepts lecture (Tue PM) | ? | ? |
| 3D web viewer exercise (Wed AM) | ? | ? |
| APIs & requests explanation | ? | ? |
| Deployment guide (Thu) | ? | ? |
| Presentation template | ? | ? |
