## Summary
TD-JEPA introduces a temporal-difference (TD) latent-predictive representation learning approach for zero-shot unsupervised RL. Unlike prior work that relies on one-step prediction, on-policy data, or a single task, the core contribution is a novel TD loss that enables multi-step, policy-conditioned latent prediction from offline, reward-free transitions. Built on this, the algorithm trains a state encoder, a separate task encoder, a policy-conditioned multi-step predictor, and parameterized policies jointly in latent space—enabling zero-shot reward optimization via linear regression at test time. The paper provides formal guarantees (non-collapse, successor measure factorization, policy evaluation bounds) and demonstrates competitive performance on 65 tasks across 13 datasets from ExoRL and OGBench, with especially strong gains in pixel-based settings.

---

## Strengths

- **Principled off-policy multi-step prediction**: The shift from MC-JEPA (requires on-policy rollouts) to TD-JEPA (requires only offline transitions) is the central algorithmic contribution and is rigorously motivated. The Bellman-bootstrap decomposition that makes this possible is clearly derived and connects naturally to established TD theory for successor features.

- **Comprehensive and unified theoretical analysis**: Four theorems cover different aspects of the method: optimal predictor characterization (Th. 1), non-collapse under proper initialization (Th. 2), relationship between TD-JEPA gradients and successor-measure TD losses (Th. 3), and a policy evaluation error bound (Th. 4). The "gradient matching" argument (Theorems 1 and 3) that connects the latent-predictive losses to non-latent-predictive successor measure losses is particularly elegant and reportedly subsumes and generalizes all prior theoretical analyses of latent-predictive representations.

- **Strong pixel-based results across diverse domains**: TD-JEPA achieves the top aggregate performance on DMC-RGB (628.8 vs. next best 582.4) and matches the state of the art on OGBench-RGB, across locomotion, navigation, and manipulation. The probability-of-improvement analysis (Figure 2) robustly confirms statistical superiority in visual domains, addressing the common problem of outliers masking aggregate trends.

- **Well-motivated dual-encoder architecture**: The paper provides both theoretical intuition (separate dimensionality and content for state control vs. task abstraction) and empirical support (Figure 3 right, showing consistent gains from the asymmetric design). The ablation against the symmetric (shared-encoder) variant isolates the benefit cleanly.

- **Fast adaptation with frozen encoders**: Section 6 demonstrates that pre-trained state representations transfer efficiently to new tasks—often without fine-tuning—improving sample efficiency significantly over training from scratch. This is a meaningful practical benefit beyond zero-shot performance.

---

## Weaknesses

### Fatal
None.

### Major
1. **Strong and potentially limiting theoretical assumptions**: Theorems 1 and 3 require a uniform state distribution (A2) and symmetric transition kernels (A3)—the latter being atypical for most practical RL environments (e.g., deterministic policies on directional dynamics). The non-collapse guarantee (Th. 2) further assumes that predictors are re-optimized to convergence at each representation update step, which is not how the practical algorithm works. While the authors note these can be relaxed in the appendix, the main text leaves open the question of how much performance degrades as these assumptions are violated, and whether the theoretical guarantees remain informative in realistic settings.

2. **Mixed proprioceptive manipulation results**: In OGBench proprioceptive (goal-reaching with precise manipulation), TD-JEPA notably lags on cube-single (34.20 vs. HILP's 74.20, BYOL-γ*'s 79.40), cube-double (3.60 vs. HILP's 20.00), and antmaze-me (20.20 vs. FB's 51.60). The method matches HILP's aggregate OGBench score (37.98 ≈ 37.98) but this masks significant underperformance on tasks requiring precise long-horizon goal-reaching with proprioception. No clear explanation is offered for this failure mode.

### Minor
1. **Non-collapse result is only partial**: Theorem 2 shows that covariance matrices are preserved over time—i.e., they do not go to zero if initialized non-degenerate. It does not show that representations converge to useful, diverse solutions (non-trivial content). "Proper initialization" is stated informally as "unitary covariance," but the practical implications for non-trivial random initializations in deep networks are not discussed.

2. **Evaluation protocol partially changes baselines**: All baselines are augmented with an explicit state encoder that they were not originally trained with, and this yields substantial improvements for some methods (up to 2.4×). This is a fair methodological choice for isolating encoder quality, but it means the reported baseline numbers differ substantially from published results, making cross-paper comparison harder and leaving some ambiguity about what drives performance—encoder architecture vs. training objective.

### Trivial
None worth noting.

---

## Nice-to-Haves
- An empirical study of the sensitivity to the orthonormality regularization coefficient λ across domains would help practitioners understand robustness.
- The paper briefly mentions that BYOL-γ* implements a bi-directional update that TD-JEPA cannot, but quantifying this difference (rather than just discussing it in Appendix C.3) would strengthen the technical comparison.

---

## Novel Insights
The "gradient matching" theorems (Th. 1 and 3) are a genuine theoretical contribution beyond the paper's practical claims. By showing that gradient descent on latent-predictive objectives—both Monte Carlo and TD—produces exactly the same update direction as minimizing the corresponding non-latent-predictive successor measure approximation loss, the paper provides a clean, unified justification for why these objectives work. This result subsumes prior analyses for single-policy, one-step, or on-policy settings and extends them to multi-policy, multi-step, off-policy dynamics. Theorem 4 then closes the loop from successor measure approximation quality to policy evaluation error, creating a provable chain from the training objective to zero-shot optimality. This theoretical spine connects the JEPA paradigm (originally introduced for vision) to successor feature theory in a way that could inform future unsupervised RL method design.

---

## Suggestions
- Analyze or discuss when the symmetric-transition-kernel assumption approximately holds in practice, and empirically test whether performance degrades as this assumption is violated (e.g., comparing on environments with highly asymmetric dynamics).
- Provide error bars or ablations on the number of policy parameters (z-samples per batch) to understand sensitivity to the policy diversity term.
- Investigate the OGBench proprioceptive manipulation gap more explicitly—is it a coverage issue (low-coverage datasets), a task-structure mismatch with the linear reward assumption, or a training instability?

---

## Score and Decision

TD-JEPA is a well-executed paper that integrates latent-predictive learning with successor feature theory in a novel and principled way. The TD formulation enabling off-policy multi-step prediction is a meaningful algorithmic advance over prior work. The theory is thorough and offers real explanatory value; the experiments are broad and the pixel-based results are compelling. The weaknesses—strong theoretical assumptions, and underperformance on proprioceptive manipulation—are real but do not invalidate the core contributions.

MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>