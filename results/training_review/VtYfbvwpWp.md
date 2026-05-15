Here is my consolidated review.

---

## Summary

This paper introduces GoodDrag, a diffusion-based drag editing method with two core technical improvements: (1) Alternating Drag and Denoising (AlDD), which distributes drag operations across multiple diffusion time steps rather than performing them all at once, reducing accumulated perturbation artifacts; and (2) Information-Preserving Motion Supervision (IP), which anchors handle point features to the original starting point to combat the feature drifting problem. The authors additionally contribute the Drag100 benchmark dataset with user-specified masks, a DAI (Dragging Accuracy Index) metric, and a GScore metric leveraging Gemini as an LMM-based evaluator. On both quantitative metrics and a user study, GoodDrag outperforms DragDiffusion and SDE-Drag.

## Strengths

- **The AlDD framework is a well-motivated, effective architectural change.** The core insight — that performing all drag operations at a single diffusion time step causes perturbations too large for subsequent denoising to correct — is clearly explained, and the toy experiment in Fig. 3 provides intuitive support. The ablation in Fig. 8 directly validates this: without AlDD, the edited owl's body shows clear inconsistencies; with AlDD, fidelity is substantially improved. The framework achieves this with no additional computational overhead (same total denoising steps).

- **Information-preserving motion supervision directly addresses a diagnosed failure mode.** The paper identifies feature drifting as the root cause of artifacts and failed point tracking (Fig. 10), traces it to the gradient of the standard motion supervision loss, and proposes a simple fix (anchoring to the original handle point features). The heatmap analysis in Fig. 11(a) quantitatively shows that IP produces more concentrated, higher-variance feature distance maps, and Fig. 11(b) shows a substantially smaller feature distance curve (blue vs. orange). The ablation in Fig. 9 confirms that IP without multiple gradient steps fails, while IP with J=3 succeeds — validating both the solution and the associated engineering choice.

- **Multiple converging lines of evidence.** The paper does not rely on a single evaluation axis. The quantitative results (DAI in Table 1, GScore in Table 2) show substantial gains (DAI at γ=1: 0.0696 vs. 0.1477 for DragDiffusion; GScore: 7.94 vs. 6.87). These are corroborated by a user study with 27 participants (Fig. 7, GoodDrag preferred in both drag accuracy and perceptual quality) and extensive qualitative comparisons across diverse images (Figs. 4–6). The ablation studies separately verify the contribution of each component.

- **The Drag100 benchmark is a useful community contribution.** By providing manually labeled masks and control points across diverse categories and task types, it enables controlled, reproducible "apples-to-apples" comparisons — addressing a real gap in the literature where prior datasets did not provide masks, leading to uncontrolled evaluation.

## Weaknesses

### Fatal
None.

### Major
- **DAI metric is a reasonable but incomplete measure, and its limitations are not discussed.** The DAI (Eq. DAI) computes the MSE between a patch at the original handle point 𝒑ᵢ in the source image and a patch at the target point 𝒒ᵢ in the edited image. This captures whether the source content *moved* from 𝒑ᵢ to 𝒒ᵢ — which is appropriate for relocation and some rotation/rescaling tasks. However, the Drag100 dataset explicitly includes *content removal* and *content creation* tasks (e.g., closing/opening a mouth), where the content at 𝒒ᵢ should differ from the content at 𝒑ᵢ (because new content must be hallucinated or removed). For these tasks, a low DAI does not necessarily indicate success, and the metric does not capture inpainting/creation quality at all. The paper does not provide per-task breakdowns of DAI, so it is unclear how much of the headline improvement in Table 1 is driven by relocation-dominated tasks vs. being robust across all five task types. This is a significant gap in the evaluation. The paper's overall contributions remain supported by the GScore, user study, and qualitative results, but the DAI evidence is weaker than presented.

- **The DragDiffusion* control partially addresses the gradient-step confound but the isolation is imperfect.** The paper compares GoodDrag (70 drags × J=3 gradient steps = 210 total supervision steps) against DragDiffusion* (210 drags × J=1 = 210 total supervision steps). The critic correctly notes that this simultaneously increases the number of *drag operations* (and thus point-tracking steps), which independently affects accuracy. The comparison is actually *conservative* — DragDiffusion* gets more point-tracking steps, which should help it — and GoodDrag still wins by a large margin, so the conclusion is not threatened. However, a cleaner control (DragDiffusion with 70 drags and J=3) would have been more precise. The paper should acknowledge this nuance rather than presenting the control as a complete isolation.

### Minor
- **GScore validation uses a small sample.** The correlation with human judgment (Table 3, Spearman ρ=0.708) is computed on only 12 images processed by 3 methods (36 judgments). While the gap with NR-IQA baselines (TReS 0.250, MUSIQ -0.125, TOPIQ 0.083) is striking, the confidence intervals are wide; a larger study would be needed for the claim that GScore is a fully "validated evaluation protocol." The paper should frame GScore as a promising direction rather than a definitive solution. Additionally, comparing GScore (which uses the original image as reference) against NR-IQA methods (which do not) is not a like-with-like comparison.

- **The Drag100 dataset is dominated by animal images (58/100).** While the paper transparently reports the category distribution and includes 16 landscapes, 10 objects, 6 humans, 5 art, and 5 plants, the heavy skew toward animals limits the claim of comprehensive diversity. The paper does not report per-category breakdowns of DAI/GScore, so it is unclear whether performance is uniform across categories or driven primarily by animal images.

