- Decision: Reject
- Avg Score: 5.33
- Scores: 6, 5, 5
Now I have a thorough understanding of the paper. Let me write the consolidated final review.

## Summary

This paper studies representational limitations in value-decomposition MARL. It makes three contributions: (1) a necessary and sufficient condition for when Linear Mixing Functions (LMF) can represent the action-value function (Theorem 3.3: LMF succeeds iff the MMDP is "decomposable"); (2) a two-stage mixing framework called MUD that achieves complete representational capacity under the IGM constraint by rescaling bounded SMMF differences; (3) identification of Optimal Representational Interference (ORI) — cross-interference in training due to shared local Q-functions — and two gradient-shaping mitigations (MUD-SmG, MUD-StG).

## Strengths

- **First formal characterization of when LMF works (Theorem 3.3).** The paper proves a necessary and sufficient condition: the action-value function is linearly factorizable iff the underlying MMDP is decomposable into independent sub-MMDPs with additive rewards and factorized transitions. This goes beyond prior awareness that LMF has limited capacity by specifying exactly when it does not. The toy-game experiment (Fig. 6) provides supporting evidence that LMF's RMSE is near-zero on decomposable MMDPs and large on indecomposable ones.

- **MUD framework with provably complete capacity under IGM (Section 4.1).** The paper identifies that SMMF's limitation stems from the bounded range of Δf (the difference between greedy and non-greedy joint Q-values). By introducing a second stage that rescales multi-channel SMMF differences via learned positive weights and biases, MUD achieves R(ΔF) = [0, +∞) while preserving monotonicity and IGM. The framework subsumes QPLEX as a special case. This is a principled architectural contribution.

- **Identification of Optimal Representational Interference (ORI) as a training-level obstacle (Section 4.2).** The paper recognizes that complete capacity is necessary but not sufficient: shared local Q-functions create cross-interference between the representations of different action-values. The optimal representation ratio w* (Eq. 11) provides a quantitative measure. The matrix-game experiment (Fig. 7) shows that MUD and QPLEX (both with complete capacity) still converge to suboptimal fixed points due to ORI, while MUD-SmG/StG with gradient shaping escape it — demonstrating that ORI is a real and distinct problem from capacity.

- **Gradient-shaping methods that address ORI in practice.** MUD-SmG (exponential decay weighting by ΔF) and MUD-StG (step-function with stop-gradient) are simple, practical interventions. The predator-prey experiment (Fig. 8) shows that under severe punishment (-5), only MUD-SmG and MUD-StG succeed, while QPLEX (complete capacity but no ORI mitigation) and all other baselines fail.

## Weaknesses

### Fatal
None.

### Major

- **Experimental evaluation is far too narrow to support the claimed generality.** The paper promises "various benchmarks" (abstract, line 20) but evaluates on only three small-scale settings: a custom 4×4 toy gridworld, a single 3×3 matrix game, and a partially-observed predator-prey variant. No results on standard MARL benchmarks (SMAC, LBF, GRF, etc.). The predator-prey experiment (Fig. 8) consists of single learning curves with no error bars, no number of seeds reported, and minimal environment description (observation space, dynamics, reward structure not detailed). The matrix game (Fig. 7) also lacks variance measures. The claim that MUD-SmG/StG "outperform baselines" across domains is not supported by the presented evidence — the experiments test only two small, non-standard domains beyond the toy game. For a paper that claims to solve a fundamental limitation and proposes new methods, this level of evidence is insufficient to demonstrate general effectiveness.

- **ORI formalization remains incomplete and the causal link to performance is not established.** The definition of w* (Eq. 11) depends on π(u|s), which is not clearly specified — in value-based methods, the policy is usually greedy or ε-greedy, but the paper does not state which. The paper shows correlation (MUD-SmG/StG achieve higher w* and better performance) but does not establish a causal mechanism or theoretically justify why the proposed gradient-shaping forms (exponential decay, step-function) specifically address ORI. The step-function variant (MUD-StG) introduces a hard threshold with stop-gradient that could cause optimization difficulties, but no analysis is provided. No sensitivity analysis of the hyperparameter α in MUD-StG is given.

### Minor

- **The decomposable/indecomposable conditions in the toy game experiment are unclearly described.** The paper says "For the decomposable case, consider two decompositions… For the indecomposable case…" (Section 5.1) but never defines what changes between the decomposable and indecommissible setups. This undermines interpretability of the key empirical support for Theorem 3.3.

