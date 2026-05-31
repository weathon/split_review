Now let me run calibration searches to score this paper.**Round 1 Bracket: 5.0 – 7.0**

Now let me narrow within this bracket.Now I have enough information to write the final review. Let me synthesize everything.

---

## Summary

This paper proposes two self-supervised algorithms—MadDist and TDMadDist—for learning the Minimum Action Distance (MAD) between states using only unlabeled state trajectories, requiring neither rewards nor explicit action labels. The authors also introduce d_simple, a novel asymmetric quasimetric that is computationally lightweight yet competitive with more complex alternatives. Finally, the paper contributes a benchmark suite of environments with known ground-truth MAD values spanning deterministic/stochastic and discrete/continuous settings, enabling rigorous evaluation of MAD approximation methods.

---

## Strengths

- **Scale-invariant loss is well-motivated and demonstrably effective.** Eq. 5 divides the squared error by the trajectory step difference (j−i), preventing long-horizon state pairs from dominating training. This design is directly validated by Figure 3, where MadDist achieves Pearson correlations >0.9 and ratio CV <0.2 across diverse asymmetric and large-scale environments, compared to collapse or high variance in the baselines.

- **Quasimetric formulation correctly captures directional structure.** By supporting d_simple, d_WN, and d_IQE (Eqs. 3–5, Section 5), the method faithfully models irreversibility in tasks like CliffWalking and KeyDoorGridWorld. Figure 3 confirms the necessity: the symmetric Hilbert baseline collapses (CV >0.35) in those environments while MadDist maintains CV ≈ 0.1.

- **Strong downstream planning performance.** The learned MadDist embeddings achieve near-perfect (1.00 ± 0.00) success rates in five OGBench PointMaze configurations including stitch and giant layouts (Table 1), surpassing all baselines. This validates that metric-level accuracy translates to practical downstream utility—not just curve fitting.

- **Novel benchmark with known ground truth.** The suite (NoisyGridWorld, KeyDoorGridWorld, CliffWalking, PointMaze variants, OGBench variants) is a concrete community contribution enabling controlled evaluation. Prior evaluations of MAD approximation have lacked ground-truth access.

- **d_simple is a genuinely compact quasimetric contribution.** Unlike d_WN and d_IQE, which involve learned weight matrices or interval geometry, d_simple (Eq. 3) requires no additional parameters beyond the embedding itself, yet the ablation (Appendix E, referenced in Section 5) shows competitive performance. Proofs that d_simple satisfies the triangle inequality and latent positive homogeneity are in Appendix B.

---

## Weaknesses

### Fatal
None.

### Major

- **Missing direct predecessor as a baseline.** Section 6.1 explicitly describes MadDist as "similar to prior work (Steccanella & Jonsson, 2022), but differs in the use of a quasimetric distance function and a scale-invariant loss." The loss in Eq. 2 (their method) is reproduced in detail. Yet Steccanella & Jonsson (2022) is entirely absent from the experimental comparison; the only baselines are QRL (quasimetric + locality constraint) and Hilbert (symmetric). This omission means MadDist's improvements cannot be cleanly attributed: relative to QRL, MadDist differs simultaneously in (a) the quasimetric formulation, (b) the richer supervision signal (all within-trajectory pairs, not just locality), and (c) the scale-invariant loss. Without Steccanella & Jonsson as a baseline, no experiment isolates the contribution of asymmetry from the other two changes. Since the paper's central framing is that quasimetric asymmetry is the key missing ingredient, this is a material evidential gap.

- **No ablation isolating quasimetric contribution from supervision signal.** Closely related to the above: a symmetric-distance version of MadDist (replacing d_simple/d_WN/d_IQE with an L2 norm but keeping the scale-invariant loss and all-pairs supervision) would directly test whether the quasimetric is necessary or whether the richer supervision alone explains MadDist's gains over QRL. Without this, the paper's headline claim—"asymmetric quasimetrics are the key missing ingredient"—rests on a comparison that confounds these factors. Running this ablation in CliffWalking and KeyDoorGridWorld (the two environments with strongest asymmetry) would suffice.

### Minor

- **Seed count inconsistency between Section 7 and Figure 3.** Section 7 states: "All reported results are means over five independent runs (random seeds)." The Figure 3 caption states: "Shaded regions minimum and maximum values across three random seeds." Five versus three seeds is a concrete factual discrepancy in the submitted manuscript. Given that some variance bands are wide (Table 1 shows TDMadDist standard deviations of 0.24–0.30), this inconsistency should be resolved.

