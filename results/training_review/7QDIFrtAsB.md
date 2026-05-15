Now I have all the information needed to produce a thorough, evidence-based review. Let me write the final consolidated review.

## Summary

This paper proposes NCSBAD, an anomaly detection method for tabular data that uses a noise-conditional score network (NCSN) trained on normal data to compute an anomaly score based on the denoising prediction error at a fixed low noise level. The method is evaluated on an extensive benchmark comprising 57 ADBench datasets (121 sub-datasets) plus 15 additional datasets, against 49 baseline methods. The authors present two variants: NCSBAD (fixed 200 training epochs) and NCSBADVAL (validation-based checkpoint selection via AUC-ROC). The paper claims state-of-the-art performance, parallelizable inference as an advantage over DDPM-based methods, and inherent interpretability via per-feature anomaly scores.

## Strengths

- **Extensive benchmarking effort**: The evaluation spans 57 ADBench datasets plus 15 additional datasets against 49 baseline methods, making this one of the largest empirical comparisons for tabular anomaly detection. The per-dataset results are reported across multiple metrics (AUC-ROC, AUC-PR, F1, adjusted versions).

- **Addresses a practical and underexplored problem**: Tabular anomaly detection is important across finance, healthcare, and cybersecurity, yet generative-model-based approaches have been predominantly developed for image/video domains. Applying NCSNs to tabular data is a reasonable and potentially useful direction.

- **Parallelizable inference is a genuine advantage**: The anomaly score computation (Eq. 4) averages over independent noise realizations at a single fixed noise level, which is embarrassingly parallel. This is a meaningful practical improvement over DDPM-based methods (Livernoche et al., 2024) that require sequential Markov-chain inference steps.

- **The method is conceptually simple and transparent**: The anomaly score (MSE between predicted noise and actual noise at a fixed time step) follows naturally from the training objective, and the architecture (three-layer MLP with time embeddings) is straightforward and reproducible.

## Weaknesses

### Fatal
None.

### Major

