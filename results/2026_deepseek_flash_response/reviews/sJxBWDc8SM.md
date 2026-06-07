Now I have all the calibration context I need. Let me write the final review.

## Summary

This paper empirically investigates why modern recurrent models (Mamba, Hyena, Mamba2, DeltaNet) underperform Transformers on associative recall and copying tasks. The core finding is that SSMs exhibit a critical optimization instability — they succeed only within an extremely narrow learning-rate window — while Transformers are robust across orders of magnitude. Through careful tuning and controlled ablations, the paper shows this instability has systematically confounded prior expressivity comparisons, and identifies the 1D convolution as the architectural feature enabling 1-layer SSM expressivity. The paper is an empirical analysis, not a new method.

## Strengths

- **Systematic demonstration that optimization instability confounds prior expressivity conclusions.** Figure 1 is the paper's strongest contribution: it cleanly shows Mamba and Hyena achieve high accuracy only within a narrow LR window, while Attention maintains near-perfect accuracy across ~2 orders of magnitude. The dashed vertical lines marking the grid used by Arora et al. (2023) fall outside these windows, providing concrete evidence that prior work's conclusions were artifacts of suboptimal tuning. This finding is practically important for the community.

- **Controlled ablation isolating the 1D convolution as the mechanistic driver of 1-layer expressivity.** Table 2 presents a clean causal decomposition: removing conv1d from 1-layer Mamba collapses accuracy from 99% to 2%, and conversely adding convolution to 1-layer Attention raises accuracy to 99%. This controlled swap experiment cleanly identifies the architectural component that bridges the expressivity gap between the two model classes.

- **Cross-task validation of all main findings.** The narrow-LR-window and width-vs-depth scaling findings replicate on the copying task (Figure 5, Table 1) in addition to MQAR, demonstrating the results are not dataset-specific. Table 1's demonstration that a deeper-but-narrower Mamba (24×1024, 150M params) fails at 16% while a shallower-but-wider Mamba (12×1408, same params) succeeds at 100% is a practically useful scaling insight.

- **DeltaNet as an existence proof that SSM stability can match Transformers.** Figure 7 shows DeltaNet maintaining high accuracy across a broad LR range (approximately 1e-05 to 0.3) at both tested dimensions, while Mamba and Mamba2 show sharp peaks. This demonstrates the architectural feasibility of stable SSM training.

## Weaknesses

### Fatal

None.

### Major

- **Framing mismatch between thesis scope and evidence scope.** The paper's central thesis states: "*Transformers differ from SSMs not in terms of expressive power but mainly because of their optimization dynamics*" (line 39). This is a claim about expressive power writ large. The evidence, however, is confined to two synthetic benchmarks (MQAR and copying). While these are well-motivated and correlated with language modeling, the thesis as stated goes beyond what the experiments can support. A claim such as "on recall and copying benchmarks, prior expressivity conclusions are confounded by optimization instability" would be fully supported and equally significant. The conclusion (Section 8) partially acknowledges this, but the abstract and introduction frame the contribution in broader terms that the evidence does not fully warrant. This mismatch should be resolved by narrowing the claim.

### Minor

- **Gradient mechanism for instability is hypothesized but untested.** Section 7 attributes the narrow LR window to gradient dynamics — vanishing gradients from the decay rate in Mamba's A_k matrices vs. Householder-based mixing in DeltaNet. This is a plausible hypothesis, but the paper provides no gradient-level evidence: no gradient norm measurements, no spectral analysis of the Jacobian, no comparison of gradient flows across architectures. Given that the paper's central contribution is about *optimization* instability, the absence of any direct gradient analysis is a noticeable gap in the explanatory chain. This does not invalidate the empirical finding, but it limits the paper's ability to explain *why* the instability exists.

- **Induction-head interpretation in Section 6 is based on thin evidence.** The paper observes a loss bump during 1-layer Attention training and states it "resembles the formation of an induction head circuit" (Section 6). The evidence is a single training curve (Figure 6). No attention-pattern visualization, head analysis, or probing is performed. The paper uses hedging language ("resembles," "we hypothesize"), but the claim that the model "attempts to form induction heads" goes beyond what a loss-curve bump alone supports. This interpretation should either be substantiated with mechanistic analysis or removed in favor of a purely descriptive observation.

- **DeltaNet comparison is limited in scale.** DeltaNet results (Figure 7) are presented only for model dimensions up to 256, explicitly because "that was the maximum size supported by the DeltaNet implementation" (Section 7). Mamba is tested at dimensions up to 2048. The claim of "Transformer-level robustness" for DeltaNet would be strengthened by results at the scales where Transformers and Mamba were tested. The paper is transparent about this limitation, but it weakens the comparison.

### Trivial

- No statistical quantification of LR window width (e.g., the range over which each model achieves ≥90% of peak accuracy) is provided, which would make the "narrow window" characterization more precise and interpretable.
- The paper does not explore whether 1-layer Transformers could succeed with a different optimizer or schedule, which is a natural question given the paper's own thesis.

## Nice-to-Haves

