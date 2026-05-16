Now I have a complete understanding of the paper and can verify all reviewer claims against the source. Let me write the consolidated review.

---

## Summary

This paper proposes a pipeline that combines differential pairwise affinity computation, non-negative tensor factorization (NTF), and nested weighted stochastic block modeling (NWSBM) to infer dynamic functional connectomes from calcium imaging data in *C. elegans*. The key innovation is tensorizing pairwise affinities (time × worms × neuron pairs) rather than raw neural activity, enabling the extraction of time-varying community structures that align with experimental stimuli. A biological experiment silencing the predicted neuron AWB confirms its unexpected role in salt sensation, providing real validation of the method's predictive utility.

## Strengths

- **Novel tensor formulation for dynamic connectome discovery**: The paper introduces a tensor with dimensions time × worms × pairwise affinities (rather than neurons × time), which allows non-linear affinity computation prior to factorization and enables NTF to automatically discover temporal intervals where affinity patterns are preserved across animals (Section 2.2, Fig. 2b). This is a genuine methodological contribution that addresses a real gap in the connectomics literature.

- **Experimental validation of a surprising biological prediction**: Silencing AWB (predicted by the algorithm to cluster with the salt-sensing circuit despite being canonically an aversive olfactory neuron) produced a significant +25% increase in salt avoidance (p = 5.7e-11). The result contradicts the expected outcome (silencing an aversive neuron should *decrease* avoidance), making it a non-trivial and biologically interesting discovery that demonstrates the method's ability to generate testable hypotheses beyond known circuit annotations (Section 3.2, Fig. 4).

- **Biologically motivated differential affinity measure**: The paper defines local affinity based on the sign and magnitude of derivatives during monotonic changes, avoiding pitfalls of standard global correlation (e.g., high cosine similarity between two silent neurons). The measure captures both coincident increases and decreases in activity and is interpretable as likelihood of interaction (Section 2.1, Fig. 2). The approach is clearly differentiated from prior work using static correlation (e.g., Yemini et al., 2021).

- **Principled community detection with automatic model selection**: The choice of NWSBM is justified by a benchmark on synthetic weighted networks (Table 1), where NWSBM achieved the highest mean NMI on 6 of 9 network types. The method uses Bayesian inference and description-length minimization, requiring no hyperparameter tuning and providing model averaging via MCMC (Section 2.3).

## Weaknesses

### Fatal
None.

### Major

- **The core differential affinity computation is underspecified to the point that the method cannot be reproduced.** The paper states that affinities are computed from "periods of monotonic increase or decrease" using "absolute derivatives" (Section 2.1), but never defines: (a) how the start and end of a monotonic interval are detected (threshold on derivative sign duration? smoothing method?); (b) whether the affinity is a single scalar per time point or per interval segment; (c) whether the measure is computed pointwise or over a sliding window; (d) what exactly is compared — the derivative values, their signs, their magnitudes, or their absolute values. The phrase "how likely it is for the two neurons to be interacting" is intuitive but mathematically vague. Since the affinity computation is the pipeline's first step, this underspecification propagates uncertainty through all downstream results. This is the most consequential weakness because it prevents independent verification and future use of the method.

- **The paper's claims substantially exceed what the evidence supports.** The abstract states the method can "robustly predict causal interactions between neurons to generate behavior," and the introduction claims "our results are confirmed with experiments that silence specific neurons." However, only *one* neuron (AWB) was silenced, and the experiment tests only whether that neuron's ablation alters a behavior — it does not validate the inferred *community structure* (which other neurons form the community, the temporal dynamics, or the tensor factorization itself). A single ablation of one neuron, even if well-executed, does not constitute robust validation of "causal interactions between neurons" (plural). The paper would be stronger if claims were calibrated to match the evidence: e.g., "generates testable hypotheses about functional roles of individual neurons, one of which was experimentally confirmed."

- **Critical methodological details that govern the pipeline are missing.** The paper does not report: (a) the number of neurons remaining after restricting to sensory/interneurons (started at 189, but the filtered count is not given); (b) the time resolution of the recordings or the resulting tensor dimensions (T, W, P); (c) the number of tensor components R used and how it was selected — this is a non-trivial model selection problem in CP decomposition; (d) whether the tensor factorization was run once or with multiple random initializations, and whether shown components are representative. The paper references "~A1 for details" for the LFR benchmark parameters, but this appendix content was stripped by the parser. Some of these details are standard to report and their absence weakens reproducibility.

### Minor

- **The community detection benchmark does not evaluate the full pipeline.** Section 4.3 benchmarks NWSBM against other methods on LFR synthetic networks, which tests only the community detection component in isolation. The NTF factors fed into NWSBM have unknown structural properties (sparsity, noise characteristics) that LFR networks may not simulate. Moreover, the absolute NMI scores are low for all methods (mostly 0.2–0.65), and on Net 8, three competitors achieve NMI=1.0 while NWSBM scores only 0.51. This does not convincingly justify the choice of NWSBM over simpler alternatives, though the paper's claim that NWSBM "outperformed the others in the majority of cases" (6/9) is technically correct. A full-pipeline comparison on the real data (e.g., against sliding-window correlation + Louvain) would have been more informative.

