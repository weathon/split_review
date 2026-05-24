## Summary

QUOKA proposes a training-free, hardware-agnostic sparse attention method optimized for chunked prefill. The core insight is that queries with low cosine similarity to the mean query interact with more keys and contribute more to attention logits, enabling a two-stage KV subselection: first retain representative queries via cosine dissimilarity, then subselect KV pairs via cosine similarity. Experiments across RULER, LongBench, NIAH, and Math500, on 5 model families (Llama 3.2, Qwen 2.5/3, SmollM3, GPT-OSS) and 3 hardware platforms (A100, RTX 2080, Xeon CPU), show near-dense accuracy while using 88% fewer KV pairs, with up to 5× attention speedup and 3× TTFT reduction.

## Strengths

- **Novel query-selection insight grounded in geometry.** The observation that queries far from the mean query (in cosine similarity) have broader attention patterns is underexplored in prior sparse attention work. The correlation of 0.737 between the selection score \(S_q\) and \(\max_k(A)\) (Figure 2c) provides empirical grounding, and the geometric reasoning is cleanly motivated.

- **Strong and consistent accuracy gains over baselines.** On RULER (Table 1, \(B_{\text{SA}}=1024\)), QUOKA outperforms all baselines by 10–20% across 4K–32K lengths (e.g., Llama 3.2-3B at 4K: 86.71 vs. next best 78.25). On LongBench (Table 3), QUOKA maintains normalized accuracy ≥0.94 even at a budget of 512, while the strongest baseline (SampleAttention) reaches only 0.74–0.86. Using only 25% of the KV cache, accuracy stays within 1–3% of the dense baseline (Table 2).

- **Meaningful latency reduction across diverse hardware, not just GPUs.** QUOKA achieves up to 5× attention speedup and 3× TTFT reduction on an A100 (Figure 5a,b), up to 7× on a Xeon CPU (Figure 5c), and 5–6× on an RTX 2080 (Figure 5d). The speedups hold across all three platforms, which is unusual and important—most sparse attention work reports only GPU results.

- **Hardware-agnostic by design.** Unlike kernel-level sparsity methods that depend on custom CUDA kernels, QUOKA uses only standard linear algebra operations (cosine similarity, mean, gather; Algorithm 1). This makes it portable to CPUs, consumer GPUs, and edge accelerators without re-implementation.

- **Robustness to hyperparameters.** Ablations (Section 4.5, Tables 11–12) show accuracy degrades gracefully as sparsity increases and remains stable across choices of chunk size \(B_{\text{CP}}\) and number of selected queries \(N_q\), enabling practical deployment tuning.

## Weaknesses

### Minor

1. **Unexplained >1.0 normalized accuracy.** In Table 3, Smollm3 at \(B_{\text{SA}}=1024\) and 2048 shows normalized accuracy of 1.03 and 1.028, meaning QUOKA reportedly exceeds the dense baseline on LongBench. The abstract and conclusion also mention surpassing dense attention on Math500. These are unusual results for a sparse approximation method. The paper does not explain whether this reflects a genuine phenomenon (e.g., sparsity filtering irrelevant tokens) or is within measurement noise. No error bars or confidence intervals are provided for any accuracy results. This does not undermine the core claim (which is about *near*-dense accuracy with speedups), but it is an evidential gap that should be addressed—either by discussing the mechanism or by acknowledging the values are within noise and adding statistical analysis.

2. **SnapKV and KeyDif appear in Table 1 without description.** The "Sparse Attention Baselines" paragraph (Section 4) lists only SampleAttention, LessIsMore, SparQ, and Loki. Yet Table 1 includes SnapKV and KeyDif as rows with no description of how they were implemented or adapted for the chunked-prefill setting. This makes the comparison opaque for two of the entries in the main accuracy table.

3. **Core observation validated on only one layer/head.** Figure 2 shows the correlation between \(S_q\) and \(\max_k(A)\) for Llama 3.2-3B, layer 0, head 11. While the method's overall effectiveness is demonstrated across many models, showing that this specific geometric pattern holds across layers and heads would significantly strengthen the motivation. As written, it is unclear whether the pattern is general or an artifact of this particular layer/head.

### Trivial

- The condition \(B_{\text{CP}} > N_Q\) and the default \(N_Q\) value in Algorithm 1 are not stated until later sections; stating them upfront would improve clarity.
- No error bars on accuracy results, though latency results are averaged over 100 trials (Section 4.6).

## Nice-to-Haves

