Now I have a thorough understanding of the paper. Let me produce the consolidated review.

---

## Summary

VOVTrack tackles open-vocabulary multi-object tracking (OVMOT) from a video-centric perspective, adding two key innovations over the prior image-level OVTrack baseline: (1) a **tracking-state-aware prompt-guided attention** mechanism that weights detection candidates by estimated quality (occlusion, blur, etc.) during classification training, and (2) a **self-supervised object similarity learning** strategy that leverages raw unlabeled video (534.1K frames from TAO) through intra/inter-consistency and category-consistency losses to train the association head. The method achieves state-of-the-art TETA scores on TAO validation (38.1 base, 34.4 novel) and test (37.0 base, 29.4 novel), outperforming prior OV methods including those using additional CC3M training data.

## Strengths

1. **State-of-the-art performance on the OVMOT benchmark.** Table 1 shows VOVTrack achieving the highest TETA, LocA, and AssocA on both base and novel classes of the TAO validation and test sets, surpassing all prior methods including QDTrack, TETer, and the direct baseline OVTrack (+2.6 base TETA, +6.6 novel TETA on validation). Notably, it outperforms OVTrack+RegionCLIP (which uses an additional 3M CC3M images) on most metrics, demonstrating both effectiveness and data efficiency.

2. **Self-supervised learning from raw video is clearly effective.** The ablation (Table 2, "w/o self-supervised learning" vs. full) shows removing self-supervision drops base TETA from 38.1→36.3 and novel TETA from 34.4→31.3, confirming that the proposed temporal consistency losses provide substantial gains beyond what static image-pair training alone can achieve. This is the first approach to use raw temporal video data for OVMOT training.

3. **Prompt-guided attention contributes meaningfully, with targeted ablations.** Removing prompt-guided attention (Table 2) drops novel TETA from 34.4→29.8, and removing just the piecewise weighting drops it further to 31.7, showing that both the attention mechanism and its thresholded weighting strategy are important. The qualitative visualization in Figure 3 provides supporting evidence that high-attention regions correspond to clear, unoccluded objects while low-attention regions are blurry or occluded.

4. **Comprehensive ablation study.** Table 2 systematically ablates each component (prompt attention, piecewise weighting, self-supervised learning, long-short sampling, category consistency, intra-consistency, inter-consistency), showing that every component contributes positively, especially for novel classes where the task is hardest.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

1. **Piecewise weighting thresholds ($d_\text{low}=0.3$, $d_\text{high}=0.6$) are given without sensitivity analysis.** These thresholds directly control how many candidates are filtered, downweighted, or boosted. A small change could affect training dynamics and final performance. No ablation varying these values is provided, so the reader cannot assess how robust the reported results are to this choice. While not fatal, this is a standard expectation for a central hyperparameter.

2. **The experimental design does not include an ablation that strips both prompt attention and self-supervision simultaneously to match OVTrack's protocol exactly.** The "w/o prompt-guided attention" ablation retains self-supervised learning, and the "w/o self-supervised learning" ablation retains prompt attention. Neither replicates OVTrack's training recipe (no prompt attention, no video self-supervision). Although the component-wise gains can still be inferred by comparing to OVTrack's published numbers, a direct ablation matching OVTrack's protocol would cleanly separate the sources of improvement and strengthen the central claim.

3. **The number of clusters $K$ in K-means for the category-consistency constraint is not reported.** The paper states "We use the clustering algorithm of K-means" (line 307) but does not specify how $K$ is chosen. Since this directly affects how object boxes are grouped into pseudo-categories for the $\mathcal{T}_c$ constraint, the missing detail makes it difficult to reproduce or assess the sensitivity of this component.

