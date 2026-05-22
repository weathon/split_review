Now let me write the final consolidated review.

## Summary
Pi-CCA introduces a replay-free continual learning framework for vision-language models that preserves the canonical correlation spectrum and subspaces (the "CCA certificate") of the whitened cross-covariance, rather than relying on proxy objectives like logit distillation or similarity matching. The method stores a compact, sketched summary of the pre-trained alignment geometry and constrains adaptation via spectral and subspace-angle regularization losses, all while maintaining constant memory and remaining compatible with parameter-efficient tuning (LoRA). Across MTIL, X-TAIL, VLCL, and ConStruct-VL, Pi-CCA achieves state-of-the-art results among replay-free methods.

## Strengths
- **Novel formulation of forgetting as alignment-geometry drift.** Rather than regularizing proxy signals (logits, similarities, parameters), Pi-CCA directly targets the canonical spectrum and subspaces of the whitened cross-covariance — the very structure underlying CLIP's zero-shot transfer. This is a principled departure from prior VL-CL work and is supported by the correlation evidence linking geometry drift to performance drops (Figure 3) and by the component ablation (Table 3), where removing spectral or subspace terms causes the largest degradation.

- **State-of-the-art results across four VL-CL tracks without replay.** Pi-CCA outperforms all replay-free baselines on MTIL (Avg 76.8 vs. 75.2), X-TAIL (Avg 68.1 vs. 67.4), VLCL (I2T R@1 48.6), and ConStruct-VL (FA 75.2, AF 2.7). It even surpasses GIFT (which uses diffusion-based synthetic replay) on VLCL and ConStruct-VL, demonstrating that geometry-first regularization can substitute for data storage.

- **Replay-free, constant-memory design with practical deployment advantages.** The certificate uses only sketched $h \times k$ projectors and streaming EMAs, independent of dataset size. The Pareto analysis (Figure 2) identifies a broad efficient ridge around $(k, h) = (64, 256)$, confirming robustness to capacity choices. The method is also agnostic to the downstream task loss and compatible with LoRA.

- **Thorough supporting analyses.** The prompt invariance stress test (Figure 4) quantitatively demonstrates the benefit of $\mathcal{L}_{\text{pi}}$ under increasing perturbation strength. The task-order sensitivity analysis (Figure 5, 20 random orders) shows narrow IQRs, confirming robustness to sequence ordering — a known vulnerability in many CL methods.

## Weaknesses

### Major

- **Perfect correlations in the geometry-vs-performance analysis (Figure 3) raise a verification flag.** Two panels report Pearson $r = 1.00$ and Spearman $\rho = 1.00$, and the other two report $r = 0.99$, $\rho = 1.00$. These values would imply zero scatter around the regression line and perfect rank-order monotonicity across multiple perturbation sources (certificate size, EMA rates, invariance strength, whitening, LoRA capacity, etc.). However, the caption describes "realistic scatter," which is incompatible with $r = 1.00$. This discrepancy — whether it is a rounding artifact ($0.9995 \to 1.00$), an issue with how the sweep was conducted (deterministic parameter coupling), or a reporting error — must be clarified. If the correlations are genuinely $1.00$, the claim that "geometry drift predicts retention" is far too strong and the figure does not support it as presented. The authors should provide a version with visible variance (e.g., multiple independent runs, error bars, or jittered points).

- **No standard deviations for the main classification results (Table 1).** Table 2 reports variances for VLCL and ConStruct-VL, but Table 1 (MTIL and X-TAIL) reports only single numbers. Given that the gains over the strongest baselines are modest (e.g., MTIL Avg 76.8 vs. 75.2 for C-CLIP; X-TAIL Avg 68.1 vs. 67.4 for RAIL), it is unclear whether these differences are statistically significant. The paper should report means and standard deviations over multiple seeds (at least 3) for all metrics in Table 1.

### Minor

- **Framing overstates "preservation" of the original pre-trained geometry.** The paper describes the method as "preserving pre-trained cross-modal generalization" (Abstract, Introduction) and treating alignment as "a first-class invariant" (Section 1). However, the certificate itself is updated via a slow EMA (Eq. 13: $\rho^*_{1:k} \leftarrow (1-\alpha)\rho^*_{1:k} + \alpha \hat{\rho}_{1:k}$), meaning it is a moving reference, not a fixed invariant. The paper acknowledges this ("preserve the alignment skeleton while allowing controlled plasticity," Section 3.4) and the ablation shows that $\alpha=0$ (fully frozen certificate) still performs well (MTIL Avg 75.6 vs. 76.8), so this is not a fatal issue. Nevertheless, the "invariant" language is imprecise and should be revised to reflect that the method constrains the *rate* of alignment drift rather than enforcing an absolute invariant.

- **Hyperparameter sensitivity of loss coefficients $\lambda_1, \lambda_2, \lambda_3$ is not reported in the main text.** The total loss (Eq. 7) has three scaling coefficients plus internal parameters ($\xi, \eta, J, M, \alpha, \beta$). The ablations (Table 3) turn entire components on/off but never vary the $\lambda$ coefficients continuously. The paper references Appendix §A.3 for sensitivity experiments, but this section is not accessible. A figure sweeping at least $\lambda_1$ and $\lambda_2$ would increase confidence that reported results do not rely on brittle tuning.

