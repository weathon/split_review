Now I have a clear picture. Let me summarize my calibration analysis and write the final review.

**Bracket from Round 1:** QZO sits roughly between 4.5 and 6.5 based on comparison with relevant ZO/quantization fine-tuning papers.

**Round 2 narrowing:** The closest anchors confirm placement around 5.0-6.0. QZO is:
- Clearly stronger than SCoM-ZO (4.00), SubZero (4.25), MeZO-A3dam (4.75), Three-Stage (5.40)
- Comparable to Sparse MeZO (5.50, rejected) and ZO+Static Sparsity (5.80, accepted)
- Clearly weaker than HiZOO (5.67 — but HiZOO has stronger theory), LoRAM (6.20), QA-LoRA (6.33), LQ-LoRA (6.75)

QZO has broader empirical evaluation than ZO+Static Sparsity (5.80) but the missing QLoRA comparison is a notable gap. I place QZO at **5.5**.

---

## Summary
QZO proposes fine-tuning quantized LLMs by applying zeroth-order optimization to continuous quantization scale parameters rather than discrete weights, with directional derivative clipping (DDC) to stabilize training. The method achieves ~18× memory reduction vs. 16-bit AdamW fine-tuning, is demonstrated across OPT and Llama models on five NLP benchmarks with both 4-bit (GPTQ) and 2-bit (AQLM) quantization, and enables 13B model fine-tuning on a single 24GB GPU.

## Strengths
- **Clever core formulation (Q-SPSA).** Perturbing quantization scales rather than discrete weights cleanly resolves the precision mismatch that blocks ZO from quantized models. Decomposing the model as Δ⊙θ̄ and perturbing only Δ (Definition 3.3, Eq. 5) is simple, well-motivated, and validated for both scalar-based (GPTQ, 4-bit) and codebook-based (AQLM, 2-bit) quantization (Tables 1 and 3).
- **DDC is validated empirically.** Figure 2 shows training collapses to NaN at step 22 without DDC but remains stable for 1,000+ steps with it. Figure 3 demonstrates robustness to the clipping threshold C for C ≥ 75.
- **Strong memory and compute efficiency backed by data.** Table 2 shows QZO trains ~1% of the parameters and uses ~1% of the FLOPs of MeZO (e.g., 8.19×10^13 vs 9.91×10^17 for OPT-6.7B) while achieving competitive accuracy. Memory profiling confirms 3× less GPU memory than MeZO.
- **Broad empirical coverage.** Three model families (OPT-6.7B, Llama-2-7B, Llama-3.1-8B), five NLP benchmarks spanning classification and generation (Table 1), plus 2-bit extreme quantization on Llama-2-13B (Table 3). QZO consistently beats the zero-shot quantized baseline.
- **Orthogonality to PTQ is demonstrated, not just claimed.** Validation with both GPTQ (scalar-based, 4-bit) and AQLM (codebook-based, 2-bit) provides concrete evidence of the plug-and-play property.

## Weaknesses

### Fatal
None.

### Major
- **Missing QLoRA comparison.** QLoRA (Dettmers et al., 2023) is the most prominent method for memory-efficient fine-tuning of quantized LLMs. It is cited in the references but never used as a baseline, nor discussed in the related work section. Since the paper's core claim is about enabling memory-efficient fine-tuning of quantized models, the absence of a QLoRA comparison makes it difficult to assess QZO's practical advantage over the existing standard approach. While QZO and QLoRA use fundamentally different strategies (zero-order vs. backpropagation + LoRA), they compete for the same use case and a comparison is needed to establish QZO's value proposition.

### Minor
- **Unexplained anomalous result.** For Llama-3.1-8B on CB, QZO scores 69.6 vs. MeZO's 91.1 — a 21.5-point gap. This directly contradicts the claim that QZO "performs on par with MeZO" and is never discussed or explained. If it reflects a real failure mode, this is important. If it is noise, error bars or multiple runs would clarify.
- **No error bars or multiple runs.** All results in Tables 1-3 are single-run. ZO methods are known for high gradient variance, and single-run results provide no information about whether performance differences are statistically meaningful.
- **2-bit results are thin.** Table 3 reports only Llama-2-13B with AQLM, comparing QZO against the zero-shot quantized baseline only. Several improvements are marginal (RTE: 53.1→54.5, BoolQ: 69.2→70.2). No comparison against MeZO or any other fine-tuning method.
- **Fine-tuning upper bound uses SGD, not AdamW.** The paper acknowledges this is due to resource constraints (footnote 2). SGD likely understates the gap between QZO and full fine-tuning, weakening the upper-bound comparison.
- **Theorem 1 depends on stripped appendix.** The claim that the clipped gradient estimate is unbiased (Theorem 1) cannot be verified without the appendix proof. The practical DDC results stand regardless, but the theoretical claim is unverifiable as presented.

