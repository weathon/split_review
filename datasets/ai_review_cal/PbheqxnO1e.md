- Decision: Accept
- Avg Score: 7.00
- Scores: 5, 8, 8
Now I have a complete picture. Let me produce the final consolidated review.

## Summary

This paper introduces a method to compress 3D Gaussian Splatting (3DGS) representations by storing only a sparse set of "parent" Gaussians and predicting "children" Gaussians on-the-fly via small MLPs powered by a shared hash grid and a modified self-attention mechanism. The key insight is that spatially nearby Gaussians share redundant information, so a parent point's features can be used to predict its children's positions, colors, opacities, scales, and rotations. Adaptive Tree Manipulation (ATM) allows children to be promoted to parents during optimization, and whole trees to be pruned. On the Mip-NeRF 360° dataset, the method achieves 19.5× storage reduction over 3DGS while simultaneously improving PSNR, and its largest configuration (C3) outperforms all prior compression methods in quality while remaining smaller than any of them.

## Strengths

1. **Dramatic storage reduction with improved quality on Mip-NeRF 360°**: The method achieves 19.5× storage reduction compared to 3DGS while also improving PSNR (Tab. 1, line 171). This directly supports the core claim of "dramatically reducing the hard drive footprint while featuring similar or improved quality."

2. **Largest configuration beats all prior works while staying smallest**: The C3 configuration uses only 20% of ScaffoldGS storage and 4.5% of 3DGS storage, yet achieves higher PSNR than both on Mip-NeRF 360° (Fig. 3, lines 163-164). This demonstrates that compression does not require a quality trade-off.

3. **Adaptive Tree Manipulation (ATM) is a novel and effective mechanism**: The ablation study (Tab. 2, lines 199-202) shows removing ATM causes a measurable PSNR drop, and Fig. 4 visually confirms that most parent nodes originate from promoted children, especially in geometrically complex regions. This mechanism goes beyond standard 3DGS cloning/splitting.

4. **Systematic ablation studies isolate each component**: Tables 2-4 quantify the impact of removing the hash grid, attention, ATM, scene contraction, and position/distance inputs, with clear PSNR drops (e.g., 0.8 dB without contraction, lines 193-210). This provides rigorous validation of each design choice.

5. **Self-attention mechanism demonstrably improves storage efficiency**: Adding attention reduces the number of parent points from 1.06M to 884K on average across Mip-NeRF 360° scenes, contributing to lower storage while maintaining quality (line 196-197).

6. **On-device feasibility demonstrated**: The method runs on iPhone 14 without out-of-memory errors, whereas 3DGS and ScaffoldGS fail for all benchmark scenes. Among methods that run on device, it achieves smaller storage and better rendering quality than LightGS and CompactGS (line 183).

## Weaknesses

### Fatal
None.

### Major

- **Missing runtime/timing analysis undermines claims about real-time and on-device execution**. The paper states "Our aim is to build an efficient GS representation, with low storage requirements, high-fidelity rendering and **real-time execution**" (line 143), claims prediction adds "negligible overhead" (line 46), and asserts the method can "unlock wide adoption of GS-based applications on resource-constrained devices" (line 48). Yet **zero timing measurements** are reported—no FPS, no inference latency, no comparison of the overhead of the prediction pipeline vs. the savings from fewer stored points. The on-device experiment (line 183) only checks memory feasibility, not rendering speed. If the hash-grid lookups, attention, and four MLPs per tree slow rendering by a meaningful factor, the practical deployment claim collapses. This is the most significant gap in the paper's evaluation relative to its own motivational framing.

### Minor

- **No ablation of the branching factor K**. The number of children K is set to "at most 2" (line 150) with no ablation of K=1, 4, 8, etc. Since the entire compression gain depends on storing one parent per K children, the choice of K is central and deserves analysis. Practitioners cannot make an informed trade-off without this data.

- **Warm-up training described as "crucial" but not ablated**. The paper states warm-up is "crucial" (line 136-137) and that without it the model produces "substandard performance," yet no ablation experiment quantifies this degradation. Given that 3DGS does not require warm-up, understanding the method's sensitivity to this component is important.

