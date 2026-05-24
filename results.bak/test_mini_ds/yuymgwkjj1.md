Now I have a good picture. Let me write the consolidated review.

**Round 1 bracket**: 4.5–6.5 based on the initial wide search (weak anchors ~2–3, middle anchors 4–7, strong anchors 8+). The paper sits squarely in the middle range.

**Round 2 narrowing**: After inspecting AVOID (6.00), Explaining OOD Paradox (5.67), HamOS (6.75), OOD Detection with Synthetic Data (4.75), and Double Descent Meets OOD (6.50), I place the paper at approximately 5.5. It is weaker than AVOID (less thorough experiments, no theoretical decomposition) and the Explaining OOD Paradox paper (less theoretical depth), but stronger than the straightforward "OOD Detection using Synthetic Data Generation" (4.75) because it has a principled motivation tied to the known complexity bias and a method that generalizes across modalities.

---

## Summary

This paper addresses the well-known likelihood bias in normalizing flows for OOD detection — flows tend to assign inflated likelihoods to low-complexity OOD inputs. The authors propose generating synthetic low-complexity outliers (via Gaussian blur + augmentations for images; length filtering + synonym replacement for text) and training with a softplus-based adversarial likelihood objective that penalizes high likelihoods on these outliers. Experiments on image benchmarks (CIFAR-10/100, SVHN, LSUN, iSUN, CelebA, and high-dimensional medical/blur/quality datasets) and text benchmarks (IMDb as ID, four OOD sets) show consistent AUROC/FPR95 improvements over the MLE baseline, often matching or exceeding training with a limited number of real outliers.

## Strengths

1. **Consistent and often large empirical improvements**: Across Tables 2, 3, 5, and 6, the proposed Gaussian+CCM variant substantially improves over vanilla MLE. For instance, CIFAR-10 → SVHN: AUROC rises from 79.2% (MLE) to 97.6% (Gaussian+CCM). These gains are not cherry-picked; they hold across nearly every ID–OOD pair reported.

2. **Synthetic outliers match or exceed real outliers without requiring labeled OOD data**: In several settings (e.g., CIFAR-100 ID, LSUN OOD: 98.8% vs. 96.9% for real outliers), the fully unsupervised synthetic outlier approach performs comparably or better than using 10% real OOD data. This is the paper's strongest practical claim and is directly supported by the tables.

3. **Modality-agnostic design**: The method transfers cleanly from images to text, with Table 6 showing non-trivial AUROC gains (e.g., +35.1% on SST-2). The synthetic outlier generation strategy is adapted to each modality's structure but follows the same principle, which strengthens the claim that the approach is general.

4. **Ablation of synthetic outlier components**: Tables 2 and 3 decompose the effect of Gaussian blur alone, CCM augmentation alone, and their combination, showing that the full pipeline yields the best or near-best results. This provides useful evidence for the design choices.

5. **Clean softplus-based objective**: The softplus formulation (Section 2.3) avoids the manual threshold selection needed by prior clamping approaches (Schmier et al., 2022), and the bounded loss surface (illustrated in Figure 1) is a reasonable technical improvement for training stability.

## Weaknesses

### Fatal
None.

### Major

1. **The evaluation does not isolate the complexity-ordering mechanism central to the paper's motivation.** The entire paper is motivated by the claim (Hypothesis 1, Table 1) that normalizing flows fail when ID is *more complex* than OOD, and the method is "specifically designed to correct the bias toward simpler OOD inputs" (Section 2.1). Yet the experimental results (Tables 2, 3, 5, 6) present aggregate metrics per OOD dataset without stratifying by the complexity ordering of the ID–OOD pair. The paper acknowledges that the complexity-adjusted score "can be misleading" when OOD is more complex (Section 3.1), but this caveat is about the *scoring* method, not the *training* mechanism. If the method also improves performance in cases where OOD is *more* complex than ID (where no bias exists in the first place), the claimed mechanism is not "bias correction" but something closer to general regularization. A stratified analysis — reporting performance separately for (a) ID less complex than OOD, (b) ID more complex than OOD — is needed to substantiate the core claim. This is the most consequential weakness because it directly undermines the paper's stated contribution.

