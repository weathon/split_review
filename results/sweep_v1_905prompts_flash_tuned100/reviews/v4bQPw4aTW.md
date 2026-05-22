Now I have enough calibration anchors to finalize. Let me synthesize the review.

## Round 1 Bracket
Based on the calibration search:
- **Weak anchors** (avg 2.5–3.4): rejected papers on unrelated LM alignment topics → AdaBoN is clearly stronger
- **Middle anchors** (avg 4.25–6.5): includes Damani et al. (6.5, same problem) and Inference-Aware FT for BoN (5.67, related) → AdaBoN is comparable to weaker than Damani et al. but not as weak as some of the lower-middle anchors
- **Strong anchors** (avg 8.0+): papers on different topics (SPA, FlexPrefill, SMC generation) → AdaBoN is clearly below these

**Initial bracket**: [4.0, 6.5]

## Round 2 — Narrowing

The most directly relevant anchor is **Damani et al. (6.5)** which addresses the exact same problem. AdaBoN shares the same core weakness (no/weak adaptive baselines) that was noted in Damani et al.'s reviews. However, Damani et al. reports stronger results (up to 50% compute reduction) across more diverse domains. AdaBoN's results are more modest (BWR 0.54–0.62), and it lacks latency measurements despite claiming latency as a key advantage. The **Inference-Aware Fine-Tuning for BoN (5.67)** is another relevant anchor — it also had limited baselines and was accepted.

Comparing AdaBoN to Damani et al. (6.5): AdaBoN is weaker in terms of empirical effect size, lacks adaptive baselines that Damani et al. at least partially included (random allocation), and makes unsupported latency claims. Comparing to the 5.67 anchor: AdaBoN has broader evaluation (more LM-RM pairs, more datasets) but a weaker core evidential case.

**Final score**: 5.0 — borderline between weak accept and reject. The paper has a clear, simple method and extensive evaluation, but the missing adaptive baselines and modest effect sizes prevent it from being a strong acceptance. The paper is comparable to lower-scoring accepted papers, but the evidential gaps are structural.

## Review

## Summary

This paper proposes AdaBoN, a two-stage adaptive allocation strategy for Best-of-N alignment. Given a batch of K prompts and a total inference budget BK, AdaBoN first uses a small exploration budget (d samples per prompt) to estimate each prompt's reward distribution via Gaussian KDE, then greedily allocates the remaining budget across prompts based on estimated marginal gains from additional sampling. The method is evaluated on 12 LM-RM pairs across three datasets (AlpacaEval, HH-RLHF, PKU-SafeRLHF) using two proposed metrics: Batch Win Rate (BWR) and Expected Survival Time (EST).

## Strengths

1. **Training-free, model-agnostic design.** Unlike Damani et al. (2024), AdaBoN requires no auxiliary model training — it works out-of-the-box with any LM-RM combination and any per-prompt budget. This is a genuine practical advantage for deployment.

2. **Extensive and systematic evaluation.** The paper evaluates AdaBoN across 12 LM-RM pairs, 3 datasets, and 50 distinct batches per setting (Section 4.1). Table 1 and Table 2b show that AdaBoN achieves median BWRs of 0.54–0.62, with over 75% of batches exceeding 0.50 for all pairs. The Qwen-Mistral pair achieves 100% of batches above BWR > 0.50. This breadth makes the empirical claims more robust than prior work.

3. **Consistent improvement vs. uniform allocation demonstrated via EST.** The EST metric (Table 2a) shows median values of ~150 for B=120, indicating AdaBoN competes with uniform allocations using ~25% larger per-prompt budgets. This provides a concrete sense of the computational savings.

4. **Ablation on batch size and budget.** The paper shows (Figure 3, Appendix K) that AdaBoN's advantage grows with batch size K and is robust across different inference budgets B, which strengthens the case for the method's practical utility.

5. **Clean theoretical grounding.** Proposition 3.1 proves concavity and monotonicity of the expected-max function, justifying the greedy allocation as optimal under true expectations. While this is a standard result, its explicit statement is useful for the paper's self-containedness.

