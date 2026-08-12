# teach-from-scratch

An agent skill that teaches a system by **building it from zero, one step at a time** — like a hands-on video tutorial, instead of touring a finished codebase.

Inspired by and adapted from [mattpocock/skills — teach](https://github.com/mattpocock/skills/tree/main/skills/productivity/teach). Where `teach` walks through an existing system piece by piece, `teach-from-scratch` reconstructs it from nothing: each step closes the concrete gap the previous step left behind, so the learner always sees *why this brick, why now*.

## How it works

1. **Intake** — the agent asks what you want to build, the gear (fidelity), the practice form, and where the code should live.
2. **Teardown** — before building anything, the target system is torn down into an ordered chain of steps in `BUILD-PLAN.md`. The full chain is written and confirmed first — then you build.
3. **Build one step at a time** — each step is a self-contained HTML file: the gap it closes, the smallest change, proof it works, practice, and the next gap.
4. **Close the step** — progress goes back into `BUILD-PLAN.md`, reusable knowledge is distilled into `reference/`.

## Gears

| Gear | Form | Depth |
| --- | --- | --- |
| `simplified-paper` | HTML only, code as illustration | ~3–5 steps, architectural shape only |
| `full-paper` | HTML only, code as illustration | full fidelity, every decision |
| `skeleton` | real code workspace | walking skeleton: interfaces, wiring, mocks |
| `full` | real code workspace | every step genuinely implemented and runnable |

For code gears, the build site is chosen dynamically: a sandbox `./build/` for self-contained targets, or the user's own project when the target only exists inside a host (e.g. a UE camera system belongs in their UE project).

## Files

- `SKILL.md` — the skill body: intake, teardown, build loop, practice
- `GEARS.md` — the four gears and how to choose
- `BUILD-PLAN-FORMAT.md` — format of the build plan (single source of truth)
- `STEP-FORMAT.md` — format of each step's HTML file

## Usage

Works with agent CLIs that support skills (e.g. Claude Code, Kimi Code). Symlink or copy this directory into your user skills directory (`~/.claude/skills/`, `~/.agents/skills/`, …), then invoke it:

```
/teach-from-scratch What system would you like to build from scratch?
```

## License

MIT
