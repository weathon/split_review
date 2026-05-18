Now I have a thorough understanding of both the paper and the reviewer claims. Let me produce the final consolidated review.

---

## Summary

This paper proposes Behavior-Supported Policy Optimization (BSPO), a method to mitigate reward over-optimization in RLHF by using the next-token distribution of the reward training dataset (the "behavior policy") to detect out-of-distribution (OOD) actions and regularize the value function via a behavior-supported Bellman operator. Theoretically, the operator is proven to be a γ-contraction whose fixed point underestimates OOD actions without affecting ID ones, and policy iteration with it yields monotonic improvement to the optimal behavior-supported policy. Empirically, BSPO consistently achieves higher gold reward across three proxy model scales (774M, 1.1B, 2.7B) while maintaining a lower rate of OOD token generation.

## Strengths

1. **Consistent outperformance across model scales.** Figure 3 shows that across all three proxy model sizes, BSPO achieves the highest gold reward with a sustained upward trend, while all five baselines (PPO, KL-Penalty, CPPO, ENS-UWO, ENS-WCO) exhibit the characteristic plateau-or-decline pattern of reward over-optimization. This is the paper's most direct empirical evidence.

2. **Direct evidence that BSPO suppresses OOD generation during RL.** Figure 4(b) tracks the count of behavior-unsupported actions per response over training. Baselines show a sharp spike in unsupported actions coinciding with over-optimization onset, whereas BSPO maintains a consistently low count. This provides a mechanistic link between the regularization and the improved outcomes.

3. **Rigorous theoretical analysis of the idealized operator.** The paper proves that the behavior-supported Bellman operator is a γ-contraction (Theorem 1), that its fixed point underestimates OOD actions without affecting ID actions (Theorem 2, Corollary 2), and that policy iteration yields monotonic improvement to the optimal behavior-supported policy (Theorem 3). The equivalence of V- and Q-function evaluation under the operator is also established (Corollary 3, Theorem 4). These guarantees are stronger than what existing RLHF reward-regularization methods provide.

4. **Ablation demonstrating advantage over distance-based constraints.** Figure 4(c) compares BSPO with KL-penalty methods at varying coefficients. BSPO avoids over-optimization even at large KL divergence distances, whereas KL-penalty only works within a narrow proximal region. This highlights the value of directly modeling the ID region via behavior policy rather than relying on proxy distance constraints.

5. **Lightweight implementation with single-model architecture.** The ScoreLM model combines reward prediction and behavior distribution prediction in a single architecture (Figure 2a) with accuracy comparable to standard reward models (Figure 2b), adding minimal memory and computational overhead over standard PPO.

## Weaknesses

### Fatal
None.

### Major

1. **The paper does not explain how the binary β(a|s) > 0 condition is realized in practice, creating a critical implementation gap.** The behavior policy β is a neural network (ScoreLM) trained via next-token prediction. With a standard softmax output layer over the vocabulary, β(a|s) is strictly positive for every token in every state, making the condition β(a|s) > 0 always true and the "otherwise" branch of the Bellman operator (Eq. 1 and Eq. 7) unreachable under a literal reading. The paper defines the core mechanism around this binary classification — Definition 1, the Bellman operators, Figure 1(c)'s categorization, and Figure 4(b)'s tracking of "unsupported actions" all depend on it — yet never specifies whether a threshold (e.g., β(a|s) < ε → "unsupported"), logarithm-domain underflow handling, or some other practical approximation is used. This is a significant reproducibility concern: a reader cannot determine from the paper text how the algorithm actually works in practice. The empirical results (Figures 3 and 4b) clearly show BSPO produces different behavior from standard PPO and does track non-zero counts of "unsupported actions," so the method clearly *does* work — but the gap between the theoretical formalism and the implementation is unacknowledged and unexplained. The authors should explicitly describe their practical classification mechanism, justify the threshold if one is used, and discuss whether the theoretical guarantees approximately carry over.

**Why this is Major, not Fatal:** The empirical evidence (Figures 3, 4b, 4c) demonstrates that the method works as intended. The gap is in presentation and documentation, not in the validity of the results. The code is provided in supplementary material. This is fixable with a clear description.

### Minor

1. **The gap between the theoretical analysis (exact policy iteration, exact Bellman operator) and the practical implementation (PPO with clipped surrogate, parameterized critic, single-step value updates) is not discussed.** The contraction and fixed-point theorems apply to the idealized operator, but the actual algorithm uses function approximation and PPO's clipped objective. This gap is standard in the RL literature, but the paper presents the implementation as "theoretically consistent" (Section 4) without acknowledging where approximations might break the guarantees. A brief discussion of the assumptions under which the theory approximately holds would strengthen the paper.

2. **The α hyperparameter balancing reward and language modeling losses in Eq. 5 is not analyzed or justified.** No sensitivity study or selection criterion is provided. Since the quality of the behavior policy β depends on this hyperparameter (a poorly tuned α could harm either the reward prediction or the next-token distribution), this omission weakens the validation.

3. **The win rate figure (Figure 4a) is shown only for the 2.7B proxy model.** The main results (Figure 3) cover all three scales, but the win rate comparison — which directly measures alignment quality — is missing for the 774M and 1.1B settings. These should at least be summarized in a table.

