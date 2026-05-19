- Decision: Reject
- Avg Score: 3.75
- Scores: 8, 3, 3, 1
Now I have all the information needed. Let me produce the final consolidated review.

## Summary

ZO-Offloading presents a CPU-offloading framework specialized for zeroth-order (ZO) fine-tuning of large language models. By exploiting ZO's dual-forward-pass structure (which eliminates backward passes and activation caching), the system dynamically offloads model parameters to CPU memory and overlaps upload, computation, and offload across three CUDA streams. Additional optimizations include reusable one-block GPU memory, a fused parameter-update strategy, low-bit compression for AMP mode, and asynchronous checkpointing. The headline result is fine-tuning OPT-175B on a single 24 GB GPU — a capability no prior method achieves — with throughput comparable to the MeZO baseline for models where MeZO fits in GPU memory.

## Strengths

- **Enables OPT-175B fine-tuning on a single 24 GB GPU**: Table 1 shows ZO-Offloading fits OPT-175B in both FP32 and FP16 modes using only 48 MB of GPU memory, while the baseline MeZO fails due to memory constraints. This is the paper's central and most compelling claim — a genuine capability breakthrough for hardware-constrained practitioners.

- **Dynamic scheduler with proven throughput benefit**: Section 5.1 and Algorithm 1 describe a three-stream CUDA scheduler that uploads, computes, and offloads consecutive transformer blocks concurrently. The ablation study (Table 2) quantifies its impact: removing the scheduler drops OPT-6.7B throughput from 0.227 to 0.176 token/sec (77 % of the full system), establishing that the overlap is measurably effective.

- **Reusable one-block memory eliminates malloc/free overhead**: Section 5.2 pre-allocates a single reusable GPU buffer. Table 2 shows this feature has the largest individual impact — disabling it drops OPT-6.7B throughput to 0.084 token/sec (37 % of the full system), far greater degradation than disabling the scheduler or efficient updating.

- **Efficient parameter updating fused with dual forward passes**: Section 5.3 applies the ZO gradient update before the next iteration's dual forward passes, halving CPU-GPU transfers compared to the naive approach. Table 2 confirms a non-zero contribution (e.g., OPT-6.7B throughput falls to 0.210 from 0.227 when disabled).

- **AMP mode with low-bit compression evaluated across formats**: Section 6.3 (Table 3) evaluates FP16, BF16, and FP8 compression during CPU-GPU transfers. For communication-bound models (OPT-2.7B, OPT-6.7B), FP8 compression yields higher throughput than no compression, and the finding that OPT-1.3B (computation-bound) is an exception is correctly noted and explained.

## Weaknesses

### Fatal

None.

### Major

- **Accuracy verification claimed but absent from the paper**: Section 6.1 states "We conducted accuracy verification experiments to confirm this" and that these tests "affirm that our ZO-Offloading method preserves model accuracy across different model sizes and data formats," yet **no accuracy numbers, convergence curves, or task-performance metrics appear anywhere in the manuscript**. The paper's title and framing center on "fine-tuning," and a central claim is that the framework operates "without any additional time cost and decreases in accuracy" (lines 25, 27 — the grammar suggests a missing "no" before "decreases"). For a system that claims to enable fine-tuning, providing zero evidence of actual task accuracy is a significant evidential gap. While the core contribution (throughput and memory reduction) does not depend on introducing a new optimization algorithm, the paper explicitly asserts accuracy preservation as a verified property and should present the supporting data.

### Minor

- **Asynchronous checkpointing described but not experimentally evaluated**: Section 5.5 presents a well-designed asynchronous checkpointing scheme that exploits CPU residency and overlaps disk saving with computation. However, no experimental results validate its effectiveness (e.g., checkpointing latency per iteration, impact on training interruption, or CPU memory overhead). As it stands, this component is an unvalidated design proposal within an otherwise evaluated system.

- **Communication-computation overlap is asserted but not directly measured**: The scheduler design (Section 5.1) claims that ZO's dual forward passes "extend computation times, communication delays are no longer the primary bottleneck in most scenarios." While the throughput numbers provide indirect evidence, the paper does not present direct measurements (e.g., GPU utilization, per-stream timeline breakdown) that would quantify the overlap efficiency or characterize when communication-dominated vs. computation-dominated regimes occur. The 13 % throughput drop for OPT-125M suggests the scheduler is not fully effective in all regimes, but the conditions favoring different regimes are not analyzed.

