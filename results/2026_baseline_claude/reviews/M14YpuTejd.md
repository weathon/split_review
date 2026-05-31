## Summary

This paper identifies three key methodological problems in the emerging online map-based motion prediction protocol for autonomous driving: (1) a train-validation gap caused by applying the map model on its own training data when constructing the motion model's training set, (2) a perception range mismatch—popular online mapping models cover only ~30×60 m while motion prediction must cover agents 100+ m away—which is obscured by evaluating only the ego vehicle, and (3) non-discriminative metrics dominated by static agents. The authors propose OMMP-Bench, a benchmark with a spatially disjoint data partition, refined agent-selection metrics (moving, non-ego, split by distance), and a boundary-free baseline that augments out-of-scope agents with deformable-attention image features.

---

## Strengths

- **Empirically demonstrated train-val gap.** Table 1 and the mAP figures (87.6 on train vs. 50.3 on val) provide concrete, reproducible evidence that the default protocol is fundamentally flawed. This is an easy-to-miss problem that could mislead the entire sub-field and is clearly presented.
- **Well-motivated metrics critique.** Evaluating only the ego vehicle is demonstrably misaligned with the stated purpose of motion prediction (collision avoidance with other agents). Table 6 shows that the ego vehicle is consistently the easiest agent to predict, while distant non-ego agents are the hardest—exactly where improvements are most needed.
- **Boundary-free baseline is effective.** The deformable-attention image-feature method yields a 12.7% minADE reduction for far non-ego agents (MapTRv2-CL + HiVT), and consistent gains across all four map/motion model pairs in Table 7. The improvement specifically concentrates where the range gap is most acute.
- **Spatial overlap analysis.** Figure 4 and the finding that 87% of the original nuScenes validation data overlaps with the training set is a concrete, actionable finding that extends recent community awareness (Yuan et al., 2024).

---

## Weaknesses

### Fatal
None.

### Major
- **Extremely limited model coverage.** The entire benchmark is built on 2 map models (MapTR, MapTRv2-CL) and 2 motion models (HiVT, DenseTNT). Whether the identified problems and the boundary-free baseline generalize to more modern or stronger models (e.g., StreamMapNet, LanSegNet as map models; QCNet, MTR++ as motion models) is entirely untested. A benchmark paper should demonstrate robustness across a broader set of baselines.
- **nuScenes-only scope with a smaller validation set.** The new partition yields only 86 motion validation scenes (versus 150 in the original val split). Given that the entire benchmark rests on nuScenes, absolute metric values are hard to interpret for the community and model ranking could be unstable with such a small val set. The paper does not analyze variance or report confidence intervals.

### Major (secondary)
- **The boundary-free baseline is technically shallow.** Applying deformable attention on multi-view image features to provide context for out-of-scope agents is a reasonable engineering choice but represents minimal technical novelty. The method section (Eq. 1) is two lines. The paper could explore why this works better than simply expanding the map range or using BEV features, but the analysis is limited to "image features do not have out-of-scope issues."

### Minor
- **Table 5 appears to have a duplicate row** (rows 2 and 3 both show `✗ ✓ ✗ ✗` with different minADE values 0.6829 vs. 0.6558). This may be an OCR artifact, but if genuine it undermines the ablation's readability.
- **The benchmark only evaluates moving vehicles as per 2+ m / 3 s.** The paper does not analyze sensitivity to this threshold or compare with alternatives, which may affect how many agents are included and overall metric values.
- **No discussion of how OMMP-Bench connects to the test-server evaluation** needed for community benchmarking; there is only an offline validation set.

### Trivial
- The description of the protocol in Figure 3's caption (Lower panel reference says "Upper") appears to be a parser artifact.

---

## Nice-to-Haves

- An analysis of model ranking stability under the proposed vs. original split would strengthen the claim that OMMP-Bench is a more reliable benchmark.
- Including at least one more recent map model (e.g., StreamMapNet) and one query-centric motion model (e.g., QCNet) would significantly increase the benchmark's immediate utility.
- Reporting variance across multiple runs or seeds, given the small validation set (86 scenes), would improve scientific rigor.

---

## Novel Insights

The most genuinely novel contribution is the demonstration that the standard two-stage training pipeline for online map-based motion prediction creates a structural data-leakage problem: because the map model is evaluated on its own training set during the construction of motion training data, the motion model is inadvertently trained on near-perfect maps but evaluated on degraded maps. This is a non-obvious and field-wide problem. The secondary insight—that evaluating only the ego vehicle systematically hides the worst failure cases (far agents outside map coverage)—is also a concrete and actionable finding, even if the underlying observation (static agents are easy) is known from other benchmarks. The combination of these two points reveals that prior results in this sub-field are essentially incomparable to realistic deployment conditions.

---

## Suggestions

- Extend Table 7 to include at least one stronger map model (StreamMapNet) and one newer motion model to validate that conclusions generalize beyond the two models currently tested.
- Report the number of agents in each evaluation group and provide error bars or inter-run variance on the 86-scene val set to support statistical credibility.
- Explicitly discuss the relationship between OMMP-Bench's val set (86 scenes) and the original nuScenes val split in terms of scene diversity (urban types, weather, etc.) to ensure the evaluation set is representative.
- Clarify the duplicate row in Table 5 and the "boundary only" condition.

---

## Score and Decision

The paper makes a clear, well-evidenced contribution to a nascent but rapidly growing sub-field: it identifies and quantifies two structural flaws in the dominant protocol and proposes a concrete benchmark to correct them. The boundary-free baseline is simple but effective. The main weaknesses—narrow model coverage and limited technical depth of the baseline—weigh against a strong accept, but they do not invalidate the benchmark's core value. The community genuinely needs this kind of systematic audit of new protocols.

MY FINAL SCORE: <score>6</score>
MY FINAL DECISION: <decision>Accept</decision>