Now I have all the evidence I need. Let me compile the final review.

## Summary

This paper proposes Quantized Zeroth-order Optimization (QZO), which fine-tunes quantized LLMs by perturbing the *continuous quantization scales* (∆) rather than the discrete integer weights. This eliminates gradients and optimizer states (via ZO) while compressing weights to 4-bit or 2-bit (via PTQ), achieving peak memory of ~5 GB for a 7B model — about 3× less than MeZO (the ZO baseline on 16-bit models) and up to 18× less than full-precision AdamW fine-tuning. Experiments on OPT-6.7B, Llama-2-7B, Llama-3.1-8B, and Llama-2-13B across five NLP tasks show that QZO is competitive with MeZO on most tasks despite operating on far lower precision, and a directional derivative clipping (DDC) technique stabilizes training that otherwise collapses.

## Strengths

- **Genuinely novel core idea.** Perturbing quantization scales rather than discrete weights for ZO gradient estimation is a clean solution to the discrete-vs-continuous mismatch that arises in quantized models. The paper correctly identifies the problem (SPSA cannot perturb integer weights) and proposes a principled alternative that re-uses the existing quantization infrastructure. This idea is simple, transferable to both scalar-based (GPTQ) and codebook-based (AQLM) quantization, and is clearly explained in Section 3.2.1.

- **Demonstrated and significant memory savings.** Figure 1 and Table 1 show concrete peak-memory numbers across three model families: QZO (4-bit) uses 4.8–6.3 GB versus 14.8–20.5 GB for MeZO (16-bit) — a ~3× reduction on the directly relevant ZO baseline. The paper also reports the 18× figure against full-precision AdamW, which is a legitimate but different comparison point. The practical impact is underscored by fine-tuning Llama-2-13B (2-bit) on a single 24 GB GPU (Table 3).

- **Directional Derivative Clipping (DDC) is convincingly effective.** Figure 2 shows that without DDC the training collapses to NaN within 22 steps, while with DDC it remains stable for 1,000+ steps. The sensitivity analysis in Figure 3 shows that performance is stable for C ≥ 75, providing practical guidance. The theoretical claim of unbiasedness (Theorem 1) is appropriate, and the variance-reduction reasoning, while having a minor notation imprecision, is conceptually sound: pointwise reduction in |d| leads to reduced second moment, and unbiasedness then implies reduced variance.

- **Broad evaluation.** The method is tested on three 7B-scale model families (OPT, Llama-2, Llama-3.1) and a 13B model, across five tasks spanning classification (SST-2, RTE, CB, BoolQ) and generation (SQuAD), using two different quantization schemes (GPTQ 4-bit, AQLM 2-bit). Training statistics in Table 2 (parameter count, FLOPs) provide useful complementary efficiency measures.

## Weaknesses

### Fatal
None.

### Major
- **"On par with MeZO" claim is slightly overbroad.** While QZO is competitive with MeZO on most of the 15 task–model combinations, there are notable gaps. On Llama-3.1-8B, CB drops from 91.1 (MeZO) to 69.6 (QZO), and BoolQ drops from 83.4 to 78.2. On OPT-6.7B SST-2, the gap is 93.0 vs. 87.6. The paper's abstract and conclusion state "performs on par with MeZO" without qualification, and the body text says "on most datasets, QZO performs on par with MeZO" (line 258). The latter is accurate, but the former over-generalizes. The paper should acknowledge the specific tasks where QZO underperforms and discuss why (e.g., CB is a small dataset where higher variance in ZO estimates may be more damaging when combined with quantization noise).

- **Missing comparison to QLoRA / adapter-based fine-tuning of quantized models.** QLoRA (Dettmers et al., 2023) is cited in the references but never discussed as an alternative approach for fine-tuning quantized models. QLoRA fine-tunes 4-bit models using low-rank adapters with backpropagation, achieving a different point in the memory–performance trade-off space. A comparison — even if only in a brief discussion with cited memory figures — would help readers understand when QZO is preferable (no backward pass, single-stage pipeline) versus when QLoRA may be better (higher performance ceiling, widely adopted). The related work section discusses "memory-efficient training" and "LLM quantization" as separate areas without connecting them to QLoRA-style approaches, which are the most practically relevant alternative.

### Minor
- **No statistical significance / repeatability for ZO stochasticity.** Zeroth-order methods are inherently stochastic (random perturbation vector z). The paper reports only single-run results without standard deviations or multiple seeds. Given that ZO gradient estimates have high variance, confidence intervals across 3–5 seeds would substantially strengthen the evidence, particularly for the smaller datasets (CB, RTE) where the gap between QZO and MeZO is within a few points.
- **Variance-reduction derivation has a notation imprecision.** Equation 8 writes Var[ĝ'] = E[‖ĝ'‖²] − E[‖ĝ'‖]², but the standard formula is Var[ĝ'] = E[‖ĝ'‖²] − ‖E[ĝ']‖². The subsequent substitution (∇L)² for E[‖ĝ'‖]² indicates the authors intended the latter. The conclusion (Var[ĝ'] ≤ Var[ĝ]) is correct given Theorem 1 and Eq. 7, but the derivation as written is technically sloppy.

### Trivial
- The paper writes "QZO w/ DDC can be seen as setting C to an infinitely large value" (paragraph after Figure 3), which is a writing error: QZO *with* DDC uses C=100, so the intended statement is about QZO *without* DDC.

## Nice-to-Haves

