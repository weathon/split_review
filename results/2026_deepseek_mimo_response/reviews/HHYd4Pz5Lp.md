Now I have all the calibration I need. Let me write the final review.

## Summary

DelRec introduces the first surrogate-gradient-learning (SGL) method for training axonal/synaptic delays in recurrent connections of spiking neural networks. The method uses a differentiable triangle interpolation with an annealing width parameter σ to handle non-integer delays during training, rounding to integers for inference. DelRec achieves new state-of-the-art on SSC (82.58%) and PS-MNIST (96.21%) using only vanilla LIF neurons, and matches SOTA on the saturated SHD benchmark. A systematic functional study on SHD compares recurrent vs. feedforward delays under parameter and sparsity constraints.

## Strengths

- **First SGL-based method for recurrent delays with well-specified technical approach.** The differentiable interpolation (triangle function with annealing σ, Eqs. 9–13) is logically consistent and the adaptation from DCLS to the recurrent setting involves genuine complexity: future-oriented scheduling, buffer management, and support-limited computation (Eqs. 12–13). The method is compatible with any neuron model fitting the standard SNN formalism (Eqs. 1–3).

- **New SOTA on SSC and PS-MNIST using simple LIF neurons.** Table 1 shows 82.58±0.08% on SSC (vs. 82.03% SiLIF) with 0.37M parameters and 96.21% on PS-MNIST (vs. 95.77% ASRC-SNN) with 0.16M parameters. These results are achieved without the complex neuron models (adaptive, resonant, structured state-space) used by competitors, demonstrating that delay learning can substitute for neuron-level sophistication.

- **Insightful functional study.** Section 3.2's three-phase approach (validation → simplification → comparative) on SHD is methodologically thorough. Fig. 3C shows recurrent delays degrade more gracefully than feedforward delays as parameter count drops from ~10k to ~2k, providing genuine insight into when and why recurrent delays help most. The finding that even random fixed recurrent delays improve over vanilla RSNN (Fig. 3B) suggests delays help gradient propagation, not just temporal feature extraction.

- **Rigorous evaluation practices.** The paper uses a clean 80/20 train/validation split for SHD with 10 seeds, honestly acknowledges SHD saturation above ~93%, and appropriately excludes SHD from the main results table. The comparison is deliberately restricted to LIF-derived models for fairness (footnote 1, Table 1).

## Weaknesses

### Fatal
None

### Major

- **PS-MNIST SOTA claim lacks variance reporting.** The paper states "we only test one seed as all the previous state-of-the-art models on the dataset" (line 132). The improvement is 0.44% (96.21% vs. 95.77% ASRC-SNN). Without any standard deviation, the SOTA claim is under-supported. The SSC result is run with 3 seeds (±0.08%), showing the infrastructure exists. Running even 3 seeds for PS-MNIST would resolve this and is the single highest-leverage improvement for the paper.

### Minor

- **Moderate methodological novelty.** The core technical idea adapts DCLS's triangle interpolation (Hammouamri et al., 2024) to recurrent connections via a scheduling matrix. The paper is transparent about this lineage (line 122: "A similar strategy was used in [Hammouamri et al., 2024]"). The recurrent setting adds genuine complexity, but the interpolation mechanism is directly borrowed.

- **Equation reference error.** Line 98 states "One can notice in Eq.15 that the function h_{σ,d}(τ) has a finite support," but the equations in the paper number only up to (13). This is a misnumbering (likely should reference Eq. 9 or 11).

- **Random fixed recurrent delays not characterized.** Fig. 3B shows random fixed recurrent delays outperform vanilla RSNN, but the paper does not specify how these delays were sampled (uniform? over what range?).

### Trivial
None

## Nice-to-Haves

- **Sensitivity analysis of σ annealing schedule.** The initial σ value and annealing rate are key design choices, but no ablation is provided on their sensitivity. Even a brief analysis would strengthen confidence in the method's robustness.

- **Computational overhead quantification.** The scheduling matrix adds memory and compute overhead vs. vanilla RSNN. A brief training time or memory comparison would be valuable, especially given the paper's concluding pitch about neuromorphic hardware deployment.

- **Analysis of learned delay distributions.** What do the learned delays actually look like after training? Do different neurons learn different values? This would provide insight into *why* recurrent delays help, not just *that* they help.

## Removed Points

These points are flagged to be removed, treat them with caution.

- **Harsh critic's speculation that Eq. 15 reference is a parser artifact.** Verified: equations in the paper number (1)–(13) and line 98 references "Eq.15." This is a real misnumbering in the paper, kept as minor weakness.
- **Strength finder's "first combination of feedforward and recurrent delays"** — valid but minor, noted in passing rather than as a standalone strength.
- **Harsh critic's concern about SSC improvement being "narrow."** The SSC improvement (0.55%) shows non-overlapping error bars (±0.08% vs. ±0.25% for SiLIF). This is a real, statistically supported improvement. The concern applies mainly to PS-MNIST (single seed), which is already captured as a major weakness.
- **Strength finder's "efficient implementation with no predefined maximum delay"** — partially true (Eq. 13 approximates the support range) but the overhead is not quantified, making this claim hard to fully evaluate.

## Novel Insights

