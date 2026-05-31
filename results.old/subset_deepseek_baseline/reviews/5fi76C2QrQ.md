## Summary

This paper introduces FunKAN, a Functional Kolmogorov-Arnold Network that generalizes the Kolmogorov-Arnold theorem to Hilbert spaces, enabling direct processing of 2D feature maps without flattening. FunKAN parameterizes its inner functions via truncated Hermite spectral expansions and integrates into a U-shaped segmentation architecture (U-FunKAN), achieving state-of-the-art IoU on BUSI, GlaS, and CVC-ClinicDB with significantly lower computational cost. The approach is also demonstrated on an MRI enhancement task as additional validation.

## Strengths

- **Novel and theoretically motivated architecture**: FunKAN departs from standard KAN-based backbones by operating directly on feature maps via spectral decompositions, addressing the fundamental limitation of flattening spatial structure. The use of Hermite basis functions with learned grid deformation is a clean, differentiable mechanism.
- **Strong empirical results with low computational cost**: U-FunKAN achieves the highest IoU on all three segmentation benchmarks while requiring only 4.35 Gflops—substantially less than U-KAN (14.02), U-Mamba (2087), and even lightweight competitors like U-NeXt (4.58). The ablation study on channel scaling (Table 3) and basis count (Figs. 4–5) provides practical guidelines.
- **Thorough and reproducible experimental setup**: The evaluation covers three diverse modalities (ultrasound, histology, colonoscopy) with multiple runs, standard deviations, and detailed implementation specifications (PyTorch Lightning, CUDA/cuDNN versions, seed management, data splits). The additional MRI enhancement task (Table 4) convincingly shows generalization beyond segmentation.

## Weaknesses

### Major

1. **The theoretical claim is unsubstantiated**. The paper markets a "Functional Kolmogorov-Arnold theorem" as a core contribution, but Statement 3.1 is merely hypothesized, not proven. The derivation from that statement to the actual architecture (Eqs. 5–6) relies on the Riesz representation theorem and a hand-wavy two-step simplification; the connection is not rigorous. The grid deformation module, while empirically effective, is introduced heuristically without theoretical grounding from the functional KAN framework. This overclaim weakens the paper's principal novelty claim.

2. **The comparison baseline set is incomplete for a "state-of-the-art" claim**. While U-FunKAN achieves highest IoU on all three datasets, Table 1 shows that on BUSI, UKAGNet achieves F1=77.64 vs U-FunKAN's 77.37, and on CVC, U-KAN achieves F1=91.88 vs 91.42. The paper's claim of "state-of-the-art segmentation accuracy across three distinct medical imaging modalities" is true for IoU but not uniformly for F1. Additionally, UKAGNet's Gflops/params are not reported in Table 2, making the efficiency comparison incomplete.

### Minor

1. The derivation of the grid deformation module from the functional KAN framework is unclear. Equation (6) introduces deformed Hermite basis functions  ψ_{l,k}(χ_{l,i})  that depend on input features, but the theoretical justification for why this dependency should be learned via a residual block rather than arising from the spectral expansion itself is not explained.

2. The number of Hermite basis functions  r=6  is adopted from prior work, yet the ablation (Fig. 4) shows that  r=8  gives better IoU/F1 on BUSI. The paper acknowledges the trade-off with inference time (Fig. 5), but does not explore whether  r=8  would yield better results on GlaS and CVC as well.

### Trivial

- In Table 1, the F1 row for U-KAN on CVC has a weird "±" symbol rendered as LaTeX `\pm` in the text. (Parser artifact.)

## Nice-to-Haves

- Provide a proof sketch or at least a rigorous statement of the functional KAN representation under plausible assumptions (e.g., compact operators, spectral truncation). This would solidify the theoretical contribution.
- Report Gflops and Params for UKAGNet in Table 2 to allow a head-to-head efficiency comparison with U-FunKAN on all baselines.
- Include qualitative comparisons (segmentation maps) from competing methods (e.g., U-KAN, U-Mamba) alongside U-FunKAN in Fig. 6 to make the visual differences clear.

## Novel Insights

None beyond the paper's own contributions. The idea of using deformed Hermite basis expansions within a KAN-like framework to preserve spatial structure is a genuinely novel architectural insight, but the synthesis of known components (spectral expansion, grid deformation, U-Net) does not reveal a deeper principle beyond what the paper states.

## Suggestions

1. Either downgrade the "theoretical contribution" claim to a "theoretically motivated" heuristic, or provide a precise mathematical statement and proof of the functional KAN representation under specific conditions (e.g., compactness, bounded domain). The current Statement 3.1 is too vague and unsupported.

2. Add a direct efficiency comparison (Gflops, params, inference speed) between U-FunKAN and UKAGNet on the same hardware, given that UKAGNet achieves competitive F1 on BUSI.

3. For the selected default  r=6 , provide evidence beyond the BUSI ablation that it is optimal on GlaS and CVC, or at least acknowledge that  r=8  might improve those datasets too.

## Score and Decision

Score: 6.0

Decision: Accept

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>