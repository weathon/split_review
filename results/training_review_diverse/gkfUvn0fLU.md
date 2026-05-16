Now I have a thorough understanding of the paper and can verify the reviewer's claims. Let me write the consolidated review.

## Summary

This paper studies reward model overoptimization in the context of composite reward functions (combinations of multiple RMs). The authors first analyze how correlation between component RMs shifts the "proxy points" (values beyond which further optimization degrades ground-truth performance). They then propose reformulating RLHF as a constrained MDP, using these proxy points as thresholds with Lagrange multipliers as learned dynamic weights, preventing overoptimization. They introduce several constrained variants (μ-PPO, ξ-PPO, All-PPO) and a practical single-run variant (NM-PPO) using Nelder-Mead optimization to identify thresholds during training. Results on DailyDialog with GPT-2 show that the constrained methods (particularly ξ-PPO) achieve better and more stable evaluation performance than standard PPO with fixed weights.

## Strengths

1. **Novel formulation of composite RM overoptimization as a constrained RL problem.** The paper identifies a real problem—weighting and overoptimization in composite RMs—and recasts it as a CMDP with proxy points as thresholds and Lagrange multipliers as learned weights. This is a well-motivated and principled approach that goes beyond fixed-weight linear combinations.

2. **Clear empirical evidence that constrained methods outperform standard PPO.** Figure 3 shows that μ-PPO and ξ-PPO achieve substantially higher evaluation scores than standard PPO with optimized fixed weights, and that ξ-PPO remains stable when training is extended 3× while PPO degrades. These results are supported by 5 seeds and demonstrate the practical benefit of the approach.

3. **NM-PPO reduces computational cost.** The Nelder-Mead variant identifies proxy points during a single run, saving the multiple runs needed by competing methods. The simplex trajectories converge to local maxima of the evaluation surface (Figure 6), validating the gradient-free approach. This is a practical contribution for scaling to larger models.

4. **Proxy-point thresholds are validated.** The paper shows (Figure 5) that using the estimated proxy points as thresholds outperforms both 10%-higher and 10%-lower thresholds, and that accounting for RM correlation when setting thresholds outperforms using independently estimated proxy points. This strengthens the core claim that the identified thresholds are meaningful.

5. **Constraint satisfaction is empirically verified.** Figure 4 confirms that μ-PPO meets or exceeds thresholds, All-PPO stays below them, and ξ-PPO approximately hits them—the constrained algorithms behave as designed.

6. **Practical engineering contributions.** The description of specific modifications (sigmoid/tanh bounding of Lagrange multipliers, low-momentum updates, replacing value estimates with Monte-Carlo returns for constraint violation) provides useful guidance for making primal-dual RL work in practice.

## Weaknesses

### Fatal
None.

### Major

1. **Framing oversells connection to human preferences.** The paper evaluates using the held-out automated metric (METEOR + intent classifier) as ground truth, which is itself a proxy—not human judgments. The abstract and introduction frame the problem in terms of "human preferences" and "human evaluation" (e.g., "reward models fitted to human feedback," "worse human ratings"). However, the experiments demonstrate proxy-to-proxy overoptimization, not necessarily overoptimization with respect to actual humans. The paper acknowledges this (line 71: "in line with prior work that uses held out metrics as the ground truth for convenience of iteration") and discusses it in Section 6, but the central claims in the abstract and introduction do not carry this caveat. This disconnect between framing and evidence weakens the external validity of the claimed contributions. The authors should either (a) include a small-scale human evaluation or (b) substantially temper the language to make clear that this is a study of proxy-to-proxy overoptimization.

2. **Joint proxy point identification is underspecified (reproducibility gap).** The paper states (line 79) that "the maximizing point (θ_intent^★, θ_meteor^★) indeed differs from the proxy points found by only considering one RM at a time" and that this point comes from "a fitted surface." However, the paper never explains: (a) what data were collected to fit this surface (which combinations of reward weights, how many runs), (b) what fitting method was used, or (c) how the maximum is extracted. This is critical because these joint proxy points are used as the thresholds in the main constrained RL experiments (μ-PPO, ξ-PPO, etc.). Without this description, the main results cannot be replicated, and it is unclear whether the thresholds are reliable. The paper should provide a clear description of the procedure, including number of runs, range of weightings, fitting algorithm, and any validation.

### Minor

1. **Correlation claim is weakly supported.** The paper claims that "correlation between component RMs has a significant effect on the locations of these points" (abstract). This is supported by a single comparison (Figure 1): the joint maximum differs from the independent maxima. However, the degree of correlation between METEOR and intent on DailyDialog is not reported, nor are there any controlled experiments varying correlation. This claim is plausible but the evidence is thin. The authors should either report the correlation coefficient or soften the claim.

2. **Missing hyperparameter details.** The paper mentions optimizers and momentum (line 147) but does not provide a comprehensive table of hyperparameters for PPO, the constrained methods, or the Nelder-Mead search. This is needed for reproducibility. (The pseudocode referenced as Algorithm 1 was in the appendix, which was stripped by the parser—this should be ensured in the main text or supplement.)

