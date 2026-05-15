Now I have a thorough understanding of the paper and can verify the reviewer claims directly. Let me produce the consolidated review.

## Summary

This paper proposes Diffusion Bridge Network (DBN), a method to approximate deep ensemble predictions at reduced inference cost. DBN uses a conditional diffusion Schrödinger bridge (specifically I2SB) to learn a stochastic transport from a single ensemble member's logit distribution to the target ensemble's logit distribution, then distills the multi-step diffusion process into a single inference step. Experiments on CIFAR-10, CIFAR-100, and TinyImageNet show DBN achieves near-DE-3 performance with substantially lower FLOPs than the full ensemble and competing methods.

## Strengths

- **Direct transport from single member to ensemble output via diffusion bridge.** Unlike Bridge Network (BN), which requires learning low-loss subspaces between pairs of ensemble members and builds bridges that grow quadratically with M, DBN directly maps from a single source model's output to the ensemble output (Sec 3.2). This eliminates the expensive curve-learning step and reduces the number of bridges needed.

- **Inference cost reduction through distillation.** DBN adapts progressive distillation (Sec 3.4) to reduce the multi-step reverse diffusion to a single step, achieving practical single-pass inference. The resulting system requires only one lightweight score network evaluation beyond the source model forward pass (~1.166× relative FLOPs of a single network).

- **Higher ensemble capacity per bridge than BN.** A single DBN can absorb information from ~3 ensemble members, while BN is capped at 2 (Sec 4.3, Fig. 3). This means DBN needs fewer bridges to cover the same ensemble size.

- **Multi-bridge extension with shared source.** When a single DBN is insufficient, the paper proposes combining multiple DBNs that all share the same source model (Sec 3.6), so the additional cost per bridge is limited to the lightweight score network rather than a full model forward pass.

## Weaknesses

### Fatal
None.

### Major

- **Temperature distribution p_temp never specified.** The method's core construction of the source distribution (Eq. 4) depends critically on sampling the annealing temperature T from some distribution p_temp. The paper states "T ∼ p_temp" (line 126) but never defines this distribution, its range, or its functional form. Without this, the method is underspecified and the results cannot be independently reproduced or understood.

- **Poor calibration (ECE) acknowledged but not analyzed.** The paper reports that "DBN also shows poor ECE scores even with high performance in the other uncertainty metrics" (line 223). Since improving uncertainty quantification is a primary motivation of ensemble methods, this is a significant concern. The paper notes the problem but provides no analysis of why it occurs (e.g., is the stochasticity producing overconfident or underconfident predictions? does the confidence histogram match DE?), no ablations attempting to fix it, and no discussion of whether this undermines the practical value of the approach for uncertainty-aware tasks.

