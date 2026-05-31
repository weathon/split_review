Now I have all the verification I need. Let me produce the final consolidated review.

---

## Summary

This paper proposes a mutual information estimator that combines the difference-of-entropies (DoE) framework with normalizing flows. The key innovation is a block autoregressive normalizing flow (B-NAF) architecture that jointly parametrizes both the marginal density \(q_X\) and the conditional density \(q_{X|Y}\) within a single network, enabling simultaneous estimation of \(H(X)\) and \(H(X|Y)\) by deactivating off-diagonal weight blocks. Experiments on synthetic Gaussian data (standard, cubic-transformed, and sparse-correlation) show competitive or superior performance compared to discriminative baselines (MINE, SMILE, InfoNCE, NWJ, DEMI) and a separately-trained B-NAF baseline.

## Strengths

1. **Novel joint parametrization reduces bias in several settings.** The block autoregressive structure enables a single flow to estimate both \(H(X)\) and \(H(X|Y)\) by masking off-diagonal weights (lines 215–230). The paper reports that on cubic Gaussians and small-sample regimes, the separate BNAF baseline exhibits bias that NDoE BNAF does not (line 249), directly supporting the claimed bias-reduction benefit of joint estimation.

2. **Near-zero estimation error on Gaussian benchmarks where discriminative methods systematically underestimate.** Across dimensionalities 20–100 and sample sizes 32K–128K, the paper shows (via Figures 2–5) that discriminative methods (MINE, SMILE, InfoNCE, NWJ, DEMI) all underestimate true MI, while NDoE BNAF remains near zero error. The text states: "All the discriminative methods tend to underestimate MI. This issue does not occur in our proposed flow-based models for Gaussian variables" (line 248).

3. **Theoretical grounding via variational characterization.** Lemma 2.1 and Corollary 2.2 provide a rigorous proof that conditional entropy equals an infimum of cross-entropy over conditional densities, establishing the DoE formulation used in the paper (Equations 4–6). This connects the method to principled foundations.

4. **Robustness to nonlinear dependencies compared to misspecified DoE.** On cubic-transformed Gaussians, the standard DoE baseline (with a misspecified logistic density) shows large bias, while the flow-based NDoE BNAF handles the nonlinearity substantially better (line 249, Figures 2–4 bottom rows). This demonstrates a concrete advantage of using flexible normalizing flows over fixed parametric families.

## Weaknesses

### Fatal
None.

### Major

1. **Results are reported only in figures without any numerical tables.** No quantitative table of means, standard deviations, or confidence intervals is provided for any experiment. The text makes comparative claims (e.g., "our proposed model achieved better performance across different dimensionalities and sample sizes") but the reader cannot verify the magnitude of differences, the variance across the 10 runs, or whether improvements are statistically significant. This is an evidential gap that undermines rigorous evaluation of the method's claimed advantages.

2. **Empirical scope is narrow and does not support claims of broad applicability.** The evaluation is confined to Gaussian distributions (standard, cubic-transformed, sparse-correlation). While these serve as sanity checks with known ground truth, they are among the simplest possible settings. The paper concludes that the method is "a good candidate for use in research that optimizes MI" (line 251) and claims general advantages, yet provides no experiments on non-Gaussian high-dimensional benchmarks (e.g., the Czyż et al. (2023) benchmarks that the paper itself cites), real-world data (images, text, biology), or discrete data. The paper acknowledges this limitation (lines 252–254) but the gap between claims and evidence remains large.

3. **The advantage of joint over separate estimation is not uniformly supported by the presented results.** The paper's own results show that on sparse Gaussian data with larger MI, the separate BNAF baseline *outperforms* the proposed joint NDoE BNAF (line 249: "BNAF outperformed NDoE, BNAF for larger MI"). This is inconsistent with the claimed superiority of joint estimation. No ablation study isolates whether improvements come from the joint architecture, the specific flow design, or the training procedure. Without isolating the source of improvement, the core methodological thesis is only partially supported.

### Minor

1. **Training procedure has residual ambiguity.** The paper references "Algorithm 1, which optimizes for \(H(X|Y)\) and \(H(X)\) simultaneously" (line 230), but the preceding sentence speculates about a two-stage procedure ("It is, however, conceivable that one can begin with a network that approximates \(H(X)\) and then optimize the off-diagonal weights..."), creating confusion about the actual optimization protocol. The exact details of weight sharing, gradient flow, and whether the two entropy terms are truly optimized in a single pass or alternated would benefit from clarification.

