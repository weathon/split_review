I've thoroughly read the paper and verified each claim against the actual text. Let me now produce the consolidated review.

---

## Summary

This paper introduces a method to condition protein backbone diffusion models on dynamical properties derived from Normal Mode Analysis (NMA). The method uses an analytical loss function (NMA-loss) that compares pairwise angles and relative amplitudes of displacement vectors in the lowest non-trivial normal mode, avoiding the need for a separate neural network for conditioning. The approach is demonstrated on a custom GVP-based denoiser and transferred to the pretrained Genie model without retraining, with joint conditioning on both dynamics and structure for hinge-motif proteins.

## Strengths

- **First conditioning of protein diffusion on dynamical properties**: The paper identifies an underexplored and biologically important problem. No prior work in protein generative modeling conditions on dynamics (Section 2.1). This novelty is genuine and well-motivated by the link between low-frequency collective motions and protein function.

- **Analytical loss replaces an external neural network**: Rather than training a classifier that would need to approximate eigenvectors of variable-size matrices (a technically difficult problem), the paper uses a closed-form invariant NMA-loss (Equation 15) that operates on the denoised structure's normal modes. As noted in Section 3.1, this avoids the retraining-per-matrix problem of neural eigenvector approaches.

- **Transferability to a pretrained model without retraining**: The method is applied to Genie by modifying only the sampling scheme. The hinge-target experiments (Section 5.2) produce proteins matching target hinge motifs, with scTM pass rates of 0.41–0.78 depending on target. This plug-and-play transfer is demonstrated, not just claimed.

- **SDE-theoretic formalization**: The derivation of the conditional score (Section 3.1, Equations 8–14) follows the reconstruction-guidance framework, providing a principled basis for the joint conditioning of structure and dynamics.

- **Invariant loss design**: The NMA-loss uses pairwise cosine angles and normalized amplitudes, ensuring rotation/translation invariance and avoiding dependence on eigenvector sign or absolute amplitude — genuine design necessities that are correctly handled.

## Weaknesses

### Major

- **Dynamics conditioning evaluation is partially circular**: The primary evidence that dynamics conditioning "works" (Section 5.1, Figure 2) is that NMA-loss is lower for conditional samples than unconditional ones. But NMA-loss is exactly the loss being minimized during sampling. While visual inspection (Figure 3) provides qualitative support, the paper lacks an independent quantitative dynamics validation — for example, computing normal modes of the *final generated structures* using a standard, separate NMA implementation (e.g., an anisotropic network model via a tool like ProDy) and comparing the resulting displacement vectors to the targets. Without this, it is unclear whether the guidance translates into genuine dynamical properties or merely exploits artifacts of the same NMA computation used during sampling.

- **Joint conditioning experiments are underpowered and lack key baselines**: Only 27 conditional samples survive filtering across three targets (Section 5.2), which is too small for reliable conclusions given the high variance across targets (scTM > 0.5 proportions of 0.48, 0.78, 0.41). Crucially, the paper does not report unconditional scTM pass rates for the same targets — only joint-conditioning and dynamics-only conditioning numbers are given. Without knowing how designable unconditional Genie samples of these lengths are, it is impossible to assess whether dynamics conditioning degrades designability or not. The dynamics-only conditioning scTM values (0.93, 1.0, 0) are themselves erratic and raise questions about target-specific effects that are not discussed.

- **The computation of v(x) is underspecified**: The entire method hinges on computing normal mode displacement vectors v(x) from the denoised structure (expected positions at t=0). The paper (Section 3.2) repeatedly says "derived from expected positions at t=0" but never states which specific NMA model is used (e.g., ANM cutoff distance, spring constant model, mass weighting), how the eigenvector of the lowest non-trivial mode is obtained, or — critically — whether this computation is differentiable and how gradients of the loss backpropagate through it at each sampling step. If the eigenvector computation is not differentiable, the gradient signal for guidance would need approximation; if it is differentiable, the computational cost of an eigenvalue decomposition at every sampling step (250 steps) should be discussed. This omission makes the method non-reproducible from the paper text alone and obscures its practical feasibility.

### Minor

- **Genie integration details are lacking**: Genie operates on SE(3) frames, and the paper does not explain how coordinates are extracted from frames for NMA computation, nor how the gradient of the loss propagates through the SE(3) frame parameterization. The guidance scales (2000–3000) are large and not discussed in terms of their effect on sampling quality. While these are likely standard practices in the code release, the paper should at least outline the approach.

