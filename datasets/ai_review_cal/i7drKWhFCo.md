- Decision: Accept
- Avg Score: 7.00
- Scores: 8, 6, 8, 6
Now I have a thorough understanding of the paper and all the reviewer inputs. Let me construct the final consolidated review.

## Summary

The paper presents SC-VAE, a family of methods that combine conditional variational autoencoders (C-VAEs) with parametric "scrubbers" (linear MALS, polynomial MAQS/MACS, quadratic discriminant QD, kernel MI estimator) to disentangle nuisance variables (speed, heading, animal identity) from latent representations of 3D animal pose sequences. The key idea is replacing finicky adversarial neural networks with closed-form or near-closed-form scrubbers that provide controlled degrees of disentanglement. Results show that SC-VAE reduces decodability of nuisance variables from latents, merges over-segmented behavioral clusters, and improves disease detection in a Parkinsonian mouse model.

## Strengths

1. **Parametric scrubbers (MALS, MAQS, QD, MI) reliably reduce decodability of nuisance variables, outperforming adversarial baselines.** Figure 2 shows that SC-VAE-MALS, -MAQS, and -MI achieve substantially lower linear and nonlinear \(R^2\) for heading and speed compared to gradient reversal (GR) and neural discriminator (ND), and SC-VAE-QD achieves near-chance identity classification. This directly demonstrates the paper's central claim that explicitly modeled scrubbers produce more disentangled representations than adversarially trained networks.

2. **Scrubbing reduces nuisance-driven over-segmentation and produces more interpretable behavioral clusters.** Section 4.4 (Figure 3) provides concrete evidence: after scrubbing, within-cluster variance of heading and speed increases substantially (e.g., circular variance of heading rises from ~0.25 in VAE to ~0.9 in SC-VAE-MI), and walking behaviors previously split across clusters by speed are merged. This directly supports the paper's motivating argument that nuisance variability obscures behavioral structure.

3. **Adaptive moving average estimation of sufficient statistics is hyperparameter-free and stabilizes training.** The self-tuning EMA (Section 3.5) avoids manual tuning of smoothing factors, and the paper shows that the proposed parametric scrubbers are more reliable than adversarial approaches that "require delicately tuned" learning rates. This is a practical advance over existing adversarial disentanglement methods.

4. **The framework enables controlled disentanglement matched to the dependence between nuisance and behavior.** Section 4.4 demonstrates that full nonlinear scrubbing (MI) of speed destroys meaningful cluster structure (walking/rearing/grooming no longer aligned), while linear scrubbing (MALS) preserves it while still merging speed-split walking clusters. This supports the paper's claim that users can match scrubber strength to the variable's relationship with behavior.

## Weaknesses

### Fatal
None.

### Major
None. The core methodology is sound and the main claims are supported.

### Minor

1. **Missing error bars on key quantitative results.** Figure 2 (R² values for decoding), Table 1 (motion synthesis consistency), and Table 2 (classification accuracy, Pearson r) are reported as point estimates without measures of uncertainty. Only the effect size \(d\) in Table 2 includes ±SEM. Given variability in deep learning training and behavioral data, the absence of run-to-run variance or confidence intervals makes it hard to assess whether observed differences between methods are reproducible. For example, the claim that SC-VAE-MALS is "more reliable" than GR/ND would be substantially strengthened by showing variance across training seeds.

2. **PD application compares only one SC-VAE variant.** Table 2 evaluates VAE, C-VAE, and SC-VAE-QD, but not other SC-VAE variants (MALS, MAQS, MI, GR, ND). While QD is the natural choice for categorical identity scrubbing, the paper's framing suggests a general framework for disentanglement. Including even one additional scrubber (e.g., SC-VAE-MALS, which uses the MMD-based approach for identity, or SC-VAE-MI) would clarify whether the benefit is specific to QD's quadratic discriminant model or general to identity scrubbing. The "Reverse Control" (scrubbing disease label) is a good sanity check, but it does not substitute for comparing scrubber variants.

