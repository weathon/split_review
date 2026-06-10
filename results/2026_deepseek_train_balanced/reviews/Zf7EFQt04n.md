## Summary

The paper proposes FeudalNav, a three-tiered hierarchical visual navigation system using a self-supervised Memory Proxy Map (MPM) as a latent-space memory, a WayNet trained on human demonstrations for waypoint prediction, and a learned classifier for low-level obstacle-avoidance. The main claims are achieving SOTA on image-goal navigation in Gibson/Habitat without using RL, graphs, odometry, or metric maps, while being orders of magnitude more data-efficient (37K frames vs. millions for competitors).

## Strengths

- **Data efficiency is dramatic and well-documented.** Training on ~37K frames from 117 LAVN trajectories on a single consumer GPU (vs. 14.5–500M frames on up to 64 GPUs for competitors) is a concrete practical advantage supported by explicit training details (Section 4, line 139). This is a genuine, specific claim that clearly distinguishes the approach from prior work.

- **Ablation study convincingly isolates the MPM's contribution.** Table 2 systematically varies MPM type (none, binary cluster, binary all-observations, Gaussian heatmap), WayNet input, and worker type. Removing the MPM drops straight success to ~37%; adding the Gaussian variant ("H") raises it to 57–67%. The Gaussian heatmap outperforms binary variants by ~28%, confirming that the *specific MPM design* drives performance.

- **Novel synthesis of ideas that jointly avoids standard navigation crutches.** The three-tier feudal hierarchy with an isomap-imitated latent latent space, human-demonstration-trained WayNet, and classifier-based low-level worker is a genuinely new combination that achieves competitive results without RL, graphs, odometry, or metric maps.

## Weaknesses

### Fatal
None.

### Major

1. **No variance or statistical significance for any reported result.** Table 1 (main results) and Table 2 (ablation) report only single point estimates. The test set covers ~6K point pairs across 14 environments, making it straightforward to report per-environment variance or results across seeds. Without this, the reader cannot assess whether FeudalNav's advantage over NRNS+SLING on straight trajectories (67.5 vs. 64.4 Succ, a ~5% relative gain) is robust or within noise. Several ablation configurations show dramatic swings (e.g., "H" + 3 RGBD-M + Cl on curved drops to 25.33 Succ from 60.2 — a 58% change from altering only input frame count), but without variance estimates it is impossible to distinguish genuine sensitivity from random variation. This undermines the precision of every comparative claim in the paper.

2. **The central spatial-encoding claim for the MPM rests on a qualitative comparison on a single trajectory.** The claim that the MPM encodes "a proxy for relative distance between real world observations" (Figure 4, caption) is the conceptual foundation for replacing odometry and graphs. Yet the evidence is a visual heatmap comparison of SMoG, MoCo, ResNet, and SwAV feature-distance matrices against ground-truth metric distances — for *one* trajectory in *one* environment (Copemish, line 221). No quantitative correlation (Spearman ρ, Kendall τ, or any other metric) between SMoG feature distance and metric distance is reported. The paper's key technical innovation is thus validated only by eyeballing.

### Minor

1. **No limitations or failure-case analysis.** The paper makes strong claims about replacing graphs and odometry but does not acknowledge obvious failure modes: visual aliasing (two visually similar but spatially distant locations producing nearby MPM embeddings), SuperGlue failures in texture-poor environments, or degradation of the isomap imitator's approximation on unseen environments. This omission makes it difficult to assess the method's practical scope.

2. **WayNet is evaluated only qualitatively.** WayNet's predicted waypoints are shown alongside human ground-truth clicks (Figure 3) with the claim that "the majority of the samples show high overlap." No quantitative metric (pixel-distance error, angular error) is reported. For a claimed contribution (contribution #2), this is a notable absence.

3. **Inflated percentage claims obscure the real magnitude of improvements.** The paper reports "3380% improvement over BC methods on curved trajectories" (line 201). This arises because BC methods achieve near-zero success (1.7% Succ), making any non-zero result appear dramatic in relative terms. Absolute numbers (FeudalNav 60.2% vs. BC 1.7%) tell a cleaner and more honest story than the inflated percentages.

4. **Speculative real-world claim.** "In the real world, it is less likely that a robot will be tasked to find an object within a straight line of sight from itself" (line 204) is presented to justify emphasizing curved-trajectory results but is unsupported by any evidence or citation.

5. **Hyperparameter sensitivity not analyzed.** The three confidence thresholds α_c, α_k, α_m are all set to 0.7 "empirically" (line 139). The ablation does not vary these, so the reader cannot gauge robustness to this choice.

### Trivial
None.

## Nice-to-Haves

- Compute a quantitative correlation (Spearman ρ) between SMoG feature distances and metric distances across multiple trajectories/environments to rigorously validate the MPM.
- Add a brief quantitative evaluation of WayNet (pixel-distance error to human ground-truth on held-out LAVN data).
- Discuss the NRNS+SLING curved SPL anomaly (43.7 Succ but only 14.3 SPL — successful trajectories are ~3× optimal length), which may indicate a qualitative behavioral difference worth noting.

## Removed Points

- The concern that baselines were "evaluated under potentially different conditions" is removed as speculative — the paper explicitly follows the NRNS evaluation protocol (line 141), making this an unsupported assertion.
- The vague "Strengthening the Paper on Its Own Terms" suggestions from the harsh critic that duplicate the weaknesses above are absorbed into the Nice-to-Haves section.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. **Add variance reporting to Tables 1 and 2.** Report mean ± std across environments or random seeds. This is the single highest-leverage improvement for rigor.
2. **Quantify the MPM's spatial encoding.** Compute and report Spearman ρ or Kendall τ between SMoG feature distance and metric distance across multiple trajectories and environments.
3. **Add a limitations paragraph** acknowledging visual aliasing, SuperGlue failure modes, isomap imitator approximation error, and conditions under which FeudalNav may fail (e.g., distance bins or environment types with lower performance).
4. **Replace inflated percentages** (3380%) with absolute comparisons or frame them transparently as improvements from near-zero baselines.
5. **Include a brief hyperparameter sensitivity analysis** for the three confidence thresholds (α_c, α_k, α_m).

## Score and Decision

The paper introduces a genuinely novel combination of ideas with impressive data efficiency and a convincing ablation study. However, its central claims are undercut by two significant evidential gaps: (a) the complete absence of variance reporting, which makes the claimed SOTA results unverifiable in terms of robustness, and (b) the core MPM spatial-encoding claim resting on a single qualitative visual comparison. For a top venue, these gaps are too large to overlook in the current form, though they are addressable with additional experiments.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Reject</decision>