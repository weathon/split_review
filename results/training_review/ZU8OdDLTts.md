Now I have all the information needed. Let me compose the final consolidated review.

## Summary

This paper proposes ARB-LLM, a family of 1-bit post-training quantization methods for LLMs built on an alternating refinement (ARB) framework that iteratively updates the binarization parameters (μ, α, B) to progressively align the distributions of binarized and full-precision weights. Two key extensions are introduced: ARB-X which leverages calibration data in the refinement, and ARB-RC which adds a column-wise scaling factor to address column-wise deviations in LLM weights. A refined column-group bitmap (CGB) strategy further improves performance. Experiments across OPT, LLaMA1/2/3, and Vicuna families show substantial perplexity reductions over the prior SOTA binary method BiLLM (e.g., LLaMA-7B: 49.79 → 14.03 on WikiText2).

## Strengths

- **Novel alternating refinement framework.** The ARB algorithm (iterative update of μ, α, B based on the residual) is a principled and well-motivated departure from one-shot binarization used in prior methods like BiLLM and PB-LLM. The theoretical guarantee that quantization error does not increase after τ iterations (Theorem 1) provides formal grounding absent in prior work.

- **Row-column scaling (ARB-RC) is well-motivated and effective.** The observation of column-wise deviations in LLM weights (Figure 2) is genuine, and the introduction of a column scaling factor α^c directly addresses this structural issue. ARB-LLM_RC achieves lower perplexity than BiLLM while also using less memory (2.63 GB vs. 2.93 GB for LLaMA-7B without CGB).

- **Comprehensive ablation study.** Tables 4a–f systematically isolate the contributions of each component (ARB vs. ARB-X vs. ARB-RC, CGB, iteration count, calibration set size, group number). For example, even ARB with 1 iteration (15.23 perplexity for ARB-LLM_RC) already dramatically outperforms BiLLM (49.79), showing the core framework is highly effective.

- **Significant perplexity improvements across multiple model families.** Tables 1–3 show ARB-LLM_RC reduces perplexity over BiLLM by up to ~72% on LLaMA-7B (49.79 → 14.03) and ~69% on OPT-6.7B (47.65 → 14.92) at the same bit-width (~1.1 bits). Results span OPT (1.3B–66B), LLaMA1/2/3 (7B–70B), and Vicuna, demonstrating broad applicability.

