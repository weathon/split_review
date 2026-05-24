Now I have a thorough understanding of the paper. Let me compose the consolidated review.

## Summary

This paper introduces TNT (Two-stage Non-linear Training), a training framework for deep memory modules (e.g., Titans, TTT) that decouples training efficiency from inference performance. Stage 1 uses a hierarchical memory architecture — a global memory processing large chunks for long-range context and multiple parallel local memories with periodic state resets that break sequential dependencies, enabling massive context parallelism. Stage 2 fine-tunes the local memories with small chunk sizes to maximize inference accuracy with minimal overhead. Experiments on Titans models show up to 17× training speedup while improving perplexity and reasoning accuracy compared to the baseline.

## Strengths

- **Hierarchical memory with periodic state resets enables context parallelism for non-linear RNNs.** Section 4.1.1 (Eq. 6) introduces a reset mechanism that breaks sequential dependencies between local memory shards, allowing them to be processed in parallel across devices. Figure 4 demonstrates linear runtime scaling with sequence length, and Table 1 reports up to 17.37× training speedup — directly addressing the long-standing difficulty of parallelizing non-linear recurrences.

- **Q-K Projection empirically mitigates the compression-retrieval domain mismatch.** Section 4.1.2 proposes projecting the query onto the key subspace before retrieval. The ablation study (Table 3) shows that removing this projection increases perplexity from 21.04 to 22.01, confirming its practical effectiveness for Challenge 2.

- **The two-stage design cleanly separates efficiency from accuracy.** Stage 1 focuses on throughput (large chunks, context parallelism), while Stage 2 adapts the model to high-resolution inference (small chunks) with only 5% additional compute. Table 2 shows Stage 2 consistently improves upon Stage 1 results.

- **Comprehensive ablation study validates each design choice.** Table 3 systematically tests hierarchical memory (adding local modules improves PPL from 23.53→20.15), global memory (removal hurts → 25.60), Q-K Projection, and Stage 2 fine-tuning, providing clear causal evidence for each component.

## Weaknesses

### Fatal
None.

### Major

- **Speedup comparison uses an unsubstantiated target loss.** Table 1 reports time to reach loss 3.20 as the basis for the 17× speedup claim, but the paper never justifies why 3.20 was chosen or demonstrates that the speedup holds to convergence on a standard metric. Since loss 3.20 (~24.5 PPL) is close to the final perplexity of the Titans C=8 baseline (25.07 PPL), this choice is not obviously unreasonable, but the paper should explicitly justify it and/or additionally report time-to-convergence or time-to-match a fixed baseline quality. Without this, the headline speedup figure rests on an unsupported choice.

- **Accuracy comparisons are confounded by architectural capacity.** The paper claims all models have 150M parameters but does not explain how the parameter count is kept constant when TNT uses 1 global + up to 4 local memory modules versus the original Titans' single memory module. The ablation (Table 3) shows perplexity improving monotonically as local memories are added (21.04→20.74→20.47→20.15). While even TNT with 1 local memory (21.04 PPL) substantially beats Titans (23.53 PPL), the incremental gains from additional modules cannot be attributed solely to the training paradigm rather than increased capacity. The paper should clarify how parameters are balanced and/or include a controlled comparison (e.g., TNT with 1 local memory vs. Titans with equivalent total memory parameters).

- **Generality claims are unsupported by the evaluation.** The paper states "TNT is a general training paradigm applicable to any deep memory module" and the abstract claims "Evaluated on Titans and TTT models." However, TNT is only instantiated on Titans in the experiments. TTT (Sun et al., 2024) appears only as a baseline — not with TNT applied to it. Without at least one additional demonstration on a different deep memory architecture, the claim of generality remains unsubstantiated and the framing is misleading.

### Minor

- **Stage 2 fine-tuning gains are marginal.** The best Stage 2 improvement is from 23.13 to 23.09 PPL (Table 2). The paper does not report variance or confidence intervals, so it is unclear whether this ~0.04 PPL improvement is statistically significant. Since Stage 2 is framed as a key contribution, the paper should discuss significance or provide evidence beyond one-point improvements.

- **Q-K Projection is only applied to local memories.** Section 4.1.2 states "We apply projection only locally as its fine-grained nature makes it more sensitive to the mismatch," but provides no empirical or theoretical justification for why global memory would not benefit from the same projection. While this does not invalidate the approach, the reasoning is incomplete.

