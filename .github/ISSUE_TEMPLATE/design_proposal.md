---
name: Design proposal
about: Larger API or behavior change (RFC-lite); use after a quick chat in Discussions if unsure
labels: enhancement
---

## Motivation

What problem does this solve for users? Link related issues if any.

## Proposed API or behavior

Sketch signatures, defaults, and how this interacts with plain Matplotlib.

## Style contract checklist

SignalPlot stays small and honest. Check all that apply to this proposal:

- [ ] Stays close to Matplotlib primitives (no new plotting framework).
- [ ] Respects the README palette and spine rules (or documents a deliberate, narrow exception).
- [ ] Avoids misleading scales (e.g. bar baselines, axis limits).
- [ ] Keeps dependencies unchanged unless there is strong justification.

## Alternatives

What could users do today with SignalPlot + Matplotlib alone?

## Migration

If this is breaking, how should existing code change?
