Now I have a thorough understanding of the paper. Let me produce the consolidated final review.

## Summary

This paper identifies and analyzes "reward collapse" in RLHF — the phenomenon where reward models trained on preference rankings produce prompt-independent reward distributions during the terminal phase of training. The authors provide a theoretical analysis showing that, under an overparameterization assumption where the per-prompt ranking objectives are exactly maximized, the reward distribution converges to a prompt-independent form determined solely by the utility function, yielding closed-form Beta or endpoint-mass distributions. They propose "prompt-aware" optimization — using different utility functions for different prompt types — as a principled solution. Synthetic experiments with response length as ground-truth reward validate that collapse occurs in a trained DeBERTaV3 reward model and that prompt-aware training can separate reward distributions across prompt types.

## Strengths

- **Formal identification and theoretical characterization of a genuine phenomenon.** The paper rigorously defines reward collapse and traces it analytically to the prompt-independent structure of the ranking-based objective when each per-prompt problem is exactly optimized. The closed-form limiting distributions (Beta for power/negative-power utilities, mass at endpoints for log-sigmoid) are clean and lead to testable predictions.

- **Theoretical predictions match observed empirical behavior.** The paper demonstrates that neural network training with different utility functions produces reward distributions qualitatively matching the theory: power utilities yield polarized/smooth Beta shapes, negative-power utilities yield near-uniform distributions, and log-sigmoid yields probability mass at the endpoints. This agreement between a per-prompt scalar analysis and actual multi-prompt neural network training is nontrivial and supports the theory's relevance.

- **Principled prompt-aware solution derived from the same framework.** The proposed approach of making the utility function prompt-dependent follows directly from the same optimization analysis used to predict collapse. The solution is grounded in theory rather than heuristic, and the synthetic experiments confirm it produces distinct reward distributions for open-ended vs. concrete prompts.

- **Rigorous convergence and uniqueness results.** Theorem 4 establishes, under bounded strongly concave utilities, that the limiting reward distribution exists, is unique, and solves a variational problem — a clean theoretical contribution independent of neural network details.

## Weaknesses

### Fatal
None.

### Major

1. **The theoretical explanation relies on an assumption whose validity is unverified.** The argument reduces the multi-prompt neural network objective to independent per-prompt scalar problems by assuming the network is "sufficiently overparameterized" to exactly maximize each per-prompt objective. A neural network shares parameters across prompts, and whether it can simultaneously realize the exact per-prompt optima for all prompts is neither justified theoretically (no reference to any overparameterization result) nor tested empirically. Without this link, the paper is analyzing a per-prompt decoupled problem and *observing* that neural networks also exhibit collapse, but the causal mechanism may differ (e.g., limited capacity, optimization dynamics, dataset biases). The claim that theory "predicted" collapse before experiments confirmed it is therefore imprecise — the theory predicts collapse of the per-prompt scalar problem, and the experiments show collapse in neural network training, but the connection between the two remains correlational.

2. **Experimental validation is too narrow to support the paper's practical claims.** All experiments use response length (word count) as the ground-truth reward, with two hand-crafted length distributions to simulate open-ended and concrete prompts. This is a single one-dimensional, deterministic, perfectly observable signal — far from the multidimensional, noisy, and often inconsistent human preferences in real RLHF. No experiments are conducted on standard RLHF datasets (e.g., HH-RLHF, WebGPT, SHP). The paper frames reward collapse as practically important for LLM alignment, but the evidence only supports its existence in a highly synthetic setting. The Discussion acknowledges computational constraints, but the gap between the claimed generality and the experimental scope is large.

3. **No demonstration that reward collapse degrades downstream RLHF performance.** The paper asserts that collapse is "clearly undesirable" and "potentially lead[s] to miscalibration," but provides no experiment showing that collapse harms alignment quality, calibration, or any downstream metric. Without evidence that collapse actually causes problems, the practical motivation — and the case for prompt-aware optimization as a *solution* rather than just an alternative — is weakened.

### Minor

1. **No quantitative metric for collapse.** The paper relies on visual inspection of histograms to assert that distributions have "converged" or are "identical." Metrics like average pairwise Wasserstein distance between per-prompt reward distributions, or variance of per-prompt mean rewards, would make comparisons across utility functions rigorous and reproducible.

2. **No quantitative goodness-of-fit between theory and experiment.** The paper claims the predicted Beta and endpoint-mass distributions are validated empirically, but provides no quantitative comparison (e.g., KL divergence, two-sample KS test) between the theoretical limiting distributions and the neural network's empirical reward distributions. This would directly test whether the theory explains the observed collapse.

