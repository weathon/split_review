## Summary

This paper investigates why naive output alignment (minimizing layer-wise reconstruction error) fails for 1-bit post-training quantization (PTQ) of LLMs, and proposes remedies. The authors provide diagnostic analysis (Figures 1–2) showing that layer-wise output matching can increase block-level loss, that quantization errors accumulate across layers, and that token-similarity matrices drift. They propose (a) confining output alignment to only the last fully-connected layer of each block, (b) using the true full-precision input (output error) rather than the quantized input (activation-conditioned error), and (c) an Attention Matrix Preservation (AMP) mechanism that blends parameters using sign-of-gradient masks from a token-similarity objective. Experiments on OPT (1.3B–30B) and LLaMA-2/3 show consistent perplexity improvements over prior 1-bit PTQ methods across most settings.

## Strengths

1. **Diagnostic analysis revealing why naive output matching fails** — Figure 1 shows that for several layers of LLaMA-2-7B, ARB-X (layer-wise output matching) increases block-level loss relative to ARB (weight alignment), despite reducing layer-level loss. This directly motivates the paper's selective strategy and is a genuine, self-contained contribution.

2. **Demonstration of error accumulation and attention degradation** — Figure 2 quantifies two phenomena: (top) block-wise MSE relative to full-precision grows with depth under ARB-X even while cosine similarity stays high; (bottom) token-similarity matrices (a proxy for attention structure) drift from the full-precision baseline. These measurements concretely support the claim that naive output alignment degrades attention in deeper layers.

3. **AMP ablation shows large effect on LLaMA** — Table 3 shows that removing AMP increases perplexity by over 10 points on LLaMA-2-7B (C4: 19.25 → 29.12), while the effect on OPT-6.7B is much smaller (16.22 → 16.35). This controlled ablation provides strong evidence that AMP is critical for architectures like LLaMA that use RMSNorm, and the paper offers a principled hypothesis (direction-sensitivity under RMSNorm vs. LayerNorm) to explain the asymmetry.

4. **Closed-form optimization for the output-error objective** — The paper derives analytical updates for α_c (Eq. 5), rows of B (Eq. 6), and α_r (Eq. 8), enabling efficient block-wise optimization that explicitly accounts for accumulated quantization error rather than relying on the activation-conditioned approximation used in ARB-X.

5. **Consistent improvements across 28 of 29 evaluated settings** — The method outperforms all baselines across OPT models (1.3B–30B) on C4, WikiText2, PTB, and zero-shot QA, and across LLaMA-2/3 on C4 and WikiText2. The gains over the strongest baseline (ARB-RC) are modest but consistent.

## Weaknesses

### Fatal
None.

### Major

1. **Unexplained failure on LLaMA-2-7B / PTB** — In Table 2, the method achieves perplexity 3166 on PTB for LLaMA-2-7B, which is ~4× worse than ARB-RC (763) and ARB-X (681), even though it uses the same bit width (1.06 bits). The paper's justification — "the large perplexity indicates that the metric cannot provide a meaningful evaluation" — is insufficient. While PTB perplexities at these extreme values are indeed less reliable, the fact that three baselines (PB-LLM at 1.7 bits, ARB-RC, ARB-X) all produce substantially lower perplexities suggests a genuine pathological behavior of this method on this specific model/dataset pair. The paper acknowledges this exception but does not investigate whether it stems from a numerical instability, a bug, or a systematic failure mode that could silently affect other settings. This weakens the paper's claim of "consistent" improvement.