## Weaknesses

### Major

1. **No comparison against any adaptive baseline.** The paper compares AdaBoN only against uniform allocation (the minimax optimal non-adaptive policy). While the authors explain that the primary prior work (Damani et al., 2024) is not directly comparable due to different regimes and computational cost, the evaluation would benefit enormously from even a simple adaptive heuristic — e.g., "allocate all remaining budget to the prompt with the highest observed max reward" or "Thompson-sampling-like allocation based on the exploration phase." Without any adaptive baseline, the paper cannot demonstrate that its specific design choices (KDE, greedy marginal-gain allocation) are meaningful — it only shows that *any* adaptive strategy can beat uniform. This is a structural gap that limits the paper's contribution from "a useful method" to "evidence that adaptivity helps, which is already known."

2. **Latency claims are unsupported by any measurement.** The paper repeatedly emphasizes that AdaBoN minimizes latency because it needs only two sequential LM calls (Section 3, Abstract). However, no latency measurements are reported anywhere. The method involves fitting KDEs and running Monte Carlo simulations with m=1024 samples per marginal gain estimate (Algorithm 2, Line 3), which adds non-trivial compute overhead. Without actual runtime data, the latency advantage is asserted, not demonstrated.

### Minor

3. **Modest effect size and limited adaptivity.** Median BWRs of 0.54–0.62 represent a 4–12% win over a coin flip. With d=0.75B (90 out of 120 samples per prompt used for exploration), only 25% of the total budget (150 out of 600 samples) is actually subject to adaptive allocation. It is unclear whether the gains come primarily from the KDE-based greedy allocation or simply from the exploration phase serving as a non-uniform allocation mechanism. Experiments with smaller d (e.g., 0.5B) would clarify this.

4. **BWR interpretation and reward-scale sensitivity.** The BWR aggregates *summed* max-rewards across prompts with potentially different reward scales (as noted in Section 4.2, reward values are "only meaningful comparatively"). If one prompt's rewards are systematically higher in scale than another's, the allocation that benefits that prompt will mechanically win more often — BWR could partially reflect scale differences rather than genuine difficulty differences. The paper discusses this concern but does not address it (e.g., by per-prompt normalization or rank-based aggregation).