- **No variance or confidence intervals reported.** Perplexity and accuracy results in Table 2 and Table 3 are reported as single numbers without training variance. Given that the accuracy metrics show some variability (e.g., TNT Stage 1 with 3 local memories scores 40.2% vs. 41.0% with 2 local), confidence intervals would help assess robustness.

### Trivial
None.

## Nice-to-Haves
- An ablation on the periodic reset interval $S_L$ would help understand the trade-off between parallelism and context preservation.
- A synthetic or small-scale experiment validating that Q-K Projection maps queries into the trained key subspace would strengthen the theoretical motivation.
- Visualizations of memory state evolution across resets (e.g., measuring state distance at reset boundaries) would build intuition for the mechanism.

## Removed Points

These points are flagged to be removed; treat them with caution:

- **"Core contribution is a new architecture, not a training paradigm"**: The paper explicitly introduces both architectural innovations (hierarchical memory, periodic resets) AND a training methodology (two-stage). The framing as a training paradigm is reasonable since the two-stage approach is a training strategy; calling this a framing "misrepresentation" is overly categorical and ignores the paper's dual contribution.

- **"Q-K Projection does not convincingly solve Challenge 2"** (theoretical speculation about non-linear domain): The paper provides clear empirical evidence (Table 3: 22.01→21.04 PPL) that the projection helps. Theoretical purity concerns are not required for an empirically validated technique, and the critic's assertion that it "does not guarantee" anything is speculation, not a demonstrated flaw.

- **"1.3× faster than FlashAttention is suspicious"**: The paper acknowledges TNT lacks custom kernels and provides the runtime data in Figure 4 showing TNT C_L=128 at ~550ms vs. FlashAttention at ~1000ms at 32K length. The flat scaling profile is consistent with the claimed parallelism mechanism and is backed by reported numbers.

- **"Runtime nearly flat with sequence length is suspicious"**: This is a direct consequence of the claimed innovation (context parallelism breaking sequential dependencies). The data is reported transparently and is consistent with the method's design.

- **"The paper does not clarify whether both models use the same number of TPU cores"**: The paper states "Experiments are conducted on a TPUv4 pod (2x2x2 topology, model parallelism 2)" — this is specified for all experiments.

## Novel Insights

The most interesting observation from the reviews that goes beyond the paper's own contributions is the nature of the accuracy vs. capacity confound. The monotonic improvement in Table 3 as local memories are added (23.53→21.04→20.74→20.47→20.15) strongly resembles a scaling law in memory module count, which is not discussed in the paper. This raises an intriguing question: could simply scaling the number of parallel memory modules (without the two-stage training) yield similar gains? The paper's ablation removing global memory (25.60 PPL) shows the hierarchy is critical, but the interaction between the number of local modules and the reset mechanism deserves deeper analysis. Additionally, the nearly flat runtime scaling of TNT C_L=16 across sequence lengths (Figure 4) suggests that at small chunk sizes, the model is dominated by fixed overhead rather than compute — a phenomenon worth investigating for future efficiency improvements.

## Suggestions

1. **Justify or replace the target loss in Table 1.** Show time-to-convergence (e.g., time to reach the final perplexity of the baseline), or report time-per-iteration × iterations-to-quality to make the speedup claim more robust.

2. **Clarify parameter accounting.** Explain how the 150M parameter count is maintained across TNT configurations with different numbers of local memory modules. If the count is approximate or if memory module parameters are negligible relative to the main model, state this explicitly.

3. **Apply TNT to at least one other deep memory architecture** (e.g., TTT) to substantiate the generality claim, or tone down the claim to reflect that TNT has been validated on Titans.

4. **Report variance or confidence intervals** for the main results (Tables 2, 3), particularly for the Stage 2 improvements and reasoning accuracy metrics.

5. **Empirically justify the target loss 3.20** by showing that it corresponds to a meaningful point in training (e.g., the convergence point of the Titans C=8 baseline, or a perplexity threshold of practical interest).

## Score and Decision

The paper makes a genuine contribution to training efficiency for deep memory modules, with a clever architectural innovation (periodic resets enabling context parallelism) and a well-designed ablation study. However, three issues reduce its strength: the speedup claim rests on an unsubstantiated target loss, the accuracy comparisons are confounded by architectural capacity, and the generality framing is unsupported by the evaluation. These are addressable with additional experiments and clarifications, but as presented they weaken the paper's central claims. The method itself is sound and the empirical improvements over Titans are real.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>