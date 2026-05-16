Now I have a thorough understanding of the paper and all the reviewer claims. Let me compile my final review.

---

## Summary

SurfDesign proposes a surface-conditioned protein inverse folding method that claims two core technical contributions: (1) surface-based equivariant message passing (SEMP) that incorporates normals and curvatures to leverage the manifold structure of molecular surfaces, and (2) a hybrid parameter-efficient fine-tuning (PEFT) technique to integrate protein language model knowledge with the surface geometric encoder. The paper reports state-of-the-art sequence recovery (74.13% on CATH 4.2, exceeding 70% across multiple benchmarks) with gains of 18–28% over prior methods.

## Strengths

- **Strong motivation and problem framing.** The paper convincingly argues that surface-conditioned design is more directly relevant to protein function than backbone-conditioned design, and that existing surface methods treat molecular surfaces as discrete point clouds rather than continuous manifolds. This motivation is well-stated and identifies a genuine gap.

- **Comprehensive empirical evaluation across multiple benchmarks.** Results are reported on CATH 4.2, CATH 4.3, TS50, TS500, and multi-chain PDB complexes. The paper additionally evaluates structure recovery (scTM, scRMSD) via self-consistent protocol and surface recovery metrics (volume, distance, normal vectors), providing multi-faceted validation beyond raw sequence recovery.

- **Consistent and substantial performance improvements.** SurfDesign achieves 74.13% recovery on CATH 4.2 (vs. prior SOTA), 72.14% on CATH 4.3, 82.16% on TS50, 84.70% on TS500, and >80% on multi-chain PDB. These gains are consistent across settings, including zero-shot generalization to unseen families.

- **Ablation studies and scaling analysis.** The paper decomposes contributions of curvatures (~11.86% recovery improvement) and PLM knowledge (~13.43% recovery improvement), and demonstrates scaling benefits with larger PLMs (up to 76.01% recovery with ESM-2 3B).

## Weaknesses

### Fatal

- **Core technical contributions are not described.** The paper's two central claims — SEMP and the hybrid PEFT technique — are named but never specified. Section 2.2 ("Surface Geometric Network") devotes four paragraphs to differential geometry background (tangent spaces, Darboux frames, PCA-based pseudo-curvatures) but does not contain a single equation for message computation, aggregation, or node/edge updates. It does not specify how equivariance is implemented, what the network architecture is, or how the surface encoder interfaces with the PLM. The PEFT technique is mentioned only in the abstract and Figure 2's caption; there is no description of which PLM layers are fine-tuned, what adapter architecture is used, or how the fusion works. Without this information, the contribution is unverifiable and the paper is not reproducible. This is not a minor omission — the paper's core claim to have designed a new method cannot be evaluated.

### Major

- **Implausibly large performance gains without adequate explanation or controlled comparison.** SurfDesign reports relative improvements of 18–28% over strong baselines (VFN-IF-ESM, KW-Design, SurfPro) on standard benchmarks where gains of 1–2% are typically meaningful. The paper provides no error bars, no per-structure breakdown, and no analysis of whether evaluation protocols are perfectly aligned. Critically, because the method is not described, the reader has no basis to assess whether these gains are credible or artifacts of mismatched evaluation. The ablations partially help but are uninterpretable without knowing the baseline architecture.

- **Disconnect between theoretical framing and actual implementation.** The paper motivates SEMP with sophisticated differential geometry language (C^∞ manifolds, tangent spaces, Darboux frames, geodesic curvatures) but the actual implementation reduces to a k-NN graph on a denoised point cloud with PCA-based pseudo-curvatures (eigenvalues of a covariance matrix) used as node features. The paper acknowledges at line 72 that these are "a substitute and approximation," but the "manifold-aware" branding far exceeds what the implementation delivers. There is no formal connection demonstrated between the claimed manifold perspective and the algorithm (e.g., no convergence to a continuous operator, no discretization of the Laplace–Beltrami operator, no equivariance to reparametrization). The theoretical discussion is largely disconnected from the algorithmic choices.

### Minor

- **The abstract overstates training data.** The abstract (line 20) claims SurfDesign is "trained on the entire PDB database," but Section 3 (line 81) clarifies this is the curated multi-chain dataset from Dauparas et al. (2022), clustered at 30% identity — the standard preprocessed subset, not the "entire PDB." This should be corrected for precision.

