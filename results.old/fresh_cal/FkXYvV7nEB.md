Now I have a thorough understanding of the paper and can verify each claim against the text. Let me compose the final review.

## Summary

KV-Dict introduces a post-training KV cache compression method that represents each key/value vector as a sparse linear combination of atoms from a learned, input-agnostic dictionary. The idea is novel: instead of quantizing cache entries, the method decomposes them via Orthogonal Matching Pursuit (OMP) into a handful of dictionary atoms, storing only indices and scaled coefficients in CSR format (3s+2 bytes per vector). A universal dictionary is trained once per model on WikiText-103 and applied off-the-shelf across tasks and inputs. The method achieves memory regimes below what 2-bit quantization can reach (sub-15% of full cache) and demonstrates competitive performance with quantization baselines on LongBench, GSM8K, and MMLU-Pro.

## Strengths

- **Compression below 2-bit quantization limits with meaningful accuracy.** With sparsity s=4, KV-Dict compresses to ~15.8% of full cache (including buffer) — a regime below KIVI-2's practical minimum — and maintains non-trivial accuracy (e.g., 39.2% on GSM8K with Mistral-7B, over 40% on Llama-8B models). This is a genuine capability advance: no existing quantization method can operate at this memory level while retaining usable performance.

- **Universality validated by reconstruction error.** Table 1 shows that a dictionary trained only on WikiText-103 achieves relative reconstruction error of 0.19±0.05 on CNN/DailyMail and 0.19±0.06 on TweetEval — lower than the error of a sparse autoencoder on its own *training* domain (WikiText-103: 0.20). This quantitative evidence supports the claim that a single, fixed dictionary generalizes across diverse input distributions.

- **Consistent Pareto dominance across model scales.** Figure 4 plots memory vs. accuracy on GSM8K for 3 model sizes (1B, 3B, 8B) across 6 compression methods. KV-Dict consistently lies on the Pareto frontier, and in the sub-20% memory regime it is the only method operating in that range while maintaining non-trivial accuracy.

- **Fine-grained, continuous memory control.** Unlike quantization methods locked to discrete bit-widths, the sparsity parameter s allows any integer-level adjustment. Tables 2 and 3 show s ∈ {4, 8, 10, 24, 32} producing smooth memory-accuracy trade-offs, enabling budgets between the fixed points of baselines.

- **Well-motivated method with clean theoretical framing.** The observation of subspace clustering in key states (Figure 2) provides a natural justification for dictionary learning. The memory formula (3s+2 bytes per vector), complexity analysis (O(Nm + l_seq s) vs. O(l_seq m)), and the use of buffering with parallelized OMP are all clearly described.

## Weaknesses

### Fatal
None.

### Major

1. **Asymmetric buffer sizes confound the GSM8K and MMLU-Pro comparisons.** On GSM8K and MMLU-Pro, KV-Dict uses a buffer of nb=128 tokens (kept in full precision), while KIVI is configured with nb=64 "for stronger memory savings" (line 139; Table 3 caption). A larger buffer preserves more recent tokens in full precision, which directly helps task performance independent of the compression method. At the same *reported* KV size, KV-Dict therefore allocates more memory to the buffer and less to the compressed portion, making the comparison unequal. The claim that KV-Dict "outperforms" baselines at ~25% KV size on GSM8K may partly reflect this buffer advantage. The LongBench experiments (where both methods use nb=128) are not affected by this issue, which is good — but the GSM8K and MMLU-Pro results need re-running with matched buffer configurations to isolate the effect of the compression method itself.

2. **Latency analysis lacks any baseline comparisons.** Section 3.3 reports absolute latencies for OMP and the forward pass (Table 5), but provides no comparison to the unmodified model, to KIVI, to ZipCache, or to any other compression method. The forward pass latency (83 ms for N=1024, 133 ms for N=4096, summed across 32 layers) and OMP latency (e.g., ~150 ms for N=4096) are presented without context. The paper claims OMP runs in parallel with generation, but without end-to-end wall-clock time measurements or baseline latencies, the practical viability of KV-Dict in latency-sensitive settings is unsubstantiated. Given that OMP adds significant compute, a practitioner cannot tell whether the overhead is acceptable.

3. **KV size matching between KV-Dict and KIVI in Table 3 is not clearly verified.** The paper states "Sparsity level s is set to match the average KV size of KIVI" (line 151). However, for Mistral-7B, KV-Dict (s=24) reportedly shows 24.6% KV size while KIVI-4 shows 18.7% — a 5.9 percentage point gap. These are not matched sizes. If true, this undermines the claim of fair comparison at similar memory budgets and makes it difficult to attribute performance differences to the compression method rather than to memory allocation discrepancies. The authors should either enforce stricter matching (within 1%) or explain why the matching is approximate and how residual differences affect conclusions.

4. **The "near-lossless" claim is overstated.** The term "near-lossless" appears in the contribution list (line 33) and conclusion (line 211). However, at 12.4% KV size on LongBench, KV-Dict incurs a 5.6 percentage point drop on Llama-3.1-8B-Instruct (line 141), with larger drops on hard tasks like Qasper. Even at 36.9% KV size on GSM8K, the drop is ~3pp on Llama models (line 158). While the contribution text qualifies this as "given similar memory requirements" relative to baselines, the conclusion removes that qualifier. A 5.6pp degradation is not "near-lossless" by any standard, and the term should be calibrated or dropped.