2. **Activation function mismatch between methods introduces a confounding factor.** The proposed B-NAF method uses tanh activations, while the discriminative baselines use ReLU (line 247). This makes it impossible to attribute performance differences solely to the MI estimation principle versus the neural architecture choices. The separate BNAF baseline also presumably uses tanh, so the within-generative comparison is controlled, but the primary comparison against discriminative methods is confounded.

3. **No theoretical analysis of claimed unbiasedness and consistency.** The paper claims the estimator is "unbiased and consistent" (line 18) but provides no proof or even a sketch of the argument. Given that the DoE estimator's unbiasedness depends on exact density representation (sufficient capacity, global optimum), and the experiments show residual bias on cubic Gaussians, some formal treatment of when and why unbiasedness holds would strengthen the paper.

4. **Parameter count matching between methods is imprecise.** The paper states that B-NAF layers use "\(20\times20\)-d, \(10\times50\)-d, \(6\times100\)-d hidden dimensions" which is "roughly the same as the 512 hidden units in discriminative methods" (line 247). The notation is ambiguous and the matching is approximate, making it difficult to assess comparison fairness.

### Trivial
- None.

## Nice-to-Haves
- **Add tabular results** (means and standard deviations over 10 runs) for all experimental settings to enable proper evaluation.
- **Include at least one non-Gaussian benchmark** from the Czyż et al. (2023) collection to demonstrate the method works beyond Gaussian assumptions.
- **Add an ablation study** that directly compares joint NDoE BNAF to separate BNAF while controlling for architecture size, training budget, and initialization.
- **Report runtime/computational cost** comparison, since normalizing flows are typically more expensive than critic networks and the practical trade-off is important.
- **Include a precise algorithmic pseudocode** for the training procedure specifying whether optimization is simultaneous or sequential.

## Removed Points
These points are flagged to be removed; treat them with caution.

- **Criticism that Algorithm 1 is missing entirely from the text:** The algorithm image is absent due to PDF parsing artifacts. Per instructions, removed as a parser issue.
- **Criticism that the paper does not clearly state which version of the DoE estimator is used:** The paper explicitly states "DoE (McAllester & Stratos, 2018), the DoE method, where the distributions is parameterized by isotropic Gaussian (correct) or logistic (misspecified)" (line 245). This is factually incorrect as a criticism.
- **Criticism that the method "cannot be reproduced or properly evaluated" / "structural flaw":** Overstated. The method is described — architecture, loss functions, deactivation principle, and a reference to Algorithm 1 are all present. Some details could be clearer (minor weakness), but the core technical contribution is assessable.
- **Strength claiming "improved bias-variance trade-offs" without qualification:** The paper does show bias reduction in some settings, but the same results show the separate baseline outperforms the joint method in other settings (sparse Gaussian, larger MI). The strength is qualified in the retained weaknesses above.

## Novel Insights
The two reviews offer complementary perspectives that, taken together, surface an interesting tension: the harsh critic views the joint parametrization as insufficiently validated, while the strength finder identifies genuine empirical support on Gaussian benchmarks. Neither reviewer contests that the core idea (DoE + block autoregressive flows for joint density estimation) is sensible and grounded in variational principles. The most interesting observation to emerge is that the paper's own results *contradict* its central success narrative in one regime (sparse Gaussian, larger MI, where separate BNAF outperforms NDoE BNAF). This suggests the joint architecture provides benefits that are task-dependent rather than universal — a nuance that is acknowledged in the text but not analyzed or explained. A deeper investigation of *when* joint estimation helps versus hurts would be more valuable than a blanket claim of superiority.

## Suggestions
1. **Add full numerical tables** (mean ± std over 10 runs) for every experimental condition, so the reader can evaluate the magnitude and variability of performance differences.
2. **Include at least one non-Gaussian benchmark** (e.g., from the Czyż et al. (2023) challenge set) to demonstrate the method's generality beyond Gaussian-based data.
3. **Provide precise pseudocode or explicit training protocol** clarifying whether the two entropy terms are optimized in a single joint pass or in alternating steps, and how the "deactivation" operation is implemented at the weight level.
4. **Add an ablation study** directly comparing joint NDoE BNAF vs. separate BNAF while controlling for all architectural and optimization variables, to isolate the benefit of joint estimation.
5. **Address the theoretical claim** of unbiasedness and consistency with a formal argument or at minimum a sketch of the conditions under which it holds.

## Score and Decision

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>