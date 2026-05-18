Now I have all the information I need. Let me synthesize the final review.

## Summary

This paper presents a comprehensive empirical study of Bayesian neural network surrogates for Bayesian optimization, evaluating seven model families (GP, HMC, SGHMC, deep ensembles, LLA, I-BNN, DKL) across diverse synthetic and real-world benchmarks. Its key findings are: (i) surrogate rankings are highly problem-dependent, (ii) HMC is the best approximate inference method for finite-width BNNs, (iii) I-BNNs excel in high-dimensional settings, and (iv) deep ensembles perform surprisingly poorly. The study is extensive, timely, and fills a clear gap in the BO literature.

## Strengths

1. **Comprehensive evaluation across diverse problems establishes problem-dependent ranking.** The paper tests seven surrogate families on synthetic and real-world benchmarks spanning dimensions 2–100, single/multi-objective, continuous/discrete inputs, and non-stationary objectives (Figures 3–6). Figure 7 summarizes relative scores confirming no single model dominates globally, directly challenging the default use of GPs.

2. **Identification that I-BNNs excel in high-dimensional settings.** Figure 6 and Section 4.3 show I-BNNs consistently achieve the highest rewards on polynomial (d=40), NN function draw (d=100), and knowledge distillation (d=60) problems, while GPs and other BNNs lag. This provides a concrete, low-cost alternative to GPs for a known failure mode.

3. **Systematic sensitivity analysis on BNN architecture and hyperparameters.** Figures 1–2 and Section 3.2 isolate the effect of prior variance, likelihood variance, network depth, and width on posterior predictive distributions and optimization performance, providing practical guidance absent from prior work.

4. **Empirical demonstration that deep ensembles perform poorly as BNN surrogates under limited data.** Figure 3 shows ensembles plateauing well below competitors, with Section 4.4 confirming this is due to limited data (performance improves with more queries). This is a useful negative result given ensembles' popularity elsewhere.

## Weaknesses

### Major

1. **Fixed default architecture may disadvantage some inference methods.** The paper's main comparative experiments (Figs. 3–5) appear to use a single default architecture (3 hidden layers, width 128, tanh, prior variance 1, likelihood variance 1 specified for the visualization in Fig. 1). However, Section 3.2 demonstrates that the optimal architecture is problem-dependent (Fig. 2). While the paper notes in line 235 that hyperparameter variations have "minimal effects on the performance" (deferred to Appendix), the architecture search in Section 4.5 shows that better architectures can substantially improve BNN performance (e.g., on Pest Control). The concern is that deep ensembles—known to benefit from wider networks—may be differentially disadvantaged by this fixed choice, and HMC may be less sensitive to it because the full posterior compensates. The paper does not re-run the main comparisons with method-specific tuned architectures. This does not invalidate the core findings, but it weakens the generalizability of claims like "deep ensembles work surprisingly poorly" and "HMC works the best." The authors should temper these comparative claims to acknowledge they are conditional on the chosen architecture, or demonstrate robustness across architectures.

### Minor