- **No comparison to a lightweight deterministic mapping.** DBN uses a complex stochastic framework (diffusion bridge + distillation) to approximate a deterministic target (the ensembled logits). A natural baseline is a lightweight MLP (matching the score network's cost) trained with L2 or KL loss to directly predict ensemble logits from source features. If such a simple baseline matches DBN's performance, the entire diffusion apparatus would be superfluous. While the paper compares to ensemble distillation (ED), ED distills the full student model, not a lightweight network on top of precomputed features, so it does not answer this question. This gap undermines the core claim that the diffusion bridge is the right tool for this task.

### Minor

- **Noise term ξ₁ in single-step inference never ablated.** During inference (Eq. 9), Gaussian noise ξ₁ is added to the distilled prediction. The paper never studies the effect of this noise—whether it helps or hurts accuracy and calibration, or whether it should be removed when distillation has already produced a near-deterministic mapping. This makes it impossible to understand what the stochastic component contributes.

- **No comparison to training the objective (Eq. 6) directly with N'=1.** The paper distills a 5-step diffusion into 1 step, but never compares this to directly training a single-step model with the same loss. This would isolate whether the distillation pipeline adds value beyond direct optimization.

- **Error bars and number of independent runs not reported.** The trade-off plots (Fig. 4) and capacity figure (Fig. 3) lack confidence intervals or error bars, and the number of independent trials is unspecified. Given the stochastic nature of the method (temperature sampling, diffusion noise), this makes it difficult to assess the statistical significance of the reported improvements.

- **Choice of pre-distillation steps (5) not justified.** The paper states "5 steps are enough to approximate the transport" (line 205) but provides no ablation or analysis of how this choice affects performance.

### Trivial

- The paper's claim of "sub-linear scaling" (line 26) describes Bridge Network, not DBN; the framing in the introduction could be clearer about which scaling property belongs to which method.

## Nice-to-Haves

- Reporting GPU-hours for training DBN vs. BN vs. ED would help quantify the training-time trade-off that the paper acknowledges as a limitation.
- Visualizing examples where DBN's confidence deviates from DE (failure cases for calibration) would strengthen the analysis of the ECE issue.
- A sensitivity study of p_temp (e.g., fixed T vs. random T, range of temperatures) would clarify a key design choice.

## Removed Points

These points are flagged to be removed, treat them with caution:

- *"Table 1 absent from text; no numerical results given"* — The table is imported via `\input{tables/classification}` (line 221). The parser strips external files; the table exists in the original submission. REMOVED (parser artifact).
- *"Diffusion framework is unjustified"* — The paper provides explicit justification in lines 134 (avoiding trivial copy solutions, satisfying I2SB's distributional requirement). The claim of no justification is incorrect. The related sub-point about missing deterministic baseline is kept in Major.
- *"Scaling argument is misleading; DBN cost grows linearly not sub-linearly"* — The paper never claims DBN has sub-linear scaling; it describes BN's sub-linear scaling in the introduction (line 26) and frames DBN's improvement as reducing BN's *quadratic* bridge count (line 28). The critic conflates BN's property with DBN's. REMOVED (factual misunderstanding).
- *"Derivation from I2SB to reverse SDE is hand-wavy"* — The paper references I2SB (Liu et al., 2023) which provides the full derivation; the presentation is a summary consistent with the reference. REMOVED (strawman).
- *"The capacity experiment shows DBN saturating at 3 ensembles, meaning a single DBN cannot handle even moderate ensemble sizes"* — The paper acknowledges this limitation and proposes the multi-bridge extension to address it (Sec 3.6). This is a design choice, not a failure. Weakened to minor (capacity limit noted by authors).
- *"Missing related works"* — REMOVED per hard rules (cannot verify existence of omitted citations).
- *"Formatting/style nitpicks"* — REMOVED per hard rules.

## Novel Insights

None beyond the paper's own contributions. The reviews largely converge on the same set of concerns (missing specification of p_temp, unexplained poor calibration, insufficient ablations) and the same strengths (novel application of DSB to fast ensembling, distillation to single-step inference, improved capacity over BN).

## Suggestions

1. **Define p_temp.** Without this specification, the method cannot be reproduced. Report the distribution family, parameters, and whether it was tuned per dataset.
2. **Add a lightweight deterministic baseline.** Train a small MLP (matching score network cost) on source features to predict ensemble logits with L2/KL loss. If DBN outperforms it, the diffusion complexity is justified; if not, the paper's framing needs revision.
3. **Analyze the poor ECE.** Investigate whether the noise in the diffusion process (temperature randomization, ξ₁) causes miscalibration. Provide confidence histograms comparing DBN vs. DE and suggest remedies (e.g., temperature scaling post-hoc).
4. **Ablate the noise term ξ₁.** Report ACC, NLL, and ECE with and without ξ₁ during inference. This separates deterministic prediction quality from the stochastic component.
5. **Report error bars.** Include standard deviations over multiple runs for the key metrics in Table 1 and Figures 3-4.

## Score and Decision

This paper presents a genuinely novel approach to fast ensembling using diffusion bridges, with convincing reductions in inference cost. However, it suffers from a significant underspecification (p_temp never defined), an acknowledged but unanalyzed calibration failure that undercuts the uncertainty motivation, and the absence of a simple deterministic baseline that would justify the framework's complexity. These issues are addressable but substantial in their current form. The paper is not fatally flawed but requires major additions before it can be accepted.

MY FINAL SCORE: <pineapple>5.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>