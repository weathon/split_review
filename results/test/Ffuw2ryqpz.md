Now I have thoroughly read the paper. Let me produce the consolidated review.

## Summary

Real3D proposes a self-training framework that enables training Large Reconstruction Models (LRMs) on single-view real-world images — a data source far more abundant than the synthetic 3D assets or multi-view captures conventionally used. The framework combines (i) a cycle-consistency pixel-level loss with stop-gradient and curriculum learning, (ii) a CLIP-based semantic loss with hard negative mining, and (iii) an automatic data curation pipeline to filter occluded instances. Starting from a TripoSR base model trained on Objaverse, Real3D jointly fine-tunes on curated real images and synthetic data. The method consistently outperforms prior work (TripoSR, LRM, LGM, CRM, InstantMesh) across four evaluation datasets including MVImageNet, CO3D, OmniObject3D, and an in-the-wild test set, with PSNR gains of 0.5–0.7 on average.

## Strengths

1. **First LRM trained on single-view real images via a carefully designed self-training framework.** The paper proposes two complementary unsupervised losses — cycle-consistency (pixel-level) and CLIP-based semantic similarity (image-level) — that provide supervision where no ground-truth novel views exist. The ablation on CO3D (Table "ablation") shows the full method achieves 19.18 PSNR vs. the TripoSR baseline's 18.44 (+0.74, ~4% relative). The design choices (stop-gradient to prevent trivial solutions, curriculum to handle compounding errors, hard negative mining to avoid the multi-head problem) are each validated by ablation.

2. **Consistent outperformance across four diverse evaluation datasets.** Real3D surpasses all baselines on MVImageNet (+0.72 PSNR over TripoSR on novel-view synthesis, Table 1), CO3D (+0.74 PSNR, Table co3d), OmniObject3D (+0.74 PSNR, Table omniobject), and the in-the-wild Real3D test set (+0.82 PSNR self-consistency, Table wild). The gains are consistent across both in-domain and out-of-domain settings, suggesting the improvement is not spurious.

3. **Larger gains from single-view real data than prior methods achieve from multi-view real data.** On MVImageNet, Real3D's Δ over TripoSR (+0.032 CLIP, +0.010 LPIPS, +2.08 PSNR self-consistency) exceeds LRM*'s Δ over LRM (+0.020 CLIP, +0.016 LPIPS, +1.28 PSNR; see Table 1 "Δ" rows). This directly supports the paper's claim that training on abundant single-view real images can be more effective than collecting scarce multi-view real data.

4. **Scalability demonstrated with increasing data volume.** The paper reports (Fig. 4, referenced in ablation text) that performance improves consistently as more real images are added to training, supporting the potential for further scaling.

## Weaknesses

### Fatal
None.

### Major

1. **The automatic data curation method is critically underspecified.** Section 3.2 (lines 164–165) consists of only two sentences: "Our data curation method aims to select high-quality shape instances from real images. Specifically, we find it is important to train the model with un-occluded instances. Thus, we develop an automatic occlusion detection method leveraging the synergy between instance segmentation and single-view depth estimation." This filtering reduces 3M raw instances to 300K — a 10× selection — yet no algorithmic steps, no precision/recall validation against a held-out human-labeled set, and no ablation isolating the curation filter's independent contribution (vs. just the amount of data) are provided. The paper bills curation as a contribution in the abstract ("we develop an automatic data curation approach"), and the dataset "Real3D-300K" is named after the paper itself. Reproducing or even critically evaluating the paper requires understanding how occlusion is detected via the "synergy" of segmentation and depth, which is not disclosed. *Why this matters:* This is not a minor missing detail — it is a core component of the data pipeline that the paper cannot be reproduced without.

2. **FID computation for the semantic similarity metrics is underspecified.** The paper states: "we render 7 views where the azimuths are uniformly sampled in range [0, 360] and no elevations. We use semantic metrics of LPIPS, CLIP similarity, and FID score" (line 223). FID is a distributional metric requiring two sets of images, but it is not explained whether FID is computed over rendered views per-instance, over the entire test set as a distribution, or using some other protocol. This matters because FID is reported as a key measure of improvement (e.g., 106.5 vs. 128.5 in Table wild), and the result is not interpretable or reproducible without this detail.

### Minor

1. **The in-the-wild test set (Real3D-300K test split) shares the same curation pipeline as the training data.** The paper keeps aside 1000 images from the curated dataset, meaning the test and training distributions are both filtered by the same occlusion-detection criterion. This creates a risk that numbers partly measure how well the model fits the curation filter. However, this concern is substantially mitigated by the paper's three other evaluation settings (MVImageNet, CO3D, OmniObject3D), which are fully independent datasets with ground-truth multi-view data and show consistent improvements. The paper would be stronger with an additional evaluation on truly unfiltered in-the-wild images.

