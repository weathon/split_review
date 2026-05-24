Now I have all the information needed to verify the reviewer claims and calibrate the score. Let me write the consolidated review.

## Summary
2-3 sentence summary of the paper's contribution.

This paper introduces Regularization by Text (TReg), a zero-shot latent diffusion inverse solver that uses textual descriptions as a regularizer to reduce ambiguity in ill-posed inverse problems. The core technical contributions are a latent optimization framework that jointly enforces data consistency and semantic alignment with a text prompt, and an adaptive negation mechanism that dynamically refines the null-text embedding to suppress artifacts. The method is evaluated on super-resolution, deblurring, inpainting, Fourier phase retrieval, and gamma correction, showing strong results including successfully breaking the symmetry that defeats prior diffusion-based solvers in phase retrieval.

## Strengths

1. **Novel and well-motivated concept of text regularization for ambiguity reduction.** The idea of using textual descriptions as a perceptual prior to resolve ambiguities in inverse problems is genuinely novel and well-justified. The paper draws a clean parallel between human perceptual biases and the proposed text-conditioning mechanism, and this framing differentiates TReg from prior diffusion inverse solvers that treat text conditioning as an optional afterthought rather than a core regularizer.

2. **Strong evidence of ambiguity reduction (Figure 3) and symmetry breaking (Figure 6).** Figure 3 quantitatively demonstrates that pixel-level variance across multiple reconstructions drops substantially when text conditioning is provided, directly supporting the paper's core claim. Figure 6 is especially compelling: Fourier phase retrieval is a well-known challenging non-linear problem, and TReg's ability to consistently recover the correct face (while LDPS fails) provides clear empirical evidence that text regularization resolves intrinsic symmetries that image-only priors cannot.

3. **Adaptive negation demonstrably improves output quality.** Tables 1-2 show that adaptive negation improves FID scores substantially (e.g., from 144.4 to 124.2 on SR×16 for "ice cream") while maintaining comparable PSNR. Figure 2(b) provides clear visual evidence that disabling adaptive negation introduces text-related artifacts (digits "020808" in a fox image), establishing the practical importance of this component.

4. **Competitive or superior quantitative results across multiple settings.** In Tables 1-2, TReg achieves higher PSNR and lower FID than DDRM, PGDM, PSLD, and PSLD+CFG by large margins (e.g., PSNR 21.09 vs. 16.47 for PSLD+CFG on SR×16). The comparison against PSLD+CFG is especially informative since that baseline also uses text conditioning via CFG, demonstrating that TReg's latent optimization framework adds value beyond simply applying CFG to an existing solver.

5. **Zero-shot generalization across diverse image domains.** Figure 4 shows successful reconstructions on ImageNet, AFHQ, FFHQ, and LHQ datasets using only class-related prompts, without any task-specific fine-tuning. This demonstrates that TReg robustly leverages the LDM prior across different visual categories.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

1. **Missing null-text ablation in the main quantitative tables.** The paper provides qualitative null-text comparisons (Figure 5, "Ours w/o text" column) and ambiguity-reduction variance comparisons (Figure 3, where the "without text" condition uses null text while retaining latent optimization). However, the core PSNR/FID results in Tables 1-2 only compare TReg (with text) against baselines. A row showing "TReg with null text" in Tables 1-2 would directly quantify how much of the improvement comes from text conditioning versus the latent optimization procedure itself, and would make the contribution of text regularization more precisely measurable.

2. **No hyperparameter sensitivity analysis.** The method introduces several tunable parameters: the guidance scale ω, step size ρ_t for the DPS update, the update range Γ (footnoted as critical but not discussed in the main text), and the learning rate η for adaptive negation. The paper states that some are "empirically chosen" without reporting how sensitive the results are to these choices. A brief sensitivity analysis would strengthen reproducibility.

3. **No explicit limitations section.** The paper assumes that a suitable text prompt describing the desired solution is available a priori. While the paper states this assumption in Section 4 ("We assume that both the measurement and a text prompt describing the solution are provided"), it does not discuss scenarios where no sensible prompt exists (e.g., medical imaging of unseen pathology) or the impact of prompt quality on reconstruction. A brief limitations discussion would help readers understand the scope of applicability.

4. **FID computation details not fully specified for per-class results.** FID is reported per-class on only 250 images, which can produce high-variance estimates. The paper should acknowledge this limitation or report confidence intervals.

5. **Variable splitting simplification noted but not justified.** The latent optimization (Eq. 12-13) sets the dual variable to zero without updating it, which is a simplification of proper ADMM. The paper is transparent about this choice but does not discuss why this simplification does not degrade convergence or solution quality, or whether a full ADMM update would further improve results.

### Trivial

- Equation (15) has some unclear notation mixing \(\tilde{\alpha}_{t-1}\) and \(\bar{\alpha}_{t-1}\).
- "Update Range Γ" is a critical hyperparameter only mentioned in a footnote in Algorithm 1; it should be discussed in the main text.

## Nice-to-Haves

- A study on prompt quality: varying the text prompt from perfect (true class) to vague ("a photo") to misleading ("dog" for a cat image) and reporting the effect on reconstruction quality. This would establish the robustness of the method and honestly acknowledge its limitations.
- A human evaluation for the mismatched-text experiment (Table 3) asking raters to judge whether the reconstruction simultaneously looks like the measurement and exhibits the described concept. The paper acknowledges the y-MSE/CLIP trade-off and handles it reasonably with three metrics plus qualitative results, but a human study would strengthen this evaluation.
- Runtime/FLOPs comparison in the main text (currently summarized only in the appendix, as noted).

## Removed Points

