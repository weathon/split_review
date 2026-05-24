Now I have all the information needed. Let me synthesize the final review.

**Calibration summary:**

**Round 1 bracket** (wide): Between 3.5 and 7.5. Anchors: weak band (avg 2.0–3.2: poor papers with fatal gaps), middle band (avg 4.0–6.4: DBellQuant reject 4.0, PT²-LLM accept poster 4.5, Quant-dLLM accept poster 6.4), strong band (avg 8.0: not topically comparable — transducing LMs, multi-turn conversation, etc.).

**Round 2 narrowing**: Queried (3.5, 5.5) and (5.5, 7.0). Read the full reviews for Urt7MPg1u0 (Rethinking 1-bit Optimization, 4.0, Reject), Ra5rXQvuFP (DBellQuant, 4.0, Reject), 7QZanjCD6M (PT²-LLM, 4.5, Accept Poster), hsgl5Owiio (BitNet Distillation, 4.67, Reject), and HD7tuVakmR (Quant-dLLM, 6.4, Accept Poster).

**Comparisons**: This paper is **better** than DBellQuant (4.0) — its analysis (Section 3) is a genuine diagnostic contribution, its closed-form derivations are well-specified, and its evaluation is broader. It is **comparable to slightly better than** PT²-LLM (4.5) and BitNet Distillation (4.67) — those papers were criticized for weak novelty and missing baselines, whereas this paper offers real insight into why output alignment fails. It is **worse** than Quant-dLLM (6.4) — that paper had a clearer motivation tied to a domain-specific gap, cleaner methodology, and stronger evaluation. The AMP sign ambiguity and unexplained PTB failure prevent this paper from reaching that tier.

**Final score: 5.0** — solid borderline paper with real contributions and fixable problems.

---

## Summary

This paper studies why naive layer-wise output alignment fails in 1-bit post-training quantization of LLMs. The diagnostic analysis (Section 3) identifies three failure modes: (i) reducing layer-level loss does not guarantee block-level loss reduction, (ii) quantization errors accumulate across layers as the target shifts, and (iii) indiscriminate output matching degrades token similarity structure, harming attention. Based on these insights, the paper proposes a method that replaces the activation-conditioned error with the true output error (using full-precision targets), applies output alignment selectively (only to the last FFN layer of each block), and introduces Attention Matrix Preservation (AMP) to mask updates that would degrade token similarity. Experiments on OPT (1.3B–30B) and LLaMA-2/3 (7B–13B) show consistent perplexity improvements over prior 1-bit PTQ methods across most settings.

## Strengths

- **Diagnostic analysis of output alignment failure (Section 3) is a genuine contribution.** Figure 1 shows that reducing layer-wise error through output matching does not reliably reduce block-level loss — several layers under ARB-X have *higher* block loss than the simpler weight-aligned ARB baseline. Figure 2 measures how the activation-conditioned error diverges from the true output error as depth increases, providing concrete evidence of error accumulation. This analysis stands independently of the proposed method and advances understanding of 1-bit PTQ.

- **The output error formulation is principled and well-motivated.** Equation (3) replaces the activation-conditioned objective \(\|\hat{X}W - \hat{X}\hat{W}\|\) with the true output error \(\|XW - \hat{X}\hat{W}\|\), directly addressing error accumulation. The closed-form derivations for \(\alpha_c^*\), \(B^*\), and \(\alpha_r^*\) (Equations 5–8) are provided with clear algebra, and the use of `torch.linalg.lstsq` for numerical stability shows practical care.

- **AMP ablation shows large, architecture-dependent effects.** Table 3 demonstrates that AMP improves LLaMA-2-7B perplexity from 29.12 → 19.25 on C4 (a ~10 point gain), while helping OPT-6.7B more modestly (16.35 → 16.22). This validates the paper's claim that output alignment degrades attention in RMSNorm-based architectures and that AMP mitigates it.

- **Consistent improvements across most model-dataset pairs.** On OPT models (Table 1), the method outperforms ARB-RC, ARB-X, BiLLM, and PB-LLM on C4, WikiText2, PTB, and zero-shot QA. On LLaMA models (Table 2), it outperforms on C4, WikiText2, and (except for one case) PTB. Gains reach up to 4.85 PPL on OPT-1.3B C4 relative to ARB-RC.

## Weaknesses

### Major

- **AMP update rule (Equations 10–11) is mathematically ambiguous.** The AMP masks \(M^r, M^c, M^B\) are defined as the sign of the gradient, which returns values in \(\{-1, 1\}\). The update rule \(\alpha_r = \alpha_r \cdot (1 - M^r) + \alpha_r^* \cdot M^r\) then produces: when \(M^r = 1\), \(\alpha_r = \alpha_r^*\) (take the closed-form); when \(M^r = -1\), \(\alpha_r = 2\alpha_r - \alpha_r^*\). The latter case pushes the parameter away from both the current value and the closed-form optimum — a mathematically unusual operation with no clear interpretation as an attention preservation mechanism. If the intent is a binary mask in \(\{0, 1\}\), then taking sign of the gradient does not produce that. The paper must clarify what range the masks take, justify the negative-case update geometrically, or reformulate the masking. This ambiguity undermines reproducibility of the core claimed improvement.

