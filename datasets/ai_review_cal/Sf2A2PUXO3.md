- Decision: Accept
- Avg Score: 5.75
- Scores: 6, 6, 5, 6
Now I have a thorough understanding of the paper. Let me produce the final consolidated review.

---

## Summary

This paper proposes using dropout (both Bernoulli and Gaussian) as a fast mechanism to explore the Rashomon set of neural networks for estimating predictive multiplicity. The authors provide theoretical bounds linking dropout parameters to the probability that a dropout-perturbed model lies within a given loss deviation (Rashomon parameter), covering linear models (ridge regression, Brier-score classifiers) and feed-forward neural networks. Empirically, on 6 UCI datasets and a COCO human-detection task with YoloV3, they show that dropout produces higher estimates of multiplicity metrics (VPR, RC, Ambiguity, Discrepancy) than retraining with different random seeds under the same loss deviation, while achieving 20×–5000× per-model speedup. They further demonstrate applications in ensemble-based multiplicity mitigation and model selection.

## Strengths

- **Novel framework for Rashomon set exploration in neural networks.** The paper is the first to connect dropout with Rashomon set membership, providing a concrete alternative to costly retraining or adversarial weight perturbation for exploring near-optimal models. This fills a real gap—prior work on predictive multiplicity focused on tractable special cases (linear models, sparse decision trees, GAMs) or expensive retraining.

- **Theoretical grounding connecting dropout parameters to loss deviation.** Propositions 1–4 establish probability bounds showing that, under controlled dropout rates (asymptotically vanishing with dimension), dropout-perturbed models lie in the Rashomon set with high probability. The extension to FFNNs (Proposition 4) is a nontrivial result leveraging Lipschitz continuity of activations and provides a concrete bound on loss deviation in terms of dropout variance, network depth, and width.

- **Consistent and substantial computational speedup.** Table 1 reports 28×–305× per-model speedup over retraining and 1121×–5345× over AWP across datasets. These are genuine orders-of-magnitude savings, making multiplicity estimation practical for neural networks where retraining hundreds of models would be prohibitive.

- **Empirical demonstration that dropout explores more diverse models than retraining under the same loss budget.** Figure 1 shows that across six UCI datasets and six multiplicity metrics, both Bernoulli and Gaussian dropout produce consistently higher estimates than retraining. Since both methods produce subsets of the true Rashomon set (verified by the loss constraint), higher estimates indicate tighter lower bounds on the true multiplicity.

- **Downstream applicability.** The framework is shown to enable (i) ensemble-based multiplicity reduction and (ii) model selection for lower multiplicity (Figure 3), and is validated on a complex real-world architecture (YoloV3 on MS COCO, Figure 2), demonstrating generalization beyond simple feed-forward nets.

## Weaknesses

### Fatal
None.

### Major

- **Post-hoc quantile selection for per-sample metrics.** For VPR and RC (metrics defined per sample), the paper states: "we plot the values of 50% or 90% quantile, depending on which quantile value best shows the difference between dropout and the baseline methods" (line 274). This is explicit cherry-picking of the most favorable presentation, not a pre-specified analysis choice. While the overall trend is consistent across multiple metrics, the quantile selection undermines the rigor of the comparison for these two metrics. The authors should either pre-specify the quantile or report both (or a measure of distribution, e.g., a boxplot).

- **Theoretical analysis addresses membership probability, not coverage of the Rashomon set.** Propositions 2–4 establish that dropout models are *likely to belong* to the Rashomon set, which is necessary but not sufficient for effective multiplicity estimation. The paper does not characterize whether the sampled models span the range of predictions—the extremes of score variation, the decision boundary, or the diverse regions that determine multiplicity. A degenerate exploration returning 100 nearly identical models could satisfy all membership bounds but would be useless for estimating VPR, ambiguity, or discrepancy. The empirical results (Figure 1) provide evidence that dropout does explore diverse regions in practice, but this is not backed by any theoretical characterization of prediction variance, output covariance, or coverage. A direct empirical analysis of how prediction diversity varies with dropout rate (e.g., pairwise model disagreement vs. loss deviation) would substantially strengthen the paper.

### Minor

- **No error bars, confidence intervals, or measures of variability on reported multiplicity estimates.** The paper obtains 100 models per dropout parameter setting (line 269) but reports only point estimates in Figure 1. Given the stochastic nature of both dropout and retraining, readers cannot assess the stability or statistical significance of the reported differences. Bootstrapped confidence intervals or multiple independent runs would address this.

- **Loose theoretical bounds for practical finite-dimensional settings.** The Markov-inequality-based bounds in Propositions 2–4 can become vacuous (negative) for realistic parameter ranges (e.g., p=0.1, M=10, ε=0.1 gives a bound of 1−10.1/0.1 = negative). The asymptotic claim (probability → 1 as d→∞ with vanishing dropout rate) is mathematically valid but provides limited practical guidance for choosing dropout rates on finite datasets. Proposition 4's bound also grows exponentially in depth K and linearly in max width m, limiting its applicability to deep networks. The paper acknowledges these limitations implicitly through the asymptotic framing, but should be explicit about the practical looseness of the bounds.

- **Missing comparison with MC Dropout (inference-time dropout) as a baseline.** The paper cites Gal & Ghahramani (2016) as related work on uncertainty estimation but does not compare against their approach as a baseline for multiplicity estimation. MC Dropout also generates multiple models from a single pre-trained network via dropout at inference time, making it a natural (and computationally similar) competitor. A comparison would clarify the specific benefit of the paper's parameter-control approach over the standard inference-time dropout setup.

