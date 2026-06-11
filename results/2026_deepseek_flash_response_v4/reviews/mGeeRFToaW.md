Now I have a solid picture of the calibration landscape. Let me write the final review.

## Summary

This paper proposes Quantized Zeroth-order Optimization (QZO), which enables fine-tuning of quantized LLMs by perturbing the continuous quantization scale parameter (Δ) rather than discrete quantized weights, combined with a directional derivative clipping (DDC) method for stabilization. QZO eliminates gradients and optimizer states via zeroth-order optimization while also compressing weights via PTQ. Experiments on OPT-6.7B, Llama-2-7B, Llama-3.1-8B, and Llama-2-13B across five NLP tasks show QZO can fine-tune 4-bit and 2-bit models with ~3× memory reduction over MeZO (the prior ZO baseline) and ~18× over full 16-bit fine-tuning, while achieving broadly on-par accuracy.

## Strengths

1. **Core idea (Q-SPSA) is novel and principled.** The paper identifies that ZO cannot directly perturb discrete quantized weights and proposes to perturb the continuous quantization scale Δ while keeping integer codes fixed (Definition 3.3, Eq. 5). This avoids the de-quantization/re-quantization overhead required by prior ZO+quantization approaches (ZO-signSGD-based methods cited in Section 2). This is the paper's primary technical contribution and is clearly articulated.

2. **Measured memory savings are concrete and significant.** Figure 1 and Table 1 report actual peak-memory measurements showing 4.8–6.3 GB for 7B-level 4-bit models versus 14.8–20.4 GB for MeZO (16-bit) — a clean 3× memory reduction. The 18× reduction versus full AdamW fine-tuning is also well-documented. These numbers are credible.

3. **Compatibility with both scalar-based and codebook-based PTQ.** QZO is evaluated on GPTQ (4-bit scalar) and AQLM (2-bit codebook) within the same framework, demonstrating generality beyond a single quantization scheme. Section 3.2.1 explains how Q-SPSA generalizes to both paradigms.

4. **DDC ablation is clean and convincing.** Figure 2 shows training without DDC collapses to NaN by step 22, while DDC maintains stability for 1,000+ steps. Figure 3 demonstrates robustness across a wide range of clipping thresholds (75–150). This is well-designed experimental evidence for the practical importance of DDC.

5. **2-bit extreme quantization results demonstrate feasibility.** Table 3 shows QZO fine-tuning a 2-bit Llama-2-13B on a single 24GB GPU, beating the zero-shot baseline across all tasks. This goes beyond what prior ZO+quantization work has shown.

## Weaknesses

### Major

1. **FLOPs accounting in Table 2 is inconsistent and the computation-efficiency claims are unsupported.** The QZO FLOPs values vary wildly across models: 8.19×10¹³ (OPT-6.7B), 2.26×10¹⁶ (Llama-2-7B), 7.9×10¹⁶ (Llama-3.1-8B). The ratio to MeZO FLOPs ranges from 0.008% (OPT-6.7B) to 2% (Llama-2-7B) to 7% (Llama-3.1-8B), yet the text (line 251) claims "1% of the FLOPs of MeZO" as a general statement. The OPT-6.7B number (8.19×10¹³) is orders of magnitude below what would be expected if forward-pass computation were included — both QZO and MeZO perform two full forward passes through a 6.7B-parameter model per step, which costs on the order of 10¹⁶–10¹⁷ FLOPs. The paper must clarify exactly which operations are counted and why the numbers differ so dramatically across architectures. As presented, the FLOPs comparison undermines the computation-efficiency claims.

2. **The variance-reduction argument for DDC depends on an unsupported unbiasedness claim.** Theorem 1 states that the clipped gradient estimate is unbiased. Clipping the directional derivative d at ±C is a non-linear operation that generally shifts the expectation whenever |d| > C on a non-negligible set. The variance-reduction derivation in Eqs. 7–8 depends on this unbiasedness claim (specifically, the last step in Eq. 8 replaces E[||∇̂'||]² with (∇L)² via Theorem 1). If the estimate is biased, the inequality Var[∇̂'] ≤ Var[∇̂] does not follow from the algebra shown. The proof is deferred to the stripped Appendix A, but the claim contradicts standard properties of clipping. **The empirical benefit of DDC is clearly demonstrated (Figure 2) and is not in doubt** — the issue is with the theoretical framing. A correct analysis would characterize the bias-variance tradeoff, and the paper would be better served by this honest treatment.

### Minor

3. **No variance or statistical significance reported.** Tables 1 and 3 report single runs without standard deviations or repeated-seed experiments. With only 1,000 training examples per task, results could be noisy. For example, QZO achieves 85.5 F1 vs. MeZO's 80.7 on SQuAD with Llama-2-7B (a 4.8-point gap in QZO's favor), while QZO scores 69.6 vs. MeZO's 91.1 on CB with Llama-3.1-8B (a 21.5-point gap against QZO). Without error bars, the reader cannot assess whether these gaps are meaningful or due to run-to-run variability.

