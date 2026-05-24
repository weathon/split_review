## Summary

This paper identifies three misconceptions in the recently proposed online-map-based motion prediction protocol: (1) inappropriate data splits that cause a train-validation gap in two-stage training, (2) misaligned perception ranges between online mapping models and motion prediction, and (3) non-discriminative metrics that only evaluate the ego vehicle. The authors propose **OMMP-Bench**, a corrected benchmark with a spatially-disjoint three-way split, refined metrics that evaluate all moving non-ego agents with close/far grouping, and a boundary-free image-feature baseline that alleviates the out-of-range issue. The analysis is timely and the identified problems are genuinely important for the community, with the proposed fixes consistently improving performance across multiple combinations of mapping and motion prediction models.

## Strengths

1. **Identifies real and previously overlooked problems in an emerging benchmark protocol.** The paper convincingly shows that the standard nuScenes split leads to a train-val gap in two-stage training (Figure 3 and Table 1), that the map model's perception range (30×60 m) is insufficient for agents beyond ~100 m, and that reporting only ego-vehicle metrics masks these issues (Table 6: static agents achieve minADE 0.002). These are substantive findings that will benefit the community.

2. **Well-motivated new spatio-temporally disjoint split.** The paper manually partitions nuScenes into three spatially-non-overlapping sets (map train: 367, motion train: 397, motion val: 86 scenes), reducing geographic overlap from 87% to 5% (Figure 4). The conceptual argument — that the map model's accuracy should be similar during motion training and evaluation — is sound, and Table 1 confirms that the proposed split improves minADE from 0.6839 (default) to 0.6308.

3. **The boundary-free image-feature baseline is simple and effective.** Using Deformable Attention to let agents retrieve raw image features from the mapping model's backbone (unconstrained by the BEV perception range) consistently improves performance, especially for far agents. On MapTRv2‑CL + HiVT, far-agent minADE drops from 0.6999 to 0.6274 (12.7% reduction, Table 7). This is a practical contribution that directly addresses the misaligned-range issue.

4. **Meaningful metric refinements.** Moving from ego-only to all moving non-ego agents and splitting results into close/far groups (Table 7) provides a much more informative evaluation. The paper demonstrates that methods improving ego prediction can hurt far-agent prediction (e.g., MapTRv2‑CL + DenseTNT unc/bev increase far minADE by ~4%), validating the need for these refined metrics.

5. **Useful analysis of map element influence.** Table 5 shows that centerlines alone achieve near-best performance (minADE 0.6631 vs. 0.6308 for all elements), providing concrete guidance for online mapping model design.

## Weaknesses

### Fatal
None.

### Major

1. **Split comparison in Table 1 is not fully controlled.** The proposed split (Setting 1) differs from the default split (Setting 3) in multiple confounded dimensions: map-model training set size (367 vs. 700 scenes), motion-model training set size (397 vs. 700 scenes), and spatial-overlap degree. Setting 4 (two random halves of nuScenes Train) achieves similar performance to Setting 1 (0.6373 vs. 0.6308) while presumably still suffering from spatial overlap with the validation set. This suggests that removing the train-val gap (which Setting 4 also does by having the map model infer on unseen data) is the dominant factor, but it also means the evidence that spatial disjointness itself is critical is weaker than a controlled ablation would show. The paper would benefit from multiple geographically-disjoint splits with variance reporting to isolate the overlap factor.

2. **No variance or confidence intervals reported.** All Table entries are single values with no indication of variability across random seeds, data splits, or training runs. Many observed differences are small (e.g., Table 4: minADE 0.6163 vs. 0.6272 for img vs. unc; Table 1: 0.6308 vs. 0.6373). Without error bars, a reader cannot assess which differences are meaningful. For a benchmark that others will use to compare future methods, establishing the stability of results is essential.

### Minor

3. **Missing direct experiment on wider-range online maps for motion prediction.** Section 3.3 shows that (a) extending the map perception range to 100×100 m crashes online map quality (Table 2: MapTR mAP 0.124→0.014) and (b) GT maps at 100×100 m improve motion prediction (Table 3). The paper concludes that "simply expanding the perception range… ultimately fail[s] to improve motion prediction," but this is inferred rather than directly observed. Actually running motion prediction with online maps at 100×100 m (even with low map quality) would turn this inference into direct evidence and strengthen the motivation for the image-feature baseline.

4. **"Close" vs. "far" threshold not precisely specified.** The paper states that the split is "decided by whether within the perception range of online mapping models" (Section 3.4), but does not state the exact metric threshold (e.g., the 30×60 m range of MapTR) or whether this threshold is held fixed or varies per mapping model. This should be explicitly documented for reproducibility.

5. **Table 5 appears to have a formatting/duplication issue.** Rows 2 and 3 both show "✗ ✓ ✗ ✗" (boundary only) with different minADE values (0.6829 and 0.6558). One of these rows likely corresponds to a different element combination (e.g., boundary + something else). This should be corrected.

### Trivial
None.

## Nice-to-Haves