- **Incomplete statistical reporting for the validation experiment.** The p-value (5.7e-11) and effect size (+25%) are reported, but the baseline avoidance rate, the test used (t-test? permutation test?), means and standard deviations per condition, and whether the experimenter was blinded are not stated. Without these, the reader cannot fully assess the robustness of the result.

- **No systematic analysis of how tensor components were selected for presentation.** Figures 3 and 4 show only a few components that align with stimulus times. It is unclear how many components were extracted (R = ?), whether any were uninterpretable, and what criterion was used to select which components to analyze via community detection. The pipeline description suggests the NTF "automatically cluster[s] affinity networks," but the mapping from NTF components to community detection is ad-hoc without a principled selection criterion.

### Trivial

- The paper states "unsupervised approach" in the abstract, which is broadly correct for the NTF step but the community detection uses a generative model with Bayesian inference. This is a minor framing imprecision.

- Discussion over-generalizes to "social and ethological situations" without evidence, but this is typical and not harmful.

## Nice-to-Haves

- **Full-pipeline baseline comparison on real data**: Compare the proposed method against a simpler approach (e.g., sliding-window Pearson correlation + Louvain/spectral clustering) on the *C. elegans* data to quantitatively demonstrate the value of NTF and the nonlinear affinity measure.

- **Validate additional predictions**: The paper identifies "several neurons not previously known to play a role" in salt sensation. A table listing all predicted neurons with prior literature support for each, plus even a computational validation (e.g., cross-worm prediction), would substantially strengthen the claim.

- **Sensitivity analysis**: Show how results change with respect to key hyperparameters — the smoothing bandwidth for derivative computation, the minimum monotonic interval length, and the number of tensor components R. This would address concerns about robustness.

- **Dedicated limitations paragraph**: A candid discussion of the method's assumptions (e.g., that affinity patterns are stationary within a tensor component, the lack of statistical tests for community significance, potential artifacts from the histamine-gated silencing system) would strengthen scientific credibility.

## Removed Points

These points were flagged by reviewers but removed based on the rules:

- **"The benchmark does not validate the full pipeline"** (weakened version kept as Minor — the original framing as a structural flaw was too harsh since the paper scopes this as "Comparison with other community detection methods," not a full-pipeline evaluation)
- **Criticisms about missing appendix content or "~A1 for details"** — the parser strips appendix sections; this is not an author error
- **Demands for broader validation against other methods not cited in the paper** — the paper's baseline choices are defensible within its scope
- **Claims that NWSBM's choice is unsupported** — the benchmark does show NWSBM scores highest on 6/9 networks, partially supporting the choice
- **Nitpicks about whether the approach is truly "unsupervised"** — a framing issue with no impact on the technical contribution
- **Demands that the paper should also cover fMRI or social network applications** — outside the paper's stated scope

## Novel Insights

The harsh reviewer raises the important point that the validation experiment, while positive, tests only one neuron's ablation on a population-level behavior, which does not validate the *community structure topology* or the tensor factorization's temporal segmentation. This is a genuinely insightful criticism: the paper's central claim is about discovering *dynamic community organization*, but the experiment only tests whether a single predicted neuron affects a behavior. These are different kinds of claims. Beyond this, the reviews do not produce a genuinely novel insight that the paper itself does not already articulate.

## Suggestions

1. **Provide a precise, step-by-step algorithmic definition of the differential affinity measure** (pseudocode or explicit formulas). This is the single highest-impact improvement for reproducibility. Specify: how derivatives are computed (smoothing method, filter size), how monotonic intervals are detected, and how the scalar affinity value is derived from the derivative comparison at each time point.

2. **Calibrate the claims to match the evidence.** Replace "robustly predict causal interactions between neurons" with language such as "generates testable hypotheses about functional circuit membership, one of which is experimentally validated here."

3. **Report all standard methodological details** that govern the pipeline: tensor dimensions (T, W, P), number of components R and how it was selected, number of neurons after filtering, number of MCMC runs for model averaging, and the specific statistical test used for the behavioral assay.

4. **Add a systematic overview of all tensor components** — how many there are, what fraction align with known stimulus intervals, and how components were selected for community detection analysis.

5. **Include a limitations paragraph** addressing the key assumptions and potential failure modes of the pipeline.

## Score and Decision

The paper addresses an important problem — inferring dynamic functional connectivity from neural activity — and the central idea of tensorizing pairwise affinities rather than raw traces is novel and well-motivated. The experimental validation of AWB's role in salt sensation, while limited to one neuron, is a real strength and demonstrates the pipeline's practical utility. However, the core contribution is substantially weakened by the underspecification of the affinity computation, the mismatch between the strength of the claims and the evidence, and the missing procedural details that prevent reproducibility. The paper is on the right track and the ideas are promising, but in its current form the methodological description is too incomplete to be published as a citable reference. I recommend major revision with specific emphasis on specifying the affinity algorithm and calibrating claims.

MY FINAL SCORE: <pineapple>5.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>