- **Unexplained failure on LLaMA-2-7B / PTB (PPL 3166 vs. ARB-RC 763).** Table 2 shows that on PTB, the proposed method achieves perplexity 3166 for LLaMA-2-7B — worse than ARB-RC (763), ARB-X (681), and even PB-LLM (657). The paper dismisses this with "the large perplexity indicates that the metric cannot provide a meaningful evaluation," but this is not an explanation. Other methods produce meaningful numbers (albeit high) on the same metric; the proposed method's 4× worse result is a real failure that directly contradicts the blanket claim of "consistently outperforms." The lack of any analysis (controlled ablation on this setting, investigation of AMP vs. no-AMP on PTB, etc.) is a significant gap. For LLaMA-2-13B on PTB, the method (196.64) is also behind ARB-X (182.10), showing the issue is not confined to 7B.

### Minor

- **Selective layer strategy is unablated.** The paper restricts output alignment to "the last fully connected layer of each block" with the justification "since it has the most direct impact on the block loss." No ablation compares this choice against alternatives (e.g., first FC layer, attention layers, all layers, or a data-driven selection). Given that the paper's own analysis (Section 3.1) shows that some layers are harmful to block loss when output-aligned, the specific selection mechanism is a key design decision that needs empirical support.

- **Improvements over ARB-RC are modest on larger models.** For OPT-30B, the gain on C4 is 13.34 → 13.15 (0.19 PPL) and on zero-shot QA it is 57.11 → 57.70 (+0.59%). While consistent, these margins raise the question of whether the added complexity (pseudoinverse least-squares, alternating optimization, AMP masking, selective application) represents a practical net advance over the simpler weight-alignment baseline at larger scales.

### Trivial

- **Notation issue in Equation (9):** The AMP objective is written as \(\| (\hat{X}\hat{W}\hat{W}^\top\hat{X}^\top) \odot (XWW^\top X^\top) \|\) which suggests a Frobenius norm of the Hadamard product, but the next line clarifies the actual computation is the trace of the product (Frobenius inner product). These are different quantities unless all entries are nonnegative. The notation should be consistent.

## Nice-to-Haves

- An ablation comparing the selective layer strategy (last FC vs. other choices) would strengthen the paper considerably.  
- A controlled experiment on the PTB LLaMA-2-7B failure — varying AMP on/off, selective layer choices — to diagnose whether the issue lies in attention preservation or the output error objective itself.  
- Reporting wall-clock overhead for the alternating closed-form optimization compared to ARB-RC (currently only in the appendix) would help practitioners assess the practical cost.  
- The AMP hypothesis about RMSNorm vs. LayerNorm could be tested more rigorously by applying AMP to OPT models (LayerNorm) with a controlled variation.

## Removed Points

- *Criticism that AMP Objective (Eq 9) is "written as a norm, which is ambiguous"* — The second line clarifies it as a trace; the notation is not ideally precise but understandable. Downgraded from the harsh critic's severity to a Trivial notation point.
- *Criticism about "no analysis of convergence or sensitivity" of the pseudoinverse* — The paper explicitly notes using `torch.linalg.lstsq` for stability, which is standard practice. This is a reproducibility nitpick beyond normal expectations for a PTQ paper.
- *Strength Finder's generic strengths about "important problem" or "clear writing" * — Removed as non-specific. Strength Finder's concrete, evidence-backed strengths are retained.

## Novel Insights

None beyond the paper's own contributions. The diagnostic analysis in Section 3 is itself the most insightful part of the paper — the finding that layer-wise output matching can *increase* block-level loss, and that error accumulation shifts the optimization target, is a genuinely useful observation for the 1-bit PTQ community. The AMP mechanism's large effect on LLaMA versus OPT is suggestive of an architectural interaction (RMSNorm vs. LayerNorm) that would be worth investigating further but is not conclusively proven here.

## Suggestions

1. **Clarify the AMP masks.** Specify the range of \(M^r, M^c, M^B\) (are they \(\{0,1\}\) or \(\{-1,1\}\)?) and justify the update rule's behavior when the mask is negative. If the masks are binary \(\{0,1\}\), replace sign with an indicator function \(\mathbf{1}_{>0}\). If they are \(\{-1,1\}\), explain the geometric meaning of the \(2\alpha_r - \alpha_r^*\) case.
2. **Diagnose the PTB LLaMA-2-7B failure.** Add an ablation varying AMP on/off and the selective layer strategy on this specific setting. If the metric is genuinely unstable for this model-dataset combination, show evidence (e.g., variance across calibration seeds) rather than dismissing the result.
3. **Add an ablation on the selective layer strategy.** Compare output-aligning the last FC vs. first FC vs. all layers vs. attention layers within each block for at least one model.
4. **Tone down "consistently outperforms"** to "generally outperforms" or add a clarifying note about the PTB exception in the abstract and conclusion.

## Score and Decision

Round 1 bracket: 3.5–7.5 (wide bracketing using three topical queries across the score range).  
Round 2 narrowing: 4.0–5.5 (comparison against DBellQuant 4.0, PT²-LLM 4.5, BitNet Distillation 4.67, Quant-dLLM 6.4).  
The paper is above the 4.0 reject-level papers (DBellQuant, Rethinking 1-bit Optimization) due to genuine diagnostic contributions and broader evaluation. It is comparable to PT²-LLM (4.5, accepted poster) but held back by the AMP sign ambiguity and the unexplained PTB failure — issues that are fixable but real. It is below Quant-dLLM (6.4) which had cleaner methodology and a stronger evaluation for its niche.  
Final score: **5.0**.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Accept</decision>