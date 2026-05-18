Now I have a thorough understanding of the paper and all the reviewer claims. Let me write the final consolidated review.

## Summary

This paper proposes NeuralPES, a deep-ensemble-based algorithm for non-stationary contextual bandits. The core idea is to combine (a) an ensemble of reward models, (b) a sequence model that predicts future reward model weights, and (c) a predictive model that uses those predicted weights to estimate rewards — with the aim of prioritizing exploration toward information that remains useful beyond a single timestep. The paper provides theoretical analysis of an idealized linear version (LinPS) and evaluates NeuralPES on a synthetic AR(1) logistic bandit and two real-world recommendation datasets (MIND, KuaiRec), showing statistically significant improvements over neural bandit baselines.

## Strengths

- **Novel and well-motivated algorithm design.** NeuralPES is, to my knowledge, the first algorithm that jointly achieves neural-network scalability and exploration that targets "lasting information" in non-stationary environments. The architecture — combining reward models, sequence models that predict future weights, and predictive models that gate which information propagates — is a thoughtful integration of ideas from ensemble sampling and predictive sampling. The paper clearly explains why each component is needed.

- **Consistent and significant empirical outperformance on real-world data.** Table 1 shows NeuralPES achieving the highest average reward/CTR/rating across all three experiments with non-overlapping confidence intervals (e.g., 0.1552±0.0013 vs. next-best 0.1513±0.0012 on MIND; 1.3421±0.0016 vs. 1.3172±0.0023 on KuaiRec). Figures 2b–2d confirm this advantage holds over the entire time horizon, not just at the endpoint. These experiments preserve temporal order, directly testing natural non-stationarity (e.g., day-of-week patterns in MIND).

- **Ablation studies validate the key components.** Figure 2e shows that removing the predictive model ("Neural Sequence Ensemble") causes performance to collapse, and that regularization for continual learning (Eq. 4) consistently improves results. This provides direct empirical support for the two main design choices.

- **Realistic evaluation setup.** The MIND experiment feeds data in chronological order over 1 week and visualizes day-of-week CTR patterns; the KuaiRec experiment uses 12-hour windows over 2 months. This directly tests performance under natural, pronounced non-stationarity rather than relying solely on synthetic shifts.

## Weaknesses

### Major

None. The algorithm specification issues are concrete but fixable, and none invalidates the paper's core claims.

### Minor

1. **Pseudocode/text inconsistency in action selection (Algorithm 4, line 266).** The text description (Section 4.3, step 3) clearly states: sample a single particle *m*, use the *m*-th predictive model, and pick the action maximizing that model's output. However, the pseudocode sums over *all* predictive models `i = 1 to M` while using the predicted weights and base features only from the sampled particle *m*:
   ```
   A_t ∈ argmax_{a ∈ A_t} Σ_{i=1}^M f^{pred}(w^{pred}_{i,t}; (ŵ_{m,t+2} ⊙ b(ψ_m; C_t, a)))
   ```
   This is a concrete inconsistency that prevents unambiguous re-implementation. The authors should align the pseudocode with the text description (or explain if the aggregation is intentional).

2. **Sequence model trained one-step-ahead, used two-steps-ahead without explanation.** The sequence model is trained via Eq. 6 to predict w_{m,j+1} from w_{m,j-L+1:j}. During inference (Algorithm 4, rollout), it is directly asked to produce ŵ_{m,t+2}. The parameter `x=2` is passed to `TrainSequenceNN` but never appears in the training objective (Eq. 6 always targets the immediate next step). If the model is meant to be applied recursively for two steps, this is not stated or implemented in the pseudocode. If a direct two-step prediction is intended, the training objective must match. This needs clarification.

3. **Predictive model training data provenance.** The predictive model is trained using w_{m,j+2} (Eq. 8) as part of its input. The replay buffer stores (c, a, r, j) tuples. The algorithm passes historical weights w_{m,1:t-1} as a separate argument to `TrainPredictiveNN`, making this feasible via a lookup table, but the paper does not explain this mechanism. The memory cost of storing per-timestep per-particle weights (O(MK), which is modest) should be stated for completeness and reproducibility.

4. **Sliding window baselines are underspecified.** The paper compares against "sliding window versions" of Neural Ensemble, Neural LinUCB, and Neural Linear but does not specify the window size used, how it was chosen, or whether it was tuned per baseline or per dataset. This is a standard experimental detail that should be provided. The current level of description makes the comparison difficult to reproduce.

5. **Theory-algorithm gap.** The theoretical analysis (Section 4.4) studies LinPS, an idealized linear version with known features φ, fixed action sets, and known posterior structure. The paper acknowledges this provides "intuition and evidence" for NeuralPES and describes how each neural component approximates its LinPS counterpart (e.g., base networks ≈ posterior over φ, sequence models ≈ posterior over θ_{t+2}). However, no analysis or empirical diagnostic is given to verify that the approximation preserves the "lasting information" property. This is a common and often acceptable level of theoretical grounding in ML papers, but the paper's overall claim that "NeuralPES emphasizes the acquisition of lasting information" conflates the idealized algorithm's property with the real one's.

