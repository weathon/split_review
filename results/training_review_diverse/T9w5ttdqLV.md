Now I have a thorough understanding of the paper and all the claims. Let me write the consolidated review.

## Summary

The paper investigates representational limitations in value-decomposition for cooperative MARL. It makes three primary contributions: (1) a theoretical characterization showing that Linear Mixing Functions (LMF) only avoid representational limitation when the task is a "decomposable MMDP" — a rare case — with a necessary-and-sufficient condition (Theorem 3.3); (2) the Mixing for Unbounded Difference (MUD) framework, which rescales SMMF's bounded differences into unbounded ones to achieve complete representational capacity under IGM; (3) identification of Optimal Representational Interference (ORI) as a fundamental training obstruction in value decomposition, with gradient-shaping solutions (MUD-SmG and MUD-StG). Experiments on a toy game, a matrix game, and predator-prey provide supporting evidence.

---

## Strengths

1. **First necessary-and-sufficient characterization of when LMF is expressively sufficient.** Theorem 3.3 cleanly connects task structure (decomposable MMDP) to linear factorizability of the action-value function. This goes beyond prior work (Son et al., 2019; Rashid et al., 2020a) which focused on solutions rather than diagnosing when the limitation actually occurs. The concept is original and intellectually substantive.

2. **Principled derivation of MUD from SMMF's bounded-difference limitation.** Section 4.1 provides a clear argument: SMMF's output differences Δf are bounded from above by Δf' (Eq. 8), so the range condition for complete representation (Eq. 7, R(Δf) = [0, +∞)) is violated. MUD's rescaling of these differences via learned weights and biases to achieve unbounded range is a natural and well-motivated extension. The paper correctly shows QPLEX is a special case of MUD, demonstrating generality.

3. **Identification of Optimal Representational Interference (ORI) as a distinct training-phase problem.** The ORI concept (Section 4.2) — that joint-action values sharing local Q values interfere during training — is a genuine insight that goes beyond representational capacity alone. The paper demonstrates empirically that even methods with complete representational capacity (MUD (Eq.9), QPLEX) can fail in practice due to ORI, and that gradient shaping to increase the representation weight of the optimal action (MUD-SmG, MUD-StG) can overcome this. The predator-prey results under punishment -5, where only MUD-SmG/StG succeed while QPLEX, WQMIX, and QTRAN fail, support the practical relevance of this issue.

4. **Clear and well-structured presentation.** The paper progresses logically from problem diagnosis (Section 3) to capacity-complete architecture (Section 4.1) to training obstruction (Section 4.2) to experimental validation (Section 5). The theoretical derivations are generally precise, and the figures (as described) effectively illustrate the key ideas.

---

## Weaknesses

### Fatal
None.

### Major

1. **Narrow experimental evaluation with no statistical rigor.** The paper tests on only three environments: a custom toy game, a single 2-agent matrix game, and predator-prey. There is no evaluation on standard cooperative MARL benchmarks (e.g., SMAC, GRF, multi-agent MuJoCo, LBF). Furthermore, the paper reports no error bars, confidence intervals, or multi-seed statistics — every figure appears to show single training trajectories or single-run point estimates. Given the well-known variance of deep MARL training, single runs are insufficient to establish that MUD-SmG and MUD-StG *reliably* outperform baselines.

2. **Ground-truth action-values are themselves approximated.** In the expressiveness verification experiment (Section 5.1), the "actual action-values" are approximated by a separately learned non-factorized Q function (Q_ct). The reported RMSE thus measures agreement between two learned functions, not representational error relative to the true optimal action-values. The toy game has a known optimal return (4), which could have been used as a more principled ground truth for verification.

3. **Inconsistency between the toy game and matrix-game results for MUD (Eq. 9) is not explained.** In the toy game (Section 5.1, Fig. 6b), MUD (Eq. 9) achieves the highest return in both decomposable and indecomposable cases and is never called out as failing. Yet in the matrix game (Section 5.2), MUD (Eq. 9) "is still easily stuck in the sub-optimal point" due to ORI. The paper does not discuss what task properties determine whether ORI is severe enough to cause failure, leaving an important gap in the understanding of when the proposed solutions are actually needed.

### Minor

1. **Division by zero in MUD-SmG (Eq. 12).** The term `(1 - Q_a / Q_{a,gre})` is undefined when `Q_{a,gre} = 0` and can cause numerical instability when `Q_{a,gre}` is near zero. The paper does not acknowledge or address this issue, nor does it describe any safeguards used in implementation.

2. **Unspecified behavior policy in the ORI formalization (Eq. 11).** The optimal representation ratio `w*` depends on `π(u|s)`, which is never defined. In deep MARL, the behavior policy is non-stationary and complex; the paper does not explain how `w*` is estimated or used during training, nor does it clarify whether `π` refers to the behavior policy, target policy, or some other distribution.

3. **MUD-StG's stop-gradient (Eq. 13) is a training technique presented as a functional form.** The piecewise definition of `ΔF` with stop-gradient (`SG(Q_a)`) describes a training procedure, not a property of the mixing function itself. Presenting it as a functional definition is misleading. Additionally, the hyperparameter `α` in the step function is not studied or ablated (though the hard-rule about stripped sections may account for missing ablation content).

