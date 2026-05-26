Now I have all the information needed. Let me compose the final consolidated review.

## Summary

This paper introduces **monitorability** as a property of neural networks — the intrinsic ability to detect inference errors from internal-layer activations — and proposes the **MIRA Score**, a practical metric that quantifies it using only in-distribution data and FGSM perturbations. The metric perturbs inputs toward decision boundaries, measures the separability of perturbed vs. unperturbed features via Mahalanobis distance (calibrated through a χ² surprisal transform), and integrates over perturbation magnitudes. Experiments across vision (CIFAR-10/100), tabular (Sensorless Drive), and NLP (SST-2 finetuning) with 4–5 architectures per domain show a consistent trend where models with higher MIRA also achieve higher OoD detection AUROC across three detectors (ODIN, Mahalanobis, Energy).

## Strengths

1. **First formal definition of monitorability (Definition 1, §3.2).** The paper provides the first mathematical characterization of when a model's internal representations can, in principle, be used to judge prediction quality. This fills a conceptual gap — prior work studied *how* to detect anomalies but not how to quantify *whether* a model's features make such detection possible.

2. **MIRA Score is a practical, data‑efficient metric (Definition 2, Eq. 4).** MIRA is computed entirely from in-distribution data using efficient FGSM perturbations, requires no OoD datasets or detector tuning, and the χ² surprisal calibration provides a dimension-agnostic scale. This makes it usable at pre-deployment time as a model selection tool.

3. **Cross-modal empirical validation with a clear trend.** The paper tests 4–5 diverse architectures per domain across vision (CNN, DenseNet, CustomNet, ViT), tabular (MLPs, Transformers), and NLP (RoBERTa, DistilBERT, ELECTRA, DeBERTaV3). In all three modalities, higher MIRA scores correspond to higher best-achievable OoD AUROC. The contrast is particularly stark at the extremes: ViT (MIRA=89.25, AUROC≈99%) vs. CustomNet (MIRA=−0.07, AUROC≈44–78%) on CIFAR-10; WideMLP (MIRA=63.5, AUROC≈93%) vs. DeepTransformer (MIRA=4.37, AUROC≈78%) on tabular; DeBERTaV3 (MIRA=3794, AUROC≈86%) vs. DistilBERT (MIRA=2016, AUROC≈77%) on NLP. This consistency across fundamentally different data types and architectures strengthens the case that MIRA captures something general about representation quality.

4. **Comprehensive evaluation scope.** The use of three OoD detectors (ODIN, Mahalanobis, Energy) based on different principles, multiple OoD datasets per domain, and architectures ranging from small custom CNNs to pretrained ViTs and transformers provides broader evidence than is typical for a first-introduction paper.

## Weaknesses

### Fatal
None.

### Major

1. **Validation proxy does not fully align with the definition.** Definition 1 frames monitorability as the ability to determine whether a prediction is correct (or erroneous) from internal-layer activations — this covers *all* error types, including misclassifications on in-distribution inputs. The experimental validation, however, is limited entirely to OoD detection performance. The paper itself acknowledges (§2) that "misclassifications may also occur for ID inputs, which is a distinct scenario not directly addressed by OoD detection," yet the validation never tests this scenario. Because MIRA uses FGSM perturbations (which can cause misclassifications by crossing decision boundaries), it is plausible that the metric captures error-detectability more broadly — but this is not demonstrated. Without a direct link to ID error detection, the paper's central claim that MIRA measures "the intrinsic ability of a model to highlight potential inference errors" (Abstract) is only partially supported.

2. **Correlation claim lacks statistical quantification.** The paper asserts that MIRA "consistently correlates" with detection performance, but the evidence is entirely qualitative: no rank correlation coefficient (Spearman or Kendall) is reported, no confidence intervals are given, and there is no scatter plot relating MIRA to best AUROC. With only 4–5 models per domain, the sample is too small for strong statistical inference. While the overall trend is visually apparent (high-MIRA models tend to have high detection AUROC, and vice versa), the strength and reliability of the claimed correlation cannot be assessed. Exceptions to the monotonic trend exist (e.g., in Table 2, DeepMLP MIRA=12.71 with best AUROC=86.24, while Transformer MIRA=7.87 with best AUROC=85.36 — the ordering flips), and the paper neither acknowledges nor explains them. The claim of "good correlation" (Discussion, §4.4) needs to be backed by quantitative evidence.

