## Summary
# Final Review Report

## Summary

This paper proposes GeONet, a mesh-invariant deep neural operator network designed to learn the Wasserstein geodesic between probability distributions. By recasting the optimal transport (OT) problem as an operator learning task, GeONet jointly trains primal and dual neural networks to satisfy the coupled continuity and Hamilton-Jacobi partial differential equations (PDEs) derived from the Benamou-Brenier dynamic formulation. A key advantage of the method is that it does not require ground truth geodesic data during training, relying instead on boundary pairs of initial and terminal distributions. The authors demonstrate that GeONet achieves comparable accuracy to standard OT solvers on Gaussian mixture distributions and MNIST images, while offering orders-of-magnitude faster inference and zero-shot super-resolution capabilities. The paper is well-motivated and addresses a meaningful computational bottleneck in OT, though it requires stronger differentiation from prior neural OT methods, clearer methodological clarifications regarding mesh-invariance and loss weighting, and more rigorous analysis of out-of-distribution generalization and error decomposition.

## Strengths
1. **Novel Methodological Integration:** The paper successfully bridges optimal transport theory and neural operator learning by formulating the Wasserstein geodesic problem as a coupled PDE system (continuity and Hamilton-Jacobi equations). This physics-informed operator learning approach is conceptually elegant and avoids the need for expensive ground truth geodesic data during training.

2. **Mesh-Invariance and Super-Resolution:** GeONet's ability to predict geodesics at arbitrary resolutions without retraining is a significant practical advantage over traditional mesh-dependent OT solvers. The zero-shot super-resolution capability is well-demonstrated in the Gaussian mixture experiments and adds substantial value for applications requiring high-fidelity transport paths.

3. **Computational Efficiency:** The amortized inference nature of GeONet provides orders-of-magnitude speedups compared to iterative OT solvers like POT, especially on fine grids. This makes the method highly suitable for real-time applications and online learning settings where repeated geodesic computations are required.

4. **Comprehensive Experimental Validation:** The paper includes a diverse set of experiments covering continuous densities, discrete point clouds, and real image data (MNIST). The inclusion of out-of-distribution (OOD) testing and runtime comparisons provides a reasonably thorough empirical evaluation of the method's capabilities and limitations.

## Weaknesses
1. **Insufficient Differentiation from Prior Neural OT Methods:** The introduction cites recent machine learning methods for Wasserstein geodesics (e.g., Liu et al., 2021; 2023; Pooladian et al., 2023; Tong et al., 2023) but fails to explicitly state their limitations relative to GeONet. Without this contrast, the novelty and motivation of the proposed method are obscured, making it difficult for readers to understand why GeONet is necessary.

2. **Overstated Duality Gap Claim:** The paper claims that the training process ensures a "zero duality gap" between the primal and dual dynamic OT problems. Neural network approximations of coupled PDEs typically minimize residuals but do not guarantee an exact zero duality gap. This overstatement threatens the scientific defensibility of the method and should be bounded to reflect approximation limits.

3. **Ambiguity Regarding Mesh-Invariance:** The method claims mesh-invariance, yet the branch networks require fixed discretization of input distributions during training. The paper does not clearly distinguish between training-time discretization and inference-time continuous evaluation, which may confuse readers regarding the true scope of the mesh-invariance claim.

4. **Lack of Loss Weighting Guidance:** The loss function introduces weighting hyperparameters ($\alpha_1, \alpha_2, \beta_0, \beta_1$) for balancing PDE residuals and boundary conditions, but provides no guidance on their selection or sensitivity. In coupled PDE training, improper weighting can cause one residual to dominate, leading to poor convergence. This omission compromises reproducibility.

5. **Confounded Error Evaluation on MNIST:** The MNIST experiment uses an autoencoder to map images to a low-dimensional space before applying GeONet. The reported ambient-space L1 errors conflate autoencoder decoding error with geodesic estimation error, making it unclear how much of the error stems from the neural operator versus the representation learning step.

6. **Limited Analysis of Out-of-Distribution Generalization:** Table 2 shows a significant increase in L1 error for out-of-distribution (OOD) pairs (12.9-16.4%) compared to in-distribution pairs (~5-8%). The paper does not analyze this OOD gap or discuss why generalization degrades for unseen distribution pairs, weakening the claim of robust generalization.