- **The construction of the "diverse anchor prompt set" is underspecified.** Section 3.2 states that the prompt-invariant certificate is constructed from a "diverse anchor prompt set" and that "by default we maintain a global certificate (one per model) constructed from a diverse anchor prompt set," but no details are given about what this set contains, how large it is, whether it overlaps with the training perturbations, or whether the same set is used across all tasks. This matters because if the anchor set is identical to training-time perturbations, the "prompt invariance" may not generalize to unseen prompt styles.

- **Missing baseline: task loss + weight decay / L2 on LoRA parameters.** The paper compares against many strong VL-CL methods but does not include a simple ablation that uses only $\mathcal{L}_{\text{task}}$ plus standard regularization (e.g., weight decay on LoRA parameters). This would help isolate the benefit of the CCA-specific losses from generic regularization effects.

### Trivial

- None worth flagging.

## Nice-to-Haves
- The paper mentions a "time-continual study on TiC-YFCC/RedCaps" in Section 4.1 but does not report any results. Including this would strengthen the claim of alignment robustness over long streams.
- Reporting computational cost on a more modest GPU (e.g., RTX 3090) would increase practical utility beyond the reported A100 numbers.
- Testing task-order sensitivity on tracks beyond MTIL (e.g., VLCL or ConStruct-VL) would broaden the robustness claim.

## Removed Points
- **Certificate EMA as a "fatal flaw" / "structural misrepresentation"** — REMOVED. The paper explicitly states it "preserves the alignment skeleton while allowing controlled plasticity" (Section 3.4). The ablation shows $\alpha = 0$ (frozen certificate) still performs strongly (75.6 vs 76.8), confirming that the method works even with strict preservation. The critic's framing of this as a structural flaw that invalidates the core claim is not supported by the paper.
- **"Missing related works"** — REMOVED per instruction.
- **"Code not released during review"** — REMOVED per instruction (common practice at ICLR, and the paper commits to releasing it).
- **Criticism that baselines "use full backbones or different adapter ranks" without evidence** — REMOVED as speculation not grounded in paper text.
- **"Appendix stripped" complaints about missing proofs/experiments** — REMOVED per instruction (parser artifact, not author error).
- **Formatting/style nitpicks** — REMOVED per instruction.

## Novel Insights
None beyond the paper's own contributions.

## Suggestions
- Clarify the Figure 3 perfect-correlation issue: report whether these are rounded values (e.g., $r = 0.999$ displayed as $1.00$), provide individual data points from multiple independent runs, and discuss whether the sweep's deterministic nature (varying one parameter at a time from a fixed configuration) artificially inflates correlation by eliminating independent noise sources.
- Add standard deviations to Table 1 (MTIL, X-TAIL) over at least 3 random seeds.
- Revise the framing from "preserving invariants" to "constraining alignment drift" or similar, to align with the actual EMA-based certificate mechanism.
- Include a simple $\mathcal{L}_{\text{task}} + \text{weight decay}$ baseline to isolate the CCA losses' contribution.
- Specify the anchor prompt set construction (size, diversity criteria, overlap with training perturbations).
- Provide a sensitivity sweep of the main $\lambda$ coefficients (even a single figure varying $\lambda_1$ while fixing others) to demonstrate robustness.

---

## Score and Decision

### Calibration Report

**Round 1 — Bracketing.** Three queries on VL-CL topics:
- Low band (avg < 3.5): Papers at ~2.0–3.0 (CoFiCL, CoLaP) — rejected or withdrawn; substantially weaker than Pi-CCA in novelty and scope.
- Middle band (3.5–7.5): Compo-ReAlign (6.0, Poster), CoMem (5.0, Poster), ECA (5.0, Reject), KeepLoRA (5.5, Poster), RLAP-CLIP (6.0, Poster).
- High band (7.5+): No relevant VL-CL papers; retrieved anchors from unrelated areas (embodied navigation, text-to-3D), confirming 8+ is not appropriate.

Initial bracket: **5.0 – 7.0**.

**Round 2 — Narrowing.** Two queries within (4.5, 7.5) and (5.5, 7.5). Compared Pi-CCA against Compo-ReAlign (6.0), KeepLoRA (5.5), RLAP-CLIP (6.0), CoMem (5.0), and ECA (5.0).

Pi-CCA is stronger than CoMem and ECA (more principled core idea, broader evaluation across 4 tracks). It is comparable to Compo-ReAlign and RLAP-CLIP in novelty and empirical scope, with a slight edge in evaluation breadth (4 tracks vs. 3) and in the conceptual originality of the CCA certificate. However, the Figure 3 perfect-correlation concern is a real weakness that the comparably-rated papers do not share, preventing a higher score.

**Final score: 6.0** — solid paper with a novel contribution, strong empirical backing, and addressable weaknesses.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>