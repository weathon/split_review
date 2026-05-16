Now I have a thorough understanding of the paper. Let me construct the final review, carefully cross-checking each reviewer claim against the actual text.

---

## Summary

This paper introduces LieRE (Lie group Relative position Encodings), which generalizes Rotary Position Embeddings (RoPE) from 1D sequences to *n*-dimensional inputs by replacing the standard block-diagonal 2D rotation matrices with dense rotation matrices learned via the exponential map of a skew-symmetric basis. The method is evaluated on 2D image classification (CIFAR-100, ImageNet) and 3D video classification (UCF101), reporting relative accuracy improvements of 10.0% over DeiT III on CIFAR-100 and 15.1% over absolute position encodings on UCF101, as well as training-compute and data-efficiency gains.

## Strengths

- **Novel and well-motivated generalization of RoPE.** LieRE extends RoPE from 1D sequences to *n*-dimensional inputs by learning dense rotation matrices from a skew-symmetric basis (Section 3, Algorithm 1). The connection to Lie theory — in particular, the trade-off between commutativity (Eq. 2, block-diagonal 2D rotations) and the weaker approximation property (Eq. 1, dense rotations) — provides clear mathematical grounding (Section 2.1). The paper shows that setting the block size to 2 recovers RoPE-Mixed exactly, making the generalization explicit (line 75).

- **Substantial accuracy gains across 2D and 3D tasks.** On CIFAR-100, LieRE achieves a 10.0% relative improvement over DeiT III, 7.3% over VisionLlama, and 2.2% over RoPE-Mixed; on ImageNet the trends are consistent (Section 5.1, Table 1). On UCF101 (3D video), LieRE achieves a 15.1% relative improvement over absolute position encodings. Results are reported with 95% confidence intervals.

- **Training compute and data efficiency.** LieRE requires 3.9× fewer training epochs to match the final accuracy of the DeiT III baseline on CIFAR-100 (Section 5.4, Figure 4b), and outperforms the full-data baseline using only 70% of the training data (Section 5.2, Figure 3b). These efficiency gains are the largest among compared methods.

- **Systematic capacity ablations.** The paper varies the LieRE block width (LieRE₈ vs LieRE₆₄, Figure 4a), the number of learned bases (per-head vs per-layer vs shared, Table 2), and the transformer backbone size (ViT-T, ViT-B, ViT-L, Table 4), providing practical design guidance for deploying LieRE.

- **Patch shuffling validates positional encoding usage.** LieRE models show the largest accuracy drop under patch shuffling (Table 3), directly confirming that the encoding is being utilized more heavily than baselines, not ignored.

## Weaknesses

### Fatal
None.

### Major

- **The source of LieRE's gains is not fully isolated: the Lie-group formulation vs. larger rotation capacity.** The paper frames LieRE as a generalization of RoPE-Mixed and compares LieRE₈ / LieRE₆₄ (block sizes 8 and 64) against RoPE-Mixed (block size 2). However, this confounds two variables: (1) the Lie-group learning mechanism (skew-symmetric basis + exponentiation) and (2) the larger rotation block size. A controlled baseline that parameterizes larger rotation blocks *without* the Lie-group formulation — e.g., composing multiple independent RoPE-Mixed rotations per block, or learning a rotation matrix directly via orthogonal parameterization — would isolate whether the improvement comes from the specific LieRE mechanism or simply from increased rotational capacity. Without this control, the paper's attribution claims ("LieRE's advantage comes from breaking commutativity") are not fully supported by the experiments. The block-size ablation (Figure 4a) shows that larger blocks help, which is necessary but not sufficient to show that *how* LieRE parameterizes those blocks is what matters.

### Minor

- **The 3D baseline implementation is underspecified.** For the UCF101 experiments, the paper states it compares against "RoPE-Mixed" but does not describe how RoPE-Mixed (originally designed for 2D image grids) was extended to 3D video (line 113). The text says "similar to the previous section," which is too vague to assess fairness. The reported 1.5% relative improvement over this baseline is uninterpretable without knowing the details of the 3D adaptation.

- **Efficiency claims lack uncertainty quantification.** The 3.9× training-step reduction and 70% data-efficiency numbers are presented as point estimates without confidence intervals, error bars, or description of how the thresholds were determined (e.g., whether the comparison is pointwise or area-under-curve). While the paper does report 95% CIs for accuracy in Table 1, the absence of similar rigor for the efficiency claims weakens their evidentiary weight.