## Key Issues
1. **Novelty and Motivation Clarity (Major):** The paper does not explicitly differentiate GeONet from recent neural OT methods (e.g., Liu et al., 2021; 2023; Pooladian et al., 2023; Tong et al., 2023). Without stating the limitations of these baselines (e.g., reliance on ground truth geodesics, fixed mesh constraints), the contribution appears incremental. *Fix:* Add a dedicated paragraph in the introduction contrasting GeONet with these methods, highlighting its unique advantages (mesh-invariance, PDE-constrained training without ground truth).

2. **Scientific Defensibility of Duality Gap Claim (Major):** The claim that GeONet ensures a "zero duality gap" is scientifically risky. Neural approximations minimize residuals but do not guarantee exact zero duality. *Fix:* Revise the wording to "approximates the zero duality gap by simultaneously satisfying the continuity and Hamilton-Jacobi equations" and acknowledge approximation limits in the limitations section.

3. **Reproducibility of Loss Weighting (Major):** The loss weighting hyperparameters ($\alpha_1, \alpha_2, \beta_0, \beta_1$) are critical for coupled PDE training but lack selection guidance. *Fix:* Report the specific values used, describe the tuning procedure (e.g., validation set search), and discuss sensitivity or adaptive weighting alternatives.

4. **Error Decomposition in MNIST Experiment (Major):** The ambient-space L1 error on MNIST conflates autoencoder decoding error with geodesic estimation error. *Fix:* Explicitly state that the encoded-space error provides a tighter assessment of GeONet's intrinsic performance, and consider reporting autoencoder reconstruction error separately to disentangle the sources.

5. **Out-of-Distribution Generalization Analysis (Major):** The significant OOD error increase (12.9-16.4%) is reported but not analyzed. *Fix:* Add a discussion paragraph analyzing why generalization degrades for OOD pairs and propose potential mitigations (e.g., curriculum learning, adversarial training, or expanded training distribution coverage).

## Actionable Suggestions
1. **Revise Introduction for Explicit Differentiation:** After citing recent ML geodesic methods (Liu et al., 2021; 2023; Pooladian et al., 2023; Tong et al., 2023), add one sentence explicitly contrasting them with GeONet. *Example:* "However, these methods typically require ground truth geodesic data for supervised training or remain constrained to fixed mesh resolutions, limiting their flexibility and data efficiency."

2. **Bound the Duality Gap Claim:** Replace "ensure zero duality gap" with "approximate the zero duality gap by simultaneously satisfying the continuity and Hamilton-Jacobi equations." Acknowledge that neural approximations minimize residuals rather than achieving exact theoretical bounds.

3. **Clarify Mesh-Invariance Scope:** After Eq. (13), add one sentence distinguishing training discretization from inference evaluation. *Example:* "Although the branch networks require fixed discretization of the input distributions during training, the trunk networks enable continuous evaluation at arbitrary spatial and temporal points $(x, t)$ during inference, thereby achieving output mesh-invariance."

4. **Report Loss Weighting Details:** After Eq. (17), add a brief note on hyperparameter selection. *Example:* "The weights $\alpha_1, \alpha_2, \beta_0, \beta_1$ are selected via a validation set to balance the magnitude of PDE residuals and boundary violations, with typical values reported in Appendix H. We also observe that adaptive weighting schemes can further stabilize training."

5. **Disentangle MNIST Error Sources:** In the MNIST experiment discussion, clarify that ambient-space error includes autoencoder decoding error. *Example:* "Note that the ambient-space L1 error includes both the geodesic estimation error in the encoded space and the autoencoder's decoding error; thus, the encoded-space error provides a tighter assessment of GeONet's intrinsic performance."

6. **Analyze OOD Generalization Gap:** After Table 2, add a paragraph analyzing the higher OOD error. *Example:* "The increased error on OOD pairs suggests that GeONet's generalization is bounded by the coverage of the training distribution space. Future work could explore curriculum learning or adversarial training to improve robustness to distribution shifts."

