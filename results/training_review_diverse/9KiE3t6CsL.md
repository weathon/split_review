Now I have enough information to construct a thorough, verified review. Let me assemble it.

## Summary

ALBAR proposes an adversarial training framework for debiasing action recognition models against both background and foreground static cues, without requiring bias attribute labels or a separate critic model. The method uses three losses applied to a static clip (sampled and repeated frame): adversarial cross-entropy to penalize static-cue predictions, entropy maximization to prevent label-flipping, and a gradient penalty for regularization. The paper reports a 12% improvement in contrasted accuracy on HMDB51 and identifies/fixes background leakage in the existing UCF101 bias protocol.

## Strengths

1. **Adversarial debiasing without attribute supervision** — The framework eliminates the need for bias attribute labels, pretrained critics, or specialized augmentations by using a single 3D encoder with a static clip sampled from the video itself (Sec. 3.2–3.4, ablation in Table 3). This is a genuine architectural departure from prior work requiring scene/object classifiers or salient-frame detectors.

2. **Large combined debiasing improvement on HMDB51** — ALBAR achieves 53.02% contrasted accuracy on the HMDB51 SCUBA/SCUFO protocol, surpassing StillMix (40.62%) by over 12% (Table 1). This is the paper's central result and the most direct evidence that the method simultaneously reduces both background and foreground bias. Compatibility with StillMix pushes this further to 53.68%.

3. **Identification and correction of background leakage in the UCF101 protocol** — The paper demonstrates that THUMOS-14 bounding boxes used in the prior protocol allow background information to leak into the evaluation (Figure 2) and proposes tighter SAM-Track segmentation masks with manual validation (Sec. 4.2). This is a methodological contribution independent of ALBAR itself.

4. **Component ablation validates each loss term** — Table 3 systematically shows that only the combination of all three losses achieves the best result; the entropy loss prevents the trivial label-flipping solution, and the gradient penalty provides marginal but positive regularization (Sec. 3.3–3.4).

## Weaknesses

### Fatal
None.

### Major
None that are structural or threatening to the core claims.

### Minor

1. **Clarity needed on whether UCF101 baselines were re-evaluated under the new protocol** — The paper states "Results in Table 2 show results on our newly created benchmark" and the caption reads "All experiments use Swin-T pretrained using Kinetics-400." The Implementation Details section says "For all experiments, we use..." the same backbone and augmentations. This language *implies* all methods were re-implemented/re-run under the new protocol, but the paper never explicitly states: "We re-ran all baselines on the new protocol with identical settings." An explicit statement would resolve ambiguity and strengthen credibility, especially since the background leakage fix could asymmetrically affect methods. This is a presentation/clarity gap rather than a structural flaw, and the authors can address it straightforwardly.

2. **Contrasted Accuracy metric partially aligns with the entropy maximization objective** — The Contrasted Accuracy counts a prediction correct iff the model is correct on SCUBA (motion clip) AND incorrect on SCUFO (static clip). ALBAR's entropy maximization explicitly trains the model to have uniform (i.e., incorrect) predictions on static clips, which directly optimizes the SCUFO component of the metric. While this is *part of the intended behavior* (the goal is to not rely on static cues), and while the SCUBA accuracy and ARAS evaluation are separately reported and not confounded, the paper would benefit from explicitly separating how much of the contrasted accuracy gain comes from better motion features (SCUBA) vs. the entropy-induced uniform predictions on SCUFO. The authors could plot SCUFO entropy across methods or control for static-clip entropy during evaluation.

3. **Downstream task gains are marginal and lack error bars** — The improvements on UCF-Crime (AUC: 82.19→82.40, +0.21) and THUMOS14 (mAP: 66.4→68.0, +1.6) are small, with no variance or significance tests (Table 5). The paper also does not justify why HMDB51 debiasing transfers to surveillance anomaly detection or sports action localization. This evidence is too weak to support broad downstream-benefit claims. The authors should either add error bars across multiple seeds, strengthen the analysis, or temper the claims and relegate this to supplementary material.

4. **No error bars on main bias-evaluation results** — While the paper reports "average Top-1 accuracy across 3 runs," no standard deviations or confidence intervals are provided for any table (Tables 1–4). Given small absolute differences in some comparisons, this makes it difficult to assess whether improvements are statistically reliable.

