Now I have all the information I need. Here is my final consolidated review:

---

## Summary

This paper identifies three systematic misconceptions in the emerging online-map-based motion prediction protocol: (1) inappropriate data splits causing a train-val gap under two-stage training, (2) misaligned perception ranges between online mapping models (e.g., 30×60m) and motion prediction (agents up to 100m+), and (3) non-discriminative metrics that evaluate only the ego vehicle and include trivial static agents. The authors propose OMMP-Bench with a spatially-disjoint three-way split, refined metrics that evaluate moving non-ego agents split by close/far distance, and a simple image-feature baseline to supplement map context for out-of-range agents.

## Strengths

1. **Quantitative demonstration of the train-val gap and a clean fix.** Table 1 shows that the default split yields minADE=0.6839 while the proposed split gives 0.6308, a measurable improvement. Row 2 shows that naively adding more data (Map Train + Motion Train) actually hurts (0.7006), confirming the distribution shift — not data quantity — is the issue. Figure 3 explains the mechanism clearly.

2. **Clear characterization of the perception-range mismatch.** Table 2 shows that extending MapTR's range from 30×60m to 100×100m collapses mAP from 0.124 to 0.014 (a 91% drop), while Table 3 shows GT maps at the larger range would help motion prediction only marginally (minADE 0.6154 → 0.6003). This convincingly demonstrates that simply scaling up map range is not viable.

3. **Refined metrics that surface previously hidden performance variation.** Table 6 shows that under the proposed metrics, the gap between HiVT+MapTR and DenseTNT+MapTR on "Moving Non-Ego Far" agents is a factor of 3.5× (minADE 0.6997 vs. 2.4140), while the existing ego-only metric showed a much smaller gap. This validates the claim that prior metrics were non-discriminative.

4. **Useful ablation of map element types (Table 5).** The systematic comparison of centerlines, boundaries, dividers, and pedestrian crossings provides concrete guidance for both mapping model design and motion prediction input selection.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor
1. **Close/far threshold is underspecified.** The paper states agents are classified as "close" or "far" based on "whether within the perception range of online mapping models" (line 261), but does not specify the exact geometric rule. The MapTR perception range is a 30×60m rectangle centered on the ego vehicle — it is unclear whether classification uses Euclidean distance from ego, rectangular bounding-box containment, or some other criterion. Different rules could shift population sizes and metrics.

2. **The "img" baseline's benefit for close agents is not discussed.** The paper motivates the image-feature baseline as a solution for agents outside the map's perception range. However, Table 7 shows it also improves close-agent predictions (e.g., MapTR+HiVT, Moving-Non-Ego-Close minADE 0.5585 → 0.5275, a ~5.5% improvement). The paper does not acknowledge or discuss this, leaving it ambiguous whether the improvement comes from genuinely addressing the range issue, from complementary features that help all agents, or simply from increased model capacity via the Deformable Attention module.

3. **No variance reporting on the small validation set.** The motion validation set contains only 86 scenes. The paper reports no standard deviations, confidence intervals, or multi-seed results anywhere. For a benchmark that aims to provide definitive comparisons, the lack of any uncertainty quantification is a concern — especially given that the proposed split shrinks the evaluation set relative to the default nuScenes val split.

4. **Resolution limitation of image features for distant agents not acknowledged.** The paper correctly notes that image features "do not have out-of-scope issues," but does not discuss that an agent 80–100m away occupies only a few pixels in the camera image, severely limiting the information content of those features. This is a practical limitation of the proposed baseline that should be acknowledged.

### Trivial
None.

## Nice-to-Haves
- A capacity-controlled ablation for the "img" baseline (e.g., adding a similarly sized feature module that does not use image features) would strengthen the attribution of improvement to the image modality specifically.
- Reporting results across multiple random seeds (3–5) would help the community calibrate trust in the reported numbers.
- The paper could quantify the interaction between the train-val gap and the range misalignment problem — i.e., whether the distribution shift compounds the difficulty for far agents.

