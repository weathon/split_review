Now let me write the final consolidated review.

## Summary

This paper introduces TNT, a two-stage training paradigm for deep memory modules (such as Titans and TTT). Stage 1 employs a hierarchical memory architecture — a global memory operating on large hardware-friendly chunks plus multiple local memories with periodic state resets enabling context parallelism — to accelerate training. Stage 2 is a brief fine-tuning phase that adapts the model to smaller chunk sizes for inference. Experiments on the Titans architecture at 150M scale show up to 17.37× speedup over the baseline while improving perplexity by ~1–2 PPL.

## Strengths

1. **17× training speedup with accuracy improvement.** Table 1 shows TNT (C_L=64) reaches the target loss in 1.12 hours versus 19.48 hours for the Titans (C=8) baseline — a 17.37× speedup — and Table 2 shows consistent perplexity improvements (~1–2 PPL on C4, FineWeb, PG19) over Titans baselines. These are large, practically meaningful gains.

2. **Context parallelism via periodic local memory resets.** Section 4.1.1 introduces a key innovation: resetting local memory to a learned initial state W_init at segment boundaries (Eq. 6), breaking sequential dependencies across shards. This is a clean solution to a longstanding challenge in parallelizing non-linear recurrences, and the speedup numbers in Figure 4 and Table 1 confirm it works in practice.

3. **Q-K Projection addresses compression-retrieval mismatch.** The ablation in Table 3 shows that removing Q-K Projection increases perplexity from 21.04 to 22.01 (~5% relative degradation), confirming its practical importance. The running-sum implementation (Section 4.1.2) is efficient with O(d²) constant-size state.

4. **Linear runtime scaling.** Figure 4 demonstrates that TNT's runtime grows linearly with sequence length, while Titans with C=16 grows quadratic in wall-clock time. At 32K length, TNT (C_L=128) is faster than FlashAttention (1.3×), a strong practical result for long-context training.

## Weaknesses

### Major

1. **Stage 2 fine-tuning benefit is marginal and the narrative around it is oversold.** The paper frames Challenge 3 (chunksize mismatch) as a fundamental problem and presents Stage 2 as its solution. However, the evidence for Stage 2 providing meaningful benefit is thin. The best Stage 1 model achieves 23.13 PPL; Stage 2 achieves 23.09 — a difference of 0.04 PPL with no variance or significance test reported. The paper also never directly validates the claim that Stage 2 fixes: it does not show that a Stage 1 model evaluated with a smaller inference chunk degrades, and that Stage 2 fine-tuning recovers the gap. Without that control, the improvement could simply be additional training on the same data. The paper itself admits Stage 2 requires only 5% additional compute, and the improvement is so small that the contribution would be unchanged if Stage 2 were removed entirely. At minimum, the authors should provide the missing control experiment (Table: Stage 1 evaluated with small chunk → degraded PPL; Stage 2 → recovered) or substantially temper the claims about resolving Challenge 3.

2. **Claimed generality is not demonstrated.** The abstract and introduction state that TNT is a "general training paradigm applicable to any deep memory module." The abstract further claims TNT was "evaluated on Titans and TTT models." In practice, TNT is only instantiated on Titans — TTT appears solely as a baseline trained with its own method, not with TNT's framework. The method's architectural modifications (hierarchical memory, Q-K projection, periodic resets) are architecture-specific: they depend on the deep memory module's fast-weight update structure. Demonstrating TNT on at least one other architecture (TTT is the natural choice since it is already a baseline) is necessary to support the generality claim. Without it, the contribution should be scoped as specific to (or validated on) the Titans architecture.

### Minor

3. **No variance or error bars reported.** No standard deviations or confidence intervals are provided for any metric. For the Speedup results in Table 1 and perplexity values in Table 2 — especially the tiny 0.04 PPL Stage 2 gain — this is a noticeable gap. While single-run evaluation is common in this setting, reporting variance (or at minimum the number of seeds) would substantially strengthen the claims.

4. **Q-K Projection overhead is not analyzed.** The running-sum formulation requires maintaining a d×d matrix, which is O(d²) per token (where d is typically 256 for 150M models, giving d²=65K). The paper states this "can be maintained efficiently" but provides no FLOPs analysis or wall-clock time overhead measurement. Including this analysis would help readers assess the practical trade-off of the projection.

5. **No empirical comparison to directly related concurrent work.** The paper cites Zhang et al. (2025) and Guo et al. (2025) as recent attempts to address the same efficiency problem, and provides brief qualitative differentiation in Section 1. A direct empirical comparison (even at smaller scale) or a more detailed analytical argument for why TNT's approach is preferable would help position the contribution relative to the current literature.

6. **Evidence for Challenge 2 (compression-retrieval domain mismatch) is indirect.** The ablation shows that removing Q-K projection hurts perplexity (21.04→22.01), which confirms the mechanism is useful. However, the paper does not isolate whether the improvement comes from fixing the hypothesized domain mismatch versus simply adding a learned projection that provides additional representational capacity. The mechanism is plausible but the evidence is indirect.

### Trivial

7. **Global memory chunk size sensitivity not explored.** All experiments use C_G = 2048. An ablation over global chunk sizes (e.g., 512, 1024, 4096) would help understand the sensitivity of this hyperparameter.

