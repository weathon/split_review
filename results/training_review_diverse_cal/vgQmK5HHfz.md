Now I have a thorough understanding of the paper. Let me construct the consolidated review.

---

## Summary

This paper proposes a mutual information estimator that combines the difference-of-entropies (DoE) principle with normalizing flows. The key idea is to use a single block-autoregressive normalizing flow (B-NAF) with a weight-deactivation mechanism to jointly estimate both the marginal entropy H(X) and the conditional entropy H(X|Y) within a shared architecture. This joint estimation is claimed to improve bias-variance trade-offs compared to separately trained generative models and discriminative MI estimators. Experiments on correlated multivariate Gaussians (including cubic and sparse variants) show that the proposed method (NDoE BNAF) reduces underestimation bias compared to discriminative methods (MINE, SMILE, InfoNCE, NWJ, DEMI) and a separately trained BNAF baseline.

## Strengths

1. **Joint estimation within a shared architecture reduces bias compared to separately trained generative models.** The paper shows that in the cubic Gaussian case with 32K samples, the separate-BNAF estimator exhibits large bias when MI is close to zero, while the proposed NDoE BNAF mitigates this (Section 4.1, Fig. 4 bottom). This directly supports the claim that sharing the network structure for marginal and conditional density estimation improves bias.

2. **Consistently lower estimation error than discriminative baselines across multiple dimensions, sample sizes, and data types.** In 20-d, 50-d, and 100-d Gaussian experiments with 32K–128K samples, the proposed method achieves estimation error closest to zero among all methods (Figs. 2–4). The paper reports that "all the discriminative methods tend to underestimate MI. This issue does not occur in our proposed flow-based models for Gaussian variables" (Section 4.1). This provides direct evidence supporting the central claim of improved bias.

3. **Theoretical grounding via variational characterization of conditional entropy (Lemma 2.1).** Lemma 2.1 and Corollary 2.2 establish that conditional entropy can be expressed as an infimum over conditional densities, extending the standard entropy variational characterization. This justifies the joint optimization framework and provides theoretical support for unbiasedness and consistency in the limit of sufficient capacity and samples.

4. **Architectural simplicity of the B-NAF for the DoE estimator.** The B-NAF's triangular Jacobian enables efficient log-determinant computation, and the block matrix structure permits a straightforward deactivation operation (setting off-diagonal weights to zero) to switch between marginal and conditional density estimation within the same network (Section 2.2.1, Section 3).

5. **Systematic evaluation with controlled comparisons.** The experiments vary dimensionality (20, 50, 100), sample size (32K, 64K, 128K), true MI values, and data types (Gaussian, cubic, sparse Gaussian). Neural network capacity is roughly matched between generative and discriminative methods. Comparisons also include a Real NVP variant of the proposed method and a separately trained BNAF, providing some controlled baselines.

## Weaknesses

### Fatal
None.

### Major

1. **Proposed "long-run training behavior" experiments are promised but absent.** The paper states twice that certain experiments exist or will be presented: "The final experiments will be the long-run training behavior on the proposed estimator" (Section 4, line 241) and "In the 20-dimensional Gaussian case, SMILE occasionally overestimated MI, which we will further analyze in the long-run training experiments" (Section 4.1, line 249). However, the experimental section contains only Subsection 4.1 (Gaussian benchmarks) and then moves directly to conclusions. No long-run training analysis appears anywhere in the paper as presented. This makes the paper feel incomplete — either these experiments were intended for a section that was cut, or the statements are erroneous forward references. Either way, the reader cannot evaluate claims that depend on this missing analysis.

2. **Missing comparisons against the most directly comparable flow-based MI estimators.** The introduction surveys three recent generative/flow-based MI estimators — DINE (Duong & Nguyen, 2023), Butakov et al. (2024), and MINDE (Franzese et al., 2024) — yet the experiments compare only against discriminative methods and a separate-BNAF baseline. The paper's contribution is explicitly positioned as a flow-based alternative, and the title emphasizes "normalizing flows," but no evidence is provided that the proposed estimator improves over other flow-based estimators. The paper relegates these comparisons to future work (conclusions, line 254), but this significantly weakens the empirical support for the claimed improvements. Including even one of these methods on the Gaussian benchmarks would substantially strengthen the evaluation.

### Minor

1. **The training procedure for joint optimization is ambiguous.** The paper describes two distinct cost functions (L₁ for H(X|Y), L₂ for H(X) with deactivated weights) and states that Algorithm 1 "optimizes for H(X|Y) and H(X) simultaneously" (line 230). It also suggests a two-phase procedure: "one can begin with a network that approximates H(X) and then optimize the off-diagonal weights to obtain an approximation of H(X|Y)" (line 216). It is not clear which of these is actually used in the experiments, whether training alternates between the two objectives, or if the "simultaneous" optimization uses a combined loss. For a methods paper, this level of ambiguity about the core algorithmic contribution is a significant presentation gap that hinders reproducibility.

