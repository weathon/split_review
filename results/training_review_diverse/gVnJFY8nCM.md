Now I have a thorough understanding of the paper and the reviews. Let me synthesize my findings.

## Analysis of Reviewer Claims vs. Paper

**Key verification results:**

1. **Initialization control (Critical Issue 2b):** The paper explicitly states "The samples are obtained from the same prior policy used in Residual-MPPI" (line 236). Both Guided-MPPI and Residual-MPPI use prior-policy initialization as shown in Algorithm 1 (lines 106-109). The reviewer's claim that initialization is not controlled is **factually wrong** — the comparison does isolate the evaluation function.

2. **Theoretical derivation (Critical Issue 1):** The paper's Theorem 1 shows the equivalence between max-entropy action distributions and MPPI optimal distributions. The text says "It suggests that MPPI can well approximate the maximum-entropy optimal policy... We can then derive Residual-MPPI straightforwardly by defining the evaluation function S^aug." This is plausible as a motivation/heuristic but is presented as a stronger theoretical justification than it truly provides. This is a **valid minor weakness** but not structural.

3. **Algorithm/Eq. discrepancy:** The reviewer notes that the -λ û^T Σ^{-1} ε term appears in Algorithm 1 but not in Eq. (6). This term is the control prior from the MPPI importance weight formula (Eq. 5) — the constant part gets absorbed by normalization. This is **standard MPPI implementation** and a minor clarity issue at most.

4. **GTS planning baseline (Critical Issue 3):** Valid point — a vanilla MPPI/MPC with a hand-crafted cost would strengthen the GTS experiment.

5. **Full-MPPI tuning:** The reviewer raises concerns about Full-MPPI's catastrophic failure suggesting poor tuning. This is a reasonable concern but the paper's main comparison is Guided-MPPI vs. Residual-MPPI, both of which use the same sampling infrastructure. Minor weakness.

Now producing the final consolidated review.

## Summary

This paper proposes Residual-MPPI, an online planning algorithm for customizing pre-trained continuous-control policies toward new objectives without retraining. The core idea is to use the prior policy's log-probability as a surrogate for the unknown original task reward inside an MPPI sampling-based MPC loop, augmented with an add-on reward. Experiments on MuJoCo benchmarks and on the champion-level GT Sophy 1.0 racing agent in Gran Turismo Sport demonstrate that the method can reduce undesired behaviors (e.g., off-course driving) with modest performance trade-offs, using orders-of-magnitude less data than RL-based alternatives.

## Strengths

- **Novel integration of RQL with MPPI for online continuous-control customization**: The paper is the first to propose an *online* (training-free) policy customization method for continuous action spaces. Prior RQL work required SAC-based training for continuous control or was limited to discretized actions (Residual-MCTS). Residual-MPPI plans entirely at execution time (Algorithm 1), directly addressing a significant practical bottleneck (Sec. 1, lines 29–31).

- **Theorem 1 establishes a formal connection between MPPI and maximum-entropy optimal policies**: The paper proves that the MPPI optimal action-sequence distribution and the max-entropy policy's action distribution share the same functional form under appropriate assumptions (γ≈1, large noise variance). This provides a theoretical grounding for incorporating the prior policy's log-likelihood into the MPPI evaluation function, going beyond a purely heuristic approach (Sec. 3.1, Theorem 1 and surrounding text).

- **Consistent empirical advantage over Guided-MPPI across all four MuJoCo environments**: In Table 1, Residual-MPPI outperforms Guided-MPPI (which uses the true ground-truth reward with the same prior-policy-guided sampling) on every task — Total Reward, Basic Reward, and Add-on Reward. In HalfCheetah: 1948.14 vs. 1821.19 (total reward); in Swimmer: −61.00 vs. −147.77; in Hopper: 7398.29 vs. 6146.35; in Ant: 6808.38 vs. 5485.85. This comparison controls for initialization and sampling distribution.