- A breakdown of time spent in QUOKA's selection stages (subselection, scoring, gathering) vs. the attention kernel itself would help assess the overhead of the selection process.
- Sensitivity to chunk size \(B_{\text{CP}}\) beyond the default 128 is mentioned in the appendix; a summary in the main text would strengthen robustness claims.
- Results on larger models (e.g., 70B scale) would increase generality.

## Removed Points

These points from the inputs are excluded under the filtering rules:

- **Theorem 1 proof "relegated to the appendix"** — the parser strips appendix sections; the proof exists in the original submission. Rule: *Remove weaknesses about missing appendix content.*
- **"Baselines may have been suboptimally adapted / given the same query-subselection step"** — the paper describes each baseline's mechanism as originally designed; giving them QUOKA's query subselection would change their fundamental design. The comparison methodology follows standard practice. Rule: *Remove criticisms about unfair comparison if changing the baseline would alter its core mechanism.*
- **"Weak theoretical support" / Theorem 1 "does not directly imply" the selection criterion** — the paper provides intuition connecting the theorem to the selection rule, and the empirical results validate the approach. The criticism is a matter of interpretation, not a factual error. Rule: *Remove strawman weaknesses that claim something is missing when the paper does address it.*
- **"Reproducibility: undisclosed hyperparameters"** — the paper states "All hyperparameters and test configurations are documented in the main text and appendix." Rule: *Remove nitpicks about reproducibility for items that are either documented or standard.*
- **Generic concern sweeps** (e.g., "could the metric be measuring a proxy") — these surfaced through the broad-area prompting but lack a specific anchor in the paper. Rule: *Remove speculation that lacks a concrete citation or equation.*

## Novel Insights

The key insight is that query *geometry* (distance from the mean query in cosine-similarity space) correlates with breadth of attention—queries far from the mean interact with more keys and are thus more informative for KV selection during prefill. This is a genuinely underexplored perspective in the sparse attention literature, which typically treats queries homogeneously or samples them uniformly. The connection between angular position in query embedding space and attention coverage provides a principled basis for query subselection that goes beyond heuristic approaches.

## Suggestions

1. Add confidence intervals or standard deviations for the accuracy results (Tables 1–3, especially the >1.0 normalized values) to clarify whether these are stable improvements or within noise.
2. Describe SnapKV and KeyDif in the baseline section, or remove them from Table 1 if they were included for reference without a controlled adaptation.
3. Extend the analysis in Figure 2 to at least 3–5 layers and heads across 2–3 models to demonstrate the generality of the geometric observation.
4. Include a 2–3 sentence summary of chunk-size sensitivity in the main text rather than deferring entirely to the appendix.

## Score and Decision

**Calibration summary:**

| Anchor | Avg Score | Round | Comparison to QUOKA |
|--------|-----------|-------|---------------------|
| HASA (Hjk1tWIdvL) | 5.00 | R1 bracketing | Weaker — limited novelty, less comprehensive evaluation |
| ChunkAttention (9k27IITeAZ) | 4.50 | R1 bracketing | Weaker — different focus (prefix sharing), less general |
| Cascading KV Cache (dSneEp59yX) | 6.00 | R1 bracketing + R2 narrowing | Comparable — similar quality, slightly less evaluation breadth |
| Chunk-Distilled LM (nrvoWOWcyg) | 6.50 | R1 bracketing | Different focus (text generation), moderate comparison |
| FlexPrefill (OfjIlbelrT) | 8.00 | R1 bracketing | Stronger — more sophisticated dynamic patterns, cleaner evaluation |
| ChunkKV (8sglLco8Ti) | 5.25 | R2 narrowing | Weaker — limited novelty, evaluation gaps |
| LazyLLM (am5Z8dXoaV) | 5.00 | R2 narrowing | Weaker — evaluation less comprehensive |
| OmniKV (ulCAPXYXfa) | 6.00 | R2 narrowing | Comparable — similar contribution level, more models tested in QUOKA |
| CoreInfer (s3003xWtfd) | 6.25 | R2 narrowing | Different focus (sparse activations), moderate comparison |
| SharedContextBench (gkUyYcY1W9) | 6.50 | R2 narrowing | Different type (benchmark paper) |

**Round-1 bracket:** 4.0–8.0 based on topical similarity  
**Round-2 narrowing:** The paper clusters near 6.0 anchors (OmniKV, Cascading KV Cache) and is clearly stronger than 5.0-5.25 anchors (HASA, ChunkKV, LazyLLM)  
**Final score:** 6.0 — a solid paper with a genuinely novel insight, comprehensive experimental evaluation, and practical value, held back from higher scores by the unexplained >1.0 normalized accuracy, missing baseline descriptions for Table 1 entries, and limited cross-layer/head validation of the core geometric observation.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>