Now I have a thorough understanding of the paper and all the reviewer claims. Let me construct the final review.

---

## Summary

This paper proposes CDiffuser, an offline RL method that integrates contrastive learning with diffusion-based trajectory planning. The core idea is to treat high-return states from the offline dataset as positive samples and low-return states as negative samples, then introduce a contrastive loss that pulls the generated trajectory's states toward high-return states and pushes them away from low-return states. The method is evaluated on 14 D4RL tasks and compared against CQL, IQL, DT, TT, MOPO, Diffuser, and Decision Diffuser. The central claim is that CDiffuser makes effective use of abundant low-return trajectories to improve performance, particularly when high-return data is scarce.

## Strengths

- **Consistent gains on challenging datasets empirically verified.** Table 1 shows CDiffuser (best variant) outperforms both Diffuser and Decision Diffuser on 6 of 9 locomotion tasks by non-trivial margins. The gains are especially pronounced on datasets with many low-return trajectories (e.g., +18.0 over DD on Hopper-Medium, +9.2 over DD on Walker2d-Med-Replay).

- **Controlled ablation isolates the role of low-return negatives.** The ablation (Figure 3) compares CDiffuser, CDiffuser-C (no contrastive loss), and CDiffuser-N (trained on high-return samples only). CDiffuser outperforms both variants on all 9 tasks, and CDiffuser-N is *worse* than CDiffuser-C on 4 tasks — directly proving that the benefit comes from incorporating low-return negatives, not merely from having more data.

- **Mixed-dataset study directly validates the core motivation.** In Table 2, CDiffuser's advantage over the best baseline grows as data quality drops. On Rand-Exp with ratio 0.1, CDiffuser-SRD scores 48.0 vs Diffuser 33.8 (+14.2); on ratio 0.3, 88.7 vs 75.8 (+12.9). This directly confirms the paper's thesis: the method is most helpful precisely when high-return trajectories are scarce.

- **Reward distribution analysis provides causal evidence for the contrastive mechanism.** By removing the return predictor from both CDiffuser and CDiffuser-C (Figure 5), the paper shows that CDiffuser generates trajectories with higher probability density on high rewards. This isolates the effect of the contrastive loss from the return predictor, providing direct evidence that the contrastive mechanism shifts generation toward higher returns.

- **Portability tested on two base planners.** Table 3 shows the contrastive mechanism improves both Diffuser (all 3 tasks) and Decision Diffuser (2 of 3 tasks) when transplanted, supporting generality beyond the authors' specific architecture.

## Weaknesses

### Fatal
None.

### Major

- **Baseline comparison in Table 1 is not apples-to-apples.** The primary results table reports CQL, IQL, DT, TT, and MOPO as single numbers with no standard deviations, while Diffuser, DD, and CDiffuser include standard deviations. The paper states "We conducted 10 trials with different seeds" (line 270) but does not clarify whether this applies to all methods or only CDiffuser; the table caption says "computed over 50 random seeds" but the non-diffusion baselines lack variance estimates. In contrast, Table 2 explicitly reports "50 random seeds for CDiffuser, and 10 random seeds for baselines" with error bars for all methods. The discrepancy suggests the non-diffusion baseline scores in Table 1 may have been taken from prior publications rather than re-run under the same evaluation protocol. This makes it difficult to assess the statistical significance of CDiffuser's reported advantages over those baselines. **Why it matters**: The paper's claim of "best or second-best on 6 of 9 locomotion tasks" relies on comparisons against methods whose evaluation conditions may differ in seed count, evaluation horizon, or return normalization.

### Minor

- **Contrastive loss variant is insufficiently justified and not ablated.** Equation (9) removes the positive term from the standard InfoNCE denominator and sums over multiple positives in the numerator simultaneously. The paper offers only the brief statement "we made these modifications primarily for the sake of the model's effectiveness" (line 207) with no ablation comparing this variant against standard InfoNCE, a triplet loss, or other alternatives. The unusual formulation could produce a negative loss (if positive similarities dominate) or numerical instability (if the denominator shrinks); neither possibility is discussed. **Why it matters**: The contrastive loss is the paper's core technical contribution; its design choices should be empirically justified.

- **Critical hyperparameters are not reported in the paper.** The values of the contrastive temperature $T$, the number of positive/negative samples $\kappa$, the soft-threshold parameters $\xi$ and $\zeta$ (Eqs. 5–6), the loss weights $\lambda_d$, $\lambda_v$, $\lambda_c$, and the guidance scale $\rho$ (Eq. 3) are all absent. The paper states code is publicly available, but for a standalone submission this lack of transparency hinders reproducibility and makes it impossible for readers to assess the method's sensitivity to these choices. **Why it matters**: A multi-objective loss with several interacting hyperparameters requires documented values or a sensitivity analysis.

- **Ablation results (Figure 3) are shown without error bars.** The bar chart compares CDiffuser, CDiffuser-C, and CDiffuser-N across 9 tasks without any indication of variance. Given that Table 1 reports standard deviations for the full CDiffuser method, the lack of error bars in the ablation undermines the statistical support for the ablation claims. **Why it matters**: The paper claims "CDiffuser-C exhibits poorer performance across all nine tasks" and "CDiffuser-N achieves lower performance than CDiffuser in all 9 tasks" — these absolute statements would be strengthened by evidence that the differences are statistically significant.