- **Real-world validation on champion-level GT Sophy 1.0 with dramatic sample efficiency**: Residual-MPPI reduces off-course steps of the champion GT Sophy agent by over 50% (from 93.13 to 36.60 after few-shot fine-tuning) with only ~3% lap time increase (from 117.77 to 120.75). The dynamics model required only ~2,000 laps of data vs. 80,000 laps for Residual-SAC — a 40× improvement in sample efficiency (Sec. 5, Table 2). The 60Hz real-time constraint on PS5 hardware makes this a particularly strong practical demonstration.

## Weaknesses

### Fatal
None.

### Major

- **The GTS experiment lacks a planning-only baseline**: The GTS evaluation compares against GT Sophy 1.0 (prior policy) and Residual-SAC (RL), but not against a vanilla MPPI or simple MPC that uses a hand-crafted cost for being off-course (e.g., distance to track center). Without such a baseline, the reader cannot distinguish whether the improvement comes from the proposed log π surrogate or simply from the use of any model-based planner. This gap is notable because the MuJoCo experiments already demonstrate that the log π term outperforms ground-truth reward, so the GTS experiment is the place to show this holds in a complex real-world setting. A baseline that uses MPPI with a cost defined as `c_offcourse + λ·||a||` (without log π) would resolve this.

### Minor

- **The theoretical justification is overstated**: The paper frames Residual-MPPI as being "derived" from Theorem 1 (Sec. 3.1, line 148: "We can then derive Residual-MPPI straightforwardly"). In reality, Theorem 1 establishes an equivalence between two distributional forms, but no formal steps connect this to replacing the unknown reward with log π. The actual contribution is a well-motivated heuristic: use log π as a proxy for the original task's long-term value within MPPI. This is a reasonable algorithmic innovation, but presenting it as having a theoretical derivation from Theorem 1 overclaims. Reframing as "theoretically motivated" rather than "derived" would be more accurate.

- **Full-MPPI's catastrophic failure raises tuning concerns**: Full-MPPI achieves negative total rewards in HalfCheetah (−3590.68) and near-zero in Hopper (21.09), suggesting the MPPI implementation (horizon, samples, covariance, temperature) is not well-tuned for these domains. While the paper's main comparison is between Guided-MPPI and Residual-MPPI (both using the same sampling infrastructure), the poor Full-MPPI results mean we lack a reference point for whether the MPPI parameters are generally reasonable. This would be less concerning if the paper reported a tuning procedure or a sensitivity analysis.

