Now let me do the calibration searches to score the paper appropriately.Based on Round 1, I place the paper in the **5–6.5 bracket**. Now let me narrow:Now I have sufficient calibration data to write the final review. Let me synthesize everything.

---

## Summary

This paper proposes Overflow-Aware Activity Regularization (OAR), a training-time technique that mitigates ciphertext message-space overflow in CGGI-based FHE evaluation of quantized RNNs. OAR identifies that overflow regions are not uniformly harmful — some "correct" regions produce the right sign activation output despite wrapping modulo *k* — and introduces a periodic hat-function regularizer that nudges pre-activations from incorrect into correct overflow regions. Combined with ModSign (a modulus-aware binarization function that closes the training-inference gap), OAR enables use of a smaller plaintext modulus (5–6 bit), recovering accuracy lost by the single-ciphertext quantization procedure of Anonymous [2025]. The resulting system achieves 90.82% top-1 accuracy on encrypted MNIST with 1.9M parameters in 2.1s per sample using two A100 GPUs.

---

## Strengths

1. **Novel, mathematically well-motivated regularizer.** The two key observations — that overflow regions divide into "correct" and "incorrect" for sign activation (Observation 1, Section 3), and that incorrect values can be nudged into neighboring correct regions (Observation 2) — are non-trivial and elegantly formalized. The resulting periodic hat-function OAR (Eqs. 2–4) penalizes only incorrect-region values and limits displacement to at most *k*/4 positions, a design feature that reduces optimization strain relative to L₁ regularization.

2. **Substantial accuracy recovery at target bit-widths.** Table 1 demonstrates that OAR boosts test accuracy by +71% (5-bit) and +43% (6-bit) relative to the non-OAR baseline, with both settings using ModSign. This directly substantiates the core claim that OAR enables practical single-ciphertext RNN evaluation with small plaintext moduli.

3. **Validated encrypted-vs-plaintext consistency.** Table 3 (parameter set 2) reports a gap of only 0.17% between encrypted and plaintext top-1 accuracy, and Table 4 shows near-zero activation percent-differences and an output-layer MAE of 2.02 against a possible maximum of 1024 — providing direct, quantitative evidence that OAR enables accurate encrypted computation.

4. **Demonstrated scalability to a larger network.** Section 4.1.4 successfully trains an 8.48M-parameter RNN across 128 timesteps at 92.69% plaintext accuracy, and the same model evaluates over encrypted data within 0.17% of plaintext (Table 3), showing OAR generalizes beyond the baseline MNIST setup.

---

## Weaknesses

### Fatal
None.

### Major

**Missing ablation between OAR and ModSign.** Section 3.2 asserts that "experimenting with the [ModSign] function itself, the model did not quantize and perform well," but presents no supporting data. Section 4.1.1 compares models with and without OAR, but both settings use ModSign — so there is no condition that isolates the contribution of OAR alone, ModSign alone, or their interaction. This is the paper's core contribution: the combination of OAR and ModSign is described as necessary, yet the necessity of each component is not empirically demonstrated. A 2×2 ablation table (sign vs. ModSign, OAR vs. no-OAR) across 5- and 6-bit would directly establish whether both components are independently necessary and substantiate the claim that "ModSign alone is insufficient."

**Evaluation is limited to a single synthetic task.** The only benchmark is MNIST processed row-by-row, with the "enlarged" experiment simply upscaling the same images to 128×128. The introduction motivates the work with speech recognition and financial forecasting — applications where long-range recurrence actually matters — but neither is evaluated. Processing sequential pixel rows is not representative of tasks where recurrent dynamics are complex and critical. Whether OAR generalizes to richer temporal dependencies (and whether its hyperparameter sensitivity, visible in Table 2, remains manageable there) is entirely untested. For a paper titled "towards practical large-scale privacy-preserving RNNs," this limits the strength of the practical claim.

### Minor

**Extreme hyperparameter sensitivity without selection guidance.** Table 2 reveals that 5-bit accuracy shifts by more than 60% between regularization rates of 10⁻⁵ and 10⁻⁴. The paper describes this as "expected due to the finer granularity of the 5-bit domain," but offers no procedure for selecting the regularization rate on a new task other than grid search. For a method proposed as a practical tool, this is a real usability concern.

**The framing of the 274x latency improvement partially overreaches.** Section 1 (line 18) introduces the 274x figure prominently. Section 5 does contextualize it — comparing a full system (CGGI + GPU + OAR) against SHE's CKKS-based CPU-evaluated system on a different dataset and task — but the introduction framing gives the reader the impression that OAR is primarily responsible for this speedup. The actual contribution of OAR to latency is indirect: by enabling a smaller plaintext modulus (6-bit instead of 11-bit), it permits smaller encryption parameters, yielding faster PBS. A brief statement quantifying OAR's specific contribution to the latency reduction versus the inherited gains from the CGGI scheme and GPU acceleration would remove ambiguity.

**The 8% accuracy gap from full precision is underanalyzed.** Section 5 acknowledges "an 8% drop from the 99% accuracy of full-precision plaintext MNIST evaluation," which is a consequence of the binary-ternary quantization scheme from Anonymous [2025] compounded by the 6-bit modulus constraint — not something OAR introduces or resolves. Given the "practical" framing of the title, a brief analysis of this cost (e.g., whether it is intrinsic to the quantization scheme or whether OAR could partially close it with further tuning) would strengthen the paper's honesty about its scope.

### Trivial
None warranting separate mention.

---

## Nice-to-Haves

