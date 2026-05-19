- Decision: Reject
- Avg Score: 5.20
- Scores: 6, 5, 5, 5, 5
Now I have all the information needed. Let me produce the final consolidated review.

## Summary

This paper proposes TopoSD, a method for lane segment perception that integrates standard-definition map (SDMap) priors into an online HD map construction pipeline. The authors introduce two complementary SDMap encoding methods — spatial map encoding (rasterizing road geometry into 2D canvas maps with curvature information) and map tokenization (encoding polyline instances as token vectors via a Transformer encoder) — which are fused into the BEV feature extraction stage. They further propose a Topology-Guided Decoder (TGD) that uses a predicted adjacency matrix to iteratively refine both geometric and topological features via successor/predecessor feature propagation. On the OpenLaneV2 benchmark, TopoSD achieves 40.2% mAP (+6.7) and 34.5% TOP (+9.1) over the strong LaneSegNet baseline.

## Strengths

- **Complementary SDMap encoding methods, cleanly validated by ablation**: Table 3 (Exp 1–4) shows that spatial encoding alone yields +3.3 mAP/+3.5 TOP, tokenization alone yields +3.7 mAP/+5.1 TOP, and their combination yields +5.6 mAP/+5.3 TOP over the LaneSegNet baseline. This provides direct, disentangled evidence that both encodings contribute meaningfully.

- **Topology-Guided Decoder produces measurable improvements**: Comparing Exp 6 and Exp 7 in Table 3, adding TGD improves AP\(_{ls}\) from 37.8 to 38.6 and TOP\(_{lsls}\) from 32.0 to 34.5 (+2.5). The gain is concentrated on the topology metric, consistent with the mechanism's design intent.

- **Robustness to SDMap noise is quantitatively demonstrated**: Table 4 shows that training with noise augmentation (rot5_std5_prob0.5) reduces the mAP drop under noisy test inputs from –41.3% to –1.4%, and the TOP drop from –29.3% to –2.2%. This is a practical and well-executed study.

- **Inference efficiency validated on real hardware**: Table 5 reports 3.3 FPS on V100 for the full model, and the paper additionally provides ONNX deployment latency on Jetson Orin X (2–4 ms for SD fusion modules under FP16), demonstrating that the added SDMap processing is lightweight enough for deployment.

- **Large-margin improvements on a challenging benchmark**: The main results (+6.7 mAP, +9.1 TOP) over a strong baseline (LaneSegNet) are substantial, and Table 2 confirms consistent gains across all bucket metrics (DET\(_{ls}\), DET\(_{a}\), DET\(_{t}\), TOP\(_{lsls}\), TOP\(_{lste}\), OLS score).

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

- **P-MapNet comparison uses a modified input representation, reducing interpretability**. The table caption states the authors "follow the official implementation regarding the cross-attention, OSM-CNN and the downsampling settings" for the P-MapNet baseline. However, the body text (line 194) clarifies: "For the LaneSegNet model incorporating P-MapNet, we utilized our spatial encoded maps as SDMap inputs." This means the "LaneSegNet + P-MapNet" rows in Table 1 use TopoSD's own map encoding as input rather than the raw OSM raster data that P-MapNet was designed to process. The comparison is therefore not a direct replication of P-MapNet but a hybrid. While the disclosure is present in the text, the table row labels (and the implication that this is a "fair comparison with contemporary works") could mislead readers into thinking this is the original P-MapNet. The authors should either (a) run the original P-MapNet pipeline with its native input encoding, or (b) relabel the rows to make the hybrid nature explicit (e.g., "P-MapNet fusion + TopoSD encoding").

- **Spatial map encoding is underspecified for reproducibility**. The description (lines 104–106) mentions drawing SDMap polylines into "different canvas maps" with "thick lines" using "cosines and sines of the inclination angle of the road line segments to express the curvature." This leaves several key details unspecified: the number of canvas maps/channels, how the inclination angle is rasterized per pixel (e.g., for a polyline segment spanning multiple pixels), what "thick lines" means quantitatively (line width in pixels), how overlapping or crossing roads are handled, and the exact output tensor dimensions before the CNN. Since spatial map encoding is presented as one of the two core encoding contributions, these details are needed for replication and critical assessment.

- **No variance or confidence-interval reporting**. All results in Tables 1, 2, 3, and 4 are single-run numbers with no standard deviations or multi-seed averages. The gains from the Topology-Guided Decoder (+0.8 AP\(_{ls}\), +2.5 TOP\(_{lsls}\) in Exp 6→7) and from some fusion-position choices (e.g., Exp 4→6: +0.8 mAP) are modest enough that they could be within run-to-run variance. Reporting at least 2–3 seeds with mean and std for the main table and key ablations would substantially strengthen confidence in the claims.

