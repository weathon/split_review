---
job_id: 970e25d8-a0db-4194-b750-17dcd0f68cae
agent_id: ICLR_main_2026_2
status: COMPLETED
filename: Ir0HMkRpYb.pdf
paper: Stylos: Multi-View 3D Stylization with Single-Forward Gaussian Splatting
main_score_norm: 0.6
desk_reject: false
---
# Desk Rejection Assessment:
## Paper Length
Pass ✅.

## Topic Compatibility
Pass ✅. The paper is clearly within ICLR scope, it proposes a feed-forward representation learning and generative vision method for pose-free 3D stylization using transformer features and 3D Gaussian scene representations.

## Minimum Quality
Pass ✅. The submission contains all core scientific sections, including abstract, introduction, related work, method, experiments, quantitative/qualitative results, and conclusion, and it presents a coherent empirical study with enough technical substance to merit full review.

## Prompt Injection and Hidden Manipulation Detection
Pass ✅. I did not find any hidden prompts, suspicious instructions to automated reviewers, or other manipulative content in the provided paper text and figures.

# Expected Review Outcome:
## Summary
This paper presents Stylos, a feed-forward framework for 3D style transfer that takes one or more unposed content images plus a separate style image, and predicts a stylized 3D Gaussian scene together with camera parameters in a single forward pass. The method builds on a VGGT-style geometry backbone, introduces style injection through cross-attention blocks, and adds a voxel-level 3D style loss that aligns voxelized scene features with 2D style statistics. Experiments on CO3D, DL3DV-10K, and Tanks & Temples evaluate reconstruction, stylization consistency, artistic quality, efficiency, and controllable style interpolation.

## Strengths
1. The paper targets a meaningful problem setting. Moving from per-scene optimization to a single-forward, pose-free 3D stylization pipeline is practically important, especially for applications where reconstruction and stylization must happen quickly and on unseen scenes.

2. The overall system design is sensible and reasonably well motivated. Separating geometry prediction from style-conditioned appearance prediction is a good inductive bias, and the architecture in **Figure 1** helps communicate this split clearly: geometry heads are attached to the VGGT pathway, while style is injected through CrossBlocks before the style head. This figure is one of the stronger parts of the presentation because it makes the training-stage split and the geometry/style factorization relatively easy to follow.

3. The empirical results are broadly strong. In **Table 3**, Stylos is consistently best on the reported short-range and long-range consistency metrics across all four Tanks & Temples scenes. The margins are not tiny in several cases, for example on Garden long-range LPIPS/RMSE and on M60 short-range RMSE, which supports the central claim that the method improves cross-view consistency.

4. The speed advantage is compelling. **Table 4** shows that Stylos is much faster than optimization-based baselines and also faster than Styl3R in the reported setup. Even allowing for some caveats about resolution and protocol, the basic takeaway, namely that the proposed approach is efficient enough for practical use, is well supported.

5. The paper includes useful ablations on both the fusion design and the style loss. In **Table 1**, the global CrossBlock variant consistently improves over frame-only and hybrid variants on most metrics, which gives some evidence that globally shared style-conditioning better preserves multi-view structure. The qualitative examples in **Figure 2** are aligned with this claim: the global variant indeed appears to retain the pizza crust and topping layout more faithfully than the frame-only variant.

6. The voxel-level style loss is a reasonable attempt to make the style objective more 3D-aware than standard per-image statistics matching. The progression from image-level to scene-level to voxel-level losses in **Equations (3), (4), and (5)** is conceptually clean, and **Table 2** suggests that the 3D loss improves consistency and artistic score over the plain image-level loss.

7. The paper does a decent job showing that the method is not limited to a fixed number of views. The discussion around **Figure 4** and the view-count scaling analysis indicate some practical awareness about the tradeoff between more context and degraded quality when moving outside the training regime.

## Weaknesses
1. The main technical novelty is somewhat narrower than the paper sometimes suggests. The method is built heavily on existing components, VGGT for geometry, AnySplat-style feed-forward 3DGS prediction, standard transformer cross-attention for style injection, VGG-statistics style losses, and a CLIP loss in fine-tuning. The new ingredients are mainly the specific geometry/style pathway split and the voxelized statistics loss. That can still be a worthwhile contribution, but the paper occasionally presents the system as more architecturally distinct than it really is. This matters because for ICLR, the contribution should be judged relative to the amount of inherited machinery, not just the end-task improvement.

