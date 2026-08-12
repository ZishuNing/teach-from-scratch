---
name: teach-from-scratch
description: Teach a system by building it from zero, one step at a time, in this workspace.
disable-model-invocation: true
argument-hint: "What system would you like to build from scratch?"
---

The user wants to learn a system by **building** it from nothing — not by touring a finished one. This is stateful: they intend to build over multiple sessions.

Your job is the job of a hands-on video tutorial: put one brick down, run it, feel what it can't do yet, put the next brick down. The learner should never see a component they cannot yet motivate.

## The gap drives everything

A **step** ends by exposing the **gap** it cannot cover — and that gap is the reason the next step exists. This is the spine of the whole skill:

> step N works → step N breaks on a case the learner can see → step N+1 is the fix

Never introduce a concept before its gap has been felt. An abstraction that arrives before the pain it solves is the failure this skill exists to prevent. If you cannot name the gap that motivates a step, the step is in the wrong place in the chain — or does not belong.

## Workspace

- `BUILD-PLAN.md` — the target, the gear, the build site, and the ordered chain of steps with progress. The single source of truth for where the build stands. Format: [BUILD-PLAN-FORMAT.md](./BUILD-PLAN-FORMAT.md).
- `./steps/*.html` — one file per step, `0001-<dash-case-name>.html`. Format: [STEP-FORMAT.md](./STEP-FORMAT.md).
- `./reference/*.html` — compressed, printable reference distilled from steps: the final architecture, interface tables, glossary. Steps are read once; reference is read forever.
- `./assets/*` — reusable components shared by every step: stylesheet first, then quiz widgets, diagram helpers, anything a second step would otherwise duplicate. Read this directory before authoring a step, and put anything reusable here instead of inlining it.
- `NOTES.md` — user preferences and working notes.
- `./build/` — the code the learner writes, when the build site is a sandbox in this workspace. On `simplified-paper` / `full-paper` it does not exist.

Author steps and reference in the user's language. Keep code, identifiers, and paths in their original form.

## Step 1 — Intake

Ask the user, in one round:

1. **Target** — what system, and against which source? A real repo to reverse-engineer, a paper, a spec, or your reconstruction from trusted sources. Get the path or URL.
2. **Gear** — read [GEARS.md](./GEARS.md) and present the four gears: `simplified-paper`, `full-paper`, `skeleton`, `full`. The gear decides how much fidelity every later decision buys.
3. **Practice form** — quiz only, write-it-yourself only, or both.
4. **Build site** — where the code lives, for the code gears only. Judge it yourself first and propose: a sandbox `./build/` for anything self-contained; the user's own project when the target only exists inside a host (a UE camera system belongs in their UE project, not a sandbox). Ask only if you genuinely cannot tell.

Then read the target with your tools. Do not plan from parametric memory — read the actual source, and cite it.

Done when `BUILD-PLAN.md` exists with target, gear, practice form, and build site recorded, and the user has confirmed it.

## Step 2 — Teardown

Before building anything, tear the target down into the chain that will rebuild it. This is strict: the full chain is written first, then you build.

Work backwards from the finished system, then order forwards by dependency. For every step in the chain, record: what it adds, what the learner can observe at its end, and the gap that hands off to the next step.

Done when every step in `BUILD-PLAN.md` satisfies all of:

- it names a single addition, small enough to land in one sitting
- its end state is observable — runnable output for a code gear, a worked-through trace for a paper gear
- it depends on nothing a later step introduces
- it names the gap motivating the next step, and the last step's gap is the honest limitation of the finished build

Show the chain to the user and get confirmation before building. A wrong chain wastes every step built on it.

## Step 3 — Build one step

Build exactly the next unbuilt step in the chain. Never build ahead, never bundle two steps into one file.

Each step file follows [STEP-FORMAT.md](./STEP-FORMAT.md) and, per the chosen gear ([GEARS.md](./GEARS.md)), carries: the gap inherited from the previous step, the smallest change that closes it, the observable end state, practice in the chosen form, and the gap it leaves behind.

For a code gear, the learner's code must reach the recorded end state before the step is done — run it, or have the learner run it and report back. A step whose end state was never observed is not done.

Open the step file for the user with a CLI command.

Done when the step file exists, its end state has been observed, and its gap is stated.

## Step 4 — Close the step

- Update the step's status and any chain revision in `BUILD-PLAN.md`. Revising the chain mid-build is normal — record why.
- Distil into `./reference/` anything the learner will look up again: an interface that stabilised, the architecture as it now stands, a new term for the glossary. Once a glossary exists, every later step uses its wording.
- Record in `NOTES.md` any preference the user expressed about pace, depth, or style.

Then return to Step 3 for the next step.

## Practice

Practice is what makes the build stick, and its shape follows the practice form chosen at intake:

- **Quiz** — recall questions on decisions already made, especially *why this and not the obvious alternative*. Every answer option gets the same word count and character length, and identical formatting: no shape clues.
- **Write-it-yourself** — the learner writes the step's code against a stated contract before seeing your version. Give them the interface and the end state to hit; fold your implementation behind a disclosure element so it cannot be read by accident.
- **Both** — contract first, learner writes, folded reference implementation, then quiz on the decisions inside it.

Feedback must be immediate: automatic in the browser for a quiz, a runnable check for written code.

## Grounding

Every claim about the target cites the source — file and line for a repo, section for a paper. When you reconstruct rather than read, say so plainly in the step.

Each step recommends one primary source to read or watch, and reminds the learner that you are their teacher: they should ask you followup questions on anything unclear.

Steps link to each other and to reference documents by HTML anchor, so the chain is navigable in both directions.