### Minor

1. **Dictionary storage overhead is acknowledged but excluded from KV size percentages.** The 16.8 MB dictionary (line 91) is small relative to model weights but is not incorporated into the reported KV size percentages. For a single-user deployment, this adds to peak memory and should at minimum be noted in the memory accounting.

2. **Eviction-based baselines are missing from the main LongBench and GSM8K tables.** Eviction methods (SnapKV, PyramidKV) are evaluated only on MMLU-Pro (Figure 5). For a paper that claims superiority over eviction methods broadly, their absence from the primary task tables is a gap.

3. **Ablation claims lack numerical evidence in several places.** The error-thresholding early termination (Section 3.2, point 1) and the performance-without-buffer experiment (point 2) are described qualitatively with no accompanying table or figure. The adaptive dictionary learning (point 3) is described but not quantitatively evaluated.

4. **Reported KV size includes the buffer, making comparisons at different buffer sizes not apples-to-apples.** Because the reported percentage averages the buffer (full precision) with the compressed portion, two methods with different buffer sizes but the same total percentage have different ratios of compressed-to-buffer memory. The paper should report the compressed-only memory usage separately or use identical buffer sizes.

### Trivial
None.

## Nice-to-Haves

- **Latency comparison to baselines** under matched conditions (end-to-end time per token for the uncompressed model, KIVI, ZipCache, and KV-Dict at multiple sparsity levels). This is critical for deployment.
- **Ablation on dictionary size N** showing performance at N=512, 1024, 2048, 4096 to justify the chosen size.
- **Per-task breakdown** for LongBench results (beyond the three tasks in the ablation) to show where the method works well and where it struggles.
- **Reporting actual GPU memory usage** (including CSR format overhead, intermediate OMP tensors) rather than just the theoretical KV size percentage.

## Removed Points

- "No comparison to the full uncompressed model as an oracle" — **Removed (factually incorrect).** Tables 2 and 3 both include "Full cache is in FP16" results (lines 149, 151), and line 141 explicitly compares to the full cache.
- "No discussion of the dictionary's additional memory footprint in the total cache calculation" — **Removed (factually incorrect).** Line 91 states: "the dictionaries add an additional 16.8MB to the model's storage requirements for 7B/8B models."
- "Reproducibility: the OMP implementation relies on specific batched routines; the paper should cite or describe the implementation details sufficiently" — **Removed (trivial reproducibility nitpick).** The paper cites Lubonja et al. (2024) and Zhu et al. (2020) for implementation specifics, which is standard practice.
- Strength: "Near-lossless performance at comparable memory budgets" — **Removed (conflicts with verified weakness #4).** The "near-lossless" claim is overstated; the strength is rephrased as competitive performance rather than lossless.
- "Sensitivity to dictionary size N" from Section-by-Section notes — **Moved to Nice-to-Haves.** A reasonable suggestion but not a weakness.

## Novel Insights

The harsh critic's observation about the asymmetric buffer configuration reveals a subtle but important evaluation pitfall: when comparing compression methods at *reported* memory budgets, differences in how methods allocate the budget between a "safe" full-precision buffer and the aggressive compression mechanism can confound comparisons even when total memory is matched. This insight extends beyond KV-Dict to the broader KV cache compression literature: papers comparing quantization, eviction, and sparse methods should standardize buffer sizes (or report compressed-only and buffer memory separately) to isolate the compression method's intrinsic quality.

## Suggestions

1. **Re-run GSM8K and MMLU-Pro experiments with KIVI at nb=128** (or KV-Dict at nb=64) to make the comparison symmetric. If KV-Dict still outperforms KIVI, the case is much cleaner. If performance changes, honestly report both configurations.

2. **Provide latency comparisons** to the unmodified model and at least one baseline (KIVI is the natural choice) under identical conditions. Report end-to-end time per token, not just per-operation latencies.

3. **Enforce strict KV size matching** (within 1%) between compared configurations, or explicitly explain why approximate matching does not affect conclusions. Consider interpolating sparsity levels rather than using only integer s values.

4. **Calibrate the "near-lossless" language.** Use "competitive performance at comparable memory budgets" or "graceful degradation" — terms that accurately describe the observed trade-offs.

5. **Add eviction baselines to LongBench and GSM8K** to support the claim of superiority over eviction methods.

6. **Report compressed-only memory** (without buffer) alongside the total to allow readers to assess the compression method independently of buffer effects.

**Originality:** High. Applying sparse dictionary learning to KV cache compression is novel and well-motivated.  
**Importance of research question:** High. KV cache memory is a major deployment bottleneck.  
**Claims supported?** Partially. The universality claim is well-supported (Table 1). The sub-2-bit compression claim is supported. The comparative performance claims are weakened by asymmetric buffer settings and unclear KV size matching.  
**Soundness of experiments:** Moderate. The evaluation covers multiple models and tasks, but has confounds (buffer sizes) and gaps (latency baselines, eviction baselines on main tasks).  
**Clarity of writing:** Good. The method is clearly explained with proper notation and complexity analysis.  
**Value to the community:** Potentially high. If the evaluation issues are resolved, the method opens a promising new direction.

## Score and Decision

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Reject</decision>