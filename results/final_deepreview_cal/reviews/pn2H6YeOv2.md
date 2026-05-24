Now I have all the information I need. Let me produce the consolidated review.

---

## Summary

This paper proposes PI-CCA, a replay-free continual learning framework for vision-language models that reframes forgetting as drift of the canonical correlation analysis (CCA) alignment geometry. The key idea is to maintain a compact "certificate" of the top-k canonical spectrum and subspaces, then constrain new-task adaptation to preserve these invariants via spectral, subspace-angle, and prompt-invariance losses. Across MTIL, X-TAIL, VLCL, and ConStruct-VL benchmarks, PI-CCA achieves state-of-the-art results among replay-free methods while using only mini-batch statistics and constant memory.

## Strengths

- **Strong, consistent empirical performance across four benchmarks**: Tables 1 and 2 show PI-CCA achieves best or near-best results on all tracks (e.g., MTIL Avg 76.8, X-TAIL Avg 68.1, VLCL I2T R@1 48.6, ConStruct-VL FA 75.2 / AF 2.7), outperforming strong baselines including C-CLIP, DIKI, MG-CLIP, and RAIL, and even surpassing the synthetic-replay method GIFT without storing or generating data.

- **Well-designed component ablation validates the CCA-specific design**: Table 3 demonstrates that removing the spectral term (λ₁=0) or subspace term (λ₂=0) causes the largest performance drops (~2.2–2.7 pp on MTIL, ~2.3–2.7 on VLCL R@1), confirming that both the canonical correlation spectrum and subspace directions are necessary contributors beyond the base task loss.

- **Prompt-invariance mechanism provides genuine robustness to phrasing shifts**: Figure 4 shows that PI-CCA with L_pi maintains flatter degradation curves under increasing prompt perturbation strength s, with +2.44 pp R@1 improvement (ID) and +2.51 pp (OOD) at s=1.0 compared to the no-invariance variant, demonstrating that the projector-averaging approach meaningfully reduces sensitivity to prompt/style variation.

- **Task-order insensitivity indicates reliable behavior**: Figure 5 reports narrow IQRs (≤0.8 pp) across 20 random MTIL task orders for Avg, Last accuracy, and AF, establishing that the method's performance is not an artifact of favorable task ordering.

- **Efficiency analysis supports practicality**: Figure 2 provides a Pareto analysis of certificate capacity (k, h) versus memory and step time, identifying a broad efficient ridge (k ∈ [48,96], h ∈ [192,320]) where performance remains high with modest resource costs.

## Weaknesses

### Fatal

None. The core claims — that explicitly constraining CCA geometry achieves strong replay-free VL-CL performance — are supported by the main results and ablations.

### Major

- **The geometry–performance correlation analysis (Figure 3) reports implausibly perfect correlation coefficients (Pearson r = 1.00, Spearman ρ = 1.00 in two of four panels)**: The data points are generated from within-method ablations (certificate size, EMA rates, invariance strength, etc.) where drift and performance drop are both computed relative to a single reference configuration. While this setup can produce strong correlations, r = 1.00 over tens of real experimental data points is not credible and signals either (a) a hidden deterministic relationship in the measurement protocol that inflates the coefficient, or (b) a very small number of data points. Either way, the reported coefficients overstate the strength of evidence that drift predicts generalization, and the analysis does not distinguish between a causal link and a self-fulfilling measurement. This weakens the paper's central narrative that geometry drift is a reliable *predictor* of downstream performance.

- **Classification-track results (MTIL, X-TAIL, Table 1) lack any measure of uncertainty**: Unlike Table 2 (VLCL and ConStruct-VL, which report mean ± std), Table 1 provides only point estimates without standard deviations, confidence intervals, or indication of the number of seeds. The margins over the strongest baselines are modest (1.6 pp on MTIL Avg over C-CLIP; 0.7 pp on X-TAIL Last over RAIL), and without variance estimates it is impossible to assess whether these differences are meaningful or within noise. This is a standard expectation for empirical ML papers and its absence on the primary classification table weakens the SOTA claim.

### Minor

- **The prompt perturbation strength s is defined only qualitatively**: The paper describes s ∈ [0,1] as "token-level synonym swap/back-translation/template jitter ratio," but does not specify the exact procedure mapping s to perturbation magnitude (e.g., probability of swapping a given token, number of back-translation rounds). This limits reproducibility of the prompt-invariance stress test and makes it hard to interpret what s = 0.6 corresponds to in practice.

- **Initial certificate construction detail is deferred**: The description "constructed from a diverse anchor prompt set" for the pre-continual CCA certificate is stated in the main text but the specification of what constitutes "diverse" and how many anchor prompts are used is left to the appendix. While this is a reasonable scope choice, the conceptual clarity of the method would benefit from at least a one-sentence summary of the construction procedure in the main body.

### Trivial

- The 3D Pareto plot (Figure 2a) encodes forgetting only as color, making the AF dimension difficult to read precisely; the 2D view (Figure 2b) partially compensates but only for the Avg vs. memory trade-off.

## Nice-to-Haves

