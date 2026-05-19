- Decision: Reject
- Avg Score: 4.75
- Scores: 6, 3, 5, 5
Now I have thoroughly verified everything against the paper. Let me produce the final consolidated review.

## Summary

The paper proposes SERA (Sample Efficient Reward Augmentation), a framework for offline-to-online RL that augments the environment reward with an intrinsic reward based on Q-conditioned state entropy, encouraging exploration during online fine-tuning. The method is designed as a plug-and-play module applicable to various model-free offline RL algorithms. Empirical results show that adding SERA improves online fine-tuning performance across several algorithms (CQL, Cal-QL, IQL, TD3+BC, AWAC, SAC) on D4RL tasks.

## Strengths

- **Plug-and-play versatility demonstrated across 6 algorithms**: SERA is tested with CQL, Cal-QL, IQL, TD3+BC, AWAC, and SAC, showing consistent improvement in online fine-tuning performance across all of them (Figure 4, Section 5.1). This provides reasonable evidence of generality beyond a single base algorithm.

- **Outperformance against prior offline-to-online specialized methods**: When combined with CQL, SERA achieves the highest aggregate score (83.8) compared to APL, PEX, and BR on Antmaze and Gym-MuJoCo tasks (Figure 7, Section 5.2), suggesting the reward-augmentation approach is competitive with more complex algorithmic frameworks.

- **Ablation validating the necessity of the pre-trained Q-network**: Figure 8(a) shows that using a randomly initialized Q-network for the intrinsic reward degrades performance below baseline, while using the offline pre-trained Q-network improves it. This directly supports the core design choice of leveraging the pre-trained critic for conditioning.

- **Rigorous aggregate statistical reporting**: The paper reports IQM, median, and mean with confidence intervals following Agarwal et al. (2022) (Figure 3), which goes beyond simple average reporting and strengthens the reliability of the aggregate claims.

- **Competitive with exploration baselines where compared**: In comparisons with RND, SE, and VCSE on IQL and AWAC (Figure 5b), SERA achieves the best performance on the selected tasks, providing evidence that the Q-conditioned design can outperform V-conditioned alternatives in this limited setting.

## Weaknesses

### Major

- **Incomplete method specification preventing reproducibility**: Equation (2), the core formula for the intrinsic reward, contains undefined notation. The term `n_v(i)` is not defined — the text later discusses `n_x(i)` (the k-th nearest neighbor index) but uses `n_v(i)` in the formula without explanation. The symbol `φ` (presumably the digamma function) is not introduced. The paper does not specify how the replay buffer is sampled for nearest-neighbor computation (e.g., whether all past states are stored or a subset is sampled). Without a complete, clear formulation, the method cannot be independently implemented or verified.

- **Theoretical claims are substantially overclaimed**: The paper asserts that SERA "implicitly implements State Marginal Matching (SMM) and penalizes out-of-distribution (OOD) state actions" (abstract). This is not supported by any derivation. Definition 5 defines "Approximate SMM" as maximizing unconditional state entropy, but SERA maximizes Q-conditioned state entropy — the gap between these is not explained. The paper offers no argument connecting Q-conditioned entropy to SMM or to OOD penalization. Additionally, Theorem 4.2 is essentially a standard property of double-Q networks (the minimum of two estimators is a lower bound w.r.t. each), which does not constitute "conservative policy improvement" in the offline RL sense of controlling OOD extrapolation error.

- **Insufficient justification for the central design choice (Q-conditioning over V-conditioning)**: The paper's core claim is that Q-conditioned state entropy is preferable to V-conditioned or unconditional state entropy for offline-to-online fine-tuning. Yet the explanation provided (Section 4.3) is vague: "encouraging the agent to consider the distinctions between decisions and states." The ablation in Figure 8(a) only validates that pre-training helps versus random initialization — it does not compare Q-conditioning to V-conditioning. The single comparison to VCSE (V-conditioned) in Figure 5(b) is limited to two base algorithms (IQL, AWAC) and a subset of tasks. This is insufficient to establish Q-conditioning as a generally superior design.

### Minor

- **Limited comparison to exploration baselines on primary algorithms**: Comparisons to RND, SE, and VCSE are conducted only with IQL and AWAC (Figure 5b), not with CQL or Cal-QL, which are the paper's primary algorithms where the largest gains are claimed. Since CQL/Cal-QL are the foundation of the main results, the lack of exploration-baseline comparisons on these algorithms weakens the evidence that SERA's specific design (vs. generic exploration bonuses) drives the improvement.

