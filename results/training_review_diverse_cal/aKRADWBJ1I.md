Now I have all the information needed to produce the consolidated review. Let me synthesize.

---

## Summary

This paper proposes ActSafe, a model-based safe reinforcement learning algorithm that maintains a pessimistic safe set of policies and optimistically selects policies within that set to maximize epistemic uncertainty. The core contribution is a theoretical analysis (Theorem 4.1) proving that ActSafe guarantees safety during all learning episodes and achieves an ε-optimal policy within a finite number of episodes — the first such result for model-based safe RL with continuous state-action spaces. The paper also presents a practical variant using neural network ensembles and LBSGD that scales to high-dimensional vision-based control tasks (Safety Gym, RWRL). Empirical results show zero cost violations in GP-based environments and reduced constraint violations in vision-based tasks.

## Strengths

1. **First theoretical safety and finite-sample-complexity guarantees for model-based safe RL in continuous state-action spaces.** Theorem 4.1 proves that ActSafe never violates the safety constraint during learning and converges to an ε-optimal policy within a bounded number of episodes, with an explicit sample-complexity bound (Equation 4). The paper carefully situates this claim relative to prior work — Berkenkamp et al. (2021) and Baumann et al. (2021) are model-free approaches that optimize over policy parameters and are thus in a different setting. This theoretical contribution is novel and significant.

2. **Principled two-phase algorithm that explicitly addresses the exploration–expansion dilemma.** Unlike many deep safe RL methods that only optimize the extrinsic reward subject to constraints (and thus may never expand the safe set to reach the optimal policy), ActSafe separates learning into an intrinsic exploration phase (maximizing epistemic uncertainty to expand the safe set) and an extrinsic exploitation phase. This is a well-motivated design grounded in the safe Bayesian optimization literature.

3. **End-to-end bridge from theory to high-dimensional visual control.** The paper identifies three key insights from the theory (intrinsic reward for expansion, pessimism for safety, constrained selection from the safe set) and implements them using RSSMs, probabilistic ensembles, and LBSGD. This is a non-trivial engineering effort that allows the method to scale where prior theoretically grounded safe exploration methods (e.g., GoSafe, SafeOpt) could not.

4. **Empirical evidence for the necessity of pessimism and intrinsic exploration.** The GP experiments (Figure 2) show Ablations, comparing ActSafe against a version without pessimism and against Opax (unsafe exploration), cleanly demonstrating that pessimism is necessary for safety. The sparse-reward experiments (Figure 5) show that the intrinsic exploration phase is critical for performance when rewards are uninformative.

## Weaknesses

### Fatal
None. The theoretical contribution is sound and stands independently. The empirical evaluation has issues but none that invalidate the core claims.

### Major

1. **Offline data initialization confounds the vision control comparison.** The paper states (lines 321–322) that ActSafe uses 200K environment steps of offline data collected by a random policy for all vision experiments, and notes that "ensuring safety with an NN model with randomly initialized weights is impractical without any additional prior knowledge." However, it does **not** clarify whether the baselines (LAMBDA, BSRP-Lag, CPO) received the same offline data initialization. If ActSafe starts with a model that already provides a reasonable safety prior while baselines start from scratch, the safety advantage in Figure 4 (significantly reduced constraint violations) could reflect the initialization rather than the algorithm's intrinsic safe exploration mechanism. The paper mentions additional experiments without offline data in the appendix (line 322), but these do not remedy the ambiguity of the main comparison. **This is the single most significant weakness in the empirical evaluation.** The authors should either state what initialization each baseline received, or — better — run all baselines with the same offline data warm-start.

### Minor

2. **GP experiments lack statistical rigor for the safety claims.** Section 4.1 evaluates ActSafe on Pendulum and Cartpole for only 10 episodes and, from the text, appears to show results from a single run (or an unspecified number of seeds). The paper states "ActSafe does not incur any costs during learning" (line 308), a strong claim that is not backed by statistical evidence (multiple seeds, violation counts, confidence intervals). Given the probabilistic nature of the guarantee (with probability at least 1−δ), a single trajectory or one-seed result is insufficient to demonstrate that the guarantee is realized in practice. This is especially important because the safe seed ensures safety early, but the expansion phase could still lead to violations.

3. **The claim that the practical variant "preserves the safety guarantees" is too strong.** The paper states (line 247): "Note that Ŝ_n ⊆ S_n, making it a conservative estimate of S_n, therefore selecting policies from Ŝ_n still preserves the safety guarantees." While the subset relationship is mathematically correct for the **definitions**, the practical implementation uses neural network ensembles with no calibration guarantees, a different safe set definition (Equation 6 vs. Definition 2), and an LBSGD planner solving a non-convex problem without optimality guarantees. The theoretical guarantees rely on the well-calibrated model and the specifics of the RKHS setting. The paper does acknowledge the practical variant as a "relaxation" derived from "key insights" of the theory, and uses the word "heuristically" in the conclusion (line 366), but the mid-paper phrasing ("preserves the safety guarantees") overstates what is actually inherited. This should be explicitly qualified.

