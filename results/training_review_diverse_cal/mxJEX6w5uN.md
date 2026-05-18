Now I have a thorough understanding of the paper and can verify each reviewer claim against the actual text. Let me write the consolidated review.

---

## Summary

This paper proposes Scaff-PD, an algorithm combining accelerated primal-dual (APD) updates with SCAFFOLD-style control variates for solving distributionally robust optimization (DRO) problems in federated learning. The key theoretical contribution is proving that Scaff-PD achieves O(1/T²) convergence in the strongly-convex–concave setting and linear convergence in the strongly-convex–strongly-concave setting — the first such rates for federated DRO. The algorithm is evaluated on synthetic data and real-world benchmarks (CIFAR-100, TinyImageNet) with comparisons to FedAvg, SCAFFOLD, DRFA, AFL, and q-FFL.

## Strengths

- **First accelerated and linear convergence rates for federated DRO.** Theorem 1 proves an O(1/T²) rate in the strongly-convex–concave setting and Theorem 2 proves linear convergence exp(−O(T)) in the strongly-convex–strongly-concave setting. Prior work (e.g., DRFA) achieved only O(1/R) sublinear rates. These are nontrivial advances and are the paper's strongest contribution.

- **Bias-corrected local steps tailored to the min-max DRO structure.** The algorithm combines Nesterov-style extrapolation on the dual variable (Eq. 4) with SCAFFOLD-style control variates (Algorithm 2) to correct client drift during local steps. The dual variable is updated globally (avoiding impractical per-client dual updates), while local primal steps are corrected via bc_i and bc. The theory shows that the resulting rates match those of centralized accelerated primal-dual algorithms.

- **Superior worst-20% accuracy under high heterogeneity.** On CIFAR-100 with α=0.01, Scaff-PD achieves 29.30% worst-20% accuracy versus 26.77% for DRFA and 15.93% for FedAvg (Table 1). Similar gains hold on TinyImageNet (25.32% vs. 22.32% for DRFA, α=0.01). These improvements are meaningful for fairness-motivated applications.

- **General formulation covering multiple fair FL objectives.** Section 3 shows that the min-max problem in Eq. (1) subsumes agnostic FL, α-CVaR, q-FFL, and proportional fairness through appropriate choices of Λ and ψ, making the framework broadly applicable.

## Weaknesses

### Major

- **Insufficient experimental reporting for reproducibility and fair comparison.** The paper omits several critical details:
  - The value of ρ (regularization strength in ψ) used in the main Table 1 results is not stated — the ρ ablation (Figure 2) explores {0.1, 0.2, 0.5} but does not say which value was selected for the main comparison.
  - The number of local steps J for real-world experiments is not reported (only specified for synthetic data: J=100).
  - The number of communication rounds used for real-world results is not given.
  - Hyperparameter tuning protocols for baselines are absent. Notably, q-FFL performs dramatically worse than FedAvg in some settings (e.g., 5.43% worst-20% on CIFAR-100 α=0.01 vs. 15.93% for FedAvg), suggesting the q value or learning rate may not have been well-tuned. Without disclosure of tuning procedures, it is unclear whether Scaff-PD's advantage reflects algorithmic merit or asymmetric tuning effort.
  
  These gaps prevent independent reproduction and weaken the empirical case for practical efficacy.

- **Lack of ablation studies isolating the algorithm's components.** The experiments never isolate the effect of Scaff-PD's two key innovations: the Nesterov-style extrapolation (θ_r term) and the SCAFFOLD-style bias correction. Would a non-accelerated primal-dual with SCAFFOLD achieve similar rates? Is θ_r actually providing acceleration in practice, or is the improvement primarily from the bias correction? An ablation setting θ_r = 0 throughout would directly answer this, but is absent. Without such studies, the empirical results do not disentangle which component drives the observed improvements.

- **No convergence curves for real-world comparisons with primary baselines.** Table 1 reports only final accuracy (after an unspecified number of rounds). Figure 2 shows accuracy-vs-rounds curves but only for different ρ values and only compared to SCAFFOLD — not against DRFA, AFL, or other DRO baselines. The paper's title claims "Communication Efficient" performance, but without accuracy-vs-rounds or accuracy-vs-communication plots for the main baselines, this claim is not empirically validated for deep-learning-scale tasks.

### Minor

- **Overstatement in the introduction about "matching" the average objective.** The introduction (line 45) claims "the sample complexity as well as the communication complexity for the DRO problem matches that of the easier average objective." However, Remark (lines 310–312) acknowledges that solving DRO with Scaff-PD requires a multiplicative factor of `(√(L_xx/μ_x) + √(L_λx²/(L_xx μ_λ)))` more communication rounds than ProxSkip on the average objective. The rate order w.r.t. ε (log(1/ε)) is the same, but the condition-number-dependent factor is nontrivial, and the introduction's unqualified "matches" is misleading.

