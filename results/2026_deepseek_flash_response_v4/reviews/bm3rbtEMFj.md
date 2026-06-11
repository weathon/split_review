Now let me write the final consolidated review.

## Summary

ELMUR proposes a transformer decoder augmented with per-layer external memory embeddings, bidirectional token-memory cross-attention (mem2tok/tok2mem), and an LRU-based update rule using replacement or convex blending. It is evaluated via behavior cloning on the synthetic T-Maze, the MIKASA-Robo robotic manipulation suite (visual observations, continuous actions, sparse rewards), and the 48-task POPGym benchmark. The paper also provides a theoretical analysis establishing exponential forgetting bounds, a closed-form half-life expression, and memory boundedness guarantees. The core idea — per-layer persistent memory with LRU management — is clean, well-described, and the ablation study cleanly isolates the contributions of individual components.

## Strengths

1. **Extreme long-horizon retention on T-Maze (Figure 3):** ELMUR achieves 100% success rate on corridors up to 1M steps with a context window of only L=10 and S=3 segments, representing a ~100,000× horizon extension relative to the attention window. All baselines (RATE, DT, BC-LSTM, DMamba, TrXL) drop sharply as corridor length increases. This provides direct quantitative evidence that the external-layer-memory design delivers on the paper's central claim.

2. **Systematic ablation isolating each design component (Table 3, Figure 6):** The ablation cleanly attributes performance — removing LRU drops success from 1.00→0.43, removing both LRU and relative bias drops to 0.22, shared memory instead of per-layer drops to 0.45, while MoE→MLP preserves accuracy at 1.00±0.00. This confirms that the LRU write policy and per-layer design (not MoE blocks) are the critical ingredients.

3. **Strong results on disclosed MIKASA-Robo tasks (Table 1):** On the 4 reported manipulation tasks, ELMUR achieves the best success rate across all. The improvement on TakeItBack-v0 (0.78±0.03 vs. 0.42±0.24 for RATE) and RememberColor3-v0 (0.89±0.07 vs. 0.65±0.04) shows substantial margins on challenging visuomotor tasks.

4. **Inference speed advantage despite larger parameter count (Section 5.2 RQ4):** ELMUR (2.1M params) runs at 6.8±0.5 ms/step, faster than RATE (1.7M params, 7.2±0.3 ms) and DT (1.8M params, 10.7±0.1 ms), demonstrating that the memory mechanism does not impose a computational penalty.

5. **Theoretical guarantees on memory dynamics (Section 4):** The exponential forgetting bound (Proposition 1, Eq. 9), closed-form half-life (Corollary), effective horizon formula H(ε), and boundedness proof (Proposition 2) provide formal support beyond what most empirical RL/IL papers offer.

## Weaknesses

### Fatal
None.

### Major

1. **Inconsistent MIKASA-Robo task count and selective reporting in the main text.** The abstract (line 9) and introduction (line 27) state ELMUR achieves best success rate on "21 out of **23** tasks," but the main experiment section (Table 1 caption, line 236) references "all **32** MIKASA-Robo tasks" in the appendix. This internal inconsistency (23 vs. 32) is confusing and undermines trust in the aggregate claims. Furthermore, only 4 of these tasks appear in the main paper's Table 1. Among the 4 disclosed tasks, the picture is mixed: while ELMUR wins convincingly on RememberColor3-v0 (0.89) and TakeItBack-v0 (0.78), on RememberColor5-v0 and RememberColor9-v0 **all methods perform poorly** (<25% success), and ELMUR's reported advantage (0.19 and 0.23 vs. 0.10–0.17 for baselines) is small in absolute terms. The reader cannot verify the "about 70% aggregate improvement" and "21 of 23 tasks best" claims from the main text alone.

2. **λ values not reported for main experiments.** The paper's theoretical analysis centers on λ as the key hyperparameter governing retention (Proposition 1, half-life ~ M·L·ln2/λ, effective horizon H(ε) = M·L·ln(ε)/ln(1-λ)). However, the main T-Maze (Figure 3), MIKASA-Robo (Table 1), and POPGym (Table 2) experiments **do not state which λ value(s) were used**. The ablation (Figure 6a) varies λ on RememberColor3-v0, and Figure 6(b-d) explicitly fixes λ=0 "to isolate other effects" — but the operational λ for the headline results is absent. Since the theoretical half-life scales inversely with λ, knowing λ is necessary to interpret whether the 100% retention at 1M steps required an impractically small λ or a reasonable one. The paper directs to an appendix hyperparameter table (Table 7) that was not accessible in the reviewed version.

