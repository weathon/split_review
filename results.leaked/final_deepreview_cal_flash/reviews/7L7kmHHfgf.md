Now I have a thorough understanding of the paper and the calibration anchors. Let me compose the final review.

## Summary

This paper proposes **PIRN**, a prototype-driven reconstruction framework for few-shot multimodal anomaly detection. It introduces three innovations: Balanced Prototype Assignment (BPA) using optimal transport to prevent codebook collapse, Adaptive Prototype Refinement (APR) that dynamically updates prototypes during inference, and Multimodal Normality Communication (MNC) that exchanges normal information across RGB and 3D surface-normal modalities. The method is evaluated on MVTec-3D-AD, Eyecandies, and Real-IAD D3 under few-shot and full-shot settings, consistently outperforming prior methods while being substantially more efficient (85% fewer FLOPs vs. prior SOTA).

## Strengths

1. **Consistent and substantial few-shot improvement.** PIRN outperforms all baselines across MVTec-3D-AD and Eyecandies at 5-, 10-, and 50-shot settings (Table 1). The gains against the controlled baseline INP-Former (same input, same frozen DINOv2 encoder) are +3.9, +3.7, and +2.4 AUROC_I on MVTec-3D-AD. This controlled comparison isolates the benefit of the proposed modules from the backbone choice.

2. **BPA demonstrably prevents codebook collapse.** The t-SNE visualization (Figure 1 Right) directly contrasts softmax assignment (prototypes cluster at a single point) with BPA (uniform prototype distribution over normal features). This is concrete evidence that the balanced-OT formulation achieves its stated goal.

3. **MNC effectively leverages cross-modal information.** Table 3 shows that RGB+SN consistently outperforms either modality alone (e.g., 10-shot AUROC_I: 0.922 vs. 0.879 SN-only, 0.827 RGB-only), with the largest gain at 5-shot where per-modality coverage is weakest. This directly supports the value of cross-modal communication.

4. **Dramatic efficiency gains without sacrificing accuracy.** Table 4 shows PIRN uses 103.36 GFLOPs (17.49ms) versus FIND's 728.46 GFLOPs (76.09ms) at comparable AUROC_I (0.922 vs. 0.921) — an ~85% FLOPs reduction and 4.35× speedup. This is a genuine practical advantage.

5. **Strong anomaly localization on Real-IAD D3.** Despite using only two modalities (RGB + surface normals) versus D³M's three, PIRN achieves the best pixel-level AUROC (0.961) and wins on 13/20 categories (Table 8), validating the robustness of the cross-modal reconstruction design.

6. **Interpretable prototype analysis.** The OT-movement visualization (Figure 4) shows that normal tokens undergo small shifts while anomalous tokens require large displacements toward normal prototypes, providing an intuitive explanation for how the method achieves discrimination.

## Weaknesses

### Fatal
None.

### Major

**Comparison against baselines is not fully controlled for input representation and backbone strength.**
PIRN uses surface-normal maps (derived from 3D point clouds) as the 3D input modality and a frozen DINOv2 ViT-B/14 encoder. Most baselines — M3DM, CFM, 3D-ADNAS — operate on raw point clouds and use different backbones (PointNet++ for 3D, ResNet or smaller ViT for RGB). These baselines are not adapted to use the same surface-normal input or the same DINOv2 encoder. Consequently, the reported performance gaps cannot be cleanly attributed to the proposed modules (BPA/APR/MNC) rather than to the more informative input representation or stronger backbone.

