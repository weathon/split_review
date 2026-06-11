## Summary

This paper presents a large-scale empirical study (3,000+ runs, ~20,000 GPU hours) comparing the optimization dynamics of SSMs (Mamba, Hyena, Mamba2, DeltaNet) and Transformers on multi-query associative recall (MQAR) and copying tasks. The key findings are: (1) SSMs exhibit a critically narrow learning-rate window that prior work missed; (2) SSMs and Transformers have opposing scaling preferences — SSMs benefit from width, Transformers from depth; (3) the 1D convolution is the decisive architectural component enabling 1-layer Mamba to solve MQAR; (4) DeltaNet achieves Transformer-like learning-rate robustness through Householder-based updates that avoid vanishing gradients. These findings collectively demonstrate that optimization stability is a primary differentiator between these model classes, alongside any inherent expressivity differences.

## Strengths

- **Systematic identification of SSM learning-rate brittleness, replicated across two tasks.** Figures 1 and 5 show that both Mamba and Hyena succeed only within a narrow LR window on MQAR and copying, while Transformers maintain performance over 2–3 orders of magnitude of LR. This is convincingly demonstrated to have confounded prior evaluations (Arora et al., 2023; Jelassi et al., 2024).

- **Clean causal ablation isolating the 1D convolution as the decisive component for single-layer MQAR.** Table 2 shows that removing the 1D convolution from a 1-layer Mamba drops accuracy from 99% to 2%, and adding a convolution to a 1-layer Attention raises accuracy from 2% to 99%. This goes beyond correlation to causation and precisely identifies where expressivity differences originate.

- **Demonstration that parameter-matched comparisons require respecting SSM scaling preferences.** Table 1 shows a 150M-parameter Mamba with 24 layers (width 1024) achieves 16% on copying, while a same-parameter Mamba with 12 layers (width 1408) achieves 100%. This crisply shows that scaling along wrong axes (depth for SSMs) produces misleading conclusions — a valuable practical lesson for the field.

- **Identification of DeltaNet as a stability-improving variant with a concrete mechanistic hypothesis.** Figure 7 shows DeltaNet maintaining high accuracy across a wide LR range, unlike Mamba and Mamba2. The hypothesised explanation — Householder-based updates avoid vanishing gradients from diagonal A with decay rates (Trockman et al., 2024) — provides actionable architectural guidance.

## Weaknesses

### Fatal
None.

### Major

1. **Central thesis overshoots what the paper's own evidence supports.** The paper states (line 39): *"Transformers differ from SSMs not in terms of expressive power but mainly because of their optimization dynamics."* Yet Sections 4 and 7 show that a 1-layer Transformer cannot solve MQAR (~2%) while a properly-tuned 1-layer Mamba can (99%). The paper's own ablation traces this to the 1D convolution rather than the core recurrent mechanism — a valuable finding — but this makes the blanket "not in terms of expressive power" claim inaccurate. The paper would be stronger with a more precise thesis: *in multi-layer settings, optimization is the primary differentiator; in 1-layer settings, genuine expressivity differences exist but are attributable to specific architectural components (convolution) rather than core mechanism differences.*

### Minor

1. **Induction-head interpretation for 1-layer Transformers is speculative.** Figure 6 shows a loss bump with no corresponding accuracy gain, which the paper interprets as the Transformer *"attempt[ing] to form induction heads"* — a phenomenon previously documented only in multi-layer models. The paper hedges with "hypothesize" and "attempts," but no mechanistic analysis (attention map visualization, causal tracing) supports the claim. A more conservative interpretation — that the loss bump reflects poor conditioning or saddle-point dynamics — would be equally consistent with the data. This observation is still interesting; the narrative simply overinterprets it.

2. **MQAR-to-language-modeling correlation is asserted, not established.** The paper states (line 9) that these benchmarks are "highly correlated with language modeling performance" and suggests the findings "re-contextualize prior performance evaluations" including large-scale LM comparisons. The correlation is cited (presumably from prior work) but not demonstrated here. The limitation is acknowledged in the conclusion (line 243), but several intermediate claims are stronger than the proxy-task evidence supports. This is a common tension in synthetic-benchmark papers and does not undermine the core findings, but the scope of the claims should be calibrated to the evidence.

### Trivial
None.

## Nice-to-Haves

- Include the specific LR grid values used by Arora et al. (2023) in the main figures' annotations so readers can directly assess the "missed LR" claim without consulting the appendix.
- Show the symmetric experiment for Transformers on the copy task (deep vs. wide Transformer with matched parameter counts) to strengthen the "opposite scaling" narrative symmetrically.

## Removed Points

