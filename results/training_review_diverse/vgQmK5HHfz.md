Now I have a thorough understanding of the paper and can verify every claim. Let me compile the final consolidated review.

## Summary

The paper proposes NDoE-BNAF, a mutual information estimator combining the difference-of-entropies (DoE) framework with a single block-autoregressive normalizing flow (B-NAF) that jointly parametrizes the marginal entropy H(X) and conditional entropy H(X|Y) through a deactivation mechanism. The key innovation is using one architecture for both terms rather than training separate generative models, which the authors show reduces bias compared to separately trained flows. The method is evaluated on correlated, cubic-transformed, and sparse Gaussian benchmarks across dimensions 20–100 and sample sizes 32K–128K.

## Strengths

1. **Joint parametrization via block-autoregressive flows is a clean and well-motivated idea.** The deactivation mechanism (zeroing off-diagonal weight blocks) elegantly reuses the same flow architecture to estimate both H(X|Y) with the full network and H(X) after deactivation. The B-NAF architecture's triangular Jacobian makes this operation straightforward, and the paper explains the 2D and general nD cases (Section 3, lines 204–232).

2. **Empirical reduction of bias vs. separately trained flows on Gaussian benchmarks.** The paper directly compares NDoE-BNAF against BNAF (two separately trained flows) and shows that the separate approach "exhibits a slight bias across all true MI values" especially in cubic-transformed cases where "BNAF shows a larger bias when MI is close to zero, an issue not observed with NDoE-BNAF" (Section 4.1, line 249). This provides direct evidence for the core claim that joint estimation improves bias.

3. **Consistent outperformance of discriminative lower-bound estimators.** Across all settings (correlated, cubic, sparse Gaussians), discriminative methods (InfoNCE, MINE, SMILE, NWJ, DEMI, DoE) systematically underestimate MI, while NDoE-BNAF produces estimates much closer to the true value (Section 4.1, line 248). This is a clean demonstration that generative DoE approaches can overcome the known downward bias of variational lower-bound methods.

4. **Honest acknowledgment of limitations.** The conclusions explicitly discuss dependence on Gaussian base distributions, stability issues, and the need for future comparison with DINE, Butakov et al., and MINDE (Section 5, lines 251–254). This transparency is commendable and helps readers understand the scope of the contribution.

## Weaknesses

### Fatal
None.

### Major

1. **No empirical comparison with the most directly related generative MI estimators.** The paper cites DINE (Duong & Nguyen, 2023), the flow-based estimator of Butakov et al. (2024), and MINDE (Franzese et al., 2024) in the introduction and acknowledges them as "other generative approaches" to compare with, but defers all such comparisons to future work (lines 34, 253–254). Since these methods share the generative philosophy and represent the most relevant baselines, the paper cannot substantiate its claimed advantages over "state of the art methods" without evaluating against them. The comparison against separately trained BNAF is a helpful ablation, but it does not substitute for comparison against published generative MI estimators that also achieve strong Gaussian performance.

2. **No uncertainty quantification despite reporting "10 runs."** The paper states "All results were computed over 10 runs on the testing sets generated with different random seeds" (line 247) but reports results only as point estimates (estimation error I−Î) in narrative form. No error bars, standard deviations, or confidence intervals are presented for any experiment. Given that the paper's central claim is "better performance," the absence of variance information makes it impossible to assess whether differences between methods are statistically significant or merely noise across runs. This is a fundamental omission for an empirical comparison paper.

### Minor

3. **The training procedure is incompletely specified.** While the paper describes the architecture and the deactivation mechanism conceptually, two key specifics are missing: (a) the cost function **L₂** for H(X) is referenced ($\mathcal{L}_{2}$, line 230) but never written as an equation — the reader must infer it; (b) it is unclear whether the two objectives are optimized jointly (gradients from both at each step) or sequentially, and how the deactivation is applied during training (at initialization only, or toggled). Algorithm 1 is referenced but its content is not present in the parsed main text; even so, the surrounding text leaves ambiguity about the training dynamics. This hampers reproducibility.

4. **The "improved bias-variance trade-offs" claim is asserted but not empirically supported.** The abstract (line 4) invokes improved bias-variance trade-offs, yet the experiments report only aggregate estimation error (I−Î) with no decomposition into bias and variance components. There is no analysis of estimator variance across runs, no comparison of the variance of NDoE-BNAF vs. discriminative methods, and no ablation isolating how the joint parametrization affects variance. The paper attributes improvements to joint estimation, but the mechanism (bias-variance trade-off) is not demonstrated.

5. **Evaluation is restricted to Gaussian-based synthetic benchmarks.** The experiments cover correlated Gaussians, cubic-transformed Gaussians (non-linear but still Gaussian-derived), and sparse Gaussians. While these are standard in the MI estimation literature, the paper claims broad applicability but tests no non-Gaussian or real-world data. The cubic transformation is a step toward non-linearity, but the base distribution remains Gaussian, and the method's reliance on a Gaussian base distribution is itself a limitation the authors acknowledge. The Czyż et al. (2023) benchmarks, cited in the introduction, would have provided more challenging and diverse test cases.

