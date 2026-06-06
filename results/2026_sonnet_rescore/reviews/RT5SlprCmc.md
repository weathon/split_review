## Summary

The paper proposes two self-supervised algorithms, MadDist and TDMadDist, for learning the Minimum Action Distance (MAD) from state trajectories, relying neither on reward signals nor on observed actions. It also introduces d_simple, a novel computationally simple quasimetric, and a diverse benchmark suite with known ground-truth MAD values. MadDist's core innovations are a scale-invariant loss (Eq. 5) and support for asymmetric quasimetric embeddings; empirical results show strong Pearson correlation and near-perfect planning success rates on OGBench PointMaze environments.

---

## Strengths

- **Scale-invariant loss prevents long-distance domination (Eq. 5):** By dividing the squared error by the index separation (j-i), MadDist avoids the bias in S&J's squared-error loss (Eq. 2), where far-apart pairs with large raw errors overshadow nearby pairs. The paper explicitly motivates this design and the resulting high Pearson correlations (>0.9) across environments confirm it works.

- **Quasimetric embeddings capture directional structure:** Figure 3 clearly shows that the symmetric Hilbert baseline degrades substantially in asymmetric environments (CliffWalking Ratio CV ~0.35, KeyDoorGridWorld ~0.6), while MadDist maintains low CV (~0.1–0.2). The direct comparison isolates the benefit of modeling directional irreversibility.

- **Planning results are impressive:** Table 1 shows MadDist achieving 1.00±0.00 success on PM Large Navigate, PM Large Stitch, and PM Medium Navigate, and 0.99±0.07 on PM Giant Stitch — consistently outperforming QRL (best 0.97) and Hilbert (best 0.67). This demonstrates that embedding accuracy translates to downstream task performance.

- **Benchmark suite with ground-truth MAD:** The controlled suite covering discrete/continuous, stochastic/deterministic, and noisy-observation settings enables unusually precise quantitative evaluation — a concrete and reusable community resource.

- **d_simple quasimetric:** Eq. 3 defines a parameter-free quasimetric that provably satisfies the triangle inequality and is computationally lightweight, yet matches or beats more elaborate quasimetrics (IQE, Wide Norm) in the ablation in Appendix E.

---

## Weaknesses

### Fatal
None.

### Major

- **Most direct predecessor (Steccanella & Jonsson, 2022) is absent as a baseline.** Section 6.1 explicitly frames MadDist as extending S&J (reproducing their loss as Eq. 2 and describing the two key differences: quasimetric distance and scale-invariant loss). Yet S&J is not included in any experiment. Without this comparison, the paper cannot isolate whether gains over QRL come from (a) the quasimetric formulation, (b) the richer trajectory supervision signal, or (c) the scale-invariant loss. The most natural ablation point — S&J's loss with a quasimetric — is missing entirely. This is the single most important evidential gap given the paper's own framing.

- **QRL comparison conflates quasimetric vs. supervision signal.** The Discussion (Section 7) acknowledges: "QRL only uses the locality constraints to learn the embeddings, while our method leverages the path distances between arbitrary states in a trajectory." MadDist therefore differs from QRL in at least two simultaneous ways. The paper's central claim — that asymmetric quasimetric distance is the key missing ingredient — is not directly demonstrated because no ablation separates the quasimetric from the richer supervision. A symmetric-distance version of MadDist's loss run in CliffWalking and KeyDoorGridWorld would suffice to make this claim.

- **Seed-count inconsistency.** Section 7 states: "All reported results are means over five independent runs (random seeds)." Figure 3's caption states: "Shaded regions minimum and maximum values across three random seeds." Three seeds vs. five seeds is a material discrepancy, given that standard deviations in Table 1 are already wide (e.g., TDMadDist 0.74±0.26 on PM Giant Stitch, MadDist 0.93±0.17 on PM Giant Navigate). This factual inconsistency must be resolved.

### Minor

- **TDMadDist's contribution is underexplored given its consistent underperformance.** The Discussion notes "TDMadDist underperforms the MadDist and QRL algorithm," but TDMadDist is presented as a coequal contribution. Notably, TDMadDist achieves 0.99±0.05 on PM Giant Navigate (Table 1) while MadDist achieves only 0.93±0.17 — an apparent exception to its general underperformance that goes unanalyzed. The paper would benefit from either identifying when TD bootstrapping helps or framing TDMadDist as a comparative negative result (which is itself informative).

- **Reversal between embedding accuracy (Figure 3) and planning success (Table 1) is unaddressed.** In Figure 3, TDMadDist's Pearson correlation (~0.85) trails MadDist (~0.9) on OGBench PM Giant Navigate. Yet in Table 1, TDMadDist (0.99±0.05) beats MadDist (0.93±0.17) on the same environment. This ranking reversal suggests planning success is not a monotone function of Pearson correlation, but this is never discussed. Understanding this discrepancy is important for interpreting which metric matters.

