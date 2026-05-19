- Decision: Accept
- Avg Score: 6.50
- Scores: 8, 3, 6, 6, 8, 8
Now I have all the information needed. Let me produce the final consolidated review.

## Summary

This paper introduces SharedContextBench, a benchmark for evaluating long-context LLM methods under multi-turn and multi-request scenarios where the KV cache is reused across queries. It comprises 12 tasks spanning four long-context abilities (string retrieval, semantic retrieval, global information processing, multi-tasking) across two shared-context modes. The paper evaluates five categories of long-context methods (gated linear RNNs, hybrid SSM-attention, sparse attention, KV cache compression, prompt compression) on eight LLMs, and introduces a novel sparse attention variant (Tri-shape). The key finding is that methods maintaining O(n) KV cache (sparse encoding with dense decoding) perform reliably across turns, while sub-O(n) memory methods (KV compression, pure SSMs) degrade significantly, particularly on incompressible retrieval tasks.

## Strengths

1. **First benchmark specifically designed for KV cache reuse scenarios.** The paper identifies a genuine gap: existing long-context benchmarks (NIAH, RULER, InfiniteBench) evaluate only single queries, while real applications involve repeated queries sharing the same context. SharedContextBench's 12 tasks with two shared-context modes (multi-turn and multi-request) directly target this gap (Section 1, Fig. 1, Table 2).

2. **Broad and methodical evaluation across models and methods.** The paper tests five categories of long-context solutions (sparse attention, KV compression, prompt compression, SSMs, hybrid models) on eight distinct LLMs spanning transformers from 8B to 72B plus Mamba and Jamba (Table 1, Section 3). Results show consistent trends across architectures, not artifacts of a single model.

3. **Attention analysis provides mechanistic insight into why sub-O(n) methods fail.** Fig. 5a/5b visualizes the attention distribution across turns for Retr.KV, showing that critical KV pairs are highly query-dependent and shift unpredictably across turns. This directly explains why query-aware compression (SnapKV) and fixed-state models (Mamba) succeed on the first query but fail on follow-ups — a finding grounded in model internals, not just aggregate metrics (Section 4).

4. **Useful distinction between compressible and incompressible tasks.** Section 4 explicitly discusses that tasks like summarization and many-shot ICL can tolerate sub-O(n) methods because their inputs contain repetitive/redundant information, while Retr.KV and Retr.Prefix-Suffix require full O(n) memory. This nuance prevents overgeneralization of the benchmark results and provides a principled framework for practitioners to decide which method to use.

5. **Query-awareness analysis with practical implications.** Table 5 tests three methods (SnapKV, Tri-shape, MInference) with and without the query during encoding. The finding that dynamic sparse attention (MInference) generalizes better without the query is directly relevant to prefix caching in real systems where the query is unavailable during shared-context encoding (Section 4).

## Weaknesses

### Fatal
None.

### Major

1. **Overgeneralized central claim relative to the methods actually tested.** The Section 4 heading "Sub-O(n) Memory is Almost Infeasible in Multi-Turn Decoding" makes a categorical claim, but the paper evaluates only a subset of sub-O(n) approaches: StreamingLLM, SnapKV, LLMLingua-2, and Codestral-Mamba. Entire families of compression methods are absent — learned eviction (H2O, Keyformer), quantization-based compression (KIVI, FP8), and hybrid CPU-GPU offloading strategies. Section 4 discusses CPU-GPU offloading as "another promising approach" but does not test it. The claim is well-supported for the methods tested, but the wording implies a universality the evidence does not establish. The paper's own "Compressible and Incompressible Tasks" discussion (Section 4) correctly notes that sub-O(n) methods "remain useful for simpler tasks," which is at odds with the "almost infeasible" framing. The title question "How Lossy are Long-context Methods?" is answered primarily through incompressible tasks, making the headline result more dramatic than the evidence warrants. (Note: the abstract uses the more measured language "often struggle," which is appropriate.)

2. **No statistical variance or sensitivity reporting.** All results are reported as point estimates under greedy decoding with no standard deviations, confidence intervals, or multiple-seed averages (Section 3). For a benchmark intended to serve as a reference for comparing methods, the absence of any measure of variability is a significant omission. Some tasks involve random generation (KV pair positions, needle placement, string content), and it is impossible to judge whether observed differences between methods (e.g., Tri-shape vs. A-shape, or small differences between models) are reliable or within noise. Hyperparameters for tested methods (compression ratios, sparse pattern sizes) are fixed with no sensitivity analysis reported.

### Minor

3. **Tri-shape method is under-specified in the main text.** Tri-shape is listed as a contribution ("novel training-free sparse attention method") but receives only a brief description: "incorporates bottom query tokens into A-shape" (Section 3, Fig. 3). No formal definition, exact token counts, selection criterion for "bottom query tokens," or pseudo-code is given. While details may reside in appendix §C.2, a novel method claiming contribution status requires a self-contained description in the main body.

