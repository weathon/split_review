Now I have all the information I need. Let me synthesize the final review.

My round-1 bracket placed this paper between 5.0 and 6.5. After round-2 narrowing with papers like Palu (5.75, accepted), OSTQuant (6.20, accepted), and I-LLM (5.00, rejected), I can place LUT-GEMM at approximately **5.5**. It is stronger than all the rejected papers (I-LLM at 5.00, LRQ at 5.25, KVTQ at 4.40, k-OOC at 4.33) due to its real GPU kernel measurements, comprehensive model evaluations, and clear engineering contribution. It is slightly below accepted papers like SpQR (6.50) and OSTQuant (6.20) which have stronger analytical/theoretical depth, but comparable to Palu (5.75, accepted) which similarly contributed an optimized kernel with some validation gaps.

Now let me write the consolidated review, applying filtering discipline strictly.

## Summary
2-3 sentence summary of the paper's contribution.

## Strengths
- strength 1 with evidence
- strength 2 with evidence

## Weaknesses
### Fatal
### Major
- weakness 1 — why it matters
### Minor
- weakness 1 — why it matters
### Trivial
- weakness 1

## Nice-to-Haves
- suggestion that would improve but is not a core flaw

## Removed Points
Points that were removed with justification

## Novel Insights

## Suggestions

## Score and Decision

Let me write it up now.## Summary

This paper presents LUT-GEMM, a GPU kernel for quantized matrix multiplication that avoids the expensive dequantization step required by prior weight-only quantization methods (e.g., OPTQ, AWQ). The key idea is to represent quantized weights in the Binary-Coding Quantization (BCQ) format and use lookup tables (LUTs) to precompute all possible dot products between activation sub-vectors and binary weight patterns, trading arithmetic for table lookups. The paper extends BCQ with a bias term to also represent uniform quantization, enabling LUT-GEMM to accelerate a wide range of existing quantization schemes. Experiments on OPT-175B and LLaMA models show substantial latency improvements (up to 2.1× over OPTQ on OPT-175B) and enable single-GPU inference for models that would otherwise require multiple GPUs, with measured energy savings.

## Strengths

- **Real GPU kernel with measured speedups across multiple scales.** Table 1 reports kernel-level latency on the first FFN layer of OPT-175B: LUT-GEMM with 3-bit achieves 0.225 ms vs. OPTQ's 0.3599 ms (1.6×) and cuBLAS FP16's 0.7256 ms (3.22×). These are real hardware measurements on A100 GPUs, not simulations or extrapolations (Section 4.1, Table 1). The end-to-end results in Tables 3 and 4 confirm that these gains translate to full-model inference.

- **Enables single-GPU inference for models that otherwise require model parallelism.** OPT-175B requires 8 GPUs with FP16 (42.4 ms) but runs on a single GPU with LUT-GEMM 3-bit (51.6 ms) — comparable latency with 8× fewer GPUs (Table 4). Similarly, LLaMA-65B is OOM on a single GPU with FP16 but fits with 3-bit LUT-GEMM (31.3 ms, 1-GPU) (Table 3). The energy measurements in Table 2 (LUT-GEMM-1-12288-2: 43.49 mJ vs. cuBLAS-8: 299.96 mJ) concretely quantify this benefit.

- **Extends BCQ to represent uniform quantization via a bias term.** Section 3.3 and Figure 3 show how adding a bias term to BCQ allows it to represent both non-uniform (q distinct scaling factors) and uniform (single scaling factor) quantization. This is the conceptual bridge that lets LUT-GEMM accelerate weight formats from methods like AWQ and OPTQ, which is a genuine insight beyond pure kernel engineering.

- **Provides a fine-grained latency-accuracy trade-off via group-wise quantization.** Figure 4(a) maps normalized latency against group size g, showing that for g ≥ 128 latency plateaus while accuracy continues to improve. Table 5 quantifies this for OPT-175B: with 2-bit quantization, varying g from 32 to 128 trades perplexity (8.94→9.58) for latency (55.2→46.5 ms). This gives practitioners a principled control knob.

## Weaknesses

### Fatal

None.

### Major

- **The conversion from uniform quantization to BCQ is asserted but not empirically validated.** The paper claims in Section 3.3 that any uniform quantization (e.g., from AWQ or OPTQ) can be exactly reformulated in extended BCQ form, with details deferred to the stripped Appendix C. The perplexity numbers in Tables 3 and 5 come from models run through LUT-GEMM, but the paper never verifies that the BCQ-converted weights produce the same perplexity as the original quantized weights run through the original method's kernel. Table 5 explicitly notes that perplexity values are "extracted from the OPTQ reference" (line 239), not measured end-to-end through LUT-GEMM, so the reader cannot tell whether the BCQ conversion introduces additional approximation. If the conversion is not exact, the speed-accuracy trade-off presented for LUT-GEMM may not be a fair comparison against the prior work whose weights it claims to reuse. A simple verification experiment — comparing perplexity of the same quantized weights run with and without LUT-GEMM — would resolve this.

- **The LUT construction overhead is not measured or reported in any experiment.** The paper's complexity model (Eq. 2) includes a build term O(2^μ · n/μ) and assumes it is negligible when mq ≫ 2^μ. But for typical LLMs (m=12288, q=3), 2^μ could be 256 or 1024, meaning mq = 36864 while the build cost involves 2^μ · n/μ operations — potentially tens of thousands of FP16 arithmetic operations that are material at GPU timescales. The kernel-level (Table 1) and end-to-end (Tables 3–5) latency measurements are not broken down to show how much time is spent building LUTs vs. reading from them vs. scaling. Without this breakdown, the reader cannot verify that the claimed "computational reduction" is realized, or determine whether the speedup is primarily a memory-bandwidth effect of reduced weight movement.

