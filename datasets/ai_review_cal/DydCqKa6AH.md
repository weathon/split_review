- Decision: Accept
- Avg Score: 6.75
- Scores: 8, 6, 5, 8
Now I have a thorough understanding of the paper and all the reviewer claims. Let me synthesize the final review.

## Summary

This paper introduces a new task—context-aware pedestrian movement generation from web videos with noisy labels—along with the CityWalkers dataset (30.8 hours, 120K+ pedestrians, 227 cities) and the PedGen diffusion model. PedGen handles noisy pseudo-labels via iterative reconstruction-based filtering and a learnable mask embedding for partial labels, and incorporates scene context (lifted from 2D to 3D voxels), body shape, and goal destinations as conditioning. Experiments on CityWalkers, Waymo, and CARLA show PedGen outperforms adapted baselines.

## Strengths

- **Large-scale diverse pedestrian movement dataset (CityWalkers).** The paper constructs a dataset with 30.8 hours of video, 120,914 pedestrians, 16,215 scenes across 227 cities and 49 countries. Ablation in Table 4 shows training on CityWalkers dramatically outperforms training on the prior outdoor dataset SLOPER4D (e.g., 3.82 vs. 1.85 mADE with all context factors), directly supporting the claim that scale and diversity from web videos are critical.

- **Automatic iterative label filtering for pseudo-label noise.** The reconstruction-based anomaly detection uses a context-free PedGen model to identify and remove low-quality labels, yielding a measurable 2.9% improvement in aADE (Table 3). This directly addresses the paper's core challenge of learning from noisy web-video labels.

- **Training with partial labels via a learnable motion mask embedding.** By replacing missing frames with a mask embedding and computing loss only on available frames, the model leverages incomplete tracks common in web videos. Table 3 shows this improves aADE by 5.8% over using only complete labels.

- **3D context encoder that lifts 2D scene labels into a local voxel representation.** The encoder unprojects depth and semantic maps, extracts a 3D local point cloud, and voxelizes it with semantic voting. Ablation in Table 4 shows that replacing this with 2D DINOv2 features ("-3D rep.") degrades performance, and removing semantic labels also hurts, demonstrating the value of the proposed encoding over prior 2D-only scene conditioning.

- **Zero-shot generalization to out-of-distribution environments.** PedGen achieves the best performance on Waymo (real-world, human-annotated) and CARLA (simulated) test sets without any fine-tuning (Table 1), showing that learning from diverse web videos with the proposed model transfers to novel environments.

## Weaknesses

### Fatal
None.

### Major

- **Main evaluation relies on a noisy validation set, and external corroboration is underpowered.** The CityWalkers validation set uses the same pseudo-labeling pipeline as training. The paper candidly acknowledges this (Section 3: "label noise from web videos is still inevitable"), but the principal quantitative results (Table 1 on CityWalkers) measure performance against noisy labels. The Waymo evaluation mitigates this with human-annotated data, but comprises only **80 test samples** (line 148). With 50 generated trajectories per sample, there is substantial room for variance, and no confidence intervals or statistical tests are reported. The CARLA set (262 samples) is synthetic. The paper's central claim—that PedGen produces more *realistic* pedestrian motion—would be substantially strengthened by a clean, manually verified test subset from the web video domain.

- **Baseline adaptation is underspecified.** The paper states it made "minimum adjustments" to adapt MDM, HumanMac, and TRUMANS (lines 157–160) but does not detail how each baseline received the three conditioning signals (scene context, body shape, goal). For example, MDM was designed for text/action conditioning; whether the scene+shape+goal were flattened into a single embedding, input as separate tokens, or handled via architectural modifications is not described. HumanMac's adaptation is not described at all beyond its original use of history motion. Without this information, it is difficult to assess whether the reported gaps (e.g., aADE 4.08 vs. 5.37 on CityWalkers without goal) reflect method superiority or uneven adaptation quality.

### Minor

