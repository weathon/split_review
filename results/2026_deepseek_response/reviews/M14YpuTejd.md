Now let me write the final review with the calibration evidence and score.

## Summary

This paper identifies three misconceptions in the emerging protocol for online-map-based motion prediction: (1) inappropriate data splits causing a train-validation gap, (2) misaligned perception ranges between mapping and prediction models, and (3) non-discriminative metrics that evaluate only the ego vehicle. It proposes OMMP-Bench, a corrected benchmark with a spatially-disjoint data partition, refined metrics (evaluating moving non-ego agents, stratified by distance), and a simple baseline using deformable attention over image features to compensate for limited map coverage.

## Strengths

1. **Clear diagnosis of a genuine train-val gap with quantitative evidence.** Figure 3 shows that under the default split, map mAP drops from 87.6 (training) to 50.3 (validation), while the proposed spatially-disjoint split yields similar accuracy during motion training and evaluation (48.9 vs 50.3). This cleanly demonstrates the distribution shift that prior work overlooked.

2. **Distance-stratified non-ego metrics that reveal hidden failure modes.** Table 6 and 7 separate "Moving Non-Ego Close" from "Moving Non-Ego Far," showing far agents consistently underperform (e.g., minADE 0.6997 vs 0.5585 for HiVT+MapTR), which the existing ego-only metrics completely obscure. This is a simple but impactful methodological contribution.

3. **Demonstrates spatial overlap in existing dataset splits.** Figure 4 shows 87% of validation data spatially overlaps with the training set in the default split vs. 5% in the proposed split between map-train and motion-train. This concretely explains why existing splits overestimate generalization.

4. **Systematic evaluation of map element influence.** Table 5 compares six combinations of map element types (divider, boundary, pedestrian crossing, centerline), showing centerlines alone achieve nearly the best performance (0.6631 vs 0.6308 for all elements), providing actionable guidance for online mapping design.

5. **Comprehensive empirical evaluation.** Table 7 evaluates 4 combinations of mapping × motion models (MapTR/MapTRv2-CL × HiVT/DenseTNT) across 4 method variants (base/unc/bew/img), providing a thorough empirical foundation.

## Weaknesses

### Fatal
None.

### Major

1. **Confounded evidence for attributing motion prediction improvement to gap elimination (Table 1).** The comparison between Setting 1 (proposed split) and Setting 3 (default split) differs in two respects simultaneously: (a) the data split strategy, and (b) the amount of data used to train the mapping model (367 scenes in the map-train set vs. ~700 scenes in the full nuScenes training set). The mapping model in Setting 1 is substantially weaker, which could change the difficulty distribution of the motion prediction task in ways independent of closing the train-val gap. Setting 4 (two 50% subsets of the official training set) achieves results similar to Setting 1 (0.6373 vs 0.6308), yet this split likely still has spatial overlap between map training and motion evaluation data. The paper claims the split "leads to an explicit performance enhancement...demonstrating the importance of reducing the train-val gap" (end of Sec 3.2), but this causal claim is not adequately supported without a controlled ablation that isolates the gap-elimination effect — for example, holding the mapping model constant while varying only the data split for the motion model. That said, the underlying phenomenon (the default split has a serious train-val gap and the proposed split eliminates this gap) remains convincingly demonstrated by Figure 3; the confound weakens but does not invalidate the paper's core diagnostic contribution.

### Minor

2. **Image-feature baseline not fully characterized.** The proposed "img" baseline (Sec 3.3, Table 4, Table 7) uses deformable attention over image features and outperforms MapBEVPrediction ("bew"). However, the paper does not discuss whether the BEV features in MapBEVPrediction already contain information beyond the 30×60m nominal mapping range (since the encoder processes images with a wide receptive field). It also does not ablate the deformable attention mechanism itself — e.g., comparing against a simpler bilinear interpolation of image features at the projected agent position. Without this analysis, the source of improvement (image features vs. the attention mechanism itself) remains unclear.

3. **Overlap statistics for motion-val vs. map-train not reported.** The paper reports that only 5% of motion-train data overlaps with map-train data (Figure 4 caption) but omits the overlap between motion-val and map-train, which is equally important for understanding the split's effectiveness.

4. **No variance or confidence intervals.** All results are reported to four decimal places without standard deviations or confidence intervals. Given that nuScenes scenes vary considerably, this makes it difficult to assess whether observed differences between methods are statistically reliable.

