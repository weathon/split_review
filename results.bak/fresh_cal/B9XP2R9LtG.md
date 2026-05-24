Now I'll synthesize the final review.

## Summary

This paper presents the first dedicated quantitative scaling study of intrinsic activation sparsity in decoder-only Transformer LLMs. It introduces PPL-\(p\%\) sparsity, a metric that balances performance and sparsity via adaptive per-layer thresholds tied to a target PPL increase. Through experiments across 5 model scales (0.1B–1.2B) with ReLU and SiLU activations, the paper identifies: (1) opposite training-time sparsity trends (ReLU becomes sparser, SiLU denser) with convergent power-law forms, (2) a width-depth bottleneck point below which sparsity increases linearly, and (3) near scale-invariance of limit activation sparsity under similar width-depth ratios. The findings offer practical guidance for designing sparser, more efficient LLMs.

## Strengths

- **PPL-\(p\%\) sparsity achieves a better performance–sparsity trade-off than prior metrics.** Figure 3 and the accompanying analysis show the proposed metric consistently yields lower PPL than Straightforward ReLU, Top-\(k\), and FAT-\(\epsilon\) baselines at matched sparsity ratios across multiple model scales. The metric demonstrably recognizes weakly-contributed neurons more precisely.

- **First quantitative scaling laws for activation sparsity in decoder-only LLMs.** Section 4.2 derives closed-form equations (convergent increasing power-law for SiLU, convergent decreasing logspace power-law for ReLU) with fitted curves across five model scales (Figure 4). This goes beyond prior qualitative work and provides a predictive tool for sparsity as a function of training tokens.

- **Discovery of a width-depth bottleneck that governs sparsity.** Section 4.3 shows that activation ratio increases linearly with width-depth ratio up to a bottleneck point (~114 for 0.1B ReLU models) and then plateaus. Combined with the performance interval (Figure 6), this gives concrete architectural guidance for designing sparser models.

- **Demonstration that limit activation sparsity is weakly correlated with parameter scale.** Figure 7 shows at most ±2.7 percentage point variation in limit activation ratio from 0.1B to 1.2B. The analysis is supported by activation-frequency distributions across datasets (Figure 9) and token-wise comparisons (Figure 10), providing converging evidence that activation patterns are insensitive to model size.

- **Practical validation that PPL-1% sparsity preserves downstream performance.** Table 1 reports that models at PPL-1% sparsity achieve average scores on commonsense reasoning and reading comprehension benchmarks comparable to the dense baseline, confirming real-world applicability.

- **Novel perspective on sparsity convergence as a lens for neuron specialization.** Section 5 connects the slower convergence of sparsity (vs. loss) to ongoing neuron specialization, an insight that is underexplored in existing scaling analyses.

## Weaknesses

### Fatal
None.

### Major

- **Inconsistent specification of training tokens relative to parameter scale.** Section 3.2 (line 72) states training tokens are "no less than 80 times the scale of non-embedding parameters," but the Figure 4 caption (line 116) says "no less than 190 times." These differ by more than 2×. The discrepancy matters for interpreting whether the asymptotic regime is plausibly approached and which standard was actually used. This must be resolved in revision.

- **Width-depth ratio analysis is limited to a single configuration (0.1B, ReLU only).** While the paper is transparent about this scope (Section 4.3 explicitly states "on the 0.1B ReLU-activated model"), the bottleneck value (~114) and the recommended interval (74–282) are presented as actionable design guidance without evidence that they generalize to larger scales or to SiLU-activated models. The paper's claim of being "comprehensive" is weakened by this mono-scale architectural analysis.

### Minor

- **No goodness-of-fit statistics or confidence intervals for the fitted power-laws.** The limit values \(A_0\) in Eqs. (4)–(5) are extrapolated from finite training runs (80–190× parameter-scale tokens). No R², RMSE, residual analysis, or confidence intervals on \(A_0\) are reported. The central claim that limit sparsity is weakly correlated with scale rests on these extrapolated values, and readers cannot assess how tight the constraint is.

- **Hyperparameter transfer confound between ReLU and SiLU experiments.** Section 3.3 states that training follows MiniCPM's optimal batch sizes and learning rates, which were likely tuned for SiLU-based models. Using the same hyperparameters for ReLU models may systematically affect sparsity evolution. The paper does not discuss this potential confound.

