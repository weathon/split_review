Now I have all the information I need. Let me synthesize.

---

## Summary

This paper introduces **MoSH**, a framework for multi-objective optimization (MOO) where a decision-maker can specify *soft bounds* (desirable levels) and *hard bounds* (strict thresholds) per objective. The work proposes a two-step pipeline: (1) **MoSH-Dense**, which densely samples the Pareto frontier in the region of interest using Bayesian optimization with random scalarizations applied through soft-hard utility functions, and (2) **MoSH-Sparse**, which sparsifies the dense set via the SATURATE robust submodular optimization algorithm. The paper provides theoretical guarantees for the sparsification step and evaluates on five domains including brachytherapy treatment planning, engineering design, LLM personalization, and neural network model selection.

## Strengths

- **Novel conceptual framework of soft-hard bounds for MOO.** The paper formalizes a previously unmodeled but practically ubiquitous scenario: practitioners have both hard constraints (must-not-violate) and soft preferences (desirable but not required) for each objective. The piecewise-linear soft-hard utility function (HSF) with its four design traits (hard lower bound mapping to −∞, monotonicity, concavity after the soft bound, saturation) operationalizes this intuition cleanly. The brachytherapy example (cover ≥90% tumor, ideally ≥95%; bladder dose <513 cGy, strict <601 cGy) makes the practical need concrete. Evidence: Section 2.2, Equation 1.

- **Two-step pipeline with strong theoretical guarantees for the sparsification step.** The reduction of the sparsification problem to robust submodular optimization (RSOS) and the use of SATURATE (Krause et al., 2008) is principled and comes with a near-optimality guarantee: the returned sparse set achieves at least the optimal worst-case utility ratio within a factor ψ of the target cardinality, with O(|D|² m log(m)) function evaluations. Evidence: Section 4, Lemma 1, Theorem 2 (lines 201–214). This is the paper's cleanest theoretical contribution.

- **Extensive empirical validation across diverse and practical domains.** The method is evaluated on five distinct problems: synthetic Branin-Currin, four-bar truss engineering design, LLM personalization, cervical cancer brachytherapy, and neural network model selection. The brachytherapy experiment uses real patient data and clinical knowledge. The method achieves >99% of maximum desired utility within 5 validation points across settings and >3% higher HSF-defined utility than baselines on the brachytherapy task. Evidence: Section 5, Figures 3–6.

## Weaknesses

### Major

- **Step 1 evaluation uses only task-specific metrics that inherently favor MoSH, with no standard MOO metrics reported.** All four evaluation criteria for Step 1 (Soft-Hard Fill Distance, Soft-Hard Positive Samples Ratio, Soft-Hard Hypervolume, Soft Region Distance-Weighted Score) are defined with respect to the soft and hard bounds — the very construct that only MoSH leverages. The paper acknowledges that "EHVI, although superior in some metrics" (line 290) but never names which metrics, quantifies the gap, or reports standard hypervolume or Pareto-front approximation quality. This makes the claim of "generally matching or surpassing other baselines in all four metrics" difficult to interpret as evidence of superior optimization. A fairer evaluation would include standard hypervolume (with the hard bound as reference) to show that MoSH does not sacrifice overall PF coverage while focusing on the preferred region.

- **The robustness claim of Step 2 (maximin over λ) is not directly tested.** The paper formulates a maximin problem (Eq. 3, line 196) — maximize the minimum utility ratio over λ ∈ Λ — and uses SATURATE specifically to address the worst-case λ. Yet the evaluation (Section 5.2.2, lines 284–285) tests performance against *a single simulated λ** drawn from a distribution centered at the soft bounds. The end-to-end bar plot and the sparsification curves (Figure 6) also use this single λ*. This does not validate the *robustness* claim: the worst-case utility ratio over a diverse set of λ values (including ones far from the soft region, e.g., uniform over the simplex) is never reported. The whole motivation for SATURATE over greedy is robustness to the worst case, but this is never empirically tested.

### Minor

- **Theorem 1 (Step 1 convergence) is incomplete as a guarantee.** The theorem states that expected Bayes SHF regret ≤ (1/T) expected cumulative SHF regret + o(1), and concludes that the utility ratio converges to 1 as T→∞. However, no bound on the cumulative SHF regret is provided; the theorem only relates the two quantities. Convergence requires that cumulative regret be sublinear in T (O(√T) or O(log T)), which is neither proven nor referenced from Paria et al. (2020) beyond a mention that "our approach follows similarly." The paper overstates this as "formal guarantees on our proposed dense Pareto frontier sampling algorithm" (line 157). Scaling back the claim to note that convergence follows from standard GP-UCB analysis (with appropriate references) would be more accurate.