- **No independent check of mode correspondence**: The NMA-loss compares displacement vectors in the assumed lowest non-trivial mode. The guidance may push the structure toward having the target displacement pattern, but it does not guarantee that the mode in which those displacements occur is actually the *lowest non-trivial* mode of the generated structure. This nuance is not discussed.

### Trivial

- None beyond what is already captured above.

## Nice-to-Haves

- A discussion of the computational cost: how many eigenvalue decompositions are performed per sampling step, and whether this scales acceptably to longer proteins or more sampling steps.
- Reporting unconditional scTM baselines for the same target lengths to contextualize the joint conditioning results.
- Ablation showing the effect of each term in the NMA-loss (angle vs. amplitude).

## Removed Points

- **Criticism that dynamics-only conditioning scTM of 0 for hemoglobin is "concerning"**: This observation is factual and the paper itself reports it without comment. The reviewer elevated it to a concern, but it is organic to the results — the paper reports the finding honestly. It is kept as part of the broader "results are erratic" point rather than removed.
- **Criticism that the paper does not discuss whether the method "merely aligns displacements or actually changes large-scale collective motions"**: This is effectively the same as the circular-evaluation concern and is already captured.
- **"The NMA-loss operates on displacement vectors of a specific normal mode... the guidance may push the structure toward having that pattern in some mode, but the correspondence is not guaranteed"**: This is a valid nuance and is kept in Minor Weaknesses.

## Novel Insights

The most interesting tension from the reviews is the gap between the paper's conceptual contribution (dynamics-conditioned protein generation is genuinely novel and well-framed) and the experimental evidence (which relies on a circular metric, small samples, and missing baselines). The critical question that neither the paper nor the reviewers fully resolve is: *does conditioning on NMA-loss during sampling actually produce structures whose lowest-frequency motions correspond to the target, or does it mostly ensure that the denoised trajectory momentarily aligns with the target in a way that an independent NMA of the final structure would not corroborate?* This is the single most important question for a follow-up study to address.

## Suggestions

1. Perform an independent dynamics validation: generate conditional and unconditional samples, compute their normal modes using a standard publicly available NMA tool with a fixed protocol (e.g., ProDy ANM with a 12Å cutoff), and compare the resulting displacement vectors for the conditioned residues to the targets. This would break the circularity and convincingly demonstrate whether the conditioning transfers to a realistic dynamical analysis.

2. Generate more samples per target (at least 100) and report unconditional scTM baselines for proteins of the same lengths. This would clarify whether dynamics conditioning degrades designability and provide statistically meaningful pass rates.

3. Fully specify the computation of v(x): state the NMA model (cutoff, spring constant, mass weighting or not), how the lowest non-trivial eigenvector is selected and extracted, and whether (and how) the computation is made differentiable. If the code is available, reference the relevant module.

4. Discuss the computational cost of per-step eigenvalue decompositions and the rationale for the large guidance scales used with Genie (2000–3000).

## Score and Decision

**Originality**: High. The problem of conditioning on dynamics is genuinely novel and underexplored. The analytical loss approach is clever.

**Importance**: High. Dynamical properties are critical for protein function and currently ignored by generative models.

**Claims support**: Moderate. The core claim of dynamics conditioning is supported only by circular evidence (NMA-loss minimization) plus qualitative visual inspection. The joint conditioning results are promising but underpowered.

**Soundness**: Moderate. The theoretical framework is sound, but the experimental validation has significant gaps (circular metric, small samples, missing baselines, underspecified core computation).

**Clarity**: Moderate. The method is clearly motivated and the theory is well-presented, but the core mechanistic detail (how v(x) is computed) is missing, which undermines reproducibility.

**Value**: High potential, but the current evidence does not fully substantiate the claimed contribution.

Overall: The paper tackles an important and genuinely novel problem with a methodically interesting approach. However, the empirical evaluation has significant gaps that prevent the core claims from being fully supported. The dynamics conditioning evidence is partially circular, the joint conditioning experiments are underpowered and lack critical baselines, and a key implementation detail (the computation of v(x) and its differentiability) is left unspecified. Major revisions are required.

MY FINAL SCORE: <pineapple>5.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>