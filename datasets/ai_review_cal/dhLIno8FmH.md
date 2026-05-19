- Decision: Accept
- Avg Score: 6.75
- Scores: 8, 8, 8, 3
Now I have all the information needed. Let me produce the consolidated review.

## Summary

This paper proposes NICE, a self-supervised contrastive learning framework that aligns EEG responses with image features to perform zero-shot object recognition. The framework uses an EEG encoder with temporal-spatial convolution and optional self-attention/graph-attention modules, trained with InfoNCE loss against a CLIP image encoder. On a 200-way zero-shot task using a large EEG-image dataset (1,854 concepts, 10 subjects), NICE-GA achieves a top-1 accuracy of 15.6% and top-5 of 42.8%, substantially outperforming the prior method BraVL (5.8%/17.5%). The paper also provides multi-faceted biological plausibility analyses (temporal, spatial, spectral, semantic) and analyzes the effects of data diversity and trial repetition.

## Strengths

1. **Large improvement over prior state-of-the-art on a substantial benchmark**: NICE-GA achieves 15.6% top-1 and 42.8% top-5 in 200-way zero-shot classification, compared to BraVL's 5.8%/17.5% (Table 2). The gap is large (9.8% absolute top-1 improvement) and holds across all 10 subjects in both subject-dependent and subject-independent settings. The chance level is 0.5%, so even the weakest NICE variant (6.2% subject-independent) is well above chance.

2. **Systematic biological plausibility analysis spanning multiple dimensions**: The paper investigates temporal (time-window ablation, Fig. 2B), spatial (electrode-region ablation, Fig. 2C), spectral (frequency-band classification, Fig. 2E), and semantic (RSA, Fig. 3A) aspects of EEG-based decoding. The electrode ablation study shows that removing occipital electrodes drops accuracy by 3.8% (p<0.01) and temporal by 1.9% (p<0.05), aligning with known ventral-stream regions. This goes well beyond the narrow analyses typical in prior EEG decoding work.

3. **Practical insight on data diversity vs. repetition**: Figure 4A systematically compares increasing the number of distinct image conditions versus increasing trial repetitions. Adding conditions yields significant gains throughout (p<0.01 from 25% to 50%, p<0.05 thereafter), while adding repetitions beyond 75% gives no significant improvement. This provides actionable guidance for EEG dataset design.

4. **Thorough encoder ablation study**: Table 3 compares four alternative EEG encoders (ShallowNet, DeepNet, Conformer, EEGNet) and four image encoders (ResNet-50, pre-trained ResNet-50, ViT-B/16, pre-trained ViT-B/16, CLIP), allowing the reader to assess the contribution of each architectural choice.

## Weaknesses

### Fatal

None.

### Major

1. **Headline results use 80-trial averaging; the abstract does not disclose this.** The reported top-1 accuracy of 15.6% is obtained by averaging all 80 test repetitions of each image. The paper states this in Section 4.1 ("We averaged all EEG repetitions of one image to ensure the signal-to-noise ratio") and provides per-repetition curves in Fig. 4B (10 repetitions → 9.9% top-1, 30.1% top-5). However, the abstract, contributions, and main performance discussion present the 80-repetition numbers without qualification. For a BCI-oriented method, single-trial or few-trial performance is the practically relevant metric, and the current framing overstates what the method can achieve from brief signals. **This is a presentation/framing issue, not a methodological flaw**, but it is significant enough that the abstract and highlights should clearly state the number of repetitions used.

2. **Insufficient external baselines to support the "state-of-the-art" claim.** The only external method compared is BraVL (Du et al. 2023), originally designed for fMRI decoding. No supervised baseline is provided (e.g., training a linear classifier on EEG features and testing zero-shot via nearest-class-mean to image features). No alternative self-supervised approach applied to EEG (e.g., SimCLR or BYOL trained on EEG alone) is compared. While the internal ablations are thorough, the paper's claim that cross-modal contrastive learning is the key driver of performance is not directly tested against a supervised counterpart. The comparison against BraVL is valid and shows clear improvement, but the absence of these baselines limits the strength of the broader claims about the framework's necessity.

### Minor

1. **Multiple-comparison correction not reported in electrode ablation.** Figure 2C reports six p-values from the electrode-region ablation (occipital, temporal, parietal, central, frontal, full set) without any adjustment (Bonferroni, FDR, etc.). While this is an exploratory analysis, the absence of correction weakens the statistical rigor of the biological claims.

