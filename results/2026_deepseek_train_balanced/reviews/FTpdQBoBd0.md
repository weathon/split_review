## Summary

This paper diagnoses why direct fine-tuning of Stable Diffusion on specialized datasets underperforms, identifying through CLIP-based metrics that fine-tuning fails to substantially improve text-image alignment or reduce alignment drift. It then proposes a contrastive generation framework that directly optimizes text feature representations during training to address both issues. Experiments on CUB (200 bird species) and Oxford Flowers (102 flower categories) show large quantitative improvements over standard fine-tuning and the unfine-tuned model across FID, Inception Score, and linear classification accuracy.

---

## Strengths

1. **Novel diagnostic framework analyzing why fine-tuning underperforms.** The paper introduces text-image alignment (measured by CLIP contrastive loss) and text-image alignment drift (measured by Fréchet distance between text/image feature changes) as interpretable indicators. Figure 2b provides direct evidence that standard fine-tuning (SD-FT) barely improves alignment over the unfine-tuned model, and Figures 3–4 visually show that alignment drift of fine-tuned models remains far from real-data distributions. This goes beyond prior work that focuses solely on final generation quality without analyzing *why* direct fine-tuning is limited.

2. **Large-margin quantitative improvements.** On the non-captioned CUB* benchmark, the method reduces FID from 52.94 (SD) / 41.34 (SD-FT) to 26.70 and lifts linear classification accuracy from 42.15% / 56.46% to 74.72%. On Oxford Flowers*, FID drops from 44.24 / 37.78 to 25.35 and accuracy rises from 78.53% / 79.19% to 91.69%. These are substantial gains that clearly demonstrate the approach's effectiveness within its tested scope.

3. **Principled adaptation of contrastive learning to captionless multi-category datasets.** The category-level contrastive formulation (Equation 4) correctly treats all image-text pairs within a category as mutual positives, and the paper validates this on both captioned and captionless settings. The prompt design leveraging tokenizer properties (category index + 50,000 as a hint) is a clever and practical engineering contribution that avoids the impracticality of per-category rare tokens for datasets with many classes.

4. **Resource efficiency.** Training takes only 5 epochs (~3 hours on a single A100 GPU for CUB with 200 classes), making the method accessible to researchers with limited compute.

---

## Weaknesses

### Major

1. **No comparison against methods practitioners would actually use.** The paper compares only against unfine-tuned SD and standard full fine-tuning (SD-FT). The Related Work section discusses Dreambooth (dismissed for multi-class scenarios), LoRA (mentioned only for computational efficiency), and controllable generation methods — yet none are evaluated. LoRA, in particular, is a widely used baseline for fine-tuning text-to-image models on specialized data and can handle multi-class datasets at a similar parameter budget to the proposed approach. Without comparing against LoRA or similar methods (e.g., Custom Diffusion adapted to multi-class), the paper cannot substantiate its central claim that the method *improves fine-tuning performance* in any practically meaningful sense — only that it improves over doing nothing or standard full fine-tuning. This undermines the practical claim the paper is built on.

2. **The total training objective is never specified.** The paper describes a contrastive loss (L_ctr) in detail but never writes down the full loss function that is actually optimized. The ablation study varies a balancing coefficient λ (Table 3), and line 145 mentions a "contrast coefficient of 0.1," but the equation for the total loss — presumably L_total = L_diffusion + λ·L_contrastive — is never stated. The diffusion denoising loss itself is not defined. Since the method hinges on the interaction between these two objectives, this is a basic reproducibility failure.

3. **Uncontrolled architectural modification confounds the comparison.** Line 145 states: "We replace the text encoder without projection layers in SD with a text encoder that has projection layers." The SD-FT baseline presumably uses the original text encoder without projection layers. This means the comparison conflates two changes: the contrastive loss *and* an architectural change (adding projection layers). Improved performance could partly stem from the additional expressivity of the projection layers. This must be addressed — either by matching the architecture across baselines or by ablating the projection layer separately.

4. **Narrow evaluation scope relative to the claims.** The method is tested on exactly two datasets (CUB and Oxford Flowers), both fine-grained classification datasets with centered subjects on simple backgrounds. The abstract describes the approach as "versatile," but there is no evaluation on face datasets, architectural-style datasets, or datasets with complex scenes — precisely the kinds of "specialized datasets" the paper evokes. Only one training budget (5 epochs, batch size 24, one learning rate) is tested. While the results within this scope are strong, they do not support claims of generality or versatility.

### Minor

