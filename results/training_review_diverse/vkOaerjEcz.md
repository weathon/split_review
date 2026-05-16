## Summary

This paper introduces MTMC (Maximum Token Manifold Capacity), a simple regularization loss for Generalized Category Discovery (GCD) that maximizes the nuclear norm of the class-token matrix from a ViT backbone. Applied on top of existing GCD frameworks (SimGCD, CMS), MTMC prevents dimensional collapse by encouraging more uniform singular value distributions and higher von Neumann entropy. The method is remarkably concise (three lines of code), yields consistent accuracy gains across six benchmarks (notably +4.7% on ImageNet100 with SimGCD), and achieves 100% correct estimation of the number of categories on ImageNet100.

## Strengths

- **Consistent and often substantial accuracy gains across diverse GCD benchmarks.** Table 1 shows MTMC improves both SimGCD and CMS on all six datasets. The gains are particularly notable on ImageNet100 (+4.7% for SimGCD, +2.4% for CMS), Stanford Cars (+2.9%/+3.2%), and Aircraft (+2.3%/+1.2%). This is the paper's strongest evidence that the method works.

- **Superior estimation of the number of clusters (K).** Table 2 shows CMS+MTMC achieves 100% correct K estimation on ImageNet100 and reduces estimation error on every other dataset (e.g., from 5→3 on CUB). This is an impressive result that directly supports the claim that richer representations yield decision boundaries better aligned with true data structure.

- **Theoretical grounding connecting nuclear norm maximization to increased von Neumann entropy** (Theorem 1, Section 3.3). Figures 2, 4, and 5 provide empirical backing that MTMC produces more uniform eigenvalue distributions, higher entropy, and lower Frobenius norm—consistent with preventing dimensional collapse. The analytical results are clean and informative.

- **Extremely simple, plug-and-play implementation.** The core loss is three lines of code and requires no architectural changes. Figure 3 shows robustness to the sole hyperparameter λ and feature dimensionality D, lowering adoption barriers.

- **Honest analysis of limitations.** Section 4.3 candidly discusses why gains are smaller on CIFAR100 (low-resolution images lose high-frequency detail) and Herbarium19 (OOD data with high category overlap), demonstrating nuanced understanding of when the method is and isn't effective.

## Weaknesses

### Fatal
None.

### Major

- **The paper's central narrative — that MTMC enhances "intra-class representation completeness" — is not directly supported by the method's design or evidence.** The loss (Eq. 5) maximizes the nuclear norm of a matrix formed from *all unlabeled samples in a mini-batch*, irrespective of class. This is a *global* regularizer that prevents dimensional collapse in the overall feature space. The paper then reinterprets this global effect as specifically enriching *intra*-class representations, but never measures per-class representation quality (e.g., average per-class nuclear norm, per-class eigenvalue distributions, or intra-class pairwise distances relative to baselines). The claim is *plausible* (preventing global collapse likely helps individual clusters too) but *unsubstantiated by the form of evidence the paper promises*. Figures 4 and 5 analyze the global autocorrelation matrix, not class-conditional statistics. Either the paper should reframe the contribution as "a global collapse-prevention regularizer for GCD" (which would be a different, weaker claim) or provide class-conditioned measurements that directly link the method to richer intra-class structure. This mismatch between the narrative and the evidence is the paper's most significant weakness.

### Minor

