## Summary

This paper proposes PQN (Parallelised Q-Network), a simplified Q-learning algorithm that eliminates both the replay buffer and target network by combining vectorized parallel environments with LayerNorm and ℓ₂ regularization. The authors provide a theoretical analysis showing that LayerNorm bounds off-policy and nonlinear TD instability (scaling as O(1/√k) with network width k), and prove existence of a stabilizing width for regularized two-layer critics. Empirically, PQN is evaluated across Atari, Craftax, and multi-agent domains (Overcooked, Hanabi, Smax), demonstrating competitive performance with substantially reduced wall-clock time and memory footprint.

## Strengths

1. **First rigorous analysis of how LayerNorm stabilizes TD without target networks.** Lemma 1 (lines 148–154) provides explicit O(1/√k) bounds showing that LayerNorm suppresses both off-policy instability and nonlinear instability. Theorem 1 (line 161) establishes that for sufficiently wide LayerNorm critics, the TD stability criterion holds. This formalizes the "deadly triad" intuition in terms of Jacobian conditions and goes beyond prior empirical observations (Fellows 2023, Lyle 2023/2024, Bhatt 2024) by providing a provable guarantee.

2. **PQN is a genuinely simple and clean algorithm with strong empirical support across diverse domains.** Algorithm 1 is essentially vectorized Watkins Q-learning with a normalized network — strikingly simpler than DQN, Rainbow, or PPO. The evaluation spans Atari (full 57-game suite), Craftax, Overcooked, Hanabi, and Smax — broader coverage than typical Q-learning papers. The replay buffer ablation (lines 336–337) directly validates the core design choice: adding a buffer causes a ~6× training slowdown in Craftax with no performance gain.

3. **Principled distinction between LayerNorm and BatchNorm, with supporting ablations.** Section 3.3 explains why BatchNorm requires additional tricks (double Q-learning, batch renormalization) to stabilize TD, creating a gap between theory and practice that does not exist for LayerNorm. The ablation in Atari-10 (line 331) confirms that BatchNorm can degrade performance, while LayerNorm consistently helps. This provides practical guidance beyond the specific PQN algorithm.

## Weaknesses

### Fatal
None.

### Major

1. **The theoretical guarantees are proven for a two-layer network, but PQN uses deeper architectures in practice, and the paper's attempt to bridge this gap is insufficient.** The analysis in Section 3 considers a specific architecture: one LayerNorm hidden layer of width k with a linear readout (lines 142–147). The paper asserts (line 147) that "Deeper networks with more LayerNorm layers may be used in practice, however our analysis reveals that only the final layer weights affect the stability of TD with wide LayerNorm neural networks." This claim is presented as flowing from the theory, but the theory explicitly analyzes only the two-layer case. Extending the O(1/√k) bound or the existence guarantee (Theorem 1) to deep CNNs with multiple LayerNorm layers and nonlinearities would require nontrivial additional analysis that is not provided. The "Convergence: Yes" entry for PQN in Table 1 (line 218) inherits this ambiguity: the convergence guarantee applies to the regularized TD update in the proven architecture, not necessarily to the deep networks used in the experiments. This gap weakens the central narrative that theory directly justifies practice. **(The empirical results remain interesting independently, and the paper does transparently describe the architecture analyzed, so this is not fatal — but it is a significant overreach in how the theory is presented.)**

### Minor

2. **Several comparative claims rest on statistically thin evidence.** The Craftax result reports 16% (PQN-RNN) vs. 15.3% (PPO-RNN) — a 0.7% absolute difference — with no measure of variance, confidence intervals, or effect size (line 290). The Atari-10 claim that "PQN outperforms PPO in terms of sample efficiency, final score, and training time" (line 278) is presented without error bars despite using only 3 seeds. While 3-seed reporting is common in ALE papers, the strong comparative language would benefit from uncertainty quantification, especially given the tight margin in Craftax.

