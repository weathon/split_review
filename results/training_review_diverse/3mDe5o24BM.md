Now I have all the evidence I need. Let me construct the final consolidated review.

## Summary

The paper proposes HFDream, a pipeline that uses human feedback to fine-tune a text-to-image diffusion model for viewpoint-aligned generation, which then improves text-to-3D synthesis via DreamFusion. By collecting human annotations on multi-view 2D images (rather than costly 3D assets), training a view-direction reward model, and fine-tuning the T2I model with a normalized reward-weighted loss, the method achieves consistent gains in both 2D view-alignment and downstream 3D quality. Human evaluation shows a 31% win margin in text alignment and 26% in 3D quality over the DreamFusion baseline.

## Strengths

- **Well-motivated approach that avoids 3D data.** The paper tackles a real problem (viewpoint inconsistency in DreamFusion) with a principled alternative to 3D-asset-based methods. The explicit question "How to improve geometric consistency without using 3D data?" (Section 1, lines 12–13) is clearly answered by the proposed human-feedback pipeline. The approach bypasses the distribution-shift and diversity-loss issues known to affect methods fine-tuned on Objaverse.

- **Consistent and substantial improvements across multiple evaluations.** Human pairwise evaluation (Figure 5a) on 244 3D assets with 4 raters each shows DF-HFDream winning DF-IF by 45%–14% for text alignment and 51%–25% for 3D quality. The view-alignment survey (Figure 5b) shows 50% perfectly aligned outputs vs. 32% for DF-IF. These are large, meaningful gaps. Quantitative metrics (Table 2) show HFDream outperforming baselines on both seen and unseen prompts across normalized reward, CLIP R-Precision Color, and CLIP R-Precision Normal.

- **Normalized reward (softmax over viewpoints, Equation 2) is a practical innovation.** The paper identifies that raw reward values vary across viewpoints and that direct use of the learned reward destabilizes training. The softmax normalization over four viewpoint prompts is a simple but effective fix, clearly motivated (Section 3.3, lines 98–104). This addresses a real engineering challenge in multi-category reward-weighting and goes beyond prior RLHF-for-T2I work (Lee et al., Fan et al.).

- **Fine-tuned reward model achieves ~90% classification accuracy vs. <10% for ImageReward on some views.** Figure 6 demonstrates a dramatic improvement in view-direction classification, and the evaluation separates seen/unseen objects relative to the reward model's training. This directly supports the claim that the reward model predicts view alignment more accurately than the off-the-shelf ImageReward (contribution bullet 2).

- **Method generalizes to personalized text-to-3D (HFDreamBooth3D).** Section 4.5 and Figure 7 show that combining HFDream with DreamBooth produces view-consistent personalized 3D outputs without additional algorithms, while the same procedure with the original DeepFloyd-IF fails. This demonstrates practical applicability beyond the core setting.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

- **Data augmentation pipeline from ~4,800 annotated images to "over 200K augmented preference pairs" is not fully detailed.** The paper mentions negative pairing (each valid image paired with a different-viewpoint negative) and oversampling of minority viewpoints (Section 3.2, line 83; Section 4.1, line 129), but does not give a step-by-step account. Simple negative pairing would yield ~14,400 pairs (4,800 × 3 negatives); reaching 200K requires additional augmentation/oversampling steps that are not quantified. While the general approach is plausible, the lack of detail makes it hard to assess the practical annotation cost and data diversity. The paper should clarify the exact augmentation recipe and the oversampling factor.

- **Reward model evaluation lacks a clear held-out test set.** Section 4.4 reports "validation accuracy... on its training dataset with 5K images" (line 178). The phrasing is ambiguous — it is unclear whether the 5K images are a proper held-out validation split or drawn from the training pool. The paper earlier notes a validation split is used for checkpoint selection (line 129), but no independent test-set accuracy is reported. While the dramatic accuracy gap (~90% vs. <10%) makes overfitting to the validation set unlikely to reverse the conclusion, a cleaner test-set evaluation would strengthen the claim that the reward model generalizes.

- **Limited scale of human annotations and evaluation prompts.** The human-labeled dataset covers 18 objects and 9 scenes (162 prompts, ~1,200 images per direction). The evaluation set contains 61 prompts (23 seen, 38 unseen). The paper itself acknowledges that performance degrades on unseen prompts (Section 4.2, line 143: "its performance drop on unseen prompts... does suggest the potential need for larger and more diverse human datasets"). This does not invalidate the contribution — the method clearly works with limited data — but it raises a genuine question about how the method scales to broader visual domains. The contribution would be strengthened by demonstrating the method on a larger, more diverse dataset.

- **Statistical significance not reported for quantitative results.** Tables 1 and 2 and the human evaluation (Figure 5a) do not include confidence intervals, p-values, or variance estimates. For the human evaluation with 244 assets and 4 raters, bootstrapped confidence intervals on win rates would be informative. This is a common gap in the field but worth noting.