- **PointMaze ground truth is itself an approximation.** Section 7 states: "we use in our experiments to approximate the ground truth MAD by computing the all pairs shortest path using Floyd-Warshall over the maze graph." For PointMaze (a continuous environment), reported metrics conflate discretization error in the ground truth with method error. The paper treats PointMaze as providing known MAD but does not quantify this approximation.

### Trivial

None.

---

## Nice-to-Haves

- **Symmetric-MadDist ablation:** Running MadDist's full loss (scale-invariant + contrastive) with a symmetric distance (L2 norm) instead of a quasimetric in CliffWalking and KeyDoorGridWorld would cleanly isolate the quasimetric contribution. This single experiment would make the paper's central asymmetry claim unambiguous.
- **Regime analysis for TDMadDist:** If TDMadDist has an advantage in certain settings (e.g., very short trajectories where trajectory-length supervision is sparse), showing it explicitly would rescue TDMadDist as a meaningful contribution rather than a curiosity.
- **d_simple geometric limitations:** d_simple measures how much the source embedding exceeds the target (Eq. 3), contributing positively only when x_i > y_i. In environments with complex non-linear connectivity (e.g., multi-room mazes), this inductive bias may force distorted embeddings. A brief discussion of this would help practitioners decide when d_simple is appropriate.
- **d_max sensitivity:** The contrastive loss L_r (Eq. 6) introduces d_max as a new hyperparameter. A brief analysis of sensitivity to d_max across environments would clarify its practical robustness.

---

## Removed Points

*These points are flagged to be removed; treat them with caution.*

- **Harsh Critic — d_max hyperparameter criticism (Section 6.1):** The critic noted d_max has no principled choice and is deferred to Appendix D. Per the rules, missing appendix details should not be penalized — the appendix exists in the original submission. Moved to Nice-to-Have for practical sensitivity analysis.

- **Harsh Critic — d_simple geometric constraint speculation:** The critic argued that for environments without a clear linear ordering, d_simple may force distorted embeddings. This is speculative (not grounded in failure cases observed in experiments) and the paper shows empirically that d_simple works well. Moved to Nice-to-Have.

- **Strength Finder — "TDMadDist introduces a new learning paradigm":** This strength is largely invalidated by TDMadDist's consistent underperformance noted by the paper itself. Not a reliable strength.

- **Strength Finder — generic importance claim:** The introductory framing that MAD is important is generic and not a paper-specific strength. Removed.

---

## Novel Insights

The seed-count inconsistency (Section 7 vs. Figure 3) and the planning/correlation ranking reversal on PM Giant Navigate together suggest the paper has not fully examined the conditions under which each method excels. The reversal implies that Pearson correlation of embedding distances, while useful, is not a sufficient predictor of downstream planning success — TDMadDist's bootstrapped objective may inadvertently calibrate distances in a way that is suboptimal for regression but better suited for goal-directed search. This is an uncharted and potentially important finding about the relationship between representation quality metrics and task metrics.

---

## Suggestions

1. Add Steccanella & Jonsson (2022) as a baseline — their loss (Eq. 2) is already reproduced; only adding an experiment is required.
2. Run a symmetric-distance ablation of MadDist in the two asymmetric environments (CliffWalking, KeyDoorGridWorld) to isolate the quasimetric contribution from the supervision signal.
3. Resolve the seed inconsistency between Section 7 (5 seeds) and Figure 3 (3 seeds); standardize and restate.
4. Add a paragraph analyzing the PM Giant Navigate discrepancy between Figure 3 and Table 1 — this may reveal something important about the relationship between representation metrics and planning performance.
5. Either provide a regime analysis for TDMadDist (e.g., varying trajectory length) or explicitly frame it as an informative negative result.

---

## Score and Decision

**Evaluation axes:**
- *Originality:* Moderate. MadDist is incremental over Steccanella & Jonsson (2022) with two targeted changes (quasimetric + scale-invariant loss). d_simple and the benchmark suite are novel. The TD formulation is less original and underperforms.
- *Importance:* High. MAD learning is a broadly useful primitive for goal-conditioned RL, and a reliable approximation method with a controlled benchmark is a genuine contribution.
- *Claims supported:* Moderate. MadDist's empirical results are strong, but the paper's central attribution claim (quasimetric as the key ingredient) is not cleanly supported due to confounded comparisons and the absence of the S&J baseline.
- *Soundness:* Good. The methodology is principled; proofs for d_simple are deferred to the appendix (which exists). The seed inconsistency is a factual error.
- *Clarity:* Good. The paper is well-organized and the formalism is clean.
- *Community value:* High. The benchmark suite alone is a durable contribution; MadDist's strong planning results make it immediately useful.

The paper is close to acceptance: the MadDist results are strong, the benchmark suite is a real contribution, and the scale-invariant loss is a simple but non-obvious fix. However, the absence of the most natural baseline and the unsupported central attribution claim are real evidential gaps that fall short of the standard for a methods paper claiming asymmetric quasimetrics as the key missing ingredient. These are fixable in a revision.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>

<subscores>
<originality>3</originality>
<importance>4</importance>
<claims_supported>3</claims_supported>
<soundness>3</soundness>
<clarity>4</clarity>
<community_value>4</community_value>
</subscores>