Now let me run the Round 1 bracketing calibration search:Let me narrow within the bracket [5.5, 7.5] with Round 2:Now I have sufficient calibration data. Let me write the final consolidated review.

---

## Summary

QZO (Quantized Zeroth-order Optimization) fine-tunes post-training quantized LLMs by perturbing continuous quantization scales (rather than discrete integer weights) to estimate ZO gradients, eliminating backpropagation while compressing the model to 4-bit or 2-bit. A companion technique, Directional Derivative Clipping (DDC), stabilizes training by clipping the estimated directional derivative scalar before the gradient update. Compared to 16-bit full-parameter fine-tuning, QZO achieves over 18× memory reduction; against MeZO (ZO on 16-bit weights), QZO uses ~3× less memory while achieving broadly competitive performance on five NLP benchmarks across three 7B-class model families plus a 13B model under extreme 2-bit quantization.

---

## Strengths

1. **Principled and clean core mechanism**: Decomposing θ = Δ ⊙ θ̄ and perturbing only the continuous scale Δ while holding the integer weights fixed is a well-motivated solution to the precision-gap problem in ZO optimization of quantized weights (Section 3.2.1). This is more elegant than competing approaches (e.g., ZO-SignSGD variants) that require re-quantizing weights at every step.

2. **Clearly measured memory efficiency**: Figure 1 and Table 1 provide actual GPU peak-memory measurements (e.g., Llama-2-7B: QZO 5.0 GB vs. MeZO 14.8 GB vs. AdamW 92.2 GB), directly validating the 18× headline claim rather than relying on theoretical estimates.

3. **Broad empirical coverage**: Experiments span three 7B-class model families (OPT-6.7B, Llama-2-7B, Llama-3.1-8B), a 13B model under extreme 2-bit quantization (Table 3), five NLP tasks (classification and generation), and two qualitatively different quantization paradigms (scalar GPTQ at 4-bit; codebook AQLM at 2-bit).

4. **DDC addresses a genuine training stability problem with causal evidence**: Figure 2 shows that without DDC, training collapses to NaN at step 22 due to exploding directional derivatives. Figure 3's ablation shows robustness to threshold choice for C ≥ 75, providing actionable hyperparameter guidance.

5. **Competitive performance at 3× lower memory**: QZO frequently matches or exceeds MeZO (16-bit) — e.g., Llama-2-7B on SQuAD: 85.5 vs. 80.7 F1 (Table 1) — despite operating on 4-bit quantized weights.

---

## Weaknesses

### Fatal
None.

### Major

1. **FLOP accounting is internally inconsistent in Table 2, undermining the computation-efficiency claim** — Section 4.2 states "QZO uses only about 1% of the trainable parameters and 1% of the FLOPs of MeZO." Table 2 does not support this across models: for Llama-2-7B the QZO/MeZO FLOP ratio is ~2% (2.26 × 10¹⁶ / 1.13 × 10¹⁸), and for Llama-3.1-8B it is ~7% (7.9 × 10¹⁶ / 1.13 × 10¹⁸). The OPT-6.7B entry is especially anomalous: QZO FLOPs are reported as 8.19 × 10¹³ — 264× *lower* than fine-tuning (2.17 × 10¹⁶) — despite both methods running the same full-model forward passes over 20k steps. The Llama entries show no such discrepancy between QZO and fine-tuning FLOPs (2.26 × 10¹⁶ vs. 2.47 × 10¹⁶ for Llama-2-7B). This strongly suggests the OPT-6.7B row contains a reporting error, and the "1% of FLOPs" claim appears to be anchored on that anomalous entry. The methodology for counting FLOPs needs to be made explicit and consistent across all three models.

2. **Missing QLoRA comparison** — QLoRA (Dettmers et al., 2023) is cited but not evaluated. It is the most direct practical alternative for low-memory fine-tuning of quantized LLMs: it quantizes weights to 4-bit and runs LoRA adapters in full precision, requiring backward passes only through the adapters. The paper provides no explanation for excluding it. A practitioner choosing between gradient-free ZO (QZO) and adapter-based methods (QLoRA) in a 5–8 GB GPU budget cannot make that decision from this paper. Even reporting QLoRA's memory footprint and one representative task score would situate QZO meaningfully in the landscape.

