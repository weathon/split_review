- Decision: Reject
- Avg Score: 5.25
- Scores: 5, 5, 5, 6
Now I have all the information I need from the paper. Let me construct the final consolidated review.

## Summary
2-3 sentence summary of the paper's contribution.

The paper proposes PC-CLIP, a method that finetunes CLIP's text encoder so that *differences* between image embeddings align with LLM-generated text descriptions of visual differences between the images. This improves CLIP's embedding geometry, enabling new capabilities such as zero-shot difference-based classification (ranking images by attributes like size or color) and comparative prompting that improves classification on confused classes. Controlled baselines (COCO FT and Rewrite FT) isolate the benefit of the comparative supervision.

## Strengths

- **Novel finetuning objective that targets CLIP's known geometric deficiency.** The paper directly addresses CLIP's inability to support analogies/arithmetic in embedding space by aligning image-difference vectors with LLM-generated text descriptions of differences (Eq. 1, Fig. 1). This is a clean, well-motivated idea that prior VLM finetuning work has not explored.

- **Enables difference-based classification — a capability CLIP lacks entirely.** Table 1 shows PC-CLIP achieves 67.55% on CUB and 67.44% on CIFAR-100 difference-based classification, while CLIP hovers near chance (53.32% and 54.92%). The results are reported with standard errors over 5 seeds, and the improvement is large and consistent across all four datasets (AwA2, CIFAR100, CUB, Flowers102).

- **Controlled baselines cleanly isolate the comparative signal.** The paper includes finetuning on the same COCO data without comparisons (COCO FT) and with LLM-rewritten captions that are non-comparative (Rewrite FT). PC-CLIP outperforms both across almost all settings, demonstrating that the comparative supervision itself — not extra data or extra LLM text — drives the improvement.

- **Quantitative evidence that the text encoder better localizes class differences.** Table 5 directly measures the cosine distance between class-prompt-difference embeddings and LLM comparison embeddings. PC-CLIP consistently reduces this distance (e.g., 0.92 vs. 1.04 on CIFAR-100) while increasing distance for the reversed comparison (1.08 vs. 0.96), confirming improved geometric structure.

- **Comparative prompting shows promising gains on confused classes, with transparent reporting.** Table 3 reports that PC-CLIP + comparative prompting improves accuracy on all 5 datasets' confused subsets (e.g., +7.00 on EuroSAT, +9.38 on Flowers102), while CLIP + comp improves on 3/5 and can sharply hurt (e.g., −3.40 on EuroSAT). The paper explicitly acknowledges that the pair selection differs across models.

## Weaknesses

### Fatal
None.

### Major

- **The comparative prompting evaluation is confounded by differing pair selection across models.** The "3 most confused class pairs" are selected independently from each model's confusion matrix (line 246, line 250). The paper acknowledges the pairs can differ between CLIP and PC-CLIP. This means the delta improvements in Table 3 are not directly comparable across models: the selection bias (which classes are confused and by how much) is entangled with whether PC-CLIP's embeddings better support the vector arithmetic. The within-model delta (model vs. model+comp on the same pairs) is informative, but the cross-model claim that "PC-CLIP observes larger gains" is weakened. A cleaner evaluation would fix the same class pairs for both models and compare the resulting deltas. This is the most significant methodological gap in the paper.

### Minor

- **The training loss function is underspecified.** Equation (1) states the objective is `ℓ(g(I₁)−g(I₂), f(T₁,₂))` but says "ℓ can represent any particular loss function" (line 113). The actual choice of loss (InfoNCE? cosine-similarity margin? MSE?) is never disclosed. This is important for reproducibility.

- **Missing error bars or confidence intervals on zero-shot classification and CLIPScore results.** Table 2 (zero-shot), Table 4 (extended prompts), and Table 6 (CLIPScore) report point estimates without variance. The zero-shot gains are 1–2% on most datasets — small enough that without error bars it is unclear whether they are reliable. The CLIPScore improvement (0.532→0.542) similarly lacks variance.

