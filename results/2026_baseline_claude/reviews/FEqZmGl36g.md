Now I have a thorough understanding of the paper. Let me write the review.

---

## Summary

ESS-Flow is a training-free, gradient-free method for controlled generation with pretrained flow-based generative models. The core insight is that sampling in the Gaussian source space of such models (rather than the complex data space) causes Jacobian terms to cancel, allowing exact pointwise evaluation of a posterior density without any Jacobian computation. The authors leverage Elliptical Slice Sampling (ESS), which is designed precisely for Gaussian priors with complex likelihoods, to perform MCMC in the source space. The method is demonstrated on materials design targeting extreme properties and on protein structure prediction from sparse distance measurements.

---

## Strengths

- **Elegant mathematical insight with genuine practical value.** The Jacobian cancellation in Equation (3) — that sampling from $\pi(z) \propto g(T_\theta(z))p(z)$ requires neither Jacobian computation nor gradients through $T_\theta$ — is clean, correct, and impactful. This perfectly aligns the problem structure (Gaussian prior, complex potential) with the algorithmic strengths of ESS.

- **Genuine capability gap filled: non-differentiable potentials.** The space-group experiment (Table 3) is particularly compelling: ESS-Flow achieves 92.3% target group membership using a binary indicator potential from a non-differentiable program, while gradient-based methods cannot even be applied. This is a real capability that competing methods simply cannot offer.

- **Strong empirical results on materials design.** In Table 2, ESS-Flow achieves mean absolute errors of 8.99, 10.53, and 1.85 for bulk modulus, shear modulus, and band gap respectively — improvements of 4–10× over the next-best method (DAPS). The histograms in Figure 3 confirm ESS-Flow concentrates mass near the target values. On the band gap S.U.N.T. metric in Table 3, ESS-Flow achieves 16.0% while all other methods are essentially 0.0%.

- **Honest discussion of limitations.** The authors explicitly acknowledge that ESS-Flow struggles when the prior poorly covers the target (e.g., noiseless image inpainting, exact equality constraints). This contextualizes the method's applicability and scope clearly.

- **Well-situated theoretically.** The authors cite and adapt Proposition 1 from Natarovskii et al. (2021) to establish geometric convergence of the Markov chain in the source space, providing rigorous theoretical grounding.

---

## Weaknesses

### Fatal
None.

### Major

- **Uniqueness (diversity) collapses for ESS-Flow in several tasks.** In Table 3, ESS-Flow's uniqueness rates drop to 46.1% (bulk modulus) and 30.5% (shear modulus), far below DAPS (80.8% and 74.6%). The S.U.N.T. metric partially recovers due to higher target-achievement rates, but low uniqueness suggests the MCMC chain may be under-mixing or collapsing to a small number of high-potential modes. This could limit the practical diversity of generated candidates in materials discovery, where diversity is critical. The paper does not analyze or explain this phenomenon, nor does it address whether longer chains or thinning would recover diversity.

- **Protein experiment is a single structure.** Only one protein (PDB:7r5b) is evaluated, and the modified distance observation protocol (truncating to < 6 Å, adding noise) makes direct comparison with ADP-3D and prior work less clean. With n=10 samples per method, statistical conclusions are weak. ESS-Flow achieves worse data fidelity ($d_y$ = 37.02 vs. 3.43 for ADP-3D), and while the authors argue ADP-3D produces unrealistic structures (ELBO, clash counts), the experiment does not show ESS-Flow finding structures that *both* fit the data and are realistic — it primarily preserves realism at the cost of data fit.

### Minor

- **Multi-fidelity sampling degrades severely for sharp targets.** Effective sample sizes of 0.1% and 1.0% for band gap and stability tasks render importance reweighting nearly unusable there. This is acknowledged, but presenting this as a contribution (Section 4.2 and 5.1.1) when it fails on half the tasks may overstate its current maturity.

- **Runtime comparison is deferred to the Appendix** without any in-text summary. Since ESS requires multiple ODE solves per proposal (potentially many during bracket shrinkage), understanding compute cost relative to baselines is important for a fair comparison. The claim that ESS-Flow uses "fewer function evaluations than unconditional generation" without context makes it hard to assess efficiency.

### Trivial

- The toy experiment in Figure 2 is well-chosen but uses a 2D problem; a slightly higher-dimensional illustration would strengthen the motivation.

---

## Nice-to-Haves

- An analysis of chain mixing length or autocorrelation would clarify whether the low uniqueness in Table 3 can be resolved by running longer chains.
- The multi-fidelity section would benefit from exploring delayed acceptance ESS (Bitterlich et al., 2025) as the authors themselves propose, even briefly, rather than only reporting a proof-of-concept that fails for sharp distributions.
- Including a second protein structure (different length or fold class) in Section 5.2 would make the protein results more generalizable.

---

## Novel Insights

ESS-Flow's key insight — that the change-of-variables from data space to source space exactly cancels the Jacobian determinant (Equation 3), transforming an intractable posterior into a form naturally suited to gradient-free MCMC — is an elegant application of a mathematical identity that, while straightforward in hindsight, has not been exploited in the controlled generation literature. Combined with the observation that ESS's elliptical proposals correspond to gradient-free connected exploration of data-space curves, this establishes a clean conceptual bridge between continuous normalizing flows and Gaussian-prior MCMC methods. The implication that any pretrained diffusion or flow model can serve as a plug-in prior for gradient-free Bayesian inference — without touching the noising schedule or training procedure — is a practically important contribution, especially for scientific applications relying on black-box simulators.

---

## Suggestions

- Report per-method wall-clock times and ODE function evaluation counts in the main paper, not only the appendix. A brief table summarizing compute alongside Table 2 would improve reproducibility and fairness assessment.
- Investigate and report MCMC diagnostics (autocorrelation length, effective sample size from MCMC perspective) to understand the low uniqueness rates, and try thinned or longer chains.
- For the protein experiment, consider reporting across multiple proteins or using a quantitative realism metric across the full set (not just the best-of-10), to strengthen statistical conclusions.

---

## Score and Decision

ESS-Flow makes a well-motivated and theoretically sound contribution to training-free controlled generation. The gradient-free formulation enables applications genuinely out of reach for competing methods (non-differentiable potentials, categorical quantization), and the materials results are convincingly strong. The main concerns are the diversity collapse in MCMC-generated materials and the limited scope of the protein experiment, but neither invalidates the core contribution. The paper is well-written, acknowledges its limitations honestly, and provides a useful tool for scientific generative modeling.

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>