4. **The sample complexity bound is presented but not interpreted.** Equation (4) involves T^6, C^4, β^4_{n^*}, the maximum information gain γ_{n^*}(k), and the number of expansions H. The bound is never instantiated for any concrete system, and the meaning of H (number of expansions) in practice is not discussed. Even a brief discussion of the bound's scaling with dimension, horizon, or kernel would help readers assess its significance. As it stands, the bound is a symbolic result whose practical implications are opaque.

### Trivial

5. **Computational cost is not reported.** Training an ensemble of RSSMs with LBSGD for high-dimensional vision tasks is likely expensive. A brief note on wall-clock time or number of gradient steps would help readers assess practicality.

## Nice-to-Haves

- A concrete instantiation of the sample complexity bound for a simple system (e.g., 1D GP with known kernel) showing how many episodes n* would be required to achieve a given ε.
- A more explicit comparison to safety-filter approaches (e.g., Dalal et al.) discussing when filters versus safe-set expansion are preferable.

## Removed Points

These points were raised by reviewers but are removed for the reasons stated:

- **Criticism about missing appendix content (LBSGD ablation, distribution shift experiments, humanoid benchmark):** These sections are referenced in the paper (lines 322, 361) and exist in the original submission; the parser strips appendix sections from all papers. Not a valid weakness.
- **Concern about the "first-of-its-kind" claim vs. Berkenkamp et al. and Baumann et al.:** Those works are model-free (optimizing over policy parameters directly). The paper's claim is specifically about **model-based** RL with continuous state-action spaces, which is a different setting. The paper discusses these works in Related Work and correctly distinguishes itself.
- **Concern about D(π,π') not being implemented in practice:** The paper clearly separates the theoretical safe set definition (which uses D) from the practical constraint (Equation 7, which uses a pessimistic cost estimate). The D function is a theoretical construct for the analysis; the practical algorithm uses a tractable relaxation. This is by design and is clearly explained.
- **Concern about the extrinsic exploration phase and model updating potentially violating safety:** Algorithm 2 shows that the constraint (max_{f'∈Q_n} J_c(π, f') ≤ d) is enforced in every episode of both phases. The model is updated and the constraint is re-evaluated with the updated uncertainty — this is the expected behavior and does not create a safety gap.
- **Concern about 10 episodes being insufficient to test safety:** The reviewer's point about statistical rigor (multiple seeds) is kept in Minor #2 above. But the criticism about the horizon being "2000 environment interactions" as inherently insufficient is unfounded without specifying the environment complexity.

## Novel Insights

The most interesting observation emerging from this review is about the **structural tension between the theoretical analysis and the practical scaling strategy**. The theory achieves guarantees by maintaining an explicit safe set S_n and model set M_n via intersection (M_n = M_{n-1} ∩ Q_n), which is fundamentally a **contraction** operation — the set of plausible dynamics shrinks as data accumulates. The practical algorithm, by contrast, *replaces* this with Q_n alone, which is a confidence interval that both shifts and shrinks as the model is updated. This means the practical algorithm is doing something qualitatively different from the theory: it uses pointwise pessimistic cost estimates rather than the intersection-based model set. The paper cites berkenkamp2021bayesian and sukhija2022scalable as making "similar relaxations," but those methods also operate in the model-free/BO setting where the function being modeled (cost) is the same as the function being optimized, not a dynamics model that is then used to plan. Whether this substitution preserves the core guarantees under the neural network approximation is an open question that the paper does not fully address.

## Suggestions

1. **Clarify baseline initialization in vision experiments.** State explicitly whether LAMBDA, BSRP-Lag, and CPO also received 200K offline data steps. If not, provide a comparison where all methods receive the same offline warm-start, or show that ActSafe without offline data still outperforms baselines.

2. **Add multiple seeds and violation statistics to the GP experiments.** Report the maximum per-episode cost across 10+ seeds, with the fraction of runs where cost ≤ d, to substantiate the claim that ActSafe "does not incur any costs."

3. **Weaken the safety guarantee claim for the practical variant.** Replace "selecting policies from Ŝ_n still preserves the safety guarantees" (line 247) with a qualified statement: "Ŝ_n ⊆ S_n holds at the level of definitions, and any policy selected from Ŝ_n is safe under the theoretical model assumptions; however, since the neural network model is not guaranteed to be well-calibrated in the sense of Definition 4.1, the formal safety guarantee does not extend to the practical implementation."

4. **Discuss the sample complexity bound qualitatively.** Add a paragraph showing the bound's scaling behavior (e.g., polynomial in T, exponential in effective dimension through γ_n(k)) and what it implies about when the algorithm is practical.

## Score and Decision

The paper makes a meaningful theoretical contribution — novel safety and sample-complexity guarantees for model-based safe RL in continuous spaces — and proposes a practical extension that connects these ideas to high-dimensional visual control. The main empirical weakness (uncontrolled offline data initialization in vision experiments) undermines the comparative safety claims but does not affect the core theoretical result. The paper is above the acceptance threshold.

**MY FINAL SCORE: <pineapple>6.0</pineapple>**
**MY FINAL DECISION: <orange>Accept</orange>**