- **No parameter-matched baseline.** LieRE adds ~580k parameters (ViT-B). The paper does not include a control that adds a similar number of parameters through another mechanism (e.g., increasing the transformer hidden dimension), leaving open the possibility that some of the gains reflect additional capacity rather than the encoding method itself.

- **Learning dynamics of the skew-symmetric basis are opaque.** The paper states the basis is "learned" (line 69) but does not specify its initialization (zero? identity?), whether any constraints (e.g., orthonormality) are enforced, or whether numerical stability issues arise from computing the matrix exponential during training. These details matter for reproducibility and for understanding behavior at early training stages.

### Trivial
None.

## Nice-to-Haves

- Reporting wall-clock training time or FLOPs would strengthen the compute-efficiency claims (3.9× step reduction might not translate to 3.9× time reduction if the matrix exponential adds overhead).
- Evaluating on a 4D synthetic task (e.g., 3D video with a temporal dimension already tested, or a higher-dimensional toy problem) would strengthen the claim of generalizing to *n*-dimensional inputs beyond 2D and 3D.
- The alternative interpretation of patch shuffling results (accuracy drop = overfitting to position vs. genuine utilization) is worth a brief discussion.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **"Insufficient experimental detail for reproducibility (missing optimizer, LR, batch size, etc.)"** — The paper specifies the backbone (ViT variants, line 82), epochs (200 for ImageNet, line 120-121), augmentation (RandAugment, line 82), and that pre-trained weights are not used (line 82). Per the meta-review guidelines, nitpicks about undisclosed hyperparameters of the sort normally documented in a camera-ready appendix are to be removed. The paper cites DeiT III (Touvron et al., 2022) as a baseline, which implicitly anchors the training recipe.

- **"No discussion of computational cost (matrix exponential overhead)"** — Noted as a nice-to-have, not a weakness invalidating results. Many positional encoding papers do not report per-step FLOPs.

- **"The paper should cover higher-dimensional inputs (4D+)"** — Testing 2D and 3D is a reasonable scope. Demanding 4D+ is scope creep for a paper already demonstrating the method across multiple modalities.

- **The harsh critic's claim that "the paper does not explain why LieRE is fundamentally different from simply using a larger block-diagonal rotation matrix in RoPE-Mixed"** — The paper explicitly addresses this (Section 2.1, Eq. 1 vs Eq. 2; Section 3, line 71; Section 5.3.2, line 175). The difference is commutativity of block-diagonal 2D rotations vs. the non-commutative dense rotations enabled by LieRE.

- **Strength Finder's claimed strength about "patch shuffling confirms effective use" being a supporting strength** — This is kept. However, the claim that the 10.0% and 15.1% are "substantial accuracy gains" is factually correct as stated.

## Novel Insights

None beyond the paper's own contributions. The reviews surface a genuine experimental-design gap (the missing same-capacity control) but do not contribute a novel analysis, theoretical insight, or reinterpretation of the results beyond what the paper already presents.

## Suggestions

1. **Add the critical missing control:** Compare LieRE against a baseline that uses the *same* rotation block size (8 or 64) parameterized without the Lie-group machinery — e.g., by composing independent 2D RoPE-Mixed rotations or by learning block-diagonal rotation matrices directly. If LieRE still outperforms, the Lie-group formulation is validated; if not, the contribution reduces to "larger blocks are better," which is a weaker but still publishable result.
2. **Specify the 3D baseline details:** Describe how RoPE-Mixed was adapted to 3D video (e.g., separate RoPE axes per spatial and temporal dimension, or a Kronecker product structure).
3. **Add uncertainty quantification for efficiency claims:** Report the range or confidence intervals for the 3.9× and 70% numbers, and state the exact accuracy threshold used for the compute-reduction measurement.
4. **Describe skew-symmetric basis initialization and regularization:** Clarify how the basis matrices are initialized, whether there are constraints (e.g., Frobenius norm regularization), and whether the matrix exponential introduces numerical stability issues during training.

## Score and Decision

The paper introduces a genuinely novel extension of RoPE with a clean mathematical motivation and demonstrates clear empirical improvements across multiple tasks. The core weakness is that the experiments do not fully isolate whether the gains come from the Lie-group formulation or simply from larger rotation block sizes — an attribution gap that weakens but does not invalidate the contribution. The paper is above the acceptance threshold but would be strengthened by addressing this control.

**Score: 6.0**

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>