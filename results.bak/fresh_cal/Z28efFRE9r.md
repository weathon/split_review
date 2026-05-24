Now I have all the information needed. Let me compile the final consolidated review, carefully verifying each claim against the paper.

---

## Summary

AuthFace proposes a two-stage blind face restoration (BFR) framework: (1) fine-tuning StableDiffusion-XL on a curated dataset of 1,500 extremely high-quality (8K+) facial portraits with photography-guided captions, yielding a face-oriented generative diffusion prior; (2) training a ControlNet adapter with a time-aware latent facial feature loss that weights eyes and mouth regions more heavily at intermediate diffusion steps where their shapes emerge. Experiments on synthetic (CelebA-Test) and three real-world datasets (LFW-Test, WebPhoto-Test, WIDER-Test) show leading performance on multiple non-reference perceptual metrics (LPIPS, MANIQA, MUSIQ, CLIPIQA).

## Strengths

- **Face-oriented fine-tuning concretely improves facial detail generation.** The ablation study (Table 2, exps a vs b) shows that replacing the original SDXL prior with the fine-tuned version raises CLIPIQA from 0.6465→0.7088 on CelebA and MUSIQ from 67.01→72.35 on WebPhoto. The T2I generation example in Fig. 2(b) visualizes sharper skin texture and clearer facial features from the fine-tuned model — concrete evidence that the small curated dataset meaningfully adapts the prior.

- **Time-aware latent facial feature loss reduces artifacts and outperforms constant weighting.** In Table 2, the time-aware variant (exp d) outperforms the constant-weight variant (exp c) on all four real-world metrics (e.g., MANIQA 0.6624 vs 0.6449 on CelebA; MUSIQ 75.76 vs 73.66). The qualitative comparison (Fig. 5/ablation figure) shows visible reduction of artifacts in eye and mouth regions. The weight formula (Eq. 3) is grounded in the logit-normal sampling from Stable Diffusion 3 and in the empirical observation of when facial shapes emerge (Fig. 3).

- **First place on multiple non-reference perceptual metrics across several benchmarks.** On CelebA-Test (Table 1), AuthFace achieves the best LPIPS (0.2143), MANIQA (0.6624), MUSIQ (75.76), and CLIPIQA (0.7065). On real-world datasets, it leads in MANIQA on LFW-Test (0.6431, exceeding the next best by 0.09), WIDER-Test (0.5941), and WebPhoto-Test (0.5860). These consistent wins across independent non-reference metrics support the claim of perceptually authentic results.

- **Photography-guided annotation is well-motivated for the task.** The paper identifies that for face-oriented fine-tuning, semantic-only captions (accessories, attributes) are insufficient because cropped/aligned face images share similar semantics but vary in photographic style. Using LLaVA-1.6 to generate tags capturing lighting, skin texture, and sharpness (Fig. 2a) is a thoughtful design choice specifically tailored to this domain.

## Weaknesses

### Fatal

None.

### Major

- **Missing identity preservation evaluation.** The paper's core claim is achieving "authentic" face restoration, yet no identity similarity metric (e.g., ArcFace cosine similarity, FaceNet distance) is reported on any dataset. Identity preservation is arguably the most important dimension of authenticity — a restored face that looks visually pleasing but alters identity is not authentic. Without this measurement, the reader cannot distinguish whether the method genuinely recovers the subject's appearance or generates a plausible but different face using the fine-tuned prior. This gap directly undermines the paper's central framing and needs to be addressed for the contribution to be fully validated. *(Verified: metrics listed in Sec. 4.1, lines 234–236, include PSNR, SSIM, LPIPS, MUSIQ, MANIQA, CLIPIQA, FID — no identity metric.)*

### Minor

- **Loss formulation shows sensitivity that warrants discussion.** The ablation study (Table 2) reveals that constant-weight facial feature loss (exp c) degrades performance on several metrics compared to no facial loss at all (exp b): PSNR drops from 25.59→23.95, MUSIQ from 74.42→73.66. While the paper acknowledges this pattern (lines 338–340), the sensitivity raises the question of how carefully the time-weight parameters (*m*, *s* in Eq. 3) were selected and whether the approach requires dataset-specific tuning. The paper would benefit from discussing this fragility more directly.

