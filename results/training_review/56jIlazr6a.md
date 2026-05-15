Now I have all the information needed. Here is my consolidated review.

---

## Summary

This paper introduces Unified Uncertainty Calibration (U2C), a framework that combines aleatoric and epistemic uncertainties into a single calibrated softmax over \(c+1\) classes (the original \(c\) in-domain classes plus an out-domain abstention class). Instead of the standard reject-or-classify (RC) rule — which hard-thresholds an epistemic uncertainty score — U2C learns a non-linear calibration function \(\tau_u\) that maps the epistemic uncertainty estimate into a \((c+1)\)th logit, then produces a softmax that allows continuous trading off between in-domain classification and abstention. The paper provides a theoretical decomposition comparing RC and U2C (Lemmas 5.1, 5.2) and reports experiments on ImageNet benchmarks covering in-domain, covariate shift, near-OOD, and far-OOD settings with four different epistemic uncertainty estimators.

## Strengths

- **Soft, joint calibration of aleatoric and epistemic uncertainties**: U2C replaces RC's hard binary threshold with a shared softmax over \(c+1\) classes, directly addressing the three problems identified with RC (no communication between uncertainty sources, miscalibrated binary decisions, inability to correct misspecified uncertainty estimates). This is formalized in Section 4 (Eq. 8) and is the paper's core conceptual contribution.

- **Formal theoretical comparison with RC**: Lemmas 5.1 and 5.2 decompose the error and NLL differences between RC and U2C as functions of probability mass in the four decision regions \((A,B,C,D)\). While not deep theorems, they make precise the intuitive conditions under which each method wins, and correctly highlight that RC produces degenerate (infinite) NLL on entire regions that U2C handles softly.

- **Consistent empirical improvement across benchmarks and uncertainty estimators**: Table 1 reports results for 9 benchmarks × 4 epistemic uncertainty methods (MaxLogit, ASH, Mahalanobis, KNN). The pattern of improvement with only rare, small deteriorations is the best evidence that U2C delivers on its central claim.

- **Framework agnostic to the choice of epistemic uncertainty estimator**: The method works with logit-based, feature-reshaping, distance-based, and nearest-neighbor uncertainty estimates, demonstrating generality beyond any single detector.

- **Insightful quadrant-of-knowledge framing**: The decomposition into known-knowns, known-unknowns, unknown-knowns, and unknown-unknowns (Section 4) provides a useful conceptual vocabulary, even if metaphorical.

## Weaknesses

### Fatal
None.

### Major

1. **Insufficient baselines to support the claimed scope.** The paper compares U2C *only* against reject-or-classify (RC). While RC is the standard approach for *combining* uncertainty estimates into a \(c+1\) prediction, the paper's introduction claims U2C "yields state-of-the-art performance across a variety of standard ImageNet benchmarks." This claim is not supported. To substantiate "state-of-the-art," the paper would need to compare against at least one or two methods that produce calibrated \(c+1\)-dimensional predictions (e.g., learning to abstain with a reject option via an augmented softmax baseline, or methods that add a learned constant logit). The comparison against RC alone establishes that U2C improves over the standard practice, which is a genuine contribution, but the paper overclaims by implying broader SOTA.

2. **Missing specification of \(\tau_u\) (the epistemic calibration function).** The paper describes \(\tau_u\) as a "non-linear epistemic calibration function" (Section 4) and optimizes its parameters via cross-entropy on the relabeled validation set, but never states its functional form — is it a small neural network? A spline? A polynomial? This is a critical reproducibility gap. Without this detail, readers cannot re-implement or assess the capacity of the learned mapping.

3. **No ablation of the relabeling design choice.** Section 4 relabels the top 5% most uncertain in-domain validation examples as \(c+1\) to create training signal for the abstention class. The paper neither justifies this design choice quantitatively nor ablates it (e.g., varying the fraction, or testing alternative strategies such as relabeling only misclassified examples). The Discussion (Section 7) raises this as an open question ("could it be beneficial to explicitly relabel confident in-domain mistakes...?"), which suggests the authors are aware more analysis is needed. While relabeling is a reasonable proxy for creating abstention training signal, its effects on the method's behavior should be studied.

### Minor

- **Base classifier architecture and training details are absent.** The paper does not state which architecture is used for the main experiments (it mentions ResNet152 and ViT-32-B only as additional experiments in a deferred appendix). Standard practice on ImageNet experiments requires specifying the backbone, pretraining source, and any fine-tuning. Without this, the results are not reproducible.

- **Hyperparameters of epistemic uncertainty methods are unspecified.** The paper uses four different uncertainty estimates (MaxLogit, ASH, Mahalanobis, KNN) but does not report key hyperparameters (e.g., \(k\) for KNN, the pruning fraction for ASH). These matter for reproducibility.

- **The "state-of-the-art" claim in the introduction is not supported by the experimental design.** The abstract claims only that U2C "significantly outperforms reject-or-classify," which is supported. But the introduction's claim of "state-of-the-art performance" overstates what the experiments demonstrate.

