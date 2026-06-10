Now I have all the calibration data I need. Let me write the final consolidated review.

## Summary

This paper proposes "Marginal Flow," a density estimation framework where a parametric distribution q(x|w) has its parameters w marginalized out by sampling them from a learnable distribution q_θ(w), realized by feeding base distribution samples through an unconstrained neural network f_θ. The model claims to uniquely combine exact density evaluation, single-step sampling, architectural flexibility, and manifold learning capability. The framework is demonstrated on synthetic datasets, simulation-based inference, Wishart distributions on positive-definite matrices, and manifold learning in image latent spaces.

## Strengths

- **Genuinely novel framework with unique property combination**: Table 1 positions Marginal Flow as uniquely combining exact likelihood, single-step sampling, efficient training, free-form Jacobians, and manifold support. The structural reason is clear: density evaluation only requires forward passes through f_θ and evaluating closed-form q(x|w_i), avoiding Jacobian determinants, inversions, or ODE solving (Section 2.2, lines 141–143). No existing method offers this specific combination.

- **Empirically demonstrated orders-of-magnitude runtime speedups**: Figure 3 shows Marginal Flow maintains near-constant ~10⁻³s runtime for both sampling and density evaluation across dimensions 10² to 10⁵, while NF and FM exhibit steep scaling and OOM errors. This is a concrete, well-documented advantage.

- **Fast convergence during training**: Figure 7 plots test log-likelihood vs. wall-clock time across five 2D synthetic datasets. Marginal Flow consistently reaches higher test log-likelihood in orders of magnitude less training time than NF, FM, and FFF — a genuine and practically relevant advantage.

- **Well-motivated marginalization with clear illustrative evidence**: Figure 1 directly demonstrates that optimizing fixed mixture components collapses to a discrete GMM with N_c=10, while resampling from q_θ(w) with the same nominal N_c produces a smooth learned density. This concretely motivates the core mechanism.

- **Flexible parametric family demonstrated beyond Gaussians**: Section 4.3 shows that replacing Gaussian q(x|w) with Wishart distributions enables learning distributions on symmetric positive-definite matrices. Marginal Flow achieves lower test KL than NFs on 10×10 matrices and scales to 100×100 matrices (d=5050) where NFs are computationally prohibitive (Figure 9). This is a non-trivial demonstration of the framework's modularity.

- **Training flexibility via both forward and reverse KL**: Figure 8 shows Marginal Flow can be trained with reverse KL divergence (requiring both efficient sampling and density evaluation from an unnormalized target), achieving comparable or better performance than NFs — a capability most competing methods lack.

## Weaknesses

### Fatal

None.

### Major

- **The "exact density" claim is misleading and central to the paper's positioning**: The model's density q_θ(x) = (1/N_c) Σ q(x|w_{θ,i}) is evaluated by sampling {z_i} from the base distribution, computing w_i = f_θ(z_i), and averaging. Because z_i are resampled per evaluation (line 58: "resampled from q_θ(w) at each iteration"), evaluating q_θ(x) twice at the same point x with the same parameters θ yields different values — it is a Monte Carlo approximation of the true marginal ∫ q(x|w) q_θ(w) dw. This is fundamentally different from a normalizing flow where q(x) is a deterministic function of x and θ. Yet Table 1 (line 25) gives both Marginal Flow and NF identical checkmarks for "Efficient exact likelihood." The paper never acknowledges this stochasticity, never analyzes how approximation quality depends on N_c, and never reports N_c values for any experiment. This claim permeates the abstract, Table 1, Section 2.2 ("The density q_θ(x) can be exactly evaluated"), and the conclusion. The paper should (a) acknowledge the density is a stochastic estimate and discuss its variance, (b) analyze how N_c affects density estimation quality, and (c) qualify the Table 1 comparison to distinguish deterministic exact density (NF) from stochastic exact density (Marginal Flow).

