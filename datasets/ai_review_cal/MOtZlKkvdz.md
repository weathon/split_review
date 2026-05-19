- Decision: Reject
- Avg Score: 3.67
- Scores: 3, 5, 3
Now I have all the information needed. Let me produce the final consolidated review.

## Summary

This paper proposes four prompting strategies (Perturbation-based, Prediction-based, Instruction-based, and Explanation-based ICL) for using LLMs (GPT-3.5 and GPT-4) as post hoc explainers of predictive models on tabular data. The authors evaluate faithfulness using PGI/PGU (for ANNs) and FA/RA (for LR models), finding that LLMs outperform SHAP, ITG, and random baselines, and can mimic existing explainers with as few as 4 ICL examples. The work is positioned as the first systematic framework for LLM-based model explanation.

## Strengths

- **Systematic framework with diverse prompting strategies**: The paper introduces four distinct, well-motivated prompting strategies (Perturbation-, Prediction-, Instruction-, and Explanation-based ICL) that span varying levels of information about the model and the local neighborhood. This provides a structured starting point for future work on LLM-based explanation (Section 3, Figures 1).

- **Explanation-based ICL effectively mimics existing explainers with very few examples**: Using only *n*<sub>ICL</sub>=4 examples, LLM-generated explanations achieve faithfulness comparable to the original post hoc methods (LIME, SmoothGrad, Integrated Gradients, etc.) across all four metrics. For low-performing methods like ITG and SHAP, the LLM-augmented versions even improve FA/RA scores, suggesting LLMs can enhance weak explainers (Figure 4, Section 4.2 Finding 2).

- **Comprehensive ablation study on design choices**: The paper systematically ablates the number of ICL samples, perturbation format (raw values vs. differences), and temperature, showing that (a) an intermediate number of ICL samples works best, (b) presenting changes (differences) substantially improves faithfulness, and (c) temperature τ=0 is optimal. These are actionable findings for practitioners (Figures 7, 10, 11; Section 4.2 Finding 5).

- **GPT-4 outperforms GPT-3.5, linking reasoning capability to explanation quality**: GPT-4 consistently yields more faithful explanations than GPT-3.5 across strategies (e.g., 4.53% higher FA and 48.01% higher RA on Adult dataset), demonstrating that stronger LLM reasoning produces better explanations — a non-trivial result that validates the approach's dependence on LLM capability (Figures 6–8, Section 4.2 Finding 4).

## Weaknesses

### Fatal
None.

### Major

1. **The ground-truth definition for Logistic Regression FA/RA metrics is problematic.** The paper uses global LR model coefficients (|βᵢ|) as the ground-truth top-*k* explanation for *each test input* (Section 4.1, line 113: "i.e., LR model coefficients"). For a linear model, the *local* contribution of feature *i* to a specific prediction **x** is βᵢ·xᵢ (in log-odds space), not βᵢ alone. A feature with a large |βᵢ| but a near-zero value in the test instance is not important for that prediction. Using global coefficients means the ground-truth is identical for every test sample, so FA/RA measures whether the LLM identifies globally large coefficients rather than locally important features. This does not invalidate the ANN results (which use the proper PGI/PGU metrics), but it undermines the LR-specific claims, including the headline "72.19% accuracy" figure (which is FA for top-*k*=1 on LR models) and the conclusion that LLMs "accurately identify the most important feature."

2. **The claim that LLMs perform "on par with state-of-the-art post hoc explainers" is overstated.** The abstract (line 4) and introduction (line 19) make this unqualified claim. However, for LR models, LIME and gradient-based methods achieve "almost perfect" FA/RA scores [100%] (line 127, line 139), while the best LLM strategy achieves ~72.19% FA for top-*k*=1. The paper's own data refute the "on par" framing for the LR setting. The contribution is more accurately described as: LLMs substantially outperform weak baselines (SHAP, ITG, random) and are competitive on ANN PGI/PGU metrics, but are significantly less faithful than standard methods on LR FA/RA metrics. This mismatch between rhetoric and evidence weakens the paper's central narrative.

### Minor

1. **No zero-shot baseline is included.** The paper evaluates Perturbation-, Prediction-, and Instruction-based ICL (all of which provide perturbed samples), but does not test a simple zero-shot prompt asking the LLM "which features are most important for this prediction?" without any ICL examples or perturbations. A zero-shot baseline would isolate the value added by the expensive perturbation-based prompting strategies and establish a lower-bound on LLM explanation capability.