2. **Single acquisition function limits scope of conclusions.** The paper uses only Monte-Carlo Expected Improvement (MC-EI) across all experiments (line 226). While MC-EI is the natural choice for BNN surrogates (it requires only posterior samples), different acquisition functions (e.g., UCB, KG) interact differently with uncertainty estimates. If some surrogates have poor uncertainty but good means (as the paper's own hybrid analysis suggests: GPs have better uncertainty, BNNs better means), the ranking could shift under acquisition functions that weight uncertainty more heavily. This is a scope limitation, not a flaw, but the conclusions should be understood as conditional on EI.

3. **The "problem-dependent ranking" finding is stated but not explained.** The paper's central finding is that no surrogate dominates and rankings depend on the problem. However, the paper does not analyze *what properties* of the objective (smoothness, effective dimensionality, degree of non-stationarity) predict which surrogate will excel. The analysis groups results by input dimensionality and multi-output objectives, but a more principled decomposition could turn the negative result into actionable guidance. For instance, measuring function length-scales, local roughness, or the overlap between the NNGP kernel and the true function could explain *why* I-BNNs work on some problems and GPs on others.

4. **Architecture search only demonstrated for HMC-based BNNs.** The architecture search (Section 4.5, line 315–318) shows improved performance for "BNNs" generically. The sensitivity study (Section 3.2) is conducted with HMC only ("We highlight results for HMC, as it is the gold standard," line 136). If the architecture search was only done with HMC-based BNNs, the claim that "performance of BNNs can significantly increase" (line 318) is somewhat broad, since the benefits may not transfer to SGHMC, LLA, or ensembles.

### Trivial

None.

## Nice-to-Haves

- Sharper situational characterization: the paper could analyze *why* certain objectives favor different surrogates (e.g., measuring effective dimensionality, assessing overlap between the NNGP kernel and the unknown objective kernel). Even a simple synthetic experiment where the true function is drawn from known kernels would strengthen the explanatory power.
- The hybrid mean/uncertainty ablation (Section 4.5) is insightful; providing the full quantitative results for a representative subset of problems (rather than a qualitative summary) would strengthen the evidence about whether mean or uncertainty drives performance.
- Testing robustness to a second acquisition function (e.g., UCB or KG) on a subset of problems would broaden the conclusions.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **"Missing number of MC samples for acquisition function"** – The paper defers experimental details to the appendix (line 363: "We provide the code needed to reproduce all experiments in the supplementary material attached"). Since the appendix is stripped by the parser, this detail cannot be confirmed as missing.
- **"I-BNN implementation vaguely described (NNGP vs NTK)"** – Likewise deferred to appendix and supplementary code.
- **"'Revisiting Standard Assumptions' section disconnected from narrative"** – This section tests whether standard GP assumptions (Matérn kernel, marginalization) are actually optimal, which is a valid and connected experimental contribution. It strengthens rather than undercuts the GP comparisons by showing robustness.
- **"Deep ensembles may be disadvantaged by fixed narrow architecture"** – This is already a sub-component of the fixed architecture concern (addressed in Major #1). The paper's own analysis (Section 4.4) shows ensembles improve with more data, offering a competing explanation. The concern is real but not a separate weakness.
- **"Fixed architecture may suppress ensemble expressiveness (width 128, prior variance 1)"** – Deep ensembles do not use a "prior variance" in the BNN sense; they use regularization/weight decay. The critic conflates BNN prior variance with regularization for ensembles. However, the underlying concern about architectural sensitivity stands and is captured in Major #1.
- **Generic/superficial strengths from Strength Finder** – All listed strengths are specific and evidence-backed; none were dropped.

## Novel Insights

The most novel synthetic insight is the paper's implicit observation that the value of different BNN inference procedures in BO roughly mirrors their sample efficiency: HMC (gold-standard, data-efficient) works best, ensembles (data-hungry) fail under limited data, and I-BNNs (fixed strong prior, no learned hyperparameters) excel in high dimensions where data is sparse relative to the input space. This suggests a trade-off between the strength of the prior and the amount of representation learning the data can support — a framing the paper could have made more explicit but that emerges clearly from the results.

## Suggestions

1. **Qualify comparative claims** as conditional on the chosen default architecture. Specifically, the statements about deep ensembles performing "surprisingly poorly" and HMC being "the most successful" should acknowledge that these rankings may shift with architecture.
2. **Add a small analysis** (even in prose) characterizing the problem properties that correlate with each surrogate's success. For example, compute empirical length-scales or local Lipschitz constants for a subset of benchmarks and show which surrogates handle which regimes.
3. **Report the full hybrid ablation results** numerically for a representative subset rather than only a qualitative summary, so readers can assess whether mean or uncertainty is the primary driver.
4. **Make experimental details explicit** (number of MC samples, NNGP kernel specification, architecture for each main experiment) in the main text or a clearly marked table, rather than relying entirely on the appendix.

## Score and Decision

MY FINAL SCORE: <pineapple>7.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>