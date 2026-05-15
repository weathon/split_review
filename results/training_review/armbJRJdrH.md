Now I have verified all key claims against the paper. Let me produce the final consolidated review.

---

## Summary

The paper introduces the Robust Representation Consistency Model (rRCM), a framework for certified adversarial robustness that pre-trains a ViT via contrastive learning to align representations of noisy and clean versions of the same image at different noise levels, then fine-tunes with a consistency-regularized classification objective. The core idea is to replace the two-stage pipeline of diffusion-based randomized smoothing (purification + classification, with heavy computation) with a single model that performs implicit denoising-and-classification in one forward pass. On ImageNet, rRCM-B-Deep achieves higher certified accuracy than diffusion-based methods (DDS, DensePure, DiffSmooth) across all perturbation radii while reducing inference cost by orders of magnitude (53 seconds vs. 20+ minutes).

## Strengths

1. **Empirically strong efficiency–performance trade-off against diffusion-based methods.** Table 1 shows rRCM-B-Deep substantially outperforms DDS, DensePure, and DiffSmooth on ImageNet (e.g., 63.1% vs. 44.9% certified accuracy at r=0.5) while reducing inference latency from 20+ minutes to ~53 seconds. This is the paper's strongest empirical contribution — a single-pass classifier that matches or exceeds the accuracy of multi-step diffusion purification pipelines at a fraction of the cost.

2. **Novel training formulation unifying denoising and classification.** The paper reformulates the denoising objective as a discriminative representation-alignment task (Equation 7), combining a consistency loss (pairing samples at adjacent noise levels with identical noise) with a standard contrastive loss on augmented views. This two-stage design (pre-training + fine-tuning) enables a single model to classify perturbed inputs directly, eliminating the separate denoiser+classifier pipeline of prior work. The approach is clearly described in Section 3 and illustrated in Figure 2.

3. **Demonstrated scalability with model size and batch size on ImageNet.** Figures 3–4 show monotonic improvement in certified accuracy going from rRCM-S to rRCM-B-Deep and with increasing batch size, with no sign of saturation. This is a practical advantage and the paper explicitly acknowledges the potential for further gains with larger compute budgets.

4. **State-of-the-art results on CIFAR-10.** Table 2 shows rRCM-B surpasses DDS (Carlini et al.) by up to 6.4% (at r=0.5) and is competitive with ensemble methods like Boosting (Horváth et al.) while using a single model.

## Weaknesses

### Fatal
None.

### Major

1. **Gap between the PF ODE narrative and the actual pair construction.** The paper consistently motivates the pre-training as aligning points "along the PF ODE sampling trajectory" (abstract, Section 3.1, Section 3.2, Figure 2). However, the actual construction uses the approximation $\mathbf{x}_{t_{n-1}} = \mathbf{x}_{t_n} + (t_{n-1} - t_n)\boldsymbol{\epsilon}$, which — after substituting the forward-sampled $\mathbf{x}_{t_n} = \mathbf{x}_0 + t_n\boldsymbol{\epsilon}$ — reduces to $\mathbf{x}_{t_{n-1}} = \mathbf{x}_0 + t_{n-1}\boldsymbol{\epsilon}$ with the same noise $\boldsymbol{\epsilon}$. This is a forward-process pairing, not a true PF ODE step. The paper acknowledges the score function is unknown and cites Song et al. (2023) for the approximation (Section 3.3), but the narrative throughout the paper substantially overstates the connection. The method is better described as a multi-level noise contrastive pre-training with a consistency model–inspired approximation, and the current framing inflates the claimed novelty. The core empirical contribution (a single-pass robust classifier) is not invalidated, but the motivation is misleading.

2. **Clean accuracy of rRCM models is not reported.** The paper reports that the ViT classifier used for baselines (DDS, DensePure, DiffSmooth) achieves 81.35% on ImageNet, but never reports the clean accuracy of rRCM models. Since certified accuracy at small radii is bounded above by clean accuracy, a stronger base classifier could explain part of the improvement. This is especially relevant for comparisons with classical methods (SmoothAdv, Boosting, MACER) that use different architectures (ResNets) and whose numbers are taken from published results without re-running under controlled conditions. The comparison with diffusion-based methods is partially controlled (same ViT backbone) but still lacks a clean-accuracy baseline for rRCM.

### Minor

1. **Missing ablation studies that would isolate the source of improvement.** The paper does not ablate (a) training rRCM from scratch without pre-training (only a qualitative claim is made on line 133), or (b) removing the consistency-loss term from Equation 7 (keeping only the MoCo-v3-style contrastive loss). Without these ablations, it is unclear whether the pre-training stage or the specific noise-pair construction is responsible for the gains, versus the strong contrastive pre-training backbone itself.

