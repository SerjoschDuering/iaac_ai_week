# IAAC AI Week -- Course Plan (v2)

**Feb 16-20, 2026 | 4 working days + Friday presentations**
**Daily: 10:30-13:30 (morning) + 14:30-17:30 (afternoon) = 6h/day**
**~29 students | ~7 experienced "Captains" | 2 instructors**

---

## THE ARC (in 5 sentences)

On Monday, students land in a startup that just signed its first client: check buildings against regulations. They get their hands dirty -- open IFC files, write a check function, see results in 3D. On Tuesday, the board demands speed and standards: teams add AI to their tools, agree on a shared data format, and start building agents that reason about compliance. On Wednesday, the board drops the bomb -- "the investor demo is Friday, we need a real product" -- and captains step up to design a unified platform while teams race to connect their pieces. Thursday is the integration sprint: everything comes together, gets deployed, and the startup rehearses its pitch. Friday, they present to "investors."

---

## PHILOSOPHY

Students are a startup. They don't follow a syllabus -- they respond to escalating demands from "the board" (instructors). Complexity grows organically:

```
Mon: Write a function         → "Here's a regulation, can you check it?"
Tue: Make it smarter with AI  → "We need to scale this, agree on standards"
Wed: Connect the pieces       → "The client wants a real product"
Thu: Ship it                  → "Investors are coming Friday"
```

**Three engines drive the week:**

1. **Board meetings** -- end-of-day reveals that push teams into the next level of complexity. What gets "decided" in each board meeting is scripted in advance but feels emergent.
2. **Agent Skills** -- after each board meeting, a new skill file is seeded into the shared repo. Students' AI coding assistants pick it up automatically. This is how standards propagate without micro-managing.
3. **Miro** -- the shared canvas where everything is visible: team progress, tool documentation (input/output), PRDs, user stories, architecture sketches. If it's not on Miro, it doesn't exist.

---

## CAPTAIN EVOLUTION

| Day | Captain Role | What They Do |
|-----|-------------|-------------|
| **Mon** | Floor support | Help teammates with setup, debug installation issues, translate instructions for confused students |
| **Tue** | Quality lead | Ensure their team's tools are documented (input/output on Miro), represent their team at the board meeting schema discussion |
| **Wed** | Architect | Lead the brainstorming: what features does the platform need? Sketch integration plan. Coordinate who builds what |
| **Thu** | Tech lead / PM | Own the integration sprint, assign tasks, unblock their team, prepare the demo narrative |

---

## OPEN DECISIONS (must resolve before Day 1)

| # | Decision | Options | Impact |
|---|----------|---------|--------|
| 1 | **Do students write code manually or via AI agents?** | A) Colab/notebook first, AI agents from Day 2. B) AI agents from start. C) Hybrid. | Determines teaching approach |
| 2 | **Which AI coding tool?** | Claude Code, Cursor, Codex CLI, or let them choose? | Setup instructions + skill compatibility |
| 3 | **Final product teaser** | What do we show on Day 1 morning? Prototype enough or need a mockup? | Students need a north star |
| 4 | **Shared repo structure** | Monorepo with folders per team? One repo per team? Template repo they clone? | Affects Monday afternoon setup |
| 5 | **Who lectures what?** | Split between Serjoscha and colleague | Need to assign before Monday |
| 6 | **Colab/notebook or local IDE from Day 1?** | Colab is zero-setup but limited. Local IDE is real but setup takes time. | Monday afternoon depends on this |

---

## THE PLAN

### Monday Feb 16 -- "Make It Work"

*Goal: Students understand the project, see where it's going, get set up, and write their first check tool.*

#### Morning (10:30-13:30)

| Time | What | Format | Notes |
|------|------|--------|-------|
| 10:30-11:15 | **Final Product Teaser** | Demo + talk | Show the prototype in action. Then: LLM agent basics, tool use analogy ("your function is a tool an AI can call"), derive the week's progression from simple to complex. "This is where you'll be by Thursday." |
| 11:15-11:30 | **Company Simulation Kick-off** | Talk | You ARE a startup. Instructor = CEO/board. Captains = tech leads. Board meetings = client demos. Miro = your war room. If it's not documented, it doesn't exist. |
| 11:30-11:45 | Break | | |
| 11:45-12:45 | **IFC Deep Dive** | Lecture + live demo | What's inside an IFC file. Entity types, spatial hierarchy, property sets, THE VENDOR PROBLEM. Live: open a file in ifcopenshell, query elements, show how properties hide in different places. |
| 12:45-13:30 | **Discussion** | Open | What did students learn from pre-course podcasts? Questions about IFC? Initial ideas for what regulations could be checked? Group formation starts. |

