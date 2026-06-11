Now I have a clear picture from all anchors. Let me compile the final review.

**Calibration analysis:**

| Anchor | Avg Score | Round | Comparison |
|--------|-----------|-------|------------|
| LeanQuant (ISqx8giekS) | 5.17 | R1 | Similar profile — good method with missing details/justifications; accepted despite concerns. Our paper comparable but PTB dismissal is more concerning. |
| FlatQuant (pxGucWt9vM) | 5.20 | R1/R2 | Similar quality; had unfair comparison concerns. Our paper's weaknesses are different but comparable in severity. |
| SliM-LLM (tjlTczcnPz) | 5.40 | R2 | Stronger ambition but had "slower than FP16" fatal practical issue. Our paper doesn't have a practical failure of that magnitude but has the PTB anomaly. Slightly weaker overall. |
| Super Weight (0Ag8FQ5Rr3) | 4.60 | R2 | Discovery/analysis paper; our paper has much stronger technical contribution. Clearly below our paper. |
| FPTQ (ykhRO1mAg3) | 4.00 | R2 | Clearly below — less thorough analysis and weaker results. |
| NeuroQuant (44cMlQSreK) | 7.20 | R1 | Clearly above — strong theoretical framework and comprehensive evaluation. |
| Scaling Laws for Precision (wg1PCg3CUP) | 8.00 | R1 | Clearly above — impactful findings with rigorous methodology. |

**Round 1 bracket**: 4.0–5.5 → narrowed to **4.8–5.3** after reading Round 2 anchors. Our paper is comparable to but slightly weaker than LeanQuant (5.17) and FlatQuant (5.20), mainly due to the PTB dismissal and AMP justification gap. **Final score: 5.0.**

---

## Summary
This paper investigates why naive output-alignment objectives underperform in 1-bit post-training quantization (PTQ) of LLMs. Through a diagnostic analysis on LLaMA-2-7B, it identifies three failure modes: layer-wise output matching does not guarantee block-level loss reduction, activation-conditioned error accumulates across layers, and output alignment can disrupt attention patterns. The paper proposes three remedies: (1) a reformulated objective targeting true output error ‖XW − X̂Ŵ‖ rather than activation-conditioned error, (2) an Attention Matrix Preservation (AMP) mechanism to protect token-similarity structure, and (3) a selective strategy applying output alignment only to the last FC layer of each transformer block. Experiments on OPT (1.3B–30B) and LLaMA models show consistent perplexity improvements over baselines on C4 and WikiText2.

## Strengths
- **Systematic diagnostic analysis (Section 3):** Figures 1–2 provide a genuinely insightful three-part diagnosis of why naive output alignment fails: (i) layer-wise output matching can increase block-level loss relative to weight matching (Fig. 1), (ii) activation-conditioned error diverges from true output error as quantization proceeds (Fig. 2, top panels), and (iii) token similarity matrices degrade in deeper layers (Fig. 2, bottom). This analysis is well-executed and explains the gap between the intuitive appeal of output alignment and its disappointing performance in practice.
- **Reformulated Output Error objective with closed-form solutions (Section 4, Eqs 3–8):** Replacing ARB-X's activation-conditioned error ‖X̂W − X̂Ŵ‖ with the true output error ‖XW − X̂Ŵ‖ directly addresses the error accumulation problem identified in Section 3.2. Deriving closed-form solutions for α_c (Eq. 5), B row-wise updates (Eq. 6), and α_r (Eqs. 7–8) under this cross-term objective is non-trivial technical work.
- **AMP mechanism validated by dramatic ablation (Table 3):** Removing AMP causes LLaMA-2-7B C4 perplexity to jump from 19.25 to 29.12 (>50% degradation), confirming its critical role for RMSNorm-based architectures. The architecture-dependent sensitivity (AMP matters far more for LLaMA than OPT) is well-explained via RMSNorm vs. LayerNorm normalization properties (Section 5.3).
- **Consistent empirical gains across OPT scales on core benchmarks (Table 1):** On C4, the method reduces PPL from 27.70 (ARB-RC) to 24.69 on OPT-1.3B and from 13.34 to 13.15 on OPT-30B. Gains hold across five OPT scales and three LLaMA models on C4 and WikiText2, covering two architecture families.

## Weaknesses

### Fatal
None.

### Major
- **LLaMA-2-7B PTB collapse is dismissed rather than investigated (Table 2):** The proposed method achieves 3166 perplexity on PTB for LLaMA-2-7B, substantially worse than ARB-X (681), ARB-RC (763), and PB-LLM (657) — the baselines it claims to improve upon. The paper's response is: "the large perplexity indicates that the metric cannot provide a meaningful evaluation" (line 233). This is evasive: the paper treats PTB as valid evidence when reporting OPT results (Table 1), but dismisses it when the method underperforms on LLaMA. The paper also states that the method "consistently outperforms previous state-of-the-art quantization approaches across all benchmarks" (line 176), while later noting the exception only in passing. The paper should investigate why the proposed method (particularly AMP or the output-error objective) degrades on PTB for LLaMA-2-7B rather than dismissing the result.
- **AMP objective (Eq. 9) lacks theoretical justification:** AMP maximizes the element-wise (Hadamard) product of the quantized and full-precision token-similarity matrices: max ‖(X̂ŴŴᵀX̂ᵀ) ⊙ (XWWᵀXᵀ)‖. The natural formulation for preserving similarity structure would minimize their difference: ‖X̂ŴŴᵀX̂ᵀ − XWWᵀXᵀ‖. The product-based objective conflates structural similarity with magnitude — if the quantized model produces token similarities with larger magnitudes (even in incorrect patterns), the product increases. No justification is provided for why the product form is preferable, and no ablation comparing product vs. difference-based objectives is reported. Since Table 3 shows AMP is critical for LLaMA performance, this choice deserves scrutiny.

