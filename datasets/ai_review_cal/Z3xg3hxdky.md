- Decision: Reject
- Avg Score: 5.40
- Scores: 6, 6, 3, 6, 6
Now I have a thorough understanding of the paper. Let me produce the final consolidated review.

## Summary

The paper introduces Dynamic Sequence Parallelism (DSP), a sequence parallelism abstraction for multi-dimensional transformers (e.g., video models with spatial and temporal attention). DSP dynamically switches the parallel dimension between computation stages using an all-to-all resharding primitive that is decoupled from the modules themselves. The paper reports per-layer communication volume of \(2M/N\) for DSP versus \(4M/N\) for DeepSpeed-Ulysses, \(8M\) for Megatron-SP, and \(2M\) for Ring Attention, with end-to-end throughput improvements of 32%–10× on 128 H100 GPUs.

## Strengths

- **Well-motivated and original idea.** DSP addresses a genuine gap: existing sequence parallelism methods (Megatron-SP, DeepSpeed-Ulysses, Ring Attention) are designed for single-dimension transformers and do not naturally handle multi-dimensional transformers where independent computations occur along separate sequence dimensions. The observation that resharding only between computation stages (not within them) can eliminate unnecessary communication is sound.

- **DSP's own communication analysis is clearly justified.** The paper provides a concrete per-layer communication volume of \(2M/N\) for DSP on a 2D transformer (two all-to-alls per layer, each with volume \(M/N\)), and Table 2 (dynamic primitives) cleanly defines the three operations. The \(2M/N\) volume is well-derived from the paper's own formulation.

- **Empirical results show meaningful improvements.** End-to-end throughput comparisons on 128 H100 GPUs (Fig. 3) show DSP outperforming DeepSpeed-Ulysses by 32%–75% and other methods by up to 10× across sequence lengths 0.5M–4M tokens. Weak-scaling (Fig. 4) and strong-scaling (Fig. 5) results further demonstrate consistent advantages. Memory consumption (Fig. 7) also favors DSP, with lower total usage and no cache bloat.

- **Adaptability is explicitly discussed.** Section 3.3 demonstrates awareness of compatibility with FlashAttention, multi‑query/grouped‑query attention, Mamba, RWKV, and integration with FSDP, DeepSpeed, Megatron‑LM, etc. This breadth is a genuine advantage over embedded methods that require module-specific modifications.

## Weaknesses

### Fatal
None.

### Major

- **Ambiguity in the baseline communication analysis (Section 5.1).** The paper's derivation of baseline communication volumes for the 2D transformer setting is unclear and insufficiently justified. Specifically:
  - For **DeepSpeed-Ulysses**, the text says "4 communication operations in temporal block" and reports \(4M/N\). It is ambiguous whether this accounts for one block or both blocks. Since a 2D transformer layer has two blocks (spatial and temporal), a reader cannot determine from the text alone whether \(4M/N\) represents the total per-layer volume or only the temporal block's volume. If it is only one block, the per-layer volume would be \(8M/N\).
  - For **Ring Attention**, the reported volume of \(2M\) per layer is stated without clarifying whether it covers one or two blocks. Standard analysis would give \(2M\) per block (each device communicates K and V partitions over N ring steps), yielding \(4M\) for two blocks.
  - The paper does not specify how the baseline methods handle the transition between the two sequence dimensions (spatial → temporal), or whether an explicit reshard is inserted between blocks. This makes it difficult to verify whether the comparison is apples-to-apples.
  
  These ambiguities do not necessarily mean the reported numbers are wrong, but they prevent independent verification of the claimed communication advantage. The DSP volume (\(2M/N\)) is well-justified on its own terms; the issue is in the *baseline* characterization.

### Minor

- **Inconsistent claims about communication reduction.** The abstract and contribution list state "at least 50% communication volume reduction," while the Introduction (line 24) and Conclusion (line 282) claim "at least 75%." Table 3 shows \(2M/N\) vs \(4M/N\) for DeepSpeed-Ulysses (50% reduction). The 75% figure appears to be against Megatron-SP (\(8M\) vs \(2M/N\)), but this anchoring is never clarified. This inconsistency undermines precision.

- **Confounding factor in throughput comparison.** The experiments set "the sequence parallel size to the minimum for each method" (Section 6.1). Since methods have different constraints (e.g., DSP is not head-number-constrained while DeepSpeed-Ulysses and Megatron-SP are), this means different methods may allocate different numbers of GPUs to sequence parallelism vs data parallelism. The resulting throughput comparison therefore reflects not just the efficiency of the sequence-parallel mechanism but also the allocation of GPUs between parallelism dimensions. This should be controlled or discussed.

