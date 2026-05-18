Now I have a complete picture. Let me synthesize the final review.

## Summary

This paper makes two contributions: (1) FairFedMed, a new medical FL dataset for group fairness with 15,165 paired 2D SLO fundus images and 3D OCT B-scans from glaucoma patients, annotated with six demographic attributes across three simulated sites; and (2) FairLoRA, a fairness-aware FL framework that extends SVD-based low-rank adaptation by assigning per-demographic-group singular value matrices while sharing singular vector matrices across groups. Experiments show FairLoRA improves overall AUC and the ESAUC fairness metric over FedAvg, FedHEAL, PromptFL, and FedOTP on both 2D and 3D modalities.

## Strengths

1. **First FL group-fairness dataset with paired 2D/3D medical images.** FairFedMed contains 15,165 real clinical samples with both 2D SLO and 3D OCT modalities plus six demographic attributes (race, ethnicity, language, age, gender, marital status). Prior FL datasets for fairness lack medical images, paired modalities, or comprehensive demographic annotations. This fills a genuine gap (Section 3).

2. **Consistent improvements over non-fairness baselines across both modalities and backbones.** FairLoRA improves overall AUC by 2.7–4.7% (2D) and 3.4–5.3% (3D) with ViT-B, and ESAUC by 4.1–5.9% (2D) and 4.1–6.7% (3D) over methods like FedAvg and PromptFL that do not explicitly address group fairness. The improvements are consistent across both 2D and 3D modalities and two backbones (ResNet50, ViT-B), shown in Tables 1–4.

3. **Ablation isolates the benefit of per-group S matrices.** Figure 5b directly compares LoRA, SVD-based LoRA, and FairLoRA under the same federated setting. FairLoRA achieves the highest overall AUC (79.3%) and ESAUC, while SVD-LoRA shows "significant fluctuations across clients" in fairness metrics. This provides controlled evidence that the per-group customization is driving fairness gains, not just the low-rank structure.

4. **The per-group SVD design is principled and lightweight.** Rather than maintaining separate full models per group, FairLoRA only customizes the diagonal singular value matrices per group while sharing U and V. This adds minimal parameter overhead and is cleanly motivated by the SVD framework (Section 4.3).

## Weaknesses

### Fatal
None.

### Major

1. **Missing comparison against fairness-aware FL baselines.** The related work discusses FairFed (Ezzeldin et al., 2023) and FairTrade (Badar et al., 2024) as state-of-the-art group-fairness FL methods, yet neither appears in the experiments. The paper claims "state-of-the-art performance" in both accuracy and fairness, but its baselines (FedAvg, FedHEAL, PromptFL, FedOTP) do not explicitly target group fairness. Without comparing against methods designed for the same problem, the fairness claims are unsupported. The paper should include these baselines (or explain concretely why they cannot be applied to medical image classification) to substantiate the contribution.

2. **Backbone and pretraining protocol for baseline methods is ambiguous.** FairLoRA uses CLIP (ViT-B/16 or ResNet50). PromptFL and FedOTP are described as "based on CLIP" (line 116). But for FedAvg and FedHEAL, it is never stated whether they use the same CLIP-pretrained backbone, a randomly initialized backbone, or some other pretrained weights. Since the tables are split by backbone, the baseline rows presumably use the matching backbone — but whether they benefit from CLIP's strong pretraining or start from scratch is left unclear. If FedAvg/FedHEAL use a standard (non-CLIP) initialization while FairLoRA uses CLIP, the comparison is fundamentally unfair. This must be clarified for the results to be interpretable.

3. **How 3D OCT B-scans are adapted to 2D CLIP is not explained.** The dataset contains 3D OCT B-scans with 128 slices per sample (line 42), but CLIP is a 2D model. The paper never describes whether (a) single 2D slices are selected, (b) slices are aggregated/averaged, (c) a 3D-to-2D projection is used, or (d) some other strategy is employed. This is a basic architectural detail that must be specified for reproducibility.

### Minor

4. **ESAUC is cited but not defined in the paper.** The metric is named as "equality-scale AUC (ESAUC) (Luo et al., 2024)" (line 116), giving readers the name and a citation to look up. However, the paper does not explain what the metric computes — e.g., whether it is the minimum group AUC, a disparity measure, or a normalized score. A brief self-contained definition would improve readability and prevent confusion.

5. **No error bars, confidence intervals, or multiple seeds reported.** All results appear to be from single runs (the paper does not mention random seeds or repetitions). Given the stochastic nature of FL (partial client participation, random initialization) and only three clients, single-run results are not reliable. Reporting at least three random seeds with standard deviations would substantiate the claimed improvements.

