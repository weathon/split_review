Now I have all the information I need. Let me compose the consolidated review.

---

## Summary

This paper identifies a critical flaw in the standard definition of "semantic shift" for OOD detection: when the training setup aggregates fine-grained classes (e.g., dog breeds) into a coarse label (e.g., "dog"), the classifier treats breed-level variation as covariate rather than semantic, making novel breeds undetectable by post-hoc methods. The paper formalizes this by defining the **Semantic Space** as the span of differences between ID class-mean vectors and the **Covariate Space** as its orthogonal complement, then proves (Theorem 1) that shifts confined to the Covariate Space are undetectable by any post-hoc method built on the classifier's output. A "Tractable OOD" definition is proposed, requiring shifts in the Semantic Space. Experiments on synthetic data and a carefully designed ImageNet-dog protocol confirm the predictions, including the striking result that ten different post-hoc methods all score ~50% AUROC on novel dog breeds under a breed-aggregated training setup.

---

## Strengths

1. **Precise formal definitions of Semantic and Covariate Spaces (Definitions 1, 2).** The paper provides a rigorous mathematical decomposition of the input space based on ID class means. Proposition 1 gives operational meaning by showing that covariate components are constant across ID classes, so variation in the Covariate Space does not affect classification. This formalization is the paper's core conceptual contribution and directly addresses the ambiguity in existing definitions of "semantic shift."

2. **Theoretical proof of intractability for post-hoc methods (Theorem 1, Corollary 1).** Under stated assumptions (Gaussian data, linear classifier, Assumptions 1 and 2), the paper proves that if OOD and ID distributions have identical projections onto the Semantic Space, their output distributions under the classifier are indistinguishable (KL divergence of zero). This pins down *exactly* when post-hoc OOD detection must fail — a non-trivial and well-scoped theoretical result.

3. **Controlled, multi-method empirical validation.** The synthetic experiment (Table 1) shows all three methods at ~50% AUROC when Semantic shift is absent, regardless of Covariate shift. The ImageNet-dog experiment (Table 2, main paper) is even more compelling: under the "breed-aggregated" setup, **all ten** post-hoc methods drop to ~50% AUROC on OOD-breed detection, while under "breed-separated" they exceed 70%. The use of multiple methods, multiple random seeds, and visual evidence (t-SNE, confidence distributions) collectively provides strong support for the theory.

4. **Tractable OOD definition with quantitative δ parameter (Definition 4).** The paper redefines well-posed OOD based on distance in Semantic Space rather than arbitrary label difference. Table 2 (synthetic δ experiment) demonstrates monotonic improvement in AUROC as δ increases, showing the definition captures the actual difficulty of detection and provides a principled criterion for benchmark design.

5. **Weight matrix analysis confirming the mechanism (Figure 2).** The visualization of the linear classifier's weight matrix shows that weights corresponding to Covariate dimensions converge to zero during training, exactly as predicted by Proposition 2. This provides a clear mechanistic explanation for the intractability.

---

## Weaknesses

### Fatal
None.

### Major

1. **Theory is proven only for the linear-Gaussian case; the scope of the central claim extends beyond what is formally established.** Theorem 1 and Proposition 2 are proved for linear classifiers on Gaussian data with spherical covariance and leverage Assumptions 1 and 2 about classifier training. The paper then uses these results to draw conclusions about deep neural network classifiers on high-dimensional images. The ImageNet experiments show the predicted pattern holds for ResNet-18, which is encouraging but does not constitute a theoretical guarantee. The paper is honest about this in the Limitation section ("there remains a lack of theoretical proof for more general training scenarios"), but the abstract and introduction state the theoretical analysis as a general contribution without qualifying the scope up front. For example, the abstract says "we offer a more precise definition… allowing us to *theoretically analyze which types* of OOD distributions make the detection task intractable" — the reader could reasonably infer this analysis covers the nonlinear case. The gap between the restricted setting of the proof and the breadth of the conclusions merits more prominent caveating. (See also: Limitation section, lines 383–385.)

2. **The definition of Semantic Space depends entirely on the ID label set, making it difficult to operationalize for real benchmarks without additional analysis.** Definition 1 constructs the Semantic Space from differences between ID class means. Whether a given OOD sample is detectable depends on the specific ID classes chosen, not on any intrinsic property of the OOD sample. The paper acknowledges this as a feature, but does not provide a methodology for checking whether existing OOD benchmarks (e.g., CIFAR-10 vs. SVHN, ImageNet vs. iNaturalist) are "tractable" under this definition. A discussion of how to apply the framework to common benchmarks — even as a post-hoc analysis without new experiments — would significantly increase the paper's practical impact.

### Minor

1. **Assumption 2 (covariance sign matches weight sign) lacks a rigorous justification.** The paper provides an intuitive argument (positive weight → monotonically increasing function of input dimension → positive covariance) and validates the assumption in experiments (deferred to a section stripped by the parser). Given that this assumption is non-trivial for softmax classifiers where the prediction for class *i* depends on all weights, a brief formal justification or additional intuitive reasoning in the main text would help readers assess its reasonableness.