3. **Small number of models per domain limits generalizability.** With 4 models for vision (per dataset), 5 for tabular, and 4 for NLP, it is difficult to determine whether the observed trend is robust or driven by a few extreme points (e.g., ViT vs. CustomNet on CIFAR-10). A larger model zoo (e.g., 10+ architectures per domain) would substantially strengthen the claim that MIRA is a reliable comparative tool.

### Minor

1. **Potential confounding between MIRA and the validation detector set.** MIRA uses Mahalanobis distance (via the χ² surprisal) to measure feature separability, and one of the three detectors used to define "best achievable detection performance" is itself the Mahalanobis-based detector (Lee et al., 2018b). In many blocks — especially NLP (all four models) and tabular (all five) — the Mahalanobis detector is the best performer, so the "best AUROC" is largely determined by the same geometric principle used in MIRA. This does not invalidate the results: the trend holds even when Mahalanobis is *not* the best detector (e.g., DenseNet on CIFAR-10, where Energy outperforms Mahalanobis but the MIRA ordering still aligns). However, the concern deserves explicit discussion and ideally a sensitivity analysis that excludes the Mahalanobis detector from the "best-of" aggregation.

2. **Unvalidated assumptions behind the metric.** (a) The paper uses FGSM perturbations intended to move inputs toward decision boundaries, but never reports what fraction of perturbed inputs actually change the model's prediction. If most remain correctly classified, MIRA primarily measures feature sensitivity to gradient-direction perturbations rather than error detectability. (b) The χ² calibration of the surprisal score relies on a class-conditional Gaussian assumption inherited from Lee et al. (2018b), but no diagnostic (Q–Q plot, normality test) is provided for any of the 13 models tested. If the assumption is violated, the surprisal values become uninterpretable. (c) The accuracy-reduction threshold used to define ε_min is only specified in the appendix (Appendix B.6), and no sensitivity analysis is given for how different thresholds affect MIRA values or model rankings.

3. **No uncertainty estimates on MIRA.** The MIRA score is computed from a finite set of ID samples and a discretized integral over ε, but no bootstrap confidence intervals or variance estimates are reported. Without these, it is unclear whether the observed MIRA differences between models (e.g., ResNet-18 at 6.05 vs. DenseNet at 16.01 on CIFAR-10) are statistically meaningful or could arise from sampling noise.

4. **p(ε) and discretization unspecified.** The MIRA definition includes an integral over ε with a user-defined distribution p(ε). The paper says "for example, choosing p(ε) uniform" but does not state what was actually used in the experiments, nor the discretization scheme for the integral. These implementation details affect reproducibility.

### Trivial
None of substance that are not parser artifacts.

## Nice-to-Haves

- **Direct validation on ID error detection.** Augment the OoD proxy with a setup where errors are induced on ID inputs (e.g., using the same FGSM perturbations at magnitudes that actually flip predictions, or using naturally misclassified ID samples) and test whether MIRA predicts the detectability of these errors. This would directly connect the metric to Definition 1.

- **Quantify the correlation.** Provide a scatter plot of MIRA vs. best-achievable AUROC with a Spearman rank correlation and bootstrap confidence intervals. If the number of models per domain is too small for meaningful correlation, aggregate across domains (using normalized MIRA and AUROC) or add more architectures.

- **Compare against simpler baselines.** Report how MIRA compares to trivial proxies for "monitorability" such as mean softmax confidence, average feature norm, or intra-class / inter-class distance ratio. If a simpler alternative correlates equally well with OoD performance, the paper's contribution is weakened and should be acknowledged.

- **Disentangle the confound.** Recompute the "best achievable" detection by excluding Mahalanobis-based detectors, or compare MIRA against each detector individually.

- **Report wall-clock time.** The paper claims MIRA is efficient (RQ4) but provides no runtime comparison against tuning multiple OoD detectors.

