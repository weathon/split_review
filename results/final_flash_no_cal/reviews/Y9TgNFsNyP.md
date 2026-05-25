Now I'll produce the final consolidated review.

## Summary

This paper introduces FF-Erase, the first machine unlearning framework designed specifically for Forward-Forward (FF) models. It identifies two key challenges that cause conventional gradient-ascent unlearning to fail on FF models — sensitivity to parameter tuning and layer-wise independent training — and addresses them with a goodness-guided strategy that uses a separate guidance model to stabilize layer-wise updates. The paper also proposes G-MIA, a membership inference attack that leverages per-layer goodness scores to verify unlearning effectiveness. Experiments on image classification benchmarks (CIFAR-10/100, MNIST, Fashion-MNIST) across three architectures (TinyCNN, AlexNet, VGG13) show that FF-Erase achieves unlearning effectiveness comparable to retraining from scratch while being 1.9–3.1× faster.

## Strengths

- **First machine unlearning method for Forward-Forward models.** The paper identifies a genuinely new problem — unlearning in FF models — and articulates why conventional methods (gradient ascent) are not feasible due to FF's BP-free, layer-wise independent training. This fills a clear gap in the literature as FF models gain traction. Experimental evidence in §6.3 (Fig. 5) confirms that GA either causes model collapse (λ ≥ 10⁻¹) or fails to forget (λ ≤ 10⁻²), supporting the motivation.

- **Well-designed unlearning approach with strong empirical validation.** FF-Erase's guidance-model strategy is principled: the guidance model provides stable target goodness distributions for the forgetting forward, while the recovering forward maintains utility on remaining data. The ablation study (Table 1) systematically maps the efficiency–effectiveness trade-off across 10 guidance-model configurations, including a "random guidance" ablation (R.G.M.) that catastrophically degrades performance (Acc_t = 55.53%), cleanly demonstrating the necessity of a stable, informed guidance model.

- **Thorough evaluation across diverse settings.** Experiments span 4 datasets (CIFAR-10/100, MNIST, Fashion-MNIST), 3 FF architectures (TinyCNN, AlexNet, VGG13), and two FF algorithms (CwComp, Deeperforward). The main unlearning result (Fig. 4) shows FF-Erase achieving a G-MIA score of 0.5245–0.5260 (retraining: 0.532) at 29–39% of the retraining time, supporting both effectiveness and efficiency claims.

- **Novel verification tool.** G-MIA provides a way to quantitatively verify unlearning in FF models using goodness signals, outperforming the black-box FL baseline across all settings and matching/exceeding white-box methods (GR, GAP, ST) on deeper networks (VGG13, CIFAR-100). This is a useful contribution even after accounting for the access-level terminology issue.

## Weaknesses

### Major

None.

### Minor

- **G-MIA's "black-box" classification is imprecise and inconsistent with the paper's own definitions.** The paper defines black-box MIAs as using "only the model's final prediction output" (§2) but G-MIA requires per-layer goodness vectors. While goodness vectors are a natural output of FF forward passes (rather than model parameters or gradients), claiming "strict black-box constraint" (§2) is over-reaching. The paper should relabel G-MIA as a "gray-box" or "goodness-based" attack and explicitly state the access assumption (the attacker obtains per-layer goodness scores during inference). This correction would not diminish the technical contribution.

- **No variance estimates or confidence intervals for main results.** The core experiments (Table 1, Figures 4–5) are reported as point estimates with no indication of variability across runs. Given stochasticity in training, data splits, and the random sampling of forgetting data (20% of training data), reporting results over multiple seeds (e.g., 3–5 runs) would substantially strengthen confidence in the findings.

- **Hyperparameter selection for early stopping is underspecified.** The termination thresholds ε₁ and ε₂ are listed in Algorithm 1 and described in §4.1, but the paper gives no concrete values, tuning procedure, or sensitivity analysis. Similarly, the recovery frequency K is described only as "empirical" (§4.1) with no ablation or guidance on how it should be set for different datasets. This limits reproducibility.

