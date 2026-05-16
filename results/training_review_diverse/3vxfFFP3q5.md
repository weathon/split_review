Now I have all the information needed. Let me write the final consolidated review.

---

## Summary

This paper proposes VOVTrack, a method for open-vocabulary multi-object tracking (OVMOT) that introduces two main innovations over prior work (OVTrack). First, a **tracking-state-aware prompt-guided attention** mechanism uses adjective pairs (e.g., "unoccluded and occluded") to estimate per-proposal quality during tracking and weight training samples accordingly, improving detection. Second, a **self-supervised object similarity learning** framework leverages 534.1K frames of unlabeled TAO video data to train the association head via intra-consistency (pairwise symmetry and triple-wise cyclicity) and inter-consistency (spatial-appearance) losses. VOVTrack achieves state-of-the-art results on the TAO benchmark, outperforming OVTrack and even OVTrack+RegionCLIP (which uses 3M additional CC3M images) on most metrics.

## Strengths

1. **Tracking-state-aware prompt-guided attention is novel and well-validated.** The idea of using adjective prompt pairs to model object states (occlusion, blur, etc.) during tracking and using the resulting attention weights to downweight low-quality proposals is clean and domain-appropriate. The ablation study (Table 2) confirms its contribution: removing the attention mechanism drops novel TETA from 34.4 to 29.8, and removing the piecewise weighting strategy drops it further to 31.7. This is a direct, measurable contribution that is specific to the video tracking setting and not borrowed from image-based OVD.

2. **First method to use raw unlabeled video for OVMOT self-supervised training.** Prior work (OVTrack) relied on static hallucinated image pairs that ignore temporal continuity. VOVTrack's use of real video data with consistency-based losses (intra/inter/category) is a genuinely new capability for the OVMOT setting. The ablation shows that removing the full self-supervised learning pipeline drops base TETA from 38.1 to 36.3 and novel TETA from 34.4 to 31.3 (Table 2). The individual ablations (w/o intra, w/o inter, w/o category consistency, w/o long-short sampling) each show degradation, supporting the method's overall design.

3. **State-of-the-art results without large-scale external data.** VOVTrack outperforms all prior methods on the TAO validation and test sets, including OVTrack+RegionCLIP which uses the additional CC3M dataset (3M images). On the validation set, VOVTrack achieves 38.1/34.4 TETA on base/novel classes vs. OVTrack+RegionCLIP's 36.3/32.0 (Table 1). This demonstrates that video-centric design can compensate for additional static image data.

## Weaknesses

### Fatal
None.

### Major

1. **Confounded evaluation of self-supervised learning: the specific SSL method and the additional data are not isolated.** The primary comparison pits VOVTrack (which uses 534.1K unlabeled TAO frames for self-supervised pre-training) against OVTrack (which does not use TAO videos at all). The ablation "w/o self-supervised learning" (Table 2) removes the SSL losses *along with the use of the unlabeled data entirely*. This means the observed improvement from 36.3→38.1 (base TETA) and 31.3→34.4 (novel TETA) could partially or entirely reflect the benefit of additional training data rather than the specific consistency losses. To isolate the contribution of the proposed SSL formulation, the paper would need a baseline that uses the *same unlabeled data* with a simpler SSL objective (e.g., contrastive learning on object crops, or using only the intra-consistency loss without the cyclicity/inter losses). Without this control, the paper's central claim that the specific consistency learning strategy is responsible for the gains is not fully supported. The paper is transparent about the data usage, but the experimental design does not pin the improvement to the method over the data.

### Minor

2. **K-means clustering for category consistency is unvalidated and a key hyperparameter (K) is unspecified.** The category-consistency constraint groups region proposals via K-means on classification head features, then restricts consistency learning to within-cluster pairs. The implementation details (Section 3.4) state "We use the clustering algorithm of K-means" but never specify the number of clusters *K* or how it was chosen. No clustering quality metrics (purity, NMI, adjusted Rand index) are reported — even for base classes where ground-truth labels exist. Since the classification head was trained only on base classes, its features may not discriminate well for novel classes, potentially making the clustering noisy and introducing contaminated self-supervision. The ablation (w/o category consistency drops novel TETA from 34.4 to 32.2) shows that *some* grouping helps, but does not verify the clustering is correct or that the results are robust to the choice of K.

3. **Adaptive temperature τ in Eq. (3) is not specified.** The paper describes τ as an "adaptive temperature adjustable parameter" in the normalized similarity matrix softmax (Eq. 3, line 233), but neither its initial value nor its adaptation mechanism is reported in the implementation details (Section 3.4). Temperature is typically critical in contrastive/consistency learning, and leaving it unspecified impairs reproducibility.

