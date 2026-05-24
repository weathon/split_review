Now I have a thorough understanding of the paper and all the reviews. Let me write the final consolidated review.

---

## Summary

Neon introduces a simple yet powerful post-hoc method for improving pre-trained generative models by negatively extrapolating away from the parameter direction induced by fine-tuning on self-generated synthetic data. The core insight is that mode-seeking inference samplers (common in practice) create a predictable anti-alignment between synthetic-data and real-data population gradients. By reversing this degradation direction through a linear parameter merge, Neon redistributes probability mass from over-represented to under-represented modes, improving recall and overall FID. The method is validated across diffusion, flow matching, autoregressive, and few-step models on CIFAR-10, FFHQ, and ImageNet, achieving state-of-the-art FID of 1.02 on ImageNet-256 (xAR-L) with only 0.36% additional training compute.

## Strengths

- **Rigorous theoretical justification of anti-alignment.** Theorems 1 and 2 (Section 3.1) prove that mode-seeking samplers induce a negative inner product between synthetic and real data population gradients, guaranteeing that negative extrapolation reduces the true data risk. The 2D Gaussian toy example (Figure 2) visually confirms the geometric intuition. The theory covers autoregressive models (temperature, top-k, top-p sampling) and diffusion/flow models (ODE solvers with CFG), connecting the abstract condition to concrete standard practices.

- **Universal empirical gains with minimal compute.** Across four model families and multiple datasets, Neon consistently lowers FID using only self-generated synthetic data and <1% (often <0.5%) additional training compute. The xAR-L result (FID 1.28 → 1.02, 0.36% extra compute) is a new state of the art. Even with as few as 1k synthetic samples, near-optimal improvement is attained for xAR models. The gains are substantial and robust (Figure 5, Figure 7).

- **Mechanism convincingly revealed through precision-recall dynamics.** Figures 4 and 6 demonstrate that Neon systematically trades precision for recall, directly matching the theoretical prediction that it redistributes mass from over-represented to under-represented modes. The joint optimization of extrapolation weight \(w\) and CFG scale \(\gamma\) is shown to expand the achievable precision-recall frontier beyond what either parameter alone can access.

- **Cross-architecture transfer and robustness.** Figure 8 shows that synthetic data from one architecture (flow matching, IMM) can improve a different base model (EDM), with theoretical backing in Appendix B.8. Neon remains effective across a wide range of base model qualities (Figure 9, compensating for 40% reduction in real training data) and is robust to synthetic data quality (Figure 10, near-optimal for CFG scales in [1,3]).

## Weaknesses

### Fatal

None.

### Major

None.

### Minor

- **The "no new real data" claim requires qualification.** Neon requires no new real *training* data, but hyperparameters (\(w\), fine-tuning budget, synthetic dataset size, and for some models \(\gamma\)) are selected via FID on a held-out set of real images (Section 4: "10k/50k samples for hyperparameter search/final evaluation"). In a truly data-scarce deployment, obtaining such a validation set may be non-trivial. The paper should acknowledge this and ideally explore whether data-free proxies (e.g., synthetic-data log-likelihood) could substitute. This does not undermine the method's effectiveness but narrows the scope of the "no real data" narrative.

- **Compute cost of synthetic data generation not explicitly included.** The paper reports Neon's overhead as a fraction of the original training budget (e.g., 0.36% for xAR-L), but it is unclear whether generating the synthetic dataset \(\mathcal{S}\) (up to 750k images for xAR models) is factored into these percentages. For large autoregressive models, this generation cost can be non-trivial. The paper should clarify whether the percentages include generation and, if not, provide the total cost so readers can assess the full resource requirement.

- **Joint optimization with CFG obscures Neon's standalone contribution.** For autoregressive and few-step models, the reported FID gains come from jointly searching over \(w\) and \(\gamma\). The paper acknowledges that co-optimization is crucial and explains the complementary roles (\(w\) boosts recall, \(\gamma\) boosts precision). However, reporting the FID with Neon applied while keeping \(\gamma\) fixed at the base model's optimal value — at least for one representative setting — would cleanly isolate Neon's standalone contribution and preempt concerns about overselling.