- **No naive ZO-offloading baseline for throughput comparison**: The evaluation compares only against MeZO (GPU-only, no offloading). The ablation study (Table 2) convincingly shows the contribution of each feature via reverse ablation, but a comparison against a straw-man ZO-offloading implementation (e.g., synchronous block-by-block offloading with no pipelining, no reusable memory) would more directly demonstrate the aggregate benefit of the system-level contributions. As-is, a practitioner cannot gauge how much improvement the full framework provides over a simple first-attempt offloading approach.

### Trivial

- Line 25 and line 27 contain "operates without any extra time cost and decreases in accuracy" and "achieved with no additional time cost and decreases in accuracy" — these appear to be missing a negation (likely "no decrease in accuracy" or "without decrease in accuracy").

## Nice-to-Haves

- Including absolute throughput values alongside the ratios in Table 1 would let readers assess real-world speed directly, rather than computing from the MeZO baseline numbers.
- A brief discussion of how ZO convergence rates (established in prior work like MeZO) interact with the reported throughput to yield estimated wall-clock training times for a representative fine-tuning scenario would strengthen the practical significance claims.
- Reporting variance (e.g., multiple runs) on throughput numbers would strengthen the reliability of the measurements.

## Removed Points

These points were considered but removed with justification:

- **Convergence analysis missing** (Harsh Critic, point 3): The critic asks for analysis of how many ZO iterations are needed to converge and estimated wall-clock time. This is scope creep — the paper is a systems paper about throughput and memory, not about optimization convergence. ZO convergence properties are well-studied in prior work (Malladi et al., 2023); the system contribution stands on throughput/memory metrics.
- **Memory numbers questionable for OPT-30B** (Harsh Critic, Section-by-Section): The 565 GB figure for OPT-30B in Table 1 cannot be verified from the extracted text (table is an image), and the critic concedes it "does not undermine the core comparison." Speculative without access to the table data.
- **AMP compression drift concern** (Harsh Critic, Section 5.4): The critic speculates that low-bit compression during offload could cause numerical drift. This is a hypothetical concern with no evidence — the paper describes computing updates in FP32 and states accuracy was verified. Without accuracy results to check (a separate weakness), this is speculation.
- **Baseline comparison is "misleadingly narrow"** (Harsh Critic, point 2): The critic calls for a non-optimized ZO offloading baseline. The reverse ablation study (Table 2) actually provides this information by disabling features and measuring the throughput drop. While a forward-adding ablation would be cleaner, the reverse ablation is a valid approach for tightly integrated systems and partially addresses this concern. Downgraded from "critical" to minor.
- **Training time estimates / statistical significance / GPU memory breakdown** (Harsh Critic, Missing Parts): These are generic requests that would strengthen the paper but are not weaknesses in their current absence. The throughput numbers and memory figures already communicate the core contributions.
- **Strength Finder's strength about asynchronous checkpointing** is partially dropped because the design is novel but unvalidated — it belongs as a described design, not a demonstrated strength.

## Novel Insights

None beyond the paper's own contributions. The reviewers' analyses surface no contradictory evidence or alternative interpretation that changes the paper's framing.

## Suggestions

1. **Add accuracy results** for at least one task (e.g., SST-2, consistent with the throughput experiments) across multiple model sizes (OPT-1.3B, OPT-6.7B, OPT-13B) comparing MeZO vs. ZO-Offloading. This is the single most impactful improvement — it directly addresses the paper's most significant gap and costs minimal experimental overhead since the authors already state the experiments were conducted.

2. **Include direct overlap efficiency measurements** (e.g., a timeline showing GPU utilization across CUDA streams during one iteration) to substantiate the claim that ZO's dual forward passes make communication no longer the primary bottleneck.

3. **Evaluate the asynchronous checkpointing scheme** experimentally, even if briefly — reporting checkpointing latency per iteration under the proposed scheme vs. a synchronous baseline would validate this design.

4. **Fix the grammar issue** in lines 25 and 27 where "decreases in accuracy" appears to be missing a negation ("no decrease in accuracy").
