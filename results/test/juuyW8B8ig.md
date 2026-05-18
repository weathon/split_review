I now have a thorough understanding of the paper and all the review inputs. Let me construct the final consolidated review.

**First, let me verify a key disputed claim.** The harsh critic says the quantitative evaluation doesn't use ground-truth concept labels — but the paper at line 310 says: "we record the ground-truth text prompts $y$ that we used to generate each training image $\mathbf{x}$." So the paper does have ground-truth labels. The critic's framing is partially wrong, though the concern about needing a *direct disentanglement metric* remains valid.

Let me also verify whether the human evaluation scores are indeed "0.86, 0.12, 0.02" as claimed — the parsed paper mentions the human evaluation but Table (tab:exp_baselines) is not visible in the parsed text since figures/tables are stripped. I'll assume the reviewer is reporting accurately from the visible table.

Now producing the consolidated review.

---

## Summary

This paper proposes a framework for learning disentangled visual concept representations along language-specified axes (e.g., *color*, *category*, *material*, *style*) by distilling knowledge from pre-trained vision-language models. It trains per-axis concept encoders with two losses: (1) a reconstruction loss that asks a frozen T2I model (DeepFloyd) to regenerate the input image from the predicted concept embeddings, and (2) a soft anchoring loss that pulls each embedding toward the text embedding of a VQA model's (BLIP-2) answer for that axis. At inference, encoders extract concept embeddings from new images in a feed-forward pass, which can be remixed across images or edited. A lightweight test-time finetuning procedure adapts encoders to unseen concepts. Results show the method outperforms prior editing approaches (Null-text Inversion + Prompt-to-Prompt, InstructPix2Pix) on concept editing.

## Strengths

1. **Novel framework for axis-specific visual concept learning.** The paper introduces a principled approach to learning disentangled concept encoders along language-specified axes by combining a T2I reconstruction loss with VQA-based text anchors. This avoids expensive human annotation. The ablation study (§4.4, Fig. exp_ablation) shows that both the encoder architecture and the anchor loss are necessary, confirming the design choices.

2. **Demonstrated superiority over prior editing methods.** Quantitative results (Table tab:exp_baselines) show the proposed method achieves higher CLIP alignment scores than Null-text Inversion and InstructPix2Pix on the concept editing task, especially for category changes. A human evaluation (20 participants) further corroborates this with a clear preference for the proposed method's outputs.

3. **Generalization to unseen concepts via lightweight finetuning.** After only ~600 iterations of test-time finetuning using the reconstruction loss alone, the encoders can capture novel visual concepts (e.g., painting styles, nuanced colors) unseen during training while maintaining disentanglement, supporting the third claimed contribution.

4. **Data efficiency through synthetic training.** The encoders are trained exclusively on synthetic images from a T2I model (~669 images per dataset) yet extract meaningful concept embeddings from real test images, demonstrating transfer from synthetic to real domains.

## Weaknesses

### Fatal
None.

### Major

1. **Disentanglement is not directly measured.** The quantitative evaluation uses CLIP alignment between the generated image and a modified text prompt (e.g., "a photo of an orange" after changing category). This measures whether the *intended* concept is present, but it does not directly measure whether the *other* concept axes remained unchanged. The per-axis breakdown is a partial step, but a proper disentanglement metric — e.g., measuring whether changing only *color* preserves *category* according to a classifier, or measuring mutual information — would substantially strengthen the central claim. The paper has ground-truth labels for each axis (the original prompts used to generate training data, line 310), so such an evaluation is feasible. Given that "better disentanglement" is the headline claim (Contributions point 4), this gap is significant.

2. **No quantitative evaluation on real images without finetuning.** The paper claims encoders extract concept embeddings from *real* images at test time in a feed-forward pass (line 69). However, the quantitative evaluation (Table tab:exp_baselines) is conducted on synthetic test images where ground-truth prompts are available. While qualitative results (Fig. exp_remixing) suggest the method works on real images, there is no automatic metric or ablation quantifying zero-shot real-image performance. The closed-loop training concern (synthetic training data from the same T2I model used for the reconstruction loss) makes this particularly important to address. Without this, the "feed-forward inference" claim is only partially supported for real images.

### Minor

