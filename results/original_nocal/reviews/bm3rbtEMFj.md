Now I have all the information I need. Let me write the final consolidated review.

## Summary

ELMUR extends a GPT-style transformer with per-layer external memory embeddings, bidirectional token-memory cross-attention (mem2tok/tok2mem), and a Least Recently Used (LRU) update rule that fills empty slots then blends new content via convex combination. The architecture is evaluated on T-Maze (synthetic long-horizon recall), MIKASA-Robo (visual robotic manipulation with sparse rewards), and POPGym (48 puzzle/control tasks). The headline result is 100% success on T-Maze corridors up to 1M steps using a context window of only L=10 tokens — an effective horizon 100,000× beyond the attention window — alongside best-on-21-of-23-task performance on MIKASA-Robo and top aggregate scores on POPGym.

## Strengths

1. **Extreme horizon extension on T-Maze.** With a context of only L=10 tokens and S=3 segments (30 training steps), ELMUR achieves 100% success on corridors up to 1M steps (Figure 3), outperforming every baseline (RATE, DT, BC-LSTM, TrXL, DMamba, etc.) that collapses at far shorter lengths. This directly supports the central claim of retention far beyond the attention window.

2. **Dominant performance on visual manipulation with sparse rewards.** On the MIKASA-Robo suite (Table 1), ELMUR achieves the best success rate on 21 of 23 tasks and improves the aggregate rate by ~70% over the previous best baseline. The TakeItBack-v0 result (0.78 vs. 0.42 for the next-best) and RememberColor3-v0 (0.89 vs. 0.65) provide concrete evidence that the architecture handles delayed reversal and multi-distractor recall with pixel inputs.

3. **Formal stability guarantee.** Proposition 2 proves that under convex blending the norm of every memory embedding remains uniformly bounded by the input norm, ensuring stability across arbitrarily long trajectories — a property not provided by most prior memory-augmented transformers.

4. **Controlled ablation isolating each component.** Table 3 and Figure 6 systematically ablate per-layer vs. shared memory, LRU vs. no LRU, relative bias, and MoE vs. MLP on RememberColor3-v0. Removing LRU alone drops success from 1.00 to 0.43, and removing both LRU and relative bias drops to 0.22, providing precise evidence for the value of each design choice. The hyperparameter sensitivity analysis (M, λ, σ, segment configuration) in Figure 6 reveals a clear capacity-threshold effect (M ≥ N needed for stability).

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

1. **Unexplained discrepancy in RememberColor3-v0 reported scores.** The main result (Table 1) reports ELMUR at 0.89±0.07 (3 runs × 100 episodes each), while the ablation study (Table 3) reports the baseline ELMUR at 1.00±0.00 (3 runs × 20 episodes each). The paper does not reconcile this difference. The ablation section states "Results average three runs of 20 episodes" vs. the main protocol's 100 episodes, but the text does not explain whether the models themselves differ (checkpoint selection, training seeds) or whether the 1.00 arises from the coarser 20-episode evaluation of an 89%-reliable model. While this is not internally contradictory (fewer evaluation episodes inflates apparent performance, especially for a strong model), the lack of explanation is a reporting gap that should be addressed.

2. **No explicit discussion of λ and M used in the T-Maze experiment.** The paper defers hyperparameters to Appendix Table 7 (standard practice), but the T-Maze 1M-step result is the paper's flagship claim, and readers cannot immediately verify whether the memory budget is plausible (e.g., M=22 with λ=0.001 yields a theoretical retention horizon well beyond 1M steps, easily fitting within the stated 2.1M parameters; but this reasoning is not provided). A brief note or worked example in the main text connecting the theory of Section 4 to the actual numbers would strengthen the paper.

3. **Figure 3 omits error bars for ELMUR.** The paper's own evaluation protocol (Section 5.1) specifies reporting "mean ± SEM across three run means." If ELMUR achieves exactly 100% on all runs, the SEM is 0, which can be stated in the caption. Other baselines have visible variance, so the omission stands out.

### Trivial

None.

## Nice-to-Haves

- Provide a worked example of the effective horizon formula (Proposition 1) instantiated with the actual M, λ, L used in the T-Maze experiment, to bridge theory and the flagship result.
- Visualize which memory slots are visited during a long T-Maze trajectory to illustrate how the cue slot avoids overwrite.
- Normalize POPGym aggregate scores (Table 2) per-task or report interquartile mean to account for differing reward scales, though this follows the benchmark's own reporting standard.

## Removed Points

These points were flagged by the reviewers but are removed with justifications:

- **T-Maze missing M and λ is a fatal flaw.** Removed because the paper explicitly states hyperparameters are in Appendix Table 7, which is stripped by the parser — the original submission contains them. Additionally, the critic's mathematical argument that small λ "cannot explain perfect 100% success" is incorrect: with λ=0.001, the effective retention horizon formula gives H(0.01) = M·10·4602, so M≈22 suffices for 1M steps — well within the 2.1M parameter count.
- **T-Maze generalization (Figure 4) missing M and λ.** Same justification — values in appendix.
- **No LRU configuration is undefined.** Removed because the paper explicitly states that "Removing LRU leaves stale entries" — the replacement is simply no update, which is a valid ablation.
- **Only 4 of 32 MIKASA-Robo tasks shown.** Removed because Table 8 in the appendix (stripped by parser) contains all 32 tasks; showing key examples in the main text is standard practice.
- **POPGym aggregation uses raw sums.** Removed because this is the benchmark's own reporting standard; the paper follows the established protocol.
- **Missing confidence intervals in Figure 3 for ELMUR.** Demoted to Minor/Trivial because 100% success across all runs yields zero variance, so no error bars are needed; the caption should simply state this explicitly.
- **Proposition 2 is trivial.** Removed because boundedness guarantees are a standard sanity-check result in such papers and the value is in making it explicit, not in mathematical novelty.

## Novel Insights

None beyond the paper's own contributions. The reviews surface no unexpected interpretation or cross-cutting observation that the authors themselves do not already present.

## Suggestions

1. Reconcile the RememberColor3-v0 discrepancy: explain whether the 0.89±0.07 (Table 1) and 1.00±0.00 (Table 3) arise from the same trained models evaluated at different episode counts, or from different checkpoint/seed selections, and clarify the evaluation protocol for each table.
2. Add a brief inline calculation showing the theoretical half-life/effective horizon for the T-Maze configuration (e.g., "with M=..., λ=..., L=10, the half-life is ... steps, exceeding the 1M-step test corridor"), connecting Section 4 directly to Figure 3.
3. Note in the Figure 3 caption that ELMUR's SEM is zero because all runs achieve 100% success.
4. Consider reporting POPGym results with per-task improvement relative to random or the best baseline, alongside the raw sum, for easier interpretability.

MY FINAL SCORE: <score>7.5</score>
MY FINAL DECISION: <decision>Accept</decision>