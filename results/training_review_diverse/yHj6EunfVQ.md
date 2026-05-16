Now I have all the information I need to produce the consolidated review.

## Summary

CoSPaL presents a weakly-supervised spatio-temporal video grounding (WSTVG) approach built on the Grounding DINO foundation model. It introduces three components — Tubelet Phrase Grounding (TPG) for joint spatial-temporal alignment, Contextual Referral Grounding (CRG) for query decomposition via GPT-3.5, and Self-Paced Scene Understanding (SPS) for curriculum learning over scene complexity. The method achieves state-of-the-art results on VidSTG and HCSTVG-v1/v2 with substantial margins (e.g., +7.9% m_vIoU on HCSTVG-v1 over WINNER), while using significantly fewer computational resources than fully-supervised alternatives.

## Strengths

1. **First effective adaptation of a foundation model to weakly-supervised spatio-temporal video grounding, with strong empirical evidence.** The paper identifies three concrete failure modes of a naive G-DINO video adaptation (temporal inconsistency, imbalanced query attention, dense-scene confusion) and shows that CoSPaL systematically overcomes them. The ablation in Table 5 demonstrates a 10.8% m_vIoU gain over the W-GDINO baseline on VidSTG declarative (14.3→25.1), with each component contributing measurable, non-overlapping gains.

2. **State-of-the-art results with large and consistent margins across multiple benchmarks.** CoSPaL surpasses the prior weakly-supervised SOTA (WINNER) by 7.9% m_vIoU on HCSTVG-v1 and 4.4%/3.3% m_vIoU on VidSTG declarative/interrogative splits (Tables 2–3). The gains are consistent across higher IoU thresholds (vIoU@0.3 and 0.5), indicating robust spatio-temporal localization rather than narrowly optimized metrics.

3. **Computational efficiency that is a genuine practical advantage.** CoSPaL uses a single GPU with a frozen detection backbone, versus 8–32 GPUs for fully-supervised methods (Figure 5). Training requires 2.5–6.5× less GPU memory per device and 2–4× less total training time. This makes the approach accessible to resource-constrained settings, which is a meaningful contribution beyond raw accuracy.

4. **Systematic ablation study that isolates each component's contribution.** Tables 4–5 disentangle the effects of spatial grounding, temporal grounding, TSA, CRG, and SPS, and study them both individually and in combination. Table 6 provides a fair backbone-controlled comparison (WINNER re-implemented with Faster R-CNN). This gives readers a clear picture of what each piece contributes.

## Weaknesses

### Fatal
None.

### Major
None. The issues below are genuine but addressable; none invalidate the paper's core claims or SOTA results.

### Minor

1. **SPS ablation lacks a controlled non-curriculum baseline.** The SPS evaluation in Tables 4–5 progressively increases the tubelet upper bound (4→7→all). However, there is no control trained from scratch with *all* tubelets for the *same total number of training iterations* without a curriculum. The observed gains from progressive stages could therefore be partially attributable to increased total training time or to early-stage data filtering, rather than to the curriculum itself. The paper claims SPS as a core contribution (contribution 3), so isolating the curriculum effect is important. While Table 5 shows SPS helps consistently across TPG, CRG, and TPG+CRG — which provides some evidence — the missing controlled comparison means the exact mechanism of improvement is not fully pinned down. This is fixable in a revision.

2. **Training schedule for SPS is under-specified.** The paper states (line 150): "The model is trained for 10 epochs with 5 iterations over the dataset through each sub-phrases." This phrasing is ambiguous — it is unclear whether each sub-stage receives 10 epochs, 5 passes, or some other allocation. It is also unclear how videos are filtered in each stage: does Stage 1 include *only* videos with ≤4 tubelets, or does it include all videos but clamp the tubelet count to 4? The paper references supplementary materials for hyperparameter details (which the parser strips), but the main text should provide enough clarity for basic reproducibility.

3. **GPT-3.5-based query decomposition is unanalyzed.** The CRG module uses GPT-3.5 to decompose queries into sub-parts (Q_ol, Q_og). The paper only says "We use GPT-3.5 to extract quantifier and phrases" (line 139) with no prompt details, no success-rate analysis, and no ablation comparing against a deterministic heuristic (e.g., POS-based extraction) or manual decomposition on a sample. Since GPT-3.5 calls are non-deterministic and not transparent, readers cannot gauge the reliability of this component or reproduce the exact decompositions. This weakens the evidence that CRG's 1–2% gains come from the decomposition itself rather than from some other aspect of the module.