5. **EST truncation and interpretation.** The paper truncates the infinite sum in Equation 5 to 2B (Section 4.3) but does not discuss the truncation bias. The EST values (~150 for B=120) are interpreted as "competitive against 20-25% larger budgets," but this interpretation assumes uniform allocation performance scales linearly with N, which it does not (it's concave in N by Proposition 3.1). The EST is a useful heuristic but its translation to "equivalent budget" is imprecise.

6. **No statistical significance testing.** BWR values are reported as median [Q1, Q3] over 50 batches, but the paper does not test whether these are significantly above 0.50 (e.g., signed-rank test) or report confidence intervals around the median. Given the modest effect sizes, this would help gauge reliability.

### Trivial

7. The paper states "20% larger inference budgets" (Abstract) when EST ~150 vs. B=120 is actually 25% larger (150/120 = 1.25). Minor imprecision.
8. Proposition 3.1 is a standard known fact about order statistics — the framing as a contribution is slightly overclaimed.

## Nice-to-Haves

- Report the actual expected cumulative reward (Equation 1) directly, not just win rates. This would let readers assess the absolute impact.
- Ablate the Monte Carlo sample size m=1024 to test sensitivity.
- Validate the KDE fit quantitatively (e.g., hold-out log-likelihood) across LM-RM pairs beyond the visual inspection in Figure 1.
- Add simple adaptive heuristics as baselines (highest-observed-max heuristic, variance-based allocation).

## Removed Points

- **"No theoretical analysis beyond Proposition 3.1"**: The paper's contribution is primarily empirical/methodological, and theoretical regret bounds are not standard for this type of empirical systems contribution. Demanding a regret bound is scope creep.
- **"The KDE validation is only visual"**: The paper notes in Section 3.1 that they tried Gaussian and Skew-Normal MLE and found KDE performed better (Table 16, Appendix K.3). While a quantitative comparison would strengthen the paper, claiming this is an "evidential gap" overstates the issue.
- **"BWR metric is not adequately validated"**: The paper explicitly justifies BWR over expected cumulative reward due to RM score scale issues (Section 4.2). The critic's concern about inter-prompt scale differences conflates the task objective (maximize sum of max-rewards) with a metric deficiency. Both AdaBoN and uniform allocation are evaluated on the same draws; the comparison is fair.
- **"The exploration budget d tuning grid is coarse"**: The paper shows at most 0.03 BWR variation across d ∈ {0.6, 0.7, 0.75, 0.8}B and recommends d=0.75B. This is adequate for the purpose.

## Novel Insights

The most interesting observation from the reviews is that the core evidential challenge for adaptive compute-allocation papers is consistent across both this work and the prior Damani et al. paper: **demonstrating that the specific sophisticated mechanism matters more than simple adaptive heuristics**. Both papers were criticized for weak baselines, yet both papers present different mechanisms (trained predictor vs. test-time KDE). This suggests the field needs a standardized set of adaptive baselines (e.g., highest-reward heuristic, variance-guided allocation) before any specific method can claim superiority. A second observation: the regime distinction this paper draws (small batch, large budget) is genuinely underexplored, and the training-free approach is a practical differentiator, but the paper does not fully exploit this advantage by showing *where* training-free estimation actually outperforms a trained predictor.

## Suggestions

1. **Add at least one simple adaptive baseline.** The highest-leverage experiment is to compare AdaBoN against a "greedy heuristic" that, after exploration, allocates all remaining budget to the prompt(s) with the highest observed maximum reward so far. This directly tests whether the KDE-based marginal-gain computation is beneficial. If AdaBoN outperforms this heuristic, the paper's claims are substantially stronger; if not, the paper still makes a contribution by showing that simple heuristics are sufficient.

2. **Report actual runtime/latency numbers.** Since latency minimization is a stated motivation, measure and report the end-to-end time for AdaBoN's exploration + KDE fitting + Monte Carlo + allocation vs. uniform allocation, broken down by component.

## Score and Decision

**Score**: 5.0  
**Decision**: Borderline. The paper has a clear contribution (training-free adaptive BoN allocation with broad evaluation) but is held back by structural evidential gaps — primarily the complete absence of adaptive baselines and unsupported latency claims — that prevent a strong acceptance. The paper's central claim (AdaBoN consistently outperforms uniform allocation) is supported, but whether the *specific method* design matters more than any simple adaptive heuristic remains unanswered.

## Anchors Used for Calibration

| Paper | Avg Score | Round | Comparison |
|-------|-----------|-------|------------|
| Learning How Hard to Think (Damani et al.) | 6.5 | R1, R2 | Same problem; stronger results, more domains, but shares weak-baseline issue. AdaBoN is weaker overall. |
| Inference-Aware Fine-Tuning for BoN | 5.67 | R1, R2 | Related topic; limited evaluation (1 model, 1 task). AdaBoN has broader evaluation but weaker core evidence. |
| Inference Scaling Laws | 5.75 | R1, R2 | Different topic (compute-optimal inference, not adaptive allocation). AdaBoN is comparable in strength. |
| Adaptive Data Optimization | 5.5 | R2 | Different topic. AdaBoN is comparable. |
| Prompt Optimization with Human Feedback | 4.6 | R2 | Different topic, rejected. AdaBoN is stronger. |
| Multi-Objective ORPO Alignment | 3.4 | R1 | Different topic, rejected. AdaBoN is clearly stronger. |
| Decoding-Free Candidate Selection | 3.0 | R1 | Different topic, rejected. AdaBoN is stronger. |
| Efficiently Deploying LLMs | 3.0 | R1 | Different topic, rejected. AdaBoN is stronger. |

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>