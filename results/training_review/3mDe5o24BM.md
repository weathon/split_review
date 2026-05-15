Now I have a thorough understanding of the paper and all reviewer claims. Let me construct the final consolidated review.

## Summary

The paper proposes HFDream, a method that fine-tunes text-to-image diffusion models using human feedback to improve multi-view generation and thereby enhance text-to-3D generation via DreamFusion. The pipeline involves: (1) collecting human labels for generated multi-view images, (2) training a reward model to assess view-direction alignment, (3) fine-tuning the diffusion model using a reward-weighted loss with softmax normalization across viewpoints, and (4) integrating the fine-tuned model into DreamFusion. The approach avoids reliance on 3D asset datasets.

## Strengths

1. **Human-feedback-based view alignment without 3D assets**: The pipeline generates realistic multi-view images using human labelers rather than 3D datasets, directly avoiding the distribution-shift issue that motivates the work (Section 1). This claim is supported by the 3D human evaluation (Figure 5a): DF-HFDream achieves a 31% win-rate advantage in text alignment and 26% in 3D quality over DreamFusion with the original model.

2. **Normalized reward for stable multi-view fine-tuning**: The softmax normalization of rewards across four viewpoints (Equation 2) addresses the instability caused by varying reward scales across directions (Section 3.3). Table 1 shows consistent improvements across all four viewpoints (e.g., 0.900 vs. 0.516 for side view on seen prompts).

3. **Reward model accurately predicts view-direction alignment**: The fine-tuned reward model improves view-direction classification accuracy from below 10% (original ImageReward) to approximately 90% across all directions, even for unseen objects (Figure 6). This supports the claim that the reward function captures human assessments of view alignment.

4. **Generalization demonstrated through multiple evaluation channels**: The paper provides both human surveys (win rates, view-alignment percentages) and automated metrics (CLIP R-Precision on Color and Normal renderings) across seen and unseen prompts (Table 2, Figures 5a, 5b). The consistency strengthens the evidence for practical improvements in text-to-3D quality.

## Weaknesses

### Fatal

None.

### Major

1. **No ablation studies for key design choices.** The pipeline contains several non-trivial components: reward normalization (softmax over viewpoints), KL penalty, top-20% filtering based on reward, and LoRA-based fine-tuning. None are ablated. It is impossible to determine which component drives the improvement or whether simpler alternatives (e.g., direct rejection sampling without the reward model) would perform similarly. Given that the paper claims methodological novelty for the normalization scheme, this gap is significant. (Section 3.3, Section 4.1)

2. **The 2D view-alignment evaluation uses a circular metric.** Table 1 reports "normalized reward score" from the same reward model that was optimized during fine-tuning. No human evaluation, third-party metric (e.g., CLIP direction consistency), or held-out benchmark is provided for 2D generations. This makes the quantitative 2D results difficult to interpret as independent evidence. The qualitative examples (Figure 2) are helpful but insufficient to establish the degree of improvement. (Section 4.2, Table 1)

### Minor

1. **Motivation-evaluation mismatch regarding 3D-data methods.** The introduction frames the work as overcoming limitations of 3D-data-based approaches (MVDream, Zero-1-to-3): "To overcome this fundamental limitation, we ask the following question: How to improve the geometric consistency of 3D generation without using such 3D data?" However, no 3D-data-based method is included in the experimental comparison — all baselines are DreamFusion variants (DF-IF, DF-PerpNeg). The paper demonstrates that HFDream improves DreamFusion without 3D data, which is a valid contribution, but the stronger framing about overcoming the limitations of 3D-data methods is untested. The paper would benefit from either adding such comparisons or softening the framing. (Sections 1, 4.3)

2. **Reward model validated only on the base model's output distribution.** Figure 6 reports classification accuracy on the reward model's validation set (images from DeepFloyd-IF). If the fine-tuned HFDream produces images with different characteristics, the reward model's accuracy may degrade, potentially leading to reward hacking during fine-tuning and unreliable evaluation in Table 1. The paper does not investigate this distribution shift. (Section 4.4)

3. **The human-annotated dataset is small and lightly documented.** The dataset includes 18 objects, 9 scenes, 162 prompts, and approximately 1200 annotated images per direction. No information is given on the number of annotators, inter-annotator agreement, or how ambiguous cases (e.g., a 45° angle) were handled. The drop in reward scores from seen to unseen prompts (e.g., 0.900 to 0.646 for side view) also suggests the dataset's limited diversity constrains generalization. (Section 3.1, Section 4.2)

