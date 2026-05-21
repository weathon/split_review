Now I'll write the final consolidated review.

---

## Summary

This paper proposes QZO (Quantized Zeroth-order Optimization), a method for fine-tuning quantized neural networks by perturbing the continuous quantization scale (rather than the discrete weights) within a zeroth-order optimization framework. The key ideas are Quantized SPSA (Q-SPSA), which estimates gradients by perturbing the scale parameter Δ instead of the discrete weights, and Directional Derivative Clipping (DDC) to stabilize training. Experiments on OPT-6.7B, Llama-2-7B, Llama-3.1-8B, and Llama-2-13B show that QZO achieves significant memory reduction (18× vs AdamW, 3× vs MeZO) while obtaining competitive performance on several NLP benchmarks.

## Strengths

1. **Clean and novel technical idea.** The core insight — perturbing the continuous quantization scale Δ rather than discrete quantized weights for gradient estimation — is creative and technically sound. It elegantly sidesteps the infeasibility of perturbing discrete weights and avoids de-quantization/re-quantization at each step. This is a genuinely non-obvious extension of SPSA to quantized models.

2. **Substantial and clearly demonstrated memory reduction.** Figure 1 and Table 1 show that QZO with 4-bit models uses 4.8–6.2 GB of memory vs 14.8–20.4 GB for MeZO and 26.0–31.9 GB for SGD fine-tuning. The memory profiling covers three model families consistently, and the 18× reduction relative to AdamW is well-supported. The 2-bit experiment on Llama-2-13B (5.78 GB on a single 24 GB GPU, Table 3) further demonstrates the practical value.

3. **Orthogonality to multiple PTQ families.** QZO is validated with both scalar-based (GPTQ, 4-bit) and codebook-based (AQLM, 2-bit) quantization, showing that the approach is not tied to a specific quantization scheme. This is a genuine practical advantage over prior ZO+quantization methods that only work with specific quantized representations.

4. **Empirical evidence for DDC stabilization.** Figure 2 clearly shows that without DDC, training collapses (NaN loss by step 22), while with DDC the loss and directional derivatives remain stable over 1,000 steps. This ablation is convincing and well-presented.

## Weaknesses

### Major

1. **FLOPs numbers in Table 2 are inconsistent and likely methodologically wrong.** The ratio of MeZO-to-QZO FLOPs varies wildly across models: ~12,000× for OPT-6.7B (9.91e17 vs 8.19e13), ~50× for Llama-2-7B, and ~14× for Llama-3.1-8B. Both methods perform two full forward passes per step through models of similar size; the forward pass cost should dominate the FLOPs and be comparable. The variance across models cannot be explained by the reduced precision of quantized weights alone. The paper claims "about 1% of the FLOPs of MeZO" but the actual ratios range from 0.008% to 7%. This suggests the QZO FLOPs may only count the scale update while omitting the forward passes, making the computation-efficiency claim unreliable. The paper's central claim in this section ("QZO demonstrates both memory-efficiency and computation-efficiency") rests on these numbers.

2. **Theoretical claim about DDC unbiasedness is not credible from the presented material.** Theorem 1 asserts that the clipped gradient estimate d'·z is an unbiased estimator of the true gradient. Since d' = clip(d, -C, C) is a non-linear function of d, and d depends on the same random direction z used in the estimator, unbiasedness does not follow from standard SPSA unbiasedness without strong additional assumptions (e.g., that clipping never activates, which trivializes the claim, or a specific distributional symmetry). The proof is deferred entirely to Appendix A (stripped), and the in-text derivation in Eq. 8 contains notational gaps (e.g., dropping norms, jumping from E[‖∇̂‖]² to (∇L)²). If the claim is incorrect, the variance reduction argument collapses and DDC is left as a purely empirical heuristic, which undercuts a stated contribution of the paper.

3. **Missing standard deviations / confidence intervals for any result.** ZO methods are known to have high variance (the MeZO paper reports standard deviations). Table 1 reports only single-run numbers. Without error bars, the reader cannot assess whether QZO's performance gaps to MeZO (e.g., CB with Llama-3-8B: 91.1 vs 69.6, or BoolQ: 83.4 vs 78.2) are statistically significant or noise. This is especially important given the paper's "on par" narrative.

### Minor

