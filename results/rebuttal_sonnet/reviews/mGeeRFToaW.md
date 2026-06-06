Now I have enough information from the paper to evaluate the rebuttal. Let me produce the updated meta-review.

---

## Summary

QZO (Quantized Zeroth-order Optimization) fine-tunes post-training quantized LLMs by perturbing continuous quantization scales (rather than discrete integer weights) to estimate ZO gradients, eliminating backpropagation while compressing models to 4-bit or 2-bit. A companion technique, Directional Derivative Clipping (DDC), stabilizes training by clipping the estimated directional derivative scalar before the gradient update. Compared to 16-bit full-parameter fine-tuning, QZO achieves over 18× memory reduction; against MeZO (ZO on 16-bit weights), QZO uses ~3× less memory while achieving broadly competitive performance across five NLP benchmarks and three 7B-class model families.

---

## Rebuttal Assessment

**Weakness: FLOP accounting inconsistency (Major)**
- **Author's response:** Partially address
- **Assessment:** Partially convincing — The authors candidly concede the OPT-6.7B QZO FLOP entry (8.19 × 10¹³) is anomalous and "likely contains a reporting or measurement error." They also acknowledge the "1% of FLOPs" claim in Section 4.2 is overstated and should be corrected to ~2–7% based on the valid Llama data. Paper-verified: Table 2 confirms QZO/MeZO FLOP ratios of ~2% (Llama-2-7B: 2.26×10¹⁶ / 1.13×10¹⁸) and ~7% (Llama-3.1-8B: 7.9×10¹⁶ / 1.13×10¹⁸). Section 4.2 still reads "QZO uses only about 1% of the trainable parameters and 1% of the FLOPs of MeZO" — this is verifiably contradicted by the paper's own Llama data. The concession is honest but the error remains uncorrected in the current paper.
- **Score impact:** Weakness unchanged (no in-paper fix)

**Weakness: Missing QLoRA comparison (Major)**
- **Author's response:** Partially address
- **Assessment:** Partially convincing — The author's methodological argument (QLoRA requires backprop, QZO doesn't, thus MeZO is the appropriate comparator) is principled but insufficient to fully dismiss the reviewer's concern. A practitioner with a 5–8 GB GPU budget would naturally consider both QLoRA and QZO, and the paper gives them no basis for comparison. The author commits to adding at least a memory-footprint comparison in a revision — but this is not in the current paper. Verified: QLoRA is cited in Section 2 and the references (Dettmers et al., 2023) but does not appear as a baseline anywhere in Tables 1–3.
- **Score impact:** Weakness unchanged (no in-paper fix)