2. **The Lipschitz constant analysis does not provide meaningful evidence for the claimed mechanism.** Table 4 reports that the Lipschitz constant (estimated as the maximum gradient norm over 1000 random samples) increases after training with synthetic outliers. However, estimating a *supremum* over the entire domain by taking a maximum over a finite sample of 1000 points is a well-known poor estimator. The paper provides no causal evidence linking this increase to OOD detection performance (e.g., no correlation analysis, no local Lipschitz measurements around ID vs. OOD samples, no ablation controlling for other training differences). The increase could be an artifact of any number of training changes. This section reads as an afterthought rather than a meaningful validation, and the claim that it "supports the hypothesis" is over-stated relative to the evidence provided.

### Minor

3. **Limited baseline comparisons.** The core comparisons (Tables 2, 3) are against (a) vanilla MLE and (b) training with 10% real outliers. The paper does compare to complexity-adjusted scoring (Serra et al., 2020) as a post-hoc method, which is the most directly relevant bias-correction baseline. However, there is no comparison to other established bias-mitigation techniques for normalizing-flow OOD detection, such as the typicality test (Nalisnick et al., 2019) or likelihood ratios (Ren et al., 2019) applied to an MLE-trained flow. While the paper's contribution is primarily about *training* rather than *scoring*, these baselines would help contextualize whether synthetic-outlier training is genuinely more effective than alternative ways to address the bias.

4. **No error bars or statistical significance reported.** All tables report point estimates without standard deviations, confidence intervals, or indication of multiple seeds. Given randomness in outlier generation (random augmentation selection, Gaussian blur, synonym replacement), single-run results could be misleading. This is a notable omission, especially in the high-dimensional experiments (Table 5) and the text experiments (Table 6) where the dataset is small (1000 training samples).

5. **Text evaluation is limited in scope.** Only one ID dataset (IMDb, 1000 samples) is used for text experiments. The dramatic +35% AUROC gain on SST-2 is presented without analysis of the relative complexity of SST-2 vs. IMDb, leaving it unclear whether this is bias correction or simply a large distributional mismatch that is easy to exploit. The text outlier generation (length filtering + synonym replacement) is not ablated — no experiment separates the contribution of each component.

6. **No ablation comparing the softplus objective against the clamped negative log-likelihood baseline it claims to improve upon.** The paper contrasts its softplus approach with the manual thresholding used by Schmier et al. (2022) but never runs an experiment with the clamping baseline to demonstrate that softplus is actually better. This weakens the claim that the softplus design is a concrete improvement.

7. **The complexity-adjusted scoring is used selectively.** The paper applies complexity-adjusted scoring in some settings but not others, with the rationale that it "can be misleading" on higher-complexity OOD datasets. While this is acknowledged, it would strengthen the evaluation to apply a consistent scoring rule or to systematically compare both scoring approaches across all settings and discuss the trade-offs explicitly.

8. **The connection between the complexity measure for text and individual-sample scoring is unclear.** Text complexity is defined as (gzip-compressed dataset size)/(number of texts), which is a *dataset-level* quantity. It is used in Section 2.1 to order datasets by complexity, but the paper does not specify how this relates to the per-sample scoring used in the text experiments (which uses likelihood-based scoring). This is not a critical flaw but creates ambiguity about how the complexity ordering is operationalized at inference time.

### Trivial

- The Gaussian blur kernel radius of "1" is not specified in terms of pixels vs. sigma units.
- Figure 3 shows the complexity-vs-likelihood scatter plot for only one ID dataset (CIFAR-10). A similar plot for other ID datasets would strengthen the qualitative demonstration.

## Nice-to-Haves
- A comparison of the proposed method against post-hoc bias-correction scoring methods (typicality test, likelihood ratio) applied to an MLE-trained flow would clarify whether the training-time correction is complementary to or redundant with these approaches.
- An analysis of the quality and complexity of synthetic text outliers (e.g., do they actually have lower gzip complexity than ID samples?) would validate the text outlier generation procedure.
- A hyperparameter sensitivity study for the outlier generation probability (set to 0.5 in the paper) would help assess practical robustness.

## Removed Points

- *"The synthetic outlier generation for images depends on augmentations (CutPaste, CutMix, MixUp) that were originally designed for supervised or semi-supervised learning... blurs the line between unsupervised and exposure-based methods."* — These are data augmentation techniques applied without labels; using them does not turn the method into a supervised approach. The paper's setup remains unsupervised.

- *"Comparison baselines are too weak and incomplete to justify claims"* — This criticism is overstated because the paper does compare against complexity-adjusted scoring (the most directly relevant bias-correction baseline). The concern about missing likelihood-ratio/typicality baselines is valid but more minor, and is retained in Minor Weakness #3 in a tempered form.