1. **"On par" claim is overbroad.** The abstract and conclusion state that QZO "performs on par with MeZO." While this holds for many tasks, there are clear exceptions: CB with Llama-3-8B (MeZO 91.1 vs QZO 69.6, a 21.5-point gap), BoolQ with Llama-3-8B (83.4 vs 78.2), and RTE with Llama-3-8B (70.0 vs 66.8). The in-text discussion ("On most datasets, QZO performs on par with MeZO") is more measured, but the high-level framing should be adjusted to acknowledge these gaps.

2. **Missing contextualization against other memory-efficient fine-tuning methods.** The paper claims "maximum reduction in memory consumption" but does not compare or discuss QLoRA (Dettmers et al., 2023), which is the most widely used method for fine-tuning quantized LLMs (4-bit base + LoRA adapters). QLoRA is cited in references but not mentioned in the Related Work or experiments. A direct comparison of memory footprint and performance would be valuable to contextualize QZO's advantages, especially since QLoRA also eliminates large gradient/optimizer storage through a different mechanism (small trainable adapter parameters). The paper's own Related Work section on "Memory-Efficient Training" (lines 51–57) discusses GaLore, MeZO, and CoLM but omits QLoRA entirely.

3. **Asymmetry in the upper-bound comparison.** The memory profiling in Figure 1 includes AdamW (which has the largest memory footprint), but the performance upper-bound uses SGD fine-tuning (which has much lower memory). This means the 18× memory reduction is relative to AdamW, while all accuracy comparisons are against SGD fine-tuning with lower memory cost. This asymmetry should be disclosed more prominently — the impressive 18× number and the "on par" performance comparison use different baselines, and the paper currently treats them as one unified story.

4. **No wall-clock time or training throughput reported.** The paper argues for computation efficiency but provides only FLOPs (which are suspect) and no actual runtime measurements. ZO methods with two forward passes per step are typically slower per step than backpropagation; reporting actual training time would allow readers to assess the practical speed-accuracy-memory tradeoff.

### Trivial

- The variance derivation in Eq. 8 writes "(∇_Δ L)^2" without a norm on the gradient; the intended mathematical object is ambiguous.
- The paper states "about 1% of the FLOPs of MeZO" but the actual ratios vary from 0.008% to 7% across models; the text should match the actual numbers.

## Nice-to-Haves

- A comparison to QLoRA and/or LoRA in terms of both memory and accuracy on the same benchmarks would significantly strengthen the positioning of QZO in the memory-efficient fine-tuning landscape.
- Sensitivity analysis for the clipping threshold C across more than one dataset (Figure 3 only varies C on SST-2) would strengthen the DDC claims.
- Discussion of how input-dependent / dynamic quantization scales would interact with Q-SPSA, since the main experiments use static group-wise quantization.

## Removed Points

*"Missing comparison to ZO-signSGD-based methods (Feng et al., Zhou et al., Bar & Giryes)"* — The paper discusses these methods qualitatively in the Related Work (Section 2, lines 61). Comparing against methods that use a fundamentally different approach (sign-based optimization on discrete weights with re-quantization) is a nice-to-have, not a required baseline. These methods are referenced but an experimental comparison is scope-appropriate to omit.

*"O(d) per step in Algorithm 1"* — The paper explicitly notes (line 137) that one may perturb entire linear layers to save computation, following the MeZO approach. This is a known implementation detail, not a methodological flaw.

*"Missing comparison to GaLore"* — GaLore targets optimizer state reduction for AdamW, not ZO or quantization. It is a different paradigm and not a necessary baseline.

*"The fine-tuning baseline uses SGD, not AdamW"* — The paper acknowledges this (footnote 2: "Due to limited budget on computational resources, fine-tuning experiments are conducted with SGD optimizer unless otherwise specified"). This is a reasonable resource constraint, though the asymmetry with memory profiling (which uses AdamW) is noted in the minor weaknesses.

*"Missing discussion of computational overhead / per-step cost / activation memory details"* — These are standard follow-up questions but not critical gaps. The paper provides sufficient algorithm details to reconstruct the method.

*"Cites QLoRA in references but does not discuss it in related work"* — Actually, QLoRA is in the references (line 324) which confirms its existence. The discussion omission is noted in Minor Weakness #2.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. **Correct the FLOPs analysis.** Provide a clear accounting of what operations are counted, including two forward passes per step. Report consistent numbers across models and validate the methodology. If the forward pass through quantized weights uses different hardware arithmetic (INT4/INT8), explain how FLOPs are computed and why the numbers differ from the full-precision baseline. Alternatively, replace FLOPs with wall-clock training time, which is more practically meaningful.

