Now I have a thorough understanding of the paper. Let me produce the final consolidated review.

---

## Summary

This paper studies why naive layer-wise output alignment fails for 1-bit post-training quantization of LLMs. Through diagnostic experiments, it identifies three failure modes: (1) layer-wise output minimization does not guarantee block-level loss reduction, (2) quantization errors accumulate across layers under activation-conditioned alignment, and (3) output alignment can degrade token-similarity matrices that drive attention. The paper then proposes a selective output-alignment strategy (applied only to the last fully-connected layer of each transformer block) paired with an Attention Matrix Preservation (AMP) mechanism that uses gradient-sign masking to preserve attention structure. Experiments on OPT (1.3B–30B), LLaMA-2 (7B, 13B), and LLaMA-3 (8B) show perplexity and zero-shot QA improvements over prior 1-bit PTQ methods on most benchmarks.

## Strengths

1. **Section 3's diagnostic analysis is a genuine contribution.** Figure 1 demonstrates concretely that minimizing layer-level output error can *increase* block-level loss for many layers, directly challenging the assumption of prior output-matching methods. Figure 2 (top) shows that under ARB-X, MSE relative to the true full-precision output grows with depth while cosine similarity stays high — a clear articulation of error accumulation that motivates the paper's shift to a direct Output Error objective (Eq. 3). Figure 2 (bottom) quantifies drift in token-similarity matrices, linking output alignment to attention degradation. These analyses are well-executed and provide value independent of the proposed method.

2. **The method consistently outperforms prior 1-bit PTQ methods across most settings.** On OPT models (Table 1), the method achieves the best perplexity on C4, WikiText2, and PTB across all five model sizes (e.g., OPT-1.3B C4: 24.69 vs. next-best ARB-RC 27.70). On LLaMA models (Table 2), the method is best on C4 and WikiText2 for both 7B and 13B (e.g., LLaMA-2-7B C4: 19.25 vs. ARB-RC 20.4). Zero-shot QA accuracy also improves, though margins are small.

3. **Ablation confirms that both the Output Error objective and AMP are essential.** Table 4 shows that replacing the proposed Output Error with Activation-conditioned Error increases perplexity (LLaMA-2-7B C4: 19.25 → 19.97). Table 3 shows that removing AMP causes a catastrophic 10‑point PPL increase on LLaMA-2-7B (19.25 → 29.12), confirming both the attention-degradation diagnosis and the effectiveness of the cure.

4. **Closed-form optimization makes the method tractable.** Equations (5), (6), and (8) provide non-iterative updates for the binarization parameters under the Output Error objective, avoiding expensive gradient steps during quantization.

5. **Evaluation spans multiple model families and scales.** Experiments cover OPT (1.3B–30B), LLaMA-2 (7B, 13B), and LLaMA-3 (8B) across three language modeling benchmarks and seven zero-shot QA datasets, demonstrating generalization beyond a single architecture.

## Weaknesses

### Fatal

None.

### Major

1. **The catastrophic failure on LLaMA-2-7B / PTB (PPL 3166) is dismissed rather than analyzed, and the claim of "consistently outperforming" is contradicted.** On this setting (Table 2), the method achieves perplexity 3166 — roughly 4–5× worse than ARB-RC (763) and ARB-X (681). The paper states only that "the large perplexity indicates that the metric cannot provide a meaningful evaluation." This is insufficient. The sentence appears after the method acknowledges that it is an exception ("with the exception of Llama-2-7B model evaluated on PTB dataset"), but no analysis is given for why the method collapses specifically on this setting. Meanwhile the abstract and conclusion claim the method "consistently outperforms" prior methods. The FP baseline itself is anomalously high (LLaMA-2-7B PTB: 37.91; 13B: 50.93 — larger model, *higher* PPL), which suggests a systematic evaluation issue, but the paper does not investigate or correct this. The result is a clear empirical counterexample to the "consistently outperforms" claim, and the paper's treatment of it harms evidential confidence in the other results.

2. **Missing ablation of the selective-layer design.** The method restricts the proposed Output Error objective to only the last fully-connected layer of each transformer block, using ARB-RC (weight alignment) for all other layers (Section 4.2). This design decision is stated without empirical justification and is never ablated. The central framing of the paper is "rethinking output alignment," yet the vast majority of layers are quantized with a prior weight-alignment method. Without seeing results for (a) Output Error on all layers, (b) Output Error on the last layer only (the chosen design), and (c) no Output Error (pure ARB-RC), the reader cannot isolate how much of the gain comes from the new objective vs. the specific selective placement. This is the single most important missing experiment.

### Minor

3. **AMP relies on a hard gradient-sign heuristic without convergence guarantees.** The Attention Matrix Preservation mechanism (Eq. 10–11) computes gradient signs w.r.t. a trace objective and uses them as binary switches between the closed-form optimum and the current parameter value. This is a heuristic: there is no unified optimization that jointly balances the output-error and AMP losses, no convergence analysis, and no study of whether the binary masks oscillate or stabilize. While the ablation shows AMP is empirically effective, the mechanism would be stronger if reframed as a regularized objective (e.g., $\mathcal{L}_\text{total} = \mathcal{L}_\text{output} + \lambda \mathcal{L}_\text{AMP}$) with alternating optimization. The architecture-dependent behavior (large effect on LLaMA, negligible on OPT) is attributed post-hoc to RMSNorm, which is plausible but not experimentally verified (e.g., by modifying the normalization in one direction).