7. **Expand Limitations Section:** Add a sentence acknowledging theoretical convergence limits and loss sensitivity. *Example:* "Additionally, like other physics-informed neural networks, GeONet lacks theoretical convergence guarantees for the coupled PDE system and exhibits sensitivity to loss weighting hyperparameters, which requires careful tuning during training."

## Storyline Options + Writing Outlines
### Abstract Outline (Complete)
- **S1 (Problem & Domain):** Optimal transport (OT) offers a geometrically meaningful framework for comparing data distributions, but computing the Wasserstein geodesic remains computationally expensive and mesh-dependent.
- **S2 (Significance/Challenge):** Traditional solvers suffer from the curse of dimensionality, while recent neural methods often require ground truth geodesic data or fixed mesh resolutions, limiting their flexibility.
- **S3 (Prior Gap):** Existing approaches lack a unified framework that combines mesh-invariance, PDE-constrained learning, and data efficiency without expensive supervised labels.
- **S4 (Proposed Method):** We present GeONet, a deep neural operator that learns the Wasserstein geodesic by enforcing the coupled continuity and Hamilton-Jacobi PDEs derived from the Benamou-Brenier dynamic formulation.
- **S5 (Key Result & Bounded Implication):** GeONet achieves L1 errors comparable to standard OT solvers on Gaussian mixtures and MNIST, while reducing inference-stage computational cost by orders of magnitude and enabling zero-shot super-resolution.

### Introduction Outline (Complete)
- **P1 (Big Picture & Applications):** Establish the relevance of OT and Wasserstein geodesics in machine learning, generative modeling, and control systems. Emphasize why the *geodesic path* itself (not just the distance) is critical for interpolation and trajectory planning.
- **P2 (Traditional Limitations):** Discuss mesh-dependence and scalability issues of classical OT solvers (Hungarian, Sinkhorn). Highlight the accuracy-computation trade-off in entropic regularization.
- **P3 (Recent ML Methods & Gap):** Cite recent neural OT methods (Liu et al., 2021; 2023; Pooladian et al., 2023; Tong et al., 2023). Explicitly state their limitations (e.g., reliance on ground truth geodesics, fixed mesh constraints) to motivate GeONet's novelty.
- **P4 (Neural Operator Motivation):** Introduce neural operators (DeepONet, FNO, PINNs) as mesh-independent, data-driven PDE solvers. Explain why operator learning is uniquely suited for OT (zero-shot generalization across function spaces).
- **P5 (Contributions Summary):** Clearly list the three core contributions: (1) Mesh-invariant neural operator for Wasserstein geodesics, (2) PDE-constrained training without ground truth geodesics, (3) Zero-shot super-resolution capability. Bound the duality gap claim to approximation limits.

## Priority Revision Plan
| Priority | Action Item | Expected Impact | Effort |
|---|---|---|---|
| **P0** | Add explicit differentiation from recent neural OT methods in Introduction (P3). | Clarifies novelty and motivation; prevents perception of incremental contribution. | Low |
| **P0** | Bound the "zero duality gap" claim to approximation limits in Abstract and Method. | Improves scientific defensibility; avoids overstatement. | Low |
| **P0** | Report loss weighting hyperparameters ($\alpha_1, \alpha_2, \beta_0, \beta_1$) and tuning procedure. | Enhances reproducibility; addresses critical training stability concern. | Low |
| **P1** | Clarify mesh-invariance scope by distinguishing training discretization from inference evaluation. | Resolves methodological ambiguity; strengthens claim precision. | Low |
| **P1** | Disentangle autoencoder decoding error from geodesic estimation error in MNIST experiment. | Improves evaluation rigor; provides tighter performance assessment. | Medium |
| **P1** | Analyze out-of-distribution (OOD) generalization gap after Table 2. | Demonstrates awareness of method boundaries; suggests future robustness improvements. | Low |
| **P2** | Expand limitations section to include theoretical convergence limits and loss sensitivity. | Shows methodological maturity; aligns with PINN/DeepONet literature standards. | Low |

**Revision Order:** Execute P0 items first to secure novelty and defensibility. Follow with P1 items to strengthen evaluation clarity. Complete P2 items for final polish.