- **The AlDD framework's sensitivity to noise levels is not analyzed.** When AlDD performs motion supervision at different time steps (different noise levels), the U-Net feature maps operate at varying levels of abstraction and receptive field sizes. The paper does not discuss whether this variability affects point-tracking accuracy or convergence behavior.

- **The toy experiment (Fig. 3) uses additive Gaussian noise as a proxy for drag perturbations.** The paper explicitly treats this as a "simulation" and the real evidence comes from the ablation (Fig. 8), but the analogy is imperfect — drag perturbations are structured feature-alignment changes, not i.i.d. Gaussian noise. This can be misleading if taken out of context.

### Trivial
- None.

## Nice-to-Haves
- **Failure case analysis:** The paper shows only successful results. Drag editing can fail in various ways (over-smoothing, incomplete dragging, unrealistic interpolation). A failure case section would strengthen the paper's honesty and help practitioners understand limitations.
- **Hyperparameter sensitivity:** Key parameters (B=10, K=70, J=3) are fixed without sensitivity analysis. It would be informative to know how performance varies with B (number of drags per denoising step) and J (number of gradient steps).
- **Per-category and per-task analysis:** Both DAI and GScore broken down by category (animals vs. landscapes vs. objects) and task type (relocation vs. rotation vs. content creation) would significantly strengthen the evaluation.
- **Measure actual content displacement:** Because IP enforces similarity to the original patch, there is a risk that it might suppress legitimate deformation. Quantifying how far handle points actually moved (displacement magnitude) would confirm that low DAI reflects accurate dragging rather than insufficient editing.

## Removed Points
These points are flagged to be removed; treat them with caution.

- **"IP is a straightforward engineering insight"** — This is a subjective judgment that conflates simplicity with triviality. The paper correctly identifies the problem (feature drifting), traces it to the loss function, proposes a principled fix, and discovers a nontrivial challenge (optimization difficulty requiring J>1). The ablation validates this empirically. This is a genuine contribution regardless of perceived simplicity.

- **"Missing related works"** — Cannot be verified without external sources; removed per instructions.

- **"Typos/formatting/style nitpicks"** — Removed as these are parser artifacts or not substantive.

- **"The DragDiffusion* control entirely fails to isolate the contribution"** — Overstated. The control is informative and conservative (DragDiffusion* gets more point-tracking opportunities and still loses). A cleaner control would be better, but the existing comparison supports the paper's claims, not undermines them.

## Novel Insights
None beyond the paper's own contributions. The reviews surface useful methodological concerns (metric validity across task types, control design for confounding variables, sample size for metric validation) but do not reveal any non-obvious discovery about the method itself that the paper does not already articulate.

## Suggestions
1. **Report DAI and GScore per task type.** Break down the Drag100 results by relocation, rotation, rescaling, content removal, and content creation. This will clarify whether DAI is suitable for all task types and whether GoodDrag's advantage is uniform. It is the single most impactful improvement the authors can make.
2. **Add a cleaner control for the gradient-step confound.** Run DragDiffusion with 70 drag operations and J=3 gradient steps per drag (matching GoodDrag's pattern without AlDD or IP). This would isolate the effect of IP-specific gradient structure from the number of gradient steps.
3. **Expand GScore validation.** Report confidence intervals for the Spearman correlation and ideally validate on a larger sample (≥50 images) to increase statistical reliability.
4. **Add per-category performance analysis** for Drag100 (animals vs. landscapes vs. objects vs. humans) to assess whether the benchmark skew affects conclusions.
5. **Include representative failure cases** and a discussion of failure modes to help users understand the method's limitations.
6. **Quantify handle-point displacement magnitude** to verify that low DAI reflects successful dragging rather than insufficient editing (i.e., that content is actually moving).

## Score and Decision

**Originality:** Moderate. The two main ideas (AlDD and IP) are well-motivated and effective, though individually they are not radical departures from existing approaches. The combined system and the benchmark contributions raise the overall originality.

**Importance of research question:** High. Drag editing is an active area with clear practical value for intuitive image manipulation, and the specific problems addressed (perturbation accumulation, feature drifting) are genuine obstacles to deployment.

**Claims supported:** Mostly. The core qualitative and user study evidence is strong. The quantitative DAI evidence is weakened by the metric's limited suitability for certain task types (content removal, creation). The paper would benefit from per-task analysis.

**Soundness of experiments:** Good overall. The ablations are well-designed and provide insight. The main weakness is the DAI metric's undiscussed limitations and the imperfect gradient-step control. The user study is small but supportive.

**Clarity of writing:** Good. The method is clearly described, the motivation is well-articulated, and the ablation analysis is informative.

**Value to community:** Moderate to high. GoodDrag is a practical improvement that establishes a strong baseline. The Drag100 benchmark and evaluation protocols are useful resources.

Considering all factors: the paper has real technical contributions validated by multiple lines of evidence (ablations, qualitative comparisons, user study, and — with caveats — quantitative metrics). The DAI metric limitation is a significant concern but not fatal, as the paper does not rely on DAI alone. The paper would benefit from revisions to address the per-task analysis gap, but the core contributions are sound and the method is clearly better than prior work.

MY FINAL SCORE: <pineapple>7.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>