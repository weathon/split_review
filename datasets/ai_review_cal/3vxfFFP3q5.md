- Decision: Reject
- Avg Score: 5.60
- Scores: 5, 6, 6, 5, 6
Now I have a thorough understanding of the paper. Let me produce the final consolidated review.

## Summary

VOVTrack addresses open-vocabulary multi-object tracking (OVMOT) by introducing two video-centric innovations: (1) a prompt-guided attention mechanism that uses manually chosen adjective pairs (e.g., "unoccluded/occluded") to weight region proposals during detection training, and (2) a self-supervised association method that leverages unlabeled TAO video frames via cycle-consistency, spatial overlap, and category-consistency losses. Experiments on the TAO benchmark show substantial improvements over the prior SOTA OVTrack.

## Strengths

1. **Self-supervised association learning from raw video data—well-validated.** The paper proposes training the association head on 534K unlabeled TAO video frames using intra-consistency (pair-wise symmetry and triple-wise cyclicity) and inter-consistency (spatial overlap) losses. Ablation (Table 2) shows removing self-supervised learning drops novel TETA from 34.4 to 31.3, providing clear evidence that raw video data significantly boosts OVMOT performance without extra annotation. This is a timely and practical contribution.

2. **Tracking-state-aware prompt-guided attention shows clear empirical gains.** The ablation (Table 2) demonstrates that removing the prompt-guided attention mechanism reduces base TETA from 38.1 to 35.7 and novel TETA from 34.4 to 29.8—substantial drops that confirm the mechanism's practical importance, even if its precise operating mechanism warrants further analysis.

3. **State-of-the-art performance on TAO.** Table 1 shows VOVTrack achieves the highest TETA on both validation (38.1 base, 34.4 novel) and test (37.0 base, 29.4 novel) sets, outperforming all prior methods including OVTrack, QDTrack, and TETer. Notably, it exceeds methods that train on an additional 3M CC3M images on most metrics.

4. **Systematic ablation covering all components.** Table 2 independently ablates prompt-guided attention, piecewise weighting, self-supervised learning, short-long-interval sampling, category consistency, intra-consistency, and inter-consistency. This provides clear evidence for the marginal gain of each design choice.

5. **Long-short-interval sampling design is effective.** The ablation shows removing this sampling strategy reduces novel TETA from 34.4 to 33.1, demonstrating that diverse temporal intervals help learn robust association features.

## Weaknesses

### Fatal
None.

### Major

1. **The prompt-guided attention mechanism's claimed interpretation is insufficiently validated.** The paper's core interpretation is that CLIP-based text embeddings' similarity to state-prompt pairs (e.g., "unoccluded" vs. "occluded") reliably captures object tracking states (occlusion, blur, etc.), and that this *state-awareness* drives the improvements. However, the paper provides no controlled experiment to disentangle whether the specific *prompt content* matters, or whether any contrastive adjective pair—or a generic proposal-quality proxy (e.g., objectness score, IoU with ground truth)—would produce similar gains. The qualitative examples (Fig. 5) are anecdotal. The ablation "w/o piecewise weight strategy" still uses the prompt-based weights, just without thresholding. What is missing is an ablation that replaces the prompts with random projections or a simple non-prompt-based quality score. Without this, the claimed interpretation ("tracking-state-aware") is plausible but unsubstantiated; the mechanism could simply be a form of hard-example mining. This weakens one of the paper's two named contributions.

2. **The comparison with OVTrack is partially confounded by asymmetric data usage.** VOVTrack uses 534K unlabeled TAO video frames for self-supervised association training, while OVTrack uses no TAO data at all. The headline gains on novel TETA (34.4 vs. 27.8 on validation) are partially driven by this data advantage. The ablation "w/o self-supervised learning" (31.3 novel TETA) partially controls for this and still shows improvement over OVTrack (27.8), confirming the prompt-attention mechanism contributes independently. Nevertheless, the main comparison table does not make the data-use asymmetry sufficiently prominent, and the paper's claim of "same training dataset (annotations)" in the contributions, while technically qualified, could mislead a casual reader.

### Minor

