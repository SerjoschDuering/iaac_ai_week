## IAAC One-Week Intensive Course (Refined Overview)

### Context
- **Institution:** IAAC, Barcelona
- **Duration:** 1 week intensive
- **Schedule:** 4 main working days + final presentations on Friday
- **Daily format:** ~6 hours/day, split into 2 blocks of ~3 hours
- **Theme:** AI-supported software development for the AEC industry (architecture/building domain)
- **Participants:** ~29 students
- **Experience distribution:** ~7 students are already experienced with coding and AI-assisted development ("vibe coding")
- **AI tools:** Mixed -- students use Claude Code, Cursor, Windsurf, Codex, Copilot, etc.

### Company Story (Course Framing)
Students **are** a startup called (name TBD -- students pick on Day 1). They just landed their first contract: a Spanish real estate developer needs an automated platform that checks building models against regulations before construction begins.

- **CEO / Board:** Instructor. Sets deadlines, drops new requirements at "board meetings," plays the impatient client.
- **Tech Leads (Captains):** 7 experienced students. Own team delivery, attend cross-team standups, make architecture decisions.
- **Engineers:** Remaining ~22 students. Build features within their team.

"Board meetings" (end-of-day demos) are where new requirements get introduced organically: "The client now wants one unified dashboard," "Legal says we need CTE DB-SUA support," etc. This drives the milestones without them feeling like homework.

### Team Structure (Evolving)

**Key principle: all teams start equal.** No specialized frontend or infra team on Day 1. Everyone does the same thing first -- learn IFC, write checks, get comfortable.

**Later stages (Day 3-4):** Pull people from existing teams to form new specialized teams as needs emerge. Announced at a "board meeting."

```
Day 1-2:  All teams equal -- everyone writes IFC checks
          ┌──────┬──────┬──────┬──────┬──────┐
          │  A   │  B   │  C   │  D   │  E   │
          │checks│checks│checks│checks│checks│
          └──────┴──────┴──────┴──────┴──────┘

Day 3-4:  New teams form by pulling people from existing teams
          ┌──────┬──────┬──────┬─────────────┬──────────┐
          │  A   │  B   │  C   │  Frontend   │  ???     │
          │tools │tools │tools │ (pulled     │ (pulled  │
          │      │      │      │  from teams)│  from    │
          │      │      │      │             │  teams)  │
          └──────┴──────┴──────┴─────────────┴──────────┘
          (possible additional team TBD -- orchestration? deployment?)
```

Captains nominate who moves. This mirrors how real startups reallocate people when new needs emerge.

### Core Project Challenge
- **Input data:** IFC building models (from IFC-Bench dataset -- 21 projects, 37 IFC files, CC BY 4.0)
- **Dataset:** https://huggingface.co/datasets/sylvainHellin/ifc-bench
  - 1,027 question-answer pairs with known ground truth
  - 4 complexity categories (direct retrieval, aggregation, spatial, incomplete info)
  - Useful as Day 1 warmup exercises AND as test buildings for compliance checks
- **Goal:** Build tools/workflows that check IFC models against regulations
- **Checks include:**
  - Clearly defined rule checks (dummy regulations, simplified CTE excerpts)
  - Open-ended checks requiring contextual interpretation (maps to IFC-Bench Category 4)
- **Strategy:** Start with dummy regulations on Day 1-2 (e.g., "doors >= 0.80m", "rooms >= 9m2"). Introduce real simplified CTE excerpts on Day 3 for teams that are ahead.

### Shared Result Schema (The Contract)
Locked on Day 1. All teams produce results in this format. Frontend builds against it from the start.

```python
{
    "element_id": "3x4F...",       # IFC GlobalId
    "element_type": "IfcDoor",     # IFC entity type
    "element_name": "Door #42",    # Human-readable name
    "rule": "Door Width",          # Check name
    "requirement": ">= 800 mm",   # What the regulation demands
    "actual": "700 mm",            # What was found
    "passed": false                # true / false / null (N/A)
}
```

### Prototype (Starting Point)
Existing Gradio app in `prototype/` with:
- 4 working checks: room area, wall thickness, door width, window per room
- 3D GLB viewer with red/gray highlighting of failures
- IFC-to-GLB conversion via ifcopenshell + trimesh
- See `prototype/LEARNINGS.md` for gotchas (pset fallbacks, PBR materials, world coords)

