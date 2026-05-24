Now I have a well-calibrated view. Let me construct the final review.

## Summary

This paper presents CaPT (CLIP as a Prior Teacher), an asymmetric-modalities co-training framework that integrates CLIP into semi-supervised learning. The key idea is to jointly train a fully fine-tuned unimodal vision network alongside a parameter-efficiently adapter-tuned CLIP model, using entropy-weighted co-pseudo labels to fuse their predictions. The method achieves strong empirical results across multiple benchmarks, most notably under extreme label scarcity (e.g., +21.38% over the second-best method on CIFAR-100 with one label per class).

## Strengths

1. **Large-margin improvements in extremely low-label regimes (Tables 1, 3).** Under one-label-per-class settings, CaPT outperforms the second-best method by 21.38% on CIFAR-100 (82.51% vs. 61.13%) and by 4.05% on EuroSAT (96.33% vs. 92.28%). These margins are far beyond typical SSL improvements and directly demonstrate the claimed reduction of label dependency. The improvement is consistent across all 6 USB settings and on ImageNet (+9.33% over RegMixMatch at 10 labels/class).

2. **Comprehensive and informative ablation study (Table 6).** The paper systematically isolates each design component: removing feature-augmented consistency (-0.57%), replacing entropy weighting with equal weights (-0.87%), removing bidirectional flow (-0.88%), and ablating the entire CLIP module (-6.23%). This validates that every claimed component contributes positively.

3. **Resource efficiency (Table 4).** CaPT adds only 8.00% memory and 11.18% training time over the FreeMatch baseline while achieving substantial accuracy gains, making the framework practical where full CLIP fine-tuning would be prohibitive.

4. **Clear and well-motivated problem framing.** The empirical demonstration (Figures 1a–1c) that SSL performance collapses under extreme label scarcity or low label quality is compelling. The attention map analysis (Figure 3) provides visual evidence that the asymmetric-modalities design yields genuinely different representations compared to unimodal co-training.

5. **Scalability across diverse benchmarks (Tables 2, 5).** CaPT shows strong performance on ImageNet and 5 of 6 fine-grained datasets, including Flowers102, StanfordCars, SUN397, DTD, and SVHN, demonstrating its general applicability beyond simple datasets that overlap with CLIP's pretraining corpus.

## Weaknesses

### Major

1. **Missing comparison against other CLIP-integrated SSL baselines.** The paper compares CaPT against standard SSL methods (FixMatch, FreeMatch, RegMixMatch, etc.) that do not use CLIP. Since CaPT's primary advantage comes from incorporating CLIP's external knowledge, the evaluation would be far more informative if it included baselines such as: (a) using adapter-tuned CLIP predictions as a fixed teacher to pseudo-label unlabeled data and then training a standard SSL method; (b) using CLIP's zero-shot predictions to initialize pseudo labels and then running a standard SSL method. The current ablations (CaPT-Deb ≈ DebiasPL, CaPT-Uni ≈ unidirectional CLIP→vision) partially address this, but the paper would be strengthened by directly comparing against these simpler alternatives to demonstrate that its specific co-training mechanism—and not merely the presence of CLIP—is responsible for the gains. The ablation shows that 85% of the improvement over FreeMatch (5.35/6.23 percentage points) comes from adding CLIP in any form; the co-training bidirectional flow contributes only 0.88%. This does not invalidate the contribution but makes the missing baselines more consequential.

2. **Theoretical theorem is overclaimed and loosely connected to modern SSL practice.** Theorem 1.1 derives a bound on pseudo-label error for a **nearest-prototype classifier** under a Gaussian mixture model. Modern SSL methods use deep neural networks, confidence thresholds, consistency regularization, and strong augmentations—none of which appear in the theorem's setting. The paper frames this as revealing a "fundamental limitation" of SSL, but the theorem is essentially a formalized intuition (poor labeled data → worse pseudo labels) dressed in notation. This does not deepen the paper's contribution and distracts from the genuine empirical motivation (Figures 1a–1c), which is already strong and self-contained.

### Minor

3. **Small gains from the core co-training mechanism.** While the full CaPT framework outperforms baselines substantially, the specific novel components (entropy-based weighting, feature-augmented consistency, bidirectional flow) each contribute modest improvements (0.57%–0.88% on CIFAR-100). The paper's narrative emphasizes "richer cross-modal information exchange" and "asymmetric-modalities co-training," but the ablation suggests these components play a supporting rather than primary role. The dominant driver is simply integrating CLIP (in any form) with a fully fine-tuned vision network. A more measured framing would improve the paper.

4. **No standard deviations reported for ImageNet (Table 2).** Given the variance typical in SSL experiments, single-run numbers without error bars are unreliable for drawing conclusions about relative method performance on this dataset.

5. **FGVC-Aircraft failure acknowledged but not analyzed.** The paper notes that CaPT fails to improve on FGVC-Aircraft but provides no analysis of why CLIP's prior proves unhelpful on this particular dataset. Understanding this failure mode would improve the paper's scientific contribution and help users assess when the method is applicable.