- Report training wall-clock time. ZO requires two forward passes per step; the paper reports FLOPs but not actual runtime, which would help practitioners understand the throughput trade-off.
- Test whether the clipping threshold C=100 transfers across diverse tasks/models beyond the one ablation (Llama-2-7B on SST-2).
- For the 2-bit experiments (Table 3), providing a MeZO baseline on the same quantized model (even if infeasible on a single GPU) would contextualize how much of the performance comes from the ZO optimization vs. the quantization.

## Removed Points

These points from the reviewers were checked against the paper and are not included as weaknesses:

- "The method does not fine-tune the quantized model; it fine-tunes only quantization scales." *Removed:* The paper is transparent about this (Section 3.2.1: "perturb the scaling component ∆ while keeping the discrete weights θ̄ fixed"), and adjusting ∆ changes the effective weights w = ∆ ⊙ w̄. The title "Fine-Tuning Quantized Neural Networks" is accurate.
- "18× memory reduction is cherry-picked against an irrelevant baseline." *Removed:* The paper clearly labels the comparison as "compared to full-parameter fine-tuning in 16 bits" (abstract, Figure 1). The 3× reduction over MeZO is also reported. Both comparisons are valid for different purposes.
- "Theoretical argument for DDC is not rigorous." *Removed:* The core logic is correct — pointwise d'² ≤ d² implies E[‖ĝ'‖²] ≤ E[‖ĝ‖²] (Eq. 7), and combining this with unbiasedness (Theorem 1) gives Var[ĝ'] ≤ Var[ĝ]. The only issue is a notation imprecision (E[‖ĝ'‖]² vs. ‖E[ĝ']‖²) that does not affect the conclusion.
- "Unified framework language is overstated." *Removed:* Standard phrasing; the paper does unify ZO and quantization in a single optimization procedure.
- "SGD as upper-bound is a weak baseline." *Removed:* The paper discloses this limitation in a footnote and explains it is due to budget constraints.
- "Missing comparison to QLoRA" from the section-by-section notes of the harsh critic. *Kept* as a Major weakness, as explained above, because it is a genuine gap in contextualizing the contribution.

## Novel Insights

The reviews do not surface any observation about the paper that goes beyond what the paper itself asserts. The core insight — that one can perturb quantization scales rather than discrete integer weights to enable ZO fine-tuning — is the paper's own contribution, and the reviews essentially confirm this finding.

## Suggestions

1. Qualify the "on par with MeZO" claim explicitly. Add a sentence in the abstract and conclusion noting that "QZO achieves competitive performance on most tasks, with notable gaps on 2 of 15 settings (Llama-3.1-8B on CB and BoolQ)."
2. Add a discussion of QLoRA and similar methods (e.g., LoRA-FA, GPTQ-LoRA) to the related work, and ideally a quantitative comparison (memory, performance) in the main experiments or the appendix.
3. Repeat the main experiments (at least SST-2 and SQuAD for each model) with 3–5 random seeds and report means and standard deviations.
4. Fix the notation in Eq. 8 to use ‖E[ĝ']‖² instead of E[‖ĝ'‖]².
5. Add wall-clock training time to Table 2.

## Score and Decision

### Calibration details

**Round 1 (bracketing):** Queried three bands for ZO/quantized fine-tuning papers.
- Low band (score < 3.5): Anchors scored 2.50–3.00 — rejected ZO fine-tuning papers with fundamental flaws (missing baselines, irreproducible results, flawed methodology). QZO is clearly stronger.
- Middle band (3.5–7.5): Anchors scored 3.60–6.00 — including FZOO (5.0, poster), a ZO-only paper with a less novel contribution but broader convergence theory, and CoA-LoRA (5.5, poster), a quantized fine-tuning paper with limited LLM experiments.
- High band (7.5+): Anchors scored 8.00 — on completely different topics (not comparable).

Initial bracket: between 4 and 7, likely between 5 and 6.

**Round 2 (narrowing):** Queried the 4.5–6.5 and 5.0–7.5 bands.
- Read FZOO (5.0, poster): ZO optimization only, no quantization. QZO has a more novel core idea (scale perturbation) and comparable experimental rigor → QZO is slightly stronger.
- Read CoA-LoRA (5.5, poster): Quantized fine-tuning with adapters. CoA-LoRA was critiqued for limited true LLM experiments. QZO experiments on 7B–13B LLMs are more compelling → comparable.
- Read Optimizers Under Quantization (5.33, poster): Empirical study on smaller models. Different genre.

Final calibration: QZO sits between FZOO (5.0, poster) and the upper edge of CoA-LoRA (5.5, poster). Its novel core idea and solid empirical validation on true LLMs justify a score above 5.0, but the overclaiming and missing QLoRA comparison prevent it from reaching 6.0.

**Anchors consulted:**
- bR32fsXLbf (3.00, reject): DASP paper; lower-quality ZO fine-tuning → QZO is stronger
- tmTpi5swZ7 (2.67, withdrawn): P-GAP paper; had reproducibility issues → QZO is stronger
- NMlF3YjS8E (5.00, poster): FZOO paper; ZO-only, less novel core idea → QZO is slightly stronger
- 9OUg0nJE72 (5.50, poster): CoA-LoRA; quantized fine-tuning, good but limited LLM experiments → comparable
- mVldAuDAn5 (5.33, poster): Optimizer–quantization study; different genre → not directly comparable
- jMzXLsHdnF (5.20, reject): Forward-only Hessian-free CD; rejected → QZO is stronger
- 2Dn4yHYLQJ (3.60, reject): Learned ZO optimizer; rejected → QZO is stronger

**Final score: 5.5**

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Accept</decision>