Now I have all the information I need. Let me synthesize the final review.

---

## Summary

This paper presents MadDist, a self-supervised method for learning asymmetric state embeddings that approximate the Minimum Action Distance (MAD) — the minimum number of steps needed to transition between states — using only unlabeled state trajectories. The method combines a scale-invariant regression loss, a contrastive term, and constraint penalties with a novel simple quasimetric to model asymmetric distances. A bootstrapped variant, TDMadDist, is also proposed. The approach is evaluated on a diverse benchmark suite spanning discrete/continuous state spaces, stochastic/deterministic dynamics, and noisy observations, where MadDist consistently outperforms prior symmetric and quasimetric baselines in both distance-approximation accuracy and downstream planning success.

## Strengths

- **MadDist's core loss design is well-motivated and effective.** The scale-invariant objective (Equation 5) prevents far-apart state pairs from dominating the loss, while the contrastive term (Equation 6) prevents representation collapse and the constraint penalty enforces trajectory-derived upper bounds. These components together yield a method that consistently recovers the ground-truth MAD with higher Pearson correlation and lower Ratio CV than QRL and Hilbert baselines across all tested environments (Figure 3).

- **The evaluation is comprehensive and well-controlled.** The paper introduces a benchmark suite where ground-truth MAD is known — including KeyDoorGridWorld (asymmetric key-door dynamics), CliffWalking (irreversible cliff transitions), and PointMaze variants (from UMaze to OGBench Giant Maze) — and evaluates three complementary metrics (Spearman, Pearson, Ratio CV). This addresses a genuine gap: prior MAD-approximation work lacked systematic accuracy evaluation.

- **The learned representations translate directly to downstream value.** Table 1 shows MadDist achieving near-perfect or perfect planning success rates (1.00±0.00 on four PointMaze variants, 0.99±0.07 on Giant Stitch), decisively outperforming QRL, TDMadDist, and Hilbert. The strong performance on *stitch* datasets — which require composing information from disconnected trajectories — demonstrates the representations capture global environment structure, not just local trajectory patterns.

- **The simple quasimetric (Equation 3) is a genuinely useful contribution.** Despite its minimal form — a weighted combination of max and average ReLU differences — it yields state-of-the-art performance when embedded in MadDist, outperforming QRL which uses the more complex IQE formulation. The paper shows this is not merely a parameter-count advantage but a well-chosen inductive bias for MAD approximation.

## Weaknesses

### Fatal

None.

### Major

None. The main contribution (MadDist) is methodologically sound and empirically well-supported.

### Minor

- **TDMadDist is presented without analysis of its underperformance.** The bootstrapping objective (Equation 8) uses `min(j-i, 1 + d_{θ'}(s_{i+1}, s_j))` as a target. Since the true MAD satisfies only `d_MAD(s_i, s_j) ≤ 1 + d_MAD(s_{i+1}, s_j)` — with equality not guaranteed when a shorter path skips `s_{i+1}` — this objective can systematically bias estimates upward. The paper notes empirically that TDMadDist underperforms MadDist but offers no diagnosis. While TDMadDist is not the main contribution, providing this analysis would turn a mixed result into an instructive comparison and strengthen the paper's narrative about why direct supervision (MadDist) is preferable to bootstrapping.

- **The ground-truth MAD approximation for continuous PointMaze environments lacks sufficient detail.** The paper states (Section 7) that MAD is approximated by computing all-pairs shortest paths "over the maze graph," but does not specify how continuous (x,y) positions are mapped to grid cells for computing the reference distance. While approximating a continuous MDP's MAD via a discretized grid is a reasonable protocol, the lack of detail about the mapping and its potential mismatch with the true continuous MAD leaves some ambiguity about the reliability of the reported correlation metrics on these environments.

- **Key hyperparameter `d_max` is introduced without discussion in the main text.** The contrastive loss (Equation 6) depends on `d_max`, which controls the target separation for randomly sampled pairs. Its role — whether it sets a soft ceiling on distances, how it interacts with the scale-invariant loss, and how sensitive performance is to its value — is not addressed in the main body. Even a single sentence characterizing its function and typical values would improve the self-containedness of the presentation.

### Trivial

- **The `1.00 ± 0.00` success rates in Table 1** (PM Large Navigate/Stitch, PM Medium Navigate/Stitch) are reported without comment. Whether this reflects a deterministic planning process, ceiling performance, or a reporting convention deserves a brief note.

- **Computational scalability of the contrastive term** (random pair sampling from all states in all trajectories) is not discussed, which matters for practitioners applying the method to large state spaces.

## Nice-to-Haves

- Including a brief note about when the simple quasimetric (`d_simple`) suffices versus when richer alternatives (IQE, Wide Norm) might be needed would contextualize the architectural choice, given that Appendix E reportedly ablates this comparison.
- A discussion of sensitivity to the loss weights `w_r`, `w_c` and the horizon cutoff `H_c` in the main text would reassure practitioners about the method's robustness to hyperparameter choices.