- **Anomaly filtering threshold and iteration count not reported.** The label-filtering method (Section 4) removes samples with reconstruction error "greater than a certain threshold" but the threshold value is never given. The number of iterative filtering rounds is also unspecified. This limits reproducibility of a claimed 2.9% aADE improvement.

- **Waymo evaluation lacks uncertainty quantification.** The zero-shot results on Waymo (80 test samples) are a key evidence point for real-world generalization, but no confidence intervals, bootstrapped estimates, or variance across runs are reported. Given the small sample size, this omission is notable.

- **Monocular depth estimation errors not discussed.** The context encoder lifts 2D depth (ZoeDepth) and semantics into a 3D voxel representation, but the paper does not discuss how errors in monocular depth estimation propagate into the voxel condition or how the model copes with these inaccuracies. The ablation against 2D DINOv2 features is helpful but does not isolate depth quality as a variable.

### Trivial
None.

## Nice-to-Haves

- A controlled comparison of the iterative diffusion-based filtering against simpler alternatives (e.g., thresholding on keypoint confidence, detection bounding-box stability, or WHAM reconstruction error without retraining) would help isolate the value of the proposed approach.
- A human evaluation study (e.g., "which generated motion looks more natural?") would complement displacement-error metrics, especially given the noisy validation set.
- Additional architecture details (number of transformer layers, hidden dimensions, diffusion steps K, learning rate) in the main text would aid reproducibility.

## Removed Points

These points were flagged in the reviews but are removed or demoted as follows:

- **"Iterative label-filtering may introduce selection bias by removing rare but valid movements"** (Harsh Critic point 3, part 1). This is speculation about what *might* be removed, not a verified flaw. The paper's ablation shows the filtering improves metrics, and without evidence that legitimate data was disproportionately removed, this is not a concrete weakness. (Moved to Removed.)

- **"Inter-rater reliability statistics for manual cleaning not provided" / "how many videos were manually reviewed"** (Harsh Critic, Section 3 notes). These are excessively granular requests for a dataset paper at this scale; manual cleaning is described as a supplementary quality check, not a core annotation process. (Moved to Removed.)

- **"No user study"** (Harsh Critic, Missing Parts). While valuable, human evaluation of motion realism is not standard practice for displacement-error-based motion prediction papers in this community. (Moved to Nice-to-Haves.)

- **"The paper should report sensitivity to the anomaly-filtering threshold and mask embedding initialization"** (Harsh Critic, Strengthening section). This is a reasonable suggestion for future work but not a current weakness, as the method works as-is. (Moved to Nice-to-Haves.)

- **"Missing hyperparameters"** claim in the Harsh Critic's Missing Parts section is partially addressed by the code release promise. The specific parameters (layers, dimensions, K) are common in code releases for this subfield. (Moved to Nice-to-Haves with reduced prominence.)

- Some generic strengths from the Strength Finder were reviewed; all listed strengths are concrete and evidence-backed, so none were removed.

**Note on score calibration:** No weakness here is fatal. The validation noise concern is real but transparently acknowledged and partially mitigated by Waymo/CARLA evaluations. The baseline adaptation concern is real but typical for new tasks where no off-the-shelf method exists. These are addressable weaknesses in a paper that otherwise makes a clear contribution (new task, large dataset, well-designed model with thorough ablations).

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. **Add a clean test subset.** Manually verify 200–300 samples from CityWalkers to create a clean evaluation set, or at minimum report results on a held-out subset with higher-confidence labels. This would directly address the main evaluation concern.

2. **Detail baseline adaptations.** For each baseline (MDM, HumanMac, TRUMANS), specify exactly how scene context, body shape, and goal were encoded as input. If this information is extensive, provide it in supplementary material.

3. **Report confidence intervals on Waymo results.** Bootstrapped 95% CIs on the 80-sample Waymo evaluation would quantify the uncertainty readers should attach to these zero-shot results.

4. **Report the anomaly filtering threshold** and number of iterative rounds in the paper text or supplement.

5. **Discuss depth estimation errors.** Even a brief paragraph acknowledging the limitations of monocular depth (ZoeDepth) and their potential impact on the voxel representation would strengthen the method section.
