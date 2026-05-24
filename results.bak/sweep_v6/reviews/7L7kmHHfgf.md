Now I have everything I need. Let me write the final consolidated review.

---

## Summary

PIRN proposes a prototype-driven reconstruction framework for few-shot multimodal anomaly detection (MAD). It introduces three components: Balanced Prototype Assignment (BPA) using optimal transport to prevent codebook collapse, Adaptive Prototype Refinement (APR) that updates prototypes at inference via gated GRU, and Multimodal Normality Communication (MNC) for cross-modal knowledge exchange. The method is evaluated on MVTec-3D-AD, Eyecandies, and Real-IAD, achieving strong few-shot performance with substantially lower FLOPs than prior reconstruction-based MAD methods.

## Strengths

- **Clear and well-motivated framework.** The three challenges identified (codebook collapse, static prototypes, missing cross-modal interaction) map directly to the proposed BPA, APR, and MNC. The use of a compact prototype codebook as an information bottleneck is a sensible design choice for few-shot settings, and the integration of optimal transport for balanced assignment is technically clean.

- **Consistent gains over the backbone-controlled baseline.** INP-Former is explicitly re-implemented with the same ViT-B/14 DINOv2 backbone as PIRN, and PIRN outperforms it by meaningful margins (e.g., +3.7 AUROC_I at 10-shot on MVTec-3D-AD, +4.0 at 10-shot on Eyecandies). Since INP-Former is uniformly the strongest baseline across settings, this provides credible evidence that the proposed components contribute beyond backbone choice.

- **Dramatically lower computational cost.** Table 4 shows PIRN achieves the best AUROC_I (0.922) while requiring only 103.36G FLOPs and 17.49ms latency — an 85% FLOP reduction and 4.35× speedup over FIND. This is a concrete engineering advantage over prior reconstruction-based MAD methods.

- **Thorough ablation studies.** The paper ablates codebook size K, decoder depth L, token aggregation methods for APR, and modality availability (RGB-only vs. SN-only vs. both). These studies confirm the information bottleneck intuition (too many prototypes or too deep a decoder hurt performance) and demonstrate that the method is not overly sensitive to hyperparameters.

- **Strong localization on Real-IAD with fewer modalities.** PIRN achieves the best pixel-level AUROC (0.961) on the challenging Real-IAD D3 dataset, using only two standard modalities (RGB + surface normals) compared to D³M's three-modality setup. This demonstrates practical generalization to real-world conditions.

## Weaknesses

### Fatal
None.

### Major

- **Uncontrolled backbone for most baselines.** The paper compares against M3DM, CFM, 3D-ADNAS, AST, and BTF without stating whether these were re-implemented with the same frozen DINOv2 backbone used by PIRN. Only INP-Former is explicitly adapted to match PIRN's two-stream ViT-B/14 architecture. Since features from a strong frozen encoder like DINOv2 alone can give competitive AD performance (as evidenced by INP-Former already beating all other baselines by wide margins), the reported gains over M3DM, CFM, etc. cannot be cleanly attributed to PIRN's proposed