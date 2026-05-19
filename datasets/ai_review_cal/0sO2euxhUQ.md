- Decision: Reject
- Avg Score: 4.00
- Scores: 5, 3, 3, 5
Now I have a thorough understanding of the paper and both reviews. Let me synthesize.

## Summary

The paper proposes a Bayesian variational inference method for jointly learning the causal variables, causal graph (structure), and parameters of a linear Gaussian latent Structural Causal Model (SCM) from low-level (high-dimensional) data, given known intervention targets. The key technical contribution is a posterior factorization (Eq. 7) where \(q(\mathbf{Z} \mid \mathcal{G}, \Theta) = p(\mathbf{Z} \mid \mathcal{G}, \Theta)\), which eliminates the need for hard alternating optimization between inference of latent variables and graph structure. Experiments on synthetic vector data and on a chemistry block-image dataset show the method outperforms VAE and GraphVAE baselines on structure recovery (E-SHD, AUROC), parameter recovery (MSE), and variable recovery (MCC).

## Strengths

- **Tractable posterior factorization that avoids hard alternating optimization.** The derivation in Section 4.2 (Eq. 7) shows that by factorizing as \(q(\mathbf{Z}|\mathcal{G},\Theta)\,q(\mathcal{G},\Theta)\) and noting that the posterior over \(\mathbf{Z}\) given \((\mathcal{G},\Theta)\) equals the prior \(p(\mathbf{Z}|\mathcal{G},\Theta)\), the KL term between them vanishes. This is a clean and principled solution to a known difficulty (cited from Brehmer et al., 2022), and it genuinely distinguishes the approach from naive two-stage or alternating schemes.

- **Strong results on synthetic linear-projection data.** When the node ordering (permutation) is given, the method achieves perfect graph recovery (\(\mathbb{E}\)-SHD = 0, AUROC = 1) for \(d=5,10,20\) across ER-1/2/4 graphs (Figure 2, Section 5.1.2). When the permutation is learned, performance remains good. These results cleanly demonstrate that the core inference machinery works for its target setting (linear Gaussian SCM, linear projection to observations).

- **Honest treatment of identifiability limits.** The paper explicitly acknowledges (Section 5.1.2) that permutation learning fails under *nonlinear* projections (3-layer MLP), connects this to theoretical identifiability results (Brehmer et al., 2022; Varici et al., 2022), and reports that performance in that setting is near the null-graph baseline. This scientific transparency is a strength.

- **Evaluation on a causally controlled image benchmark.** Rather than using CelebA with heuristic causal graphs, the paper evaluates on the chemistry environment (Ke et al., 2021), where the true causal graph, variables, and parameters are known by construction. This provides a more rigorous benchmark for latent causal discovery.

## Weaknesses

### Fatal
None.

### Major

1. **Ambiguity about whether the permutation is given or learned in the pixel (chemistry) experiment (Section 5.2, Figure 5).** This is the paper's strongest claim — that it learns the SCM from pixels — but the paper never states whether the true node ordering (permutation) is provided to the model or must be inferred. The synthetic experiments carefully distinguish the two cases (Figure 2 captions say "given a node ordering" vs. "over node orderings"; the nonlinear projection results explicitly say "given the permutation \(P\)"). By contrast, the chemistry experiment results (Figure 5) and its associated text contain no such statement. This matters because: (a) the paper's own analysis (Section 5.1.2) shows permutation learning fails under nonlinear projection and attributes this to identifiability theory, and (b) the chemistry environment's rendering from causal variables to images is a nonlinear mapping (even if not an arbitrary MLP). If the permutation was given, the evaluation does not test the full latent discovery problem. If it was learned, the near-perfect results contradict the paper's own earlier finding, and the discrepancy needs explanation. This must be clarified before the central experimental claim can be evaluated.

2. **Baselines are too weak to support the claimed advantage of joint inference.** The paper compares only against VAE (which assumes independent latents, trivially incapable of recovering causal structure) and GraphVAE (which learns edges but has no causal mechanism, no intervention modeling, and whose parameters are set to 1, harming its MSE). The paper acknowledges it is "the first to study this setting," yet it cites Brehmer et al. (2022) — a method that also learns latent causal variables and structure from low-level data under interventions (with different supervision: paired observational/interventional data). A comparison against Brehmer et al. (adapted to this setting) or even a simple two-stage baseline (train a VAE on interventional data, then run BCD Nets on the learned latent means) would isolate whether the proposed joint inference is necessary or beneficial. Without such baselines, the evidence does not demonstrate that the proposed method outperforms a reasonable alternative.

