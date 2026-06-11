**Round 1 bracket:** [4.5, 7.0] — the paper is clearly above Sparkle (4.50) and STUPD (4.33) but below top-band papers (7.5+).

**Round 2 narrowing:** The most topically comparable anchors are Sparkle (4.50, rejected) where GRAID is substantially stronger (8.5M pairs vs 2K images, 4 backbones vs 1, finer-grained experiments); DivScene (6.25, rejected) where GRAID has a cleaner contribution; and Does Spatial Cognition Emerge (6.75, accepted) / GeomRel (6.67, accepted) where GRAID has comparable thoroughness but a weaker framing choice.

**Final score:** 6.0 — solid, well-executed paper with genuine contributions.

---

## Summary

GRAID is a framework that generates spatial VQA training data using only 2D bounding boxes and geometric rules, avoiding errors from 3D reconstruction and LLM hallucinations. It produces 8.5M VQA pairs from three driving datasets, achieving 91.16% human-validated accuracy. Fine-tuning experiments show that models trained on GRAID data learn transferable spatial concepts that generalize across question types and benchmarks (BLINK, A-OKVQA, etc.), demonstrated across four different VLM backbones.

## Strengths

1. **2D-only geometric analysis avoids cascading 3D reconstruction errors**: GRAID operates exclusively on 2D bounding boxes, which are far more reliable than monocular depth/pose estimates. The paper demonstrates this advantage through a head-to-head human evaluation: a community SpatialVLM dataset achieved only 57.6% valid answers while GRAID achieves 91.16% human-validated accuracy (Section 4).

2. **SPARQ predicate-based early rejection yields measurable efficiency gains**: Concrete timing data is provided: RightOf predicates complete in 5.17ms vs. 46.95ms for full realization (~9× faster), and LargestAppearance predicates finish in 0.02ms (1407× speedup) while implying realization success 78.8% of the time (Section 3.2). Both average and extreme cases are reported transparently.

3. **Fine-tuning on GRAID data yields cross-dataset and cross-question-type generalization**: RQ1 shows a model fine-tuned on GRAID-BDD improves from 31%→80.7% on held-out GRAID-BDD and from 38%→67.1% on unseen GRAID-NuImages. RQ2 shows training on only 6 question types improves accuracy on over 10 held-out types, with overall gains of +47.5 pp on BDD and +37.9 pp on NuImages (Section 5, Figure 3). This demonstrates that the model learns transferable spatial concepts rather than memorizing dataset-specific patterns — this is the paper's most compelling evidence.

4. **Consistent gains across four VLM backbones on external benchmarks (RQ3)**: Llama 3.2 11B, Gemma 3 4B, Qwen2.5 VL 3B, and Qwen3 VL 8B are fine-tuned on GRAID data and evaluated on five benchmarks (BLINK, NaturalBench, A-OKVQA, RealWorldQA, VSR). Llama shows +32.5% on A-OKVQA and +15.94% on BLINK overall, with +41.13% on BLINK's Relative Depth subset. Testing multiple architectures reduces the chance that gains are specific to one model family (Section 5).

5. **Configurable margin_ratio for depth-based questions**: Rather than SpatialVLM's wide [50%, 200%] tolerance, GRAID uses a margin_ratio parameter that only realizes a depth question when the predicted distance ratio exceeds a threshold, providing a principled way to avoid ambiguous questions (Section 4).

## Weaknesses

### Fatal
None.

### Major

1. **The headline validity comparison (91.16% vs 57.6%) compares fundamentally different question types, and the paper's framing overstates the implication.** SpatialVLM questions are metric (e.g., "How far is object A from object B?") requiring monocular depth estimation — intrinsically harder questions with continuous answers. GRAID asks qualitative binary questions (e.g., "Is there at least one traffic sign to the left of any truck?") deterministically answerable from 2D bounding box coordinates. The paper acknowledges this distinction in Section 4 ("rather than asking how far an object is in terms of metric distance, it's easier to answer which object is closer"), but the abstract, introduction, and conclusion present the 33-percentage-point gap as straightforward evidence of "higher quality" without adequately qualifying that the two datasets test different kinds of spatial reasoning at different difficulty levels. This framing is the paper's most consequential weakness. **However, the paper's core contributions — the framework, SPARQ, and especially the transfer learning results (RQ2, RQ3) — do not depend on this comparison and stand on their own.**

### Minor

2. **The "similar planes" check is mentioned but never defined.** Section 3.2 states that for RightOf, bounding box pairs must "lie on similar planes" to avoid ambiguous spatial relations, yet the paper never specifies how coplanarity is determined from 2D bounding boxes alone. Without depth information, this appears to require some heuristic, but no implementation detail is provided. Additionally, Algorithm 1 (the RightOf realizer) does not include this check, creating a mismatch between the text and the algorithm.

3. **The 57.6% figure is attributed to the SpatialVLM method in the introduction, but it comes from a community reimplementation.** The abstract and introduction (lines 9, 51) frame 57.6% as "a dataset produced by a current training data generation pipeline" and "SpatialVLM... yet our human evaluation reveals that only 57.6% of questions are valid," which could be read as evaluating the original method. Section 4 properly clarifies that OpenSpaces is "generated by the community implementation of SpatialVLM." The paper should consistently distinguish the method from this specific reimplementation.

4. **No confidence intervals reported for human evaluation percentages.** With N=317 for GRAID and N=250 for OpenSpaces, the reported percentages have non-trivial sampling uncertainty that should be quantified (Section 4).

