Now I have all the calibration information. Let me write the final consolidated review.

## Summary of Calibration Anchors

**Round 1 (Bracketing):** Weak anchors (avg ~3.0) were papers on sampling/decoding that were clearly weaker than AdaBoN. Middle anchors (avg 5.0–6.5) contained the most relevant comparisons. Strong anchors (avg 8.0) were papers on different topics (diffusion models, precision scaling) — AdaBoN is not in that tier.

**Round 2 (Narrowing):** The key comparison is Damani et al. "Learning How Hard to Think" (6.50, Accepted, scores 6,8,6,6) — the direct prior work on the same problem. AdaBoN is slightly weaker due to the exploration-budget framing issue and modest gains, but has broader evaluation and no-training advantage. Against Inference-Aware Fine-Tuning for BoN (5.67, Accepted), AdaBoN is stronger. Against Inference Scaling Laws (5.75, Accepted), AdaBoN is comparable. Against Large Language Monkeys (5.00, Rejected), AdaBoN is clearly stronger.

**Final score:** 5.5, positioned below Damani (6.50) but above Large Language Monkeys (5.00), comparable to Inference-Aware Fine-Tuning (5.67) and Inference Scaling Laws (5.75).

---

## Summary

AdaBoN proposes a two-stage adaptive allocation strategy for Best-of-N inference-time alignment. Given a batch of prompts and a fixed inference budget, the method first spends an exploration phase (d samples per prompt) to estimate each prompt's reward distribution via Gaussian KDE, then greedily allocates the remaining budget to prompts with the largest estimated marginal gains. The method is evaluated across 12 LM-RM pairs, 3 datasets, and 50 batches, showing median Batch Win Rates of 0.54–0.62 against uniform allocation.

## Strengths

1. **Test-time-only operation, no auxiliary model training**: Unlike the most directly related prior work (Damani et al., 2024), AdaBoN requires no per-LM-RM-pair training. The paper concretely demonstrates the practical significance: for their experimental scope (12 LM-RM pairs, 3 datasets, K=5, B=120), the competing method would need to train 216,000 separate MLPs (Section 4.2). AdaBoN works out-of-the-box for any LM-RM combination (Section 3).

2. **Principled justification for greedy allocation**: Proposition 3.1 proves that the expected maximum reward is concave and monotonically increasing in the number of samples for any distribution with finite first moment. This guarantees that the greedy algorithm (Algorithm 1) is optimal for the subproblem of allocating the remaining budget given estimated value functions, by the result of Federgruen and Groenevelt (1986).

3. **Broad evaluation with careful statistical design**: The experiments cover 12 LM-RM pairs (4 LMs × 3 RMs) across 3 datasets with 50 independently sampled batches each (Section 4.1). The paper explicitly notes that Damani et al. (2024) — the only prior work on the same allocation problem — evaluates on "a single LM, a single RM, and a single batch of prompts" for real-valued rewards. The 50-batch design with quartile-based reporting provides a meaningful assessment of variability.

4. **Well-motivated evaluation metrics (BWR and EST)**: The Batch Win Rate avoids relying on absolute reward values — which the paper correctly notes are often arbitrary logits — by measuring pairwise comparisons against the uniform baseline (Section 4.2). The Expected Survival Time quantifies how much larger a uniform budget AdaBoN competes with, giving an interpretable measure of computational savings.

5. **Gaussian KDE with Scott's rule works robustly without per-pair tuning**: The paper shows that a single automatic bandwidth selection rule suffices across all 12 LM-RM pairs (Section 4.3). They additionally report that two alternative estimators (Gaussian MLE, Skew-Normal MLE) perform worse (Table 16, Appendix K.3), providing evidence that the simplicity of KDE is not leaving performance on the table.

## Weaknesses

### Fatal
None.

### Major

1. **The exploration budget is not "small" — 75% of the total budget is spent uniformly, which undermines the adaptive framing.** The abstract describes "a small exploration budget" and Contribution (2) states the method "use[s] a small exploration budget." However, the primary experimental configuration uses d = 0.75B: 75% of the total budget (450 of 600 samples for K=5, B=120) is allocated uniformly as exploration, with only the remaining 25% allocated adaptively. Characterizing 75% as "small" is misleading. The ablation over d ∈ {0.60B, 0.70B, 0.75B, 0.80B} (Appendix G.1) is limited to a narrow window of large values and never tests genuinely small exploration budgets (e.g., d=0.1B or d=0.2B) that would more convincingly demonstrate adaptivity. The paper's framing should be adjusted to acknowledge that the method is primarily uniform allocation with a modest adaptive tail.

### Minor

