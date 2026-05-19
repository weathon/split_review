- Decision: Reject
- Avg Score: 5.67
- Scores: 5, 6, 6
Now I have all the information needed to produce a thorough, verified review.

## Summary

This paper presents MedJourney, a method for counterfactual medical image generation that learns from multimodal patient journeys. Given two chest X-rays from different time points, it uses GPT-4 to synthesize natural-language progression descriptions from the corresponding reports, creating training triples (prior image, progression description, new image). These triples are used to fine-tune a latent diffusion model conditioned on both a prior image and a text instruction. The paper introduces a two-stage curriculum that first pretrains on abundant single image-text pairs before instruction-tuning on counterfactual triples. Experiments on MIMIC-CXR report substantial improvements over RoentGen, InstructPix2Pix, and Stable Diffusion on a composite CMIG score.

## Strengths

- **GPT-4-based scalable pipeline for generating instruction-following data from real patient journeys.** Section 3 and Figure 2 detail the process: GPT-4 takes two radiology reports (Impression sections) at different time points and produces a clean, natural-language progression description. This yields 9,354 training triples automatically, solving the key bottleneck of missing annotated instruction data in the medical domain. The ablation (Table 2) confirms that GPT-4 descriptions consistently outperform using raw Impressions across all settings.

- **Substantial quantitative improvement over prior methods on a multi-faceted evaluation.** Table 1 shows MedJourney achieves a CMIG score of 83.23 versus RoentGen at 66.08, InstructPix2Pix at 42.12, and Stable Diffusion at 18.14. The gains are largest on race AUC (97.22 vs. 84.71) and age Pearson correlation (79.38 vs. 28.91), where conditioning on the prior image is essential. These large margins are not attributable to metric quirks — the advantage is consistent across all three component metrics.

- **KL divergence analysis provides a diagnostic insight that strengthens the paper's reliability claims.** Table 4 reports MedJourney has a KL divergence of 10.9 vs. RoentGen's 40.74 (vs. the real reference distribution). The paper explicitly identifies (lines 445-447) that the pathology classifier used for evaluation may not perform equally across all categories and that this confound could inflate prior methods' reported accuracy. By showing that MedJourney's images are much closer to real image distributions, the paper argues its own evaluation is likely more trustworthy — a thoughtful self-critique that strengthens, rather than weakens, the paper.

- **Segmentation concordance analysis demonstrates anatomy preservation.** Table 5 (Dice score 81.05 for MedJourney vs. 74.04 for the prior-to-reference alignment and 67.38 for RoentGen) provides additional evidence that the model preserves anatomical layout while executing prescribed changes, using a separate segmentation model independent of the evaluation classifiers.

## Weaknesses

### Fatal

None.

### Major

- **The two-stage curriculum learning benefit is not well-supported by the ablation evidence.** The paper frames the two-stage curriculum as a core contribution (abstract: "we introduce a two-stage curriculum that first pretrains…and then continues training"). However, Table 2 shows that with registration (the setting used in the final model), two-stage improves CMIG from 82.83 to 83.23 — only 0.4 points. Without registration, two-stage actually *hurts* performance (76.38 vs. 80.76). The paper's own narrative in Section 5.2 acknowledges this ("without registration, two-stage training actually produces worse results"). The marginal improvement does not justify the prominence given to this design choice. Reframing the curriculum as a minor ablation detail rather than a central contribution would better match the evidence.

- **The image registration method is not described.** Section 3 (Dataset) contains the paragraph title "\paragraph{Image registration.}" with absolutely no content following it (line 135). Registration has a substantial effect on results (Table 2: ~6-8 point improvement on race AUC), yet the reader cannot tell what method was used (affine? deformable? which tool/library?), what parameters were used, or how the registration score threshold for filtering was set. This is a critical reproducibility gap.

### Minor

- **The CMIG geometric mean can break with negative age correlations.** The CMIG score is computed as sqrt(pathology_AUC × sqrt(race_AUC × age_corr)). Pearson correlation can be negative, in which case sqrt(race_AUC × negative) is undefined. While all reported age correlations are positive (ranging from 2.73 to 79.38), the metric formula has an inherent fragility that should be addressed — e.g., by taking absolute values, adding a constant shift, or using a different aggregation. This is a design issue with the evaluation framework itself.

- **No confidence intervals or statistical significance for any result.** Comparisons in Tables 1 and 2 involve differences as small as 0.4 points (82.83 vs. 83.23). Without error bars, confidence intervals, or significance tests, it is impossible to determine whether these differences are meaningful or within noise. This is especially important for the two-stage vs. one-stage comparison given it supports a core narrative claim.

