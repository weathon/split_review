Here is the consolidated final review.

## Summary

This paper introduces MetaCLIP, a transparent and reproducible data curation algorithm that reconstructs CLIP's metadata construction (from WordNet and Wikipedia), sub-string matching, and per-entry balancing. The core finding is that MetaCLIP, applied to CommonCrawl with 400M image-text pairs, outperforms CLIP's proprietary WIT-400M across multiple zero-shot benchmarks under matched training conditions (e.g., 70.8% vs. 68.3% on ImageNet with ViT-B/16). Scaling to 2.5B data with the same training budget yields 82.1% on ViT-bigG/14. The paper provides a clean ablation study isolating balancing as the critical ingredient.

## Strengths

- **Reproducible curation that outperforms CLIP's proprietary data under matched conditions**: MetaCLIP-400M achieves 70.8% zero-shot ImageNet (ViT-B/16) vs. CLIP's 68.3% and OpenCLIP's 67.0%, under identical model, training budget, and evaluation protocols (Table 1). This directly supports the paper's central claim that data curation — not architecture or objective — is the key differentiator.

- **Rigorous ablation isolating the critical role of balancing**: Training on the full 1.6B unbalanced pool yields only 61.9% ImageNet accuracy (ViT-B/32), while MetaCLIP's balanced 400M subset achieves 65.5% (Table 3). Removing balancing from MetaCLIP drops accuracy from 65.5% to 60.8% (Fig. 1). This cleanly demonstrates that metadata-based balancing is necessary.

- **Detailed reconstruction of CLIP's metadata pipeline**: The paper rebuilds CLIP's 500k-query set from WordNet and Wikipedia with specified thresholds, providing composition statistics (Table 1) and distribution analysis showing 114k of 500k entries have zero matches, while only 3.2% of entries account for 94.5% of raw counts — actionable insights for the community.

- **Efficient algorithm avoiding expensive inverted indexing**: The independent-sampling procedure (Algorithm 1) replaces inverted-index construction with per-pair sampling, enabling scaling to 10.7B matched pairs. This is a practical engineering contribution for large-scale data pipelines.

## Weaknesses

### Fatal
None.

### Major

- **The scaling analysis (1B vs. 2.5B) confounds data distribution with training epochs.** All scales are trained for the same 12.8B seen pairs, meaning MetaCLIP(1B) sees 12.8 epochs while MetaCLIP(2.5B) sees only ~5.1 epochs. The paper attributes performance differences (e.g., 1B outperforming 2.5B on fine-grained tasks like CUB, Flowers) to the threshold \(t\) and resulting head/tail distribution, but the epoch effect is a major confound: the 1B model sees tail data 2.5× more often. The conclusions about "similar accuracy for 1B and 2.5B" and the associated distribution analysis (Fig. 3, cumulative sums) are therefore ambiguous — they do not cleanly separate the effect of data distribution from the effect of repeated passes. The 400M main comparison is unaffected by this issue, but the scaling story is incomplete.

### Minor

- **The claim that the independent-sampling algorithm "is equivalent to CLIP's curation" is imprecise.** The two procedures differ: CLIP's inverted-index approach applies an exact per-entry cap (sampling without replacement from each entry's list), while MetaCLIP uses independent Bernoulli trials (expected cap, with variance). For large counts (t=20k on pools with millions of pairs), the difference is practically negligible, but the paper provides no formal analysis or simulation to justify the equivalence claim. The algorithm should be described as a close approximation rather than an exact replica. This does not undermine the paper's main results — MetaCLIP works well regardless — but it weakens the "demystification" narrative.

- **Only a single training run is reported for most experimental conditions.** The paper notes that standard deviation is small (\(\pm 0.1\%\) for ImageNet ViT-B/32) based on multiple seeds, but this variance estimate is only reported for one configuration. Readers cannot assess the stability of other results.

- **The thresholds for metadata construction (PMI≥30, pageview frequency≥70) are estimated without sensitivity analysis.** While the paper acknowledges these are estimates, the impact of varying these thresholds on downstream performance is not explored.

### Trivial

- The abstract's claim that the success of CLIP is attributed to data and "not the model architecture or pre-training objective" is presented as a belief/hypothesis. The experiments only vary data while keeping architecture and objective fixed, which is consistent with the claim but does not prove that architecture/objective are unimportant. The paper's framing is reasonable for a data-centric study, but the wording could be sharpened.

## Nice-to-Haves

- A comparison to DataComp (Gadre et al., 2023) under matched training settings would strengthen the empirical contribution, especially since the paper discusses DataComp in Related Work and claims an advantage from "starting from scratch" (not using a pretrained filter). However, DataComp uses a fundamentally different approach (CLIP-based filtering), so its absence is not a flaw — a direct comparison would be a useful addition but is not required given the paper's scope.

- Retrieval benchmarks (Flickr30k, COCO) would provide a more complete picture of data quality beyond zero-shot classification, though the paper's evaluation scope is defensible.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **"Missing references to DFN (Fang et al., 2023) and Negodo et al. (2024)"**: Removed per the rule that missing related works should not be mentioned, as external sources cannot confirm their existence or relevance.

- **"The paper does not explain why online balancing is slightly better"**: Removed as factually incorrect — the paper explicitly states: "The better accuracy for online balancing is explained by the larger diversity in head data."

- **"The paper should discuss how substr_matching handles overlapping matches and de-duplication"**: Removed as implementation detail nitpicks that are not central to the paper's contribution.

- **"Comparison to DataComp is missing"**: Moved to Nice-to-Haves (see above) rather than a weakness, as the paper's scope (reconstructing CLIP's pipeline from scratch) makes DataComp's CLIP-filtering approach a different class of method. The exclusion is defensible.

## Novel Insights

Beyond the paper's own contributions, the reviews surface a useful observation: the independent-sampling algorithm and CLIP's per-entry cap are not precisely equivalent, and interrogating this gap reveals that the paper's real contribution is a practical, scalable approximation that works empirically — not a verified reverse-engineering of CLIP's exact process. Reframing MetaCLIP as a "replica-inspired" rather than "equivalent" approach would make the paper's methodological stance cleaner and more defensible.

## Suggestions

1. **Clarify the equivalence claim**: Replace "equivalent to CLIP's curation" with "a close approximation" or "asymptotically equivalent for large pools," and provide a brief analysis showing that the expected per-entry counts match while variance is controlled at scale. A small simulation on a random subset comparing per-entry inclusion sets between the two methods would definitively settle this.

2. **Address the epoch confound in scaling**: Either (a) train the 1B and 400M sets for proportionally fewer iterations so all scales see the same number of epochs, or (b) explicitly acknowledge that the scaling comparisons are confounded and reframe the conclusions accordingly (e.g., "MetaCLIP(1B) with more repeated passes over tail data matches or exceeds MetaCLIP(2.5B) with fewer passes but more head diversity").

3. **Report multi-seed variance for the main comparisons** (at least for the headline result: ImageNet ViT-B/32 and ViT-B/16).

4. **Soften the "data, not architecture" language** to "data is the primary driver" or "data plays a more critical role than commonly assumed," since the paper does not isolate architecture effects.

## Score and Decision

This paper makes a substantial contribution: it provides a working, open-source data curation pipeline that achieves state-of-the-art CLIP performance starting from CommonCrawl, and it rigorously ablates the importance of metadata balancing. The core 400M comparison is clean and convincing. The main weaknesses — the imprecise equivalence claim and the confounded scaling analysis — are addressable and do not invalidate the core findings. The paper is clearly written, the experiments are generally well-controlled, and the community would benefit from its release.

MY FINAL SCORE: <pineapple>7.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>