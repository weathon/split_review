Now I have a thorough understanding of the paper and all the reviewer claims. Let me synthesize the final review.

## Summary

This paper proposes a gradient-free adversarial attack method targeting XAI explanations for time series regression. The approach uses Particle Swarm Optimization (PSO) with a Dynamic Time Warping (DTW)-based objective function and an explanation-based local attack strategy that perturbs only the most important time points. Experiments are conducted across three model architectures (LSTM, TCN, Transformer) and four XAI methods (Saliency Map, SmoothGrad, LIME, SHAP) on two datasets.

## Strengths

- **First gradient-free attack for time series XAI explanations.** The paper identifies and fills a genuine gap: existing gradient-free attacks on XAI (e.g., GA-based) have only been applied to images and tabular data, with no prior work on time series (Section 2). The method can attack non-differentiable XAI methods (LIME, SHAP) that gradient-based approaches cannot handle.

- **Introduction of DTW as an attack objective function tailored for time series.** The paper compares DTW against existing image-oriented objectives (top-k, center-of-mass) and demonstrates that center-of-mass, designed for images, yields the poorest performance (Section 5.4). This provides empirical support that time series explanations benefit from dedicated objective functions.

- **Explanation-based local attack strategy with conceptual advantages.** The local attack perturbs only the 20% most important time points rather than the entire sample. The paper shows that this achieves comparable explanation disruption to global attacks while better preserving overall time series structure and reducing computational cost (Section 5.5, Figs. 2–3), addressing the real concern that perturbations are more perceptible in time series line plots than in images.

- **Empirical comparison across diverse models and XAI methods.** The paper evaluates 12 model+XAI combinations across two datasets (Table 1), identifying LSTM+SG as the most robust combination and SHAP as particularly vulnerable. This provides a useful initial map of robustness patterns.

## Weaknesses

### Fatal
None.

### Major

- **No comparison to any baseline attack method.** The experiments compare different variants of the proposed method (DTW vs. top-k vs. center-of-mass objectives; local vs. global attack) but do not include any external baseline — not random perturbation of the same magnitude, not a simple heuristic (e.g., adding small fixed noise to the top-k points without PSO iteration), and not the existing GA-based gradient-free attacks cited in Section 2. The abstract claims the paper "demonstrates the superiority of our proposed...method" and that it "compare[s] our approach with existing attack methods," but no such comparison is present. Without a random/no-optimization baseline, the reader cannot determine whether the observed explanation changes are attributable to the PSO+DTW optimization or simply reflect the inherent sensitivity of XAI methods to any targeted perturbation.

- **Missing experimental details that prevent reproducibility.** (a) Only one dataset is named (SZtick, Section 5.5); the other is never identified. No dataset characteristics are provided (dimensionality, time series length, number of samples, train/test splits, source). (b) Model architectures (LSTM, TCN, Transformer) are not specified — no layer counts, hidden units, or other design choices. (c) The threshold δ in Eq. 5 is never assigned a numerical value. (d) The 20% perturbation budget is used without justification or sensitivity analysis. These omissions constitute a significant reproducibility gap.

- **Local attack strategy lacks the critical control experiment.** The local attack selects the 20% most important time points from the original explanation and perturbs them. The comparison against global attack shows comparable effectiveness, but there is no control condition — e.g., randomly selecting 20% of time points, or selecting the 20% least important points. Without this control, we cannot determine whether the "explanation-based" selection strategy provides any benefit over arbitrary selection of the same number of points, or whether perturbing the explanation's own highlighted points is trivially effective.

- **Overclaim in the abstract versus actual experimental evidence.** The abstract states the paper "demonstrate[s] the superiority of our proposed objective function and local attack strategy" and claims comparison "with existing attack methods." In reality, the only comparisons are between variants of the proposed method (different objectives, local vs. global attack). There are no comparisons with any prior attack method from the literature. The experimental evidence supports that the method *works* to some degree, but not that it is *superior* to alternatives.

### Minor

- **Text reports only qualitative patterns, not specific numerical results.** While Tables 1 and 2 contain the experimental numbers (visible in the original PDF), the accompanying text describes results only in qualitative terms: "metrics close to 1," "relatively unstable," "differences...are minimal." The text would be strengthened by citing specific TKI, SRC, and DTW values to support the verbal claims. This also makes it harder for the reader to assess the magnitude of effects without repeatedly cross-referencing the tables.

- **Section 5.5 mentions "KS explanation"** (unclear abbreviation, possibly a typo for SG/SM or another XAI method), but "KS" is not defined anywhere in the paper.

