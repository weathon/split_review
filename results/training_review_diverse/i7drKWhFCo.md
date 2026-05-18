Now I have all the information I need. Let me compose the final consolidated review.

## Summary

This paper presents SC-VAE (Scrubbed Conditional Variational Autoencoder), a framework for disentangling nuisance variables (speed, heading direction, animal identity) from 3D animal pose dynamics. The core technical contribution is replacing adversarial neural-network-based disentanglement with parametric "scrubbers" (linear least-squares, quadratic, quadratic discriminant, and mutual information estimators) that use adaptive exponential moving averages of sufficient statistics, avoiding the training difficulties of adversarial methods. The paper demonstrates that SC-VAE variants reduce decodability of nuisance variables from latent representations, improve conditional motion synthesis consistency, reduce over-segmentation in behavioral clustering, and enhance detection of Parkinsonian behavioral phenotypes in a mouse model.

## Strengths

- **Achieves targeted disentanglement beyond standard C-VAE**: The paper shows convincingly that conditional VAEs alone are insufficient for disentanglement (e.g., heading remains linearly decodable from C-VAE latents in Figure 2). SC-VAE variants significantly reduce both linear and nonlinear decodability of heading, speed, and animal identity, as quantified by R² decreases and classification accuracy drops. The heading disentanglement results approach the rotationally-preprocessed oracle baseline (VAE Processed).

- **Improves conditional motion synthesis fidelity**: SC-VAE scrubbers boost the consistency of generated sequences when conditioned on random heading or speed. SC-VAE-ND achieves R²=0.93 for heading and SC-VAE-MI achieves 0.40 for speed (Table 1), substantially outperforming vanilla C-VAE (0.48 and 0.05 respectively). This demonstrates that scrubbing residual information actually strengthens the conditional generation capability.

- **Enhances detection of Parkinsonian behavioral phenotypes**: Scrubbing animal identity with SC-VAE-QD increases effect size (d=1.52) and healthy-vs-disease classification accuracy (82%) relative to C-VAE (1.38, 77%), while also strengthening correlation of behavioral change with dopamine denervation extent (r=0.67, Table 2). The reverse control (scrubbing disease label) confirms improvements are not artifacts. This is a compelling real-world application.

- **Introduces hyperparameter-free parametric scrubbers as an alternative to adversarial neural networks**: The adaptive EMA-based MALS, MAQS, and QD scrubbers avoid the architecture and hyperparameter tuning difficulties of gradient reversal and neural discriminator approaches. The paper provides evidence (Figure 2) that SC-VAE-GR and SC-VAE-ND are less reliable in producing representations that are even linearly invariant to nuisance variables, whereas the parametric scrubbers achieve more consistent disentanglement.

## Weaknesses

### Fatal
None.

### Major

- **Core quantitative results lack error bars or statistical assessment**: Figure 2 (decodability R² and classification accuracy) and Table 1 (motion synthesis R²) present only single-point estimates without confidence intervals, standard errors, or significance tests. The PD analysis in Table 2 correctly includes mean ± SEM, making its absence in the other figures conspicuous. This is a structural concern because the paper's central claim—that SC-VAE parametric scrubbers are *more reliable* than adversarial alternatives—depends on stable, reproducible comparisons. Without measures of variability (across random seeds, training runs, or cross-validation folds), the reader cannot distinguish systematic advantage from lucky initialization. Adding error bars would substantially strengthen the paper's claims.

- **Disentanglement experiments use data from only n=3 animals**: The main evaluations of heading, speed, and identity scrubbing (Section 4.2, Figures 2–3) draw from 3 mice (324k frames each). Although the frame count is large, the frames are not independent—they come from three individuals. The paper's own PD dataset (n=36) and analysis demonstrate that individual differences matter, so the generalizability of the disentanglement results beyond these three animals is unclear. Per-animal breakdowns or validation on additional subjects from the PD dataset would address this concern.

### Minor

- **Missing scrubber variants from the PD analysis**: Table 2 reports results for VAE, C-VAE, SC-VAE-GR, SC-VAE-QD, and Reverse Control but omits SC-VAE-MALS, SC-VAE-MAQS, SC-VAE-MI, and SC-VAE-ND without explanation. If these variants were tested, the results should be shown; if not, the paper should explain their exclusion given they are central to the method's taxonomy.

- **Clustering analysis has a mild circularity**: Section 4.4 identifies "walking clusters" using a separate vanilla VAE to define reference labels. Since the vanilla VAE representations may themselves be contaminated by nuisance variables, the reference clusters are not ground-truth behavioral labels. The analysis remains informative (it shows that scrubbing merges clusters that were split by nuisance variation), but the interpretation that these merged clusters correspond to "true" walking behaviors should be tempered.

