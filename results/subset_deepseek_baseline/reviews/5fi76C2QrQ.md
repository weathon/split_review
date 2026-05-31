## Summary

The paper introduces FunKAN, a neural framework that generalizes Kolmogorov-Arnold networks to functional spaces by processing 2D feature maps directly via truncated spectral expansions over Hermite basis functions. Integrating FunKAN into a U-shaped architecture (U-FunKAN) yields competitive segmentation results on BUSI (ultrasound), GlaS (histology), and CVC-ClinicDB (colonoscopy) datasets with relatively low computational cost. The authors also apply FunKAN to an MRI enhancement task.

## Strengths

- **Novel spatial adaptation of KAN**: The idea of extending Kolmogorov-Arnold networks to operate on 2D feature maps without flattening is a natural and relevant innovation that addresses a known limitation of vanilla KAN for vision tasks.
- **Consistent empirical improvements**: U-FunKAN achieves the best IoU on all three medical segmentation benchmarks and shows low variance across runs, indicating stable training behavior.
- **Computational efficiency**: The proposed model has low GFLOPs (4.35) and modest parameter count (3.6M) compared to most baselines, making it attractive for resource-constrained clinical settings.
- **Ablation studies**: The paper provides systematic exploration of channel scaling and the number of Hermite basis functions, giving practical guidance for architecture design.

## Weaknesses

### Major

- **Theoretical overclaim**: The claimed “generalization of the Kolmogorov-Arnold theorem to functional spaces” (Statement 3.1) is presented as a hypothesis without proof, rigorous formulation, or even a sketch of how the classical theorem extends to Hilbert spaces. The connection between this claimed generalization and the actual implementation (discrete grids, spectral truncation, attention-like dot products) is loose and not formally derived. This overstates the theoretical contribution and undermines the paper’s credibility.
- **Unfair or incomplete baseline comparisons**: UKAGNet results are reported without standard deviations, suggesting they may have been taken from the original paper rather than re-evaluated under identical conditions. The improvements over the strongest competing baseline (U-KAN) are modest on GlaS (+0.38 IoU) and CVC (+0.88 IoU), and given the reported variance, the statistical significance is unclear—no significance tests are provided. The BUSI improvement is larger but U-KAN has high variance there.
- **Insufficient method description for reproducibility**: The computation of Hermite basis functions on a 2D deformed grid is not clearly specified (are they separable? how are they evaluated at deformed coordinates?). The role of the “attention matrix” and its relationship to the dot product with basis functions is ambiguous. The architecture diagram (Figure 1) does not resolve these computational steps. Without code (promised post-acceptance), the method cannot be fully assessed or reproduced.
- **Tangential supporting experiment**: The MRI enhancement experiment addresses a different task with a different architecture and does not directly support the segmentation claims. The interpretability analysis (Figure 7) is superficial—showing spectral energy distribution and a learned function surface does not convincingly demonstrate “interpretability” or robustness.

### Minor

- **Overclaimed SOTA status**: U-FunKAN does not achieve the best F1-score on BUSI (77.37 vs. UKAGNet’s 77.64) or CVC (91.42 vs. U-KAN’s 91.88), weakening the “state-of-the-art” claim. The authors rationalize this as an IoU–F1 trade-off but it conflicts with the headline claim.
- **Channel scaling choice**: Larger U-FunKAN variants obtain higher accuracy (e.g., 70.62 IoU on BUSI) yet the paper selects a smaller model as the primary proposal. While this trade-off is reasonable, the paper should better justify why the smaller variant is preferable beyond raw GFLOPs (e.g., deployment constraints, inference latency on GPU).
- **Missing modern segmentation baselines**: Comparisons with recent architectures like TransUNet, SwinUNet, or nnUNet are absent; these are standard benchmarks in medical segmentation and would strengthen the evaluation.

### Trivial

None.

## Nice-to-Haves

- Run all baselines under identical conditions and report full standard deviations for every method.
- Perform statistical significance tests (e.g., paired t-test or bootstrapped confidence intervals) on the key comparisons.
- Provide a pseudocode or an algorithmic description of the FunKAN layer to clarify the exact operations.
- Release the code during the review process to support reproducibility.

## Novel Insights

None beyond the paper’s own contributions. The observation that low-order Hermite coefficients may correspond to smoother, more generalizable features is interesting but remains speculative and not empirically validated.

## Suggestions

1. **Tone down theoretical claims**: Either provide a rigorous statement (with proper caveats) or reframe the contribution as a KAN-inspired architecture for spatial data rather than a theorem generalization.
2. **Standardize baseline evaluation**: Re-run all competing methods (including UKAGNet and U-KAN) with the same data splits, training procedure, and evaluation protocol to ensure a fair comparison.
3. **Clarify the FunKAN layer computation**: Add a step-by-step algorithmic description or pseudocode detailing how the deformed grid, Hermite basis evaluation, attention matrix, and final feature map are computed.
4. **Include significance tests**: Report confidence intervals or p-values to support claims of improvement over baselines.

## Score and Decision

**Score**: 4  
**Decision**: Reject

MY FINAL SCORE: <score>4</score>  
MY FINAL DECISION: <decision>Reject</decision>