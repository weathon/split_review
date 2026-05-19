- Decision: Reject
- Avg Score: 5.60
- Scores: 6, 5, 8, 6, 3
Now I have all the information needed. Let me produce the consolidated review.

## Summary
This paper proposes a robust novelty detection method that handles style shifts without requiring environment metadata. The approach crafts an auxiliary OOD set by using Grad-CAM to localize core features in ID images, then distorting those regions with hard augmentations. A teacher–student framework with a contrastive loss encourages alignment on ID samples and divergence on OOD samples. The method is evaluated on seven datasets against nine existing methods, reporting up to 12.7% improvement in robust AUROC.

## Strengths

- **Strong and consistent performance gains across diverse benchmarks.** Table 1 reports robust AUROC improvements of up to 12.7% over prior methods on datasets spanning synthetic shifts (Waterbirds, Colored MNIST), industrial defect detection (MVTecAD, Visa), autonomous driving (Cityscapes→GTA5), and medical imaging (Brain Tumor, Camelyon17). This breadth of evaluation directly supports the claim of a general-purpose robust ND solution.

- **Metadata-free approach that outperforms methods requiring environment labels.** The method does not need environment annotations — a practical advantage over RedPanda, PCIR, GNL, and Stylist — yet achieves higher robust performance (e.g., 81.7% vs. RedPanda's 77.3% on Waterbirds). The paper explicitly acknowledges that RedPanda was granted environment labels (Table 1 footnote), making the comparison transparent and fair.

- **Guided OOD crafting without external data or generative models.** The core idea — using Grad-CAM with light augmentations to produce a style-agnostic saliency map, then distorting only high-saliency regions — is novel and principled. The ablation in Table 4 confirms this strategy outperforms alternatives that require generative models (Dream-OOD, GOE) or additional datasets (FITYMI, MIXUP), demonstrating that the design choice is effective beyond its practical convenience.

- **Well-structured ablation study isolating design choices.** Table 3 systematically ablates the auxiliary OOD set, the classification task, the contrastive loss, and the guided crafting strategy. Each removed component degrades performance, confirming that the full pipeline contributes meaningfully.

## Weaknesses

### Fatal
None.

### Major

- **Contradictory description of training set composition undermines reproducibility.** Section 2 contains three inconsistent statements about the training data: (i) "the training set consisted solely of samples from **D**" (line 36), (ii) "we crafted a training set composed of ID samples from both **D** and **D′**" (line 37–38), and (iii) "the ratio of 100:0, used in our main results, represents a scenario where no samples from **D′**_ID are included in the training data" (line 38). The Waterbirds experiment description (line 143) compounds the confusion by explicitly stating that 180 land-birds-with-water-background samples (**D′**_ID) were included in training, which contradicts the 100:0 claim. It is unclear whether different datasets used different mixing ratios and, critically, whether all baselines were trained on the exact same training sets. This ambiguity makes it difficult to interpret the reported gains and to reproduce the results.

- **No variance or statistical significance reported for any result.** The main results (Table 1), ablations (Tables 3–4), and all other quantitative findings are reported as single numbers without confidence intervals, standard deviations, or significance tests. The ablation tables show differences as small as 0.4–1.9% between competing configurations; without variance estimates, it is impossible to assess whether these differences are meaningful or merely noise. Given that the paper's core claim rests on a 12.7% improvement, the absence of any error characterization is a notable gap.

### Minor

- **Theorem 1 provides no practical insight into why the proposed intervention succeeds.** The theorem is a standard uniform convergence bound decomposed into a VC-dimension term and an ℓ₂ distance between A-OOD and real OOD core distributions. The paper acknowledges that this reduces to a bound that depends on how close the generated and real OOD distributions are — this is a restatement of the desideratum, not a theoretical justification that the Grad-CAM-based intervention achieves that closeness. The theoretical section does not meaningfully strengthen the paper's contributions.

- **Validation of the OOD crafting strategy is indirect.** The claim that the crafted samples are "near-OOD" (similar in style to ID but different in core features) is supported only through downstream task performance (Table 4). No qualitative examples of generated samples are visible in the main paper (Figures 10–11, referenced as showing examples, are in the appendix which is stripped by the parser), and no quantitative analysis (e.g., feature-space distance to real OOD, human evaluation, or distributional similarity metrics) is provided. While the ablation is informative, direct validation would strengthen confidence in the core mechanism.

- **The contribution of the teacher's binary classification layer is not fully isolated.** Setup B in Table 3 removes both the binary layer and the classification task simultaneously. The paper does not include an ablation where the binary layer is retained but trained without the classification objective, or where the teacher is kept entirely frozen while training the student. The individual contribution of the teacher's binary head is therefore confounded.

### Trivial

- The paper does not provide a complete list of the light and hard transformations used, referring only to examples ("color jitter," "elastic transformation"). A complete specification is important for reproducibility.
- The loss function (Eq. 1) is typeset with formatting issues that make the denominator difficult to parse; this appears to be a parser artifact but the original should be checked.

## Nice-to-Haves

- Reporting inference time and model size would help assess practical deployability, especially since the method runs both teacher and student at test time.
- A brief discussion of batch size sensitivity would be helpful, as the contrastive denominator scales with the batch.
- Testing on an alternative backbone (e.g., ViT) would strengthen claims about generality, though is not required for acceptance.

## Removed Points

These are points from the reviewers that I have removed with brief justification:

- *"Grad-CAM may highlight background textures rather than core features"* — This is speculative criticism. The ablation (Setup D, Table 3) shows that using random regions (similar to CutPaste) performs worse than the Grad-CAM-guided strategy, which provides empirical evidence that the saliency-based selection is effective. Removed as speculative.

- *"The method relies on a specific pre-trained ResNet-18 backbone and its biases are not analyzed"* — Scope creep. A paper need not test every possible backbone; the current choice is standard and the method is described generally.

- *"The method would work with a ViT or a randomly initialized network"* — Requesting experiments beyond the paper's scope. Removed.

- *Missing related works* — I cannot verify the existence of missing references without external sources. Removed per instructions.

- *"Missing proofs in appendix"* — The parser strips appendices. Removed per instructions.

- *Formatting nitpicks about garbled characters, missing braces, etc.* — These are parser artifacts, not author errors. Removed per instructions.

- *"Reproducibility concerns such as hyperparameters not disclosed"* — The paper provides the key hyperparameters: 200 epochs, AdamW, lr 1e-4, weight decay 1e-5, batch size 128, α ∈ [0.20, 0.50]. This is adequate for a conference submission.

- *Strength Finder's generic strengths* — Removed generic/superficial claims such as "the paper addresses an important problem" and vague praise without concrete evidence anchors.

## Novel Insights

None beyond the paper's own contributions. The reviews surface a genuine contradiction in the evaluation protocol description (100:0 ratio vs. actual Waterbirds mixture), and flag the lack of error bars as a significant gap, but neither constitutes a novel observation about the problem or method itself.

## Suggestions

1. **Resolve the training set composition inconsistency.** State unambiguously for every dataset what fraction of **D′**_ID samples (if any) were included in training, and confirm that all baselines were trained on identical data. If the 100:0 ratio indeed applies to most experiments, explain the Waterbirds exception clearly (or correct the text if the 100:0 claim is in error).

2. **Add error bars.** Report results over at least 3 random seeds (or provide some other measure of variance) for the main results and key ablations. A few single-percent differences in the ablation tables may be noise; variance estimates resolve this.

3. **Validate the OOD crafting directly.** Show sample images of crafted OODs, and optionally measure their feature-space proximity to real OODs using a frozen pretrained encoder. This would make the near-OOD claim concrete and complement the ablation in Table 4.

4. **Clean up the theoretical section or reframe it.** If Theorem 1 is presented primarily as motivation (i.e., "the gap depends on the A-OOD/real-OOD distance, so we should minimize this distance"), state this explicitly rather than offering it as a formal proof. Alternatively, add an analysis or experiment that connects the bound to a measurable property of the crafted samples.
