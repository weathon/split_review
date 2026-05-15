Now I will write the consolidated final review.

## Summary

This paper investigates two well-known phenomena in contrastive vision-language models (VLMs)—the modality gap and object bias—and argues that both are triggered by an information imbalance between images (information-rich) and captions (information-sparse). The authors introduce two new metrics (RMG for the modality gap, MOAD for object bias), conduct a large-scale correlational study across 98 off-the-shelf VLMs, create a fully-controllable synthetic dataset (MAD) for causal intervention, and present experiments on real data (CC12M) to support their hypothesis. Key findings include that only a few embedding dimensions drive the modality gap, that object bias stems from per-sample caption prevalence rather than global word frequency, and that reducing information imbalance shrinks both the gap and the bias while improving accuracy.

## Strengths

1. **Clean synthetic dataset (MAD) enabling causal intervention.** The construction of a fully-controllable dataset based on Morpho-MNIST, where caption content can be varied precisely while keeping images fixed, is a major methodological contribution. This allows the authors to manipulate information imbalance in an otherwise confounding-free setting, providing the cleanest evidence available for the hypothesized causal link (Section 6.1, Figure 6).

2. **Large-scale correlational analysis across 98 VLMs.** The study of modality gap vs. performance across a diverse set of pre-trained models (CLIP, SigLIP, etc.) trained on various datasets, along with the explicit treatment of confounders (model size, embedding size, dataset size), provides the most comprehensive empirical characterization of the gap–performance relationship to date (Section 4.1, Table 1, Figure 2). The finding that the naive positive correlation reverses after controlling for confounders resolves prior controversy.

3. **Novel, principled metrics (RMG and MOAD).** The Relative Modality Gap (RMG, Equation 2) addresses a known limitation of the standard L2M measure by accounting for intra-modality spread, and the Matching Object Attribute Distance (MOAD, Section 5) formalizes "object bias" beyond simple accuracy differences, enabling cleaner analysis. MOAD's generic formulation extends naturally to other bias types.

4. **Demonstration that object bias stems from per-sample caption prevalence, not global word frequency.** The analysis of LAION-2B captions (Figure 5a) disproves the intuitive explanation that objects are simply more frequent words, and the controlled MAD experiment (Figure 5b) elegantly shows that the factor always present in the caption (whether object, color, or thickness) always becomes the target of bias. This is a clean mechanistic result.

5. **Entropy–gap connection.** The finding that the modality gap provides flexibility for controlling logit entropy (Section 6.2, Figure 7), separate from the temperature parameter, is a genuinely novel insight that reframes the gap from "bug" to potential "feature."

## Weaknesses

### Fatal
None.

### Major

1. **Real-data validation is too narrow to support the generality claimed.** The real-data experiment (Section 6.1) uses a single model architecture (CLIP RN50), a single dataset (CC12M), and a single manipulation strategy (dropping contiguous caption segments). While the paper acknowledges that the synthetic setting avoids confounding factors, the conclusion that "our hypothesis also holds on real data" (line 469) would be substantially stronger with variation across architectures (e.g., SigLIP, different ViT scales), datasets (e.g., YFCC, RedCaps), or manipulation types (e.g., removing random words vs. contiguous segments). The current real-data evidence is consistent with the hypothesis but insufficient to rule out architecture- or dataset-specific explanations.

2. **The claim of a negative correlation after controlling for confounders is deferred to a reference that is absent from the extracted main text.** The paper states "when we control for these factors, we observe the expected negative correlation... (see \cref{sub:fixed_dataset})" (line 188), but this section is not present in the main text (it was in the appendix). While this is a parser artifact, the consequence is that the reader of the main paper cannot evaluate the quality of this critical evidence. This particular analysis is central to the paper's justification that "the modality gap is a problem worth fighting," yet its evidential basis is opaque in the main narrative. The authors should either move this analysis to the main paper or provide a clear summary of the controlled results.

### Minor

1. **The object bias trend under high information imbalance is not fully reconciled with the paper's mechanistic story.** The synthetic experiment's sub-caption (line 398) notes "Larger information imbalance (fewer attributes) → larger gap & smaller bias," and panel (II) of Figure 6a shows object bias decreasing when the caption is most impoverished. The main text (lines 457, 471) consistently states that reducing imbalance reduces both gap and bias, which is the opposite of a monotonic relationship. While this can be explained (e.g., when almost no attributes are in captions, the model cannot develop differential sensitivity to attributes, making MOAD appear small), the paper does not provide this explanation or discuss the non-monotonicity, leaving an apparent tension between the figure and the text's narrative.

2. **The entropy experiment (Section 6.2) is correlational and confounded.** The finding that models with frozen temperature increase the gap more than those with learnable temperature to achieve similar entropy is consistent with the proposed explanation, but alternative explanations exist (e.g., training dynamics differ when temperature is frozen in ways unrelated to entropy control). The paper partially acknowledges this (footnote on lines 488–490) but the caveat is easy to miss and the presentation otherwise implies a causal interpretation.

