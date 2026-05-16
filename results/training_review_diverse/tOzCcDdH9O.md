Now I have all the information needed. Let me produce the final consolidated review.

---

## Summary

This paper introduces Matryoshka Diffusion Models (MDM), a family of diffusion models that perform joint denoising over multiple resolutions using a NestedUNet architecture and a progressive training schedule. The key contribution is enabling end-to-end pixel-space generation at resolutions up to 1024×1024 without cascaded models or autoencoder latent spaces, trained on the modestly-sized CC12M dataset (12M images). The method is evaluated on class-conditional ImageNet generation, text-to-image on CC12M/COCO, and text-to-video on WebVid-10M.

## Strengths

- **Joint multi-resolution diffusion process in an extended space (Section 3.1):** The paper formulates denoising over multiple resolutions simultaneously, where each resolution's noisy latent conditions on all resolutions. This is a clean, principled departure from both cascaded (separate models per resolution) and latent (separate autoencoder) approaches. The non-Markovian property of the resulting backward process is a theoretically interesting point that enriches the modeled distribution.

- **NestedUNet architecture enabling weight and computation sharing (Section 3.2, Figure 4):** The architecture nests low-resolution parameters inside high-resolution blocks, allocating the bulk of computation (attention layers) to lower-resolution feature maps. This provides a concrete mechanism for parameter sharing across resolutions—both methods use the same 64×64 base model, yet MDM outperforms CDM with fewer total parameters and half the inference steps (line 154).

- **Progressive training schedule (Section 3.3):** Training starts at low resolution and gradually adds higher-resolution objectives, which the paper shows (via ablation in Section 4.5) accelerates convergence and improves final quality. This is well-motivated: low-resolution training is computationally cheaper, and the gains transfer to high-resolution performance.

- **End-to-end pixel-space generation at 1024×1024 on a modest public dataset (Abstract, Section 4):** MDM demonstrates that a single pixel-space model can reach 1024×1024 resolution trained on CC12M (12M images), achieving zero-shot CLIP scores on COCO comparable to Imagen (which uses a much larger, non-public dataset). The commitment to using only publicly available, reproducible datasets (CC12M, ImageNet, WebVid-10M) is a genuine strength for the community.

- **Versatility across tasks with a unified pipeline:** The same framework is applied to class-conditional generation, text-to-image, and text-to-video with minimal task-specific changes, suggesting generality beyond image-only settings.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

- **The Cascaded DM baseline comparison is weakened by the paper's own admission about base model training (Section 4.2, line 154):** The paper states that the 64×64 base model used for both MDM and CDM is "not aggressively trained," and that this causes "a large gap between training and inference wrt the conditioning inputs" for the cascaded approach. While both methods use the exact same base model (making the comparison internally fair), the claim that "Cascaded DM significantly underperforms MDM" (which the paper presents as evidence for MDM's superiority) would be stronger if the CDM baseline used a converged 64×64 model as practiced in the cascaded diffusion literature. This is a transparency strength (the authors flag the issue themselves), but it limits how strongly the CDM comparison can be interpreted as evidence of a fundamental advantage of the joint formulation rather than a specific training regime choice.

- **No quantitative evaluation for video generation (Section 4, Figures 7-9):** The video results are presented only as qualitative frames with no metrics (FVD, IS, CLIP score, or any comparison to video baselines). The paper's claim that MDM "generalize[s] gracefully to video generation" would be substantially strengthened by even a single standard video metric. As it stands, the video results are suggestive but not evaluated.

- **Missing computational cost analysis for the efficiency claims:** The paper repeatedly emphasizes efficiency (parameter sharing, computation allocation, progressive training savings) but provides no FLOP counts, per-resolution memory measurements, or wall-clock comparisons between MDM and baselines. Parameter counts are given (450M for the inner UNet), and training hardware is specified (8/32 A100 GPUs), but there is no direct cost comparison (e.g., "MDM uses X GFLOPs vs. Y for CDM" or "MDM trains in Z hours vs. W for Simple DM"). The efficiency argument is qualitative rather than quantitative.

- **The third baseline is incompletely enumerated (Section 4.2, lines 143-144):** The enumerated list of baselines reads "3 / and subsequently train diffusion models that match the dimensions of the MDM UNet." From context (line 153 clarifies this is LDM), the description is understandable, but the broken enumeration suggests a drafting oversight that should be fixed.

### Trivial

