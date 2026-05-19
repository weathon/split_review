- Decision: Reject
- Avg Score: 3.00
- Scores: 3, 3, 3, 3
Now I have all the information needed. Let me produce the final consolidated review.

## Summary

The paper presents ViMoE, an empirical study of integrating Mixture-of-Experts (MoE) layers into Vision Transformers (ViT). The key contributions are: (1) introducing a shared expert that stabilizes MoE training and eliminates the need for exhaustive layer scanning, (2) using routing heatmaps to empirically identify which MoE layers truly specialize (deep layers) and which do not (shallow layers), and (3) deriving efficient architectures by retaining only critical MoE layers. Experiments on ImageNet-1K classification and ADE20K semantic segmentation, all starting from DINOv2 pretrained weights, support the main findings.

## Strengths

- **Shared expert demonstrably stabilizes MoE training across different numbers of MoE layers (Fig. 2(b))**: With a shared expert, accuracy remains nearly constant (~84.2%) for all values of L (1 to 12), whereas without a shared expert, accuracy drops sharply after a peak (e.g., from >84% down to ~83.6% for L=12). This is a clear, practically useful finding.

- **Routing heatmaps provide a diagnostic tool to identify which MoE layers truly specialize (Fig. 3, Fig. 5)**: The heatmaps show that only deep MoE layers (e.g., l=1,2) exhibit clear diagonal patterns where each expert handles distinct classes, while shallow layers (l=12) show near-uniform routing. This evidence directly supports the claim that most MoE layers can be removed without harming accuracy.

- **Efficient ViMoE derived from routing analysis outperforms the DINOv2 baseline at modest cost (Table 1)**: With N=8, L=2 and shared expert, ViMoE achieves 84.2% top-1 accuracy using 24.4M activated parameters and 6.74G FLOPs, improving over the DINOv2 baseline (83.1%, 22.0M, 6.14G) and matching the costlier all-layer MoE version (84.3%, 36.2M, 9.77G).

- **Image-level routing matches token-level accuracy while being substantially more efficient for classification (Table 6)**: Both strategies achieve 84.2–84.3% accuracy, but image-level routing activates only 2–5 experts per image versus 10–94 for token-level routing. This is a practical design insight.

- **Cross-task validation on semantic segmentation confirms generalizability of the core findings (Table 2, Fig. 4)**: The same routing patterns (deep layers specialize, shared expert stabilizes) hold on ADE20K, and using only the last MoE layer (L=1) yields 51.5 mIoU, surpassing the DINOv2 baseline (50.8) and denser configurations.

- **Controlled comparison shows sparse MoE outperforms dense structures with matched activated parameters (Table 7)**: ViMoE with N=8, L=2 (24.4M activated params) achieves 84.2%, while a dense model with the same activated parameter count achieves only 83.6%. This directly isolates the benefit of MoE's divide-and-conquer routing over simply adding dense capacity.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

- **No variance or run-to-run statistics reported despite claims about "stability"**: The paper argues that shared experts stabilize training and prevent performance degradation, but all accuracy numbers appear to be single runs. Reporting at least 2–3 seeds with standard deviations would substantiate the stability claim. This is especially important for the comparison between "with shared expert" and "without shared expert" trends in Fig. 2.

- **Routing degree analysis is a post-hoc observation, not a validated finding**: The observation that optimal configurations cluster around 32–64 routing combinations (D ≈ 32–64) is interesting but derived entirely from the configurations that happened to work. No independent prediction or systematic test is conducted to verify the claim that "approximately 32 to 64 routing combinations are sufficient." The paper presents this as speculation ("we suggest," "this implies"), but the phrasing in the text (e.g., "implies that approximately 32 to 64 routing combinations are sufficient") could be read as a stronger claim than the evidence supports. This should be framed more cautiously as a suggestive pattern.

