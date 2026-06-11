Now I have strong calibration. Let me produce the final review with all analysis integrated.

## Summary

AdaSVD proposes two techniques for SVD-based LLM compression: (1) **adaComp**, which compensates for SVD truncation error by alternately updating U and V matrices via Moore-Penrose pseudoinverse with a stack-of-batch strategy, and (2) **adaCR**, which assigns layer-specific compression ratios based on input-output cosine similarity. Experiments on multiple LLM families (LLaMA2, OPT, Vicuna, Mistral) show consistent perplexity and commonsense reasoning improvements over prior SVD-based methods.

## Strengths

1. **Moore-Penrose pseudoinverse for numerically stable post-truncation updates** (Section 3.1, Figure 3a): The paper identifies that naive gradient-based or direct-inverse updates for post-truncation compensation are numerically unstable. Reformulating the optimization as a least-squares problem and solving via Moore-Penrose pseudoinverse yields smooth convergence, empirically demonstrated in Figure 3(a). This is a principled improvement over prior SVD-based methods (FWSVD, ASVD, SVD-LLM), which lack post-truncation compensation.

2. **Layer-adaptive compression ratio (adaCR) based on input-output similarity** (Section 3.2, Table 3b, Figure 4): Prior SVD compression methods apply uniform compression ratios across layers, ignoring varying layer importance. AdaSVD assigns compression ratios proportionally to normalized cosine similarity between input and output activations. Table 3b validates this empirically across all tested compression ratios (e.g., 60% CR on WikiText-2: 69.46 with uniform vs. 50.33 with adaCR).

3. **Stack-of-batch strategy for GPU memory constraints** (Section 3.1, Figure 3b): The paper addresses a practical deployment constraint — large calibration datasets exceed GPU memory — by shuffling samples into fixed-size buckets, reducing compression error relative to a naive small-batch baseline.

4. **Consistent empirical advantage over SVD-LLM across multiple settings** (Tables 1, 2, 4): AdaSVD outperforms the prior state-of-the-art SVD-LLM on all three language modeling datasets and five reasoning datasets at 40%, 50%, and 60% compression ratios on LLaMA2-7B. This advantage generalizes to OPT-6.7B, Vicuna-7B, and Mistral-7B, and holds when combined with GPTQ-INT4 quantization.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

1. **Figure 1 y-axis description is inconsistent with Table 1 data**: The Figure 1 caption states the y-axis shows perplexity in log₁₀ scale ranging from 10⁰ to 10² (PPL 1–100). However, Table 1 reports vanilla SVD, FWSVD, and ASVD perplexities in the thousands to tens-of-thousands at 40% compression (e.g., SVD PPL 39,661, log₁₀ ≈ 4.6). These values cannot be plotted within the stated axis range. If the figure shows only a subset of methods (those on-scale), this should be stated explicitly in the caption. As written, the figure description and the table data are incompatible, which erodes confidence in the paper's central visual exhibit.

2. **Iteration-ablation text contradicts the data shown in Table 3c**: Section 4.3 states "under higher compression ratios, additional iterations lead to performance improvements." However, Table 3c shows that at 60% compression (the highest ratio presented in the main paper), 1 iteration yields PPL 50.33, while 3 iterations yield 64.12 and 15 iterations yield 62.34 — 1 iteration is best. The claim may be supported by 70%/80% data in the appendix, but the main paper's data does not support the textual claim. The text and table should be aligned.

3. **Percentage improvements in Table 1 are unverifiable against the raw numbers**: Parenthetical percentages listed next to AdaSVD's perplexity values (e.g., 18%, 158%, 18% at 40% compression) do not match standard improvement calculations over the SVD-LLM baseline values in the same table. For example, the WikiText-2 improvement at 40% is (16.11−14.76)/16.11 ≈ 8.4%, not 18%; the C4 improvement at 60% is (561.00−239.18)/561.00 ≈ 57.4%, not 157%. Some percentages match (WikiText-2 at 60%: ~44%), but many do not. The paper does not specify how these percentages are computed, making the reported gains unverifiable.

4. **GPTQ integration results are presented without discussing whether quantization helps or hurts**: Table 4 shows that adding GPTQ-INT4 to already SVD-compressed models substantially *increases* perplexity compared to SVD alone (e.g., AdaSVD at 40%: PPL 14.76 → 22.55; SVD-LLM at 40%: 16.11 → 33.56). The paper only states that AdaSVD+GPTQ outperforms SVD-LLM+GPTQ, without discussing whether the combination of SVD and quantization is practically useful or why GPTQ degrades performance on top of SVD compression.

