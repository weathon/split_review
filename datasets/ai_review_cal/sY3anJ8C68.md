- Decision: Accept
- Avg Score: 6.25
- Scores: 6, 5, 6, 8
Now I have a thorough understanding of the paper and have verified the reviewer claims. Let me write the consolidated review.

## Summary

This paper proposes E-MAC, a video object counting framework with three components: (1) Temporal Collaborative Fusion (TCF) using optical flow to align density maps across frames, (2) Density-Embedded Masked Modeling (DEMO) that treats the density map as a second modality in a masked autoencoder, and (3) Spatial Adaptive Masking (SAM) that uses density maps to selectively retain foreground tokens during training. The paper also introduces DroneBird, a large-scale video dataset of birds captured from a drone viewpoint, with 3.6M annotations and multi-attribute labels. Experiments on four datasets show state-of-the-art or competitive results.

## Strengths

- **New large-scale video bird counting dataset (DroneBird):** The paper introduces the first video bird counting dataset from a drone viewpoint, with 3,686,409 annotations, 9,389 trajectories, multi-attribute labels (illumination, density, perspective, distance, posture), high resolution (up to 2160×4096), and a wide density range (8–673 objects per frame). This fills a gap in existing datasets which are mostly human-centric or single-image. (Section 3, Table 1)

- **Clear ablation evidence for all three contributions:** On the FDST dataset, the ablation study (Table 2) isolates each component: TCF provides 5%–16% improvement (Exp I→II), SAM provides 32% MAE improvement (Exp II→III), and DEMO provides 27% MAE improvement (Exp II→IV). The full model (Exp V) achieves 1.29 MAE, a 47% reduction from the baseline (2.45). Loss ablations (Table 3) similarly validate each loss term's contribution.

- **Competitive results across diverse datasets:** E-MAC achieves best MAE/RMSE on Mall (1.35/1.76), FDST (1.29/1.69), VSCrowd (6.0 MAE), and DroneBird (38.72/42.92), outperforming both image-based and video-based methods including recent ones like STGN and FRVCC (Table 1). The evaluation spans indoor (Mall), outdoor human crowds (FDST, VSCrowd), and natural bird flocks (DroneBird).

- **Thorough hyperparameter analysis:** The paper systematically studies the background retention probability \(\mathcal{P}\) (Fig. 3a), mask ratio (Fig. 3b), and loss weights \(\lambda_{1-4}\) (Fig. 3c–f), with clear explanations of the observed trends (e.g., the downward-rebound curve for \(\mathcal{P}\), the optimal mask ratio at 0.72).

## Weaknesses

### Fatal

None.

### Major

- **No variance or significance reporting:** All results are single-run point estimates with no standard deviations, confidence intervals, or significance tests. This is a serious gap because several reported gains are small: on DroneBird, the MAE improvement over MAN (image-based) is 38.72 vs. 39.11 (~1%), and on VSCrowd the RMSE is tied with GNANet (10.3 vs. 10.2). The reader cannot assess whether these differences are reliable. The paper should report results over multiple runs with mean ± std.

- **SAM's reliance on ground-truth density during training is not disentangled from genuine learned representations:** SAM sorts image tokens by values in the ground-truth density map and retains the highest-density tokens (or, with probability \(\mathcal{P}\), the lowest). While the paper is transparent about this (line 148: "We sort the ground-truth density map"), the ablation showing a 32% MAE improvement from SAM (Exp II→III) conflates the benefit of using GT labels as an input filter with any learned masking strategy. The paper would be substantially strengthened by a control experiment — e.g., comparing SAM against (a) random masking at the same mask ratio, or (b) masking guided by predicted density from a warmup model. Without such controls, the true generalization of SAM as a method (rather than a supervised training heuristic) is unclear.

- **DroneBird dataset is insufficiently documented in the main paper for standalone evaluation:** The main paper lacks: (1) number of videos and total frames; (2) train/val/test splits; (3) explicit release/availability statement; (4) annotation protocol details (e.g., how occlusions were handled). The per-attribute experimental results are shown only as a small embedded figure (Fig. 1, right part) with no numerical values — the bars are unreadable at print scale. A dataset of this scale deserves a formatted table with numerical MAE/RMSE per attribute. These gaps prevent the community from independently validating or using the dataset.

### Minor

- **"Self-representation learning" framing is overstated:** DEMO takes the density map (derived from point annotations) as both input modality and reconstruction target. This is a supervised multi-modal masked regression task, not unsupervised representation learning as in MAE (which reconstructs the raw image without labels). The paper calls this "self-representation learning" a dozen times (abstract, introduction, method, conclusion) but the mechanism is better described as "supervised masked multi-modal regression." This does not invalidate the contribution but should be corrected for clarity.