5. **Framing around demographic bias is not supported by evaluation** — The introduction mentions "harmful sources, such as a person's physical appearance attributes like skin color, facial hair etc." as foreground bias, raising expectations that the paper evaluates demographic fairness. The evaluation only measures static appearance bias through SCUBA/SCUFO protocols (background replacement, static frames). The Limitations section acknowledges this gap, but the framing in the introduction could misleadingly imply demographic fairness evaluation. The authors should either evaluate demographic bias or scope their claims more precisely in the introduction.

### Trivial

1. The paper refers to "SCUFA" instead of "SCUFO" in one instance (line 93), though the meaning is clear from context.
2. The gradient penalty loss contributes only ~1 point and "does not have a large effect on its own" (row d, Table 3) — this is noted in the paper but the statistical significance of this contribution is unclear.

## Nice-to-Haves

- A 2×2 factorial ablation (adversarial × entropy) would cleanly separate the interaction of the two main loss terms, beyond the existing row-by-row presentation in Table 3.
- A discussion of training time / memory overhead from the gradient-penalty backward pass would help practitioners assess practical costs.
- A "motion-only" evaluation (e.g., blacking out background entirely) could provide additional evidence that the model relies on motion rather than static cues.

## Removed Points

These points are flagged for removal per hard rules. Treat them with caution.

- **"Sections 3.1–3.2 are missing / equations not fully specified"** — The extracted text jumps from Section 2 to Section 3.3 due to PDF parser stripping. The original paper contains the full method (Eq. 1, Eq. 2, Sec. 3.1–3.2). This is a parser artifact, not an author omission.
- **"Missing appendix content"** — References to appendices (e.g., "C for results on the existing benchmark") refer to content stripped by the parser; the original submission contains these sections.
- **"Weakness about qualitative results being merely illustrative"** — Qualitative integrated-gradient visualizations (Figure 3) are presented as illustrations, not as primary evidence; this is standard practice and not a weakness.
- **Weaknesses about the ablation not being a clean 2×2 factorial** — The existing ablation (Table 3) tests each component individually and in combination, which is a standard and reasonable design. The requested 2×2 factorial is a presentation preference, not a flaw.
- **Strength from Strength Finder about "demonstrated downstream task benefits"** — This strength conflicts with verified Weakness #3 (downstream gains are marginal/no error bars). Per rules, the weakness wins; the strength is dropped.
- **"Re-ran vs. prior-publication numbers"** concern from the harsh critic treated as fatal — The paper's language ("For all experiments," "All experiments use Swin-T") strongly implies re-implementation; the lack of an explicit statement is a clarity gap, not a structural flaw.

## Novel Insights

The key insight from synthesizing these reviews is that the method's elegance (single encoder, no external critic, no bias labels) also creates a subtle evaluation challenge: because the entropy loss directly targets static-clip predictions, the metric that counts *incorrect* static-clip predictions as correct (Contrasted Accuracy) partially rewards behavior the loss was designed to produce. This makes it especially important to separately verify that SCUBA accuracy (which requires genuine motion understanding) also improves, and to include error bars so readers can assess whether the combined metric gain is driven more by the motion or static component. The paper does report SCUBA accuracy separately and includes ARAS evaluation, but the community would benefit from a direct analysis that decomposes the contrasted accuracy gain.

## Suggestions

1. Add an explicit statement to the camera-ready version: "All baselines were re-implemented/re-run using the same backbone, augmentations, and training hyperparameters on our new UCF101 protocol."
2. Report standard deviations across the 3 runs for all metrics in Tables 1–4.
3. Include an analysis that separates the contrasted accuracy gain into its SCUBA and SCUFO components, showing that SCUBA accuracy also improves independently.
4. Either add multiple-seed evaluations with error bars to the downstream tasks (Table 5) or soften the claims about downstream benefits.
5. In the introduction, avoid raising expectations about demographic bias evaluation unless it will be evaluated; scope the foreground bias discussion to the actual evaluation (static appearance cues).

## Score and Decision

The paper proposes a well-motivated method and reports a strong 12% improvement on HMDB51 contrasted accuracy, which is the main result. The UCF101 protocol fix is also a valid contribution. The identified weaknesses (metric-alignment concern, lack of error bars, marginal downstream eval) are real but none threaten the paper's core claims. All concerns are addressable in a camera-ready revision.

**Score: 6.5** (Accept)

MY FINAL SCORE: <pineapple>6.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>