3. **The "50× faster" headline claim conflates multiple sources of speedup that are not disentangled.** The Atari speed comparison (Table, lines 374–386) compares PQN (JAX-based, 128 parallel environments, pure-GPU end-to-end) to a traditional DQN pipeline (single CPU environment, GPU training). The table caption honestly states this, but the paper never isolates what fraction of the 50× gain comes from algorithmic simplifications (removing the replay buffer and target network) vs. infrastructure improvements (parallel environments, JAX compilation, pure-GPU pipeline). A controlled baseline — a modern vectorized DQN that keeps the replay buffer and target network but uses the same JAX/parallel infrastructure as PQN — would clarify this. Without it, a reader cannot tell whether the core message is "our algorithmic simplifications are faster" or "parallelization + JAX is faster (which applies to any algorithm)." The Craftax buffer ablation (lines 336–337) partially addresses this for that domain, showing a 6× slowdown from the buffer alone, but no equivalent exists for Atari.

### Trivial
None.

## Nice-to-Haves

- A controlled speed ablation for Atari: compare PQN to a vectorized JAX DQN that retains the replay buffer and target network but uses the same environment parallelism. This would disentangle infrastructure gains from algorithmic gains and strengthen the paper's central claim about the replay buffer being the main bottleneck.
- Reporting interquartile means (IQM) or confidence intervals for the Atari-10 and Craftax comparisons, especially for the tight Craftax margin (16% vs. 15.3%).

## Removed Points

These points were flagged during review but removed after verification against the paper:

1. **"Paper never isolates what the algorithmic removal of the replay buffer contributes to speed"** — Factually incorrect. The Craftax ablation (lines 336–337) directly compares PQN with and without a replay buffer, showing a ~6× slowdown from the buffer. This criticism is removed.
2. **"Comparison to Ape-X is misleading"** — Ape-X is mentioned once in passing (line 278) as an example of sample-inefficient distributed Q-learning, not as a primary speed baseline. This is a minor remark, not a central comparison. Removed.
3. **"Proofs entirely deferred to appendix"** — This is standard practice at ICLR given page limits. The paper clearly states where proofs are located and provides intuition in the main text. Removed.
4. **"Convergence: Yes table entry is misleading"** — The table compares algorithms, and PQN uses the regularized TD update for which convergence is proven. The entry is defensible given what is claimed. Removed.
5. **"BatchNorm vs LayerNorm discussion is qualitative"** — The paper does relate this to the theoretical analysis of running statistics vs. per-instance normalization. Removed as overly harsh.
6. **Several formatting/style nitpicks** about parser artifacts (stray \end{align} on line 142, missing equation reference). These are parser issues, not author errors. Removed.

## Novel Insights

The reviews surface one observation that goes beyond the paper's own framing: the theory-practice gap here is structurally similar to a recurring tension in RL theory papers — a clean theoretical result for a simplified architecture is presented alongside an algorithm that works in practice with a much richer architecture. The paper's claim that "only the final layer weights affect stability" for deeper networks is presented as a consequence of the analysis, but it is actually a conjecture that would require additional composition arguments. Recognizing this pattern could help the authors (and the field) be more precise about what the theory covers vs. what remains an empirical observation. The paper's strength is that it does not hide this gap entirely — the architecture is clearly stated — but it papers over it in the narrative framing.

## Suggestions

1. Explicitly delineate the scope of the theoretical guarantees: state clearly that Theorem 1 applies to the two-layer architecture analyzed, and characterize the deeper-network claim as a motivated conjecture supported by empirical results rather than a proven corollary.
2. Add an Atari speed ablation comparing PQN to a vectorized JAX DQN baseline that retains replay buffer + target network, to isolate the algorithmic speed contribution.
3. Report variance (e.g., interquartile mean or confidence intervals) for the Craftax and Atari-10 comparisons where strong comparative claims are made.

## Score and Decision

This paper makes a genuine contribution: a novel theoretical analysis of LayerNorm's stabilizing effect on TD, paired with a clean, practical algorithm that is well-validated across diverse domains. The main weakness — a gap between the theory's scope (two-layer networks) and the practical architecture (deep networks) — is real and should be honestly delineated, but it does not undermine the empirical contributions or the theoretical insight as stated. The paper would benefit from tighter statistical reporting and a cleaner speed decomposition, but these are addressable. I recommend acceptance.

MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>