4. **No efficiency metrics accompany the accuracy results.** The paper is about long-context *methods* whose raison d'être is trading accuracy for efficiency (speed, memory, or FLOPs). Yet only accuracy is reported. A reader cannot judge whether a given accuracy drop is acceptable for the efficiency gain. Reporting prefilling FLOPs, decoding memory footprint, or wall-clock time would substantially strengthen the benchmark's utility as a reference for practitioners.

5. **Multi-tasking tasks involve artificial insertion of distractors.** Mix.RepoQA+KV and Mix.Sum+NIAH construct multi-tasking scenarios by inserting KV pairs into code or needles into papers (Section 2.1). This is a reasonable first step, but the paper does not discuss whether these artificial patterns reflect realistic multi-tasking or introduce artifacts (e.g., out-of-distribution patterns that confuse models in ways unrelated to multi-tasking).

### Trivial
None.

## Nice-to-Haves

- **Efficiency metrics** (prefilling/decode memory, wall-clock time, or FLOPs) would let readers judge the accuracy-efficiency trade-off directly, making the benchmark more useful to practitioners.
- **Per-task degradation table** directly isolating first-turn vs. later-turn accuracy for each method (beyond the aggregate trends in Fig. 2a and the per-task averages in Fig. 4) would sharpen the paper's central argument about multi-turn failure.
- **Longer-session analysis** — the benchmark averages ~5 turns per session. Testing with longer sessions (e.g., 10–20 turns) would show whether degradation plateaus or continues, and whether some methods are more robust to session length.
- **Self-generated context limitation** — the paper uses ground-truth answers for follow-up context (following prior work), which is reasonable but avoids the realistic case where model-generated errors compound. A brief discussion of this would strengthen the limitations paragraph.

## Removed Points

These points were flagged in the inputs but are removed with justification:

- **"Benchmark task design may systematically favor full-KV-cache methods"** — The paper explicitly addresses this in Section 4 ("Compressible and Incompressible Tasks"), noting that sub-O(n) methods remain useful for compressible tasks and that "compressible tasks may overestimate a model's capabilities." The paper acknowledges the design choice and discusses its implications. The criticism is already addressed by the paper's own content.

- **"No analysis of how the number of turns affects degradation"** — Figure 4 shows "Performance of different long-context methods across various tasks and turns," and Figure 2a shows trends across requests. The paper does include per-turn analysis. This criticism is factually incorrect.

- **"MInference tested with default settings; unclear if others tuned"** — The paper states "exact implementation and configuration details can be found in §C.2." Without seeing the appendix, this concern cannot be verified. Applying equal default settings across methods is standard practice for benchmarks of this kind.

- **"Self-generated vs. ground-truth context"** — The paper explicitly states it uses ground-truth answers (following Zheng et al., 2023a; Wang et al., 2024) and justifies this choice to avoid compounding errors. This is a deliberate design decision, not an oversight.

- **All "Strengthening the Paper on Its Own Terms" points** — These are good suggestions but framed as weaknesses, which they are not. Several are already addressed (distinction between compressible/incompressible tasks), and others are scope expansions.

## Novel Insights

The reviews surface a useful tension: the paper's strongest evidence (attention visualization showing query-dependent KV shifts across turns) and its broadest claim ("sub-O(n) memory is almost infeasible") sit at different levels of generality. The attention analysis is mechanistic and convincing for the specific case of incompressible retrieval tasks, but neither the reviews nor the paper itself provide analogous mechanistic evidence for semantic retrieval or global information tasks, where sub-O(n) methods show mixed results. This suggests the paper's real contribution is more precise than its framing: it demonstrates a *mechanistic reason* why sub-O(n) compression fails on exact-match retrieval in shared contexts, rather than establishing a universal impossibility. Future work could test whether this mechanism generalizes to other task types and compression families.

## Suggestions

1. **Retitle the Section 4 heading** from "Sub-O(n) Memory is Almost Infeasible in Multi-Turn Decoding" to something more measured such as "Sub-O(n) Memory Methods Degrade Sharply on Incompressible Tasks in Multi-Turn Decoding," which aligns with the evidence presented.
2. **Add variance estimates** for the main results (e.g., bootstrap confidence intervals or standard deviations across multiple generated task instances). If greedy decoding makes the output deterministic conditional on input, report variance across different random seeds for task generation.
3. **Add a summary table** showing per-task, per-method accuracy on turn 1 vs. later turns, to directly quantify the degradation the paper argues is central.
4. **Specify Tri-shape more precisely** — provide the exact formula, selection criterion for "bottom query tokens," and the number of tokens used — either in the main text or with a clear pointer to a fully detailed appendix section.
5. **Include at least one efficiency metric** (e.g., peak GPU memory usage during decoding, or wall-clock time per token) in a supplementary table, so practitioners can evaluate the accuracy-efficiency trade-off.
6. **Discuss the limitation** that multi-tasking tasks use artificially inserted distractors, and acknowledge potential artifacts from this construction.
