## Summary

This paper introduces DelRec, a method for learning per-neuron axonal delays in recurrent connections of spiking neural networks using surrogate gradient learning. The approach employs a differentiable triangular interpolation scheme with annealed spread width, coupled with a scheduling buffer, enabling gradient-based optimization of real-valued delays that are rounded to integers at inference. Using only simple LIF neurons, DelRec achieves state-of-the-art accuracy on the Spiking Speech Commands (SSC) dataset (82.58±0.08%), a new best on PS-MNIST (96.21%), and matches SOTA on SHD. An extensive ablation study on SHD convincingly demonstrates that learned recurrent delays outperform both fixed recurrent delays and learned feedforward delays, especially under low-parameter constraints.

## Strengths

- **Novel method for an underexplored direction in SNNs**: Learning per-neuron delays in recurrent connections is genuinely under-explored in the SNN literature. DelRec's differentiable interpolation (triangular spread with annealing) is a principled way to handle non-integer delays during training while converging to clean integer delays at inference, without requiring a prespecified maximum delay range.

- **Strong empirical results with careful ablation**: SSC results are reported with 3 seeds (82.58±0.08%), beating all prior methods that use simple LIF neurons. The SHD study (Figure 3B, 3C) is the paper's strongest section: it compares 6 controlled model variants at matched parameter counts, showing that learned recurrent delays reach ≈82% on SHD with only ~10k parameters, versus ≈80% for feedforward delays and ≈40% for vanilla RSNN. The finding that recurrent delays provide more benefit than feedforward delays when representational capacity is limited is clearly supported.

- **Systematic isolation of recurrent-delay contribution**: The SHD ablation controls for parameter count, neuron model, and architecture, cleanly attributing gains to learned recurrent delays rather than other factors.

- **Reproducibility commitment**: Code is provided via anonymous repository, using publicly available datasets and the SpikingJelly framework.

## Weaknesses

### Major

1. **Single-seed PS-MNIST result undermines a core SOTA claim.** The paper reports 96.21% on PS-MNIST as a new state-of-the-art, but this comes from a single training run. The justification ("we only test one seed as all the previous state-of-the-art models on the dataset") does not remedy the problem — it propagates an existing bad practice. The 0.44% margin over the previous best (95.77%) is well within typical run-to-run variance for this benchmark. Without multiple seeds and reported mean ± std, the PS-MNIST SOTA claim is not credible as presented. This is a fixable issue (run more seeds), but it affects a headline result.

2. **Overstated novelty claim.** The abstract and introduction state that DelRec is "the first SGL-based method to train axonal or synaptic delays in recurrent spiking layers." However, the paper itself cites Xu et al., who learn a recurrent delay parameter per layer using backpropagation — which, in the SNN context, implies surrogate gradient learning (the paper defines SGL precisely as "training SNNs with backpropagation"). The *form* of delay parameterization differs (per-neuron interpolation vs. per-layer softmax selection from a fixed set), but the general "first SGL-based" claim is inaccurate. The contribution should be reframed precisely: e.g., "first differentiable-interpolation method for per-neuron recurrent delays that does not require prespecifying a maximum delay range."

### Minor

3. **No analysis of what delays are actually learned.** The paper introduces a method to learn per-neuron delays but never shows the resulting delay values. A histogram of learned delays (for the best SSC model or a representative SHD model), or a visualization of how delays evolve during training, would meaningfully strengthen the claim that the optimization produces useful temporal offsets rather than arbitrary values. This is a missed opportunity in an otherwise strong ablation study.

4. **Missing discussion of computational overhead and limitations.** The scheduling buffer has dimension N × ceil(1 + max_d + (1+σ)). How does this scale with layer size and max delay? No runtime comparison or complexity analysis is provided. The conclusion would also benefit from a brief limitations paragraph (e.g., static delays at inference, memory overhead of the buffer).

5. **SOTA claims need qualification in the main text.** The paper states "new state-of-the-art accuracy scores on both SSC and PS-MNIST datasets" without immediately qualifying the comparison scope. A footnote acknowledges that multi-compartment and attention-based models achieve higher scores on PS-MNIST (e.g., Chen et al. 2024 report 97.78%), but the main text reads as an unqualified SOTA claim. This is easy to fix by making the scope (SOTA among simple-LIF models) explicit in the main text.

### Trivial

6. The PS-MNIST architecture (1 layer of 64, then 2 layers of 212 neurons) is asymmetric and is not explained. If this was chosen to match a prior baseline's parameter count, that should be stated.

