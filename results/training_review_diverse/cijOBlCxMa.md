Now I have a thorough understanding of the paper and can verify each reviewer claim against the actual text. Let me compose the final consolidated review.

## Summary

This paper introduces CustomNet, a zero-shot object customization method that integrates 3D novel view synthesis (via Zero-1-to-3) into text-to-image diffusion models. The method adds explicit viewpoint control (camera pose parameters [R,T]), location control (concatenating the reference object at a user-specified bounding box), and flexible background control (via a dual cross-attention module accepting text or a reference image). A data construction pipeline using natural images (OpenImages) with Zero-1-to-3 synthesized novel views is also proposed. The paper claims state-of-the-art identity preservation and viewpoint diversity compared to both optimization-based (DreamBooth, Textual Inversion) and encoder-based (BLIP-Diffusion, ELITE, GLIGEN) methods.

## Strengths

- **Novel integration of 3D viewpoint control into object customization.** The paper correctly identifies that prior encoder-based methods suffer from a copy-pasting effect because they lack explicit 3D awareness. Building on Zero-1-to-3 to add viewpoint conditioning is a well-motivated architectural choice, and the ablation (Fig. 5, right) shows that removing [R,T] indeed collapses to copy-pasting while adding it enables viewpoint variation while preserving identity.

- **Dual cross-attention for disentangled object and background control.** The paper introduces a clean design that feeds object features and text features through separate cross-attention modules. The ablation (Fig. 6, 5th column) shows that without this separation, viewpoint control degrades because object and background conditioning become coupled. This is a practical contribution for unified customization.

- **Data construction pipeline from natural images.** The "reverse" pipeline — segmenting objects from natural images, synthesizing novel views with Zero-1-to-3, and using the original image as the target — is a clever way to obtain realistic training pairs. The ablation (Fig. 6, 4th column) shows that without it, training on Objaverse+simple blending produces floating artifacts.

- **Unified framework with three simultaneous controls (viewpoint, location, background).** The paper demonstrates (Fig. 7) that all three controls can be exercised together, which no prior zero-shot customization method achieves in a single model.

## Weaknesses

### Major

- **No confidence intervals or variance estimates for any automatic metric.** The paper evaluates "26 different prompts on 50 objects 3 times" — 3,900 generations — yet reports DINO-I, CLIP-I, and CLIP-T as single point estimates without standard deviations, standard errors, or confidence intervals. This makes it impossible to assess whether CustomNet's advantages are statistically reliable. The gap in CLIP-I between CustomNet (0.8164) and GLIGEN (0.8152) is only 0.0012 — with no error bars, the reader cannot tell if this difference is meaningful or noise. This weakens the paper's central performance claims.

- **User study methodology is opaque.** The paper reports "2700 answers" and per-metric preference percentages (78.78% for identity similarity, etc.) but provides no details on: number of participants, question format (pairwise comparison vs. Likert rating), whether comparisons were blinded, how objects/prompts were sampled for each participant, or any measure of inter-rater agreement. The results are anomalously lopsided (CustomNet 78.78% vs. DreamBooth 13.33% for identity) without methodological transparency. This makes the user study difficult to interpret as rigorous evidence.

- **Ablation studies are exclusively qualitative.** All five ablation analyses (viewpoint control, pretraining initialization, input concatenation, data pipeline, dual cross-attention) are demonstrated only through cherry-picked visual examples (Figs. 5 and 6). No quantitative metrics (DINO-I, CLIP-I, or even a small-scale user rating) are reported for any ablation condition. This leaves the individual contribution of each design component at the level of visual anecdote rather than systematic evidence.

### Minor

- **DreamBooth comparison details are underspecified.** The paper states "Dreambooth requires several images of the same object to finetune" but does not specify how many images were used per object, whether these were generated from a single reference (standard practice in diffuser implementations) or drawn from multiple viewpoints, or whether the reference image used for evaluation was among the training set. This makes it harder to assess whether the comparison is fair — DreamBooth evaluated with held-out identities vs. CustomNet using the same reference as input could differ systematically.

- **Resolution confound with baselines.** CustomNet operates at 256×256 (inherited from Zero-1-to-3). Most baselines (DreamBooth, BLIP-Diffusion, etc.) operate at 512×512. The paper acknowledges this in its limitations but does not discuss how it may affect the comparison. Lower resolution could penalize texture preservation metrics, making the comparison less apple-to-apple.