### Minor
- **Selective layer-wise application sidesteps rather than solves the block-level loss problem:** Section 3.1 demonstrates that layer-wise output matching does not guarantee block-level loss reduction. However, the proposed remedy — apply output alignment only to the last FC layer of each block and fall back to weight alignment (ARB-RC) for all other layers (Section 4.2) — is a workaround, not a solution to the fundamental problem. The paper has not shown how to make output alignment effective for interior layers; it has simply abandoned output alignment for them. This narrows the contribution relative to the framing.
- **Gains over the strongest baseline (ARB-RC) are modest for larger models and downstream tasks:** On zero-shot QA, OPT-13B improves from 55.01 to 55.06 (+0.05 points, within noise) and OPT-30B from 57.11 to 57.70 (+0.59). On C4 perplexity, gains shrink as model size increases: OPT-1.3B achieves a 10.9% relative improvement but OPT-30B only 1.4%. For practical deployment with larger models, the advantage over ARB-RC may be negligible.
- **Diagnostic analysis (Section 3) conducted on a single model with a single calibration set:** The three-part analysis uses only LLaMA-2-7B with the C4 calibration set. While the patterns are plausible and the paper does test the final method on OPT and LLaMA-3, the motivating insights are presented as general findings about 1-bit PTQ without evidence that the same diagnostic patterns hold across architectures.

### Trivial
- Weight-bit counts differ between OPT (1.11) and LLaMA (1.06) for the same methods without explanation (Tables 1–2).

## Nice-to-Haves
- Calibration-set ablations (different datasets or sizes) would strengthen claims about robustness and address sensitivity concerns.
- Statistical significance or variance estimates for key results, particularly given the marginal QA improvements.
- Runtime and memory overhead analysis is deferred to the appendix; key numbers would benefit the main text.

## Removed Points
These points are flagged to be removed, treat them with caution:
- **Missing baselines (OneBit, BitDistiller):** The Harsh Critic suggested these as stronger baselines. Removed per policy — reviewers should not invent missing related works that may or may not exist.
- **Equation 2 parser artifact (‖X̂Ŵ − X̂Ŵ‖):** This is a PDF extraction artifact, not an author error. The original submission likely reads ‖X̂W − X̂Ŵ‖.
- **LLaMA QA results deferred to Appendix:** The Harsh Critic questioned whether these claims can be verified. Removed — the appendix exists in the original submission; the parser strips appendices from all papers.
- **Missing runtime/memory overhead in main text:** Moved to Nice-to-Haves as a common improvement suggestion applicable to almost any systems paper, not a substantive weakness.
- **No statistical significance reported:** Moved to Nice-to-Haves; single-run evaluation without confidence intervals is standard practice for large-scale LLM quantization benchmarks.
- **Section 3 tension between block-level loss and end-to-end perplexity:** The Harsh Critic noted that ARB-X sometimes increases block-level loss yet achieves lower perplexity on LLaMA-2-7B PTB than ARB-RC. While this is an interesting observation, the paper already acknowledges the relationship is not straightforward, and this does not rise to a standalone weakness.
- **"Selectively dismissing PTB" claim exaggerated:** The Harsh Critic claimed the paper treats PTB as valid for OPT but dismisses it for LLaMA. In reality, the paper reports PTB numbers for all models and methods without comment for OPT, and only dismisses the specific LLaMA-2-7B case where *all* methods produce pathological numbers (BiLLM: 5243, PB-LLM: 657, ARB-RC: 763). The core weakness remains (the paper's method is worse than baselines on this setting), but the "selective dismissal" framing overstates the issue. The retained major weakness reflects the actual problem.

## Novel Insights
The paper's diagnostic finding that layer-wise output matching (ARB-X) can *increase* block-level loss relative to simple weight matching (ARB) despite reducing layer-level loss (Fig. 1) is genuinely counterintuitive and worth documenting. The architectural sensitivity finding — that output alignment degrades attention patterns far more severely in RMSNorm-based architectures (LLaMA) than LayerNorm-based ones (OPT) — provides a concrete mechanistic hypothesis that could inform future quantization work beyond this paper.

## Suggestions
- Investigate and explain the LLaMA-2-7B PTB failure mode. Is AMP over-correcting? Does the output-error objective become numerically unstable on PTB's distribution for LLaMA architectures? A failure analysis would transform this from a liability into a finding.
- Compare the current product-based AMP objective (Eq. 9) against a difference-based formulation in an ablation. If the product form is indeed superior, provide theoretical or empirical justification.
- Calibrate the "consistently outperforms" language to acknowledge the PTB exception transparently and the modest gains on larger models for downstream tasks.
- Replicate at least one diagnostic analysis (e.g., Fig. 1 or Fig. 2) on an OPT model to support the claimed generality of the motivating insights.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>