- **Ensemble application does not report whether accuracy is maintained.** Figure 3a shows that multiplicity decreases with ensemble size, which is expected from variance reduction. The paper does not report whether the ensemble's accuracy degrades, stays constant, or improves as more dropout models are added. Without this, readers cannot assess the practical viability of the ensemble mitigation strategy.

### Trivial

- **Figure 1 is dense:** The figure contains many subplots (6 datasets × 6+ metrics), making individual panels difficult to read, especially for smaller datasets (Dermatology, Contraception). While the aggregated trends are clear, better structuring (e.g., separate figures by metric or dataset) would improve readability.

## Nice-to-Haves

- **Ground-truth calibration on a tractable problem.** Validating against a small synthetic or linear-model setup where the true Rashomon set can be enumerated (e.g., ridge regression where it is an ellipsoid, Eq. 4) would directly answer whether dropout's higher multiplicity estimates are closer to the true values and provide convergence rates. This would address the main evidential gap.

- **Budget-based speed comparison.** Instead of "per-model" speedup (which treats a dependent dropout sample as equivalent to an independent retrained model), a comparison of multiplicity estimate quality vs. total wall-clock time (including pre-training) would more honestly capture the trade-off between speed and sample diversity.

- **Ablation on dropout placement.** The paper could explore dropping out only the last layer vs. all layers, or varying dropout rates by layer depth, as suggested in the future directions section.

## Removed Points

*These points were raised by reviewers but are removed from the main assessment for the reasons stated. Treat them with caution if referenced elsewhere.*

- **Critique that dropout may produce over-estimates (Critic Point 2, part).** The claim that dropout models could "produce over-estimates by including models not truly almost-optimal" is addressed by the paper's methodology: all models are verified against the same loss deviation constraint (line 325). Since both dropout and retraining produce subsets of the same Rashomon set (defined by L(h) ≤ L(h*)+ε), higher estimates logically imply tighter *lower* bounds. The paper does not claim exact estimation, so this specific over-estimation concern does not apply. Removed as factually incorrect regarding the paper's claims.

- **Proposition 1 using bw'* = (1-p)bw* instead of bw*.** The paper explicitly acknowledges this limitation (lines 162–166) and states it is improved in subsequent propositions. Removed because the authors already address it.

- **Speedup per-model being "misleading" due to dependent samples.** The paper acknowledges this limitation (lines 326–327, 372). The per-model speed numbers are literally correct (comparing the time to generate one model). The distinction between dependent and independent samples is a trade-off the paper discusses, not a misrepresentation. Demoted to Nice-to-Have (budget-based comparison) rather than a weakness.

- **Criticism that the dropout limitation is "relegated to a supplement."** The limitation is stated in the main paper's Discussion section (line 372). The appendix provides supplementary experimental evidence, which is standard practice. Removed.

- **Missing related works.** Per the instructions, I cannot assess missing related works without external sources. Removed.

- **Reproducibility concerns about undisclosed hyperparameters.** The paper reports dropout rates (p ∈ [0.0, 0.2], α ∈ [0.0, 0.6]), architecture (single hidden layer, 1k neurons), and number of models (100 per setting). These are adequate for reproducibility. Removed.

- **Formatting/style nitpicks.** Removed per guidelines.

## Novel Insights

The key insight from synthesizing the reviews is a disconnect between the paper's theoretical framework and its strongest evidence. The theory (Propositions 1–4) addresses a narrow question—bounding the probability that a single dropout perturbation stays within a loss budget—but the paper's most compelling claim (dropout explores the Rashomon set *better* than retraining) depends on a different property: the *diversity* of predictions across dropout samples. The empirical evidence for diversity (Figure 1) is actually the stronger contribution, yet it is not supported by the theoretical analysis. This means the paper's novelty rests more on the empirical discovery that dropout-perturbed models span diverse predictions within the Rashomon set than on the theoretical membership bounds. A reviewer reading the theory might overestimate its role in supporting the main claims, while the empirical finding is under-analyzed (no error bars, no ablation, no ground-truth calibration). The paper would be much stronger if it leaned into this empirical result with proper statistical methodology, rather than framing the theory as the primary contribution.

## Suggestions

1. **Pre-specify the quantile or report distributional information for per-sample metrics.** Use a single quantile (e.g., 90th percentile consistently) or show boxplots/confidence bands for VPR and RC, eliminating the "best shows the difference" selection criterion.

2. **Add error bars or confidence intervals** to all multiplicity estimates in Figure 1, bootstrapped over the 100 dropout/retraining samples or across multiple independent runs.

3. **Include MC Dropout as a baseline.** Since MC Dropout (Gal & Ghahramani, 2016) also generates multiple models from a single pre-trained network via inference-time dropout, it is the most natural comparator for the proposed method. A comparison would clarify the advantage of the parameter-controlled approach.

4. **Add an empirical analysis of prediction diversity vs. dropout rate.** Show pairwise model disagreement, variance of output scores, or the span of the empirical Rashomon set as a function of dropout parameters. This would directly address the coverage concern and connect the theory (membership) to the application (multiplicity estimation).

5. **Validate on small-scale ground-truth problem** (e.g., linear model on synthetic data where the Rashomon ellipsoid can be enumerated). Show that dropout's multiplicity estimates converge to the true values, confirming the "higher = better" assumption.