- **Memory advantage while improving accuracy.** ARB-LLM_RC without CGB uses 2.63 GB (vs. BiLLM's 2.93 GB) for LLaMA-7B while achieving substantially better perplexity, showing that row-column scaling is both more accurate and more compact.

## Weaknesses

### Fatal
None.

### Major

- **The claim of surpassing FP16 models on zero-shot QA is insufficiently supported.** The abstract, introduction, and conclusion prominently state that ARB-LLM_RC is "the first to surpass FP16 models of the same size." The only supporting evidence is Figure 3, which shows *averaged* accuracy over 7 QA datasets as a bar chart with no error bars, no per-task breakdowns, and no numerical values. Given that ARB-LLM_RC has 2–3× *higher* perplexity than FP16 (e.g., LLaMA-7B: FP16 5.68 → RC 14.03), the claimed QA superiority is counter-intuitive and the paper offers no discussion of this discrepancy. This is a significant overreach: without per-task numbers, variance estimates, and an explanation of how a model with much worse perplexity can surpass FP16 on QA, the headline claim is unverifiable. The paper's core technical contribution (improving over BiLLM) is strong enough to stand without this claim, and the authors should either provide rigorous supporting evidence or tone down the claim to "competitive with FP16" or "advancing the frontier of binary LLM performance."

### Minor

- **No discussion of the perplexity–QA accuracy discrepancy.** The paper shows ARB-LLM_RC has 2–3× higher perplexity than FP16 but claims to surpass FP16 on zero-shot QA. This pattern is unusual and deserves explicit analysis — e.g., is the perplexity metric less meaningful for binarized models? Are the QA tasks not perplexity-sensitive? The silence on this point weakens the paper's narrative coherence and leaves readers with a seemingly contradictory result.

- **Time overhead is substantial without clear justification of the practical trade-off.** ARB-LLM_RC with CGB takes 76 minutes vs. BiLLM's 45 minutes (~70% increase) for LLaMA-7B, while memory savings over BiLLM are modest (2.83 GB vs. 2.93 GB). The paper states this is "acceptable" but does not articulate the practical deployment scenario where the trade-off is worthwhile, especially since the perplexity improvement is large but still far from FP16 quality.

- **The speedup ratio in Theorem 2 is stated as proportional to 389× but the constant of proportionality is not derived.** The expression η ∝ 1/(k·(1/(nT) + 1/(BL))) gives the scaling behavior but not the actual factor. The claimed 389× is based on plugging in specific numerical values (n=4096, B=128, L=2048, T=15, k=128) but it is unclear what operations are counted and whether precomputation of S is included.

### Trivial

- **The L1 norm switch in Eq. 4 (line 187) for updating B₁, B₂ is not justified.** The main objective (Eq. 1) uses L2, but the binary search for B updates uses L1 without explanation. Since only 4 candidates exist the practical difference is likely small, but the rationale should be stated.

- **The CGB improvement, while real, is modest** (ARB-LLM_RC: 15.85 → 14.03 on WikiText2) and the paper could more clearly communicate the cost–benefit.

## Nice-to-Haves

- Per-task zero-shot QA accuracy results with error bars in a table (even if in supplementary) would significantly strengthen the paper.
- A plot of perplexity vs. ARB iteration count would make the convergence behavior concrete and help practitioners choose the right number of iterations.
- A footnote acknowledging that the FP16-surpassing claim refers specifically to zero-shot QA (not overall language modeling quality) would prevent misinterpretation.

## Removed Points

These points are flagged to be removed, treat them with caution:

- **"Theorem 1 proof is relegated to supplementary and not available"** — Removed per Hard Rules: missing appendix / deferred proofs are parser artifacts; the supplementary exists in the original submission.
- **"Pseudocode deferred to supplementary"** (multiple instances) — Removed per Hard Rules: same reason as above.
- **"Missing standard deviations / confidence intervals for perplexity is a weakness"** — Removed as a formatted weakness because single-run reporting is the standard in this field (the critic even concedes "This is common in the field but still a weakness"). However, the lack of error bars on the *zero-shot QA* figure (where a strong novelty claim rests) remains as a Major weakness.
- **"The decouple bitmap ablation showing complete failure without both bitmaps is trivial"** — Removed as a strawman; the authors present it as a sanity check, not a substantive result.
- **"Figure 1 shows only OPT-6.7B on QA while perplexity comparisons are omitted"** — Removed because Figure 1 is a teaser figure; the main results include both perplexity tables and full QA figures.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. **Tone down or properly qualify the FP16-surpassing claim.** Provide a supplementary table with per-task zero-shot QA accuracy, numerical values, and ideally variance estimates. Alternatively, reframe as "the first binary PTQ method to match or approach FP16 performance on zero-shot QA" — this is still a striking result and is better supported.

2. **Add a brief discussion of the perplexity–QA accuracy relationship.** Even a paragraph acknowledging that perplexity and downstream accuracy can diverge for heavily quantized models, and that the QA results suggest the binarization preserves task-relevant information despite higher perplexity, would address the current gap.

3. **Report the numerical QA accuracy values** in the main paper (or a clear pointer to the supplementary table) rather than only in a bar chart, so readers can verify the claim.

## Score and Decision

The paper makes a genuine technical contribution — the alternating refinement framework for binary LLM quantization is novel, well-motivated, and yields the largest perplexity improvements over prior binary PTQ methods. The ablations are thorough, the method is evaluated across multiple model families, and the core results (significantly outperforming BiLLM) are clearly and repeatedly demonstrated.

The most serious weakness is the overclaimed FP16-surpassing result, which is insufficiently supported and not reconciled with the perplexity evidence. However, this does not invalidate the paper's core contribution, which remains strong even if the FP16 claim is removed or qualified. The paper would benefit from toning down this claim or providing rigorous supporting evidence (per-task numbers with variance). The remaining issues (time overhead discussion, speedup ratio derivation, L1 justification) are minor and easily addressed.

**Recommendation: Accept** with mandatory revisions to either (a) provide rigorous per-task QA accuracy with variance estimates and discuss the perplexity–QA discrepancy, or (b) remove/qualify the FP16-surpassing claim to match the evidence level.

MY FINAL SCORE: <pineapple>7.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>