- **N_c is never analyzed or even reported**: The parameter N_c (number of mixture components sampled per evaluation) is critical — it controls the Monte Carlo approximation quality and computational cost scales linearly with it. The paper states N_c "is not required to be fixed" (line 58) and claims "the modeling capacity is not directly linked to N_c anymore" (line 64), but provides no evidence for this claim. No experiment reports what N_c values were used, and no ablation shows how performance varies with N_c. This is a significant omission for understanding the method's practical behavior.

- **Experimental evaluation is insufficient for the breadth of claims**: The core experiments are predominantly on 2D synthetic data. The most compelling non-toy benchmark — simulation-based inference (SBI, Section 4.2) — is entirely deferred to the appendix with only a brief SOTA claim in the main text (line 280: "Due to space constraints we report results in the Appendix in Figure 14"). The manifold learning experiments (Section 4.4) use entirely qualitative evaluation — no quantitative metrics (FID, interpolation smoothness, reconstruction error) are reported. Missing: any standard density estimation benchmark (UCI, tabular), high-dimensional evaluations beyond the Wishart case, and comparisons to modern flow matching variants or score-based methods.

### Minor

- **Universality claim lacks formal justification**: Section 2.1 states "The resulting marginal q(x) is universal for many families of distributions q(x|w), e.g. if q(x|w) is a kernel (Micchelli et al., 2006)" without proof that the specific construction — where q_θ(w) is realized via neural network f_θ from a base distribution — inherits this universality property. The Micchelli reference concerns universal kernels, but the paper's construction involves a different mechanism.

- **Runtime comparison details deferred**: The runtime comparison (Figure 3) is compelling but architecture details (N_c, network size) are in Appendix A.3.1. Since the speed advantage depends on implementation choices, having these details in the main text would strengthen the comparison.

### Trivial

None.

## Nice-to-Haves

- Analysis of how density estimation quality varies with N_c across different problem dimensions
- Quantitative metrics for manifold learning experiments (e.g., interpolation smoothness measures, Fréchet distance)
- A limitations section discussing failure modes and scalability concerns
- SBI results elevated to main text given it's the most compelling non-toy experiment
- At least one standard density estimation benchmark (UCI datasets) for direct comparability with the broader literature

## Removed Points
These points are flagged to be removed, treat them with caution:
- "Missing related works (MDNs, kernel methods, random features)": Removed per rules — cannot verify existence of external works not cited.
- "Multi-modal experiment is trivial": Removed — the paper explicitly addresses this concern (line 216: "Marginal Flow is not a mixture model...since w_i are always resampled") and Figure 5 shows competitors fail on this task.
- "Characterization of VAEs as limited is outdated": Removed — this is a style/related work nitpick that doesn't affect the core contribution.

## Novel Insights
The paper's genuinely novel contribution is the insight that marginalizing mixture component parameters through an unconstrained neural network mapping — with resampling at each training iteration — yields a framework that uniquely combines properties (density evaluation, single-step sampling, no architectural constraints, manifold support) that no existing method provides simultaneously. The key mechanism is that resampling w_i from q_θ(w) each iteration prevents collapse to a finite GMM while maintaining the ability to exactly compute the mixture density for any given realization. The Wishart extension (Section 4.3) is a particularly compelling demonstration of the framework's modularity: simply swapping q(x|w) enables a fundamentally different application domain (distributions on positive-definite matrices) with scale (d=5050) that competitors cannot match.

## Suggestions

1. **Address the stochastic density explicitly**: Add a section analyzing the variance of q_θ(x) as a function of N_c, report N_c values for all experiments, and qualify the "exact density" claim in Table 1 to distinguish it from NF's deterministic exact density.
2. **Add N_c ablation study**: Show how performance and runtime scale with N_c — this is essential for practical adoption.
3. **Move SBI results to the main text**: This is the strongest non-toy experiment and the SOTA claim is important enough to warrant full main-text treatment.
4. **Add quantitative evaluation for manifold learning**: At minimum, report interpolation smoothness metrics or downstream task performance.
5. **Include a limitations section**: Discuss scalability beyond current experiments, sensitivity to base distribution choice, and failure modes.