2. **No error bars or statistical significance tests are provided.** PSNR gains are modest (0.5–0.7), yet no standard deviations, confidence intervals, or significance tests are reported for any comparison. Given that evaluation sets may have variance, it is unclear whether the observed gains are reliable. This is a common issue in the LRM literature but would substantially strengthen the quantitative claims.

3. **The canonical-pose assumption for real-world inputs is stated but not analyzed.** The paper uses TripoSR as the base model, which is "an LRM without input pose and intrinsics conditioning" (line 85). Line 108 mentions φ as the "constant canonical pose of the input view." Real-world images have arbitrary object orientations, yet the paper does not discuss or validate how the model handles this — e.g., whether inputs are rotated to a canonical frame, or how performance degrades under increasing rotation. A brief analysis (or acknowledgment as a limitation) would strengthen the paper, especially since the claimed advantage is "closing the training-inference gap" for in-the-wild images.

4. **The ablation table (Table ablation) would benefit from a row isolating raw (uncurated) data with only the input-view loss.** The closest existing rows are "raw + $L_{in}$" (18.63 PSNR) and "clean + $L_{in}$" (18.60 PSNR), but a direct comparison between raw data with and without the self-training losses would clarify how much gain comes from curation vs. the proposed losses.

### Trivial
None.

## Nice-to-Haves

- A deeper analysis of why stop-gradient prevents the trivial solution in cycle-consistency (e.g., does it turn the loss into a form of self-supervised learning akin to BYOL?).
- Evaluation on truly unfiltered in-the-wild images from sources like OpenImages or LAION, even if the numbers are lower.
- Analysis of robustness to arbitrary input rotations (e.g., rotating test images by 30°, 60°, etc.) to characterize the operating range of the canonical-pose assumption.

## Removed Points

These points were flagged by reviewers but removed or downgraded after verification against the paper:

- **Criticism that "missing appendix" or "missing proofs" make the paper incomplete.** The parser strips these sections; the original submission has them. → *Removed per hard rule.*
- **Criticism that "no missing related works are cited."** Per instructions, I cannot confirm the existence of missing related works. → *Removed per hard rule.*
- **Criticism about the cycle-consistency trivial solution not being acknowledged.** The paper *does* acknowledge this (lines 89, 118–119) and provides ablation analysis showing the issue (Table ablation, row e2e+curriculum at 17.78 PSNR). The critic's ask for deeper analysis is fair but downgraded to Nice-to-Have. → *Downgraded per soft rule (paper partially addresses).*
- **Claim that "the paper should also cover Y / domain Z / additional tasks."** The paper's scope is well-defined and the four evaluation datasets cover diverse settings. Requests for broader coverage constitute scope creep. → *Removed per hard rule.*
- **Strengths from Strength Finder that conflict with verified weaknesses:** None conflict directly. Some strengths about "novel evaluation metrics" and "scalability demonstrated" are kept as they are supported. → *Kept.*

## Novel Insights

The most interesting observation from the reviews is the *asymmetry* the paper itself highlights: single-view real images can yield larger gains than multi-view real data, even though multi-view data provides strictly more supervision per instance. This suggests that the bottleneck is not the *amount of supervision per example* but the *diversity and naturalness of the training distribution* — a finding that, if robust, has implications beyond LRMs to any 3D learning task where synthetic data dominates. The harsh critic's concern that the curation pipeline is a black box is the review's most important signal, because it directly touches whether this finding is trustworthy: if the curation filter itself selects easy examples, the observed gains could partially reflect selection bias. An honest discussion of this would strengthen the paper significantly.

## Suggestions

1. **Expand Section 3.2 with a concrete description of the occlusion detection algorithm.** This is the single most impactful change. Describe the specific steps: how instance segmentation (SAM?) and depth estimation interact — e.g., do you compute depth discontinuity at mask boundaries? Do you check depth consistency across the mask interior? Provide at minimum precision/recall on a small human-annotated set of occluded vs. unoccluded instances.
2. **Clarify how FID is computed for the semantic similarity metrics** — whether over rendered views per test sample as a set, over the full test set distribution, or using a different protocol. This is critical for reproducibility.
3. **Add a brief discussion of the canonical-pose assumption** — acknowledge that real-world images have arbitrary orientations, state whether any pose normalization is applied, and provide some robustness analysis.
4. **Report standard deviations or significance indicators** for key comparisons, even if using bootstrapping or split-half estimates.
5. **Add an ablation row:** raw (uncurated) data + input-view loss only, to fully disentangle the curation effect from the self-training loss effect.

## Score and Decision

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>