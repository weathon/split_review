Now I have all the information I need. Let me synthesize the final authoritative review.

## Summary

This paper studies reward model overoptimization in the context of composite (multi-component) reward functions for RLHF, identifying that correlation between component RMs shifts the "proxy points" beyond which further optimization degrades true performance. The authors propose constrained RLHF methods (μ-PPO, ξ-PPO) that use these proxy points as per-RM constraint thresholds with learned Lagrange multipliers to dynamically weight components. They also introduce NM-PPO, which uses Nelder-Mead optimization to identify proxy points within a single training run. Experiments on DailyDialog with GPT-2 using METEOR and intent RMs show that the constrained methods improve evaluation performance relative to standard PPO.

## Strengths

- **First study of overoptimization in composite reward models, showing correlation effects on proxy points.** The paper empirically demonstrates that the joint optimum of two RMs differs from their independent proxy points (Section 3, Figure 2), establishing a concrete motivation for why composite-RM overoptimization is a distinct problem requiring new approaches.

- **Constrained RLHF methods (μ-PPO and ξ-PPO) achieve better evaluation performance than standard PPO and PPO-SAT baselines.** The paper provides direct evidence in Section 5 (Figure 3/Fig:eval_all) that these methods yield higher evaluation scores over training. The paper additionally shows that the constrained approach is more robust to extended training duration (Figure 3 right panel), a practical benefit.

- **Constraints are empirically satisfied as designed.** Section 5 (Figure 4/Fig:constraint_satisfaction) verifies that μ-PPO reaches or exceeds thresholds, All-PPO stays below them, and ξ-PPO approximately hits them, confirming the Lagrangian mechanism operates as intended.

- **Ablation confirms proxy point thresholds are empirically optimal.** The paper compares ξ-PPO with thresholds 10% higher/lower and with independent (uncorrelated) proxy points, showing the correlated proxy-point thresholds yield the best performance (Figure 5/Fig:proxy-pt_performance).

- **The idea of using constrained optimization to bound individual RM contributions is principled and well-motivated.** The paper provides clear theoretical background (CMDPs, Lagrangian relaxation) and connects the problem—overoptimization of composite RMs—to the proposed solution (per-RM constraints with learned multipliers) in a coherent way.

## Weaknesses

### Fatal
None.

### Major

- **The evaluation metric (the "evaluation score" / "ground-truth" metric used to determine proxy points and evaluate methods) is never explicitly defined.** Section 3 states "Our choice is in line with prior work that uses held out metrics as the ground truth for convenience of iteration" citing Gao et al. 2022, but never specifies *what* this metric actually is — whether it is a held-out gold-standard RM, human ratings, another automated metric, or a composite thereof. All quantitative claims (Figures 2–6) depend on this undefined quantity. Without knowing what is being measured, readers cannot assess the validity, significance, or reproducibility of the reported results. This is a serious expositional gap.

- **A natural baseline is missing: early stopping on the 10-run PPO grid.** The paper uses 10 initial PPO runs to select fixed RM weights for the PPO baseline, and separately uses 10 runs to identify proxy points for the constrained methods. However, the paper does not compare against a baseline that simply trains 10 PPO runs with different weight combos and picks the *best checkpoint* (by evaluation score) directly. This baseline would use the same budget of 10 runs and test directly whether dynamic Lagrange multipliers add value over simply picking the best model from a sweep, without the complexity of fitting proxy-point surfaces and running a second constrained training phase. Omitting this comparison weakens the claim that the constrained framework is responsible for the improvement.

### Minor

- **NM-PPO is validated only anecdotally.** The paper presents a single trace of Nelder-Mead (Figure 6) and acknowledges that "the feasible region of threshold pairs is relatively small" and that "there is a moderate chance that the initial simplex already contains at least one threshold pair which produces reasonable performance" — meaning success may be sensitive to initialization luck. The paper does not run multiple independent NM-PPO trials with different random initial simplexes to characterize variance, nor does it report how many Nelder-Mead function evaluations were required. The claim of "significant computation savings" is not supported with distributional evidence.

- **The empirical study of correlation effects is thin.** The paper claims as a contribution "analysis of reward model overoptimization in the context of composite reward functions, showing that the correlation between RMs has a significant influence on proxy points." This is supported by a single figure (Figure 2) comparing joint vs. independent proxy points. The actual correlation between METEOR and intent scores is never reported or systematically varied (e.g., low, medium, high correlation regimes). Without a controlled study, the observation that "the joint optimum differs from independent optima" is a basic consequence of reward interaction rather than a substantive empirical finding.

