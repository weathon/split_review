Now I have all the information I need. Let me construct the final consolidated review.

---

## Summary

GeoTimeCLIP introduces a joint framework for simultaneously predicting both the capture time (month and hour) and geo-location of an image using a retrieval-based approach. The method uses three encoders (image, location, time) aligned in a shared embedding space, with two key innovations: (1) a cyclical time representation using Random Fourier Features on a toroidal manifold, and (2) a Temporal Metric Learning loss that replaces hard-positive/negative contrastive learning with soft targets based on temporal distance. Experiments on SkyFinder (time prediction) and Im2GPS3k/GWS15k (geo-localization) show that joint training improves time prediction over time-only baselines, the proposed loss outperforms contrastive and ranking alternatives, and geo-localization is competitive with dedicated expert methods.

## Strengths

- **Temporal Metric Learning loss substantially outperforms alternatives (Table 2):** The proposed loss achieves significantly lower month and hour errors than CLIP-based contrastive loss, Rank-N-Contrast, and the geo-localization contrastive loss with false-negative masking. This directly validates the paper's core methodological claim that soft targets based on temporal distance are more suitable for image-time alignment than hard-negative approaches.

- **Jointly training time and location improves time prediction over time-only models (Table 1):** GeoTimeCLIP (joint) outperforms TimeCLIP (time-only), showing that the geo-localization objective provides useful inductive biases for time prediction. This supports the paper's central thesis that the two tasks are complementary.

- **Competitive geo-localization against dedicated expert methods (Table 5):** GeoTimeCLIP achieves state-of-the-art at the 1 km threshold on GWS15k (0.415 vs. 0.368 for PIGEOTTO) and competitive results on Im2GPS3k — notable for a jointly trained model that does not use auxiliary metadata and has 15× fewer parameters than the MLLM-based Img2Loc.

- **Robustness to limited training data and label noise (Tables 3–4):** With only 10% of the data (~12.5k samples), month error increases by only ~0.3 months, and the model handles injected Gaussian noise up to σ=2 without major performance degradation. This demonstrates practical robustness.

- **Cyclic time representation with toroidal distance is empirically beneficial (Table 2):** The ablation replacing toroidal distance with standard L2 distance degrades month prediction, confirming that the cyclical geometric treatment is meaningful.

## Weaknesses

### Fatal
None.

### Major

- **No variance or statistical significance reported for any experiment.** All tables (1, 2, 5) report single numbers without error bars, confidence intervals, or significance tests. Some comparisons involve very small differences (e.g., cyclic vs. L2 hour error differences that may be within noise), making it impossible to assess whether reported rankings are reliable. The paper's central claim that the proposed loss "significantly outperforms" alternatives is not supported without a measure of variance. **Fixable** by repeating experiments with multiple seeds and reporting mean ± std, ideally in time for the rebuttal.

### Minor

- **Time prediction metrics (E_m, E_H) are not fully defined in the main paper.** The paper states "mean absolute month error" and "mean absolute hour error" but does not specify whether these use a cyclic or linear distance. For months, a prediction of January for a December ground-truth yields error 11 under naive L1 but error 1 under cyclic treatment. The TPS formula uses normalized cyclic errors, but the primary metrics remain ambiguous. The paper defers to Supplementary Sections C–E, but the main text should be self-contained on this point.

- **Dataset handling for joint training is underspecified.** The training set combines MP-16 (4.72M images, GPS only) and CVT (~304k images, GPS + timestamps). The paper defines the training tuple as (image, GPS, timestamp) for all samples, but does not explain how MP-16 images — which have no timestamps — are handled during training. Are the time encoder and temporal loss simply not applied to those samples? Is there a two-stage procedure? This is critical for interpreting the joint-training claim in Table 1, because the improvement of GeoTimeCLIP over TimeCLIP could be confounded by different amounts of training data or training stages.

- **TimeCLIP baseline description is insufficient.** TimeCLIP is described as "akin to GeoCLIP but focusing exclusively on time prediction" (line 126). It is not explicitly stated whether it uses the proposed temporal metric loss or the standard GeoCLIP contrastive loss, nor whether it is trained only on CVT or also on MP-16 (without the location loss). This information is needed to interpret the comparison in Table 1.

