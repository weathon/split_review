Now I have enough context. Let me compile the final review.

## Summary

The paper proposes PIRN, a prototype-driven reconstruction framework for few-shot multimodal anomaly detection. PIRN processes RGB images and surface-normal maps through frozen ViT encoders and reconstructs features via a learned prototype codebook with three innovations: Balanced Prototype Assignment (BPA) using optimal transport to prevent codebook collapse, Adaptive Prototype Refinement (APR) using a GRU to adapt prototypes at inference, and Multimodal Normality Communication (MNC) to exchange normalcy cues across modalities. Experiments on MVTec 3D-AD, Eyecandies, and Real-IAD D3 show consistent gains over baselines in few-shot settings, with comprehensive ablations and strong efficiency.

## Strengths

- **Strong and consistent empirical gains across benchmarks and shot settings.** Table 1 shows PIRN outperforms all baselines on MVTec 3D-AD and Eyecandies at 5-, 10-, and 50-shot (e.g., +3.9 AUROC_I at 5-shot on MVTec 3D-AD), with the margin narrowing but persisting in the full-shot regime. Table 8 further demonstrates competitive performance on the challenging Real-IAD D3 dataset.

- **Thorough ablation of each proposed component.** Table 2 isolates BPA, APR, and MNC, showing each contributes measurable gains (e.g., removing all modules drops from 0.922 to 0.828 AUROC_I), and the full combination is best. Additional ablations cover codebook size (Table 5), decoder depth (Table 6), and token aggregation strategy in APR (Table 7).

- **Visual evidence that BPA prevents codebook collapse and improves normal/anomalous separability.** Figure 1 (Right) provides t-SNE showing BPA achieves a uniform prototype distribution over normal patches vs. collapsed prototypes with softmax assignment. Figure 4 shows feature displacement analysis where normal tokens undergo small shifts toward prototypes while anomalous tokens are displaced more drastically.

- **Excellent computational efficiency.** Table 4 shows PIRN achieves 0.922 AUROC_I with 103G FLOPs and 17.5ms latency — 85% fewer FLOPs and 4.35× faster than FIND (728G FLOPs, 76ms), the previous SOTA.

- **Well-motivated method design.** Each component (BPA, APR, MNC) addresses a clearly articulated challenge in few-shot multimodal AD (codebook collapse, train-test distribution gap, and lack of cross-modal collaboration), giving the architecture strong conceptual coherence.

## Weaknesses

### Fatal

None.

### Major

- **Unclear fairness of baseline comparisons.** The paper states that INP-Former was adapted to use the same ViT-B/14 backbone and surface-normal inputs as PIRN. However, for the other baselines (BTF, AST, M3DM, CFM, 3D-ADNAS), the paper does not specify whether they were evaluated with the same surface-normal maps and the same frozen DINOv2 ViT-B/14 encoder used by PIRN, or run with their original configurations (which may use different 3D representations and backbones). Since encoder quality and input representation can substantially affect anomaly detection performance, this ambiguity makes it difficult to isolate how much of the reported gains come from the proposed architecture vs. a stronger feature extractor or more informative 3D modality. The paper would be significantly strengthened by clarifying — or re-running — the comparisons under a controlled setting where all methods share identical inputs and a frozen feature backbone.

### Minor

- **APR inference-time safety not directly validated.** APR updates prototypes at test time using OT-weighted context from the test image. The paper argues that anomalous patches contribute weakly due to diffuse OT assignments and that the GRU gates suppress residual contamination. Table 2 shows that removing APR entirely reduces performance (0.916 vs. 0.922), which validates APR's value overall, but does not isolate whether test-time adaptation itself ever causes prototype drift toward anomalies. A simple ablation disabling APR at inference only (while keeping it during training) would directly address this.

- **"Vector-quantized discrete prototypes" terminology is imprecise.** The reconstruction via the OT plan (Eq. 2) computes a continuous weighted sum of prototypes, not a discrete quantization as in VQ-VAE. The prototypes are updated via gradient-based learning without a commitment loss. This does not affect the method's validity but may mislead readers expecting discrete codebook mechanics.

### Trivial

- The paper could benefit from clarifying prototype initialization and the exact internal operations of the decoder layers (dimensions, normalization, feedforward components) to improve reproducibility, though the core architecture is well-described.

## Nice-to-Haves

- An ablation isolating the cross-modal communication in MNC beyond simple multi-modal fusion would strengthen the claim that prototype exchange "enables each modality to reinforce the other's understanding of normality." For instance, comparing against a baseline that concatenates intra-modal reconstructions from both branches without MNC's two-stage exchange would test whether the communication mechanism adds value beyond independent processing.

- Reporting per-category results in the main paper (currently noted as in Appendix Tab. 11) would help readers assess whether gains are consistent across all classes or concentrated on a subset.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **Harsh critic: "Table 2 is garbled / uninterpretable"** — This is a PDF parser artifact, not a paper issue. The original submission's Table 2 is clearly formatted. REMOVED.

- **Harsh critic: "Real-IAD D3 comparison (Table 8) is hard to parse due to formatting"** — Again a parser artifact. The original table is properly structured. REMOVED.