- **Limited architectural scope.** All experiments use a single 2D-transformer architecture (OpenSora-style) with exactly two sequence dimensions. The paper acknowledges this limitation ("may not adapt well to single-dimensional ones") but does not demonstrate generalization to higher dimensions (\(K > 2\)) or to other multi-dimensional architectures. While this does not invalidate the results for the 2D case, it qualifies the generality of the claims.

- **No error bars or variance reported.** All throughput numbers appear to be single-run point estimates. For a systems paper with hardware-dependent measurements, some indication of variance would improve confidence.

- **No discussion of backward-pass communication costs.** The paper analyzes forward-pass communication only. In training, the resharding strategy must be reversible for gradient computation, and the additional all-to-all during the backward pass could double communication costs. This is not discussed.

### Trivial

None.

## Nice-to-Haves

- A compute-vs-communication breakdown (e.g., profiled communication time as percentage of total step time) would help attribute the throughput gains more directly to the claimed communication reduction.
- Reporting the lines of code or API surface for integrating DSP vs baselines would substantiate the "ease of use" claim.

## Removed Points

These points from the harsh critic are removed with justifications:

1. **Claim that DeepSpeed-Ulysses volume should be \(8M/N\).** The critic's arithmetic assumes each all-to-all has volume \(2M/N\) and multiplies to \(4 \times 2M/N = 8M/N\). Under the paper's consistent definition (Table 2, where Switch all-to-all volume is \(M/N\)), 4 all-to-alls across two blocks gives \(4M/N\). The critic's specific numerical claim is incorrect, even though the broader ambiguity concern (above) stands.

2. **Criticism that "reshape step for dimensions beyond 2" is undefined.** The notation \(\mathrm{Reshape}(\mathbf{X}, [B \times \prod_{j \neq i} S_j, S_i, C])\) is standard and clear. This is a notation nitpick.

3. **Criticism about "High/Low" frequency labels in Table 2 being "misleading."** The paper explicitly notes that Split/Gather are used only at boundaries and their costs are negligible. This is adequately addressed in the text (Section 3.3, "their costs negligible").

4. **Claims that Megatron-SP volume could be wrong.** The paper's description (4 operations per block × 2 blocks = 8 operations, resulting in \(8M\)) is internally consistent under standard definitions. The critic's confusion stems from ambiguous phrasing, not an actual arithmetic error.

5. **Speculative claims about "unfair baseline setup" and that results "may reflect an unfair baseline setup rather than genuine superiority."** These are assertions without evidence from the paper. The paper does not describe a deliberately unfair setup; it describes ambiguity in the analysis. The two are different.

6. **Criticism about missing appendix content and missing related works.** Removed per instructions: appendix content is stripped by the parser, and I cannot verify missing related works without external sources.

## Novel Insights

The harsh critic and strength finder between them surface one observation not fully articulated in the paper: the tension between the "minimum sequence parallel size" experimental choice and the claim of "apples-to-apples" comparison. The critic identifies this as a potential confound, while the paper treats it as a natural consequence of DSP's fewer constraints. The insight is that DSP's advantage has two sources — (1) fundamentally lower communication volume per operation, and (2) the ability to use smaller sequence-parallel groups (freeing GPUs for data parallelism) — and the experimental design does not cleanly separate them. Disentangling these two effects would strengthen the paper.

## Suggestions

1. **Clarify the baseline analysis (Section 5.1).** Provide a step-by-step description of how each baseline method is applied to a 2D transformer layer with two blocks, explicitly stating: (i) what communication happens within each block, (ii) what communication (if any) happens between blocks, and (iii) how the total per-layer volume is computed. Then re-derive the numbers in Table 3 with clear formulas.

2. **Harmonize the communication reduction claims.** Pick one number (50% or 75%) that is precisely defined relative to a specific baseline, or state the range explicitly (e.g., "50% vs DeepSpeed-Ulysses, up to 75% vs Megatron-SP").

3. **Address the sequence-parallel-size confound.** Either run a controlled experiment where the same number of GPUs is used for sequence parallelism across all methods, or explicitly discuss how the GPU allocation differs and why the comparison is still fair.

4. **Add a discussion of backward-pass costs.** Analyze whether the switch all-to-all is used symmetrically in the backward pass and what the total (forward + backward) communication cost is.

5. **Add variance information.** Report throughput across multiple runs or at least indicate the measurement methodology (single run, best of several, etc.).
