Now I have all the information I need to produce the consolidated review.

## Summary

This paper introduces Matryoshka Diffusion Models (MDM), an end-to-end framework for high-resolution image and video synthesis. MDM proposes a joint diffusion process over multiple resolutions in an extended space, combined with a NestedUNet architecture where lower-resolution features and parameters are nested within higher-resolution computations. The method enables progressive training from low to high resolutions and achieves pixel-space generation at up to 1024×1024 resolution without cascaded or latent stages, demonstrating competitive results on class-conditioned ImageNet generation, text-to-image on CC12M, and text-to-video on WebVid-10M.

## Strengths

1. **Novel formulation of joint multi-resolution diffusion with nested architecture.** The paper formalizes a diffusion process over an extended space of multiple resolutions (Section 3.1), where the denoising of each resolution depends on all resolutions jointly. The NestedUNet architecture (Section 3.2) shares parameters and computation across resolutions, so that low-resolution processing is nested within the high-resolution stream. This is a well-motivated design that directly addresses the computational challenges of high-resolution diffusion without cascaded or latent stages.

2. **Progressive training provides measurable convergence improvements.** Section 3.3 describes a progressive training schedule that gradually adds higher-resolution objectives. The ablation in Section 4.3 shows that increasing low-resolution pre-training iterations monotonically improves high-resolution FID curves. The main experimental comparisons (Section 4.2) demonstrate that MDM with progressive training converges faster and achieves better final FID than both Simple DM (standard UNet) and Cascaded DM baselines, with the latter using more combined parameters and twice the inference steps.

3. **Demonstrates 1024×1024 pixel-space generation from a modest dataset (CC12M, 12M images).** The paper trains a single pixel-space model at 1024×1024 resolution on the publicly available CC12M dataset and reports competitive zero-shot FID/CLIP scores on COCO, with maximum CLIP score similar to Imagen (trained on much larger datasets). The explicit choice of CC12M for reproducibility is a community-conscious decision.

4. **Versatility across domains.** The same MDM framework is applied to class-conditional image generation (ImageNet 256×256), text-to-image (CC12M 256×256 and 1024×1024), and text-to-video (WebVid-10M 16×256×256) with minimal changes, demonstrating generality beyond a single task.

## Weaknesses

### Fatal

None.

### Major

1. **Insufficient operational differentiation from f-DM (Gu et al. 2022).** The paper acknowledges that f-DM's scheduler is "employed in our work" (Section 5, Related Work) and that the noise schedule follows f-DM (Section 3.1). However, the paper never explicitly states *how MDM differs operationally* from f-DM. Does f-DM also perform joint denoising across resolutions, or is its process sequential? Does f-DM use parameter sharing across scales? Without this clarification, a reader familiar with f-DM cannot assess whether MDM's claimed novelty (joint multi-resolution denoising + NestedUNet) represents a genuine advance over the closest prior framework or a relatively incremental modification. The paper needs to state, ideally in a bullet or a small table, what the key architectural and procedural differences are. This is the most significant weakness because it blurs the novelty boundary.

### Minor

1. **Prose relies on vague quantitative language instead of stating key numbers inline.** The paper repeatedly describes results as "comparable results to prior works," "better performance," and "strong zero-shot generalization" without citing specific FID or CLIP scores in the narrative. While tables exist in the original submission (the text references `\cref{tab:literature}`, `\cref{fig:baseline_curves}`, etc., which are in separate files the parser could not include), the prose itself should anchor the reader with at least the headline numbers. For example, stating "MDM achieves FID X on ImageNet 256×256 vs. Y for Simple DM" would let the reader immediately grasp the improvement without finding Table 2.

2. **Video generation evaluation is entirely qualitative.** The paper presents video results (Section 4.2, Figure 6) only through sample visualizations. No quantitative metric (e.g., FVD, CLIP score for video) is reported. Since video is presented as evidence of the method's versatility, the absence of any standard quantitative evaluation weakens this claim.

3. **Progressive training wall-clock speedup is asserted but not measured.** The paper claims that progressive training "greatly speeds up the training of high-resolution models w.r.t. wall clock time" (Section 3.3) and the overall training time is noted as "2-5 days... with 4 nodes of 8 GPU A-100 machines" (Section 4.1), but no controlled comparison of wall-clock time to final FID for MDM with vs. without progressive training is provided. The convergence curves show FID improvement per iteration, but the efficiency advantage in real time—a key selling point—remains unsubstantiated.

4. **No baselines of other methods trained on CC12M.** The paper argues that CC12M is preferable as a community benchmark and uses it for text-to-image training, but all literature comparisons are against models trained on much larger datasets. It would strengthen the paper to provide at least one reference baseline (e.g., a Simple DM or standard LDM trained on CC12M under similar conditions) so the reader can contextualize whether MDM is strong or CC12M is simply easier.

### Trivial

None.

## Nice-to-Haves

- A small table or bullet list explicitly contrasting MDM and f-DM on key design dimensions (joint vs. sequential denoising, parameter sharing, architecture type, training schedule) would cleanly resolve the novelty boundary question.
- Including wall-clock training time to reach a given FID for MDM with and without progressive training would substantiate the efficiency claim.
- A single quantitative video metric (e.g., FVD) on a standard video benchmark would strengthen the claim of generality.

## Removed Points

These points were identified by the reviewers but are removed per the filtering rules. They are recorded here for transparency:

- *Criticism that quantitative results are not visible because tables are in separate files (Critical Issue 1, first half)* — The tables are present in the original submission via `\input{}` commands. The parser could not include these files, but they exist. The remaining concern about vague prose is kept as Minor #1 above.
- *Criticism about NestedUNet architecture details relying on pseudocode/figures not visible* — The pseudocode is in a separate `\input{}` file and figures are images; these are parser artifacts, not author omissions.
- *Criticism about missing comparison to published FID scores from end-to-end baselines (Hoogeboom et al.)* — The paper has a `comparison_sota` table comparing against literature and describes Simple DM as equivalent to Hoogeboom et al. The comparisons exist; this point overstates the gap.
- *Strength Finder strength about "strong text-to-image generation" being fully supported* — Partially removed because the paper does not state specific FID numbers inline; the strength overstates what the visible text alone confirms. The core claim is retained in Strength #3 but qualified.

## Novel Insights

None beyond the paper's own contributions. The reviews do not surface any observation about MDM that the paper does not already articulate.

## Suggestions

1. **Clarify the relationship with f-DM explicitly.** Add a short paragraph or table in Section 3 comparing MDM and f-DM on the forward process structure (joint vs. sequential), architecture (NestedUNet vs. what f-DM uses), parameter sharing, and training schedule. This single change would resolve the most significant uncertainty about the paper's novelty.

2. **State the headline FID/CLIP numbers inline in the prose.** Add one sentence to Section 4.2 such as: "MDM achieves FID X on ImageNet 256×256, compared to Y for Simple DM and Z for Cascaded DM; zero-shot FID on COCO is A with CLIP score B." This makes the empirical contribution tangible without requiring the reader to find the right table.

3. **Add a wall-clock time vs. FID plot for the progressive training ablation.** A simple figure showing training time on the x-axis and FID on the y-axis for MDM with and without progressive training would substantiate the efficiency claim concretely.

4. **Include at least one quantitative metric for the video experiment** (e.g., FVD on a standard subset of WebVid-10M or UCF-101) to validate that the model learns temporal structure beyond plausible single frames.

## Score and Decision

MY FINAL SCORE: <pineapple>6.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>