- **G-MIA's dependence on shadow model quality is not discussed.** The attack (§5) requires training shadow models on synthetic data generated via model inversion. The paper does not analyze how the quality of this synthetic data affects attack accuracy, nor does it discuss cases where model inversion may produce poor-quality training data for the shadow models. Since the comparison methods (GR, GAP, ST) do not require shadow models, this asymmetry deserves explicit acknowledgment.

- **The paper contains one factual inconsistency in Table 1's discussion.** The text (§6.4) states "the Acc_f drops to 55.53%" for R.G.M., but Table 1 shows Acc_f = 51.18% and Acc_t = 55.53%. The referenced value matches Acc_t, not Acc_f. This should be corrected.

### Trivial

- The paper does not discuss limitations (e.g., restriction to image classification, the per-class goodness assumption) despite claiming extensive evaluation. A brief limitations paragraph would improve framing.
- Figure captions in the main text are duplicated (e.g., the same caption appears twice for Figures 1, 2, 3, 4). This appears to be a formatting artifact.

## Nice-to-Haves

- **Additional unlearning baselines.** The paper compares only against GA and retraining. While the claim that existing BP-based methods are infeasible is conceptually argued and supported by GA's failure, the evaluation would be strengthened by showing that other approximate unlearning approaches (e.g., influence-function-based methods adapted to FF) also fail or require non-trivial modification.
- **Broader task domains.** The method is tested only on image classification. A discussion of how FF-Erase might transfer to other FF application domains (graphs, text, recurrent architectures) would improve generality.

## Removed Points

These points were raised by one or both reviewers but filtered out after verification against the paper:

1. **"Insufficient baseline comparison: distillation-based unlearning should be added."** The paper already evaluates a randomly-initialized guidance model (R.G.M.) which serves as an ablation for what happens when the guidance signal is poor — the closest analogue to a "distillation from incompetent teacher" baseline. The critic's suggestion is speculative about whether such methods could be adapted to FF; the paper's claim is that *existing BP-based methods as designed* are infeasible, which GA's failure demonstrates. This criticism is not grounded in a concrete flaw in the paper.

2. **"The paper should evaluate on non-image tasks."** This is scope creep. The paper clearly scopes to image classification (consistent with prior FF literature) and evaluates on 4 standard benchmarks across 3 architectures. Extending to other modalities is future work, not a required component of the current contribution.

3. **"Potential circularity: G-MIA uses the same goodness distributions FF-Erase manipulates."** The paper reports both G-MIA scores and accuracy on the forget set as independent signals, partially addressing this concern. This is a generic concern that would apply to any verification method tied to the model's outputs and does not constitute a specific weakness.

## Novel Insights

None beyond the paper's own contributions. The key insight — that FF models' layer-wise independence and sensitivity to parameter tuning make conventional GA unlearning fail, and that a guidance model providing stable goodness targets can enable effective unlearning — is well articulated by the paper itself.

## Suggestions

1. **Clarify G-MIA's threat model.** Rename G-MIA from "black-box" to "goodness-based" or "gray-box" MIA, and explicitly state the attacker's capability: per-layer goodness vectors are accessible (e.g., when the model is deployed on client devices or when an API exposes intermediate representations). Discuss scenarios where such access is and is not realistic.

2. **Add variance estimates.** Report results from multiple runs (3–5 seeds) for the main experiments (Table 1, Figures 4–5), or at minimum note the absence of such estimates as a limitation.

3. **Provide concrete values or tuning guidance for ε₁, ε₂, and K** used in the reported experiments, and ideally include a small sensitivity analysis for the most critical hyperparameter (K).

4. **Correct the Table 1 textual error** where Acc_f is referenced but Acc_t value is quoted (55.53% vs 51.18%).

5. **Add a limitations paragraph** discussing the scope (image classification, per-class goodness assumption, shadow model dependency) and potential avenues for future work.

## Score and Decision

The paper makes a clear, original contribution — it is the first to tackle machine unlearning for Forward-Forward models — and supports it with thorough experimentation. The main issue (G-MIA terminology) is fixable and does not undermine the core contribution. The paper would benefit from variance reporting and hyperparameter clarification but these are standard minor improvements, not structural flaws.

MY FINAL SCORE: <score>7.5</score>
MY FINAL DECISION: <decision>Accept</decision>