## Removed Points

These points are flagged to be removed; treat them with caution:

- **Harsh Critic: "d_max role and tuning are deferred to the appendix" as a significant omission.** The appendix is stripped in the review copy; the paper may well discuss this there. This concern is retained above as a minor presentation point about main-text self-containedness, but the claim that the information is entirely missing is not verifiable.
- **Harsh Critic: "missing sensitivity discussion" as a standalone major weakness.** The paper states that Appendix E contains ablation studies demonstrating robustness to latent dimension, quasimetric choice, and dataset size. Stripped appendices prevent verification. Retained only as a nice-to-have about main-text coverage of specific hyperparameters.
- **Strength Finder: "TDMadDist introduces a bootstrapped TD objective... demonstrating competitive planning success."** While factually true that TDMadDist achieves 0.99±0.05 on PM Giant Navigate, this selectively highlights the best result. TDMadDist underperforms MadDist across nearly all metrics and environments. The strength is retained but contextualized.
- **Strength Finder: "thorough ablation studies (described in Section 7 and detailed in Appendix E)."** We cannot verify appendix content. The claim is noted as stated by the authors but not independently confirmed.

## Novel Insights

None beyond the paper's own contributions. The reviews confirm that the paper's combination of scale-invariant loss, simple quasimetric, and trajectory-only supervision for MAD approximation is genuinely novel and effective. The TDMadDist analysis gap is an insight the reviews surfaced — identifying a specific structural reason (the `≤` vs. `=` relationship in the TD target) why bootstrapping may be fundamentally mismatched to MAD learning — but this insight belongs to the review process, not the paper.

## Suggestions

- Add a brief analysis (even 2-3 sentences) diagnosing *why* TDMadDist's bootstrapping objective may overestimate MAD: note that `d_MAD(s_i, s_j) ≤ 1 + d_MAD(s_{i+1}, s_j)` is an inequality, not an equality, and pushing the learned distance toward the right-hand side can inflate estimates when trajectories are suboptimal. This would strengthen the paper's case for MadDist's simpler supervised approach.
- In the PointMaze description, add one sentence specifying how continuous (x,y) positions map to grid cells for ground-truth computation (e.g., "each position is assigned to the nearest grid cell center" or "the state is discretized to the containing grid cell").
- Add a brief note in the main text about `d_max` — its role (e.g., "d_max sets a soft ceiling encouraging random state pairs to be at least this far apart, preventing the embedding from collapsing all states together") and its typical setting.

## Score and Decision

**Calibration anchors used:**

| Anchor | Avg Score | Round | Comparison |
|--------|-----------|-------|------------|
| `RmOXAa5H5Y` (Simplicial repr. learning) | 3.00 | 1 (weak) | Significantly weaker: narrow contribution, limited evaluation |
| `x7Q0uFTH2a` (Weak bisimulation metric) | 3.75 | 1 (mid) | Weaker: theoretical issues, sloppy presentation, baseline concerns |
| `oEzY6fRUMH` (State Chrono Representation) | 4.75 | 1 (mid) | Weaker: mixed results, limited evaluation, ad-hoc loss design |
| `TOiageVNru` (Physics-informed TD metric) | 6.00 | 2 (narrow) | Comparable but weaker: improvements over baselines are modest, ablation limited to single environment |
| `cWdAYDLmPa` (Unbalanced Atlas) | 6.67 | 1+2 (mid) | Comparable: good evaluation but clarity issues, less decisive empirical gains |
| `I7DeajDEx7` (Episodic Temporal Distance) | 6.75 | 2 (narrow) | Comparable: strong results but limited action spaces, novelty concerns |
| `ms0VgzSGF2` (Bridging State/History Repr.) | 6.75 | 2 (narrow) | Different type: primarily theoretical; not directly comparable |
| `agPpmEgf8C` (Predictive aux. objectives) | 8.00 | 1 (strong) | Stronger: broader scope, brain-science connection, all reviewers confident accept |

**Round-1 bracket:** Between 5.5 and 7.5, with the paper clearly above the 3.75-4.75 rejected papers and below the 8.0 top-tier accepts.

**Round-2 narrowing:** The paper sits above TOiageVNru (6.00) — which had modest empirical gains and mixed reviews — and is comparable to or slightly stronger than I7DeajDEx7 (6.75) and cWdAYDLmPa (6.67). Like I7DeajDEx7, this paper has a clear novel method, strong empirical results across diverse benchmarks, and minor weaknesses (under-analyzed secondary method, some implementation details not discussed). Unlike cWdAYDLmPa, this paper's motivation is crisp, its results are decisive, and its practical value is demonstrated through downstream planning.

**Final score:** 7.0 — a solid accept. The MadDist method is well-designed, well-motivated, and convincingly outperforms existing approaches across a carefully constructed benchmark. The TDMadDist analysis gap and ground-truth approximation detail are addressable in revision and do not undermine the core contribution.

MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>