2. **Results lack statistical significance and variance.** All results are reported as point estimates without confidence intervals, standard deviations, or significance tests. Given the known variability of LLM outputs (even at temperature τ=0, due to sampling randomness and neighborhood perturbation variance), it is impossible to assess whether observed differences between prompting strategies or between LLMs and baselines are reliable. This is a genuine limitation for an empirical study.

3. **The ICL sample limitation is a practical concern.** The paper transparently reports (Figure 7, Finding 5) that LLM faithfulness *decreases* when the number of ICL samples exceeds roughly 16, while LIME improves with more samples. The paper attributes this to "limited capabilities of LLM for longer prompt length." While honestly reported, this means the LLM approach cannot leverage more information to improve explanations — an unusual and limiting property for a practical explainer that contrasts with standard methods.

4. **Evaluation uses only n=100 test samples.** The paper tests on 100 random samples from each dataset's test split. While acceptable as a pilot study, this small sample size means the reported figures (e.g., 72.19%) could be driven by a few datasets or instances. A breakdown per dataset or a larger evaluation would strengthen confidence.

### Trivial
None.

## Nice-to-Haves

- A discussion of cost and latency implications (API costs for GPT-4 with 10,000 perturbations serialized as text per instance) would help set expectations for practical deployment.
- Investigating *why* LLM faithfulness drops with more ICL samples (e.g., recency bias, positional attention patterns) would be a valuable follow-up study but is not required.

## Removed Points

These points from the inputs were removed with brief justification:

- **Criticism about LIME₁₆ comparison being unfair** (Harsh Critic Section 4.2): Removed because the paper *also* compares against LIME-1000 (Figure 3 caption) and acknowledges it outperforms. The LIME₁₆ comparison is an apples-to-apples control for perturbation count, which is methodologically sound.
- **Criticism that "first framework" claim is questionable due to prior work like Bills et al. (2023)** (Harsh Critic, Section-by-Section Notes): Removed. The paper explicitly discusses Bills et al. (2023) and correctly notes that work explains neuron activations, not model-level feature importance. The "first framework" claim is substantiated.
- **Criticism about the paper's inability to handle larger ICL sets being "disqualifying"** (Harsh Critic, Critical Issue 3): Downgraded from "fatal/disqualifying" to Minor. The paper transparently reports this limitation. It is a real concern but not disqualifying — many practical XAI methods have sample-size sweet spots. The paper frames it as a finding, which is appropriate.
- **Criticism that the RA for Recidivism being nearly zero suggests "the LLM is not doing meaningful reasoning"** (Harsh Critic, Section 4.2): Removed. The paper acknowledges this and provides a plausible explanation (alphabetical ordering due to near-identical coefficient magnitudes) and shows Instruction-based ICL improves RA from 0 to 0.5. The paper handles this transparently.
- **Strength about "first systematic framework" being novel** (Strength Finder #1): Retained but modified to be precise about what is claimed. The "first framework" claim is kept in strengths because the paper substantiates it.
- **Strength that LLM explanations "match or exceed several SOTA methods"** (Strength Finder #2): Kept but contextualized. The paper shows LLMs outperform ITG, SHAP, and random, and are competitive on ANN PGI/PGU. The "match or exceed" framing is softened to reflect that LLMs are clearly worse than LIME/gradient on LR.
- **Criticism about missing variance/statistical significance as a weakness of the "strength finder's" strengths**: The strength finder did not claim statistical significance — this is purely a weakness, handled above.

## Novel Insights

None beyond the paper's own contributions. The reviews do not contribute observations that the paper itself does not already surface or imply.

## Suggestions

1. **Fix the LR ground-truth definition**: Adopt a proper local ground-truth (e.g., the feature contribution βᵢ·xᵢ for each instance, or simply the feature with the largest |βᵢ·xᵢ|) for FA/RA metrics on LR models. Alternatively, drop the LR FA/RA analysis and focus on model-agnostic PGI/PGU metrics for both LR and ANN, which would make the evaluation consistent and avoid the ground-truth issue entirely.

2. **Calibrate the claims**: Replace "on par with state-of-the-art" with precise language such as "LLMs substantially outperform weak baselines (SHAP, ITG, random) and are competitive with LIME and gradient methods on model-agnostic faithfulness metrics for ANNs, though they underperform these methods on LR models." This aligns the narrative with the data.

3. **Add a zero-shot baseline** to quantify the marginal benefit of perturbation-based ICL examples.

4. **Report variability**: Run multiple queries per instance and/or multiple neighborhood perturbation seeds, and report standard deviations or confidence intervals for the main results.

5. **Enlarge the evaluation set** (e.g., n=500 test samples) or, at minimum, provide per-dataset breakdowns of the headline results.
