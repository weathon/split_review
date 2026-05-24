Now I have a thorough understanding of the paper and all the claims. Let me produce the final consolidated review.

## Summary

This paper proposes CaPT (CLIP as a Prior Teacher), an asymmetric-modalities co-training framework that integrates CLIP into semi-supervised learning. The method jointly trains a fully fine-tuned unimodal vision network alongside a parameter-efficiently fine-tuned multimodal CLIP model, using entropy-weighted co-pseudo labels to fuse their predictions. CaPT achieves state-of-the-art results across multiple SSL benchmarks, with particularly large gains in extreme low-label regimes (e.g., +21.38% on CIFAR-100 with one label per class).

## Strengths

1. **State-of-the-art performance across standard SSL benchmarks (Tables 1–3).** CaPT consistently outperforms 12 prior SSL methods on 6 USB settings, ImageNet, and extreme low-label regimes. The gains are substantial and stable (low variance across seeds). These empirical results are the paper's strongest evidence.

2. **Thorough ablation study isolating each design component (Table 6).** The paper ablates adapter-tuning (CaPT-Ada: −16.40%), the DebiasPL-style prior injection (CaPT-Deb: −3.80% to −12.73%), unidirectional flow (CaPT-Uni: −0.88%), feature augmentation (−0.57%), and entropy-based weighting (−0.87%). This decomposition allows readers to assess each component's contribution.

3. **Demonstrated efficiency relative to comparable approaches (Table 4).** CaPT uses only 8% more memory and 11% more time than FreeMatch while improving accuracy from 78.60% to 84.83%. The efficiency stems from freezing CLIP's encoders and using adapter-tuning plus feature-level augmentation.

4. **Wide evaluation scope.** The paper evaluates on standard benchmarks (USB, ImageNet), extreme low-label settings (1 label/class), and fine-grained datasets (6 datasets), demonstrating the framework's generality beyond simple image classification.

## Weaknesses

### Major

- **Missing controlled baseline: "CLIP as static teacher" for a standard SSL method.** The paper shows that CaPT (84.83% on CIFAR-100 with 2 labels/class) outperforms FreeMatch without CLIP (78.60%) and adapter-tuned CLIP alone (74.90%). However, a critical missing baseline is: *use CLIP's adapter-tuned predictions as fixed pseudo labels for FreeMatch (or another SSL method) without bidirectional co-training.* Such a baseline would isolate whether CaPT's co-training mechanism adds value over simply using CLIP as a static teacher. Without it, one cannot rule out the possibility that the bulk of CaPT's gains come from CLIP's prior alone, with the co-training framework adding modest additional benefit. The ablation study partially addresses this (CaPT-Uni, which is CLIP→vision unidirectional flow, achieves 83.95%, only 0.88% below full CaPT), but CaPT-Uni still involves co-training objectives on the CLIP side; a true static-teacher baseline would not fine-tune CLIP at all during SSL training. This is the single most important experiment that would substantiate the paper's central contribution.

- **The contribution from asymmetric-modalities co-training is modest relative to CLIP injection.** From Table 6: "only UPM" (FreeMatch baseline) = 78.60%, "CaPT-Uni" (CLIP→vision one-way) = 83.95%, full CaPT = 84.83%. The gain from adding CLIP in any form is 6.23%, but the marginal gain from bidirectional asymmetric co-training (CaPT-Uni → full CaPT) is only 0.88%. Meanwhile, no experiment quantitatively compares CaPT against a symmetric co-training baseline (e.g., co-training two ViTs with different initializations, à la CLS) under the same training setup. The paper argues that asymmetry avoids a "pattern-homogeneity bottleneck" (Figure 3), but this is supported only by qualitative attention maps, not by an accuracy comparison. The claimed importance of the asymmetric design over the co-training framework as a whole is not well-supported.

### Minor

- **Theorem 1.1 is for a simplified model and does not directly inform CaPT's design.** The theorem bounds pseudo-label error for a nearest-prototype classifier under a Gaussian-mixture generative model. While it serves as mathematical motivation for why label dependency exists in prototype-based SSL, it does not apply to the neural network classifiers and consistency-regularization framework used in CaPT or the baselines. It is never referenced in the method section or used to motivate any design choice (e.g., the thresholding mechanism, the entropy-based weighting, the adapter architecture). The claim that the paper "theoretically establish[es] the label dependency that constrains SSL" is overstated — the analysis occupies a motivational role, not a foundational one for the proposed method.

