Now let me write the final consolidated review.

## Summary

This paper identifies a computation imbalance problem that arises in 3D parallel training of vision-language models due to heterogeneous vision/language components and varying input sizes — a problem the paper demonstrates concretely by showing that naively switching from DeepSpeed ZeRO-3 to Megatron-DeepSpeed on InternVL-Chat-1.5 *degrades* throughput (0.63x). The authors propose OmniBal, a three-component framework that rebalances computation across data (iterative sampling and filtering for balanced mini-batches), model (search-based pipeline partitioning), and memory (adaptive re-computation). Extensive experiments across 9 model combinations (1B–110B), multiple datasets, both DeepSpeed and Megatron-DeepSpeed backends, and various image resolutions show consistent speedups of 1.5x–3.2x while maintaining benchmark performance.

## Strengths

- **Clean ablation confirming each component delivers additive gains.** Table 2 shows data balance alone (61.8→51.9), adding model balance (→29.0), and adding memory balance (→21.3 GPU days). Each component contributes meaningful improvement, and the pipeline dependency (data→model→memory) is empirically validated.

- **ISF achieves zero padding while maintaining low cross-device imbalance.** Table 3 reports pad ratio = 0 (versus 0.31 baseline, 0.378 device-group, 0.014 sorted) and simultaneously achieves low dist ratios (0.02 ViT, 0.14 LLM). No other method in the comparison achieves both goals simultaneously — sorted has low padding (0.014) but poor dist ratio (0.47/0.40); device-group has better dist ratio but high padding (0.378).

- **Search-based BMP reduces communication volume where profile-based methods increase it.** Table 4 shows DreamPipe (profile-based) increases communication by +16.6 MB relative to the parameter-based partition, while BMP reduces it by −21.0 MB. Despite slightly higher forward-time variance, BMP achieves the best GPU days (29.0 vs. 30.9), validating the trade-off between load balance and communication cost.

- **Consistent speedups across 9 model combinations from 1B to 110B.** Table 5 tests InternVL-6B and EVA-CLIP variants (1B–18B) paired with Llama3-8B/70B, InternLM2-20B, Yi-34B, and Qwen1.5-110B, achieving 1.9x–3.2x speedups. The largest model (Qwen1.5-110B, 3.2x) provides the strongest evidence that the method scales with problem severity.

- **ISF converges in <1 minute** (Section 4.3): stabilizes within 5 iterations, with overhead negligible relative to multi-day training runs.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

- **Abstract's headline speedup conflates the baseline.** The abstract claims "about 1.8x speed-up" compared with "open-source training code of InternVL-Chat." The original InternVL-Chat training code uses DeepSpeed ZeRO-3, against which OmniBal achieves **1.54x** (38.9→25.3 GPU days, Table 1). The 1.83x figure is against the Megatron-DeepSpeed baseline (61.8→21.3), which the paper itself shows is 0.63x slower than DeepSpeed for this task — i.e., the larger speedup partly reflects fixing a problem introduced by switching backends. The main text is transparent about both comparisons, but the abstract's wording conflates them. This should be corrected to avoid misleading readers.

- **No variance or error bars for any experimental result.** GPU days and benchmark scores in every table are single scalars. For benchmark metrics like MMVet that vary 45.0–50.0 across conditions for the same model (Table 1), the absence of error bars makes it impossible to distinguish meaningful differences from noise. While running multiple seeds for 38.9-GPU-day training runs is genuinely expensive, the benchmark evaluations themselves could be repeated to provide error bars, and the limitation should at minimum be acknowledged.

- **No sensitivity analysis of the search radius (r=1) for model partitioning.** The search space is limited to partitions within ±1 layer of a greedy anchor, yielding just 27 candidates for N=4. The paper does not examine whether the greedy anchor is close to optimal, nor show that larger radii (r=2, r=3) produce no further gains. This is not a fatal gap — BMP empirically beats the profile-based competitor at 29.0 vs. 30.9 GPU days — but the lack of sensitivity analysis weakens the claim that the search is genuinely finding the optimum.

- **No training loss curves to verify that ISF regrouping preserves learning dynamics.** The paper shows final benchmark scores are comparable, which is the most practically important check. However, showing that training loss curves overlap between OmniBal and baseline would more directly address whether the modified mini-batch composition changes the effective training distribution.

### Trivial

- **ISF algorithm prose is ambiguous about data handling.** The text in Section 4.3 says "removing all non-satisfying samples within P." Examining Algorithm 2 shows that undersized groups are removed from the candidate set P but their samples remain in D for future iterations — data is not discarded. This should be clarified to prevent reader confusion.

## Nice-to-Haves

- Report cluster topology (interconnect, nodes, NVLink vs. InfiniBand), since communication cost is an explicit optimization target in BMP.
- Discuss whether the method applies to training paradigms beyond SFT (e.g., RLHF, continual pre-training).
- Report overhead of profiling per-layer computation time and running 20 iterations per partition candidate, currently omitted.

## Removed Points

The following points from the input reviews were evaluated and removed with justification:

1. **"Dataset discrepancy undermines comparison to prior work"** — The paper transparently states the InternVL-1.5 dataset is unavailable and uses InternVL-1.2. All methods are compared on identical data, making relative comparisons valid. The paper does not claim that its GPU days match published InternVL-1.5 costs.

2. **"Headline speedup is framed against deliberately weakened baseline"** — While the abstract wording is imprecise (handled above), the harsh critic's stronger claim that "the method's primary contribution is enabling Megatron-DeepSpeed to work well" is incorrect: OmniBal also achieves 1.54x on the original DeepSpeed setup. The larger Megatron improvement is expected because that backend introduces pipeline parallelism, which the model partitioning component specifically addresses.

3. **"ISF has an unresolved data discarding problem"** — Verified against Algorithm 2: groups that fail the threshold have their samples remain in D for future iterations. No data is discarded. The prose is ambiguous (noted in Trivial weaknesses) but the algorithm is correct.

4. **Various formatting/style nitpicks, missing related-work complaints, and speculative "could be" criticisms** — Removed per filtering rules. These reflect reviewer knowledge gaps or parser artifacts, not author errors.

## Novel Insights

None beyond the paper's own contributions. The central insight — that computation imbalance in VLM 3D parallelism must be addressed at three interconnected levels (data→model→memory), with each level enabling the next — is the paper's genuine conceptual contribution, and no reviewer produced a deeper analytical insight beyond this framing.

## Suggestions

1. Correct the abstract to report speedups against both baselines transparently, e.g., "achieving a 1.54× speedup over the original DeepSpeed-based training code and up to 1.83× when using Megatron-DeepSpeed with our method."

2. Clarify the ISF filtering-stage description: state explicitly that samples from undersized groups remain in D and are re-sampled in subsequent iterations.

3. Add training loss curves for at least one representative setting (e.g., 6+20B, InternVL-1.2M) to confirm learning dynamics are unaltered.

4. Discuss sensitivity of ISF hyperparameters Qv and Qt, which are determined via a heuristic (Qt=4K, Qv derived from average text-to-image ratio).

5. Acknowledge the r=1 limitation and ideally provide a sensitivity study showing that larger radii do not yield further gains.

MY FINAL SCORE: <score>8.0</score>
MY FINAL DECISION: <decision>Accept</decision>