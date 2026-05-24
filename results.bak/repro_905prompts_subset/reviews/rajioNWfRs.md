Now I have sufficient calibration. Let me produce the final review.

## Summary

TNT introduces a two-stage training paradigm for deep memory modules (Titans/TTT-style architectures) that decouples training efficiency from inference performance. Stage 1 uses a hierarchical memory with a global module (large chunks) and multiple parallel local modules (small chunks) with periodic state resets, enabling context parallelism for non-linear recurrences. Stage 2 fine-tunes only the local memories at a smaller chunk size to resolve the train-inference chunk-size mismatch. The paper reports up to 17.37× training speedup over the most accurate Titans baseline while simultaneously improving perplexity.

## Strengths

- **17× training speedup with quality improvement**: Table 1 shows TNT reaches target loss 3.20 in 1.12 hours vs. 19.48 hours for the best Titans baseline (C=8), and Table 2 shows TNT Stage 1 achieves lower perplexity (23.13) than the best Titans model (25.07). The speed is simultaneously traded for quality — this is a genuine both-and result, not a trade-off.

- **Periodic state reset enables context parallelism for non-linear recurrences**: Eq. 6 introduces a clean mechanism: resetting local memory states to a learned \(W_{\text{init}}\) at boundaries of length \(S_L\). This breaks sequential inter-chunk dependency, allowing parallel processing of all local shards — a non-trivial innovation since non-linear RNNs (with normalization between steps) resist standard parallelization techniques.

- **Q-K Projection is well-motivated and validated**: Section 4.1.2 identifies a genuine domain mismatch (memory compresses keys but retrieves queries) and proposes projecting the query onto the past-key subspace. The ablation (Table 3) shows removing it degrades perplexity from 21.04 to 22.01, demonstrating it is not an optional add-on.

- **Good multi-scale temporal modeling**: Adding more local modules at different resolutions (from {8} to {4,8,16,32}) progressively reduces perplexity (24.10 → 23.13), showing the hierarchical memory captures patterns at multiple granularities.

- **Linear runtime scaling**: Figure 4 shows TNT's per-step runtime remains nearly constant (~400–550 ms) as sequence length grows from 2K to 32K, while Titans grows super-linearly to ~4000 ms.

- **Clear problem framing**: Section 3 crisply articulates three challenges (inefficient training, compression-retrieval mismatch, chunksize sensitivity) that the paper then systematically addresses.

## Weaknesses

### Major
None.

### Minor

- **Abstract overclaims evaluation on TTT**: The abstract states "Evaluated on Titans and TTT models," but TNT is only instantiated on Titans in the experiments. TTT appears solely as a baseline in Table 2. There is no TTT-based TNT model in the paper. The abstract should be rephrased to reflect the actual experimental scope (e.g., "Evaluated on Titans, with TTT as a baseline") or TNT-on-TTT experiments should be added.

- **Target loss in Table 1 is underspecified**: Table 1 reports time to "reach the same target loss 3.20" but never states whether this is training loss or validation loss, or on which dataset/split. Since Section 5.3 evaluates on multiple corpora (C4, FineWeb, PG19), the reader cannot determine how the target was set. The paper should clarify this and ideally report time-to-a-fixed-perplexity on a held-out validation set to avoid cherry-picking concerns.

- **Stage 2 evidence is thin on the core claim**: Challenge 3 (chunksize mismatch) predicts that a Stage 1 model evaluated at small chunk sizes degrades, and Stage 2 fixes this. Table 2 shows Stage 2 improves final perplexity (e.g., 23.13 → 23.09), but this delta is small and could be within run-to-run variance. The paper never does the controlled experiment: take a Stage 1 model, evaluate it with a small inference chunk (e.g., C=1) to demonstrate the degradation, then fine-tune and show recovery. Figure 2 demonstrates the mismatch problem on Titans, but a direct TNT-controlled experiment is missing.

- **Q-K Projection computational cost not quantified**: The projection requires maintaining a running \(O(d^2)\) outer-product sum per local memory. The paper motivates the mechanism but never breaks down how much of TNT's runtime is spent on projection vs. core memory operations. Given that the projection is a quadratic operation in \(d\), quantifying this would help practitioners assess the overhead trade-off.

- **Parameter budget allocation not explained**: The paper states all models are 150M parameters, but does not explain how adding a global memory module and multiple local memory modules is compensated for within the fixed budget (e.g., reduced base model depth/width). The paper should clarify this to preempt confound questions.

### Trivial
- None.

## Nice-to-Haves
- The controlled experiment for Stage 2 (evaluate Stage-1 model at C=1, observe degradation, fine-tune, compare) would significantly strengthen the chunksize-mismatch claim.
- A computational breakdown showing projection vs. memory-update vs. communication time would aid reproducibility and practical adoption.
- Scaling beyond 150M parameters (even a discussion or small-scale extrapolation) would improve impact. The speedup from context parallelism may differ at larger scales where communication overhead changes.