6. **Dataset limitations are not discussed.** The paper transparently reports the demographic statistics (76.9% White, 92.7% Non-Hispanic, 92.5% English-preferred — lines 42–45) and states sites are "separate sites" but does not clarify whether they correspond to real institutions or are simulated partitions of a single cohort. The skewed demographics and single-disease scope limit the generality of conclusions. Acknowledging these limitations would strengthen rather than weaken the paper.

7. **No IRB or ethics statement for the medical dataset.** The paper uses real patient data with demographic attributes but does not state the data source, de-identification process, or IRB approval status. This is a requirement for medical-data papers at most venues.

8. **Communication cost and round count not reported.** FairLoRA claims computational efficiency via low-rank adaptation, but no FL round counts, total communication cost, or training times are reported for any method. These numbers would help assess the practical benefit.

### Trivial

9. **Weighted averaging of orthonormal matrices.** The paper aggregates client U and V matrices via weighted averaging (line 95), then observes that the averaged matrices remain approximately orthonormal (line 102). Weighted averaging of orthonormal matrices does not generally preserve orthonormality; the paper should briefly explain why this approximation holds or why it does not harm performance.

10. **Initialization description is somewhat vague.** The initialization (line 102) describes "a linear space of values ranging from 0.5 to 0.1" and "a cyclic pattern" for the remaining ranks. While the general idea is clear, these terms are not precisely defined. Specific formulas or pseudocode would aid reproducibility.

## Nice-to-Haves

- A brief definition of ESAUC (even one sentence) would make the paper self-contained.
- Reporting group-wise AUCs as both a table and a visualization of the gap between best and worst group would strengthen the fairness analysis.
- An ablation comparing FairLoRA on different rank values would help understand sensitivity to this hyperparameter.
- Adding communication cost (parameters transferred per round) for all methods would quantify the efficiency claim.

## Removed Points

These points are flagged to be removed; treat them with caution.

1. **"ESAUC is not defined — technical gap preventing reproducibility."** — The paper *does* define ESAUC by name ("equality-scale AUC") and provides a citation (Luo et al., 2024). While a brief explanation would help, calling this a "technical gap that prevents reproducibility" is an overstatement. Downgraded to Minor (#4 above).

2. **"One-hot encoding in FairLoRA is underspecified for multi-group clients."** — The paper clearly states that π is a one-hot vector "ensuring that only the target demographic group has a non-zero value" (line 89). This is standard: per-sample, the one-hot selects the S matrix for that sample's demographic group. If a client has multiple groups, different samples naturally activate different S matrices. The paper is sufficiently clear. Removed as factually incorrect criticism.

3. **"Dataset limitations are not honestly discussed" (framed as critical).** — The paper transparently reports full demographic statistics. The limitation is that the paper does not *discuss* the implications of the skew, but this is a minor oversight, not a critical flaw. Downgraded to Minor (#6 above).

4. **"No comparison to existing fairness-aware FL methods" framed as "fatal omission."** — This is a genuine major weakness, but not fatal: the paper's contributions include both a dataset (which stands regardless) and a method that demonstrably improves fairness over non-fairness baselines. The claim is incomplete, not invalidated. Kept as Major (#1).

5. **"Table 2" and "Table 4" are referenced as if visible** — The parser stripped table images from the PDF. The original submission contains these tables. This is a parser artifact, not an author error.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. **Add FairFed and FairTrade (or the closest applicable fairness-aware FL methods) to the experimental comparison.** This is the single most important change. If they cannot be applied to this task, explain why and use the best available proxy.

2. **Clearly state the backbone, pretraining, and training protocol for every baseline in every table.** Specify whether FedAvg and FedHEAL use CLIP-pretrained weights, random initialization, or another pretrained model.

3. **Explain how 3D OCT B-scans (128 slices per sample) are processed into 2D inputs for CLIP.** Include this in the experimental setup section.

4. **Add error bars over at least three random seeds.** This is standard practice and essential for FL experiments.

5. **Include an IRB/ethics statement and data source information** for the FairFedMed dataset. This is a standard requirement for papers introducing medical datasets with human subject data.

6. **Provide a brief self-contained definition of ESAUC** — even one sentence stating what it measures (e.g., "the average of group-specific AUCs weighed inversely by their disparity") would suffice.

## Score and Decision

The paper addresses an important problem and makes two worthwhile contributions: a new dataset and a method with an interesting design. The dataset is a genuine resource for the community. However, the evaluation is incomplete in ways that undermine the core fairness claims: no comparison against existing fairness-aware FL baselines, ambiguous backbone specifications, and unexplained 3D-to-2D conversion. These are addressable, but in its current form the evidence does not support the claimed state-of-the-art fairness results. The paper should be revised to address these gaps before acceptance.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>