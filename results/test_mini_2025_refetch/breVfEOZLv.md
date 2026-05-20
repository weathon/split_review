Here is the consolidated final review.

---

## Summary

This paper investigates weak-to-strong knowledge distillation for vision models. It introduces AdaptConf, an adaptive confidence distillation loss (Eq. 2) that replaces the static hyperparameter α of AugConf (Burns et al., 2023) with a per-sample weight β(x) derived from the cross-entropy discrepancy between the strong model's soft and hard predictions. The method is evaluated across classification (CIFAR-100, ImageNet), few-shot learning, transfer learning, and noisy-label learning, consistently outperforming baselines including AugConf.

## Strengths

1. **Consistent empirical improvements across diverse settings.** AdaptConf outperforms AugConf (the closest prior weak-to-strong method) on every teacher–student pair reported in Tables 2, 3, 4a, 4b, 5, 6, 7, and 8. The improvement is not limited to one architecture or dataset — it holds across CNN families (ResNet, WRN, VGG), lightweight nets (ShuffleNet, MobileNet), ViT-based transfer learning, few-shot learning, and noisy-label scenarios. This breadth of validation supports the claim that dynamic weighting offers practical value over a fixed α.

2. **Method works in the challenging teacher-only (no ground truth) setting.** In Table 4b, where only the weak teacher's predictions are available, AdaptConf improves over the teacher by up to +6.08% (ShuffleNetV1→ResNet32×4), substantially outperforming standard KD baselines. Similarly, in Table 7, AdaptConf achieves +2.15% (ImageNet) and +4.57% (iNaturalist) over the teacher in the teacher-only column. These results demonstrate the method's potential in scenarios where ground-truth labels are absent — arguably the most practically interesting weak-to-strong setting.

3. **Ablation study shows robustness to hyperparameter variation.** Figure 2 demonstrates that AdaptConf achieves higher average accuracy and narrower performance variation than AugConf across different hyperparameter settings, suggesting the adaptive mechanism reduces sensitivity to tuning.

## Weaknesses

### Fatal
None. The paper's core empirical claims — that AdaptConf consistently outperforms baselines — are supported by the reported results. No weakness identified invalidates the experimental findings outright.

### Major

1. **Erroneous summary table (Figure 1) undermines credibility of results presentation.** The radar chart's accompanying table shows identical numbers for ALL baseline methods (KD, FitNet, RKD, DKD, AugConf, Train from scratch) on several tasks: 70.46 on FSL-miniImageNet, 83.86 on TL-ImageNet, 74.16 on CLS-ImageNet-S, 76.64 on CLS-ImageNet-D, 79.63 on CLS-CIFAR-D, and 77.58 on CLS-CIFAR-S. Cross-referencing with the actual data tables reveals these values are not correct averages of the underlying per-method results. For example, in CLS-CIFAR-S (Table 2), the average of AdaptConf across 6 teacher–student pairs is 77.58, but AugConf's true average is ~77.33 and KD's is ~77.04 — yet the table shows 77.58 for all methods. Likewise, on TL-ImageNet, AdaptConf reports 76.94 while every baseline shows 83.86, an inversion of the expected ordering. This is not a formatting nitpick — the table appears to copy one method's column across all rows, producing values that are inconsistent with the paper's own experimental results. This error calls into question the reliability of the numerical reporting in the paper's headline figure.

2. **The adaptive weighting mechanism does not behave as claimed.** The paper states that β(x) enables the strong model to "discern when to prioritize its own predictions over the guidance of the weak model" (lines 142-143). However, the mathematics works in the opposite direction. β(x) = exp(CE(f,f̂)) / (exp(CE(f,f̂)) + exp(CE(f,f_w))), where β weights the self-supervision term. When the strong model is **confident** (CE(f,f̂) ≈ 0) and **disagrees** with the weak model (CE(f,f_w) large), β ≈ 0, placing nearly all weight on the weak model's supervision — exactly when the strong model is most likely correct and the weak model wrong. Conversely, when the strong model is **uncertain** (CE(f,f̂) large), β is larger, increasing reliance on its own uncertain predictions. The paper offers no formal justification for this functional form, and the claimed interpretability ("confidence-based weighting") does not match the math. This does not necessarily invalidate the empirical results — the loss may still act as a useful regularized self-training objective for other reasons — but the paper's central methodological narrative is inconsistent with its actual mechanism.