#### Afternoon (14:30-17:30)

| Time | What | Format | Notes |
|------|------|--------|-------|
| 14:30-15:15 | **Setup Sprint** | Hands-on | Clone template repo (with IFC sample data pre-loaded). Install VS Code (or Cursor) + GitHub Desktop. Brief explanation of each tool. Captains help their teams. |
| 15:15-15:30 | **Look at a Sample Regulation** | Talk + demo | Show one concrete regulation (e.g., "doors must be >= 800mm"). Walk through: how would you check this against an IFC file? What's the input? What's the output? |
| 15:30-16:45 | **Exercise: Build Your First Check Tool** | Hands-on | Each team writes 1-2 check functions in Colab/notebook. Pattern: read IFC → extract property → compare to threshold → return result. **Key rule: every tool must be documented on Miro** -- what's the input, what's the output, what regulation does it check. Then: add function to our Gradio app ("insert your function here" placeholder). Visualize results in the 3D viewer. |
| 16:45-17:00 | Break | | |
| 17:00-17:30 | **Teams present on Miro** | Demo round | Each team shows: their check function, its documentation (input/output), and the Gradio visualization. Quick, 3 min per team. |

> **No board meeting on Monday.** Let them go home proud of what they built. The pressure starts Tuesday.

**Monday checkpoint:** Every team has 1+ working check function, documented on Miro (input/output/regulation), visible in the Gradio app.

**Miro after Monday:**
```
┌─────────────┐  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐
│   Team A    │  │   Team B    │  │   Team C    │  │   Team D    │  │   Team E    │
│             │  │             │  │             │  │             │  │             │
│ Tool: Door  │  │ Tool: Room  │  │ Tool: Wall  │  │ Tool: Stair │  │ Tool: Fire  │
│ Width Check │  │ Area Check  │  │ Thickness   │  │ Width Check │  │ Exit Count  │
│             │  │             │  │             │  │             │  │             │
│ In: IFC +   │  │ In: IFC +   │  │ In: IFC +   │  │ In: IFC +   │  │ In: IFC +   │
│ threshold   │  │ min area    │  │ min thick.  │  │ min width   │  │ min exits   │
│ Out: pass/  │  │ Out: pass/  │  │ Out: pass/  │  │ Out: pass/  │  │ Out: pass/  │
│ fail list   │  │ fail list   │  │ fail list   │  │ fail list   │  │ fail list   │
└─────────────┘  └─────────────┘  └─────────────┘  └─────────────┘  └─────────────┘
```

---

### Tuesday Feb 17 -- "Make It Talk"

*Goal: Tools become smarter with LLMs. Students learn AI-driven development. The shared schema emerges.*

*Note: Colleague has lunch date ~14:00-15:00*

#### Morning (10:30-13:30)

| Time | What | Format | Notes |
|------|------|--------|-------|
| 10:30-11:30 | **Lecture: LLMs + Tool Use** | Lecture | LLM recap from podcasts. APIs -- what they are, how to call one. LLM autonomy levels (from autocomplete → tool use → full agent). Structured outputs -- making LLMs return JSON, not prose. Live demo: call an LLM API, get structured output. |
| 11:30-11:45 | Break | | |
| 11:45-13:00 | **Exercise: Add an LLM-Powered Tool** | Hands-on | Each team adds a tool that **calls an LLM** as part of its check logic. Example: "Given this IFC element description, does it meet accessibility requirements?" The LLM interprets, the tool returns structured pass/fail. **Document on Miro**: input, output, what the LLM does inside. |
| 13:00-13:30 | **Discussion** | Open | What worked? What's hard about getting structured output from an LLM? What patterns are emerging? |

#### Afternoon (14:30-17:30)

