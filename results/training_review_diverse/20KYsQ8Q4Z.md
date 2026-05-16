Now I have a thorough understanding of the paper and have verified all the reviewer claims. Let me produce the final consolidated review.

## Summary

This paper introduces Group Testing Bayesian Optimization (GTBO), which adapts noisy adaptive group testing — a methodology originally developed for binary-outcome problems — to identify axis-aligned active dimensions in continuous black-box functions. GTBO first runs a testing phase using a mutual-information-based group selection criterion to identify which dimensions affect the objective, then performs Bayesian optimization on the detected active subspace with informative GP lengthscale priors. The method is evaluated on synthetic benchmarks (Branin2, Levy4, Hartmann6, Griewank8 extended with inactive dimensions) and two real-world benchmarks (124D Mopta08, 180D LassoDNA), showing competitive or superior performance against methods including TuRBO, SAASBO, HeSBO, BAXUS, ALEBO, and CMA-ES.

## Strengths
- **Extension of group testing to continuous black-box functions**: The paper adapts noisy adaptive group testing (previously limited to binary outcomes) to work with real-valued, noise-perturbed function evaluations. This is a non-trivial theoretical contribution that enables group testing for feature selection in Bayesian optimization and potentially other continuous settings. The key innovation is modeling the difference between perturbed and default evaluations as a Gaussian mixture under two concrete assumptions (noise-only vs. signal-present), detailed in Section 3 with Assumptions 1 and 2.
- **Reliable identification of active dimensions**: GTBO correctly identifies all active dimensions across all runs on the synthetic benchmarks, with a false-positive rate of ~0.05% (6 misclassifications out of 1180 inactive dimensions over ten runs), as shown in Figure 2 (labeled fig:synthetic_gt in the paper). The group testing phase converges in 39–112 iterations, which is modest relative to the total budget.
- **Competitive optimization performance**: On both synthetic noisy benchmarks and real-world high-dimensional problems, GTBO frequently outperforms or matches state-of-the-art methods including TuRBO, SAASBO, HeSBO, BAXUS, and CMA-ES. The performance on the 124D Mopta08 benchmark shows a particularly sharp drop right after the group testing phase (Figure 4), directly visualizing the benefit of identifying the active subspace.
- **Interpretability as a by-product**: Unlike many black-box high-dimensional BO methods, GTBO explicitly informs the user which dimensions are active, providing insight into the application — a feature highlighted in the abstract and discussion as valuable for practitioner understanding.
- **Thorough sensitivity analysis**: The paper systematically ablates GTBO's classification accuracy under varying noise levels, total dimensionality, and number of active dimensions (Figure 5/8), honestly documenting the method's robustness and its breakdown point when assumptions are violated.

## Weaknesses

### Fatal
None.

### Major
- **Ad-hoc variance estimation with limited justification**: The noise variance σ²_n and function-value variance σ² are estimated by splitting dimensions into roughly √D bins, computing differences from a default configuration, and taking the √D largest differences as signal and the rest as noise (Section 3, end of first paragraph after Assumptions 1–2). This procedure assumes at most √D active dimensions — a heuristic that is itself an input to the method. If the true number of active dimensions exceeds √D, the noise estimate is contaminated by signal differences; if far fewer, the signal estimate is noisy. The sensitivity analysis confirms that with 32 active dimensions out of 100 (√100=10), the method breaks down. The paper does not offer a principled alternative (e.g., joint Bayesian estimation of variances with activeness probabilities) or analyze how performance degrades under intermediate violations of this assumption. While the paper acknowledges the assumption, the centrality of these variance estimates to the group-testing likelihood makes this a genuine methodological gap.

- **Unclear budget allocation between group testing and optimization**: The paper never explicitly states the total evaluation budget for GTBO or how it is split between the group testing and optimization phases. The synthetic benchmark plots (Figure 3) show 100 total iterations, and the text states that GT converges in 39–112 iterations. This makes it impossible to determine, for a problem where GT requires 112 evaluations, how many evaluations remain for optimization — or whether GT was simply not run to full convergence within the budget. Without this information, the comparison to methods that spend the entire budget on optimization is harder to interpret. It would substantially strengthen the paper to specify the budget split and separately show the optimization-phase-only performance after the GT phase concludes.

### Minor
- **Modest real-world improvements on LassoDNA**: The paper itself notes that "the performance increase after group testing is not as visually apparent" on LassoDNA (Section 4.3). Given overlapping standard errors, it is not clear that GTBO significantly outperforms TuRBO (5 trust regions) or CMA-ES on this benchmark. The paper's claim of "frequently outperforming state-of-the-art" is somewhat stronger than the evidence across both real-world benchmarks supports.
- **Gibbs kernel adaptation underspecified**: The SMC procedure references Cuturi et al. (2020) and states "a modified Gibbs kernel for discrete spaces" (Section 3), but does not describe how this kernel is adapted to the continuous-outcome setting. This level of detail makes independent reproduction harder than it should be.
- **Sensitivity analysis varies only one parameter at a time**: The sensitivity analysis (Section 4.4) varies noise, total dimensions, and effective dimensions one at a time. Interactions between these factors are not explored (e.g., high noise with many active dimensions).
- **No statistical significance tests**: The paper reports means and standard errors but does not perform any hypothesis test (e.g., paired t-test or rank-based test) to support claims of superiority over competitors, especially on benchmarks where error bars overlap.