- **Control variate design differs from SCAFFOLD without explicit discussion.** The paper recomputes bc_i^r = g_i(x^r) as a fresh stochastic gradient each round rather than maintaining persistent control variates as in SCAFFOLD. While this is valid and the theory handles it through the bounded noise assumption (Assumption 3), the paper describes it as "à la Scaffold" without clarifying the difference. The variance properties of the correction term −bc_i + bc differ from SCAFFOLD's persistent variates, and a brief discussion would improve clarity.

- **"Optimal rate" claim for the stochastic setting is unsupported.** The paper (line 45) claims an "optimal rate of O(1/T)" but provides no lower bound or citation to a matching lower bound for the DRO min-max setting. While O(1/T) is optimal for standard stochastic convex optimization, the optimal rate for the federated DRO min-max problem may differ, and the claim should be qualified.

- **Best-20% accuracy mentioned but not reported.** Lines 449–451 state that the paper studies the trade-off between average, worst-20%, and best-20% accuracy, but best-20% numbers are never shown in Table 1 or anywhere else. This is claimed evidence for "not sacrificing much on average and best-20% accuracy" but the data to support it is absent.

- **Secure aggregation compatibility claim is unsubstantiated.** The paper claims compatibility with secure aggregation (line 42), but the algorithm requires the server to see each client's scalar loss L_i^r and gradient bc_i^r. How this is compatible with secure aggregation (which typically hides individual contributions) is not explained.

### Trivial

- None.

## Nice-to-Haves

- Convergence plots (accuracy vs. communication rounds) for Scaff-PD vs. DRFA/AFL on at least one real dataset would substantially strengthen the communication-efficiency claim.
- An ablation of the θ_r extrapolation (setting θ_r = 0 throughout) on synthetic or real data.
- Reporting the ρ value, J, number of rounds, and hyperparameter tuning grid used for Table 1.
- A brief discussion of the dual update cost scaling with N (the paper focuses on cross-silo with N=20, which is fine, but setting expectations for cross-device settings would help).
- A note on how the control variate recomputation each round differs from SCAFFOLD's persistent variates.
- Adding best-20% accuracy numbers to Table 1 or a supplementary table.

## Removed Points

- **"Paper does not clarify whether bc_i is a full gradient or stochastic gradient"** — The paper explicitly defines g_i(·) as a stochastic gradient (Eq., lines 85–88) and Algorithm 1 sets bc_i^r = g_i(x^r). The paper does clarify this. The deeper variance concern is retained above (reframed under Minor).

- **Missing related works** — Removed per guidelines (no external sources to confirm existence).

- **Formatting/style nitpicks** (typos, grammar, punctuation, etc.) — These are parser artifacts, not author errors.

- **Missing appendix/proofs content** — Parser strips these sections; they exist in the original submission.

## Novel Insights

The reviews converge on a clear picture: the paper's theoretical contribution is its strongest asset, delivering the first accelerated and linear convergence rates for federated DRO. The algorithm design is principled (exploiting the linear structure of the min-max interaction term to apply APD with bias-corrected local steps). The weakness is squarely in the empirical evaluation, which lacks the reproducibility details and ablations needed to validate the practical claims. This suggests the paper would benefit from either (a) substantially expanding and documenting the experiments, or (b) reframing the contribution as primarily theoretical with illustrative experiments, rather than claiming strong practical validation.

## Suggestions

1. **Report all experimental hyperparameters for Table 1** — specifically the ρ value, J (number of local steps), number of communication rounds, and the grid search ranges used for each baseline's hyperparameters.
2. **Add convergence curves** for real-world experiments showing accuracy (average and worst-20%) vs. communication rounds for Scaff-PD and at least 2 baselines (e.g., DRFA, AFL).
3. **Run an ablation** removing the extrapolation step (θ_r = 0) on synthetic data to demonstrate the acceleration component's empirical contribution.
4. **Qualify the introduction's claims** about matching the average objective, e.g., "the communication complexity is of the same order in ε as that of the average objective, with an explicit condition-number-dependent factor detailed in our analysis."
5. **Report best-20% accuracy numbers** to support the fairness claim about not sacrificing the best clients' performance.
6. **Add a brief discussion** of how the control variate design (recomputed each round) relates to SCAFFOLD's persistent variates and why it still provides valid bias correction.

## Score and Decision

MY FINAL SCORE: <pineapple>5.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>