| Time | What | Format | Notes |
|------|------|--------|-------|
| 14:30-15:00 | **Lecture: AI-Driven Development** | Talk (30min) | Vibe coding. Spec-driven development. PRDs and user stories. The loop: *define what you want → write it down → let the AI build it → review → iterate.* "Your job is to be the architect, not the bricklayer." |
| 15:00-15:15 | **Lecture: Agent Skills** | Talk (15min) | What is an Agent Skill? How does AGENTS.md work? "This is how our company's engineering standards propagate -- every AI assistant reads the same rules." |
| 15:15-15:30 | Break | | |
| 15:30-16:15 | **--- BOARD MEETING #1 ---** | All-hands | |

> **Board Meeting #1: "We Need Standards"**
>
> **What's discussed:** Review all tools on Miro. Look at the different input/output formats each team used. "Team A returns a list of dicts, Team C returns a dataclass, Team E returns raw strings. The client can't work with this chaos."
>
> **What's decided:** "We need ONE shared output schema for ALL check tools. Captains -- propose a format based on what you built. You have 15 minutes."
>
> Captains huddle, sketch a schema on Miro. Board approves (or tweaks). Schema is locked.
>
> **Sprint goal announced:** "By end of Thursday, we need an AI agent that can answer: *Is this building compliant?* using ALL of our tools. Start now."
>
> **What's seeded:** `Skill: validation-schema` -- describes the agreed-upon output format. Every AI assistant now enforces it. Students also get: `Skill: ifc-check-template` -- a template for writing checks that conform to the schema.

| Time | What | Format | Notes |
|------|------|--------|-------|
| 16:15-16:30 | **Exercise: Set Up the Skill** | Hands-on (15min) | Students pull the new skill into their repo. Test that their AI assistant knows the schema. Quick verification: "describe the check output format" → AI should answer correctly. |
| 16:30-17:15 | **Exercise: PRD → Agent** | Hands-on | **The loop begins.** Each team writes a PRD on Miro: "An AI agent that uses our check tools to answer compliance questions about a building." Break it into user stories. Then: implement with PydanticAI (decided at the board meeting). Test in the Gradio app's chat interface. |
| 17:15-17:30 | Buffer / continued work | | |

**Tuesday checkpoint:** Every team has (1) tools conforming to the shared schema, (2) a PydanticAI agent that uses those tools, (3) a PRD + user stories on Miro.

**Miro after Tuesday:**
```
┌──────────────────────────────────────────────────────────────────┐
│                    SHARED OUTPUT SCHEMA                          │
│  {element_id, element_type, element_name, rule, requirement,    │
│   actual_value, passed}                                         │
└──────────────────────────────────────────────────────────────────┘
        │              │              │              │
┌───────┴───┐  ┌───────┴───┐  ┌───────┴───┐  ┌───────┴───┐
│  Team A   │  │  Team B   │  │  Team C   │  │  Team D   │  ...
│           │  │           │  │           │  │           │
│ Tools (3) │  │ Tools (2) │  │ Tools (4) │  │ Tools (2) │
│ Agent PRD │  │ Agent PRD │  │ Agent PRD │  │ Agent PRD │
│ Stories   │  │ Stories   │  │ Stories   │  │ Stories   │
└───────────┘  └───────────┘  └───────────┘  └───────────┘
```

---

### Wednesday Feb 18 -- "Make It Connect"

*Goal: Teams learn how services communicate. Captains design the platform. Integration begins.*

#### Morning (10:30-13:30)

| Time | What | Format | Notes |
|------|------|--------|-------|
| 10:30-11:15 | **Lecture: How Software Talks** | Lecture (45min) | APIs and endpoints -- the waiter analogy from the podcast, now concrete. REST basics (GET, POST). How a frontend calls a backend. Databases -- where do check results live? How does the frontend read them? Quick live demo: call an API endpoint, get JSON back. |
| 11:15-11:30 | Break | | |
| 11:30-12:30 | **Exercise: Connect Something** | Hands-on | Teams take their agent/tools and expose ONE endpoint (e.g., "POST /check with an IFC file, get results back"). Or: write results to a shared database. The goal is: make your work accessible to OTHER teams, not just your laptop. |
| 12:30-13:30 | **--- BOARD MEETING #2 ---** | All-hands | |