## Experiment Inventory & Research Experiment Plan
### Completed Experiment Inventory
| Exp ID | Objective/Hypothesis | Setup (data/split/protocol/baselines) | Metrics | Main Outcome | Claim Supported | Current Limitation |
|---|---|---|---|---|---|---|
| E1 | GeONet accuracy on continuous densities | 1D/2D Gaussian mixtures; identity, random, high-res, OOD pairs | L1 error | ~5-8% in-distribution, ~13-16% OOD | Mesh-invariance, super-resolution | OOD generalization gap unanalyzed |
| E2 | GeONet accuracy on discrete point clouds | 2D Gaussian point clouds; vs CFM, RF, POT baselines | L1 error | Lower error than CFM/RF; captures geodesic behavior | Discrete data handling | Fixed resolution for baselines |
| E3 | GeONet on real image data | MNIST digits; autoencoder encoding/decoding | L1 error (encoded/ambient) | Encoded error ~1-2%, ambient ~25-68% | Real-data applicability | Error conflates autoencoder + geodesic |
| E4 | Runtime efficiency comparison | 1D/2D Gaussians; vs POT library | Runtime (mean±std) | Orders of magnitude faster than POT | Amortized inference speed | POT accuracy thresholds manually tuned |

### Research-Theme Gap Diagnosis
The core research-value claims (mesh-invariance, PDE-constrained training without ground truth, computational efficiency) are well-supported. However, the **generalization robustness** claim is weakly supported due to the unanalyzed OOD error gap. Additionally, the **evaluation rigor** on real data is compromised by the confounded autoencoder error in the MNIST experiment.

### Proposed Research Experiments (P0/P1/P2)
| Target Claim | Hypothesis | Minimal Design | Controls/Baselines | Metrics | Success Criterion | Estimated Cost/Time | Expected Paper-Quality Gain |
|---|---|---|---|---|---|---|---|
| OOD Generalization | GeONet generalization is bounded by training distribution coverage | Train on restricted Gaussian subset; test on shifted means/covariances | In-distribution baseline | L1 error delta | Error increase < 5% | Low (1 day) | Validates robustness claim; suggests curriculum learning |
| Error Decomposition | Autoencoder decoding contributes significantly to ambient-space error | Report autoencoder reconstruction error separately on MNIST test set | GeONet encoded-space error | L1 error breakdown | Decoding error < 50% of ambient error | Low (2 hours) | Disentangles error sources; strengthens evaluation rigor |
| Loss Weighting Sensitivity | Performance is sensitive to $\alpha_1, \alpha_2, \beta_0, \beta_1$ values | Sweep weights over log-scale grid; report variance in L1 error | Default weights | L1 error std | Std < 10% of mean | Medium (2 days) | Demonstrates training stability; improves reproducibility |

**Traceability Rule:** Each proposed experiment maps to an unresolved core claim (OOD generalization, evaluation rigor, reproducibility) and provides a concrete quality improvement path.

## Novelty Verification & Related-Work Matrix
External literature search was not started in this run; novelty/comparison conclusions are deferred to manual verification.

## References
External literature search was not started in this run; no external references are listed.

## Scores
**Final Score:** 6.5/10

**Rationale:** The paper presents a conceptually elegant and practically valuable method (GeONet) that bridges optimal transport theory and neural operator learning. The mesh-invariance, zero-shot super-resolution, and computational efficiency claims are well-supported by the experiments. However, the score is moderated by several major weaknesses: insufficient differentiation from prior neural OT methods, an overstated duality gap claim, lack of loss weighting guidance, and confounded error evaluation on MNIST. These issues threaten the scientific defensibility and reproducibility of the method. With the proposed revisions (explicit baseline contrast, bounded duality claim, hyperparameter reporting, and error decomposition), the paper would significantly improve in rigor and clarity.

**Post-Revision Target:** [7.5, 8.5]/10

**Justification:** If the authors address the P0/P1 revision items (novelty clarification, duality gap bounding, loss weighting details, OOD analysis, and MNIST error decomposition), the paper will achieve strong claim-evidence alignment and reproducibility. The core methodological contribution and experimental results are solid, and the remaining gaps are fixable without requiring new major experiments. This would elevate the paper to a competitive standard for acceptance.