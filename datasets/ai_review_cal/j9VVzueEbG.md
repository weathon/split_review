- Decision: Accept
- Avg Score: 7.00
- Scores: 6, 8, 6, 8
Now I have a thorough understanding of the paper and the inputs. Let me construct the final consolidated review.

---

## Summary

ZETA introduces a top-\(k\) attention mechanism that uses Z-order (Morton) curves to map low-dimensional keys and queries into one-dimensional space, enabling parallel sorting and binary search-based nearest-neighbor retrieval that respects causal masks. The paper additionally provides a theoretical analysis of key/query dimensionality trade-offs and an Adaptive Cauchy-Softmax that aligns better with Euclidean distance in the low-dimensional space. Empirical results on associative recall, the Long Range Arena (LRA) benchmark, and WikiText-103 language modeling demonstrate system-level effectiveness and improved efficiency, with ZETA's Triton implementation matching or exceeding FlashAttention in runtime for long sequences.

---

## Strengths

- **Novel integration of Z-order curves for parallel top-\(k\) selection under causal masks.** The paper identifies a genuine limitation of prior top-\(k\) attention methods (Reformer, Mao et al.) — their inability to parallelize nearest-neighbor search with causal masking — and solves it by sorting 1-D Z-order encoded keys and constraining each query's search to past chunks. This design is clearly articulated in Section 3.2.2, and the efficiency benchmarks (Table 3/Table 4 text) confirm the practical benefit, with ZETA's forward pass at sequence length 8192 (72 ms) being faster than FlashAttention (107 ms) and substantially faster than naive attention (1653 ms), empirically validating the \(\mathcal{O}(N\log N)\) complexity claim.

- **Strong system-level results on Long Range Arena (LRA).** The paper reports that ZETA achieves the highest average accuracy among compared models on LRA, outperforming the next best competitor (Zhu & Soricut, 2021) and notably exceeding vanilla Transformers and efficient variants (Reformer, Linformer, Performer) across most tasks. This suggests the overall ZETA system is effective for long-sequence modeling, even if the source of the gains requires further attribution analysis.

- **Adaptive Cauchy-Softmax as a principled replacement for dot-product softmax in Euclidean retrieval.** The Cauchy kernel's heavier tails align naturally with the Euclidean nearest-neighbor search used in ZETA, and the trainable \(\gamma\) parameter allows dynamic adjustment of receptive fields per layer. Figure 2c shows Cauchy-Softmax consistently outperforming Negative Euclidean and Inverse Euclidean operators across tested \(d_K\) values on MQAR.

- **Memory efficiency competitive with optimized implementations.** Table 4 shows ZETA's memory consumption at length 8192 (2736 MB) is far below naive attention (9080 MB) and only 1.16× FlashAttention (2362 MB), demonstrating practical space advantages from the sparse top-\(k\) formulation.

---

## Weaknesses

### Fatal

None.

### Major

- **Abstract overclaims WikiText-103 results, contradicting the paper's own data.** The abstract states ZETA "outperforms attention and its variants on ... WikiText-103 language modeling." The paper's own Table 1 data (reported in Section 4.1 text) shows ZETA achieving perplexity 26.3, which is *worse* than vanilla Transformer (26.2), Reformer (25.6), and CosFormer (23.1). Higher perplexity is worse, so "outperforms" is incorrect for WikiText-103. The body text honestly describes ZETA as "comparable to the Vanilla Transformer" (line 175), but the abstract and intro contain a factual overstatement that must be corrected. This does not invalidate the paper's overall contributions, but it undermines trust in the presentation of results.

- **No direct validation that the Z-order retrieval captures the true top-\(k\) attended tokens.** The paper's core mechanism replaces exact top-\(k\) selection (based on attention scores) with approximate retrieval via Z-order projection and a 1-D window. The only evidence for retrieval fidelity is Figure 3 (Section 4.4), which measures Euclidean nearest-neighbor overlap on *random data* — not the recall of the actual top-\(k\) by attention scores on real trained embeddings. The paper does not report what fraction of the true top-\(k\) tokens (by dot-product or Cauchy-Softmax score) are captured by the Z-order window on any real task (LRA, WikiText-103, or even MQAR). Without this, the strong LRA performance could plausibly stem from the Cauchy-Softmax, the chunking strategy, the mean-value smoothing, or interactions among components rather than from the Z-order retrieval. This is the single biggest gap in the paper's evidence chain.

### Minor

- **Theoretical analysis is loosely connected to the actual method.** Theorem 3.3 provides an upper bound on expected risk that trades off curse of dimensionality vs. locality preservation as a function of \(d_K\), and cites the Johnson–Lindenstrauss Lemma to motivate low key/query dimensions. However, this analysis is about general dimensionality reduction (random projections), not about Z-order curves specifically — there is no argument that JL-style distance preservation carries over to the deterministic Z-order space-filling curve, and the bound does not explain why a 1-D window around a binary-search insertion point should recover the true top-\(k\) tokens. The theory motivates *low \(d_K\)* (which is experimentally validated in Figure 2b) but does not analyze or justify the Z-order retrieval itself.

