Now I have enough calibration data. Let me finalize the review.

**Round 1 Bracket**: The paper sits between 5.5 and 7.5 based on comparison with:
- Low band: EfficientQAT (3.00), PrefixQuant (3.00), LLM Compression with Convex Optimization (3.00) — the paper is clearly stronger than these
- Middle band: FlatQuant (5.20), LeanQuant (5.17), OmniQuant (6.40), OSTQuant (6.20), PB-LLM (6.75), ARB-LLM (7.00), LQ-LoRA (6.75) — the paper is comparable to PB-LLM and ARB-LLM
- High band: Scaling Laws for Precision (8.00), MoE++ (8.00) — the paper is clearly weaker than these

**Round 2 Narrowing**: Within the bracket (5.5–7.5), comparison with OmniQuant (6.40), PB-LLM (6.75), and ARB-LLM (7.00) places the paper at 6.5. The paper has a stronger analytical contribution than ARB-LLM (7.0) and OmniQuant (6.40), but the 3166 PPL issue and its dishonest handling hold it back.

**Final score: 6.5**

The paper's diagnostic analysis is genuinely novel and well-evidenced, and it provides consistent improvements over baselines in most settings. However, the 3166 PPL on LLaMA-2-7B/PTB is a significant failure that is handled poorly (dismissed rather than investigated), and the "consistently outperforms" claim in the abstract/conclusion is overclaimed. These issues prevent a higher score, but the paper's analytical contributions and strong results on OPT models keep it in the solid accept range.

---

## Summary
This paper investigates why naive output-matching objectives underperform weight-matching methods in 1-bit post-training quantization (PTQ) of LLMs. It identifies three failure modes—layer-wise alignment not guaranteeing block-level improvement, accumulated quantization error causing target drift, and disruption of token-to-token attention interactions—and proposes corresponding solutions: selective output alignment at the last FC layer, an output error objective using full-precision inputs, and an Attention Matrix Preservation (AMP) mechanism.

## Strengths
- **Systematic diagnostic analysis motivating each design choice**: Sections 3.1–3.3 present three targeted analyses on LLaMA-2-7B. Figure 1 shows across 223 layers that ARB-X's lower layer-level loss does not always translate to lower block-level loss. Figure 2 (upper panels) shows MSE relative to the full-precision output grows with depth even when activation-conditioned cosine similarity stays low. Figure 2 (bottom) shows token-similarity matrices drifting from the baseline. Each diagnostic directly motivates a corresponding method component (selective alignment, output error objective, AMP).
- **Consistent improvements on OPT models across all scales and benchmarks**: Table 1 shows outperformance over all baselines (PB-LLM, BiLLM, ARB-RC, ARB-X) across OPT-1.3B through OPT-30B on C4, WikiText2, PTB, and zero-shot QA. For example, C4 perplexity improves from 27.70 (ARB-RC) to 24.69 on OPT-1.3B.
- **AMP provides large, architecture-aware gains**: Table 3 shows AMP reduces LLaMA-2-7B C4 perplexity from 29.12 to 19.25 (~34% relative improvement), while its effect on OPT-6.7B is modest (16.35→16.22). The paper links this to architectural differences (RMSNorm vs. LayerNorm), demonstrating the mechanism adapts to model characteristics.
- **Well-designed ablation studies**: Tables 3–4 cleanly isolate the contributions of AMP and the output error objective, confirming each component's value under identical conditions.

## Weaknesses

### Fatal
None.

### Major
- **Catastrophic PPL on LLaMA-2-7B/PTB handled poorly**: Table 2 shows 3166 PPL for the proposed method on LLaMA-2-7B/PTB. While this beats BiLLM (5243.01), it is far worse than PB-LLM (657.24), ARB-RC (763.19), and ARB-X (681.24). The paper dismisses this at line 233 ("the large perplexity indicates that the metric cannot provide a meaningful evaluation"), which is self-serving when three other baselines achieve reasonable scores on the same metric. The abstract and conclusion both claim the method "consistently outperforms existing 1-bit PTQ methods" (lines 9, 269), which is contradicted by this entry. A PPL of 3166 indicates a failure mode—possibly related to AMP or the output error objective interacting badly with certain model/data combinations—that warrants investigation or honest acknowledgment.
- **STB-LLM cited but excluded from all comparison tables**: STB-LLM (Dong et al., 2024) is discussed in related work (line 38) as "achieving sub-1-bit average precision while maintaining accuracy" but is excluded from Tables 1–2 without explanation. This weakens the SOTA claims.

