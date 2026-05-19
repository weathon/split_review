- Decision: Reject
- Avg Score: 4.50
- Scores: 3, 3, 6, 6
Now I have a solid understanding of the paper. Let me write the consolidated review.

---

## Summary

This paper proposes Denoising Diffusion Causal Discovery (DDCD), a framework that uses the denoising objective from diffusion models for causal structure learning. DDCD replaces the standard least-squares loss in NOTEARS with a diffusion-based denoising objective, applies the approach to both linear and nonlinear SEMs via a latent variable construction, and introduces a k-hop acyclicity constraint with reduced complexity. Experiments show competitive accuracy with significantly reduced runtime on synthetic and real-world (MI, yeast GRN) datasets.

## Strengths

- **Demonstrated computational scalability (well-supported).** Figure 3c shows DDCD models finish in ~20–30 seconds on 100-node graphs versus ~6 minutes for NOTEARS. The yeast GRN experiment (Section 4.6) processes a 4,980-node network in 34 seconds on GPU. These results directly support the paper's claim of substantial runtime reduction, which is the clearest contribution.

- **Consistent competitive performance on synthetic benchmarks.** Across linear and nonlinear synthetic data, DDCD variants achieve SHD and TPR competitive with or better than NOTEARS, DAG-GNN, GOLEM, and GAE (Figures 3b, 4b). The nonlinear model specifically recovers both structure (TPR 0.91 on ER-100) and an approximation of the nonlinear transformation function (Figure 4a), supporting the claim of extending structural learning to nonlinear settings.

- **The k-hop acyclicity constraint provides a useful, tunable relaxation.** Equation 17 defines a constraint that runs in O(k·d²) vs. O(d³) for the full NOTEARS constraint. Section 4.4 shows k=3 suffices to avoid DAG violations for most synthetic 100-node graphs. Critically, Section 4.6 finds that imposing full acyclicity harms GRN inference (consistent with known biology containing feedback loops), making the k-hop relaxation a meaningful contribution that the paper honestly evaluates.

- **Real-world interpretability demonstrated on MI dataset.** Section 4.5 and Figure 5 show that DDCD Smooth infers clinically meaningful edges (e.g., myocardial rupture → lethal outcome, pulmonary edema → nitrate use), supporting the claim that the method produces interpretable networks from real data.

## Weaknesses

### Fatal
None.

### Major

- **Theorem 1's claimed "equivalence" is technically overstated.** The paper claims the denoising objective (Eq. 8) is equivalent to the standard NOTEARS least-squares objective (Eq. 2). The derivation (Eqs. 9–12) shows that the denoising objective minimizes ||diag(√ᾱ_t)(X₀ − X₀W)||², not ||X₀ − X₀W||² directly. Since ᾱ_t varies across samples (each sample has a different time step t), the weighting is non-uniform. The claimed exact equivalence is incorrect as stated. This does not invalidate the method (the objective is still reasonable, and the smoothing benefit in Figure 2 is separately demonstrated), but the paper's central theoretical justification is overclaimed, and the paper provides no analysis of what objective is actually being optimized under the sampling distribution over t.

- **The nonlinear extension (Section 3.2) lacks principled justification.** The model introduces a latent variable Y = f₁(X) and assumes Y = YW + E₂, claiming "if an adjacency matrix W describes linear dependencies in Y, it could also be used to describe the dependencies in X." There is no theoretical guarantee that the autoencoder preserves causal structure — W is trained jointly on the denoising loss of Y and the reconstruction loss of X, and the latent space could capture spurious correlations. No ablation is provided showing that the learned W in Y-space directly corresponds to causal relationships in X-space. The empirical results on synthetic data are positive, but the internal logic of the architecture is not supported by analysis.