- **No ablation study on the reward normalization (Equation 2).** The paper claims the softmax normalization is important for training stability (Section 3.3) but does not provide an experiment showing what happens without it (e.g., reward divergence, lower quality). An ablation would strengthen the method section.

- **Win rates against DF-PerpNeg not reported numerically.** Section 4.3 says "a similar trend is observed when comparing DF-HFDream with DF-PerpNeg" (line 152) but does not give the actual win/lose/tie percentages. Figure 5a presumably shows this, but the text extraction cannot verify the figure content. The numbers should be stated in text.

### Trivial

- The paper reports validation accuracy for the reward model on a set described as "its training dataset" (line 178) — this appears to be a minor imprecision (likely meaning the human-labeled collection rather than the actual training split), but it should be clarified.

- Table 1 data and Figure 5a numbers are embedded in figures/images that are not text-readable in the extraction. The text discussion provides sufficient qualitative summary, but the precise numbers should be available in the text or a text-based table.

## Nice-to-Haves

- A comparison to 3D-data-based methods (e.g., Zero-1-to-3, MVDream) would contextualize the trade-offs between human annotation cost and quality. This is outside the paper's stated scope ("without using 3D data"), but a qualitative discussion or a small comparison would help readers understand the practical positioning.
- An ablation on the choice of reward model backbone (e.g., fine-tuning a smaller reward model from scratch vs. fine-tuning ImageReward) could isolate the contribution of the human dataset.
- Providing the evaluation prompt set as a supplementary list would improve reproducibility.

## Removed Points

These points are flagged to be removed; treat them with caution:

- *"Seen/unseen split is unclearly defined"* — Removed. The paper clearly defines it: "based on whether the object in the prompt was encountered during the training of the text-to-image model" (line 133). The harsh critic's confusion about DeepFloyd-IF's training data scope does not reflect a paper error.
- *"No comparison to 3D-data approaches (Zero-1-to-3, MVDream)"* — Removed as scope creep. The paper's explicit research question is "How to improve geometric consistency without using such 3D data?" (lines 12–13). Demanding comparison to methods that use 3D assets evaluates the paper against a different class of approach.
- *"The choice to augment negative examples with different viewpoints is not justified"* — Removed. The paper provides the justification: "prevent model bias and trivial guessing by balancing the training data" (line 83). This justification is conceptually sound.
- *"Evaluation uses self-trained metric (normalized reward score)"* — Removed as overstated. The paper also uses CLIP R-Precision (Color and Normal) which are independent metrics, and human evaluation (Figures 5a, 5b). The normalized reward score is one of several metrics, not the sole evidence.
- *"Section 4.5 is not rigorous"* — The paper presents HFDreamBooth3D as a "simple" and "preliminary" application showcase (Section 4.5, lines 197–198). Criticizing it for not being a rigorous evaluation misaligns with how the paper presents it.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. Provide a clear, step-by-step description of the data augmentation pipeline: starting from the ~4,800 annotated images through negative pairing and oversampling to the final 200K+ preference pairs, including the oversampling factor.
2. Report reward model test-set accuracy on a truly held-out set (not used for checkpoint selection), alongside the existing validation accuracy.
3. Report confidence intervals or variance estimates for the main human evaluation results (Figure 5a).
4. Add an ablation study for the reward normalization (Equation 2) to empirically demonstrate its stabilizing effect.
5. Report the DF-HFDream vs. DF-PerpNeg win/lose/tie percentages numerically in the text.

## Score and Decision

**Overall assessment:** The paper presents a clean, well-motivated, and effective pipeline for improving text-to-3D generation via human feedback on view alignment. The core claims are supported by multiple lines of evidence (automatic metrics, human evaluation, reward model analysis), and the weaknesses are minor and addressable. The paper makes a genuine contribution to the text-to-3D literature by demonstrating that human 2D annotation can substitute for costly 3D data while improving diversity and quality.

**Originality:** Moderate — builds on the RLHF-for-T2I framework (Lee et al., Fan et al.) but applies it to the novel setting of multi-view alignment for 3D generation, with a practical normalization innovation.

**Importance of research question:** High — the Janus problem and geometric inconsistency are central obstacles in text-to-3D.

**Claims supported:** Yes — the main claims (improved view alignment leading to better 3D quality) are supported by consistent evidence across metrics.

**Soundness:** Good — the methodology is sound, though the reward model evaluation could be slightly more rigorous.

**Clarity:** Good — the paper is well-structured and the method is clearly described, though the data augmentation pipeline needs more detail.

**Value to community:** The human-feedback approach offers a practical alternative to 3D-data-based methods, and the normalization technique is likely reusable.

MY FINAL SCORE: <pineapple>7.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>