Now I will produce the final consolidated review.

## Summary

This paper addresses two challenges in virtual try-on — limited paired training data and localized generation artifacts — through a dual approach. First, it introduces a human-to-garment (H2G) model that extracts canonical product-view garments from clothed human images, generating synthetic (human, garment) training pairs (12,730 upper-body + 8,939 full-body). Second, it proposes Error-Aware Refinement Schrödinger Bridge (EARSB), which spatially reweights the I²SB noise schedule using confidence maps from a weakly-supervised artifact classifier, enabling surgical correction of localized errors in GAN-generated try-on outputs. Experiments on VITON-HD and DressCode-Upper show consistent improvements, with a 59% user preference over baselines.

## Strengths

- **Synthetic data pipeline via H2G is well-validated.** The paper demonstrates (Table 3a) that adding H2G-generated synthetic pairs improves most metrics for CAT-DM, Stable-VTON, and EARSB, while a control using randomly warped garment crops *hinders* performance — confirming that the canonical product-view projection is essential. The three-criterion quality filter (clean background, front-view via DensePose, low LPIPS reconstruction error) provides a principled curation mechanism.

- **Error-aware noise scheduling is a genuine technical contribution with strong ablation support.** The spatially-varying noise reweighting (Eq. 5–6) is shown to be essential: removing the error map (EARSB w.o. M) causes "substantial decline across all metrics," and using a random map also degrades performance (Table 3c). This demonstrates the mechanism is genuinely leveraging localized error information rather than being a trivial addition.

- **Weakly-supervised classifier is cost-effective and outperforms automatic alternatives.** The classifier uses patch-level supervision on only 5% of the dataset and image-level labels for the rest. The precision-recall curve (Figure 7) shows it substantially outperforms both the unsupervised classifier (UC) and the automatic compositing-based classifier (CC). This practical deployability consideration is a genuine strength.

- **User study provides complementary human evaluation.** Amazon MTurk workers (100 randomly selected pairs, ≥3 workers each) preferred EARSB 59% of the time, with at least 10% higher preference over both GP-VTON (GAN-based) and Stable-VTON (SD-based) along both texture consistency and image fidelity dimensions.

- **Modular design with well-separated components.** The paper cleanly separates the synthetic data augmentation (independent of the refinement model), the error classifier (can be tailored for specific models), and the refinement framework (can work with different initial GANs). Ablations verify each component's individual contribution.

## Weaknesses

### Fatal
None.

### Major
- **Which GAN generates the initial x₁ for the main results (Table 1) is not specified.** The paper states x₁ is from "a try-on GAN model (Lee et al., 2022; Shim et al., 2024)" and Figure 1 illustrates with SD-VTON, but the primary quantitative comparison never states which GAN's output EARSB refines. An ablation in Section 4.2 tests different GANs (HR-VTON, SD-VTON, GP-VTON) but this is separate from the main results. Without this detail, the results are not reproducible and the reader cannot assess whether the reported gains reflect genuine refinement capability or artifact of a particular initialization. This is the single most important missing detail for reproducibility.

- **The comparison against diffusion-based try-on methods has a structural asymmetry that is not adequately acknowledged.** EARSB is a *refinement* model that starts from an already-generated GAN output, while Stable-VTON, TPD, and LaDIVTON generate try-on results from scratch (using pretrained SD weights). The two inference paradigms are fundamentally different. The paper's claim that EARSB+H2G "outperforms SD baselines" conflates this distinction. The comparison against CAT-DM is fair (CAT-DM also refines GAN outputs, as noted in line 201), but the general framing in Table 1 and Section 4.1 treats all SD methods as comparable. The paper should clearly separate comparisons into: (a) EARSB vs. GAN baselines (demonstrating refinement improvement), (b) EARSB vs. CAT-DM (fair head-to-head of refinement methods), and (c) informative but asymmetric comparison against full-generation SD methods with an explicit caveat.

