Now I have a thorough understanding of the paper. Let me construct the consolidated review.

---

## Summary

CustomNet integrates 3D novel view synthesis (from Zero-1-to-3) into object customization for text-to-image diffusion models. It enables simultaneous control over viewpoint (via explicit camera parameters [R,T]), location (via concatenating a transformed reference image to the UNet input), and background (via a dual cross-attention mechanism accepting text or a reference background image). The method is trained on a combination of Objaverse multi-view data and a constructed pipeline from OpenImages natural images, and operates zero-shot at inference. Ablations confirm that the explicit viewpoint parameters are critical for producing diverse outputs rather than copy-paste effects.

---

## Strengths

1. **Explicit viewpoint control enables simultaneous identity preservation and viewpoint variation.** The ablation in Fig. 7 (Fig. 5 in the paper) directly demonstrates this: without the [R,T] parameters, CustomNet collapses to copy-pasting. With them, the model generates genuinely different views while retaining identity. This is the paper's clearest and best-supported contribution.

2. **Well-designed dual cross-attention for disentangled object and background control.** The ablation in Fig. 6 (5th column) shows that replacing dual cross-attention with a single shared cross-attention degrades viewpoint control and hinders background generation, validating the design choice.

3. **Data construction pipeline improves output harmony.** The ablation in Fig. 6 (4th column) shows that training without the proposed reverse pipeline (using Zero-1-to-3 to generate novel views from natural images) yields "floating" artifacts, while the full pipeline produces more natural compositions. This is a practical contribution for training customization models on natural image datasets.

4. **Zero-shot operation without test-time optimization.** Unlike DreamBooth and Textual Inversion, CustomNet requires no per-object fine-tuning, making it dramatically more practical. This is correctly highlighted and verified in the experimental setup.

---

## Weaknesses

### Fatal
None.

### Major

1. **No error bars, variance, or confidence intervals on any automated metric.** The paper reports point estimates (DINO-I, CLIP-I, CLIP-T) for 50 objects × 26 prompts × 3 random seeds, but does not report standard deviations. For generative models with stochastic sampling, this is a significant gap — the reported differences between methods cannot be assessed for statistical significance. This is especially important given the large DINO-I gap between CustomNet (0.7742) and DreamBooth (0.6333), which is architecturally explainable (CustomNet concatenates the reference to the UNet input, giving it direct pixel access) but needs variance reporting to be properly evaluated.

2. **User study protocol is critically underspecified.** The paper reports "collected 2700 answers for Identity similarity (ID), View variation (View), and Text alignment (Text)" with results of 78.78%, 64.67%, and 67.84% preference for CustomNet. No details are given on: number of participants, whether comparisons were pairwise or multi-way, whether the study was blinded, how pairs were constructed/randomized, or which methods were compared against each other. Without these details, the extremely lopsided results (CustomNet 78.78% vs. DreamBooth 13.33% on identity) are hard to interpret. This is the single most significant evaluation weakness.

3. **Missing quantitative comparison against the most directly relevant baseline: two-stage Zero-1-to-3 + inpainting.** The paper acknowledges this baseline (Sec. 3) and presents only one qualitative comparison (Fig. 5) against SD-Inpainting and Paint-by-Example. Since CustomNet's core idea is to integrate Zero-1-to-3 with background/location control into a single model, a quantitative comparison against the two-stage pipeline (Zero-1-to-3 → inpainting) on the same metrics and user study is the most natural and important baseline. The current evidence is insufficient to justify the unified design over the simpler alternative.

### Minor

1. **Training data pipeline uses Zero-1-to-3 outputs as reference images without analyzing distribution shift.** For the OpenImages portion of training data (line 139), the reference object image fed to the model is a Zero-1-to-3 generated novel view, not a real image. This means the training distribution includes outputs of the same model whose viewpoint-conditioning it inherits. The paper does not ablate whether the model generalizes meaningfully beyond Zero-1-to-3's distribution or simply learns to reconstruct natural images from Zero-1-to-3 style references. At minimum, testing on references from a different novel-view method (or real multi-view captures) would strengthen the generalization claim.