## Nice-to-Haves

- Show learned delay distributions (histograms per layer) and/or their evolution during training.
- Provide a brief complexity analysis or empirical runtime comparison for the scheduling buffer.
- Discuss limitations explicitly (static delays at inference, buffer memory overhead).

## Removed Points

The following points were raised by reviewers but are removed with justification:

- **Harsh critic's concern about Table 1 column for ASRC-SNN ("Rec. Delays" checkmark)**: The table distinguishes methods with checkmarks; the granularity (per-layer vs. per-neuron) is discussed in the text. This is a minor presentation preference, not a substantive weakness.
- **Harsh critic's claim that the SHD functional study should "double down" by reporting delay distributions**: This was kept as a minor weakness (item 3 above), not upgraded to a major requirement — the existing ablation is already the paper's strongest evidence.
- **Harsh critic's note about "Algorithm 1 not in main text"**: The appendix exists in the original submission; the parser strips appendices. This is not a valid criticism.
- **Strengths about "generic compatibility with any spiking neuron model"**: While stated in the paper, the experiments only use LIF neurons, making this a claimed rather than demonstrated strength. Downgraded to nice-to-have.
- **Harsh critic's criticism about PS-MNIST architecture asymmetry**: Kept as trivial (item 6) — it is a minor omission but worth noting.

## Novel Insights

None beyond the paper's own contributions. The key finding — that per-neuron recurrent delays learned via differentiable interpolation provide a greater benefit than feedforward delays under low-parameter constraints on temporal benchmarks — is clearly articulated in the paper itself.

## Suggestions

1. Run PS-MNIST with at least 5 seeds, report mean ± std, and adjust the SOTA claim accordingly. If the variance is small and the result holds, the claim becomes credible; if not, position it as "competitive" rather than SOTA.
2. Correct the novelty statement to be precise about what distinguishes DelRec from Xu et al. (e.g., "first differentiable per-neuron recurrent delay method that does not require prespecifying a maximum delay range").
3. Add a figure showing the distribution of learned delays (histogram per layer for at least one benchmark).
4. Qualify the SOTA claims in the main text to explicitly state the comparison scope (simple LIF neurons) and note in the abstract/intro that higher results exist with more complex neuron models.

## Score and Decision

### Calibration Anchors

**Round 1 — Bracketing:**
- *Weak band (<3.5)*: SI6zocV2SS (1.50), 7eYmijcuqO (3.00), fnO5h1CFyh (3.00), NPzuN3Rxi8 (3.00). All substantially weaker — fundamental flaws or not about SNN training.
- *Middle band (3.5–7.5)*: vq75kRCYuY (4.00, Reject), yBP36xQhZl (5.00, Reject), drPDukdY3t — DeepTAGE (6.25, Accept), vlQ56aWJhl (5.00, Reject). DeepTAGE is the most relevant anchor: an accepted SNN training method with comparable empirical scope.
- *Strong band (>7.5)*: nwDRD4AMoN (9.00), RWJX5F5I9g (8.00), Xo0Q1N7CGk (8.00), aWXnKanInf (8.00). Clearly stronger papers with deeper theoretical contributions or broader impact.

**Round 1 bracket**: 5.5–7.0

**Round 2 — Narrowing:**
- 6iM7mmVhXh (5.75, Reject), eN4g4cjFX1 (5.75, Reject), 9HsfTgflT7 — Temporal Flexibility (6.20, Accept), xwKt6bUkXj (6.75, Accept), MiPyle6Jef — QP-SNN (6.75, Accept), qzZsz6MuEq (6.60, Accept), FlH6VB5sJN (5.20, Reject).

The anchors that are closest: DeepTAGE (6.25, Accept) and Temporal Flexibility (6.20, Accept) are accepted papers on SNN training methodology with similar strengths and weaknesses. DelRec has a clearer method contribution than DeepTAGE (which reviewers found lacked theoretical analysis), and a stronger ablation than Temporal Flexibility (which had marginal performance gains). However, the single-seed PS-MNIST result is a real evidential gap. QP-SNN (6.75, Accept) has more thorough experiments but less novelty. I place DelRec slightly below QP-SNN and slightly above Temporal Flexibility.

**Final score**: 6.0 — a solid accept-level paper that addresses an underexplored direction with a sound method and strong evidence on two of three benchmarks. The PS-MNIST issue and overstated novelty are fixable in revision.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>