- **Number of experimental seeds and standard deviations are not reported**: Table 1 reports normalized scores after fine-tuning but does not specify the number of random seeds or provide standard deviations. While the aggregate plot (Figure 3) uses confidence intervals, the per-task results lack variance information, making it difficult to assess the reliability of individual task improvements.

- **Sensitivity to the k-nearest-neighbor hyperparameter**: The ablation (Figure 6) shows that performance is substantially affected by the choice of k (state cluster size), with optimal values varying by task (e.g., k=20 for walker2d, k=10 for hopper, k≈25 for antmaze-large-diverse). The paper acknowledges this but does not discuss how to select k in practice for new tasks, which reduces the plug-and-play appeal.

- **Theorem 4.1's optimality claim is ambiguous**: The theorem states the converged SERA soft policy is "optimal" but does not specify whether this is optimality with respect to the original MDP reward or the augmented reward. If the latter, the claim is trivial; if the former, no argument is provided that the intrinsic reward does not bias the policy away from the original objective.

### Trivial

- Inconsistent task count: The paper says "12 tasks" (Section 5) but the Figure 2 caption refers to "16 selected tasks."

## Nice-to-Haves

- An ablation studying sensitivity to the scaling coefficient λ would strengthen the hyperparameter analysis. The paper claims λ=1 works universally but does not test this.
- A discussion of failure cases or tasks where SERA might hurt performance would provide a more balanced presentation.
- Direct comparison to O3F (cited in the paper but not compared experimentally) would strengthen the competitive evaluation.

## Removed Points

These points were raised in the input reviews but are removed for the following reasons:

- **Missing proofs in appendix / per-task results in Table 10**: The parser strips appendix content from all papers; these exist in the original submission. Removed per instructions.
- **Standard deviation for Figure 7 aggregated chart**: The paper states per-task results are in Table 10 (appendix). The main paper's aggregate presentation is standard practice for space reasons.
- **Typos and formatting issues in equations**: These are PDF parser artifacts, not author errors.
- **Missing comparisons to ReBR**: Not a verifiable standard baseline in the context of this paper; the reviewer did not provide a citation.
- **Criticism that "the aggregate statistical plot masks variance per task"**: The paper provides per-task learning curves (Figure 2) alongside the aggregate plot; this is standard practice.
- **Strength about "theoretical guarantees" (from Strength Finder)**: Theorem 4.2 is a standard double-Q property, and Theorem 4.1's optimality is ambiguous. Neither constitutes a novel theoretical guarantee beyond what prior work (SAC) already established.

## Novel Insights

The harsh critic correctly identifies that the paper's theoretical framework — linking SERA to SMM and OOD penalization — is essentially unsupported window dressing. The genuine empirical insight is that a Q-conditioned entropy bonus, computed via a KNN-based KSG estimator using the offline pre-trained Q-network, consistently improves online fine-tuning across multiple base algorithms. However, the critic also surfaces that this empirical claim is weakened by the absence of exhaustive ablation on why Q-conditioning specifically (rather than V-conditioning or unconditional entropy) is necessary, and by the incomplete specification of the estimator itself. The tension between the paper's ambitious theoretical framing and its modest empirical comparisons is the central unresolved issue.

## Suggestions

1. **Complete the method specification**: Explicitly define every symbol in Equation (2), including `n_v(i)` and `φ`. Clarify how the replay buffer is maintained and sampled for nearest-neighbor computation.
2. **Scale back or properly support the theoretical claims**: Either remove the unsupported claims about SMM and OOD penalization, or provide a rigorous derivation connecting Q-conditioned state entropy to these concepts. Clarify what Theorem 4.1's optimality refers to.
3. **Strengthen the Q-vs-V comparison**: Add explicit comparisons between Q-conditioned and V-conditioned (VCSE) intrinsic rewards on CQL and Cal-QL, not just on IQL/AWAC.
4. **Report seed counts and standard deviations** in Table 1 for each task.
5. **Add exploration-baseline comparisons on the primary algorithms** (CQL, Cal-QL) to show that SERA's specific design, not just any exploration bonus, drives the reported improvements.
