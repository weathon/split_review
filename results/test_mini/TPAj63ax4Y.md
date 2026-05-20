## Summary

This paper proposes a three-stage framework (Segment, Select, Correct) for weakly-supervised Referring Image Segmentation. Stage 1 uses Grounding DINO + SAM to generate candidate instance masks for the object category mentioned in a referring expression. Stage 2 selects the most likely correct mask via CLIP-based reverse-blur visual prompting. Stage 3 trains a RIS model using a constrained greedy matching loss that exploits the multi-expression-per-object structure in RefCOCO datasets to correct zero-shot selection mistakes. The method achieves new state-of-the-art in both zero-shot and weakly-supervised RIS, narrowing the gap to the fully-supervised LAVT from ~33% to as little as 7% on RefCOCO+ testA. The ablations convincingly isolate the contribution of each stage.

## Strengths

- **Large and robust performance gains.** The full weakly-supervised method (\ours) outperforms prior weakly-supervised methods (TRIS, TSEG, Shatter&Gather) by up to 26 oIoU points, and the zero-shot variant (\zsours) outperforms GL CLIP by up to 16.5 oIoU points. These margins are large enough that missing error bars do not undermine the core claims.

- **The constrained greedy matching loss is the clear driver of improvement.** The ablation in Table 2 shows that the correction step (jumping from 37.02 to 57.22 oIoU on RefCOCO val) is responsible for most of the gain, while additional training on the same zero-shot masks (+40 epochs) gives negligible improvement. This cleanly isolates the contribution.

- **Thorough stage-wise ablations with oracle upper bounds.** Each stage is ablated independently on held-out training examples (Tables 3-5), with oracle comparisons (73.27 oIoU for mask generation) and random baselines (21.81), providing clear readers with a clear understanding of remaining headroom.

- **Efficient trained inference.** Once trained, the model runs in 0.2s per sample (vs. 1.78s for \zsours and 2.95s for GL CLIP (SAM)), a practical advantage for deployment.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

- **The method exploits a dataset structure that may not hold in all deployment scenarios.** The constrained greedy matching loss critically depends on having multiple referring expressions per object instance so that constraints ② (same object → same mask) and ③ (different objects → different masks) can be enforced. This matches the standard weakly-supervised setting from prior work (TRIS, TSEG, Shatter&Gather) and the paper acknowledges the limitation (Discussion: "more successful in datasets where there are more referenced objects per image"). However, the paper would benefit from evaluating a single-expression-per-object variant to clarify how much performance drops when this structure is absent.

- **Missing oracle upper bound for the full pipeline.** The paper reports an oracle for Stage 1 mask generation (73.27 oIoU on 1k samples) but does not report an oracle for the output of Stage 3 (i.e., what performance would the model achieve if the greedy matching had access to ground-truth assignment decisions?). This would help quantify remaining headroom.

- **Pseudocode typo in Algorithm 1.** Line 152 checks `if c in C or j in C`, but `C` contains tuples `(j', c')`, so this condition as written would never be true. The conceptual description in the main text (line 133) correctly uses `(j,c) not in C`, so the algorithm is clear, but the pseudocode should be fixed.

- **The class projection step in Stage 1 requires a priori knowledge of the object categories.** The paper acknowledges this limitation in the Discussion. It is not a fatal issue given that the same limitation applies to the baselines and that open-vocabulary detectors continue to improve.

### Trivial
- The paper does not report error bars or variance. Given the margins (10-26% improvements over baselines), this does not threaten any core claim but would strengthen the presentation.
- Figure 6 caption references subfigures (a) and (b) but the figure environment uses `subfigure` without labels — a minor formatting issue.

## Nice-to-Haves
- Evaluate on a simulated single-expression-per-object scenario to test generalizability beyond the multi-reference benchmark structure.
- Report the Stage 3 oracle (greedy matching with ground-truth assignments) to quantify remaining headroom.
- Test whether skipping the class projection step entirely by using Grounding DINO's open-vocabulary detection (which already supports arbitrary text queries) degrades performance on the full dataset (the ablation on 1k samples shows a drop from 73.27 to 58.87, but this deserves verification at scale).