### Trivial

6. The paper does not specify hyperparameter values in the main text (e.g., the Beta distribution parameter α for Mixup, confidence threshold defaults). These are deferred to Appendix F (stripped by the parser). While not a fatal omission, including key defaults in the main text would improve self-containedness.

7. The thresholding mechanism for handling low-confidence predictions from both modules simultaneously is not fully discussed. If both modules produce low-confidence predictions, the co-pseudo label's effective supervision weight becomes near-zero — this case merits a brief discussion.

## Nice-to-Haves

- Report the evolution of entropy-based weights over training to substantiate the claim that CLIP dominates early and the unimodal network takes over later.
- Discuss data contamination concerns more upfront in the main text (currently deferred to Appendix M). CLIP's training data likely overlaps with CIFAR, STL-10, and EuroSAT. The fine-grained experiments partially address this, but the concern should be acknowledged directly.
- Compare against backbone specifications: the paper says UPM uses "the same training configuration and backbone as USB" (ViT-B/16), while CLIP uses ViT-B/32. Explicitly discuss any implications for fairness.

## Removed Points

These points are flagged to be removed; treat them with caution:
- **Harsh critic's "unfair comparison invalidates headline claims."** This overstates the issue. The paper's contribution IS integrating CLIP into SSL; comparing against non-CLIP methods is standard practice when proposing a new technique. The ablations (CaPT-Deb, CaPT-Uni) provide relevant internal comparisons. The missing baselines are a real gap (addressed in Major weakness #1 above), but do not "invalidate" the claims.
- **Harsh critic's speculation that missing appendix sections would change evaluation.** Parser-stripped appendix content (hyperparameters, proofs) is assumed to exist in the original submission and cannot be used as a basis for criticism.
- **Strength Finder's generic strengths like "addressed an important problem."** These are too generic to meaningfully support the paper.
- **Harsh critic's claim about "data contamination" as a core weakness.** The paper explicitly addresses this in Appendix M and through fine-grained benchmarks; the concern is acknowledged, not ignored.

## Novel Insights

The harsh critic's most valuable observation—that the co-training mechanism contributes only ~14% of the total gain over FreeMatch, with the rest coming from simply adding CLIP—is actually instructive when read alongside the ablation. It reveals that the paper's real contribution is not the bidirectional co-training per se but rather an efficient, well-engineered pipeline for adapting CLIP to serve as a reliable teacher for SSL in low-label regimes. The entropy-based weighting and feature-augmented consistency, while individually modest, cumulatively add ~2.3% over the unidirectional baseline, and the total framework (+6.23% over FreeMatch) is practically significant. The paper would be strengthened by reframing its narrative around "efficient CLIP integration for SSL" rather than "co-training breakthrough," since the empirical evidence supports the former framing more strongly.

## Suggestions

1. **Add at least 2–3 CLIP-based SSL baselines** in revision: (a) adapter-tune CLIP, use its predictions to pseudo-label unlabeled data, then train FreeMatch on the combined set; (b) use CLIP zero-shot predictions to initialize pseudo labels and run FreeMatch. This would isolate whether the co-training framework adds value beyond simply having CLIP available.
2. **Tone down the theoretical contribution.** Move Theorem 1.1 to the appendix and replace the "fundamental limitation" framing with a clear statement that it formalizes intuition. The empirical motivation (Figures 1a–1c) is sufficient on its own.
3. **Reframe the contribution** around the central question: "How can we efficiently adapt a frozen CLIP model to provide reliable guidance to a fully fine-tuned SSL network?" This aligns better with what the evidence actually demonstrates.
4. **Add error bars for ImageNet results** and analyze the FGVC-Aircraft failure case briefly (even a hypothesis would help).
5. **Report key hyperparameter defaults** (β-distribution α, confidence threshold) in the main text.

## Score and Decision

**My final bracket:** After round 1, the paper plausibly sits between 4.5 and 6.5, bracketed by SemiCLIP (5.80, Accept, strong topical match) on the high side and WSFT (4.75, Reject) / DIPS (5.00, Reject) on the low side.

**Round 2 narrowed the bracket to 5.0–6.0.** Compared to SemiCLIP (5.80), CaPT has stronger empirical results (21.38% vs. 1.72–6.58% gains) and a more novel asymmetric-modalities framework, but SemiCLIP's evaluation was more complete (it compared against other CLIP methods) and it had fewer framing issues. CaPT is clearly above BOPL (5.33, Reject) and WSFT (4.75, Reject) in both result strength and methodological novelty. The paper is comparable to SemiCLIP in overall quality, with a slight deduction for the evaluation gap and overclaimed theory.

**The paper makes a genuine contribution** with strong empirical evidence, a well-engineered framework, and thorough ablations. The core weaknesses are addressable (adding CLIP-based baselines, reframing the narrative) and do not undermine the core finding that CaPT substantially reduces label dependency in SSL. The paper is recommended for acceptance with revisions addressing the evaluation gap.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Accept</decision>