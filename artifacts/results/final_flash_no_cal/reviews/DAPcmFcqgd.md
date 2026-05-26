Now I will write the consolidated review.

## Summary

MoEP (Modular Expert Paths) introduces a decoder-only architecture that combines layer-level parallelism with MoE-style routing to add sparsity while keeping the total parameter count fixed (for the base variant). The method interleaves dense layers with a middle stack of parallel blocks that operate at reduced hidden dimension, using top-k routing to activate different subsets of blocks per token. Evaluated on the BabyLM strict-small track, MoEP achieves the highest overall text-average score among all official baselines and demonstrates faster early learning than its dense GPT-2 counterpart.

## Strengths

1. **Novel architectural contribution for fixed-budget sparsity.** MoEP addresses an underexplored area — layer-level MoE placement with parallel blocks at reduced dimensionality — and provides a concrete design that adds sparsity without increasing total parameters. Section 3.1 and Figure 2 clearly describe the interleaving of dense layers, MoE shrink/grow projections, and the parallel block stack, which differentiates MoEP from the dominant sublayer-level MoE approaches.

2. **MoEP achieves the highest overall text-average score among all official BabyLM strict-small baselines.** Table 1 shows MoEP's overall text-average (including AoA) = 44.50, surpassing GPT-BERT causal (41.20), GPT-BERT focus-causal (40.00), GPT-BERT mixed-causal (39.20), and GPT-2 HF (37.40). This is direct evidence that the sparse parallel-block design, while keeping total parameters fixed (28M vs. 28M for GPT-2), delivers competitive performance on the full evaluation suite.

3. **Demonstrated faster early learning and better sample efficiency.** The training dynamics analysis (Appendix A.3 and Section 5.1) shows that MoEP "exhibits more comprehensive early learning, reaching peak performance at the 30M checkpoint" whereas GPT-2 converges more slowly. This provides qualitative evidence that modular sparse routing accelerates pattern discovery, a substantively interesting property of the method.

4. **Controlled comparison of linear vs. SwiGLU experts yields a practical insight.** The paper compares MoEP (linear projection experts, 28M params) with MoEP-SwiGLU (SwiGLU-based experts, 38M params) under otherwise identical settings. The finding that "lightweight linear experts are more effective at the small scale" (Section 5.1) is a useful empirical observation for practitioners working with compact models.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

1. **The MoEP-SwiGLU variant (38M params) breaks the paper's central "fixed parameter count" premise without explicit discussion.** The abstract and Section 1 frame MoEP as "a solution to add sparsity while keeping the total parameter count fixed." While the base MoEP variant satisfies this (28M vs. 28M GPT-2), MoEP-SwiGLU uses 38M parameters — a 36% increase. Table 2 reports the parameter counts transparently, but the main text never acknowledges that this variant deviates from the fixed-budget constraint or explains why the increase is necessary. This risks misleading a reader who skims the paper.

2. **No ablation of the routing and architectural components.** The paper evaluates only one configuration of MoEP. Core design choices — number of parallel blocks \(P\), top-\(k\) value, dimension reduction ratio (\(d_L/d_P\)), and most importantly the routing mechanism itself — are never tested. Without comparing MoEP to a version where all parallel blocks are always activated (i.e., no top-\(k\) routing), it is unclear whether the performance improvement comes from the routing/sparsity, the reduced-dimension parallelism, or the specific hyperparameter choices. Such controls are standard in MoE papers and would substantially strengthen the evidence.

3. **No computational cost analysis despite efficiency claims.** The paper argues for "efficiency" and "compact" sparsity based solely on parameter count. For Transformers, FLOPs and wall-clock time are important additional axes. MoEP uses routing overhead and a middle stack of parallel blocks — a FLOP-count or training-time comparison with GPT-2 and GPT-BERT would clarify whether the approach is genuinely more efficient per unit of performance.

4. **Limited engagement with why GPT-BERT outperforms MoEP on the excluding-AoA metric.** On the macro average excluding AoA, GPT-BERT variants score substantially higher (54.10 vs. 49.00). The paper notes this only implicitly through the table, with no discussion of whether the gap is due to MoEP's unidirectional attention, the smaller hidden dimension of its parallel stack, the routing itself, or the bidirectional pretraining objective of GPT-BERT. A candid limitations discussion would improve credibility.

## Nice-to-Haves

- An ablation measuring the contribution of the MoE shrink/grow projections independently from the parallel-block routing.
- Analysis of routing behavior (e.g., load balancing over blocks, expert specialization patterns over training) to deepen understanding of why MoEP learns faster.

## Removed Points

These points were flagged by the reviewers but are removed from the main weaknesses for the following reasons:

- **"Factual invalidity of the headline performance claim" (Harsh Critic):** The critic asserts that Table 1 contradicts the claim that MoEP "achieved the highest performance across all models." This is a misreading. The paper qualifies this claim with "when the AoA task score was included in the Macro Average" (Section 5.1, line 166). Table 1 confirms MoEP's overall text-average (44.50) is indeed the highest among all baselines (GPT-BERT causal 41.20, focus-causal 40.00, mixed-causal 39.20, GPT-2 HF 37.40). The excluding-AoA comparison is separately acknowledged to only beat GPT-2. The paper's claims are factually consistent with its data.

- **"Inconsistency in the fixed parameter count premise" (Harsh Critic):** Partially valid (kept as Minor weakness 1 above), but the claim that the paper "quietly breaks the design constraint" is overstated. Table 2 clearly reports the parameter counts for all variants, and the base MoEP (the core contribution) does satisfy the fixed-budget premise. The retained weakness is that the main text should have explicitly addressed this deviation.

- **Missing related works / reproducibility concerns about unreleased models:** The paper cites BabyLM, GPT-BERT, etc. as existing entities. No reviewer concern about model availability is retained per the hard rules.

- **"The evaluation lacks rigor" / generic area-of-concern sweeps without specific anchors:** Removed per filtering discipline.

- **Formatting/style nitpicks:** Removed per hard rules.

- **Strength Finder's generic/unsupported strengths:** All strengths listed above are concrete, specific to the paper, and grounded in evidence. No strengths were removed for being generic.

## Novel Insights

None beyond the paper's own contributions. The two reviews do not surface a genuinely novel observation that the paper itself misses.

## Suggestions

1. **Acknowledge the MoEP-SwiGLU parameter increase explicitly** in Section 3 or Section 5, noting that it deviates from the fixed-budget premise and explaining why it is included (e.g., as a comparison of expert types under relaxed constraints).

2. **Add at least two ablation studies:** (a) MoEP with all parallel blocks always activated (no routing) to isolate the effect of sparsity, and (b) MoEP with varying \(P\) or top-\(k\) to show sensitivity to these design parameters.

3. **Include a FLOP-count table or training-time comparison** for MoEP vs. GPT-2 and GPT-BERT, even if approximate, to substantiate efficiency claims.

4. **Add a brief discussion of the GPT-BERT comparison** in Section 5 (or a dedicated limitations paragraph) acknowledging the architectural differences and why MoEP underperforms GPT-BERT on the excluding-AoA metric.

## Score and Decision

MY FINAL SCORE: <score>4.0</score>
MY FINAL DECISION: <decision>Accept</decision>