## Removed Points

These points were flagged by the harsh critic but are removed (with justification):

- **"Parameter count is confounded"** (Fatal): REMOVED. The paper explicitly states "We train 150M parameter models" (Section 5.1). All models, including TNT variants, total 150M parameters. The reviewer's claim that TNT "almost certainly exceeds" is speculation without evidence, contradicted by the paper's explicit statement. The paper could be clearer about *how* the budget is distributed, but the claim that comparisons are confounded is unsupported.

- **"Chunkwise time-to-quality metric is inflated"**: WEAKENED to Minor (target loss not specified). The 17× headline uses Titans C=8 as baseline, which is the slowest configuration. But Table 1 also shows meaningful speedups against faster configurations (e.g., 5.25× vs C=128). The inflation concern is partly valid (the slowest baseline gives the biggest number) but the paper is transparent about this — multiple baselines are shown.

- **"Stage 2 improvement within run-to-run variance"**: WEAKENED to Minor. The improvements are small but consistent across all configurations (every Stage 2 row improves over its Stage 1 counterpart). The absence of confidence intervals is a typical limitation for single-run evaluations at this scale, and the consistency partially mitigates the concern.

- **"Titans implementation may be suboptimal"**: REMOVED. This is speculation. The paper uses the original Titans implementation following the authors' own paper. The runtime gap is explained by the architectural difference (sequential vs. parallel), not by implementation quality.

- **"Section notes on parallelism implementation, hardware details, etc."**: REMOVED. These are standard implementation details deferred to an appendix (which was stripped by the parser). The paper describes the sharding strategy at the appropriate level for the main text.

- **Strength Finder strengths about "general paradigm" and "problem importance"**: TRIMMED. The claim that TNT is a general paradigm applicable to multiple architectures is valid in principle but only demonstrated on one architecture (Titans), so it is kept but noted. Generic framing strengths are removed.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. Specify the target loss in Table 1 (dataset and split) and consider reporting time-to-a-fixed-validation-perplexity instead.
2. Add the controlled Stage 2 experiment: evaluate Stage 1 at C=1 (or small C) to show degradation, then fine-tune and show recovery.
3. Clarify the abstract's scope — replace "evaluated on Titans and TTT models" with "evaluated on Titans (with TTT as a baseline)" or add TNT-on-TTT results.
4. Provide a brief parameter allocation breakdown showing how the 150M budget is distributed across global memory, local memories, and the base network.
5. Include a runtime decomposition somewhere (even in the appendix) to show Q-K projection cost.
6. Add discussion of how the optimal \(S_L\) (reset period) is chosen — this is a key hyperparameter that governs the parallelism-expressiveness trade-off.

## Score and Decision

**Calibration:**

*Round 1 bracket (wide):* The paper sits between the weak-anchor band (avg 2.33–3.00, papers with limited contributions or flawed methodology) and the strong-anchor band (avg 7.60–8.50, high-impact papers with extensive evaluation). This gave an initial bracket of roughly (3.5, 7.5).

*Round 2 narrowing:*
- **MELODI** (avg 6.25): Hierarchical memory compression for long contexts. TNT is comparable — both propose hierarchical memory for efficiency — but TNT has stronger evaluation (perplexity + downstream reasoning benchmarks vs. MELODI's perplexity-only) and the periodic-reset innovation is more fundamental than MELODI's compression scheme. TNT is slightly stronger.
- **LongGen** (avg 6.40): Hybrid sparse/dense attention for efficient long-context. Different problem (extending LLM context vs. training deep memory modules), similar contribution level. TNT's speedup is larger (17× vs. 1.55×) but evaluated at smaller scale.
- **Memory Mosaics** (avg 6.25): Mixed reviews (3,8,8,6). TNT has cleaner experiments and better-supported claims.
- **LongLoRA** (avg 7.00): More impactful paper with larger-scale experiments. TNT is below this bar.
- **Decision Transformers w/ Memory** (avg 5.75): TNT has stronger empirical contributions.

*Final bracket:* After round 2, the paper sits between 5.75 (Decision Transformers w/ Memory) and 6.40 (LongGen), closer to the upper end. The paper has genuine technical novelty, clear problem framing, well-designed ablations, and strong speedup numbers. The weaknesses (abstract oversell, under-specified target loss, thin Stage 2 evidence) are real but minor. This is a solid paper that would benefit from revisions but is already a clear contribution.

**Score: 6.0** — A solid paper with clear contributions, well-supported main claims, and mostly minor weaknesses that are addressable.

**Decision: Accept**

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>