- **Dual cross-attention mechanism under-specified.** The description states that object features and text features go through "two distinct cross-attention modules," with query features Q from the UNet, and object/text key-value pairs separately. However, the paper does not specify how the two attention outputs are combined (summed, concatenated, gated, alternated). The equation intended to formalize this (Eq. 2) is an empty environment in the extracted text (a parser artifact), but even from the prose the exact mixing mechanism is not sufficiently specified for reproduction.

### Trivial

- None.

## Nice-to-Haves

- Reporting failure cases (objects with complex geometry, extreme viewpoints > 90°, reflections) would strengthen the paper's honesty and help future work.
- A quantitative comparison for the location control component (e.g., measuring how precisely the output bounding box matches the target) would strengthen the location control claim.

## Removed Points

These points are flagged to be removed, treat them with caution:

- **"User study numbers given to two decimal places implies unjustified precision"** — This is a formatting/style nitpick. The decimal precision is standard reporting practice and does not affect the validity of the numbers.
- **"Empty equation (2)"** — This is a PDF extraction parser artifact, not an author error. The surrounding text (Q, K_o, V_o, K_b, V_b) describes the intended computation.
- **"The paper does not report the split between Objaverse-derived and OpenImages-derived data"** — The paper explicitly states "(250+500)K data pairs," which communicates the 250K Objaverse / 500K OpenImages split.
- **"Location control is not ablated independently"** — The paper does ablate location control via the "w/o Concat" condition in Fig. 6 (3rd column), which is precisely an ablation of the concatenation-based location mechanism.
- **"More informative comparison would include DCI / Cut-and-Paste spatial layouts"** — This is a request to add missing comparisons with methods not evaluated. The paper's comparison set (DreamBooth, Textual Inversion, BLIP-Diffusion, ELITE, GLIGEN, SD-Inpainting, Paint-by-Example) is already reasonable for the claimed scope. Such additions would constitute scope creep.
- **"The paper does not compare alternative location encodings"** — The paper proposes a specific location mechanism (concatenation) and ablate it. Demanding comparison with all alternative encodings (positional embeddings, location tokens) is scope creep for a single-method paper.

## Novel Insights

None beyond the paper's own contributions. The reviews surface the standard tension between a novel, well-motivated idea and an evaluation that does not yet meet the rigor needed to fully support the claims. No reviewer identified an insight the paper itself missed about the problem or method.

## Suggestions

1. **Add standard deviations or confidence intervals for all automatic metrics.** With 50 objects and 3 seeds, you have ample samples to report DINO-I and CLIP-I as mean ± std per metric. This single addition would substantially strengthen the quantitative evaluation.

2. **Document the user study methodology.** Report: number of participants, whether pairwise comparisons were blind, how objects/prompts were sampled per participant, the exact question wording, and whether each metric was evaluated in separate or joint comparisons. If the study used a particular platform (Amazon Mechanical Turk, etc.), specify it.

3. **Add a quantitative ablation table.** For each of the five ablation conditions (w/o [R,T], w/ SD ckpt, w/o Concat, w/o DataPipeline, w/o DualAttn), report DINO-I and CLIP-I on the same evaluation set. Even a smaller-scale measurement (e.g., 10 objects × 10 prompts) would be far more informative than visual cherry-picks alone.

4. **Specify the DreamBooth setup.** State the number of training images per object, whether they were single-view augmented versions or multi-view captures, and whether the reference image was withheld from training.

## Score and Decision

**Originality:** Good — integrating 3D novel view synthesis into customization with explicit viewpoint control is a novel direction.  
**Importance of research question:** High — overcoming the copy-pasting effect in customization is a recognized problem.  
**Support for claims:** Moderate — claims are plausible and partially supported, but key evidence (metrics variance, user study details, quantitative ablations) is missing or under-documented.  
**Soundness of experiments:** Moderate — the experimental design is reasonable in scope but lacks statistical rigor and methodological transparency.  
**Clarity of writing:** Good — the paper is well-structured and the motivation is clear.  
**Value to the community:** Potentially high if the evaluation gaps are addressed; as-is, the technical contributions are clear but the empirical case is incomplete.

The paper addresses an important problem with a novel and well-motivated approach. The architectural contributions (viewpoint control, dual cross-attention, data pipeline) are technically sound. However, the experimental evaluation has significant gaps that prevent the paper from making a fully convincing empirical case: no variance reporting for any automatic metric, an opaque user study, and exclusively qualitative ablations. These issues are fixable but are not minor — they cut across the entire results section. The paper cannot be accepted in its current form, but the core ideas merit further development.

MY FINAL SCORE: <pineapple>4.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>