2. **No variance/uncertainty measures are reported in text.** The paper repeatedly discusses bias-variance trade-offs and states results are averaged over 10 runs, but the text reports only point estimates (bias). No standard deviations, confidence intervals, or other variance metrics are provided. Without these, the "variance" component of the claimed bias-variance improvement is unsubstantiated. (Figures may contain error bars, but the text should also discuss variance, especially since a core selling point is bias-variance trade-off.)

3. **The claim of an "unbiased and consistent" estimator is overstated without qualification.** The paper states "We propose an unbiased and consistent mutual information estimator" (Section 1, line 18). In practice, unbiasedness holds only asymptotically with sufficient model capacity and optimization — the finite-sample bias from misspecification and optimization error is the central topic of the paper's own experiments. A phrasing like "asymptotically unbiased under sufficient expressivity" would be more precise.

4. **The method is only evaluated on Gaussian-based synthetic data.** All experiments involve correlated Gaussians (with or without cubic transformations or sparse structure). The paper acknowledges this limitation (conclusions, line 252–254) and notes more challenging benchmarks exist (Czyż et al., 2023), but does not use them. While this is acceptable for an initial methods paper, the narrow scope limits the strength of the claims about general applicability.

### Trivial

- Corollary 2.2 is presented but never used in the remainder of the paper.
- Minor imprecision: "cross-entropy" is used to refer to both the density-level quantity and the Monte Carlo objective without clear distinction.
- The text contains a few awkward phrasings (e.g., "the recently introduced MINDE estimator Franzese et al. (2024), which is based on diffusion models and represents a complementary approach" trails off grammatically on line 34).

## Nice-to-Haves

- An ablation study showing how the number of B-NAF layers or hidden dimensions affects MI estimation accuracy.
- Discussion of computational cost (wall-clock time) relative to discriminative methods, especially since normalizing flows require Jacobian computation.
- Clarification of whether the base density is fixed (standard Gaussian) or has learned parameters, and how this interacts with the MI estimate.
- Experiments on at least one non-Gaussian benchmark from Czyż et al. (2023) to demonstrate broader applicability.

## Removed Points

These points were flagged by reviewers but are removed or downgraded per the consolidation rules:

- **Criticism that Algorithm 1 is only in a figure:** The algorithm exists in the original submission as a figure. The parser strips images. The textual description of the training procedure (Section 3) is sufficient to convey the core approach, though it could be clearer (kept as a Minor weakness above rather than a Major one).
- **Criticism that "no measures of variance are reported" as a fatal flaw:** The paper reports 10-run averages and figures (unviewable in parsed text) may contain error bars. The lack of textual variance reporting is a Minor issue, not a fatal one.
- **Criticism that "the paper's own direction is a generative MI estimator" — the comparison against separate BNAF is a generative baseline.** The paper does compare against a flow-based generative baseline (separate BNAF), partially addressing concerns about missing generative comparisons. The missing comparisons are specifically DINE, Butakov et al., and MINDE.
- **Strength Finder claim about "robustness across both linear and nonlinear dependencies"** — kept but downgraded since the only nonlinear case tested is a cubic transformation of Gaussians, which is still fundamentally Gaussian in base structure.

## Novel Insights

None beyond the paper's own contributions. The reviews did not surface an unexpected finding that the authors themselves missed.

## Suggestions

1. **Clarify the training procedure explicitly.** Provide pseudocode or a clear description of whether training is sequential (train H(X) first, then H(X|Y)), alternating (switch modes each mini-batch), or uses a combined loss. This is the single most important fix for reproducibility.
2. **Either include the long-run training experiments or remove all references to them.** The two references to "long-run training experiments" that do not exist in the paper undermine its completeness. If these experiments exist in a supplementary, state so explicitly.
3. **Add at least one comparison against a flow-based MI estimator (e.g., Butakov et al. or DINE) on the Gaussian benchmarks.** This would directly support the positioning of the contribution as a flow-based alternative.
4. **Report variances alongside biases** in the text (or at minimum confirm that figures contain error bars and describe their content) to substantiate the bias-variance trade-off claims.
5. **Qualify the "unbiased and consistent" claim** to reflect its asymptotic nature.

## Score and Decision

The paper proposes a genuinely interesting idea — using a single B-NAF with weight deactivation for joint marginal/conditional entropy estimation — and provides empirical evidence that it reduces underestimation bias compared to discriminative methods on Gaussian benchmarks. However, the paper as presented suffers from two significant weaknesses: (a) promised long-run training experiments are missing, making the paper feel incomplete, and (b) the most directly comparable flow-based MI estimators cited in the introduction are not included in the evaluation, leaving the core comparative claim unsupported against the paper's own positioning. Additionally, the training procedure is described ambiguously enough to hinder reproducibility. These issues are addressable with major revision but prevent acceptance in the current form.

MY FINAL SCORE: <pineapple>5.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>