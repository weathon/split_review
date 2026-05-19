- Decision: Reject
- Avg Score: 6.20
- Scores: 5, 5, 8, 5, 8
Now I have a thorough understanding of the paper. Let me synthesize the final review.

## Summary

Point-PQAE introduces a cross-reconstruction generative paradigm for self-supervised learning on 3D point clouds. Unlike prior methods that reconstruct masked points within a single view (e.g., Point-MAE), Point-PQAE generates two decoupled views via a novel crop mechanism and reconstructs one view from the other using a positional query block with relative positional embeddings (RPE). The method achieves strong empirical results on ScanObjectNN classification, few-shot learning on ModelNet40, and competitive results on segmentation tasks, outperforming the self-reconstruction baseline Point-MAE by notable margins.

## Strengths

1. **Novel cross-reconstruction paradigm for point cloud SSL** — The paper is the first to formulate cross-reconstruction between two decoupled views as a generative pre-training task for point clouds, moving beyond the standard masked self-reconstruction (Point-MAE). This is clearly described in Figure 1 and Section 1.

2. **First point-cloud-specific crop mechanism for SSL** — The paper designs a random crop mechanism (select a center point and its nearest neighbors) that avoids the inconsistency of naively applying 2D cropping to irregular 3D data. Table 4c shows that removing the crop (setting minimum crop ratio to 1.0) significantly degrades performance, validating its importance.

3. **Positional query block with relative positional embeddings** — The cross-attention module uses fixed sin-cos RPE of the relative geometry between views as the query. Table 4a shows RPE substantially outperforms learnable embeddings, absolute PE, and no PE (e.g., learnable PE drops 3.4% on OBJ-BG vs. sin-cos RPE), demonstrating the design's effectiveness.

4. **Strong empirical results across multiple benchmarks** — Point-PQAE achieves new best results on ScanObjectNN (e.g., improving over Point-MAE by 6.7% and 4.4% on MLP-LINEAR and MLP-3 protocols), strong few-shot learning performance, and competitive segmentation results. It also outperforms or matches cross-modal methods (ACT, ReCon) that use 2D pretrained teachers while using only single-modal point cloud data.

5. **Robust generalization across crop ratios** — Figure 3 shows that when pre-trained with minimum crop ratio 0.6, the model reconstructs views generated at other crop ratios (0.7, 0.9), indicating it learns cross-view geometry rather than overfitting to the training ratio.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

1. **Coordinate frame mixing in RPE construction** — The RPE concatenates $\mathbf{G}_2$ (FPS centers computed in view 2's normalized-and-rotated coordinate frame) with $\mathbf{RL}_{1\rightarrow2} = \mathbf{L}_1 - \mathbf{L}_2$ (the offset between geometric centers computed in the original absolute coordinate space before normalization). These quantities derive from different reference frames. The paper's motivation — that the RPE supplies a clean geometric offset between the two views — is therefore not strictly satisfied; the network receives a mixed-representation input. However, this does not invalidate the method: the concatenated 6D vector still carries complementary information (internal patch structure + cross-view offset), sinusoidal encoding treats each dimension independently, and the learned projections can accommodate the mixed representation. The empirical results confirm the approach works. The authors should either recompute $\mathbf{RL}$ in a consistent coordinate frame or explicitly acknowledge this design choice and justify why it is still effective.

2. **Missing direct two-view self-reconstruction baseline** — The paper's central argument is that cross-reconstruction is more challenging and informative than self-reconstruction. The only self-reconstruction baseline is single-view Point-MAE. A more precise ablation would compare against a two-view self-reconstruction setup where each view is reconstructed from its own encoder representation (no cross-attention, but still using two views). While Table 4d (removing decoupling augmentations) partially addresses this concern by showing that two undecoupled views yield much lower performance, and Table 4c shows that adding crop to Point-MAE does not help, neither directly isolates cross-reconstruction from the two-view paradigm. Adding this comparison would strengthen the paper's core claim.

3. **Overclaim in the introduction** — The introduction states that Point-PQAE achieves "new state-of-the-art performance on several benchmarks, e.g., outperforming all published methods on few-shot learning." Table 2 tells a more nuanced story: under the FULL protocol, Point-PQAE is not universally superior across all settings (e.g., ReCon shows competitive or better results on some configurations). The claim should be qualified to reflect the actual pattern (e.g., "outperforms prior methods in most few-shot settings" or "achieves competitive or superior few-shot performance"). The body text in Section 4.2 is already more measured; the introduction should be aligned.

### Trivial

1. **Unmotivated sinusoidal encoding base** — The fixed base value of 10000 for sinusoidal encoding is copied from MAE (2D images) without justification for why this specific base is appropriate for 3D spatial coordinates. While the ablation in Table 4a shows sin-cos RPE works well, the choice of base is not ablated.

## Nice-to-Haves

- **Ablation on the minimum crop ratio** $r_m$ and number of patches $n$ — these hyperparameters likely influence the difficulty of cross-reconstruction and the quality of learned representations.
- **Ablation on number of views** — could the same or better benefit be obtained with three or more decoupled views?
- **Pre-training loss comparison** — a plot showing cross-reconstruction vs. self-reconstruction loss on hold-out data would directly demonstrate which task is "harder."
- **Runtime/compute comparison** — the two-view design doubles encoder cost; a training-time comparison with Point-MAE would help practitioners.

## Removed Points

These points from the reviewers were evaluated and removed for the reasons stated:

- **"Normalization description is ambiguous"** (Harsh Critic §3.1) — The paper states "min-max normalization, centered on $\mathbf{L}_1$ and $\mathbf{L}_2$," which is sufficiently clear for practitioners.
- **"Table 2 is difficult to parse"** — Formatting nitpick; the table is readable despite dense formatting. Not an author error.
- **"Base 10000 is arbitrary, not justified"** — Moved to Trivial rather than kept at higher severity; it is a minor observation about an unablated choice.
- **"No ablation on RPE coordinate frame consistency"** — Merged with Weakness 1 (coordinate frame issue) rather than treated as a separate missing-ablation point.
- **Criticisms about missing appendix, proofs, or reproducibility** — Removed per instructions (the PDF parser strips appendices; these exist in the original submission).
- **Strength Finder strengths that are generic** — No such strengths found; all listed strengths are specific and evidence-grounded. Minor conflict: Strength Finder's "state-of-the-art on few-shot learning" partially conflicts with Weakness 3; I kept the weakness version as the more precise one.

## Novel Insights

None beyond the paper's own contributions. The review process surfaces a useful observation: the RPE design is empirically validated but geometrically mixed, suggesting that transformer cross-attention can tolerate — and perhaps even benefit from — heterogeneous spatial information where one component encodes internal patch structure (in normalized local coordinates) and another encodes global cross-view offset (in absolute coordinates). This robustness is worth noting but does not constitute a novel insight beyond what the paper already demonstrates.

## Suggestions

1. In the RPE section, explicitly note that $\mathbf{RL}$ and $\mathbf{G}$ are computed in different coordinate frames and justify why this design is still effective (or recompute $\mathbf{RL}$ in the normalized space for geometric consistency).
2. Add a two-view self-reconstruction baseline where each view is independently reconstructed from its own encoder representation (no cross-attention), to isolate the effect of cross-reconstruction from the effect of having two views.
3. Temper the introduction's few-shot claim to match the table (e.g., "outperforms prior methods in most few-shot settings").
4. Add ablation on the sinusoidal encoding base value for 3D coordinates in a supplement.