- **The Topology-Guided Decoder's closed-loop dynamics are not analyzed**. The adjacency matrix is predicted from the same instance queries that it then reweights (line 126: "a topology head is used to predict the topology adjacency matrix... Then we use this predicted topology matrix to fuse the geometrical information of the predecessor and the successor"). This creates a potential feedback loop where the queries produce the topology, which then modifies the queries, which then produce new topology, etc. The paper does not discuss the risk of mode collapse (e.g., the decoder learning to always predict near-identity or fixed-pattern adjacency matrices) or provide analysis of how the predicted adjacency matrices evolve across decoder layers. While the ablation shows the mechanism works empirically, a deeper diagnostic would strengthen the claim that genuine topology-geometry mutual enhancement is occurring rather than the model simply learning a fixed reweighting pattern.

### Trivial
None.

## Nice-to-Haves

- A per-scenario breakdown (e.g., urban vs. rural, dense vs. sparse road networks) of where the SDMap encoding helps most would provide additional insight into the method's strengths and limitations.
- The source of the SDMap data (OpenStreetMap vs. proprietary) could be stated explicitly in the dataset description.

## Removed Points

These points were raised in the reviews but have been removed after verification against the paper:

- **Claim that existing approaches "ignore" topology-geometry interaction is overstated**: The paper says "the mutual influence of topology and geometry has not been fully explored" (line 121), which is a measured claim. No removal needed — the critic's concern is not a valid weakness.
- **"Indispensable" design claim not fully supported**: The paper's ablation (Table 3, Exp 2→4→6) shows each added design component improves results. The word "indispensable" is a rhetorical flourish; the evidence does support the claim that all components contribute. Removed as overly pedantic.
- **Y-axis scale inconsistency across subfigures**: This is a visual formatting choice, not a substantive issue. Removed per formatting/style rule.
- **Comparison with SMERF not clearly differentiated**: The paper explicitly states its tokenization builds on SMERF but encodes "a larger range" (line 79), and the spatial encoding is an entirely additional contribution. The distinction is adequately drawn. Removed.
- **Missing per-scenario analysis**: Demand for analysis outside the paper's stated scope. Removed.
- **Equation notation ambiguity**: The parentheses in Eq. 1 are correct and unambiguous. Removed.

## Novel Insights

The harsh critic's observation about the P-MapNet comparison — that replacing P-MapNet's native OSM raster input with TopoSD's spatial encoded maps conflates input representation with fusion mechanism — is the most valuable meta-insight. It means the "LaneSegNet + P-MapNet" row (33.2 mAP) primarily tests P-MapNet's cross-attention fusion architecture operating on TopoSD's encoding, not the original P-MapNet method. The gap between this row (33.2) and Ours-1 (39.9) therefore reflects the combined effect of TopoSD's encoding strategy *plus* its simpler additive fusion design, rather than the fusion mechanism alone. A cleaner comparison would require either feeding P-MapNet its original OSM raster input or adding a row that uses TopoSD's fusion method with P-MapNet's original input.

The critic's concern about TGD's closed-loop dynamics (topology predicted from queries that are then reweighted by the same topology) is also a genuinely useful note: the empirical +2.5 TOP gain is real, but without visualizing the learned adjacency matrices or tracking their evolution across decoder layers, the paper does not fully dispel the concern that the decoder might learn shallow reweighting patterns rather than genuine mutual refinement.

## Suggestions

1. **Clarify the P-MapNet baseline**: In Table 1, either run the original P-MapNet pipeline with its native OSM raster input (to provide a true comparison), or rename the rows to "LaneSegNet + P-MapNet fusion w/ TopoSD encoding" to avoid misleading readers about what is being compared.

2. **Provide multi-seed statistics**: Run at least 2–3 seeds for Table 1 (main results) and Table 3 (ablation, especially Exp 6 vs. Exp 7) and report mean ± std. This is the highest-leverage improvement to the paper's evidence quality.

3. **Detail the spatial map encoding**: Specify the number of canvas channels, the rasterization resolution, how inclination cos/sin values are assigned per pixel, line width in pixels, and how overlapping road polylines are composited. Even a paragraph in the supplement would suffice.

4. **Analyze the Topology-Guided Decoder**: Visualize a few predicted adjacency matrices from different decoder layers to show they are non-trivial and evolve meaningfully. Compare the topology prediction accuracy with and without TGD to confirm the gain is not merely from added parameters.

5. **Standardize noise-study figure axes**: The four subfigures in Figure 4 use different y-axis ranges, making cross-metric comparison harder than necessary. Using a common y-axis range (e.g., 0–45) would improve readability.
