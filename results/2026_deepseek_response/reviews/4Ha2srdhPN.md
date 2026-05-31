## Summary

This paper presents GRAID, a framework that generates high-quality spatial reasoning VQA data by analyzing only 2D bounding boxes from object detectors, deliberately avoiding error-prone 3D reconstruction and LLM-based question generation. GRAID includes SPARQ, a predicate-based interface that accelerates generation by early rejection of infeasible candidates (up to 1407× speedup). Applied to BDD100k, NuImages, and Waymo, it produces over 8.5M VQA pairs. Human evaluation shows 91.16% validity vs. 57.6% for a SpatialVLM-generated dataset. Fine-tuning experiments demonstrate that models trained on GRAID data learn transferable spatial concepts that generalize across datasets, question types, and external benchmarks.

---

## Strengths

1. **Human evaluation provides concrete quality evidence.** The paper conducts a careful human evaluation with 4 annotators over 317 GRAID pairs and 250 SpatialVLM pairs across comparable protocols. The 91.16% validity rate for GRAID vs. 57.6% incorrect answers for SpatialVLM (Section 4, line 182-188) directly supports the headline claim in a verifiable, quantitative way.

2. **Cross-dataset and cross-question-type generalization is convincingly demonstrated.** RQ1 (Section 5, line 198) shows that SFT on GRAID-BDD improves accuracy on held-out GRAID-BDD from 31%→80.7% (+49.7 pp) and on unseen GRAID-NuImages from 38%→67.1% (+29.1 pp). RQ2 (line 200-201) shows that training on only 6 question types improves accuracy on over 10 held-out types, including size/aspect questions never seen during training. This provides strong evidence that the model learns transferable spatial primitives, not dataset-specific patterns.

3. **SPARQ efficiency is measured with concrete, reported numbers.** The paper provides specific timing benchmarks (Section 3.2, line 136): predicate completion averages 5.17ms vs. 46.95ms for full realization (9× slowdown on lightweight templates), and up to 1407× speedup on heaviest templates like `LargestAppearance`. This is a verifiable engineering contribution that directly supports scalability claims.

4. **Clean differentiation from prior work via structured comparison.** Table 1 (line 67-76) systematically compares GRAID against SpatialVLM, SpatialRGPT, and SpaRE across six features (3D reconstruction avoidance, LLM-based QA avoidance, architectural changes required, etc.), giving readers a clear, specific understanding of GRAID's advantages.

---

## Weaknesses

### Major

None.

### Minor

1. **Inconsistency between Algorithm 1 and the text description of the "similar planes" check.** The text (Section 3.2, line 138) states that the `RightOf` realization algorithm requires checking that candidate bounding boxes "lie on similar planes" as a necessary condition. However, Algorithm 1 (lines 110-134) only checks `IoU = 0` and `x_min(b1) > x_max(b2)` and contains no plane-awareness or y-coordinate check. The text explicitly says "The full algorithm of the `RightOf` question is provided in Algorithm 1," yet this condition is absent. This does **not** invalidate GRAID's core approach—the 2D geometry insight is still sound—but it signals an unclear implementation detail that should be resolved. Either add the check to the pseudocode or explain why it was omitted (e.g., because bounding box overlap already handles the practical cases).