4. **The derivation from the AMP objective to the mask updates is notationally unclear.** Equation (9) writes the objective as "maximizing" a Frobenius norm of a Hadamard product, which is actually a Frobenius inner product. The jump to gradient-sign gating in Eqs. (10)–(11) is presented without justification for why a hard binary switch from gradient signs is preferable to soft weighting or a regularized loss.

### Trivial

5. The AveQA improvements on OPT are small (often <1%, e.g., OPT-1.3B: 45.76 vs. 45.22) and no statistical significance is reported. This is not unusual for this type of evaluation in the quantization literature, but it limits the strength of the downstream-task claims.

## Nice-to-Haves

- A convergence/stability analysis of the AMP mask updates (do the binary switches oscillate?).
- A variant that reformulates AMP as an explicit regularizer ($\mathcal{L}_\text{total} = \mathcal{L}_\text{output} + \lambda \mathcal{L}_\text{AMP}$) with alternating optimization, which would be more principled and easier to extend.
- A summary of computational overhead in the main text (currently deferred to Appendix D).
- A controlled experiment isolating the effect of RMSNorm vs. LayerNorm to verify the hypothesis about LLaMA's sensitivity.

## Removed Points

The following points from the reviewers are removed or demoted with justification:

1. **"The method does not practice the output alignment it preaches"** — This is a misunderstanding. The paper's analysis (Section 3.1) explicitly demonstrates that indiscriminate layer-wise output alignment can be harmful. The selective strategy is motivated by and consistent with this analysis. The missing ablation (Weakness 2 above) is the real issue, not a framing mismatch.

2. **Criticism that PB-LLM uses a different bit-width (1.7 vs 1.11/1.06)** — The paper reports bit-widths transparently in the tables. This is a factual observation, not a weakness of the method. Asymmetric bit-widths are noted but the critic's implication of unfair comparison is not pursued; if anything the asymmetry favors the *baseline* (higher bit-width), making the paper's improvements against PB-LLM more meaningful.

3. **"The statistical significance of the AveQA improvements should be reported"** — Reporting significance tests for zero-shot evaluation on seven datasets is not standard practice in the LLM quantization literature. The margins are indeed small, but the critic does not cite a standard that the paper violates.

4. **"Computational overhead should be in the main text"** — This is a presentation preference. The overhead analysis exists in the appendix (which is standard). Moving it to the main text would be a minor improvement.

5. **"The analysis in the derivation of AMP is unclear"** — This is noted and kept as a minor weakness (Weakness 4) rather than removed; the unclear derivation is a real presentation issue but not a fatal flaw.

## Novel Insights

The most novel insight that emerges from the cross-review is that **the paper's diagnostic analysis (Section 3) is stronger and more self-contained than its proposed solution**. The identification of three failure modes of output alignment — block-level loss discrepancy, error accumulation, and attention degradation — stands on its own as a contribution to understanding 1-bit LLM quantization. The method that follows is effective on most benchmarks but carries un-ablated design choices (selective layer placement) and a heuristic component (AMP) whose success is architecture-dependent and ungrounded. A revised version that either ablates the selective strategy thoroughly or reformulates AMP as a principled regularizer would substantially strengthen what is already a useful empirical paper. The PTB LLaMA-2-7B failure, if honestly analyzed rather than dismissed, could reveal valuable boundary conditions on when output alignment works.

## Suggestions

1. **Run the missing ablation** comparing (a) Output Error on all layers, (b) Output Error on last FC layer only (current design), and (c) no Output Error (pure ARB-RC) for at least one model and dataset. This is the single most informative experiment the paper lacks.

2. **Analyze the PTB LLaMA-2-7B failure** rather than dismissing it. Investigate whether it stems from an evaluation bug (the FP numbers are anomalous), a genuine method limitation, or data characteristics. If the FP scores are wrong, correct them and re-run all PTB numbers. If the method collapses, explain why.

3. **Reformulate AMP** as an explicit regularizer: $\mathcal{L}_\text{total} = \mathcal{L}_\text{output} + \lambda \mathcal{L}_\text{AMP}$ and optimize with alternating closed-form updates. This would remove the heuristic hard-gating and make the method more principled and extensible.

4. **Tone down the "consistently outperforms" language** or qualify it with the observed exception. Accuracy in claims matters more than sweeping rhetoric.

## Score and Decision

The paper makes a genuinely valuable diagnostic contribution (Section 3) and proposes a method that works well across most benchmarks. However, the unanalyzed failure on PTB LLaMA-2-7B (which directly contradicts the "consistently outperforms" claim) and the missing ablation of the central design choice (selective layer placement) are significant weaknesses that prevent a strong recommendation. With these addressed, the paper would be clearly acceptable. In its current form, I recommend borderline acceptance.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>