- **Prose description of the NestedUNet nesting mechanism (Section 3.2, lines 85-91) is somewhat vague.** The paper states "low resolution latents will be fed progressively along with standard down-sampling" without precisely specifying how the information flows between resolution branches, how parameters are shared, or how the number of resolution levels is handled. Figure 4 and the pseudocode (in the original submission's included file) fill this gap, but the main-text description alone would benefit from a clearer algorithmic statement.

## Nice-to-Haves

- Report FLOPs, per-resolution memory usage, and wall-clock training times for MDM vs. each baseline to substantiate the efficiency claims quantitatively.
- Add a standard video metric (e.g., FVD) on a public video benchmark to support the video generation results.
- Compare the number of function evaluations (NFEs) for MDM vs. cascaded approaches at inference time; the paper notes CDM uses "twice as many inference steps" but a formal NFE comparison would be useful.
- Acknowledge that the extended-space formulation increases the number of latent variables the model must handle, which may complicate convergence or require careful tuning of per-resolution noise schedules.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **"Quantitative results cannot be assessed in parsed text"** — The tables (comparison_sota, comparison_learning, comparison_ablation) and learning curves (Fig. 5, 6) are in LaTeX `\input{}` files stripped by the parser. The original submission has these. Per hard rules: parser artifacts are not author errors.
- **"NestedUNet pseudocode missing"** — The paper says "A pseudo code for NestedUNet... is present as follows" followed by `\input{sections/pseudo}`. The pseudocode exists in the original submission; the parser stripped the included file. Per hard rules: missing included content is a parser artifact.
- **"Ablation results only referenced via figure numbers"** — The ablation tables are in `\input{tables/comparison_ablation}`. Same parser-artifact status.
- **"No evidence for scalability claim about allocating parameters to lowest resolution"** — The paper states this as an "early exploration" finding (line 90) and cites related findings in Hoogeboom et al. (2023). This is a reasonable claim at the level of confidence stated.
- **Claims about missing computational details** (FLOPs, memory, wall-clock) — Partially inaccurate: the paper provides parameter counts (450M), training hardware (8/32 A100 GPUs), and training time (2–5 days in a footnote on line 124). The paper does not provide per-resolution breakdowns or direct baseline comparisons of compute, which is a valid minor weakness (kept above) but the reviewer's framing overstated the absence.
- **"Missing comparison with [reviewer's preferred method]"** — The paper provides controlled comparisons against three baselines (Simple DM, Cascaded DM, LDM), which is adequate for a paper presenting a new method class.

## Novel Insights

The reviews surface a nuanced tension: the paper's key comparative result (MDM > CDM) rests on a comparison where both methods share the same 64×64 base model, yet the CDM baseline likely underperforms relative to what a fully converged cascaded model would achieve. This is not fatal—it is internally consistent—but it means the paper's strongest comparative claim is not yet established at the level the title and framing suggest. The paper's genuine novelty lies elsewhere: showing that a joint multi-resolution formulation with a nested architecture suffices to make pixel-space generation at 1024×1024 practical on a modest dataset, without separate super-resolution stages or autoencoders. This is a finding that stands independently of the CDM comparison.

## Suggestions

1. **Retrain the CDM baseline with a fully converged 64×64 model** (or report the gap between the current CDM and a better-tuned version) to cleanly separate the effect of the joint formulation from training intensity.
2. **Add at least one quantitative video metric** (e.g., FVD on a standard benchmark) to substantiate the video generation claims.
3. **Include a computational cost table** comparing FLOPs, peak memory, and wall-clock time for MDM vs. each baseline to back the efficiency claims with numbers.
4. **Fix the broken baseline enumeration** (line 143-144) and make the third baseline's identity explicit in the enumerated list.
5. **Clarify the NestedUNet nesting mechanism** in prose—specifically how resolution branches connect and how parameter sharing is implemented—so the architecture description is self-contained in the main text.

## Score and Decision

The paper makes a well-motivated and clearly articulated contribution: a joint multi-resolution diffusion formulation with a nested architecture that enables pixel-space generation at high resolutions without cascaded or latent methods. The experimental setup uses publicly available datasets, the ablations are well-structured, and the results (to the extent they can be assessed from the available text) support the main claims. The weaknesses are real but minor—none undermine the core contribution. The CDM baseline concern is internally fair (same base model) but limits the strength of one comparative claim; the missing video metrics and efficiency analysis are addressable gaps rather than structural flaws. The paper merits acceptance.

**Score:** 7.5

MY FINAL SCORE: <pineapple>7.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>