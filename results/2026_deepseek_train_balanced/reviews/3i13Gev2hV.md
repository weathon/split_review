## Summary

This paper proposes HyCoCLIP, an extension of hyperbolic vision-language models (specifically MERU) that incorporates compositional scene hierarchies via bounding-box-level supervision. The key idea is to jointly model intra-modal hierarchies (whole image → object boxes, full text → noun phrases) and inter-modal hierarchies (text → image) through a unified contrastive and entailment-based objective in hyperbolic space. Experiments on GRIT (20M pairs) show improvements over CLIP and MERU on zero-shot classification (+5 points ImageNet), scene understanding benchmarks (60% vs near-random on VL-CO), and hierarchical classification metrics.

## Strengths

- **Explicit modeling of both intra-modal and inter-modal hierarchies in a single hyperbolic objective.** The paper formalizes how whole images relate to their object boxes (intra-modal) alongside the standard text→image (inter-modal) entailment, using a unified loss (Eq. 7, hCE). The ablation study (Table 5, referenced in Sec. "Pre-training loss terms") confirms that each entailment term contributes positively to performance, providing direct evidence that the compositional formulation is not just decorative.

- **Demonstration that naive box inclusion hurts CLIP/MERU while the hierarchical formulation helps.** The paper explicitly tests adding box-level data as additional samples to CLIP and MERU, reporting that this "does not improve performance, despite nearly doubling the samples" (Sec. "Zero-shot image classification"). HyCoCLIP, using the same box data but with hierarchical losses, improves ImageNet accuracy to 45.8% vs. 40.1% (MERU) and 40.6% (CLIP). This contrast provides causal evidence that the hierarchical formulation, not simply more data, drives the gains.

- **Large gains on compositional scene understanding where CLIP and MERU are near-random.** On VL-Checklist-Object (object perturbation), CLIP and MERU give near-random performance while HyCoCLIP reaches 60% accuracy. On VG-Attribution it achieves 68.4% mean accuracy, surpassing all baselines. These benchmarks directly test compositional reasoning about objects in scenes, validating the paper's central claim.

- **Consistent improvements on hierarchical classification metrics using the WordNet hierarchy of ImageNet labels.** The paper reports consistent improvement on hierarchical metrics, directly confirming that the learned hyperbolic space better represents the class-label hierarchy — a property that neither CLIP nor MERU adequately captures.

## Weaknesses

### Fatal

None.

### Major

None.

### Minor

- **No controlled ablation isolating the hierarchical formulation from box-level data augmentation.** The paper's strongest claim is that the *hierarchical inductive bias* drives improvement, not simply more training signal from boxes. While the paper shows that CLIP+boxes and MERU+boxes degrade (supporting the claim), a cleaner test would be to train HyCoCLIP with box-level data but *without* the hierarchical losses (e.g., treating boxes as additional positives in a standard contrastive loss). The current ablation (Table 5) toggles individual loss terms but does not compare against a non-hierarchical box-augmented baseline using the same architecture and data. This one experiment would substantially sharpen the paper's central claim.

- **The RegionCLIP comparison is confounded by multiple uncontrolled variables.** HyCoCLIP uses ViT-B/16 trained on GRIT (20M images), while RegionCLIP uses ResNet50x4 trained on CC3M (3M images) with a frozen text encoder from CLIP-400M. The paper transparently reports these differences, yet claims HyCoCLIP "surpasses RegionCLIP on the novel categories" without sufficient caveats about the incommensurable training setups. This comparison should be either removed or presented with explicit acknowledgment that the different architectures, data sizes, and training protocols preclude a direct comparison.

- **The η threshold parameter is introduced but never specified or analyzed.** The modified entailment loss (Eq. 9) introduces η as a scalar multiplier on the half-aperture ω(q), but the paper does not report what value of η is used, whether it is tuned, or how different values affect the learned embedding geometry. Given that the method is built on this loss modification, its opacity is a meaningful gap.