3. **Missing standard deviations or confidence intervals for main results.** All tables report "average over 3 trials" without variance. Many improvements over AugConf are in the 0.1–0.5 percentage point range (e.g., Table 2: +0.31% on ResNet20→ResNet56, +0.14% on ResNet32→ResNet110; Table 3: +0.36% on ResNet18→ResNet34). Without any measure of variability, it is impossible to assess whether these margins are statistically significant or within run-to-run noise. Given that 3 trials is a small sample, reporting standard deviations is essential for the reader to evaluate the method's reliability.

4. **Missing natural baselines for the teacher-only setting.** In the setting where ground-truth labels are unavailable (Tables 4b, 7 "Teacher" column), the most natural competitor is a self-training / pseudo-labeling baseline (e.g., Lee 2013, confidence-thresholded self-training). The paper compares against standard strong-to-weak KD methods that were never designed for this scenario, and AugConf (the only prior weak-to-strong method). Absent a self-training baseline, it is unclear whether AdaptConf's gains come from the adaptive weighting or simply from the self-supervision term CE(f, f̂) acting as a regularizer, which a simpler pseudo-labeling baseline would also provide.

### Minor

1. **The claim about "surpassing fine-tuning strong models on full datasets" (abstract) is overstated.** On ImageNet transfer learning (Table 7a), AdaptConf with GT achieves 83.86%, while standard fine-tuning of ViT-B/16 from MAE pretraining typically achieves similar values (83–84%). The paper does not include a direct comparison to standard fine-tuning of ViT-B without the weak teacher, making the claim unsupported by controlled evidence.

2. **Teacher-only results are substantially below supervised training, and this is not discussed.** In Table 4b, AdaptConf achieves 72.93% on MobileNet-V2→VGG13 without GT, while the same student trained with full supervision in Table 4a achieves 75.26%. The paper should explicitly acknowledge and discuss this gap, rather than framing all teacher-only results as unqualified successes.

3. **Figure 2 x-axis labeling is confusing.** The caption states that α is varied for AugConf and temperature T for AdaptConf, but the x-axis labels "KD, AugConf, AdaptConf" are categorical, making it unclear what the spread of points within each category represents. The figure is described in text but hard to interpret independently.

4. **The β(x) analysis in Figure 3 is interpreted inconsistently.** The paper states "the proportion of samples with β = 0.5 increases, indicating that the student model's performance is improving and being aligned with the weak teacher's correct classifications." However, Figure 3 shows the highest proportion in the 0.8–0.9 β range, not at 0.5. The text and figure caption both discuss β = 0.5 but the data shows β concentrated near 0.8–0.9, suggesting the strong model heavily weights its own predictions — which is consistent with self-training but at odds with the "alignment with weak teacher" interpretation.

5. **The relationship between Eq. 2's β(x) and temperature T is not defined.** The ablation varies temperature T, explaining it controls "the degree of probability distribution in soft labels during the computation of CE." But the paper never specifies how T enters Eq. 2 — the equation uses raw CE without any temperature scaling term. The default value of T in the main experiments is also not stated.

### Trivial
None. All issues noted above have at least minor substance.

## Nice-to-Haves

- A self-training / pseudo-labeling baseline (teacher-only setting) to isolate the benefit of the adaptive weighting from the self-supervision term.
- Standard deviations for all main results.
- A synthetic or controlled experiment where ground truth is known (which model is correct on each sample) to validate whether β(x) assigns weights sensibly.
- Direct comparison to standard fine-tuning of the strong model without the weak teacher in transfer learning (Table 7).

## Removed Points

- **Criticism about "unconventional Δ definition" in Table 1**: Δ = baseline minus strong is unusual but clearly defined and not ambiguous; removed as a preferential nitpick.
- **Criticism that weak model's hard label f̂_w(x) "appears in text but is not used in equation"**: The variable f_w(x) (soft label) is what's needed in CE; f̂_w(x) is mentioned in passing text but the equation correctly uses soft labels. Removed as a misunderstanding of the notation.
- **Criticism about "CE(f(x), f̂(x)) uses hard label"**: CE with a hard label as target is standard practice (standard classification loss). Removed as factually incorrect.
- **Strength about "beating DKD"**: While factually correct, this is not a genuine strength since DKD was designed for strong-to-weak, making the comparison inherently disadvantageous to DKD. Moved here.
- **"Robustness to hyperparameter variation" strength**: While present, the claim that AdaptConf "shows smaller performance fluctuations than AugConf" is supported but the visual presentation (Figure 2) makes comparison difficult. The strength is partially valid but the evidence is weaker than claimed.

