Now I have everything I need. Let me write the final consolidated review.

## Summary

This paper identifies three "fatal flaws" in LoRA for short fine-tuning — Dropout's slow convergence of its regularization effect, zero-initialization causing asymmetric A/B training dynamics, and the scaling factor's "ripple effect" across layers — and proposes ALLoRA, which removes Dropout and the scaling factor and instead applies a per-row adaptive learning rate inversely proportional to the ℓ₂ norm of the LoRA output. The method is simple, removes two hyperparameters, and shows small but consistent accuracy improvements (~0.3%) over LoRA and DoRA across multiple LLMs and tasks.

## Strengths

1. **Principled analysis of Dropout's convergence for short training.** The paper derives that the gap between the empirical and expected loss under LoRA with Dropout scales as `Std[·]/√N` (Eq. 8, lines 119-122), and empirically demonstrates that even with dropout rate 0.05, many realizations are needed for the empirical estimate to approach the expected loss (Figure 1, lines 92-96). While the connection to SGD dynamics could be tighter, this is a novel quantitative argument about Dropout's limited value in the fine-tuning regime.

2. **Clean identification and empirical validation of asymmetric regularization between A and B.** The paper computes the gradient of the Dropout-induced regularizer (Eqs. 13-14, lines 151-154), showing that A's regularization is proportional to ‖B_row‖² (zero at initialization) while B's regularizer is proportional to ‖XA_column‖² (large at initialization). Figure 3 (lines 143-147) validates this asymmetry: varying λ changes B's norm by >500% but A's norm by only ~30%.

3. **Formalizes the "ripple effect" as an exponential bound.** Proposition 1 (lines 188-190) provides a tight bound showing that the output norm can grow as Θ((1+η)^L) with depth. While this is a worst-case bound that applies to any additive perturbation, it formally captures a genuine concern about LoRA's scaling factor interacting across many layers.

4. **ALLoRA is a clean, well-motivated method that removes two hyperparameters.** The adaptive learning rate scheme (lines 266-269) is simple, the implementation is straightforward, and it eliminates the need to tune the dropout rate and scaling factor α/r, replacing them with a single parameter η that controls the adaptive schedule.

5. **Consistent improvements across diverse settings.** Table 3 (lines 348-384) shows ALLoRA or ALLoRA+D achieving the best average accuracy in 5 out of 6 model/rank combinations against DoRA on commonsense reasoning, and Table 2 (lines 304-320) shows improvements across all ranks on perception tasks. The ablation study (Section 6) systematically compares ALLoRA against its natural variants (ALLoRA-OD, ASF-LoRA) and shows it is the best in its family.

## Weaknesses

### Fatal
None.

### Major

1. **Missing experimental comparison to LoRA+, the most directly relevant baseline.** The paper acknowledges LoRA+ (Hayou et al., 2024) in the related work (line 51) as proposing "different learning rate to different low-rank matrices" — which directly addresses the paper's "second flaw" (A/B asymmetry). The paper even says its findings "support the conclusion of LoRA+" (line 140). Yet LoRA+ is never compared experimentally. Since LoRA+ addresses the same problem through a simpler mechanism (different fixed learning rates for A and B), its omission prevents the reader from judging whether ALLoRA's more complex per-row adaptive scheme provides meaningful added value. This is the single most significant gap in the experimental evaluation.

2. **No measures of variance or statistical significance.** The paper's central empirical claim is an average improvement of ~0.3% over LoRA and DoRA. Despite stating that perception experiments are "averaged over 5 runs" (line 298), no standard deviations, confidence intervals, or error bars are reported in any table or figure. The individual task-level comparisons in Table 3 show many cases where the difference is ≤0.3% (e.g., LLaMA-7B r=16: ALLoRA+D 77.6 vs DoRA 77.5; LLaMA-7B r=32: ALLoRA+D 78.4 vs DoRA 78.4 — a tie). Without variance estimates, the reader cannot determine whether the claimed advantage is systematic or within run-to-run noise. This is particularly concerning given that DoRA's own results vary unexpectedly (e.g., LLaMA2-7B: DoRA averages 80.5 at r=16 but drops to 79.7 at r=32, which is atypical for a higher-rank variant and suggests measurement noise).

3. **"Fatal flaws" framing is disproportionate to the evidence.** The paper calls Dropout, zero-initialization, and the scaling factor "three fatal flaws" (line 21) that make LoRA "unfit for short training" (line 29). Yet ALLoRA's improvements over LoRA and DoRA average ~0.3%. If these were truly fatal structural problems, the fix should produce substantially larger gains. This framing mismatch undermines the paper's credibility — the analysis identifies real issues, but the evidence suggests they are mild design concerns rather than fatal flaws.

