Now I have all the information I need. Let me produce the consolidated review.

## Summary

This paper proposes FairerCLIP, a kernel-based method to debias CLIP's zero-shot predictions. The approach formulates debiasing as an optimization problem in reproducing kernel Hilbert spaces (RKHSs) using an HSIC-based dependence measure, leading to closed-form alternating updates via a generalized eigenvalue problem. The method aims to handle both spurious correlations and intrinsic dependencies, can operate with or without ground-truth labels, and achieves 4–10× training speedups. Experiments on Waterbirds, CelebA, FairFace, and CFD show competitive or state-of-the-art debiasing performance across multiple settings.

## Strengths

- **Unified framework across multiple debiasing scenarios**: Unlike prior approaches specialized for either spurious correlations or intrinsic dependencies, and for either supervised or unsupervised settings, FairerCLIP achieves competitive or superior performance in all four combinations. On spurious correlation benchmarks (Table 2, w/ labels, ViT-L/14), FairerCLIP obtains the highest worst-group accuracy (86.0% on Waterbirds, 85.2% on CelebA) and smallest gap (6.1%, 2.5%). On unsupervised settings, it leads on both metrics (78.1% WG Waterbirds, 86.1% WG CelebA). No other method matches this breadth.

- **Order-of-magnitude training speedup**: The RKHS formulation yields closed-form updates, making training 4–10× faster than baselines. Table 4 reports training times: FairerCLIP takes 32 seconds (Waterbirds) and 222 seconds (CelebA), versus 1202 and 20602 seconds for the next-best Contrastive Adapter.

- **Strong sample efficiency under limited data**: On the Chicago Face Database (597 samples), all baselines nearly fail (WG ~35%, gap ~54%), while FairerCLIP achieves WG 54.7% and gap 21.8% (Figure 4). This demonstrates practical advantage under data-scarce conditions.

- **Effective debiasing without ground-truth labels**: FairerCLIP uses pseudo-labels from CLIP's zero-shot predictions and iteratively refines the target label. On CelebA w/o labels (Table 2, ViT-L/14), it attains WG 86.1% (gap 1.9%), beating Orth-Cali (WG 76.1%, gap 10.1%) by a large margin. On FairFace (Table 3), it reduces MaxSkew@1000 to 0.097 (sex) and 0.408 (race) for ViT-B/32.

- **Thorough ablation studies validate design choices**: The paper systematically ablates Dep(Z,Y), Dep(Z_I, Z_T), and iterative label updating (Table 5). Removing Dep(Z,Y) causes WG to drop 14.5% and EOD to rise to 0.195%; fixing pseudo-labels reduces WG from 86.1% to 81.1%. These confirm each component's contribution.

- **Geometric illustration provides intuition**: Figure 2 offers an accessible visual explanation of how the encoder seeks directions aligned with the target label, orthogonal to the sensitive attribute, and close to the other modality's representations.

## Weaknesses

### Fatal
None.

### Major

- **Near-zero EOD in Table 1 lacks variance estimates.** FairerCLIP reports EOD of 0.02% (ResNet-50) and 0.005% (ViT-L/14) on the CelebA intrinsic-dependency task, where the next best baseline achieves 1.0%. These are the paper's most striking results and directly support the core claim about handling intrinsic dependencies. Yet no standard deviations, confidence intervals, or multi-seed results are reported for this table, while the spurious-correlation results (Table 2) do include ± values. Without error bars, readers cannot assess whether these striking values are stable or a chance outcome of a specific data split or initialization. This is the most significant evidential gap in the paper.

### Minor

- **The γ regularization term in Theorem 1 (Eq. 8) is not defined in the main text.** Equation (151) includes γI on the right-hand side of the generalized eigenvalue problem, but the paper never introduces γ, explains its role (e.g., stabilizing matrix inversion or enforcing a norm constraint), or states how it is chosen. This is necessary for the method to be fully reproducible from the main paper.

- **The intrinsic-dependency evaluation is limited in scope.** The paper's most distinctive claim — handling intrinsic dependencies better than prior work — rests on a single experiment: CelebA with high-cheekbones vs. sex. Only one dataset and one attribute pair are used. While intrinsic dependencies are harder to construct in standard benchmarks, the claim would be stronger with additional evaluations.

- **The sample-efficiency claim is narrowly supported.** The CFD experiment (597 samples) is striking, but the paper does not systematically study sample efficiency across different dataset sizes (e.g., subsampling CelebA or Waterbirds at 10%, 25%, 50%). The claim is plausible but supported by only one small-dataset experiment.

- **Average accuracy trade-off is not discussed explicitly.** In Table 2, FairerCLIP's average accuracy is consistently lower than some baselines (e.g., 87.8% vs. 94.6% for ERM on CelebA ViT-L/14 w/ labels). While "Gap" is the appropriate primary metric for fairness, the accuracy cost should be discussed more directly so practitioners can calibrate expectations.

- **Ablations are conducted only on CelebA.** The ablation study (Table 5) examines all component removals on CelebA but not on Waterbirds or FairFace. The findings may be dataset-specific, and the ablations for the unsupervised setting are also only on CelebA.

