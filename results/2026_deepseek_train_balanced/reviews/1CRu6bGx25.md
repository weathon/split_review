## Summary

This paper proposes FI (First-order local Influence), a stability measure for Large Language Models grounded in information geometry. FI quantifies the sensitivity of model outputs to local perturbations in either input space (pixels) or parameter space (weights), and is theoretically guaranteed to be invariant under diffeomorphic reparameterization — a property that alternatives like the Jacobian norm lack. The authors apply FI to four settings: pixel-level vulnerability analysis in a VLM (one qualitative example), parameter sparsification, mixed-precision quantization, and model merging, showing in each case that high-FI components are more impactfully perturbed than random or low-FI components.

## Strengths

1. **Genuine theoretical advantage with explicit demonstration.** Theorem 2.3 proves FI's reparameterization invariance, and the paper concretely shows why this matters (lines 71–83): under the ReLU scaling symmetry \((\theta_1,\theta_2) \to (k\theta_1, k^{-1}\theta_2)\), the Jacobian norm diverges as \(k\) grows while FI remains unchanged. This is a clear, grounded argument for FI over naive sensitivity measures.

2. **Controlled causal intervention.** In the VLM experiment (Section 3.1), masking the top-10 FI patches flips the model from a correct to an incorrect answer, while random masking with matched information loss does not. This head-to-head intervention provides causal evidence that FI identifies genuinely fragile input regions, not merely high-salience features.

3. **Quantitative benchmarks for quantization and merging.** The paper reports specific numbers: protecting 5% of high-FI channels mitigates "over 90% of the performance loss while requiring merely an additional 0.1 GB of memory" (lines 186–188), and the FI-Protect strategy yields "15–20% increase in performance across multiple benchmarks" for model merging (line 200). These concrete figures support the practical potential of the approach.

## Weaknesses

### Major

1. **No comparison against any existing method across all four experiments.** Every experiment compares FI only against random selection or low-FI baselines. The pixel-level analysis does not compare against any saliency method (GradCAM, Integrated Gradients, attention rollout). The parameter sparsification does not compare against magnitude-based pruning or Fisher-based importance. The quantization experiment does not compare against any actual quantization method (GPTQ, AWQ, etc.). The model merging experiment does not compare against DARE, TIES-Merging, or any existing forgetting-mitigation technique. Showing FI beats random is a necessary sanity check but does not establish that FI adds value over what already exists. The paper itself frames Hessian-based approaches as the alternative (Section 1, line 20: "Existing approaches... primarily rely on the Hessian matrix") but never benchmarks against them. Without any comparative evaluation, it is impossible to assess whether FI's theoretical advantages translate to practical benefits over the state of the art.

2. **External perturbation analysis rests on a single qualitative example.** The entire pixel-level vulnerability evaluation (Section 3.1) uses one image from ScienceQA with one question. The cross-modal prompt analysis is on the same single example. There is no quantitative aggregation across a dataset, no statistical significance testing, and no comparison to baselines. A single qualitative anecdote cannot support the paper's claims about "highlighting the value of our framework in conducting cross-modal analysis and improving model robustness" (line 155). This should be turned into a proper quantitative evaluation across the ScienceQA validation set.

3. **Parameter sparsification does not control for the confound with parameter magnitude.** The sparsification experiment (Section 3.2) compares FI-guided removal against random removal but not against magnitude-based removal (removing the largest-magnitude parameters). If high FI values correlate with large parameter magnitudes, the results could simply reflect the known fact that large weights matter more. This is a minimal control that the paper omits, and addressing it is necessary to establish that FI provides information beyond trivial correlation with weight scale.

### Minor

1. **No computational cost reporting.** The method requires computing and (potentially) inverting a metric tensor whose dimension matches the number of parameters or channels being perturbed. The paper acknowledges this as future work (line 209) but does not report any runtime, memory usage, or scaling behavior for its experiments. This makes it difficult to assess practical feasibility.

2. **Overclaimed psychological terminology.** The paper states that sparsifying high-FI parameters "induces catastrophic forgetting and hallucinations" (line 165), but the experiment measures only MMLU multiple-choice accuracy — a proxy for knowledge degradation, not a direct measurement of forgetting or hallucination phenomena. The claims should be calibrated to what the experiment actually measures.

3. **Novelty boundaries could be clearer.** The paper presents FI as a "novel influence measure" but the core theoretical framework — perturbation manifold, Fisher information metric, closed-form FI as \(\nabla f^\top G^{-1} \nabla f\), and reparameterization invariance — is inherited from Shu & Zhu (2019), Zhu et al. (2007), and Zhu et al. (2011), which the paper transparently cites. The genuine novel elements (adaptation to auto-regressive LLMs, sequence-generation FI formulation) are valuable but more modest than the paper's overall framing suggests. Explicitly delineating inherited vs. novel components would strengthen the paper.

### Trivial

- There is a minor inconsistency in the VLM experiment between computing FI "for each pixel" (line 139) and masking "top-10 FI value patches" (line 143). The granularity of the perturbation unit (pixel vs. patch) should be clarified.

## Nice-to-Haves

- Reporting confidence intervals or variance across random seeds for the sparsification and quantization experiments.
- A dedicated limitations section discussing the computational overhead of FI, the dependence on the choice of objective function \(f\), and the challenge of selecting the perturbation dimension \(\omega\).
- Extending the single-example VLM analysis to a quantitative dataset-wide evaluation.

## Removed Points

These points are flagged to be removed; treat them with caution.

- *Criticism about missing Table 1 content.* The table was stripped by the PDF parser; the original submission contains it. Removed per hard rule about parser artifacts.
- *Complaint that the paper "does not correspond to currently available systems" or questions release status of cited models/tools.* All cited models are assumed to exist per hard rules.
- *Criticism about "unfair comparison" that would favor the baseline.* No such issue applies here; the comparisons all favor the author's method (FI beats random), but the core weakness is the *absence* of comparisons to existing methods, which is a different criticism retained in Major #1.
- *Several generic "could be" speculation points from the harsh critic (e.g., "could the metric be measuring a proxy?")* — these lack concrete anchors in the paper and were merged into the specific verified weaknesses above.
- *Formatting/style nitpicks and requests for hyperparameters/complete training logs.* Removed per hard rules.

## Novel Insights

None beyond the paper's own contributions. The reviews surfaced no genuinely novel synthesis beyond what the paper itself presents.

## Suggestions

1. **Add comparative baselines** to all four experiment settings — at minimum one per setting: a saliency method (e.g., Integrated Gradients) for pixel-level analysis, magnitude pruning for sparsification, one existing quantization method (e.g., GPTQ), and one merging technique (e.g., TIES-Merging). This is the single most impactful improvement.

2. **Turn the VLM analysis into a quantitative evaluation** across the ScienceQA validation set: measure whether masking high-FI patches causes more errors than masking random patches or patches identified by other methods.

3. **Add a magnitude-based sparsification baseline** to the parameter sparsification experiment to control for the correlation between FI and weight scale.

4. **Report computation time and memory** for FI computation at the scales tested, so readers can assess practical trade-offs.

MY FINAL SCORE: <score>4.5</score>
MY FINAL DECISION: <decision>Reject</decision>