### Trivial
- The convergence threshold in Section 4.1 lists $C_\text{lower} = 5\times10^3$, which would be 5000 in a probability context where values are in [0,1]. This appears to be a parser artifact (the exponent sign was likely lost from $5\times10^{-3}$), but it could confuse readers relying on the extracted text.

## Nice-to-Haves
- A simpler screening baseline (e.g., one-at-a-time perturbations or random grouping with equal budget) would help isolate the benefit of adaptive group testing from the mere act of identifying active dimensions.
- A dedicated limitations subsection synthesizing when the method is likely to fail (e.g., non-axis-aligned subspaces, dense effective subspaces, high noise, or many active dimensions violating the √D assumption) would improve the paper's presentation.
- Joint Bayesian estimation of σ²_n, σ², and ξ within the SMC framework could replace the ad-hoc binning heuristic, making the method more principled and robust.

## Removed Points
These points are flagged for removal from the main evaluation; they are listed here for completeness but should not affect the overall assessment.

- **"Circular dependence" claim (critical issues)**: The critic asserts that Assumptions 1–2 rely on estimated variances, creating a "circular dependence." This misreads standard parameter estimation: the assumptions define the generative model, and variances are estimated separately from data. This is not circular and is standard practice.
- **"Curve continues past 100 iterations" claim (critical issues)**: The critic claims the GTBO curve "continues past 100 iterations" when it does not — the x-axis extends to 100. This reflects a misreading of the plot.
- **C_lower typo criticism (Section-by-Section Notes)**: The critic flags $5\times10^3$ as a probable typo for $0.05$. The value $5\times10^3 = 5000$ is nonsensical for a probability threshold, but this is a parser artifact (minus sign stripped from $5\times10^{-3}$) and not an author error.
- **"Unfair comparison" budget argument (critical issues)**: The critic argues that GTBO's budget includes identification while other methods spend all on optimization, calling for other methods to also have a "discovery" phase or for separate evaluation. Comparing methods on equal total budget is standard practice; GTBO's internal allocation is a design choice, not an unfair advantage. The underlying concern about unclear budget split is real and retained in Major above; the framing as an unfair comparison is not.
- **"The method requires a default point and fixed prior" (Discussion notes)**: The critic lists these as limitations. These are design features of any method with assumptions, not specific weaknesses requiring mitigation.
- **Griewank optimum concern**: The critic mentions the Griewank center optimum as a potential issue, but the paper already explicitly addresses this (Section 4.3), noting it uses a non-standard default away from the optimum and that the center optimum actually boosts projection-based competitors.

## Novel Insights
The reviews surface a tension that the paper itself does not fully grapple with: the group testing phase's variance estimation relies on a √D active-dimension heuristic that is simultaneously a core assumption of the method and a significant limitation on its applicability. The sensitivity analysis honestly documents the breakdown point (32 active out of 100 dimensions), but the paper treats this as an expected parametric limitation rather than investigating whether the method could be made robust to violations through alternative variance estimation strategies. This suggests a potentially productive future direction: joint Bayesian inference of variances and activeness, or a two-stage approach where conservative variance estimates are first used and then refined as the active set is narrowed.

## Suggestions
1. **Clarify the evaluation protocol**: Explicitly state the total evaluation budget for each experiment and how it is split between the group testing and optimization phases. Provide a separate plot showing optimization-only performance (starting after GT concludes) so readers can assess the value of knowing active dimensions independently of the cost of discovering them.
2. **Strengthen the variance estimation**: At minimum, show that the √D binning heuristic performs well across a wider range of active-dimensionality ratios. Ideally, replace it with a principled alternative (e.g., joint Bayesian estimation with conjugate priors within the SMC framework).
3. **Add statistical tests**: Report p-values or Bayesian credible intervals for the key comparisons, especially on the real-world benchmarks where error bars overlap.
4. **Add detail on the Gibbs kernel modification**: Describe how the SMC Gibbs kernel is adapted to the continuous-outcome setting to aid reproducibility.

## Score and Decision

This paper presents a genuinely novel combination of group testing and Bayesian optimization, with a clear motivation and empirical validation that generally supports its claims. The core idea — using adaptive group testing to identify active variables for high-dimensional BO — is well-executed and the results are promising. However, two weaknesses prevent this from being a stronger contribution: the ad-hoc variance estimation heuristic (central to the method's correctness, yet not rigorously justified or compared to alternatives) and the unclear budget allocation between the testing and optimization phases (which makes the experimental comparisons harder to interpret than they should be). These are addressable in revision and do not invalidate the contribution, but they reduce the current paper's convincingness.

I recommend acceptance with the expectation that the authors clarify the evaluation protocol and address the variance estimation in a discussion or extended analysis.

MY FINAL SCORE: <pineapple>6.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>