## Removed Points

These points are flagged to be removed; treat them with caution.

1. **"The zero-shot baseline comparison is misleading because baselines are not contemporary"** — The paper does include a proper baseline (G-DINO + SAM, line 238) that keeps the mask generator identical (Grounding DINO + SAM) and varies only the selection method. G-DINO + SAM achieves 27.59 oIoU while \zsours achieves 34.39 on RefCOCO val, showing that the selection mechanism matters beyond the mask generator. The critic's claim is factually incorrect.

2. **"The 33%-to-7% claim is presented as a general statement in the abstract"** — The abstract literally says "in some cases from around 33% to as little as 7%." The experiments section then gives RefCOCO+ testA as the specific example. This is accurate framing.

3. **"The paper does not discuss failure cases where Stage 1 misses an object"** — The paper explicitly discusses this on line 133: "the number of set bluedataset masks might be smaller than the number of objects if Stage 1 fails to segment one or more instances."

4. **"Class projection limitation should be stated earlier"** — The paper acknowledges it in the Discussion. This is a presentation preference, not a substantive weakness.

5. **Most of the "Missing Experiments" and "Deeper Analysis Needed" items** — These are standard extensions that would strengthen any paper but are not required for soundness given the paper's already thorough ablations and large margins.

6. **Strength Finder's generic strengths** ("this paper addressed an important problem") — dropped as they lack specific content or conflict with verified weaknesses.

## Novel Insights

None beyond the paper's own contributions. The core novelty is the constrained greedy matching loss that leverages the multi-reference structure to correct zero-shot selection mistakes — this is well-articulated in the paper.

## Suggestions

- Fix the pseudocode in Algorithm 1 (line 152: change `c in C or j in C` to `(j,c) in C`).
- Add an oracle upper bound for Stage 3 to show remaining headroom.
- If space permits, include an experiment using only one expression per object to demonstrate robustness to the single-expression setting.

## Score and Decision

**Calibration anchors (all from the human review corpus):**

| Path | Avg Score | Comparison |
|------|-----------|------------|
| `/home/wg25r/split_review/datasets/deepreview_13k_calibration/EQAHilKZ8D.md` | 2.20 | Much weaker — limited experiments on 3-4 images, unclear methodology. This paper is substantially stronger. |
| `/home/wg25r/split_review/datasets/deepreview_13k_calibration/mXh8LbXXpx.md` | 3.50 | Weaker — primarily a benchmark study with a simple ensemble of existing methods. This paper contributes a novel algorithmic framework with larger gains. |
| `/home/wg25r/split_review/datasets/deepreview_13k_calibration/0jUeqlQxMi.md` | 4.00 | Weaker — retrieval-augmented panoptic segmentation with limited novelty and missing comparisons. This paper has cleaner ablations and stronger results. |
| `/home/wg25r/split_review/datasets/deepreview_13k_calibration/cSAAGL0cn0.md` | 5.50 | Comparable — both are weakly-supervised segmentation papers with solid contributions. This paper has clearer ablations and larger empirical margins. |
| `/home/wg25r/split_review/datasets/deepreview_13k_calibration/4JbrdrHxYy.md` | 6.00 | Similar — both propose annotation-free pipelines using CLIP+SAM with strong empirical results and similar-level technical novelty. |
| `/home/wg25r/split_review/datasets/deepreview_13k_calibration/Pm1NXHgzyf.md` | 6.00 | Similar — both introduce a well-structured framework with thorough experiments and clear writing. This paper has stronger quantitative margins over baselines. |
| `/home/wg25r/split_review/datasets/deepreview_13k_calibration/QzPKSUUcud.md` | 6.25 | Slightly stronger — simple yet effective zero-shot segmentation with strong results and clean exposition. Comparable contribution level. |

Relative to these anchors, the paper delivers a clear, well-ablated framework with large empirical gains (10-26% over prior work). The main limitation — reliance on the multi-reference structure — is a characteristic of the standard weakly-supervised setting it operates in, not an oversight. The paper does not have fatal flaws.

MY FINAL SCORE: 6.0
MY FINAL DECISION: Accept