3. **No ablation of the conditioning component.** The architecture has two active components: conditioning (concatenating \(\mathbf{v}_t\) to \(\mathbf{z}_t\)) and scrubbing (penalizing \(\mathbf{v}_t\) decodability from \(\mathbf{z}_t\)). The paper does not test whether scrubbing applied to a vanilla VAE (without conditioning) achieves similar disentanglement. Such an ablation would isolate the benefit of the conditioning module and clarify whether the two components are complementary or redundant.

4. **Adversarial baselines may be under-tuned, and the comparison fairness is partially acknowledged but not quantified.** The paper states that GR and ND are "challenging" to tune and "unreliable," but does not report a systematic hyperparameter search (learning rates, architectures, training schedules) for these baselines. The claim that parametric scrubbers are more reliable would be stronger if accompanied by evidence that reasonable tuning of GR/ND was attempted. However, the paper is transparent about the difficulty, so this is a minor concern.

5. **The \(\beta\) regularization parameter for linear scrubbing (Eq. 4) and the kernel bandwidth for MI estimation are not specified in the main text.** The paper gives a conceptual description but does not state the values used. The appendix (stripped from this extraction) may contain these details, but they should be at least summarized in the main paper.

### Trivial
None.

## Nice-to-Haves

- **Cluster sensitivity analysis:** The number of clusters \(k=50\) is used throughout. A brief sensitivity check (e.g., \(k=20, 50, 100\)) would strengthen the robustness of the clustering results in Figure 3.
- **Discussion of why MA-QS failed to disentangle speed:** Section 4.2 notes that MA-QS did not affect speed disentanglement (unlike heading), but does not discuss why. Since this is an informative failure mode, a brief explanation would help practitioners.
- **Computational cost comparison:** The paper claims parametric scrubbers are practically advantageous but does not compare training time or stability empirically.

## Removed Points

These points were flagged for removal but are listed for completeness:

- *"Missing appendix content / missing implementation details"* — REMOVED per instructions: the parser strips appendices; they exist in the original submission. The paper repeatedly cites Appendix A.2, B, C, D for architecture and training details.
- *"Related work coverage gaps"* — REMOVED per instructions: I cannot verify missing related work from external knowledge.
- *"Typos / formatting artifacts"* — REMOVED per instructions: parser-induced issues are not author errors.
- *"Reproducibility concerns about undisclosed hyperparameters in appendices"* — REMOVED per instructions: the paper refers to appendices for full implementation details; this is standard practice.

## Novel Insights

None beyond the paper's own contributions. The synthesis of the two reviews confirms the paper's core narrative: parametric scrubbers with controlled expressiveness are more reliable and practical than adversarial neural network approaches for disentangling nuisance variables in behavioral data. The key insight that emerges from reading the paper alongside the reviews is that the paper's main contribution is not the SC-VAE framework alone, but the demonstration that different scrubber choices map onto different biological requirements (e.g., heading is safe to fully disentangle, speed is not) — and the reviews' emphasis on missing ablations and error bars points to where the evidence could better support this nuanced claim.

## Suggestions

- Add mean ± std (or bootstrapped confidence intervals) over at least 3–5 training seeds to Figures 2 and Table 1, and to the accuracy and correlation columns of Table 2.
- Include at least one additional SC-VAE variant (e.g., SC-VAE-MALS or SC-VAE-MI) in the PD analysis (Table 2) to determine whether identity scrubbing benefits generalize beyond QD or are specific to it.
- Add an ablation comparing scrubber + vanilla VAE vs. scrubber + C-VAE for at least one variable (heading is the cleanest case) to isolate the contribution of conditioning.
- State the numerical values of key hyperparameters (\(\beta\) for linear scrubbing, kernel bandwidth for MI) in the main paper (not only in the appendix).
- Briefly hypothesize why MA-QS fails to disentangle speed — is the relationship between speed and latent structure fundamentally non-quadratic, or is there an interaction with the C-VAE conditioning?

---

The paper tackles a real and well-motivated problem, proposes a sensible family of solutions, and provides convincing evidence for the main claims about heading and speed disentanglement and clustering improvement. The PD application is promising but incomplete. The weaknesses are evidential rather than structural — they point to what additional experiments would make the paper stronger, not to foundational flaws.