4. **Transition from the maximization objective (Eq. 4) to the minimization loss (Eq. 5) is not explained.** Eq. (4) is formulated as `max S = S_intra + α·S_inter`, but the implemented loss is `L = L_intra + α·L_inter` which is minimized. The transformation — how maximizing consistency becomes minimizing a loss composed of L() from Eq. (6) and BCE — is abrupt and confusing for readers.

5. **No statistical variance reported.** Results are reported as single runs without error bars or standard deviations. Given that the absolute TETA improvements over OVTrack are modest (2–6%), the significance of the improvements is unclear. While single-run evaluation is common in this area, reporting variance would substantially strengthen the evidence.

### Trivial

- The dagger (†) in the TAO column of Table 1 is not accompanied by an explicit footnote in the extracted text (likely a parser issue that will be resolved in the camera-ready version), but readers would benefit from a clear caption note stating that this indicates use of TAO unlabeled video data.

## Nice-to-Haves

- **Ablation over prompt pairs**: The choice of four specific prompt pairs (e.g., "complete and incomplete", "unoccluded and occluded", etc.) is reasonable but heuristic. Varying the number of pairs or different prompt formulations would strengthen the evidence that performance is robust to prompt engineering.
- **Clustering validation**: Reporting clustering metrics (purity, NMI) on base classes and showing qualitative cluster examples for novel classes would turn a current weakness into a transparent strength.
- **Discussion of IoU_thres=0.9**: The paper uses a 0.9 IoU threshold for the inter-consistency assignment matrix. Reporting the proportion of adjacent-frame object pairs that satisfy this threshold would help readers assess the sparsity of this supervisory signal.

## Removed Points

These points are flagged to be removed; treat them with caution:

- **"The phrase 'same training dataset (annotations)' is misleading"** — The paper's contribution statement explicitly says "(annotations)" to clarify this distinction. This is precise and transparent, not misleading. **Removed: factually incorrect criticism.**
- **"The dagger in Table 1 should be explicitly clarified"** — This is likely a parser artifact (the footnote was stripped). The paper's main text clearly states that it uses TAO unlabeled videos. **Removed: parser artifact / formatting issue.**
- **"No ablation varying the prompts" framed as a core weakness** — This is a reasonable suggestion but not a weakness; it is a nice-to-have. **Moved to Nice-to-Haves.**
- **"λ not specified"** — λ is specified as 0.007 in the implementation details (line 304). **Removed: factually incorrect.**

## Novel Insights

The reviews surface one genuinely novel observation beyond the paper's own contributions: the prompt-guided attention mechanism elegantly repurposes the CLIP text encoder's semantic understanding to assess *object state quality* (occlusion, blur, completeness) rather than *category identity*. This is a clever cross-modal transfer — using language prompts designed for state description to produce training weights — that could generalize beyond tracking to other video tasks where sample quality varies over time (e.g., self-supervised video representation learning, active frame selection). The fact that this simple weighting scheme produces measurable gains (4.6 TETA on novel classes) without any state-level annotations is noteworthy.

## Suggestions

1. **Add a controlled SSL baseline.** Train a version of VOVTrack that uses the same 534.1K unlabeled TAO frames but with a simpler self-supervised objective (e.g., contrastive learning with random temporal crops, or the intra-consistency loss only without cyclicity/category clustering). If the full method still outperforms this baseline, the claim about the specific consistency formulation is solid. If not, reframe the contribution around "using unlabeled video data for OVMOT" more generally.
2. **Report the number of clusters K and clustering quality metrics** (purity, NMI for base classes). Perform a sensitivity analysis over K to show robustness.
3. **Specify τ** — its initial value, whether it is learned or fixed, and if adaptive, describe the adaptation mechanism.
4. **Clarify the Eq. (4)→Eq. (5) transformation** — state explicitly that maximizing consistency is equivalent to minimizing the proposed loss (or explain any re-formulation).
5. **Add standard deviations** over at least 3 runs for the main results and key ablations.

## Score and Decision

The paper makes a clear contribution to a relatively new problem (OVMOT) with two well-motivated components. The prompt-guided attention is cleanly validated. The self-supervised video training direction is valuable and underexplored in this setting. The main reservation is the confounded evaluation of the SSL component, which prevents full attribution of the gains to the proposed consistency formulation versus the additional data. This is a significant weakness but not a fatal one — the paper's core novelty (using video data and tracking-state awareness for OVMOT) remains intact, and the method achieves SOTA results. The paper would benefit from a controlled baseline in a revision but is publishable in its current form with the limitation acknowledged.

MY FINAL SCORE: <pineapple>6.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>