5. **No variance across random seeds reported for fine-tuning experiments.** RQ1 and RQ2 train for only 200 steps on a fraction of an epoch, which could make results sensitive to random seed (Section 5). Reporting results across 2-3 seeds would increase confidence.

6. **The validity of the depth-based question variant is not reported.** The human evaluation uses only the "without depth" variant of GRAID-BDD (Section 4). Since depth estimation is less reliable than 2D boxes, the validity rate for the depth variant is likely lower and should be reported.

### Trivial
7. Algorithm 1 for RightOf does not include the "similar planes" check described in the text, creating a mismatch between the description and the pseudocode.

## Nice-to-Haves
- A controlled comparison where both GRAID and SpatialVLM-style questions are generated from the *same* source images would isolate the effect of question/answer quality from data distribution differences.
- Reporting object detection accuracy on the source datasets would help contextualize the ~9% error rate (how much stems from detection failures vs. rule design vs. ambiguous scenes).
- A small-scale demonstration on a non-driving dataset (e.g., COCO) would substantiate the domain-agnostic claim without requiring large-scale generation.
- Testing longer training with early stopping on the regressed question types (LessThanThresholdHowMany) would clarify whether the observed regression is indeed overfitting.

## Removed Points
- **Criticism about the 1400× speedup being misleading**: The paper reports BOTH the average case (9× for RightOf) AND the extreme case (1407× for LargestAppearance) in the same paragraph (Section 3.2), with the additional context that 78.8% of predicate successes imply realization success. The paper is transparent about the range.
- **Criticism that the human evaluation "checks whether the code is correct"**: Showing evaluators images with bounding boxes superimposed is standard practice for VQA data validation. The paper additionally has evaluators assess without boxes to judge difficulty on a Likert scale. This is a standard protocol, not a flaw.
- **Criticism about missing tables 4, 5, 6 in the appendix**: These tables are in the appendix which was stripped by the parser. The paper reports key results textually. Weaknesses about missing appendix content are removed per policy.
- **Criticism about missing related works/citations**: Cannot verify without external sources per policy.
- **Formatting/typo criticisms**: These are parser artifacts, not author errors.

## Novel Insights
None beyond the paper's own contributions. The harsh critic and strength finder converge on the same central tension: the paper's strongest experimental result (transfer learning in RQ2 — training on 6 simple question types improving 10+ unseen types) is its least flashy claim, while the headline validity comparison (91.16% vs 57.6%) is the most attention-grabbing but also the most methodologically questionable due to asymmetric question difficulty. The paper would be stronger if it foregrounded the transfer results and presented the comparison with appropriate caveats.

## Suggestions
1. Reframe the comparison with SpatialVLM to explicitly acknowledge the different question types: GRAID generates qualitative spatial questions answerable from 2D geometry, while SpatialVLM tackles harder metric questions requiring 3D estimation. The 91.16% figure remains impressive as a measure of data fidelity within its chosen class of questions, but should not be presented as a simple "higher quality" verdict over a harder task.
2. Define the "similar planes" heuristic or remove the check from the description if it is not actually implemented. Ensure Algorithm 1 matches the text description.
3. Consistently distinguish "the community implementation of SpatialVLM" from "the SpatialVLM method" throughout the paper, not just in Section 4.
4. Add confidence intervals for human evaluations and report variance across seeds for fine-tuning experiments.
5. Report validity for the depth variant; consider a small-scale non-driving domain demonstration.

## Calibration Anchors

**Round 1 — Bracketing:**
| Paper | Avg Score | Round | Comparison |
|---|---|---|---|
| Sparkle (vXG7d2VlHU) | 4.50 | R1 | Most topically similar; GRAID is substantially stronger (8.5M pairs vs 2K images, 4 backbones vs 1, human eval) |
| STUPD (eqz5aXtQv1) | 4.33 | R1 | Synthetic spatial dataset; GRAID has broader evaluation |
| On Inherent 3D Reasoning (uBhqll8pw1) | 4.00 | R1 | Evaluation-only paper, no data generation framework |
| Depth/Height Perception (t1LfiWCYux) | 4.00 | R1 | Evaluation-only, more limited scope |
| DivScene (G6DLQ40VVR) | 6.25 | R1 | Benchmark+method paper; GRAID has clearer contribution |
| PhysBench (Q6a9W6kzv5) | 8.00 | R1 | Comprehensive benchmark, different contribution type |
| GenSim (OI3RoHoWAN) | 8.00 | R1 | Robotics simulation, different topic |

**Round 2 — Narrowing:**
| Paper | Avg Score | Round | Comparison |
|---|---|---|---|
| Sparkle (vXG7d2VlHU) | 4.50 | R2 | Best topical match; GRAID clearly stronger |
| Does Spatial Cognition Emerge (WK6K1FMEQ1) | 6.75 | R2 | Comprehensive spatial cognition benchmark, accepted; GRAID comparable in thoroughness |
| GeomRel (FjQOXenaXK) | 6.67 | R2 | Geometric reasoning benchmark+method, accepted; GRAID comparable but different contribution type |
| DivScene (G6DLQ40VVR) | 6.25 | R2 | GRAID has cleaner narrative and more consistent evaluation |
| Spatial Frame of Reference (84pDoCD4lH) | 4.67 (retrieval avg) / 7.40 (review avg) | R2 | Ambiguity in spatial language evaluation, different contribution type |

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>