## Calibration Report

### Retrieved Anchors

**Round 1 (Bracketing):**
- WxLwXyBJLw — "Flow Matching for One-Step Sampling" (avg 3.25, Reject): Proposed one-step sampling for flow matching but with unclear methodology. Marginal Flow is clearly stronger.
- SEvJfuCtPY — "Phase-aware Training Schedule" (avg 3.00, Reject): Narrow contribution on training schedule for flow on Gaussian mixtures. Marginal Flow is clearly stronger.
- iXbUquaWbl — "End-to-end Learning of Gaussian Mixture Priors" (avg 6.50, Accept): Novel mixture prior for diffusion samplers. Comparable novelty but better evaluation depth. Marginal Flow is slightly below due to density claim issue.
- iTFdNLHE7k — "Kernelised Normalising Flows" (avg 6.75, Accept): Novel flow paradigm. Strong theoretical motivation, limited large-scale evaluation. Marginal Flow is below due to density claim issue.
- g7ohDlTITL — "Flow Matching on General Geometries" (avg 8.00, Accept): Foundational contribution. Marginal Flow is clearly below.
- 4NTrco82W0 — "Beyond Squared Error for GFlowNets" (avg 7.33, Accept): Different domain but clearly stronger evaluation and theoretical grounding.

**Round 2 (Narrowing):**
- oiDvwOhvjq — "Convex Potential Mirror Langevin Algorithm" (avg 5.50, Reject): Novel sampling method for EBMs with theoretical convergence proof but split reviews. Marginal Flow is comparable in novelty but has different weaknesses.
- Qfqb8ueIdy — "Unified Framework for Consistency Generative Modeling" (avg 5.00, Reject): Novel framework with weak evaluation (only toy + CIFAR-10). Marginal Flow is clearly above this.
- ZLSdwjDevK — "Riemannian Diffusion Mixture" (avg 5.67, Reject): Novel framework for manifold diffusion. Similar issues (overclaimed scalability, limited evaluation depth). Marginal Flow has broader applications and stronger speed evidence.
- kBNIx4Biq4 — "Lifting Architectural Constraints of Injective Flows" (avg 6.50, Accept): Novel framework with manifold learning, more thorough evaluation (toy/tabular/image), addresses theoretical concern. Marginal Flow is below due to density claim issue.
- 2Chkk5Ye2s — "Diverse Mixture of Generative Models" (avg 5.80, Accept): Different contribution type (mixture selection). Marginal Flow is comparable.
- 99YEbiBbdy — "Dimension-Independent Rates for Neural Density Estimation" (avg 6.75, Reject): Strong theoretical contribution. Different focus.
- BZtEthuXRF — "Manifold Diffusion Fields" (avg 6.67, Accept): Manifold-aware diffusion with strong evaluation. Marginal Flow is slightly below.

### Bracket and Final Positioning
Round 1 bracket: 4.5–6.5. Marginal Flow has a novel framework with unique property combination and strong speed evidence, but the "exact density" overclaim and limited evaluation depth weigh against it.

Round 2 narrowing: Compared against papers at 5.00 (clearly above), 5.50 (comparable), 5.67 (above due to broader applications), 5.80 (comparable), and 6.50 (below due to density claim and evaluation depth). This places the paper at **5.5** — in the lower-middle of the bracket, above borderline-reject papers but below clear accepts, reflecting genuine novelty tempered by the overclaim issue.

## Score and Decision

The paper proposes a genuinely novel framework with compelling speed and convergence advantages, demonstrated across multiple application domains including a non-trivial Wishart distribution extension. However, the central "exact density" claim is misleading (the density is stochastic, unlike NF's deterministic exact density), N_c is never analyzed or even reported, and the evaluation is predominantly synthetic/toy with the strongest benchmark deferred to the appendix. These issues prevent acceptance in current form, though the core idea has clear merit.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>