- **The LLM personalization experiment lacks specification of evaluation metrics.** The paper describes the proxy-tuning setup (lines 314–315) but does not state how "conciseness" and "informativeness" are quantitatively measured (e.g., output length, ROUGE-L, human ratings). Without this, the experiment is not reproducible.

- **The simulated λ* used for evaluation is drawn from a distribution centered at the soft bounds, weakening the ">99% utility" claim.** The maximum desired utility is computed using a precomputed dense set D, not the true PF. The claim that the DM can reach >99% of maximum desired utility within 5 points should be caveated as being with respect to the dense approximation and a specific λ* distribution, which is a fairly forgiving evaluation.

### Trivial

- The paper says it "proves that (2) obtains the optimal compact Pareto-optimal set of points from (1)" (abstract), but Theorem 2 guarantees near-optimality within a multiplicative factor ψ of k, not optimality. This is a minor wording overclaim.

- Figure caption for the end-to-end bar plot (Figure 6) lacks a legend or description of bar coloring; the text says "only the dense set changes" but this is ambiguous without knowing which baselines correspond to which bars.

## Nice-to-Haves

- An ablation study of the HSF parameters (β, ζ) on a synthetic problem would help users understand sensitivity. The paper states that other functional classes with the four traits suffice but tests only one configuration.
- Reporting standard hypervolume alongside the soft-hard metrics would allow readers to judge the Pareto-front quality trade-off.
- Evaluating Step 2 against a held-out set of λ values (including uniform over the simplex) would directly validate the robustness claim.
- A brief discussion of why constrained Bayesian optimization (e.g., treating hard bounds as constraints with penalty methods) was not used as a baseline would clarify the positioning.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **Criticism that prior MOO methods "lack the same capabilities" is overbroad (from Section-by-Section Notes).** This is a subjective positioning judgment. The paper does cite relevant works (Paria et al., Malkomes et al.) and makes a defensible claim. Not removed entirely but downgraded to a Nice-to-Have.
- **Criticism about missing related work comparisons (goal programming, desirability functions, constrained BO).** Per instructions, missing related works are not to be mentioned.
- **Notation/merging of cases in Eq. 1 (Section-by-Section style note).** This is a presentation preference, not a weakness.
- **The function is not Lipschitz continuous at α_H.** This is by design (hard constraint maps to −∞); the critic acknowledges the acquisition function will avoid this region. Purely a design observation.
- **Denominator requires unknown true maximum over PF.** The paper uses the dense set D as the approximation (line 285). This is standard practice and acknowledged implicitly.

## Novel Insights

Beyond the paper's own narrative, the reviews reveal that the paper's most novel and solid contribution is the *combination* of soft-hard preferences with a two-step pipeline that cleanly separates exploration (Bayesian optimization for dense coverage of the preferred region) from exploitation-for-presentation (submodular sparsification). The SATURATE-based sparsification with the HSF utility ratio as the submodular objective is theoretically principled and practically useful. However, the paper's evaluation strategy creates an asymmetry that prevents the reader from assessing whether MoSH is truly a better *optimizer* or merely a better *metric-fitter*. The criticism about the untested robustness claim is the most damaging: the paper uses a robust optimization algorithm but does not test it against the very diversity of preferences (λ) that motivates the robustness machinery. This gap means the paper would benefit significantly from a richer evaluation design before its claims can be fully trusted.

## Suggestions

1. **Add standard hypervolume evaluation** (with reference point at the hard bounds, penalizing infeasible points with −∞) for Step 1. Report alongside the soft-hard metrics to allow readers to see the trade-off.
2. **Test Step 2 robustness directly**: sample a diverse held-out set of λ values (e.g., uniform over the simplex) and report the *minimum* utility ratio over this set for each sparsification method. This directly validates the maximin claim.
3. **Scale back the Theorem 1 claim** or provide a proper cumulative regret bound. At minimum, note that convergence follows from standard GP-UCB analysis (Srinivas et al., 2010) under the same conditions and cite the appropriate reference.
4. **Specify the LLM evaluation metrics** (conciseness and informativeness measurements) for reproducibility.

## Score and Decision

The paper makes a genuine conceptual contribution and the two-step pipeline is well-motivated. However, the evaluation has two significant gaps: (1) Step 1 uses only metrics tailored to MoSH without standard comparison, and (2) Step 2 never tests the worst-case robustness claim that motivates SATURATE. These are addressable but weaken the paper in its current form. The paper is borderline — the core ideas are sound but the evidence for the claimed improvements is incomplete.

MY FINAL SCORE: <pineapple>5.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>