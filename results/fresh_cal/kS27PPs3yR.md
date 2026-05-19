Now I have all the information I need. Let me produce the consolidated review.

## Summary

This paper proposes FAPrompt, a zero-shot anomaly detection (ZSAD) framework that learns *fine-grained abnormality prompts* by introducing two modules: (1) **Compound Abnormality Prompting (CAP)** — each abnormality prompt is formed by sharing the normal prompt's tokens and adding a few learnable abnormal tokens, enabling multiple complementary abnormality representations; and (2) **Data-dependent Abnormality Prior (DAP)** — which selects the top-*M* most abnormal patch embeddings from each test image and injects them into the abnormality prompts as a sample-wise prior, improving cross-dataset generalization. Experiments across 19 industrial and medical datasets show consistent improvements of 3–5% AUC/AP over prior ZSAD methods.

## Strengths

- **Compound prompting design (Eq. 1).** The insight that abnormal patterns are "unexpected patterns overlaying normal patterns" is well motivated, and the design of decomposing each abnormality prompt into shared normal tokens + a few learnable abnormal tokens is a clean, novel way to encourage proximity to normality while capturing diverse abnormal patterns. This is a genuine conceptual advance over single-prototype approaches like AnomalyCLIP.

- **Orthogonal constraint for prompt complementarity (Eq. 2).** The orthogonal loss $\mathcal{L}_{oc}$ enforces diversity among abnormality prompts. The ablation (Table 5) confirms its value: removing it drops industrial image-level AUROC from 88.1 to 87.2 and AP from 87.0 to 86.3, directly supporting the claim that the prompts capture non-redundant patterns.

- **DAP module with the prior learning loss (Eq. 4–5, 7–8).** The idea of deriving a sample-wise abnormality prior from the top-*M* most abnormal patches and the explicit regularization $\mathcal{L}_{prior}$ that suppresses the prior on normal images is well designed. The ablation shows DAP boosts medical pixel-level PRO from 62.9 to 64.8, and removing $\mathcal{L}_{prior}$ degrades it.

- **Extensive and fair evaluation.** The paper compares against 8 methods (both handcrafted and learnable prompts) across 13/14 datasets for image/pixel-level evaluation, plus an ensemble baseline (Table 3). The consistent improvement on most datasets (e.g., BTAD image-level: +3.7 AUROC over AnomalyCLIP; DAGM pixel-level: +2.7 AUROC, +4.4 PRO) substantiates the core claims. The hyperparameter sensitivity analysis (Figs. 5, 6) for *K* (number of prompts) and *M* (selected patches) adds methodological rigor.

- **Disentangled ablation (Table 5).** The ablations isolate CAP alone, CAP w/o $\mathcal{L}_{oc}$, DAP alone, DAP w/o $\mathcal{L}_{prior}$, and the full model, across both industrial and medical domains with both image- and pixel-level metrics. This clearly attributes gains to each component.

## Weaknesses

### Fatal
None.

### Major

- **No error bars or run-to-run variance reported.** All results in the main tables (Tables 1 & 2), the ensemble comparison (Table 3), and the ablation (Table 5) are single-run numbers. For claimed improvements of 3–5% AUC/AP, it is impossible to distinguish genuine gains from favorable initialization or noise. The paper even demonstrates awareness of seed variability by using multiple seeds to construct the AnomalyCLIP ensemble (line 294), yet applies no such analysis to its own method. This is the most significant evidential weakness, as several comparisons involve margins <1% (e.g., MVTecAD pixel-level AUROC: 90.6 vs. 91.1 for AnomalyCLIP; AITEX image-level AUROC: 71.9 vs. 73.0 for WinCLIP).

- **The central claim of "fine-grained abnormality semantics" mapping to specific defect types is not validated.** The paper motivates CAP with examples like "color stains, cuts, holes, and threads on carpet" (line 5–6), but the evaluation only measures aggregate AUC/AP. The t-SNE (Fig. 4) shows that different prompts produce different decision boundaries — evidence of *complementarity*, not evidence that each prompt corresponds to a *semantically distinct defect type*. The orthogonal constraint guarantees the prompt embeddings are numerically diverse, but does not guarantee interpretable specialization. The paper would substantially strengthen its central narrative with a retrieval experiment (e.g., top-5 images per prompt) or anomaly-map visualization showing different prompts firing on different physical defect types.

