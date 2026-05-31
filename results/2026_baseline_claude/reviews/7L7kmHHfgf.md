## Summary

PIRN is a framework for few-shot multimodal anomaly detection (MAD) that reconstructs intra-modal features from a compact prototype codebook while enabling cross-modal normality exchange. Three core components are introduced: (1) Balanced Prototype Assignment (BPA) via balanced optimal transport to prevent codebook collapse; (2) Adaptive Prototype Refinement (APR) via a GRU that updates prototypes at inference using the current sample's normal context; and (3) Multimodal Normality Communication (MNC) that aligns prototypes across modalities via a Graph Attention Network and injects cross-modal normal knowledge via gated cross-attention. Experiments on MVTec 3D-AD, Eyecandies, and Real-IAD D3 show consistent improvements over the selected baselines in few-shot regimes.

---

## Strengths

- **Consistent empirical gains across multiple benchmarks and shot settings.** On MVTec 3D-AD and Eyecandies, PIRN outperforms all reported baselines at 5/10/50/all shots across AUROC_I, AUROC_P, and AUPRO. The gains over the strongest listed baseline (INP-Former) are meaningful in the few-shot regime (~3–4 AUROC_I points at 5- and 10-shot).
- **Compelling computational efficiency.** Table 4 shows PIRN achieves 103.36G FLOPs and 17.49ms latency—85% fewer FLOPs and 4.35× faster than FIND—while matching it in image-level AUROC. For resource-constrained deployment this is a significant practical advantage.
- **Thorough ablation studies.** Tables 2, 5, 6, and 7 rigorously isolate the contribution of each component (BPA, APR, MNC), prototype count K, decoder depth L, and APR aggregation strategy. The OT-movement visualization in Fig. 4 is a useful analytical tool showing normal vs. anomalous token displacement toward prototype anchors.
- **Principled motivation for each design choice.** BPA addresses the well-known codebook collapse with a balanced OT formulation; APR targets the train-test distribution gap; MNC avoids unreliable dense cross-modal patch matching by operating at the prototype level. Each problem is real and the proposed solutions are sensible.

---

## Weaknesses

### Fatal
None.

### Major

**1. Selective exclusion of FIND from main comparison tables.** FIND (Li et al., 2025) is cited in Table 4 as the "SOTA" method, achieving AUROC_I = 0.921 on 10-shot MVTec-3D-AD—virtually identical to PIRN's 0.922 (+0.001 difference). Yet FIND does not appear in Table 1 (the main comparison), leaving the reader unable to judge whether PIRN actually improves over FIND's accuracy or only matches it. The paper also uses FIND's pipeline to generate surface normal maps, making it a direct point of comparison. Excluding a method from accuracy comparisons while including it only in an efficiency table, where PIRN appears to tie it, undermines the claim of "consistently superior performance over existing baselines."

**2. Weak theoretical justification for APR's anomaly filtering.** Section 3.3 claims that "anomalous patch tends to be assigned more diffusely across prototypes, thereby contributing weakly to each prototype context," and that the GRU's gating mechanism "restricts the integration of unreliable anomalous contexts." The balanced OT plan assigns all N tokens to all K prototypes by construction (uniform marginal constraints), so anomalous patches are not excluded—only diluted. Furthermore, GRU gates learned from purely normal training data have no explicit mechanism to recognize and suppress anomalous contexts at test time. The argument relies on the hope that anomalous patches will have diffuse OT assignments and low GRU gate activation, but this is not proven empirically (e.g., no ablation shows what happens when anomalous regions are actually present and dominant in a test image).

**3. Real-IAD D3 results fall short on the key image-level metric.** On Real-IAD D3, PIRN achieves AUROC_J 0.873 versus D³M's 0.890—a gap of 1.7 points. The paper attributes this to D³M using tri-modal inputs, which is valid context, but the gap remains without a controlled experiment (e.g., PIRN with a third modality, or D³M with only RGB + surface normals) to isolate the effect of modality count. The full-data regime on a challenging industrial benchmark is arguably the most realistic evaluation, and the paper does not lead with the strongest interpretation of these results.

### Minor

- The ablation in Table 2 is performed only on MVTec-3D-AD at 10-shot. It is not shown whether the component contributions are consistent across Eyecandies, Real-IAD, or different shot values. The interaction between BPA and APR may differ when data is even more scarce (5-shot).
- The GAT in Stage 1 of MNC (number of attention heads, layers, KNN value k) is not specified in the main text, making reproducibility harder.
- The paper claims K = 10 as optimal (Table 5), but this ablation is on the all-shot setting only. In a 5-shot setting, fewer prototypes might be needed to avoid overfitting; this is not examined.

### Trivial
- Table 2 as rendered has all checkmarks filled in every row, making it impossible to determine the actual ablation configurations from the text alone (parser artifact).

---

## Nice-to-Haves

- Including FIND in Table 1 (or explicitly explaining why it was omitted and what its scores are on all benchmarks and shot settings) would substantially strengthen the claims of superiority.
- An experiment where anomalous test images with high anomaly density are fed through APR, along with a measurement of prototype drift, would directly validate the claim that GRU gating suppresses anomalous context.
- Sensitivity analysis of the number of GNN layers and the KNN neighborhood size in MNC Stage 1 would help practitioners tune the method.

---

## Novel Insights

The idea of operating cross-modal communication at the prototype (codebook) level rather than at the dense patch level is a meaningful architectural insight: by aligning high-level symbolic representations of normality across modalities before injecting them back into per-patch reconstruction, the method avoids the unreliability of direct patch-to-patch cross-modal alignment under data scarcity. The use of balanced OT within the inference loop (APR's context extraction) to achieve soft anomaly suppression without explicit anomaly labels is an interesting self-supervised idea, though it remains under-validated. The efficiency benefit—matching SOTA accuracy at nearly one-seventh the compute—deserves more prominence as a standalone contribution beyond the few-shot framing.

---

## Suggestions

- Report FIND's full results (AUROC_I/P, AUPRO) on MVTec-3D-AD and Eyecandies across all shot settings in Table 1, or provide an explicit explanation for its omission.
- Add a controlled experiment on APR robustness: inject synthetic anomalies into test images at varying densities and plot prototype drift before/after APR to empirically validate the anomaly-filtering claim.
- Provide component ablations on at least one additional dataset (Eyecandies) and at the 5-shot setting to check generality.
- Specify GAT hyperparameters (heads, layers, k in KNN) in the implementation details section.

---

## Score and Decision

The paper addresses a real and underexplored problem (few-shot multimodal anomaly detection), proposes principled solutions backed by consistent empirical gains, and delivers compelling efficiency advantages. However, the omission of FIND from the main accuracy tables—when FIND essentially matches PIRN's image-level AUROC—is a significant gap in the comparative evaluation that weakens the central performance claims. The APR anomaly-filtering argument also lacks rigorous empirical support. These are addressable issues, but they leave a material uncertainty about the paper's novelty margin.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>