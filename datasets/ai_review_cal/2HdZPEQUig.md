- Decision: Reject
- Avg Score: 3.00
- Scores: 1, 3, 5, 3
Now I have all the information needed. Let me produce the final consolidated review.

---

## Summary

Interpreter introduces a hierarchical slot attention architecture for unsupervised video object segmentation. The first level compresses image features into image-level slots via reconstruction; the second level compresses these frame-level slots across a full video into video-level slots using a Sinkhorn divergence loss (handling the unordered nature of slot sets). Attention maps are propagated between the two levels to derive per-frame segmentation masks. The method processes entire YTVIS-19 videos (up to 36 frames) in one pass without chunking, and achieves 54.2 mIoU on YTVIS-19 (+4.1 over the prior best method, BA), while struggling on the synthetic MOVi-E dataset (-11 mIoU relative to baselines).

---

## Strengths

1. **Novel hierarchical architecture that avoids full-frame feature-map reconstruction at the video level.** The two-level design (image-level slot autoencoder → video-level slot set-reconstruction) is a principled way to extend object-centric learning to longer videos without the expensive pixel/feature-map reconstruction that forces prior work (SOLV, BA) to use short windows (T=3–5) and post-hoc matching. The paper demonstrates that this enables processing of full 36-frame YTVIS-19 videos without chunking (Sec. 3.1, Fig. 1).

2. **Sinkhorn divergence as a principled loss for unordered slot sets.** Because image-level slots form an unordered set, standard structured losses cannot be applied. The paper formulates video-level reconstruction using Sinkhorn divergence (Eq. 2, Sec. 3.1), an entropy-regularized optimal transport distance that is permutation-invariant and differentiable. This is a technically sound solution to a nontrivial problem that prior work in this line has not addressed.

3. **State-of-the-art segmentation mIoU on YTVIS-19.** The method achieves 54.2 mIoU on a 300-video holdout set, outperforming BA (50.1) and SOLV (45.3) by clear margins (Table 1). This is reported as the mean over 3 random seeds. The +4.1 mIoU improvement over the previous best is a genuine empirical result that supports the value of the proposed approach.

4. **Attention propagation mechanism is clean and well-designed.** The composition of image-level attention maps with the decomposed video-level attention map (Sec. 3.2) provides a direct, parameter-free way to map image features to video-level slots for segmentation, requiring no additional decoding stage.

---

## Weaknesses

### Fatal
None.

### Major

1. **The "efficient" and "scaling" claims are asserted without supporting evidence.** The paper's title and motivation are built on efficiency and scaling to longer videos without chunking. Yet there are zero measurements of wall-clock runtime, GPU memory, or throughput. The longest video evaluated is 36 frames (YTVIS-19) and 24 frames (MOVi-E). While the paper does *demonstrate* processing full videos without chunking (which prior work at T=3–5 could not), it never quantifies whether this is *faster* or *more memory-efficient* than chunked alternatives on matched video lengths, nor does it test on videos longer than 36 frames. The efficiency claim therefore remains a structural intuition rather than a verified result. This is the paper's most significant evidential gap.

2. **No ablation of the method's core technical components.** The ablations (Table 3) vary only the number of image-level slots and the clustering distance threshold. There is no isolation of: (a) Sinkhorn divergence vs. a simpler set-matching loss (e.g., Hungarian with L2), (b) the hierarchical two-level design vs. a flat approach (e.g., training video-level slots directly on frame features without the image-level autoencoder), or (c) the attention propagation mechanism. Without these ablations, performance gains cannot be cleanly attributed to the proposed technical ingredients vs. the strong backbone (DINOv2 ViT-B/14), longer temporal context, or hyperparameter tuning.

### Minor

3. **Standard deviations are not reported.** The paper reports means over 3 random seeds for Tables 1–3 but does not provide variance or error bars. Given the well-known training instability of slot-attention methods, the reader cannot assess whether the reported improvement margins are statistically reliable.

4. **MOVi-E failure analysis is qualitative only.** The method underperforms all baselines by -11 mIoU on MOVi-E. The explanation (the model "breaks up movement trajectories," re-assigning slots when objects change motion state) is supported solely by qualitative examples in Figure 4. No quantitative analysis (e.g., slot re-assignment frequency, comparison of trajectory consistency across methods) is provided, making it hard to evaluate whether this is a fundamental limitation or a solvable issue.

5. **The cost function for Sinkhorn divergence is not specified.** The paper provides the blur value (0.05) and scaling (0.5) but does not state what ground distance is used in the cost matrix (cosine, Euclidean, or other). Geomloss (the implementation used) defaults to squared Euclidean, but this should be stated explicitly for reproducibility.