- **No quantitative comparison against a symmetric co-training baseline under the same experimental protocol.** The paper cites CLS (Yao et al., 2022) as prior work on symmetric co-training and argues that CaPT's asymmetric design is superior, but it never reimplements or compares against a symmetric co-training variant in its own evaluation framework. Such a comparison (e.g., CaPT but with two pure-vision ViTs instead of CLIP+ViT) would directly quantify the benefit of modality asymmetry.

- **Failure on FGVC Aircraft is not analyzed.** On FGVC Aircraft (Table 5), CaPT underperforms FreeMatch (50.12% vs. 51.43% with 5 labels/class) and RegMixMatch (64.33% vs. 66.21% with 10 labels/class). The paper notes this but does not analyze *why*. CLIP zero-shot accuracy on this dataset is 18.97%, which suggests the prior is weak, but the paper does not examine whether the co-training framework itself degrades performance relative to the unimodal SSL baseline, or whether different prompt engineering or adapter-tuning strategies could mitigate this.

### Trivial

None.

## Nice-to-Haves

- A symmetric co-training baseline (two pure-vision ViTs) under the CaPT pipeline to quantify the benefit of asymmetric modalities.
- Experiments with more powerful VLMs (e.g., SigLIP, EVA-CLIP) to substantiate the "future-proof framework" claim.
- Analysis of why CLIP's prior is less effective on FGVC Aircraft (e.g., class granularity, domain shift, prompt sensitivity).

## Removed Points

**"Unfair comparison — CaPT uses CLIP while baselines don't."** This criticism frames the comparison as fundamentally invalid. However, the paper's contribution is a framework for *integrating* CLIP into SSL; comparing against SSL methods without CLIP is the standard way to demonstrate usefulness of the framework. The paper is not claiming to have invented a better SSL algorithm in isolation; it claims to have built a better system by incorporating CLIP. This is a valid contribution framing. The more precise and actionable version of this concern (missing CLIP-as-static-teacher baseline) is retained in the Major weaknesses above.

**"The evaluation lacks rigor / the comparison is unfair on ImageNet where RegMixMatch uses MAE pre-training."** Same reasoning as above — the paper compares systems, not ablation-controlled SSL algorithms. The specific request for a controlled baseline is kept; the blanket "unfair comparison" framing is removed.

**"DebiasPL and CLIP-Adapter already address the goal of integrating CLIP into SSL."** The paper explicitly distinguishes itself from these methods (Figure 2) and shows CaPT outperforms their reimplementations (CaPT-Deb, CaPT-Ada) in Table 6. An ablation comparison is present.

**"Missing appendix content / proofs."** The appendix is stripped by the parser; this is not an author error.

**Various style/formatting nitpicks and speculative concerns.** Removed per the filtering rules.

## Novel Insights

The entropy-based weighting mechanism (Section 3.3, Equations 11–13) provides an adaptive way to balance supervision from CLIP and the unimodal network during training, allowing CLIP to dominate early and the fully fine-tuned network to take over later. This is a practical design choice that addresses the fundamental tension between a frozen/lightly-tuned prior model and a heavily-trained task model. The feature-level Mixup for CLIP (Section 3.2.2) further avoids the computational cost of re-encoding high-resolution images for strong augmentations, a pragmatic efficiency-accuracy trade-off. These two engineering contributions are the most novel aspects of the method beyond the basic idea of co-training with CLIP.

## Suggestions

1. **Add the CLIP-as-static-teacher baseline**: Run FreeMatch (or RegMixMatch) where CLIP's adapter-tuned predictions are used as fixed pseudo labels for the unlabeled data (no bidirectional flow, no CLIP fine-tuning during SSL). This will directly answer whether the co-training mechanism adds value beyond CLIP's prior alone.
2. **Add a symmetric co-training baseline**: Replace CLIP in MPM with a second pure-vision ViT (different initialization) and keep everything else the same. Compare accuracy to full CaPT to quantify the benefit of asymmetry.
3. **Analyze the FGVC Aircraft failure**: Report CLIP zero-shot accuracy on each fine-grained dataset, examine whether the co-training framework actively hurts (vs. doing nothing), and discuss whether prompt engineering or adapter design could mitigate this.
4. **Tone down the theoretical claim**: Clarify that Theorem 1.1 provides motivation for the label-dependency problem, not a theoretical foundation for CaPT specifically.

## Score and Decision

The paper makes a practical contribution — a well-engineered framework that integrates CLIP into SSL — and backs it with extensive experiments showing strong gains. The weaknesses are real but addressable: the missing controlled baseline is the most significant gap. The theory is decorative but not harmful. The core empirical finding (CaPT improves over strong SSL baselines) is credible and supported by the data.

MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>