- **Harsh critic: "Reproducibility details — provide explicit information on prototype initialization, learning rates for codebook vectors, exact architecture"** — The paper already provides substantial implementation details (optimizer, learning rate, epochs, backbone, number of prototypes, number of decoder layers). The additional detail requested is standard practice to defer and does not constitute a weakness. REMOVED as a standalone criticism; partially retained as Trivial.

- **Strength Finder: "This paper addressed an important problem"** — Generic framing without concrete evidence that this specific problem framing is what makes the paper valuable. DROPPED (absorbed into the broader method-strength framing above).

## Novel Insights

The paper's use of balanced optimal transport for both prototype assignment (BPA) and prototype refinement context aggregation (APR) within a unified decoder architecture is a genuinely clean design. The dual role of OT — preventing codebook collapse in BPA and providing anomaly-robust context vectors in APR — creates a coherent framework where the same mathematical tool serves complementary purposes. The observation that cross-modal communication at the prototype level (rather than dense patch-to-patch alignment) is more robust under few-shot constraints is well-supported and practically valuable.

## Suggestions

- The baseline fairness concern is the most important issue to address. The authors should either confirm that all baselines were run with identical surface-normal inputs and the same frozen ViT-B/14 DINOv2 backbone, or re-run comparisons under this controlled setting. If some baselines inherently require different inputs (e.g., point clouds), this should be explicitly disclosed and the implications discussed.

- Add the suggested "APR disabled at test time" ablation to directly validate that test-time prototype refinement does not degrade performance on anomalous images.

- Clarify the "vector-quantized discrete prototypes" phrasing — "learnable continuous prototypes" or "soft-codebook prototypes" may be more accurate given the OT-weighted reconstruction.

## Score and Decision

### Round 1 — Bracketing

I retrieved three bands of calibration anchors:
- **Weak (<3.5)**: CLIP-LAD (3.00), Generalized AD with Knowledge Exposure (2.50), Meta-Tasks FSL (2.50), MIMOSA (2.60). These papers have significant methodological or evaluation weaknesses. PIRN is clearly above this tier.
- **Middle (3.5–7.5)**: Prototype-oriented Fast Refinement for Few-shot IAD (5.50), PTAD (4.25), H-PAD (5.60), Prototype-based OT for OOD (4.60). The most comparable, "Prototype-oriented Fast Refinement" (5.50), shares the prototype + OT + few-shot AD theme but is single-modality, has less comprehensive experiments, and suffers from unclear methodology. PIRN is clearly stronger.
- **Strong (>7.5)**: Deep Orthogonal Hypersphere Compression (8.00), TTA against Multi-modal Reliability Bias (8.00), Transfusion (7.60), ViT Needs Registers (8.00). These are high-impact papers with fundamental contributions and near-flawless execution. PIRN does not reach this tier due to the baseline fairness reporting gap.

**Round 1 bracket: 5.5–7.5.**

### Round 2 — Narrowing

I pulled anchors in the 5.0–7.5 range:
- **MMAD benchmark (6.50, accept)**: A dataset/benchmark contribution for MLLMs in industrial AD. Well-executed but limited methodological novelty. PIRN has deeper methodological contribution and more empirical validation. PIRN is comparable or slightly stronger.
- **One-for-All Few-Shot AD (6.40, accept)**: Proposes a new few-shot AD paradigm with prompt learning. Has similar strengths (comprehensive experiments, novel framing) but reviewers noted module clutter and insufficient ablations. PIRN's ablations are more thorough and its architectural coherence is stronger. PIRN edges above this.
- **ThermalGaussian (6.60, accept)**: Multimodal 3D reconstruction via Gaussian splatting. Different task but comparable quality level.
- **Transformer Fusion with OT (6.50, accept)**: Uses OT for model fusion. Interesting but different domain.

Comparing PIRN against these anchors: PIRN has stronger methodology than the MMAD benchmark (which is primarily a dataset contribution), more thorough ablations than the One-for-All paper, and comparable experimental breadth. However, the baseline fairness concern in PIRN is a real gap that none of these anchors share in the same way — the MMAD benchmark had concerns about diversity analysis, and the One-for-All paper had concerns about module clutter and missing ablations.

PIRN fits between the One-for-All Few-Shot AD (6.40) and the MMAD benchmark (6.50), with stronger overall methodology but a salient reporting gap on baseline fairness. I place it at **6.5**.

### Anchor Summary

| Anchor | Avg Score | Round | Comparison |
|--------|-----------|-------|------------|
| gTsLBDMZrL (Prototype Fast Refinement) | 5.50 | 1 | Single-modality, less comprehensive; PIRN is clearly stronger |
| 8TBGdH3t6a (H-PAD) | 5.60 | 1 | Time-series AD, different domain; PIRN has broader evaluation |
| JDiER86r8v (MMAD benchmark) | 6.50 | 2 | Dataset paper, good but less methodological depth; PIRN is comparable |
| Zzs3JwknAY (One-for-All Few-Shot AD) | 6.40 | 2 | Similar domain, PIRN has more thorough ablations and stronger architectural coherence |
| ybFRoGxZjs (ThermalGaussian) | 6.60 | 2 | Different task; comparable execution quality |
| LjeqMvQpen (Transformer Fusion + OT) | 6.50 | 2 | Different domain; comparable novelty level |

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>