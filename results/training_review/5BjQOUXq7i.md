Now I have a thorough understanding of the paper. Let me construct my final review.

## Summary

The paper proposes RegMix, which formulates data-mixture selection for LLM pre-training as a regression task. It trains 512 small (1M parameter) proxy models on diverse data mixtures, fits a regression model (LightGBM) to predict Pile-CC validation loss from mixture weights, then simulates the optimal mixture and trains a large (1B parameter/25B token) model. The key claims are: (1) the rank invariance hypothesis (relative ranking of mixtures is consistent across scales) holds with 97.12% Spearman correlation from 1M→1B models, (2) the identified mixture matches/exceeds DoReMi at 10% of the compute, (3) web corpora correlate more strongly with downstream performance than Wikipedia, and (4) domain interactions are too complex for human intuition or scaling laws.

## Strengths

1. **Large-scale systematic empirical study.** Training 512×1M models and 64×1B models with different mixtures is a substantial investment that provides a rich dataset for understanding data mixture effects. This goes well beyond the typical scope of mixture selection papers.

2. **Counterintuitive finding about web corpora.** The paper convincingly shows (Figure 4) that Pile-CC validation loss correlates more strongly with downstream task performance than Wikipedia loss, challenging common assumptions about "high-quality" data. The follow-up analysis with C4100Domain subdomains (e.g., www.ign.com) strengthens this finding.

3. **Rank invariance evidence across model sizes.** The 97.12% Spearman correlation (LightGBM, Table 1) when predicting rankings of 1B/25B models from 1M/1B proxy models provides meaningful support for the core hypothesis, and the 98.64% correlation for 60M models shows clean model-size transfer.

4. **Practical guideline about proxy design.** Figure 3 shows that increasing the number of proxy models helps more than increasing per-model tokens beyond ~0.25B — a useful finding for practitioners designing similar experiments.

5. **Robustness to OOD settings.** Figure 5 (right panel) shows RegMix outperforms human baselines even when Pile-CC is completely excluded from the training corpus and optimized for via proxy, demonstrating the method doesn't require the target domain in the training data.

## Weaknesses

### Fatal
None. No single error invalidates the paper's core claims, though several weaknesses collectively undermine the strength of the contributions.

### Major

1. **Negligible improvement over the simplest possible baseline (Pile-CC Only).** In Table 3, RegMix achieves an average downstream score of 48.6, while Pile-CC Only achieves 48.5 — a difference of 0.1 points with overlapping standard deviations (±0.3 for both). RegMix beats Pile-CC Only on only 5 of 13 tasks, and loses on several. If the regression framework's value is that it supposedly discovers meaningful cross-domain interactions, the fact that it barely outperforms "train exclusively on Pile-CC" is deeply concerning. The paper's central methodological contribution — the regression model that jointly considers all domains — is not shown to add value over this trivial heuristic. The interesting finding that Pile-CC alone works surprisingly well is a genuine empirical contribution, but it undercuts rather than supports the RegMix method.

2. **DoReMi comparison uses renormalized weights without re-running DoReMi's optimization.** The paper takes DoReMi's published weights and renormalizes them across the 17 available Pile subsets (the original used 22). The paper acknowledges "this may result in sub-optimal performance for DoReMi" (line 295), but still draws conclusions like "matches or surpasses DoReMi while utilizing only 10% of the compute budget." This comparison does not reflect DoReMi's performance if run on the same 17-domain setup, and the compute-efficiency comparison inherits this uncertainty. The 3.7×10¹⁹ FLOPs figure for DoReMi is stated without derivation or citation. A fair comparison would require re-running DoReMi on the same 17-domain setup.

3. **Rank invariance hypothesis has limited validation scope.** The hypothesis is tested on only one extrapolation path: 1M/1B→1B/25B tokens (with 60M/1B as an intermediate model-size check). There is no independent test of the token-count dimension (same model size, different tokens) and no validation at substantially larger scales (e.g., 7B+ models). The 60M models use the same 1B token budget, so they isolate model-size invariance but not token-count invariance. The claim that the hypothesis generalizes to much larger scales (70B models, 15T tokens) is an extrapolation without evidence.

### Minor

4. **Comparison to best random mixture is confounded.** The paper claims RegMix (48.6, 5-run avg) surpasses the "Best Model" from Table 2 (47.9). However, the "Best Model" column in Table 2 reports the per-task best performing model among the 64 candidates, and 47.9 is the average of per-task bests — not the average of a single best overall model. The correct comparison would be: train the top-1 predicted mixture multiple times and compare to the single best overall random mixture (also multiple runs) with statistical testing. The current comparison is suggestive but methodologically loose.

5. **"Transcending scaling laws" claim is not rigorously supported.** Section 5.5 argues that data mixture effects are more complex than scaling laws predict, based on a qualitative scatter plot (Figure 5). The paper does not compare RegMix against any scaling-law-based predictor (e.g., Ye et al. 2024, Ge et al. 2024). Without a direct comparison, the claim is unsupported, and it would be more accurate to say RegMix makes different assumptions (non-parametric regression) without claiming superiority.