1. **No sensitivity analysis for prompt pair selection.** The paper selects four specific adjective pairs ("complete/incomplete", "unoccluded/occluded", "unobscured/obscured", "recognizable/unrecognizable") and piecewise thresholds (0.3, 0.6) without any sensitivity analysis. It is unknown whether performance depends critically on these choices or generalizes across different prompt sets and threshold values.

2. **Category-consistency clustering not analyzed for quality.** The K-means clustering operates on classification features learned from *base classes only*, so its behavior for novel objects is unclear. The ablation (Table 2) confirms that removing category-consistency hurts performance (novel TETA drops from 34.4 to 32.2), but the paper provides no cluster-quality metrics (e.g., purity, NMI) or analysis of whether the clusters actually group objects of the same novel category together. This mechanism may work, but its inner workings remain opaque.

3. **Smaller relative improvement on test set ClsA not discussed.** On the test set, VOVTrack's novel-class ClsA (4.5) trails OVTrack+RegionCLIP (6.1), whereas on the validation set VOVTrack achieves 6.0 vs. OVTrack+RegionCLIP's 11.4 (though the latter uses additional CC3M data). The paper reports these numbers but does not discuss why the classification accuracy gap behaves differently on the test set versus validation set.

### Trivial
None.

## Nice-to-Haves

- **Validate prompt attention with a controlled experiment.** Replace the prompt-based weights with a generic quality proxy (e.g., RPN objectness score, or a binary oracle flag for "clean" vs. "degraded") and compare performance against the current prompt-based weights. This would reveal whether the state-prompts carry information *beyond* generic quality signals, and would substantially strengthen the paper's interpretive claims.
- **Analyze cluster purity for the K-means step** using the ground-truth categories available in TAO (even though not used during training). This would show whether the category-consistency constraint actually groups same-category objects together or is measuring something else.
- **Report computational cost** (training time, GPU-hours) since the method involves multiple training stages and the self-supervised loss computes pairwise and triplet similarities.

## Removed Points

*These points are flagged to be removed; treat them with caution.*

1. **"No variance or statistical significance reported"** — Single-run evaluation on these large-scale benchmarks is standard practice in the MOT/OVD community. This is a generic criticism that does not reflect a paper-specific weakness.

2. **"The ablation w/o category consistency still includes self-supervision, so it is not a clean ablation of the clustering's role"** — This misreads the paper. The ablation "w/o category consistency" *removes* the clustering while keeping all other self-supervised losses, which is exactly a clean ablation of the clustering's contribution.

3. **"Efficiency relative to data usage"** (Strength Finder point) — This strength conflicts with the verified weakness about asymmetric data comparison (VOVTrack uses unlabeled TAO data while baselines like DeepSORT+RegionCLIP use 3M CC3M images *in addition to TAO annotations*). Since the data-use comparison is not apples-to-apples, this claimed strength is removed per the rule that weaknesses win over conflicting strengths.

## Novel Insights

None beyond the paper's own contributions. The two reviews converge on the same central tension: the self-supervised association component is well-motivated and convincingly validated, while the prompt-guided attention mechanism shows clear empirical benefit but lacks the controlled experiments needed to substantiate its claimed interpretation as "tracking-state-aware." This asymmetry in validation strength between the two contributions is the review's most useful signal.

## Suggestions

1. **Add a controlled ablation for the prompt attention mechanism** where the state prompts are replaced by (a) random adjective pairs, (b) a generic objectness score from the RPN, to test whether the *specific prompt content* drives the improvement or whether any weighting-by-quality scheme would work.

2. **Make the data-use difference more transparent** by adding an explicit sentence in the comparison table caption or Section 4.2 stating that VOVTrack additionally uses unlabeled TAO video frames (534K) for self-supervised training, while OVTrack does not.

3. **Add sensitivity analysis** for prompt pair selection (vary the number of pairs, substitute different adjectives) and for the piecewise thresholds \(d_\text{low}, d_\text{high}\) to demonstrate robustness to these hyperparameter choices.

4. **Analyze the K-means clustering quality** by measuring cluster purity on the TAO validation set (where ground-truth categories are available), to confirm that the category-consistency constraint actually groups objects by meaningful category.
