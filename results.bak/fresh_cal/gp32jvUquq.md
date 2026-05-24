Now I have all the evidence needed to produce the final consolidated review.

---

## Summary

This paper proposes Basis Sharing, an SVD-based LLM compression method that goes beyond compressing individual weight matrices in isolation. It horizontally concatenates weight matrices from multiple layers, applies input-aware SVD (using the whitening/scaling matrix from SVD-LLM adapted to the multi-layer setting by vertically concatenating input activations), and shares a common basis across layers while retaining per-layer coefficients. The paper also analyzes which weight matrix types (e.g., $W_K$, but not $W_O$) benefit from sharing and how to group layers. Experiments on LLaMA, LLaMA2, OPT-6.7B, Mistral-7B, and GPT-2 compare against SVD-LLM, ASVD, FWSVD, and Dynamic Tying.

## Strengths

- **Novel cross-layer basis sharing via concatenated SVD.** The core idea — horizontally concatenating weight matrices from multiple layers, performing SVD, and sharing the resulting basis while keeping per-layer coefficients — is a genuine departure from prior SVD methods (SVD-LLM, ASVD, FWSVD) that compress each layer independently. It also differs from earlier parameter sharing approaches that force identical weight matrices (requiring training from scratch), by allowing layers to share a structural basis but retain individual functionality through unique coefficients (Section 3.1, Figure 3.1).

- **Weight matrix type analysis guides which matrices to share.** The paper provides a concrete, quantitative criterion: it measures Frobenius loss on the input-scaled matrices ($\mS\mW$) for sharing vs. not sharing each matrix type. For example, sharing $W_K$ across two layers in LLaMA2-7B *reduces* loss (61817.3 vs 66682.9), while sharing $W_O$ *increases* it (10618.3 vs 4355.1+4895.7) — giving a clear rule about which types admit sharing (Section 3.2, Figure 3.5).

- **Consistent perplexity reduction across multiple LLM families without fine-tuning.** On LLaMA-7B, LLaMA2-7B, OPT-6.7B, and Mistral-7B, Basis Sharing achieves lower perplexity than ASVD, FWSVD, and SVD-LLM at 20%–50% compression ratios without any fine-tuning. In particular, OPT-6.7B and Mistral-7B show up to 25% PPL reduction compared to SVD-LLM (Table 3 cited in Section 4.2).

- **Systematic study of group size and fine-tuning recovery.** The paper evaluates groups of 2, 4, 8, 16, and 32 consecutive layers, both in zero-shot settings and after LoRA/full-parameter fine-tuning (Section 4.3). This provides practical guidance on the trade-off between compression and quality.

- **Throughput improvement demonstrated on real hardware.** Under a 50% compression ratio, Basis Sharing achieves 1.57× throughput of the dense LLaMA-7B model on a single A100 GPU (Section 4.4).

## Weaknesses

### Fatal

None.

### Major

None.

### Minor

- **Adjacent-layer grouping rationale relies heavily on a single visualization.** The paper states that "adjacent layers lead to smaller Frobenius loss" based on Figure 3.5 (pairwise Frobenius loss for LLaMA2-7B $W_K$ and $W_O$), but does not quantitatively demonstrate that off-diagonal (non-adjacent) pairs are systematically worse across the full matrix. The subsequent empirical study (Section 4.3) confirms that 2-layer grouping works well in practice, partially mitigating this concern, but the design rationale in Section 3.3 would benefit from stronger quantitative support.

- **Throughput comparison is only against the dense model.** The hardware benchmark (Section 4.4) compares Basis Sharing's throughput only against the uncompressed model, not against other SVD-based compressed models (e.g., SVD-LLM at the same compression ratio). Since all SVD methods reduce parameter count, it is unclear whether the speedup comes from the specific sharing structure or merely from the lower parameter count that any SVD method provides.

- **S-matrix update for high compression ratios (≥40%) is underspecified.** The paper mentions (Section 4.1) that when compression ratio ≥ 40%, "deviated inputs" are used to update the $\mS$ matrix for subsequent layers, "similar to that in SVD-LLM." The exact procedural details (e.g., whether this is iterative, how the deviation is computed) are not fully described, which could affect reproducibility.

- **No error bars or variance measures.** All results are reported as point estimates without confidence intervals or standard deviations. While single-run evaluation is common in this area, zero-shot evaluations are known to be sensitive to calibration details; even a single replicated run would strengthen confidence in the reported margins.

