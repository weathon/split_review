- Decision: Reject
- Avg Score: 4.25
- Scores: 3, 3, 5, 6
I now have all the verification I need. Let me construct the final consolidated review.

---

## Summary

CrossNovo proposes a framework that distills bidirectional latent knowledge from a Non-Autoregressive Transformer (NAT) decoder into an Autoregressive Transformer (AT) decoder for de novo peptide sequencing. The method uses joint training with a shared encoder, importance-annealed multitask loss, a cross-decoder attention module, and gradient blocking to prevent the AT loss from corrupting the NAT decoder. Experiments on two 9-species benchmarks report improvements over both AT and NAT baselines (e.g., AA recall 0.785→0.811, peptide recall 0.621→0.654 on the v1 dataset).

## Strengths

- **Novel cross-decoder attention with gradient blocking**: The paper introduces a cross-attention mechanism (Section 3.4, Eq. for **h**ₜ^update) that allows the AT decoder to attend to the NAT decoder's final-layer embeddings while blocking gradients to prevent the AT loss from corrupting the NAT's CTC-optimized representations. This is a specific architectural contribution that directly enables the claimed knowledge transfer direction.

- **Principled analysis of distillation direction**: Section 3.5 provides a clear argument for why distilling NAT→AT is safe while the reverse direction would leak ground-truth information through the AT decoder's causal mask. This demonstrates careful consideration of information flow and data leakage — a point that is often overlooked in distillation papers.

- **Consistent SOTA results across two benchmarks**: On 9-species-v1, CrossNovo achieves average AA recall 0.811 and peptide recall 0.654, surpassing the best prior AR model (0.785/0.621) and remaining competitive with NAT baselines. On the more challenging 9-species-v2, it achieves peptide recall 0.786 and precision 0.906, the highest reported. Per-species breakdowns (Section 4.3) confirm the model combines AT strengths on Human/Mouse with NAT strengths on other species, consistent with the paper's central claim.

- **Importance annealing schedule**: The dynamic weighting λ_AT = i/T (Section 3.3) that transitions from NAT-dominated to AT-dominated optimization is a key differentiator from standard multitask learning. It is well-motivated: let the bidirectional NAT representations mature first, then let the AT gradually take over.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

- **No statistical significance reporting**: The paper reports all results as single-point estimates without standard deviations, confidence intervals, or multiple-run statistics. For improvements of the magnitude reported (e.g., AA recall +0.026, peptide recall +0.033 on v1), it is not possible to assess robustness to seed variation or optimization stochasticity. Adding variance estimates over 3–5 runs would meaningfully strengthen the evidence. While single-run evaluation is common in this field for large models, the paper should acknowledge this limitation and ideally provide some measure of variance.

- **Source of baseline numbers not clarified**: The paper states "we followed previous work…and utilized the same training set" (Section 4.1) and lists baselines in Section 4.2, but does not explicitly state whether baseline performance numbers were taken from published papers or reproduced in the same environment. If taken from published results, differences in data splits or preprocessing could affect fairness. A brief clarification would resolve this.

- **No limitations discussion**: The paper ends without a limitations section. Several points would be natural to mention: the fixed maximum peptide length of 40 inherited from the NAT decoder, reliance on MassIVE-KB training data (generalizability to different instrument types or sample preparations is untested), and the computational overhead of the two-decoder architecture. Adding a brief limitations paragraph is standard practice and would improve the paper's completeness.

### Trivial

- **Ablation summary not visible in main text**: The Introduction and Conclusion reference "comprehensive ablation studies," but no ablation table appears in the main text (these likely reside in the appendix, which was stripped by the parser). Including a concise main-text summary table isolating the contributions of joint training, cross-decoder attention, and gradient blocking would make the paper self-contained for readers who do not consult the appendix.

## Nice-to-Haves

- **Inference efficiency comparison**: Since NAT decoders are typically fast at inference and CrossNovo uses an AT decoder for final generation, reporting relative runtime or FLOPs would help readers understand the practical trade-off introduced by the distillation framework.
- **Ablation of the positional encoding offset**: The paper's choice to place NAT features at positions 1–40 and spectrum features starting at 41 (Section 3.4) follows logically from the fixed NAT length, so this is not a weakness. However, a brief ablation (e.g., swapping the offset or using separate positional encodings without offset) would confirm the design is not brittle.

## Removed Points

These points were flagged for removal; treat with caution.

1. **Positional encoding offset of 41 is "ad hoc" / not justified** — REMOVED. The paper clearly explains (line 105) that NAT features occupy positions 1–40 (following the fixed NAT length from prior work) and spectrum features start at 41 to separate the two information sources. This follows straightforwardly from the design and does not need additional justification.

2. **Downstream antibody data not shown in main text** — REMOVED. The Introduction mentions this (line 15), and results likely appear in the appendix, which was stripped by the parser. Per the hard rules, missing appendix content is not a valid weakness.

3. **Inference speed / efficiency not reported** — DEMOTED to Nice-to-Have. This is not a core claim of the paper and is a standard request, not a weakness.

4. **Strength Finder generic/superficial claims** — None of the identified strengths were generic; all were specific and evidence-backed. No strengths removed.

5. **Ablation studies "not accessible in the main text" as a critical issue** — DEMOTED to Trivial. The studies exist in the full submission (appendix); the criticism that a main-text summary table is missing is valid but does not rise to a critical issue, since the paper acknowledges the ablations exist.

## Novel Insights

None beyond the paper's own contributions. The reviews surface standard concerns about statistical rigor and presentation completeness but do not identify any missed conceptual angle or methodological blind spot that would reshape the paper's interpretation.

## Suggestions

1. **Add variance estimates** for the main results on both benchmarks. Even reporting results over 3 random seeds with mean ± std would substantially improve the evidential foundation.
2. **Include a compact ablation table in the main text** (or a dedicated subsection) showing the contribution of each component: (a) AT-only baseline, (b) joint training only, (c) joint training + cross-decoder attention, (d) full model with gradient blocking. This directly addresses whether the cross-decoder module — the paper's most novel component — provides additive benefit beyond joint training alone.
3. **Clarify whether baseline numbers are reproduced or cited** from prior publications. A single sentence in Section 4.2 would suffice.
4. **Add a limitations paragraph** covering model length constraints, training data coverage, and computational cost.