- **No ablation of the channel dimension d in MUD.** Since MUD generalizes QPLEX and the number of SMMF channels (d) is a structural parameter, understanding its impact on capacity and training is important.

- **No discussion of limitations.** The paper does not acknowledge the computational overhead of MUD relative to QMIX, potential issues with the stop-gradient operator in MUD-StG, or any failure cases.

- **π(u|s) in Eq. 11 is not defined for the value-based setting.** In value decomposition, the policy is typically greedy; the paper should specify how w* is computed during training.

### Trivial
- The experiments section (line 224) lists "Ablation studies" as part 3, but no explicit ablation section appears.

## Nice-to-Haves

- Adding at least one standard MARL benchmark (e.g., SMAC scenarios) with multiple random seeds and error bars would substantially strengthen the empirical case.
- A formal derivation showing that the gradient-shaping forms (exponential decay, step-function) approximate optimization of a specific objective related to ORI would elevate them beyond heuristics.
- Reporting w* for all compared methods (not just MUD-SmG/StG) in the matrix game would strengthen the claim about ORI being the cause of QPLEX/MUD failure.
- Sensitivity analysis of the α hyperparameter in MUD-StG.

## Removed Points

These points are flagged to be removed, treat them with caution:

- **Theorem 3.3 proof deferred to appendix / cannot be verified.** Removed per hard rule: the parser strips appendix sections from all papers; proofs exist in the original submission. The paper's main text gives an intuitive explanation and figure, and the full proof is in the appendix of the original submission.

- **Missing hyperparameters, network architectures, training details / reproducibility nitpicks.** Removed per hard rule: the rule explicitly states to remove nitpicks about "undisclosed hyperparameters, trivial implementation details."

- **Missing related works (CDS, DOP).** Removed per hard rule: "DO NOT mention missing related works, as you do not have external sources to confirm their existence and could be making things up."

- **Formatting/style nitpicks, typos, notation inconsistencies (parser artifacts).** Removed per hard rule about parser errors and style nitpicks.

- **Criticism that MUD-SmG/StG are "ad hoc" heuristics.** Weakened and moved to Minor: the paper provides theoretical grounding (monotonic decrease of weight with ΔF) and empirical validation; the claim that they are purely "ad hoc" overstates the case.

- **Strength Finder claims that are generic or sycophantic (e.g., "the paper addresses an important problem").** Removed per soft rule: dropped strengths that are generic rather than grounded in specific evidence.

## Novel Insights

The two reviews, when combined, reveal a tension that is productive but under-explored in the paper itself. The Harsh Critic is correct that the experimental evaluation is far too thin to carry the claimed generality. However, neither review fully explores the following: the paper's core narrative arc (capacity characterization → complete capacity → ORI prevents realizing capacity → gradient shaping mitigates ORI) is logically elegant, but the evidential chain has a critical missing link. The toy game verifies the capacity characterization (contribution 1). The matrix game shows that complete-capacity methods (MUD, QPLEX) still fail due to ORI, and gradient shaping fixes it. But no experiment cleanly isolates whether ORI is *the* cause of failure versus other training dynamics (e.g., optimization landscape, reward sparsity, representation learning). The predator-prey result, while practically impressive, confounds multiple factors. A cleaner causal experiment — e.g., artificially manipulating w* while keeping the architecture fixed — would resolve this gap. Neither review explicitly identifies this specific missing causal isolation, which is the deepest unresolved question the paper raises.

## Suggestions

1. **Expand the experimental evaluation.** Add at least one standard benchmark (SMAC, LBF, or GRF) with multiple random seeds (≥5) and report mean/standard deviation. This single change would transform the empirical support from "suggestive" to "convincing."

2. **Clarify the decomposable vs. indecomposable cases in the toy game.** State explicitly what changes in the environment setup between the two conditions.

3. **Define π(u|s) in Eq. 11 clearly.** In value-based MARL, specify whether this is the behavior policy, target policy, or greedy policy during training, and explain how w* is computed in practice.

4. **Add an ablation on the channel dimension d** to show how many SMMFs are needed and the impact on performance.

5. **Include w* curves for all methods** (not just MUD-SmG/StG) in the matrix game experiment to strengthen the ORI argument.