- **Controlled split ablation:** Running the proposed split with multiple random scene assignments (3–5 geographically-disjoint partitions) and reporting mean±std of the motion prediction metrics would substantially strengthen the split analysis.
- **Direct online-map range experiment:** Evaluating motion prediction with online maps at 100×100 m would turn the current inference into direct evidence.
- **Disentangle the image-feature benefit:** An ablation separating agents with vs. without map coverage could clarify when image features are most critical.
- **Split creation documentation:** A brief summary of how the 850 scenes were manually partitioned and an analysis of city balance in each subset would aid reproducibility.

## Removed Points

These points are flagged as removed; treat them with caution.

1. **"The 87% overlap might actually make the gap smaller"** — Removed because it conflates two separate issues. The spatial overlap (87%) affects the *map model's* generalization evaluation, while the train-val gap for *motion prediction* arises from the map model seeing its training data during motion training but unseen data during evaluation. The paper correctly distinguishes these.
2. **"Add more recent motion prediction models (e.g., MTR, QCNet)"** — Removed as scope creep. The paper uses HiVT and DenseTNT because these are the models used in the existing protocol (Gu et al., 2024a,b) that the paper analyzes. The benchmark is designed to be extensible, not exhaustive.
3. **Reproducibility nitpicks about undisclosed hyperparameters** — Removed per instructions; these are typically handled by the appendix and code release.
4. **"Section 4.1 should note what proportion of the original validation set is retained"** — Removed because the paper explicitly states "86 scenes" for motion val. While the proportion could be stated explicitly, it is easily computed.

## Novel Insights

Beyond the paper's own contributions, the most interesting observation from the cross-review analysis is the asymmetric effect of different improvement strategies: methods like MapUncertaintyPrediction and MapBEVPrediction improve ego-vehicle prediction but actually *hurt* far non-ego prediction in several configurations (Table 7). This finding — that a method can simultaneously improve on one evaluation dimension and degrade on another — underscores why the paper's proposed multi-faceted metrics (close vs. far, ego vs. non-ego) are necessary and why the field cannot rely on the narrow ego-only metric from prior work. The paper surfaces this pattern but does not fully explore it; it opens a potentially rich direction for understanding how online map errors propagate differently across agent distances.

## Suggestions

1. Add variance estimates (or at minimum, results from 3 seeds) for the central comparison in Table 1 and for the main method comparisons (Tables 4, 7).
2. Run the missing direct experiment: evaluate motion prediction with 100×100 m online maps (even if accuracy is low) to close the inference gap in Section 3.3.
3. Explicitly state the threshold used for close/far classification and whether it is model-dependent or fixed.
4. Fix the row duplication in Table 5 and verify that all ablation configurations are correctly labeled.
5. Consider adding a controlled ablation where the map-model training set size is held constant while only the overlap with the motion sets is varied.

## Score and Decision

### Calibration Anchors

**Round 1 — Bracketing:**  
- Low band (avg < 3.5): pzZjyYee6L (2.50), DCg9r2DKKe (2.50), 0qfIhtel8N (3.00) — much weaker papers; generally rejected with fundamental issues.  
- Middle band (3.5–7.5): 72MSbSZtHv (RedMotion, 5.33), sEJYPiVEt4 (ESDMotion, 5.25), KyqtKhv6q1 (4.25), 9tiQ0aBK7c (TopoSD, 5.20), r125wFo0L3 (5.00).  
- High band (avg > 7.5): Y6aHdDNQYD (MOS, 8.00), syThiTmWWm (Cheating Benchmarks, 7.75), 6s5uXNWGIh (MLE-Bench, 8.00), jOmk0uS1hl (Training on Test Task, 8.00) — accepted papers with stronger empirical validation.

**Round 1 bracket: [5.0, 6.5]** — The paper is clearly stronger than the low-band papers and weaker than the high-band ones in experimental rigor, but comparable to or better than the middle-band anchors in its topical area.

**Round 2 — Narrowing:**  
- IkqcUzUogm (4.75) — benchmark/evaluation paper, weaker execution. The current paper is better motivated and more concrete.  
- RTHbao4Mib (Words and Deeds, 6.25) — accepted paper on benchmark design. The current paper is slightly weaker on experimental thoroughness but has a similar level of conceptual contribution.  
- Vv76fCYffN (SSR, 6.40, Accept) — method paper with stronger experimental validation but similar overall quality. The current paper has a different contribution type (analysis vs. method) but is in the same quality band.  
- LsURkIPYR5 (LaneSegNet, 6.00, Accept) — mixed reviews (8,5,5,6). Similar score despite concerns about motivation and writing. The current paper has clearer problem formulation.  
- efeBC1sQj9 (SEPT, 7.00, Accept) — stronger experiments. The current paper is not at this level of rigor.

**Final score determination:** The paper sits between the 5.25–5.33 anchors (ESDMotion, RedMotion) and the 6.0–6.4 anchors (LaneSegNet, SSR). It has clearer motivation and more novel contributions than ESDMotion but shares some of its rigor limitations (old baselines, no error bars). It is not as experimentally strong as SSR or SEPT. The core analysis is valuable and the proposed benchmark is a genuine improvement over the status quo, but the evidential support for the central split claim would benefit from more rigorous controls. **Score: 6.0.**

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>