The SHD functional study provides the genuinely novel insight that recurrent delays are most beneficial under tight parameter budgets — they degrade more gracefully than feedforward delays as network capacity shrinks (Fig. 3C). The observation that even random fixed recurrent delays help over vanilla RSNN suggests delays improve gradient propagation (as sketched in Fig. 1B), not just temporal feature extraction. This dual mechanism — enabling both richer temporal representations and better gradient flow — is a useful conceptual contribution that extends beyond the method itself.

## Suggestions

1. Run 3–5 seeds for PS-MNIST with standard deviations to substantiate the SOTA claim.
2. Fix the "Eq.15" reference (should be Eq. 9 or 11).
3. Specify how random fixed recurrent delays were sampled in the functional study.
4. Add a brief ablation on σ schedule sensitivity.
5. Characterize learned delay distributions (histograms of per-neuron delays).
6. Report training time/memory overhead vs. vanilla RSNN and DCLS baselines.

## Calibration Report

### Round 1 — Bracketing

| Anchor | Path | Avg Human Score | Round | Comparison |
|--------|------|----------------|-------|------------|
| DHTM | fnO5h1CFyh.md | 3.00 | 1 | Unrelated neuroscience method; paper under review is much stronger |
| CAN | SI6zocV2SS.md | 1.50 | 1 | Catastrophic forgetting paper; completely different quality level |
| RNN dynamics | 7eYmijcuqO.md | 3.00 | 1 | RNN temporal dynamics theory; no SOTA results, rejected |
| TVRNN | NPzuN3Rxi8.md | 3.00 | 1 | Neuronal connectivity analysis; unrelated |
| DeNN | pIJR9uPjy3.md | 4.50 | 1 | Delay Neural Networks — same topic but clarity issues, no SOTA; paper under review stronger |
| SNN Layer Sync | 6iM7mmVhXh.md | 5.75 | 1 | Asynchronous SNN — interesting but mixed results; paper under review has clearer contributions |
| FGT | yBP36xQhZl.md | 5.00 | 1 | Forward gradient SNN — moderate novelty, no SOTA; paper under review stronger |
| SOLO | vq75kRCYuY.md | 4.00 | 1 | Online SNN training — performance drops; paper under review much stronger |
| SpikePoint | 7etoNfU9uF.md | 5.75 | 1 | SNN for event cameras with SOTA; similar contribution level but paper under review has better functional study |
| Spike-driven V2 | 1SIBN5Xyw7.md | 5.67 | 1 | SNN Transformer; accepted with similar quality |
| Barrel Cortex | UvfI4grcM7.md | 6.75 | 1 | Biologically constrained model; different type of contribution, upper bracket anchor |
| Spiking ViT | qzZsz6MuEq.md | 6.60 | 1 | Novel attention for SNNs with SOTA; comparable novelty and quality |
| ST-DANO | eN4g4cjFX1.md | 5.75 | 1 | SNN neuron optimization; SOTA on one dataset but many weaknesses; paper under review stronger |
| Temporal Flex SNN | 9HsfTgflT7.md | 6.20 | 1 | Temporal flexibility method; marginal improvements; paper under review has stronger SOTA claims |
| SNN Conversion | XrunSYwoLr.md | 7.00 | 1 | First transformer-to-SNN conversion; more novel technique but paper under review has better empirical validation |
| Brain Bandit | RWJX5F5I9g.md | 8.00 | 1 | Neuroscience theory; different field, not comparable |
| Grid Cells | Xo0Q1N7CGk.md | 8.00 | 1 | Grid cell theory; different field |
| RL Predictive | agPpmEgf8C.md | 8.00 | 1 | RL + neuroscience; different field |
| Invariance Manifolds | kbjJ9ZOakb.md | 8.00 | 1 | Visual cortex theory; different field |

### Round 1 Bracket: 5.5–7.0

The paper is clearly stronger than rejected SNN papers (DeNN 4.5, SOLO 4.0, FGT 5.0) and comparable to or better than accepted SNN papers at 5.75–6.20. It sits below the most novel accepted papers (SNN Conversion 7.0) due to moderate technical novelty.

### Round 2 — Narrowing

| Anchor | Path | Avg Human Score | Round | Comparison |
|--------|------|----------------|-------|------------|
| Temporal Flex SNN | 9HsfTgflT7.md | 6.20 | 2 | Paper under review has stronger SOTA claims and better functional study → above 6.2 |
| Spiking ViT | qzZsz6MuEq.md | 6.60 | 2 | Spiking ViT has more architectural novelty; paper under review has cleaner evaluation → comparable ~6.5 |
| SNN Conversion | XrunSYwoLr.md | 7.00 | 2 | More novel technique; paper under review slightly less novel but better empirical validation → below 7.0 |

### Final Score Positioning

The paper sits above Temporal Flexibility SNN (6.20) due to stronger SOTA results and a more insightful functional study, comparable to Spiking Vision Transformer (6.60) in terms of contribution quality, and below SNN Conversion (7.0) due to less technical novelty. The single-seed PS-MNIST issue and moderate novelty prevent a higher score, but the clear SOTA on two benchmarks, the valuable functional study, and the thorough evaluation justify a solid score.

**Final Score: 6.5**

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>