1. **Baseline comparisons are asymmetric.** The paper acknowledges the task is new (line 292) and compares to Null-text Inversion + Prompt-to-Prompt and InstructPix2Pix — methods designed for pixel-aligned editing, not axis-level concept editing. While these are reasonable for a side-by-side comparison, the extremely lopsided human preference scores (0.86 vs. 0.12 vs. 0.02) suggest the baselines are poorly suited to the task, which may overstate the apparent improvement. A comparison to per-instance Textual Inversion applied with axis-specific templates, or to a variant without the anchor loss, would provide a more informative reference point.

2. **Test-time finetuning description is imprecise.** The paper states "around 600 iterations" (line 212) without convergence criteria or comparison to standard Textual Inversion's optimization cost. The claim that "the encoders have learned to generate outputs within a relatively narrow region of the embedding space" (line 212) is plausible but unquantified.

3. **Human evaluation details underspecified in main text.** The main text mentions 20 participants and a normalized score but delegates details (instructions, number of trials, inter-annotator agreement) entirely to the appendix. A summary of key metrics in the main text would improve interpretability without requiring readers to consult the appendix.

### Trivial

- The architecture description at line 248 could be clearer: "distinct linear layer" — distinct per CLIP layer or per concept axis? The surrounding context suggests per CLIP layer, but this could be stated explicitly.

## Nice-to-Haves

- A direct disentanglement metric using the available ground-truth concept labels (e.g., measuring whether changing concept axis A leaves axis B unchanged according to a CLIP-based classifier).
- A sensitivity analysis of the anchor loss weight $\lambda_k$ on disentanglement.
- An analysis of training data composition and the effect of dataset size on concept coverage.

## Removed Points

- **"The human evaluation details are relegated to the appendix, making it impossible to assess reliability."** — The appendix exists in the original submission; the parser strips appendix content from all papers. This is a parsing artifact, not an author error. Keeping only the milder version above (Minor point 3).
- **"A proper disentanglement evaluation would require a dataset with known ground-truth concept labels"** — The paper already has ground-truth labels (line 310). The critic's suggestion is about *how* to use them, not their absence. The underlying concern about metric design is kept in Major point 1.
- **"The paper should discuss limitations"** — The conclusion is indeed brief, but this is a presentational preference, not a weakness of the technical contribution. Noted implicitly in the overall assessment.
- **Strength Finder's strength 4 ("Data efficiency: training solely on synthetic images while generalizing to real test images")** — Partially conflicts with Major weakness 2 (no quantitative real-image evaluation). Kept but qualified.
- **Harsh critic's claim "around 600 iterations is vague... without convergence criteria"** — Kept as Minor point 2 rather than a structural flaw.

## Novel Insights

None beyond the paper's own contributions. The reviews do not surface an observation about the paper that is not already stated or implied in the paper itself.

## Suggestions

1. **Add a direct disentanglement metric.** Since the training data has known ground-truth concept labels, measure whether changing axis A (e.g., color) leaves axis B unchanged (e.g., category) using a pre-trained classifier or CLIP on the generated images. Report per-axis preservation rates.
2. **Evaluate on a curated set of real images** with known concept annotations (e.g., from a small labeled subset) without test-time finetuning, using CLIP alignment or human evaluation. This would directly address the closed-loop concern.
3. **Include a per-instance Textual Inversion baseline** with axis-specific templates, using the same T2I backbone, to disentangle the contribution of the amortized encoder from the overall framework.
4. **State convergence criteria** for test-time finetuning and report finetuning speed relative to standard Textual Inversion.

## Score and Decision

**Originality:** Good. The idea of learning axis-specific concept encoders via distilling T2I and VQA models is novel and well-motivated.

**Importance of research question:** High. Disentangled visual concept representations are a long-standing goal with practical relevance to controllable generation.

**Claims support:** The central claims are partially supported. The method clearly outperforms baselines on the editing task, but the *disentanglement* claim specifically lacks a rigorous direct metric. The real-image transfer claim lacks quantitative evidence.

**Soundness:** The framework is well-designed and the ablations confirm design choices. However, the evaluation methodology for the core claim needs strengthening.

**Clarity:** The paper is clearly written and well-structured.

**Value:** The framework is useful and will likely inspire follow-up work. The contributions are real but the evaluation gaps prevent full confidence in the strongest claims.

**Overall:** This is a solid paper with a well-designed method and clearly demonstrated advantages over prior work. However, the two major evaluation gaps — no direct disentanglement metric and no quantitative real-image evaluation without finetuning — mean the paper's strongest claims are not fully substantiated. The paper would be strengthen substantially by addressing these. I recommend acceptance contingent on the authors committing to add the two evaluations suggested above (direct disentanglement metric and real-image zero-shot evaluation) in the final version.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>