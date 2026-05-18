Now I have all the information needed. Let me produce the final consolidated review.

---

## Summary

This paper introduces DeepGeoCCA, a self-supervised geometric deep learning framework for learning shared latent representations from paired covariance-based neuroimaging data (e.g., EEG and fMRI). The core theoretical contributions are (1) a novel *geodesic correlation* measure defined on the SPD manifold that generalizes correlation to covariance-valued data, and (2) a relaxed ε-geodesic constraint with a provable bound that makes the objective trainable with SPD neural networks. Experiments on simulations, simultaneous EEG-fMRI (8 subjects, resting-state), and multi-view EEG motor imagery show the framework learns latent representations with higher geodesic correlation than Euclidean baselines (CCA, DeepCCA, VICReg) and a Riemannian baseline (RieCCA).

## Strengths

- **Novel geodesic correlation measure on the SPD manifold.** The paper formalizes a geometrically principled correlation metric that respects the SPD structure of covariance-based neuroimaging data, which is a sound theoretical advance over standard CCA and DeepCCA that operate in Euclidean space (Section 3, Definition). The measure is well-defined because the SPD manifold with AIRM is a Cartan-Hadamard manifold, guaranteeing unique orthogonal projections.

- **ε-geodesic constraint with a provable theoretical bound.** The relaxation method enables training with neural networks while controlling deviation from exact geodesic projection. The theorem in Section 3.2 provides an explicit upper bound (δ → 0 as ε → 1) on the tubular neighborhood width, directly supporting the claim of a controllable projection region.

- **Significant improvement over baselines on simultaneous EEG-fMRI data.** DeepGeoCCA with TSMNet achieves substantially higher test-set geodesic correlation than CCA, RieCCA, DeepCCA, and VICReg (Table 1), with statistical significance testing. This demonstrates that the framework can learn shared representations that generalize to held-out data.

- **Compatibility with existing SPD neural architectures.** The loss function operates on tangent-space projections (symmetric matrices; Remark 3), making it straightforward to integrate with any network that outputs symmetric/SPD matrices. The paper validates this by using SPDNet, TSMNet, and Tensor-CSPNet within the same framework.

- **Handles real neuroimaging challenges.** The framework explicitly addresses large distribution shifts across subjects/runs via subject/run-specific batch normalization (Section 4.2) and re-centering baselines, showing the method is designed for realistic data constraints rather than idealized toy problems.

- **Flexible geodesic speed initialization.** Remark 1 describes how geodesic speeds can be pre-defined by downstream task characteristics or learned from data, demonstrated in the motor imagery experiment (Section 4.3) where speeds are initialized from tangent-space principal components.

## Weaknesses

### Fatal
None.

### Major

- **Primary real-data validation is thin for the advertised scope.** The simultaneous EEG-fMRI experiment (Section 4.2), which is the paper's headline application, uses only 8 subjects in a resting-state paradigm (eyes open/closed). While the paper transparently calls this a "proof-of-concept" (Section 5), it also claims the method "extract[s] shared, latent brain dynamics whose coupling generalizes to unseen data" — a claim that would be far better supported by leave-one-subject-out or cross-dataset validation. The 10-fold CV on this small cohort provides limited evidence that the framework handles the inter-subject variability the paper itself highlights. This gap substantially tempers the practical significance of the contribution.

- **Downstream task gains are small and not clearly superior to other SSL methods.** In the motor imagery experiment (Section 4.3), DeepGeoCCA yields statistically significant but small improvements (+1–3%) over no pre-training, and the paper states "the effect remained small across scenarios *compared to other SSL pre-training losses*" (emphasis added). This means DeepGeoCCA does not clearly outperform alternative SSL objectives on the downstream task. The honest reporting is appreciated, but this result weakens the claim that geodesic correlation is beneficial for downstream performance beyond what simpler SSL methods provide.

### Minor

- **Key hyperparameters (ε) not reported for real-data experiments.** The paper thoroughly explores ε in the simulation (Figure 3c) and reports default loss coefficients (α₁=1, α₂=0.25, α₃=0), but the chosen ε value for the EEG-fMRI and motor imagery experiments is never stated. Reproducibility requires this information, and a practitioner cannot assess how the relaxation parameter was set in the primary evaluation scenarios.