- **Cauchy-Softmax ablation limited to Euclidean-based variants; not compared to standard dot-product softmax.** Figure 2c compares Negative Euclidean, Inverse Euclidean, and Cauchy-Softmax, showing Cauchy wins. But the standard dot-product softmax — which would be the natural baseline — is absent. Additionally, the Cauchy-Softmax ablation is only on the synthetic MQAR task; no ablation on LRA or WikiText-103 isolates whether the Cauchy kernel (vs. dot-product softmax with the same low \(d_K\)) is responsible for the performance gains. Similarly, the "cumsum" mean-vector smoothing mentioned in Section 3.4 is not ablated.

- **LRA results reported without confidence intervals or run-to-run variation.** Only point estimates are given. Given the substantial gap over baselines claimed in Table 2, variance information would help assess reliability. Baselines are also limited to circa 2020–2021 efficient Transformers; more recent state-space models (S4, Mamba, Hyena) that achieve strong LRA results are not included for comparison.

- **Some algorithmic details are underspecified.** The chunk size \(M\) and window size \(K\) (used in the top-\(k\) search) are not given concrete values for the main experiments. The procedure for handling query Z-order encoding relative to key sorting could be clarified. This does not prevent understanding the core idea but hinders exact reproducibility.

### Trivial

- Minor formatting issues in the equation for Theorem 3.3 (line 89–93) show garbled characters ("\ensuremath Ḋ \mathcal Ḋ D Ḍ Ḍ"), likely from the PDF extraction pipeline.

---

## Nice-to-Haves

- **Direct retrieval-recall metric on real data.** The single most impactful addition would be measuring the recall@k of the Z-order window against the true top-\(k\) attention scores on trained LRA or WikiText-103 models. This would directly validate whether the approximation is faithful.
- **Ablation of ZETA vs. an "oracle" variant** that uses exact top-\(k\) (full attention scores) on the same low-dimensional keys with the same Cauchy-Softmax, to disentangle gains from the Z-order approximation vs. other architectural choices.
- **Add standard dot-product softmax to the ablation in Figure 2c** and run the Cauchy-Softmax comparison on at least one LRA task.
- **Report confidence intervals** for LRA and WikiText-103 results.
- **Experiment examining whether the \(\mathcal{O}(N\log N)\) efficiency holds for very large \(N\)** beyond the tested range, with a breakdown of time spent on Z-order encoding vs. sorting vs. kernel computation.

---

## Removed Points

These points are flagged to be removed; treat them with caution.

- **"Z-order curves are not suitable for dot-product similarity" criticism removed.** The paper's claim that dot-product similarity does not reflect Euclidean locality is standard and correct — normalized vectors would still give different rankings than Euclidean distance in low dimensions. This is not a confusion; it's an accurate motivation for switching to a Euclidean-based kernel.
- **Missing proofs in the theoretical section removed.** The proof of Theorem 3.3 was likely in the appendix, which the parser stripped. Stating a theorem without its proof inline is standard practice.
- **Missing code/release status removed** per hard rule: cited entities are assumed to exist.
- **Criticism about Figure 1 oversimplification removed.** The argument about Euclidean vs. dot-product in 1D is conceptually valid as motivation; the figure cannot be independently verified from text alone, and the paper's qualitative point is standard.
- **Criticism about Associative Recall being "unremarkable" removed.** The paper claims ZETA "matches" standard attention — which is exactly what the data shows. This is a correct and appropriate claim, not a weakness.
- **Generic "evaluation lacks rigor" framing removed** (per filtering discipline): lacks a concrete anchor.
- **Speculative-fatal claim about "if normalization were X, reported values would be impossible" removed** — no such concrete claim was actually made; removed as speculative.

---

## Novel Insights

The reviews surface a tension that the paper does not fully grapple with: ZETA is a *system* with multiple interacting components (low \(d_K\), Z-order encoding, chunked sorted search, Cauchy-Softmax, mean-value smoothing), each of which could independently contribute to the strong LRA results. The paper provides strong system-level evidence but weak component-level attribution. This is a common pattern in efficient-attention papers, but it is particularly acute here because the Z-order retrieval is the paper's marquee contribution, yet it receives the least validation. The locality-preservation experiment (Figure 3) measures overlap in *Euclidean nearest neighbors on random data* — not *attention-score nearest neighbors on trained data*. An experiment bridging this gap would substantially strengthen the paper. A second, more subtle insight: the chunking strategy for causal masking (Section 3.2.2) is arguably as important as the Z-order encoding itself for achieving parallelism, but it is underemphasized relative to the Z-order contribution.

---

## Suggestions

1. **Correct the abstract** to say "matches or outperforms on LRA and is competitive on WikiText-103" rather than "outperforms … on WikiText-103."
2. **Add a direct retrieval-recall experiment** measuring what fraction of the true top-\(k\) attention scores are captured by the Z-order window on a real task (e.g., one LRA task or WikiText-103), across different window sizes \(k\) and dimensions \(d_K\). This would directly validate the core approximation.
3. **Ablate the Cauchy-Softmax vs. standard dot-product softmax** (with the same low \(d_K\)) on at least one LRA task, and ablate the mean-vector smoothing.
4. **Report confidence intervals** for LRA and WikiText-103 results over 3+ runs.
5. **Specify concrete hyperparameters** (chunk size \(M\), window size) used in the main experiments.
6. **Tighten the theoretical section** to either (a) drop the disconnected JL-based bound and replace it with a geometric argument about Z-order box-counting properties and why 1-D windows approximate nearest neighbors for low-dimensional data, or (b) clearly scope it as motivational background and rename accordingly.

---