4. **Section 4.5 (HFDreamBooth3D) is a tangential qualitative demonstration.** Only two examples are shown with no quantitative evaluation. It does not strengthen the core claims and could be condensed or moved to supplementary. (Section 4.5)

### Trivial

1. **No confidence intervals or error bars.** The quantitative results in Tables 1 and 2 (images) do not report variance across seeds, despite the paper using multiple random seeds. The human evaluation also does not provide variance across raters or prompts.

2. **Win-rate reporting is non-standard.** The paper reports "45%–14%" and "51%–25%" as win-lose rates and calls these "31% improvement" and "26% improvement" (win rate minus lose rate). A more standard approach would report win rate among decisive comparisons, and the tie rates (41% and 24%) are not stated in the text. (Section 4.3)

3. **Minor clarity issues.** The relationship between "KL-O" (cited to Fan et al., 2023) and the objective in Equation 1 could be stated more explicitly. The phrase "original text prompt y" in Section 3.2 is ambiguous about whether it refers to the generation prompt or the reassigned prompt.

## Nice-to-Haves

- A human evaluation for 2D view-alignment (e.g., "which image best matches the viewpoint?") to validate that the normalized reward score translates to perceptible improvement, independent of the reward model.
- A comparison against at least one 3D-data-based method (e.g., MVDream) to support the paper's motivational claims, or alternatively, a revision of the framing to better match the experiments.
- Ablation experiments isolating the contribution of each design component (normalization, KL penalty, reward-based filtering, LoRA).

## Removed Points

These points were identified in the inputs but are removed/relocated for the reasons stated:

- **"The claim that prior work using 3D data 'loses sample diversity and fidelity' is asserted without citation or evidence"** — This is a background motivation claim. The two cited 3D-data methods (Shi et al., 2023; Liu et al., 2023b) are properly cited, and the distribution-shift concern is a widely recognized issue in the field. The claim serves to motivate why the authors pursue an alternative approach, not as a contribution claim requiring independent proof. Removed as it is not a substantive weakness about the paper's own contributions.

- **"Notation is unclear... KL-O from Fan et al. (2023) without defining it"** — The paper explicitly refers readers to Fan et al. (2023) for the full definition. This is standard practice. Removed as a clarity nitpick that cites a paper for details.

- **Various minor phrasing critiques** (e.g., ambiguous wording in Section 3.2 about "original text prompt," the number of unique human-labeled images) — These are minor clarity issues that do not affect the paper's validity and are already addressed or implicit from context. Remaining clarity issues are captured in the Trivial section above.

## Novel Insights

None beyond the paper's own contributions. The reviews do not surface a perspective on the work that the authors themselves do not already articulate.

## Suggestions

1. **Add ablation studies** on at least (a) no reward normalization (raw reward), (b) no KL penalty, (c) random filtering instead of reward-based top-20% filtering, and (d) no LoRA (full fine-tuning or no fine-tuning). Report these on both the 2D reward score and the 3D human evaluation to isolate what drives improvement.

2. **Include at least one 3D-data-based baseline** (e.g., MVDream + DreamFusion) in the 3D comparison, or revise the introduction to avoid claiming to "overcome" the limitations of 3D-data methods without testing against them.

3. **Validate the reward model on HFDream outputs** by collecting a sample of HFDream-generated images, obtaining human viewpoint labels, and measuring classification accuracy to rule out reward overfitting.

4. **Add confidence intervals or error bars** to the quantitative results (Tables 1 and 2) and report variance across seeds.

5. **Expand the human annotation documentation** with the number of annotators, inter-annotator agreement, and handling of ambiguous cases.

6. **Either expand Section 4.5 with quantitative evaluation or remove it** to avoid presenting a thin result as part of the core experimental narrative.

## Score and Decision

The paper proposes a well-motivated and sensible application of human-feedback fine-tuning to improve multi-view generation for text-to-3D synthesis. The core claim — that HFDream improves DreamFusion's 3D outputs — is supported by a human evaluation (win rates, view-alignment percentages) and CLIP-based metrics, which are largely independent of the authors' own reward model. The qualitative results are visually convincing, and the reward normalization is a technically sound design choice.

However, the lack of ablation studies is a significant gap that prevents attribution of improvement to specific components, and the 2D evaluation relies on a circular metric. The paper's contribution is narrower than its motivational framing suggests (no comparison to 3D-data methods). These issues do not invalidate the core findings but do limit the paper's current form.

The paper makes a solid, incremental contribution that would benefit from additional experimental rigor. With reasonable revisions (particularly ablations and metric independence), it would be a strong paper.

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>