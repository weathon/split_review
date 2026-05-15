Now I have enough information from the paper to verify the reviewer claims. Let me compose the consolidated review.

## Summary

CLIBD applies CLIP-style contrastive learning to align images, DNA barcodes, and taxonomic text labels in a shared embedding space for insect species classification. The method is evaluated on BIOSCAN-1M and INSECT datasets using retrieval-based classification and downstream zero-shot learning tasks. The central technical finding is that using DNA as an alignment target (I+D) yields better image representations for taxonomic classification than using text alone (I+T).

## Strengths

- **DNA proves to be a more effective alignment target than taxonomic text for image representations.**  The paper shows that the I+D model consistently outperforms the I+T model across taxonomic ranks, with the species-level macro H.M. for unseen species showing a meaningful gap. This is a non-obvious finding — DNA barcodes, which are not directly visual, provide a richer supervisory signal than human-assigned text labels, and the result is cleanly demonstrated.

- **Novel and well-motivated problem direction.**  Integrating DNA barcodes with images for classification is a genuinely underexplored area. The paper correctly identifies that DNA barcodes (available at scale from initiatives like BOLD) can serve as an alignment signal without requiring expert taxonomic labels, which are scarce (under 10% species-level labels in BIOSCAN-1M).

- **Principled evaluation design.**  The explicit seen/unseen species split for evaluating generalization, and the use of retrieval (nearest-neighbor matching) rather than a fixed classification head, are both appropriate methodological choices that enable handling of novel classes.

- **Effective use of partially labeled data.**  The contrastive learning framework naturally leverages the large fraction of records with only partial or missing taxonomic labels (fewer than 10% have species-level labels), which is a realistic constraint for real-world biodiversity datasets.

## Weaknesses

### Fatal
None.

### Major

- **The BioCLIP comparison is fundamentally unfair.** CLIBD is fine-tuned on BIOSCAN-1M (the evaluation dataset itself), while BioCLIP is evaluated zero-shot without any fine-tuning on this domain. The paper acknowledges this asymmetry only indirectly (line 208: "BioCLIP was trained on a much broader dataset") but does not fix the comparison protocol. A proper comparison would require either fine-tuning BioCLIP on BIOSCAN-1M or evaluating CLIBD zero-shot on a dataset outside BIOSCAN-1M without prior training on it. The claim that CLIBD "consistently outperforms BioCLIP" is therefore an artifact of an uneven evaluation setup, not a genuine architectural advantage. This is the most significant weakness because it inflates the paper's central performance narrative.

- **The "over 8%" improvement claim in the abstract is vague and not clearly substantiated.**  The abstract states the method "surpasses previous single-modality approaches in accuracy by over 8% on zero-shot learning tasks," but no single experiment in the paper is cleanly tied to this number. The improvement from "no alignment" (6.27%) to I+D+T (52%) uses off-the-shelf untrained encoders as the baseline. The improvement of I+D+T over I+T is more defensible as a within-method ablation but is not explicitly reported as "over 8%" anywhere. This ambiguity in the headline claim undermines reader trust and should be replaced with a precise, experiment-tied statement.

### Minor

- **The "zero-shot" framing is non-standard and somewhat overstated.**  The paper defines zero-shot as evaluating on species not seen during contrastive training, but inference requires labeled reference samples (images or DNA) from those unseen species as keys in the retrieval database. This is more accurately described as a retrieval-based open-set or few-shot-like scenario than zero-shot as commonly understood in the CLIP literature (where only class-name text prompts are needed, not labeled exemplars). The paper does define its setting clearly (line 132-134), which partially mitigates this concern, but the terminology invites misunderstanding.

- **Cross-modal image-to-DNA retrieval performance is very low.**  While the paper honestly acknowledges this (line 274: "performance still lags behind intra-modal performance"), the species-level accuracy for image-to-DNA retrieval on unseen species (reported elsewhere as ~3-7%) is barely above random. The paper's stated motivation includes "classify taxa for which no images exist in reference databases," but the cross-modal retrieval accuracy is far too low to support this use case in practice. This doesn't invalidate the main contribution (DNA improving *image-to-image* retrieval), but it means the "bridge" metaphor substantially overstates what is currently achievable.

- **The INSECT/BZSL results provide only weak support for the method's contributions.**  The BZSL framework itself is from prior work; CLIBD merely supplies feature encoders. The improvement over the baseline (ResNet-101) is modest, and the "no fine-tuning" variants sometimes perform *worse* on unseen species than the baseline. This downstream evaluation is suggestive but not strongly probative of the method's value.

- **No confidence intervals or variance estimates are reported.**  Given the long-tailed species distribution and small test splits for rare unseen species, the reported point estimates could have substantial variance. This is a standard expectation in machine learning evaluation.

### Trivial

- The attention visualization (Figure 6) is purely qualitative. It provides interpretive texture but no quantitative evidence that the observed attention patterns causally relate to the accuracy improvements.

## Nice-to-Haves

- A controlled unimodal baseline where the image encoder is fine-tuned on BIOSCAN-1M with a supervised classification head (even using partial labels) would cleanly isolate the benefit of cross-modal alignment from the benefit of training on the target dataset.
- Analysis of why image-to-DNA retrieval fails — e.g., whether the top-1 error is typically a taxonomically close species — would clarify whether the embedding space at least captures coarse taxonomic structure.
- UMAP/t-SNE visualization of the multimodal embedding space would provide interpretable evidence of alignment quality.

## Removed Points

- **"The 8% claim is fabricated"** — Removed as overstatement. The paper does show improvements, though not cleanly tied to the specific "8%" number. The abstract should be more precise, but "fabricated" is not accurate.
- **"Cross-modal retrieval invalidates the claimed bridge"** — Removed as overstatement. The paper acknowledges the low performance. The main contribution (I+D > I+T for image-to-image) does not depend on cross-modal retrieval being high.
- **"The contradiction about DNA being expensive"** — Removed. The paper says DNA is more expensive than images (line 24) but more readily available than taxonomic labels (line 32). These are different comparisons and not contradictory.
- **"Missing appendix" / "appendix unavailable"** — Removed per hard rules. The appendix exists in the original submission; the parser strips it.
- **"Missing related works"** — Removed per hard rules: I cannot confirm what related works exist outside the paper.
- **"Formatting/style nitpicks"** — Removed per hard rules.

## Novel Insights

None beyond the paper's own contributions. The reviewers' insights largely concern framing and comparison issues rather than uncovering new findings from the paper's data.

## Suggestions

1. **Fix the BioCLIP comparison.** Either fine-tune BioCLIP on BIOSCAN-1M and re-evaluate, or evaluate CLIBD zero-shot on an external dataset without BIOSCAN-1M training. The current comparison is methodologically unsound and inflates the reported results.

2. **Replace the vague "over 8%" abstract claim** with a precise statement tied to a specific experiment and comparison (e.g., "I+D+T improves species-level macro H.M. by X percentage points over I+T on unseen species" or similar).

3. **Re-frame "zero-shot"** as "retrieval-based classification on unseen species" or "open-set retrieval" to avoid terminological confusion.

4. **Add confidence intervals** (e.g., bootstrap estimates) for the main results, especially for unseen species where class sizes are small.

5. **Add analysis of cross-modal retrieval errors** — are the top-5 matches taxonomically close even when the top-1 is wrong? This would substantially strengthen the "bridge" claim even with low top-1 accuracy.

## Score and Decision

I will now produce the final score and decision.

MY FINAL SCORE: <pineapple>5.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>