6. **Low per-frame FG-ARI on YTVIS-19 is acknowledged but not deeply analyzed.** The method achieves 28.5 FG-ARI vs. 38.5 for BA. The paper's explanation (slot attention "aura" artifacts) is plausible and supported by noting that other slot-attention methods also cluster in the same low range (SMTC: 31.4, SOLV: 29.1). However, no quantitative evidence (e.g., decoder output visualizations, per-video mIoU/FG-ARI correlation) is provided to verify the "aura" hypothesis or to explore whether the mIoU gain comes at the cost of per-frame segmentation quality.

7. **Unquantified failure modes.** The paper identifies "spurious clustering of similar entities" as a common failure mode (Fig. 3) but does not measure its frequency or its impact on the reported aggregate metrics.

### Trivial
None.

---

## Nice-to-Haves

- A direct comparison of wall-clock time and GPU memory against a chunked variant of the same method would turn the efficiency claim from unsupported to validated.
- An ablation replacing Sinkhorn divergence with Hungarian matching + L2 loss would be the strongest evidence that the optimal transport formulation matters.
- Testing on videos longer than 36 frames (e.g., on a dataset like DAVIS with longer clips, or by stitching YTVIS clips) would strengthen the scaling claim.
- Reporting backbone sizes for all baselines would clarify fairness of comparison.

---

## Removed Points

- **"FG-ARI measures temporal consistency"** — REMOVED because it is factually wrong. The paper explicitly defines FG-ARI as "mean per-frame Foreground Adjusted Rand-Index" (line 67), a per-frame metric, not a temporal consistency metric. The critic's claim that low FG-ARI indicates identity-switching across frames is based on a misunderstanding of what FG-ARI measures.

- **Missing related works on optimal transport for object-centric learning (Driess et al., Goyal et al.)** — REMOVED per instructions: I cannot verify the existence or relevance of these citations without external sources, and these points reflect reviewer knowledge gaps, not author errors.

- **"The paper does not discuss efficiency of processing longer videos"** — PARTIALLY REMOVED (the core point about missing efficiency metrics is retained as Major weakness #1; the claim that videos "are quite short" in absolute terms is removed because 36 frames is the full dataset length and is longer than prior work's chunked windows of 3–5 frames).

- **Sinkhorn divergence "blur value not stated"** — REMOVED because the paper *does* state it: "blur value of 0.05" (line 69). The critic missed this.

- **"Training/evaluation protocol is unusual" (train on combined splits)** — REMOVED because the paper states this follows prior work (Aydemir et al., 2023; Ding et al., 2024) and explains the protocol explicitly (line 65). This is standard practice for this benchmark setup.

- **"Video padding by repetition could introduce artifacts"** — REMOVED as speculative; the paper notes this was tried and found not to adversely affect results (line 141: "extending the sequence through repetition to be an easier solution that does not adversely affect results").

- **"Missing appendix/supplementary material"** — REMOVED per instructions: the parser strips these; they exist in the original submission.

---

## Novel Insights

The harsh critic and strength finder both identify the same fundamental tension: Interpreter achieves a convincing SOTA mIoU on realistic video (YTVIS-19) but struggles on synthetic MOVi-E, and the paper's main architectural novelty (avoiding chunking via hierarchical set reconstruction) is simultaneously its strongest selling point and its weakest evidence (because no efficiency metrics are provided). The reviews collectively reveal that the paper is best understood as an *architecture contribution* — demonstrating that hierarchical slot attention with Sinkhorn-based set reconstruction can work for video segmentation — rather than an *efficiency contribution*. The efficiency framing in the title and abstract overpromises relative to what is actually measured. A useful insight from the tension between the two reviews is that the method's weakness on MOVi-E (slot re-assignment across motion changes) and its low FG-ARI on YTVIS-19 may both stem from the same root cause: the Sinkhorn reconstruction objective, by treating each set of slots as a distribution, may naturally group slots by feature similarity rather than by object identity across temporal state changes. This is an interesting failure mode that deserves quantitative characterization in future work.

---

## Suggestions

1. **Rebalance the paper's framing.** The central claim should be the novel hierarchical architecture and SOTA mIoU, not unsupported efficiency claims. Consider changing the title to something like "Hierarchical Slot Attention with Set-Level Reconstruction for Video Object Segmentation" and adding a concrete efficiency/throughput comparison to substantiate the "efficient" claim or removing the claim entirely.

2. **Add one key ablation.** Replacing Sinkhorn divergence with Hungarian matching + L2 loss (while keeping everything else identical) would be the single most informative experiment for the reviewer community. It would directly test whether the optimal transport machinery is necessary.

3. **Report standard deviations.** Three runs with mean and std is minimal; given the known variance of slot attention, this is essential for the reader to trust the SOTA claim.

4. **Quantify the MOVi-E failure mode.** Report the frequency of slot re-assignment across motion-state changes, or compute a trajectory-consistency metric (e.g., measuring how often the same video-level slot maps to the same ground-truth object before vs. after a motion change).

5. **Specify the Sinkhorn ground cost explicitly** in the methodology section.

---
