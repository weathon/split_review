## Summary

This paper presents a data synthesis and curation pipeline for CUDA kernel generation, motivated by the observation that concise reasoning traces correlate with higher-quality kernels. The authors construct the ConCuR dataset (4,892 curated CUDA kernel + CoT pairs) and fine-tune QwQ-32B into KernelCoder, which achieves strong results on KernelBench (58% pass@1 Exec on Level 1, 59% on Level 2) with only 64 A100 GPU hours of training — far more efficient than existing approaches like Kevin (>600 H200 hours). The paper also proposes average reasoning length (ARL) as a difficulty metric for kernel generation tasks.

## Strengths

- **Novel and counterintuitive observation linking reasoning conciseness to correctness (Figure 3).** The paper provides empirical evidence from 90,810 generation samples that shorter reasoning traces strongly correlate with correct kernels (accuracy dropping from ~0.65 at 0–256 tokens to ~0.04 at 20k+ tokens), while also showing speedup is roughly independent of reasoning length (r = -0.047). This directly challenges assumptions in prior work (s1, DeepSeek-R1) and is a genuinely useful finding for the community.

- **Impressive training efficiency.** KernelCoder achieves state-of-the-art performance using only 4,892 samples and 64 A100 GPU hours (Table 3), compared to Kevin's >600 H200 hours and AutoTriton's 640+ GPU hours. This is a concrete and practically important contribution.

- **Data curation pipeline that works better than any single criterion.** The ablation study (Table 4) shows that the full three-component selection (shortest CoT among fastest kernels + high-speedup kernels + single-operator balancing) substantially outperforms random selection (58% vs 39% Exec Level 1), max-length selection (34%), min-length selection (35%), and speedup-first selection (42%). This empirically validates the multi-criteria design.

- **The dataset generalizes across multiple base models.** Table 5 shows consistent improvements when fine-tuning Qwen3-8B, Qwen3-32B, and QwQ-32B on ConCuR, demonstrating the dataset's quality is not tied to a single architecture.

## Weaknesses

### Major

- **The central causal claim — that conciseness causes better kernels — is not cleanly isolated.** The ablation study compares fundamentally different selection strategies that conflate *which tasks are selected* with *which kernel within a task is selected*. 5K-min selects the shortest CoT per task then keeps the 4,892 tasks with shortest overall CoTs, while KernelCoder uses a multi-criteria procedure (shortest CoT among fastest kernels + speedup > 5 + single-operator balancing). A cleaner test would fix the task set and vary only the within-task selection criterion (e.g., compare training on shortest-CoT vs. longest-CoT kernels for the same tasks, holding speedup constant). Without this, the paper's title claim ("Conciseness Makes State-of-the-Art Kernel Generation") is not fully supported by the experimental design.

- **The evaluation does not properly discuss or control for the relationship between training tasks (KernelBook) and evaluation tasks (KernelBench).** The paper trains on kernels generated from KernelBook tasks and evaluates on KernelBench. While the paper does not claim these are the same tasks, it also does not analyze their overlap or discuss the potential generalization concern. This is particularly important because the strongest baseline (Kevin*) is noted as explicitly training on 180 KernelBench problems (Table 3 footnote), and the paper's own comparison against frontier models not exposed to this distribution (DeepSeek-R1, Claude-4-sonnet) does show strong results — but the paper should transparently address this. A generalization test on held-out tasks (e.g., KernelBench Levels 3-4, or a different benchmark like TritonBench) would substantially strengthen the claims.

### Minor

- **The ablation does not isolate the contribution of each individual selection criterion.** The paper combines three criteria in the full method: (a) shortest CoT among fastest kernels, (b) speedup > 5, (c) single-operator balancing. Testing each criterion alone and in pairwise combinations would help understand which component drives improvement, and whether the three criteria interact synergistically.

- **ARL as a difficulty metric is validated only on models related to the generator.** While Table 7 shows the trend holds across multiple models (including DeepSeek-R1-0528, which mitigates pure circularity concerns), the ARL is computed from Kevin-32B's generations. The paper would benefit from computing ARL using a different generator (e.g., DeepSeek-R1) and showing the difficulty division is consistent.

- **Exclusion of KernelBench Levels 3 and 4.** The paper excludes these as "exceeding the capabilities of current LLMs" — this is reasonable but means we don't know how much headroom exists. Reporting even baseline performance on these levels would be informative.

### Trivial

- **$G_{\text{speedup}}$ in Table 7** is labeled as "geometric average of speedups" but the exact formula is not given. This is a minor clarity issue.

- **The paper should note that Kevin* also trains on KernelBench tasks** (as shown in Table 3 footnote) when discussing the fairness of comparisons.