3. **The text encoder's object bias is acknowledged but not explained within the information imbalance framework.** The paper notes that text encoders also exhibit some object bias (though smaller than image encoders) and suggests this is because the text encoder "can simply encode the entire information" (line 357). However, if the text encoder has access to all information, it should show zero bias, not a smaller bias. Possible explanations (e.g., weight sharing in early layers, training dynamics, or repeated caption patterns across samples) are not explored. This does not invalidate the core claim, but it leaves the mechanistic account incomplete.

4. **The Kendall-τ neighborhood analysis (Table 2) lacks a baseline.** The reported values (0.34–0.51) are described as indicating "dissimilar neighborhoods," but no reference point is provided (e.g., what value would random embeddings produce? What value indicates "similar" neighborhoods?). Without calibration, the reader cannot assess whether these distances are large or small.

### Trivial
- The neighborhood analysis (Table 2) would benefit from a baseline for interpretation.

## Nice-to-Haves
- **Reverse-direction tests** (e.g., making images less informative by adding noise or removing patches while keeping captions intact) would strengthen the causal claim, but are not required given the paper's explicit scope on the real-world regime where images are more informative than captions.
- **Validation of RMG** against L2M on tasks where the "true" gap direction is known (e.g., on synthetic data) would strengthen the metric's case.
- **Examples of embedding dimensions removed** in the ablation experiment (Section 4.2) with concrete image-text pairs would improve interpretability.

## Removed Points

These points were removed per the review guidelines (see below for justifications). They are listed here for traceability but were not included in the assessment.

- **Criticism about the controlled analysis (sub:fixed_dataset) not being shown in the main text.** The subsection was in the appendix, which the parser stripped from the extracted text. Per the established rules, parser-stripped sections are not author errors. This is a presentation concern, not a missing analysis. *(Handled as Major weakness #2 above in modified form.)*
- **Criticism that the causal claim is unsupported because the reverse direction (images less informative than captions) was not tested.** The paper's domain is specifically the real-world setting where images are more informative than captions. Testing the reverse imbalance would test a different scenario and is scope creep. The paper provides causal evidence in the direction it claims (manipulating caption informativeness while keeping images fixed).
- **Criticism about text encoder bias being "inconsistent" with the framework.** The paper explicitly acknowledges the text encoder shows smaller bias (lines 357–358, 460) and provides an explanation: the text encoder knows what to encode, whereas the image encoder must model uncertainty. That the text encoder shows *some* bias is not a contradiction—the claim is that the bias is *larger* for the image encoder, which the data support.
- **Formatting/style nitpicks** about metric validation or baseline calibration. These are addressed as minor weaknesses where substantive.
- **Criticism about missing related works.** Per guidelines, I cannot verify the existence of missing references.

## Novel Insights

The most interesting observation to emerge from synthesizing the reviews is that the paper's own synthetic data (MAD) produces a more complex relationship between information imbalance and object bias than the paper's headline narrative suggests. The figure indicates that object bias (as measured by MOAD) can *decrease* under extreme imbalance (very few attributes in captions), even as the modality gap grows. This suggests that object bias and the modality gap, while both causally linked to information imbalance, may respond to it through different mechanisms and at different thresholds. The modality gap appears to respond monotonically to imbalance (more imbalance → larger gap), while object bias may follow a U-shaped or thresholded pattern. This nuance—which the paper acknowledges in the figure but does not fully discuss—could open a more refined research program: instead of "imbalance causes both," the true relationship may be that a *moderate* imbalance is most conducive to object bias, while extreme imbalance simply makes both modalities encode poorly. This insight is not present in the paper itself and emerges from cross-referencing the reviews with the paper's own data.

## Suggestions

1. **Move or summarize the controlled correlation analysis** (currently in the appendix as `sub:fixed_dataset`) into the main paper, since it is central to the claim that the modality gap is worth fighting. At minimum, include a table or clear statement of the partial correlation coefficients after controlling for confounders.

2. **Broaden the real-data validation** by repeating the CC12M experiment on at least one additional dataset and one additional architecture (e.g., SigLIP ViT-B/16). This would substantially increase confidence in the generality of the information imbalance hypothesis.

3. **Discuss the non-monotonic relationship** between information imbalance and object bias observed in the synthetic data (Figure 6a, panel II). A brief explanation of why extreme imbalance can reduce MOAD values (e.g., because the model ceases to differentiate attributes at all) would resolve the apparent tension between the figure sub-caption and the main text's narrative.

4. **Include a baseline for the Kendall-τ neighborhood distances** (e.g., expected distance for random embeddings) in Table 2 so readers can interpret the reported values.

5. **Provide a brief discussion of why the text encoder exhibits any object bias** despite the information imbalance hypothesis predicting it should have full information. Even a speculative paragraph pointing to weight-sharing, initialization dynamics, or caption repetition would strengthen the mechanistic account.

## Score and Decision

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>