## Removed Points

These points are flagged to be removed; treat them with caution.

1. **Harsh Critic's "ResNet-18 vs. DenseNet ordering reversal" example** — The critic claims this contradicts the paper's claim because ResNet-18 (MIRA=6.05) has higher Mahalanobis AUROC (~93.4%) than DenseNet (MIRA=16.01, Mahalanobis ~90.1%). However, the paper's claim is about correlation with the *best achievable* detection performance, not Mahalanobis individually. For DenseNet, the best detector is Energy (~94.29%), which is higher than ResNet-18's best (Mahalanobis ~93.38%). The ordering is therefore consistent with the paper's claim. This criticism misunderstands the validation protocol.

2. **Harsh Critic's "Definition 1 is not operationalizable"** — The paper explicitly frames Definition 1 as an "abstract formalization" (§3.3, first sentence) and immediately proposes MIRA as a practical metric that approximates it. The critic's observation is accurate at a philosophical level but does not identify a flaw — the paper does not claim Definition 1 is directly checkable.

3. **Harsh Critic's "t-SNE can create spurious separations"** — While technically true of t-SNE, this is standard practice for qualitative visualization. The t-SNE plots are presented as illustration, not as primary evidence. The quantitative evidence is in Tables 1–3. This criticism does not threaten any core claim.

4. **Strength Finder's "t-SNE visualizations confirm the structural interpretation"** — This strength is somewhat overclaimed; the t-SNE plots are illustrative but not confirmatory evidence. However, since the primary evidence is in the tables, the t-SNE visualization is a reasonable supporting illustration and is kept in the Strengths section only as a minor supporting point.

## Novel Insights

The reviews surface two observations that go beyond the paper's own analysis:

1. **The metric-validation confound is asymmetric across domains.** The potential circularity (MIRA uses Mahalanobis, the validation set includes Mahalanobis) is a real concern in NLP and tabular experiments, where Mahalanobis is the dominant detector. But in the vision experiments, Mahalanobis is not always the best detector (e.g., DenseNet on CIFAR-10), and the correlation still holds. This asymmetry suggests the confound is not fatal but deserves domain-specific discussion — a nuance the paper does not address.

2. **The paper's core claim is more precisely "MIRA predicts which model will perform best under OoD detection" rather than "MIRA measures error-detectability in general."** The formal definition promises the latter, but the validation only delivers the former. This gap, which both the paper and the reviewer identify, could be closed with relatively modest additional experiments (e.g., detecting FGSM-caused flips on ID data), and doing so would substantially strengthen the paper.

## Suggestions

1. **Add a scatter plot with Spearman correlation** — For each domain, plot MIRA vs. best-achievable AUROC, report the rank correlation coefficient with a bootstrap CI. This single addition would address the most significant weakness (qualitative correlation claim) with minimal new computation.

2. **Add an ID error detection experiment** — Use the same FGSM perturbations (at magnitudes that cause actual misclassifications) and measure whether a simple detector (e.g., Mahalanobis distance on penultimate-layer features) can distinguish correct from incorrect predictions. Show that models with higher MIRA make these errors more detectable.

3. **Exclude Mahalanobis from the "best-of" aggregation** in a supplementary analysis to verify that the correlation is not driven by the shared geometric principle.

4. **Report the fraction of FGSM-perturbed inputs that change class**, and show that MIRA values are stable across different accuracy-reduction thresholds (ε_min) via a sensitivity analysis.

5. **Add error bars on MIRA values** (e.g., bootstrap over ID samples) to allow readers to assess whether model differences are meaningful.

6. **State the actual p(ε) and discretization used** in the experiments (even briefly in the main text) for reproducibility.

## Score and Decision

The paper initiates a genuinely new direction — formalizing and quantifying a model's "monitorability" — and provides a plausible first metric with cross-modal evidence. However, the validation has significant gaps relative to the paper's own definition (OoD proxy vs. error detection), the central correlation claim is asserted qualitatively without statistical support, and key metric assumptions go unexamined. These issues are addressable but currently weaken the contribution.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>