## Summary

The paper introduces TAK (Task Arithmetic with KFAC regularization), a dataless method for improving weight disentanglement in Task Arithmetic. The core insight is that, under model linearization, representation drift regularization reduces to a quadratic form involving the Jacobian Gram matrix — which equals the Generalized Gauss-Newton (GGN) matrix under squared loss. This link allows the authors to leverage KFAC, a well-established block-diagonal Kronecker approximation of the GGN, to build a pre-computable, data-free regularizer. Additionally, they propose a merging heuristic that accumulates per-task KFAC factors into a single surrogate, reducing storage and computational complexity from O(T) to O(1) in the number of tasks.

---

## Strengths

- **Principled theoretical derivation with a clean insight.** The reduction of representation drift (under linearization) to a GGN-type quadratic form is elegant and eliminates data dependence while preserving the regularization structure (Eq. 3). The connection to existing second-order optimization literature is well-placed.

- **State-of-the-art performance while being dataless.** On 8 Vision task negation, TAK surpasses τJp (which uses task data), achieving 3.4% target accuracy vs. τJp's 6.7% on ViT-B/32 (Table 2). On task addition, TAK matches τJp while being completely privacy-preserving.

- **O(1) scalability via the merging heuristic.** Eq. (8) reduces the multi-task complexity from O(T) to O(1). The empirical gap between the naïve O(T) formulation and the O(1) surrogate is marginal for medium-sized architectures (Table 3), validating the approximation in practice.

- **Practical efficiency.** KFAC pre-computation for all 8 Vision tasks takes only ~4 minutes using MC=1 (vs. 199 minutes with exact computation). During training, the overhead is roughly one-third of τJp. No inference-time overhead is incurred.

- **Thorough ablations and analysis.** The paper systematically investigates: number of KFAC estimation examples/MC samples, KFAC compression strategies (quantization, pruning, SVD, block-diagonalization), frequency of regularizer application, task localization behavior, and robustness to α-scaling. These provide strong evidence that design choices are well-calibrated.

- **Robustness to hyperparameter tuning.** TAK at α=1 (no tuning) consistently achieves near-peak performance, a significant practical advantage over methods that require cross-task validation sets.

---

## Weaknesses

### Fatal
None.

### Major

- **The merging heuristic (Eq. 8) lacks theoretical justification.** The decomposition $\sum_{t} \lambda_t (B_t \otimes A_t) \approx (\sum_t B_t) \otimes (\sum_t \lambda_t A_t)$ is presented as a heuristic with no bound on approximation quality. While experiments show marginal gaps on ViT-B/16 and T5-base, the gap is non-negligible on ViT-B/32 (86.5 naïve vs. 85.8 accumulated at α=1). The paper's own claim that smaller architectures are more sensitive to curvature quality (which is where the gap is most pronounced) raises the concern that this heuristic may degrade further in challenging regimes. A brief theoretical analysis — or at least conditions under which the heuristic is exact or tightly bounded — would significantly strengthen this component.

- **The non-linear regime application is ad hoc.** The theoretical derivation holds strictly under linearization, yet the paper extends to the non-linear setting by combining TAK with Attention-Only Fine-Tuning (which approximately induces linear dynamics). While this empirically works, the justification is loose: results in the non-linear regime show TAK + Attention FT outperforms baselines, but this benefit is partially attributed to the Attention FT itself. A more careful ablation isolating the contribution of KFAC vs. the choice of Attention FT in this regime is missing.

### Minor

- **Table 1 comparison is incomplete for TaLoS.** TaLoS (dataless competitor) is only reported with best α, not at α=1, making the comparison at fixed α incomplete for the non-linear regime.

- **Scalability to large models is underexplored.** The paper notes that KFAC storage scales quadratically with layer width, and applies compression strategies as a workaround. However, the evaluation stops at ViT-L/14 (~300M parameters). KFAC for truly large-scale models (>1B parameters) is not addressed and could be a real barrier.

### Trivial

- In Eq. (8), the λ_t weights appear asymmetrically in the merged approximation (weighting A^l but not B^l). This asymmetry is not discussed.

---

## Nice-to-Haves

- A theoretical analysis of the merging heuristic error would be very valuable; even a simplified single-layer case would clarify the conditions under which it holds.
- Evaluation on a larger language model (e.g., Flan-T5-XL or a decoder-only LLM) would demonstrate broader applicability.
- A comparison with Fisher Information Matrix-based regularizers (which also relate to the GGN) in the TA context would help position the contribution.

---

## Novel Insights

The principal novel insight is the identification that representation drift regularization under linearization is structurally equivalent to a GGN quadratic form — a perspective that simultaneously removes data dependency and bridges task arithmetic to the rich literature on curvature approximations. This reformulation, while straightforward in retrospect, is non-obvious and opens up a principled design space: different curvature approximations (diagonal, KFAC, Kronecker-free) yield different regularizers with different accuracy-efficiency trade-offs. The merging heuristic (Eq. 8) is a practically useful aggregation scheme that enables constant-complexity multi-task regularization without requiring per-task storage. The finding that KFAC matrices can be bundled and shared alongside pretrained checkpoints — much like optimizer accumulators — is a valuable conceptual contribution for the model-sharing ecosystem.

---

## Suggestions

- Provide a theoretical bound or sufficient condition under which the Kronecker merging heuristic (Eq. 8) is exact or well-approximated — even a simple commutative special case would clarify the regime of validity.
- Include ablations in the non-linear regime where TAK regularization is applied without Attention FT, to isolate its standalone contribution in that setting.
- Extend Table 3 to include results under very high T (e.g., T=20), since the practical benefit of O(1) complexity is more pronounced in that regime.

---

## Score and Decision

TAK is a well-executed paper that makes a clean and insightful theoretical contribution (representation drift ↔ GGN), backs it with comprehensive experiments across vision and language benchmarks, achieves state-of-the-art results while being dataless, and provides thorough ablations that build trust in the design. The main limitation — the lack of theoretical grounding for the merging heuristic — is real but does not undermine the core contribution. The task negation results (outperforming the data-using τJp) and the robustness to α-scaling are particularly strong. This is clearly above the venue mean and merits acceptance.

MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>