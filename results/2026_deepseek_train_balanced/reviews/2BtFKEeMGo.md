Here is the final consolidated review.

---

## Summary

This paper proposes a constraint-based formulation for programmatic weak supervision — replacing latent generative models (e.g., Snorkel) with accuracy-bound constraints on each weak labeler. The authors develop an alternating minimization algorithm that projects model predictions onto constraint-satisfying distributions via KL-divergence, and provide theoretical analysis of the constrained function class. Experiments on 8 text classification datasets from WRENCH show competitive performance against Majority Vote, Snorkel, and LoL(S).

## Strengths

1. **Novel constraint-based formulation avoids generative-model assumptions**: Unlike prior work requiring conditional independence or parametric mixture-model assumptions, the paper's formulation only needs per-weak-labeler accuracy bounds (Section 2, equations 2 and 4). This is a genuinely different and arguably simpler inductive bias for weak supervision.

2. **Elegant continuous relaxation of the discontinuous constraint problem**: The conversion of discontinuous accuracy-bound constraints into a continuous KL-divergence projection loss (Lemma 3.1, Proposition 3.7) enables gradient-based optimization. The exponential tilting solution (Proposition 3.7) is particularly clean and non-trivial.

3. **Empirical competitiveness and robustness**: On 8 WRENCH datasets, Ours(V) outperforms Snorkel, MV, and LoL(S) (Table 1). The method degrades gracefully under noisy ηⱼ estimates (Figure 2), which is practically important since accuracy bounds from domain experts will be approximate.

4. **Generalization analysis with practically computable diagnostic terms**: Theorem 4.6 extends error guarantees beyond weak labeler coverage via Wasserstein distances, and the terms t_f(S) and u_f(S) can be computed from unlabeled data — an unusual and useful diagnostic property.

## Weaknesses

### Major

1. **Theory-algorithm gap**: The theoretical analysis (Section 4) characterizes the idealized constrained function class $\tilde{\mathcal{F}}$ under exact constraint satisfaction. However, the practical algorithm (Section 3.2) uses a one-step parallel Newton-Raphson update that "does not give an exact projection" (line 199). There is no analysis of: (a) whether the alternating minimization converges to a feasible point of $\tilde{\mathcal{F}}$, (b) the approximation error of the projection step, or (c) conditions under which the approximate projection yields a near-feasible solution. Lemma 3.2 only shows monotonic decrease of the objective, not convergence to a stationary point or to feasibility. This decouples the paper's strongest formal claims from what the algorithm is provably doing.

2. **Theorem 4.5 (conflict-based error improvement) assumes constant weak labelers**: The theorem showing that conflicting weak labelers improve error bounds via the subtraction term is proven only when each weak labeler predicts a constant label ($g_j(X) = j-1$, line 281). Real weak labelers are input-dependent functions that label specific patterns, not constants. The brief suggestion to merge same-label weak labelers into a "super weak labeler" does not address this limitation — the underlying assumption that predictions do not vary with input remains. As stated, the theorem does not support the paper's broader claims about denoising effects of multiple input-dependent weak labelers.

3. **The validation-label dependency is undertreated**: The validation set (size 100) is used for both (a) estimating per-weak-labeler accuracy bounds ηⱼ (for Ours(V)) and (b) tuning all hyperparameters (learning rate, weight decay, epochs, α). While the comparison against Sup(V) is a good control, the paper does not analyze how performance degrades with smaller validation sets (e.g., 10, 50 points). The Beta(1,2) prior for ηⱼ estimation is mentioned but not motivated or analyzed for sensitivity. This makes it unclear how much labeled data is truly needed for the method to work.

### Minor

4. **Limited experimental breadth**: Only 3 baselines are compared despite WRENCH including FlyingSquid, MeTaL, WeaSEL, CAGE, etc. Only text classification datasets (8 datasets) are tested — no vision, medical, or other modalities are evaluated despite the method being formulated generically. Only a single architecture (1-hidden-layer network, hidden size 16, on frozen BERT embeddings) is used. This limits how broadly the claimed superiority can be asserted.

5. **The realizability assumption (Lemma 4.2) is not discussed**: The lemma requires $f^* \in \tilde{\mathcal{F}}$ for zero error on the agreement region. This strong assumption is neither validated nor discussed in terms of when it might hold or fail in practice.

6. **Robustness experiment tests only symmetric noise**: The ablation (Figure 2) adds uniform noise symmetrically around ηⱼ, but systematic over- or under-estimation (e.g., all bounds are too optimistic) would be a more realistic failure mode and is not tested.

### Trivial

None.

## Nice-to-Haves

- A sensitivity analysis on validation set size (e.g., 10, 50, 100, 200) used for ηⱼ estimation would directly address the question of how much labeled data is needed.
- Comparison to self-training or semi-supervised baselines would help isolate the benefit of the constraint projection from the benefit of using unlabeled data generally.

## Removed Points

These were raised in the reviews but removed after cross-checking against the paper:
- **"Circular formulation"**: One reviewer argued the constraints contain the quantity being minimized, making the formulation circular. This misunderstands the formulation — constraints bound the model's disagreement with weak labelers, not with the true label. These are distinct quantities.
- **"Connection to noisy labels never developed"**: The paper uses noisy-label learning as inspiration in the introduction. This is context-setting, not a claimed contribution.
- **"Section 3.1 on ILP is disproportionate"**: A style/presentation nitpick without substance.
- **"Wasserstein distance terms may be irregular for complex classifiers"**: Speculative concern without evidence in the paper.
- **"The Lipschitz bounds are diagnostic not predictive"**: This is true of most generalization bounds in ML theory; not a specific weakness of this paper.
- **Strength about Theorem 4.5 as "provable benefit of multiple weak labelers"**: This strength is partially valid but is overstated given the theorem's limiting assumption of constant weak labelers. The remaining strengths are retained.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. Provide convergence analysis of the alternating minimization algorithm, or at minimum characterize the fixed points and conditions under which the approximate projection yields a near-feasible solution.
2. Expand experimental evaluation to include more WRENCH baselines (FlyingSquid, MeTaL) and at least one non-text modality.
3. Include a sensitivity analysis on the validation set size used for ηⱼ estimation.

## Score and Decision

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>