- **SRD sampling strategy lacks implementation details.** The dynamic consistency component uses MiniBatch K-Means clustering and transition probabilities among clusters, but the paper specifies neither the number of clusters used nor how transition probabilities are computed from cluster memberships. **Why it matters**: The SRD variant underperforms SR on many tasks; without full specification, readers cannot reproduce or understand when one strategy should be preferred.

- **Compatibility study is limited in scope.** Table 3 tests only 3 Med-Expert tasks. The improvement for DD$^+$ is 0 on HalfCheetah (with a post-hoc explanation about DD's separate state-action modeling), and the study does not test the method on more challenging data compositions (e.g., Med-Replay or mixed datasets). **Why it matters**: The portability claim would be stronger with a broader evaluation.

### Trivial

- **Inconsistent seed counts.** Line 270 says "10 trials with different seeds" while the Table 1 caption says "computed over 50 random seeds." The Table 2 caption says "50 random seeds for CDiffuser, and 10 random seeds for baselines." The discrepancy between 10 and 50 deserves clarification.
- **Loss weight λ_c is mentioned but λ_v λ_d λ_c are never given concrete values nor ablated** (this overlaps with the hyperparameter point above but is narrower — even a brief sensitivity study on λ_c would address it).

## Nice-to-Haves

- **Error bars on the ablation bar charts** (Figure 3) — essential for statistical rigor.
- **A comparison of the proposed contrastive loss vs. standard InfoNCE** on at least one task to validate the design choice.
- **Discussion of computational cost** — the contrastive module (projection network, sampling, K-Means) adds overhead relative to Diffuser.
- **A dedicated limitations paragraph** discussing when the method might fail (e.g., datasets where low-return states are not informative because the dataset is too homogeneous, or environments where state-based contrast is less meaningful).
- **Statistical significance tests** (e.g., paired tests between CDiffuser and Diffuser/DD on key tasks).

## Removed Points

- **"First" claim about contrastive learning in policy learning**: The harsh critic says this is overstated because CURL and Contrastive RL also apply contrastive learning to RL. However, the paper's own related work section (line 477–482) clearly distinguishes CDiffuser by noting that prior methods "apply contrastive learning to enhance the state representations" while CDiffuser "adopts contrastive learning to constrain the generated sample, rather than learning representations." The claim is scoped specifically to this different usage. Removed as already addressed in the paper.

- **UMAP visualization is "misleading" or "qualitative"**: The harsh critic says Figure 4 (UMAP) "can be misleading." UMAP visualizations are a standard qualitative tool in RL papers and are supplemented here by the quantitative reward distribution analysis (Figure 5). This is a style nitpick. Removed.

- **Missing appendix or proofs**: Removed per instructions (parser strips appendix content; it exists in the original submission).

- **Missing related works**: Removed per instructions (no external sources to verify completeness).

- **Formatting/style nitpicks**: Removed per instructions.

- **Claim that baseline numbers "appear to be taken from D4RL leaderboards"**: While the lack of std devs in Table 1 is a genuine concern about experimental rigor (retained as a Major weakness), the critic's phrasing that they "appear to be taken from D4RL leaderboards rather than being reproduced" is speculative. The core issue — asymmetric reporting — is retained; the speculation about source is dropped.

## Novel Insights

**None beyond the paper's own contributions.** The reviews surface a clear tension between the paper's conceptual appeal (using low-return trajectories as contrastive negatives is a natural idea that the community has not explored in this form) and its experimental reporting gaps (asymmetric baseline comparison, missing hyperparameters). Neither reviewer identifies an unexpected failure mode or a fundamentally new application of contrastive learning outside what the paper claims. The most useful insight contributed by the meta-review process is that the strongest evidence for the method is not Table 1 (where baseline comparisons are unfair) but Table 2 (the mixed-dataset study, which is fairly reported with error bars for all methods) and the ablation study (which cleanly separates the effect of low-return negatives from mere data quantity). The paper would benefit from centering its narrative on these experiments rather than Table 1.

## Suggestions

1. **Re-run all baselines in Table 1 under a common protocol** with matched seeds, evaluation horizons, and return normalization. Report standard deviations for every method. This is the single change that would most strengthen the paper.
2. **Report all hyperparameter values** in a table (T, κ, ξ, ζ, λ_d, λ_v, λ_c, ρ, number of K-Means clusters).
3. **Add an ablation comparing the proposed contrastive loss against standard InfoNCE** on at least one medium-difficulty task (e.g., Hopper-Medium).
4. **Add error bars to the ablation bar chart** (Figure 3) using the same evaluation protocol as the main table.
5. **Expand the compatibility study** to include at least one Med-Replay or mixed-dataset task to test portability under data-scarce conditions.
6. **Add a brief sensitivity analysis** for λ_c and κ to show the method is not brittle to these choices.
7. **Clarify the seed count**: resolve the "10 trials" vs "50 random seeds" inconsistency.

## Score and Decision

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>