5. **Model sizes and inference throughput not reported**: The paper reports compression as the fraction of parameters retained in SVD factors but never states the resulting model size in MB/GB or the inference speedup (tokens/second). For a compression paper targeting resource-constrained deployment, these metrics are directly relevant.

### Trivial
None.

## Nice-to-Haves

- Comparison of adaCR against alternative importance metrics (e.g., Fisher information, singular-value entropy, output sensitivity) would strengthen the claim that cosine similarity is a principled and not just convenient choice.
- Variance or confidence intervals for the reported perplexity numbers, given calibration data sampling randomness.
- Clarification of the relationship between compression ratio percentage and the resulting rank k relative to the original matrix rank.

## Removed Points

These points from the inputs are removed with brief justification:

- **"Original model scores are incorrect (MMLU 7.34%, C4 PPL 45.30)"**: REMOVED — parser-induced column misalignment. Table 4 reports C4=7.34 for the original model, which is within the expected range. The 45.30 and 7.34 values in Table 1 are almost certainly columns shifted by the complex table structure, not the paper's actual numbers.
- **"Missing Table 2"**: REMOVED — appendix content stripped by parser.
- **"Method novelty is limited" / "standard linear-algebra tools"**: REMOVED — opinion-based framing. Applying pseudoinverse-based alternating updates to the specific problem of post-truncation SVD compensation for LLMs is a legitimate contribution, and the paper's empirical results demonstrate its value.
- **"No statistical significance"**: REMOVED — single-run evaluation is standard practice for LLM compression benchmarks; this is not a weakness specific to this paper.
- **"FWSVD/ASVD reproduction quality concerns"**: REMOVED — speculative without evidence that the reproduction from official repos was unfaithful.
- **Strength: "Addresses an important problem"**: REMOVED — generic and applies to most papers in this area.

## Novel Insights

None beyond the paper's own contributions. The harsh critic and strength finder did not surface any observation that meaningfully reframes or extends the paper's claims.

## Suggestions

1. Resolve the Figure 1 discrepancy: either correct the axis range description or explicitly note which methods are omitted from the plot and why.
2. Clarify the basis for the percentage improvements in Table 1, or remove them if they cannot be consistently justified.
3. Align the iteration-ablation discussion (Section 4.3) with the data shown in Table 3c, or explicitly reference the appendix results that support the claim.
4. Add a brief discussion of why GPTQ increases perplexity on top of SVD compression (Table 4) and under what circumstances the combination is beneficial.
5. Report model sizes in MB/GB and inference throughput (tokens/second) at each compression ratio.

---

## Calibration Report

**Round 1 — Bracketing (3 queries):**
- Weak anchors (<3.5): `SLiM: One-shot Quantized Sparse Plus Low-rank` (3.67), `AutoTrunc` (4.00), `TensorGPT` (3.75)
- Middle anchors (3.5–7.5): `ASVD` (6.25), `Low-Rank Correction for Quantized LLMs` (5.00), `Compressing LLMs: The Truth is Rarely Pure and Never Simple` (6.75), `OATS` (6.25)
- Strong anchors (>7.5): No directly comparable papers found (retrieved papers were on data selection, fine-tuning, scaling laws)

**Initial bracket: 4.5 – 6.5**

**Round 2 — Narrowing (2 queries in 4.5–6.5 band):**
- `ASVD` (6.25, Reject) — The most directly comparable anchor. ASVD also proposes activation-aware SVD with iterative calibration. AdaSVD has a more comprehensive evaluation (more models, datasets) and a clearer novel component (post-truncation compensation), but also has presentation issues (figure/table inconsistency, unclear percentages) that ASVD does not. → **AdaSVD is slightly weaker than ASVD.**
- `MoE-SVD` (5.00, Reject) — SVD compression for MoE models. AdaSVD has clearer methodology and more thorough evaluation. → **AdaSVD is stronger than MoE-SVD.**
- `Low-Rank Correction for Quantized LLMs` (5.00, Reject) — Different setting (quantization correction) but similar level of contribution. → **AdaSVD is comparable.**
- `Two Sparse Matrices (DSF)` (6.33, Accept) — More novel factorization approach with strong results. AdaSVD has clearer LLM-specific motivation but narrower scope. → **AdaSVD is weaker than DSF.**

**Final score:** 5.5. The paper has genuine contributions (adaComp is a novel post-truncation compensation mechanism; adaCR is a well-motivated departure from uniform compression) and reasonably thorough evaluation across multiple models. However, the presentation issues (Figure 1 vs. Table 1 inconsistency, unverifiable percentage improvements, iteration-text mismatch) reduce confidence in the empirical claims and prevent acceptance in the current form. The paper sits between the reject-level SVD compression papers (~4–5) and the stronger, cleaner compression papers (~6–7).

---

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>