2. **TSConv does not significantly outperform EEGNet.** In Table 3, TSConv achieves 13.8% top-1 vs. EEGNet's 13.1%, a 0.7% difference that is not significant (p > 0.05, as stated on line 323). The paper acknowledges this but still claims TSConv "outperformed these methods" unconditionally. The claim should be qualified to reflect that TSConv's advantage over EEGNet is not statistically significant.

3. **Key biological analyses lack cross-subject representation.** The topographies (Fig. 2A) and time-frequency maps (Fig. 2D) are shown for a single subject only. The RSA matrix (Fig. 3A) is averaged across 10 subjects without showing individual variability or confidence intervals. While aggregating is understandable for space, the paper would be stronger by reporting across-subject consistency or providing individual examples in supplementary material.

4. **Data-subset selection for Fig. 4A is underspecified.** The paper reports accuracy when using 25%/50%/75%/100% of image conditions but does not state how the subset of conditions was chosen (random? stratified by category?). This matters because non-random selection could bias the curve's shape.

### Trivial

None.

## Nice-to-Haves

- Report the learned temperature parameter τ's final value, as it is listed as a learned parameter in Algorithm 1.
- If practical, report results with 1 trial (no averaging) or with a small number like 5 trials, to establish the lower bound of the method's capability.
- Consider adding a supervised linear-probe baseline (train classifier on 1654 training classes via cross-entropy, then test zero-shot transfer to 200 unseen classes using feature similarity) to directly test whether the contrastive alignment adds value over standard supervised learning.
- Quantify the Grad-CAM analysis (Fig. 4C) by computing the correlation between attention weights and known functional regions (occipital/temporal) across subjects rather than showing a single qualitative example.

## Removed Points

*These points were identified in the reviews but do not belong in the final assessment for the following reasons:*

- **Reproducibility / multiple seeds**: The harsh critic requests reporting results over multiple seeds for each subject. Across-subject standard deviation is already reported; within-subject run-to-run variance is not standard for this type of EEG decoding benchmark where each subject is treated as a single run. Reproducibility is not a core weakness here.
- **Detailed hyperparameter sensitivity**: Requests about initialization/range of learned temperature, sensitivity to batch size, etc., are standard nitpicks that apply to nearly all deep learning papers and do not threaten the paper's claims.
- **False negatives in contrastive loss**: The concern about images of the same concept inadvertently paired as negatives is speculative; the training set has 1654 distinct concepts with 10 images each, and the paper states images appear in "pseudo-randomized order." Without evidence of a concrete problem, this is not a verifiable weakness.
- **Clinical interpretability / BCI practical feasibility**: The paper's scope is demonstrating feasibility of EEG-based zero-shot object recognition, not deploying a clinical BCI. Criticizing the absence of a deployment strategy is scope creep.
- **Formatting/style nitpicks**: Notes about Eq. 1's Softmax dimension, Table 1's Dimension column notation, and the description of "original data" in the Grad-CAM section are minor presentation issues introduced or amplified by the PDF-to-text parsing and do not affect the paper's scientific content.
- **ResNet pre-training performing worse**: The paper already provides a plausible explanation (distribution mismatch between ImageNet-1k and the EEG dataset's image stimuli) on line 334. This is adequately addressed.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. **Reveal the repetition count in the abstract.** Change "achieves state-of-the-art results ... with a top-1 accuracy of 15.6%" to "achieves state-of-the-art results (top-1 accuracy of 15.6% when averaging 80 test-trial repetitions; 9.9% with 10 repetitions)." This single change would eliminate the most significant framing issue.

2. **Add a supervised baseline.** Train a linear classifier on the EEG features from the 1654 training classes using cross-entropy loss, then evaluate zero-shot transfer to the 200 test classes by comparing test EEG features to image-feature prototypes. This directly tests whether the contrastive alignment is the key to the improvement or whether the EEG encoder itself carries sufficient discriminative information.

3. **Clarify that TSConv's advantage over EEGNet is not statistically significant** in the text, and avoid the unqualified claim that TSConv "outperformed these methods."

4. **Report individual subject RSA matrices** or provide a supplementary figure showing subject variability, so readers can assess whether the semantic clustering pattern is consistent.

---