2. **Inter-annotator agreement is not reported for the human evaluation.** The paper uses four human evaluators (Section 4, line 184) with independent random seeds, and reports summarizing aggregate statistics (28 unique problematic pairs, 91.16% valid). However, no agreement metric (e.g., Fleiss' kappa or pairwise agreement) is reported. Given that 28/317 pairs were flagged as problematic, it is valuable to know how many were flagged by multiple annotators versus single annotators. This is standard practice for human evaluation studies and would strengthen confidence in the validity assessment.

3. **Metric framing in the abstract conflates positive and negative measures.** The abstract states that GRAID achieves "91.16% human-validated accuracy" while the SpatialVLM dataset has "a 57.6% human validation rate." However, Section 4 (line 182) reports that 57.6% of SpatialVLM answers were **incorrect**—a negative measure—while 91.16% of GRAID pairs had no issues. These are not the same metric (one is percent-clean, the other percent-incorrect). The 57.6% figure used in the abstract as a "validation rate" is actually the error rate (implying 42.4% valid answers, not 57.6%). The large gap is real and directionally correct, but the framing as the same metric is misleading. The authors should report consistent positive metrics for both datasets.

### Trivial

None.

---

## Nice-to-Haves

- **Test with predicted detections.** The paper deliberately uses ground-truth AV annotations to isolate GRAID's effectiveness (justified in Section 4, line 155), but a small experiment with a standard detector (e.g., YOLOv8) on a subset would strengthen the claim of being "detector-agnostic" and demonstrate practical deployment feasibility.
- **Explicit limitations paragraph.** The paper does not discuss cases where 2D geometry may be ambiguous for spatial relations (e.g., perspective projection causing objects at different depths to appear left/right of their true 3D ordering, severely occluded objects). Adding this would preempt a natural criticism and improve completeness.
- **Report consistent positive metric for SpatialVLM.** Compute the percentage of pairs with both valid question and correct answer (instead of just incorrect-answer rate) for both datasets to enable a clean apples-to-apples comparison.

---

## Removed Points

These points were flagged by reviewers but removed from the main weaknesses for the stated reasons:

- **"Missing Tables 4, 5, 6"** — The paper's tables were stripped by the PDF parser; they exist in the original submission.
- **"Missing SpatialVLM training details (dataset size, steps, hyperparameters)"** — The main text (line 202) states "full training details are provided in Appendix A.3," which was stripped by the parser. RQ1 and RQ2 training details are fully specified in the main text.
- **"Never tests with a real object detector"** — This is a deliberate scope choice (the paper states it uses ground-truth annotations "so that we can evaluate GRAID's effectiveness in isolation," line 155). Moved to Nice-to-Have.
- **"Algorithm 1 doesn't match text's 'similar planes' description"** — This is real and is kept as a Minor weakness above (it was not removed).
- **"Missing limitations section"** — Moved to Nice-to-Have.

---

## Novel Insights

None beyond the paper's own contributions. The reviews do not surface any perspective not already present in or derivable from the paper.

---

## Suggestions

1. Resolve the discrepancy between Algorithm 1 and the text: either add the "similar planes" (y-coordinate overlap) check to the pseudocode or clarify why it was omitted and how the text description should be interpreted.
2. Report inter-annotator agreement (Fleiss' kappa or pairwise agreement) for the human evaluation.
3. Recalculate and report a consistent positive metric (percent of pairs with both valid question and correct answer) for both GRAID and SpatialVLM datasets, and use this in the abstract.

---

## Score and Decision

### Calibration

**Round 1 (Bracketing):** Three calibration queries on spatial reasoning data generation.

| Anchor | Score | Round | Comparison |
|--------|-------|-------|------------|
| `V73W8MXnNW` — Progressive Visual Relationship Inference | 3.00 | 1 | Lower-quality work; GRAID is significantly stronger |
| `Akccupz2pP` — GTD-LLM gaze target | 3.40 | 1 | Unrelated task, lower quality |
| `IlleFmPNb6` — Training-Free RAG for KI-VQA | 3.40 | 1 | Unrelated task |
| `uBhqll8pw1` — 3D Reasoning of VLMs in Indoor Scene Layout | 4.00 | 1 | Similar topic; GRAID is stronger with more concrete contributions |
| `vXG7d2VlHU` — Sparkle | 4.50 (Reject) | 1 | Most similar anchor. Sparkle also trains on synthetic spatial data. GRAID provides a full framework + large-scale dataset + human eval, making it substantially stronger |
| `84pDoCD4lH` — COMFORT (FoR evaluation) | 7.40 (Accept) | 1 | Higher-quality work with deep analysis; GRAID has a more practical contribution (usable datasets + framework) and comparable experimental rigor |
| `9Y6QWwQhF3` — FoREST | 4.25 (Reject) | 1 | Lower quality |
| `WyEdX2R4er` — Visual Data-Type Understanding | 8.00 (Accept) | 1 | Stronger overall; GRAID is below this |
| `Q6a9W6kzv5` — PhysBench | 8.00 (Accept) | 1 | Larger-scale benchmark effort; GRAID is below this level |
| `3i13Gev2hV` — Compositional Entailment Learning | 8.00 (Accept) | 1 | Stronger theoretical contribution |
| `7gUrYE50Rb` — EQA-MX | 8.00 (Accept) | 1 | Stronger overall |

**Round 1 initial bracket:** 5.5–7.5. GRAID is clearly above the reject-level papers (3.0–4.5) but below the 8.0-level papers (PhysBench, Visual Data-Type). It sits around COMFORT (7.40) in quality.

**Round 2 (Narrowing):** Two queries targeting 4.5–6.5 and 6.0–8.0.

| Anchor | Score | Round | Comparison |
|--------|-------|-------|------------|
| `Dkz8npDqAv` — 3D Annotation | 5.33 (Reject) | 2 | Different task; GRAID is stronger |
| `NuHYh4YKNe` — Spatial Localization | 6.25 (Accept) | 2 | Comparable quality; GRAID has more practical contribution |
| `NDkpxG94sF` — V-DETR 3D Object Detection | 6.00 (Accept) | 2 | Different task |
| `HBEjrlu7Aa` — Object-level Data Augmentation | 5.67 (Reject) | 2 | Different task |
| `g1fkhbhHjL` — Black Sheep (spurious correlations) | 7.00 (Accept) | 2 | Similar rigor; GRAID comparable |
| `X1OfiRYCLn` — Dynamic Multimodal Evaluation | 7.50 (Accept) | 2 | Stronger; GRAID is slightly below this |
| `G6DLQ40VVR` — DivScene (object navigation) | 6.25 (Reject) | 2 | GRAID is stronger |
| `WK6K1FMEQ1` — SPACE (spatial cognition) | 6.75 (Accept) | 2 | Similar scope (spatial reasoning); GRAID compares well. SPACE is a comprehensive benchmark with 15 tasks but no data generation framework; GRAID provides a practical tool + datasets |

**Final assessment:** GRAID is a solid paper with a clear, sound idea, a convincing human evaluation, and compelling generalization experiments. Its weaknesses are minor (algorithm pseudocode inconsistency, missing inter-annotator agreement, metric framing). It is clearly above reject-level papers (3–5) and comparable to mid-level accept papers (6.5–7.5). It does not reach the level of the strongest papers (8.0+). The most comparable anchor, SPACE (6.75, Accept), is a thorough benchmark paper; GRAID is more practically useful and has stronger evidence for its core claims. I place it slightly above SPACE.

**Final score: 7.0, Accept.**

MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>