- **The Dice score table (Table 5) has an unclear reference baseline.** The row labeled "Reference Image" shows Dice 74.04, while MedJourney achieves 81.05. The table caption says "segmentation concordance between reference and counterfactual," but it is not obvious what "Reference Image" as a counterfactual means (likely the Dice between prior and reference segmentation, showing natural anatomical shift over time). This needs clarification to avoid misinterpretation.

### Trivial

- Line 297 has a typo: "\paragraph{Baseline systems.}" and line 293 has "\paragraph{Implemetantion details.}"

## Nice-to-Haves

- **A medical-domain fine-tuned InstructPix2Pix baseline.** The paper compares against off-the-shelf IP2P (general domain), which is a weak comparison. Fine-tuning IP2P on the same MIMIC-CXR triples would isolate the benefit of the specific design choices (BiomedCLIP, two-stage curriculum, registration). The gap between fine-tuned IP2P and MedJourney would more cleanly demonstrate the contribution of these components.

- **Full GPT-4 prompt details.** The prompt is shown in a figure (Figure 3), but temperature, max tokens, system prompt, and any post-processing steps are not reported.

- **Data filtering threshold specification.** The paper states pairs are "filter[ed] out … for which the registration score is below a threshold" (line 136) without reporting the threshold value.

## Removed Points

These points from the reviewers are removed for the following reasons:

- **"Evaluation metrics do not measure what they claim" — pathology AUC confound**: The paper *already acknowledges* this confound in Section 5.3.1 (lines 445-447) and provides KL divergence analysis showing MedJourney's images are closer to real distributions, mitigating the concern rather than ignoring it. The claim that results are "non-interpretable" is disproportionate given the paper's own diagnostic analysis.

- **Race AUC is "highly contested"**: This is a general concern about race prediction from chest X-rays, not a specific problem with this paper's methodology. Using the Gichoya 2022 classifier as a proxy for feature retention is standard practice in the field. The criticism is speculative and lacks a concrete anchor in the paper.

- **"CMIG score ad hoc, designed to produce a winning number"**: Speculative assertion without evidence. The geometric mean is a reasonable aggregation choice and is justified ("robust to results of varying scales"). The critic provides no alternative or specific evidence that the metric was cherry-picked.

- **"No method that actually conditions on the prior image is compared"**: Factually incorrect. InstructPix2Pix (IP2P) is an image-editing model that takes a prior image and instruction. The paper explicitly compares against it.

- **"Dice score red flag (reference image scores lower than generated)"**: Misunderstands the table. The "Reference Image" row (74.04) likely reflects the Dice between prior and reference segmentation (natural anatomical variation over time). MedJourney's 81.05 means the generated image is *more* aligned with the reference than the prior was — a positive result. The table labeling is unclear but the interpretation is not a flaw.

- **"Hallucinations reveal brittleness"**: The paper transparently discusses hallucinations and their fixes (data cleaning, resolution matching). This is good scientific practice, not a weakness.

- **"No human evaluation"**: Scope creep. Extensive quantitative evaluation is the standard for this type of work at top venues. Human studies for plausibility are not a prerequisite for acceptance.

- **"KL divergence presented without context"**: The table caption explicitly says "lower the better" (line 413). KL divergence is a standard, well-understood metric. The context is sufficient.

- **Missing hyperparameters**: The paper reports learning rate (1e-4), batch size (32), epochs (200+128), GPU setup (8×A100), optimizer (AdamW), and data augmentation. This is above-average detail for a conference paper.

- **Missing related works**: Cannot be cited without external verification.

## Novel Insights

The harsh critic's observation about the two-stage curriculum — that the paper's own ablation data shows it provides only marginal benefit over one-stage training with registration — is the most substantive finding. The paper frames the curriculum as a central contribution, but Table 2 tells a different story: one-stage + registration achieves 82.83 CMIG, and adding two-stage pushes it to 83.23 (Δ=0.4). Meanwhile, without registration, two-stage is actively harmful (76.38 vs. 80.76). This pattern, combined with the missing registration method description, suggests that the registration preprocessing — not the two-stage curriculum — is the primary driver of success. The paper would be well-served by acknowledging this more directly and either strengthening the evidence for the curriculum or reframing it as an optional enhancement rather than a key contribution.

## Suggestions

1. Replace the empty "Image registration" paragraph with a concrete description of the registration method (affine/deformable? tool? parameters?).
2. Add confidence intervals or error bars to all main results (Tables 1 and 2) so readers can assess the reliability of small-margin comparisons.
3. Address the CMIG geometric mean fragility: add a small constant to age correlation before taking the square root, or use absolute values, or switch to a different aggregation that handles negative values gracefully.
4. Reframe the two-stage curriculum as a minor improvement (or strengthen the evidence by including a "no pretraining at all" baseline that shows clear overfitting).
5. Release source code and trained models as promised.
6. Clarify the "Reference Image" row in the Dice score table.