- **"First completely data-driven SSL framework" claim is questionable.** The paper states it is "the first completely data-driven SSL framework" for simultaneous EEG-fMRI (Section 5), yet cites Deligianni et al. (2014) and Dähne et al. (2015) which also use data-driven paired EEG-fMRI approaches (though not SSL). The qualifier "SSL" may technically distinguish the work, but the claim invites unnecessary scrutiny and should be softened.

- **Geodesic constraint is only partially satisfied on real data without discussion of implications.** The R² values in Table 1 (~0.73–0.81 for DeepGeoCCA) indicate the learned representations are not tightly "on" the geodesics. While the paper provides a theoretical bound on the deviation (Section 3.2), it does not discuss how the observed residual deviation affects the claimed benefits of the geometric approach. The practical question — does partial constraint satisfaction degrade the representations? — remains unaddressed.

- **Qualitative t-SNE visualizations without quantitative structure measures.** Figure 4 shows t-SNE plots of the latent representations, but the paper does not supplement these with quantitative clustering or alignment metrics (e.g., silhouette score, geodesic distance to the ideal geodesic).

- **Computational cost and training stability not discussed.** The framework relies on specialized SPD neural network architectures (SPDNet, Tensor-CSPNet, SPDMBN). The paper does not discuss computational overhead or training stability compared to Euclidean counterparts, which would be relevant for practitioners considering adoption.

- **No ablation of the variance-preserving loss (ℒ_σ).** The paper defaults to α₃=0 and only enables ℒ_σ "if a specific architecture tends to dimensional collapse" (Remark 2). It is not reported whether ℒ_σ was used in the EEG-fMRI experiment, and no ablation shows its effect. A simple ablation on one dataset would clarify its role.

### Trivial
None.

## Nice-to-Haves

- **Cross-dataset or leave-one-subject-out validation** on the EEG-fMRI task would substantially strengthen the generalization claims.
- **A more challenging synthetic benchmark** (higher dimensions, non-linear mixing, multiple shared sources) would better demonstrate the framework's ability to recover latent structure beyond what CCA/RieCCA capture.
- **Quantitative clustering metrics** (silhouette score, geodesic distance measures) for the latent representations would strengthen the analysis beyond qualitative t-SNE.
- **Ablation of the variance-preserving loss** to clarify when it is needed and what effect it has.

## Removed Points

- **"Incomplete comparison to relevant baselines (SPD contrastive learning, Riemannian SSL frameworks)"** — The paper's baseline zoo (CCA, RieCCA, DeepCCA, VICReg) is defensible for this class of paper. The specific methods the reviewer asks for are not established baselines in this field, and the reviewer's claim about the paper's phrasing ("fail to maintain these particular geometric properties when learning correlation relationships") misreads the paper: the claim is about the *correlation learning objective* not respecting SPD geometry, which is factually correct since VICReg and DeepCCA operate in Euclidean space. Removed per: the paper's baseline choices are defensible within its class; the criticism partially misreads the paper.

- **"DeepCCA (2013) is a linear deep CCA variant"** — DeepCCA uses neural networks, not linear projections. This is factually incorrect. Removed.

## Novel Insights

None beyond the paper's own contributions. The reviews do not surface any observation about the work that is not already stated in the paper.

## Suggestions

1. **Report ε and all hyperparameter choices** for every real-data experiment in a table — this is essential for reproducibility.
2. **Soften the "first completely data-driven SSL framework" claim** — it invites unnecessary debate and does not strengthen the contribution.
3. **Add a brief discussion** of how well the ε-geodesic constraint is actually satisfied on real data (given the observed R² values) and whether the residual deviation measurably impacts representation quality.
4. **Either add a LOSO experiment or explicitly qualify the generalization claim** to reflect the 8-subject, proof-of-concept scope.
5. **Include a simple ablation** (even on one dataset) showing the effect of the variance-preserving loss ℒ_σ.

## Score and Decision

This paper presents a genuinely novel theoretical contribution — the geodesic correlation measure and the ε-geodesic constraint framework — and demonstrates it works better than relevant baselines on a real neuroimaging task. The methodology is principled, the theory is sound, and the framework is compatible with existing SPD architectures. However, the empirical validation is limited: the primary multi-modal experiment uses only 8 subjects, and the downstream task shows only marginal gains that are not clearly superior to other SSL methods. The paper is a solid methodological advance with preliminary but not yet compelling evidence of practical impact. It falls into the marginal accept / weak accept range.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Accept</decision>