6. **Regret vs. average reward in the synthetic experiment.** The paper reports average reward (Table 1) for the AR(1) logistic bandit but shows regret only in the spoiler figure (Figure 1). Given that the ground-truth parameters are known in this synthetic setup, including regret in the main table would be more informative and would directly connect to the theoretical analysis. This is a minor presentation choice.

### Trivial

- Line 28: "envrionment" → "environment"
- The paper uses both `\mathrm{TrainNN}` (Algorithm 4) and `\mathrm{TrainRewardNN}` (Algorithm 2) for the same function; the naming should be consistent.

## Nice-to-Haves

- **Comparison to the original predictive sampling algorithm (Liu et al. 2023) on the synthetic AR(1) environment.** The paper cites predictive sampling as the direct inspiration and notes it "does not scale," but a small-scale comparison on the low-dimensional (d=10, 10 actions) synthetic setup would directly test whether the neural approximation retains the benefit of the linear version. Since scalability is not a concern here, this would strengthen the empirical story.

- **Inclusion of a non-neural non-stationary baseline** (e.g., SW-UCB, D-UCB, or change-point TS) on the synthetic experiment. While the paper's scope is neural methods, a single non-neural baseline on the small synthetic setup would ground the "state-of-the-art" claim more broadly.

- **Empirical diagnostic for the "lasting information" property.** For example, tracking the predictive variance on actions whose value is about to change, or comparing LinPS vs. TS regret on a linear variant of the AR(1) environment — this would bridge the theoretical analysis and the neural algorithm.

## Removed Points

These points from the reviewers are flagged to be removed; treat them with caution:

- The harsh critic's claim that the theoretical bounds "do not contain any explicit term that quantifies *difference* between LinPS and TS" — The paper explicitly compares bounds in prose (Lines 377–381, 408–410) and recovers the TS bound as a special case. The bounds structure (I(θ₃;θ₂|θ₁) vs. H(θ₁)) does support the qualitative claim. This is a reasonable presentation choice, not a flaw.

- The critic's complaint that "average reward conflates inherent difficulty with algorithm performance" — The paper shows *both* average reward (Table 1) and regret (Figure 1) for this experiment.

- The critic's framing of the state-of-the-art claim as unsupported — The paper claims to outperform "state-of-the-art **neural** contextual bandit learning algorithms" (Line 30), which is narrower than the critic implies. Comparisons against sliding-window variants of the same neural baselines are appropriate for this scope claim.

- Various minor formatting critiques and "the paper should also cover Y domain" complaints that represent scope creep.

## Novel Insights

None beyond the paper's own contributions. The review process did not produce a genuinely novel observation that the paper itself does not articulate.

## Suggestions

1. **Fix the action-selection pseudocode** in Algorithm 4 (line 266): either remove the summation over `i` to match the text, or if the ensemble aggregation is intentional, explain the rationale and update the text accordingly.

2. **Align sequence model training with inference.** Either train with two-step targets (or recursive application) to match the inference-time use of predicting ŵ_{m,t+2}, or explain why one-step training is sufficient for two-step prediction (e.g., Markov property of the weight process).

3. **Specify the sliding window sizes** used for all "Window" baselines, and state whether they were tuned separately per baseline/dataset or fixed uniformly.

4. **Add a brief statement** explaining how w_{m,j+2} is obtained during predictive model training (e.g., stored in a timestamp-indexed array of historical weights) and the memory cost (O(MK)).

5. **Tone down the theoretical claim** in the conclusion (line 548: "We theoretically demonstrated that the algorithm effectively prioritizes exploration for enduring information") to match the paper's own framing as "intuition and evidence" (line 325) for LinPS, which is an idealized version.

## Score and Decision

**Originality:** Good. The combination of ensemble sampling with sequence prediction of future weights and a predictive model for gating information is genuinely novel in the neural non-stationary bandit literature.

**Importance:** High. Scaling non-stationary bandit algorithms to neural-network-based systems is a practically important problem with clear applications in recommendation systems.

**Claims:** Partially supported. The empirical claims are well-supported. The theoretical claims about "lasting information" are supported for the idealized linear version but not directly for NeuralPES.

**Soundness:** Moderate. The empirical methodology is sound (20 seeds, non-overlapping CIs, temporal-order preservation, ablation studies). The algorithm specification has several inconsistencies that weaken reproducibility as written.

**Clarity:** Moderate. The high-level ideas are clearly communicated, but the pseudocode inconsistencies and missing experimental details reduce clarity.

**Value:** High if the algorithm specification issues are resolved. The combination of neural scalability with lasting-information exploration addresses a real gap in the literature.

**Overall:** The paper proposes a well-motivated algorithm with strong empirical evidence of effectiveness on real-world non-stationary data. The main concerns are concrete fixable issues in the algorithm specification (pseudocode inconsistency, sequence model training/inference mismatch) and underspecified experimental details (window sizes). These do not undermine the core contribution but must be corrected for reproducibility.

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>