### Trivial
- **Framing could be more precise about parameter count.** The abstract and introduction could be read as claiming full fine-tuning, when in practice only ~1% of parameters (quantization scales) are updated. Table 2 makes the numbers clear, but earlier framing could be sharper.
- **Algorithm 1 pseudocode shows per-parameter perturbation**, while the text states per-layer perturbation is used in practice. The paper acknowledges this discrepancy but the pseudocode remains inconsistent.

## Nice-to-Haves
- Characterize what QZO can and cannot learn given that each scale multiplicatively controls 128 weights (for group size 128).
- Study the effect of quantization group size on the accuracy-memory trade-off.
- Compare DDC to standard gradient clipping used in ZO training.

## Removed Points
These points are flagged to be removed, treat them with caution.

- **18× figure attribution criticism (from Harsh Critic):** The claim that 18× conflates quantization savings with ZO savings. The paper is technically correct — the total reduction is 18× — and the breakdown is clear from context (4× from quantization, ~4.5× from ZO). Removed as a rhetoric preference, not a substance error.
- **"Inherently more efficient and flexible" claim about ZO-signSGD (from Harsh Critic):** This is a qualitative claim in the related work section, not a central result. The paper's experimental results provide the actual evidence. Removed as a nitpick about related work framing.
- **MeZO hyperparameters not reported (from Harsh Critic):** The paper states they use MeZO's official code. Using default hyperparameters from established open-source code is standard practice. Removed as a reproducibility nitpick.
- **Group size implications not discussed (from Harsh Critic):** Moved to Nice-to-Haves. This is an interesting direction but not a weakness — the paper uses standard GPTQ group size 128 throughout.
- **DDC vs. standard gradient clipping not discussed (from Harsh Critic):** Moved to Nice-to-Haves. The paper provides independent validation of DDC's effectiveness.
- **QZO framed as PEFT not full fine-tuning (from Harsh Critic):** The paper does not hide that only ~1% of parameters are trained — Table 2 explicitly reports trainable parameter counts. Addressed in Trivial weakness about framing precision.

## Novel Insights
The most striking empirical finding is in Table 2: by fine-tuning only quantization scales (~1% of parameters), QZO achieves competitive accuracy with MeZO while using ~1% of the FLOPs. This suggests that for many downstream NLP adaptations, adjusting per-group multiplicative scaling factors captures a surprising amount of the necessary parameter changes, pointing toward a new axis in the PEFT design space that is complementary to low-rank adaptation.

## Suggestions
- Add a QLoRA comparison on at least one model/dataset pair. This is the most important addition for establishing practical value.
- Report results with multiple random seeds (even just 3) and include standard deviations, or at minimum discuss the anomalous CB result.
- Expand the 2-bit experiments with a MeZO comparison to strengthen that section.

---

**Calibration anchors referenced:**

| Anchor | Score | Round | Comparison |
|--------|-------|-------|------------|
| SCoM-ZO/LeZO (vqJZb9SX1T) | 4.00 | R1 | QZO is stronger: broader evaluation, actual quantization integration, more models |
| SubZero (FK6T0U4Mg1) | 4.25 | R1 | QZO is stronger: cleaner core idea, quantization results, better empirical coverage |
| MeZO-A3dam (OBIuFjZzmp) | 4.75 | R1/R2 | QZO is stronger: more substantial contribution beyond optimizer tweaks |
| Three-Stage Optimization (zcx6rIMbbR) | 5.40 | R2 | Comparable; QZO has cleaner methodology and broader evaluation |
| Sparse MeZO (4Kw4KAoVnx) | 5.50 | R2 | Comparable; QZO's scale-perturbation idea is more novel than weight selection |
| HiZOO (bEqI61iBue) | 5.67 | R1 | HiZOO has stronger theoretical contribution; QZO has broader empirical coverage |
| ZO+Static Sparsity (myYzr50xBh) | 5.80 | R1/R2 | Closest match; both combine ZO+quantization. QZO has broader evaluation; both share missing-baseline concerns |
| LoRAM (s7DkcgpRxL) | 6.20 | R2 | QZO is weaker: LoRAM has more complete methodology and evaluation |
| QA-LoRA (WvFoJccpo8) | 6.33 | R1 | QZO is weaker: QA-LoRA has more mature contribution and stronger baselines |
| LQ-LoRA (xw29VvOMmU) | 6.75 | R1 | QZO is weaker: LQ-LoRA has ILP formulation, stronger theoretical grounding |

The paper sits between the rejected Sparse MeZO (5.50) and the accepted ZO+Static Sparsity (5.80). QZO's novel core idea and broader evaluation are offset by the missing QLoRA comparison, the unexplained CB anomaly, and thin 2-bit results. Final score: 5.5.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>