- Decision: Reject
- Avg Score: 4.75
- Scores: 3, 5, 5, 6
Now I have thoroughly verified all claims against the paper. Here is my consolidated final review.

---

## Summary

This paper introduces GCIP, a framework that learns sparse subgraphs for GNN-based graph classification by formulating the problem as a bi-level optimization: an inner loop trains a classifier on a subgraph, while an outer loop uses a policy-based RL agent (PPO) to decide which nodes or edges to remove. Two hyperparameters, λ and d, give practitioners direct control over the balance between sparsity and accuracy. The framework supports both node-level and edge-level removal. On nine graph classification benchmarks, GCIP achieves accuracy competitive with full-graph methods while using substantially fewer nodes or edges (e.g., node ratios below 30% on several datasets).

---

## Strengths

- **Bi-level optimization with explicit control parameters (Equations 3–4, Figures 3–4).** The nested structure cleanly separates the sparsity objective from the performance objective, directly addressing the paper's stated limitation that prior methods "do not allow practitioners to directly control the trade-off between predictive performance and sparsity." The ablation study empirically validates that both λ and d steer the solution toward sparser or more accurate regimes as intended (e.g., d=0.05 yields ~5% remaining nodes/edges).

- **Two distinct removal policies for node-level and edge-level sparsification (Section 4.2.1).** The paper provides clear formulations for both modes, broadening applicability (e.g., edge removal preserves all nodes, enabling potential use for node classification tasks). The combinatorial complexity of each setting is acknowledged.

- **Competitive accuracy with substantially sparser subgraphs (Tables 1–2).** Across nine datasets, GCIP_E achieves the best average ranking among sparse models (shared with TopK_hard), and GCIP_N consistently achieves the highest sparsity ranking — often using fewer than 30% of nodes. This supports the claim that the method "competes in performance … while relying on significantly sparser subgraphs."

- **Stable training dynamics (Figure 2).** The evolution plots for accuracy, PPO reward, and node/edge ratio across training epochs show smooth convergence by epoch 800, indicating that the bi-level optimization procedure works as intended without instability.

---

## Weaknesses

### Fatal
None.

### Major

- **Reproducibility gap: PPO and bi-level optimization details are underspecified.** The paper states "We employ gradient descent for both optimizations, with a larger learning rate for the inner optimization" (Section 4.1) but does not specify: (i) how often the RL policy is updated relative to the classifier (alternation schedule), (ii) PPO-specific hyperparameters (clip epsilon, number of epochs per update, batch size, GAE λ), (iii) whether reward normalization is used, or (iv) learning rate schedules for either optimization. These omissions make independent reimplementation unnecessarily difficult.

- **No statistical significance testing for accuracy comparisons.** Table 1 reports means and standard deviations from 5-fold cross-validation, but the paper does not perform any significance test (e.g., Wilcoxon signed-rank). Given that many entries show overlapping standard deviations, it is unclear whether observed differences between methods are reliable.

### Minor

- **Interpretability is measured only through the sparsity proxy; no direct evidence is provided.** The paper explicitly equates sparsity with interpretability (line 12: "interpretability in this context is linked to graph sparsity"; line 182: "Reducing the node and edge ratio percentages … making the models more interpretable") and argues that hard removal (no information leakage from omitted parts) makes the subgraph self-contained. This is a reasonable premise, but the paper does not provide qualitative examples of learned subgraphs (e.g., do they correspond to meaningful functional groups in molecular datasets?), human evaluation, or interpretability-specific metrics such as fidelity or stability. The paper's framing repeatedly emphasizes "interpretability," but the evaluation only demonstrates controllable sparsity.

- **"Up to 10x faster inference" claim is unsupported.** Line 190 states that "GCIP is at least as fast as SUGAR in training, and up to 10 times faster in inference," but no timing measurements, tables, or comparisons are provided. This claim cannot be assessed or reproduced.

- **Theoretical concern with the reward function at λ=0 is not discussed.** When λ=0, the reward reduces to R_s when the sparse prediction is correct and -R_s when it is incorrect (Equation 5). The paper does not analyze the degenerate possibility that the agent could achieve high reward by removing all information and relying on the classifier being correct by chance (e.g., 1/K on a balanced dataset). Empirically, the paper shows this does not occur (line 171: "Even for λ=0.0, around 15–20% of nodes and edges persist"), but the theoretical gap is worth acknowledging.

### Trivial
None.

---

## Nice-to-Haves

- Include qualitative visualizations of learned subgraphs, especially on molecular datasets, to directly support the interpretability claim.
- Add fidelity and stability metrics commonly used in the interpretability literature.
- Provide actual training and inference time measurements with standard deviations.
- Discuss or ablate the scalability of the policy to larger graphs (the largest dataset used is DD with ~500 nodes; the independent-Bernoulli policy assumption may weaken on graphs with thousands of nodes).

---

## Removed Points

The following points from the original reviews are removed with justification:

- **"Hyperparameter tuning procedure biases the comparison" (Harsh Critic #2).** The paper tunes the GNN classifier hyperparameters on GIN and applies them to all methods. Because this procedure favors the baseline (GIN) over the author's method (GCIP), the asymmetry makes GCIP's comparison *harder*, not easier. Per the filtering rules, an asymmetry that disadvantages the author's method is not a valid weakness. The paper also transparently acknowledges this: "This procedure partially explains GIN's superior performance."

- **"The discussion of SUGAR is somewhat dismissive" (Harsh Critic, Related Work).** This is a subjective editorial judgment, not a verifiable weakness, and is removed.

- **"Missing parts" about alternative policy architecture and scalability analysis (Harsh Critic, Missing Parts #4–5).** These are suggestions for additional experiments that go beyond what is required for a sound evaluation of the paper's stated contribution. They are moved to Nice-to-Haves.

---

## Novel Insights

None beyond the paper's own contributions. The reviews surface a genuine gap between the paper's interpretability framing and its sparsity-only evaluation, but this is a limitation already implicit in the paper's own definition of interpretability. The main technical contribution — controllable sparsification via bi-level RL optimization with λ and d — stands on its own.

---

## Suggestions

1. **Add PPO hyperparameters and alternation schedule** to the experimental setup (or supplementary material), including: PPO clip epsilon, number of epochs per PPO update, learning rates for both inner and outer optimization, reward normalization details, and the update frequency ratio between the RL policy and the classifier.
2. **Perform statistical significance tests** (e.g., Wilcoxon signed-rank) on the accuracy comparisons across datasets to substantiate claims about relative performance.
3. **Provide timing measurements** to support the "up to 10x faster inference" claim, or remove the claim if evidence cannot be included.
4. **Include at least a qualitative analysis** of the learned subgraphs (e.g., example subgraphs from molecular datasets with known functional groups) to bridge the gap between sparsity and the paper's interpretability framing.

---