- **"SurfDock" copy-paste error.** Line 92 refers to "SurfDock" instead of "SurfDesign," suggesting a copy-paste error from prior work that undermines confidence in careful preparation.

- **No sequence diversity analysis.** The paper acknowledges that surface-conditioned design is underdetermined (multiple valid sequences can produce similar surfaces), but does not analyze whether the high recovery rates come at the cost of reduced diversity — an important consideration for functional design.

- **Missing discussion of computational cost.** No comparison of parameter counts, training time, or inference speed relative to baselines, making it difficult to assess practical trade-offs.

### Trivial

- The paper does not mention plans to release code or model weights. While not a requirement, this compounds the reproducibility concern from the incomplete method description.

## Nice-to-Haves

- Adding error bars or per-structure distributions for main results would strengthen credibility of the reported gains.
- A controlled comparison where the only variable is the conditioning modality (backbone vs. surface) while keeping architecture identical would better isolate the benefit of surface conditioning.
- Analysis of failure cases (e.g., buried residues, low-SASA regions) would validate the motivation about surface conditioning.

## Removed Points

These points are flagged for removal by the instructions; treat them with caution.

- **Criticism about "not yet released" code/models.** The Harsh Critic says "No code or model weights are mentioned." Per instructions, criticisms about release status of cited items should be removed. However, the paper does not cite its own code — this is an observation about what the paper lacks, not a challenge to a cited entity. I keep it as trivial.
- **The Harsh Critic's request for "full specification of SEMP architecture"** is not removed — it is a valid Major weakness because the method is genuinely not described.
- **The Harsh Critic's claim that the paper does not "acknowledge that backbone-conditioned methods are not directly comparable" in the overclaim about "foremost to exceed 70% recovery."** The paper does compare against backbone-conditioned methods (ProteinMPNN, ESM-IF, etc.) in its tables, and it explicitly positions itself as a surface-conditioned method. The statement is about being the first surface-conditioned method to exceed 70%, which is reasonable. Removed as a strawman.

## Novel Insights

The Harsh Critic's most insightful observation is that the paper's theoretical framing (continuous manifolds, Darboux frames, geodesic curvatures) is disconnected from its actual implementation (PCA-based pseudo-curvatures on k-NN graphs with normal vectors from PyMol). This gap between rhetoric and realization is common in geometry-aware ML papers and deserves careful attention. The Strength Finder correctly identifies that the multi-faceted evaluation (sequence recovery, structure recovery, surface recovery) is a genuine methodological strength that goes beyond what most inverse folding papers provide. However, neither reviewer notices that the paper's central tension — using a PLM to overcome data scarcity for a fundamentally geometric task — raises an interesting question about whether the PLM is compensating for weak surface features or genuinely integrating complementary information. The ablations suggest both contribute, but without the method specification, this cannot be assessed.

## Suggestions

1. **Rewrite Section 2.2 to actually specify the method.** Replace the differential geometry textbook material with concrete equations for: edge construction, node/edge feature vectors, message function m_ij = f(x_i, x_j, n_i, n_j, ψ_i, ψ_j, ...), aggregation function, update function, and the equivariance mechanism. Include a diagram of the network forward pass.

2. **Dedicate a subsection to the PEFT technique.** Specify which PLM layers are adapted, what adapter/LoRA architecture is used, how the surface encoder outputs are fused with PLM representations, and what parameters are trainable vs. frozen.

3. **Add controlled comparisons** where the same network architecture is trained with and without surface features (normals, curvatures) to isolate their contribution.

4. **Add error bars or per-structure distributions** to the main recovery results, and discuss why the gains are so large relative to typical increments in the field.

## Score and Decision

This paper addresses a genuinely important problem (surface-conditioned protein design) with a plausible motivation and impressive empirical results. However, the core technical contribution is not described: the two claimed innovations (SEMP and hybrid PEFT) are named but never specified algorithmically. A paper whose method cannot be evaluated or reproduced cannot be accepted. The substantial performance gains, while promising, are uninterpretable without knowing what the method actually does. Rejection is necessary, though the direction is promising and the empirical work is otherwise thorough.

MY FINAL SCORE: <pineapple>3.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>