- **Ablation experiments conducted at 10K steps rather than full 30K**. The paper explicitly states this (line 187), and the 0.8 dB drop from removing scene contraction could differ with full training. While this is acknowledged, it limits the conclusiveness of the ablation results.

- **No statistical uncertainty reported for any metric**. PSNR differences among 3DGS variants are often within 0.1–0.2 dB. Single-run results without error bars or multiple seeds make it hard to assess whether reported advantages are significant. The claim of "best PSNR" on Mip-NeRF 360° (line 171) would be stronger with confidence intervals.

- **Theoretical concern about ATM deletion rule not isolated**. The paper deletes entire trees based on parent statistics only, arguing that important children would already have been promoted (line 125). A child that is moderately important but below the promotion threshold could be lost when its parent is deleted. The overall ATM ablation shows benefit, but a controlled ablation (delete based on parent stats vs. both parent and child stats) would better validate the deletion rule's safety.

### Trivial

- The phrasing "up to 20× reduction on average" (line 48) is slightly discordant—"up to" describes a maximum while "on average" describes a central tendency. The actual reported value is 19.5× (line 171), so the "up to 20×" framing is essentially correct but could be phrased more precisely.

## Nice-to-Haves

- **Hash-grid storage breakdown**: The paper reports total storage but does not decompose it into the hash grid, parent positions/scales, and MLP weights. If the hash grid itself is large, the net savings may be less impressive in certain settings.

- **Pareto curve with throughput axis**: Adding FPS vs. size measurements on a mobile device would directly support the on-device motivation and be more valuable than additional ablation studies.

- **Comparison with simple quantization baselines**: Standard 3DGS + vector quantization would provide context for whether the complexity of the proposed prediction pipeline is necessary to achieve the reported compression.

- **Clarify which configuration (C1/C2/C3) is used in the main quantitative table**: The text says "we report three configurations" (line 155) but it is unclear which one appears in Tab. 1 vs. how the three are distinguished.

## Removed Points

These points are flagged to be removed, treat them with caution:

- **"Attention mechanism is lightly described"**: The paper provides Eq. 1, explains the design choices (no positional embedding, permutation invariance, gated residual), and notes the empirical finding about the projection. The description is adequate for the paper's scope. Removed as a nitpick.

- **"Teaser figure claim is too strong without statistical backing"**: The teaser (line 25) shows a specific scene comparison and claims "Ours shows the best PSNR" for that scene. This is a qualitative illustration, not a general claim. Removed as a strawman.

- **"Overstated PSNR claims" (the critic's general framing)**: The paper explicitly qualifies "best PSNR" to the Mip-NeRF 360° dataset (line 171) and honestly acknowledges that ScaffoldGS has better PSNR on Tanks&Temples (line 172). The claim is not overstated; it is properly scoped. The no-error-bars concern is retained as a Minor weakness above; the "overstated" framing is removed.

- **"Missing comparison with CompactGS in size-quality plot"**: The paper does compare across all methods in Fig. 3, and the on-device section directly compares with CompactGS. The critic's phrasing "does not compare the rendering quality per unit storage with CompactGS" is inaccurate.

- **"Tanks&Temples narrative undermines central thesis"**: The paper explicitly acknowledges that ScaffoldGS has better PSNR on this dataset while noting 2.4× smaller storage. This is honest reporting, not a flaw. Removed.

- **"On-device comparison is inconsistent because baselines OOM"**: The paper's on-device claim is about feasibility ("can successfully run"), not speed. It is valid to note that 3DGS and ScaffoldGS OOM. The missing speed data is already captured under the Major weakness above. Removed as redundant/overlapping.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. **Report timing measurements** — at minimum, FPS on GPU and on the iPhone 14 for your method vs. LightGS and CompactGS (the baselines that fit in memory). This directly supports the on-device and real-time framing and is the single most impactful addition.

2. **Ablate the branching factor K** (e.g., K=1, 2, 4, 8) to show the storage-quality trade-off and give practitioners a principled way to choose K.

3. **Run the experiment with 3 random seeds** and report mean ± std for the main metrics to establish statistical significance, especially given the small PSNR differences among competing methods.

4. **Ablate the warm-up stage** to quantify its impact, since the paper describes it as "crucial."

5. **Provide a storage breakdown** (hash grid, parent positions/scales, MLP weights) to help readers understand where the savings come from.