### Minor
- **Selective layer strategy lacks empirical justification**: Section 4.2 states output alignment is applied "only to the last fully connected layer of each block, since it has the most direct impact on the block loss." This is asserted without ablation comparing to alternatives. Given the paper's central thesis that *which* layers receive output alignment matters, this is a conspicuous omission.
- **Convergence criteria not specified**: Line 161 says "we jointly optimize all three variables until convergence" but does not specify convergence criteria, iteration counts, or sensitivity. Algorithm 1 is deferred to Appendix E (stripped by parser, likely present in the original).

### Trivial
None.

## Nice-to-Haves
- Computational cost / quantization time comparisons would strengthen practical claims (likely in Appendix D, stripped by parser).
- Investigating the LLaMA-2-7B/PTB failure mode would significantly strengthen the paper.

## Removed Points
These points are flagged to be removed, treat them with caution:
- **Equation (2) typo** (||X̂Ŵ − X̂Ŵ||²): Almost certainly a PDF parser artifact, not an author error. The original LaTeX likely reads ||X̂W − X̂Ŵ||².
- **Missing Appendix content**: Appendix B (derivations), D (overhead analysis), E (Algorithm 1), and other appendices are stripped by the parser. The authors likely address convergence criteria and overhead there.

## Novel Insights
The paper's three-part diagnostic framework (layer-vs-block mismatch, accumulated error drift, attention degradation) is genuinely novel and well-evidenced. The observation that AMP's effectiveness correlates with RMSNorm vs. LayerNorm architecture is an insightful finding that could guide future quantization-aware design. These analytical contributions go beyond incremental method improvement and provide reusable insights for the field.

## Suggestions
- Investigate and honestly report the LLaMA-2-7B/PTB failure—either fix the underlying issue or acknowledge the limitation explicitly. Revise the abstract/conclusion to say "outperforms across most settings" rather than "consistently outperforms."
- Include STB-LLM in comparison tables or explain its exclusion (e.g., different comparison setting due to sub-1-bit precision with added kernel/storage costs).
- Ablate the selective layer choice (last FC vs. other layers) to justify this core design decision.
- Consider presenting AMP token similarity analysis in the main text rather than appendix, given it is the most novel technical component.

## Calibration Report

### Anchors Retrieved

| Round | Paper Path | Avg Human Score | Comparison |
|-------|-----------|----------------|------------|
| 1 | Ternary Language Models (TriLMs) | 2.86 | Weaker — pretraining-focused, different setting |
| 1 | EfficientQAT | 3.00 | Weaker — QAT approach, rejected |
| 1 | PrefixQuant | 3.00 | Weaker — activation quantization focus, rejected |
| 1 | LLM Compression with Convex Optimization | 3.00 | Weaker — different framework, rejected |
| 1 | PB-LLM | 6.75 | Similar — first binarization for LLMs, limited novelty but solid |
| 1 | ARB-LLM | 7.00 | Similar — extends BiLLM with alternating refined binarization; this paper builds on it with stronger analysis |
| 1 | STBLLM | 6.00 | Comparable — sub-1-bit binarization, different approach |
| 1 | QRazor | 5.20 | Weaker — 4-bit quantization, different setting |
| 1 | Scaling Laws for Precision | 8.00 | Stronger — foundational scaling law work |
| 2 | OmniQuant | 6.40 | Comparable — learnable quantization, good experiments but limited novelty |
| 2 | FlatQuant | 5.20 | Weaker — rejected, less comprehensive |
| 2 | LeanQuant | 5.17 | Weaker — less analytical depth |
| 2 | OSTQuant | 6.20 | Comparable — distribution transformation for quantization |
| 2 | LQ-LoRA | 6.75 | Similar — low-rank + quantized decomposition |
| 1 | MoE++ | 8.00 | Stronger — different domain, higher impact |

### Round 1 Bracket: 5.5–7.5
The paper is clearly stronger than the low-band anchors (3.0–3.0) and clearly weaker than the high-band anchors (8.0). It sits among the middle-band quantization papers.

### Round 2 Narrowing: 6.0–7.0
Compared to OmniQuant (6.40), this paper has stronger analytical motivation. Compared to ARB-LLM (7.00), it has a stronger diagnostic contribution but the 3166 PPL issue and overclaimed "consistently outperforms" prevent it from matching ARB-LLM's score. The paper lands at 6.5—comparable to PB-LLM (6.75) and slightly below ARB-LLM (7.00), reflecting strong contributions tempered by a visible failure case with poor handling.

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>