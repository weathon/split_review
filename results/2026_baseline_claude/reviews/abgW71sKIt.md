---

## Summary

This paper investigates why naive output-matching (aligning quantized model outputs to full-precision outputs) underperforms weight-matching in 1-bit post-training quantization (PTQ) for LLMs. The authors identify three root causes: (1) layer-wise output matching does not guarantee block-level loss reduction, (2) accumulated activation errors cause the alignment target to drift from the true full-precision output, and (3) naive output alignment distorts token similarity matrices, degrading attention. Based on these findings, they propose a method that reformulates the quantization objective to use full-precision activations as the target (Output Error), introduces an Attention Matrix Preservation (AMP) mechanism via gradient-sign masking, and restricts output alignment to the last FC layer of each block. Empirical results on OPT (1.3B–30B) and LLaMA-2/3 (7B–13B) consistently surpass prior 1-bit PTQ baselines on perplexity and zero-shot accuracy.

---

## Strengths

- **Principled diagnostic analysis.** Section 3 provides concrete, reproducible preliminary experiments on LLaMA-2-7B that directly motivate each design decision. Figure 1 shows that naive layer-wise output alignment raises block-level loss relative to weight alignment for a non-trivial fraction of layers; Figure 2 shows the growing divergence between Activation-conditioned Error and Output Error as quantization depth increases. Each design element maps cleanly to an identified failure mode.

- **AMP achieves substantial practical impact.** Table 3 shows that removing AMP raises LLaMA-2-7B perplexity from 19.25 to 29.12 (C4) and from 15.42 to 26.24 (WikiText2), a ~10-point degradation. The hypothesis that RMSNorm makes LLaMA more sensitive to directional perturbation than OPT's LayerNorm is a testable and plausible mechanistic explanation.

- **Consistent empirical superiority.** The method outperforms all 1-bit PTQ baselines (PB-LLM, BiLLM, ARB-RC, ARB-X) on C4 and WikiText2 across all model families and scales, with particularly large gains on smaller models (e.g., 27.70→24.69 PPL on OPT-1.3B/C4 vs. ARB-RC, and 47.60→24.69 vs. ARB-X). Ablation experiments (Tables 3 and 4) isolate the contribution of both the Output Error objective and AMP individually.

- **Closed-form optimization.** The alternating optimization over (B, α_r, α_c) with closed-form updates (Eqs. 5–8) keeps computational overhead low while operating under the new Output Error objective, which is non-trivial because the full-precision input X and quantized input X̂ are both involved.

---

## Weaknesses

### Fatal
None.

### Major

1. **Unexplained catastrophic failure on LLaMA-2-7B / PTB.** The method scores 3166 PPL on PTB for LLaMA-2-7B, versus 657 (PB-LLM), 681 (ARB-X), and 763 (ARB-RC). All baselines are far better. The authors dismiss this by saying "the large perplexity indicates that the metric cannot provide a meaningful evaluation," but this is incorrect: the other methods achieve well-differentiated, finite values on the same metric, so the metric clearly functions. A 4× increase over already-high baselines suggests the method is catastrophically destabilizing this model on this distribution. No diagnosis or ablation is provided. This is the most significant empirical weakness and casts doubt on the method's reliability.

2. **Selective application heuristic lacks ablation.** The decision to apply output alignment exclusively to the last FC layer of each block is presented as a design choice motivated by it having "the most direct impact on block loss." However, no ablation is shown comparing this against alternatives (e.g., all layers, first layer, most salient layer as determined by Figure 1). This is important because the choice is a core part of the algorithm and has no analytical justification.

3. **Equation (2) contains a clear error in the ARB-X objective.** The ARB-X loss is written as `||X̂Ŵ − X̂Ŵ||² = Tr[(W − Ŵ)^T S(W − Ŵ)]`, but the left-hand side is identically zero. The intended expression is `||X̂W − X̂Ŵ||²`. Because ARB-X is the primary comparison baseline whose limitations motivate the entire paper, an error in how its objective is stated undermines the rigour of the exposition.

### Minor

1. **Gram matrix mismatch.** In Eq. (2) for the ARB-X objective, the Gram matrix is `Ŝ = X̂^T X̂`, but in the corrected form `||X̂W − X̂Ŵ||²` this would expand to `Tr[(W − Ŵ)^T X̂^T X̂(W − Ŵ)]`. The notation introduced in Eq. (5) uses `S = X̂^T X` (cross-Gram matrix) rather than `Ŝ = X̂^T X̂`, but the relationship and distinction between S and Ŝ across equations (2)–(8) is not always made explicit.

2. **Coverage of larger LLaMA models.** 1-bit quantization is most practically relevant for very large models (e.g., LLaMA-2-70B, LLaMA-3-70B) where the memory savings are most critical. Results are limited to ≤13B parameters.

3. **Overhead analysis is deferred to the appendix.** For a PTQ paper, calibration time and memory cost are first-class concerns, yet they are absent from the main text.

### Trivial
None beyond the equation typo already flagged above.

---

## Nice-to-Haves

- An ablation comparing "apply output alignment to last FC layer" vs. "apply to the layer with lowest ARB-X block-level loss (from Figure 1)" would directly validate the selective application strategy.
- A convergence study (number of alternating iterations vs. performance) would characterize the practical efficiency of the closed-form optimization loop.
- A direct inspection of the token similarity matrices for both OPT and LLaMA (with and without AMP) beyond the description in Section 5.3 would clarify the claimed RMSNorm mechanism.

---

## Novel Insights

The most genuinely novel insight is the demonstration that output alignment, despite being a more directly aligned objective, can be *worse* than weight alignment at the block level for a non-trivial fraction of layers—and that this failure is architecture-dependent. The proposed explanation linking RMSNorm (LLaMA) vs. LayerNorm (OPT) to differential vulnerability to directional perturbation of token representations is insightful and could have broader implications for understanding architecture-specific sensitivity in PTQ. The formulation of the AMP objective (maximizing the Frobenius inner product of token-similarity matrices as a proxy for preserving learned attention structure) is a useful framing that may generalize to other compression settings.

---

## Suggestions

- Provide a thorough investigation of the LLaMA-2-7B / PTB failure (3166 PPL). Determine whether it is caused by AMP misapplication, by accumulation error in the PTB distribution, or by a bug. If the PTB distribution is truly out-of-distribution for LLaMA-2-7B even for baselines, explain *why* the method is 4× worse rather than dismissing the metric.
- Correct Eq. (2) to state `||X̂W − X̂Ŵ||²` with explicit parentheses.
- Add a Table ablating the selective-application heuristic (last-FC vs. all-layers vs. first-FC) to empirically justify the design choice.
- Move at least the summary of overhead numbers (calibration wall time, peak memory) to the main text.

---

## Score and Decision

The paper provides a clear diagnostic framework for understanding why naive output alignment fails in 1-bit PTQ, proposes principled solutions for each identified issue, and demonstrates consistent empirical gains across a range of models and benchmarks. The AMP mechanism is novel and impactful (10-point PPL improvement on LLaMA-2-7B). The principal concern is the unexplained and severe regression on LLaMA-2-7B/PTB, which the authors do not diagnose. The missing ablation on the selective-application heuristic is a secondary concern. Overall, the contributions are meaningful and the paper advances the state of 1-bit PTQ, but the unaddressed anomaly tempers confidence.

MY FINAL SCORE: <score>6</score>
MY FINAL DECISION: <decision>Accept</decision>