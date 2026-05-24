Now I have a solid calibration picture. Let me synthesize the final review.

**Calibration Summary:**

**Round 1 — Bracketing:** Initial bracketing placed the paper between 4.5 and 7.0 based on weak anchors (EvoEngineer, avg 2.0 — worse than this paper on all dimensions) and middle anchors (Tracing Provenance, avg 5.5; Tool-Agent Evaluation, avg 4.5). The paper is clearly stronger than the weak anchors and comparable to or slightly above the middle anchors.

**Round 2 — Narrowing:** Retrieved anchors within the kernel generation domain: Kevin (avg 5.0, Poster), From Large to Small (avg 5.0, Poster), STARK (avg 5.5, Poster), SparseRL (avg 6.0, Oral), and methodology-adjacent papers (Tracing Provenance 5.5, Code-Induced Reasoning 5.5). 

Comparing to Kevin (5.0, Poster): The current paper achieves stronger KernelBench results (Exec 58/91 vs 50/86 for Kevin on Level 1) with a simpler SFT approach versus Kevin's multi-turn RL. However, Kevin had a more fundamental training-evaluation contamination (trained on 180/200 KernelBench tasks), making the current paper's similar but less severe task-overlap concern more manageable. The current paper is clearly stronger than Kevin.

Comparing to STARK (5.5, Poster): STARK is a multi-agent framework with strong results (100% on KernelBench L1-L3), but requires expensive Claude-4-Sonnet API calls. The current paper is more lightweight (32B model, SFT) and addresses the data scarcity problem more directly. Comparable quality but different contribution type.

The current paper's main contribution — a data curation pipeline for kernel generation with a novel empirical observation about reasoning length — is well-executed with strong ablations. However, two concerns (potential train/eval task overlap, evidence for the core "same-task" claim being weaker than presented) prevent it from being in the 6.5+ range. I place it at 6.0, similar to SparseRL (6.0, Oral) in quality but Poster-level scope.

Now writing the review.

## Summary
2-3 sentence summary...

## Strengths
Verified strengths from the paper...

## Weaknesses
I need to carefully filter the harsh critic's points.

Let me think about each:

1. **Task overlap**: The paper uses KernelBook for training data generation and KernelBench for evaluation. The paper does not discuss whether these are disjoint. This is a legitimate concern, though the specific claim of "largely overlapping" is asserted by the critic without evidence I can verify from the paper. But the paper itself should address this. I'll keep this as a Major weakness but frame it as "the paper does not discuss task-level separation" rather than asserting overlap.

2. **Data generation cost**: Valid - the paper reports 64 A100 hours for fine-tuning but the data generation cost is not reported. However, this is a one-time cost and many SFT papers don't report data generation costs. I'll keep this as a Minor weakness.

3. **Within-task evidence**: Valid - the paper claims "for the same task" but shows cross-task aggregated evidence. The within-task analysis is in Appendix B which is stripped. I'll keep this as a Major weakness.

4. **fast₁ metric**: The paper reports fast₁ at pass@1 and pass@10. The critic says higher thresholds should be reported. This is a reasonable suggestion but not a core flaw. Minor.

5. **ARL circularity**: Addressed by showing the division works across multiple models including DeepSeek-R1-0528. Minor.

Let me also check the strength finder claims:

**Strength 1**: "Empirical discovery that shorter reasoning traces correlate with higher correctness for the same task" - As noted, the "for the same task" part is not convincingly demonstrated with the cross-task aggregated evidence in Figure 3. I should note this caveat.

**Strength 2**: "Data curation method that jointly optimizes..." - Well-supported by Table 4. Keep.

**Strength 3**: "SOTA correctness on KernelBench while using far fewer training resources" - Well-supported. Keep but note the potential task overlap caveat.

Let me also look for the "high-performance" language the harsh critic mentions.

Actually, let me just verify a few things from the paper before writing.

Let me check the 5K-random description - the critic says "5K-random uses only correct kernels, not the full pipeline." Let me look at what the paper says.

