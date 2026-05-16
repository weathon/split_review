Now I have thoroughly verified the paper against the reviewer claims. Let me produce the final consolidated review.

## Summary

Self-TPT introduces a test-time prompt tuning framework for vision-language models that replaces expensive per-image adaptation with text-only self-supervised learning on the target class names. The key innovation is Contrastive Prompt Tuning (CPT), which creates multiple views of each class name by varying token position in the prompt sequence and applies contrastive learning on the text embeddings. The paper also contributes a gradient correlation analysis showing that CPT gradients align positively with classification gradients, and a gradient matching loss to further enhance this alignment. Self-TPT achieves state-of-the-art accuracy across cross-dataset, base-to-new, and domain generalization benchmarks while being 25× faster and using 30× less memory than prior TPT methods.

## Strengths

- **Dramatic and well-documented efficiency gains**: Table 1 shows Self-TPT achieves 146.7 FPS (vs. 5.3 for PromptAlign) with 0.32 GB memory (vs. 11.2 GB) on CLIP-B/16. Even the augmented variant Self-TPT-v (29.3 FPS, 0.66 GB) maintains a substantial advantage. These numbers directly deliver on the paper's core goal.
- **State-of-the-art accuracy across three benchmarks**: Self-TPT-v achieves 67.85% (cross-dataset, +0.93% over PromptAlign), 77.47% (base-to-new, +1.21% over PromptSRC+TPT), and 65.38% (domain generalization, +1.82% over PromptAlign) per Tables 2–4. The gains are consistent across datasets, not driven by outliers.
- **Novel and principled text-only adaptation paradigm**: By restricting test-time adaptation to class names only (Section 3.2), Self-TPT eliminates the per-image computation fundamental to all prior TPT methods. This is a genuinely different approach that the paper transparently describes and motivates.
- **Empirical gradient correlation analysis**: Figure 2 demonstrates positive cosine similarity between CPT and classification gradients across 10 of 11 datasets. This provides a principled explanation for why the text-only SSL task aids classification — a stronger justification than typical ad-hoc auxiliary losses.
- **Thorough ablation and versatility studies**: Tables 5a–5c ablate each component (CPT, TTA, GM) individually, confirming all contribute. Tables 6–7 show the method transfers across backbones (RN50, RN101, ViT-B/32, ViT-B/16, ViT-L/14), to EVA-CLIP, and maintains performance with only 25% of source data. This breadth strengthens confidence in the method's generality.
- **Data efficiency insight**: The analysis of source data quality (Figure labeled Fig. 5 in the paper) showing that class diversity matters more than per-class instance count is practically useful for deployment scenarios.

## Weaknesses

### Fatal
None.

### Major

- **The accuracy comparison conflates two different forms of adaptation.** In cross-dataset and base-to-new settings, Self-TPT adapts prompts to the target class names via CPT — a signal that prior TPT baselines (TPT, PromptAlign, DiffTPT) do not use. These baselines adapt to image content via entropy minimization or prediction agreement, which is a fundamentally different source of information. While the paper mentions this difference (Section 3.2: "decoupling the test-time adaptation from specific test samples"), it does not discuss how this affects the fairness of direct accuracy comparisons. The 0.93% cross-dataset improvement over PromptAlign, for example, could reflect the benefit of class-name adaptation rather than superiority of the CPT formulation itself. The ablation (Table 5a) partially addresses this by comparing CoOp vs. CoOp+CPT+TTA, but the main comparison tables (2–4) do not include a baseline that also performs class-name-level adaptation without the full SSL machinery, making it difficult to isolate what drives the gains. The domain generalization results (Table 4, +1.82%) are cleaner because the label set is identical across source and target, so the advantage cannot come from new-class adaptation and is a genuine strength.

### Minor

- **No variance estimates reported.** All results are averaged over three seeds (line 223), but no standard deviations, confidence intervals, or per-seed breakdowns are shown. Given that some margins are narrow (e.g., 0.93% on cross-dataset, and several per-dataset differences are <1%), the statistical significance of individual improvements is unclear. This is standard practice in the prompt learning literature but still limits the reader's ability to assess result stability.

- **Architecture of the SSL projection head h not specified.** The paper introduces h(·) in Eq. 5 (line 115) and uses it for the CPT loss, but never states its architecture (e.g., number of layers, hidden dimensions, activation functions). Since h is jointly trained (θ_h appears in the optimization) and affects the text features used for contrastive learning, this omission hinders full reproducibility.

- **EMA decay rate α not reported.** The gradient matching loss (Eq. 7, line 179) uses an exponential moving average of gradients with decay rate α. The value of α is never disclosed. This is a hyperparameter that should be reported for reproducibility.