- **Computational cost of the compression process is not reported.** The paper reports that FWSVD runs out of memory, but does not report the wall-clock time or peak memory usage of Basis Sharing's own compression step. For a compression method, the cost of compressing is relevant for practical adoption.

### Trivial

None.

## Nice-to-Haves

- A comparison of throughput against other SVD-compressed models (e.g., SVD-LLM) would clarify whether the basis sharing structure itself confers a speed advantage beyond parameter reduction.
- Reporting wall-clock time and memory usage of the compression process itself would aid practical deployment decisions.
- The choice of adjacent-layer grouping could be further validated by showing that the pairwise Frobenius loss matrix (Figure 3.5) correlates with downstream perplexity or accuracy, rather than relying on it as a proxy.

## Removed Points

These points are removed from the main review; treat them with caution.

1. **"Internal inconsistency in selection criterion"** — REMOVED. This criticism misunderstands the paper. The Figure 3.3 example shows that RAW (unscaled) Frobenius loss is a poor proxy for output error. To address this, the paper introduces the scaling matrix $\mS$, derived from the input data via $\mS(\mS)^T = cholesky(\mX^T\mX)$, and applies SVD to the *scaled* matrices $\mS\mW$. The Frobenius loss comparison in Section 3.2 is performed on these scaled matrices, which directly incorporate input structure. The paper builds on the established SVD-LLM framework here, and there is no inconsistency: the criticism conflates raw Frobenius loss (which the paper correctly identifies as problematic) with input-aware scaled Frobenius loss (which the paper uses as its criterion).

2. **"Missing experimental data (table placeholders)"** — REMOVED. The LaTeX command placeholders (e.g., `\accuracyTable`) are artifacts of the PDF-to-text extraction process. The instructions explicitly state that tables exist in the original submission and that formatting artifacts should not be treated as author errors. The paper's quantitative claims are structurally present and would be verifiable from the original PDF.

3. **"Selection bias in baseline comparisons (post-hoc grouping, hyperparameter differences)"** — REMOVED. The paper transparently discusses the group-size trade-off (Section 4.3): "Grouping four or five layers... is more reasonable when compression ratio is lower than 30%... Two layers sharing a basis matrix is a good choice when the compression ratio is larger than 30%." The main results use 2-layer grouping across 20%–50% ratios, which the paper shows is optimal for >30% and a reasonable consistent choice. The claim about different hyperparameter setups is not substantiated — the paper uses the same calibration setup (256 Wikitext-2 samples, 2048 tokens, FP64 for $\mS$) as SVD-LLM.

4. **"Learning rate difference between LoRA and full fine-tuning raises comparability questions"** — REMOVED. The paper explicitly addresses this: "WikiText-2 is relatively a small dataset to fine-tune the large model. Directly using this dataset to fine-tune could easily lead to overfitting. Therefore, we reduce the \textit{learning\_rate} from 1e-4 to 2e-6" (Section 4.3). The reasoning is valid — different learning rates are appropriate for LoRA (which updates far fewer parameters) vs. full fine-tuning on a small dataset.

5. **"Frobenius-based rule may not generalize" (speculative)** — REMOVED. The criticism speculates that the selection criterion "could fail for other configurations" without providing evidence. The paper tests across multiple model families (LLaMA, LLaMA2, OPT, Mistral) and compression ratios, providing empirical support.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. Strengthen the adjacent-layer grouping justification by providing a quantitative summary of the pairwise Frobenius matrix (e.g., mean/median loss for adjacent vs. non-adjacent pairs), and ideally showing that this metric correlates with downstream PPL.
2. Add a throughput comparison against at least one other SVD method (e.g., SVD-LLM) to isolate the effect of the sharing structure.
3. Provide more detail on the S-matrix update procedure for high compression ratios.
4. Include at least one measure of variance (e.g., multiple calibration seeds) for the main results.

## Score and Decision

The paper proposes a well-motivated and novel extension of SVD-based compression to cross-layer parameter sharing. The core method is sound, the weight matrix type analysis provides actionable design guidance, and the experimental results span multiple LLM families and compression ratios with consistent improvements. The weaknesses are minor — none threaten the core claims. The "internal inconsistency" criticism raised by the harsh reviewer is based on a misunderstanding of how the scaling matrix $\mS$ connects scaled Frobenius loss to output error. The paper is a solid contribution to the LLM compression literature.

MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>