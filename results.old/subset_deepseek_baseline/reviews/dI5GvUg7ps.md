## Summary

RewardRank proposes a two-stage learning-to-rank framework that directly optimizes counterfactual user utility rather than relying on heuristic proxy metrics like NDCG. In the first stage, a transformer-based reward model is trained on logged query groups to predict the utility of any item permutation. In the second stage, a ranker is trained end-to-end to maximize this predicted utility using the SoftSort differentiable permutation operator, with a correction term to handle reward misspecification. The authors introduce two reproducible benchmark suites—PO-Eval (parametric oracle on Baidu-ULTR) and LAU-Eval (LLM-as-user on Amazon-KDD-Cup)—and show that RewardRank achieves the highest counterfactual utility on both benchmarks, while also establishing state-of-the-art offline relevance performance on real click data from Baidu-ULTR.

## Strengths

- **Addresses a practically important problem:** The paper convincingly demonstrates that optimizing traditional ranking metrics like NDCG can be sub-optimal for maximizing true user utility, and provides a data-driven method to directly optimize the latter. This is relevant for any system where user engagement or purchase decisions depend on list-level properties beyond simple relevance ordering.
- **Well-motivated and clear framework:** The two-stage approach (learn a reward model from logged interactions, then train a ranker via differentiable sorting) is logically presented, and each design choice—SoftSort, auxiliary per-item loss, misspecification correction—is supported by ablations.
- **Introduces reproducible counterfactual testbeds:** The paper proposes PO-Eval and LAU-Eval, two automated evaluation protocols that fill a gap in the literature where reproducible counterfactual ranking evaluation was largely missing. These testbeds allow researchers to compare methods without costly online A/B tests and with full control over the oracle model.
- **Strong empirical results:** RewardRank outperforms a comprehensive set of baselines (ListNet, ListMLE, LambdaRank, PiRank, URCC*, PG-rank*) on both counterfactual metrics across both testbeds, and achieves new state-of-the-art on real click data from Baidu-ULTR (DCG@5=5.83, DCG@10=8.42). The gains are consistent and statistically significant.
- **Thorough analysis of reward misspecification:** The paper includes an ablation showing that down-weighting poorly calibrated reward predictions (via λ) improves stability and performance, which is a practical contribution for training with learned rewards.

## Weaknesses

### Fatal
None.

### Major
- **Reliance on the logged data distribution for the reward model:** The reward model is trained on logged interactions that come from a specific logging policy. This means the reward model’s predictions are most reliable for permutations similar to those seen in the training data, and may be poorly calibrated for far-out-of-distribution permutations. While the misspecification correction helps, the paper does not analyze how the reward model’s accuracy degrades as the ranker’s policy deviates from the logging distribution. This is a fundamental challenge in offline policy learning and could limit the approach’s practical generalization.
- **SoftSort differentiability assumption:** The paper uses SoftSort to obtain differentiable permutation matrices, but the definition in Eq. (8) depends on the hard ranking $\hat{\pi}(k)$ (the k-th ranked item according to the scores). The hard sorting operation is non-differentiable; the gradient through SoftSort is only an approximation that treats the sorted order as fixed for the forward pass. The paper does not discuss this approximation or its potential impact on training stability and convergence. A minor clarification would strengthen the technical presentation.

### Minor
- **Baseline construction for URCC* and PG-rank\***: These variants replace the original utility (e.g., NDCG) with the same transformer-based reward model used by RewardRank, which makes them less faithful to the original methods. The paper includes standard LTR baselines (ListNet, etc.) that do not use the reward model, so the comparison is still informative, but the label “URCC*” / “PG-rank*” could be confusing. A clearer statement that these are *reward-enhanced* versions of the original methods would help.
- **Computational cost:** The transformer backbone with 12 layers and 110M parameters plus the soft permutation computations may be expensive. The paper does not report training time, inference cost, or memory usage, which would be useful for practitioners assessing scalability.

### Trivial
- The caption of Figure 2 is repetitive and contains garbled text (likely an OCR artifact). This does not affect the scientific content.

## Nice-to-Haves
- Analysis of how the reward model’s prediction error changes as the ranker’s output distribution diverges from the logging distribution (e.g., via empirical KL divergence or distribution shift metrics).
- Comparison with a simpler reward model (e.g., a linear model or an MLP) to isolate the benefit of the transformer for permutation-aware utility modeling.
- Discussion of the temperature τ annealing schedule, if any was used during training.

## Novel Insights

Beyond the paper’s own contributions, a key observation is that even state-of-the-art listwise ranking methods (PiRank) achieve high NDCG but fail to improve true user utility (purchase/click rate) by a meaningful margin. This reinforces the idea that offline ranking metrics, while useful as surrogates, can mask misalignment with the actual behavioral objective. The paper shows that directly optimizing a learned counterfactual reward—even when that reward is itself imperfect—can yield better alignment than optimizing a handcrafted metric. The two evaluation protocols (PO-Eval and LAU-Eval) also provide a template for testing counterfactual ranking methods under controlled yet realistic conditions.

## Suggestions

- Clarify how the gradient of SoftSort is computed given that the hard sorting operation is non-differentiable. Provide a short derivation or reference to the standard practice (e.g., using the straight-through estimator or treating the sorted order as fixed for backpropagation).
- Discuss the risk of reward model exploitation when the ranker produces rankings far from the training distribution, and whether any additional regularization (e.g., KL control) was considered.
- Include training time and GPU memory comparisons for the main methods in the appendix to help readers assess computational requirements.

## Score and Decision

**Score:** 8.0  
**Decision:** Accept  

The paper tackles a relevant and timely problem, proposes a well-designed framework with clear components, contributes two valuable reproducible testbeds, and provides strong empirical support across multiple settings. The weaknesses are minor relative to the overall quality and contribution. I recommend acceptance.

MY FINAL SCORE: <score>8.0</score>
MY FINAL DECISION: <decision>Accept</decision>