6. **No sensitivity analysis for the Dirichlet α range (0.1–5.0).** The choice of α determines how extreme the sampled mixtures are, which directly affects the regression model's training distribution. Without ablation, it is unclear whether the method is sensitive to this choice or whether the reported results depend on a particular sampling strategy.

### Trivial

7. **No report of the single top-predicted mixture performance.** The paper averages the top-100 predicted mixtures for the final model (line 138). It would be informative to see whether the top-1 prediction performs similarly or worse, and whether averaging is critical.

8. **"8 out of 14" claim in text vs 13 tasks in table.** The text says "beats all other three methods on the task performance in 8 out of 14 cases" (line 295), but the table shows 13 benchmarks. (Possibly counting average as a 14th case — minor inconsistency.)

## Nice-to-Haves
- Re-run DoReMi on the same 17-domain setup to get a clean compute efficiency comparison.
- Validate rank invariance at a larger scale (e.g., 3B or 7B model) or at least test token-count invariance independently (same model size, different token budgets).
- Report the top-1 predicted mixture performance (without averaging top-100) to measure whether averaging is critical.
- Compare RegMix against a scaling-law-based mixture optimizer (Ye et al. 2024, Ge et al. 2024) to substantiate the "transcending scaling laws" claim.

## Removed Points
- **Criticism about Abstract/Introduction compute claim**: "the overall compute cost of 512 small models (~2% of one 1B model) is small mostly because the small models are tiny" — This is exactly the point. The paper makes a specific claim about their setup, not a general guarantee. This is a restatement of the paper's own contribution, not a weakness.
- **Criticism about Section 5.2 being "circular"**: The critic claims the paper chooses Pile-CC because it correlates and then optimizes it, calling this circular. This misunderstands the methodology — the correlation is discovered from data, then used as a proxy target. This is standard surrogate optimization and not circular.
- **Criticism about Section 5.4 (linear coefficients vs LightGBM)**: The paper explicitly uses linear regression for visualization and LightGBM for prediction. This is a standard and appropriate choice.
- **Criticism about Table 2 "Best Model" being "best per-task, not the best overall"**: While this is actually correct about the table structure, the critic's framing suggests this invalidates the comparison entirely, which overstates the problem. The issue is that the comparison is loose, not that it's meaningless. Moved here because the critic's specific phrasing was more misleading than helpful — the core concern is better captured in Minor weakness #4.

## Novel Insights
The key tension in this paper is between its genuine empirical contributions and the weak evidence for its claimed methodological advance. The finding that Pile-CC alone nearly matches the regression-optimized mixture is simultaneously the paper's most interesting and most damning result. It suggests that for this particular dataset and evaluation setup, the primary signal is simply "use more web data" — a rule of thumb that does not require complex regression. However, this does not mean the method is useless; rather, it means the paper's evidence does not demonstrate its value above a trivial baseline in this specific setting. The question the paper raises but does not answer is: in what settings (different data distributions, larger scales) would the regression framework's modeling of cross-domain interactions actually matter?

## Suggestions
1. **Strengthen the core comparison**: Train the best random mixture from the 64 candidates multiple times (5 runs) and compare directly to RegMix (also 5 runs) with a proper statistical test. If RegMix does not significantly outperform the best random mixture, the paper should honestly report this.
2. **Address the Pile-CC Only baseline directly**: The paper should explicitly discuss why RegMix barely improves over Pile-CC Only, and ideally run a controlled experiment where Pile-CC is not available (as in the OOD experiment) to show the method's value in settings where the simple heuristic fails.
3. **Re-run DoReMi fairly**: Either re-run DoReMi on the 17-domain setup, or remove the compute-efficiency claim and present the comparison as "using published weights (which may be suboptimal for our setup)."
4. **Validate at one additional scale**: Even a 3B or 7B model on 2 mixtures (predicted vs. random) would substantially strengthen the rank invariance claim.
5. **Tone down the scaling law claim**: Replace "transcend scaling laws" with a more measured statement: the regression approach makes different assumptions and captures non-parametric relationships that parametric scaling laws may miss.

## Score and Decision

The paper addresses an important problem and presents a large-scale empirical study with several interesting findings. However, the core methodological claim — that the regression framework discovers a superior mixture by modeling domain interactions — is not convincingly supported. The method's performance is indistinguishable from training exclusively on Pile-CC, and key comparisons (DoReMi, best random mixture) have significant methodological weaknesses. The paper's genuine contributions (the web corpora finding, proxy scaling guidelines, rank invariance evidence) are valuable but do not constitute a validated new method. Major revisions with stronger experimental evidence would be needed.

MY FINAL SCORE: <pineapple>4.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>