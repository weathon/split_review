Now I have all the information needed. Let me write the final review.

## Summary

This paper proposes two algorithms (MadDist and TDMadDist) for learning the Minimum Action Distance (MAD) — the minimum number of steps needed to transition between states — from state-only trajectories, without requiring actions or rewards. The method uses quasimetric embeddings to capture asymmetric distances and introduces a simple computationally-efficient quasimetric (d_simple). The paper also contributes a benchmark suite of environments with known ground-truth MAD. Empirically, MadDist consistently outperforms QRL and Hilbert baselines on correlation, coefficient of variation, and downstream planning metrics across grid worlds and continuous mazes.

## Strengths

1. **State-only self-supervised learning of MAD from trajectories.** The paper proposes a principled framework for learning the Minimum Action Distance from state trajectories without requiring action labels or reward signals (Section 6, Figure 1). This is a genuinely useful capability for many RL settings where actions may not be logged but state sequences are available.

2. **Simple yet effective quasimetric (d_simple).** The rectified-linear-unit-based quasimetric defined in Equation (3) is computationally efficient and, as shown in Figure 3, outperforms more elaborate quasimetrics like IQE used in QRL. In KeyDoorGridWorld and OGBench PM Giant Navigate, MadDist achieves higher correlation and lower CV than QRL, demonstrating the practical value of this simple design.

3. **Diverse benchmark suite with known ground-truth MAD.** The paper introduces environments (NoisyGridWorld, KeyDoorGridWorld, CliffWalking, PointMaze variants, OGBench mazes) where the true MAD is known, enabling rigorous controlled evaluation (Section 7, Figure 2). This is a valuable community contribution for standardized evaluation of distance-learning methods.

4. **Strong handling of asymmetric distances.** Unlike the symmetric Hilbert baseline, MadDist and TDMadDist capture asymmetry in environments with irreversible dynamics (CliffWalking, KeyDoorGridWorld). In these environments, MadDist achieves substantially higher correlation and lower CV than the Hilbert baseline (Figure 3).

5. **Strong downstream planning performance.** Table 1 shows MadDist achieves 0.93–1.00 success rates across six OGBench PointMaze environments, decisively outperforming QRL (0.81–0.97) and Hilbert (0.05–0.67). This demonstrates practical utility beyond correlation metrics.

## Weaknesses

### Major

1. **Tension between the loss function and the stated target.** The paper claims to learn the *minimum* action distance, yet the main loss term (Equation 5) regresses the embedding distance to the trajectory step count *j−i*, which is only an *upper bound* on MAD. The paper states this explicitly at line 80: "Given a trajectory... it is easy to see that *j−i* is an upper bound on d_MAD(s_i, s_j)." While the composite loss includes a constraint loss L_c (Equation 7) that enforces the upper bound and a contrastive loss L_r (Equation 6) that prevents collapse, the paper does not explain how regressing toward upper bounds can recover a minimum, nor does it provide any theoretical or empirical analysis of when or why this works. For trajectories collected by a random policy (used in all experiments), the gap between trajectory distance and true MAD can be arbitrarily large (e.g., in a line world, random walks take O(L²) steps vs. L steps optimal). This gap is not analyzed and directly affects the core claim. **Why it matters:** This is the main methodological gap — the learning objective is not obviously aligned with the quantity the paper claims to learn. The paper would be significantly strengthened by analyzing this alignment (e.g., explaining how the triangle inequality and constraint losses propagate tighter bounds, or providing toy experiments showing that the learned distance converges toward the minimum rather than the trajectory distance).