### Minor

4. **The ALLoRA+D result needs better reconciliation with the Dropout critique.** The paper argues that Dropout is harmful for short fine-tuning (Section 3.1), but then reports that adding Dropout back to ALLoRA (ALLoRA+D, dropout 0.05) yields "no evident difference" (line 300) — which the paper interprets as "matching our theoretical result." This is ambiguous: if Dropout is genuinely harmful, adding it should degrade performance; if it has no effect, the claimed harm may be overstated. The paper would benefit from a clearer explanation of whether the theoretical claim is that Dropout's benefits vanish (consistent with the non-result) or that Dropout actively hurts (contradicted by the non-result).

5. **The theoretical argument against Dropout conflates loss estimation with optimization dynamics.** The bound (Eq. 8, lines 119-122) shows that averaging the loss over N independent Dropout realizations converges at rate 1/√N. However, SGD training uses one mask per step, and the variance of the per-step gradient estimator is an inherent part of the optimization dynamics — it does not need to be "averaged out" before performing updates. The bound properly characterizes the estimator variance but does not directly prove that Dropout harms short SGD training. The paper's empirical validation (Section 3.4, lines 208-218) partially compensates for this theoretical gap, but the argument as presented could be made more rigorous.

6. **The ripple effect bound is a generic property of deep networks, not a LoRA-specific flaw.** Proposition 1 (lines 188-190) derives that adding any small perturbation to each layer's weight matrix can cause exponential growth in a worst-case bound. This is true for any additive perturbation scheme (adapters, full fine-tuning with small updates), not just LoRA's factorization. The paper acknowledges the worst-case nature but could more clearly distinguish what makes this specifically a LoRA concern worth addressing.

## Nice-to-Haves

- A controlled ablation that starts from vanilla LoRA and adds only the adaptive learning rate (keeping Dropout and scaling factor) would isolate the source of improvement.
- The paper could strengthen the Dropout analysis by replacing the loss-estimation bound with a direct analysis of gradient variance under Dropout during SGD.
- For the commonsense reasoning experiments, following the same protocol (rather than comparing against published DoRA numbers from a different run) would enable a cleaner comparison.

## Removed Points
- *Generic criticisms about the Adaptive Learning framework being "unfalsifiable" or "too broadly defined"* — the framework is intentionally general and serves as a unifying formalism; this level of abstraction is not a flaw.
- *Reproducibility concerns about undisclosed hyperparameters or missing appendix code* — the main text provides sufficient description; appendix content is stripped by the PDF parser.
- *Pure formatting or style nitpicks* — these reflect PDF parsing artifacts, not paper author errors.
- *Criticism about the ripple effect being "trivial"* — the bound is standard but its application to formally characterize LoRA's depth-wise scaling interaction is worthwhile.

## Novel Insights

The three reviewers collectively surface a key tension that the paper does not fully resolve: the "fatal flaws" narrative would predict large gains from fixing them, but the empirical evidence shows only marginal improvements (~0.3%). This gap suggests either (a) that the flaws are real but minor in practice, or (b) that ALLoRA only partially addresses them. The paper would be substantially stronger if it acknowledged this tension explicitly and either recalibrated its claims or provided a direct attribution study showing how much of the improvement comes from addressing each flaw individually. A second insight, not well-developed in any review, is that the adaptive learning rate function (inverse norm scaling) implicitly recovers a form of normalization that could be related to existing methods like Rybczynski's adaptive regularization — the connection between ALLoRA's design and provably convergent adaptive gradient methods deserves further investigation.

## Suggestions

1. **Add LoRA+ as an experimental baseline.** This is the most actionable improvement — it directly tests whether ALLoRA's per-row adaptive scheme outperforms a simpler fixed differential learning rate for A and B.
2. **Report error bars for all main results.** For the perception experiments (5 runs), report ±std or ±sem. For the commonsense experiments (where DoRA numbers are taken from the original paper), either reproduce DoRA under the same conditions or acknowledge the limitation.
3. **Recalibrate the framing.** The "fatal flaws" language should be toned down to reflect the ~0.3% improvement magnitude. "Design concerns" or "limitations" would be more accurate.
4. **Reconcile the ALLoRA+D finding.** Clarify whether the Dropout critique is about vanishing benefits (consistent with the non-result) or actual harm (contradicted by it).
5. **Add an ablation isolating the adaptive learning rate.** Start from vanilla LoRA and add only the adaptive gradient scaling while keeping dropout and scaling factor, to measure the marginal contribution of the adaptive scheme.

## Score and Decision

MY FINAL SCORE: <score>4.5</score>
MY FINAL DECISION: <decision>Reject</decision>