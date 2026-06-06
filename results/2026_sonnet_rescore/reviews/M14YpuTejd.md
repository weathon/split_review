## Summary

This paper identifies and corrects three systematic methodological flaws in the emerging online map based motion prediction (OMMP) protocol: (1) a severe train-validation gap caused by inappropriate dataset splits, (2) a range mismatch between online mapping models (~30×60m coverage) and motion prediction requirements (>100m), and (3) non-discriminative metrics that evaluate only the easy-to-predict ego vehicle. The authors propose OMMP-Bench, a corrected benchmark featuring a spatially disjoint three-way split, refined metrics for moving non-ego agents grouped by distance, and a boundary-free baseline using deformable attention over raw image features to supply environmental context for out-of-range agents.

---

## Strengths

- **Compelling, well-evidenced identification of the train-val gap.** Fig. 3 documents that the online mapping model achieves mAP 87.6 on its own training set but only 50.3 on the unseen validation set — a nearly 40-point drop — directly demonstrating why motion prediction models trained on map-training-set inference fail at evaluation. The proposed three-way split produces similar mAP at both train (48.9) and val (50.3) stages, eliminating the gap. This is the paper's most important contribution and is rigorously documented.

- **Effective boundary-free baseline addressing the range mismatch.** The deformable-attention image feature retrieval (Eq. 1) provides each agent with environmental context regardless of whether it falls within the online map's perception boundary. Table 7 shows consistent and large gains for far agents across all model combinations tested — e.g., 12.7% minADE reduction for HiVT+MapTRv2-CL on the Moving-Non-Ego-Far group — directly validating that the identified range misalignment is both real and practically addressable.

- **Well-motivated, data-driven case for refined evaluation metrics.** Table 6 shows static agents achieve near-zero minADE (~0.002), confirming that their inclusion in aggregate metrics suppresses discriminability. The paper's decision to evaluate only moving non-ego agents, stratified by proximity to the ego, is clearly justified and aligns with the real purpose of motion prediction (collision avoidance with other agents).

- **Comprehensive empirical coverage.** Table 7 provides a full matrix across two online mapping models (MapTR, MapTRv2-CL), two motion predictors (HiVT, DenseTNT), and three integration methods (unc, bev, img), establishing consistent trends and giving the community a replicable starting point.

---

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

- **Table 1 cross-split comparison is not fully apples-to-apples.** Splits 1–2 are evaluated on the new Motion Val set (86 scenes), while Splits 3–4 (default protocol) are evaluated on the original nuScenes Val set. The numeric comparison across these rows cannot cleanly establish that "our split achieves better performance" because the val sets differ. The underlying train-val gap argument is compelling and well-supported by Fig. 3, but Table 1's cross-split numbers should be framed more carefully — the correct framing is "our split eliminates a known confound" rather than "our numbers are lower," since the denominator changes. A cleaner comparison would also evaluate the proposed split on the nuScenes val set, or vice versa, to isolate the split's effect.

- **86-scene motion validation set with no variance reporting.** The three-way partition yields only 86 validation scenes. nuScenes evaluation is already known to be noisy at standard scale; at 86 scenes, run-to-run or bootstrap variance may be material. For a paper whose central deliverable is a corrected benchmark intended for community use, the absence of any reliability characterization (across seeds, or via bootstrap confidence intervals) is a genuine gap. Several comparisons in Table 7 show method differences of ~1–5% in minADE; without variance estimates it is unclear which of these are robust.

- **Spatial disjointness contribution not isolated from stage-separation fix.** Split 4 in Table 1 (random 50%/50% partition of the training set, evaluated on nuScenes val) achieves minADE 0.6373, close to Split 1's 0.6308. This suggests much of the improvement comes from the stage-separation fix (training motion model on data unseen to the map model), not specifically from spatial disjointness. The paper does not directly address whether spatial disjointness provides additional benefit beyond stage separation. Given that the paper motivates the split partly on spatial disjointness grounds (Fig. 4, 87% → 5% overlap reduction), this conflation should be acknowledged.

### Trivial

- **"SOTA" claim in Section 3.3 is underspecified.** The paper states the image-feature baseline "achieves SOTA performance" (last line before Table 4), but Table 4 contains only HiVT+MapTR. The claim is accurate only within the narrow scope of the methods evaluated on OMMP-Bench and should be qualified accordingly to avoid overclaiming.

---

## Nice-to-Haves

- **Demonstrate what conclusions change under the old vs. new protocol.** The paper shows that numbers change, but does not show whether *method rankings* change. If OMMP-Bench reverses the ordering of methods that appeared superior under the old protocol, that would be a much stronger argument for the benchmark's necessity. If rankings are stable, the contribution reduces to "our absolute numbers are more honest," which still matters but less acutely.

