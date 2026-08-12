# STEP-FORMAT.md

A step is one self-contained HTML file in `./steps/`, named `0001-<dash-case-name>.html`. It teaches one brick: the gap it closes, the change that closes it, proof it works, practice, and the gap it leaves.

Beautiful and printable. Tufte, not slide deck: generous margins, readable measure, restrained rules, no decoration that carries no information. Link `../assets/style.css` — never inline what belongs in the shared stylesheet.

## Sections, in order

1. **Where we are** — one paragraph: what the build does today, and the gap inherited from the previous step. Link back to it by anchor. For step 1, this is the empty workspace and why the first brick is first.
2. **The gap** — the concrete case the current build cannot handle, shown rather than asserted: the failing input, the missing behaviour, the trace that dead-ends.
3. **The move** — the smallest change that closes the gap, and *why this and not the obvious alternative*. Cite the source for how the real system does it.
4. **The build** — the change itself. On code gears, exactly what the learner types, at the recorded build site. On paper gears, the illustration code and a trace through it.
5. **Proof** — the observable end state, stated so the learner can check it: the command and its expected output, the passing test, or the trace's final value. On code gears the learner must actually reach this.
6. **Practice** — in the form chosen at intake. See `SKILL.md`.
7. **The next gap** — what this step still cannot do, handing off to the next step. Link forward once that step exists.

## Requirements

- **One brick.** If the file teaches two additions, it is two steps.
- **Cite every claim** about the target: file and line for a repo, section for a paper. Say plainly when you are reconstructing rather than reading.
- **One primary source** to read or watch, the highest-trust one you found.
- **Ask-your-teacher reminder** — a short line telling the learner to bring anything unclear back to the agent.
- **Anchors both ways** — previous step, next step, and any reference document the step distils into.
- **Reference implementations fold.** On write-it-yourself practice, put your version inside a `<details>` element so it cannot be read by accident.