- A latency decomposition comparing the regular model at 6-bit (with OAR) vs. the minimum bit-width required without OAR to achieve comparable accuracy, translated into wall-clock latency. This would quantify OAR's specific contribution to inference efficiency and is the most compelling way to present the method's practical value.
- A brief convergence comparison between OAR and an L₁-toward-zero baseline during quantization-aware training, to empirically validate the design claim that limiting displacement to k/4 reduces optimization strain.
- Discussion of training cost: 1000 epochs of quantization-aware training on a 1.9M-parameter RNN on top of a grid search over regularization rates is non-trivial, and the practical overhead matters for the "practical" framing.

---

## Removed Points

*These points are flagged to be removed; treat them with caution.*

- **Critic: "comparison is between incommensurable systems" as a fatal flaw.** The paper (Section 5) is transparent that it compares a full system against SHE using a different scheme, hardware, and dataset. This is a limitations framing issue, not a methodological error. Retained as a Minor weakness about framing.

- **Critic: "8% accuracy gap is not discussed."** Actually, the paper does mention it in Section 5: "an 8% drop from the 99% accuracy of full-precision plaintext MNIST evaluation." Retained as a Minor weakness about depth of analysis, not absence.

- **Critic: "FF(1024) OAR metric of 70.57% may be task-specific artifact."** The alternative explanation (errors cancel due to MNIST's classification structure) is speculative. The paper offers a reasonable interpretation (OAR is robust at larger scale). Demoted — not retained as a verified weakness.

- **Critic: "claim that OAR minimizes strain to k/4 positions would benefit from empirical validation."** Valid as a nice-to-have, not a weakness that undermines the contribution.

- **Strength Finder: "State-of-the-art encrypted RNN latency at large scale" as a general strength.** Retained but scoped: the state-of-the-art claim within the FHE-RNN subfield is supported, but only for MNIST evaluation.

---

## Novel Insights

The distinction between "correct" and "incorrect" overflow regions for the sign activation function in CGGI arithmetic — and the insight that a value in an incorrect region can be corrected by an additional overflow into the next correct region — is a genuinely non-trivial structural observation about FHE message-space arithmetic. The resulting periodic regularizer design (hat functions that penalize incorrect regions and are bounded in the displacement they require) is elegantly tailored to this structure in a way that general regularization (L₁, L₂) is not. This observation is transferable: any activation function that has correct/incorrect overflow regions for a given modulus could potentially exploit a similar regularization design, making the underlying insight more general than the MNIST evaluation suggests.

---

## Score and Decision

### Calibration

**Round 1 — Bracketing:**
- Low anchors (≤3): Privacy-preserving ML papers with fundamental flaws (avg 3.0; rejected). Not comparable — this paper has a real contribution.
- Mid anchors (4–7): FHE+neural-network engineering papers: DCT-CryptoNets (6.33, accepted), Encryption-Friendly LLM (6.33, accepted), MPC-Minimized Secure LLM (6.33, rejected), PUMA (5.0, rejected), Cheaper Inference with LBA (5.75, accepted), Ditto MPC Quantization (5.33, rejected).
- High anchors (≥8): Unrelated topic (DP few-shot, scaling laws), not useful for this paper.

**Initial bracket: 5.0–6.0**

**Round 2 — Narrowing:**
- **DCT-CryptoNets (6.33, accepted):** Broader evaluation (CIFAR-10, ImageNet), comparable technical cleverness. The paper under review evaluates only MNIST — a significant gap versus this anchor.
- **Cheaper Inference with LBA (5.75, accepted):** Very similar problem domain (accumulation overflow in quantized neural networks). That paper evaluates on ResNet/ImageNet + BERT/SQuAD; this paper evaluates only MNIST. The technical contribution (OAR's observation about correct/incorrect overflow regions) is more specific and elegant, but the evaluation breadth is clearly inferior.
- **PUMA (5.0, rejected):** Much larger-scale evaluation (LLaMA-7B), but rejected for applying existing techniques without sufficient novelty. The paper under review has more genuine novelty than PUMA but far narrower evaluation.
- **Ditto (5.33, rejected):** Quantization-aware MPC inference of Transformers — similar spirit. Rejected due to limited novelty; this paper is more novel in its core technique.

**Comparison summary:** The paper is strictly between PUMA (5.0) and Cheaper Inference (5.75). It is more novel than PUMA but evaluates on a far narrower task than either accepted paper in this range. The missing OAR/ModSign ablation is a notable gap that the accepted 5.75 paper does not have. The paper falls closer to 5.0 than 5.5 due to the limited evaluation scope and missing ablation.

**Final score: 5.0**

| Anchor | Score | Round | Comparison |
|---|---|---|---|
| sruGNQHd7t (Privacy by domain shifting) | 3.0 | R1 | Much weaker — no real cryptographic contribution |
| Mhu9iNGKqP (Layerwise polynomial approx FHE) | 4.5 | R1 | Below this paper in novelty |
| lPJUQsSIxm (DCT-CryptoNets) | 6.33 | R1/R2 | This paper is below — DCT-CryptoNets evaluates ImageNet |
| pbre0HKsfE (Encryption-Friendly LLM) | 6.33 | R1/R2 | This paper is below — broader tasks, larger models |
| beAlX6RjsW (MPC-Minimized Secure LLM) | 6.33 | R2 | This paper is below — broader evaluation |
| n39ilTxSDY (Ditto MPC Quantization) | 5.33 | R1 | This paper is comparable — similar novelty, similar scope |
| oOwDQl8haC (Cheaper Inference LBA) | 5.75 | R2 | This paper is slightly below — broader evaluation in that paper |
| x3LxHdZX0f (PUMA) | 5.0 | R2 | This paper is comparable or slightly above — more novel contribution |
| wJ3GeGLFmc (Sub-8-bit integer training) | 4.5 | R2 | This paper is above — stronger contribution |

**Round 1 bracket: 5.0–6.0. Round 2 narrows to 5.0–5.5. Final score: 5.0.**

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>