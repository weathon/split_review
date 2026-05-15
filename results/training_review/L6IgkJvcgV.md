I now have a thorough understanding of the paper and all the review claims. Let me construct the final consolidated review.

---

## Summary

This paper proposes OASIS, a toolbox for measuring and understanding stereotypes in text-to-image (T2I) models. It introduces a formal, sociologically-grounded definition of stereotypes as *directional overrepresentations* relative to real-world statistics (contrasting with prior work that used statistical parity). OASIS provides four components: (M1) Stereotype Score to quantify directional attribute overrepresentation; (M2) WALS to measure spectral variance along stereotypical attributes; (U1) StOP to discover what attributes a model internally associates with a concept; and (U2) SPI to track when stereotypical attributes emerge in the latent space during generation. Experiments on SDv2, SDv3, and FLUX.1 across three nationalities show that even high-fidelity newer models still generate heavily stereotyped images.

## Strengths

- **Sociologically grounded definition of stereotype.** The paper correctly identifies that prior work conflates bias (statistical parity, e.g., 50% female doctors) with stereotypes (directional overrepresentation, e.g., 91.6% turbans for Iranian when the true rate is 0.2%). This distinction is conceptually important and the formalization in terms of $P(A|D,C) > P^*(A|C)$ is well-motivated. Evidence: Tab. 1 shows concrete examples where the directional definition captures stereotypes that parity-based metrics would misclassify.

- **Comprehensive framework with four complementary tools.** OASIS does not merely detect stereotypes but also investigates their origins — StOP discovers model-internal associations (Tab. 3 shows that FLUX.1 associates "Iranian" with "Imam" and "Sheikh"), while SPI tracks when stereotypical attributes emerge during generation (Fig. 6 shows beard and traditional clothing appear within the first 3 time steps). This multi-pronged approach goes beyond prior detection-only methods.

- **Demonstration that stereotypes persist in newer high-fidelity models.** Despite substantial improvements in image quality from SDv2 to SDv3 and FLUX.1, the paper provides concrete evidence that stereotypes remain severe. Evidence: FLUX.1 generates 84.7% of Mexican faces with mustache (Tab. 1), and SDv3 generates 91.6% of Iranian images with turbans against a 0.2% true rate.

- **Complementary role of the WALS metric.** The paper recognizes that low stereotype scores could trivially arise from low diversity, and proposes WALS to capture spectral variance. Evidence: Fig. 5 shows SDv3 has both lower stereotype scores AND lower WALS, indicating it partly reduces stereotypes by reducing variation — a nuance missed by any single metric.

- **Intersectional stereotype amplification.** The finding that stereotypes worsen for intersectional concepts (e.g., "Iranian doctor" shows more gender imbalance than "doctor" alone) is well-illustrated in Tab. 2 and carries practical implications for mitigation strategies.

## Weaknesses

### Fatal
None. The core contributions — the formal definition and the OASIS framework — are well-motivated and supported by the experiments as presented. The limitations are in the *scope and depth* of validation, not in fundamental flaws.

### Major

- **No statistical significance or variance reported for main results.** The paper reports point estimates for stereotype scores (e.g., 84.7% mustache for Mexican in FLUX.1) without confidence intervals, standard deviations, or significance tests across seeds/prompts. Given that the paper draws comparative conclusions ("stereotype scores of newer models are generally lower"), the absence of variance estimates makes it impossible to determine whether observed differences between models reflect genuine improvements or sampling noise. This is the single most impactful evidential gap.

- **SPI and predisposition analyses are based on very small samples.** The SPI analysis (Section 4.5) shows trajectories for only four images per nationality, and the predisposition analysis (Section 4.6 / Fig. 7) shows three samples. Claims that "stereotypical attributes arise during earlier time steps" and that "T2I models have stereotypical predispositions" would require systematic, quantitative aggregation across many samples with confidence bands. In their current form, these claims are supported only by visual inspection of a handful of cherry-picked cases.

- **StOP evaluation is purely qualitative.** Tab. 3 presents visually compelling results, but the paper provides no metric to assess whether the optimized prompts actually capture shared stereotypical attributes beyond manual inspection. The possibility that the discovered prompts capture background artifacts or confounds (e.g., US flag in background) rather than genuine stereotypes is not addressed.

### Minor

- **LLM-generated stereotype attributes lack human validation.** The entire measurement pipeline depends on ChatGPT-generated candidate stereotypes (Eq. 2). The paper provides no human evaluation, inter-rater reliability, or comparison against established sociological stereotype taxonomies to verify that these attributes are indeed actual stereotypes. While using an LLM for open-set discovery is pragmatic and defensible as a first step, the current results could be driven by irrelevant or confabulated attributes.

- **Internet footprint analysis is based on only three data points with a confusing definition.** Fig. 3 uses only three nationalities (Indian, Mexican, Iranian), making the claimed trend suggestive but not statistically established — no correlation coefficient or regression is reported. Moreover, the paper states it compares against "number of Internet users" but then reports *total population* numbers (881M, 96.8M, 78.1M), citing a population source. These are not the same quantity, and the figure caption still refers to "Internet users." This needs clarification.

