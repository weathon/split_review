I now have all the information needed. Let me construct the final consolidated review.

## Summary

This paper introduces the concept of *ε-interventional faithfulness* — an assumption that marginal distribution distances between observational and interventional settings reveal causal paths — and proposes a score over causal orders whose optimum provably approximates the true topological order under this assumption. The authors prove upper bounds on the expected number of reversed edges (Theorems 5.2, 6.2–6.3), introduce the Intersort algorithm to approximately optimize the score, and demonstrate strong empirical performance across linear, RFF, neural network, and synthetic gene regulatory network domains against baselines (PC, GIES, DCDI, EASE).

## Strengths

- **Novel framing of causal order learning from interventional data.** The paper is, to its knowledge, the first to propose inferring the causal (topological) order directly from single-variable interventional data (line 30). This re-framing is conceptually clean and practically motivated by domains such as single-cell transcriptomics where many single-gene perturbations are available.

- **Formal theoretical guarantees.** The paper proves nontrivial upper bounds on the expected $D_{top}$ error of the score optimum under random interventions (Theorem 5.2), including closed-form bounds for Erdős–Rényi graphs (Theorem 6.2) and scaling results showing the normalized error remains $\mathcal{O}(d)$ as $d \to \infty$ (Lemma 6.4). These are the first such guarantees for interventional causal order learning.

- **Empirical validation across diverse data types.** Intersort outperforms all four baselines on almost all settings across linear, RFF, neural network, and SERGIO-generated gene regulatory data (Figure 4), with multiple noise distributions (Gaussian, heteroscedastic, Laplace). The empirical superiority is especially clear at higher intervention ratios (50%+).

- **Robustness to data standardization.** The paper explicitly standardizes data using observational mean/variance, removing the Varsortability artifact (line 279), and Intersort still performs well. This demonstrates its success is not driven by spurious variance-based ordering cues.

- **Relaxation analysis.** Section 6 derives bounds under a weaker version of ε-interventional faithfulness where only direct children are affected by interventions, providing theoretical robustness even when the full assumption is violated.

## Weaknesses

### Fatal
None.

### Major

1. **The ε-interventional faithfulness assumption is stronger than the paper characterizes, and its practical scope remains unestablished.** The assumption requires a global all-or-nothing condition: for every intervened $i$ and every $j \neq i$, the marginal distance $D(P_{X_j}^{\text{obs}}, P_{X_j}^{\text{do}(i)})$ exceeds $\varepsilon$ *iff* there is a directed path from $i$ to $j$. The "only if" direction — requiring that *no* non-descendant's marginal changes — is especially strong and could be violated by factors such as selection effects or intervention side-effects. The paper proves the assumption holds for linear SCMs with continuous coefficients (Lemma 4.2) and when all directed paths imply a total causal effect (Lemma 4.1), but the latter essentially assumes the conclusion. The paper repeatedly calls the assumption "light" (line 19) and "a lighter version" (line 23), yet provides no characterization of its scope beyond linear systems. The authors candidly note this gap ("We leave further theoretical work to characterize how large the class...is as future work," line 98), but this is not a minor detail — the practical relevance of the entire framework hinges on knowing when this assumption holds. The relaxation in Section 6 covers cancellation effects but assumes only direct children are affected, which severely reduces the available signal.

2. **ε is treated as known in the theory, but its selection from finite samples is ad hoc.** All theoretical guarantees assume a specific ε that matches the underlying ε-margin. The paper suggests (line 115) choosing ε "smaller than the smallest non-negative distance," but with finite samples, no empirical distance is exactly zero, making this a noisy estimate. The experiments fix ε=0.3 or 0.5 across all settings with no sensitivity analysis, no cross-validation procedure, and no principled guidance. If set too high, true descendant effects fall below threshold; if too low, noise produces spurious signals. The paper acknowledges this as future work (line 290), but the gap between the theory (which requires a correct ε) and practice remains unaddressed.

3. **The theoretical guarantees apply to the score maximizer π_opt, but Intersort only approximates it, and the gap is unquantified for realistic problem sizes.** The core theoretical results (Theorems 5.1–5.2, Lemma 5.1) are statements about $\pi_{opt}$. The paper shows that for $d=5$, Intersort closely approximates the exact optimum (Figure 2, left). For $d=30$ (Figure 2, right), only Intersort's output and the theoretical bounds are shown — not the true optimum. The paper acknowledges "the error is above the upper-bounds for many settings" and "we can observe room for improvement" (line 239), but without quantifying this gap, a reviewer cannot tell whether performance limitations stem from the score itself or from the optimization. This ambiguity weakens the connection between theory and experiment.

