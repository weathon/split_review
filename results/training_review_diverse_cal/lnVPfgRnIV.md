Now I have a thorough understanding of the paper. Let me produce the consolidated review.

## Summary

This paper tackles the stability-plasticity dilemma in incremental semantic segmentation. The authors propose a compression-sparsity principle: compress old-knowledge feature representations (by shrinking their subspace diameter) while enforcing sparsity between class distributions (by maximizing inter-class peak distances in a Gaussian mixture formulation). The method dynamically adjusts both old and new representations rather than freezing old ones. On the VOC 10-1 setting, they report an 11.7% MIoU gain over prior state-of-the-art on incremental-stage classes.

## Strengths

- **Consistent and substantial empirical gains.** Across five configurations on VOC (10-1, 2-2, 15-1, 15-5) and the 100-5 setting on ADE20K, the method shows multi-point MIoU improvements, particularly on incremental-stage classes. The gains are consistent across datasets and step counts, supporting the claim that the compression-sparsity idea provides a real plasticity benefit.

- **Ablation studies support the contribution of both components.** Table 3 systematically compares configurations with and without compression (C) and sparsity (S), showing that the full C+S+KD combination outperforms partial variants. Table 4 explores feature fusion methods, and Table 5 examines the α/β trade-off, providing multiple lenses on design choices.

- **Qualitative validation of the mechanism.** t-SNE visualizations (Figure 6) show tighter intra-class clusters and larger inter-class margins under the proposed method relative to baselines, and segmentation masks (Figure 7) appear cleaner. These help confirm that compression-sparsity measurably changes the feature geometry as intended.

## Weaknesses

### Fatal

None.

### Major

1. **Constraint enforcement in Equations (8b)–(8c) is unspecified.** The paper defines reconstructed features \(F_t^r = \gamma F_t^o + \tau\) subject to a diameter-shrinking constraint (8b) and an inter-class peak-distance constraint (8c), with γ and τ described as "learnable parameters that satisfy the constraint conditions." No optimization mechanism is given — whether via Lagrange multipliers, penalty terms, projected gradient descent, or hard clamping. "Convex points" and "peak points" of the Gaussian mixture distribution are mentioned but not operationalized. The GMD itself is described as a three-dimensional distribution over pixel position and feature response, but how its peaks and diameters are computed from network features is not specified. Since these constraints are the central technical contribution, the omission prevents reproducibility. The paper points to supplementary code, but the main text should provide a clear description of the optimization strategy.

2. **Hyper-parameter inconsistency muddies which numbers correspond to which setting.** The headline 11.7% improvement on VOC 10-1 is reported with α=0.2/β=0.8 ("especially with hyper-parameters α=0.2/β=0.8 in the challenging 10-1 setting, where the plasticity rises by 11.7%"). However, the paper later states "α and β are set to 0.8 and 0.2 in this paper for qualitative and quantitative analysis" for the sake of consistency with ADE20K, and reports other gains (9.8%, 6.2%, 11.8%, 7.1%) with α=0.8/β=0.2. It is unclear which hyper-parameter setting was used for the main comparative results in Tables 1 and 2. If the 11.7% figure uses a different hyper-parameter than the one used for the main analysis, direct comparison with baselines is potentially misleading.

### Minor

1. **The theoretical analysis (Section 3.2) is motivational rather than rigorous.** The derivation from a Bayesian posterior through Taylor expansion to Equation (6) \[(H(\theta^*) - N_k F(\theta^*))/\lambda_k^p \approx \sigma_k^p\] relies on citations to Martens (2014) and Huszár (2017), but the connection from this relationship to the conclusion that "preliminary feature contraction" is beneficial is asserted rather than logically derived. The subsequent reasoning linking Equation (7) to sparsity is similarly informal. This does not invalidate the method — the empirical results stand on their own — but the paper overstates the theoretical foundation. The analysis is better understood as a post-hoc intuition than a derivation.

2. **The loss function \(\mathcal{L}_{CS}\) (Equation 12) is underspecified.** The notation \(\widetilde{P_t^i}\) and \(P_{t-1}^i\) is ambiguous: are these per-pixel logits, per-class scores, or feature vectors? The summation over \(j=1,\,j\neq i\) to \(2||C||\) is not explained. The second term uses the operator \(\otimes\) with \(Mask_u\), which is likely element-wise multiplication but is not stated. While the overall form (a contrastive-like term plus a masked BCE term) is discernible, a precise specification is needed for reproducibility.

3. **No error bars or multiple-run statistics.** Results are reported as point estimates without standard deviations or confidence intervals. While single-run evaluation is common practice in this sub-area, the lack of any variance information makes it impossible to assess whether the reported improvements (some of which are modest, e.g., <2%) are statistically stable.