- **Segmentation comparison mixes decoder architectures, making the "outperforms" claim a system-level statement rather than a backbone-level comparison**: Table 5 shows ViMoE (ViT-S/14, Linear decoder, 50G FLOPs) alongside methods using UPerNet decoders (605G FLOPs for B/16). While the Decoder column is clearly labeled and the comparison is transparent, the claim that "ViMoE significantly outperforms other methods, including those based on ViT-B/16, while requiring substantially less computational effort" conflates backbone and decoder differences — the FLOPs savings are dominated by the decoder choice, not the MoE backbone. The comparison against the DINOv2 baseline (same linear decoder) is fair, but the broader comparison should be caveated more explicitly.

- **Routing heatmaps are qualitative and lack a quantitative specialization metric**: The observation that deep MoE layers specialize while shallow ones do not is supported by visual inspection of heatmaps, but no quantitative metric (e.g., entropy of class distributions per expert, mutual information, expert-class correlation) is provided. A numerical measure would strengthen the claim and make it more reproducible.

- **Only DINOv2 pretrained weights are tested, limiting the generality of the "empirical study"**: The paper only evaluates starting from DINOv2 ViT-S/14 and ViT-B/14 initializations. Whether the shared expert stabilization and routing insights transfer to other pretrained ViTs (e.g., MAE, CLIP, DeiT) or other architectures is not explored, which narrows the scope of the "empirical study" framing.

### Trivial

- The routing degree formula \(D = (C(N,k))^L\) is mathematically correct (since \(C(N,1)=N\), giving \(N^L\)), but the \(C(N,k)\) notation could cause confusion since k=1 throughout. Simplifying to \(D = N^L\) would be clearer.

## Nice-to-Haves

- A direct control experiment that increases the dense baseline's width to match the activated parameter count of the MoE model would strengthen the comparison between sparse and dense structures. Table 7 partially addresses this, but the dense models add FFNs only in specific layers rather than uniformly widening the model.

- An analysis of how the shared expert's pretrained weight initialization (copied from the FFN) affects its ability to learn "common knowledge" versus the routed experts would be interesting, though not required for the paper's main claims.

## Removed Points

- **"Unfair segmentation comparisons invalidate headline claims" (Harsh Critic's #1, called "structural" and potentially "deceptive")**: REMOVED as a fatal/major issue. The table explicitly lists the decoder type for each method in a dedicated column. The comparison is transparent. The paper's primary claim about segmentation is "ViMoE achieves performance superior to the DINOv2 baseline with only a slight increase in cost" — this is a fair comparison (both use linear decoders). The secondary comparison against UPerNet methods is a system-level comparison where the differences are fully disclosed. Characterizing this as "deceptive" is unjustified given the transparent table labeling.

- **"Routing strategy ablation undermines strong motivation about task-objective alignment"**: REMOVED. The paper explicitly addresses this (lines 389–390), noting that image-level routing is "simpler" and achieves the same accuracy while being more efficient. There is no contradiction — the paper's motivation includes both alignment and efficiency.

- **"Routing degree formula is incorrect"**: REMOVED. The formula \(D = (C(N,k))^L\) with k=1 gives \(C(N,1)=N\), so \(D = N^L\), which is correct. The critic's concern that "D = N^L not (C(N,k))^L" misunderstands that C(N,1) = N — these are the same expression.

- **"Image-level routing for classification may discard spatial information"**: REMOVED. The paper discusses this design choice in Sec. 3.2 and explicitly uses token-level routing for segmentation precisely because spatial information matters there. For classification, the [CLS] token representation is standard practice.

- **All pure formatting/style nitpicks, missing appendix concerns, typo complaints**: REMOVED as parser artifacts or irrelevant.

- **Generic strengths about "important problem"**: REMOVED. Only concrete, evidenced strengths are retained.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. Add standard deviations across 2–3 seeds for the main accuracy comparisons, especially the "with vs. without shared expert" stability curves.
2. Add a quantitative specialization metric (e.g., entropy of class distributions per expert) to complement the qualitative heatmaps.
3. Tone down the routing degree claim to clearly frame it as a suggestive observation/hypothesis rather than an empirical finding.
4. In the segmentation results, add a caveat that the comparison against UPerNet methods reflects total system efficiency (decoder + backbone), not backbone superiority alone.
5. Consider testing at least one additional pretrained initialization (e.g., MAE or CLIP) to broaden the generality of the empirical findings.