- Gradient-level analysis (gradient norms, Jacobian spectral properties) to directly test the hypothesized mechanism behind the narrow LR window, transforming the empirical observation into mechanistic understanding.
- DeltaNet experiments at larger dimensions (512+) to confirm the "Transformer-level robustness" claim at comparable scales.
- Optimizer sensitivity analysis (AdamW, SGD with momentum) to determine whether the instability is inherent to the model class or an interaction with Adam.
- A quantitative metric for LR window width (e.g., the range of LRs over which accuracy ≥ 90% of peak) to enable precise comparisons.

## Removed Points

These points were flagged by the reviewers but removed after verification against the paper:

- *"Baseline fairness in Table 1: Mamba 12×1024 has 80M params while same-width Attention has 150M."* — The paper already provides the parameter-matched fair comparison (Mamba 12×1408 = 150M params, which succeeds at 100%). The parameter asymmetry is a structural property of SSMs, not a comparison flaw. The paper correctly shows both the unmatched and matched comparisons.
- *Various formatting, typos, and presentation nitpicks.* — These are parser artifacts from the PDF extraction, not author errors.
- *Generic concerns about missing related works.* — Cannot be verified; rule forbids inclusion.
- *Speculative criticisms about "confounders" or "proxy measurements" without concrete anchors in the paper.* — Removed per filtering discipline.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. **Reframe the central thesis** to match the evidence: "on recall and copying tasks, optimization instability confounds prior expressivity conclusions" rather than the broader claim about "expressive power."
2. **Add gradient-level analysis** (gradient norms, or spectral properties of the Jacobian across LRs) in Section 7 to support the hypothesized mechanism. This would significantly strengthen the paper's explanatory contribution.
3. **Either substantiate or remove the induction-head claim.** Provide attention-pattern visualizations or head analysis for the 1-layer Transformer, or replace the interpretation with a purely descriptive "loss bump" observation.
4. **Expand DeltaNet experiments** to dimensions ≥512 at sequence length 512 to demonstrate "Transformer-level robustness" at comparable scales.
5. **Report quantitative LR window widths** (e.g., range over which accuracy ≥ 90% of peak) as a simple addition to Figures 1, 5, and 7.

## Calibration

**Round 1 (Bracketing):** Weak anchors (avg < 3.5): papers with avg scores 2.50–3.00 — clearly worse than this paper. Middle anchors (3.5–7.5): 5.75–6.67 — comparable quality. Strong anchors (> 7.5): 7.60–8.00 — clearly stronger papers with more thorough analysis.

**Round 2 (Narrowing):** Queried within (5.0, 7.0) and (6.5, 8.0). Anchors at 5.33 (StableSSM, Reject — weaker experiments, theory-practice disconnect), 6.0 (From generalization analysis to optimization designs, Reject — cleaner theory but marginal experiments), 6.25 (Optimization Landscape of SGD, Accept — comparable style), 6.67 (Autocorrelation Matters for SSMs, Accept — solid but with similar synthetic limitations), 7.33–7.50 (stronger papers with deeper analysis or theory).

**Final score:** The paper sits at the lower end of the middle bracket. Its core empirical finding (Figure 1) is striking and important, but the framing overreach, absence of gradient-level analysis, and thin induction-head evidence prevent it from reaching the level of the 7+ anchors. The paper is comparable to the 6.0–6.25 anchors in overall rigor and contribution.

**Anchors used (all rounds):**
| Path | Avg Score | Round | Comparison |
|---|---|---|---|
| BUpdp5gETF.md | 2.50 | R1 | Much weaker |
| q541p2YLt2.md | 2.50 | R1 | Much weaker |
| 7eYmijcuqO.md | 3.00 | R1 | Much weaker |
| I1484gDBr4.md | 2.50 | R1 | Much weaker |
| EGjvMcKrrl.md | 6.00 | R1/R2 | Comparable; my paper has cleaner experiments |
| DjeQ39QoLQ.md | 6.50 | R1 | Stronger theory component |
| pymXpl4qvi.md | 6.00 | R1 | Comparable quality and scope |
| QFgbJOYJSE.md | 5.75 | R1 | Weaker empirical validation |
| d8w0pmvXbZ.md | 8.00 | R1 | Much stronger; includes gradient analysis |
| GRMfXcAAFh.md | 8.00 | R1 | Stronger; proposes new method |
| PdaPky8MUn.md | 8.00 | R1 | Stronger; more comprehensive experiments |
| Tzh6xAJSll.md | 7.60 | R1 | Stronger; precise theoretical scaling laws |
| iEfdvDTcZg.md | 6.25 | R2 | Comparable |
| sZJNkorXMk.md | 6.67 | R2 | Stronger theoretical grounding |
| BwG8hwohU4.md | 5.33 | R2 | Weaker; theory-experiment disconnect |
| hwSmPOAmhk.md | 7.33 | R2 | Stronger; theory backed by experiments |
| DhdqML3FdM.md | 7.00 | R2 | Stronger theoretical depth |
| qtTIP5Gjc5.md | 7.50 | R2 | Stronger theoretical analysis |

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>