### Trivial

- **Figure 4 caption contains a confusing typo.** The caption states: "\(w = -1\) corresponds to the model directly trained on synthetic data, i.e., \(\theta_{\text{Neon}} = \theta_r\). \(w = 0\) corresponds to the base model, i.e., \(\theta_{\text{Neon}} = \theta_r\)." These two statements contradict each other — both cannot equal \(\theta_r\). From Equation (2), \(w = 0\) gives \(\theta_{\text{Neon}} = \theta_r\) (base model) and \(w = -1\) gives \(\theta_{\text{Neon}} = \theta_s\) (the degraded, fine-tuned model). The caption should be corrected.

## Nice-to-Haves

- An ablation over learning-rate scaling factors (e.g., 0.1×, 0.5×, 1× of the original rate) for one model/dataset would demonstrate that the anti-aligned direction is robust and not an artifact of a carefully tuned recipe, improving reproducibility confidence.

- A compact main-text table aggregating key FID improvements and compute overheads across all model families would help readers quickly grasp the consistency of the gains.

- Qualitative image samples along the \(w\) axis (for fixed \(\gamma\)) visually illustrating the precision-recall trade-off would make the story more accessible to a broader audience.

## Removed Points

These points are flagged to be removed; treat them with caution:

- **"Reproducibility of the fine-tuning recipe — hyperparameters relegated to Appendix C (not available)."** Removed per policy: the appendix is stripped by the parser but exists in the original submission. The paper states that fine-tuning uses "the original training recipe at reduced learning rate (see Appendix C for details)." This is a standard and sufficient description for the main text. The concern about missing ablations on sensitivity to learning rate is retained as a Nice-to-Have rather than a weakness.

- **"Untested theoretical assumptions for diffusion/flow models — full proof not available for review."** Removed per policy: appendix proofs are stripped by the parser. The paper states the A-MONO condition explicitly in Footnote 2 and the empirical success of Neon on diffusion/flow models provides experimental validation. Calling this untestable is reviewer-side speculation, not a paper flaw.

- **"The paper would benefit from [missing related works]."** Removed per policy: we do not flag missing related works.

- **Formatting/style nitpicks about presentation, typos, or minor editorial slips** (beyond the Figure 4 caption error, which is a factual confusion worth noting). Removed per policy.

## Novel Insights

The paper reframes model collapse — typically viewed as a pathology — as a structured, exploitable signal. This conceptual shift is significant: rather than fighting degradation with complex workarounds (verifiers, discriminators, guidance), Neon shows that the degradation direction itself contains recoverable information about the model's distributional biases. The connection between inference-time mode-seeking behavior and the anti-alignment of gradients closes a loop between how we *use* models (sampling) and how we *improve* them (training), suggesting that inference samplers can serve as diagnostic tools for uncovering a model's distributional flaws.

## Suggestions

- Add a brief discussion in Section 3.1 on why common samplers (e.g., CFG, top-k) satisfy the mode-seeking property, making the theory self-contained without deferring entirely to the appendix.
- For at least one autoregressive model, report the FID achieved by applying Neon with the base model's original \(\gamma\) held fixed, to cleanly separate Neon's contribution from CFG re-tuning.
- Clarify whether the reported compute percentages include synthetic data generation cost, and if not, provide that cost separately.

## Score and Decision

**Round 1 bracketing:** The queries returned anchors spanning the full quality spectrum. The Neon paper is clearly stronger than the weak band (scores 2.00–3.40), and notably stronger than the middle band's most comparable anchor "Self-Consuming Generative Models Go MAD" (6.67, same research group's earlier work identifying model collapse). Neon is qualitatively closer to the high band anchors like "One Step Diffusion via Shortcut Models" (8.00) and "Lipschitz Singularities in Diffusion Models" (7.50). Initial bracket: **7.0–9.0**.

