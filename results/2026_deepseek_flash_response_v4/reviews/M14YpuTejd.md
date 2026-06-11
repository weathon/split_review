Now I have sufficient information to calibrate. Let me write the final review.

**Calibration anchor papers considered:**

| Paper | Score | Round | Comparison |
|-------|-------|-------|-----------|
| ITPNet (mDIXfHvoqH) | 6.75 | R1, middle | Trajectory prediction methods paper; stronger on method novelty but rejected due to outdated baselines. Paper under review has more complete experiments and its contributions (benchmark fixes) are arguably more durable. |
| SEPT (efeBC1sQj9) | 7.00 | R1, middle | Strong motion prediction methods paper with SOTA and clean ablations. The paper under review is clearly weaker — lacks the clean SOTA results and has concrete data issues. |
| RedMotion (72MSbSZtHv) | 5.33 | R1, middle | Motion prediction methods paper with questionable contributions. The paper under review has better empirical support and clearer motivation. |
| ESDMotion (sEJYPiVEt4) | 5.25 | R2, low-mid | Most topically relevant anchor — also about online maps + motion prediction. The paper under review is stronger: more rigorous analysis, better experiments, and addresses a more fundamental problem (protocol flaws vs. "yet another method"). |
| TAO-Amodal (cfuZKjGDW7) | 6.00 | R3, mid | Benchmark paper with scores 5,6,5,8. Similar type of contribution (identifying limitations in existing evaluation protocols). The paper under review has clearer motivation and stronger empirical evidence. |
| Spawrious (W0zgCR6FIE) | 5.75 | R3, mid | Benchmark addressing methodological issues (spurious correlations). Comparable contribution type; similar rigor. |
| Fusion Is Not Enough (3VD4PNEt5q) | 6.25 | R3, mid | AD safety analysis paper; accepted. Strong experiments and clear practical implications. |

**Round 1 bracket:** The paper sits between weak anchors (~3-3.5) and strong anchors (~8). The most plausible range is 5.0–7.0.

**Round 2 narrowing:** Comparing against ESDMotion (5.25), TAO-Amodal (6.00), and Fusion Is Not Enough (6.25), the paper lands around **6.0**. It is clearly stronger than ESDMotion (more rigorous, more comprehensive). It is comparable to or slightly stronger than TAO-Amodal (clearer motivation, better experiments). It is slightly weaker than Fusion Is Not Enough (which was accepted with strong practical contributions).

The Table 5 inconsistency is a concrete flaw but does not undermine the paper's core contributions (split, range analysis, metrics), which are independently supported by other experiments. The paper has real, actionable contributions for the community and identifies genuine problems in an emerging protocol.

---

## Summary

This paper identifies and fixes three misconceptions in the emerging two-stage protocol for online map based motion prediction: (1) inappropriate data splits cause a train-validation gap for the motion prediction model, (2) the perception range of online mapping models (30×60m) is mismatched with motion prediction requirements (agents up to 100m away), and (3) existing metrics that evaluate only ego trajectories or include trivial static agents are non-discriminative. The authors propose OMMP-Bench with a spatially-disjoint three-way data split, metrics that evaluate moving non-ego agents by distance, and a boundary-free baseline using image features to address range mismatch.

## Strengths

- **The train-validation gap is clearly quantified and convincingly demonstrated.** Figure 3 shows map mAP at 87.6 on the motion training set vs. 50.3 on the motion validation set under the default protocol — a 37.3-point gap. The proposed split reduces this to near parity (48.9 vs. 50.3). Table 1 confirms that downstream motion prediction improves under the new split (minADE 0.6308 vs. 0.6839 for default).

- **The perception range mismatch is empirically well-supported.** Table 2 shows MapTR's mAP collapses from 0.124 (30×60m) to 0.014 (100×100m), while Table 3 shows that longer-range *GT* maps would actually help motion prediction (minADE 0.6154→0.6003). This cleanly isolates map model capability as the bottleneck, not motion prediction capability.

- **The boundary-free baseline validates the core motivation.** Table 7 shows the "img" method achieves its largest gains on far non-ego agents (e.g., HiVT+MapTR minADE improves from 0.6997 to 0.6318), directly confirming that the range mismatch problem is meaningful and addressable.

- **Comprehensive evaluation across 16 method combinations × 3 agent groups** (Table 7) surfaces non-obvious findings — e.g., methods improving ego prediction sometimes degrade far-agent prediction — that prior ego-only evaluation would have masked.

- **Clean empirical justification for excluding static agents.** Table 6 shows both methods achieve minADE≈0.002 on static agents, proving they would make metrics artificially non-discriminative.