4. **Negative sampling strategy for the spatial contrastive loss is underspecified.** Line 90 states negative tubelets are picked "within the batch," while Equation 2 sums over \(k' \neq k\) (other tubelets in the *same* video). The relationship between intra-video and cross-video negatives is unclear, which matters for the contrastive objective's behavior. Separately, the POS masking description ("mask out noun/adjectives/verb," line 98) uses a slash that makes it ambiguous whether nouns, adjectives, verbs, or all three are masked.

5. **No variance reporting.** The main results (Tables 2–3) and ablations (Tables 4–5) report point estimates without standard deviations or multiple-seed runs. Given that several gains are in the 1–3% range (e.g., SPS adds 1.1% m_vIoU on top of TPG+CRG), some measure of variance would help assess significance.

### Trivial
- The paper does not discuss failure cases or limitations (e.g., tracker failures, scenes with very similar subjects, incorrect GPT-3.5 decompositions). A brief limitations paragraph would strengthen the paper.

## Nice-to-Haves
- A hyperparameter sensitivity analysis for the key SPS thresholds (4, 7 tubelets), the detector confidence threshold (0.4), and the number of sampled frames (32).
- The specific GPT-3.5 prompt used for query decomposition, either in the main text or supplementary.
- An ablation comparing intra-video negatives only, cross-video negatives only, and both for the spatial contrastive loss.

## Removed Points

These points are flagged as problematic per the review guidelines; treat them with caution:

- *"The claim that CoSPaL is 'the first to solve weakly supervised spatio-temporal video grounding based on a foundation model' should be softened"* — This is a defensible, specific claim. The paper qualifies it with "based on a foundation model," and no contradictory evidence was presented. Removed as a nitpick on a defensible phrasing.

- *"No other contemporary weakly supervised method is re-run with the same detection backbone"* — Table 6 explicitly compares WINNER using the same Faster R-CNN backbone, partially addressing this. The main tables report results from original papers (standard practice), and re-running every baseline with G-DINO is a large engineering effort beyond practical expectations. Removed per the rule that favors the author when asymmetry benefits the baseline.

- *"The paper should clarify the backbone used by each baseline or note that results are taken from original papers"* — This is standard practice in the field, and the paper states the comparison context. No evidence that the paper misrepresents baselines.

## Novel Insights

The most useful novel observation from the review synthesis is that the SPS component's claimed mechanism (curriculum learning via progressive tubelet counts) cannot be fully separated from the confound of increased training time with the current ablation design. This is not fatal to the paper — the overall CoSPaL pipeline delivers SOTA results regardless — but it means the paper's story about *why* SPS helps is weaker than the other two components. A controlled experiment (all tubelets from scratch for same total iterations) would cleanly resolve this. Additionally, the GPT-3.5 reliance in CRG raises a reproducibility concern that is increasingly common in vision-language work and deserves more systematic treatment than the single sentence currently provided.

## Suggestions

1. Add a controlled SPS baseline: train TPG+CRG with all tubelets from the start for the same total number of iterations as the 3-stage progressive schedule, and compare. This cleanly isolates the curriculum effect.
2. Clarify the training schedule: specify exactly how many epochs/iterations each SPS sub-stage receives, and whether videos with fewer tubelets than the upper bound are exclusively used or all videos are used with clamped counts.
3. Provide the GPT-3.5 prompt (in supplementary) and a small-scale quality analysis (e.g., human rating of 50–100 decompositions) to establish that the decomposition is reliable.
4. Clarify the negative sampling: state explicitly whether negatives in Eq. 2 are intra-video, cross-video, or both, and describe how batch-level negatives are selected.
5. Report standard deviations over at least 3 seeds for the main results (Tables 2–3) to establish statistical significance of the reported margins.
6. Add a brief limitations paragraph discussing known failure cases and when the approach struggles.

## Score and Decision

The paper presents a well-motivated, empirically strong contribution to WSTVG. The three-component framework is clearly designed to address identified failure modes, the SOTA results are substantial and consistent, and the computational efficiency advantage is practically meaningful. The weaknesses identified are genuine but addressable in a revision — none undermine the core claims or the validity of the main results. The paper would benefit from stronger experimental controls and better specification, but in its current form it already makes a clear contribution.

MY FINAL SCORE: <pineapple>7.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>