- **No discussion of limitations or failure cases.** The paper does not discuss which types of images the method struggles with (e.g., night scenes, indoor images, heavily occluded views, equatorial regions with weak seasonal variation). A brief limitations paragraph would improve the paper's completeness and guide future work.

### Trivial

- **"Zero-shot" terminology is imprecise (Table 1).** The evaluation tests generalization to unseen cameras of the SkyFinder dataset — this is cross-camera generalization, not zero-shot prediction in the conventional sense (unseen classes/tasks). The phrasing should be adjusted to avoid confusion.

- **Target distribution formulation (Eq. 5) uses an unconventional transformation without justification.** The soft target is computed as \( q_j = 1 - \frac{\exp(\delta_{i,j})}{\sum_k \exp(\delta_{i,k})} \) rather than the more standard \( q_j = \frac{\exp(-\delta_{i,j})}{\sum_k \exp(-\delta_{i,k})} \). The chosen form works correctly but a brief justification would improve readability.

## Nice-to-Haves

- A dedicated limitations section discussing failure cases would strengthen the paper's completeness.
- The text-based retrieval results (Figure 5) could be supplemented with a quantitative metric (e.g., recall@K for time/location queries) to move beyond qualitative illustration.

## Removed Points

These points were flagged by reviewers but are removed with justification after cross-checking against the paper:

- **Geo-localization comparison with PIGEOTTO is vague about metadata.** *Removed because the paper already specifies PIGEON uses "administrative boundaries, climate, and traffic" as metadata (line 35) and acknowledges that PIGEOTTO's advantage likely stems from metadata (line 245). The information is present.*

- **Qualitative results are not quantitatively evaluated.** *Removed because these are explicitly presented as qualitative (Section 4.4 title: "QUALITATIVE RESULTS"). Requesting quantitative evaluation of a qualitative section is scope creep.*

- **Training details missing from the main paper (learning rate, batch size, etc.).** *Removed per policy: the paper references Supplementary Sections C–E for these details, which the parser strips. The main paper is not expected to replicate all training hyperparameters.*

## Novel Insights

None beyond the paper's own contributions. The reviews surface a disagreement about severity — the harsh critic downweights the paper for missing error bars and underspecified training protocols, while the strength finder correctly identifies the method's strong empirical results on both time prediction and geo-localization. The core insight that emerges from synthesizing both perspectives is that the paper's contributions are solid but its **reporting rigor** (not its methodology) is what prevents it from being a clear strong accept. The Temporal Metric Learning loss on a toroidal manifold is genuinely novel, but the paper would benefit from treating its evaluation with the same care as its method design.

## Suggestions

1. **Add error bars to all main tables** (Tables 1, 2, 5) by repeating experiments with at least 3 random seeds. Report mean ± std. This is the single highest-impact revision.
2. **Define E_m and E_H explicitly in the main text**, including whether the distance is cyclic or linear.
3. **Clarify the training protocol** for mixed datasets (MP-16 with only GPS, CVT with GPS+timestamps): state explicitly how batches are composed and whether the time encoder/loss is applied to all samples or only timestamped ones.
4. **Specify the loss function used by TimeCLIP** (standard contrastive or temporal metric learning) and what data it was trained on.
5. Add a brief limitations paragraph to the conclusion.
6. Replace "zero-shot" with a more precise description in Table 1.

## Score and Decision

The paper makes a novel and well-motivated contribution: the joint time-location retrieval framework is underexplored, the Temporal Metric Learning loss is principled, and the experimental results are consistently positive across multiple tasks. The weaknesses are real but bounded — the lack of error bars is the only major concern, and it is straightforwardly fixable. The methodology is sound, the evaluation is reasonably thorough, and the paper advances the state of the art in time-of-capture prediction while being competitive in geo-localization.

**MY FINAL SCORE: <score>7.5</score>**
**MY FINAL DECISION: <decision>Accept</decision>**