- **Limited scope of empirical evaluation.** The study examines 3 nationalities and 3 models. While this is adequate for a proof-of-concept, the paper's title and abstract make broad claims about "T2I models" in general. The scope should either be expanded or the claims tempered to reflect the limited coverage.

- **No calibration or reference baseline for the stereotype score.** The paper never establishes what magnitude of $\Psi(A|D,C)$ constitutes a "harmful" stereotype vs. tolerable skew. While comparative use is valid (model A vs. model B), a reference baseline (e.g., a synthetic fair model or human image distributions) would ground the metric's interpretation.

### Trivial

- **Inconsistency in Section 4.1 Remark about bias definitions.** The paper's characterization of existing bias definitions as "not applicable" because they would require 50% turban is somewhat oversimplified. The bias literature includes many definitions beyond statistical parity (e.g., demographic parity with respect to a reference group). The core point stands (parity over attributes with very skewed real-world distributions is indeed problematic), but the framing is more dismissive than necessary.

- **Recommendation about data balancing is speculative.** The paper claims data balancing is "not suitable for resolving stereotypes due to the sheer number of concepts" without testing any mitigation strategy. This is a reasonable speculation but presented as a strong conclusion. Labeling it more clearly as a hypothesis would be appropriate.

## Nice-to-Haves

- **Human validation study of LLM-generated stereotypes.** Even a small-scale study (e.g., 20 raters evaluating 50 attribute-concept pairs) would substantially strengthen the paper's evidential foundation.
- **Quantitative evaluation of StOP.** For example, computing the likelihood that StOP-optimized prompts produce images that cluster into the same stereotype groups when fed back into the model.
- **Error analysis of CLIP-based attribute classifiers.** Reporting precision/recall on human-annotated images for attributes like "turban" or "beard" would clarify the reliability of the attribute measurements.
- **Sensitivity analysis across LLMs and CLIP variants.** Repeating the pipeline with an open-source LLM (e.g., Llama) and a different vision encoder would test robustness.

## Removed Points

These points are flagged to be removed, treat them with caution:

- **"WALS definition is entirely absent from the extracted text"** — This is a parser artifact. The original paper contains §3.2 defining WALS. The extracted text is incomplete; the definition exists in the original submission.
- **"The true distribution P^*(A|C) is not adequately justified"** — The paper references §A.1.3 with cited sources for real-world statistics. The appendix is missing due to parser stripping, not author omission. Questioning the *existence* of these cited sources is not permissible per reviewing guidelines.
- **"The mathematical condition for stereotypes is incomplete in the extracted text"** — Parser artifact; the original paper has the full definition.
- **Section 4.1 Remark about bias definitions being "misleading" and not considering "more sophisticated bias definitions"** — The paper's point is specifically about statistical parity being used as a stereotype measure in prior work, not about all possible bias definitions. This is scope-creep: the paper is about stereotypes, not exhaustively surveying bias metrics.
- **Claim that the paper "overstates its own novelty" in the Related Work section** — Insufficiently grounded; the paper's distinction between directional stereotypes and statistical parity is a genuine conceptual contribution.

## Novel Insights

A genuinely interesting observation emerges from the combination of results across the four OASIS components: the finding that StOP-discovered attributes (e.g., "Imam" for Iranian) are not present in the neutral prompts but are deeply embedded in the model's internal representations as revealed by SPI's early-timestep emergence. This suggests that stereotypes in T2I models are not *triggered* by specific words in prompts but are baked into the conditional distribution learned during training — the model's velocity field at time step 0 already points toward a turbaned, bearded figure. This has downstream implications: post-hoc prompt engineering may be fundamentally limited as a mitigation strategy if stereotypes are structural properties of the learned manifold rather than prompt-level associations.

## Suggestions

1. **Add variance estimates and statistical tests.** Report stereotype scores and WALS over multiple runs (different seeds, prompt variations) with means and confidence intervals. This is the single most impactful improvement.
2. **Expand the scope.** Add at least 5–7 nationalities and 1–2 more models (e.g., DALL-E 3 or a newer fine-tune) to support broader claims about "T2I models."
3. **Replace or clarify the Internet footprint data.** Use actual Internet user statistics (e.g., from the World Bank or ITU) rather than total population numbers. At minimum, reconcile the text's claim about "Internet users" with the population figures actually reported.
4. **Aggregate SPI quantitatively.** Report mean cosine similarity trajectories with confidence bands across hundreds of images rather than showing individual curves for 4 images.
5. **Add a small human validation set for LLM-generated attributes.** Even 50 rated attribute-concept pairs would significantly strengthen the pipeline's credibility.
6. **Temper scope claims.** The abstract and conclusion should more clearly reflect that findings are based on 3 nationalities and 3 models.

## Score and Decision

The paper introduces a conceptually important distinction (directional stereotype vs. statistical parity bias) and builds a reasonably complete toolbox around it. The core idea is novel, well-motivated, and the experimental results — while limited in scope and lacking statistical rigor — are qualitatively compelling and directionally consistent. The weaknesses are in the depth of validation, not in the soundness of the framework. With additional validation (variance estimates, broader scope, human evaluation of LLM outputs), this could be a strong paper. In its current form, it is a solid contribution with clear limitations that should be addressed.

MY FINAL SCORE: <pineapple>6.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>