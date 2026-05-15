Now I have a thorough understanding of the paper and all the reviews. Let me produce the final consolidated review.

**Quick verification of the harsh critic's key claims against the paper:**

1. **Metrics/viewpoint contradiction** — The paper uses DINO-I and CLIP-I following standard practice (BLIP-Diffusion). The user study (64.67% view variation preference) provides complementary evidence. DINO and CLIP are not perfectly viewpoint-specific; they learn some invariance. The tension exists but is not fatal.

2. **DreamBooth fairness** — The paper states "Dreambooth requires several images of the same object to finetune" (line 176) and uses "diffuser implementations" but never specifies how many images per object or whether the same single image was used. Valid concern.

3. **Quantitative ablations** — All ablations in Figs. 3-4 (paper's Fig. 3 and Fig. 4, labeled `fig:ablation_RT_control` and `fig:ablation_latent_concat`) are qualitative only. Valid concern.

---

## Summary

CustomNet introduces explicit 3D viewpoint control (via camera parameters [R,T]) into zero-shot object customization by building on Zero-1-to-3, adding location control via input concatenation, flexible background control via dual cross-attention (text or image), and a dataset construction pipeline that leverages natural images for harmony. The key claim is that explicit viewpoint control is the "missing ingredient" that enables simultaneous viewpoint variation and identity preservation without copy-pasting artifacts.

## Strengths

- **Explicit 3D viewpoint control is convincingly shown to be the key design choice.** The ablation (Fig. 4, `fig:ablation_RT_control`) demonstrates that removing the camera-pose condition [R,T] causes the model to collapse to copy-pasting, while including it enables diverse viewpoints with identity preserved. This directly supports the paper's central claim.

- **Dual cross-attention mechanism effectively disentangles foreground and background conditions.** The ablation (Fig. 5, `w/o DualAttn`) shows that a single shared cross-attention module couples viewpoint and background control, degrading both, while the dual design preserves both controls independently.

- **Dataset construction pipeline (reverse pipeline) demonstrably improves harmony.** The ablation (Fig. 5, `w/o DataPipeline`) shows that training without the natural-image pipeline produces objects that appear "floating" on backgrounds, whereas the proposed pipeline yields harmonious compositions. The idea of using Zero-1-to-3 itself to generate training pairs from natural images is clever.

- **Input concatenation of the transformed reference object provides fine texture preservation.** The ablation (Fig. 5, `w/o Concat`) shows loss of color, shape, and texture fidelity when removed, supporting the design choice.

- **User study provides direct subjective evidence for the core claims.** 78.78% of participants preferred CustomNet for identity similarity, 64.67% for viewpoint variation, and 67.84% for text alignment, with all baselines scoring below 14% in each category. This strengthens the qualitative demonstrations.

- **Zero-shot operation without test-time optimization** is a practical advantage demonstrated by the evaluation protocol, where no per-object fine-tuning is performed.

## Weaknesses

### Fatal
None. The paper makes a plausible technical contribution and no single issue invalidates its core claims.

### Major

- **DreamBooth comparison lacks sufficient detail to ensure fairness.** The paper states "DreamBooth requires several images of the same object to finetune" (Sec. 4.2) but does not specify (a) how many images were provided per object for the 50 evaluation objects, (b) whether these were from different viewpoints or augmented copies, or (c) whether the same single reference image was used for all methods. Since DreamBooth is the strongest baseline in the comparison (the only other method achieving "highly promising harmonious customization results" per the paper itself), this omission undermines confidence in the headline quantitative gap (DINO-I 0.7742 vs. 0.6333). The paper should disclose DreamBooth's input configuration explicitly.

- **The tension between the identity metrics and the viewpoint change claim is not adequately addressed.** CustomNet achieves *higher* DINO-I and CLIP-I than DreamBooth (0.7742 vs. 0.6333) while also claiming to produce larger viewpoint changes. Since DreamBooth tends to keep the viewpoint fixed (copy-paste), one would expect its identity similarity scores to be at least comparable under equal conditions. The paper does not discuss why this is not the case — for example, whether metrics are computed only on foreground regions (which would be reasonable but is not stated), whether the viewpoint changes in the evaluation are actually modest, or whether DreamBooth's known overfitting problems from single-image input explain the gap. The user study partially addresses this (64.67% view variation preference) but the paper should reconcile the numbers directly.

### Minor

- **All ablation studies are presented qualitatively only.** Figures 3–4 (the ablation figures) show image comparisons without reporting DINO-I, CLIP-I, or CLIP-T for the ablated variants. This makes it impossible to assess the statistical reliability or magnitude of each design choice's contribution. Quantitative ablations are standard for this type of analysis.

- **The user study protocol is not described.** The paper reports collecting 2700 answers and high preference percentages but does not specify the number of participants, how images were presented (side-by-side? randomized order?), whether participants were familiar with the task, or any measures to avoid bias. This limits the interpretability of the user study results.

- **Comparison to inpainting-based methods (SD-Inpainting, Paint-by-Example) is only qualitative.** A quantitative comparison (e.g., foreground-background harmony scores or identity preservation metrics for these methods) would strengthen the claim that CustomNet improves over these alternatives.

- **The CLIP-T score (0.2258) is slightly below ELITE (0.2310)** without discussion of whether this difference is meaningful or statistically significant.

### Trivial

- The text contains a minor typo: "obatain" instead of "obtain" (line 178).

## Nice-to-Haves

- **Viewpoint-specific quantitative evaluation** — Reporting angular error (mean absolute rotation error between predicted and ground truth viewpoint) or viewpoint classification accuracy would directly measure viewpoint change fidelity and resolve the tension with identity metrics.
- **Quantitative ablations** — Adding DINO-I/CLIP-I/CLIP-T for each ablation variant would substantially strengthen the paper.
- **Failure analysis** — Discussing cases where CustomNet fails (extreme viewpoints, complex geometry, non-rigid objects) would improve trust in the method.
- **Statistical significance for Table 1** — Confidence intervals or error bars for the main metrics would help assess whether differences are reliable.

## Removed Points

These points from the reviewers are flagged to be removed; treat them with caution:

- **"The equation for dual attention (Eq. 8) is empty"** — The extracted text shows an empty `\begin{equation}` environment (lines 119–121), but this is a PDF parsing artifact. The surrounding text clearly describes the mechanism. The original submission contains the formula.
- **"Ablation does not ablate the scale of multi-view pretraining (training from scratch vs. Zero-1-to-3)"** — This demands analysis of an orthogonal design choice beyond the paper's stated scope. The paper already ablates the SD checkpoint vs. Zero-1-to-3 initialization (Fig. 5, `w/ SD ckpt`).
- **"DINO/CLIP encoders are not viewpoint-invariant" as a fatal flaw** — DINO and CLIP are standard identity-preservation metrics in the field precisely because they learn some viewpoint invariance. The concern is not unfounded but is overstated as a fatal issue; the user study and the paper's own ablations provide supporting evidence.
- **"Missing related works"** — No external sources confirm what is missing; this is speculative.
- **Formatting/style nitpicks** — Parser artifacts and trivial presentation issues.

## Novel Insights

None beyond the paper's own contributions. The reviews do not surface insights about the paper that the authors themselves have not already identified or discussed.

## Suggestions

1. **Disclose DreamBooth's input configuration explicitly.** How many images per object, from what sources, and whether the same single reference image was used as for all other methods. If multiple images were used, describe how they were obtained.
2. **Add a brief discussion reconciling the identity metric scores with the viewpoint change claim.** Either note that metrics are computed on the foreground region (if so, state this), or discuss why high identity scores are not contradictory with viewpoint change (e.g., DINO/CLIP are imperfect measures of viewpoint but capture identity well, the evaluation prompts may involve modest viewpoint changes, etc.).
3. **Provide quantitative measurements for at least the key ablation variants** (e.g., DINO-I/CLIP-I for w/o RT, w/o Concat, w/o DataPipeline, w/o DualAttn). Even a single-table summary would significantly strengthen the ablation study.
4. **Describe the user study methodology briefly** (number of participants, presentation format, randomization).

## Score and Decision

The paper makes a clear technical contribution — incorporating 3D novel view synthesis into object customization with well-motivated architectural designs. The weaknesses are real but addressable: the DreamBooth fairness concern and the metrics/viewpoint tension need clarification, and the ablations need quantitative support. None of the weaknesses are fatal. The paper should be accepted after these clarifications are made.

MY FINAL SCORE: <pineapple>7.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>