### Minor

- **No discussion of datasets where FAPrompt lags behind.** On AITEX image-level, WinCLIP (73.0) and AnoVL (72.5) both outperform FAPrompt (71.9). On MVTecAD pixel-level, FAPrompt's AUROC (90.6) is lower than AnomalyCLIP's (91.1), though PRO is higher. The paper states it "significantly outperforms SotA models across almost all datasets" but does not acknowledge or analyze these counterexamples. A brief discussion of failure cases would increase trust.

- **Slight inconsistency in dataset count for ablation.** The ablation (line 319) reports averaging over "18 industrial and medical datasets," but the two main evaluation tables together span 19 unique datasets (9 + 4 + 6). The paper does not explain which dataset is excluded or why, making the ablation numbers harder to verify or reproduce.

- **Training dynamics of the CAP–DAP interaction are underspecified.** DAP selects the top-*M* patches using similarity to $\mathbf{F}_a$ (Eq. 5), where $\mathbf{F}_a$ itself depends on the prompts being learned. The paper does not clarify whether gradients flow through this selection mechanism, whether a stop-gradient is applied, or whether any warm-up/alternation strategy is used. This matters because a hard selection of top-*M* patches through a softmax-based scoring is differentiable but could produce degenerate solutions.

- **No limitations section.** The conclusion (Section 5) summarizes contributions but does not discuss any failure cases, scope limitations, or directions for improvement.

### Trivial
None.

## Nice-to-Haves

- Qualitative analysis of individual prompt specializations (e.g., retrieval or anomaly map visualization per prompt) would directly validate the paper's central motivation and significantly strengthen the narrative.
- A per-dataset breakdown of the ablation results (Table 5) would improve reproducibility over the current aggregate reporting.
- Clarifying in the method section whether the top-*M* patch selection uses straight-through gradients or a soft relaxation would resolve the minor methodological ambiguity.

## Removed Points

- **"Wrapfigure/wraptable formatting issues"** (Harsh Critic, Section-by-Section Notes): This is a formatting/artifact issue caused by the PDF parser. Removed per parser-artifact rule.
- **"AnomalyGPT citation is slightly reductive"** (Harsh Critic): The critic's quibble about whether AnomalyGPT requires "human annotations" vs. "reference samples" does not affect any substantive claim in the paper. Removed as not a real weakness.
- **Strength Finder's claim about the DAGM dataset being "the most direct evidence"**: While factually correct (98.3 vs. 95.6 AUROC), singling out one dataset as the strongest evidence is a judgment call that does not need to appear in the final review. The overall experimental scope is the real strength. Removed as redundant with the broader evaluation strength.
- **"Missing code release"** (Harsh Critic): The reviewer acknowledges this is not required. Removed per instructions (code release is a nice-to-have, not a weakness).
- **Missed opportunity for qualitative analysis**: Moved from "Weaknesses" to "Nice-to-Haves" since it is a suggestion for strengthening, not a flaw in the current paper.

## Novel Insights

None beyond the paper's own contributions. The two reviews largely converge on the same assessment: the method is well designed and the experiments are broad, but the evidence would be substantially stronger with error bars and qualitative validation of the "fine-grained" claim. Neither reviewer identified a hidden flaw or unexpected implication that the paper itself did not surface.

## Suggestions

1. **Add standard deviations** over at least 3–5 random seeds to all main and ablation tables. Even a single supplementary column would substantially raise confidence in the reported gains.
2. **Validate prompt specialization qualitatively.** Show the top-scoring test images for each of the *K* abnormality prompts, or overlay per-prompt anomaly maps, to demonstrate that different prompts capture distinct anomalous patterns (e.g., one fires on stains, another on cuts). This is the most impactful way to strengthen the paper's central narrative.
3. **Discuss the AITEX and MVTecAD pixel-level cases** where FAPrompt does not achieve the best AUROC, explaining why these datasets differ.
4. **Clarify the "18" vs. "19" dataset count** in the ablation and reconcile the numbers.
5. **Add a limitations paragraph** to the conclusion acknowledging scenarios where the method underperforms.
6. **Comment on the training dynamics** of the DAP selection: is the top-*M* selection soft or hard? Does it use a stop-gradient? A brief sentence would resolve the methodological ambiguity.

## Score and Decision

MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>