### Minor
- **No variance or confidence intervals for any metric.** SSIM, FID, KID, LPIPS are all reported as single point estimates without standard deviations, confidence intervals, or multiple runs. Several differences are numerically small (e.g., FID 11.80 → 11.41). Without variance estimates, the reader cannot assess whether the reported improvements are statistically reliable. The user study's 59% preference also lacks a confidence interval — with ~300 judgments, the 95% CI around 59% could overlap with chance.

- **Potential data contamination between synthetic sources and test sets not discussed.** The H2G model generates synthetic pairs from DeepFashion2 and UPT images. The paper does not explicitly confirm that these source datasets are disjoint from the VITON-HD and DressCode test sets. While cross-dataset overlap is unlikely, the paper should state this explicitly to rule out data leakage concerns.

- **Mathematical analysis of the spatially-varying noise schedule is incomplete.** The reweighted noise εʳ = M·ε (Eq. 5–6) produces spatially heteroskedastic noise with variance proportional to M² at each location. The paper does not discuss whether the modified forward process maintains well-defined marginals or whether the Schrödinger bridge formulation remains theoretically valid under non-isotropic noise. The empirical validation (Table 3c) is strong, but the paper would benefit from at least a brief discussion of why the formulation is expected to hold. This is a rigor gap in an otherwise well-designed method.

- **Paired and unpaired evaluation results are pooled.** The paper mentions evaluations under both settings (line 156) but reports only pooled metrics. Reporting them separately could reveal important differences in where the refinement helps most (e.g., EARSB may show larger gains in the harder unpaired setting).

### Trivial
- **No limitations discussion.** The paper would benefit from a frank discussion of limitations (e.g., dependence on a specific GAN for x₁, domain gap between synthetic and real garments, classifier generalization to unseen artifact types).

## Nice-to-Haves
- Show failure cases alongside successes, with error map visualizations (M maps overlaid on images) to illustrate what the classifier detects and misses. The paper's core mechanism is spatial noise reweighting, yet no visualization of the error map is shown beyond the precision-recall curve.
- Report paired/unpaired metrics separately to reveal any differential performance.
- Add a brief theoretical justification (or at minimum a discussion) of why the spatially-varying noise schedule maintains the Schrödinger bridge formulation.

## Removed Points
These points were removed with brief justification:
- **"L_ins notation inconsistency"** — Removed per formatting/typo rule (parser/author error, not a substantive issue).
- **"Expert denoisers trade-off not acknowledged"** — The paper explicitly states "no trade-offs (other than model size)" (line 149). The criticism is factually incorrect.
- **"Only two qualitative example rows"** — This is a nice-to-have, not a weakness. The paper's key evidence is quantitative (Tables 1, 3) and the classifier validation (Fig. 7).
- **"Strength about training from scratch on 24k pairs yet matching/bettering SD baselines"** — Removed because it directly conflicts with the verified weakness about asymmetric comparison. The framing of "outperforming" SD baselines is contested; the data-efficiency observation is still noted in context.

## Novel Insights
None beyond the paper's own contributions. The harsh critic and strength finder largely restate what the paper presents, with the critic raising valid concerns about evaluation framing and the strength finder correctly identifying the well-validated ablations.

## Suggestions
1. **Specify which GAN generates x₁ for the main results.** This must be stated explicitly in Table 1's caption or Section 4.1 to enable reproducibility.
2. **Reframe the comparison against SD-based methods.** Clearly separate the comparison into tiers: (a) EARSB vs. the GAN it refines, (b) EARSB vs. CAT-DM (fair refinement comparison), (c) EARSB vs. full-generation SD methods (informative but structurally different). Drop or qualify the "outperforms SD baselines" claim.
3. **Add variance reporting.** Run evaluations with at least 3 random seeds and report mean ± std. Add a binomial confidence interval for the user study preference.
4. **Confirm data source disjointness.** Add a one-sentence statement that DeepFashion2/UPT source images are disjoint from VITON-HD/DressCode test sets.
5. **Add a brief theoretical note on the spatially-varying noise.** Explain that the reweighting modifies the marginal distributions locally and why the SB formulation remains applicable, or at minimum acknowledge the approximation.

## Score and Decision

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>