2. **No absolute accuracy metrics for MAD recovery.** The evaluation uses Spearman/Pearson correlation and ratio CV, which measure ordering and scaling consistency but not absolute accuracy. These metrics could be high even if the learned distances are systematically overestimated by a constant factor (the paper's own metric definition acknowledges this: "if we consistently predict distances that are approximately 1.5 times the true distance, CV will be low"). The paper asserts "accurate MAD representations" but provides no scatter plots, no mean absolute error, no predicted vs. true MAD comparison. **Why it matters:** Without absolute accuracy metrics, the reader cannot assess whether the method actually recovers MAD or merely a monotonically-related proxy. The downstream planning results (Table 1) show utility but do not validate the specific claim of recovering MAD values.

### Minor

3. **Inconsistent statistical reporting.** The paper states in Section 7 ("Empirical Setup") that "All reported results are means over five independent runs (random seeds)," but Figure 3 caption says "Shaded regions indicate minimum and maximum values across three random seeds." The main text states five seeds; the figure caption states three. This inconsistency should be resolved.

4. **TDMadDist underperformance is not analyzed.** TDMadDist consistently underperforms MadDist and sometimes QRL (Figure 3). The paper notes this but offers no analysis of *why* the TD variant fails to match the direct regression variant. This omission weakens the claim that TDMadDist is a principled alternative.

5. **Which quasimetric is used for main results is not specified in the main text.** Section 5 defines three quasimetrics (d_simple, Wide Norm, IQE), and Section 6 states that the algorithms "support any quasimetric formulation." However, neither the main experiments description nor Figure 3/Table 1 specify which quasimetric was used for the reported MadDist/TDMadDist results. Appendix E contains an ablation, but the main text is ambiguous. This should be stated explicitly.

### Trivial

6. **Hyperparameter sensitivity not discussed.** The composite loss (Equations 4–7) involves hyperparameters w_r, w_c, d_max, H_c, with no discussion of how they are set or how sensitive results are to their choice.

## Nice-to-Haves

- Including absolute accuracy metrics (scatter plots, MAE between predicted and true MAD) would directly address the most important evidential gap.
- A toy experiment where the mismatch between trajectory distance and MAD is controlled (e.g., varying policy suboptimality) would clarify how the loss handles the upper-bound-to-minimum conversion.
- An ablation replacing the quasimetric with an L2 norm in MadDist would isolate the benefit of asymmetry.
- Hyperparameter sensitivity analysis for d_max and H_c.

## Removed Points

- **"The learning objective is not aligned with the claimed quantity (fatal)"** — Downgraded to Major. The paper explicitly acknowledges that j-i is an upper bound (line 80) and includes constraint loss L_c (Equation 7) and contrastive loss L_r (Equation 6) that partially address the mismatch. The concern is real but the paper's composite loss does implement inequality constraints and anti-collapse mechanisms; the issue is insufficient analysis, not a fatal structural flaw.
- **"Correlation evidence does not establish MAD"** — Merged into Weakness 2 (no absolute accuracy metrics). The core observation is valid but amplified: correlation and CV do measure how well the learned distance approximates MAD up to monotone transformation, which *is* meaningful evidence for recovering a metric.
- **"Dataset size varies without explanation"** — The paper explains this: 100 for grid worlds, 1000 for mazes. Removed as the explanation exists.
- **"Missing confidence intervals"** — The paper reports means over 5 seeds and min/max over 3 seeds (see Weakness 3 about the inconsistency). The concern about statistical rigor is noted but standard for this type of paper.
- **"Behavior policy analysis"** — Nice-to-have, not a core flaw.

## Novel Insights

The harsh critic's observation about the loss-mismatch is genuinely insightful when connected to the paper's empirical success: the fact that MadDist *does* recover accurate MAD values despite regressing toward upper bounds suggests that the combination of the constraint loss (preventing overestimation), the contrastive loss (preventing collapse), and the triangle inequality of the quasimetric (propagating local constraints globally) collectively creates an effective lower-bound-seeking mechanism. This emergent behavior is itself a noteworthy finding that the paper does not analyze. The paper's results implicitly demonstrate that local upper-bound constraints, when combined with transitivity, can recover global minimum distances — but this insight is left implicit.

## Suggestions

1. Provide scatter plots or mean absolute error between predicted and true MAD values to support the claim that the method recovers MAD itself, not just a monotonic proxy.
2. Add a controlled experiment varying behavior policy quality (random → near-optimal) to show how the gap between trajectory distance and MAD affects learned distance quality.
3. Specify which quasimetric is used for main results in the main text, not just in the appendix.
4. Resolve the inconsistency between "5 seeds" (text) and "3 seeds" (Figure 3 caption).
5. Add a brief analysis of why TDMadDist underperforms — even a single ablation experiment varying the EMA rate β would help.
6. Discuss the role of the contrastive loss (L_r) and constraint loss (L_c) in pushing the predicted distance toward the minimum rather than the trajectory distance.

## Score and Decision

**Bracket (Round 1):** The weak anchors (avg 2.50–3.33) are clearly below this paper. The strong anchors (avg 8.00) are clearly above. The paper sits in the middle band (3.5–7.5).

**Narrowing (Round 2):** Compared to *Physics-informed TD Metric Learning for Robot Motion Planning* (TOiageVNru, avg 6.00, accepted): that paper has a cleaner methodological story but similar reviewer polarization. Compared to *Episodic Novelty Through Temporal Distance* (I7DeajDEx7, avg 6.75, accepted): our paper has a more novel core formulation but less polished presentation and a more consequential unresolved issue. Compared to *Bisimulation Metric for MPC* (F07ic7huE3, avg 5.50, accepted): similar level — genuine contribution with incremental concerns. Compared to *Distributional Distance Classifiers* (qofh48zW3T, avg 6.00, rejected): our paper has stronger empirical evidence, but that paper also had the loss-target alignment issue flagged as a concern.

**Final:** The paper makes a genuine contribution with clear empirical value and a well-designed benchmark suite. The main weakness — the gap between the loss function and the claimed target — is real but not fatal because the composite loss structure (constraint loss + contrastive loss + triangle inequality) provides mechanisms that plausibly explain the good empirical results. However, the paper does not analyze this mechanism, leaving a significant gap in the narrative. The paper is slightly weaker than the strongest middle-band anchors (6.00–6.75) due to this unresolved tension and the lack of absolute accuracy metrics, but stronger than the 4.75–5.50 band.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Accept</decision>