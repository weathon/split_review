Now I have a clear picture. Let me synthesize the final review.

## Summary

This paper proposes a reinforcement learning framework for automated code refactoring that combines contrastive pre-training of code graph embeddings with a composite reward function and a graph-attention policy network. The key idea is to pre-train a syntax-guided contrastive encoder on unlabeled code graphs, then use the learned embeddings as part of an RL reward signal and policy input to improve refactoring quality. The method achieves 83.7% syntactic improvement and 93.8% semantic preservation on the Refactory dataset, outperforming the baselines reported.

## Strengths

- **Empirical gains are consistent and non-trivial across multiple datasets.** Table 1 shows the proposed method outperforms all baselines on all five metrics (SI, SP, ED, MG, GS). Table 2's ablation study confirms that removing contrastive pre-training causes the largest single drop (SI −7.5 points), providing specific evidence that the learned representations drive the advantage over handcrafted-feature methods.

- **Cross-language transfer without fine-tuning is demonstrated.** Table 3 reports that a model pre-trained on Java (CodeSearchNet) evaluated zero-shot on Python and C++ outperforms language-specific rule-based tools (PyLint, Cppcheck), showing genuine generalization that earlier RL-based refactoring methods do not claim.

- **The ablation study is informative and mostly well-structured.** Table 2 systematically removes each component (contrastive pre-training, embedding rewards, semantic tests, guided exploration), giving a clear picture of which pieces contribute to which metrics. The drop in SP when semantic tests are removed (−8.6 points) is particularly instructive.

## Weaknesses

### Fatal

None.

### Major

1. **The exploration strategy (Eq 6) does not define a distribution over actions.** The RHS of Eq 6, `π_explore(a|s) ∝ exp(−½ (h_s − h*)ᵀ Σ⁻¹ (h_s − h*))`, depends only on the current state embedding `h_s` and a prototype `h*`; there is no dependence on the action `a`. The expression is a density over *states*, not actions. The paper never explains how this quantity is converted into action probabilities. Since the exploration strategy is claimed as a contribution (Section 4.3, "embedding-guided exploration") and the ablation (Table 2) shows that replacing it with random exploration degrades MG (−6.1 points), this is not a minor presentational slip — the mechanism cannot be implemented as described. This must be resolved either by specifying how the state density induces action probabilities or by removing the claim of embedding-guided exploration.