4. **QTRAN misclassified as "implementation of LMF."** The paper states (line 259) that "QTRAN (implementation of LMF)" — this is incorrect. QTRAN uses a fundamentally different architectural framework (a transformation network with constraints) and is not a linear mixing function. While the paper may mean "value decomposition method addressing similar limitations," the phrasing is factually inaccurate.

5. **Missing environment description for predator-prey.** The predator-prey experiments (Section 5.2) provide no description of the environment setup — map size, number of agents and predators, observation/action spaces, or training hyperparameters. This makes the results difficult to interpret or reproduce.

6. **Notation inconsistency in Definition 3.1 vs. Property 3.2.** Definition 3.1 uses `\hat{U}_i` for action subsets, but Property 3.2 (line 98) uses `\hat{M}_i` in the tuple `<\hat{S}_i, \hat{M}_i, P, r_i, n_i, γ>`, where `M` presumably should be `U`. This is a minor but confusing inconsistency.

### Trivial

- Line 82 uses `\bar{n}` instead of `n` in the LMF definition — likely a copy-paste artifact.
- The sentence beginning "L M F in indecomposable MMDP" (line 116) is partially garbled and difficult to parse.
- Figure references use "Fig." and "Figure" inconsistently.

---

## Nice-to-Haves

- Evaluation on standard benchmarks (e.g., SMAC or GRF) and reporting of multi-seed statistics with error bars would substantially strengthen the empirical claims.
- An ablation study of the hyperparameter `α` in MUD-StG and the number of SMMF channels `d` would help understand sensitivity.
- A discussion of practical safeguards for the division by `Q_{a,gre}` in MUD-SmG (e.g., adding a small epsilon or clamping).
- A discussion of the computational overhead of multi-channel SMMFs vs. simpler mixing functions.

---

## Removed Points

These points are flagged to be removed per guidelines; they are listed here for traceability but should not be weighed in the final assessment.

- **Missing proof of Theorem 3.3 / Property 3.2**: The paper's text reads "The proof of Theorem 3." followed by figure description rather than a formal proof. Per instructions, appendix/deferred-proof content that may have been stripped by the parser is not to be treated as a weakness.

- **Missing hyperparameters, network architectures, training details**: Per guidelines, nitpicks about trivial implementation details not practical to include are excluded.

- **Missing ablation studies**: The paper mentions "Ablation studies" as part of the experiment plan (line 224) but no such section is visible. Per guidelines, content stripped by the parser is assumed to exist in the original submission.

- **Claim that w* axis goes to 1.5**: The paper text states w* ∈ [0,1]; the figure image is not visible in the plain-text parse, so this cannot be verified and is removed.

- **Demand for theoretical guarantees of MUD-SmG/StG avoiding ORI fixed points**: This demands a standard of proof (convergence guarantees for a deep RL training technique) not expected for heuristic gradient-shaping methods.

---

## Novel Insights

Beyond the paper's own contributions, the reviews surface one useful observation: the inconsistency between MUD (Eq. 9) succeeding in the toy game but failing in the matrix game points to an under-explored question — what structural properties of a task determine whether ORI is severe? Is it the ratio of optimal to suboptimal action-values, the size of the joint action space, the degree of agent interdependency, or something else? This is a natural next question that the paper does not address but that would be valuable for the community.

---

## Suggestions

1. **Add multi-seed experiments with error bars** on at least one standard benchmark (SMAC or GRF) to establish statistical reliability of MUD-SmG/StG's claimed superiority.
2. **Resolve the division-by-zero issue in Eq. 12** explicitly (e.g., use `max(ε, Q_{a,gre})` or a softmax-based alternative) and discuss numerical stability.
3. **Clarify the policy `π` in Eq. 11** — specify what distribution it refers to and how, if at all, `w*` is estimated during training.
4. **Explain the inconsistency** between MUD (Eq. 9) succeeding in the toy game (Section 5.1) and failing in the matrix game (Section 5.2) — what task properties determine ORI severity?
5. **Correct the QTRAN classification** — QTRAN is not an implementation of LMF.
6. **Provide environment details** for the predator-prey experiments (map size, agent counts, observation space, action space) to enable reproducibility.

---

## Score and Decision

This paper makes genuinely novel contributions — the decomposable-MMDP characterization of LMF's limitation, the MUD framework, and the ORI concept are all valuable. The theoretical analysis is the paper's strongest asset. However, the experimental evaluation is too narrow and lacks statistical rigor to fully support the claimed superiority of MUD-SmG/MUD-StG over baselines. The remaining minor issues (division by zero, undefined policy, QTRAN misclassification) are addressable. The paper's core theoretical contributions stand independent of the experimental weaknesses, and the experiments do provide proof-of-concept support even if not definitive.

**Overall**: The theoretical and conceptual contributions are solid and novel; the experiments are sufficient as proof-of-concept but not as rigorous validation. The paper would be acceptable at a venue that weights theoretical contributions more heavily than exhaustive empirical evaluation, but would need stronger experiments for a venue requiring rigorous empirical validation.

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>