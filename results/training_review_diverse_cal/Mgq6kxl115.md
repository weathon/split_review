Now I have all the information needed. Let me produce the final consolidated review.

## Summary

This paper proposes Diffusion Bridge Networks (DBN), a method to approximate deep ensemble predictions at reduced inference cost. DBN trains a lightweight conditional diffusion Schrödinger bridge that, conditioned on features from a single source model, transforms the source's (temperature-perturbed) logit into the full ensemble logit. The diffusion process is distilled to a single inference step. Experiments on CIFAR-10, CIFAR-100, and TinyImageNet compare DBN to Bridge Network (BN), ensemble distillation (ED, END2), and the full Deep Ensemble (DE). The paper reports that DBN achieves near-DE-3 performance with lower FLOPs than BN, which struggles to reach DE-2.

## Strengths

- **Direct transport from a single member to the full ensemble, avoiding low-loss subspace learning.** Unlike BN, which requires training a Bezier curve + anchor parameter for each pair of members and only predicts outputs on the subspace (not the actual target model), DBN directly maps the source's logit distribution to the ensemble's logit distribution using a conditional diffusion bridge (Sections 3.1–3.2). This design choice avoids the quadratic scaling of BN.

- **Significantly reduced inference cost while maintaining accuracy and uncertainty metrics.** The results (Section 4.1) show DBN with a single lightweight score network and one distilled step attains accuracy, NLL, and Brier scores close to DE-3 while using substantially fewer FLOPs. On TinyImageNet, DBN is reported to outperform DE-3 at less than half the computational cost. Figure 3 further demonstrates that DBN achieves the same DEE as DE with far lower relative FLOPs than BN.

- **Diffusion step distillation enables single-step inference without performance collapse.** The paper adapts progressive distillation (Section 3.3) to reduce the diffusion bridge from 5 steps to 1. Inference (Section 3.4) requires only one evaluation of the lightweight score network, and the resulting model still yields strong results — showing the distillation preserves the essential transport information.

- **Multi-bridge combination with a shared source model.** For larger ensembles beyond a single DBN's capacity, the paper proposes using multiple DBNs sharing the same source model (Section 3.5). This limits added inference cost to one additional lightweight score network per bridge and is shown to improve accuracy and DEE (Figure 3).

## Weaknesses

### Fatal
None.

### Major

