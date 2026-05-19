- Decision: Reject
- Avg Score: 5.33
- Scores: 5, 6, 5
Now I have a thorough understanding of the paper and can evaluate all claims against the actual text. Let me write the final consolidated review.

## Summary

The paper proposes VTruST, a data-centric framework for selecting training data subsets that optimize user-specified tradeoffs between accuracy, fairness, and robustness. The core idea is to define additive value functions for each trustworthiness metric, combine them with user-specified weights λ, and solve the resulting subset selection as an online sparse approximation problem using a novel online variant of Orthogonal Matching Pursuit (OMP). The framework is evaluated on social (COMPAS, Adult, MEPS20), image (CIFAR-10, MNIST, TinyImageNet), and scientific datasets.

## Strengths

1. **Novel framework combining data valuation with multi-objective trustworthiness control.** The paper proposes a principled way to combine accuracy, fairness, and robustness value functions into composite objectives (V_af, V_ar, V_rf) with user-controlled λ weights (Section 3.2). This provides explicit tradeoff control that prior data-centric trustworthy AI methods (e.g., SSFR) lack. The Pareto frontier demonstration in Figure 1 (for Adult Census) illustrates this controllability concretely.

2. **Online OMP algorithm for streaming subset selection.** Algorithm 1 and the DataReplace module (Algorithm 2) propose a novel online variant of Orthogonal Matching Pursuit that handles dynamic feature arrival across training epochs, replacing selected points when a new point improves the approximation. This is a distinct algorithmic contribution that addresses the practical challenge of subset selection during training without storing all historical features.

3. **Broad experimental evaluation with positive results across multiple domains.** The empirical results (Tables 1-3) span social fairness (3 datasets), image robustness (3 datasets with 3 architectures), and scientific data (2 datasets). Key positive results include: VTruST-F achieving EO disparity of 0.01 on MEPS20 vs. 0.06-0.09 for baselines; VTruST-R on TinyImageNet at 60% selection achieving RA 41.50 vs. SSR's 30.07 and AugMax's 40.98; and competitive or superior accuracy while using fewer data points than full-data methods.

4. **Data-centric explanations for selected subsets.** Section 4.3 provides post-hoc analysis (CF-Gap, uncertainty, distinctiveness) showing that VTruST selects more diverse and less biased samples compared to SSFR. The anecdotal comparison in Table 4 concretely illustrates the redundancy in SSFR's selections vs. diversity in VTruST's.

## Weaknesses

### Major