*Mitigating factors*: (i) The paper does provide one controlled baseline — INP-Former is adapted to use the same inputs (surface normals + RGB) and the same frozen DINOv2 backbone, and PIRN beats it by +3.7 AUROC_I at 10-shot. (ii) The ablation study (Table 2) controls for input/backbone and shows that each proposed module contributes positively. So the weakness is about *attribution* (how much of the gain over M3DM/CFM/3D-ADNAS is due to the modules vs. the better features), not about whether the full system outperforms prior work. A stronger evaluation would re-implement at least one additional baseline (e.g., M3DM's fusion logic) on top of the same surface-normal inputs and DINOv2 encoder to isolate the methodological contribution.

### Minor

1. **No variance reporting for few-shot experiments.** All few-shot results (5/10/50-shot) are reported as single numbers without standard deviations or multiple trial information (e.g., different random seeds or splits). In the few-shot regime, which normal samples are selected can substantially influence results. While the consistency of improvements across all shot settings and datasets makes it unlikely that results are artefactual, the lack of variance reporting weakens statistical confidence.

2. **MNC purification heuristic is not separately ablated or formally motivated.** Stage 2 of MNC purifies patch tokens by multiplying them element-wise with sigmoid of the BPA reconstruction: $\mathbf{Z}' = z_n \cdot \sigma(z_n^{\text{bpa}})$. This operation is described as an "attention mask" but is a somewhat unusual use of sigmoid on feature vectors. The entire MNC module is ablated (Table 2), but the purification sub-step itself is not compared against alternatives (e.g., learned gating, removing purification, using raw tokens directly). A brief empirical comparison would clarify whether this specific design is beneficial.

3. **Several implementation details are omitted.** The paper does not specify the entropy regularization coefficient in the Sinkhorn algorithm, the GRU hidden dimension, the number of attention heads in MNC's cross-attention, nor the exact loss function (a "soft mining loss" is cited to Luo et al. 2025 but the paper states "in practice we minimize cosine distance," leaving ambiguity about whether the soft mining formulation is actually used).

4. **"CTM" typo in Table 1.** The table labels CFM (Costanzino et al., 2024) as "CTM." This appears to be a transcription error.

### Trivial

**"AUROC7" in Figure 1 caption is not defined in the paper.** While likely a dataset-specific metric from Eyecandies, a definition or reference would help the reader.

## Nice-to-Haves

- An analysis of failure cases, especially when APR might incorporate anomalous information (e.g., large defects).
- Ablation of the Sinkhorn entropy regularization strength and number of OT iterations, which control the trade-off between assignment sharpness and computational cost.
- Discussion of the computational overhead of multiple Sinkhorn iterations across decoder layers beyond the aggregate FLOPs count.

## Removed Points

These points are flagged to be removed, treat them with caution:

- **Table 2 "garbled" / inconsistent checkmarks**: The parsed text shows uniform checkmark patterns across all rows, which is clearly a PDF-extraction artifact. The paper's text states "The baseline model (first row) excludes all proposed modules," confirming that the original table used proper checkmark patterns. The specific concern about "0.967 being higher than 0.922" cannot be verified from the garbled rendering and should not be held against the paper.
- **Figure 1 left plot lacking legend**: Parser artifact — the embedded image may contain a legend; the text description cannot verify this.
- **APR context vector notation ambiguous**: The description is sufficiently clear for a reader familiar with OT (column-normalization of the OT plan).
- **"Anomalous patches tend to be assigned more diffusely" lacks theoretical support**: The paper provides an intuitive justification grounded in the balanced OT formulation, which is reasonable.
- **Fusion of Z^bpa and Z^mnc via element-wise summation lacks justification**: This is a standard design choice and the whole system is ablated.
- **Soft-mining loss inconsistency**: The paper references Luo et al. (2025) for the definition and states "in practice we minimize cosine distance." This is adequate.
- **Missing related works**: Not within the scope of this review to verify.
- **Reproducibility/completeness nitpicks (undisclosed hyperparameters beyond those already standard)**: The paper provides the optimizer, learning rate, epochs, backbone, and key architectural hyperparameters.
- **Formatting/style concerns**: Parser artifacts, not author errors.

## Novel Insights

None beyond the paper's own contributions. The reviews surface two real concerns (comparison fairness, variance reporting) that the paper should address, but these are standard critiques of thoroughness rather than novel insights about the method.

## Suggestions

1. **Controlled baselines**: Re-implement at least one additional baseline (e.g., the M3DM feature fusion or CFM's alignment logic) on top of the same frozen DINOv2 features and surface-normal inputs, so the performance gap can be attributed to the methodological design rather than the feature representation. If this is impractical, provide a simple "reconstruction without prototypes" baseline using the same encoder and decoder architecture to quantify the benefit of the prototype codebook alone.

2. **Report variance**: Run at least 3 random splits for 5/10/50-shot settings and report mean ± std for all metrics. This is standard practice in few-shot literature.

3. **Ablate the purification step in MNC**: Compare the sigmoid-based masking against (a) removing it entirely, (b) using raw tokens, and (c) a learned gating mechanism to verify that the specific heuristic matters.

4. **Clarify the loss function**: Specify whether the soft-mining loss from INP-Former is used or cosine distance, and define the training loss precisely.

5. **Fix the "CTM" → "CFM" typo** in Table 1 and define AUROC7 in the figure caption or main text.

## Score and Decision

**Bracketing (Round 1)**: I queried anchors on few-shot anomaly detection with prototype/OT methods. Weak anchors (score < 3.5) averaged ~2.7; middle anchors (3.5–7.5) spanned 4.25–6.40; strong anchors (>7.5) averaged ~8.0. The paper clearly sits in the middle band — it has real methodological contributions and thorough evaluation but has identifiable weaknesses.

**Narrowing (Round 2)**: Within the middle band, the most comparable anchors are:  
- *One-for-All Few-Shot Anomaly Detection* (6.40, Accept) — similar scope (few-shot AD), similar issues (missing details, ablation concerns). PIRN has a slightly stronger evaluation (3 datasets, qualitative analysis) but a more significant comparison fairness concern; roughly comparable.  
- *AnomalyCLIP* (6.17, Accept) — comprehensive evaluation but some module justification concerns. PIRN is similar in rigor.  
- *Prototype-oriented Fast Refinement Model* (5.50, Reject) — uses OT for few-shot AD but with weaker evaluation and methodological clarity. PIRN is clearly stronger.  
- *H-PAD* (5.60, Accept) — prototype-based anomaly detection in time series. PIRN has more thorough evaluation.

**Final calibration**: PIRN is stronger than the ~5.5 papers but has a more significant weakness (comparison fairness) than the ~6.4 anchor. Placing it at **6.0** reflects a solid paper with clear contributions and rigorous evaluation, tempered by the uncontrolled baselines that prevent full attribution of the reported gains.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>