- **The "Deduction" for faster convergence in smaller models is heuristic, not derived.** The grouping model in Eq. (6) assumes group-size fractions \(t_i/d_f\) are constant across scales and then argues combinatorially that larger models converge more slowly. This is a plausible intuition, but no empirical test of the assumption is provided (e.g., whether group fractions are actually invariant). The label "Deduction" overstates the force of the argument.

- **No width-depth results for SiLU models.** The analysis in Section 4.3 covers only ReLU. Since the paper ultimately recommends ReLU over SiLU for sparsity, showing that the width-depth relationship generalizes across activation functions would substantially strengthen this recommendation.

### Trivial
- The term "data-scale ratio" used in Figure 8 and the derivative analysis is introduced without explicit definition in the main text (the definition is likely in a footnote stripped by formatting, but it should be stated plainly).
- Line 109 has an apparent formatting artifact: "PPL-$.1\%$" should likely read "PPL-$1\%$".

## Nice-to-Haves
- Validating PPL-1% across additional datasets beyond commonsense reasoning and reading comprehension (e.g., coding, math) would strengthen confidence in the metric's generality.
- Testing whether the width-depth bottleneck shifts with model scale (even at one additional scale) would substantially increase the value of the architectural guidance.
- Reporting correlation coefficients or slope uncertainties for the scale-insensitivity claim in Section 4.4 would strengthen the "weakly correlated" assertion.

## Removed Points

*These points were raised by reviewers but removed after verification against the paper. They are listed here for completeness but should not weigh on the evaluation.*

1. **Metric validity only at 0.1B (Harsh Critic Critical Issue 1).** The paper explicitly states (line 109) that "we evaluate models of **different scales** on the benchmarks" for Table 1. The claim that the metric is validated only at 0.1B is contradicted by the paper's text. **REMOVED** (factually incorrect).

2. **MoE comparison insufficiently controlled (Harsh Critic Critical Issue 4).** This is a motivating comparison in the introduction (Figure 2), not a core empirical claim. The paper states it compares MoE to a vanilla Transformer of "the same parameter scale and amount of training data" with a footnote (stripped by parser). For a motivating observation, this level of detail is adequate. **REMOVED** (scope creep; not a core claim).

3. **Top-k baseline fairness concern.** The critic suggests Top-k's usual implementation differs, but the paper's description of layer-wise Top-k (line 103) is standard, and all FFN layers in the studied architecture have the same intermediate dimension. **REMOVED** (misunderstanding).

4. **Binary search lacks specifics (validation set, granularity).** These are standard implementation details. The binary search over CETT is described conceptually, which is sufficient for reproducibility given CETT is a known prior method. **REMOVED** (implementation nitpick).

5. **Questioning the logspace power-law functional form.** The paper states "After careful attempts, we find that..." (line 113). Using an empirically determined functional form is standard practice in scaling law research. **REMOVED** (methodological nitpick without concrete flaw).

6. **Complaint about the word "comprehensive."** Subjective wording judgment. **REMOVED** (style nitpick).

7. **ReLU vs SiLU performance trade-off discussion.** The critic suggests the paper should acknowledge that SiLU models (LLaMA) achieve strong performance — the paper does compare their performance and finds it "comparable" (line 134). **REMOVED** (already addressed).

## Novel Insights

The most interesting insight emerging from this synthesis is the observation that the paper's core contribution is descriptive (discovering scaling laws) rather than prescriptive (proving optimality of any particular design), but the descriptive findings are immediately useful: the width-depth bottleneck suggests deeper architectures at fixed parameter counts yield sparser models, and the scale-insensitivity of limit sparsity means experiments at smaller scales are predictive of larger-scale behavior. The meta-reviewer notes that the harsh critic's most serious concerns (metric validation, MoE comparison) were contradicted by the paper itself, leaving the genuine weaknesses as matters of scope (mono-scale width-depth analysis) and reporting rigor (missing confidence intervals on fits). This is a fundamentally solid paper whose limitations are clearly bounded.

## Suggestions
1. Resolve the 80× vs 190× tokens-to-parameters inconsistency.
2. Add at least goodness-of-fit metrics (R² or RMSE) for the power-law fits, and preferably bootstrap-based confidence intervals on the limit values \(A_0\).
3. Explicitly discuss the hyperparameter transfer confound (MiniCPM settings likely optimized for SiLU) and its potential impact on the ReLU vs. SiLU comparison.
4. Clarify the definition of "data-scale ratio" in the main text.
5. Temper the "Deduction" label in Section 4.4 or provide an empirical test of the grouping assumption.

MY FINAL SCORE: <score>7.5</score>
MY FINAL DECISION: <decision>Accept</decision>