2. **No empirical comparison with the directly prior work (Damani et al., 2024).** The paper studies the same resource-allocation problem and offers clear differentiators (no auxiliary training, different regime, broader empirical study), but provides no direct empirical comparison. The reasons given — lack of available implementation and the computational cost of training 216,000 MLPs — are acknowledged transparently (Section 4.2). While the cost argument is reasonable for a full-scale reproduction, a smaller-scale comparison (e.g., 1–2 LM-RM pairs, a single B value, a single batch) would have grounded the claimed advantages. The paper does not attempt such a comparison.

3. **No latency measurement despite latency being stated as a primary motivation for the two-stage design.** The paper repeatedly motivates the two-stage structure by latency concerns (Section 1: "Motivated by latency concerns"; Section 2.3: "Our focus on two-stage policies is motivated by latency concerns"; Section 3: "AdaBoN minimizes latency"). Yet nowhere is latency actually measured or compared. The claim that the two-stage design minimizes latency relative to more adaptive (e.g., bandit-style) policies is a qualitative structural argument, not an empirical finding. While the structural argument about parallelization is reasonable, the gap between motivation and evidence is notable.

4. **Improvements over the uniform baseline are modest.** The median BWRs across 12 LM-RM pairs range from 0.54 to 0.62 (Table 1), meaning AdaBoN beats the uniform baseline roughly 54–62% of the time. The percentage of batches with BWR > 0.50 ranges from 76% to 100% (Table 2b), meaning in the worst case nearly a quarter of batches perform worse. The EST values (~148–156 for B=120) indicate competitiveness with uniform allocations at 23–30% larger budgets. These are real but mild gains. The paper's prose ("consistently and often significantly outperforms," "striking") somewhat inflates the practical significance of these numbers.

### Trivial

5. **The Bernoulli example in Section 2.3 uses binary rewards** whereas the paper's actual setting uses continuous rewards. While purely pedagogical, the benefit of adaptivity is easier to demonstrate with binary rewards (where a single positive sample saturates the max) than with continuous rewards (where additional samples always improve the max, albeit with diminishing returns). This does not affect the paper's core claims.

## Nice-to-Haves

- Test the method with genuinely small exploration budgets (e.g., d=0.1B, d=0.2B) to convincingly demonstrate adaptivity.
- Report wall-clock latency or throughput comparisons to substantiate the latency motivation.
- Add a small-scale comparison with Damani et al. (2024), even on a single LM-RM pair and a single batch.
- Ablate the Monte Carlo sample size m (currently m=1024) to show sensitivity to this parameter.
- Report actual expected cumulative rewards in addition to BWR to give a sense of absolute magnitude.

## Removed Points

These points are flagged to be removed — treat them with caution.

- **"No evidence that K=5, B=120 corresponds to actual deployment patterns"** (Harsh Critic): Speculative. The paper states its assumed regime and provides a plausible motivation (on-device inference). Asking for evidence that this corresponds to real-world deployments is outside the paper's scope.
- **"Models are 7-8B, not obviously small on-device models"** (Harsh Critic): The paper describes the regime as "relevant for personalized on-device inference" — a forward-looking motivation, not a claim about the specific models used.
- **"Default decoding strategy not specified"** (Harsh Critic): The paper states it uses "the default decoding strategy from Hugging Face" (Section 4.3). This is sufficient for reproducibility.
- **"No statistical significance testing"** (Harsh Critic): The paper reports quartile-based distributions across 50 batches, which is a standard and informative way to present variability. Formal hypothesis testing would be a nice addition but is not a weakness.
- **"No ablation of Monte Carlo sample size m"** (Harsh Critic): Would strengthen the paper but is not a core flaw.
- **"No analysis of dependence on number of reward distribution modes"** (Harsh Critic): Scope creep beyond the paper's stated contribution.
- **"Claim about any LM-RM combination is too broad"** (Harsh Critic): The paper says "compatible with any LM-RM combination" referring to the method's plug-and-play nature (no retraining), not that it has been tested on every possible combination. The limitation is partially acknowledged in Section 5.

## Novel Insights

None beyond the paper's own contributions. The core empirical finding — that reward distributions for popular LM-RM pairs are smooth and learnable from modest samples, enabling competitive two-stage allocation without training — is the paper's own contribution, not something surfaced by the reviews. The reviews primarily surface framing issues and missing comparisons.

## Suggestions

1. Revise the "small exploration budget" framing throughout the paper. Either test genuinely small d values (e.g., d=0.1B, d=0.2B) or describe the method as using a "moderate" exploration budget with a "modest adaptive tail."
2. Add latency measurements if the latency claim is to remain central; otherwise, downgrade the latency motivation to a design rationale without empirical claims.
3. Attempt a small-scale comparison with Damani et al. (2024) on a single configuration to provide empirical grounding for the claimed advantages.
4. Tone down language that overstates the practical significance of the gains (e.g., "striking," "consistently and often significantly outperforms").

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Accept</decision>