### Minor

- **No error bars or multiple-run statistics for any latency measurement.** GPU kernel timing can vary significantly due to clock throttling, memory contention, and thermal effects. All latency numbers (Tables 1–5) are reported as single values without variance. While single-run evaluation is common in this area (e.g., OPTQ report similarly), reporting at least mean over multiple runs would strengthen the evidence.

- **The comparison against OPTQ in Table 1 does not explicitly report memory footprint for each configuration.** The critic's concern about differing compression ratios is largely addressed by using the same q and g (3-bit, g=128) for both kernels — Eq. 4 shows the memory footprint is dominated by binary weights at g ≫ 16 — so the comparison is substantially fair. However, explicitly reporting the effective bits-per-weight for each row would remove any ambiguity and strengthen the claim that the speedup comes from avoiding dequantization rather than from more aggressive compression.

- **The hyperparameter μ (sub-vector length for LUT construction) is not reported for the end-to-end experiments.** The kernel development section (3.2) describes μ and its role, but Tables 3–5 do not specify what μ values were used. Since the LUT size (2^μ) directly affects both the build cost and the computational reduction ratio (q/μ from Eq. 2), reporting μ would help readers assess the overhead.

### Trivial

- None. (The paper is reasonably well-written; the minor issues are substantive enough to remain in Minor.)

## Nice-to-Haves

- A latency vs. batch size curve (batch 1, 2, 4, 8, 16) for at least one representative model/config. The paper already acknowledges (Section 6) that performance degrades with batch size; quantifying the boundary where LUT-GEMM loses its advantage would help practitioners understand when to use it.
- A brief ablation showing perplexity before and after BCQ conversion for the same quantized weights — even a single model/bit-width pair — would fully address the validation concern in Major weakness #1.
- Reporting μ values and LUT build-vs-read breakdown for one representative layer would strengthen the complexity analysis claim.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **Harsh Critic Issue 4 (batch size analysis):** "The paper does not analyze throughput for batched inference." The paper explicitly scopes itself (Section 6) to single-batch generation, which is the relevant regime for autoregressive LLM inference. All experiments use batch size 1. Criticizing the absence of multi-batch analysis beyond the paper's stated scope is scope creep.

- **Harsh Critic Issue 3 (memory footprint differences):** The critic claims the speed comparison against OPTQ may be unfair due to different memory footprints. With q=3, g=128, Eq. 4 gives BCQ: 3 + 16/128 = 3.125 bits/weight, while uniform quantization similarly uses q + 16/g + negligible zero-point overhead. The memory footprints are nearly identical. The critic's speculation about "more aggressive memory compression" is not supported by the analysis. This is demoted to a Minor note about explicit reporting rather than a concern about fairness.

- **Criticism about Table 5's model size column:** The critic claims the compression ratio for g=32 is computed assuming scaling-factor overhead is negligible. In fact, the numbers exactly match the formula from Eq. 4: for q=2, g=32, effective bits = 2 + 16/32 = 2.5, ratio = 16/2.5 = 6.40 ✓; for q=2, g=128, bits = 2 + 16/128 = 2.125, ratio = 16/2.125 = 7.53 ✓. The scaling-factor overhead is correctly included.

- **Strength Finder generic strengths:** Generic statements about the problem being "important" or "well-motivated" — these are true of the area but not specific to this paper's contribution.

## Novel Insights

None beyond the paper's own contributions. The harsh critic's framing of the BCQ conversion validation gap is the most insightful observation — it correctly identifies that the paper's claim of generality (supporting any uniform quantization method) rests on an unverified equivalence. The reviewer's suggested fix (compare perplexity with and without LUT-GEMM for the same quantized weights) is precisely what is needed. Beyond this, the reviews surface no fundamental flaw that the paper's authors would not already be aware of from reading their own draft.

## Suggestions

1. Add a verification experiment: measure perplexity of an AWQ/OPTQ-quantized model run through the original (dequantization-based) kernel, then run the same quantized weights through LUT-GEMM and confirm perplexity is identical. This single addition would resolve the most significant concern.

2. Report a latency breakdown for one representative layer (e.g., OPT-175B FFN, 3-bit, g=128): time spent on LUT construction, LUT reads, scaling, and accumulation. This would validate the complexity model in Eq. 2 and clarify where the speedup comes from.

3. Add standard deviation over 5–10 runs of the kernel-level latency measurements in Table 1.

4. Report the hyperparameter μ used in the end-to-end experiments and justify the choice relative to the trade-off from Eq. 2.

## Score and Decision

**Bracket and calibration summary:** Round 1 bracketed the paper between 3.0 and 8.0, narrowing to a plausible range of (5.0, 6.5). Round 2 pulled anchors including SpQR (6.50, accepted), OSTQuant (6.20, accepted), Palu (5.75, accepted), LRQ (5.25, rejected), and I-LLM (5.00, rejected). LUT-GEMM is clearly stronger than the rejected papers (LRQ, I-LLM, KVTQ, k-OOC, FPTQ) because it presents actual GPU kernel measurements with real speedups, comprehensive model evaluations, and a concrete engineering contribution. It is slightly weaker than SpQR (6.50) and OSTQuant (6.20) which have stronger analytical depth and theoretical grounding. It is comparable to Palu (5.75, accepted poster) — both contribute optimized GPU kernels with novel methodology and have some evidential gaps. The BCQ conversion validation gap and the unreported LUT overhead prevent this paper from reaching the 6.0+ tier, placing it at the lower end of the accept range.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Accept</decision>