> **Board Meeting #2: "The Client Wants a Real Product"**
>
> **What's discussed:** "The investor demo is in 2 days. Right now we have 5 separate teams with 5 separate agents running on 5 laptops. That's not a product. We need ONE platform."
>
> **Open brainstorming (everyone):** "What features does the final product need?" Students + captains brainstorm on Miro. Ideas get clustered: 3D viewer, dashboard, multi-file support, report export, login, real-time updates, etc.
>
> **What's decided:**
> - Captains are now in **lead & organization positions** -- they own the integration plan
> - Captains pick the top features from the brainstorm that are realistic for Thu
> - Teams that still need to finish checks continue, but their output must flow into the platform
> - "What tech options do we have?" Quick discussion of architecture choices (hosted API, database, frontend framework)
>
> **What's seeded:** `Skill: platform-architecture` -- describes the target architecture: how services connect, where the database is, what the API looks like, how the frontend reads data. Students' AI assistants now "know" the platform structure.

#### Afternoon (14:30-17:30)

| Time | What | Format | Notes |
|------|------|--------|-------|
| 14:30-15:00 | **Captains Planning Session** | Captains only | Captains meet separately. They sketch the integration plan on Miro: who builds what, what connects to what, what's the MVP for Thursday. Instructors available for guidance. |
| 15:00-15:15 | **Captains Present the Plan** | All-hands (15min) | Captains present their integration plan to everyone. Teams get their assignments. |
| 15:15-15:30 | Break | | |
| 15:30-17:00 | **Sprint: Build the Platform** | Hands-on | Under captain direction: some teams keep building/refining checks + agents. Others start the frontend, database, or API layer. PRD → user stories → implement loop continues. Everything goes through the seeded skills. |
| 17:00-17:30 | **Quick Status Check** | Demo round | Each captain: 2 min update. What's working, what's blocked, what's needed for tomorrow. |

**Wednesday checkpoint:** Architecture is defined on Miro. At least one integration path works (e.g., check results flowing to a database, or a basic frontend loading results from an API). Captains own the plan.

**Miro after Wednesday:**
```
┌─────────────────────────────────────────────────────────────────┐
│                     PLATFORM ARCHITECTURE                       │
│                                                                 │
│  [Frontend]  ←→  [API Server]  ←→  [Database]                  │
│      │                │                                         │
│      └── 3D Viewer    ├── /check endpoint                      │
│      └── Dashboard    ├── /results endpoint                    │
│                       └── [Check Tools + Agents]                │
│                                                                 │
│  Feature Backlog:          Assigned to:                         │
│  □ 3D viewer               Captain A's team                    │
│  □ Results dashboard        Captain B's team                    │
│  □ Multi-file upload        Captain C's team                    │
│  □ Report export            Stretch goal                        │
└─────────────────────────────────────────────────────────────────┘
```

---

### Thursday Feb 19 -- "Make It Real"

*Goal: Integration sprint. Everything connects. Polish. Rehearse.*

*Note: Sprint Recap & Planning meeting 11:00-13:00 (Serjoscha may be in/out)*

#### Morning (10:30-13:30)

| Time | What | Format | Notes |
|------|------|--------|-------|
| 10:30-10:45 | **Standup** | All-hands | Captains: 1 min each. What's the status? What's blocked? What's the plan for today? |
| 10:45-11:00 | **Mini-lecture (if needed)** | Talk | Deployment basics, or whatever topic is most blocking. Could also be: "how to present a technical product to non-technical people." |
| 11:00-13:30 | **Integration Sprint** | Hands-on | Connect all pieces. Captains coordinate. Instructors debug and unblock. **Teams that finish early:** pick items from the feature backlog brainstormed yesterday. This is open-ended -- ambitious teams can extend the platform. |

#### Afternoon (14:30-17:30)

| Time | What | Format | Notes |
|------|------|--------|-------|
| 14:30-16:00 | **Final Sprint** | Hands-on | Everything must work together. Feature freeze at 16:00 -- after that, only bug fixes. |
| 16:00-16:15 | Break | | |
| 16:15-17:00 | **Presentation Prep** | Team work | Each team prepares their Friday demo (3-5 min). Captains structure the overall narrative: "Here's what our startup built." |
| 17:00-17:30 | **Dress Rehearsal** | All-hands | Full run-through. Instructors give feedback. Timing check. |

