Here is the consolidated final review.

---

## Summary

This paper proposes a framework for learning disentangled, language-informed visual concept representations from images by distilling pre-trained vision-language models. It trains concept encoders along axes specified by language (e.g., *category*, *color*, *style*) with two objectives: (1) reproducing the input image through a frozen T2I model (DeepFloyd), and (2) anchoring concept embeddings toward VQA-derived text embeddings to improve disentanglement. At inference time, extracted concept embeddings can be remixed across images, and a lightweight test-time finetuning procedure generalizes to unseen concepts.

## Strengths

1. **Disentanglement via VQA text anchors is novel and convincingly ablated.** The soft anchoring loss (Eq. 2) pulls concept embeddings toward text embeddings from BLIP-2 VQA answers, enforcing axis-specific separation without collapsing to discrete tokens. The ablation (Section 4.5, Table 1, Fig. 6) shows that removing this loss degrades recomposition, providing direct causal evidence for its effectiveness.

2. **Generalization to unseen concepts via lightweight test-time finetuning is demonstrated.** Section 3.3 and Figure 4 show that after ~600 finetuning iterations on a single test image, the encoders can extract novel concepts (e.g., the specific style of a dog painting) never seen during training, while preserving disentanglement. This is a meaningful advance over per-instance optimization methods (e.g., Textual Inversion) which require optimizing an embedding from scratch.

3. **Quantitative and human evaluation shows advantages over text-based editing baselines.** Table 1 reports CLIP alignment scores and human preference rankings where the proposed method surpasses Null-text Inversion + Prompt-to-Prompt and InstructPix2Pix on the task of editing one concept axis while preserving others, with a category alignment score of 0.88 and overall human score of 0.73.

4. **Training on synthetic images transfers, at least qualitatively, to real images.** Section 4.1 describes training exclusively on DeepFloyd-generated images, yet the qualitative evaluations (Figs. 4, 5) use real-world test images. This demonstrates potential for synthetic-to-real generalization.

5. **Continuous embeddings capture visual nuances beyond discrete language.** Section 4.2 and Figure 7 show that continuous concept embeddings can represent subtle variations (e.g., "yellow-ish-orange") that single words cannot, enabling interpolation between concepts.

## Weaknesses

### Major

1. **Quantitative evaluation is conducted on synthetic, in-distribution data, not real images.** The quantitative experiments (Section 4.4, lines 309–310) use ground-truth text prompts "that we used to generate each training image" and operate on synthetic images from the *same distribution as training*. The paper's core claim is that concept encoders can extract concepts from *real* test images (line 69: "extract concept embeddings from real images at test time"), yet the main quantitative evidence never touches real data. While qualitative results on real images (Figs. 4, 5) are shown and a human evaluation is conducted, the primary numerical evidence for the method's effectiveness is restricted to the synthetic evaluation set. This is an evidential gap between the claims and the data.

2. **Backbone mismatch between the proposed method and baselines confounds comparison.** The proposed method uses DeepFloyd (IF-I-XL + IF-II-L) as its T2I backbone (line 154), while both baselines (Null-text Inversion + Prompt-to-Prompt, InstructPix2Pix) use Stable Diffusion (line 296). Since the primary quantitative metrics are CLIP alignment scores — which are sensitive to image quality — the comparison conflates method quality with backbone quality. The human evaluation partially mitigates this since humans can judge overall quality, but the quantitative CLIP scores remain confounded. (That said, adapting the baselines to DeepFloyd would be non-trivial since those methods were designed for SD's architecture, so the issue is partially one of practical constraints rather than experimental negligence.)

### Minor

1. **Sensitivity to the anchor loss weight λ is not explored.** The paper sets λ = 0.0001 for *category* and λ = 0.001 for other axes (line 255), but does not study how these values affect the trade-off between disentanglement and nuance capture. Since λ is a critical hyperparameter (lines 190–191 note that too large a weight causes collapse to discrete text embeddings), a sensitivity analysis would better characterize the method's robustness.

2. **No dedicated limitations or failure case discussion.** The conclusion (Section 5) summarizes contributions without acknowledging limitations. The paper would benefit from discussing scenarios where the method may fail (e.g., when VQA gives wrong answers, when concepts are outside the T2I model's distribution, when multiple objects interact).

3. **No statistical significance or variance reporting for quantitative results.** The quantitative results (Table 1) do not report confidence intervals or standard deviations. Given the relatively small training set (~669 images per dataset) and random sampling of target concepts, variance estimates are needed to assess whether differences between methods are meaningful.

### Trivial

- λ values (line 255) are given as 0.0001 and 0.001 — consider using scientific notation for readability.

## Nice-to-Haves

- A quantitative evaluation on real images using proxy metrics (e.g., concept classification accuracy on a labeled real-image dataset, or human judgments on a held-out real-image set) would directly substantiate the core claim of generalization to real images.
- A direct per-concept textual inversion baseline (learning separate tokens per axis per image and composing them) would more clearly isolate the benefit of the encoder architecture.

## Removed Points

These points were flagged by the reviewers but are removed for the following reasons:

- **"CLIP encoder frozen vs. fine-tuned not clarified"** — The paper is clear enough: "we leverage a pre-trained CLIP ViT/L-14 model... and train $K$ separate concept encoders $f_k$ on top of the features" (lines 245–247), implying CLIP is frozen.
- **"Quantitative results table not fully described due to truncation"** — The table is referenced via `\input{table/baselines}` which is a LaTeX issue, not an author omission. The parser did not render it, but the original submission contains it.
- **"Missing per-concept textual inversion baseline"** — The paper's ablation study (Section 4.5) *does* compare against per-instance optimization (the core of what the reviewer asks), showing it "deteriorates disentanglement." While the comparison is qualitative, the paper does address this concern. A more thorough quantitative comparison would strengthen the paper (noted in Nice-to-Haves), but it is not a missing baseline.
- **"Training data domain shift not measured for encoders without finetuning"** — The paper's scope is that test-time finetuning is the intended mechanism for handling unseen concepts on real images. Criticizing the lack of a zero-shot (no finetuning) real-image evaluation is scope creep; the method explicitly includes the finetuning step.
- **"Missing appendix sections"** — Stripped by the parser; not an author issue.
- **All formatting/style/typo criticisms** — Parser artifacts or trivial.
- **All criticisms questioning existence of cited models/tools/references** — Not permitted per instructions.

## Novel Insights

None beyond the paper's own contributions. The reviewer inputs did not surface a perspective on the work's implications that the paper itself does not already provide.

## Suggestions

1. Add a real-image quantitative evaluation — even a small-scale one (e.g., 50–100 real images with ground-truth axis labels evaluated via a concept proxy task or human ratings) — to directly support the claim of generalization to real images.
2. Add a controlled experiment: adapt the proposed method to use Stable Diffusion (or adapt one baseline to use DeepFloyd) to disentangle method quality from backbone effects, or at minimum discuss the confounding and its likely direction.
3. Report confidence intervals or standard deviations for all quantitative metrics across random seeds or evaluation splits.

## Score and Decision

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>