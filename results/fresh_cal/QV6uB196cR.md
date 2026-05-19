Now I have a thorough understanding of the paper. Let me synthesize the final review.

## Summary

2-3 sentence summary of the paper's contribution.

## Strengths

- strength 1 with evidence
- strength 2 with evidence

## Weaknesses

### Fatal

### Major

### Minor

### Trivial

## Nice-to-Haves

## Removed Points

## Novel Insights

## Suggestions

## Score and Decision

Let me write this up carefully.

---

After a thorough reading of the paper, here is my analysis:

**Verification of Harsh Critic points:**

1. **Assumptions not enumerated (line 137, "Under Assumptions A1-7")**: The paper references A1, A2, A3, A4-6, A7. A2 is stated as the outcome model equation (line 97-100). A3 is referenced involving φ (line 104), likely detailed in the image at line 102 (parser-stripped). A4-6 are referenced collectively at line 139 but never individually enumerated. A7 is described on line 141 (superset decomposition). **Verdict: Partially true** — A1 is never mentioned individually, and A4-6 lack individual statements. Keep as Major.

2. **Missing naive exposure baseline (Section 5.1, 5.2)**: The experiments compare against methods using either the true graph (Poly/Exp/HT) or no graph (DM). No baseline uses the assumed graph M directly in the exposure model without the VAE. **Verdict: Valid** — this baseline would isolate the VAE's contribution. Keep as Major.

3. **Power plant experiment (Section 5.4)**: The critic says it lacks ground truth. The paper says "comparable estimates to other oracle estimators" — a factual claim, not a validation claim. **Verdict: Invalid criticism** — this is standard practice for real-data experiments in causal inference. Remove.

4. **Identifiability argument sketchy (Section 4.3)**: The independence of Δe_i from true e_i is asserted but the argument (Bernoulli randomization across devices → error from extra devices is independent) is not formally spelled out. **Verdict: Valid Minor concern**.

5. **Model specification missing details (Remark 3, line 131)**: Only says "MLPs with one hidden layer and ReLU activation." Training hyperparameters absent. **Verdict: Valid Minor concern**.

6. **Airbnb M construction not explained (Section 5.2)**: Paper doesn't state how the assumed graph was built. **Verdict: Valid Minor concern**.

7. **Network uncertainty only qualitative (Section 5.3)**: Figure 5 shows bias but no RMSE. **Verdict: Valid but minor — nice-to-have**.

Now writing the review.## Summary

This paper addresses A/B testing under "identity fragmentation"—when a single user's devices are not linkable, so the true interference graph between devices is unknown. The authors formalize this as a treatment-effect estimation problem where only a superset of each user's devices is observable, model the true exposure as a latent variable, and propose a VAE-based estimator that treats the exposure computed from the superset graph as a noise-corrupted version of the true exposure. The method is backed by an identifiability argument connecting the setting to nonparametric regression with measurement error (Schennach & Hu, 2013). Experiments on synthetic Erdos-Renyi graphs (linear and quadratic outcomes) show near-zero bias across varying interference strengths, graph sizes, and treatment probabilities. An Airbnb-based simulator demonstrates robustness to model misspecification, and a real-data power-plant application shows the method's practical deployment.

---

## Strengths

1. **Formalizes a timely, practically relevant problem.** The paper clearly identifies identity fragmentation (multi-device usage, GDPR, IDFA deprecation) as a concrete threat to standard A/B testing infrastructure, and grounds it in the interference literature (Section 1). The framing—where the true device graph is unknown but a superset is available—is well-motivated and distinct from standard "known-graph" interference settings.

2. **Principled VAE-based estimator for latent exposure.** Treating the true exposure as unobserved and modeling the noisy (superset) exposure as a measurement-error proxy is a natural and principled approach. The use of the importance-weighted ELBO (Burda et al., 2016) and the DReG gradient estimator (Tucker et al., 2018) for stable training is technically sound (Section 4.2). The model handles GLM-style outcomes with neural-network parameterization.

3. **Strong synthetic evidence.** On Erdos-Renyi graphs with both linear and quadratic outcome models, the proposed estimator achieves near-zero relative bias across a wide range of interference strengths \(r\), population sizes \(n\), and treatment probabilities \(p\), while difference-in-means and polynomial regression (even with oracle true-graph knowledge) show large systematic bias (Figure 3, Section 5.1). This directly supports the core claim.

4. **Robustness to model misspecification.** The Airbnb simulator does *not* follow the assumed exposure mapping, yet the method achieves bias and MSE comparable to the Oracle Exposure model (which knows the true graph) (Figure 4, Section 5.2). This demonstrates that the VAE correction works beyond the exact model class used for derivation.

5. **Sensitivity analysis on network uncertainty.** Section 5.3 systematically varies the percentage of added/omitted edges and confirms the expected trade-off: supersets reduce bias (with increased variance), subsets increase bias (Figure 5). This provides practical guidance for when the method is reliable.

---

## Weaknesses

### Fatal
None.

### Major