2. **Selective layer strategy (last FC per block) is stated without empirical justification** — Section 4.2 specifies that output alignment is restricted to only the last fully-connected layer of each block because it has "the most direct impact on the block loss." No ablation compares this choice against alternatives (e.g., the first FC layer, the attention projection, or a data-driven selection derived from Figure 1's diagnostic). If the method's performance is sensitive to which layer is selected, the current design is unsupported. This is the most critical missing ablation in the paper.

### Minor

1. **AMP update rule is heuristic and unevaluated against simpler alternatives** — The AMP mechanism (Eqs. 9–11) computes sign-of-gradient masks from a secondary token-similarity objective and uses them to blend original and optimal parameter values. While the ablation shows AMP is effective, the paper does not compare this specific formulation to simpler alternatives (e.g., adding the AMP objective as a regularization term to the primary loss, or directly regressing the similarity matrix). Without such a comparison, it is unclear whether the benefit comes from the specific design or from any mechanism that preserves token similarity.

2. **Modest improvements over the strongest baseline** — For OPT-30B on C4, the gain over ARB-RC is 13.34 → 13.15 (0.19 PPL); for LLaMA-2-7B on C4, 20.4 → 19.25 (1.15 PPL). These are real improvements but modest relative to the gap from full precision. For zero-shot QA, the average improvement over ARB-RC is ≤1% across all OPT model sizes, which is within typical benchmark noise.

3. **Zero-shot QA results reported only as averages** — Table 1 reports accuracy averaged over 7 datasets, but individual per-dataset results are not shown for OPT models. The 0.78% gain on OPT-6.7B (52.58 → 53.33) could be driven by one or two datasets. Per-dataset breakdown is needed to assess consistency.

4. **Clarity issue in AMP objective notation** — Equation 9 writes the AMP maximization as ‖(·) ⊙ (·)‖ where the norm notation is ambiguous. The second line clarifies this is the Frobenius inner product (trace form), but the first line's ‖·‖ could be misinterpreted as a matrix norm.

### Trivial
None.

## Nice-to-Haves

1. **Replace the fixed "last FC" selection with a principled rule** — One promising approach: use the block-level loss from the Section 3.1 analysis to determine per-layer whether output matching helps, and apply it selectively only where it reduces block loss. This would directly leverage the paper's own diagnostic insight.

2. **Compare AMP against a simple additive regularization** — For instance, adding Tr[ẐẐ^T ZZ^T] as a regularizer to the primary loss would test whether the sign-mask blending mechanism is essential or whether any similarity-preserving objective suffices.

3. **Investigate the LLaMA-2-7B/PTB failure** — Even if the issue is confirmed as a numerical pathology of the metric at extreme perplexities, documenting the root cause (e.g., specific layer where the quantized model produces degenerate outputs) would strengthen trust in the method's generality.

4. **Report per-dataset zero-shot results and optionally include variance over 3 runs.**

## Removed Points

*The following points from the inputs were removed with justification:*

- **"Two orders of magnitude worse than every baseline"** — Removed because it is factually incorrect. BiLLM produces 5243 on the same setting (worse than 3166), and PB-LLM at 1.7 bits is not directly comparable. The ratio is ~4×, not two orders of magnitude. The underlying concern (PTB failure) is retained as a Major weakness with corrected framing.
- **Missing comparison with STB-LLM** — Removed per policy: requesting additional baselines is scope creep. The existing baseline set (PB-LLM, BiLLM, ARB-RC, ARB-X) covers the principal 1-bit PTQ methods.
- **Variance/statistics request** — Removed because perplexity is deterministic given calibration data, and variance reporting for zero-shot QA is a soft recommendation, not a methodological gap.
- **"Only Llama 7B studied" (from strength finder conflict check)** — Not applicable; this paper studies OPT 1.3B–30B and LLaMA-2/3 at multiple sizes.
- **Generic strength ("addresses important problem")** — Removed from strengths as too generic.

## Novel Insights

None beyond the paper's own contributions. The diagnostic analysis (Figures 1–2) is the most novel aspect; the method components are reasonable extensions of prior work rather than paradigm-shifting innovations.

## Suggestions

1. Add an ablation comparing different layer selections within a block (first FC, attention projection, last FC, all layers) to justify the design choice.
2. Investigate and report the root cause of the LLaMA-2-7B/PTB failure, or at minimum provide evidence (e.g., per-layer output norms, degenerate samples) characterizing the failure mode.
3. Compare the AMP sign-mask blending against a simple additive regularization of the token-similarity objective to isolate whether the specific update mechanism matters.
4. Report per-dataset zero-shot results in the main paper or appendix to validate that the average improvement is not driven by a single dataset.

## Score and Decision

### Round 1 — Bracketing

| Band | Query | Anchors Found | Avg Scores |
|------|-------|---------------|------------|
| Weak (<3.5) | 1-bit PTQ of LLMs | PrefixQuant (3.0), EfficientQAT (3.0), CVXQ (3.0), BMLM (3.0) | ~3.0 |
| Middle (3.5–7.5) | 1-bit PTQ of LLMs | **PB-LLM (6.75)**, **ARB-LLM (7.00)**, **STBLLM (6.00)**, QRazor (5.20) | 5.20–7.00 |
| Strong (>7.5) | 1-bit PTQ of LLMs | Spectra (7.60), Scaling Laws for Precision (8.00), CBQ (7.60) | 7.60–8.50 |

**Initial bracket:** 5.5–7.0. The paper is not as weak as the 3.0 papers (which had fundamental flaws) nor as strong as the >7.5 papers (which have broader impact and cleaner methods). It falls between STBLLM (6.0) and ARB-LLM (7.0).

### Round 2 — Narrowing

| Query | Anchors | Avg Scores |
|-------|---------|------------|
| Output alignment PTQ (4.5–6.0) | Output Align. Length Gen. (5.50), Eval. Quant. LLMs (4.75), LLM-QAT (5.00), FlatQuant (5.20) | 4.75–5.50 |
| Output alignment PTQ (6.0–7.5) | **PB-LLM (6.75)**, **ARB-LLM (7.00)**, OSTQuant (6.20), OmniQuant (6.40) | 6.20–7.00 |

**Comparison to anchors read in full:**
- **ARB-LLM (7.00)** — Direct predecessor. ARB-LLM has a cleaner method (alternating refinement + column-wise scaling + CGB) with more thorough ablation. The current paper's diagnostic analysis is more insightful, but its method section is weaker (heuristic layer selection, untested AMP design). The PTB failure is a blemish ARB-LLM does not have. **The current paper is slightly weaker than ARB-LLM.**
- **PB-LLM (6.75)** — Broader scope (PTQ + QAT) but was criticized for limited evaluation tasks and missing ablation. The current paper has stronger diagnostic analysis and broader evaluation, but PB-LLM's method was cleaner. **Comparable quality, slightly tilted toward PB-LLM.**
- **STBLLM (6.00)** — Criticized for being a combination of existing techniques. The current paper has more novel diagnostic insights but shares similar "incremental method" criticisms. **Current paper is stronger than STBLLM.**
- **OmniQuant (6.40)** — Simple, well-ablated method for 2–4 bit quantization. The current paper targets a harder regime (1-bit) and has stronger diagnostic contributions, but weaker ablations. **Comparable.**

### Final Score

**Score: 6.0** — The paper has a genuine contribution in its diagnostic analysis of why output matching fails for 1-bit PTQ, and the proposed method consistently improves over strong baselines on 28 of 29 settings. However, the method itself has notable heuristic design choices (selective layer without ablation, AMP without comparison to alternatives) and one unexplained catastrophic failure on LLaMA-2-7B/PTB. The paper is between STBLLM (6.0) and ARB-LLM (7.0) in quality — it has stronger diagnostics than either but a less rigorous method section than ARB-LLM.

**Decision: Accept** — The diagnostic contribution alone (Figures 1–2) is a meaningful advance that justifies publication; the method improvements, while imperfect, are reasonable first steps building on those insights.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>