From the paper: "Random Selection (5K-random): For each task, we randomly select one correct kernel with its CoT (if such a kernel does not exist, we skip). Then, we randomly select 4,892 tasks along with their corresponding kernel."

So 5K-random does use only correct kernels. That's fine for an ablation baseline.

Let me check the part (c) concern about dataset composition.

From page 4: "(c) In addition, we found that designing a CUDA kernel for a single operator typically requires implementing it as a standalone kernel... Therefore, we need to balance the ratio of these two types of tasks in our dataset. To this end, we identified 544 samples with CUDA kernels for single operators and their CoTs."

And: "In total, we have 3,934 samples in this part. (b) We included kernels with speedups greater than 5, as these high-performance kernels are valuable for learning. This part contains 414 samples."

Total: 3,934 + 414 + 544 = 4,892. So part (c) is in addition to parts (a) and (b). The critic's concern about overlap is addressed by the paper - the three parts are additive, not overlapping.

OK, I have enough information now. Let me write the review.Now I have all the information I need. Let me compile the final review.

## Calibration Report

**All Anchors Retrieved:**
1. LU27DiW5ik — EvoEngineer (avg 2.00, Reject) — Round 1. CUDA kernel optimization via LLMs. Much weaker than current paper; lacks ablation studies, has questionable evaluation methodology.
2. pwBxnCcptN — CASS (avg 3.33, Withdrawn) — Round 1. GPU code transpilation. Different task (transpilation vs generation), less directly comparable.
3. SFUMPoEQoC — RISCompiler (avg 2.50, Reject) — Round 1. RISC-V vectorization. Different domain, weaker execution.
4. y6je0oiwEg — Datatype tagging (avg 2.00, Withdrawn) — Round 1. Algorithmic tasks, small-scale. Not comparable.
5. Eem0IYVORm — Tracing Provenance (avg 5.50, Poster) — Rounds 1&2. Reasoning distillation analysis. Related methodology (data curation for reasoning), comparable quality but different domain.
6. chLlLbI7de — TRACE (avg 4.50, Reject) — Round 1. Agent evaluation framework. Different domain, weaker methodological contribution.
7. cqNAjXUBOV — Tables2Traces (avg 5.00, Reject) — Round 2. Tabular data reasoning distillation. Related methodology.
8. 2H03gm4Rq6 — TRACE Agent Benchmarks (avg 5.00, Poster) — Round 1. Agent benchmark evolution. Different domain.
9. xu1XwVZtDi — Kevin (avg 5.00, Poster) — Round 2. **Directly comparable**: multi-turn RL for CUDA kernel generation on KernelBench. Current paper achieves stronger results (58/91 Exec vs 50/86 on Level 1) with simpler SFT approach. Current paper is clearly stronger on empirical results.
10. vqESUhcSOG — From Large to Small (avg 5.00, Poster) — Round 2. CUDA optimization transfer. Comparable domain, slightly weaker empirical execution.
11. VdLEaGPYWT — SparseRL (avg 6.00, Oral) — Round 2. Sparse CUDA generation with RL. Strong paper in similar domain; current paper is comparable but not clearly stronger.
12. nWaZTH1JMx — STARK (avg 5.50, Poster) — Round 2. Multi-agent kernel optimization on KernelBench. Comparable quality, different approach (agentic vs SFT-based).
13. LIv0bfJZIi — Code-Induced Reasoning (avg 5.50, Poster) — Round 2. Code's effect on reasoning. Related methodology (data-centric study).
14. DM0Y0oL33T — Generative Universal Verifier (avg 8.00, Oral) — Round 1. Multimodal reasoning. Different domain, much higher tier.
15. VKGTGGcwl6 — LLMs Get Lost (avg 8.00, Oral) — Round 1. Multi-turn conversation. Different domain.
16. Various other high-scoring anchors — Not directly comparable.

**Round 1 bracket:** 4.5–7.0
**Round 2 narrowing:** Paper is clearly stronger than Kevin (5.0) and comparable to STARK (5.5) and SparseRL (6.0). Given the empirical SOTA results and clear ablation studies but tempered by unaddressed task-overlap concern and weak within-task evidence for the core claim, the paper sits at **6.0**.

