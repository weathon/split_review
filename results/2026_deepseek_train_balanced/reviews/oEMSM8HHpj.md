## Summary

The paper proposes three contrastive learning strategies—temporal contrast (same location, different times), spatial contrast (nearby locations, same period), and standard self-contrast—for pre-training ViT models on street view imagery. The central hypothesis is that each strategy encodes different types of visual information (temporal-invariant features for place recognition, neighborhood ambiance for socioeconomic prediction, holistic scene information for safety perception), and the four-way comparison across three tasks shows that each strategy indeed dominates on a different task. The paper also provides attention-map analyses linking pre-training objective to representation behavior.

---

## Strengths

- **The three-way experimental pattern directly validates the central hypothesis.** GSV-Temporal achieves 100% recall on CrossSeason across all K (Section 4.2), GSV-Spatial attains the highest average R² = 0.5888 across 18 socioeconomic indicators (Section 4.3), and GSV-Self achieves the top accuracy of 88.68% on safety perception (Section 4.4). That each strategy dominates on a *different* task, and that these align with the stated hypotheses, is non-trivial evidence that the spatiotemporal inductive biases shape representations as intended.

- **Attention-map and attention-distance analyses (Section 4.5) provide mechanistic evidence linking pre-training objective to representation behavior.** The visualization in Figure 2 shows that GSV-Temporal's query token placed on a car exhibits *no attention* to that car, directly demonstrating that temporal contrast learns to ignore dynamic objects—exactly the property required for VPR. GSV-Spatial produces the largest attention distance (spatial broadness), while ImageNet-Self yields the smallest (object-centric focus). This connects pre-training objective → representation geometry → downstream task suitability.

- **All three GSV-pretrained variants consistently outperform the ImageNet-pretrained MoCo v3 baseline across all three tasks.** On socioeconomic prediction (Section 4.3), even the worst GSV variant (self-contrast, R² = 0.5609) beats ImageNet (0.5209); on VPR and safety perception, the GSV models likewise exceed the ImageNet baseline. The consistency of this margin strengthens the claim that street-view-specific pre-training adds genuine value over generic large-scale natural-image pre-training.

- **The evaluation protocol is carefully standardized across contrastive variants.** All models use the same ViT Base architecture, optimizer (AdamW), batch size (1024), 300-epoch schedule, and are trained on datasets standardized to 1 million pairs (Section 4.1). This controls for confounds that often plague SSL comparison papers.

---

## Weaknesses

### Fatal

None.

### Major

- **Missing comparisons against the most directly related prior work.** Urban2Vec (Wang et al., 2020b) and KnowCL (Liu et al., 2023) are cited in Related Work (Section 2.3) as existing spatiotemporal self-supervised methods for street view imagery. Urban2Vec's core idea—treating nearby street view images as positive pairs—is closely related to GSV-Spatial. Yet neither method appears anywhere in the experiments. Similarly, SeCo (Manas et al., 2021) is cited for temporal contrast in remote sensing but not compared. A method paper that does not compare against its closest existing analogues cannot support its claim of advancing the state of the art. This is the most significant weakness: the claimed novelty relative to Urban2Vec is asserted ("these approaches fail to explore the natural meanings of the spatiotemporal attributes," line 29) but never demonstrated experimentally.

- **Potential data leakage in the socioeconomic evaluation.** The local-version spatial contrast dataset is constructed using Los Angeles block group boundaries as the unit for positive pairs (Section 4.1, line 74: "we defined each block group as an urban area and constructed positive pairs based on the block group boundaries"). The downstream socioeconomic evaluation then uses socioeconomic indicators for those *same* Los Angeles block groups (Section 4.3, lines 102–104). During pre-training, the spatial contrast model sees positive pairs constructed from the exact block group boundaries later used for evaluation. Since block groups encode socioeconomic boundaries, the model could learn to associate visual features specific to individual block groups—effectively "cheating" by memorizing the spatial structure that correlates with the target labels. The self-contrast and temporal-contrast models would not benefit from this leakage, systematically inflating GSV-Spatial's apparent advantage. The paper does not discuss or attempt to control for this (e.g., by pre-training on one set of cities and evaluating on a held-out city).