> **Board Meeting #3 (informal, during rehearsal):** "The investors are impressed. Ship it."

**Thursday checkpoint:** The platform works end-to-end. Each team can demo their contribution. Presentations are rehearsed.

---

### Friday Feb 20 -- Presentations

| Time | What |
|------|------|
| 11:00 | *(Serjoscha has blocker 11-12)* |
| TBD | **Final Presentations** -- each team demos to "investors" / jury. The startup pitches its product. |

*Note: Serjoscha has goNEON Tech Workshop in Zurich at 15:30. Presentations must finish before that or Serjoscha joins remotely.*

---

## THE DEVELOPMENT LOOP (introduced Tuesday, used rest of week)

This is the core workflow students learn and repeat:

```
1. DEFINE   →  Write a PRD on Miro (what should this feature do?)
2. BREAK    →  Split into user stories (small, testable chunks)
3. SEED     →  Ensure the relevant Agent Skill is in your repo
4. BUILD    →  AI assistant implements based on PRD + skill + user stories
5. REVIEW   →  Does it match the PRD? Does it pass the schema?
6. DOCUMENT →  Update Miro: input/output, status, what's next
7. REPEAT
```

---

## SKILL SEEDING SCHEDULE

| When | Skill Name (conceptual) | What It Contains | Triggered By |
|------|------------------------|------------------|-------------|
| **Pre-loaded (Day 1)** | `ifc-patterns` | How to parse IFC files, property fallback patterns, common entity types | Part of template repo |
| **After Board Meeting #1 (Tue)** | `validation-schema` | The agreed-upon output format for all check results | Schema decision |
| **After Board Meeting #1 (Tue)** | `ifc-check-template` | Template for writing new checks that conform to the schema | Schema decision |
| **After Board Meeting #1 (Tue)** | `pydantic-ai-agent` | How to build a PydanticAI agent with tools | Sprint goal announcement |
| **After Board Meeting #2 (Wed)** | `platform-architecture` | Target architecture, API endpoints, database schema, how services connect | Architecture decision |
| **Thu (if needed)** | `deployment-guide` | How to deploy the platform, environment setup, hosting | Integration sprint |

---

## MIRO BOARD STRUCTURE (suggested)

| Section | What Goes Here | When It's Used |
|---------|---------------|----------------|
| **Team Zones** (5 columns) | Each team's tool documentation, PRDs, user stories, status | All week |
| **Shared Schema** | The locked output format, with examples | From Tuesday onward |
| **Architecture** | Platform diagram, who builds what, integration plan | Wednesday onward |
| **Feature Backlog** | Brainstormed features, priority, assignment | Wednesday board meeting |
| **Regulation Library** | The regulations being checked, with references | All week |
| **Presentation Flow** | Demo script, who presents what, timing | Thursday |

---

## WHAT STUDENTS NEED BEFORE DAY 1

| Item | Status |
|------|--------|
| Listen to 5 pre-course podcasts | Podcasts being prepared |
| Python 3.10+ installed | Need setup instructions |
| VS Code or Cursor installed | Need setup instructions |
| AI coding tool set up | **DECISION NEEDED** |
| GitHub account | Need to communicate |
| Google account (for Colab, if using) | Need to communicate |

---

## MATERIAL TO PREPARE

| Item | When Needed | Who? | Status |
|------|------------|------|--------|
| Final product teaser / demo script | Mon AM | ? | Prototype exists |
| Company simulation intro script | Mon AM | Serjoscha? | Concept exists |
| IFC deep dive lecture | Mon AM | ? | ? |
| Template repo with sample IFC data | Mon PM | ? | Needs creation |
| Gradio app with "insert your function here" | Mon PM | ? | Prototype needs adapting |
| Sample regulation handout | Mon PM | ? | ? |
| LLM + Tool Use lecture | Tue AM | ? | ? |
| AI-driven development lecture (vibe coding, PRDs) | Tue PM | ? | ? |
| Agent Skills lecture (15min) | Tue PM | ? | ? |
| Skill files (see seeding schedule) | Tue-Wed | ? | Need to write |
| APIs + databases lecture | Wed AM | ? | ? |
| Miro board template | Day 1 | ? | ? |
| Presentation template | Thu PM | ? | ? |