- **No systematic guidance for choosing among scrubber variants**: The paper finds empirically that for heading (independent of behavior), MI scrubbing works best; for speed (partially dependent), MALS is preferable to avoid destroying behavioral clustering; for identity, QD works. This is useful but the paper does not distill a diagnostic procedure or rule of thumb for a practitioner encountering a new dataset and nuisance variable. The conclusion acknowledges this, but it remains a practical limitation.

### Trivial
None.

## Nice-to-Haves

- A sensitivity analysis for the "self-tuning" smoothing factor in the EMA-based scrubbers, showing that the adaptive scheme actually reduces sensitivity to the fixed difference parameter.
- Qualitative examples (e.g., videos or pose sequences) of generated motions conditioned on different nuisance variable values, to give a concrete sense of what "consistent motion synthesis" means.
- Reporting the latent dimension D used for each model and a brief robustness check showing results are not sensitive to its choice.

## Removed Points

- **R² metric misinterpretation (critic: "could it reflect trivial collapse"):** Removed because higher R² in this setup corresponds to better conditioning (the generated sequence's speed/heading matches the conditioned input). Trivial collapse (ignoring the input) would produce low R², not high. The criticism reflects a misunderstanding of the metric.
- **Latent dimension D not reported:** Removed because the paper references Appendix C.1 for model architecture details, which the parser strips. This information exists in the original submission.
- **Self-tuning smoothing factor sensitivity analysis:** Downgraded to Nice-to-Have. The paper describes the adaptive scheme and references Appendix A.2 for details. Requesting a new sensitivity analysis is a wishlist item, not a core flaw.
- **Strength claim about "principled guidance":** Removed because it conflicts with the verified weakness that no systematic diagnostic procedure is provided. The weaker, accurate formulation ("demonstrates empirically that scrubbing level depends on variable-behavior dependence") is retained in Strengths.

## Novel Insights

The reviews surface one genuinely novel insight beyond the paper's own contributions: the finding that the *degree* of scrubbing nonlinearity needs to be matched to the dependency structure between the nuisance variable and the behavioral semantics creates a design principle that could extend beyond animal pose analysis. Specifically, variables approximately independent of behavior (heading direction, camera angle, illumination) admit aggressive nonlinear scrubbing (MI), while variables with inherent behavioral entanglement (speed, vigor) require constrained scrubbing (linear/polynomial) to preserve semantic structure. This insight—that perfect invariance is not always desirable—challenges the default assumption in adversarial disentanglement that more scrubbing is always better, and could inform disentanglement practice in other domains (e.g., removing confounders from medical images where some confounders carry legitimate clinical signal).

## Suggestions

1. **Add error bars or confidence intervals** to all key quantitative results (Figures 2, 3; Table 1). At minimum, report results across 3–5 random seeds or training runs. This directly addresses the paper's own emphasis on *reliability* as a distinguishing feature of the proposed method.
2. **Report per-animal variability** for the n=3 disentanglement experiments, or validate on additional animals from the PD dataset (which already has n=36). A scatterplot showing individual animal decodability would help assess generalizability.
3. **Include all scrubber variants in the PD analysis** (Table 2) or explicitly justify why MALS, MAQS, MI, and ND were excluded. Even a brief statement ("MALS/MAQS/MI were not designed for categorical variables") would suffice.
4. **Add a brief diagnostic guideline** for practitioners: even a rule of thumb (e.g., "if the variable is approximately independent of action semantics, start with MI; if partially dependent, start with linear scrubbing; if categorical, start with QD") would significantly increase the paper's utility.

## Score and Decision

**Originality**: Good — the parametric scrubber approach with adaptive EMA is a novel and practical contribution to the disentanglement literature.
**Importance**: High — nuisance variable disentanglement is a recognized bottleneck in behavioral neuroscience.
**Claims support**: Moderate — the core claims are supported but weakened by the absence of error bars and limited N.
**Soundness**: Good methodology, but the evaluation would benefit from statistical rigor.
**Clarity**: Well-written and clearly structured.
**Value**: Valuable contribution that will be of interest to the behavioral neuroscience community.

The paper presents a practical, well-motivated framework with a compelling real-world application. The main weaknesses (missing error bars, n=3 sample size) are addressable and do not invalidate the core contribution. The method's novelty and potential impact outweigh these limitations.

MY FINAL SCORE: <pineapple>6.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>