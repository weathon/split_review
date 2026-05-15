Now I have thoroughly verified each claim against the paper. Let me write the final consolidated review.

## Summary

This paper presents a second-order theoretical framework for model compositionality in non-linear networks, showing that the composed model's risk can be upper-bounded by individual risks when models remain in the pre-training basin. The theory motivates two complementary incremental learning algorithms — ITA (individual training with a pre-training-anchored regularizer) and ILE (ensemble training minimizing pairwise task-vector distances) — both with constant per-task complexity. Experiments on class-incremental benchmarks show strong accuracy gains over prior compositional methods, with additional demonstrations of zero-shot specialization and unlearning via task-vector arithmetic.

## Strengths

- **Generalizes compositionality theory to non-linear networks via second-order expansion.** The Jensen inequality (Eq. 3–4) is derived for the second-order approximation of the loss around pre-training weights, and the paper explicitly contrasts this with prior work that required linearized networks (Eq. 5–6). This provides a principled explanation for why staying near the pre-training basin promotes compositionality, extending beyond the tangent-space regime. (Lines 48–69)

- **Theorem 1 provides an exact decomposition of the ensemble loss into individual losses plus a non-negative Riemannian distance term Ω.** This analytic gap (Eq. 8–9) is then approximated by a tractable diagonal-Fisher regularizer, giving a principled basis for the regularization used in both algorithms rather than an ad hoc penalty. (Lines 106–136)

- **Two dual algorithms (ITA and ILE) with strong empirical results across multiple benchmarks.** Table 1 reports final accuracy on five standard class-incremental datasets plus two domain-shifted ones. Both methods outperform or match strong baselines (SEED, APT, InfLoRA, TMC) on most datasets, sometimes by large margins (e.g., +5–10% on CIFAR-100 and CUB-200). Performance on domain-shifted datasets (Resisc45, CropDisease) is a genuine strength, showing robustness when pre-training optimality is challenged. (Lines 180–184)

- **Computational efficiency is a concrete advantage.** Both methods achieve O(1) per-task inference cost via cumulative averaging of weights. The closed-form gradients for the regularizer further reduce overhead. (Lines 163, also developed in Section 3)

- **Ablation and analysis confirm the role of the proposed regularization.** Table 2 shows that removing the EWC-like term significantly degrades accuracy. Figure 1 visualizes how the regularization tightens the Jensen bound, directly supporting the theoretical claim. (Lines 186–195)

## Weaknesses

### Fatal
None.

### Major

- **Specialization and unlearning results lack baseline breadth.** The composition experiments (Tables 2 and 3 in the paper) compare only against TMC (linearized models). The main evaluation (Table 1) includes SEED, APT, and InfLoRA — methods that also support some form of composition — but these are absent from the specialization/unlearning experiments. The paper's claims about "better disentanglement" and "more effective unlearning" rest on a single baseline comparison, which is insufficient to substantiate these central claims. (Line 200: "The results are in ... where we compare with TMC.")

### Minor

- **The core theoretical guarantee applies to the second-order approximation, not the exact loss, and the gap is not quantified.** While the paper is transparent about this (lines 48–53, 69, 161, and Section 6), the practical validity of the approximation depends on task vectors remaining small and the Hessian PSD assumption holding. Neither condition is empirically verified (e.g., measuring the Taylor remainder or the smallest Hessian eigenvalue). The paper's claim that linear probing "enforces the optimality of pre-training weights" (line 157) is overstated — LP only updates the classification head, not the backbone, so the gradient on new tasks may be non-zero at θ_ptr for backbone parameters, and the Hessian PSD condition is unverified.

- **The EWC-like regularizer derivation relies on the assumption that τ_t is small (linearizing the KL divergence).** In incremental settings with many tasks or large distribution shifts, later task vectors may drift sufficiently that this approximation degrades. The paper acknowledges drift as a concern in Section 6 but does not analyze how much drift is tolerable.

- **The "constant memory" claim is qualified but the qualification is somewhat ambiguous.** The paper states O(1) memory "provided we are not interested in more complex forms of composition than the simplest uniform average (as required for model customization and unlearning)" (line 163). However, specialization and unlearning (which the paper evaluates) require storing individual task vectors, which is O(T). The constant-memory claim holds only for the basic composition setting, not for the use cases the paper highlights as contributions.

### Trivial

- Figure 2's analysis of the empirical risk vs. upper bound uses the second-order approximation (quadell), not the true loss. The practical implications are somewhat unclear without verification that the third-order remainder is negligible for the plotted trajectories.

## Nice-to-Haves

- Quantify the gap between the second-order approximation and the true loss during training (e.g., plot the Taylor remainder) to establish when the theory is empirically trustworthy.
- Compare specialization/unlearning against the full set of baselines used in the main experiments (SEED, APT, InfLoRA) to strengthen those claims.
- Evaluate on open-vocabulary models (e.g., CLIP), as suggested in the future work section.
- Empirically check the Hessian PSD condition after linear probing by measuring the smallest eigenvalue on new-task data.

## Removed Points

- *"The critical distinction between the exact risk and its second-order approximation is glossed over"* — The paper explicitly addresses this at lines 48–53, 69, 161, and in Section 6. Not factual.
- *"The transition from quadell to ell in later sections should be carefully justified"* — The paper explicitly states at line 161: "the full loss ell is instead employed in our algorithms" and explains why this is standard practice. Not a missing justification.
- *"Standard deviations are promised in supplementary but not shown in the main paper"* — Standard practice; results are averaged over three runs with SD in supplementary (line 182). Not a weakness.
- *Missing related works* — No external sources to confirm existence; rule forbids this.
- *Formatting/style nitpicks and reproducibility nitpicks about trivial implementation details* — These are parser artifacts or standard practice.

## Novel Insights

The Harsh Critic's observation that the pre-consolidation step (linear probing) does not actually enforce the theoretical condition (Hessian PSD on new task data) is an insightful point that the paper does not fully grapple with. The paper asserts LP "enforces optimality" but then acknowledges on domain-shifted datasets (Resisc45, CropDisease) that "pre-training optimality is challenged" — only to note that the method still works well. This suggests an interesting decoupling: the theory may provide useful regularization even when its conditions are only approximately met, hinting that the practical value of the second-order formulation may lie more in the structure of the regularizer than in strict satisfaction of the Jensen bound. A deeper investigation of this robustness would be valuable future work.

## Suggestions

1. **Expand composition baselines.** Compare specialization and unlearning against SEED, APT, and InfLoRA — all already used in the main evaluation — to support the disentanglement claims more convincingly.

2. **Temper the theoretical framing.** The paper should explicitly note that linear probing does not fully enforce the Hessian PSD condition on backbone parameters, and clarify that the theory motivates the regularizer rather than providing a guarantee for the exact loss used in algorithms.

3. **Add an empirical diagnostic.** A simple plot of the Taylor remainder (or a measure of task-vector magnitude relative to the pre-training basin) over the incremental sequence would help readers assess when the second-order approximation is trustworthy.

## Score and Decision

This paper makes a genuine contribution: a second-order theoretical framework for compositionality that generalizes beyond linearized networks, yielding two practical algorithms with strong results on standard benchmarks. The main weakness — limited composition baselines — is significant but does not invalidate the core incremental learning contributions, which are well-supported. The theory-approximation gap is transparently acknowledged but could be better characterized. Overall, the paper's strengths (novel theory, strong empirical results, practical algorithms) outweigh its weaknesses.

**MY FINAL SCORE: <pineapple>7.0</pineapple>**
**MY FINAL DECISION: <orange>Accept</orange>**