- **No error bars or variance estimates.** The paper asserts "no randomness involved in our experimental protocol" because the data splits are fixed. If a fixed pretrained backbone is used and the remaining steps are deterministic, this is defensible — but the paper should explicitly state that a fixed pretrained model is used to rule out training randomness.

### Trivial
None.

## Nice-to-Haves

- Reporting standard OOD detection metrics (AUROC, FPR@95TPR) as a complement to err/ece would help connect with the broader OOD detection literature. The paper's chosen metrics (err, ece over \(c+1\) classes) are appropriate for its stated goals, but adding AUROC/FPR would make the results more widely comparable.

- An ablation varying the relabeling fraction \(\alpha\) (e.g., {0.01, 0.05, 0.10, 0.20}) would clarify the sensitivity of U2C to this design parameter and whether the 5% choice is critical.

- Showing concrete examples of relabeled validation images (the top 5% most uncertain in-domain examples) would help readers assess whether these are genuinely ambiguous/misclassified cases or simply high-uncertainty correct predictions.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **Harsh critic's claim that the relabeling step is a "fundamental design flaw that invalidates the method"** — This is an overstatement. The relabeling of the 5% most uncertain in-domain validation examples as \(c+1\) is a deliberate design choice to create training signal for the abstention class. Without any signal for the \((c+1)\)th label, the model would never learn to predict abstention on in-domain data. While the paper should ablate this choice (kept as a minor weakness above), calling it "data corruption" or a "contradiction" mischaracterizes a standard proxy-training technique. The method does not "teach itself that 5% of in-domain examples are out-of-domain" in the training of \(f\); it creates a calibration-stage supervisory signal for \(\tau_u\) using the most uncertain examples as proxies.

- **Criticism about error bars being missing** — The paper's justification ("no randomness involved in our experimental protocol — the splits were computed once and set in stone") is reasonable if a fixed pretrained backbone is used. The claim is not inherently false as asserted.

- **Complaint that "Table 1 is garbled"** — This is a PDF-extraction artifact, not an author error.

- **Demand that the paper compare against methods like ODIN or Energy-based OOD detection** — These are OOD *detection* methods, not methods for unified *calibration* producing \(c+1\)-dimensional predictions. The paper's contribution is about combining aleatoric and epistemic uncertainties into a calibrated joint prediction, which is a different task. The relevant baseline for this task is RC, which the paper does compare against. (The paper still overclaims SOTA, as noted in Major weakness 1.)

- **Criticism that Lemmas 5.1 and 5.2 are "trivial" or "not deep"** — A matter of opinion. They provide formal decomposition that makes precise the conditions under which each method wins, which is a valid theoretical contribution even if modest.

## Novel Insights

The finding that most of the harsh critic's "fatal" objections dissolve upon a careful reading of the paper is, in itself, instructive. The relabeling step is not a contamination of training data but a necessary design choice to create a training signal for the abstention class. The more interesting insight emerging from the reviews is the tension between the paper's modest experimental scope (one baseline, RC) and its ambitious claim ("state-of-the-art"). The paper actually delivers on its core stated contribution — showing that a soft, jointly calibrated combination of aleatoric and epistemic uncertainty consistently outperforms the hard-threshold RC baseline — but weakens itself by claiming more than it has demonstrated. A paper that honestly claimed "U2C consistently improves over reject-or-classify" with the current evidence would be stronger than one that overreaches to "state-of-the-art."

## Suggestions

1. **Remove or qualify the "state-of-the-art" claim.** Replace it with the more accurate "significantly outperforms reject-or-classify across a variety of standard benchmarks," which is what the experiments actually support.

2. **Specify the functional form of \(\tau_u\)** in the main paper or an appendix. Even a brief statement (e.g., "a two-layer MLP with 64 hidden units and ReLU activation, trained for 100 epochs with Adam at learning rate 0.001") would resolve a major reproducibility concern.

3. **Add an ablation varying the relabeling fraction \(\alpha\)** on at least one benchmark + uncertainty estimator pair to demonstrate sensitivity to this design choice.

4. **Add a simple competitive baseline** — for example, a baseline that appends a learned constant logit or a linear function of \(u(x)\) without the non-linear calibration — to isolate the contribution of the non-linear \(\tau_u\).

5. **State the base architecture explicitly** in the main text, not deferred to an appendix, for self-containedness.

6. **Report AUROC/FPR@95TPR** as supplementary metrics so readers can situate U2C within the broader OOD detection literature, even though the paper's primary metrics (err, ece) are appropriate for its goals.

## Score and Decision

The paper makes a genuine contribution: a clean framework for jointly calibrating aleatoric and epistemic uncertainties that demonstrably improves over the standard reject-or-classify practice across diverse settings. The theoretical analysis, while not deep, is sound. The main weaknesses are overclaimed scope (state-of-the-art without sufficient baselines) and missing implementation details (form of \(\tau_u\), architecture specification, hyperparameters). None of these invalidate the core results; they are addressable in revision. However, the paper as submitted does not fully deliver on its advertised claims, which prevents it from being accepted at its current strength.

MY FINAL SCORE: <pineapple>6.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>