- *"The paper does not position its method relative to the current best OOD detection methods for normalizing flows"* — The paper positions itself relative to the MLE baseline and real-outlier training, which is standard for this type of contribution. Requesting full SOTA comparison is scope creep for a method paper focused on correcting a specific bias.

- *"Image complexity... the paper does not discuss whether using these augmentations constitutes exposure to OOD data that is not truly 'unsupervised'"* — Using augmentations on ID data without labels is still unsupervised. This criticism reflects a misunderstanding.

- Several formatting/style nitpicks from the section-by-section notes (Gaussian kernel radius specification, missing details about augmentation probabilities) are retained in a minor/trivial form rather than as substantive weaknesses.

## Novel Insights

None beyond the paper's own contributions. The reviews do not surface a perspective that the paper itself does not already contain or imply.

## Suggestions

1. **Stratify results by complexity ordering** (ID more complex than OOD vs. ID less complex vs. similar). This is the single highest-impact revision: it would directly test whether the method corrects the claimed bias or is a general regularizer.

2. **Replace the Lipschitz analysis** with something more meaningful, or drop it entirely. If kept, use local Lipschitz estimates (finite differences around ID vs. OOD samples) and correlate them with per-sample detection performance.

3. **Add error bars** (at least 3 random seeds) to all main tables.

4. **Add the clamping baseline** (Schmier et al., 2022) as an ablation for the softplus objective to substantiate the claim that softplus is an improvement.

5. **Expand the text experiments** with at least one additional ID dataset and an analysis of the complexity of synthetic text outliers relative to ID data.

## Score and Decision

**Round 1 bracket**: 4.5–6.5 (after retrieving anchors in the 0–3, 4–7, and 8+ bands).

**Round 2 narrow**: 5.0–6.0. After reading AVOID (6.00, thorough theoretical+experimental, rejected), the Explaining OOD Paradox paper (5.67, theoretical depth, rejected), HamOS (6.75, accepted), and the synthetic OOD data paper (4.75, weaker method, rejected), I position the current paper at 5.5. It is methodologically cleaner than the 4.75 anchor but has less thorough evaluation and weaker theoretical support than the 5.67 and 6.00 anchors.

**Anchors used**:
| Paper | Avg Score | Round | Comparison |
|---|---|---|---|
| rcmhydaEJp (Flow-based imputation) | 3.00 | R1 | Less relevant topic, lower quality |
| v8RDgaEtE2 (Regression CP under bias) | 2.50 | R1 | Unrelated topic, much weaker |
| jQ596tXT3k (Explaining OOD Paradox) | 5.67 | R1,R2 | Similar topic; more theoretical depth, less cross-modal evidence; current paper slightly weaker overall |
| gRXLa6LS3J (Zero-shot OD via synthetic pretraining) | 5.75 | R2 | Different approach to synthetic OD; comparable quality |
| N6ba2xsmds (HamOS) | 6.75 | R1 | Synthetic outlier generation via HMC, accepted; current paper less sophisticated methodologically |
| 7QDIFrtAsB (Anomaly Detection via Gradients) | 5.75 | R1 | Different method (score networks for tabular data); comparable quality |
| ZCOwwRAaEl (Latent BO via NF) | 8.00 | R1 | High-quality, accepted; not comparable (different problem) |
| I5lcjmFmlc (Robust Classification via Diffusion) | 8.00 | R1 | High-quality; not comparable |
| 3a505tMjGE (AVOID) | 6.00 | R2 | Similar problem (DGM overestimation for OOD), more thorough experiments and theory; current paper slightly weaker |
| eN0RyRVbSm (Double Descent meets OOD) | 6.50 | R2 | Theoretical contribution + extensive experiments; current paper less ambitious |
| zUrdd5NRLH (GROD) | 5.00 | R2 | Transformers for OOD detection; lower quality |
| 8mM5NzC7da (OOD Detection using Synthetic Data) | 4.75 | R2 | Similar concept (synthetic OOD data generation) but weaker motivation and evaluation; current paper is stronger |
| 7ZUUNMjM9T (Flow Matching Trace Objective) | 4.00 | R2 | Flow-based but different objective; lower quality |
| kRjLBXWn1T (Correcting Flows with Marginal Matching) | 5.25 | R2 | Flow correction method; comparable quality but less direct relevance |

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>