- **Single-sample qualitative analysis for local vs. global comparison.** The comparison in Section 5.5 relies on one sample's visualization and heatmap (Figs. 2–3). Aggregate quantitative statistics across the full test set would provide stronger evidence for the claimed trade-offs between local and global attack strategies.

- **The "non-differentiable" claim about LIME is slightly imprecise.** The paper correctly notes that LIME's procedure (random sampling, distance weighting, model fitting) is not practically differentiable with respect to the input. However, a case could be made that LIME's optimization *can* be made differentiable with a smooth kernel and differentiable surrogate — the paper's practical point stands, but the absolute language could be qualified.

### Trivial
- Figure 1 is referenced in the introduction with "Fig.??" (likely a stale cross-reference), and the content of the figure is not described in the text.

## Nice-to-Haves
- Sensitivity analysis varying the perturbation budget ε and threshold δ would strengthen the practical relevance of the method.
- Varying the percentage of perturbed time points in the local attack (beyond the fixed 20%) would demonstrate robustness of the approach.
- Convergence analysis showing DTW fitness over PSO iterations would provide evidence that the optimization is actually searching rather than behaving like random search.
- Adding confidence intervals or variance estimates would help assess statistical reliability.
- A defense analysis (e.g., smoothing activations as described in Section 2) would be a natural next step.

## Removed Points
The following points from the reviews are flagged to be removed; treat them with caution:

- **"No quantitative results reported in text — fatal"** (Harsh Critic, Issue 2): The tables are embedded as images in the original PDF and contain numerical results. The parser strips these images, but they exist in the submission. The criticism that the *text* lacks specific numbers is valid (kept as a minor weakness above), but the claim that results are entirely absent is a parser artifact and has been downgraded from "fatal."

- **"The paper should not be accepted — fatal assessment"**: This is a judgment, not a verifiable weakness. The assessment is reflected in the score and decision below rather than listed as a weakness.

- **"Missing related works"**: Not mentioned by reviewers, so this rule is not triggered.

- **Various formatting/style nitpicks** about parser artifacts and image rendering: These are parser errors, not author errors.

## Novel Insights
Beyond the paper's own contributions, the most interesting synthesis from the reviews is the recurring observation that the paper's core methodological contribution (PSO+DTW local attack) is evaluated through comparisons that only involve its own variants. The experiments show that DTW performs similarly to top-k and that local attack performs comparably to global attack — but no control tells us whether *any* of these variants outperform a trivial perturbation of the same time points. This pattern suggests that the field of XAI adversarial attacks for time series would benefit from standardized benchmark protocols (datasets, metrics, baselines) before meaningful claims of "superiority" can be made, and that the paper under review is a useful first step that has not yet achieved that standard.

## Suggestions

1. **Add a random perturbation baseline and a no-optimization baseline.** Perturb the same 20% of time points with small random noise (without PSO iteration) and report TKI/SRC/DTW. This is the single most important missing experiment — it determines whether the PSO+DTW machinery is actually contributing value over a trivial alternative.

2. **Remove or correct the overclaim in the abstract about "comparing with existing attack methods"** unless such comparisons are added. The current experiments compare only variants of the proposed method, not prior attack methods.

3. **Add the missing control for the local attack strategy:** compare selecting the 20% most important points against selecting 20% random points and 20% least important points, all with the same PSO optimization.

4. **Provide full dataset and model specifications** (dataset names, sources, dimensions, sample counts, architecture details) and report the numerical value of δ used in experiments.

5. **Report specific numerical values in the text** (e.g., "TKI = 0.92 for LSTM+SG vs. 0.41 for LSTM+SHAP") rather than relying solely on qualitative summaries.

## Score and Decision

**Originality**: Moderate — the idea of gradient-free attacks on time series XAI is novel and underexplored. However, the PSO + DTW + local attack combination is a reasonable but not groundbreaking technical design.

**Importance of research question**: High — XAI robustness for time series is a practically important and understudied problem, with high-stakes applications in medicine and finance.

**Claims support**: Weak — the core claims are not adequately supported due to missing baselines, missing controls, and overclaiming relative to the actual experiments.

**Soundness of experiments**: Poor — the experimental design lacks fundamental controls (no baselines, no random perturbation comparison, no ablation isolating PSO's contribution). Reproducibility is compromised by missing dataset, model, and hyperparameter details.

**Clarity of writing**: Adequate — the method is clearly described and motivated. The experimental narrative suffers from the absence of specific numbers in the text.

**Value to the research community**: Potential — if properly validated with baselines and controls, the method and findings could serve as a starting point for research on time series XAI robustness. In its current form, the evidence is too weak to trust the claimed results.

MY FINAL SCORE: <pineapple>4.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>