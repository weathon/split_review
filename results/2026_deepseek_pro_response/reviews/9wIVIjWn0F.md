Now I have a clear picture from the Round 2 comparison. Let me finalize the review.

**Round 2 comparison summary:**

- **BaFTA (5.50, Reject):** CLIP TTA with online clustering. Our paper is clearly stronger — broader evaluation, simpler method, better results.
- **BAT-CLIP (5.50, Reject):** Bimodal TTA for CLIP. Has a fatal flaw (reviewer alleges ground-truth label usage during TTA). Our paper has no equivalent fatal issue.
- **ML-TTA (6.25, Accept):** Multi-label TTA, directly comparable. Our paper outperforms it on shared benchmarks and has broader evaluation (single-label + cross-domain + multi-label vs. multi-label only), but has an unexplained dimensionality mismatch that ML-TTA doesn't have. Slightly weaker overall.
- **RLCF (6.67, Accept):** CLIP reward TTA. Broader task scope, cleaner methodology. Stronger than our paper.
- **TTE (6.50, Accept):** Weight-space TTA ensemble. Good analysis, well-executed. Stronger than our paper.

Our paper sits between BaFTA/BAT-CLIP (5.50) and ML-TTA (6.25), closer to the lower end due to the unexplained dimensionality issue affecting cross-domain results. Final score: **5.5**.

---

## Summary
This paper proposes Regression-based Test-time Adaptation (RTA), which replaces entropy-based view selection in CLIP test-time adaptation with a learned regression mapping from logit vectors to predicted cross-entropy loss. A lightweight LightGBM decision tree (max depth 5, 16 leaves) is trained once offline on pseudo-labeled ImageNet data, then used at test time to select confident augmented views by predicted loss. The method is evaluated on single-label ImageNet variants, 10 cross-domain datasets, and three multi-label benchmarks, showing consistent improvements over existing TTA methods.

## Strengths
- **Compelling Ceiling TTA oracle experiment (Tables 1–2):** Using ground-truth label cross-entropy for view selection yields enormous gains over entropy (e.g., ViT-B/16 on ImageNet-A: 90.2% LCE vs. 64.3% entropy with 64 views). This directly and convincingly motivates the regression approach and provides a concrete upper bound. This is the paper's strongest contribution.
- **Consistent empirical gains across diverse benchmarks (Tables 3–6):** RTA outperforms compared methods (TPT, DiffTPT, TDA, Zero, BCA, ML-TTA) across single-label, cross-domain, and multi-label settings for both RN50 and ViT-B/16. Gains are substantial on RN50 (+5.73% on ImageNet-A over DiTPT) and on multi-label tasks (+1.43% mAP on MSCOCO over ML-TTA with ViT-B/16).
- **Computationally lightweight design:** The regression model is a shallow decision tree (max depth 5, 16 leaves) trained on only 1,000 samples. Inference adds only a tree traversal per augmented view, in contrast to methods like TPT/DiffTPT that require per-sample gradient-based optimization.
- **Cross-domain generalization (Table 4):** The regression tree, trained on ImageNet-derived data, transfers to 10 diverse cross-domain datasets (Aircraft, Cars, DTD, EuroSAT, SUN, etc.), achieving the highest average accuracy with both backbones.
- **Sensitivity analyses (Figures 4–5):** The paper shows accuracy saturation with respect to number of augmented views and regression training samples, providing useful operational guidance.

## Weaknesses

### Fatal
None.

### Major
- **Unexplained input dimensionality mismatch for cross-domain evaluation:** The regression tree is trained on 1,000-dimensional logits from ImageNet-1k classes (Algorithm 1, Section 4.2). However, cross-domain datasets in Table 4 have different numbers of classes — e.g., Aircraft (100), Cars (196), Pets (37). A decision tree with fixed input dimensionality cannot be directly applied to logit vectors of different lengths. The paper never explains how this mismatch is handled (separate trees per dataset? logits computed against ImageNet class names regardless of the target task? some form of padding?), yet claims the method is "independent of any downstream classification task" (line 330) and requires "only one training session." This affects interpretation of all cross-domain results, which are the primary evidence for the method's generalization claims.

### Minor
- **Missing ablation against max(softmax) view selection:** The regression target is the pseudo-label cross-entropy loss, which for high-confidence pseudo-labels is closely related to `-log(max_softmax)`. The paper never compares RTA against simply selecting views by maximum softmax probability. Without this ablation, it is unclear whether the decision tree adds value beyond a simpler confidence-based selection criterion that uses CLIP's own uncertainty estimate directly.
- **Class overlap between regression set and ImageNet-variant test sets:** ImageVal-12k shares the same 1,000 classes as ImageNet-1k, IN-A, IN-V2, IN-R, and IN-Sketch. The tree could learn class-conditional logit patterns that would not transfer to novel classes, partially undermining the claim of task-independence for the ImageNet-variant results. The cross-domain results (Table 4) partially mitigate this concern.
- **Training on original images, testing on augmented views:** The regression tree is trained on logits from unmodified images (line 126: "the original image itself can actually be regarded as a view"), but at test time receives logits from randomly augmented views. The paper asserts equivalence in a single sentence without evidence that logit distributions are preserved under augmentation.
- **No variance or statistical significance reported:** All tables report single-point accuracy numbers. Some margins are very narrow — e.g., ViT-B/16 cross-domain average: RTA 68.70% vs. BCA 68.59% (0.11% difference) — making it impossible to assess whether differences are statistically meaningful.