1. **"Unfair comparison — TReg uses extra class-label information that baselines don't have."** Removed because this is the core contribution being tested. The paper compares TReg (which uses text) against DDRM/PGDM/PSLD (which don't) to demonstrate that adding text helps. This is not unfair — it is the experimental design that tests the paper's hypothesis. PSLD+CFG does use the same text conditioning and TReg outperforms it, providing a fairer apples-to-apples comparison. Furthermore, the paper provides null-text comparisons qualitatively (Figure 5) and for variance (Figure 3).

2. **"Flawed evaluation on mismatched text — metrics are insufficient and the paper treats lower y-MSE as uniformly better."** Removed because the paper explicitly acknowledges the trade-off: "In the case of y-MSE, PnP achieves a lower value due to minimal alterations made to the measurement, as depicted in the last column of Figure 5." The paper does not treat y-MSE as uniformly better; it reports three complementary metrics (LPIPS, CLIP similarity, y-MSE) alongside qualitative results. A human evaluation would be a nice addition but is not standard for this type of algorithmic contribution and the absence does not constitute a structural flaw.

3. **"Overclaimed general-purpose applicability — method assumes a text prompt is available."** Removed because the paper clearly states its assumption in Section 4: "We assume that both the measurement and a text prompt describing the solution are provided for the inverse problem." The claim of being "zero-shot" refers to not requiring task-specific fine-tuning, not to working without any text input.

4. **"Adaptive negation description is confusing."** Removed after verifying that the paper's description is coherent. The mechanism (minimizing CLIP similarity between the image representation and null embedding to push the null text away from already-captured concepts) is clearly stated and the equation is correct. The claimed confusion is not substantiated by a specific error in the paper.

5. **Strength Finder's generic/superficial strengths.** The strength about "superior quantitative performance over strong baselines" and "effective handling of mismatched text prompts" are kept as they are specific and evidenced by tables/figures.

## Novel Insights

The most striking observation that emerges from synthesizing the reviews is that the harsh critic's central complaint — that the comparison is "unfair" — fundamentally misreads the paper's contribution. The paper does not claim that text conditioning alone is superior; it claims that TReg *as a system* (latent optimization + text conditioning + adaptive negation) is better than existing solvers. The critic demands a surgical ablation to isolate the text component, but the paper already provides precisely such evidence: the qualitative "Ours w/o text" column in Figure 5, the variance reduction in Figure 3 using null text, and the w/o AN rows in Tables 1-2. The critic's "fatal" flaws reduce to minor presentation gaps (missing a null-text row in the main PSNR/FID tables) rather than structural weaknesses. This is also notable because the paper's strongest evidence — symmetry breaking in phase retrieval — is almost entirely independent of the unfair-comparison critique, since there the baseline is TReg-with-null-text (same pipeline, no text).

## Suggestions

1. Add a "TReg (null text)" row to Tables 1 and 2 to directly quantify the contribution of text conditioning to PSNR/FID.
2. Add a brief hyperparameter sensitivity analysis (at minimum, vary ω and the update range Γ) to the appendix with a summary in the main text.
3. Add a "Limitations" paragraph discussing the reliance on pre-specified text prompts and the assumption that a meaningful prompt exists.
4. Clarify the notation in Eq. (15) and move the discussion of the update range Γ from the Algorithm 1 footnote into the main text.

## Score and Decision

**Round 1 bracketing (3 queries, anchor scores: <3.5 / 3.5–7.5 / >7.5):**
- Weak anchors (avg 2.0–3.0): Mostly withdrawn/rejected papers with fundamental theoretical flaws or incomplete methods. The TReg paper is clearly stronger — no fatal errors, method is sound, experiments are comprehensive.
- Middle anchors (avg 4.0–6.0): Mix of rejected and accepted papers. The most comparable anchor is d7pr2doXn3 (Hybrid Regularization, avg 6.0, Accept Poster), a diffusion inverse solver paper accepted with minor gaps (missing baselines, no blind evaluation). TReg has a stronger conceptual contribution (novel text regularization framework vs. incremental improvement on RED-diff) and similarly minor evaluation gaps.
- Strong anchors (avg 8.0–8.5): Top-tier accepted papers (orals) with comprehensive experiments, rigorous theory, and broad impact. TReg is not at this level — the evaluation gaps and lack of thorough ablations preclude this range.

**Initial bracket:** 5.0 – 7.0

**Round 2 narrowing (2 queries, anchor scores: 4.5–6.5 and 5.5–7.5):**
- d7pr2doXn3 (6.0, Accept Poster): Most directly comparable. TReg has stronger novelty and more compelling qualitative results (phase retrieval), similar level of evaluation thoroughness. TReg is slightly stronger → score at or above 6.0.
- TRWxFUzK9K (6.5, Accept Poster): Video inverse solver. Stronger on practical impact but more incremental. TReg has comparable novelty but fewer ablation studies. TReg is slightly weaker than this anchor → score at or below 6.5.
- YOKnEkIuoi (5.8, Accept Poster): Conditional variational diffusion. Similar evaluation depth. TReg has stronger novelty → score above 5.8.
- 8xStV6KJEr (5.0, Reject): Constrained diffusion. Less novel framing. TReg is clearly stronger.
- Z9Odi09Rv9 (4.75, Reject): Paper had theoretical issues that divided reviewers. TReg is stronger.

**Final score:** 6.0

The paper sits cleanly at the level of a solid ICLR poster: a genuinely novel concept with compelling empirical validation, marred only by minor evaluation gaps (no null-text row in the main tables, no hyperparameter sensitivity analysis, no limitations section) that are all addressable without changing the paper's core contributions.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>