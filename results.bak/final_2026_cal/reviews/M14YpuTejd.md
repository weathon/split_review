Good, confirmed. Rows 2 and 3 of Table 5 have identical checkmarks but different values — a parser artifact. Let me now write the final consolidated review.

## Summary

This paper identifies several misconceptions in the emerging area of online map based motion prediction for autonomous driving: (1) inappropriate data splits that cause a train-validation gap, (2) misaligned perception ranges between online mapping models (small, e.g., 30×60m) and motion prediction needs (agents up to 100m away), and (3) non-discriminative metrics that only evaluate the ego vehicle. The authors propose **OMMP-Bench**, a corrected benchmark with a spatially disjoint data split (reducing spatial overlap from 87% to 5%), refined metrics that evaluate moving non-ego agents under distance-based groupings (close vs. far), and a boundary-free baseline that uses image features (via deformable attention) to supply environmental information for agents outside the map's perception range. Experiments across two online mapping models (MapTR, MapTRv2-CL) and two motion prediction models (HiVT, DenseTNT) validate that the proposed split eliminates the train-val gap, that distance-grouped metrics reveal pronounced difficulty cliffs, and that the image feature baseline yields consistent gains, especially for far agents (up to 12.7% minADE reduction).

## Strengths

- **Train-val gap clearly identified and corrected.** Figure 3 shows that under the default protocol, the map mAP drops from 87.6 (train) to 50.3 (val), while the proposed split yields nearly identical mAP (48.9 vs. 50.3). Table 1's Setting 2 (0.7006) vs. Setting 1 (0.6308) cleanly demonstrates that removing the map accuracy mismatch between training and evaluation improves motion prediction performance.

- **Refined metrics expose previously concealed difficulty gaps.** Table 6 quantifies that moving non-ego agents outside the perception range have minADE 0.6997 vs. 0.5585 for close agents and 0.4015 for ego — differences that prior work (evaluating only ego) completely masked. This directly supports the paper's claim that non-discriminative metrics obscured the real challenge.

- **Image feature baseline provides a principled solution to the out-of-range problem.** Table 4 shows the proposed "img" baseline (minADE 0.6163) outperforms prior BEV-feature and uncertainty methods. Table 7 confirms that gains are strongest on far non-ego agents (e.g., MapTR+HiVT: 0.6318 vs. base 0.6997, a 9.7% improvement), demonstrating that raw image features can compensate for the limited perception range of online map models.

- **Systematic analysis of map element selection.** Table 5 compares six combinations of map element types, finding that centerlines are the single most informative element type (minADE 0.6631 vs. 0.8770 for dividers only) and that using all element types yields the best performance (0.6308). This provides concrete guidance for online mapping model design.

- **Spatial overlap quantified and dramatically reduced.** Figure 4 reports that the original nuScenes split has 87% validation overlap with training; the proposed split reduces overlap to only 5% between map train and motion train sets, enabling a more honest evaluation of generalization.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

- **Table 1's headline comparison (Setting 1 vs. Setting 3) mixes different validation sets.** The paper states that the proposed split "leads to an explicit performance enhancement compared to the default split" and displays Setting 1 (Motion Val, 0.6308) vs. Setting 3 (nuScenes Val, 0.6839). These evaluation sets differ in size (86 vs. 150 scenes) and composition, making a direct comparison unprincipled. The clean comparison exists — Setting 2 (Map Train + Motion Train on Motion Val, 0.7006) vs. Setting 1 (Map Train only on Motion Val, 0.6308) — and convincingly supports the claim. The paper should foreground this comparison and explicitly state that the default-split result (Setting 3) is not directly comparable. The evidence for the claim is still present; the presentation is just misleading as written.

- **"Close" vs. "far" classification for moving agents is underspecified.** The paper defines "close" and "far" as whether an agent is "within the perception range of online mapping models" (Section 3.4). Since a moving agent can cross the 30×60m boundary during its history, the paper does not state whether the classification is based on the agent's position at the current timestep, the first observed frame, the average over history, or some other rule. Different choices produce different splits and different results. This needs to be specified for reproducibility.

- **Image feature baseline training protocol is not disclosed.** The paper describes using deformable attention to query image features from the online mapping model's backbone (Eq. 1), but does not state whether the image backbone is frozen, fine-tuned end-to-end with the motion prediction model, or trained jointly. This distinction is decisive for both performance comparison and reproducibility. If frozen, the baseline is cheaper but features may be suboptimal; if fine-tuned, the baseline may understate its cost. This must be clarified.

- **Spatial overlap detection methodology is not described.** The paper reports that the proposed split reduces overlap to 5% but does not specify *how* spatial overlap was checked (e.g., distance threshold between map elements across scenes, coordinate system used). This is needed for others to reproduce or extend the split.