2. **The choice of consecutive class-means differences in Definition 1 is not justified.** The Semantic Space is defined using $\boldsymbol{\mu}_1-\boldsymbol{\mu}_2, \ldots, \boldsymbol{\mu}_k-\boldsymbol{\mu}_{k-1}$. Any basis for the span of all pairwise differences would yield the same space, but the paper does not explain why this particular ordered basis is chosen or note that the choice is arbitrary. This is a small clarity issue but worth addressing.

3. **The effect of class selection on variance in the ImageNet experiment is not analyzed.** The paper reports mean ± variance across three random seeds that select which 100 dog classes (and which 99 non-dog classes) to use. Different class subsets produce slightly different Semantic Spaces, which could contribute to the observed variance. A brief discussion of whether the variance is primarily due to sampling noise or to which specific classes are selected would strengthen the analysis.

### Trivial

1. **Line 75 forward reference.** The remark "this simplification does not compromise the validity of the conclusions presented in the subsequent sections" appears before the experiments are presented. While the experiments do validate this claim, the forward reference could be rephrased as a hypothesis rather than an assertion at that point.

---

## Nice-to-Haves

- **Discussion of extending the theory to nonlinear models.** The paper could add a brief informal discussion (even a paragraph in the Conclusion) about why the result is expected to hold more broadly — e.g., appealing to the fact that deep classifiers learn representations that are approximately class-discriminative and that the last linear layer's weights will be approximately orthogonal to within-class variations that are not discriminative. This would bridge the gap between the linear theory and the ImageNet experiments more satisfyingly.

- **Post-hoc analysis of existing OOD benchmarks under the proposed framework.** Even without running new experiments, a reasoned commentary on how popular benchmarks (CIFAR-10 vs. SVHN, ImageNet vs. iNaturalist, etc.) fare under the Tractable OOD definition would increase the paper's practical value.

- **A remark on whether post-hoc methods could be modified to detect Covariate shifts.** The paper states that Covariate shifts are undetectable by post-hoc methods built on the classifier's output. A brief clarifying sentence about whether approaches using density estimation in the feature space (rather than classifier outputs) could circumvent this limitation would improve reader understanding.

---

## Removed Points

These points were flagged for removal — treat them with caution:

- **"The proof (in appendix) is not visible"** (Harsh Critic, re: Proposition 2). — Removed. Appendix sections are stripped by the PDF parser; they exist in the original submission. The paper explicitly references the proof location.

- **"The remark that 'this simplification does not compromise the validity' is unsupported at this point."** — Removed. It is a forward reference to the experiments; papers commonly state expected conclusions before presenting evidence. The experiments do validate the claim.

- **"No method is proposed to *achieve* tractable OOD detection when the definition is violated."** — Removed. The paper's contribution is conceptual and analytical, not methodological. Criticizing it for not proposing a new detection method is scope creep.

- **"The paper does not discuss whether post-hoc methods could be modified to detect Covariate shifts."** — Removed. This asks the paper to solve a separate problem (detecting Covariate shifts) that is outside its stated scope.

- **Weaknesses related to the Semantic Space depending on ID labels being an "evidential issue for significance."** — Repositioned from the harsh critic's framing as a major evidential issue to Minor weakness #2 (operationalization gap). The paper correctly treats this as a feature, not a bug; the legitimate concern is the lack of guidance for applying the framework, not the dependence itself.

- **Strength Finder items about "the problem being important" or similar generic framing.** — All strengths retained were verified against the paper. No generic/superficial strengths were present in the Strength Finder output.

---

## Novel Insights

None beyond the paper's own contributions. The reviews surface useful framing about the scope gap and the need for operationalization, but these are refinements of the paper's own acknowledged limitations, not novel meta-insights.

---

## Suggestions

1. **Qualify the scope of the theoretical claim more prominently in the abstract and introduction.** Add a sentence such as: "Our theoretical analysis is conducted for linear classifiers on Gaussian data; we validate its predictions empirically for deep neural networks."

2. **Add a brief intuitive justification for Assumption 2 in the main text.** A one-sentence sketch of why the covariance sign should match the weight sign for softmax would help readers quickly assess the assumption without needing to work through the complexity themselves.

3. **Add a post-hoc analysis of existing OOD benchmarks in the Discussion section.** Even a short paragraph speculating how CIFAR-10 vs. SVHN, ImageNet-O, or iNaturalist fare under the Tractable OOD definition would greatly increase the paper's practical relevance.

4. **Acknowledge the arbitrariness of the consecutive-differences basis in Definition 1**, noting that any basis for the span of pairwise differences yields the same Semantic Space.

---

## Score and Decision

This is a strong paper with a clear conceptual contribution, sound theory within its stated scope, and compelling empirical validation. The weaknesses (scope gap between linear-Gaussian theory and the broader claims, and lack of practical operationalization guidance) are real but do not undermine the core contribution. The paper is honest about its limitations and the experimental evidence convincingly supports the theory.

**Score: 8.0 / 10**

MY FINAL SCORE: <score>8.0</score>
MY FINAL DECISION: <decision>Accept</decision>