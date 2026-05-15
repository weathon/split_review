Now I have a thorough understanding of the paper and all reviews. Let me produce the consolidated review.

## Summary

The paper proposes ETC, a text-to-video diffusion framework that eliminates separate temporal attention layers by stitching video frames into a spatial grid and relying solely on spatial attention for temporal modeling. It introduces Spatial-Temporal Mixed Embedding to distinguish inter-frame and intra-frame features, and Triple-Data Training that mixes caption-video, caption-image, and label-image data to reduce dependence on expensive video-text pairs. The paper reports strong efficiency gains — using ~1% of the training data of baselines — while achieving competitive or better FVD on MSR-VTT and UCF-101.

## Strengths

- **Substantial reduction in training cost with competitive quality**: ETC is trained on 0.1M WebVid videos + image datasets (ImageNet, JDB) for only 15K iterations on 8×3090 GPUs, yet achieves FVD and user-preference results competitive with models trained on orders of magnitude more video data (WebVid-10M, LAION-5B). This data-efficiency claim is the paper's most concrete finding.

- **Clean architecture with validated components**: Ablation (Table 2) shows that the Spatial-Temporal Mixed Embedding (ME) reduces incorrect boundary segmentation from 17% to 0%, and that Triple-Data Training (TDT) improves CLIP score by 0.04. These are measured, non-obvious contributions that would benefit practitioners.

- **Faster inference**: With only 0.9B parameters (no temporal attention layers), ETC achieves 1.92 FPS inference — roughly 3× faster than LVDM (0.65 FPS). This is a practical advantage.

- **Demonstrated generalization**: The paper shows qualitative results for higher resolution (512×320) and longer videos (256 frames) after minimal fine-tuning, suggesting the Mixed Embedding transfers reasonably well.

## Weaknesses

### Fatal
None. The paper's core empirical contribution (a spatial-only T2V model trained efficiently) is not invalidated by the weaknesses below, though several are serious.

### Major

- **Unsound theoretical argument for the core claim**: Section 3 claims to "mathematically prove" that spatial attention can substitute for temporal attention because both produce "linear mappings." The equations shown — χₛ(x) = [x₁·Wₛ, x₂·Wₛ, …] and χₛₜ(x) = Σ Wₛᵀ·xᵢ·W_Tᵢ — do not describe actual self-attention, which involves a **nonlinear softmax** over similarity scores. These look like simplified linear projections, not attention. The paper defers to the appendix (Section B.2), but the main-text presentation is misleading. Because the paper lists "theoretical and experimental exploration" as contribution #1 and motivates the entire method with this argument, the weakness undermines a claimed contribution. The paper would be stronger by scoping this as an empirical observation rather than a proof.

- **Confounded key observation (Figure 2)**: The experiment compares W/O-TA (fine-tuning all pre-trained SD2.1 weights) with W-TA ("learns temporal information from scratch with new additional temporal attention"). This is **not a controlled comparison**: W/O-TA starts with a strong pretrained initialization across all parameters, while W-TA has randomly initialized temporal layers that must be learned. The observed faster convergence of W/O-TA could be entirely due to better initialization and fewer trainable parameters, not to any inherent superiority of spatial attention for temporal modeling. A fair setup would initialize the additional temporal attention from the corresponding spatial attention weights (or train it jointly from the same starting point). The paper's conclusion that "spatial attention itself has a strong potential for temporal modeling" is not reliably supported by this evidence.

- **Headline quality comparisons are not controlled**: The paper claims a "49% FVD improvement using only 1% training data," but the baselines (LVDM, VideoCrafter, VideoCrafter2, ModelScope) are trained on full-scale datasets (WebVid-10M, LAION-5B) while ETC uses a filtered 0.1M subset of WebVid plus image data. There is no experiment where a strong baseline is re-trained on the same small dataset. The FVD gap could partly reflect dataset quality differences or the baselines being evaluated outside their training distribution, not ETC's architectural advantage. The paper's quality claim would be more rigorous if it included a controlled experiment or clearly separated "better quality" from "better data efficiency" claims.

### Minor

- **No variance/confidence intervals for FVD or CLIP scores**: The paper reports point estimates without standard deviations or confidence intervals. Given that FVD can be sensitive to sample size and random seeds, this is a transparency issue (though common in the field).

- **The "4% training samples" claim partially ignores additional image data**: The training sample count (steps × batch size) accounts only for video training iterations. ETC also uses ImageNet and JDB image datasets in Triple-Data Training, so the claimed efficiency metric is incomplete.

- **The paper's own conclusion undercuts a claimed advantage**: Section 6 states "unlike autoregressive models, we do not support changes in resolution and frame rate without additional training." This contradicts the earlier claim that the Mixed Embedding "could support generation at any resolution or frame rate." The paper should reconcile this.

