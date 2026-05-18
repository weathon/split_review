Now I have all the information needed. Let me produce the final consolidated review.

---

## Summary

This paper investigates whether LLMs can generate explanations for ML models that satisfy established XAI properties (selectivity, fidelity, completeness, stability, etc.). It evaluates 6 LLMs across 11 properties using 2 tabular datasets and 5 ML models per task, comparing LLM outputs against conventional XAI methods (LIME, SHAP, DiCE). The paper finds that LLMs systematically underperform on properties requiring faithful model representation (fidelity, completeness, certainty), frequently produce unstable and error-ridden outputs, but show a concrete advantage in comprehensibility (readable natural language). It positions LLMs as plausible "translators" of outputs from rigorous XAI methods rather than as standalone explainers.

## Strengths

- **Broad, systematically designed evaluation framework**: The paper evaluates 6 LLMs across 11 XAI properties using 5 ML models on 2 tasks, with a clear methodological structure (property selection, LLM selection, task/model selection, benchmark pairing). This scope directly addresses the identified gap that prior work lacked rigorous quantitative assessment (Section 3.1, Tables 1–2). Several properties are evaluated through direct, method-independent operationalizations (Accuracy via prediction comparison, Contrastness via counterfactual effectiveness, Certainty via probability RMSE, Stability via sample consistency, Robustness via error frequency), giving those findings genuine evidentiary weight.

- **Several core findings are convincingly supported by direct evaluations**: Properties evaluated without reliance on a single benchmark method — Accuracy, Certainty, Contrastness, Stability, Robustness — all consistently show LLMs underperforming. The evidence that LLMs produce unstable explanations (high variation on identical inputs, Section 4) and commit frequent formatting/instruction-following errors (Robustness, Section 4) is methodologically sound and independently supports a key contribution: that current LLMs are unreliable for standalone use as explainers.

- **Identifies a concrete LLM strength in Comprehensibility**: Flesch-Kincaid readability scores show LLM-generated explanations are accessible at a high-school to college reading level (Tables 1–2), a capability traditional XAI methods (LIME feature weights, SHAP values) fundamentally lack. This is a genuine, practically relevant advantage for communicating to non-expert audiences.

- **Honest discussion of limitations**: Section 5 explicitly acknowledges resource constraints, prompt dependency, and the lack of standardised XAI benchmarks, and proposes concrete future directions (prompt engineering, fine-tuning, multi-modal approaches).

## Weaknesses

### Major

- **Problematic operationalization of Selectivity and Degree of Importance**: Selectivity is defined in the paper as explanations that "focus on the most influential features, not detailing each factor" (Section 2.1). Yet it is measured as cosine similarity to DiCE counterfactuals — which produce modified input instances, not feature-importance lists. How cosine similarity is computed between these heterogeneous outputs is not clearly described, and the metric does not actually capture sparsity or feature-concentration. Similarly, Degree of Importance is measured as cosine similarity to LIME feature importance values. Both operationalizations conflate "satisfying the property" with "agreeing with one specific method's output." While the paper acknowledges the lack of standard benchmarks (line 165), this does not remedy the fact that a reasonable explanation that systematically disagrees with LIME or DiCE would be penalized regardless of its actual quality. These weaknesses affect a substantive portion of the quantitative results.

- **Small sample size with no repeated runs or uncertainty quantification**: The study uses only 261 (Adult Income) and 207 (California Housing) test samples from a 99:1 split, with each LLM queried once per sample. No confidence intervals, standard deviations, or repeated queries are reported for the main metrics. Given that LLM outputs are stochastic and prompt-sensitive, the numerical precision of scores in Tables 1–2 is misleading. This is especially problematic for API-based models whose nondeterminism is user-controllable (temperature). The stability test partially addresses replication, but only for one specific evaluation.

- **The Fidelity evaluation via exact coefficient estimation is an unreasonably difficult task**: Fidelity is measured by asking LLMs to output precise numerical coefficients of a trained linear/logistic regression model from a prompt. LLMs are not trained to perform this kind of exact numerical regression, so low scores are expected and do not necessarily reflect poor fidelity in any practically meaningful sense. A more informative fidelity test would be to check whether the explanation's predictions match the model's behavior on perturbed inputs — a standard approach in XAI that does not require exact numerical coefficient recovery.

### Minor

- **Flesch-Kincaid is a weak proxy for comprehensibility**: It measures surface-level text readability (sentence length, syllable count) but not whether a non-technical user actually understands the explanation in its decision-making context. The paper acknowledges this limitation but does not adjust its conclusions accordingly.

- **Only tabular datasets are used**: Generalization claims about LLMs as explainers are limited to tabular prediction tasks (Adult Income, California Housing). The paper does not address whether findings extend to text, image, or other modalities.