5. **The alignment drift analysis (Figures 3–4) lacks quantitative support.** The paper uses t-SNE visualizations and contour plots to argue that the proposed method's alignment drift closely resembles real data, while standard fine-tuning's does not. No quantitative distributional metrics (e.g., Wasserstein distance, KL divergence) are provided to support this visual claim. The visual patterns are suggestive but not a substitute for measurement.

6. **No error bars or multiple-seed results.** No confidence intervals, standard deviations, or multi-seed averages are reported for any metric. Given the moderate dataset sizes (200 and 102 classes) and short training schedules, variance could be meaningful.

7. **Prompt design not isolated as a confounding factor.** The proposed method uses a custom prompt format ("[id of class] + 50000, a photo of [class]"). It is unclear what prompt format was used for the SD-FT baseline. If the baselines used a different or less effective prompt, the comparison is unfair. The paper does not ablate whether the prompt design alone (without contrastive loss) contributes to the improvement.

### Trivial

8. **Equation (4) has notational errors.** The denominator in the second term writes ∑_{i=1}^{N} exp(sim(v_i, t_j)/τ) where it should be ∑_{j=1}^{N} to match the standard notation. The numerator also reuses the index variable v_s ambiguously. While the conceptual idea is clear, the equation as written is formally incorrect.

---

## Nice-to-Haves

- Ablate the effect of the projection layer addition separately from the contrastive loss, to establish which component drives the gains.
- Compare against at least one competitive baseline (LoRA is the most natural candidate).
- Test on at least one non-fine-grained dataset (e.g., a face dataset or architectural-style dataset) to support claims of versatility.
- Provide quantitative distributional metrics (Wasserstein distance or similar) for the alignment drift analysis, supplementing the t-SNE/contour visualizations.
- Report results with multiple random seeds to establish statistical reliability.
- State the total loss function explicitly: L_total = L_diffusion + λ·L_contrastive (or the actual form used).

---

## Removed Points

These points were raised by reviewers but removed after verification against the paper:

- *"Figure 1 is not readable as text"* — parser artifact, not an author error.
- *"Missing discussion of Custom Diffusion, Textual Inversion"* — rule against citing missing related works.
- *"Section 2 fine-tuning protocol insufficiently described"* — line 50 explicitly states that fine-tuning refers to jointly optimizing UNet and text encoder, and Section 5 provides experimental details. The critic's concern about an "insufficiently tuned baseline" is speculative.
- *"Causality not established between alignment metrics and generation quality"* — the correlation analysis in Figure 2a is presented as suggestive evidence, not causal proof. Demanding strict causal intervention exceeds the standard for empirical ML papers and would not invalidate the method's demonstrated effectiveness.
- *"The paper does not control for CLIP encoding of generated images"* — this concern is circular with respect to the alignment measure; if generated images are poorly encoded by CLIP, that is itself evidence of poor alignment, not a confound.
- *"Grammatical/formatting issues"* — parser artifacts, not author errors.
- *"Missing appendix content"* — parser strips supplementary material from all papers.

---

## Novel Insights

None beyond the paper's own contributions. The reviews surface no genuinely novel observation that the paper itself does not make. The contrastive-generation-plus-diagnostic perspective is the paper's own contribution, and the reviewers' main insights are about experimental gaps rather than new research directions.

---

## Suggestions

- **Most important:** Add LoRA as a baseline comparison. This single addition would substantially strengthen the paper's practical claims and is relatively low-effort to run. If the proposed method outperforms LoRA at a similar parameter budget, the contribution becomes clearly meaningful.
- Address the projection-layer confound by either (a) adding projection layers to the SD-FT baseline as well, or (b) ablating the method without projection layers.
- Write the total loss function explicitly in the paper.
- Run at least one additional dataset with different characteristics (e.g., faces, scenes) and report multi-seed statistics.

---

## Score and Decision

**Score:** 5.0  
**Decision:** Reject

**Rationale:** The paper has genuine contributions — the diagnostic framework is novel, and the contrastive generation approach yields impressive results on the two tested datasets. However, the experimental validation has fundamental gaps that prevent acceptance at a top venue like ICLR. The absence of comparisons against methods practitioners actually use (LoRA, etc.), the uncontrolled architectural modification, the unspecified total loss function, and the narrow two-dataset evaluation collectively mean the paper's central claims are insufficiently supported. The contributions are real but the evidence is too thin. A substantially strengthened version (added baselines, broader evaluation, resolved confounds) could be competitive.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>