4. **GMD terminology is used ambiguously.** The paper describes a "three-dimensional Gaussian mixture distribution (GMD)" computed from pixel positions and feature responses, but never explains whether an actual GMM is fitted (e.g., via EM) or whether "GMD" is a rhetorical device for describing the empirical feature distribution. The "convex points" and "peak points" used in the constraints are not defined.

### Trivial

- Equation (13) defines \(S_t = [1 + \exp(F_t(X_t))]^{-1}\). This is \(\mathrm{sigmoid}(-F_t)\), not the standard sigmoid; the sign convention is unorthodox for a confidence score and warrants a brief justification.
- The confidence threshold of 0.7 in Equation (11) is introduced without any sensitivity analysis.

## Nice-to-Haves

- The paper could report results on Cityscapes or longer incremental sequences to strengthen generality, though the two datasets and five settings already provide reasonable coverage.
- A sensitivity analysis on the confidence threshold (0.7) used for knowledge transfer would be informative.
- A discussion of the computational overhead of computing GMD peaks and enforcing constraints during training would aid practical assessment.

## Removed Points

The following points from the reviewers were identified as invalid or scope-inappropriate per the evaluation rules:

- **"No citation or argument supports why this particular proportionality should hold" (about Equation 6):** Factually incorrect — the paper cites Martens (2014) and Huszár (2017) for the Hessian estimation.
- **"The paper does not cite or discuss relevant domain-incremental methods":** The paper cites Kim et al. 2024 and Wuerkaixi et al. 2024 for domain incremental learning. Additionally, missing related work is excluded per evaluation rules.
- **"Likely incorrectly copied" (about Equation 12):** Speculative and unsupported. The equation is ambiguous but not clearly "incorrect."
- **"Additional datasets (e.g., Cityscapes)":** Scope creep. The paper covers two standard benchmarks across five configurations.
- **"Individual effect of each [C and S] is not isolated" (ablation):** The paper does compare group configurations (1 vs 5 for C+S, 7 vs 8 for S+KD vs C+S+KD), providing some isolation.
- **"Inverse sigmoid" labeling of Equation (13):** \(1/(1+\exp(x))\) is \(\mathrm{sigmoid}(-x)\), a simple sign flip, not an inverse sigmoid. The reviewer's framing overstates the issue.

## Novel Insights

Beyond the paper's own contributions, the reviews surface a useful meta-observation: the paper's attempt to ground its method in a Bayesian/Taylor-expansion derivation is the weakest part of the contribution, while the empirical validation is the strongest. This suggests that for incremental segmentation papers in this vein, a clear empirical demonstration of the mechanism (e.g., feature-space visualizations, controlled toy experiments) may be more persuasive than post-hoc mathematical formalism that does not connect tightly to the actual algorithm. The tension between the reviewers who demand rigorous theory and those who accept heuristic motivation backed by strong experiments is a recurring dynamic that this paper illustrates well.

## Suggestions

1. **Specify constraint enforcement.** Describe exactly how γ and τ are optimized to satisfy Equations (8b) and (8c). Even a concise description (e.g., "we use a quadratic penalty method with Lagrange multiplier λ" or "γ and τ are clamped after each gradient step") would dramatically improve clarity. Define how "convex points" and "peak points" of the GMD are computed from network features.

2. **Disambiguate hyper-parameter usage.** Clearly separate which results use α=0.2/β=0.8 and which use α=0.8/β=0.2. If the main tables use the latter, the 11.7% figure should be clearly marked as an additional best-case result, and the corresponding baseline numbers under the same hyper-parameter choice should be provided.

3. **Clarify loss function notation.** Define \(P_t^i\) and \(\widetilde{P_t^i}\) as per-pixel or per-class vectors, specify the indexing convention, and state what \(\otimes\) means. A single sentence would suffice.

4. **Add error bars or multi-run statistics.** Reporting even 2–3 runs with mean and std for the key configurations would substantially increase confidence in the reported gains.

5. **Reframe the theoretical section.** Either tighten the derivation to actually connect each step to the algorithm, or explicitly present it as an intuitive motivation. The current framing ("mathematical analysis demonstrates") overclaims.

## Score and Decision

The paper addresses a real problem (plasticity in incremental segmentation) and proposes a plausible solution backed by consistent empirical gains across multiple settings. The core weaknesses — underspecified constraint enforcement, hyper-parameter inconsistency, and unclear loss function notation — are significant and would prevent a reader from reproducing or fully understanding the method as presented. However, none of these issues is structural or fatal; they are gaps in exposition and rigor that could be resolved in a major revision. In its current form, the paper does not meet the reproducibility standard required for acceptance.

MY FINAL SCORE: <pineapple>5.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>