- **Comparison protocol asymmetry for NCSBADVAL undermines the SOTA claim**: NCSBADVAL uses a held-out validation set to select the optimal training epoch based on AUC-ROC (lines 78–79), while all 49 baselines are run with "default hyperparameters provided by the authors of the original publications" (line 93) with no equivalent validation-based selection. This gives NCSBADVAL a procedural advantage independent of the core method. The paper does not report whether any baseline method could similarly benefit from validation-based early stopping. The "state-of-the-art" claim for NCSBADVAL (abstract, line 4; Figure 2 caption) is therefore not supported by a like-for-like comparison. The NCSBAD variant (fixed 200 epochs) is fairer and still ranks competitively (#1 in mean AUC-ROC, slightly behind LUNAR in F1 and AUC-PR), which partially mitigates this concern.

- **The anomaly score lacks rigorous theoretical justification**: The paper proposes using the MSE between the network's noise prediction and the actual noise ε at a single fixed noise level (the first time step, corresponding to extremely low noise) as an anomaly score. While training minimizes E[||S_θ(x_t,t) − ε||²] over all t, the inference score evaluates this loss at only one near-zero noise level. The paper states (line 58) that −S_θ/σ_t ≈ ∇_x log p_t(x), but never uses the score itself — the anomaly score is ||S_θ − ε||². No argument is given for why this particular fixed-noise-level denoising error should discriminate anomalies, nor how it relates to score-based detection principles. The method is not "grounded" in score matching theory in the way the paper implies; it is essentially a denoising autoencoder evaluated at a single perturbation scale. A theoretical analysis or even a clear intuitive argument for the mechanism would significantly strengthen the paper.

### Minor

- **No statistical significance testing**: Despite claiming superiority over 49 methods across 57 datasets, the paper reports only means and box plots (Figure 2) with no statistical significance tests (e.g., paired Wilcoxon signed-rank, McNemar). Given the substantial overlap visible in the box plots and the authors' own admission that "no single method universally dominates across all datasets" (line 95), significance testing is needed to support the claimed SOTA.

- **Interpretability claim is not substantiated for tabular data**: The interpretability demonstration (Section 5) uses MNIST-C images flattened to vectors. As the authors acknowledge (line 113: "While this is indeed a vision example"), this does not demonstrate per-feature interpretability for tabular data, where features are semantically distinct (e.g., age, income) rather than spatially correlated pixels. No quantitative evaluation or real tabular example (e.g., credit card fraud with feature attributions) is provided. The claim of "inherent and intuitive interpretability" for tabular anomaly detection is therefore unsupported.

- **Missing ablation studies for key design choices**: Several important hyperparameters are presented without empirical justification: (1) the noise schedule base σ=0.01, (2) the fixed inference time step t_fix (first of 1000), (3) NUM=70 Monte Carlo samples, (4) the MLP hidden dimension of 2048. These choices are described as critical (e.g., line 54: "the most crucial hyperparameter in our method"), yet no ablation or sensitivity analysis is performed.

### Trivial

- Figure 2 is referenced but not directly readable in the extracted text; the paper would benefit from including numerical summary tables (mean ± std across datasets) in the main text rather than only in the appendix.

## Nice-to-Haves

- A comparison of NCSBAD to a simple denoising autoencoder with the same architecture and noise level would isolate whether the multi-scale score-matching training (which distinguishes the method from a single-scale DAE) provides any benefit.
- Timing benchmarks with and without parallelization would substantiate the claimed efficiency advantage.

## Removed Points

The following points from reviewers are removed for the indicated reasons:

- **"The paper claims 'world's largest benchmark' but ADBench already contains 57 datasets"** — The paper explicitly states it uses ADBench's 57 datasets (plus 15 additional) and 49 baselines, making the benchmark composition clear. The "largest" claim is about the combined benchmark and number of baselines, not hyperbolic.

- **"The noise scale formula is given without derivation or citation"** — The paper states it is "inspired by previous work (Song & Ermon, 2020)," which is an adequate citation for a geometric noise schedule.

- **"The abstract overstates SOTA"** — The NCSBAD variant (without validation) ranks #1 in mean AUC-ROC, so the claim is not entirely baseless, though it is qualified by the fairness concern noted above.

- **"Missing timing comparison with parallelization advantage demonstrated numerically"** — The paper states that a time analysis is provided (line 95, "3 compares our method's training and inference times against baseline models"), but the parser strips tables. The claim is referenced.

- **"Strength: validation-based early stopping further boosts performance"** — This is a standard ML practice, not a novel contribution of the paper. It does not constitute a strength of the proposed method.

- **"The paper claims SOTA but the differences appear marginal"** — The paper's own Figure 2 and per-dataset tables support that NCSBADVAL has the highest mean scores. The marginality is already captured in the significance testing weakness.

- **"The weighting function λ(t) is mentioned but then ignored"** — The paper explicitly says (line 42) "without adding any of the in Section 2 described weighting adjustments," showing this is a deliberate simplification, not an oversight.

- **"Image/text embedding datasets are non-tabular"** — The paper transparently reports the composition (47 tabular, 5 image representations, 5 NLP embeddings) and includes results for these separately. This is standard in ADBench.

## Novel Insights

The reviews surface a tension not fully addressed in the paper itself: the method's practical strong point (parallelizable single-scale inference) and its theoretical weak point (unmotivated fixed-noise-level scoring) are two sides of the same coin. The paper presents the fix to a single low noise level as a design choice for minimal distortion, but this means the inference procedure discards the multi-scale information that is the hallmark of score-based models. The method would be strengthened by either (a) providing a theoretical rationale for single-scale discrimination, or (b) incorporating multi-scale information into the anomaly score while preserving parallelizability — for example, by evaluating at several noise levels in parallel.

## Suggestions

1. **Fix the comparison asymmetry**: Either (a) apply the same validation-based early stopping to all baselines (reporting the best epoch on the validation set), or (b) use NCSBAD (fixed 200 epochs) as the primary comparison and relegate NCSBADVAL to a supplementary analysis showing the marginal benefit of early stopping. The abstract and conclusion should then reference NCSBAD, not NCSBADVAL, as the main method.

2. **Add a theoretical justification or intuitive analysis** for why the single-noise-level denoising error discriminates anomalies. At minimum, show that this error correlates with data density or distance from the training manifold.

3. **Replace the MNIST-C interpretability example** with a real tabular example (e.g., feature attributions for a credit card fraud or medical diagnosis dataset). If no suitable tabular example exists, downgrade the interpretability claim from "inherent and intuitive interpretability" to "the score can be decomposed per feature in principle."

4. **Add statistical significance testing**: report paired Wilcoxon signed-rank tests between NCSBAD/NCSBADVAL and the top-5 baselines across all datasets.

5. **Include ablation studies** for the noise schedule parameter σ, the fixed inference time step, and NUM (number of Monte Carlo samples).

## Score and Decision

The paper makes a reasonable empirical contribution — large benchmark, a simple and parallelizable score-based approach for tabular anomaly detection — but is held back by three significant issues: (1) the comparison protocol favors NCSBADVAL via validation-based checkpoint selection, undermining the SOTA claim; (2) the anomaly score lacks theoretical grounding beyond being a denoising error at a single noise level; (3) the interpretability claim is not demonstrated for tabular data. These are fixable but require non-trivial changes to the evaluation and framing.

MY FINAL SCORE: <pineapple>5.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>