2. **No quantitative evaluation of viewpoint control accuracy.** The paper claims explicit viewpoint control but never directly measures whether the generated viewpoint matches the specified [R,T] (e.g., computing angular deviation between the generated object's pose and the target pose). The only evidence is qualitative (Fig. 7/Fig. 5) and the user study's "View" preference score is subjective. A direct quantitative evaluation would substantially strengthen the core claim.

3. **DreamBooth setup is underspecified.** The paper states DreamBooth "requires several images of the same object to fine-tune" (line 176) but does not specify the exact number used, training steps, or hyperparameter settings. Given that DreamBooth is the strongest identity-preservation baseline, this matters for fairness of comparison.

### Trivial

- The dual cross-attention equation (Eq. 2) appears as an empty equation environment in the extracted text. This is likely a PDF parsing artifact; the surrounding text describes the formulation adequately.

---

## Nice-to-Haves

- A simple control experiment measuring DINO-I on a direct copy-paste (same view, same location) would calibrate the upper bound of the metric and contextualize CustomNet's 0.7742 score.
- Reporting failure cases where viewpoint control fails (e.g., symmetric objects, extreme angles) would help calibrate expectations.
- A quantitative metric of object-background harmony (e.g., CLIP score between object region and background, or a learned realism scorer) could strengthen the data pipeline ablation.

---

## Removed Points

These points are flagged to be removed — treat them with caution:

- **"The DINO-I gap is implausible / the comparison was staged."** Removed because it is factually incorrect: the architectural difference (concatenating the reference to the UNet input vs. not) naturally explains why CustomNet achieves higher identity similarity metrics. This is not a sign of unfair evaluation; it is an expected consequence of the design.
- **"Viewpoint control claim is overstated since it inherits from Zero-1-to-3."** Removed because the paper's contribution is integrating viewpoint control into customization, not inventing novel viewpoint control. Many papers build on prior components. The paper is transparent about its lineage.
- **"Missing Eq. 2."** Removed because the empty equation is a PDF text-extraction artifact. The surrounding text clearly describes the dual cross-attention mechanism.
- **"Reproducibility: should specify which UNet blocks, whether the object cross-attention receives fused CLIP+[R,T] embedding, etc."** Removed because these are standard implementation details that are either inferable from the architecture (inherited from Zero-1-to-3) or beyond what is normally expected in a conference paper.
- **"The paper should include standard deviation / confidence intervals."** Not removed — this is valid and kept as a Major weakness. (The *specific* phrasing requesting "confidence intervals for large-scale benchmarks" was evaluated; the original concern about missing variance was legitimate.)
- **Strength from Strength Finder: "State-of-the-art quantitative identity preservation" — DINO-I and user study results.** Kept as a strength, but the caveats about architectural advantage and underspecified user study are noted.
- **Strength from Strength Finder: "Zero-shot operation without test-time optimization."** Kept as valid.
- **Generic strengths ("important problem," "timely direction")** from Strength Finder were removed as they lack concrete, specific evidence directly cited from the paper.

---

## Novel Insights

The reviews surface a tension not fully articulated by the paper: the architectural mechanisms that boost identity preservation (concatenating the reference to the UNet input) and the training data pipeline (using Zero-1-to-3 outputs as references) each introduce confounders that are not separately controlled for. The concatenation gives CustomNet a built-in advantage on pixel-level identity metrics that has nothing to do with viewpoint modeling, while using Zero-1-to-3 outputs during training means the model may be learning to operate within a distribution it helped create. These two factors together mean that the paper's headline quantitative results (the large DINO-I gap and the strongly lopsided user preference) may be partially driven by design choices that are orthogonal to the claimed contribution of viewpoint-aware customization. A clean evaluation would need to control for both: measure DINO-I with the reference *not* concatenated, and test generalization on references from a different novel-view generator.

---

## Suggestions

1. **Report standard deviations** for all automated metrics in Table 1, computed across objects or random seeds.
2. **Provide a detailed user study protocol** — number of participants, pairwise vs. multi-way design, blinding procedure, and how the 2700 answers break down per comparison pair.
3. **Add a quantitative comparison against the two-stage baseline** (Zero-1-to-3 → inpainting with SD-Inpainting or Paint-by-Example) on the same metric set.
4. **Directly evaluate viewpoint control accuracy** — e.g., compute the angular deviation between the specified [R,T] and the estimated pose of the generated object.
5. **Ablate the training data pipeline more thoroughly** — test on references from a different novel-view model (e.g., a NeRF-based method) to measure generalization beyond Zero-1-to-3's distribution.

---

## Score and Decision

The paper makes a genuine technical contribution: integrating explicit viewpoint control into object customization via a clean architecture with location and background control. The ablations convincingly show that the viewpoint parameters are necessary for diverse outputs. However, the evaluation has significant gaps — no variance reporting, critically underspecified user study, and the most relevant baseline (two-stage Zero-1-to-3 + inpainting) is only qualitatively compared. These weaknesses weaken but do not invalidate the core contribution. The paper would be considerably strengthened by addressing them in a revision.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>