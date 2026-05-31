Now I have enough information. Let me construct the final review.

## Summary
This paper proposes APPLe, a method for vision-language model adaptation that uses multiple GPT-3 generated prompt prototypes per class to capture visual variance, combined with an adaptive attention mechanism (to downweight flawed prototypes) and a decorrelation loss (to suppress co-occurrence of multiple prototypes). The method is evaluated on base-to-new generalization, few-shot learning, and domain generalization across 11 datasets.

## Strengths

- **Well-motivated idea with supporting analysis (Figure 4)**: The paper identifies a genuine limitation of single-prompt methods — that a singular textual embedding cannot capture the visual variance within a class. The analysis in Figure 4 (varying prototype count from 1 to 50 on ImageNet) directly validates this motivation: at 1 prototype, fine-tuning hurts new-class performance, but with ≥3 prototypes, new-class accuracy surpasses zero-shot CLIP. This is a clean empirical demonstration of the core thesis.

- **Comprehensive evaluation across settings and datasets**: The paper evaluates on 11 datasets spanning coarse, fine-grained, scene, texture, satellite, and action recognition, across three settings (base-to-new generalization, few-shot learning, domain generalization). This breadth allows assessment of the method's general applicability.

- **Ablation study isolating each component (Table 3)**: The ablation on ImageNet decomposes the framework into prototypes, training, attention, max-loss, and decorrelation loss, showing each component's contribution. This provides clear evidence that the full method's performance is not driven by a single factor.

- **Image retrieval analysis (Table 4)**: Using prototypes to retrieve the closest images and measuring mAP provides an interpretable validation that the learned prototypes encode discriminative semantic concepts, beyond just classification accuracy.

## Weaknesses

### Fatal
None.

### Major

- **Attention mechanism for unseen classes is undefined in the base-to-new setting**: The attention matrix is defined as W ∈ ℝ^{C×K} (Line 65-68), making attention weights class-specific. Training is conducted on base classes only (Line 131: "After fine-tuning the prompt prototypes and learning the attention matrix on the base classes"). The paper never explains how attention weights are obtained for classes not seen during training. Since the base-to-new generalization (Table 1) is a central experimental contribution, this gap makes the trained APPLe results in that setting difficult to interpret without clarification. The training-free version (APPLe*) does not train any attention, so it is unaffected, but the paper should clearly describe how its core trained method handles new classes at inference time.

### Minor

- **Numerical claims require cross-verification against the tables**: The abstract claims "3.66% on new classes" and "2.79% on the harmonic mean"; the introduction claims "3.83% performance gain on the new classes" for the training-free version over MaPLe. These are specific quantitative claims that the reader needs to verify against the results tables. The paper should ensure exact consistency between text claims and table values, and clearly distinguish which variant and comparison each number refers to. (Note: the tables are embedded images that cannot be read in the text extraction, so this inconsistency claim by the reviewer could not be independently verified from the extracted text.)

- **No variance or significance estimates**: No standard deviations, confidence intervals, or multi-seed results are reported anywhere. Several claimed improvements are small (e.g., +0.12% at 16 shots). Without variance estimates, it is impossible to assess whether these differences are statistically significant, especially given the large number of datasets and comparisons. While this is common practice in some VLM prompt-tuning papers, it remains a limitation.

- **Writing errors**: Line 123-124 states "PLOT respectively gained ... performance boost over PLOT" — this is a copy-paste error; the sentence should read "APPLe respectively gained ... over PLOT." The introduction (Line 23) also contains a garbled clause ("0.12% PLOT at 1, 2, 4, 8, and 16 shots"). These suggest careless editing.

### Trivial
- The limitations section (Line 170) acknowledges dependence on prompt quality and time complexity, but does not mention the missing explanation of how attention works for unseen classes in the base-to-new setting.

## Nice-to-Haves
- A sensitivity analysis on the number of GPT-3 prompts per class (K) beyond the ImageNet study in Figure 4 would strengthen generalizability claims.
- Reporting prompt generation details (exact GPT-3 prompts used, whether they are dataset-specific, how many per class) would improve reproducibility.

## Removed Points
(These points are from the input reviews but were removed for the reasons stated.)

1. **"Contradiction between text claims and tabulated results" (Harsh Critic, points 2 & 3)**: The reviewer asserts that Table 1 shows APPLe* at New=72.87 vs MaPLe at New=75.14 and APPLe HM=78.70 vs MaPLe HM=78.55, directly contradicting the paper's text claims. These specific table values cannot be verified from the extracted text because Table 1 is an embedded image. The paper's text claims (3.66% on new classes, 2.79% on HM, 3.83% gain for training-free) are stated explicitly and are internally consistent between abstract and main text. Without being able to read the table, the claimed contradiction cannot be confirmed, and the criticism is therefore removed as unverifiable.

2. **"Training-free version does not support the core narrative" (Harsh Critic, point 3)**: The reviewer claims APPLe* is worse than zero-shot CLIP on new classes. The paper explicitly states (Line 125) that "the average performance in new classes surpasses all existing training-based methods" and (Line 23) that "zero-shot CLIP with prompt prototypes can achieve better performance on unseen classes." The specific numbers the reviewer attributes to Table 3 (63.99/66.36 for prototypes-only) cannot be read from the extracted text. Since these claims depend on table values that are not accessible, the criticism is removed.

3. **"Missing appendix content" references**: Removed per filtering rule — the parser strips appendix sections from all papers; they exist in the original submission.

4. **Strength Finder's generic/overclaimed strengths**: Removed generic formulations such as "directly supports the claim" when phrased as mere restatements of paper claims without additional grounding.

## Novel Insights
None beyond the paper's own contributions.

## Suggestions
1. Clarify how the attention matrix W is handled for new classes at inference time in the base-to-new generalization setting — can W be initialized uniformly, or is there a class-agnostic mechanism? Without this clarification, the trained version's base-to-new results cannot be properly evaluated.
2. Add standard deviations or multi-seed results for at least the main experimental settings (Table 1), so that the significance of reported improvements can be assessed.
3. Fix the copy-paste error in Section 5 ("PLOT respectively gained ... over PLOT" → "APPLe respectively gained ... over PLOT") and the garbled clause in the introduction.
4. Ensure exact consistency between numerical claims in the abstract/introduction and the corresponding table values.

## Score and Decision

The paper has a well-motivated core idea and provides a reasonably comprehensive evaluation. The main weakness is a methodological clarification gap: the attention mechanism for unseen classes in the base-to-new setting is not explained, which undermines interpretability of the headline results. Writing quality has minor issues. With proper clarification, the paper could be a solid contribution. In its current form, the paper would benefit from revision.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>