- **Gradient Matching loss provides only modest gains.** The GM loss adds +0.1% (generic), +0.4% (fine-grained), and +1.5% (specialized) over the already strong CoOp+CPT+TTA baseline (Table 5a). While the improvement direction is consistent, the mechanism is not deeply validated — e.g., there is no analysis of whether gradient matching can ever hurt, or whether the improvement is statistically significant given the small magnitude.

### Trivial
- The gradient matching loss (Eq. 8, line 184) uses 1 − cos similarity but is only applied in Stage 1 (source training). The paper could make this explicit in the main text rather than requiring the reader to infer it from the ablation tables.

## Nice-to-Haves
- A controlled baseline that has access to target class names and performs a simple text-based adaptation (e.g., tuning prompts on class names with a basic clustering or similarity-based loss) would isolate whether CPT's specific SSL formulation or simply having class-name adaptation drives the gains. The ablation already does some of this (CoOp+CPT vs. CoOp), but a simpler non-SSL class-name adaptation would further clarify.
- Reporting per-seed results in an appendix would help assess the stability of the improvements, especially on the few datasets where Self-TPT underperforms the baseline.

## Removed Points

These points are flagged to be removed; treat them with caution.

1. **"The method solves a substantially different problem" / "fundamentally skewed comparison" — OVERRULED.** The paper is transparent about its text-only adaptation in Section 3.2. The end task is identical (classify target images accurately), and both Self-TPT and baselines have access to target class names (line 88: TPT operates on unlabeled test data with "candidate class names"). The difference is in how class names are used, not whether they are available. The critic's framing that "Self-TPT has access to target class names and PromptAlign does not" is factually incorrect — PromptAlign uses class names to compute classification probabilities and entropy. Removed because it misrepresents what the baselines do.

2. **"The paper does not analyze whether CPT views are discriminative enough" — OVERRULED.** Table 5b systematically ablates each of the four CPT views (front, mid, end, hand-crafted) by removing one at a time, showing performance degradation when any view is removed. This directly analyzes the contribution of each view. The critic missed this ablation.

3. **"GM loss only used during Stage 1, not during test-time adaptation" — OVERRULED.** The GM loss requires gradients from both the classification loss (labeled) and CPT loss. Stage 2 (test-time) has no labels, so classification gradients cannot be computed. The criticism ignores the fundamental constraint of the setting.

4. **"0.93% margin is small" — DOWNGRADED.** This is an opinion, not a weakness. 0.93% average improvement across 10 diverse datasets is a meaningful gain in this benchmark landscape.

5. **"The gradient correlation analysis doesn't consider if matching gradients ever hurts" — NOT A WEAKNESS.** The paper shows Table 5a where GM consistently improves or maintains performance across all three dataset categories (generic, fine-grained, specialized). No degradation is observed, which is sufficient evidence that it does not hurt in practice.

6. **"CoOp+TPT/MaPLe+TPT exhibit unstable performance gains" — This is an observation the paper itself makes (lines 346-349) and uses to motivate Self-TPT's more stable design. Not a weakness.

## Novel Insights

None beyond the paper's own contributions. The reviews do not surface a perspective on the paper that the authors have not already presented.

## Suggestions

1. Report the architecture of the SSL projection head h and the EMA decay rate α in the main text or appendix. These are small omissions but matter for reproducibility.
2. Add a note in the main comparison sections (Tables 2–4) explicitly stating that Self-TPT performs class-name adaptation that baselines do not, and briefly discussing how this might affect the comparison. The current paper mentions this in the method section but does not flag it for readers looking at the performance tables.
3. Include per-seed breakdowns or standard deviations in an appendix, particularly for the cross-dataset results where margins are tight.

## Score and Decision

The paper makes a genuine contribution: a novel text-only self-supervised approach to test-time prompt tuning that is both more efficient and more accurate than existing per-image methods. The experiments are extensive (11 datasets, 3 benchmarks, multiple backbones, EVA-CLIP, data efficiency studies), the ablations are thorough, and the efficiency gains are dramatic and well-documented. The main weakness is that the accuracy comparison does not fully disentangle the effect of class-name adaptation from the effect of the specific CPT formulation, though the ablations partially address this. The paper is well-written, the idea is clearly motivated, and the results support the claims. The missing implementation details (projection head architecture, EMA decay rate) are minor and easily fixed.

**Score: 7.0** — A solid paper with clear contributions and thorough evaluation. The main framing issue is real but does not undermine the contribution; it merely means the paper would benefit from more precise claims about what the comparison demonstrates.

MY FINAL SCORE: <pineapple>7.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>