- **Selective quantitative evaluation for generalization**: High-resolution and long-video experiments (Figure 6) are shown only qualitatively, without FVD, CLIP scores, or comparison to baselines at those settings.

### Trivial
- The Mixed Embedding formula omits the standard Θ=10000 scaling factor convention (common in positional encoding).
- The video filter threshold α is not specified, slightly hindering exact reproducibility.

## Nice-to-Haves
- **Controlled comparison for Figure 2**: Reproduce with both models starting from the same T2I pretrained checkpoint, initializing temporal attention weights from the corresponding spatial attention.
- **Controlled baseline re-training**: Train VideoCrafter2 (or another open-source baseline) on the same 0.1M WebVid subset to directly measure relative benefit under equal data conditions.
- **Failure case analysis**: Systematic study of when the stitched-grid approach fails (e.g., large motion, complex temporal dynamics).
- **Comparison to zero-shot methods**: Since ETC also lacks temporal modules, direct comparison with Text2Video-Zero, Free-Bloom, etc. on FVD/CLIP would better position the contribution.
- **Separate ablation of TDT subcomponents**: The current ablation is ME vs. TDT as monolithic modules. Ablating the FPS embedding, video filter, and each data type separately would strengthen the analysis.

## Removed Points
*These points are flagged to be removed, treat them with caution*
- Critic's claim that LVDM's FVD of 489 is "far above what the community reports" and that VideoCrafter2's 374 "seems unusually low." These numbers come from the paper's cited evaluations; I cannot verify them independently, and questioning the reported numbers for cited works risks overreach.
- Critic's complaint about Θ being undefined in the positional encoding formula. This is a minor notational convention, not a substantive flaw.
- Strength Finder's claim that "theoretical demonstration" is a core strength. Since the theoretical argument is verified as flawed, this strength conflicts with a verified weakness and is dropped per the priority rule.

## Novel Insights

A genuinely novel observation emerging from reading the paper and reviews together: the paper's most interesting finding (that competitive T2V is possible by simply fine-tuning a T2I model with stitched frames and positional cues) is actually **orthogonal to the theoretical justification**. The method's efficiency stems from a straightforward insight: if you can avoid training temporal layers from scratch, you save dramatically on data and compute. The Mixed Embedding is the key enabler (reducing boundary errors from 17% to 0%). This suggests that the community may have been over-engineering temporal modules when a much simpler approach — combined with careful positional encoding — could achieve surprisingly good results. The paper's real contribution is this empirical demonstration of simplicity, not the flawed linearity argument.

## Suggestions

1. **Drop or fundamentally revise the "theoretical" argument in Section 3.** The current claim about "linear mappings" is incorrect and undermines reader trust. Replace it with a clear empirical motivation: show that T2I models already encode weak temporal priors (e.g., via latent consistency), and that stitching frames + mixed embeddings can unlock them. Or simply characterize the approach as an empirical finding.

2. **Add a controlled experiment for Figure 2** where both W-TA and W/O-TA are initialized from the same SD2.1 checkpoint, and the temporal attention layers of W-TA are initialized from the spatial attention weights (e.g., copied). This would isolate the effect of architecture from the effect of initialization.

3. **Retrain at least one strong baseline (e.g., VideoCrafter2) on the same 0.1M WebVid subset** used by ETC and report FVD/CLIP. This would make the quality comparison apples-to-apples and either strengthen or qualify the headline claims.

4. **Separate "quality" from "efficiency" claims more clearly.** The current framing ("49% FVD improvement with 1% data") conflates both. State transparently: "ETC achieves competitive FVD despite using 1% of the training data" vs. "ETC improves over baselines trained on comparable data" (if the controlled experiment bears it out).

5. **Report FVD/CLIP with confidence intervals** (e.g., bootstrapping over generated samples) and specify the number of generated videos used for evaluation.

## Score and Decision

The paper addresses a timely and practical question (can we avoid training expensive temporal modules?). The architectural design (stitching + Mixed Embedding + Triple-Data Training) is clean and validated by ablation. The efficiency numbers are striking. However, the paper overclaims in two ways that significantly weaken it: (a) it presents a flawed "theoretical proof" as a core contribution, and (b) the headline quality comparison (49% FVD improvement) is not properly controlled — baselines are trained on much larger datasets. The core experimental finding (that a spatial-only model can produce competitive results with minimal data) remains interesting and worth communicating, but the paper needs to fix the theoretical argument and add controlled experiments to substantiate its strongest claims. 

MY FINAL SCORE: <pineapple>5.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>