1. **Assumptions A4–A6 are not individually enumerated.** Proposition 1 (identifiability, line 137) invokes "Assumptions A1–7," but the paper never provides a self-contained list. A2 is stated as the outcome model equation (line 97), A3 is described (line 104, detailed in a parser-stripped image), A7 is described (line 141), but A4–A6 are referenced only as a group (line 139: "Under A2,4-6, the problem becomes a model fitting problem") without individual statements. A1 is never mentioned individually. Because the identifiability argument is the theoretical foundation of the paper, the reader cannot fully verify which conditions are assumed. This is fixable (add a clean numbered list) but as written, the theoretical contribution is incompletely specified.

2. **Missing "naive exposure" baseline using the assumed graph without the VAE.** Every experiment compares the proposed method against baselines that either ignore the graph entirely (DM) or use the *true* graph (oracle Poly/Exp/HT). No baseline takes the assumed (superset) graph \(\mathcal{M}\) and plugs it directly into the same exposure mapping *without* the VAE's latent-variable correction. This makes it impossible to isolate whether the observed bias reduction comes from the VAE's handling of uncertainty or simply from having superset information in the exposure model. Adding this baseline (e.g., feeding the assumed graph to polynomial regression) would directly test the value of the VAE inference step.

### Minor

1. **Independence of the measurement error is stated but not formally justified.** Section 4.3 (line 141) asserts that under A7, \(e_i(\mathcal{M})\) decomposes as \(e_i(\mathcal{N}_i) + \Delta e_i\) where \(\Delta e_i\) is independent of \(e_i(\mathcal{N}_i)\). The reasoning follows from Bernoulli randomization (treatments assigned independently across devices, so error from extra devices is independent of exposure from true neighbors), but this formal step is not spelled out. Since the entire identifiability reduction to Schennach & Hu (2013) depends on this independence, a brief formal argument would substantially strengthen the theory.

2. **Training details are underspecified.** Remark 3 (line 131) states all networks are MLPs with one hidden layer and ReLU. However, learning rate, batch size, number of epochs, ELBO convergence criteria, number of importance-weighted samples \(K\), and the specific parameterization of \(p_\theta(Y|E,X)\), \(p(\tilde{E}|E)\), \(p(E|Z)\), and \(q_\phi\) are absent. This limits reproducibility.

3. **Airbnb experiment does not state how the assumed graph \(\mathcal{M}\) was constructed.** The paper describes the true data-generating process for the Airbnb simulator but not how the assumed neighborhood \(\mathcal{M}(i)\) was derived from it. Was it a random superset? Based on covariates? Without this, the reader cannot assess whether the experimental conditions match the method's superset requirement.

4. **Network uncertainty analysis (Section 5.3) is descriptive rather than quantitative.** Results are presented as relative bias curves with no formal comparison (e.g., RMSE, coverage) across conditions. The observed trade-off is consistent with the method's logic, but the section would benefit from tabular metrics.

### Trivial
None.

---

## Nice-to-Haves

- Adding RMSE alongside relative bias in the network uncertainty experiment (Section 5.3) would strengthen the quantitative analysis.
- A brief discussion of how to obtain or validate a superset graph in practice, and the practical limitations of the method when validation is impossible, would be valuable.

---

## Removed Points

**"The power plant experiment lacks ground truth and is not supportive" (Harsh Critic #3).** The paper states only that the method "provides comparable estimates to other oracle estimators" (Section 5.4, line 200)—a factual observation, not a claim of validation. Real-data experiments in causal inference routinely demonstrate practical applicability without known ground truth; this is standard practice. The criticism is removed as it misunderstands the role of this experiment.

---

## Novel Insights

The harsh critic's most insightful observation is the missing naive-exposure baseline. By comparing only against oracle (true-graph) and no-graph methods, the experimental design conflates two distinct benefits: (1) the value of superset information itself, and (2) the VAE's correction for the uncertainty in that superset. A baseline using the assumed graph directly in a standard exposure model would disentangle these and could either strengthen the paper's claims (if the VAE clearly outperforms) or reveal that the superset information alone explains most of the bias reduction. The strength finder correctly identifies that the synthetic experiments (especially Figure 3) are the strongest evidence, but this evidence would be even more convincing if the naive baseline were included.

---

## Suggestions

1. **Add a clean, numbered list of assumptions A1–A7** in Section 4, with brief plain-language statements of each. This is essential for the identifiability claim to be verifiable.
2. **Add a naive exposure baseline** to the synthetic and Airbnb experiments: use the assumed (superset) graph \(\mathcal{M}\) directly in the polynomial regression or exposure model *without* the VAE latent variable. This directly tests whether the VAE correction is responsible for the bias reduction.
3. **Provide a short formal justification** (1–2 sentences) of why \(\Delta e_i\) is independent of \(e_i(\mathcal{N}_i)\) in Section 4.3, exploiting independent Bernoulli assignment.
4. **Specify training hyperparameters** (learning rate, batch size, epochs, \(K\), convergence criteria) for the VAE in the experimental section or an appendix, and describe the parametric forms of the generative and variational distributions.

---

## Score and Decision

The paper addresses an important, timely problem with a principled method and strong experimental evidence. The two major weaknesses—incomplete assumption enumeration and a missing baseline—are both fixable and do not undermine the core contribution. I recommend acceptance conditional on addressing these points.

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>