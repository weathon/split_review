Now I have a thorough understanding of the paper and the reviews. Let me write the final consolidated review.

## Summary

This paper introduces SharedContextBench, a benchmark to evaluate long-context methods under realistic KV cache reuse scenarios (multi-turn and multi-request). It spans 12 tasks across four long-context abilities (string retrieval, semantic retrieval, global information processing, multi-tasking). The authors evaluate five categories of long-context methods across eight open-source LLMs (including SSMs, hybrids, sparse attention, KV compression, prompt compression). The central finding is that sub-O(n) memory methods degrade severely across queries while O(n)-memory sparse encoding methods maintain accuracy.

## Strengths

1. **Novel benchmark design targeting a genuine gap.** Existing long-context benchmarks (RULER, InfiniteBench) evaluate only single-query performance, ignoring the common real-world pattern of multiple queries sharing the same context. SharedContextBench explicitly fills this gap with 12 tasks spanning four abilities and two shared-context modes (multi-turn and multi-request), as clearly stated in Section 1 and detailed in Section 2.

2. **Comprehensive evaluation across a wide range of methods and models.** The paper tests five method categories (gated linear RNNs, hybrid SSM-attention, sparse attention, KV cache compression, prompt compression) on eight LLMs including Llama-3.1-8B/70B, Qwen2.5-72B/32B, Llama-3-8B-256K, GLM-4-9B, Codestal Mamba, and Jamba-1.5-Mini. The main results (Table 4, Figure 2, Figure 4) consistently show sub-O(n) methods degrading across requests while O(n) memory methods remain stable — the central claim is quantitatively supported across nearly all tasks and models.

3. **Mechanistic explanation through attention visualization.** Figure 5 provides concrete evidence for *why* sub-O(n) methods fail: critical KV pairs are highly query-dependent and shift unpredictably between turns. This goes beyond merely reporting accuracy numbers and gives practitioners a clear understanding of the underlying failure mode.

4. **Two distinct shared-context modes systematically isolate query-awareness effects.** The multi-request mode (Section 2.2) deliberately tests methods that rely on the query for sparse encoding/decoding (SnapKV, Tri-shape, MInference). Table 5 shows degraded performance without the query, providing actionable guidance for deploying prefix caching in practice.

5. **Differentiation between compressible and incompressible tasks.** Section 4 notes that sub-O(n) methods succeed on highly compressible inputs (NIAH, summarization) but fail on incompressible tasks like Retr.KV and Retr.Prefix-Suffix. This nuance prevents over-generalization and is supported by task-specific breakdowns in Figure 4.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor
1. **Tri-shape is underspecified in the main paper.** The method is described only as "incorporating bottom query tokens into A-shape" (Section 3, line 103), without defining what "bottom" means (a fixed number of tokens? a ratio? the last *k* tokens?). The sparsity ratio and exact construction are deferred to the appendix (§C.2). While the appendix likely contains these details (it was stripped by the parser), the main paper should briefly state the key hyperparameters (e.g., number of bottom tokens retained, sparsity ratio) so readers can understand the method without cross-referencing. This is a presentation issue, not a fatal flaw — Tri-shape is a minor variant added primarily as an additional baseline.

2. **The many-shot ICL task does not specify the number of shots used.** Section 2.1 lists three sub-tasks from Big-Bench Hard but omits how many examples are included per context. At 64K context, this number directly affects task difficulty and comparability with future work.

3. **Ground-truth quality for GPT-4-generated summaries and multi-task compositions is not validated.** The En.Sum task (Section 2.1) uses GPT-4-generated summaries as ground truth, and the multi-task tasks (Mix.Sum+NIAH, Mix.RepoQA+KV) combine existing tasks without sanity checks (e.g., whether the inserted needle interferes with the summarization task). A brief manual verification of a sample or automated consistency check would increase confidence in the benchmark's reliability.

4. **Llama-3-8B-256K's fine-tuning vs. architecture effects are not discussed.** As noted in Section 3, this model is a fine-tuned variant with expanded context. Its performance differences from base LLaMA-3-8B could stem from fine-tuning rather than architecture, but the paper does not address this.

5. **No explicit limitations discussion.** The paper does not acknowledge that its benchmark uses synthetic tasks (e.g., Retr.KV with random KV pairs) that may not fully reflect real-world shared-context structure. A brief limitations paragraph would improve scholarly completeness.