- **Missing comparisons to more recent baselines.** The paper benchmarks against NOTEARS, NOTEARS-MLP, DAG-GNN, GOLEM, and GAE. These are standard baselines, but the paper cites more recent methods (Sanchez et al. 2022 on topological ordering; Bello et al. 2022/DAGMA is cited in the introduction) without comparing to them. Given the paper's runtime and scalability claims, a comparison to methods like DAGMA that also target scaling would substantially strengthen the evaluation. The nonlinear SEM tested (x = Wᵀcos(x + ½) + ε) follows DAG-GNN's exact formulation, which may favor the comparison.

### Minor

- **Insufficient description of key architectural components.** The nonlinear model's f₁ and f₂ are not specified (are they MLPs? what layer sizes?). The "smoothed" version (Section 3.3) provides a conceptual description and references a "short proof" but is too vague to reproduce without the appendix. The role of γ in the k-hop constraint (Eq. 17) is not explained.

- **Optimization heuristic with no analysis.** Section 3.6 replaces the standard augmented Lagrangian with a simple linear multiplier, justified by "smoother training pattern." This is a heuristic change that could affect convergence, and no comparison to the standard optimization is shown.

- **No statistical variance reported for most benchmark results.** Figures 3b and 4b report SHD "over 10 runs" without error bars or standard deviations, making it difficult to assess whether differences between methods are significant.

### Trivial
None that survive filtering (parser artifacts removed).

## Nice-to-Haves

- An ablation replacing the denoising objective with the standard least-squares loss within the DDCD architecture (keeping all other components fixed) would directly test whether the denoising objective itself is the source of improvement, beyond the architectural changes.
- Providing GPU timings for all baselines (the paper uses CPU for all methods in Figure 3c, but DDCD likely benefits from GPU).

## Removed Points

- **"k-hop acyclicity constraint is poorly motivated and evidence against it is mixed" (from Harsh Critic).** REMOVED. The critic claims the constraint's benefits are contradicted by the GRN experiment, but the paper explicitly discusses that GRNs contain feedback loops and presents the negative result as an expected finding consistent with its message. The paper lists "We discuss when acyclicity is helpful and when it may not be" as a contribution, and does exactly that. This is not a contradiction — it is the paper honestly evaluating its own method.
  
- **"Strength: Fixed-size bootstrap sampling decouples training from dataset size" (from Strength Finder).** REMOVED. This is adopted directly from RegDiffusion (Zhu & Slonim, 2024), as the paper explicitly states. The paper presents it honestly as "the fixed-size bootstrap sampling design from RegDiffusion," so it is not a novel contribution of this paper.
  
- **"Strength: Theorem 1 proves equivalence" (from Strength Finder).** WEAKENED to note the overstatement (handled in Weaknesses). The empirical validation (Figure 2) is genuine.

- **Various formatting/style nitpicks, speculation about missing appendix content, and reproducibility nitpicks about trivial implementation details** from the Harsh Critic's "Missing Parts" section have been removed per the filtering rules.

## Novel Insights

None beyond the paper's own contributions. The reviews surface the tension between the claimed theoretical equivalence and what the derivation actually shows, which is a useful observation, but this emerged from analyzing the paper itself rather than from reviewer insight beyond what the text provides.

## Suggestions

- **Correct and clarify Theorem 1.** Acknowledge that the denoising objective minimizes a weighted version of the reconstruction error where weights depend on the diffusion schedule. Either frame it as an approximately equivalent objective that provides beneficial smoothing, or prove equivalence in expectation over the diffusion time step distribution.

- **Provide an ablation for the nonlinear model.** Show through systematic experiments that the latent variable Y preserves causal structure (e.g., by comparing W learned in Y-space against ground-truth W in X-space for synthetic data where both are known). Show the effect of removing the denoising loss term from Eq. 16.

- **Add more recent baselines.** Even a comparison to DAGMA on a subset of the synthetic benchmarks would substantially strengthen the evaluation, especially for the runtime claims.

- **Report variance/error bars** for the main SHD results (Figures 3b, 4b) to support the claim of competitive performance beyond a single point estimate.

- **Specify architectural details** (f₁, f₂ architectures, MLP design for the smoothed version, γ role, threshold for edge extraction in real-world experiments) in the main text or a clearly referenced supplement.
