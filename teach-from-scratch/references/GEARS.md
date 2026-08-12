# Gears

The gear is chosen at intake and governs every later decision: how many steps the chain has, how deep each one goes, and whether the learner writes code at all. Record it in `BUILD-PLAN.md`.

Two families:

- **Paper gears** build on the page. No project, no toolchain. Code appears as illustration only — snippets the learner reads and traces, never runs. The learner ends with a mental model of how the system is assembled.
- **Code gears** build in a real workspace. The learner types code and observes it work. The build site is decided at intake: a sandbox `./build/`, or the user's own project when the target only lives inside a host.

## `simplified-paper`

The shortest honest path from zero to a working mental model. Roughly 3–5 steps, each one a major architectural move. Skip every detail that is not load-bearing for the shape of the system.

- Illustration code: pseudocode or heavily elided real code
- End state per step: a worked-through trace, or a diagram the learner can redraw from memory
- Use when the learner wants to see *how a system like this gets built*, not build one

## `full-paper`

The same page-only form, at full fidelity. Every non-trivial decision gets its own step and its own gap. Nothing structural is elided.

- Illustration code: real code, cited to file and line
- End state per step: a trace the learner can follow line by line
- Use when the learner wants complete understanding but has no intention of writing the code

## `skeleton`

A real workspace, built as an end-to-end walking skeleton: interfaces, wiring, and mocks. Every layer exists and the whole thing runs; the depth behind each interface is stubbed.

- The learner writes types, signatures, and wiring — mocks stand in for real implementations
- End state per step: it runs, and the seam the step added is visible in the output
- Use when the learner cares about architecture and data flow, and treats the internals as replaceable

## `full`

A real workspace where every step is genuinely implemented, runnable, and — where the host supports it — tested. The finest gear, and the longest chain.

- The learner writes working code, mocks only at true external boundaries
- End state per step: it runs and produces the real behaviour; a passing test where the project has tests
- Use when the learner wants the working system, not a model of it

## Choosing

Ask; do not infer silently. When the user is unsure, ask what they will do with the knowledge — model-building points at a paper gear, shipping something points at a code gear. Gears can be upgraded mid-build: keep the finished steps and re-tear-down the remaining chain at the new gear, recording the change in `BUILD-PLAN.md`.