2. **Evaluations lack any measure of variance or statistical reliability.** Table 1 reports single numbers with no error bars, confidence intervals, or multiple-seed statistics. Figure 1 shows only one trajectory per method. Given the well-known high variance of RL training, single-run comparisons are not reliable evidence for the claimed superiority. This is especially concerning because several metric margins are modest (e.g., SI 83.7% vs. NeuroRefactor's 79.4% — a 4.3 point gap that could easily fall within one standard deviation).

3. **The symbolic-execution-based semantic preservation check is claimed but entirely unvalidated.** Section 4.5 proposes generating test cases through symbolic execution (Cadar & Sen, 2013) and comparing execution traces. No runtime statistics, coverage numbers, failure rates, or timeout analyses are reported. Symbolic execution of arbitrary code faces well-known path explosion problems and struggles with loops, recursion, and external libraries. The paper provides no evidence that this component is actually used in the experiments, how much it costs, or how frequently it succeeds. Without this validation, a core component of the reward function (the `−γ(1−δ_t)` term) rests on an unsubstantiated practicality claim.

### Minor

1. **The embedding dynamics reward lacks a principled motivation.** Equation (5) includes a term `α tanh(β Δh_t)` that rewards movement in the latent embedding space. The paper's justification ("gradient stability") explains the choice of tanh, but not why moving far in embedding space should be rewarded. The ablation shows it contributes a modest positive effect (+4.2 SI), but the paper does not analyze what `Δh` actually measures or why maximizing it correlates with code improvement. The reported Pearson correlation of r=0.72 (Figure 2) is measured on the trained policy's own trajectory and may be tautological.

2. **No analysis of what the learned embeddings capture.** For a method that centers on representation learning (contrastive pre-training + embedding-guided policy), the paper provides no t-SNE/UMAP visualizations, nearest-neighbor probes, or probing tasks to characterize what the encoder learns. The claim that embeddings are "refactoring-aware" is not directly supported.

3. **Notation in Equation (7) is ambiguous.** The expression `[W_h ‖ W_q] h_j` concatenates matrices `W_h` and `W_q` (dimensions unclear) and then applies a dot product with `a`. The description "attention weights decide how nodes aggregate information from their syntactic neighbors when they are amounting correct refactoring actions" is not a coherent explanation. This does not invalidate the overall approach but would hinder reproduction.

4. **The paper does not report runtime or computational cost of training/inference.** Given the complexity of the pipeline (graph construction, contrastive pre-training on 2M functions, 1M RL environment steps, symbolic execution per step), a discussion of feasibility and compute budget would be valuable.

### Trivial

None.

## Nice-to-Haves

- Comparing against RL baselines that also have access to the same pre-trained GNN encoder would help isolate the effect of contrastive pre-training from the method's other design choices.
- A random-embedding baseline in the ablation (replacing the contrastive encoder with a randomly initialized GAT) would strengthen the claim that pre-training, not just graph architecture, drives the gains.
- Sensitivity analysis for the main hyperparameters (τ, α, β, γ, reward weights w_q) would increase confidence in the reported configuration.

## Removed Points

These points are flagged to be removed, treat them with caution:
- **Citation quality concerns** (Marvellous et al. on researchgate.net, Kupari et al. on GitHub Pages): Per the hard rules, questioning the existence of cited references is not permitted.
- **Criticism that the method optimizes the same metrics used for evaluation**: This is partially true but common in RL for code — the reward is *designed* to optimize quality metrics. The cross-language results (Table 3) and the generalization score provide independent validation. The point about baseline asymmetry is partially addressed by the ablation study.
- **"Embeddings are static during RL, weakening guidance claim"**: A fixed encoder during RL is standard practice (it's the representation, not the encoder, that is used). The embeddings do "guide" exploration through the state representation itself — this criticism misunderstands the setup.
- **Qualitative case studies are "textbook patterns"**: Finding known patterns is valid evidence that the method works correctly; requiring discovery of "non-obvious" patterns is not a necessary criterion.
- **"No state-of-the-art comparison from 2024-2025"**: The paper cites baselines from 2022-2024; the reviewer has no external basis to assert that stronger baselines exist.
- **Missing related work**: I cannot verify the existence of omitted references.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. **Fix the exploration strategy.** Either define how Eq (6) induces a distribution over actions (e.g., by interpreting the state-density value as an exploration bonus or as a multiplicative factor on the base policy's action probabilities), or remove the claim of embedding-guided exploration and use standard ε-greedy or entropy-bonus exploration with the embeddings used only as state representations.

2. **Add statistical rigor.** Report all main results (Table 1, Table 2) with mean and standard deviation across at least 5 random seeds. Include confidence bands in the learning curves (Figure 1).

3. **Validate or replace the symbolic execution component.** Provide concrete evidence that the semantic preservation check works on the evaluated codebases: report coverage rates, average compute time per check, timeout rates, and any fallback mechanism used. If symbolic execution is impractical at RL scale, replace it with a feasible alternative (e.g., compiler-based equivalence checking, bounded model checking on small methods, or test generation from existing test suites).

4. **Redesign or ablate the embedding dynamics reward.** Either provide a principled justification for why `Δh_t` should be maximized (e.g., as an exploration bonus grounded in information gain or count-based exploration theory), or remove the term and report the method's performance without it as the primary configuration.

5. **Add embedding analysis.** Include a visualization (t-SNE) of the learned embedding space showing how refactored and unrefactored code positions relate, and at minimum a nearest-neighbor study to demonstrate what the encoder treats as "similar."

## Score and Decision

**Calibration Report**

Round 1 bracketing placed the paper between low (<3.5) and middle (3.5–7.5) band anchors, with the strongest topical similarities to CodeRule-RL (avg 4.00, Reject) and CUDA-L1 (avg 3.50, Accept Poster).

Round 2 narrowing considered 3 additional anchors: "Refactoring Codebases Through Library Design" (avg 5.50, Reject), "Behavioral Embeddings of Programs" (avg 4.67, Accept Poster), and "UniRTL" (avg 4.00, Reject). The current paper is weaker than the 5.50 anchor (which has a cleaner method and human-study validation) and comparable to the 4.00-level anchors (CodeRule-RL, UniRTL). The CUDA-L1 anchor at 3.50 is the closest match in terms of severity of methodological issues: both papers have one clearly flawed component (Eq 6 here; method/data conflation in CUDA-L1) and evaluation gaps. The current paper is slightly stronger than CUDA-L1 in experimental coverage but has a more fundamental method-specification gap.

Final score positioned at **3.5**, reflecting that the exploration strategy is not implementable as written, the evaluation lacks statistical rigor, and a claimed core component (symbolic execution) is unvalidated — three issues that collectively undermine confidence in the method's claims.

MY FINAL SCORE: <score>3.5</score>
MY FINAL DECISION: <decision>Reject</decision>