1. **The fairness value function's theoretical grounding is incomplete.** The sparse approximation formulation (Section 3.1) derives features X_i^k from a second-order Taylor expansion of the **loss function** l(θ, D') around an SGD update (lines 68–72). However, the fairness value function V_f is defined using equalized odds disparity ed(θ, D') = max(|l(θ, D'_{y0,z0}) − l(θ, D'_{y0,z1})|, |l(θ, D'_{y1,z0}) − l(θ, D'_{y1,z1})|) (lines 94–96). The paper does not show that the loss-derived features are appropriate for approximating changes in ed(θ, D'), nor does it derive features from a Taylor expansion of ed(θ, D') itself. The erroneous claim on line 96 that "ed(θ, D'_1) + ed(θ, D'_2) = ed(θ, (D'_1 + D'_2))" (which is false — the sum of two maxima is not the maximum of the sum) further indicates that the additivity argument for fairness is not properly justified. While V_f **is** additive over training datapoints by construction (it is defined as a sum of per-datapoint changes), the fundamental gap between the loss-derived features and the fairness objective means the fairness component of the framework is not adequately supported. This does not invalidate the accuracy/robustness components but weakens the claim of a unified framework handling fairness.

2. **The evaluation lacks critical baselines and overstates improvements.** (a) The robustness experiments (Table 2) compare VTruST-R against AugMax (a data-augmentation method using the full pool) and SSR (another selection method), but **no random subset from the same SAug pool** is included as a baseline. Since VTruST-R selects ω% of SAug, a random ω% of SAug is the most directly relevant comparison to show that the selection algorithm itself — not just the SAug pool — drives improvements. (b) The claimed "~10–20%" improvement (line 34) over state-of-the-art is not consistently reflected in the tables: on CIFAR-10 (60%), VTruST-R's RA of 89.21 improves over SSR's 88.0 by 1.21 points (~1.4% relative), and against AugMax's 86.44 by 2.77 points (~3.2% relative). Larger improvements appear on TinyImageNet and MNIST, but the broad "10–20%" claim is unsupported across the board. (c) The Pareto curves (Figure 1) showing tradeoff controllability are shown for Adult Census only; COMPAS and MEPS20 results are not shown.

3. **The theoretical contribution of the online OMP is weak.** Theorem 1 (Section 3.3) states that a new point replaces a selected point if its projection onto the residual exceeds that of the existing point and the existing point's coefficient is negative — this is essentially a restatement of the DataReplace algorithm's condition (Algorithm 2, line 162), not a genuine theoretical guarantee. No convergence bound, recovery guarantee, or proof is provided. The per-epoch complexity advantage claimed (O(ωM(N−ω)) vs O(ωMN)) is marginal since the algorithm still processes all N datapoints per epoch, and no empirical comparison to standard (batch) OMP on the final epoch's features is provided to demonstrate the online replacement strategy's benefit.

### Minor

1. **No hyperparameter sensitivity analysis.** The framework has two user-controlled parameters (λ and ω). No ablation or sensitivity study is provided showing how performance varies with different λ values or subset sizes ω (only 40% and 60% are shown for robustness; a single 60% for fairness).

2. **The fairness model-centric baselines are a mismatch.** The paper compares VTruST-F (data-centric) to SSFR, FairMixup, and FairDummies, which are model-centric methods that modify the training objective. While not a weakness per se, this comparison conflates the data-centric vs. model-centric dimension. The most important baseline — random 60% subset — is included, but the paper's outperformance over random is not always statistically compelling given the standard deviations and small number of runs (3 seeds).

3. **Scalability discussion is missing.** The method requires computing gradient-vector products for all N training points per epoch, which scales linearly with N. For large datasets, this is expensive. The paper does not discuss this limitation.

4. **Qualitative explanations are anecdotal.** The data-centric explanation (Section 4.3) relies on showing 10 anecdotal samples and a box plot without statistical tests, limiting the strength of the interpretability claims.

### Trivial

- In Table 1, FairMixup on MEPS20 reports ER 0.89±0.02, which is anomalously high and unexplained.
- The paper refers to MEPS-20 as both "MEPS" and "MEPS20" inconsistently.

## Nice-to-Have

- Compare online OMP against standard (batch) OMP run on the final epoch's features to demonstrate the advantage of the online replacement strategy.
- Include a random subset baseline from the SAug pool for robustness experiments.
- Show Pareto curves for all three social datasets, not just Adult Census.
- Derive or justify features for the fairness value function from a Taylor expansion of ed(θ, D') rather than relying on loss-derived features.
- Add statistical significance tests (e.g., confidence intervals over more seeds) for the main claims.

## Removed Points

These points from the reviewers were removed for the reasons stated below:

- *"MEPS20: Random actually has lower ER (0.12 vs. 0.09)"* — **Factually wrong.** The table shows VTruST-F ER = 0.09±0.003, Random ER = 0.12±0.017. VTruST-F has lower (better) ER.
- *"Fairness value function is not additive, breaking the core formulation"* — Overstated. V_f is additive over training datapoints by construction (it is defined as a sum of per-datapoint changes in ed). The erroneous justification about validation-set additivity is a real error, but it does not "break" the framework. I have recast this as a Major weakness about incomplete theoretical grounding rather than a Fatal structural flaw.
- *"The paper does not compare to influence functions/TRAK"* and *"Related work omits key data valuation methods"* — The paper explicitly mentions Shapley values, influence functions, TRAK, and gradient-based approximations on lines 25 and 461.
- *"Reproducibility: undisclosed hyperparameters" and "optimizer, learning rate, number of epochs... partially reported"* — These details are standard for a conference paper; the paper reports subset sizes and architectures. The critic overstates reproducibility concerns.
- *"Pseudocode inconsistencies"* — The condition π > π' & γ ≤ 0 & (π' + γ) > π_max in Algorithm 2 is logically consistent: π is the new point's projection, π' is the existing point's projection, and γ is the existing point's coefficient. No actual inconsistency.
- *"Spinodal result... suspicious"* — Speculative. The result (VTruST-R 40% RA > wholedata RA) is explainable by the subset removing label-corrupted or low-quality samples, which is the method's intended behavior.
- *"Complexity O(ωMN) same as standard OMP"* and *"'online' aspect does not reduce computation"* — The paper acknowledges the algorithm processes all N points per epoch; the complexity improvement is marginal but not misrepresented.
- *"Score collapse" strength from Strength Finder about improvements being "within one standard deviation"* — Removed because the claim is inaccurate for several comparisons (MEPS20 EO/DP, Adult DP, COMPAS DP all show improvements well beyond one std).
- *Generic strengths* ("addressed an important problem") — Removed as they are not specific to the paper's concrete contributions.

## Novel Insights

None beyond the paper's own contributions. The core tension identified is between the paper's framing as a unified framework for fairness, accuracy, and robustness and the insufficient theoretical connection between the loss-derived sparse approximation features and the non-loss fairness objective. This is an important design consideration for any future work attempting to extend influence-function-style feature approximations to fairness metrics involving max/absolute-value operations over group-conditioned losses.

## Suggestions

1. **Fix the fairness feature derivation.** Either (a) derive fair-specific features from a Taylor expansion of ed(θ, D') with respect to SGD updates (using subgradients where ed is non-differentiable), or (b) replace ed with a differentiable surrogate fairness metric that can be directly expanded, or (c) restrict the framework's claims to accuracy and robustness and present fairness as a preliminary/experimental extension acknowledging the approximation gap.

2. **Add a random subset baseline from the SAug pool** in Table 2. This is critical to disentangle the benefit of the SAug construction from the benefit of the VTruST selection algorithm.

3. **Tone down the "10–20%" claim** to match what the data actually supports, or provide a clear explanation of which specific comparisons yield this margin.

4. **Provide a comparison to standard (batch) OMP** on the final epoch's features to demonstrate that the online replacement strategy is beneficial rather than equivalent.

5. **Show Pareto curves for all three social datasets** and provide a sensitivity analysis for λ and ω.