- **No prompt variation tested**: A single prompt design was used per explanation type across all LLMs. Prompt sensitivity is well-documented for LLMs; the absence of even one alternative prompt per task makes the results sensitive to the specific phrasing chosen.

### Trivial

None.

## Nice-to-Haves

- For Selectivity, a sparsity-based metric (proportion of features marked as important, or concentration of feature weights) would directly measure the property as defined, rather than similarity to DiCE.
- For Fidelity, a surrogate-model agreement test on perturbed inputs (common in XAI evaluation) would be more informative than exact coefficient recovery.
- Reporting results across 2–3 prompt variations per task would help assess sensitivity.
- A third dataset with different characteristics would broaden generalizability, though the two chosen are defensible for tabular-focused scope.

## Removed Points

These points from the reviews are flagged for removal or downweighting after verification against the paper:

1. **"The paper treats conventional XAI methods as de facto ground truth across all properties"** (Harsh Critic) — **Partially removed.** This is accurate for Selectivity (DiCE) and Degree of Importance (LIME), but **factually wrong** for Fidelity, which compares to *actual model coefficients* (ground truth, not another method). For Completeness, SHAP values are a defensible benchmark since SHAP's efficiency axiom *is* a formal completeness guarantee. The criticism overstates by applying the conflation claim uniformly to all four properties when the evidence only supports it for two.

2. **"Completeness evaluation using SHAP is methodologically circular"** (Harsh Critic) — **Removed.** SHAP values satisfy the efficiency/completeness axiom by construction (the sum of SHAP values equals the prediction minus the average prediction). Using SHAP as a benchmark for completeness is not circular; it is the standard reference for this property. The paper could be more direct (checking whether LLM attributions sum to the prediction), but using SHAP as a benchmark is reasonable.

3. **"A method that produces systematically different—but still valid—explanations would be penalized" applied to Fidelity** — **Removed** for Fidelity specifically, since the comparison is to actual model coefficients (ground truth), not to another explainer. A correct explanation of a linear model *must* recover the actual coefficients; different-but-valid coefficients would mean a different model. This concern remains valid for Selectivity and Degree of Importance.

4. **Strength Finder: "Comprehensive literature synthesis"** — **Retained** (it is accurate; Section 2 provides a thorough synthesis of XAI properties and LLM evaluation).

5. **Strength Finder: "Reproducible experimental methodology"** — **Retained** but caveated: the methodology is well-detailed (API querying, prompt modularization, batch processing), though the small sample and single-run design limit reproducibility of exact numerical results.

## Novel Insights

None beyond the paper's own contributions. The reviews do not surface a perspective not already present in the paper.

## Suggestions

1. **Redesign the Selectivity and Degree of Importance metrics** to directly operationalize the property: for Selectivity, measure the sparsity or concentration of features the LLM identifies as important; for Degree of Importance, consider comparing relative ranking of features (e.g., rank correlation) rather than absolute cosine similarity to a single method, or use multiple feature attribution methods as an ensemble reference.

2. **Add uncertainty quantification**: run each LLM query at least 3 times per sample (with temperature > 0) and report means and standard deviations for all metrics in Tables 1–2. This is feasible within academic resources for 200–260 samples.

3. **Include one alternative prompt per task** to demonstrate that results are not artifacts of a specific phrasing, even if prompt engineering is not the focus.

4. **Replace the Fidelity coefficient-recovery task** with a perturbation-based surrogate agreement test: train a simple model on the LLM's explanations and measure how well it predicts the original model's outputs on perturbed inputs — a standard fidelity test in XAI.

5. **Add a qualitative human evaluation** of comprehensibility (e.g., a small user study asking non-experts to compare LLM explanations vs. LIME/SHAP output) to complement the Flesch-Kincaid scores.

## Score and Decision

The paper makes a useful contribution: it is the first systematic, multi-property evaluation of LLMs as explainers, identifies concrete weaknesses (instability, errors) that are methodologically well-supported, and identifies a genuine strength (comprehensibility). However, the core methodological issue — operationalizing two important properties (Selectivity, Degree of Importance) as similarity to a single benchmark method rather than via direct property-specific metrics — weakens a non-trivial portion of the quantitative evidence. The small sample and absence of repeated runs further limits the precision of the claims.

The paper is **not fatally flawed**: several key findings (instability, error rates, accuracy deficits, probability miscalibration, comprehensibility advantages) rest on sound, method-independent evaluations and would survive a redesign of the problematic metrics. But the paper would be significantly strengthened by addressing the selectivity/importance operationalization issue and adding uncertainty quantification. On balance, the contribution is real and the limitations are fixable, meriting a **borderline acceptance** with a clear path to a stronger paper.

MY FINAL SCORE: <pineapple>5.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>