- **Non-monotonic behavior of the alignment term is undiscussed.** In the w/ labels ablation on CelebA (blonde hair), removing Dep(Z_I, Z_T) sometimes improves Gap (1.7% vs. FairerCLIP's 2.6%) and worst-group accuracy (87.0% vs. 86.7%), while only reducing average accuracy. The paper acknowledges a decrease in average accuracy but does not discuss why the alignment term can slightly hurt the debiasing objective in some configurations.

- **Hyperparameter sensitivity is not explored.** The paper introduces trade-off parameters τ_I, τ_T, and τ_z but provides no analysis of how performance varies with these values. A plot or sensitivity table would help practitioners understand the robustness of the method.

- **The paper has no limitations section.** Important limitations go unacknowledged, including: (1) the generalized eigenvalue step may become expensive for large n despite RFF; (2) the method requires a kernel choice for the sensitive attribute; (3) the representation dimension r is bounded by rank(L_X); (4) pseudo-label initialization may fail if CLIP's zero-shot accuracy is very low.

- **Minor inconsistency between table and text.** Table 1 shows an EOD of 0.02 for ResNet-50, but the text (line 206) describes it as 0.002%. The ViT-L/14 value is consistently 0.005%.

### Trivial

- **Geometric illustration figure (Fig. 2) is described but the angles (α_{IY}, α_{IS_⊥}, α_{IT}) are not formally defined in the text.** A more precise caption or formal definition would help.

## Nice-to-Haves

- **Kernel vs. MLP encoder comparison:** The paper claims kernel methods are "particularly effective compared to shallow MLPs" but never directly tests this. An ablation replacing the RKHS encoder with a one-layer MLP trained by gradient descent on the same objective would isolate the benefit of the closed-form approach from the benefit of the objective itself.
- **Systematic sample-efficiency study across dataset sizes:** Subsampling CelebA or Waterbirds at multiple fractions (10%, 25%, 50%) would substantially strengthen the sample-efficiency claim.
- **Ablation updating Ŝ in the unsupervised setting:** The paper justifies not updating Ŝ, but an ablation updating both Ŷ and Ŝ would confirm the proposed strategy is indeed better.
- **Hyperparameter sensitivity plots** for τ_I, τ_T, τ_z would be useful for practitioners.

## Removed Points

These points are flagged to be removed per the instructions; treat them with caution.

- **"Kernel choices for K_Y and K_S are never stated"** — The paper explicitly states "All the implementation details are provided in sec:imp-details" (deferred to the appendix, which the parser strips). The same applies to the number of RFF features. Per the hard rule about appendix content, these are removed.
- **"Pseudo-code deferred to supplement"** — Per the hard rule about appendix content, removed.
- **"Why standard HSIC would not work"** — The paper does explain at line 61 (convergence rate, captures non-linear modes, analytical tractability). The reviewer appears to have missed this explanation.
- **"DFR can in principle address intrinsic dependencies"** — This is a strawman argument. The paper's claim is about the *design focus* of existing CLIP debiasing methods, not their theoretical capability. Empirically, DFR achieves EOD of 4.1–7.4% on the intrinsic-dependency task (Table 1), demonstrating that existing methods do not handle it effectively.
- **"CFD figure only qualitatively described"** — The figure is not available in the parsed text (parser limitation); the paper provides numerical values (WG, Avg, Gap) that constitute the quantitative comparison.
- **"Alternating optimization described only at high level"** — Standard for a conference paper with supplementary material; the pseudo-code exists in the appendix.

## Novel Insights

None beyond the paper's own contributions. The reviews confirm that the paper's core technical contribution — formulating CLIP debiasing as an RKHS optimization with closed-form alternating updates — is novel and effective, while also identifying that its most striking empirical claim (near-zero EOD on intrinsically dependent attributes) needs stronger evidential support. The observation about the non-monotonic effect of the alignment term on debiasing is a useful nuance surfaced by analysis.

## Suggestions

1. **Add error bars to Table 1.** Report EOD and accuracy over at least 5 random seeds with mean ± std, as is already done in Table 2. This is the single most important improvement.
2. **Define γ in the main text** (Theorem 1). State its role (regularization for the generalized eigenvalue problem) and how it is chosen (e.g., a small constant like 1e-6 or tuned on validation data).
3. **Discuss the accuracy-fairness trade-off explicitly** where FairerCLIP's average accuracy is lower than baselines, and add a brief paragraph on limitations.
4. **Resolve the EOD inconsistency** between Table 1 (0.02) and the text (0.002%) for the ResNet-50 case.
5. **Add at least one more intrinsic-dependency evaluation** or explicitly acknowledge the limitation of a single attribute-pair evaluation.

## Score and Decision

The paper makes a genuine contribution: a principled, flexible, and efficient debiasing framework for CLIP with strong results across multiple scenarios. The main evidential weakness — missing variance for the most striking result — is addressable and does not invalidate the paper's other contributions (spurious correlation results include error bars and are competitive; unsupervised results are strong; training speed is unambiguous). The methodological gaps (γ not defined) are minor presentation issues. The paper is solid but has clear room for strengthening.

**Score: 7.0** (accept, good paper with addressable weaknesses)

MY FINAL SCORE: <pineapple>7.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>