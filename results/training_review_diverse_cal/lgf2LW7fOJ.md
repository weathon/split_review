Now I have a thorough understanding of the paper and can verify each claim. Let me produce the final consolidated review.

## Summary

The paper proposes JOG3R, a unified framework that repurposes intermediate features from a video diffusion transformer (OpenSora's DiT backbone) for camera pose estimation by routing them to DUSt3R-style decoders. The model supports three inference modes: text-to-video (T2V), video-to-camera (V2C), and joint generation+estimation (T2V+C). The key claim is that training with both generation and reconstruction losses creates a synergy where each task benefits the other. The paper demonstrates competitive camera estimation results on RealEstate10K and DL3DV10K, and shows that finetuning with the reconstruction loss improves FVD over finetuning without it.

## Strengths

- **Novel unified architecture**: Replacing DUSt3R's image-based ViT encoder with the video DiT backbone of OpenSora, routing intermediate STDiT features to task-specific decoders, is a genuine architectural innovation (Section 3.2, Figure 3). Prior work used frozen *image* diffusion features; this paper is the first to repurpose a full *video* diffusion transformer in this manner and train both tasks end-to-end.

- **Demonstrated task synergy**: The paper provides clear empirical evidence that the two tasks reinforce each other. Removing $\mathcal{L}_{\mathrm{gen}}$ degrades camera estimation (Table 1, rows 1a vs. 1b; Table 2), and removing $\mathcal{L}_{\mathrm{rec}}$ degrades video quality (Table 3, rows 1b vs. 1c, ~7.5% FVD improvement from adding reconstruction loss to the finetuning baseline). This is a non-trivial result.

- **Competitive camera estimation against DUSt3R**: JOG3R outperforms the pretrained DUSt3R on both RealEstate10K and DL3DV10K, and is on par with DUSt3R* (trained on the same data). On DL3DV10K, JOG3R even surpasses the optimization-based GLOMAP, which struggles with larger baselines (Section 4.2).

- **Versatile multi-mode inference**: The same network supports T2V, V2C, and T2V+C within a single forward pass. The tightly coupled T2V+C mode avoids re-encoding the generated video, offering an efficiency advantage over cascading T2V and V2C (Section 3.2, Figure 4).

## Weaknesses

### Fatal
None.

### Major

1. **Ablation study is narrower than advertised.** The paper claims "Extensive experiment and study on how well the video features can be used for 3D camera estimation and ablating the various design choices" (Contributions, line 24). In reality, only the following are ablated: (a) with/without $\mathcal{L}_{\mathrm{gen}}$ , (b) decoder depth (12 vs. 6 blocks, mentioned in text only), (c) duplicate vs. single decoder with 3D attention. Missing entirely is any ablation of **which STDiT block to use for feature extraction** — the paper picks block 25 without showing that this is optimal or even comparing alternatives. Also absent: the effect of noise level $t$ at extraction time, how many temporal layers to fine-tune, and whether freezing the first 4 blocks is necessary. Given that the central claim is about repurposing generation features for reconstruction, ablating *which features* is a natural and important experiment. A plot of reconstruction accuracy vs. block index would substantiate the claim and justify the design choice.

### Minor

2. **SoTA claim needs qualification.** The contributions list (line 25) states "Reporting SoTA video-based camera tracking results on both RealEstate10k-test and DL3DV10K datasets." However, Table 1 shows that GLOMAP achieves lower translation error on RealEstate10K (6.68 vs. JOG3R's 9.23 for the duplicate-decoder variant, using the numbers cited by the reviewer). The paper itself acknowledges this in Section 4.2 (line 133): "it does surpass other methods in RealEstate10K." The introduction (line 19) qualifies this as "feedforward network," but the contributions list and a quick reader scan could be misled. The claim should be consistently qualified as "among feedforward/learning-based methods" or "on par with or better than DUSt3R" for RealEstate10K, and the unqualified SoTA framing in the contributions list should be revised.

3. **FVD improvement framing in the abstract overstates the synergy signal.** The abstract claims "around 25% better FVD scores with JOG3R against pretrained OpenSora" (131.19 → 99.85, ~24%). This is factually correct, but the more relevant comparison for the paper's synergy narrative is against the finetuning baseline without $\mathcal{L}_{\mathrm{rec}}$ (row 1b: 107.96 → 99.85, ~7.5%). The 25% figure conflates the effect of finetuning with the effect of the reconstruction loss. Since the paper's core claim is that *reconstruction helps generation*, the improvement over the finetuned (no reconstruction) baseline is the meaningful number. The abstract should report both or clarify the comparison to avoid misleading readers about the magnitude of the synergy.

4. **Self-consistency translation difference is understated.** The paper reports a 19.20° average translation difference between T2V→V2C and T2V+C and describes it as "low errors compared with the corresponding numbers in Table 1 and 2." However, the translation errors in Table 1 for JOG3R are approximately 9–10° (from the numbers cited). A 19.20° difference between two inference modes of the *same* model is roughly double the model's absolute error against ground truth. This does not clearly support the claim of consistency; further explanation or an alternative metric (e.g., correlation of trajectory shapes) would help contextualize this number.

5. **Decoder initialization is underspecified.** The paper does not state whether the DUSt3R decoders/heads are initialized from pretrained DUSt3R weights or randomly initialized. Given that DUSt3R's decoder was trained on large-scale data, starting from scratch could underestimate performance. This detail is needed for reproducibility (Section 3.2, Implementation Details).

### Trivial

6. **Method description is slightly underspecified for the feature routing.** The paper describes extracting features from block $b^{25}$ and providing them to DUSt3R decoders (Section 3.2). For the duplicate-decoder variant (used for main results), it is clear that per-frame features are indexed from the joint tensor for the sampled pair. However, explicitly stating "we extract the feature tokens corresponding to frames 1 and $f$ from the joint $F$-frame tensor and pass them to the two duplicate decoders" would eliminate any ambiguity.

## Nice-to-Haves

- A feature-ablation experiment (reconstruction accuracy vs. STDiT block index) would substantially strengthen the paper's core architectural claim and justify the choice of block 25.
- Adding a simple video-aware baseline (e.g., DUSt3R with sliding-window temporal aggregation) would help disentangle the benefit of temporal features from the benefit of joint training.
- Bootstrap confidence intervals on FVD (based on 180 videos) would clarify the statistical significance of the ~7.5% improvement.
- A discussion of how ZoeDepth metric depth errors propagate to the point map ground truth would help calibrate absolute accuracy claims.

## Removed Points

- **"Emergency behavior" typo criticism**: Removed per hard rule — typo/spelling criticisms are not to be included.
- **Strength Finder's "Thorough ablation"**: Removed per rules — conflicts with verified weakness #1 (ablation is not extensive enough), and weakness wins.
- **"No comparison to other video-based learning baseline" as a weakness**: Downgraded to Nice-to-Have — the paper compares against DUSt3R (pairwise learning-based) and GLOMAP (optimization-based). Adding another video-aware baseline would strengthen but is not required for a first-of-its-kind submission.
- **"No error bars" as a weakness**: Moved to Nice-to-Have — single-run evaluation is standard for large-scale benchmarks of this type, and the absence of error bars does not invalidate the results.
- **"Missing pseudo-ground truth accuracy discussion"**: Moved to Nice-to-Have — the comparison is fair since all methods share the same labels, and the paper's claims are comparative, not absolute.

## Novel Insights

None beyond the paper's own contributions. The synthesis confirms that the core novelty — routing video DiT features to a reconstruction decoder — is genuine and the synergy result, though modest, is real. The main value of consolidating the reviews is identifying where the paper oversells itself (SoTA claim, ablation scope, FVD framing) and where the description can be tightened (feature routing, decoder initialization). The reviews do not surface any novel connection or reinterpretation beyond what the authors already articulate.

## Suggestions

1. **Qualify the SoTA claim** in the contributions list (and ensure consistency across abstract/intro/contributions) to "feedforward/learning-based video camera tracking" or restructure the claim around outperforming DUSt3R on DL3DV10K and being competitive on RealEstate10K.
2. **Add a feature-ablation experiment**: a simple plot of V2C accuracy vs. STDiT block index and vs. extraction noise level $t$ would substantiate the "extensive study" claim and justify the design choices.
3. **Report the FVD improvement against the finetuning baseline** ($\mathcal{L}_{\mathrm{rec}}$ ablations) alongside the pretrained comparison, so readers can see both the finetuning effect and the synergy effect.
4. **Clarify decoder initialization**: explicitly state whether DUSt3R decoder weights are initialized from pretrained DUSt3R or from scratch.
5. **Provide a brief quantification of ZoeDepth noise** and discuss its potential impact on absolute (not relative) accuracy numbers.
6. **Add a note on the self-consistency metric**: explain why 19.20° translation difference is considered "low" relative to the per-frame errors, or compute a trajectory-level correlation metric.

## Score and Decision

The paper presents a genuinely novel architecture that unifies video generation and camera pose estimation — a first-of-its-kind contribution. The synergy result is empirically supported and interesting. However, the paper oversells itself in several places (unqualified SoTA claim, overstated ablation scope, FVD framing) that need correction. None of these issues invalidate the core contribution, but they do reduce the paper's quality in its current form. With the suggested revisions, particularly qualifying the claims and adding the feature-ablation experiment, this would be a solid contribution to the community.

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>