8. **No limitations section.** The paper ends with the Conclusion (Section 6) and could benefit from a brief discussion of limitations: (a) validation only on one architecture, (b) Stage 2 marginality, (c) sensitivity of the additional hyperparameters (S_L, C_G, W_init).

## Nice-to-Haves

- Providing parameter counts for configurations with multiple local modules to clarify whether perplexity improvements come from increased capacity or the hierarchical design itself.
- An analysis of the optimization dynamics of W_init (the learned initial local memory state).

## Removed Points

These points from the input reviews were removed with justification:

- **"Target loss (3.20) is arbitrary in Table 1"** — This is a standard time-to-quality evaluation practice; any target loss is reasonable as a comparison anchor.
- **"Transformer (w/ gating) + FlashAttention reaches target loss faster than TNT"** — The paper explicitly acknowledges this limitation and explains it is due to TNT lacking a custom kernel. This is a fair, pre-addressed point.
- **"Challenge 1 evidence is weak / Challenge 3 not well motivated"** — The paper provides adequate motivation and empirical backing (Figure 2, Section 3 text). These criticisms were swept from general category lenses rather than specific paper errors.
- **"Missing appendix content / proofs"** — The parser strips these sections; they exist in the original submission.
- **Various formatting/presentation nitpicks** — Parser artifacts, not author errors.

## Novel Insights

None beyond the paper's own contributions. One observation that emerges from synthesizing the reviews and the paper: the core innovation (periodic reset of local memory to enable context parallelism) is clean and well-executed, but its presentation as part of a "two-stage paradigm" inflates the apparent contribution. The Stage 1 hierarchical memory with resets is doing nearly all the work; Stage 2 is a minor add-on that happens to align with the "two-stage" narrative but provides negligible benefit at this scale.

## Suggestions

1. **De-emphasize or substantially revise the Stage 2 narrative.** Either remove the claim that Stage 2 resolves Challenge 3 (since the evidence is insufficient) or provide the missing control experiment: evaluate Stage 1 models at the Stage 2 chunk size without fine-tuning and show that Stage 2 recovers the gap. If the control cannot be provided, present TNT as a single-stage efficient pre-training method.

2. **Scope the generality claim explicitly to the Titans architecture, or add a TTT-based validation.** One additional architecture (TTT is the most straightforward since it is already in the baselines) would substantially strengthen the paper. If TTT does not benefit from TNT, that is also informative and should be discussed.

3. **Add a direct comparison to Zhang et al. (2025) and/or Guo et al. (2025).** Even a discussion of why these methods are not directly comparable (or a theoretical argument) would help.

4. **Report variance for at least the main results in Tables 1 and 2.**

## Score and Decision

### Calibration Anchors

**Round 1 — Bracketing:**
- *Low band (< 3.5)*: e.g., "On Sequence Segmentation with overlapped Chunks" (2.50), "Fast Salient Factor Concentration RNN" (2.33), "Long Horizon Episodic Decision Making" (1.50). These are weak/substantially flawed papers. TNT is clearly stronger than these.
- *Middle band (3.5–7.5)*: e.g., "An Evolved Universal Transformer Memory" (7.00), "Think Before You Act: Decision Transformers with Internal Memory" (5.75), "Back to Fundamentals: Re-Examining Memorization" (4.50).
- *High band (> 7.5)*: e.g., "DEPT: Decoupled Embeddings for Pre-training" (8.00), "Cut Your Losses in Large-Vocabulary Language Models" (8.50). These are strong, well-rounded papers. TNT is not at this level due to the unsubstantiated generality claim and oversold Stage 2 narrative.

**Round 2 — Narrowing:**
- *"Parallelizing non-linear sequential models over the sequence length"* (6.00, accepted): Both papers tackle parallelization of non-linear sequential models. DEER has stronger theoretical grounding and broader applicability claims, while TNT has more thorough empirical evaluation on language modeling (multiple datasets, downstream tasks). TNT's experiments are more practically convincing, but its generality claim is weaker (tested on one architecture vs. DEER's provably general method). Comparable quality overall.
- *"MELODI: Exploring Memory Compression for Long Contexts"* (6.25, accepted): Both propose hierarchical memory architectures. MELODI focuses on inference memory compression with thorough ablations; TNT focuses on training speed with more dramatic efficiency gains. TNT has better speedup numbers, MELODI has more rigorous ablation design. Slightly stronger on balance for MELODI due to more complete analysis.
- *"Ultra-Sparse Memory Network"* (6.00, accepted): A different approach to efficient memory; well-executed experiments at scale. TNT is comparable in quality.
- *"Hierarchical Context Merging"* (6.25, accepted): Training-free approach for long contexts. Well-executed but different problem scope.

**Final bracket**: Narrowed from 4–7 to 5.5–6.5 based on round 2 anchors. TNT is comparable to DEER (6.00) and weaker than MELODI (6.25) due to the overstated Stage 2 claims and unvalidated generality. It is stronger than "Think Before You Act" (5.75).

**Final Score**: 6.0 — The core hierarchical memory with periodic resets is a genuine contribution with practically meaningful speedups (17×) and consistent perplexity improvements. However, the two-stage framing oversells Stage 2, the generality claim is unsupported, and the lack of comparison to concurrent works weakens positioning.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>