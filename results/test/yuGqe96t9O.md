Now I have a thorough understanding of the paper. Let me compose the final consolidated review.

---

## Summary

This paper proposes PCRL (Probabilistic Composition Representation Learning), a pre-training framework that learns probabilistic composition representations by aligning them with crystal structural information via a soft contrastive loss. The key idea is to model each composition as a Gaussian distribution (mean and diagonal covariance), where the mean serves as the compositional representation and the variance captures uncertainty stemming from polymorphism. The composition encoder is pre-trained jointly with a structural graph encoder on the Materials Project database, then used (without structural info) on downstream tasks. Evaluation on 16 datasets (9 wet-lab experimental + 7 DFT-calculated) shows consistent improvements over deterministic composition and multi-modal baselines, and the uncertainty analysis demonstrates correlations with prediction error, number of polymorphs, and material impurity.

## Strengths

1. **Novel probabilistic encoding of composition to handle polymorphism.** The paper introduces a probabilistic composition encoder that outputs a parameterized Gaussian distribution (mean and diagonal covariance) instead of a deterministic vector, directly modeling the one-to-many mapping between composition and its polymorphic structures (Section 3.2, Equation 3). This goes beyond prior multi-modal methods (e.g., 3D Infomax) that assume one-to-one correspondence, and beyond deterministic composition-only models (Roost, CrabNet) that ignore structure entirely.

2. **Comprehensive 16-dataset evaluation showing consistent, if modest, improvements.** PCRL is evaluated on 9 wet-lab experimental datasets (Band Gap, Formation Enthalpies, Metallic, ESTM 300K/600K with three properties each) and 7 DFT-calculated Matbench datasets. In representation learning (Table 1), PCRL outperforms all baselines on 8 out of 10 property prediction tasks. In fine-tuning (Table 3), PCRL achieves the best MAE on 8 out of 10 tasks with consistent positive transfer, while other pre-training methods often show negative transfer.

3. **Meaningful uncertainty quantification tied to materials science phenomena.** The learned variance is shown to correlate with model prediction error (Figure 6a), number of possible structures (Figure 6b), and material impurity/doping (Figure 6c). Case studies (CsI, PbTe, ScN, AgSO₄) demonstrate that the model captures not just structure counts but structural similarity — compositions with structurally similar polymorphs have collapsed variance, while those with diverse polymorphs have high variance (Section 5.3).

4. **Positive transfer learning in data-scarce settings.** PCRL pre-training consistently improves fine-tuning performance over randomly initialized models across all downstream tasks, whereas other methods (GraphCL, MP Band G., MP Form. E.) often cause negative transfer. This is important for materials science given the scarcity of wet-lab experimental data.

5. **Out-of-distribution robustness demonstrated.** In a held-out evaluation where training data excludes Actinide/Lanthanide elements but test data includes them, PCRL achieves best or second-best performance on 8 out of 9 tasks, outperforming all baselines (Appendix C.2).

## Weaknesses

### Major

- **The link between learned variance and *physical* polymorphism remains incompletely validated.** The pre-training data (MP) contains structures relaxed to 0 K energy minima; the paper acknowledges this (Section 7.1) but the uncertainty analysis in Section 5.2 equates "number of possible structures in MP/OQMD" with "number of polymorphic structures" without filtering to confirm these are genuinely distinct polymorphs (different space groups, coordination environments). The variance could partially reflect the model's difficulty with structurally diverse entries rather than physically meaningful polymorphism. The qualitative analyses (Section 5.3) partially address this by showing that structurally similar polymorphs yield low variance, but a direct validation using curated sets of well-characterized polymorphs (e.g., SiO₂, TiO₂, CaCO₃) with known independent ground truth would substantially strengthen the core claim. This does not invalidate the paper's representation learning contribution, but it leaves the uncertainty-polymorphism thesis partly circumstantial.

### Minor

- **Statistical significance is not achieved against property-specific baselines on their own tasks.** In the Band Gap dataset, PCRL does not significantly outperform MP Band G. (p=0.248); in Formation Enthalpies, it does not significantly outperform MP Form. E. (p=0.923). The paper transparently discusses this (Appendix B.2) and correctly notes that these baselines are specialized for single properties, whereas PCRL aims for universal applicability. However, two of the three main experimental datasets are involved in these non-significant comparisons, which tempers the claim of universal superiority.

- **The benefit of the probabilistic formulation (sampling) over a deterministic mean-vector variant is modest.** The ablation study (Appendix C.4) shows PCRL (with sampling) beats "w/o Sampling" on 7-8 out of 10 tasks, but with small margins and overlapping standard deviations. The paper's primary argument for the probabilistic formulation is uncertainty estimation, which is valid, but the representation quality improvement from the sampling step itself is marginal. A cleaner disentanglement of the benefit of structural information vs. the probabilistic formulation would strengthen the paper.

- **The "Physical Validity" analysis of $Z\bar{T}$ is somewhat circular.** The paper argues that lower MAE in $Z\bar{T}$ implies predictions are more "physically valid." However, $Z\bar{T}$ is a deterministic function of $\sigma$, $\lambda$, and $S$; if individual properties are predicted accurately, $Z\bar{T}$ automatically follows. The insight that MP Band G.'s errors compound nonlinearly is interesting, but the framing as a distinct "physical validity" check is over-interpreted.

- **The high-throughput screening experiment (Section 4.1, Figure 4) is visual and not quantitative.** The paper shows that PCRL's top candidates overlap with those identified by other models, but does not report precision/recall, ranked list metrics, or any quantitative comparison. The claim that PCRL "outperforms all other baseline methods" is not rigorously supported for this experiment.

