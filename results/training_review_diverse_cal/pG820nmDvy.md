Now I have all the evidence I need. Let me synthesize the final review.

## Summary

This paper proposes top-*k* attention for long-context LLM inference: instead of attending to all tokens in the KV cache, it retrieves only the *k* most relevant keys using a CPU-based Faiss vector database, achieving sublinear per-token cost. The paper provides systematic evidence that attention is extremely sparse in LLaMA-family models (Figures 2–4), and shows on RULER, AlpacaEval 2.0, and OpenLLM Leaderboard benchmarks that attending to ≤2.5% of tokens recovers ≥95% of full-attention performance. The authors also demonstrate 1M-token Needle-In-A-Haystack inference on a single 16GB GPU, comparing qualitatively against StreamingLLM.

---

## Strengths

- **Multi-benchmark evidence that extreme sparsity preserves accuracy.** On RULER (Table 1), *k* = 1% of context length achieves ≥95% of baseline across all lengths up to 131k. On OpenLLM Leaderboard, performance saturates by *k* = 10 keys (Figure 1). On AlpacaEval 2.0, 2.5% of context suffices for 95% of baseline. This coverage across retrieval, generation-quality, and knowledge benchmarks strengthens the core claim beyond any single task.

- **Systematic empirical analysis of attention sparsity directly motivates the method.** Figures 2–4 show that 75% of attention mass often concentrates in <1250 of 4000 tokens, entropy is low across layers, and models correctly focus on the relevant document in multi-document settings. This grounds the top-*k* approach in observed model behavior rather than assuming sparsity.

- **Concrete demonstration of 1M-token inference on a single 16GB GPU.** Section 4.3 reports running the Needle-In-A-Haystack task at 1M tokens on one GPU node using a Faiss-backed KV cache, with successful retrieval at *k* = 10 where StreamingLLM (Figure 8) fails. This is a genuine feasibility result that prior system solutions (e.g., Ring Attention requiring multiple devices) could not match on such hardware.

- **Broad model coverage.** The method is evaluated on LLaMA-1/2/3 (base and instruct), Vicuna, and LLaMA-3.2 1B/3B, all showing the same saturation behavior (Section 4.2, Table 6). This establishes that the phenomenon is not model-specific.

---

## Weaknesses

### Fatal

None.

### Major

- **No quantitative efficiency measurements despite efficiency being the paper's central framing.** The paper's title, abstract, and introduction all emphasize running huge contexts on cheap hardware with sublinear cost, yet the evaluation contains zero runtime, latency, throughput, or peak-memory measurements. Section 4.3 demonstrates that 1M-token inference *is possible* on a 16GB GPU (a memory-feasibility result), but the reader cannot tell whether the Faiss-based retrieval with CPU–GPU communication is actually faster or more memory-efficient than alternatives such as sliding window, SnapKV, or Keyformer, or whether ANN-search overhead dominates at scale. The claim of "sublinear time" in the introduction and conclusion is never backed by wall-clock data or a complexity analysis of the full system. This gap undermines the paper's primary value proposition because the reader cannot assess the practical efficiency–accuracy trade-off that the method promises.

- **The "prescriptive recommendations for choosing the optimal *k*" (listed as a contribution) are not delivered with sufficient substance.** The paper gives a single rule of thumb—"1% of context length"—and notes that AlpacaEval requires 2.5% and QA tasks are more sensitive. This falls short of a systematic prescription that accounts for task type, layer depth, attention head specialization, or model size. The related analysis of how optimal *k* varies across these dimensions is absent, making the contribution claim overstated.

### Minor

- **Potentially overclaimed RULER result for *k* = 2.** The text states: "at *k* = 2, greater than 60% performance is achieved at all context lengths." The reviewer reports that Table 1 shows the score at 131k with *k* = 2 is 26.2 (baseline 67.2), which would be 39% of baseline rather than >60%. If accurate, this is a quantitative error in a key claim. The table is an image (parser-stripped) and cannot be independently verified from the text, but the concern is substantive enough to flag. The authors must correct or clarify this statement.

- **Limited analysis of performance breakdown by task category.** Section 4.2 notes qualitatively that QA tasks are most sensitive and have high variance, but no per-category RULER scores are reported. Providing a breakdown would help readers understand where top-*k* fails (or succeeds) and guide practical *k* selection.