- **Ablation baseline (Exp I, "pure transformer") is underspecified:** The paper describes it only as "density map regression in a pure transformer" (line 374). The reader cannot determine the architecture (e.g., ViT with what decoder head?), training recipe, or parameter count relative to the proposed method. While the relative improvements across ablations are still meaningful, a clearer baseline specification would aid reproducibility and help assess whether the starting point is competitive.

- **Dirichlet distribution's role in SAM is incompletely described:** The paper states that the symmetric Dirichlet distribution "is used to determine the number of tokens to retain for the image modality and density map modality" (line 147), but never explains the actual sampling process for \(\mathcal{N}_I^\text{ret}\) and \(\mathcal{N}_D^\text{ret}\) or how the mask ratio (0.72) interacts with this distribution. This is a gap for reproducibility.

- **Clarification needed on whether PWCNet is frozen or fine-tuned:** The loss includes \(\mathcal{L}_{\text{opt}}\) (Eq. 3), which optimizes the optical flow network via warped image reconstruction. Line 211 says "pre-trained PWCNet." If the network is fine-tuned during training, this is a notable design choice that could affect warping quality — the paper should state this explicitly and ideally provide a sensitivity analysis.

### Trivial

- None that pass filtering.

## Nice-to-Haves

- The per-attribute results on DroneBird (currently in Fig. 1 as small unreadable bars) would be much more useful as a formatted table with numerical MAE/RMSE values.
- A comparison against a variant of SAM that uses predicted (rather than GT) density maps to generate masks would clarify whether the idea can be bootstrapped without label leakage.
- Adding standard deviations to all main results (Table 1) would resolve the most significant weakness.
- The mask ratio study (Fig. 3b) is done without temporal information (stated on line 418). While the paper explains this is "to more clearly evaluate the impact," including the temporal variant would strengthen the analysis.

## Removed Points

These points are flagged to be removed — treat them with caution:

1. **"The method section does not describe any cross-attention for temporal fusion beyond the cross-attention between warped and current density maps" and introduction/method inconsistency claim.** — Factually wrong. The paper explicitly describes cross-attention at lines 123–124 ("The cross-attention between \(\hat{D}_{t-1}^\text{warp}\) and \(\hat{D}_t\) then produces \(\hat{D}^{\text{res}}_t\)") and the introduction mentions it at line 31. The introduction's "post-fusion strategy" phrasing (line 37) is consistent with this description.

2. **"Missing: any discussion of density-guided masking methods in counting (e.g., attention maps from density to guide feature learning)"** — Per instructions, missing related works should not be mentioned as weaknesses since external knowledge cannot be confirmed.

3. **Typographical note about "fore-background"** — This is a formatting/style nitpick, removed per instructions.

4. **"Mask ratio study only uses a model without temporal information — strange, since temporal is a core component. Why exclude it?"** — The paper explicitly explains its reasoning: "To more clearly evaluate the impact of the mask ratio, these experiments were specifically performed on the E-MAC without considering temporal information" (line 418). This is a legitimate experimental design choice, not a weakness.

5. **"The connection to MultiMAE is stated but not explained"** — The paper states it uses "pre-trained ViT-B from MultiMAE" as the encoder (line 211). This is sufficiently clear for a design choice. The question of how two modalities are projected is a reasonable implementation detail but not a missing explanation.

6. **Criticism that on DroneBird "the gap between video and image methods is enormous (factor >2)" as a weakness** — This actually highlights the value of DroneBird as a challenging benchmark where existing video methods fail, strengthening the case for a new method/dataset rather than undermining it.

## Novel Insights

None beyond the paper's own contributions. The harsh and strength reviews largely converge on the paper's genuine strengths (new dataset, clear ablation, competitive results) and its non-fatal weaknesses (no variance, SAM's GT reliance, incomplete dataset documentation). The key insight from synthesizing both reviews is that the core concern — SAM's use of GT density during training — is real but does not undermine the paper's contributions because: (1) the paper is transparent about it, (2) at test time the density map is fully masked and the model must reconstruct from images alone, and (3) the other two components (DEMO and TCF) are validated independently. The most impactful single improvement would be adding multiple-run statistics with error bars.

## Suggestions

1. Report all main results (Table 1) as mean ± std over at least 3 runs with different random seeds.
2. Add a control experiment for SAM: compare against random masking at the same mask ratio and, if possible, against masking guided by predicted density from a pretrained warmup model.
3. Include a dedicated table with numerical per-attribute MAE/RMSE on DroneBird (replacing or supplementing the small bars in Fig. 1).
4. Provide in the main paper: number of videos, total frames, train/val/test splits, and a release/availability statement for DroneBird.
5. Clarify the Dirichlet sampling process for \(\mathcal{N}_I^\text{ret}\) and \(\mathcal{N}_D^\text{ret}\) and how it interacts with the mask ratio.
6. Replace "self-representation learning" with more accurate terminology (e.g., "supervised masked multi-modal regression") throughout.
7. Specify whether PWCNet is frozen or fine-tuned, and if fine-tuned, report sensitivity.