3. **Prompt-aware approach requires an oracle for prompt type.** The synthetic experiments distinguish prompt types by appending fixed phrases ("Write the answer in an open-ended way" / "Write either a short answer or a long answer"), which is a perfect oracle. No method for automatically detecting prompt open-endedness in real data is proposed or tested. The paper acknowledges this as future work, but it remains a significant gap for practical deployment.

4. **Early stopping is mentioned but never evaluated.** The paper frames prompt-aware optimization as "superior to early stopping" but provides no comparison against early stopping as a baseline. It is therefore unclear whether prompt-aware training offers meaningful practical advantages over the simpler strategy.

### Trivial

- The paper could benefit from a table summarizing which utility function corresponds to which limiting distribution, for quick reference.

## Nice-to-Haves

- An experiment on a real RLHF dataset (e.g., HH-RLHF) with a practical proxy for prompt open-endedness (e.g., question length, a small classifier) would dramatically strengthen the practical relevance.
- A two-sample statistical test (KS test) on whether per-prompt reward distributions from the trained model are distinguishable, before and after collapse.
- An ablation on whether prompt-aware training introduces optimization instabilities (competing parameter updates across different $U_\text{prom}$ choices).

## Removed Points

- **"BTL extension has no experimental validation at all"** (from Harsh Critic): The paper presents Figure 6 (fig:pairwise_comparison) with numerical results for the BTL extension. While these are on the scalar optimization problem rather than neural network training, the claim of *no* validation is inaccurate. Downgraded: the point about limited scope is folded into Major weakness #2.
- **"Theorems 1–3 only characterize scalar problem, not neural network training"**: This is restating what the theorems say. The theorems are about the optimization program (4), and the paper is transparent about this. The gap between theory and practice is covered in Major weakness #1.
- **Nature of reward distribution observations in Figure 4 being "qualitative"**: Visual inspection is standard in ML papers documenting training dynamics. The quantitative metric request is preserved in Minor weakness #1.

## Novel Insights

The most interesting observation that emerges from the reviews is the tension between the paper's two audiences: the theory is genuinely clean and produces closed-form predictions that match neural network behavior in a controlled setting, but the paper frames itself as addressing a practical RLHF problem. The reviews collectively suggest that the paper's strongest contribution is the theoretical identification and analysis of collapse in the per-prompt optimization limit — a genuine mathematical finding — while the practical framing and claims are not well-supported. A more honest paper might present itself as a theoretical study with synthetic validation, making the practical connection a speculation rather than a central claim.

## Suggestions

1. **Add a quantitative bridge between theory and experiments.** Compute the KL divergence between the theoretical Beta/endpoint distributions and the empirical reward distributions from the trained DeBERTaV3 model. Show these as a function of training epoch — this would directly test whether the theory explains collapse in the neural network.

2. **Add one experiment on a real RLHF dataset.** Even a small-scale experiment on HH-RLHF with a simple proxy for open-endedness (e.g., question length, or a small classifier on prompt text) would substantially improve the practical credibility.

3. **Provide a quantitative collapse metric.** Report, for example, the average pairwise Wasserstein distance between per-prompt reward distributions at the end of training, comparing fixed-utility vs. prompt-aware approaches.

4. **Reframe the claims to match the evidence.** Either present the paper primarily as a theoretical study (adding quantitative validation) or invest in the experiments needed to support practical claims. The current framing sits uncomfortably between the two.

## Score and Decision

**Originality**: Strong. The identification of reward collapse and its theoretical analysis are novel.
**Importance**: Moderate. The phenomenon is interesting, but its practical significance for real RLHF is unsubstantiated.
**Claims**: Overclaimed relative to evidence, particularly regarding practical relevance and the theory's causal role.
**Soundness**: The theory is sound for the per-prompt scalar problem. The link to neural network training is plausible but unproven. Experiments are sound for the synthetic setting but narrow.
**Clarity**: Clear writing, well-structured.
**Value**: The theoretical results are a genuine contribution. Practitioners may find the analysis insightful even without real-data validation.

The paper makes a genuine theoretical contribution and identifies an interesting phenomenon. However, the gap between the theoretical analysis (per-prompt decoupled optimization) and the claimed practical significance (neural network training behavior that harms real RLHF) is significant, and the experiments are too narrow to bridge it. The paper would be best served by repositioning as a theoretical study with synthetic validation.

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>