### Trivial
- The complexity analysis comment for Retr.Prefix-Suffix ("similar to a prefix tree, with a computational cost of O(∑ w_i²)") describes classical algorithmic difficulty rather than LLM-relevant difficulty, making the sentence somewhat confusing for readers.

## Nice-to-Haves
- **Quantitative compressibility measure:** Section 4's discussion of compressible vs. incompressible tasks is qualitative. Reporting an entropy-based compressibility measure per task and correlating it with method performance would strengthen the analysis.
- **Wall-clock or FLOPs reporting for sparse encoding methods:** The paper correctly notes that sparse encoding methods still cost O(n) memory in decoding. Reporting prefill speedup or wall-clock time would help practitioners evaluate the practical trade-off.
- **Per-model breakdown in the main paper:** The per-model results are in the appendix (Table 10). Showing a condensed per-model breakdown of the key trend (e.g., the gap between sparse encoding and sparse decoding methods) in the main paper would improve transparency, though the current practice of showing averages + per-model in appendix is standard.

## Removed Points
*These points are flagged to be removed — treat them with caution.*

1. **"Sub-O(n) claim supported by single task / single model"** (Harsh Critic #2) — REMOVED because it factually misreads the paper. The claim is supported by the comprehensive quantitative results across all 12 tasks, 8 models, and 5 method categories (Tables 4, Figure 2, Figure 4). Figure 5 is an *illustrative* attention visualization for one task, not the primary evidence. The quantitative evidence across the full benchmark already robustly supports the claim.

2. **"Missing related work on ICL"** — REMOVED per instructions: I cannot confirm the existence of such work from external sources.

3. **"Code/data release unclear"** — REMOVED because this information was likely in the appendix (which the parser stripped).

4. **"Table 4 averages hide per-model variation"** — REMOVED because per-model results are reported in the appendix (Table 10 in §D), which is standard practice.

5. **"Statistical grounding / confidence intervals"** — REMOVED because the paper uses greedy decoding where variance is inherently low, and requesting confidence intervals for a large-scale benchmark is not standard practice in this setting.

6. **"Prefix-Suffix complexity confusing"** — REMOVED as a weakness; it is a minor presentational imprecision at most (moved to Trivial).

7. **"Section 4 compressibility is qualitative"** — DOWNGRADED to Nice-to-Haves; the qualitative observation is insightful on its own, and the quantitative extension is a suggestion for future work, not a flaw.

## Novel Insights

The Harsh Critic correctly identifies that the Tri-shape method's underspecification is the paper's most actionable weakness, but overlooks that the paper's core quantitative evidence is actually much broader than what the attention visualization alone provides. The Strength Finder correctly highlights the comprehensive evaluation scope and the two-mode design as key strengths. The most interesting insight from the reviews is the interplay between the paper's two main contributions: the benchmark itself (which is thorough and well-designed) and the empirical findings (which are robustly supported). The Tri-shape method, despite being listed as a contribution, is the weakest part of the paper and could be de-emphasized without harming the paper's value — the benchmark and the central finding about sub-O(n) methods failing in shared contexts are where the real contribution lies.

## Suggestions

1. Add a brief algorithmic specification of Tri-shape in the main paper: state what "bottom query tokens" means (fixed count? ratio?), the sparsity ratio used, and how it differs from A-shape beyond adding a local window.
2. Specify the number of shots used in the many-shot ICL task.
3. Add a brief validation note — e.g., "We manually verified 20 examples per multi-task composition and found no interference between tasks" or similar.
4. Add a one-paragraph limitations section acknowledging the synthetic nature of some tasks and discussing generalizability to real-world contexts.
5. Include a brief note on how fine-tuning may affect Llama-3-8B-256K's performance relative to its base architecture.

## Score and Decision

This is a solid benchmark paper that fills a genuine gap. The benchmark design is thoughtful, the evaluation is comprehensive (five method categories, eight LLMs), and the central finding — that sub-O(n) memory methods degrade in shared-context scenarios while O(n) sparse encoding methods remain stable — is well-supported by the quantitative results. The weaknesses are minor presentation and methodological gaps, none of which undermine the core contribution. The paper is publishable in its current form and would benefit from minor revisions.

MY FINAL SCORE: <pineapple>7.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>