4. **Qualitative validation of prompt-guided attention (Figure 3) is only visual, not quantitative.** While Figure 3 does show that high-attention regions appear clear/unoccluded and low-attention regions appear blurry/occluded, this remains a selected-example demonstration. Correlating $w_r$ against ground-truth state annotations (e.g., TAO's per-object visibility flags) on a held-out set would provide stronger evidence that the mechanism genuinely captures tracking-relevant object states rather than acting as an uncalibrated heuristic.

### Trivial

- The qualitative comparison (Figure 4) shows only successful cases. Including failure cases would provide more balanced expectations.
- The necessity of using both symmetry ($\mathbf{E}_\text{pair}$) and cyclicity ($\mathbf{E}_\text{trip}$) objectives is not discussed or ablated individually; only the combined intra-consistency is ablated as a whole.

## Nice-to-Haves

- **Cluster purity analysis**: Computing adjusted Rand index or cluster purity against ground-truth categories (even if only for base classes) would demonstrate that the clustering-based category constraint operates on reasonable groupings, addressing the concern that novel-class classification features (ClsA ~4.5–6.0%) are noisy.
- **Ablation comparing video-only vs. static-pair-only training**: Training the association head separately on raw video alone (without the 6 epochs of static pairs) and on static pairs alone would isolate how much temporal consistency adds over the hallucination-based approach of OVTrack.
- **Failure case analysis**: A few representative failure cases would help set realistic expectations and identify remaining challenges.

## Removed Points

These points from the reviewers were found to be inaccurate or invalid upon verification against the paper:

- **"The prompt-guided attention mechanism lacks validation that it actually captures tracking-related object states / never demonstrates high $w_r$ corresponds to favorable state"** — The paper does provide qualitative validation in Figure 3 and the accompanying text (lines 426–428) showing that high-attention regions correspond to clear, unoccluded objects and low-attention regions to blurry/occluded ones. The remaining valid concern (lack of *quantitative* correlation with state labels) is retained as a Minor weakness above. The claim of *no* demonstration is factually incorrect and is removed.

- **"The paper does not clarify how many unlabeled TAO frames were used for self-supervised training"** — The paper states both the total (534.1K frames in the introduction, line 50) and that training uses "the TAO training dataset without annotation for 14 epochs" (line 313). The implication is clear that the full unlabeled TAO training set is used. This is not a genuine gap.

- **Missing-related-works-type suggestions** (not applicable as no specific missing works were identified by the reviewer that could be verified).

## Novel Insights

None beyond the paper's own contributions. The reviewer feedback largely reinforces and clarifies the paper's framing rather than revealing unexpected patterns. One interesting observation from the harsh critic is that category-consistency clustering helps novel classes *more* than base classes (ablation: novel TETA drops 34.4→32.2, base drops 38.1→37.1), despite novel-class classification features being very noisy (ClsA ~4.5–6.0%). This asymmetry suggests the clustering may capture coarse category groupings robust to feature noise — a point worth exploring in future work but not a novel insight per se.

## Suggestions

1. Add a sensitivity analysis for $d_\text{low}$ and $d_\text{high}$ (e.g., $\pm 0.1$ grid) to demonstrate robustness.
2. Add an ablation that removes both prompt-guided attention and self-supervised learning simultaneously, matching OVTrack's training protocol exactly. This would cleanly attribute the total gain over OVTrack to each component.
3. Report the number of clusters $K$ in K-means and describe how it is chosen.
4. Supplement the qualitative Figure 3 with a quantitative correlation between $w_r$ and ground-truth occlusion/visibility annotations from TAO, using a small held-out subset.
5. Include a few failure cases in the qualitative analysis.

## Score and Decision

This paper addresses an important and under-explored problem (OVMOT) and delivers clearly demonstrated improvements — the core contributions are validated through systematic ablations and achieve SOTA results. The weaknesses are minor and addressable: they concern missing hyperparameter sensitivity analysis, one experimental-design gap, and limited quantitative validation of one component. No weakness threatens the central claims of the paper. The paper is well above the acceptance threshold.

MY FINAL SCORE: <pineapple>7.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>