### Minor

1. **Theorem 1's unbiasedness claim lacks main-text intuition** — Theorem 1 (p. 4) asserts that d' · z is an unbiased estimator of ∇_Δ L, where d' = clip(d, −C, C) and d = (L(Δ+εz) − L(Δ−εz)) / 2ε is itself a function of z. Clipping a nonlinear function of z before multiplying back by z does not obviously preserve unbiasedness; this is the load-bearing theoretical claim for the entire variance reduction argument in Eq. 8. The proof is in the appendix, but the main text provides no sketch of the key step. Readers will be left skeptical of the theoretical framing without some intuition.

2. **"On par with MeZO" framing is partly oversold** — On CB for Llama-3.1-8B, QZO scores 69.6 vs. MeZO's 91.1 (Table 1), a 21.5-point gap. The paper qualifies its claim with "on most datasets," but does not call attention to this specific result. CB is a small dataset with limited test examples, making results noisy, but the gap is real. The discussion in Section 4.2 should acknowledge where scale-only ZO falls visibly short.

3. **SGD rather than AdamW as the upper-bound baseline is noted only in footnote 2** — AdamW typically outperforms SGD by non-trivial margins on language tasks, meaning the actual performance ceiling for fine-tuning is higher than what Table 1 shows. This is mentioned only in footnote 2 and not discussed in the results section, which understates the remaining gap between QZO and optimal fine-tuning.

### Trivial

- Figure 3 shows clipping thresholds C = 0 through 150; the text mentions training becomes unstable above 150 but no data point beyond 150 is shown, leaving the ablation incomplete at the high end.

---

## Nice-to-Haves

- **Analysis of when scale-only updates suffice**: The finding that optimizing ~50M quantization-scale parameters often matches optimizing 6.7B full-precision parameters via ZO is scientifically interesting in its own right. Does task type (classification vs. generation, surface-form vs. reasoning) predict the performance gap? Correlating task characteristics with the QZO–MeZO gap would sharpen the paper's argument from "it works empirically" to "scale updates suffice for X class of tasks."
- **Wall-clock training time comparison**: Table 2 reports FLOPs, but practitioners primarily care about actual runtime on a single GPU. Even a brief comparison would clarify whether the FLOP advantage translates to real speedup.
- **Brief in-text summary of Stable Diffusion results**: The Appendix F diffusion results are mentioned in one sentence in the Conclusion. A small table or figure in the main body would strengthen the generalization claim beyond LLMs without requiring substantial space.

---

## Removed Points

*These points are flagged for removal; treat them with caution.*

1. **Appendix proof correctness** (harsh critic): The critic speculates that if the appendix proof of Theorem 1 is wrong, the variance reduction argument collapses. Per the hard rules, weaknesses about appendix content are inadmissible — the reproducibility statement explicitly confirms the proof is there. The retained minor weakness concerns only the lack of main-text intuition, not the proof's existence or correctness.

2. **Expressivity/parameter-count asymmetry as a structural weakness** (harsh critic): The paper explicitly designs QZO to update only quantization scales; criticizing the method for having fewer learnable parameters than MeZO misunderstands the design intent. The critic argues QZO "should explain when scale-only parameterization is sufficient," which is appropriate as a nice-to-have but not a weakness of the core paper.

3. **CB coincidence (both MeZO and QZO = 67.9 for OPT-6.7B)** (harsh critic): One matching result on a small, noisy dataset is not a meaningful concern. Removed as trivial.

4. **QLoRA "asymmetry favors the baseline" defense** (possible counterargument): Per the hard rules, REMOVE unfair comparisons only where the asymmetry *favors the baseline*. Here, omitting QLoRA hides a potential direct competitor — the asymmetry does not favor QZO. This stays as a Major weakness.

5. **Strength: "QZO uses ~1% of FLOPs of MeZO"** (strength finder): The OPT-6.7B anomaly is the sole basis for this claim; Llama results show 2–7%, not 1%. Because this strength conflicts with the verified FLOP inconsistency weakness, it is removed from Strengths per the filtering rules.

