Now I have a thorough understanding of the paper and all the reviewer claims. Let me write the final consolidated review.

## Summary

This paper presents a novel approach to using language models as cognitive models by training a small 10M-parameter GPT (Arithmetic-GPT) on synthetic arithmetic datasets that mirror expected value (EV) and present value (PV) calculations. The key idea is to pretrain on *computationally equivalent tasks* — arithmetic that a rational agent would need to master for risky and intertemporal choice — and to use *ecologically valid distributions* (Beta(0.27,0.27) for probabilities, power-law for values) derived from real-world frequencies. The paper shows that embeddings from this ecologically pretrained model predict human choice probabilities better than classical behavioral models (CPT, hyperbolic discounting) and, on some datasets, match or exceed embeddings from LLaMA3-70B. The paper also demonstrates that the learned embeddings qualitatively replicate canonical behavioral-economic functions (probability weighting, prospect-theory utility, hyperbolic discounting).

## Strengths

- **Principled causal control over training data.** By training a small model from scratch on fully specified synthetic data, the paper circumvents the data-contamination and transparency issues that plague off-the-shelf LLMs as cognitive models. The ablation studies (randomized signs degrading performance by 10–30 percentage points; Table 1 rows 2,4 vs 1,3) provide clean causal evidence that the arithmetic content itself, not just any training signal, drives the behavioral alignment.

- **Consistent benefits of ecological pretraining distributions.** The ecological variant (Beta + power-law) consistently outperforms the uniform variant on risky choice datasets (choice13k: 70.8% vs 69.3%; cpc18: 65.5% vs 63.2%) and on the gershman20 intertemporal dataset (67.8% vs 64.0%), demonstrating that mimicking real-world frequencies adds value beyond mere arithmetic training (Table 1, rows 1 vs 3).

- **Cross-domain transfer within a single model.** The same pretrained embeddings explain both risky and intertemporal choice, whereas classical models (CPT, hyperbolic discounting) are domain-specific. This supports the paper's argument that computationally equivalent EV/PV calculations provide a unifying rational principle for diverse decision domains (Section 7).

- **Comprehensive baselines.** The paper evaluates against seven baselines: CPT, hyperbolic discounting, MLPs trained directly on human data, untrained Arithmetic-GPT, and LLaMA3 in two input formats (text and arithmetic). This provides a thorough benchmark for the proposed approach.

## Weaknesses

### Fatal

None.

### Major

- **Overfitting risk in the embedding-based logistic regression, especially on small datasets.** The logistic regression uses three 320-dimensional embeddings (e_A, e_B, e_{A-B}) as predictors — totaling ~960 parameters — on human datasets as small as 270 problems (cpc18). The paper reports "adjusted R²" but provides no details on regularization (L1/L2), dimensionality reduction, or cross-validation. With p >> n on cpc18, even adjusted R² can be unreliable or inflated. This is a structural concern: the quantitative comparisons that form the paper's central evidence (Table 1) may overstate the model's explanatory power, especially on the smaller datasets. The fact that the ecological > uniform pattern holds across datasets mitigates but does not eliminate this concern.

### Minor

- **Missing statistical uncertainty.** No standard errors, confidence intervals, or significance tests are provided for any R² value. Given the small number of datasets (4 human datasets), and especially given the overfitting concern above, bootstrapped confidence intervals or at minimum a cross-validation scheme would substantially strengthen the results.

- **"Quantitative match" claim for implicit functions is somewhat overstated.** The paper reports best-fit parameters (γ=0.58, α=0.42, β=0.45, λ=1.4, k=0.08) and compares them to ranges from the literature. While the qualitative shapes align well, λ=1.4 deviates notably from the cited human estimate of ~2.25, and α=0.42 is below the typical 0.5–0.9 range. The paper does note discontinuities and says smooth functions may not be directly applicable, which partially addresses this, but the "quantitatively match" language (line 224) overstates the precision of the correspondence.

- **The 10% `<AMB>` token masking is not ablated.** The paper masks 10% of probability values with an `<AMB>` token in all synthetic datasets, but never evaluates the effect of this manipulation. The paper explains that this is intended to handle ambiguous gambles in the human data (line 104), but since it appears in *all* synthetic datasets (not just those involving ambiguity), its contribution to the results is unclear.

- **LLaMA3 embedding extraction details are underspecified.** The paper reports obtaining "embeddings from LLaMA3 for each choice problem represented in the arithmetic-equation format" (line 160) but does not specify which layer was used, whether pooling/averaging was applied, or whether any prompt was used for the arithmetic-format input. These details matter for reproducibility.

