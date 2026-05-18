Now I have sufficient information. Let me produce the final consolidated review.

## Summary

This paper proposes an end-to-end framework for learning semantic segmentation from both positive (target object) and negative (background/complementary) coarse annotations. The method uses two coupled CNNs — one estimating true segmentation probabilities, the other modeling per-pixel confusion matrices to characterize annotation noise — plus a complementary label learning branch with a transition matrix. The core idea (jointly modeling positive and negative coarse annotations via noise modeling) is novel and well-motivated by practical annotation scenarios.

## Strengths

1. **Novel combination of positive and negative coarse label learning for segmentation.** The paper is the first to simultaneously exploit both objective and complementary coarse annotations within an end-to-end noise-modeling framework (Section 1, "We introduce the first instance of an end-to-end supervised segmentation method that estimates true segmentation labels from noisy coarse annotations"). Prior WSL methods for segmentation typically use only one type of weak annotation (scribbles, boxes, etc.) without explicitly modeling both sides.

2. **Principled probabilistic formulation.** The method is grounded in a probabilistic model (Section 3.2) that factorizes the likelihood over pixels and annotation types, uses per-pixel confusion matrices to capture spatially-varying noise, and incorporates trace regularization (borrowed from Tanno et al. 2019) to address the identifiability issue between the true label distribution and the noise process.

3. **Robustness to very low-quality coarse annotations.** The paper investigates sensitivity to coarse annotation quality (Section 4.5, Figs. 3–5) and reports that performance improves gracefully as coarse annotation area increases, with the method functioning even at scribble-level ratios (0.01). On the LES-AV retinal dataset with real coarse annotations, the method achieves results "comparable to the strongly-supervised method" (Section 4.6). This is a practically important property.

## Weaknesses

### Fatal

None.

### Major

1. **Key quantitative results are absent from the main paper body.** The abstract and introduction promise quantitative comparisons, but the main paper contains no tables reporting mIoU or Dice scores against baselines on Cityscapes, MNIST, or the retinal dataset. The only concrete numerical claims ("improved 3%," "comparable to strongly-supervised") reference Table S2 in the supplementary material, which the parser strips. A methods paper claiming state-of-the-art performance must present its central quantitative comparisons in the main paper body — figures showing sensitivity curves are not a substitute for structured comparison tables. Without seeing the actual numbers against baselines, the paper's core claim is unverifiable from the main text alone.

2. **Critical architectural and algorithmic details are underspecified.** Several aspects of the method are insufficiently described:
   - The coarse annotation network that outputs 4D pixel-wise confusion matrices (W×H×L×L) is described only as "a CNN" — no architecture, layer design, or forward pass is specified (Section 3.2).
   - The transition matrix **M** for complementary labels (Section 3.3) is introduced with diagonal zeros, but it is never stated whether **M** is learned jointly, fixed a priori, or derived from data. The paper says "adding a linear layer" but does not specify how this matrix is obtained or updated during training.
   - Training details (optimizer, learning rate, batch size, number of epochs, loss weight λ, initialization strategy) are entirely absent from the main text.

### Minor

1. **Experimental comparisons are not controlled for annotation type.** The paper compares against methods using fundamentally different weak annotations (scribbles: ScribbleSup, CycleMix; bounding boxes: BoxSup, L2G; image-level labels) rather than the paper's positive+negative coarse annotations (Section 4.3). While cross-annotation-type comparison is common in the WSL literature, the paper does not explain how baselines were adapted to the same annotation budget, making it difficult to attribute performance differences to the method rather than the annotation format.

2. **No error bars or variance measures.** Given claims about robustness to annotation quality and state-of-the-art performance, the lack of any error bars, confidence intervals, or multi-run statistics weakens the empirical support (especially with only 4 test images for the retinal dataset, Section 4.1).

### Trivial

- Section 4.4 ("SEGMENTATION PERFORMANCE") appears truncated in the extracted text. If this is a parser artifact it is not the authors' fault, but the section as visible contains almost no content.

## Nice-to-Haves

- An ablation study explicitly comparing positive-only, negative-only, and combined supervision (mentioned as planned in Section 4.3 but results not shown in main text).
- Clarification of how the method scales with multiple coarse annotations per image from different annotators.
- Position the "first instance" claim more carefully with respect to Zhang et al. (2023), which the paper cites and which also uses per-pixel confusion matrices for segmentation.

## Removed Points

- **Trace regularizer "error" (Harsh Critic #2, third bullet).** The critic claims the paper's interpretation of the trace regularizer is inconsistent. This is incorrect. The paper states: "minimizing the trace encourages the estimated annotators to be maximally unreliable." Since trace(A) = ∑ⱼ p(ỹ=j|y=j), minimizing trace does indeed push correct-label probabilities toward zero, making the annotator unreliable — exactly as the paper states. The cross-entropy term then ensures fidelity to observed labels, and the combination disentangles true labels from noise, following Tanno et al. (2019). No error exists.

- **"Paper never explains how the model handles images that lack one type of annotation" (Harsh Critic, Other Observations).** The paper explicitly addresses this: "the model works even for every image x annotated by only one category of coarse annotations" (Section 3.1) and the loss functions (Eq. 4, Eq. 9) include indicator functions 1(o ∈ S(xₙ)) and 1(c ∈ S(xₙ)) that handle missing annotation types.

- **"MNIST no quantitative or qualitative result is shown."** The paper references figures (Figs. 3, 4) that contain results from MNIST experiments. Section 4.4 appears truncated by the parser; the original submission likely contains the referenced results.

- **Reproducibility nitpicks about missing hyperparameters being fatal.** Training details (optimizer, learning rate, etc.) are absent, which is a genuine weakness but belongs in Minor, not as a fatal issue, as these can be addressed in revision.

- **"First instance" claim should be softened.** This is a matter of scholarly tone, not a substantive weakness. The paper cites relevant prior work and positions its novelty as the specific combination of positive+negative coarse annotation learning.

## Novel Insights

The Harsh Critic's observation that the method cannot be properly evaluated because quantitative results are deferred to supplementary is the most severe issue — it transcends ordinary presentation nitpicks and goes to whether the paper's core claims are supported. However, the critic overreaches in claiming the trace regularizer is conceptually wrong (it is not) and in treating the deferred-results problem as fatal rather than a major presentation gap. The Strength Finder correctly identifies the novelty of jointly handling positive and negative coarse annotations, but its claimed strengths about "consistent and significant improvement" cannot be verified from the main text alone — a tension the Critic correctly identifies.

## Suggestions

1. Move (at minimum) one full comparison table (mIoU on Cityscapes val, DICE on LES-AV) from supplementary into the main paper body. This is the single highest-leverage change.
2. Specify the coarse annotation network architecture (backbone, output layers, how the 4D CM tensor is produced) and state whether **M** is learned or fixed.
3. Add training hyperparameters (optimizer, learning rate, batch size, epochs, λ value) to the experimental set-up section.
4. Add error bars or note the number of independent runs for key experiments.

## Score and Decision

The paper presents a genuinely novel idea — jointly modeling positive and negative coarse annotations via per-pixel confusion matrices and complementary label learning — with a principled probabilistic formulation. However, as submitted, the experimental section does not provide sufficient evidence to verify the claimed state-of-the-art performance. The main paper body lacks quantitative comparison tables, critical architectural details are underspecified, and training hyperparameters are absent. These are fixable issues, but the paper in its current form does not meet the evidentiary standard required for acceptance.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>