- **No ablation studies for key design choices.** The paper proposes new contrastive objectives with several tunable parameters, yet provides no ablation experiments. Untested design choices include: (a) the 100m spatial buffer size—how sensitive are results to this radius? (b) the temporal distance between images used as positive pairs—do pairs separated by months vs. years produce different invariances? (c) the scale of training data—1M pairs are used but 42M images were collected; how does performance scale? (d) the choice of MoCo v3 as the contrastive framework—would the conclusions hold under SimCLR or DINO? Without ablations, the paper cannot attribute its results to the proposed spatiotemporal positive-pair construction rather than other confounding factors.

### Minor

- **Abstract overclaims relative to actual experiments.** The abstract states the approach "significantly outperforms traditional supervised and unsupervised methods" (line 5). However, the only baseline in all experiments is ImageNet-Self (MoCo v3 trained on ImageNet), which is a *self-supervised* method, not a supervised one. No supervised baselines (e.g., Places365-pretrained models, which the paper itself identifies as the status quo for street view tasks in Section 2.3) are included. The claim is broader than what the evidence supports.

- **Safety perception evaluation on a small, filtered sample without variance estimates.** The PlacePlus 2.0 dataset is filtered to 1,144 images with extreme scores (below 3.5 or above 6.5, line 125), reducing the task to distinguishing extremes rather than modeling the full perception spectrum. The 80/20 split yields ~229 test images, and the linear classifier is trained for only 20 epochs. Accuracy (88.68%), F1, and AUC are reported without confidence intervals or significance tests. With ~229 test samples and a binary task, the observed differences between models may not be statistically reliable.

- **VPR comparisons are against generic contrastive baselines, not VPR-specific methods.** GSV-Temporal is compared only against GSV-Self and ImageNet-Self—both frozen-backbone [CLS]-token baselines. No comparison is made with methods designed for VPR (e.g., NetVLAD or any pipeline using a learned feature aggregator). While the paper's focus is on pre-training strategies rather than VPR system design, the claim that GSV-Temporal is a "superior choice" (line 89) for VPR would be stronger with at least one dedicated VPR baseline.

- **No confidence intervals or variance reported for any metric.** None of the three downstream evaluations report standard deviations, confidence intervals, or any measure of variability. The socioeconomic evaluation mentions 5-fold cross-validation (line 104) but does not report the variance across folds. Without variance estimates, the reader cannot assess whether observed differences between methods are meaningful.

- **Potential representation collapse from unrestricted shooting angle in spatial contrast.** The spatial contrast construction imposes no restrictions on shooting angle (line 74: "we did not impose any restrictions on the shooting angle for positive pairs"). Two images facing opposite directions on the same street could be positive pairs, sharing essentially no visual content yet being pushed together in the embedding space. The paper should discuss whether this risks representation collapse and how MoCo v3's momentum queue and InfoNCE loss with negative samples prevent it.

### Trivial

- **The "ImageNet-Self" baseline description is ambiguous.** The paper says "To benchmark against the MoCo v3 baseline trained on ImageNet, each dataset was standardized to consist of 1 million image pairs" (line 68). It is unclear whether this refers to the standard MoCo v3 checkpoint trained on the full 1.28M-image ImageNet-1K, or whether MoCo v3 was retrained on a 1M-image subset of ImageNet for fair comparison. These would differ in data volume and should be clarified.

- **Text describes GSV-Temporal's VPR numbers but only qualitatively describes alternative models' performance.** Section 4.2 gives specific recall values for GSV-Temporal but describes GSV-Self and ImageNet-Self only as "significantly lower performance" without citing their numbers. The data exists in Table 1 but is absent from the prose.

---

## Nice-to-Haves