- **The MDS reduction to 1D with Euclidean distance is a strong geometric assumption.** The implicit functions (Figure 3) are derived by reducing 320-dimensional embeddings to 1D using MDS with Euclidean distance. This assumes the representational geometry is approximately Euclidean, which may not hold. The qualitative patterns are interesting but the quantitative parameter estimates from this procedure should be interpreted with caution.

### Trivial

- The paper notes that the power-law value distribution comes from UK bank debits (Stewart et al., 2006). The reviewer questions whether debit magnitudes are appropriate for risky/intertemporal choice values. The paper's defense (these are real-world frequencies) is reasonable, but a brief justification of the mapping would improve clarity.

## Nice-to-Haves

- A control experiment using PCA-reduced embeddings (e.g., to 10–20 dimensions) to show that the high-dimensional fit is not picking up noise, especially on cpc18.
- An explicit comparison of representation "spread" (effective dimensionality, entropy) between ecological and uniform variants to test whether the ecological advantage is due to reduced variance.
- An ablation of the `<AMB>` token mechanism to isolate its effect.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **"LLaMA3 comparison is poorly controlled"** — REMOVED. The comparison is intentionally asymmetric (10M-parameter model vs 70B-parameter model), and the paper uses it to demonstrate *sufficiency*, not to isolate architectural effects. The asymmetry favors the baseline (LLaMA3 has far more parameters and data), so outperforming or matching it is a *stronger* result, not a confounded one. The paper's claim is that arithmetic pretraining is sufficient, not that it's the only factor — the LLaMA3 comparison supports this claim by showing that even a tiny model can match a massive one.

- **"The ecological distributions are insufficiently justified"** — Partially removed. The criticism mischaracterizes the paper's intent: the paper is not claiming these distributions perfectly match lab stimuli, but rather that they reflect real-world frequencies, which turns out to improve embeddings. The paper does cite sources (Zhu et al., 2020; Stewart et al., 2006). However, I acknowledge that a stronger bridge between "real-world frequencies" and "why they help predict lab choices" would improve the paper — this is reflected as a trivial note above rather than a weakness.

- **"MLP achieving 97.8% on cpc18 undermines the value of embeddings"** — DOWNGRADED. The paper explicitly frames the MLP as an upper-bound ceiling (line 155), notes that it uses task features rather than text/arithmetic inputs, and acknowledges it may overlook psychological constraints. The MLP comparison is a benchmark, not a competitor, and the paper's contribution is about mechanistic interpretability and cross-domain transfer, not about raw R² maximization.

## Novel Insights

The reviews surface an interesting tension: the paper claims both that ecological distributions matter and that arithmetic pretraining alone suffices. These two claims are in mild tension — if arithmetic alone suffices, why does the distributional form matter? The paper's own data shows ecological > uniform consistently, but the magnitude of the advantage is modest (~1–4 percentage points on most datasets). This suggests that the *task structure* (arithmetic computation) is doing most of the work, while the ecological distribution provides a smaller but consistent boost. The reviews correctly note that the field would benefit from understanding *why* the ecological distribution helps — is it variance reduction, better curriculum, or genuine ecological alignment? The current evidence underdetermines the mechanism.

## Suggestions

1. **Add L2-regularized logistic regression with cross-validation**, and report both regularized and unregularized R². This is the single most impactful improvement the authors could make, as it directly addresses the overfitting concern on cpc18. Show that the ecological > uniform pattern survives regularization.
2. **Add bootstrapped confidence intervals** for all R² values in Table 1. Even simple percentile bootstrap would substantially strengthen the statistical credibility.
3. **Ablate the `<AMB>` token** by training a version without it, to show whether it contributes to or detracts from the ecological advantage.
4. **Specify LLaMA3 embedding extraction details** (layer index, pooling method, prompt template) to aid reproducibility.
5. **Tone down the "quantitatively match" language** regarding the implicit function parameters — "qualitatively consistent" is more accurate for some of the reported values.

## Score and Decision

This paper proposes a genuinely novel and well-motivated approach to using LMs as cognitive models. The core idea — training small, controllable models on computationally equivalent tasks with ecologically valid distributions — is important and the results are promising. The weaknesses are addressable (overfitting risk in the logistic regression, missing statistical reporting, underspecified details) and do not invalidate the core contribution, but they do prevent the current evidence from being fully convincing. A revision with proper regularization and uncertainty quantification could make this a strong paper.

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>