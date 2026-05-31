## Summary
This paper introduces CORectifier, a novel Neural Combinatorial Optimization (NCO) solver trained using a "Rectified Reinforcement Learning" (RRL) paradigm. The method addresses reward sparsity and exploration challenges in RL-based solvers by hierarchically injecting high-quality expert sub-trajectories (at batch, instance, and intra-instance levels) into the RL training process. By probabilistically replacing segments of model-generated trajectories with expert sequences while maintaining feasibility checks, the framework manages to combine the sequential decision-making flexibility of RL with the strong guidance of supervised signals.

## Strengths
- **Improved Scalability for Sequential RL Solvers:** The method achieves a significant breakthrough in scaling RL-based constructive solvers. For instance, on TSP-500, it reduces the optimality gap by approximately 90% compared to traditional RL baselines (e.g., 4.92% vs. 16-48% for POMO/Vaswani et al.), narrowing the performance gap between RL and state-of-the-art supervised heatmap methods.
- **Hierarchical and State-Aware Guidance:** The tri-level rectification strategy (batch, instance, and intra-instance) is more sophisticated than standard teacher forcing. Specifically, Equation 10 ensures that expert actions are only injected if they are feasible within the model's current state, allowing the policy to learn how to recover and integrate expert fragments even after deviating from the expert path.
- **Improved Exploration Dynamics:** Empirical evidence in Figure 6 demonstrates that the method actually increases trajectory entropy and provides a clearer advantage signal. This suggests that the guidance acts as a "ladder" to high-quality regions of the solution space rather than causing premature mode collapse.
- **Broad Applicability and Generalization:** The framework is validated across five distinct COPs (TSP, ATSP, PCTSP, CVRP, KP) and shows robust zero-shot generalization on real-world datasets like TSPLIB and CVRPLIB. It is also shown to be backbone-agnostic, improving performance when applied to AM, POMO, and MatNet.

## Weaknesses

### Fatal
None.

### Major
- **Computational Overhead of Training:** While the paper emphasizes sample efficiency and inference speed, it lacks a quantitative analysis of the wall-clock training time overhead. The rectification process involves several additional steps during training (mask generation, expert lookups, and feasibility checks). Comparing the training time of CORectifier against vanilla POMO or Sym-NCO is necessary to fully evaluate the trade-off of the proposed supervision.

### Minor
- **Ambiguity in Intra-instance Succession for Non-permutation Problems:** In Section 3.2.1, the "Recommended Action Retrieval" step describes retrieving the "direct successor" of the previous action $a_{i,j,t-1}$ from the expert tour $\tau^*$. While this is clear for permutation-based problems like TSP, it is less clear how this maps to problems like CVRP where nodes may be visited multiple times (e.g., the depot) or where the "successor" depends on the specific route structure.
- **Heuristic Quality Sensitivity:** The method relies on reference solutions from oracle solvers (Concorde, HGS, etc.). The paper would benefit from discussing the impact of "noisy" or sub-optimal experts (e.g., using a mid-tier heuristic instead of an exact solver). This is practically important for complex COPs where exact solutions are unavailable even for training scales.
- **Hyperparameter Sensitivity in Asymmetric Problems:** For ATSP, the rectification probabilities ($p_{batch}$, $p_{inst}$) were set significantly higher (0.5) compared to other tasks (0.1). A more detailed explanation as to why asymmetric problems require such "harder" guidance would provide better insight into the method's behavior across different problem geometries.

### Trivial
None.

## Nice-to-Haves
- A wall-clock training time comparison table to complement the sample efficiency claims.
- An experiment showing performance using a weaker heuristic as the "expert" to test robustness.

## Removed Points
These points are flagged to be removed, treat them with caution:
- *Weakness about unfair comparison (Heatmap vs RL):* The reviewer noted comparisons with heatmap methods. This was removed as a weakness because the paper intentionally evaluates a sequential solver against a different paradigm (heatmap) where sequential solvers usually fail, and the results show the proposed method closing a significant portion of that gap.
- *Nitpicks on missing implementation details:* Most implementation details are present in the appendix (referenced in the text); those that are slightly ambiguous (like successor mapping in CVRP) are demoted to minor.

## Novel Insights
The core insight is that for combinatorial optimization, supervised signals are most effective when treated as "decomposable fragments" rather than rigid templates. By injecting these fragments at various granularities while the agent is exploring, the framework avoids the exposure bias of pure teacher forcing and the "blind" search of pure RL. The finding that expert guidance can actually *increase* trajectory entropy by providing more informative advantage signals is a counter-intuitive but significant observation for the design of hybrid learning algorithms in discrete spaces.

## Suggestions
- Quantify and report the training time overhead introduced by the rectifier relative to vanilla RL backbones.
- Clarify the implementation of "direct successor" retrieval for problems where nodes can be visited multiple times or where the trajectory involves visiting a central depot (e.g., CVRP).
- Briefly discuss or experiment with the effect of expert solution quality on the final performance of the RRL agent.

## Score and Decision
The paper addresses a long-standing bottleneck in RL for Combinatorial Optimization (scalability and reward sparsity) with a well-grounded hierarchical supervision mechanism. The empirical results, especially on TSP-500, are a major leap over current RL baselines.

**Calibration and Bracketing:**
In Round 1, the paper was bracketed between 6.0 and 8.0.
- `AloCXPpq54` (avg 6.0): A hierarchical RL paper for stochastic CO. CORectifier is more extensive in its evaluation (5 tasks vs 1-2) and shows more substantial improvements over established SOTA like POMO.
- `pbDqZBn2X2` (avg 5.75): A hybrid RL/Diffusion paper. It was rejected partly due to limited novelty in the RL fine-tuning phase. CORectifier’s "rectification" mechanism is more novel than standard fine-tuning.
- `jKhNBulNMh` (avg 6.67): Learns symbolic policies for branching. Strong scores (6, 8, 6). CORectifier is technically sounder in its empirical breadth and addresses a more central problem (solution construction vs branching policy).

**Final Score Determination:**
The paper is noticeably stronger than the 5.5-6.0 anchors due to the magnitude of the improvement on large scales (TSP-500 gap reduced from ~20% to ~5%). It is more similar to higher-end papers that introduce robust, general-purpose training paradigms.

**Anchors retrieved:**
1. `/home/wg25r/split_review_opus_repro/datasets/deepreview_13k_calibration/AloCXPpq54.md` (6.0): Similar hierarchical RL theme; CORectifier has significantly broader evaluation and more impressive scaling results. 
2. `/home/wg25r/split_review_opus_repro/datasets/deepreview_13k_calibration/jKhNBulNMh.md` (6.67): Strong hybrid ML4CO paper; CORectifier is comparable in significance and execution.
3. `/home/wg25r/split_review_opus_repro/datasets/deepreview_13k_calibration/pbDqZBn2X2.md` (5.75): Hybrid RL fine-tuning; CORectifier is more novel and rigorous.
4. `/home/wg25r/split_review_opus_repro/datasets/deepreview_13k_calibration/NdcQQ82mfy.md` (5.67): Hybrid RL/IL for branching; CORectifier covers more tasks and has higher impact on constructive solvers.
5. `/home/wg25r/split_review_opus_repro/datasets/deepreview_13k_calibration/CJEBFNBLhO.md` (4.25): Parallel environments for scalability; much lower technical depth than CORectifier.

MY FINAL SCORE: <score>7.5</score>
MY FINAL DECISION: <decision>Accept</decision>