4. **The quality of the next-token predictor (the behavior policy β) on the reward training data and on generated OOD responses is not reported.** The paper evaluates ScoreLM's reward prediction accuracy (Figure 2b) but does not report perplexity or any other metric for the behavior distribution prediction. This makes it difficult to assess whether β provides a reliable characterization of the training data distribution.

5. **The paper does not report total training compute (FLOPs or wall-clock time) for BSPO vs. baselines.** The claim of "negligible additional memory and computational overhead" (Section 4) would benefit from a brief quantitative comparison.

### Trivial
None.

## Nice-to-Haves

- A sensitivity analysis on the (unreported) threshold for classifying actions as "unsupported," if one is used.
- Standard OOD detection metrics (e.g., AUC, false positive rate) for the β-based classifier, comparing against simple baselines such as density estimation on reward model embeddings or ensemble disagreement — this would strengthen the motivation but is not required for the paper's core contribution.
- An ablation that removes the behavior-supported Bellman operator while keeping the ScoreLM training loss (α-weighted language modeling), to isolate whether the value regularization or the auxiliary loss drives the improvement. This is a useful future experiment but not a weakness; the existing ablation (Figure 4c) already compares against KL-penalty with the same ScoreLM reward signal.

## Removed Points

These points were flagged by reviewers but are removed or downgraded for the following reasons:

- **"The algorithm collapses to standard PPO with no OOD penalty" (from Harsh Critic, Claim 1):** Contradicted by the paper's own empirical evidence — Figure 4(b) shows BSPO tracking non-zero counts of "unsupported actions" and behaving differently from PPO. The method clearly implements a practical OOD penalty, even if the paper does not fully document how.
- **"The theory cannot be instantiated as described" (Harsh Critic, Claim 1):** Overstated. The theory defines an idealized operator; the implementation approximates it. This is standard practice. The empirical results confirm the method works. The real issue is the lack of documentation (kept as Major weakness 1).
- **"Behavior policy is never validated as an OOD detector" (Harsh Critic, Claim 2):** Incorrect — Section 3.1 and Figure 1(c) provide validation: supported responses achieve 75.91% proxy-model accuracy vs. 58.10% for unsupported responses. This is a concrete empirical demonstration. Requests for AUC/FPR are nice-to-haves, not missing validation.
- **"Synthetic setup conflates gold reward" (Harsh Critic, Claim 3):** The synthetic gold-model setup is the standard methodology in the reward over-optimization literature (Gao et al., 2023; Coste et al., 2023; Moskovitz et al., 2023). The paper explicitly acknowledges this limitation in Section 6. This is a field-wide constraint, not a paper-specific flaw.
- **"First-method claim is too narrow" (Harsh Critic, Other Observations):** The paper states "the first method that uses value regularization to address reward over-optimization" in the RLHF context, which is a reasonable claim. The paper already notes the connection to offline RL (CQL-style ideas) in the introduction. No change needed.
- **"Gold reward decrease could be catastrophic forgetting" (Harsh Critic, Other Observations):** This is an alternative explanation, not a weakness. The paper provides direct evidence (Figure 4b) linking over-optimization to OOD token generation. The two explanations are not mutually exclusive.

## Novel Insights

None beyond the paper's own contributions. The reviews did not surface a perspective that fundamentally reframes the paper's contribution or reveals an unexpected connection.

## Suggestions

1. **Specify the practical implementation of the binary β-condition.** State explicitly what threshold (e.g., β(a|s) < ε → unsupported, with ε value) or approximation (e.g., log-probability underflow, top-k filtering) is used in the code. If a threshold is used, provide a brief sensitivity analysis showing the method is robust to its choice. This resolves the most critical weakness.

2. **Add a brief paragraph in Section 4 acknowledging the gap between the idealized theoretical analysis and the practical PPO implementation.** State the conditions under which the theoretical guarantees approximately hold (e.g., when the value function approximator is sufficiently expressive, when PPO's clipped surrogate is close to the true objective).

3. **Include a sensitivity analysis or selection criterion for the α hyperparameter** (Eq. 5), and report the perplexity of the ScoreLM's next-token predictor on the reward training data.

4. **Provide the win rate results for all three proxy model scales** (either as a table or additional figures), and include a brief computational cost comparison (FLOPs or wall-clock time) for BSPO vs. baselines.

## Score and Decision

**Originality:** Good. Adapting value regularization from offline RL to the specific RLHF reward over-optimization setting, with a behavior policy defined via next-token distribution, is a solid contribution.

**Importance of research question:** High. Reward over-optimization is a recognized open problem in RLHF alignment.

**Claims support:** Mostly well-supported by empirical results. One significant documentation gap (Major weakness 1) weakens reproducibility but does not invalidate the claims.

**Soundness of experiments:** Good. Three model scales, five competitive baselines, multiple evaluation metrics (gold reward, win rate, unsupported action count, KL divergence). The ablation study (Figure 4c) is informative.

**Clarity of writing:** Generally clear. The theoretical development is well-structured. However, the failure to explain the practical implementation of the binary β-condition is a notable clarity gap.

**Value to research community:** Positive. The method is lightweight and empirically effective. Once the implementation gap is documented, the method can be readily adopted.

The paper presents a well-motivated method with strong theoretical backing and convincing empirical results. The primary weakness is a documentation gap in how the core binary condition is implemented — a significant oversight that affects reproducibility but is fixable. The paper should not be rejected on this basis alone, but the authors must address it before the work is complete.

MY FINAL SCORE: <pineapple>6.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>