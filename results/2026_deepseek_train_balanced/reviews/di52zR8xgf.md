## Summary

This paper presents SDXL, a significantly scaled-up latent diffusion model (2.6B-parameter UNet, 817M-parameter dual text encoders) with novel micro-conditioning on image size and crop parameters, multi-aspect-ratio training, and a two-stage refinement pipeline. The model demonstrates clear improvements over prior Stable Diffusion versions in human evaluation and is competitive with black-box state-of-the-art systems.

## Strengths

1. **Controlled ImageNet ablation validates size-conditioning quantitatively** (lines 68-69): The paper provides a clean three-way ablation on class-conditional ImageNet at 512² resolution — *CIN-512-only* (discards images <512px → 70k images), *CIN-nocond* (all images, no size conditioning), and *CIN-size-cond* (all images with size conditioning). *CIN-size-cond* improves over both baselines in FID and IS. This directly isolates the effect of the proposed technique using metrics appropriate for ImageNet (as the FID/IS backbones are trained on ImageNet itself).

2. **User study shows a massive win margin over prior SD versions** (line 111): The pairwise user study reports concrete win rates: SDXL with refiner at 48.44%, SDXL base at 36.93%, SD 1.5 at 7.91%, and SD 2.1 at 6.71%. The gap between SDXL base (36.93%) and the best prior version (SD 1.5 at 7.91%) is roughly a 4.7× margin. This is strong evidence of human preference.

3. **Structured comparison against Midjourney v5.1 on PartiPrompts** (lines 225-236): The paper compares SDXL against a closed-source state-of-the-art model using the PartiPrompts benchmark across 6 categories and 10 challenges, with AWS GroundTruth evaluators. SDXL outperforms Midjourney in 4 out of 6 categories, and in 7 out of 10 challenges there is no significant difference or SDXL outperforms.

4. **Transparent reporting of FID limitations** (lines 248-250): The paper candidly states that SDXL achieves *worse* FID than previous SD versions on COCO despite being preferred by humans, and explicitly backs the findings of Kirstain et al. (2023) that COCO zero-shot FID is negatively correlated with visual aesthetics. This intellectual honesty is a strength — the paper does not cherry-pick metrics.

5. **Crop-conditioning with explicit failure-mode analysis** (lines 71-84): The paper identifies a specific failure mode (cropped objects, e.g., the cut-off cat head in Fig. *comp_old_model*) and proposes a concrete conditioning fix (crop coordinates as Fourier features), showing that setting crop coordinates to (0,0) at inference produces centered objects. This links a clear failure mode to a specific architectural remedy.

## Weaknesses

### Fatal

None.

### Major

1. **Human evaluation methodology lacks sufficient detail to fully bear the evidential burden.** The paper explicitly argues that standard automated metrics (FID, CLIP) are unsuitable for foundation models (Section 7), meaning human evaluation carries the entire burden of proof for the "drastically improved performance" claim. However, the reporting is incomplete: (a) the number of participants and prompts in the main user study (line 111) is not specified; (b) no statistical significance tests, confidence intervals, or inter-rater reliability are reported for either the SD 1.5/2.1 comparison or the Midjourney comparison; (c) the Midjourney comparison reports only a "slight preference" for SDXL without an overall win percentage (line 229). While the reported win rates (SDXL variants at ~85% combined) are compelling in magnitude, the lack of methodological detail weakens the paper's central claim, which rests on these results.

2. **Missing component-level ablations on the final text-to-image model.** The ImageNet ablation for size-conditioning is a reasonable proxy, but the paper does not isolate the marginal contribution of each component (larger UNet, crop conditioning, improved autoencoder, refinement stage) to the final SDXL model's performance. Without this, it is unclear how much of the reported gain comes from architectural scale (a 3× larger UNet) versus the proposed conditioning innovations. The paper's framing implies all components contribute meaningfully, but the evidence does not support this attribution.

### Minor

3. **Midjourney comparison uses a single seed without sensitivity analysis.** Line 228 states Midjourney was run "with a set seed of 2" while SDXL's seed protocol is unspecified. A single seed can arbitrarily inflate or deflate a competitor's apparent performance. This is a nontrivial design choice given the paper's claim of being "competitive with black-box state-of-the-art image generators."

4. **Training hyperparameters for the main model are incompletely reported.** The paper specifies batch size (2048), number of optimization steps, and offset-noise level, but does not report learning rate, optimizer choice, or learning rate schedule. These are standard for reproducibility in model-release papers.

5. **Inference hyperparameters for the main evaluations are not reported.** The ImageNet ablation reports 50 DDIM steps and guidance scale 5 (line 69), but the paper does not specify what sampling steps, guidance scale, or other inference parameters were used for SDXL when generating images for the user studies or Midjourney comparison.

6. **Dataset description is minimal.** The training data is described only as "an internal dataset" (line 103) with a size distribution visualization. No information about dataset size, filtering, deduplication, or safety filtering is provided. For a model release paper, this opacity is a weakness.

7. **Refinement model architecture is unspecified.** The refinement model is described as "a separate LDM in the same latent space" trained on "high-quality, high resolution data" (line 108), but neither its architecture nor its training data composition are described.

### Trivial

None.

## Nice-to-Haves

- Full training hyperparameters (learning rate, optimizer, schedule) for better reproducibility.
- Multiple seeds for the Midjourney comparison to ensure robustness of the preference results.
- Reporting the overall win percentage with confidence intervals for the Midjourney comparison.

## Removed Points

These points are flagged to be removed, treat them with caution:

- Harsh critic's criticism that the architecture description is "hard to follow without the architecture comparison table" — the paper references \Cref{tab:modelarchcomp} which exists in the original submission and likely clarifies the description. This is partially a parser artifact issue.
- Harsh critic's comment that "AWS GroundTruth workers are raters, not expert evaluators" — this is an ad-hominem characterisation; the real substantive issue (lack of inter-rater reliability) is already covered in the Major weakness.
- Harsh critic's comment that "novelty claim is a bit overstated" regarding micro-conditioning — the paper properly cites prior work (Karras et al. 2022, line 84) and frames the contribution as the specific application to LDMs, which is reasonable.
- Strength Finder's generic strengths about the problem being "important" — these lack specific evidence.
- Harsh critic's section note about "readers who only see the abstract will get a one-sided picture" — this is speculative and not a specific weakness of the paper's content.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. Report the number of participants, number of prompts, and statistical significance (or at minimum confidence intervals) for the main user study against SD 1.5/2.1.
2. Provide a controlled ablation on the final text-to-image model that isolates at least the largest contributors (refinement stage, size conditioning, crop conditioning).
3. Use multiple seeds for the Midjourney comparison and report variance, or justify why a single seed is sufficient.
4. Report the inference hyperparameters (sampling steps, guidance scale) used in all evaluations.
5. Release the training hyperparameters (learning rate, optimizer, schedule) for the main model to improve reproducibility.

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>