## Nice-to-Haves

- A qualitative analysis of short vs. long reasoning traces for the same task, showing concrete examples of "overthinking" vs. "concise logical" traces, would strengthen the causal argument.
- Testing the ConCuR dataset on a non-Qwen base model family (e.g., Llama, CodeLlama) would strengthen the claim of broader applicability.
- Reporting results on KernelBench Levels 3-4, even if low, would provide a more complete picture of the model's capabilities and limitations.

## Removed Points

- **Criticism questioning the existence of cited benchmarks/models.** Removed per hard rules — if the paper cites KernelBook and KernelBench, they exist.
- **"The paper never defines G_speedup."** The table caption defines it as "geometric average of speedups" — sufficient for a standard metric.
- **"Missing appendix / stripped appendix content."** Removed per instructions — the parser strips these from all papers.
- **"The scarcity problem is circumvented rather than solved."** This is a generic criticism that misunderstands the paper's contribution — the contribution is a *selection* method applied to generated data, which is standard in data curation pipelines.
- **Formatting/style nitpicks.** Removed per instructions.
- **Criticism about excluding Levels 3-4 being "convenient."** The paper provides a clear, reasonable justification; excluding levels that all models fail on is standard practice.

## Novel Insights

Beyond the paper's own contributions, the reviews surface a genuinely novel meta-observation: the paper's core claim about conciseness is surprising because it runs counter to the dominant trend in reasoning research (where longer reasoning chains are prized, as in DeepSeek-R1, s1, and the "test-time scaling" literature). The paper argues that for CUDA kernel generation specifically — a well-constrained task with verifiable outputs — conciseness signals clarity rather than superficiality, and extended reasoning reflects unproductive "overthinking" (self-doubt loops, redundant verification). This suggests an important task-dependent boundary on the generality of the "more reasoning is better" hypothesis: for tasks where correctness is objectively verifiable and the solution space is relatively narrow (kernel generation, certain kinds of code optimization), conciseness may be a more reliable quality signal than for open-ended reasoning tasks like mathematical problem-solving. This is a potentially valuable insight for the broader reasoning-data curation community.

## Suggestions

1. Cleanest fix: conduct a controlled ablation that fixes the task set and varies only the within-task CoT selection criterion (shortest vs. longest vs. random), holding kernel performance constant. This directly tests whether conciseness causes improvement.
2. Add a held-out evaluation: evaluate on a set of tasks clearly disjoint from the training distribution — either manually constructed tasks, a subset of KernelBench Levels 3-4, or a different benchmark. This addresses the generalization concern.
3. Explicitly discuss the relationship between KernelBook and KernelBench in a limitations section, analyzing potential overlap and its implications for result interpretation.
4. Add single-criterion and pairwise ablations for the three selection components (conciseness+speedup, speedup>5, single-operator balancing) to isolate their individual contributions.

## Score and Decision

**Calibration anchors (from the batch retrieval):**

| Path | Avg Score | Comparison |
|------|-----------|------------|
| Kevin (xu1XwVZtDi) | 5.0 | Similar domain and concerns (trains on KernelBench tasks). KernelCoder has a more novel core observation but less technically deep contribution. Comparable quality. |
| SparseRL (VdLEaGPYWT) | 6.0 | Stronger paper overall — more thorough ablation, cleaner evaluation, honest limitations. This paper is slightly weaker. |
| CudaForge (f4GtuI2blh) | 3.5 | This paper is clearly stronger — CudaForge is a training-free agent framework with less novelty. |
| AutoTriton (8m6yY1ULKh) | 3.5 | This paper is stronger — better results and a more interesting core insight. |
| Select2Reason (MDE6S92PJR) | 3.6 | Similar theme (data selection for reasoning). This paper has stronger empirical results. |
| AceReason (IaEqjWXd1d) | 6.5 | Stronger — more thorough SFT+RL analysis across multiple scales. |
| Contamination study (GFDSGlEks2) | 4.67 | Different topic, but similar score range. This paper has a more novel core contribution. |
| OpenThoughts (7xjoTuaNmN) | 6.5 | Stronger — extensive data recipe investigation with 1000+ controlled experiments. |

**Score:** 5.0 — This paper presents a genuinely interesting observation and a practical, efficient data curation pipeline that achieves strong results. However, the central causal claim is not fully supported by the experimental design (the ablation conflates multiple variables), and the evaluation setup has an unaddressed training/evaluation overlap concern. The paper is above average for ICLR submissions in this area — comparable to Kevin (which was accepted as poster) — but would benefit from cleaner experimental design.

MY FINAL SCORE: <pineapple>5.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>