3. **Constraint satisfaction is reported only qualitatively.** For ξ-PPO, the paper only shows visual plots of constraint values (Figure 4) without reporting numerical constraint satisfaction (e.g., average absolute deviation |v_i − θ_i| at convergence). Quantitative reporting would strengthen the claim that equality constraints are accurately enforced.

4. **No statistical significance for main comparisons.** The main performance comparisons (Figure 3) lack confidence intervals or significance tests. While 5 seeds with standard error are shown, adding bootstrap tests or confidence intervals would strengthen the reliability of the comparisons.

5. **The gradient statement for inequality constraints could be clearer.** The paper states (line 98-101) that the negative gradient with respect to μ is θ_i − v_i^π, which holds for inequality constraints (≥). The equality constraint case (ξ-PPO) uses the same formula but with an unconstrained multiplier (tanh-bounded). A brief explicit distinction would improve clarity.

### Trivial
None.

## Nice-to-Haves

- **Ablate task reward choice.** The paper uses negative KL as the task reward. It would be informative to compare with a variant that uses the composite reward as task reward with equality constraints (like All-PPO but with ξ-formulation). This would isolate whether the benefit comes from the constraint structure or from the KL-centric objective.
- **Small-scale human evaluation** to validate the main results on a subset of generated responses would substantially strengthen the claims about alignment with human preferences.
- **Higher-dimensional extension** (more than 2 component RMs) would test the scalability of the approach.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **"First study" claim is unverifiable / risks being disproven.** The paper's abstract says "to our knowledge, the first study" — this is appropriately qualified. The critic's concern is reasonable but the paper already uses cautious language.
- **wrafig placement / figure labeling issues.** These are formatting artifacts (PDF/parser issues), not author errors.
- **NM-PPO caveat about initial simplex only in caption.** The paper explicitly states this caveat in the main text (line 191: "One caveat with respect to this result is..."). The critic misread this.
- **Missing pseudocode (Algorithm 1).** The paper references Algorithm 1 — this was in the appendix, which is stripped by the parser. The original submission contains it.
- **Demand for human evaluation as a strict requirement.** While a human evaluation would strengthen the paper, demanding it as a condition for acceptance would apply a standard not required of prior work (Gao et al. 2022 also used synthetic gold rewards). The critic's framing of this as a "structural" issue rather than a limitation is overstated. The point has been incorporated into Major weakness #1 above as a framing issue rather than a fatal methodological flaw.

## Novel Insights

Beyond the paper's own contributions, the reviews surface one genuinely useful observation: the tension between the paper's motivational framing (human preferences, alignment) and its experimental setup (automated metrics as ground truth) is not just a minor presentation issue—it reflects a broader question about what constitutes "overoptimization" in RLHF research. If both the proxy RMs and the ground truth are automated metrics, the phenomenon being studied is proxy-to-proxy overoptimization, which may differ substantively from proxy-to-human overoptimization. This is a subtle but important distinction that the paper's own acknowledgment (line 71) does not fully resolve, and it deserves more careful treatment in the framing.

## Suggestions

1. **Describe the joint proxy point pipeline clearly.** Add a dedicated subsection explaining: (a) what data were collected to fit the surface in Figure 1 (range of reward weightings, number of runs), (b) the fitting algorithm used, (c) how the maximum is extracted, and (d) any validation of the fitted surface. This is essential for reproducibility.

2. **Revise the framing.** Replace "human preferences" / "human evaluation" with "ground-truth evaluation metric" or "gold reward" in claims about experimental results. Keep the human-preference motivation in the introduction but make clear that the experiments evaluate proxy-to-proxy overoptimization, consistent with prior work (Gao et al. 2022).

3. **Add a hyperparameter table** covering PPO, the constrained methods, and Nelder-Mead search (learning rates, batch sizes, KL coefficient schedule, multiplier update frequency, etc.).

4. **Report numerical constraint satisfaction** for ξ-PPO (e.g., mean absolute deviation from thresholds at convergence).

5. **Report the empirical correlation** between METEOR and intent scores on DailyDialog to substantiate the correlation claim.

6. **Add confidence intervals or bootstrap tests** for the main evaluation comparisons (Figure 3).

## Score and Decision

The paper addresses an important problem (overoptimization in composite RMs) with a well-motivated method (constrained RL with proxy-point thresholds). The empirical results are promising and the practical improvements (NM-PPO, stability hacks) are useful contributions. However, two significant issues—(1) the framing-experiment disconnect regarding human evaluation and (2) the underspecified joint proxy point identification procedure—need to be resolved. These are fixable in revision and do not invalidate the core contribution.

The paper is original, the research question is important, the experiments are generally sound, and the writing is clear. With the suggested revisions, this would make a solid contribution to the RLHF literature.

MY FINAL SCORE: <pineapple>6.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>