- **5% overlap statistic appears only in the Figure 4 caption.** The main text does not mention this key number. It should appear in Section 3.2 alongside the description of the split.

### Trivial
None.

## Nice-to-Haves

- Report variance or confidence intervals for the main results in Table 7. Many differences between methods are small (e.g., 0.001 on MR), and without variance it is impossible to assess statistical significance.
- Add an ablation of the "moving" agent threshold (the paper uses 2m in 3s, which is reasonable but not justified relative to e.g., 1m, 3m, or 4m thresholds).
- Consider adding a summary row or figure to Table 7 to more clearly highlight the trend that far agents are hardest, and reorder columns so the three distance groups appear contiguously.
- The image feature baseline is called "SOTA" in Table 4; this claim should be more carefully scoped since the baseline is tested on only two map models and two motion models. It is best described as a "strong proof-of-concept."

## Removed Points

- **Table 5 formatting error (rows 2-3 appear to duplicate):** The identical checkmark patterns with different values are likely a PDF parser artifact (columns dropped during extraction), not an author error. Removed per formatting-artifact rules.
- **Missing appendix content, proofs, references:** The parser strips appendices; these exist in the original submission. Removed per rules.
- **Weakness about comparison asymmetry (Setting 1 vs 3) being "invalid":** Downgraded from the critic's framing to Minor. The evidence exists in Setting 2 vs. Setting 1; the framing is suboptimal, not the claim.
- **"Only nuScenes" limitation:** The paper explicitly acknowledges this limitation (Section 3.1: "Note that all existing online mapping based motion prediction models are conducted only on nuScenes dataset because it provides raw camera data, HD maps, and trajectories..."). The authors cannot fix this without a new dataset; it is a field-wide constraint, not a paper flaw.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

- Revise the discussion of Table 1 to lead with the clean comparison: Setting 1 vs. Setting 2 (both on Motion Val), and explicitly caution that Setting 3 uses a different evaluation set.
- Specify the agent position timestep used for the close/far classification (current step, first observed frame, or other).
- State clearly whether the image backbone is frozen or fine-tuned, including any associated training cost.
- Describe the spatial overlap detection methodology (distance threshold, coordinate reference) in the main text.
- Move the 5% overlap statistic from the Figure 4 caption into the main text.

## Score and Decision

**Calibration details** (all anchors retrieved across rounds):

| Anchor ID | Avg Score | Round | Comparison |
|-----------|-----------|-------|------------|
| f2nxdOv1Uh | 2.67 | 1 (bracket low) | Reject-level end-to-end AD paper; OMMP-Bench is clearly stronger |
| LnbMSnQpXb | 2.00 | 1 (bracket low) | Withdrawn AD paper; OMMP-Bench is much stronger |
| zW1U6SW9ra | 3.00 | 1 (bracket low) | Compressed Map Priors; different type of contribution |
| RbsLsTYi4H | 3.00 | 1 (bracket low) | Withdrawn AD paper |
| mxz5RqhCMe | 4.67 | 1/2 (bracket mid) | Stability Under Scrutiny — similar benchmark paper on online HD mapping; OMMP-Bench has fewer fundamental metric concerns |
| DUtfVs1xxD | 4.00 | 1 (bracket mid) | Online mapping model paper; rejected |
| aqwtK0OIGs | 4.50 | 1 (bracket mid) | SD map motion prediction; withdrawn, similar quality level |
| epbzV3FLcI | 6.00 | 1/2 (bracket mid) | Online Navigation Refinement — similar benchmark+dataset+metric contribution; OMMP-Bench is comparable in quality |
| OrgL5DsU0f | 6.50 | 2 (narrowing) | DrivingGen — more comprehensive benchmark; OMMP-Bench is somewhat less broad but still solid |
| vhrovHIeE4 | 5.00 | 2 (narrowing) | AlignDrive — rejected; OMMP-Bench is stronger |
| f5lIozG83H | 5.60 | 2 (narrowing) | AccidentBench — benchmark paper, rejected; OMMP-Bench has clearer contributions |
| MY0NHvqzi2 | 6.00 | 2 (narrowing) | DriveMamba — method paper, accepted; different type but similar quality |
| 4HZgkwVVFO | 5.50 | 2 (narrowing) | NeMo-map — accepted method paper; OMMP-Bench is a stronger benchmark contribution |
| l9i6q2bXnj | 5.33 | 2 (narrowing) | ARINBEV — accepted method paper |

**Round 1 bracket**: 4.5–7.0 (clear from the middle query results).

**Round 2 narrowing**: Compared directly against anchors at 5.5–6.5, the paper sits at the upper end. It is stronger than Stability Under Scrutiny (4.67, which had fundamental metric vulnerabilities) and comparable to Online Navigation Refinement (6.00, which introduced a new task). The weaknesses are addressable presentation and detail gaps, not core flaws.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>