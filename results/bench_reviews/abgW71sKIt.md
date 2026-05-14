Now I have a thorough understanding of the paper. Let me write the final consolidated review.

---

## Summary

This paper investigates why output-matching objectives fail in 1-bit post-training quantization (PTQ) of LLMs. Through empirical analysis, it identifies three failure modes: (i) layer-wise output matching can increase block-level loss, (ii) activation-conditioned error accumulates and drifts from the true target, and (iii) naive output alignment degrades token-similarity structure in attention. Based on these findings, the paper proposes a method that (a) uses true output error instead of activation-conditioned error, (b) restricts output alignment to the final FC layer of each transformer block, and (c) introduces an Attention Matrix Preservation (AMP) mechanism to protect token-similarity structure during optimization. The method consistently outperforms existing 1-bit PTQ baselines across OPT (1.3B–30B), LLaMA-2, and LLaMA-3 models on perplexity and zero-shot QA.

## Strengths

- **Thorough preliminary analysis grounding the method design.** The paper presents controlled experiments showing: (i) ARB-X's layer-wise output matching can produce higher block-level loss than weight-matching ARB (Fig. 1); (ii) activation-conditioned error drifts increasingly from the true output error with depth (Fig. 2, top); and (iii) token-similarity matrices degrade under naive output alignment (Fig. 2, bottom). These observations provide a clear, actionable diagnosis that directly motivates each component of the proposed method.

- **Consistent and substantial empirical improvements across model families and scales.** On OPT models (1.3B–30B), the method reduces perplexity by up to 4.85 PPL on C4 and 3.42 on WikiText-2 compared to the strongest baseline ARB-X (Table 1). On LLaMA-2 and LLaMA-3, it achieves 0.22–2.22 PPL drops (Table 2) and consistent zero-shot QA gains (Table 7). The improvements span model families, scales, and evaluation benchmarks, providing robust evidence of superiority.

- **Well-designed ablations that validate each design choice.** Switching from activation-conditioned error to true output error alone yields a 0.7 PPL improvement (Table 4). Removing AMP causes severe degradation (Table 3 text: >10 PPL increase on LLaMA-2-7B). Layer-wise ablation (Table 5) justifies the choice of the final FC layer for output alignment. These controlled experiments isolate the contribution of each component.

- **No additional inference or storage overhead.** The method uses the same diag(αr)·B·diag(αc) parameterization as ARB-RC, inheriting its efficiency. Quantization overhead is modest (~73 minutes for LLaMA-2-7B) and is a one-time cost (Table 6, Appendix D).

## Weaknesses

### Fatal

None.

### Major

None.

### Minor

- **The AMP update rule (Eqs. 10–11) is mathematically imprecise.** The mask M is defined as the sign of a gradient, yielding entries in {−1, +1}. In the update αr ← αr·(1−M^r) + αr*·M^r, when M = −1 this becomes αr ← 2αr − αr*, which pushes the parameter away from the optimal solution — an effect with no clear motivation. The authors likely intend a binary gate (keep vs. update), which would require a mapping like M_binary = (sign(·)+1)/2. The high-level intent is clear and the algorithm listing (Algorithm 1) confirms the intended behavior, but the mathematical presentation needs correction. This is a fixable notation issue, not a threat to the core claims.

- **No comparison to joint block-level output reconstruction.** The paper restricts output alignment to the final FC layer and justifies this with a per-layer ablation (Table 5). However, it does not compare this design against jointly optimizing all layers within a block for block-level output reconstruction. While the per-layer ablation is reasonable, a joint block-level baseline would more definitively validate the selective-layer strategy.

- **Attention pattern preservation is only measured via a token-similarity proxy, not directly.** Section 3.3 uses token-similarity matrices (cosine similarity between token representations) as a proxy for attention patterns, and AMP is designed to preserve these. However, no direct measurement of actual attention weights (e.g., KL divergence between full-precision and quantized softmax attention distributions) is provided to confirm that preserving token-similarity matrices translates to preserving attention behavior. This weakens the causal link between AMP and its claimed benefit.

### Trivial

- No error bars, standard deviations, or multiple-seed evaluation are reported for any result, making it difficult to assess the statistical significance of reported gains.
- No convergence analysis is provided for the alternating optimization procedure (Algorithm 1) that interleaves refinement steps with AMP masking.
- The "mod k" condition in Algorithm 1 (αc updated only every k iterations) is justified only by a brief ablation (Table 8) but not motivated by any principled reasoning.

## Nice-to-Haves

- A comparison against joint block-level output reconstruction (as mentioned in Minor Weaknesses) would strengthen the selective-layer claim.
- Direct visualizations of quantized vs. full-precision attention maps (softmax weights), not just token-similarity matrices, would make the AMP motivation more concrete.
- Evaluation beyond the 1-bit regime (e.g., 2-bit) would demonstrate the generality of the approach.

## Removed Points

*These points were flagged by reviewers but are not valid weaknesses. Treat them with caution.*