- **Hyperparameter specification is insufficient for reproducibility**: The paper does not state how key MPPI hyperparameters (K, T, Σ, λ, ω') were chosen — whether they were tuned per environment, held constant, or selected via grid search. Without this information, a reader cannot determine whether the advantage of Residual-MPPI over Guided-MPPI might simply reflect better-tuned parameters for the proposed method. This is particularly important because MPPI is known to be sensitive to these settings. (The paper defers to the appendix — line 223 — which is stripped from the submission.)

- **No ablation separating the effect of the log π term alone**: While the comparison with Guided-MPPI controls for initialization and sampling, the paper does not include an ablation that uses only the add-on reward r_R with prior-policy initialization (i.e., Residual-MPPI minus the log π term). Such an ablation would directly quantify how much the log π component contributes over a method that simply adds the add-on reward to the prior policy's nominal trajectory.

### Trivial

- **Task-specific metrics in Table 1 are not defined in the main text**: The symbols |θ̄| (HalfCheetah/Swimmer), z̄ (Hopper), and v̄_y (Ant) are used in Table 1 but never explained in the main body. The reader must infer from context what these represent.
- **No statistical significance testing for GTS results**: With only 30 laps, the reported differences (e.g., zero-shot 121.99 vs. few-shot 120.75 lap time) would benefit from confidence intervals or effect sizes.
- **The relationship between S^aug (Eq. 6) and S(E^k) in Algorithm 1 could be clarified**: Eq. (6) defines S^aug as Σ γ^t(r_R + ω' log π), but Algorithm 1 accumulates an additional term (−λ û^T Σ^{-1} ε) on line 114. While this term is the control prior penalty from the standard MPPI importance weight formula (Eq. 5), the paper does not explicitly reconcile why it appears in the algorithm but not in S^aug.

## Nice-to-Haves

- Report dynamics model prediction error (e.g., validation MSE) for GTS, and show how it evolves during online fine-tuning.
- Provide a sensitivity analysis for at least one MuJoCo environment showing how K, T, λ, and ω' affect performance.
- Extend the GTS experiment with a planning baseline (MPPI with a hand-crafted off-course cost) as discussed in Major weaknesses.

## Removed Points

These points are flagged to be removed, treat them with caution:

- **"No control experiment isolates the evaluation function from the initialization"** (Harsh Critic Critical Issue 2b): Factually incorrect. The paper states "The samples are obtained from the same prior policy used in Residual-MPPI" (line 236), and Algorithm 1 (lines 106–109) shows prior-policy initialization. Both Guided-MPPI and Residual-MPPI use the same initialization and sampling distribution. The comparison does isolate the evaluation function.
- **"The MPPI derivation includes a term absent from S^aug... the paper does not explain this discrepancy"**: The term −λ û^T Σ^{-1} ε is the noise-dependent part of the MPPI control prior (Eq. 5). The noise-independent constant (−(λ/2)û^T Σ^{-1} û) is absorbed by normalization (β and η in Algorithm 1). This is standard MPPI. A minor clarity improvement at most, not a substantive discrepancy.
- **"No details such as network architecture, learning rate"**: The paper defers implementation details to appendices (line 223), which are stripped by the review system. Not a paper error.
- **"The claim that Residual-SAC yields a very conservative customized policy... dismissed without discussing tuning the weight"**: The paper acknowledges the trade-off explicitly (line 295–296) and notes the 80k laps required. Discussing weight tuning is a reasonable suggestion but not a weakness of the presented results.
- **"Zero-shot caveat"** (about needing a pre-trained dynamics model): The paper is transparent about this — the intro (line 31) says "zero-shot policy customization with a provided offline trained dynamics model." No overclaiming.
- Generic strengths from Strength Finder that are redundant with core claims: several strengths already listed above subsume them.

## Novel Insights

None beyond the paper's own contributions. The reviews largely converge on the paper's stated contributions (online customization via log π + MPPI) and the identified weaknesses (GTS missing baseline, theory overstatement, tuning transparency) are standard areas for improvement rather than novel observations.

## Suggestions

1. **Reframe the theoretical connection** as a motivation/heuristic rather than a derivation. Keep Theorem 1 (it genuinely shows the distributional equivalence) but change "derive Residual-MPPI straightforwardly" to "motivate Residual-MPPI by defining..." This is a one-paragraph fix that removes the overclaim.

2. **Add a planning baseline in the GTS experiment** — even a simple MPC with a distance-to-track-center cost and the same dynamics model — to validate that the log π term (not just model-based planning) drives the improvement.

3. **Add an ablation in MuJoCo** that removes the log π term from Residual-MPPI (keeping only the add-on reward r_R with prior-policy initialization). This directly quantifies the log π contribution.

4. **Report hyperparameter choices** (K, T, Σ, λ, ω') in the main text, along with a brief statement of how they were selected (e.g., "tuned on a single seed per environment, then held fixed").

5. **Define the task-specific metrics** (|θ̄|, z̄, v̄_y) explicitly in the experiment setup section, and add confidence intervals or bootstrap estimates for the GTS results.

## Score and Decision

The paper proposes a clean, well-motivated algorithm for a practically important problem (online policy customization) and validates it on both standard benchmarks and a challenging real-time racing environment with a champion-level policy. The core contribution — using log π as a reward surrogate in MPPI — is novel and demonstrably effective. The weaknesses are addressable: the theory overstatement is a framing issue, the missing GTS planning baseline is a single-experiment gap, and the hyperparameter transparency is a reporting issue. None of these invalidate the central claim that Residual-MPPI enables effective zero-shot/few-shot customization.

The paper is ready for acceptance with minor-to-moderate revisions. The contribution is solid, the real-world GTS experiment is compelling, and the improvements over Guided-MPPI (which uses full ground-truth reward) are consistent and meaningful.

MY FINAL SCORE: <pineapple>6.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>