- **Practical modifications are not ablated.** The paper introduces several "hacks" (sigmoid/tanh bounding of Lagrange multipliers, low-momentum updates, replacing value estimates with reward-to-go for constraint violation) and states they "improved empirical performance" but does not ablate them. The reward-to-go replacement in particular departs from standard CMDP Lagrangian theory and could bias multiplier updates, yet its effect on convergence or final performance is not analyzed.

- **Error bar interpretation.** In Figure 3 (Fig:eval_all), the paper reports standard error over 5 seeds. Without statistical significance tests or effect sizes, the visual separation between methods — which may be modest — is subject to interpretation. The paper would be strengthened by reporting confidence intervals or significance tests.

- **Comparison against adaptive-KL PPO.** The paper's baseline PPO already uses an adaptive KL coefficient (a form of dynamic weighting). The paper could more sharply differentiate its contribution by comparing against alternative dynamic-weighting mechanisms (e.g., uncertainty-weighted scalarization) to show that the specific Lagrangian formulation adds unique value.

### Trivial
- The paper would benefit from showing Lagrange multiplier trajectories over training to illustrate the mechanism in action.
- Example generations comparing PPO vs. ξ-PPO would help illustrate qualitative differences in overoptimization (e.g., verbosity, hallucination).

## Nice-to-Haves
- Systematic variation of RM correlation (synthetic controls) to quantify how proxy points shift across low/medium/high correlation regimes.
- Scaling experiments to larger models (e.g., 7B) with 4+ component RMs.
- Analysis of proxy-point sensitivity to the surface-fitting method (unimodality assumption).
- Bayesian optimization as an alternative to Nelder-Mead for single-run threshold search.

## Removed Points

These points are flagged to be removed, treat them with caution:
- **"Unfair NM-PPO comparison"** (Harsh Critic, Issue 2, first subpoint): The reviewer claimed charging baselines for all hyperparameter runs while charging NM-PPO only 256k steps is "grossly unfair." This misunderstands the paper's claim — NM-PPO *includes* its Nelder-Mead search within those 256k steps. The comparison is exactly what it claims to be: total training steps including all tuning, and NM-PPO's savings come from avoiding separate hyperparameter sweeps.
- **"PPO-SAT and All-PPO not evaluated"** (Harsh Critic, Section 4): The paper explicitly evaluates PPO-SAT as a baseline in Figure 3 and All-PPO in Figure 4 (constraint satisfaction). This claim is factually wrong.
- **"Abstract overpromises about dynamic weighting"** (Harsh Critic, Section-by-Section): The paper's core contribution *is* dynamic weighting via Lagrange multipliers for composite-RM overoptimization — this is not an overpromise.
- **"Missing related works"**: Per instructions, this cannot be confirmed without external sources.
- **Formatting/style nitpicks**: Removed per hard rules.
- **Reproducibility nitpicks about undisclosed hyperparameters**: Removed per hard rules.

## Novel Insights
None beyond the paper's own contributions. The reviews do not surface a perspective that meaningfully reframes or extends what the paper itself presents.

## Suggestions

1. **Explicitly define the evaluation metric.** State what the "evaluation score" / "ground-truth metric" is in Section 3. If it is a held-out gold-standard RM, specify its architecture, training data, and how it differs from the proxy RMs. Without this, the paper's quantitative claims are uninterpretable.

2. **Add an early-stopping baseline.** Run 10 PPO runs with different RM weightings, evaluate all checkpoints on the gold-standard metric, and select the best checkpoint. Compare its performance against μ-PPO and ξ-PPO. This directly tests whether the constrained framework adds value over a simpler model-selection strategy using the same budget.

3. **Run multiple NM-PPO trials.** Report the distribution of final evaluation scores and total steps across ≥10 random initial simplexes. Characterize how often NM-PPO matches or exceeds the baselines' performance, to support the single-run savings claim with statistical evidence.

4. **Ablate the practical modifications.** Compare ξ-PPO with and without the reward-to-go replacement in the Lagrange multiplier gradient, and with and without sigmoid bounding. Report whether constraints are still satisfied and whether evaluation performance changes.

5. **Report or characterize the correlation between METEOR and intent scores**, and if feasible, construct synthetic RM pairs at controlled correlation levels to strengthen the claim about correlation effects on proxy points.

## Score and Decision

The paper addresses a real and underexplored problem with a principled approach, and the idea of using per-RM proxy points as constraint thresholds is creative and well-motivated. However, the experimental validation has several notable gaps. Most critically, the evaluation metric — on which all quantitative claims rest — is never explicitly defined, and a natural baseline (early stopping on the PPO grid) is absent. These issues weaken support for the core claims but do not invalidate the approach's potential. The paper would require substantial clarification and additional experiments to be ready for acceptance.

MY FINAL SCORE: <pineapple>5.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>