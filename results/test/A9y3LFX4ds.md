Now I have a clear picture. Let me produce the consolidated review.

## Summary

This paper introduces DiffuSearch, a discrete diffusion model for chess that predicts both the current action and a multi-step future trajectory (states and actions) conditioned on the current state. By using bidirectional self-attention and iterative denoising, the model leverages future context to improve next-action prediction without relying on explicit inference-time search (MCTS). The approach is validated on chess through extensive experiments, showing large-margin improvements over one-step policies and MCTS-enhanced baselines across action accuracy (+19.2% over one-step, +14% over MCTS), puzzle solving (+30%), and tournament Elo (+540).

## Strengths

1. **Large-margin empirical improvements across three independent metrics.** DiffuSearch consistently and substantially outperforms both searchless (S-A) and MCTS-enhanced baselines: 19.2% higher action accuracy than the one-step policy, 14% higher than MCTS, 30% more puzzles solved, and a 540 Elo gain in tournament play (Table 2). These gains are large and consistent across metrics, making a strong case that the method captures something useful beyond standard behavioral cloning.

2. **Systematic ablations identify the essential components.** The paper carefully ablates future paradigms (Table 3), future world quality (Table 4), and training methods (Table 5). Key findings include: (a) modeling both future states and actions (S-ASA) is critical — future actions alone (S-AA) collapse to 15.07%; (b) oracle world dynamics are necessary, random dynamics yield no improvement; (c) discrete diffusion with linear λ_t substantially outperforms continuous diffusion and direct prediction. These ablations provide actionable design guidance beyond the chess domain.

3. **Analysis reveals concrete efficiency advantages over explicit search.** Figure 3 shows that DiffuSearch continues to improve with increased context length (implicit depth) while MCTS plateaus after ~50 simulations, and DiffuSearch's latency grows only modestly with depth while MCTS latency rises steeply. This efficiency advantage is a concrete, measured benefit (per-move timing on identical hardware) that directly motivates the approach.

4. **Methodologically clean comparison setup.** All neural models use the same GPT-2 architecture, the same data, and the same optimizer, ensuring that differences are attributable to the proposed diffusion-based future modeling rather than architectural or optimization confounds.

## Weaknesses

### Fatal
None.

### Major
1. **The "implicit search" framing is substantially overclaimed.** The paper repeatedly describes DiffuSearch as performing "implicit search" as an alternative to explicit search algorithms like MCTS. In reality, the model is trained to generate a single optimal future trajectory and takes the first action — there is no exploration of alternative branches, no comparison of different futures, no backpropagation of outcomes, and no iterative refinement based on value estimates. The paper's technical contribution (using discrete diffusion with bidirectional attention to leverage future context for action prediction) is solid, but the "search" framing conflates prediction of a plausible future with *search*, which in this domain implies systematic reasoning over multiple possibilities. The paper attempts to motivate the analogy (e.g., Figure 1, Section 4.4 analysis of attention layers as "implicit search depth"), but the evidence does not support the strong claim that the model "searches" in any sense that would be recognized by the AI search community. This is not merely a presentation issue — it is the paper's stated central conceptual contribution (Contribution 1, lines 30–31), and it is unsupported by the evidence presented. The paper would be stronger if it reframed DiffuSearch as a method for *lookahead-aware action prediction via conditional diffusion* rather than as a search algorithm.

### Minor
1. **Missing control for bidirectional attention without diffusion.** The paper shows that an autoregressive transformer trained on the same S-ASA sequences achieves 27.39% accuracy (vs. 22.10% for S-A), and DiffuSearch achieves 41.31%. The 13.9-point gap between the autoregressive baseline and DiffuSearch is attributed to the diffusion objective, but this confounds two factors: (a) bidirectional attention (the autoregressive baseline uses causal attention) and (b) the multi-step denoising objective. A control experiment using a bidirectional transformer trained on the same S-ASA input but with a prediction head only on a_i (no requirement to denoise the future) would isolate the contribution of the diffusion objective from the contribution of bidirectional attention alone. The existing ablations partially address this (Table 5 compares training methods), but not this specific confound.

2. **Inference-time decision rule is heuristic with limited justification.** The paper uses argmax_{a_i,z_i} p_θ(a_i,z_i|s_i) as a proxy for the intractable marginal p_θ(a_i|s_i). The paper acknowledges the intractability and provides the intuition that "the best future if one action is taken" can be reflected by the joint, but provides no formal justification or empirical validation that this proxy correlates well with action quality or marginal action probabilities. An analysis showing that sampling multiple futures and aggregating first actions yields similar or better results would strengthen confidence in this design choice.

3. **Limited statistical rigor.** Tournament Elo is computed from 400 games per pair without confidence intervals. Puzzle accuracy is reported as a single number without error bars. Scaling plots (Figure 3, right) show individual runs without variance. Given the moderate dataset sizes (10k–100k games), adding confidence intervals or standard deviations across multiple seeds would help assess the reliability of the reported gains.

4. **The MCTS baseline, while standard, uses a deliberately weak value network.** The MCTS-enhanced policy uses the S-V model trained on the same limited data (10k games) as its value network, which achieves only 21.45% action accuracy on its own. The paper's main comparison thus contrasts DiffuSearch (trained on optimal Stockfish trajectories) with MCTS using a weak value function. While this comparison is standard and follows prior work (Ruoss et al., 2024), the claim that DiffuSearch "outperforms explicit search" should be caveated: it outperforms MCTS *given the same limited training data for the constituent neural components*. A comparison against MCTS with a value network trained on the full 100k dataset would better test whether DiffuSearch truly substitutes for explicit search.

