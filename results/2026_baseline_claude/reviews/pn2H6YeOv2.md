## Summary
PI-CCA reframes catastrophic forgetting in vision-language continual learning (VL-CL) as *alignment-geometry drift* and introduces a compact, replay-free mechanism to preserve it. The method computes a CCA certificate storing the top-$k$ canonical correlations and sketched canonical subspaces from pre-training, then enforces spectral and subspace consistency during adaptation using only mini-batch statistics and EMA. A prompt-invariance loss averages text-encoder projectors over synonym/template perturbations to reduce sensitivity to phrasing. Evaluated on MTIL, X-TAIL, VLCL, and ConStruct-VL, PI-CCA achieves state-of-the-art performance among replay-free methods across all four benchmarks.

---

## Strengths

- **Principled geometric reformulation.** Rather than regularizing proxy signals (logits, similarity matrices, parameter norms), PI-CCA directly targets the whitened cross-covariance invariants that underlie zero-shot transfer. This is a clean conceptual shift with clear motivation: CCA defines the alignment skeleton, so preserving it should preserve zero-shot ability. The distinction from e.g., Mod-X (off-diagonal contrastive matching) or ZSCL (distributional distillation) is genuine and well-articulated.

- **Consistent SOTA across diverse benchmarks.** Tables 1–2 show improvements over all replay-free baselines on MTIL (Avg +1.6 pp over C-CLIP), X-TAIL, VLCL I2T R@1 (+2.5 pp over C-CLIP, even surpassing synthetic-replay GIFT), and ConStruct-VL (FA +1.3 pp, AF −1.2). Gains are multi-metric and multi-benchmark, making cherry-picking unlikely.

- **Thorough ablation study.** Table 3 removes each component individually and reports drops in blue, confirming that both the spectral and subspace terms are necessary (−2.5 and −2.2 MTIL Avg respectively), that covariance EMA is more important than certificate EMA, and that the sorted spectral surrogate is negligibly different from the exact Hungarian pairing. This gives a clear picture of what each design decision contributes.

- **Memory-efficiency and Pareto analysis.** The certificate has $O(hk)$ storage ($h=256$, $k=64$ by default), independent of the model dimensionality. The 3D Pareto sweep (Fig. 2) over $k \in [16,128]$ and $h \in [128, 384]$ identifies a robust ridge and a practical knee, showing the method is insensitive to moderate over/under-specification.

- **Task-order robustness.** Evaluating on 20 random MTIL permutations (Fig. 5) shows narrow interquartile ranges for Avg/Last/AF, directly addressing the concern that any single ordering might favor the method.

- **Prompt-invariance stress test.** Fig. 4 cleanly isolates the contribution of $\mathcal{L}_\text{pi}$ as perturbation strength increases from 0 to 1 for both ID and OOD templates, showing the loss flattens the degradation slope rather than just shifting the intercept.

---

## Weaknesses

### Fatal
None identified.

### Major

1. **Suspicious Pearson/Spearman = 1.00 in Figure 3.** All four scatter panels in Fig. 3 report both Pearson $r \geq 0.99$ and Spearman $\rho = 1.00$. The caption explains the points come from sweeping "certificate size, EMAs, invariance strength, whitening, pairing, LoRA capacity/LR, sketch type." A Spearman rank correlation of exactly 1.00 across this multi-dimensional sweep means there are *zero rank inversions* — every configuration with less drift has strictly higher performance. This is plausible if the method works as claimed, but it is remarkable enough to demand explanation. If each hyperparameter variant enforces *more or less* regularization along a single performance axis, the perfect correlation is an artifact of the experimental design (both drift and accuracy are monotone in regularization strength), not an independent test of the CCA-geometry hypothesis. The paper asserts the trends "support that preserving CCA geometry predicts retention rather than being a coincidental regularizer," but this conclusion requires the sweep to actually produce non-monotone configurations — which perfect rank correlation precludes. This weakens the theoretical narrative around Fig. 3 even if the performance numbers are correct.

2. **Initial certificate calibration data unspecified.** The certificate is initialized from "pre-continual CCA quantities" $\rho_{1:k}^*$, $U_k^*$, $V_k^*$ (Eq. 2), but the paper never specifies what dataset or sample set is used to compute the reference cross-covariance. The choice of calibration set can strongly affect the certificate's quality, and any overlap with the evaluation tasks would constitute a subtle form of data leakage. This is a reproducibility gap that is more important than a formatting detail.

### Minor

1. **Prompt perturbation details.** The paper describes perturbation types as "token-level synonym swap/back-translation/template jitter ratio" with a scalar $s \in [0,1]$ but the main paper does not give the vocabulary size, back-translation languages, or template library used. Given that $\mathcal{L}_\text{pi}$ is a first-class contribution, this level of specification should appear in the main text.

2. **Modest gains over nearest competitor.** On MTIL, the margin over C-CLIP (+1.6 pp Avg) and over DIKI (+1.9 pp) is real but modest. Given that several competing baselines are concurrent 2025 submissions, some of the gap may close under their full configuration — the paper would be strengthened by a protocol-matching analysis confirming equivalent LoRA rank and training epochs.

3. **Missing comparison of step-time overhead vs. baselines.** The Pareto plot in Fig. 2 reports absolute step times for PI-CCA configurations but does not show where baselines fall on the time-vs-performance frontier. It is not possible to judge whether the small accuracy gains come with proportionally small or large computational overhead relative to methods like C-CLIP.

### Trivial
- Inconsistent capitalization of the method name ("PI-CCA" in the title/abstract vs. "Pi-CCA" in tables and figures).

---

## Nice-to-Haves
- A brief experiment studying the behavior when the pre-training calibration set is varied (e.g., random Gaussian embeddings vs. in-domain data) would strengthen confidence in the certificate's robustness.
- Including at least one baseline on the Pareto plot in Fig. 2 would anchor the efficiency story.
- An explanation of why rank correlations are exactly 1.00 (i.e., whether the sweep is inherently 1D in regularization or genuinely multi-dimensional) would clarify the significance of Fig. 3.

---

## Novel Insights
PI-CCA introduces the view that continual forgetting in VLMs is best characterized as drift of the whitened cross-covariance spectrum and canonical subspaces, rather than as drift of logits, similarity matrices, or individual weights. The observation that averaging orthogonal projectors across prompt perturbations eliminates sign/rotation ambiguity within canonical subspaces — removing the need for Procrustes alignment during certificate refresh — is a technically clean trick with potential value beyond this paper's setting. The constant-memory certificate design (storing only $hk$-sized sketches regardless of model dimensionality) is practically important for large VLMs and generalizes beyond the specific CCA application.

---

## Suggestions
- Clarify the calibration dataset used to compute the initial $\rho_{1:k}^*, U_k^*, V_k^*$ and add a sensitivity test over calibration set choices.
- Add a short explanation of the experimental design behind Fig. 3 to address whether the sweep is effectively 1D in regularization or genuinely multi-dimensional, explaining why Spearman = 1.00.
- Report the step-time and memory cost of at least two baselines (e.g., C-CLIP and ZSCL) on the Fig. 2 efficiency plot to enable direct overhead comparison.
- Specify the exact prompt perturbation library and parameters in the main text.

---

## Score and Decision

PI-CCA makes a genuine conceptual contribution by reframing VL-CL forgetting as alignment-geometry drift and operationalizing it via a principled, memory-efficient certificate. The empirical record is solid and multi-faceted. The main reservations — the unexplained perfect rank correlations in Fig. 3 and the unspecified calibration data for certificate initialization — are real but do not invalidate the core results. The performance improvements are consistent and the ablations are informative.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>