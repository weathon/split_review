## Summary

This paper proposes AttenGeo, a method for cross-view object geo-localization that introduces two modules: CVCAM (Cross-view and Cross-attention Module) which performs iterative cross-attention between query and reference views to establish spatial correspondences, and MHSAM (Multi-head Spatial Attention Module) which uses conv-deconv pairs with varying kernel sizes to refine spatial features. The paper also introduces the G2D dataset for Ground→Drone localization. Experiments on CVOGL and G2D datasets show improvements over the prior DetGeo method.

## Strengths

- **Strong ablation evidence for both proposed modules.** Table 3 shows that adding CVCAM to a same-backbone baseline (simple feature summation) raises accu@0.5 by 9–11 points across all three tasks, and adding MHSAM on top provides a further 2–6 point gain. This is clean evidence that both modules contribute independently and cumulatively, using a controlled backbone.

- **MHSAM is shown to be portable across architectures.** Table 4 demonstrates that plugging MHSAM into DetGeo (without changing the backbone or any other component) improves accu@0.5 by +4–6 points across all three tasks. This controlled experiment isolates MHSAM's contribution and shows it works as a general-purpose refinement module.

- **Positive efficiency-accuracy trade-off.** Table 5 reports that AttenGeo uses fewer parameters (21.03M vs. 22.73M) and fewer GFLOPs (81.06 vs. 88.33) than DetGeo while achieving higher accuracy, which is a genuine practical advantage (though the backbone difference partially confounds this comparison).

- **Addresses a meaningful gap in task coverage.** The G2D dataset fills the missing "Ground→Drone" localization scenario, and establishing a benchmark where none existed is useful for the community, even if the dataset documentation is incomplete in the paper.

## Weaknesses

### Major

- **The comparison against DetGeo (the state-of-the-art baseline) is confounded by an uncontrolled backbone difference.** The paper uses ConvNeXt V2-Tiny (Section 4.2) as its backbone, while DetGeo uses a different architecture (not specified in the paper). The claimed gains over DetGeo in Tables 1 and 5 could partially or entirely stem from the stronger backbone rather than from CVCAM/MHSAM. The ablation study (Table 3) does not address this: it shows that CVCAM and MHSAM improve over a simple summation baseline *using the same backbone*, which validates the modules internally but does not establish that they are responsible for the gains over DetGeo. A controlled experiment comparing CVCAM against DetGeo's QACVFM with the same ConvNeXt V2-Tiny backbone is needed to support the paper's central claim of surpassing the state-of-the-art.

- **G2D dataset contribution is insufficiently documented.** Despite being listed as a contribution (points 3 in the introduction), the only description provided is the number of sample pairs and the train/val/test split (lines 177–178). There is no information about: data collection methodology (drone platform, flight altitudes, geographic coverage), what objects are annotated and how, annotation protocols or quality control, dataset statistics by object category or scene type, or resolution/viewpoint distributions. A dataset that is barely described cannot be assessed or used by the community.

- **Missing critical baselines for MHSAM.** The paper positions MHSAM as a novel spatial attention module but does not compare it against existing off-the-shelf spatial attention mechanisms (CBAM, SE, coordinate attention) at the same position in the pipeline with the same backbone. Since Section 2.2 discusses these existing mechanisms, the omission of such a comparison makes it unclear whether MHSAM's specific conv-deconv design offers a real advantage over well-known alternatives. This is needed to substantiate the novelty claim for MHSAM.

### Minor

- **Portability results for CVCAM are mixed.** When CVCAM replaces QACVFM in DetGeo, performance improves on 2 of 3 tasks but *declines* on the Drone→Satellite task of CVOGL (Table 4). The paper's explanation ("it also attends to some non-target regions") is speculative. This does not invalidate the full AttenGeo system, which uses CVCAM + MHSAM together and performs best overall, but it does weaken the claim that CVCAM itself is uniformly superior to QACVFM.

- **Incomplete experimental details affecting reproducibility.** (a) Batch size is not reported. (b) Data augmentation strategy is not described — critical for cross-view tasks where viewpoint variation is the main challenge. (c) The learning rate schedule is described only as "decayed every 10 epochs" with no decay factor stated. (d) The evaluation metrics "accu@0.25" and "accu@0.5" are used (line 179) by referencing Sun et al. (2023) but are not defined in the paper itself; a brief definition would aid readability.

- **No error bars or statistical significance reported anywhere.** All results are point estimates without standard deviations or confidence intervals. On the G2D test set (only 370 samples), performance differences of a few percentage points may not be meaningful.

- **MHSAM padding=0 design is not justified.** With stride=1, padding=0, and kernel sizes {1, 3, 5}, the spatial dimensions shrink by 0, 2, and 4 respectively before deconvolution restores them. This means border pixels are lost for larger kernels (the "edges" of the feature map are cropped). This design choice is not discussed or motivated.

### Trivial

- The dimension tracking in the cross-attention equations (Eq. 7–8) is technically correct but could be presented more clearly for readability.

## Nice-to-Haves

- A quantitative evaluation of attention quality (e.g., attention-map IoU with ground-truth boxes, or pointing-game accuracy) would strengthen the claims about "suppressing edge noise" beyond the qualitative visualization in Figure 6.
- An analysis of failure cases would help understand when iterative cross-attention helps versus when it degrades performance (as observed in the D→S portability result).

## Removed Points

*These points were raised by reviewers but removed after verification against the paper.*

- **Equation 7 dimension "confusion":** The critic raised this but then confirmed the math is correct; the notation, while not the cleanest, is not erroneous. This is a trivial presentation observation at most.
- **"No actual multi-scale fusion mechanism" in MHSAM:** The critic claimed the heads are independently summed without learned fusion. In fact, the three heads are summed and passed through a sigmoid to produce a learned weight tensor A, which is then element-wise multiplied with the input — this *is* a learned fusion mechanism. The criticism overstates the issue.
- **Generic "Related Work is a generic survey":** The observation that Section 2.2 reads as a generic survey is not a concrete, specific weakness; the more precise version (missing CBAM/SE experimental comparisons) is retained above as a Major weakness.
- **Reproducibility concerns about "undisclosed hyperparameters" beyond batch size, data augmentation, and LR factor:** The critic listed several missing details, but some (e.g., exact output feature dimensions) are either standard for ConvNeXt V2-Tiny or minor; the most consequential ones are retained in the Minor section.

## Novel Insights

None beyond the paper's own contributions. The reviews confirm the paper's internal evidence (ablation) while identifying external validity gaps (backbone confound, missing baselines).

## Suggestions

1. **Re-implement DetGeo's QACVFM with the same ConvNeXt V2-Tiny backbone** and compare directly against CVCAM. This single experiment would resolve the main confound and either validate or refute the paper's headline claim.
2. **Benchmark MHSAM against CBAM, SE, and coordinate attention** at the same insertion point in the AttenGeo pipeline, with the same backbone and training setup.
3. **Expand the G2D dataset description** to include collection methodology, annotation protocols, object categories, and dataset statistics.
4. **Report error bars** (e.g., standard deviation over multiple runs with different seeds) for all main results.
5. **Define accu@0.25 and accu@0.5 explicitly** in the paper rather than only by reference.
6. **Specify the missing experimental details**: batch size, data augmentation strategy, and LR decay factor.

## Score and Decision

MY FINAL SCORE: <score>4.5</score>
MY FINAL DECISION: <decision>Reject</decision>