6. **Generic "important problem" strength**: Removed per filtering discipline — not specific to this paper's contribution.

---

## Novel Insights

The paper implicitly surfaces a phenomenon it does not fully explain: why does optimizing only ~50M quantization-scale parameters (~0.75% of total) via ZO frequently match or exceed optimizing all 6.7B parameters via ZO? This suggests that quantization scales, as the continuous degrees of freedom mediating between a fixed integer lattice and the effective weight space, encode disproportionately high task-relevant information per parameter. More broadly, for ZO fine-tuning specifically — where gradient estimates are inherently noisy over high-dimensional parameter spaces — concentrating perturbations on a small, well-chosen parameter set may outperform diffusing signal across the full model, a principle applicable beyond quantization.

---

## Suggestions

1. Audit Table 2 for the OPT-6.7B QZO FLOP entry (8.19 × 10¹³); provide an explicit FLOP accounting formula (steps × forward-pass FLOPs × multiplier) verifiable across all three models, and correct the "1% of FLOPs" claim in Section 4.2.
2. Add a QLoRA row (at minimum memory footprint and one task score such as SST-2 or SQuAD) to Table 1 or as a supplemental comparison table.
3. Add a 1–2 paragraph intuition for Theorem 1 in the main text explaining why clipping d (a function of z) before forming d' · z preserves unbiasedness — this will make the theoretical section self-contained for readers who do not read appendices.
4. Qualify the "on par with MeZO" summary in Section 4.2 to acknowledge the CB gap for Llama-3.1-8B and discuss what this reveals about the limitations of scale-only fine-tuning.

---

## Score and Decision

**Calibration summary:**

| Path | Avg Score | Round | Comparison to QZO |
|------|-----------|-------|-------------------|
| myYzr50xBh.md | 5.80 | R1/R2 | ZO + sparse quantization; less principled design, narrower experiment coverage. QZO is more principled and broader → QZO above this. |
| bEqI61iBue.md | 5.67 | R2 | Hessian-informed ZO; similar theoretical weight and experiment scope. QZO comparable. |
| QhxjQOMdDF.md | 6.00 | R1 | ZO + first-order hybrid; similar contribution level and experimental breadth. QZO comparable. |
| zcx6rIMbbR.md | 5.40 | R1 | Three-stage quantized fine-tuning; rejected. Narrower and less compelling. QZO clearly above. |
| 9BiVepgmWW.md | 7.00 | R1/R2 | Low-rank ZO with convergence guarantees and multiple model sizes. Stronger theoretical framing. QZO below this. |
| xw29VvOMmU.md | 6.75 | R2 | LQ-LoRA; quantized + low-rank decomposition, tests up to 70B, cleaner baselines. QZO below this. |
| vqJZb9SX1T.md | 4.00 | R1 | ZO optimizer; rejected. Less novel. QZO clearly above. |
| 6Mdvq0bPyG.md | 3.00 | R1 | EfficientQAT; rejected, incremental. QZO clearly above. |
| E4Fk3YuG56.md | 8.50 | R1 | Cut Cross-Entropy (memory-efficient LLM training kernel); much more impactful. QZO below. |

**Round 1 bracket**: 5.5–7.0. The paper is clearly above the rejected 4.0-anchors and below the strong 7.0+ anchors.

**Round 2 narrowing**: QZO sits above myYzr50xBh (5.8) due to a more principled mechanism and broader experimental coverage, but below xw29VvOMmU (6.75) and 9BiVepgmWW (7.0) which have stronger theoretical grounding and larger-scale experiments. The FLOP accounting inconsistency (Major) and missing QLoRA comparison (Major) prevent a score above 6.0–6.5. The paper is most comparable to QhxjQOMdDF (6.0), which is also an incremental-but-sound memory-efficient ZO paper accepted at a similar contribution level.

**Final score: 6.0 (Accept)**

The core mechanism is sound and practically significant, experiments are comprehensive for a paper of this type, and the method genuinely enables a new capability (quantized ZO fine-tuning without re-quantization). The two Major weaknesses are addressable in a rebuttal or revision and do not invalidate the contribution, but they prevent a higher score.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>