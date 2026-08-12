# BUILD-PLAN.md Format

`BUILD-PLAN.md` lives at the workspace root. It is the single source of truth for what is being built, under which gear, where, and how far the build has got.

## Template

```md
# Build Plan: {System}

## Target
{What is being built, in one or two sentences — the finished thing the chain arrives at.}

**Source:** {repo path / paper / URL, or "reconstructed" with the resources used}
**Gear:** {simplified-paper | full-paper | skeleton | full}
**Practice:** {quiz | write-it-yourself | both}
**Build site:** {./build/ | absolute path in the user's project | n/a for paper gears}

## Why
{The learner's reason for building this. One to three sentences, concrete. Everything in the chain traces back here.}

## Out of scope
- {What the finished build deliberately will not do — this bounds the chain}

## Chain

### 1. {Name} — {done | building | pending}
- **Adds:** {the single thing this step introduces}
- **Observable:** {what the learner sees at the end — output, trace, passing test}
- **Gap:** {what it still cannot do, which motivates step 2}
- **Step file:** [0001-{name}.html](./steps/0001-{name}.html)

### 2. {Name} — pending
- **Adds:** …
- **Observable:** …
- **Gap:** …

## Revisions
- {date}: {what changed in the chain and why}
```

## Rules

- **The chain is written in full before building.** Teardown precedes construction; a chain discovered step-by-step drifts.
- **Every step names its gap.** A step with no gap is either the last step or misplaced. The last step's gap is the honest limitation of the finished build.
- **No forward dependencies.** If a step needs something a later step introduces, the order is wrong.
- **Revise openly.** When reality forces a chain change, edit the chain and append to `Revisions` — never silently rewrite history.
- **Status lives here only.** Do not track progress in step files; that would split the source of truth.