2. **Selective reporting of the 85× inference reduction.** The 85× factor is relative to DensePure with heavy majority voting (52 min/sample). Against classical methods (SmoothAdv, ~1 min 20 s), rRCM-B's 53-second latency is only modestly faster. The paper correctly contextualizes the 85× as a comparison with diffusion-based methods, but the headline number in the abstract can create a misleading impression of the general efficiency gain.

3. **Limited certification set (500 images) without confidence intervals.** While 500-image certification is standard practice in the randomized smoothing literature (Cohen et al., Carlini et al.), reporting only point estimates on 500 samples without bootstrap confidence intervals or standard errors makes it difficult to assess the reliability of the reported numbers, especially for fine-grained comparisons where differences are small.

4. **The PF ODE limitation is mentioned but not quantified.** Section 3.3 notes that points on the stochastic forward trajectory share "similar, rather than identical, semantics" and that this "sets an upper bound on robustness," but this important limitation is not quantified — e.g., by measuring representation similarity or certified accuracy degradation as a function of the approximation quality.

### Trivial
None.

## Nice-to-Haves

- Reporting clean accuracy of rRCM models alongside the certified accuracy results.
- An ablation comparing rRCM pre-training against standard MoCo-v3 pre-training (with the same ViT backbone) to isolate the benefit of the noise-pair-specific consistency loss.
- A small-scale experiment (e.g., on CIFAR-10) comparing the proposed approximate pair construction against pairs generated with a pre-trained score model to quantify the degradation from the approximation.

## Removed Points

The following criticisms from the reviewer inputs have been filtered:

- **"The claim of being first to exploit the structured noise schedule is misleading"** — The paper qualifies this with "to the best of our knowledge" and the claim is about *training a robust classification model*, not about using diffusion models for purification. Prior diffusion-based methods use the noise schedule for separate denoising, not for training. Removed because the reviewer misreads the scope of the claim.

- **"Certification on 500 images without confidence intervals"** — This is standard practice in this subfield; the certification itself already provides statistical confidence (99.9%). Removed as a format nitpick that does not reflect a gap relative to community norms.

- **"No appendix/proofs"** — These were likely stripped by the PDF parser; the original submission may contain them. Removed per instructions.

- **"Missing related works"** — Removed per instructions (cannot verify external literature).

- **"Formatting/style nitpicks" and "typos/grammar"** — These are parser artifacts, not author errors. Removed.

- **"Figures 3–4 scalability experiments do not demonstrate a unique property"** — Scalability is a practical strength regardless of uniqueness. The paper claims scalability as a contribution, which is supported. Weakened and moved here because it does not threaten any core claim.

- **"The consistency loss uses stop-gradient (EMA rate 0) which is a known trick from SimSiam/BYOL"** — The paper attributes this to Song & Dhariwal (2023) and does not claim it as novel. This is a valid implementation detail but not a weakness. Removed.

- **"DensePure worse than DDS when no majority voting"** — The paper already describes this computation-performance trade-off explicitly (line 166). Removed because the paper already addresses it.

## Novel Insights

The reviews surface an interesting reframing of the paper's contribution: rRCM is best understood not as a method that "leverages PF ODE trajectories," but as a training-time approach that uses time-indexed noise augmentation with contrastive learning to build a noise-robust representation space. The connection to PF ODE trajectories is a framing device that borrows legitimacy from the consistency models literature, but the actual algorithm does not require score-based reverse sampling — it only needs the forward noising schedule. This decoupling suggests that the key methodological contribution (multi-level noise contrastive pre-training for certified robustness) could stand on its own without the PF ODE framing, and might even be strengthened by presenting the approach as a principled extension of randomized smoothing training (Jeong & Shin, 2020) with structured, trajectory-aware pair construction rather than as a reformulation of generative modeling.

## Suggestions

1. Tone down the PF ODE narrative to accurately reflect the approximation used. The method should be described as using a consistency-model-style approximation of PF ODE steps, or better yet, reframed as multi-level noise contrastive learning with trajectory-motivated pair construction.
2. Report clean accuracy for all rRCM variants to allow proper attribution of certified accuracy gains.
3. Add ablation studies (pre-training vs. no pre-training; with vs. without consistency loss) to justify the two-stage design.
4. Report bootstrap confidence intervals for the 500-image certification results, especially where differences between methods are small (e.g., CIFAR-10 at r=0.75).

## Score and Decision

The paper makes a genuine empirical contribution — a single-pass robust classifier that substantially outperforms diffusion-based randomized smoothing methods in both accuracy and efficiency. The core results in Table 1 are compelling and well-documented. However, the over-claimed PF ODE narrative and the missing clean-accuracy baseline weaken the paper's framing and prevent full trust in the attribution of improvements. These issues are addressable with revisions (correcting the narrative, adding clean accuracy, adding ablations) and do not invalidate the empirical findings. The paper should be conditionally accepted pending these corrections.

MY FINAL SCORE: <pineapple>6.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>