- **The frozen image encoder creates an asymmetric training setup that is not critically examined.** The paper only finetunes the text encoder (line 193), justified by computational efficiency. This means the text encoder must adapt to whatever geometry exists (or is missing) in the frozen image encoder's difference space. The paper shows this works empirically, but never discusses whether jointly finetuning the image encoder would yield further gains, or whether the frozen encoder fundamentally limits what the method can achieve.

- **PC-CLIP's zero-shot performance drops on CUB (80.08 vs. 81.72) without explanation.** Since the CUB dataset was used to generate training pairs, this drop is counterintuitive. The paper notes the drop (line 215) but offers no analysis. Possible causes (overfitting to COCO-based comparisons, noisier LLM generations for fine-grained differences, etc.) are not discussed.

- **Hyperparameter α for comparative prompting is introduced but no selection procedure is given.** Equation (3) introduces α to weigh the original class prompt against the comparison-based update, but the paper does not state what value of α was used, whether it was tuned, and if so on what split.

### Trivial

- The number of training pairs used for finetuning is not reported. The paper states 1,000 randomly sampled images (line 166) but does not state how many pairs were generated from them or whether all ~500K possible pairs were used.
- Some references to evaluation details point to an appendix (appx:image_gen, appx:image_gen_examples) that is not present in the main text.

## Nice-to-Haves

- **Compare against CyCLIP as a baseline.** CyCLIP also enforces pairwise distance structure in CLIP's embedding space, though through a different mechanism (CyCLIP uses symmetric distance constraints without semantic meaning). Including it would strengthen the claim that LLM-generated *semantic* differences are the key ingredient.
- **Statistical tests for the zero-shot differences.** Given the small margins (1–2%), reporting whether these are significant (e.g., via paired bootstrap) would strengthen confidence.
- **More systematic evaluation of text-to-image generation.** Only two qualitative examples are shown (Figure 2); generating more prompts and measuring alignment with a captioning model would strengthen this section.
- **Ablation on α values** to show sensitivity of comparative prompting to this hyperparameter.

## Removed Points

These points surfaced in the reviews but are removed from the main assessment with justification:

1. *"The comparison is not apples-to-apples because the pairs differ across models"* — Retained in modified form in Major weaknesses above; the original framing is slightly overstated because (a) the within-model delta is still informative, (b) CLIP+comp sometimes produces negative deltas, which selection bias cannot explain, and (c) the paper transparently discloses the differing pairs. The core concern is real but narrower than the critic suggests.

2. *"The authors should include significance tests for Table 1"* — The margins in Table 1 are large (e.g., 67.55 vs. 53.32) and error bars are reported. Significance testing would not change interpretation. Removed.

3. *"Method soundness" general concerns about whether the frozen image encoder is sufficient* — Retained as Minor weakness above; the general framing is replaced with a specific, verifiable observation that the paper does not critically examine this design choice.

4. *General reproducibility nitpicks about undisclosed batch size and learning rate* — These are standard implementation details and do not materially affect the assessment. The more significant reproducibility gap (unspecified loss function) is retained.

## Novel Insights

None beyond the paper's own contributions. The reviewers' main novel observation is the confound in the comparative prompting evaluation, which is already noted as a Major weakness above.

## Suggestions

1. **Fix the comparative prompting evaluation.** Run the experiment with the same fixed set of class pairs (e.g., the 3 pairs most confused by CLIP) for both models, and report the delta improvements. This cleanly separates selection effects from embedding quality.

2. **Specify the loss function** used in Equation (1). If an InfoNCE loss, state the temperature and the number of negatives; if a cosine-similarity margin loss, state the margin.

3. **Add error bars or confidence intervals** to Tables 2, 4, and 6 (zero-shot and CLIPScore results). If the zero-shot gains are not statistically significant, soften the corresponding claims.

4. **Discuss the CUB performance drop.** Provide a brief analysis of why PC-CLIP underperforms CLIP on CUB zero-shot, especially given that CUB images were included in the training data.

5. **State the value and tuning procedure for α** in comparative prompting, and consider reporting sensitivity to this hyperparameter.