---

## Final Review

## Summary

This paper proposes ConCuR, a curated dataset of 4,892 CUDA kernels with reasoning traces, and KernelCoder, a QwQ-32B model fine-tuned on this dataset via LoRA. The curation pipeline is motivated by the empirical observation that, for PyTorch→CUDA generation tasks, shorter reasoning traces correlate with higher correctness and are largely independent of kernel speedup. On KernelBench Level 1 and 2, KernelCoder achieves state-of-the-art correctness (Exec 58%/59% at pass@1, 91%/95% at pass@10, surpassing DeepSeek-R1-0528, Kevin, and Claude-4-Sonnet) using only 64 A100 GPU hours of fine-tuning. The paper also proposes average reasoning length (ARL) as a difficulty metric for kernel generation tasks.

## Strengths

1. **Well-motivated data curation strategy validated by strong ablation (Table 4).** The paper's core methodological contribution — combining conciseness (short CoT), performance (high speedup), and task-type balance — is convincingly validated. KernelCoder (58/91 Exec Level 1 pass@1/@10) substantially outperforms every single-criterion baseline (5K-random: 39/84, 5K-min: 35/86, 5K-max: 34/86, 5K-speedup: 42/83). The improvement is especially sharp on pass@1 Exec (58 vs 39 for 5K-random), demonstrating that curation boosts single-attempt correctness, not just coverage.

2. **State-of-the-art correctness on KernelBench Level 1 and 2 with efficient training.** Table 1 shows KernelCoder achieves the highest Exec scores among all compared models, including DeepSeek-R1-0528 (52%/55%), Kevin (50%/46%), and Claude-4-Sonnet (33%/26%). This is accomplished with LoRA fine-tuning on only 4,892 samples using 64 A100 GPU hours — far cheaper than Kevin's >600 H200 GPU hours for GRPO training or DeepSeek-R1's 685B-parameter inference.

3. **Reasoning length validated as a difficulty metric across multiple models.** Tables 6–7 show that tasks divided by ARL (<4000, 4000–8500, >8500 tokens) produce consistent monotonic degradation in Exec and geometric-mean speedup across six different models (Kevin-32B, Qwen3-8B, DeepSeek-V3.1-Think, DeepSeek-R1-0528, Qwen3-Coder-Plus, and KernelCoder). This provides a practical tool for constructing difficulty-stratified benchmarks.

4. **Generality across base models.** Table 5 shows SFT on ConCuR consistently improves Qwen3-8B (Exec Level 1: 31→47), Qwen3-32B (68→72), and QwQ-32B (55→91), demonstrating the dataset's quality is not tied to a specific architecture.

5. **Clear empirical observation about reasoning length and correctness (Figure 3).** The paper documents that, in aggregated data across tasks, accuracy drops monotonically from ~0.65 in the shortest CoT bin to ~0.04 in the longest, and incorrect responses have systematically longer CoTs. This finding challenges the assumption in prior work (s1, DeepSeek-R1) that longer reasoning implies higher quality for this domain.

## Weaknesses

### Major

1. **Potential task overlap between training generation and evaluation sets is not discussed.** The paper generates training data from PyTorch programs in KernelBook and evaluates on KernelBench Level 1 and 2. It does not address whether these task sets are disjoint or overlapping. Since KernelCoder outperforms QwQ-32B (which was presumably not fine-tuned on these specific task patterns) significantly on correctness, some of the reported gains could stem from the model having seen similar inputs during training data generation rather than from genuine generalization of the curation method. The paper should at minimum acknowledge this concern, discuss the relationship between KernelBook and KernelBench, or provide evidence that the results hold on a guaranteed-disjoint subset. *(Note: this concern applies symmetrically to Kevin, which trained on 180/200 KernelBench tasks directly, but the current paper should not rely on that as cover.)*