**Weakness: Theorem 1 unbiasedness lacks main-text intuition (Minor)**
- **Author's response:** Partially address
- **Assessment:** Partially convincing — The rebuttal's offered sketch ("d can be treated as an even function of z in expectation") is imprecise; d is actually an *odd* function of z (d(-z) = -d(z)), so d·z is an even function. Clipping preserves the sign of d, so d'·z is also even-in-z, but unbiasedness still requires E[d'·z] = ∇_Δ L, which is non-trivial when clipping changes the magnitude. The author acknowledges the gap and promises to add a proof sketch, but no sketch has been added to the main text. The proof in Appendix A (cited but inaccessible in this version) is the only current support.
- **Score impact:** Weakness unchanged

**Weakness: "On par with MeZO" framing partly oversold (Minor)**
- **Author's response:** Acknowledge
- **Assessment:** Unconvincing (as a fix) — The author concedes the 21.5-point CB gap for Llama-3.1-8B (69.6 vs. 91.1, confirmed in Table 1) is real and warrants explicit acknowledgment. Section 4.2 currently reads "On most datasets, QZO performs on par with MeZO" without flagging this specific failure. The author's contextual explanation (CB is noisy, small dataset, label-imbalance amplified under scale constraints) is plausible but speculative and not in the paper. No change made to Section 4.2 in the current submission.
- **Score impact:** Weakness unchanged

**Weakness: SGD as upper bound buried in footnote (Minor)**
- **Author's response:** Acknowledge
- **Assessment:** The concession is appropriate. Footnote 2 confirms the SGD caveat exists but is not repeated in Section 4.2 where fine-tuning is called "the upper-bound." The author commits to moving this into the main text. Not currently addressed in the paper.
- **Score impact:** Weakness unchanged

**Weakness: Figure 3 ablation incomplete above C=150 (Trivial)**
- **Author's response:** Acknowledge
- **Assessment:** The author explains that runs with C>150 sometimes collapse mid-training, making stable reporting non-trivial. Paper-verified: Section 4.3 states "When C is set to a value bigger than 150, the training becomes unstable and sometimes collapse." The explanation is reasonable. The author commits to adding ≥1 data point above 150 in a revision. The current ablation remains incomplete.
- **Score impact:** Weakness unchanged

---

## Strengths

1. **Principled core mechanism**: Decomposing θ = Δ⊙θ̄ and perturbing only continuous scale Δ while holding integer weights fixed elegantly circumvents the ZO-on-discrete-weights precision gap (Section 3.2.1, Definition 3.3). This avoids the re-quantization burden of ZO-SignSGD variants (Section 2).

2. **Directly measured memory efficiency**: Table 1 provides actual GPU peak-memory measurements (Llama-2-7B: QZO 5.0 GB vs. MeZO 14.8 GB vs. AdamW 92.2 GB), directly validating the 18× headline claim without relying on theoretical estimates.

3. **Broad empirical coverage**: Experiments span three 7B-class model families (OPT-6.7B, Llama-2-7B, Llama-3.1-8B), a 13B model under extreme 2-bit quantization (Table 3), five NLP tasks, and two quantization paradigms (scalar GPTQ at 4-bit, codebook AQLM at 2-bit).

4. **DDC addresses a genuine training stability problem with causal evidence**: Figure 2 shows training collapses to NaN at step 22 without DDC. Figure 3's ablation shows robustness to threshold choice for C ≥ 75, with actionable guidance for hyperparameter selection.

5. **Competitive performance at 3× lower memory**: QZO frequently matches or exceeds MeZO (16-bit) — e.g., Llama-2-7B on SQuAD: 85.5 vs. 80.7 F1 (Table 1) — despite operating at 4-bit.

---

## Weaknesses

### Fatal
None.

### Major

1. **FLOP accounting is internally inconsistent and Section 4.2's "1% of FLOPs" claim is verifiably wrong**: Table 2 shows OPT-6.7B QZO FLOPs (8.19 × 10¹³) are ~264× lower than fine-tuning (2.17 × 10¹⁶) despite both requiring full-model forward passes over 20k steps — a clear reporting anomaly. The valid Llama data yields QZO/MeZO FLOP ratios of ~2% (Llama-2-7B) and ~7% (Llama-3.1-8B), yet Section 4.2 still asserts "1% of the FLOPs." The authors concede this in the rebuttal but have not corrected the paper.

2. **Missing QLoRA comparison**: QLoRA (Dettmers et al., 2023) is cited but not evaluated. While the authors argue the ZO vs. first-order regime difference makes MeZO the primary comparator, a practitioner choosing memory-efficient fine-tuning cannot evaluate the QZO trade-off without any QLoRA reference point. The omission limits practical situatedness. No data added in revision.

### Minor

1. **Theorem 1's unbiasedness claim lacks main-text intuition**: Clipping d (a nonlinear function of z) before forming d'·z does not obviously preserve unbiasedness, and the main text provides no sketch. The author's rebuttal explanation is imprecise (confusing "even" and "odd" symmetry of d). The proof remains appendix-only.

2. **"On par with MeZO" framing is partly oversold**: The CB gap for Llama-3.1-8B (69.6 vs. 91.1, a 21.5-point deficit, confirmed in Table 1) is not explicitly flagged in Section 4.2. The paper's hedge ("on most datasets") is insufficient given the magnitude of this specific result.

3. **SGD rather than AdamW as upper-bound baseline disclosed only in footnote**: Footnote 2 buries the SGD qualification while Section 4.2 calls fine-tuning "the upper-bound," understating the true performance ceiling.

### Trivial

- Figure 3 ablation covers C = 0 to 150 but includes no data point above 150, despite Section 4.3 warning of instability there; the ablation is incomplete at the high end.

---

## Nice-to-Haves

- **Analysis of when scale-only updates suffice**: The finding that ~50M quantization-scale parameters can match/exceed 6.7B-parameter ZO is scientifically interesting. Correlating task type (classification vs. generation, surface vs. reasoning) with the QZO–MeZO gap would sharpen the theoretical narrative beyond "it works empirically."
- **Wall-clock training time comparison**: Table 2 reports FLOPs, but practitioners need actual runtime on a single GPU to assess whether the FLOP advantage translates to real speedup.
- **Brief in-body summary of Stable Diffusion results**: Appendix F diffusion results are mentioned in one sentence in the Conclusion. A small table or figure in the main body would strengthen the generalization claim.

---

## Novel Insights

QZO surfaces an underexplored phenomenon: concentrating ZO perturbations on a small, semantically structured parameter set (quantization scales, ~0.75% of total parameters) often matches or exceeds perturbing all parameters via ZO. This suggests that for ZO specifically — where gradient estimates are inherently noisy over high-dimensional spaces — a well-chosen low-dimensional parameterization may outperform the full-parameter ZO by reducing estimation noise per useful gradient signal. The quantization scales, as continuous mediators between a fixed integer lattice and the effective weight space, appear to encode disproportionately high task-relevant information per parameter. This principle may generalize beyond quantization to other structured low-dimensional fine-tuning targets in zeroth-order regimes.

---

## Suggestions

1. Audit Table 2 OPT-6.7B QZO FLOP entry; provide explicit per-step FLOP accounting formulas verifiable across all three models; correct Section 4.2's "1% of FLOPs" claim to the measured ~2–7%.
2. Add at minimum a QLoRA memory-footprint row and one representative task score (e.g., SST-2 or SQuAD for Llama-2-7B) to situate QZO in the practical landscape.
3. Add a 1–2 sentence proof sketch of Theorem 1 to Section 3.2.2, specifically explaining why clipping the scalar d (odd function of z) before forming d'·z preserves the expected gradient direction and magnitude.
4. Explicitly call out the CB gap for Llama-3.1-8B (69.6 vs. 91.1) in Section 4.2 and discuss what task characteristics may make scale-only ZO fall short.
5. Move the SGD caveat from Footnote 2 into Section 4.1 or 4.2 where "upper-bound" is asserted.

---

## Score and Decision

The rebuttal is honest: the authors concede all major and minor weaknesses without spinning them. However, candid acknowledgment does not fix the weaknesses, and no substantive changes have been made to the current paper. The two Major weaknesses — the internally inconsistent FLOP accounting with a verifiably incorrect "1% of FLOPs" claim in Section 4.2, and the absent QLoRA reference point — remain exactly as identified in the original review. The three Minor weaknesses also remain unaddressed in the paper itself. The rebuttal provides no new evidence that should raise the score, nor does it reveal additional problems that would lower it. The paper's core contribution remains sound and practically significant, and the weaknesses are correctable in revision; the score is maintained.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>