- **Figure 3 vs Table 1 reversal for PM Giant Navigate.** Figure 3 shows MadDist (Pearson ~0.9) outperforming TDMadDist in OGBench PM Giant Navigate, but Table 1 shows TDMadDist achieving 0.99 ± 0.05 planning success versus MadDist's 0.93 ± 0.17. This reversal of rankings between the two metrics is substantial enough to warrant explicit discussion—it would illustrate how embedding accuracy and planning success can decouple, and would strengthen the paper's analysis.

- **TDMadDist underperforms but lacks explanatory analysis.** The Discussion (Section 7) acknowledges "TDMadDist underperforms the MadDist and QRL algorithm" without explaining why. If bootstrapping helps in short-trajectory regimes, TDMadDist should outperform on Stitch datasets—Table 1 shows it does not (0.74 ± 0.26 vs. MadDist's 0.99 ± 0.07 on PM Giant Stitch). The paper would be stronger if it either identified TDMadDist's failure regime or, alternatively, framed the TD variant as a partial negative result: TD bootstrapping for direct distance learning does not help in these settings, which is itself informative.

### Trivial

- **d_max hyperparameter in L_r (Eq. 6) is introduced without inline justification.** The paper defers its setting to Appendix D; a brief sentence noting its role and typical range in the main text would improve readability, particularly for environments with very different diameter.

---

## Nice-to-Haves

- In environments with complex non-linear connectivity (e.g., mazes), d_simple's geometric structure (max/avg of relu(x − y)) may force the embedding into distorted shapes. A brief discussion of this limitation, or an empirical check of embedding geometry in a maze environment, would help readers understand where d_simple is most reliable.

- A brief analysis of when MAD (a lower bound in stochastic settings) is a tight vs. loose proxy for task-relevant distances, with guidance on when the approximation matters most in practice, would add value. The conclusion mentions this avenue but without substantive guidance.

---

## Removed Points

*These points are flagged as removed; treat them with caution.*

- **"Claim about quasimetric advantages is unverified due to possible appendix content."** The harsh critic raises the symmetric-MadDist ablation as potentially being in the appendix. The appendix is stripped from this submission, but the ablation in Appendix E explicitly addresses quasimetric choice (d_simple vs. d_WN vs. d_IQE), not symmetric vs. asymmetric. The concern about isolating quasimetric from supervision is retained as a Major weakness, but the speculation that it "might be in the appendix" is removed per hard rules.

- **"Floyd-Warshall discretization introduces ground-truth error that is not separated."** The critic notes that PointMaze ground truth is approximated via Floyd-Warshall over a discretized maze graph. While strictly true, this is standard practice in continuous maze evaluation and does not meaningfully alter the comparative conclusions. The paper is transparent about this approximation in Section 7. Removed as a minor nitpick that does not affect relative comparisons.

- **Strength: "TDMadDist introduces a new learning paradigm as a standalone contribution."** TDMadDist is presented as a co-equal contribution, but it consistently underperforms MadDist and QRL across almost all environments (acknowledged by the paper itself). It is not a reliable contribution; its value is limited to demonstrating viability in principle. This strength is removed as conflicting with the verified underperformance.

- **Strength: "Comprehensive benchmark enables rigorous evaluation."** This is a genuine strength but retained in the main Strengths above in more specific form; the generic formulation is removed.

---

## Novel Insights

The combination of scale-invariant normalization (Eq. 5) and asymmetric quasimetric supervision is cleaner and more empirically effective than prior methods—but the paper inadvertently surfaces an interesting empirical puzzle: embedding accuracy (Pearson/CV) and planning success rate are not monotonically coupled. TDMadDist achieves higher planning success than MadDist on PM Giant Navigate (0.99 vs. 0.93) despite worse embedding correlation, while MadDist dominates on Stitch variants. This decoupling suggests that the right distance for planning may prioritize different geometric properties than aggregate Pearson correlation, and that the choice of evaluation metric for MAD approximation deserves its own investigation.

---

## Suggestions

1. Add Steccanella & Jonsson (2022) as a baseline in at least two environments (e.g., CliffWalking and one OGBench PointMaze). Their loss (Eq. 2) is already in the paper; running their method requires only replacing the MadDist loss with Eq. 2 and keeping the symmetric metric. This directly isolates scale invariance and quasimetric contributions.

2. Add a single symmetric-MadDist ablation run: use the full MadDist pipeline with L2 norm instead of d_simple, in CliffWalking and KeyDoorGridWorld. This cleanly demonstrates the quasimetric contribution independently of the supervision signal difference.

3. Resolve the seed count inconsistency (3 seeds in Figure 3 caption vs. 5 seeds in Section 7) and verify Table 1 statistics match Figure 3 curves for PM Giant Navigate.

4. Add an explicit discussion paragraph in Section 7 (Discussion) addressing the Figure 3 vs. Table 1 reversal for PM Giant Navigate.

---

## Evaluation on Core Axes

- **Originality:** Moderate-to-good. Scale-invariant loss and d_simple quasimetric are novel; the benchmark suite is a concrete new contribution. The TD variant adds limited novelty given its underperformance.
- **Importance of research question:** Strong. MAD approximation is directly useful for GCRL, reward shaping, and option discovery; asymmetry in environment dynamics is a real, underaddressed issue.
- **Claims are well-supported:** Partially. MadDist's strong performance is empirically solid. However, the attribution of improvements to the quasimetric (vs. richer supervision or scale-invariant loss) is not directly tested.
- **Soundness of experiments:** Good for MadDist; the benchmark design is principled. TDMadDist analysis is incomplete. The seed inconsistency is a factual error.
- **Clarity of writing:** Good overall; formalism is clean, environments are well-described, discussion is honest about limitations.
- **Value to research community:** High for the benchmark suite; moderate for the algorithms given the evidential gaps.

---

## Score Calibration Summary

**Round 1 anchors:** Weak band (avg ~3.0): bisimulation / successor feature papers — clearly below this paper's contribution level. Middle band (avg 4.75–6.5): State Chrono Representation (4.75, reject), Distributional Distance Classifiers (6.0, reject), ETD (6.75, accept), OGBench (7.0, accept). Strong band (avg 8.0): topically unrelated papers.

**Round 1 bracket: 5.0 – 7.0.**

**Round 2 anchors:** Narrowing within bracket — ETD (6.75, accept): uses temporal distance + quasimetric for exploration; solid method, tested on standard benchmarks, minor weaknesses around discrete-only evaluation. OGBench (7.0, accept): benchmark paper with 85 datasets and 6 algorithm implementations, broader scope, accepted with minor concerns.

**Comparison:**
- vs. ETD (6.75): The paper under review is of similar methodological quality. However, ETD has a cleaner ablation/evaluation story (no missing predecessor baseline) and a full experimental suite. The paper under review is weakened by the missing Steccanella & Jonsson baseline and the confounded comparisons. *Slightly weaker than ETD.*
- vs. OGBench (7.0): The benchmark contribution here is smaller (fewer environments, fewer algorithms), but the algorithmic contribution is more original. Still weaker overall. *Below 7.0.*
- vs. State Chrono (4.75): Clearly stronger—better theoretical grounding, cleaner experiments, more relevant benchmarks.
- vs. Distributional Distance (6.0): Comparable or slightly above. That paper also has missing baseline concerns and mixed reviewer signals (scores 6,8,5,3,8).

**Final position:** The paper falls between 5.5 and 6.5. The evidential gaps (missing baseline, missing ablation) are genuine Major concerns, but they are fixable in a rebuttal and do not invalidate the core results. The contribution of the benchmark and MadDist algorithm is real and useful. Placing at **6.0**—above the 4.75–5.0 rejects, below the cleaner 6.75–7.0 accepts, reflecting a paper that is interesting and likely correct but not yet fully convincing on its central attribution claim.

| Paper | Path | Avg Score | Round | Comparison |
|---|---|---|---|---|
| Adiabatic RL | Q1Hr9dVfDS.md | 3.0 | R1 | Much weaker — vague contributions, multiple major issues |
| State Chrono Repr. | oEzY6fRUMH.md | 4.75 | R1/R2 | Weaker — ad-hoc losses, limited evaluation |
| Weak Bisimulation | x7Q0uFTH2a.md | 3.75 | R1 | Weaker — limited novelty |
| STARC | wPhbtwlCDa.md | 6.5 | R1 | Comparable — theoretical framing, solid experiments |
| Distributional Distance | qofh48zW3T.md | 6.0 | R1 | Comparable — similar evidential gaps, same domain |
| ETD | I7DeajDEx7.md | 6.75 | R2 | Slightly stronger — cleaner story, no missing baseline |
| OGBench | M992mjgKzI.md | 7.0 | R2 | Stronger — much larger benchmark scope, better-supported claims |

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>