2. **Either provide the DDC proof or drop the unbiasedness claim.** If Theorem 1 has a valid proof, include it in the main paper (or ensure it is in the appendix). If it relies on assumptions that may not hold (e.g., clipping rarely activates), state them clearly. Otherwise, present DDC as an empirical stabilization technique without the theoretical framing.

3. **Report standard deviations** for at least the key comparison tasks (or state that only single runs were conducted and why). This is important given the known variance of ZO methods.

4. **Adjust the "on par" narrative** to explicitly acknowledge the datasets where QZO lags behind MeZO and discuss possible reasons (e.g., CB is a small dataset where more precise weight updates may matter).

5. **Add a comparison to QLoRA** as a memory-efficient fine-tuning baseline, if only in terms of peak memory and accuracy on one or two benchmarks.

## Score and Decision

My initial round-1 bracket placed this paper between the weak anchor at 3.0 (EfficientQAT, PrefixQuant) and the middle anchor at 5.5 (Sparse MeZO). The round-2 narrowing pulled in tighter anchors: Sparse MeZO (avg 5.5, Reject), MeZO-A³dam (avg 4.75, Rejected), QA-LoRA (avg 6.33, Accept poster), and LOZO (avg 7.0, Accept poster). 

Comparing directly: Sparse MeZO (5.5, Reject) is the closest comparator — both are ZO improvements over MeZO with theoretical questions and evaluation gaps. QZO has a more novel core idea (scale perturbation) but a more serious evaluation issue (the FLOPs error is a clear methodological problem, whereas Sparse MeZO's primary weakness was incremental contribution). MeZO-A³dam (4.75, Rejected) had an incorrect proof, which is comparable in severity to QZO's questionable DDC theorem and FLOPs error. QA-LoRA (6.33, Accept) and LOZO (7.0, Accept) are cleaner in execution with stronger theory or more comprehensive evaluation.

QZO is weaker than the accept-level anchors (QA-LoRA, LOZO) due to the FLOPs inconsistency and the unverified theoretical claim. It is roughly comparable to Sparse MeZO but with a different weakness profile — greater novelty but also a more concrete error (the FLOPs numbers appear methodologically wrong rather than merely incomplete). I place the paper near Sparse MeZO but slightly lower due to the FLOPs issue being a verifiable error on the page, not a judgment call about completeness.

**Final score: 5.0**

**Decision: Reject** — The core idea (scale perturbation for ZO on quantized models) is genuinely novel and the memory results are impressive, but the evaluation is undermined by (a) FLOPs numbers that are inconsistent and appear to omit forward-pass costs, (b) an unsupported theoretical claim about DDC unbiasedness, and (c) single-run results without error bars on a high-variance method. These issues would require substantial revision — corrected FLOPs analysis, strengthened theoretical justification or reframing, and additional experimental rigor — before the paper could be considered for acceptance.

Calibration anchors used:
| Anchor | Path | Avg Score | Round | Comparison |
|--------|------|-----------|-------|------------|
| Sparse MeZO | 4Kw4KAoVnx.md | 5.50 | 1,2 | Similar-level ZO paper, rejected. QZO has more novel core idea but more concrete evaluation error (FLOPs). |
| MeZO-A³dam | OBIuFjZzmp.md | 4.75 | 1,2 | Rejected/withdrawn. Had incorrect proof. QZO has similar questionable theory + FLOPs error. |
| LOZO | 9BiVepgmWW.md | 7.00 | 1 | Accepted poster. Stronger theory and cleaner evaluation. QZO is clearly below this. |
| EfficientQAT | 6Mdvq0bPyG.md | 3.00 | 1 | Quantization paper, different problem. QZO is stronger due to novel idea. |
| QA-LoRA | WvFoJccpo8.md | 6.33 | 2 | Accepted poster. Well-executed quantization+fine-tuning. QZO is less polished. |
| OSTQuant | rAcgDBdKnP.md | 6.20 | 2 | Accepted poster. Quantization PTQ paper. Different task, similar rigor level not matched by QZO. |

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>