6. **No computational cost or parameter count comparison.** The discriminative methods and the flow-based method use fundamentally different architectures, yet the paper reports neither parameter counts nor runtime. The text notes B-NAF uses "roughly the same [hidden dimensions] as the 512 hidden units in discriminative methods" (line 246), but this is a loose comparison. Given that normalizing flow training is typically more expensive, reporting computational cost would help practitioners assess the practical trade-off.

### Trivial

- The proof of Lemma 2.1 (lines 87–93) is standard and could be shortened or deferred to an appendix without loss.
- The paper mentions "long-run training experiments" (lines 241, 249) that are not present in the parsed text (they may be in the appendix, which the parser strips). If they exist, the main paper should summarize key findings; if they do not, the claim is unsubstantiated.

## Nice-to-Haves

- **Separate bias/variance decomposition** for at least one representative setting (e.g., 20-d Gaussian at varying sample sizes) to directly support the "bias-variance trade-offs" claim in the abstract.
- **Non-Gaussian benchmarks** from Czyż et al. (2023) to test whether the method's good performance generalizes beyond Gaussian-derived data, especially given the acknowledged limitation of Gaussian base distributions.
- **Runtime and parameter count tables** for all methods to enable practical comparison.
- **Error bars** on all figures as standard practice for any multi-run experiment.

## Removed Points

*These points are flagged to be removed; treat them with caution.*

- **"The long-run training experiments... are not present in the extracted text."** — These may reside in the appendix, which the parser strips. The claim about their absence cannot be verified from the available text.
- **"Algorithm 1 (referenced but not textually defined)"** — Algorithm 1 is likely presented in a figure/box that the parser strips. The surrounding text describes its motivation. However, the related point about L₂ not being explicitly defined is retained as valid.
- **"The proof is not needed in the main text"** — This is a stylistic preference, not a substantive weakness. Moved to Trivial.
- **Strength Finder's claim of "comprehensive evaluation across multiple challenging settings"** — Overstated given the Gaussian-only scope and the absence of comparisons with other generative estimators. The evaluation is methodical within its narrow scope but not comprehensive in the broader sense.
- **Strength Finder's claim of "theoretical guarantee of convergence"** — The paper states this as a claim (line 251) but provides no formal theorem, proof, or convergence rate. It is a stated property of the DoE framework with sufficient capacity, not a novel theoretical contribution with proof.

## Novel Insights

The key insight from the reviews that goes beyond the paper's own narrative is that the paper's primary empirical contribution — showing that joint parametrization reduces bias vs. separate flow training — is a reasonable ablation, but the paper overclaims by not comparing against the most directly related generative methods (DINE, Butakov et al., MINDE) that also use density-estimation approaches to MI. The reviewers collectively see a method that is well-motivated and mechanically sound but insufficiently differentiated from the existing generative MI literature. The paper's honesty about limitations is a strength, but it also highlights that the current contribution is preliminary: the architecture is novel, but the evidence that it advances the state of the art is incomplete.

## Suggestions

1. **Add comparisons with DINE, Butakov et al. (2024), and MINDE** — these are the most directly related methods and must be included before claiming superiority over generative approaches.
2. **Report error bars** (e.g., ±1 std over 10 runs) in all figures and numerical results. This is a minimal standard for any multi-run experiment.
3. **Define L₂ explicitly** and clarify whether training is joint, sequential, or alternating. Specify how the deactivation mask is applied during optimization (gradient masking, weight zeroing, or architectural separation).
4. **Include at least one non-Gaussian benchmark** (e.g., from Czyż et al., 2023) to demonstrate robustness beyond Gaussian-derived data.
5. **Add a bias/variance decomposition** for a representative experiment to substantiate the "bias-variance trade-offs" claim in the abstract.

## Score and Decision

The paper's core idea — joint parametrization of H(X) and H(X|Y) via a deactivated block-autoregressive flow — is sensible and well-motivated. The empirical comparison against separately trained BNAF provides a clean ablation showing bias reduction. However, the evaluation is too narrow to support the broad claims of state-of-the-art performance: the most directly related generative competitors are not compared against, results lack any uncertainty quantification, and the experimental scope is limited entirely to Gaussian-derived data. The training procedure description has gaps that hurt reproducibility. These are not fatal flaws (the method itself is sound), but they substantially weaken the contribution's significance in its current form. With major revisions — especially adding comparisons to other generative MI estimators and uncertainty quantification — the paper could become a solid contribution.

**Score:** 5.0
**Decision:** Reject

MY FINAL SCORE: <pineapple>5.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>