1. **Table 3 missing numerical values (Harsh Critic, Issue 2).** The table cells in the PDF extraction are empty, but the surrounding text explicitly states the finding: "LLaMA suffers severe degradation, with perplexity increasing by over 10 points." This is a parser artifact — the original submission contains these numbers. Not a paper weakness.

2. **Bit-width control / unfair comparison with PB-LLM (Harsh Critic, Issue 3).** PB-LLM uses 1.7 bits vs. 1.06 bits for the proposed method. This asymmetry *favors the baseline* — PB-LLM gets more representational capacity and still performs worse. Per the review guidelines, comparisons favoring the baseline are not considered unfair.

3. **Missing baselines: BRECQ, GPTQ (Harsh Critic, Issue 3).** GPTQ and BRECQ are general-purpose PTQ methods not designed for 1-bit quantization. The paper compares against the standard 1-bit PTQ baselines (BiLLM, PB-LLM, ARB-RC, ARB-X). Demanding non-1-bit baselines is scope creep.

4. **"The introduction oversells" / Section 3.1 analysis from a single method (Harsh Critic, Section-by-Section).** The preliminary analysis uses ARB/ARB-X as representative methods for weight/output alignment. This is standard practice for diagnostic analysis — testing one strong representative of each paradigm is sufficient to motivate the problem. The analysis is not claimed to be exhaustive.

5. **Section 3.3 token-similarity link "asserted, not demonstrated" (Harsh Critic).** The paper explicitly frames token-similarity matrices as a *proxy* and acknowledges this limitation (Section 3.3). This is noted as a minor weakness above (lack of direct attention measurement), but the claim is not overstated.

6. **PDF parser artifacts in Tables 1–2 format.** The garbled table formatting is a parser issue. The original submission has properly formatted tables.

7. **References to Appendices D and E for overhead/algorithm details.** The parser strips appendices; these sections exist in the original submission. This is not a paper weakness.

## Novel Insights

The paper's most genuinely novel insight is the *architecture-dependent* sensitivity to output alignment: LLaMA models (using RMSNorm) suffer far more attention degradation from naive output matching than OPT models (using LayerNorm), because RMSNorm's unit-norm normalization makes the model more dependent on directional alignment of representations. This observation (Section 5.3, Table 3) explains *why* attention preservation is critical for some architectures but less so for others, and it provides a concrete hypothesis grounded in architectural differences rather than generic hand-waving about "attention is important."

## Suggestions

- **Fix the AMP masking formulation.** Replace the sign-based mask with a proper binary gate: e.g., define M_binary = (sign(∇L_AMP) + 1)/2, then use αr ← αr·(1−M_binary) + αr*·M_binary. This preserves the intended behavior (keep vs. update based on gradient sign) while making the math correct.
- **Add a footnote or brief discussion** acknowledging that the token-similarity matrix is a proxy for attention behavior, and note the relationship (or lack thereof) to actual softmax attention weights.
- **Run one model with 3 seeds** and report mean ± std for perplexity to address the reproducibility concern. Even a single model would be sufficient.

## Score and Decision

**Anchor comparison:**

| Path | Avg Score | Comparison |
|------|-----------|------------|
| `QpbtT95S95` | 6.00 | QAT scaling laws paper — more theoretically ambitious with broader implications. Our paper is narrower in scope but well-executed within that scope. |
| `ZXr3Xx7Z1O` | 5.50 | Empirical analysis of training dynamics and PTQ robustness. Similar contribution type (empirical insights + practical recommendations). Our paper additionally provides a concrete method with strong results. Comparable quality. |
| `7QZanjCD6M` | 4.50 | Ternarization PTQ method. Similar paper type with multiple design components. Our paper has more thorough preliminary analysis and stronger ablations. |
| `BE2GrBKAwD` | 4.00 | Function-preserving transforms for quantization. Our paper has clearer motivation from failure analysis and better empirical validation. |
| `Ra5rXQvuFP` | 4.00 | DBellQuant — another binarization method. Our paper is stronger in analysis depth and result quality. |
| `Urt7MPg1u0` | 4.00 | 1-bit optimization from pre-trained LLMs. Our paper is more clearly motivated and better evaluated. |
| `giIsHqVQnF` | 2.50 | LiftUQ — claims of paradigm shift but reviewers found it incremental with missing baselines. Our paper is substantially stronger. |
| `YjMCArLE1r` | 2.00 | R2Q — 2-bit QAT method with significant methodological gaps. Our paper is far stronger. |
| `0mqsIlMtfm` | 3.00 | PTQTP — ternary PTQ. Our paper has better motivation and results. |

The paper's strengths (thorough empirical analysis, consistent results, well-motivated design) clearly outweigh its minor weaknesses (imprecise AMP notation, missing block-level baseline, proxy-based attention measurement). It sits above the 4.0–4.5 borderline and is comparable in contribution quality to the 5.50 anchor. I assign **5.5 — Accept (Poster)**.

MY FINAL SCORE: <pineapple>5.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>