5. **Puzzle evaluation protocol could be clearer.** The paper reports "puzzle accuracy" as the percentage where the policy's action sequence matches the known solution. It is not fully specified whether the model generates the entire multi-step sequence in one diffusion call (and is compared as a plan) or plays interactively against a simulated opponent. Although the former interpretation is suggested by the description "action sequence exactly matches the known solution action sequence," the distinction matters for interpreting what the metric measures (multi-step prediction accuracy vs. interactive problem-solving).

### Trivial
None.

## Nice-to-Haves

- An analysis of whether sampling multiple futures and voting on the first action (rather than taking the single joint-argmax sample) improves accuracy would strengthen the connection to multi-branch search.
- A comparison against MCTS using a value network trained on the 100k dataset (the same data scale used in the scaling experiments) would better isolate whether DiffuSearch's advantage over explicit search persists with better value estimates.
- Error bars or confidence intervals on the main results would improve the paper's empirical rigor.

## Removed Points

- **Criticism about "MCTS baseline is deliberately weak and comparison is unfair":** The reviewer claimed the comparison is unfair because the MCTS baseline uses a weak value network. However, this is the standard experimental setup from prior work (Ruoss et al., 2024), and the comparison is controlled: all models are trained on the same data budget. The reviewer's suggestion to use Stockfish as a value function inside MCTS is comparing against the oracle used to generate the training data, which would be an unreasonable baseline. The claim is retained in softened form as Minor issue #4 above.

- **Criticism about "the appendix being stripped by parser":** Removed per instructions — the parser strips appendix content from all papers; they exist in the original submission.

- **Criticism about "data leakage" (puzzles from same time period as training games):** This is speculation with no evidence that the paper's evaluation is invalid. The puzzles are from a standard benchmark (Ruoss et al., 2024). Removed as unsupported speculation.

- **Criticism about "the paper trains on 10k games but cites Ruoss et al. using 10M games":** This is a factual observation about data scale, not a weakness. The paper explicitly acknowledges this as a limitation in the conclusion (line 200). Removed.

- **Strength Finder's framing of "implicit search" as a core strength:** This directly conflicts with the verified Major weakness above. When a strength and weakness disagree, the weakness wins. The strength is reformulated to describe the technical achievement (discrete diffusion enabling context-aware action prediction without inference-time search) rather than the contested "implicit search" framing.

## Novel Insights

Beyond the paper's own contributions, the most interesting takeaway from the reviews is the tension between two valid perspectives: the paper's empirical results are genuinely impressive and well-ablated, showing the method captures long-term dependencies that a one-step policy and even MCTS (with a learned value network) miss. Yet the "implicit search" framing sets up expectations the method cannot meet because it lacks the defining property of search — systematic exploration and comparison of alternatives. This tension suggests that the paper's most valuable contribution is not "search without search" but rather a demonstration that explicitly training a policy on multi-step optimal trajectories with bidirectional attention and iterative denoising can produce behavior that *looks like* it was guided by lookahead, without the computational cost of actual search. This reframing would make the paper both more honest and more interesting: it shows that the right training objective can compress search-like behavior into a single forward pass.

## Suggestions

1. **Reframe the core contribution.** Replace "implicit search" with more precise language such as "lookahead-aware action prediction" or "future-conditioned policy via discrete diffusion." The technical contribution is strong enough to stand on its own without overclaiming a conceptual connection to search algorithms.

2. **Add the missing control experiment.** Train a bidirectional transformer on the same S-ASA format with a prediction head only on a_i (no future denoising objective). Compare to DiffuSearch to isolate the contribution of the diffusion objective from the contribution of bidirectional attention.

3. **Add empirical validation of the inference rule.** Show that the joint argmax correlates reasonably with action quality (e.g., compared against Stockfish's evaluation), or show that sampling multiple futures and aggregating first actions gives similar results.

4. **Report confidence intervals or error bars** for the main results (action accuracy, puzzle accuracy, Elo). At minimum, provide standard deviations across multiple runs for the primary comparisons.

5. **Clarify the puzzle evaluation protocol** — specify whether the model outputs a full multi-step sequence in one call that is compared to the solution, or whether it interacts with a simulated opponent.

## Score and Decision

**Originality:** The idea of using discrete diffusion to predict multi-step future trajectories for action selection is novel, though it builds on established work in diffusion-based trajectory prediction (Diffuser, Decision Diffuser, Diffusion Policy).

**Importance:** The research question — whether generative modeling of future trajectories can substitute for explicit search — is timely and important, especially given growing interest in search-like capabilities for LLMs.

**Claims support:** The empirical results are well-supported by experiments and ablations, but the central conceptual claim ("implicit search") is overclaimed relative to the evidence.

**Soundness:** The experimental methodology is generally sound, with controlled comparisons, but missing a key control (bidirectional attention without diffusion) and lacking statistical rigor.

**Clarity:** The paper is clearly written, though the central framing is misleading.

**Value:** The technical contribution and empirical results are valuable to the community. The paper demonstrates a promising direction for incorporating future information into action prediction without inference-time search costs.

The paper has a solid technical contribution and strong empirical results. However, the central conceptual claim is substantially overclaimed in a way that affects how the contribution should be evaluated. The weaknesses are addressable in revision, and the underlying methodology is sound. The paper would benefit from reframing and additional controls, but the core results are credible and interesting.

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>