- **Quantitative comparison against baselines is absent.** The only direct baseline comparison is the qualitative needle-in-a-haystack heatmap against StreamingLLM (Figure 8). Existing KV-cache pruning methods (SnapKV, Keyformer — both cited in related work) and sliding-window attention are not compared on the same benchmarks, model, and hardware. A quantitative comparison on a shared task (e.g., RULER or a long-document QA dataset) would situate the method in the literature.

### Trivial

- The paper states it evaluates models "at the million token scale on a single GPU" but does not specify which GPU model or CPU configuration was used, making the result difficult to reproduce or contextualize.

---

## Nice-to-Haves

- A single end-to-end latency/memory experiment at a representative context length (e.g., 500k tokens) showing how total time and peak GPU memory vary with *k* — even without a full benchmark suite — would validate the paper's central claim far more than the current qualitative discussion.
- An analysis of Faiss search time vs. GPU attention time as a function of context length would clarify where the bottleneck lies and whether the method actually yields end-to-end speedup.
- Per-layer optimal *k* values could be explored; the paper's own data (Figure 2 showing layer-1 requiring more tokens for 75% mass) suggests this could yield further gains.

---

## Removed Points

These points are flagged to be removed; treat them with caution.

- **"Algorithm 2 is referenced but provided only as a figure whose content cannot be verified from the text (the parser stripped it)."** → Removed. Parser stripping of figures is a formatting artifact, not an author error. The original submission contains Algorithm 2.
- **"Does not cite H2O (Zhang et al., 2023) or Scissorhands (Liu et al., 2023)."** → Removed per policy: missing related works cannot be verified externally and may not exist in the form described.
- **"The claim of 'sublinear time' is not substantiated with any complexity analysis."** → Weakened/Removed. The paper correctly references the known sublinear property of approximate nearest neighbor search, which is a standard result. The lack of end-to-end empirical measurement is covered in the Major weakness above.
- **"Prescriptive recommendations are not delivered."** → Partially removed. The paper does deliver the 1% heuristic and mentions the 2.5% rule for AlpacaEval and the higher sensitivity of QA tasks. While not exhaustive, this is a reasonable first set of recommendations; the limitation is captured in the Minor weakness above.

---

## Novel Insights

None beyond the paper's own contributions. The two independent reviews largely converge: they agree that the sparsity analysis and accuracy results are solid, that the 1M-token feasibility demonstration is compelling, and that the major gap is the complete absence of efficiency measurements (latency, memory, throughput) that the paper's framing promises. The harsh critic's concern about the RULER *k* = 2 claim adds a specific verifiability concern, but the core judgment about the paper's strengths and weaknesses is consistent.

---

## Suggestions

1. **Add efficiency measurements as the highest priority.** Report end-to-end generation latency and peak GPU memory for at least one long-context workload (e.g., 500k tokens) across several *k* values, comparing against full attention and at least one approximate-attention baseline (sliding window, SnapKV, or StreamingLLM). Without this, the paper's central promise remains unvalidated.

2. **Correct or clarify the RULER *k* = 2 claim.** Report the actual scores from Table 1 alongside the baseline so the reader can see both absolute performance and fraction of baseline. Adjust generalizing statements accordingly.

3. **Provide a per-task-category breakdown of RULER scores** (NIAH, multi-hop, QA, summarization) so the reader can see where top-*k* degrades and where it holds. This directly addresses the variance noted in Section 4.2.

4. **Add at least one quantitative comparison to a prior efficient-attention baseline** on the same model and benchmark (e.g., LLaMA-3-8B on RULER vs. SnapKV or sliding window).

---

## Score and Decision

This paper has genuine contributions: the sparsity analysis is well-executed, the accuracy evaluation across three benchmarks is thorough, and the 1M-token feasibility result on a 16GB GPU is a notable demonstration. However, the paper's title and framing emphasize *efficiency* ("Running Huge Context Windows On Tiny GPUs"), yet **zero quantitative efficiency measurements** are provided. This is not a minor omission — it is a gap in the paper's central claim. The absent latency, memory, and throughput data, combined with a potentially overclaimed RULER result and lack of quantitative baseline comparison, make the paper incomplete for acceptance in its current form. The contribution could become strong with the addition of efficiency experiments and corrected reporting.

MG FINAL SCORE: <pineapple>5.5</pineapple>
MG FINAL DECISION: <orange>Reject</orange>