- **Well-bounded scope.** The paper explicitly distinguishes the two-stage online-map protocol from fully end-to-end methods (ViP3D, UniAD), avoiding confounding.

## Weaknesses

### Major

- **Table 5 contains a data inconsistency and does not support its headline claim.** Two rows have identical configurations (Boundary=✓, all others=✗) but report different minADE values (0.6829 and 0.6558). Separately, the paper claims "centerlines are most helpful" — but Table 5 has *no centerline-only condition*: every row with centerlines also includes boundaries. Without a centerline-only row, the relative importance of individual element types cannot be assessed from the presented data. The actual claim supported by the data is simply "all elements combined is best."

- **No variance or statistical significance information.** All tables report single-point estimates with no error bars, confidence intervals, or multiple-seed averages. For a benchmark paper whose main claims rest on comparing differences between conditions (new split vs. default in Table 1, img vs. base in Table 7, close vs. far in Table 6), the lack of variance information weakens confidence in whether reported differences are reliable. This is especially concerning for small absolute differences (e.g., Split 1 at 0.6308 vs. Split 4 at 0.6373 in Table 1, a gap of only 0.0065).

### Minor

- **The "img" baseline comparison is structurally asymmetric.** The image-feature baseline extracts raw sensory information via Deformable Attention, giving it access to uninterpreted visual data that the map-based baselines (using only vectorized map elements) lack. The comparison conflates the benefit of additional sensory access with the benefit of the architecture design. The paper should acknowledge this, positioning the baseline primarily as an *illustration* of what addressing range mismatch can achieve, rather than as a direct SOTA competitor.

- **Split 4 (Table 1) achieves results close to the proposed split's.** The 50/50 subset split of nuScenes training data achieves minADE 0.6373 vs. the proposed split's 0.6308. This suggests the train-val gap fix (avoiding the map model overfitting to motion training data) is the dominant factor, and spatial disjointness provides additional but modest benefit. The paper should discuss this rather than treating the new split as uniformly superior.

- **Split criteria are described only at a high level.** The paper states "we manually check the whole dataset and split it into three spatially disjoint sets" without specifying the precise algorithm or distance threshold for determining spatial overlap. For a benchmark others are expected to adopt, the generation procedure needs specification.

### Trivial

- Table 5's twin rows with identical configuration but different numbers need correction.
- The sentence "centerlines are most helpful and centerlines only achieve the second best performance" (Section 3.5) is internally contradictory.

## Nice-to-Haves

- Add a centerline-only row to Table 5 to directly support the claim about centerline importance.
- Report map model mAP on motion training vs. motion validation sets under both old and new splits to directly validate that the new split closes the map-quality gap.
- Consider running key comparisons (at least Tables 1 and 7) with 2–3 random seeds to provide variance estimates.

## Removed Points

The following points from the inputs are removed with justification:

- **Harsh Critic: "The train-val gap analysis does not acknowledge that Split 4 achieves close results."** — This is kept as a Minor weakness (it's a valid observation), not removed.
- **Harsh Critic: "The paper should evaluate map model's mAP under both splits."** — Moved to Nice-to-Have. It would strengthen the paper but is not a core flaw; the paper already shows motion prediction differences.
- **Harsh Critic: Various generic framing about the comparison being "structurally tilted"** — Kept but weakened to Minor. The asymmetric comparison is real, but the paper's framing as "a new baseline" (not a competitor) partially mitigates this, and the contribution stands on its own merits.
- **Strength Finder strengths about "important problem" or generic praise** — These generic strengths are removed. Only concrete, evidence-backed strengths are kept.
- **Strength Finder: "Systematic ablation of map element types (Table 5)"** — Demoted. The strength is partially valid but the table has a data inconsistency and the centerline claim is unsupported, making this strength unreliable as stated.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. **Fix Table 5.** Correct or explain the duplicate rows. Add a centerline-only condition to support the claim about centerline importance, or retract the unsupported interpretation.
2. **Add variance information.** At minimum, report results from 2–3 seeds or provide error bars for the key comparative claims (Tables 1, 4, 7).
3. **Clarify the "img" baseline positioning.** Acknowledge the asymmetric information access and reframe as an illustrative upper bound for range-mismatch mitigation rather than a SOTA competitor.
4. **Discuss the Split 4 result.** Acknowledge that the train-val gap fix is the primary driver, with spatial disjointness providing additional but modest benefit.
5. **Specify the spatial disjointness criteria.** State the minimum distance or overlap threshold used for the new split so others can reproduce it.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>