Students can see results on Day 1 without any infrastructure setup. Each team's first exercise: write 1-2 new check functions following the same pattern.

### Daily Rhythm

| Time | What | Company framing |
|---|---|---|
| Morning (30 min) | Mini-lecture + milestone briefing | "All-hands meeting" |
| Morning block (~2.5h) | Teams build | Sprint work |
| Midday (15 min) | Captains sync | "Tech lead standup" |
| Afternoon block (~2.5h) | Teams continue + integrate | Sprint work |
| End of day (20 min) | Demo what works | "Board meeting" / client demo |

### Technical Progression (Day by Day)

**Day 1 -- "Make it work"**
- Mini-lecture: IFC basics, ifcopenshell, the prototype
- Exercise: explore IFC-Bench questions as warmup (Category 1-2)
- Exercise: each team writes 1-2 new check functions
- Lock the shared result schema
- End of day: each team demos their checks running on a model

**Day 2 -- "Make it talk"**
- Mini-lecture: structured outputs, LLM-powered tools, what is MCP
- Teams refine checks, add LLM-based checks for open-ended regulations
- "Workflows with LLMs inside" -- tools that call an LLM for interpretation
- Begin wrapping checks as callable tools (MCP or API endpoints)
- End of day: demo tools being called programmatically, not just as scripts

**Day 3 -- "Make it smart"**
- Mini-lecture: PydanticAI, orchestration, agent patterns
- Board meeting: "Client wants a real dashboard" -- form frontend team + possibly one more
- Remaining teams: PydanticAI orchestrator that calls tools via chat
- Frontend team: build proper viewer (That Open Engine / xeokit / custom)
- Gradio chat interface alongside the viewer
- End of day: demo an agent answering "Is this building accessible?"

**Day 4 -- "Make it real"**
- Mini-lecture: deployment, integration, connecting services
- All teams integrate into one platform
- Cloud deployment (Cloudflare or similar)
- Polish, fix, connect
- End of day: full product demo rehearsal

**Day 5 -- Presentations**
- Final demos to "investors" / jury

### Agent Skills / AGENTS.md as Governance

**Cross-tool approach** (students use different AI coding tools):
- **AGENTS.md** at repo root = universal rules file (read by Cursor, Codex, Windsurf, Copilot, Claude Code, Gemini CLI)
- **Agent Skills** (agentskills.io standard) = reusable workflow instructions, also cross-tool
- **CLAUDE.md** = thin bridge for Claude Code users, references AGENTS.md

**Governance workflow:**
1. Captain standup -> agree on a standard (e.g., result schema, naming convention)
2. Instructor updates `AGENTS.md` + skills in shared repo
3. Teams `git pull`
4. Every student's AI assistant picks up the new rules automatically

**Company framing:** "Every company has engineering standards. Ours live in AGENTS.md."

**Planned skills to provide:**
- `validation-schema` -- enforces the shared result format
- `ifc-patterns` -- how to parse/query IFC data, pset fallback patterns
- `mcp-tool-template` -- template for wrapping scripts as callable tools
- `code-standards` -- naming, structure, documentation conventions

### Infrastructure Direction
- Cloudflare as deployment candidate (Workers, D1, Pages)
- Shared database for check results
- Common method for IFC file exchange between services
- Frontend viewer: That Open Engine, xeokit, or custom three.js (frontend team decides)

### Risks / Reality Check
- Plan is ambitious for one week, especially with ~22 beginners
- **Must-hit target:** Day 2 milestone (working checks + shared schema). Everything after is stretch.
- IFC parsing is a known rabbit hole -- the prototype + IFC-Bench dataset de-risk this significantly
- Success depends on strong captains carrying coordination
- The team-splitting on Day 3 could be disruptive if not handled well -- captains need advance notice
- Students on different AI tools is manageable via AGENTS.md but may cause some friction

### Open Questions
- What to call the company? (Let students decide Day 1)
- Which IFC-Bench projects to use? (Need to pick 5-6 good ones)
- What does the second new team (Day 3) do? Orchestration? Deployment? Data pipeline?
- Real CTE excerpts or fully dummy regulations?
- How to handle IFC file distribution (shared drive, HuggingFace download, pre-loaded)?