2. The paper does not sufficiently disentangle where the gains come from. The strongest headline results in **Table 3** and **Table 4** compare the full Stylos system against prior methods, but there is no clean decomposition showing how much improvement comes from:  
   (i) the stronger feed-forward 3D reconstruction backbone,  
   (ii) the global CrossBlock design,  
   (iii) the 3D voxel style loss, and  
   (iv) the two-stage training strategy.  
   The current ablations are too local. For example, **Table 1** only studies the CrossBlock topology using a pseudo-style reconstruction setup, and **Table 2** only studies the style loss while keeping the rest fixed. What is still missing is a proper factorial view of the method. This matters because otherwise the claimed contribution of the voxel loss and style-content fusion is hard to separate from simply starting from a very strong geometry foundation model.

3. The mathematical specification of the losses is weaker than it should be, and several details are underspecified. In **Equation (3)**, the notation appears inconsistent: the variance term uses $\mathcal{R}_{b,s}^{l}$ rather than $\mathcal{R}_{b,v}^{l}$, which looks like a typo but is still problematic because this equation defines one of the core baselines. More importantly, in **Equations (3)-(5)**, the operators $\mu(\cdot)$ and $\sigma(\cdot)$ are not defined precisely over which axes they are computed. Are these channel-wise moments over spatial positions, full-tensor moments, or something else? Since the paper invokes BN-style statistics, the natural interpretation is per-channel statistics over spatial locations, but this should be stated explicitly. Without that, the objective is not fully reproducible.

4. **Algorithm 1** is too incomplete to be truly informative. Line 9 appears truncated, and the actual formula for accumulating $L_{3D}$ is missing. The algorithm also hides the most important part, namely the precise definition of `VoxelizeAndFuse`, including voxel indexing, aggregation weights, handling of collisions, masking of empty voxels, and whether gradients pass through the point-to-voxel assignment or only through fused features. Since the voxel-space loss is one of the paper's key ideas, leaving its implementation at this level of abstraction weakens the paper materially.

5. The claimed geometric disentanglement is asserted more strongly than it is demonstrated. The paper repeatedly says that geometry is unaffected by style because geometry parameters are predicted only from backbone features, while style is used only for color prediction, see **Section 3.2.3**. But the full system includes stylization losses, rendering, and a shared representation pipeline during stage 1; moreover, the geometry branch and style branch are not entirely independent conceptually because the unprojected points and voxelized features are used downstream in a coupled manner. The paper does not provide a direct experiment showing geometry invariance under large style changes. For example, one could measure pose/depth/point consistency while varying the style image at inference. This matters because the main claim is not just good images, but geometry-aware stylization.

6. The evaluation protocol is not always as fair or transparent as it should be. In **Table 4** and Appendix A.4, the paper compares optimization-based methods at full resolution against feed-forward methods at their preset input resolutions, with Styl3R at $256 \times 256$ and Stylos at $448 \times 448$. This makes the timing comparison directionally useful, but not strictly apples-to-apples. Also, stylization quality can depend materially on resolution, which complicates interpreting the artness metrics. The paper should be more explicit that these comparisons bundle together method design and operating resolution.

7. The quantitative evidence for the 3D style loss is only modest. In **Table 2**, the difference between scene-level and 3D loss is quite small numerically: short-range LPIPS is identical, long-range LPIPS improves from 0.156 to 0.153, long-range RMSE is unchanged at 0.142, and ArtScore goes from 9.12 to 9.15. The qualitative examples in **Figure 3** suggest somewhat clearer benefits, but the table itself supports only a mild improvement, not a strong one. This matters because the voxel-space loss is framed as a central technical contribution.

8. The claims around scalability to dozens or hundreds of views are somewhat overstated relative to the evidence in the main paper. The text on **Page 7** says Stylos can process up to dozens or even hundreds of views, yet **Figure 4** only shows qualitative examples up to 64 views and the paper itself acknowledges degradation beyond 32 views due to train-test mismatch. If the method degrades outside the training regime and the backbone becomes less stable with more views, the scalability claim should be stated more cautiously.

9. The paper excludes at least one problematic baseline from the main quantitative comparison. On **Page 9**, StylizedGS is omitted from the main tables because of multiple failure cases, with extra numbers deferred to the appendix. I understand the practical reason, but excluding a baseline from the main comparison because it fails on some test styles is tricky. A stronger presentation would either include it with all failures counted, or clearly define a benchmark protocol that applies uniformly to all methods. Otherwise, there is room for cherry-picking concerns.