## Novel Insights

Beyond the paper's own contributions, the reviews surface no genuinely novel observation that the paper itself does not already state or imply. The tension between the claimed interpretability of β(x) and its actual mathematical behavior is the most salient insight, but it is a critique rather than a new discovery about the problem domain.

## Suggestions

1. **Fix the summary table (Figure 1).** Replace it with a clean table that correctly reports per-method averages from the underlying experimental tables, or remove the table entirely and keep only the radar chart with proper annotations.

2. **Acknowledge and discuss the β(x) mechanism honestly.** Either revise the narrative to describe what β(x) actually does — e.g., "weights the self-supervision term by exp(CE(f,f̂)), which tends to be small when the model is confident" — or provide a formal justification for why this particular functional form is beneficial. A synthetic diagnostic experiment (e.g., on a binary task where ground truth correctness is known per sample) would significantly strengthen the paper.

3. **Add standard deviations to all tables**, especially where margins are small (<1%).

4. **Add a self-training baseline** (confidence-thresholded pseudo-labeling) for the teacher-only setting.

5. **Provide a direct comparison to standard fine-tuning** (no weak teacher) in the transfer learning experiments to substantiate the claim of surpassing full-dataset fine-tuning.

6. **Clarify the role of temperature T** in the loss — define how it enters Eq. 2 and state the default value used in main experiments.

## Score and Decision

**Round 1 bracketing (three bands, topically similar to weak-to-strong/knowledge distillation):**
- Low band (score < 3.5): papers on W2S/KD scored 2.00–3.33 (withdrawn/rejected) — these papers had fundamental flaws in their core approach.
- Mid band (3.5–7.5): papers scored 5.33–7.25 (mixed accept/reject) — papers with interesting ideas but various limitations.
- High band (> 7.5): papers scored 7.6–8.0 (oral/spotlight) — clean, well-executed papers with strong contributions.

**Initial bracket**: This paper sits between 4.0 and 6.5 — better than the clearly flawed low-band papers but notably less polished/convincing than the accepted W2S papers at 6.5.

**Round 2 narrowing (inside bracket):**
- "Distilling the Knowledge in Data Pruning" (avg 5.33, reject) — clean experiments but limited novelty. Our paper has more novel methodology but has presentation/credibility issues (erroneous table, mechanism mismatch) that make it weaker than this anchor.
- "Multi-stage Decoupled Relational KD" (avg 6.0, reject) — extensive experiments but some execution concerns. Our paper is weaker due to the erroneous summary table.
- "Weak-to-Strong Generalization Through the Data-Centric Lens" (avg 6.5, poster) — clean theory + experiments. Our paper is substantially weaker due to data reporting issues and lack of theoretical grounding.
- "Understanding Calibration Transfer in KD" (avg 4.25, withdrawn) — similar score range with methodological concerns.

Comparing to these anchors: the paper is weaker than the 5.33 "Data Pruning" paper (which, despite limited novelty, had clean presentation and no data errors) but arguably comparable to or slightly stronger than the 4.25 "Calibration Transfer" paper. The erroneous summary table is the decisive factor — it is a credibility issue that papers at the 5+ level typically do not have.

**Final anchors read in full**: LC6ZtQV6u2 (6.5, poster), 4QtywskEyY (6.0, reject), 9ccZzuix2D (5.33, reject), PeLLMw3wLX (6.5, poster), uogG8BfLs2 (6.5, poster), 1xzqz73hvL (7.0, spotlight).

**Final score**: 4.5. The paper's core idea has merit and the broad experimental validation is commendable. However, the erroneous summary table (Figure 1) is a significant data reporting failure that undermines trust in the paper's numerical claims. Combined with the mathematical inconsistency between the claimed mechanism of β(x) and its actual behavior, the missing variance reporting, and the absent self-training baselines, the paper does not meet the bar for acceptance. A major revision correcting these issues could bring it to a competitive level.

**MY FINAL SCORE: <score>4.5</score>**
**MY FINAL DECISION: <decision>Reject</decision>**