- **Image-feature gain broken down by exact ego distance, not just close/far binary.** A continuous analysis of the img baseline's benefit as a function of agent-to-ego distance would make the mechanism transparent and help practitioners decide when image features are and are not sufficient as a map substitute.

- **Explicit acknowledgment of migration cost.** Since the new metrics are fundamentally different from prior work (evaluating moving non-ego agents rather than ego only), OMMP-Bench cannot directly track progress relative to existing literature. Acknowledging this and explaining why re-running prior methods on OMMP-Bench is out of scope would strengthen the paper's self-awareness about its role in the community.

---

## Removed Points

*These points are flagged to be removed; treat them with caution.*

- **Table 5 "duplicate row" (Harsh Critic).** Rows 2 and 3 of Table 5 both read "✗|✓|✗|✗" in the extracted text with different minADE values (0.6829 and 0.6558). The paper text states "centerlines are most helpful and centerlines only achieve the second best performance," which is consistent with row 3 representing a centerline-only condition (✗|✗|✗|✓) that was misrendered by the PDF extractor. Per hard rules, this is a parser artifact, not an author error. **Removed.**

- **MapTRv2-CL mAP collapse from 0.164 to 0.002 when extended to 100×100m "may only reflect training distribution."** The paper's claim is explicitly that "simply expanding the perception range of the map prediction model leads to decreased map accuracy" — i.e., that naive range extension doesn't work. The paper does not claim it is fundamentally impossible to train a longer-range model; it claims current models trained for 30×60m fail when naively extended. Table 2 directly supports this claim. The critic's alternative ("maybe fine-tuning would help") is speculative and outside the paper's stated scope. **Removed as scope creep.**

- **Criticism that SOTA is not compared against an "established leaderboard."** OMMP-Bench is itself the new benchmark; there is no prior leaderboard to compare against by construction. **Removed as a strawman.**

- **Strength: "Systematic analysis of map element types… centerlines are most informative."** While Table 5 provides useful ablations, the table's third row is ambiguous due to PDF parsing, and the paper's claim that "centerlines only achieve second best performance" cannot be independently confirmed from the extracted text. Kept as a supporting strength in spirit, but the specific centerline-only claim should be treated with caution pending table resolution.

---

## Novel Insights

The most genuinely novel observation synthesized across both reviews is the **asymmetry between how prior methods fare on ego vs. non-ego agents**: Table 7 shows that methods (unc, bev) which improve ego prediction sometimes *degrade* close non-ego prediction relative to the base method (e.g., MapTRv2-CL+DenseTNT unc and bev increase minADE for far non-ego agents by ~4%). This suggests that prior optimizations for ego-centric evaluation may inadvertently sacrifice non-ego prediction quality — a finding that is invisible under the old protocol and that the refined OMMP-Bench metrics are uniquely positioned to surface. This makes a stronger case for OMMP-Bench than the paper's own framing emphasizes.

---

## Suggestions

1. **Re-evaluate at least one split comparison on a shared val set.** To make Table 1 interpretable, run Split 1 on nuScenes val (or run Split 3/4 on Motion Val). Even a footnote showing that the trend holds would address the confounding.

2. **Report bootstrap or multi-seed standard deviations for Table 7.** Given the 86-scene val set, even a brief characterization (e.g., ±σ from 3 seeds on one model combination) would substantially strengthen the benchmark's credibility as a community reference.

3. **Add an ablation isolating spatial disjointness.** A variant of Split 1 that uses stage separation but not spatial disjointness (e.g., randomly sampled subsets from the same geographic areas) would clarify how much of the gain comes from each component.

4. **Reframe the "SOTA" claim in Section 3.3** to explicitly scope it to "best among methods evaluated on OMMP-Bench."

5. **Clarify Table 5 row 3 in the camera-ready.** Whether it is centerline-only or a duplicate of boundary-only should be made unambiguous; the paper's text implies the former.

---

**Axes assessment:**
- **Originality:** Moderate — the paper targets a specific but important protocol correction rather than introducing a novel method. The identification of the train-val gap and the image-feature baseline are creative and well-executed.
- **Importance:** High — fixing systematic methodological errors early in an emerging field has outsized long-term value.
- **Claims well-supported:** Mostly — the core claims (train-val gap, range mismatch, static-agent dilution) are all solidly supported. Some quantitative framings (Table 1 cross-split, centerline-only performance) need tightening.
- **Soundness of experiments:** Good — comprehensive model combinations in Table 7; main gap is absence of variance estimates given small val set.
- **Clarity:** Good — the paper is well-organized and identifies its contributions crisply.
- **Community value:** High — OMMP-Bench directly addresses mis-usage of an emerging benchmark protocol that already has CVPR 2024 attention.

---

MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>

<subscores>
<originality>3</originality>
<importance>4</importance>
<claims_supported>3</claims_supported>
<soundness>3</soundness>
<clarity>4</clarity>
<community_value>4</community_value>
</subscores>