**Round 2 narrowing:** Within the 7.0–9.0 range, the closest comparators are:
- "On the Stability of Iterative Retraining of Generative Models on their own Data" (6.75): Neon is stronger — it provides both theory and a practical SOTA method.
- "Linear Combination of Saved Checkpoints" (6.00): Neon is substantially stronger — broader method, deeper theory, better results.
- "Lipschitz Singularities in Diffusion Models" (7.50): Comparable quality. Neon has broader empirical scope and a SOTA result; Lipschitz has deeper single-problem analysis.
- "One Step Diffusion via Shortcut Models" (8.00): Most comparable anchor. Both introduce novel, well-motivated methods with strong experiments. Neon has stronger theory (anti-alignment proof) and broader validation (4 model families), while Shortcut Models introduces a fundamentally new training paradigm. Roughly equal quality.
- "Simplifying, Stabilizing and Scaling Continuous-time Consistency Models" (9.20): Neon is clearly below this anchor, which had multiple profound architectural innovations and pushed scaling frontiers.

**Final score: 8.0.** Neon sits squarely alongside "One Step Diffusion via Shortcut Models" (8.00). Its clever, simple idea is well-theorized and extensively validated, with a genuine SOTA result. The remaining concerns (validation data for hyperparameter selection, compute cost accounting, joint optimization isolation) are minor and addressable; none threaten the core contribution.

**All anchors retrieved:**

| Anchor ID | Avg Score | Round | Comparison to Neon |
|-----------|-----------|-------|---------------------|
| 8TbqoP3Rjg | 2.00 | R1 (low) | Much weaker — limited novelty, reject |
| TJHB4ySVZM | 3.40 | R1 (low) | Much weaker — poor presentation, reject |
| 2LhCPowI6i | 2.33 | R1 (low) | Much weaker |
| dIaykjbiiL | 2.50 | R1 (low) | Much weaker |
| QKqWnNkwPL | 3.00 | R1 (low) | Much weaker |
| Xr5iINA3zU | 5.75 | R1 (mid) | Weaker — incremental, limited novelty |
| P5UETqZXqT | 5.75 | R1 (mid) | Weaker |
| oClr2P7V0T | 4.25 | R1 (mid) | Weaker |
| ShjMHfmPs0 | 6.67 | R1 (mid) | Weaker — same group's earlier MAD paper |
| 0py3h7pops | 5.50 | R1 (mid) | Weaker |
| et5l9qPUhm | 8.00 | R1 (high) | Comparable — theory paper on collapse |
| OlzB6LnXcS | 8.00 | R1+R2 (high) | **Closest match** — similar quality |
| SctfBCLmWo | 8.00 | R1 (high) | Different domain (dataset bias) |
| LyJi5ugyJx | 9.20 | R1 (high) | Stronger — major architectural innovations |
| DJSZGGZYVi | 9.00 | R1 (high) | Stronger |
| JORAfH2xFd | 6.75 | R2 | Weaker — limited empirical validation |
| QowsEic1sc | 6.00 | R2 | Weaker — narrower scope, lower impact |
| 6O3Q6AFUTu | 8.00 | R2 | Comparable |
| 2o58Mbqkd2 | 7.33 | R2 | Slightly weaker |
| WNkW0cOwiz | 7.50 | R2 | Comparable |
| vi3DjUhFVm | 7.25 | R2 | Slightly weaker |
| 1PXEY7ofFX | 7.20 | R2 | Slightly weaker |
| eaTqsptDPL | 5.75 | R2 | Much weaker |

Bracket: 7.0–9.0 (R1) → narrowed to 8.0 based on comparison with Shortcut Models (8.00) and Lipschitz Singularities (7.50).

MY FINAL SCORE: <score>8.0</score>
MY FINAL DECISION: <decision>Accept</decision>