### Trivial
None.

## Nice-to-Haves
- Adding more recent motion prediction models (e.g., MTR, QCNet) would strengthen generality.
- A failure case analysis of the image-feature baseline (what happens when agents are occluded or outside the camera frustum) would provide useful context.
- Reporting computational cost of the image-feature baseline would be helpful for practical deployment.

## Removed Points
- **"Fatal" characterization of the data-split confound by the harsh critic.** Demoted to Major because Figure 3 independently proves the train-val gap exists and is eliminated by the proposed split. The confound weakens the *attribution* of motion prediction improvement but does not invalidate the core diagnostic finding.
- **Criticism about Setting 4 (two 50% subsets) undermining the thesis.** Setting 4 partially supports rather than contradicts the paper's thesis — it demonstrates that reducing the gap in a different way also helps.
- **"CVPR 2024 Best Paper Final List" phrasing.** Purely stylistic, not a substantive weakness.
- **Reproducibility concerns about missing appendix content.** Parser strips appendices; paper commits to releasing code/checkpoints.
- **Missing related works.** Cannot be verified from external sources per policy.
- **Formatting/presentation nitpicks.** Parser artifacts or style preferences.
- **Weaknesses about MapBEVPrediction comparison, lack of detailed overlap criteria, hyperparameter details.** These are either addressed by the paper or are standard practice for the field.

## Novel Insights
The key asymmetry revealed across the reviews is that the paper's diagnostic contributions (identifying the three misconceptions) are stronger and more rigorously supported than its solution contributions (new split, image-feature baseline). The train-val gap documentation in Figure 3, the range misalignment analysis in Tables 2-3, and the metric critique in Table 6 are clean, well-evidenced, and independently valuable. By contrast, the causal claim that the new split *improves performance by closing the gap* is not cleanly separated from confounds, and the image-feature baseline's mechanism is insufficiently ablated. This suggests the paper's most durable value is in its systematization of the problems with the existing protocol, not in the specific fixes it proposes.

## Suggestions
1. Add a controlled experiment isolating the split effect: train the mapping model on the *same* data across settings, varying only the motion model's training/evaluation split. Alternatively, measure motion prediction performance using the *same* mapping model predictions for both motion training and evaluation under the default protocol.
2. Ablate the deformable attention in the baseline by comparing against a simpler approach (e.g., bilinear interpolation of image features at projected agent positions).
3. Report motion-val vs. map-train overlap and clarify the criteria used for determining spatial disjointedness.
4. Add variance estimates (e.g., bootstrap confidence intervals) for key results.

---

## Calibration Anchors

**Round 1 — Bracketing:**
- Weak band (<3.5): avg scores 2.5–3.0 (e.g., BRSSD10k at 3.0, "Don't Reinvent the Steering Wheel" at 2.5). These are substantially weaker papers with unclear contributions.
- Middle band (3.5–7.5): avg scores 4.0–5.33 (MapDR at 5.0, RedMotion at 5.33, Large Trajectory Models at 5.0). These are in the same ballpark as the current paper.
- Strong band (>7.5): avg scores 8.0 (e.g., MOS at 8.0, MovingParts at 8.0). These are clearly stronger papers with cleaner experimental evidence.

**Round 2 — Narrowing:**
- BEV Uncertainty Benchmark (avg 5.40, benchmark paper for a related autonomous driving task). Similar in type, slightly weaker in diagnostic clarity than the current paper.
- MapDR (avg 5.00, benchmark dataset for driving rules). Comparable but the current paper's diagnostic contributions are clearer and more impactful.
- SmartPretrain (avg 6.75, motion prediction pre-training framework). Stronger than the current paper — has cross-dataset validation, thorough ablations, and cleaner experimental design.
- Pedestrian Generation CityWalkers (avg 6.75, pedestrian movement generation). Stronger than the current paper — has cleaner experimental support and a more thoroughly characterized contribution.

**Final bracket determined in Round 1:** 4.5–6.5.  
**Final score (after Round 2 narrowing):** 5.5. The paper sits above MapDR (5.0) due to its clearer diagnostic contributions, but below SmartPretrain (6.75) and PedGen (6.75) because of the confounded central experiment and incomplete baseline characterization. The diagnostic insights are genuinely valuable, but the experimental evidence for the data-split solution is not fully controlled.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>