- **FID performance lags on synthetic and some real-world benchmarks.** On CelebA-Test, AuthFace's FID (50.93) is substantially worse than SUPIR (35.01) and BFRffusion (40.74). On LFW-Test and WebPhoto-Test, FID also trails SUPIR and CodeFormer respectively. Since FID measures distributional fidelity, this gap — while not fatal given the paper's focus on non-reference perceptual metrics — suggests the method may produce outputs that are perceptually appealing but less faithful to the natural image distribution in some settings.

- **Limitation section is incomplete.** The limitation paragraph (lines 352–354) only discusses the labor cost of data collection, omitting the identity evaluation gap, the FID gap, the sensitivity of the time-aware loss, or potential overfitting concerns with a 1.5K fine-tuning set. A more comprehensive discussion would strengthen the paper's scholarly honesty.

- **No variance or statistical significance reported.** Given that some margins between methods are small (e.g., MUSIQ 75.76 vs CodeFormer's 75.56 on CelebA, CLIPIQA 0.7065 vs BFRffusion's 0.6863), reporting variance across runs would help assess whether differences are meaningful.

### Trivial

None.

## Nice-to-Haves

- Adding identity similarity metrics (ArcFace cosine similarity, FaceNet distance) on both synthetic and real-world datasets — this would directly test the "authentic" claim and is the single most impactful addition.
- Showing more than one T2I generation sample from the fine-tuned prior (Fig. 2b) to demonstrate diversity and rule out memorization of the 1.5K training set.
- A brief ablation or analysis on the effect of fine-tuning dataset size to substantiate the claim that 1.5K high-quality images suffice.

## Removed Points

*These points were flagged in the reviews but are removed here because they are inaccurate, speculative, or do not survive the filtering criteria.*

- **"Paper does not discuss the PSNR/CLIPIQA trade-off in the ablation."** — The paper explicitly discusses this at lines 338–340. Removed as factually incorrect.
- **"Dataset sufficiency and overfitting concern."** — The paper cites LIMA (Zhou et al., 2024) and Emu (Dai et al., 2023) as precedent showing that small, high-quality fine-tuning sets suffice. The concern is speculative without evidence. Removed.
- **Novelty critique ("fine-tuning SD for faces is not new").** — This is a generic judgment rather than a specific, verifiable weakness. The paper's specific combination (quality-first curation + photography-guided annotation + time-aware regional loss for BFR) is identifiable as a contribution. Removed.
- **"Pioneers a new approach" overclaim.** — This is a stylistic choice about tone, not a verifiable weakness in the paper's technical content. Removed.
- **Any concern about code/dataset availability.** — The paper states "Codes and datasets will be available upon acceptance." This is a standard statement. Removed as a false concern.

## Novel Insights

Beyond the paper's own contributions, the review surfaces a recurring tension in the BFR evaluation paradigm: the metrics used to demonstrate "authentic" restoration are dominated by general-purpose perceptual image quality assessments (MANIQA, MUSIQ, CLIPIQA) — none of which explicitly measure whether the restored face preserves the identity of the original subject. This means a method could rank highly on these metrics while subtly altering identity, making them insufficient for validating the "authentic" claim. This is not a weakness unique to AuthFace but a broader evaluation gap in the field that the paper inherits and could help address by adding identity-specific metrics to the standard benchmark set.

## Suggestions

1. **(Critical)** Add identity similarity metrics (ArcFace cosine similarity or FaceNet distance) to all four evaluation datasets. This is the single most important addition to support the "authentic" framing.
2. Include a discussion of the trade-off between perceptual quality (MANIQA, CLIPIQA) and reconstruction fidelity (PSNR, FID) in the main paper, ideally with a principled explanation of when each is appropriate.
3. Provide more T2I samples from the fine-tuned model (e.g., diverse prompts, random seeds) to demonstrate that the prior generalizes beyond memorizing the 1.5K training set.
4. Report variance or confidence intervals for the main quantitative results where feasible.

## Score and Decision

The paper makes a solid technical contribution: a well-motivated fine-tuning pipeline for adapting a T2I diffusion model to face restoration, a carefully designed time-aware loss grounded in diffusion dynamics, and a curated high-quality dataset. The experiments are extensive across four benchmarks and show consistent advantages on multiple non-reference perceptual metrics. The main weakness is the missing identity preservation evaluation, which is a notable gap given the "authentic" framing — but it is addressable in revision and does not invalidate the core methodological contribution. The method is sound, the results are competitive, and the overall direction is valuable.

**Score:** 6.5
**Decision:** Accept

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>