### Minor

3. **Missing GTrXL baseline.** GTrXL (Gated Transformer-XL) is a well-known memory-augmented transformer for RL that uses segment-level recurrence with gating. Its absence from the baseline set (which includes RATE, DT, DMamba, BC-MLP/LSTM, CQL, Diffusion Policy) is a gap. The paper would be stronger by including it or explaining its exclusion.

4. **MoE justification disconnected from results.** The paper motivates DeepSeek-MoE FFNs (line 92) as improving parameter efficiency, yet the ablation (Table 3) shows MoE→MLP yields identical accuracy (1.00±0.00). The speed advantage in RQ4 (6.8 ms vs. 7.2 ms for RATE) is partly attributable to MoE rather than the memory mechanism itself, since RATE uses standard MLP FFNs. The paper should disentangle memory-driven vs. MoE-driven efficiency gains.

5. **T-Maze result is predicted by theory and tests only 1-bit retention.** The paper frames the 100,000× horizon extension as a flagship result (abstract, introduction, conclusion). However, the theoretical analysis (Section 4) explicitly predicts this behavior — with λ=0.001, M=32, L=10, the effective horizon H_{0.01} ≈ 1.5M steps. The task tests whether a single bit (turn left/right) can be retained over a long corridor. This is a valid empirical sanity check of the theory, but it is not an empirical surprise. The framing should be adjusted to avoid overselling.

6. **Gradient detachment between segments is undiscussed.** The paper notes (line 82) that memory is detached via sg(m^{i-1}) between segments, meaning gradient flow does not propagate across segment boundaries. This implies long-horizon credit assignment must happen entirely through learned memory representations rather than gradient signals — a significant design tradeoff that the paper does not analyze or justify.

7. **No limitations section.** Section 7 (Conclusion) is purely forward-looking and positive. The paper would benefit from discussing known limitations — e.g., the dependence of retention on M and λ, the gradient detachment tradeoff, and the fact that all methods fail below 25% on RememberColor5/9 (suggesting a bottleneck beyond memory capacity).

### Trivial
- Inconsistent citation format: "Chen et al. 2021" (line 92) lacks parentheses used elsewhere.

## Nice-to-Haves
- Visualizing or analyzing what individual memory slots encode (do different slots specialize to different information types? Does the LRU policy evict the least useful information, or just the oldest?).
- Per-task breakdown of POPGym results to show which task types benefit most.
- A harder synthetic task requiring retention of multiple distinct cues (beyond 1-bit) over long horizons.

## Removed Points
These points were flagged for removal; treat with caution.
- **"λ=0 ablation creates regime fundamentally disconnected from main results":** The paper transparently states λ=0 is used "to isolate other effects" (line 261). This is a valid ablation design — studying capacity effects (M, σ, L-S) separately from blending effects. Figure 6(a) also varies λ, covering both regimes. The criticism overstates a disclosed experimental choice.
- **"CartPole-v1 tells nothing":** The paper explicitly frames this as a sanity check ("To confirm that memory mechanisms do not harm performance on fully observable MDPs," line 274). Standard practice. Removed.
- **"Theoretical analysis is not novel":** While straightforward, the analysis is cleanly presented and useful. The contribution is primarily architectural/empirical. Removed as a conflation of "not deep" with "not valuable."
- **"No analysis of what memory learns":** Standard in systems/modeling papers. Not a required analysis for acceptance.
- **Pure formatting/style nitpicks:** Removed per instructions.

## Novel Insights
None beyond the paper's own contributions. The reviews surface a consistent narrative: a clean architecture with strong empirical results, marred by reporting gaps (λ values, 23 vs. 32 inconsistency) and overselling of the T-Maze result, but with genuine strengths in the ablation methodology and theoretical grounding.

## Suggestions
1. Resolve the **23 vs. 32 task count inconsistency** between abstract and main text.
2. **Report λ values** used in all main experiments (T-Maze, MIKASA-Robo, POPGym).
3. Include the **full MIKASA-Robo table** (or a scatter plot of per-task gains) in the main paper.
4. Add **GTrXL** to baselines or justify its exclusion.
5. **Tone down the framing** of the T-Maze result from "flagship evidence" to "empirical verification of theoretical predictions."
6. Discuss the **gradient detachment tradeoff** for temporal credit assignment.
7. Add a **limitations paragraph** to the conclusion.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>