- **Missing ablation: direct regression baseline without the diffusion formalism.** The distilled inference is a single deterministic step: Z₀ = Z₁ + (β₁/σ₁)ε_{φ'}(h₁, Z₁, 0) + ξ₁ — effectively a learned function mapping (feature, source logit) to ensemble logit. The paper never compares against a similarly lightweight network trained *directly* on the same (source logit → target logit) pairs using a standard regression loss (e.g., MSE or KL divergence on the final logits). Without this ablation, it is unclear whether the diffusion/Schrödinger bridge formalism provides any benefit over a simple learned mapping. The core claim that the diffusion framework is responsible for the improvement remains unsubstantiated.

- **Insufficiently specified BN baseline implementation.** The paper reports that BN "struggles to achieve even DE-2 performance" and saturates at ~92% ACC / DEE 2 on CIFAR-10 regardless of target ensemble size (Section 4.1, Figure 3). However, the paper does not specify how many BN bridges were used for each target ensemble size, whether these bridges were trained following the original BN algorithm (Yun et al., 2023), or how the multi-bridge strategy was configured. Since the original BN paper claims sub-linear cost scaling with reasonable approximation, the reported saturation needs a clear explanation tied to the specific implementation choices. Without this, the central comparison between DBN and BN is difficult to interpret.

### Minor

- **No analysis of the number of diffusion steps.** The paper trains with 5 steps before distillation and states this is "enough" (Section 4). It does not vary this number (e.g., 2, 5, 10, 50) to show whether performance degrades with fewer steps or whether additional steps improve results. While logit space is lower-dimensional than pixel space (where hundreds of steps are typical), the lack of any step-count ablation weakens the claim that the diffusion formulation is meaningfully leveraged versus being a training detail.

- **Poor ECE acknowledged but not analyzed.** The paper notes that DBN has poor Expected Calibration Error even when accuracy and NLL are good (Section 4.1). Since calibration is a key motivation for deep ensembles, this is not a superficial limitation. The paper offers neither an explanation nor any attempt at post-hoc calibration (e.g., temperature scaling). A small experiment could determine whether this is a fundamental limitation or a fixable artifact.

- **No ablation of the temperature perturbation.** The source logit is randomized via T ~ p_temp to avoid trivial solutions (Section 3.2). The paper does not compare against a deterministic baseline (fixed T or no temperature scaling) to demonstrate that this design choice actually matters for final performance.

### Trivial
None.

## Nice-to-Haves

- Training cost (wall-clock time or training FLOPs) discussion would be helpful since the method's main selling point is efficiency.
- Exploring the use of different source models across multiple DBNs (rather than sharing one) as a way to increase diversity.
- Providing the actual numerical tables (ACC, NLL, BS, ECE, DEE, FLOPs, Params) in the main body rather than only in an input-included table that was not extracted here.

## Removed Points

The following criticisms from the harsh reviewer were removed after verification against the paper:

- **"BN was not designed to work with only one source model"** — Factually incorrect. The paper's own description of BN (lines 45–58) explicitly states that the BN takes a feature vector "computed solely from the first model θ_i" and predicts the output at the midpoint of the Bezier curve. BN is designed to work with a single source model's features.

- **"3 bridges should give DE-3 performance, 4 bridges DE-4, etc."** — Misunderstands what BN actually approximates. BN predicts the output on the Bezier-curve midpoint θ_{i,j}(0.5) — an interpolation between two modes, not the direct output of either. Even with multiple bridges, each bridge only provides a degraded 2-model interpolation, so averaging these does not recover a true 3+ model ensemble. Saturation at roughly DE-2 level is a plausible consequence of BN's design, not an implementation bug.

- **Complaint about 5 steps vs. "hundreds of steps" in pixel-space diffusion** — Apples-to-oranges comparison. Logit space (K-dimensional, where K=number of classes, typically 10–200) is far lower-dimensional than pixel space, so requiring far fewer steps is expected, not suspicious. The valid concern (kept above) is the lack of ablation across different step counts.

- Several generic or superficial strengths from the Strength Finder were dropped (e.g., "this paper addressed an important problem") as they lack specific content or conflict with verified weaknesses.

## Novel Insights

The most interesting observation emerging from cross-referencing the reviews is that the paper may have inadvertently identified a ceiling of Bridge Network that is a consequence of its fundamental design (predicting interpolated subspace outputs rather than direct model outputs) rather than a training issue. If BN's saturation at DE-2 level is indeed structural, then any method that directly transports between source and target distributions (like DBN) has a principled advantage that no amount of BN engineering can overcome. This reframes the comparison from "DBN tuned BN better" to "DBN addresses a structural limitation of BN" — which is a stronger claim than the paper itself makes explicitly. Conversely, the missing regression ablation undercuts this interpretation: if a simple MLP trained with MSE matches DBN, then the advantage over BN comes from direct transport, not from the diffusion bridge. These two claims — structural limitation of BN vs. value of the SB formalism — are not disentangled in the current paper.

## Suggestions

1. **Add a direct-regression baseline.** Train a lightweight network with the same architecture as the distilled score network on the objective E[∥s(h₁, z₁) − z₀∥²] using the same data pairs. Report ACC, NLL, and FLOPs alongside DBN. This is the single most important experiment to justify the diffusion framework.

2. **Clarify the BN implementation.** Specify the exact number of BN bridges used for each target ensemble size, whether they were trained following the original algorithm, and whether the reported saturation persists when BN bridges are added in the manner originally described by Yun et al.

3. **Vary the number of diffusion steps (e.g., 2, 5, 10) before distillation** and report final performance. If 2 steps already work, acknowledge that the SB formalism is being used as a training technique in a near-degenerate setting.

4. **Address the poor ECE** with at minimum a post-hoc temperature scaling experiment, and discuss whether this is inherent to the diffusion approximation.

5. **Ablate the temperature perturbation** by comparing against a fixed-T or no-temperature variant.

## Score and Decision

The paper presents a creative and potentially impactful idea — using a diffusion Schrödinger bridge to approximate ensemble predictions. The core contribution is well-motivated, and the reported results are promising. However, two major weaknesses prevent full confidence in the claims: (1) the missing direct-regression ablation leaves open the possibility that the diffusion formalism is unnecessary, and (2) the BN baseline comparison is insufficiently specified to allow proper interpretation of DBN's advantage. These are addressable with additional experiments but are not trivial fixes. The paper is borderline; a strengthened version with the suggested ablations would be significantly more compelling.

MY FINAL SCORE: <pineapple>5.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>