2. **Core claim that "for the same task, shorter reasoning traces tend to be correct more frequently" is not convincingly supported with within-task evidence.** The paper's central observation — which motivates the entire curation pipeline — is stated as a within-task claim, but Figure 3 presents only cross-task aggregated data. As the paper itself acknowledges, "although more challenging tasks typically require a greater number of reasoning tokens," the aggregated trend could simply reflect that easy tasks have short CoTs *and* high accuracy, while hard tasks have long CoTs *and* low accuracy. The within-task analysis is relegated to Appendix B (not available in the reviewed version), leaving a gap between the stated claim and the presented evidence. The curation method may still be effective (as the ablation shows), but the stated rationale is weaker than claimed.

### Minor

3. **Efficiency comparison omits data generation cost.** Table 3 reports "64 A100 GPU hours" for KernelCoder, but this covers only LoRA fine-tuning. Generating 90,810 kernel+CoT samples using Kevin-32B is a significant additional cost not reported or included in the comparison. While data generation is a one-time cost and may still leave the total pipeline cheaper than alternatives when amortized, omitting it makes the efficiency claim incomplete. The paper should report the total compute budget transparently.

4. **fast₁ at pass@10 is a weak indicator of performance.** The paper emphasizes "high-performance" kernels but uses fast₁ (speedup > 1×, i.e., barely faster than eager PyTorch) at pass@10 (one trial out of ten meets the threshold) as the primary performance metric. Pass@1 fast₁ is modest (17% Level 1, 39% Level 2) and the gap over baselines is smaller than for Exec. Results at stricter thresholds (fast₁.₅, fast₂) would better substantiate the "high-performance" language. Table 7 partially addresses this by reporting geometric-mean speedup, but this is not highlighted in the main results.

5. **ARL difficulty metric relies on the same generator used to create training data (Kevin-32B).** Section 6.2 computes ARL thresholds using Kevin-32B and then evaluates KernelCoder (trained on Kevin-generated data) against these thresholds. The paper shows the difficulty division holds across other models (including DeepSeek-R1-0528), which partially addresses circularity, but the thresholds themselves are not validated with a held-out generator.

6. **Certain dataset construction details lack transparency.** The paper does not report how often the condition in part (a) of the curation (shortest CoT also achieving highest speedup) actually held, making it hard to assess how dominant this selection criterion is. The description of part (c) (544 single-operator samples) is also unclear about whether these overlap with parts (a) and (b); the paper says the sum is 3,934+414+544=4,892, suggesting they are disjoint, but this should be stated explicitly.

## Nice-to-Haves

- Reporting stricter speedup thresholds (fast₁.₅, fast₂) at pass@1, especially on the ablation datasets, would directly test whether the curation method selects for genuine performance improvement.
- Computing ARL using a different generator (e.g., DeepSeek-R1) and showing the same difficulty division holds would strengthen the claim that ARL is a generator-independent difficulty metric.
- A qualitative comparison of curated vs. rejected CoTs for the same task would illustrate the "more logical and consistent" claim concretely.
- Confidence intervals or bootstrap estimates for the main results (given ~100 tasks per level) would improve statistical rigor.
- Test-time scaling comparisons (e.g., pass@100) would contextualize the value of SFT against alternative approaches.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. **Address the task overlap concern directly.** Release the task IDs used for training data generation and show they are disjoint from the KernelBench evaluation set. Alternatively, re-evaluate on a held-out subset of KernelBench tasks that are provably absent from KernelBook.
2. **Add within-task analysis to the main paper.** For each task with multiple trials, show the correlation (or rank-correlation) between CoT length and correctness. This directly supports the curation criterion in part (a).
3. **Report the total pipeline compute cost** including Kevin-32B data generation, and discuss how this compares to alternatives when amortized.
4. **Report higher speedup thresholds** (fast₁.₂, fast₁.₅) in the main tables, especially for the ablation study.
5. **Clarify the dataset composition:** state explicitly whether the three parts (a), (b), (c) are disjoint, and report how often the condition in part (a) was satisfied.

## Score and Decision

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>