- **Batch-size scaling ablation evaluates MERU, not HyCoCLIP.** The experiment (Sec. "Scaling w.r.t batch size") trains MERU-ViT-S (a baseline, not HyCoCLIP) with varying batch sizes. Since HyCoCLIP doubles the effective number of training samples per batch (images + boxes), its batch-size dynamics could differ substantially. This ablation is not informative for the proposed method and should either be run on HyCoCLIP or removed.

- **Missing implementation details in the main paper.** The curvature κ, the threshold η, the specific phrase grounding model used to generate boxes, and standard training hyperparameters (learning rate, optimizer, schedule, temperature τ) are not reported in the main text. While these may appear in a stripped appendix, they are essential for reproducibility and should be in the main paper.

- **No error bars or variance estimates.** Results are reported as single numbers. Given that VLM training is sensitive to random seeds and data ordering, variance estimates would strengthen confidence in the reported improvements, especially for the ~5-point ImageNet gain.

### Trivial

- **"For the first time" claim in the abstract is slightly overstated.** MERU already uses inter-modal entailment in hyperbolic space, and Ge et al. (2023) uses object-scene hierarchies in hyperbolic space for vision. HyCoCLIP's novelty lies in combining these lines — which is a legitimate contribution — but the phrasing "for the first time we show how to fully leverage the innate hierarchical nature" overstates the gap.

## Nice-to-Haves

- A sweep showing how different values of η affect embedding geometry (e.g., norm distributions, hierarchical separation) would turn the modified entailment loss from an opaque hyperparameter into a well-characterized component of the method.
- An analysis of why CLIP+boxes and MERU+boxes degrade (distribution mismatch, label noise, inability to handle hierarchy) would strengthen the argument that the hierarchical formulation is necessary.
- A discussion of the 59% training overhead (73h vs 46h) and whether it scales gracefully with dataset size would help practitioners assess the method's practical viability.

## Removed Points

These points were flagged by the reviewers but are removed or downgraded for the reasons given:

- **"The main comparison against baselines is confounded because HyCoCLIP uses boxes while baselines don't"** — REMOVED because the paper *does* test CLIP and MERU with box-level data (line 135), showing they degrade. This objection is factually incomplete.
- **"The entailment loss modification is negligible / not a novel loss formulation"** — REMOVED as a weakness because the paper does not position the η modification as the primary contribution; the contribution is the *compositional setup* (combining inter- and intra-modal hierarchies). The missing analysis of η is retained as a separate minor weakness.
- **Strength Finder claim about "novel thresholded aperture modification"** — REMOVED from strengths; the modification is modest and the strength finder overstates it. The paper's real contribution is the compositional setup, not the loss tweak.
- **Strength Finder's claim about "Zero-shot object detection outperforming RegionCLIP"** — REMOVED from strengths due to the confounded comparison (different architecture, data, training protocol). This result is too weakly controlled to serve as a strength.
- **Training overhead as a weakness** — REMOVED because the paper already acknowledges this ("The training time scales linear with the increase in training volume") and the critic's characterization as "non-trivial" is just a subjective emphasis on an already-reported fact.

## Novel Insights

None beyond the paper's own contributions. The reviews surface the expected tensions between method ambition and experimental control, but do not generate observations that the paper itself does not already make or imply.

## Suggestions

1. **Add a controlled ablation:** Train HyCoCLIP with box-level data but without the hierarchical entailment losses (i.e., treat box-image and box-text pairs as additional positives in a standard contrastive loss). This directly tests whether the hierarchical inductive bias drives the gains versus simply having more training pairs. This is the single most impactful addition.

2. **Report η and analyze its effect.** Provide the value used and a simple sweep showing how η changes embedding norms, aperture angles, or downstream performance.

3. **Recontextualize or remove the RegionCLIP comparison.** Either present it with explicit caveats about the different training setups or replace it with a controlled comparison using the same architecture and data.

4. **Report κ, the grounding model name, and training hyperparameters** in the main paper (or ensure they are present in the published version).

## Score and Decision

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>