10. Some of the qualitative interpretation is stronger than what the figures incontrovertibly show. In **Figure 5**, Stylos does look competitive and often best, but several baselines also produce reasonably structured outputs, and the differences are not always as decisive as the text suggests. Likewise, **Figure 6** is visually appealing, but it is only a qualitative interpolation demo without any analysis of whether the interpolation is linear in style strength, preserves scene identity, or remains stable across viewpoints. These are nice add-ons, not strong evidence.

11. There are several clarity and notation issues that accumulate. Examples include the inconsistent use of $N$ and $V$ for number of views across sections, awkward tensor shapes in **Section 3.4** such as $\mathbb{R}^{C_l \times H_1 \times W_l}$ where $H_1$ looks suspicious, and minor grammatical problems throughout. None of these are fatal individually, but together they make the method harder to audit than it should be for a paper centered on a new loss and new fusion block design.

12. The literature positioning is good but still not fully satisfying in one respect: the paper calls Styl3R the closest related work, yet the comparative discussion remains fairly high level. Given how close the problem setting is, I wanted a sharper side-by-side methodological comparison in the main paper, especially on what exactly Stylos adds beyond stronger multi-view style propagation and a voxelized loss. Right now, the distinction is understandable, but not crisply established.

## Questions
1. Can the authors provide a sharper attribution study for the full gains in **Table 3** and **Table 4**? In particular, I would like to see variants of: VGGT/AnySplat backbone only, +CrossBlocks only, +3D style loss only, and +both. This would substantially increase my confidence that the proposed components, rather than the inherited reconstruction backbone, drive the reported performance.

2. Please clarify the exact definition of the style statistics in **Equations (3)-(5)**. Are $\mu(\cdot)$ and $\sigma(\cdot)$ computed channel-wise over valid spatial or voxel positions only? How are empty voxels handled in **Equation (5)**? A precise mathematical definition would help reproducibility.

3. What exactly is the voxel fusion rule in **Algorithm 1**? Please specify the voxel size used in the main paper setting, the weighting scheme, whether confidence weights are normalized per voxel, and whether gradients flow through voxel assignments. Right now this core part is too hidden.

4. Can the authors provide a direct geometry-invariance analysis under style variation? For example, fix the same content input and vary the style image, then report changes in predicted depth, camera poses, or Gaussian positions/scales. This would test the central claim that style affects appearance but not geometry.

5. The timing comparison in **Table 4** is interesting but currently mixes different resolutions and different optimization assumptions. Could the authors report either matched-resolution inference costs where possible, or at least a clearer normalized protocol? That would make the efficiency claims easier to interpret.

6. For **Table 2**, the quantitative improvement of the 3D style loss over the scene-level loss is fairly small. Do the authors have broader statistics, confidence intervals, or more scenes showing that the improvement is robust rather than anecdotal?

7. Why is StylizedGS omitted from the main quantitative tables instead of being included with failures counted? A precise evaluation rule here would help avoid ambiguity.

## Flag For Ethics Review
- No ethics review needed.

## Details Of Ethics Concerns
No major ethics concerns are evident from the submission. The paper uses public datasets and focuses on 3D stylization methodology. As with most generative visual methods, there are generic downstream misuse possibilities, but nothing in the paper raises a distinct ethics flag requiring specialized review.

## Soundness Rating
3: good. The method is technically plausible and supported by a substantial experimental section, but some core components, especially the voxel loss and its implementation details, are underspecified enough that I cannot call the paper fully airtight.

## Presentation Rating
2: fair. The paper is readable and the high-level idea comes through, but there are enough notation inconsistencies, missing definitions, and underexplained algorithmic details that the presentation falls short of what I would expect for a method-heavy paper.

## Contribution Rating
3: good. The paper makes a useful contribution by combining feed-forward pose-free reconstruction and stylization in a practically relevant way, with strong consistency and efficiency results, even if the incremental novelty of individual components is moderate.

## Overall Rating
6: Marginally above the acceptance threshold. But would not mind if paper is rejected. The paper has real practical value and solid empirical results, especially on consistency and speed, and it addresses an important setting. My hesitation comes from the limited disentanglement of where gains come from, the modest quantitative evidence for the voxel loss specifically, and the under-specification of some core equations and algorithms.

## Reviewer Confidence
4: confident. I am familiar with the relevant literature on 3D reconstruction, Gaussian splatting, and style transfer, and I checked the main technical claims and experiments carefully, although I did not independently verify implementation details beyond what is written.