- **The negative sampling strategy in Equation (4) could be more explicit.** While the piecewise definition (a=a' vs. otherwise) is mathematically clear, the paper does not discuss minibatch construction, the number of negative pairs, or how compositions with different numbers of polymorphs are handled during training. This impacts reproducibility.

- **The hyperparameter $\beta=10^{-8}$ (Table 5) is extremely small and its choice is not justified.** At this value, the KL regularizer is essentially negligible. The sensitivity analysis (Figure 6) shows that increasing $\beta$ even slightly to $10^{-5}$ degrades performance, indicating the model is near a critical point. The paper acknowledges the sensitivity but does not explain why this particular value was chosen over alternatives.

- **The distribution of compositions with multiple structures is not reported.** The paper states "up to 32,021 compositions having multiple potential structures" — a wide range (0-32,021). If most compositions have only one structure, the variance is primarily driven by the KL regularizer rather than polymorphism. Reporting the actual distribution would help contextualize the uncertainty analysis.

### Trivial

- The initial values of $c$ and $d$ (both set to 20) in the contrastive loss are shown to be important via sensitivity analysis (Appendix C.3), but the paper does not discuss how these values were selected.

## Nice-to-Haves

- A baseline that uses a deterministic contrastive objective (e.g., InfoNCE) over all available polymorphs per composition, without a variance head, would more cleanly isolate the benefit of the probabilistic formulation from the benefit of incorporating multiple structures.
- Direct validation of the uncertainty on a curated subset of materials with well-characterized, independently verified polymorphism (e.g., SiO₂, TiO₂, CaCO₃) would significantly strengthen the paper's core claim.
- Reporting precision/recall or hit-rate metrics for the high-throughput screening experiment would make the screening claim quantifiable.

## Removed Points

- *"The loss lacks theoretical grounding"* — The paper follows HIB (a published, peer-reviewed method) and does not claim a novel theoretical contribution. The loss clearly optimizes what it claims: pulling positive pairs together and pushing negatives apart. Demanding a derivation that the loss maximises mutual information or is a "valid probabilistic representation" is a scope mismatch for an empirical methods paper. **Removed** as it evaluates the paper against the wrong class of expectations (theoretical paper vs. empirical methods paper).

- *"Related Works does not adequately situate PCRL relative to recent multi-modal pre-training"* — I cannot verify the existence or relevance of the specific works cited by the critic (M3GNet, Struct2Vec, etc.) as directly comparable approaches. **Removed** per instructions (no external verification possible).

- *"The negative sampling strategy is vague"* — Equation (4) explicitly distinguishes a=a' vs. otherwise, and the surrounding text describes the intuitive meaning. The piecewise loss is standard for contrastive methods. **Removed** as the paper is sufficiently clear on this point.

- *"The matching probability sums over both polymorphs and samples"* — This is exactly the design the paper describes: it incorporates all available polymorphs and multiple Monte Carlo samples. This is the intended behavior, not a flaw. **Removed** as it reflects a misunderstanding of the method's design.

- Several generic formatting/style nitpicks and reproducibility nitpicks about undisclosed implementation details that are standard for the field. **Removed** per instructions.

## Novel Insights

None beyond the paper's own contributions. The reviewer analyses surface a recurring tension in representation learning for materials: the difficulty of validating uncertainty claims when the pre-training data (DFT-minimized structures at 0 K) does not fully capture the physical conditions under which polymorphism is meaningful. This is a domain-specific challenge that future work on uncertainty-aware materials representations will need to confront directly, beyond what this paper's correlational analysis provides.

## Suggestions

- For directness: Validate the uncertainty estimates on a hand-curated set of materials with well-characterized polymorphism (SiO₂, TiO₂, CaCO₃, carbon allotropes) where the polymorph count and structural diversity are known independently of any database. This would convert the current correlational evidence into causal evidence.
- Disentangle the benefit of structural information from the benefit of the probabilistic head by adding a baseline that uses a deterministic contrastive loss (e.g., InfoNCE on mean vectors only) with the same access to all polymorphs per composition.
- Report the actual distribution of structures-per-composition in MP (how many compositions have 1, 2, 3, ... structures) to contextualize what drives the learned variance.
- Quantify the screening experiment with precision/recall at top-k or hit-rate metrics rather than a purely visual comparison.
- Justify the choice of $\beta=10^{-8}$ and the initial values of $c,d$ more explicitly.

## Score and Decision

**Originality (3/4)**: Novel application of probabilistic representation learning to the composition-structure one-to-many problem in materials. The combination of soft contrastive learning with a probabilistic composition encoder is well-motivated and not previously explored in this domain.

**Importance (3/4)**: Learning compositional representations that incorporate structural information without needing structure at inference time is practically valuable for materials discovery, where DFT calculations are a bottleneck.

**Claims Support (2.5/4)**: The representation quality claims are well-supported by 16-dataset evaluation. The uncertainty-polymorphism claim is partially supported but the evidence is correlational rather than causal, with caveats about the pre-training data. The paper is transparent about limitations.

**Soundness (3/4)**: Experimental methodology is thorough (5-fold CV, statistical significance tests, ablations, OOD evaluation). The main gap is in the validation of uncertainty.

**Clarity (3/4)**: Well-structured and generally clear. Some minor presentation issues.

**Value (3/4)**: The pre-trained encoder and the probabilistic formulation are likely to be useful to the materials informatics community. The uncertainty analysis provides a foundation for future work.

**MY FINAL SCORE: <pineapple>6.5</pineapple>**
**MY FINAL DECISION: <orange>Accept</orange>**