### Minor

3. **The MSE comparison with GraphVAE is weakened by the arbitrary weight assignment.** The paper states "Since GraphVAE does not learn the parameters, we fix the edge weight over all predicted edges to be 1." This choice likely inflates the MSE gap between the proposed method and GraphVAE. The paper should acknowledge this more prominently or report MSE only for methods that learn parameters.

4. **The paper uses an equal noise variance assumption (stated at line 48) but does not discuss its restrictiveness or its role in identifiability.** The equal noise variance assumption is known to enable identifiability in linear Gaussian SCMs (e.g., Ghoshal & Honorio, Hoyer et al., cited in the paper as gdseev). A brief discussion of how relaxing this would affect the method would help readers assess the scope of applicability.

5. **Limited discussion of the chemistry environment rendering process.** The paper says "blocks of different intensities according to a linear Gaussian latent SCM where the parent block colors affect the child block colors" and that the dataset allows "generating pixel data from random DAGs and linear SCMs." More detail on how causal variables map to pixels (is this rendering deterministic? known? learnable with a decoder?) would help the reader assess the experiment's difficulty and interpret the permutation ambiguity above.

### Trivial

6. The algorithm loops over \(N\) data points (line 168: "For \(i \gets 1\) to \(N\)") to perform ancestral sampling per data point. This is a minor expositional point but the inner loop could be clarified as vectorized.

## Nice-to-Haves

- An ablation study on the number of intervention sets and interventional data points would help practitioners understand data requirements.
- Runtime/wall-clock analysis for the main experiments would be informative.
- A discussion of whether the method can be extended to unknown interventions (acknowledged as future work in the conclusion).

## Removed Points

These were flagged for removal but are included with justification in case useful:

- *Criticism that the "first" claim is overstated given Brehmer et al. (2022)* — **Removed.** The paper's claim is scoped to "causal discovery in linear Gaussian latent SCMs from low-level data," which is a distinct setting from Brehmer et al. (2022) (which uses a different supervision modality: paired observational/interventional data). The claim is reasonable within its stated scope.  
- *Criticism that the paper does not discuss the equal noise variance assumption* — **Removed as factually incorrect.** The paper explicitly states "For linear Gaussian additive noise SCMs with equal noise variance, i.e., the setting that we focus on in this work" (line 48). The point about not discussing restrictiveness is retained as Minor Weakness #4.  
- *Criticism about missing related works* — **Removed per protocol (no external sources to confirm).**  
- *Criticism about lack of identifiability analysis* — **Demoted to Minor Weakness #4** since the paper does cite relevant identifiability results and discusses the permutation-learning limitation; a full theoretical analysis is not standard for an empirical systems paper.  
- *Several strength-finder "strengths" that were generic or sycophantic* — e.g., "this paper addressed an important problem" — **Removed.** Only concrete, evidence-grounded strengths are retained.

## Novel Insights

None beyond the paper's own contributions. The main synthesis insight from the reviews is that the paper's strongest empirical claim (pixel experiments) suffers from an ambiguity that neither reviewer can resolve from the text, and the baselines are too weak to confirm that joint inference is the source of the gains.

## Suggestions

1. **Clarify the chemistry experiment setup explicitly.** State whether the permutation is given or learned in the pixel experiments. If given, explain why the evaluation is still interesting (recovering variables, structure, and parameters from images with a known ordering is non-trivial). If learned, explain why the method succeeds where the synthetic nonlinear projection setting fails — what structural properties of the chemistry rendering make permutation learning possible (e.g., is the rendering a known deterministic function rather than an arbitrary nonlinear projection)?

2. **Add at least one stronger baseline.** Adapting Brehmer et al. (2022) or implementing a two-stage approach (e.g., VAE encoding → BCD Nets on latent means) would substantially strengthen the evaluation and help validate the claim that joint inference is worthwhile.

3. **Discuss the role of the equal noise variance assumption** for identifiability and what happens if it is violated.