### Minor

1. **Baseline comparison may be asymmetric.** Intersort's hyperparameters ($\varepsilon=0.3/0.5$, $c=0.5$) are tuned per domain, while the paper does not report hyperparameter sweeps for baselines. GIES uses a Gaussian BIC score (line 281) that may be suboptimal for nonlinear data, and DCDI parameters are not described. Extracting causal orders from PC/GIES CPDAGs (as the paper does) may also lose information compared to methods natively scoring orders. These factors make it unclear how much of Intersort's advantage is due to genuine superiority vs. favorable tuning.

2. **No experiments with varying sample size.** All results use a fixed 5000 observational + 100 per-intervention samples. Sensitivity to sample size would be informative, especially since Wasserstein distance convergence rates depend on dimensionality.

3. **No confidence intervals or statistical tests for baseline comparisons.** The violins in Figure 4 show distributions but are not accompanied by pairwise statistical tests, making it hard to judge whether differences are meaningful for settings where violins overlap substantially.

4. **Code and data availability not stated.** The paper should include a statement about releasing the implementation.

### Trivial
- The paper mentions runtime as $\mathcal{O}(d \cdot |\mathcal{I}| \log(d \cdot |\mathcal{I}|))$ for step 1 (line 188) but does not discuss the local search cost for larger $d$ beyond noting it may become expensive (line 239). This is adequate for the current scope but could be expanded.

## Nice-to-Haves

- **Report Dₜₒₚ alongside fraction of pairs correctly ordered**, to help readers interpret the scale of errors on dense vs. sparse graphs.
- **Analyze how often Step 2 (local search) improves over Step 1 (sort-ranking)**, to justify the additional complexity.
- **Provide a data-driven procedure for choosing ε**, e.g., using permutation tests or bootstrapping to control false positive rates for detecting distribution changes.
- **Explain the "effective intervention ratio" $p_{\text{int}} / \sqrt{p_e}$** used in Figure 2, or note if it is purely empirical.
- **Include ablation/timing studies for larger d** (e.g., d=50,100) to characterize Intersort's scaling behavior.

## Removed Points

These points were removed per the filtering guidelines:

1. The criticism about the "effective intervention ratio" lacking theoretical justification. **Reason:** The paper presents this as an empirical observation ("error is approximately monotonic when ordered by the effective intervention ratio," line 235). Asking for a theoretical derivation is scope creep — the paper does not claim this ratio is theoretically motivated.
2. The criticism about the "only if" direction being violated by "side-effects of the intervention mechanism itself." **Reason:** This is a generic concern that applies to essentially any interventional causal discovery method, not specific to this paper's framework.

## Novel Insights

The most interesting cross-review observation is that the paper's key vulnerability is not any single flaw but a compound gap: the assumption (ε-interventional faithfulness) is invoked to derive guarantees about $\pi_{opt}$; the score's ε parameter must be known; and the algorithm only approximates $\pi_{opt}$. Each link in this chain has a gap, and the empirical evaluation does not isolate which gap drives observed errors. For instance, when Intersort exceeds the theoretical upper bound (Figure 2, right), is it because the assumption is violated, because ε is mismatched, or because local search found a suboptimal permutation? The paper could strengthen the narrative by explicitly distinguishing these sources of error.

## Suggestions

1. Provide concrete examples of nonlinear SCMs (beyond linear) that provably satisfy or violate ε-interventional faithfulness. This would substantially strengthen the paper's claim that the assumption is realistic.
2. For the experiment in Figure 2 (d=30), compute an empirical upper bound on the gap by running Intersort from multiple random initializations or by solving a convex relaxation of the score maximization — anything that bounds how far Intersort is from the true $\pi_{opt}$.
3. Include a sensitivity analysis for ε: vary it systematically and show how Intersort's performance changes, with a recommendation for a data-driven selection heuristic.
4. Add a controlled experiment where the ε-interventional faithfulness assumption is systematically violated (e.g., by canceling paths or adding intervention side-effects) to test the method's robustness in regimes where the theory does not apply.

## Score and Decision

The paper makes a genuine and novel contribution — it is the first to formulate causal order learning from interventional data, provides nontrivial theoretical guarantees, and demonstrates strong empirical performance. The weaknesses are real but not fatal: the central assumption's scope needs better characterization, ε-selection is ad hoc, and the theory–algorithm gap is unquantified for larger d. These are standard gaps for a first paper on a new framework and can be addressed in future work and a camera-ready revision. The contribution is sufficient for acceptance.

MY FINAL SCORE: <pineapple>6.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>