- **No comparison to alternative collapse-prevention regularizers applied to the same backbone.** The paper shows MTMC improves over SimGCD and CMS, but does not ablate whether the gains come from nuclear-norm maximization *per se* or from *any* regularization that prevents dimensional collapse. Comparisons to simple baselines (e.g., ℓ2 penalty on feature covariance, Barlow Twins' redundancy-reduction term, or a uniform-loss regularizer applied to class tokens) would be needed to establish that nuclear norm is specifically beneficial. Without these, the novelty of the regularizer choice is unclear.

- **No variance reporting.** All results in Tables 1 and 2 appear to come from a single run. Given the modest gains on several datasets (CIFAR100: +0.5–1.0%; Herbarium19: +0.7–1.4%) and the known sensitivity of clustering to initialization, the absence of multiple seeds or confidence intervals makes it difficult to assess whether the improvements are reliable or within random variation.

- **Notation ambiguity in Section 3.1.** Equation (3) defines CTME as the nuclear norm of a single sample's class token. For a vector (which a single class token is), the nuclear norm equals its ℓ2 norm, which is 1 after normalization. The paper apparently intends the nuclear norm of a *matrix* of stacked class tokens, but this is not made explicit until Equation (5). The derivation would benefit from clearer notation distinguishing the single-token case from the batch matrix.

### Trivial

- The rendered equations contain minor formatting artifacts (broken characters in Eq. 5, garbled symbols throughout) — these are parser issues, not author errors, but the authors should ensure the camera-ready version is clean.

## Nice-to-Haves

- Add per-class measurements (e.g., average per-class nuclear norm of class-token matrices, or per-class eigenvalue distributions) to directly verify the intra-class completeness claim.
- Compare against other simple collapse-prevention losses (variance regularization, Barlow-Twins-style decorrelation) applied to the class-token matrix.
- Report main results over at least 3 random seeds with standard deviations.

## Removed Points

These points are flagged to be removed; treat them with caution:

- **Harsh critic's claim that "the method as described cannot deliver on the paper's promise" (structural/fatal framing):** This overstates the issue. The paper's empirical evidence (Tables 1–2, Figures 2, 4, 5) is consistent with the method working as intended, even if the *mechanism* narrative is slightly inflated. The critique is downgraded from "fatal/invalidates" to a Major weakness about the need for better evidence tying global regularization to intra-class effects.

- **Criticism about the introduction not answering the posed question:** The paper does answer "Can deep models... by enhancing the completeness of intra-class representations?" — it answers "yes, with MTMC" and provides Tables 1–2 as evidence. This is a matter of interpretation, not a factual omission.

- **Strength Finder's generic framing** — the claimed strengths about "novel perspective" and "honest analysis" are kept but not over-weighted, as they are somewhat generic.

- **Criticism about missing comparison to Barlow Twins/VICReg in Related Work section:** This is about experimental ablation, not missing citations. The paper's Related Work covers dimensional collapse methods adequately for context; the missing comparison belongs under experimental evaluation (already listed as a Minor weakness).

- **Criticism about the connection between MMCR and token-level reasoning being unexplained:** The motivation section (2.3) provides three explicit reasons for the token-level extension. The connection may not be rigorous but is clearly articulated.

## Novel Insights

None beyond the paper's own contributions. The reviews do not surface a perspective that the authors missed. The core observation — that a global nuclear-norm regularizer on class tokens improves GCD — stands as the paper's own contribution.

## Suggestions

1. **Reframe the contribution.** Either (a) present MTMC as a dimensional-collapse prevention regularizer for GCD (which matches the evidence), or (b) add per-class measurements (average nuclear norm within predicted clusters, per-class eigenvalue distributions) to directly support the intra-class completeness narrative.

2. **Add at least one alternative regularizer baseline.** Compare MTMC to a simple variance-regularization term or a Barlow-Twins-style decorrelation loss on class tokens, applied to the same SimGCD/CMS backbone. This would establish whether nuclear norm has specific advantages over other collapse-prevention techniques.

3. **Report results over multiple seeds.** For the main tables, even three seeds would greatly increase confidence, especially for datasets with modest gains.

## Score and Decision

The paper makes a clear empirical contribution: a simple, well-motivated regularizer that consistently improves GCD performance across multiple benchmarks, with particularly strong results on cluster-count estimation. The main weaknesses are (i) a narrative—evidence gap in the "intra-class completeness" framing and (ii) missing ablations against other regularizers. Neither is fatal; both are addressable with additional experiments or reframing. The method's simplicity, empirical consistency, and honest analysis of its limitations are genuine strengths. On balance, the paper merits acceptance.

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>