1. **"Central thesis contradicted by own evidence" (Harsh Critic #1)** — Retained as Major weakness #1 above, but downgraded from "fatal contradiction" since the paper *does* acknowledge "fundamental expressivity issues exist" (line 31) and the ablation (Table 2) precisely characterizes the source of expressivity differences. The issue is a framing overclaim, not a contradiction that invalidates the findings.

2. **"Copy task Table 1 comparison not controlled for parameter count" (Harsh Critic §5)** — Removed. This criticism misunderstands the table: the whole point is to show that matching (layers, width) between Mamba and Attention gives unequal parameter counts (80M vs 150M), and that properly parameter-matched comparisons must scale width, not depth. The paper does exactly this in rows 3–4 of the same table.

3. **"Missing wider-shallower Transformer for symmetry on copy task"** — Moved to Nice-to-Haves. A reasonable suggestion but not a weakness; the paper's claims about opposite scaling are primarily supported by the MQAR experiments.

4. **"Missed LR grid values not in main text"** — Moved to Nice-to-Haves. A minor presentational point.

5. **Strengths demoted or removed:** Strength Finder's claim about "Divergent Single-Layer Dynamics revealing Attention's attempted induction head formation" — retained as an observation but the interpretation is treated as speculative (see Minor weakness #1). The claim about "critical optimization instability" being the paper's central thesis — this is a correct strength but qualified by the overclaim issue above.

## Novel Insights

The reviews surface a key meta-observation: the paper cleanly decomposes the SSM-Transformer performance gap into two distinct phenomena — (a) a genuine expressivity differentiator that is traceable to specific architectural components (the 1D convolution), not the core recurrent-versus-attention distinction; and (b) an optimization brittleness that persists even for expressively capable models and is rooted in the recurrent mechanism's gradient dynamics. This decomposition is more nuanced and practically useful than prior work's binary "SSMs are less expressive" conclusion, and it suggests that the brittleness (unlike the expressivity gap) may be addressable through architectural innovations (as DeltaNet demonstrates).

## Suggestions

1. Recalibrate the central thesis statement at line 39. Replace the blanket "not in terms of expressive power" with a precise characterization: the key difference is optimization in multi-layer settings, while in single-layer settings expressivity differences exist but are mediated by specific architectural components (convolution) rather than core mechanism differences.

2. Tone down the induction-head language. Replace "attempts to form induction heads" with a neutral description of the observed loss bump, noting that its cause is unknown and could relate to optimization geometry rather than induction-head circuitry.

3. Explicitly separate proxy-benchmark claims from language-modeling implications, conditioning the latter as hypotheses for future work as the conclusion already partially does.

## Calibration Anchors

**Round 1 — Bracketing:**
- Strong reject band (avg < 2.5): N581Nje6fH (1.50), a8XwgTZzE0 (2.00), WM5G2NWSYC (2.00) — Current paper is much stronger.
- Weak band (2.5–4.5): YKzGrt3m2g (4.25), YuFUUcSUgx (4.00), 52XG8eexal (4.00) — Current paper is notably stronger.
- Middle band (4.5–6.1): QFgbJOYJSE (5.75, Accept), b5lXUwZiD3 (5.25, Reject), pymXpl4qvi (6.00, Accept) — Current paper is comparable to the upper end.
- Middle band (6.0–7.5): hwSmPOAmhk (7.33, Accept), GeUK3zGreN (6.50, Accept), LY3ukUANko (6.33, Accept) — Current paper is at the lower end of this band.
- Strong accept band (avg > 7.5): Tzh6xAJSll (7.60), d8w0pmvXbZ (8.00), PdaPky8MUn (8.00) — Current paper is weaker.

**Round 2 — Narrowing (bracket ~5.5–6.5):**
- h3wbI8Uk1Z: "RNNs are not Transformers (Yet)" (5.50, Accept) — Current paper is stronger: better-controlled experiments, cleaner ablations, no unfair-comparison confound.
- b5lXUwZiD3: "On Limitation of Transformer for Learning HMMs" (5.25, Reject) — Current paper is noticeably stronger: more comprehensive, more thorough ablations.
- pymXpl4qvi: "Understanding Bottlenecks of SSMs" (6.00, Accept) — Comparable; similar empirical-analysis style, current paper has more actionable ablations.
- LY3ukUANko: "Zoology" (6.33, Accept) — Current paper is slightly weaker due to lack of real LM validation, but has more thorough synthetic ablations.

**Final Score: 6.0** — The paper is a solid, well-executed empirical study with genuine, replicable contributions. Its overclaim at line 39 is a real framing issue, but the underlying findings are robust, and the DeltaNet/convection ablations provide actionable insights. The paper sits between the middle-band and upper-band anchors, comparable to "Understanding Bottlenecks of SSMs" (6.00) and slightly below Zoology (6.33).

## Score and Decision

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>