## Removed Points
These points were raised by the reviewers but removed from the main review for the reasons stated:
- **"img" baseline improvement for close agents "undermines the claimed mechanism" as a fatal flaw** — Removed: The paper presents the image-feature baseline as a practical mitigation for the range mismatch, not as a controlled experiment proving that the mechanism is exclusively far-agent supplementation. The improvement for close agents does not invalidate the approach. Reframed as a missing discussion point (Minor #2 above).
- **Capacity-controlled ablation demand as a "critical issue"** — Removed: The paper is a benchmark/diagnostic paper, not a methods paper; the baseline is a reasonable first attempt. A capacity-controlled ablation would strengthen the paper but its absence is not a critical flaw. Moved to nice-to-have.
- **Table 1 Setting 4 vs Setting 1 discussion point** — Removed: This is a genuine observation but it is a discussion point, not a weakness. The authors' choice is justified by the reasoning in the paper.
- **Generic/superficial strengths** — Removed per filtering rules.

## Novel Insights
None beyond the paper's own contributions.

## Suggestions
- Clarify the exact geometric rule for classifying agents as close vs. far.
- Add a brief discussion of why the "img" baseline also helps close agents and whether this reflects a separate mechanism.
- Acknowledge the validation set size limitation and, if feasible, add multi-seed variance estimates.
- Discuss the practical resolution limits of camera features for very distant agents.

## Score and Decision

### Calibration Procedure

**Round 1 — Bracketing (low / middle / high):**
- Low band (< 3.5): Retrieved `pzZjyYee6L` (2.50, "Don't Reinvent the Steering Wheel"), `MI0UiWeqOl` (2.33, "Poly-Autoregressive Modeling"), `DCg9r2DKKe` (2.50, "STL-Drive"), `0qfIhtel8N` (3.00, "Liquid Dino") — all rejected. Our paper is substantially stronger than these.
- Middle band (3.5–7.5): Retrieved `sEJYPiVEt4` (5.25, "ESDMotion"), `72MSbSZtHv` (5.33, "RedMotion"), `r125wFo0L3` (5.00, "Large Trajectory Models"), `8tWOUmBHRv` (4.00, "Offline Tracking"). Our paper is stronger than ESDMotion (5.25) and comparable to the others in this band.
- High band (> 7.5): Retrieved papers all at 8.00 (large-scale benchmarks like MMIE, PhysBench). Our paper is not at this level.

Initial bracket: **4.0–7.0**.

**Round 2 — Narrowing:**
- Retrieved `sEJYPiVEt4` (5.25, ESDMotion) — our paper has clearer contributions and better evidence for its diagnostic claims.
- `72MSbSZtHv` (5.33, RedMotion) — our paper is better organized and has less ambiguous contributions.
- `cfuZKjGDW7` (6.00, TAO-Amodal) — benchmark paper with mixed reviews (5,6,5,8); our paper is similarly focused but smaller in scale.
- `M42KR4W9P5` (6.67, DriveTransformer) — methods paper with SOTA results, stronger than our paper.
- `4S9bBbX1be` (5.75, DriveArena) — mixed reviews (3,6,8,6), our paper has clearer contributions.
- `DCpukR83sw` (5.75, Interactive Adjustment) — accepted despite having a fundamental assumption problem; our paper has fewer fundamental issues.
- `Im2neAMlre` (7.33, "One slice is not enough") — comprehensive evaluation methodology paper, much stronger.

Final bracket: **5.0–6.0**.

**Comparative judgment:** Our paper sits slightly above ESDMotion (5.25) because the diagnostic contributions are more crisply demonstrated and the paper is better written. It is below TAO-Amodal (6.00) in scale but comparable in contribution focus. The weaknesses (underspecified threshold, lack of variance reporting, missing discussion of baseline behavior) are real but addressable. The paper is a solid diagnostic contribution to a narrow subfield.

### Final Score and Decision

**Score: 5.5 / 10**
**Decision: Reject**

The paper identifies genuine, well-evidenced misconceptions in an emerging evaluation protocol — this is a useful service to the community. However, the scope is narrow (nuScenes only, two map models, two motion models), the validation set is small (86 scenes with no variance reporting), and several analytic details (close/far threshold, behavior of the "img" baseline for close agents) are left underspecified. These weaknesses are addressable, and the core diagnostic analysis is solid, but in its current form the paper does not meet the bar for acceptance at ICLR.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>