4. **Selective emphasis of favorable results.** The paper highlights the SQuAD Llama-2-7B result (85.5 vs. 80.7, in QZO's favor) but does not similarly call out the large gaps against QZO (e.g., Llama-3.1-8B CB: 69.6 vs. 91.1). While the broad characterization "performs on par with MeZO" is approximately correct across the 15 comparisons in Table 1, the presentation gives disproportionate weight to the single best QZO result.

5. **No comparison against QLoRA.** QLoRA (Dettmers et al., 2023) is the most directly relevant memory-efficient fine-tuning method for quantized LLMs. The paper cites it in references but never benchmarks against it. While QZO's primary contribution is as a ZO method (and QLoRA uses first-order optimization, a different paradigm), a comparison would help position QZO within the broader landscape of memory-efficient fine-tuning. Its absence leaves an open question about how QZO's accuracy-efficiency tradeoff compares to the state of the art.

6. **Hyperparameter sensitivity is underexplored.** The paper uses a single setting (lr=10⁻⁷, ε=10⁻³, C=100) across all experiments without reporting whether these were tuned per dataset or applied globally. Only the clipping threshold C is ablated. The perturbation scale ε can significantly affect ZO gradient quality, and its sensitivity is not examined.

### Trivial

7. The paper states "QZO uses only about 1% of the FLOPs of MeZO" (line 251), but the actual ratios in Table 2 are 0.008%, 2%, and 7% for the three models. The claim is inaccurate for two of the three models.

## Nice-to-Haves

- A wall-clock time comparison per step (or total time to convergence) would make the computational claims verifiable and concrete, sidestepping the FLOPs accounting ambiguity.
- An analysis of how the quantization scales Δ change during training and what the resulting effective weight updates look like would deepen understanding of the method.

## Removed Points

These points were raised by the reviewers but are excluded from the main weaknesses above:

- **"Missing comparison with QLoRA as a fatal flaw"** — Demoted to Minor. QZo is a ZO method; QLoRA uses first-order optimization. The paper's primary comparison against MeZO (another ZO method) is appropriate. A QLoRA comparison would strengthen the paper but its absence is not a fatal gap.
- **"Related work discusses QLoRA without benchmarking it"** — Removed. Related work sections contextualize prior work; they are not commit-to-benchmark lists.
- **"Custom kernel modification for AQLM is an architectural limitation not discussed"** — Removed. Modifying an existing kernel is standard implementation work; it does not invalidate the method's generality.
- **"Limited expressivity of only updating scale parameters"** — Removed. This is an intentional design choice that enables the parameter savings; it is not a bug.
- **"FLOPs comparison not credible on its face"** — Re-framed to the specific Major weakness above. The critic's framing as intentional deception is too strong; the issue is unclear accounting, not fraud.
- **Missing appendix content or reproducibility details** — Removed per instructions (parser strips appendices).

## Novel Insights

None beyond the paper's own contributions. The insight that ZO should perturb the quantization scale Δ rather than the discrete weights is the paper's core contribution; no reviewer added new insight beyond verifying or challenging this claim.

## Suggestions

1. **Clarify the FLOPs metric.** State explicitly which operations are counted. If forward-pass FLOPs are excluded, say so and consider replacing Total FLOPs with wall-clock time. If they are included, correct the numbers (the OPT-6.7B value is off by several orders of magnitude). Also correct the "1% of FLOPs" claim to match the actual ratios.

2. **Reframe the DDC theoretical analysis.** Replace the unbiasedness claim (Theorem 1) with a bias-variance tradeoff characterization. The empirical evidence in Figure 2 is strong enough to justify DDC without overclaiming theory.

3. **Add error bars.** Report at least 3 seeds with standard deviations for the main results in Tables 1 and 3. This is the minimum expectation for empirical ML papers.

4. **Add a QLoRA comparison** for at least one model-dataset combination to establish relative positioning.

5. **Ablate the perturbation scale ε** and report whether hyperparameters were tuned per dataset or applied globally.

6. **Present the full distribution of results** with balanced commentary, including cases where QZO trails MeZO by large margins.

## Score and Decision

**Calibration anchors:**

| Paper | Avg Score | Round | Comparison to this paper |
|---|---|---|---|
| Transferable Static Sparsity (myYzr50xBh) | 5.80 | R2 | Stronger experimental coverage but weaker novelty; QZO is slightly weaker overall |
| Sparse MeZO (4Kw4KAoVnx) | 5.50 | R2 | Comparable ZO method; QZO's core idea is more novel, similar experimental rigor |
| QR-Adaptor/3-Stage (zcx6rIMbbR) | 5.40 | R1/R2 | Comparable quantized-fine-tuning paper; QZO has clearer contribution |
| HiZOO (bEqI61iBue) | 5.67 | R2 | Better theoretical backing; QZO is slightly weaker |
| SubZero (FK6T0U4Mg1) | 4.25 | R2 | Weaker experiments and less novel; QZO is clearly stronger |
| L4Q (KJzz4UwqTb) | 4.50 | R1 | Limited novelty; QZO is clearly stronger |
| LQ-LoRA (xw29VvOMmU) | 6.75 | R1 | Much stronger theory and experiments; QZO is clearly weaker |
| ALLoRA (7X65yoKl3Y) | 3.33 | R1 | Weaker paper; QZO is clearly stronger |

**Round 1 bracket:** 4.5–6.0 (determined by comparing against weak anchors <3.5 and strong anchors >7.5).

**Round 2 narrowing:** Compared against papers in the 4.0–6.5 range. QZO sits between the SubZero (4.25) and Transferable Static Sparsity (5.80) anchors, closer to the upper end of that range. The novel core idea (Q-SPSA) and clean memory measurements support the upper half, but the inconsistent FLOPs accounting and questionable DDC theory hold it back from the top.

**Final calibration:** Slightly weaker than Transferable Static Sparsity (5.80) and HiZOO (5.67) due to the FLOPs inconsistency and unsupported theory claim. Somewhat stronger than QR-Adaptor (5.40) and Sparse MeZO (5.50) due to a more novel contribution. The paper has a genuinely clever core idea and real empirical value, but the two major weaknesses prevent a score above ~5.5.

**Score: 5.0 / Decision: Borderline (Revise and Resubmit)**

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>