- A direct comparison against Urban2Vec on the socioeconomic task and SeCo on a VPR proxy task would directly address the most serious weakness.
- Controlling for the data leakage issue—e.g., pre-training on one set of cities and evaluating on a held-out city—would strengthen the spatial contrast results substantially.
- Adding ablations for the spatial buffer radius (e.g., 50m, 100m, 200m) and the minimum temporal interval would demonstrate that the design choices are meaningful.
- Reporting variance (standard deviations or confidence intervals) across the 5-fold cross-validation for socioeconomic prediction would improve interpretability.
- Including a trivial-classifier baseline (e.g., always predicting the majority class) for the safety perception task would help contextualize the 88.68% accuracy.

---

## Removed Points

These points were flagged by the reviewers but removed or filtered for the reasons stated below. Treat them with caution.

- **"Computational cost of collecting 42M GSV images is not discussed"** — Removed. This is a practical/engineering concern (API costs, rate limits), not a scientific weakness. The paper appropriately describes the data collection methodology.
- **"Negative sampling strategy is not discussed in detail"** — Removed. The paper uses the standard MoCo v3 framework with InfoNCE loss. The negative sampling mechanism (momentum queue) follows the established MoCo v3 protocol and is not a novel design choice requiring separate description.
- **"Attention map analysis is based on a single image pair and two query tokens"** — Removed as a standalone weakness; this is acknowledged as qualitative/illustrative analysis in the paper itself (Section 4.5). The attention-distance analysis provides a more systematic complement. The limitation is noted but is not a flaw given the paper's framing of this section.
- **"Does not report baseline accuracy of a trivial classifier for safety perception"** — Removed. This is a suggestion that would strengthen but is not a required element; the accuracy and AUC numbers self-evidently exceed chance performance on a binary task.
- **"Spatial contrast's 'no angle restriction' contradicts claim about learning neighborhood ambiance"** — The reviewer framed this more strongly than warranted. The concern about representation collapse is theoretically valid but the MoCo v3's negative sampling (momentum queue with many negatives) is a standard mechanism to prevent collapse. I demoted this from the critic's framing to a minor weakness.
- **Any claim about missing appendix, missing proofs in appendix, or incomplete appendix** — Removed per hard rule. The parser strips appendix content from all papers; the original submission contains the referenced sections.

---

## Novel Insights

The harsh critic's identification of the data leakage problem in the socioeconomic evaluation is the single most insightful point that goes beyond the paper's own framing. The paper presents its three-way experimental pattern (temporal→VPR, spatial→socioeconomic, self→safety) as a clean validation of the central hypothesis. But the critic correctly identifies that the spatial contrast model's pre-training data is constructed from the same block group boundaries used for downstream evaluation, which means the spatial model has an unfair structural advantage that the other variants do not share. If this criticism holds, the paper's cleanest result (spatial best for socioeconomic) may be partially artifactual. This is a genuine insight that the paper itself does not acknowledge or address. The missing Urban2Vec comparison is also a critical observation—the paper draws a contrast with Urban2Vec in the related work but never substantiates it experimentally, which is a fundamental omission for a method paper.

Beyond these two points, most of the other criticisms (no ablations, no confidence intervals, safety perception on small data) are standard evaluation gaps that the paper's own community would identify.

---

## Suggestions

1. **Add comparisons against Urban2Vec and KnowCL** on the socioeconomic prediction task, and against SeCo on a suitable task. Without these, the paper's novelty claim is unsubstantiated.

2. **Control for data leakage in the socioeconomic evaluation** by either: (a) pre-training the global-version model and evaluating on Los Angeles (cross-city transfer), or (b) pre-training on Los Angeles but evaluating on held-out block groups. Report the spatial contrast results with and without the leakage control to quantify the effect.

3. **Add ablations for the spatial buffer radius and temporal interval** to demonstrate that these design choices materially affect learned representations.

4. **Report confidence intervals or standard deviations** for all key metrics, especially the 5-fold cross-validation results for socioeconomic prediction.

5. **Include at least one supervised baseline** (e.g., Places365-pretrained ViT) to substantiate the abstract's claim of outperforming "traditional supervised methods."

---

## Score and Decision

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>