### Trivial
- **Notation inconsistency in Section 4.3:** Equations 8–10 use `x_i^reg` superscripts when they should refer to test instances (`x_i^test`), creating confusion between the training and testing stages.
- **No limitations section:** The conclusion restates results without acknowledging limitations such as dependence on a regression dataset or the assumption that logit-to-loss mappings transfer across label spaces.

## Nice-to-Haves
- A characterization of cases where entropy-based selection and RTA disagree would illuminate what the tree learns beyond entropy.
- Ablation on regressor choice (tree vs. linear regression vs. small MLP) would strengthen the design justification.
- Training the tree on a dataset with zero class overlap with the test set would cleanly separate universal from class-conditional logit-to-loss mapping.

## Removed Points
These points were flagged but removed after verification against the paper:
- **"The regression target is essentially a function of CLIP's own confidence — fatal structural issue":** REMOVED as a standalone fatal claim. While the target correlates with CLIP's confidence, the tree operates on the full logit vector (not just the max), and the cross-domain results suggest it may capture richer patterns. The concern is retained as a Minor weakness (missing max-softmax ablation).
- **"The t-SNE and Spearman analyses are unsurprising since logits determine the loss":** REMOVED. This is the paper's motivational evidence, not a claimed contribution. The analysis is reasonable as empirical motivation.
- **"Abstract overpromises" / "'free lunch' framing is promotional":** REMOVED. These are stylistic critiques, not substantive weaknesses.
- **"No ablation on confidence threshold, regressor choice, augmented training":** Partially REMOVED. Demanding all of these is scope creep. The regressor-choice ablation is retained as a Nice-to-Have.
- **"Spearman analysis doesn't cleanly establish regression mapping":** REMOVED. This critiques the motivational analysis, not the method's validity. The paper uses multiple lines of evidence (t-SNE + Spearman + oracle experiment) to motivate the approach.
- **"Equation 8-10 notation is inconsistent" (from harsh critic):** Retained as Trivial.

## Novel Insights
The Ceiling TTA experiment (Tables 1–2) is genuinely insightful: it quantifies how much room for improvement exists beyond entropy-based view selection by using oracle LCE, revealing a gap of 15–25 absolute percentage points on OOD datasets. While the gap's existence is intuitive (knowing the true label helps), its magnitude is striking and provides a concrete upper bound for the entire TTA-by-view-selection paradigm. The paper's observation that this mapping can be approximated from logits alone using a shallow tree trained on diverse pseudo-labeled data is a practical insight, even if the underlying mechanism warrants further investigation.

## Suggestions
- **Critical:** Clarify how the regression tree handles different input dimensionalities for cross-domain datasets. If separate trees are trained per label space, state this explicitly. If logits are always computed against a fixed set of class names for view selection while using target class names only for final prediction, describe the mechanism clearly.
- Add a comparison against max(softmax) as a view-selection criterion — this is the most direct ablation for whether the regression tree adds value beyond CLIP's built-in confidence.
- Report standard deviations or confidence intervals, particularly for narrow-margin comparisons.
- Add a brief limitations paragraph to the conclusion.

## Anchor Comparison

| Anchor | Path | Score | Round | Comparison |
|--------|------|-------|-------|------------|
| Active Test Time Prompt Learning | pdzHpQbGrn | 2.50 | R1-low | Our paper is substantially stronger |
| IEL: Intra-Model Ensemble | 4LiegvCeQD | 2.50 | R1-low | Our paper has much broader evaluation |
| Prototypical Evolution for Few-Shot | ZaudLwn0Hm | 2.50 | R1-low | Our paper has stronger empirical results |
| Multi-Vision Multi-Prompt | j1FLTvgyAh | 2.50 | R1-low | Our paper is substantially stronger |
| ML-TTA (Bound Entropy) | 75PhjtbBdr | 6.25 | R1-mid | Comparable; our paper outperforms it but has an unexplained methodological gap |
| CLIP Reward (RLCF) | kIP0duasBb | 6.67 | R1-mid | RLCF is stronger — broader task scope, cleaner methodology |
| BaFTA | KNtcoAM5Gy | 5.50 | R1-mid/R2 | Our paper is clearly stronger — broader evaluation, better results |
| DOTA | yD2JMeKumt | 6.00 | R1-mid | Comparable; DOTA has cleaner methodology |
| Multi-Modal Reliability Bias | TPZRq4FALB | 8.00 | R1-high | Different category (analysis paper), much stronger |
| Two Effects One Trigger | uAFHCZRmXk | 8.00 | R1-high | Different category (analysis), much stronger |
| Duoduo CLIP | iGbuc9ekKK | 5.75 | R2 | Different topic (3D), not directly comparable |
| BAT-CLIP | z7PhIgVmZU | 5.50 | R2 | Our paper is stronger — no fatal methodological issues |
| Extending to New Domains | tG5mpAM7ZK | 5.33 | R2 | Our paper has stronger evaluation |
| Synergy and Diversity CLIP | Zkq4fsyjfp | 6.25 | R2 | Comparable quality, different topic |
| TTE (Linear Mode Connectivity) | 4wk2eOKGvh | 6.50 | R2 | TTE is stronger — cleaner methodology, better analysis |

**Round 1 bracket:** 5.5–6.5
**Round 2 narrowing:** The paper is comparable to BAT-CLIP/BaFTA (both 5.50, Reject) in terms of being CLIP TTA methods, but avoids their fatal flaws. It is slightly weaker than ML-TTA (6.25, Accept) due to the unexplained dimensionality issue, and clearly below RLCF (6.67) and TTE (6.50). **Final score: 5.5.**

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>