- A comparison against a simple parameter-space or feature-space L2 regularizer (e.g., weight decay toward pre-trained LoRA weights) would help isolate whether the CCA-specific terms provide gains beyond what a generic anti-drift regularizer achieves. The existing ablations (Table 3) show that each CCA term matters *within* PI-CCA, but do not rule out that simpler regularization could achieve comparable results.
- Reporting drift metrics on a held-out validation set (rather than on the same data used to compute the certificate) would strengthen the claim that alignment geometry drift predicts *generalization* rather than merely tracking within-method configuration changes.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **"Baselines may not be fair (LoRA vs. full fine-tuning)"** — REMOVED. The paper states it uses LoRA for its own method. Many cited baselines (C-CLIP, DIKI, LADA) are themselves parameter-efficient methods that use LoRA or adapters. There is no evidence in the paper that an unfair comparison exists; this is speculative. Furthermore, if the asymmetry favored the baseline (full fine-tuning has more capacity), that would only strengthen PI-CCA's case.

- **"Missing hyperparameter values (λ₁, λ₂, λ₃, α, β, M)"** — REMOVED. The paper explicitly states these are reported in Appendix A.1 and A.2. The appendix was stripped by the parser but exists in the original submission.

- **"Theory section missing from main text"** — REMOVED. The paper references §A.4 for theoretical explanation and a Theory section in the appendix. The appendix was stripped. This is not a paper flaw.

- **"No discussion of how initial pre-continual CCA certificate is computed when original pre-training data is unavailable"** — partially valid concern about underspecification, but the core idea (diverse anchor prompt set) is conceptually clear. The appendix likely contains details. Moved remaining concern to Minor.

- **"Method feasibility not examined — wall-clock time, sensitivity to batch size not analyzed"** — partially REMOVED. Figure 2 already reports peak memory (GB) and per-step wall-clock time (ms) on A100-80GB across certificate configurations. The paper also mentions sensitivity experiments in Appendix A.3. The batch-size sensitivity analysis demand is a research-direction ask, not a weakness.

- **Several harsh-critic points about reproducibility (undisclosed power-iteration steps, Newton-Schulz details)** — REMOVED per instructions: these are appendix-deferred or implementation details impractical for main-text inclusion.

- **Strength: "State-of-the-art replay-free performance" claimed as the strongest evidence** — KEPT but qualified. The improvements are genuine and consistent but modest on classification tracks, and the missing error bars on Table 1 warrant caution.

- **Strength: "The paper addressed an important problem"** — REMOVED as generic/superficial. This is true of many papers and carries no specific evaluative weight.

## Novel Insights

The paper's most valuable conceptual contribution is reframing catastrophic forgetting in VL-CL as *alignment-geometry drift* rather than proxy-signal mismatch. While representation similarity metrics (CKA, SVCCA) have been used diagnostically in CL, PI-CCA is the first to operationalize CCA invariants (spectrum + subspace) as *optimization targets* during continual adaptation. The idea of averaging sketched projectors over prompt perturbations to obtain a rotation-invariant certificate without Procrustes alignment is a neat technical insight that elegantly handles sign/rotation ambiguity in the canonical subspace.

## Suggestions

- Re-compute Figure 3 correlations on a held-out validation set rather than on the same configurations used for certificate estimation; report the actual number of data points and verify the correlation coefficients are credible.
- Add standard deviations to Table 1 (MTIL and X-TAIL) from multiple seeds, matching the reporting standard already used in Table 2.
- Provide a concise operational definition of the perturbation strength s (e.g., "s is the probability that each token is independently perturbed via synonym replacement") so the stress test is interpretable and reproducible without consulting the appendix.
- Consider including the simple L2-regularizer sanity check in a revision to preempt questions about whether the CCA machinery is strictly necessary.

## Score and Decision

**Anchor comparison:**

| Anchor | Avg Score | Round | Comparison |
|--------|-----------|-------|------------|
| sb7qHFYwBc (C-CLIP) | 6.50 | R1 | PI-CCA is more methodologically novel and directly outperforms C-CLIP; evaluation breadth is similar. Slightly weaker on presentation rigor (missing std, implausible correlation). |
| k9NYnsC4Mq (PROOF) | 5.67 | R1 | PI-CCA is clearly stronger: more novel geometric framing, broader benchmarks, more thorough analysis, and does not suffer from the inference-mismatch critique leveled at PROOF. |
| TLADT8Wrhn (TiC-CLIP) | 6.25 | R2 | TiC-CLIP is a benchmark contribution with simpler methods. PI-CCA has a stronger methodological contribution but TiC-CLIP's evaluation is more carefully executed. Comparable overall contribution level. |
| pB9XVRGVu0 (GeRA) | 5.75 | R2 | PI-CCA is more ambitious in scope (continual adaptation vs. static alignment), with more extensive experiments. Both use geometric regularization but PI-CCA's continual-learning application adds difficulty. |
| V6uxd8MEqw (MISA) | 6.50 | R2 | Different CL setting (general CL vs. VL-CL). PI-CCA's contribution is comparably novel within its domain. |
| wE1I9IGqeH | 6.00 | R2 | Different CL variant; PI-CCA's method is more technically sophisticated. |

**Round-1 bracket**: [5.0, 7.5] based on initial retrieval.  
**Round-2 narrowing**: PI-CCA sits between 5.75 (GeRA) and 6.50 (C-CLIP). It is methodologically stronger than C-CLIP but has weaker presentation rigor (implausible correlation, missing std on Table 1). I place it at **6.0** — a solid contribution with a genuinely novel approach that outperforms existing replay-free methods, but with evaluation presentation issues that prevent a higher score.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>