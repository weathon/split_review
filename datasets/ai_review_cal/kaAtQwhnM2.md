- Decision: Reject
- Avg Score: 5.40
- Scores: 5, 6, 3, 5, 8
Now I have a thorough understanding of the paper. Let me produce the final review.

## Summary

This paper extends Energy Discrepancy (ED) — a contrastive loss functional originally developed for continuous data — to discrete spaces. The authors propose three families of perturbations for discrete data (Bernoulli noise, deterministic transforms, and neighbourhood-based perturbations), use importance sampling to make the contrastive potential tractable, and introduce gradient-informed proposals for variance reduction. Experiments on Ising model recovery, binary density estimation, graph generation, and image modelling demonstrate competitive performance without MCMC during training.

## Strengths

1. **Extends ED to discrete spaces with three principled perturbation families.** The paper formalizes Bernoulli, deterministic transform, and neighbourhood-based perturbations (Section 3.1), directly addressing the limitation of prior ED work that relied on Gaussian perturbations. This is the core technical contribution and is clearly motivated.

2. **Provides a consistency guarantee (Theorem 1).** The stabilised loss \(\mathcal{L}_{q,M,w}(U)\) is proven to converge almost surely to the exact energy discrepancy \(\mathrm{ED}_{q}(p_{\mathrm{data}},U)\) as \(N,M\to\infty\). This gives a theoretical foundation that contrastive divergence lacks, and the proof is sketched.

3. **Importance-sampling interpretation of the contrastive potential is principled and unifying.** Section 3.2 reframes the intractable sum over \(\{0,1\}^d\) as an expectation under a proposal distribution, enabling both uninformed and gradient-informed proposals within the same framework.

4. **Strong empirical results across diverse discrete tasks.** On 32D density estimation, ED methods outperform PCD, ALOE, and EB-GFN in most settings (Table 1). In graph generation (Table 2), ED achieves competitive or state-of-the-art MMD against nine baselines including RMwGGIS. The method scales to high-dimensional image datasets (MNIST, Omniglot, Caltech Silhouettes) with NLL competitive with DULA and GWG.

5. **Computational efficiency is a real advantage.** Training requires only \(M\) parallel energy evaluations per data point (no MCMC chains), representing a significant reduction compared to contrastive divergence which requires sequential MCMC steps.

## Weaknesses

### Fatal
None.

### Major

1. **Ambiguity in gradient-informed proposal's importance weight normalization.** In Section 4.1, the paper states that the normalization constant of \(\rho^{\nabla}_{\mathbf{y}}(\mathbf{x})\) is "independent of the negative samples and hence does not influence the direction of the parameter gradient." This is imprecise: the normalization constant \(Z(\mathbf{y}) = \sum_{\mathbf{x}'} \exp(-\frac{1}{\tau}\nabla U_\theta(\mathbf{y})^\top(\mathbf{x}'-\mathbf{y})) q(\mathbf{y}|\mathbf{x}')\) depends on \(\theta\) through \(\nabla U_\theta(\mathbf{y})\), and therefore \(\partial \log Z(\mathbf{y})/\partial \theta\) is non-zero and appears in the gradient of the loss (15). The paper does not clarify whether the implemented loss includes this term, drops it, or uses an unnormalized proposal density for the importance weight computation. If the term is dropped, the objective being optimized differs from the ED estimator of Theorem 1 and the theoretical guarantee needs re-examination. If it is included, the claim about the gradient direction is incorrect. **This must be clarified in rebuttal** — the practical implementation likely works (empirical results support it), but the theoretical framing as written is inconsistent.

### Minor

1. **No variance or effective-sample-size diagnostics for the importance sampling estimator.** The method relies on estimating the contrastive potential via \(M=32\) Monte Carlo samples in spaces of size \(2^{784}\) (MNIST). While Theorem 1 guarantees consistency as \(M\to\infty\), there is no empirical analysis of the estimator's variance, effective sample size, or how \(M\) should scale with dimension \(d\). Such diagnostics would substantiate the method's robustness and guide practitioners.

2. **Limited exploration of the deterministic transform perturbation.** Mean-pooling (ED-Pool) is introduced in Section 3.1 but barely analyzed: it appears only in Tables 1 and 4 without discussion of when it helps or hurts, and is absent from graph/image experiments. The paper would benefit from either a clearer rationale for including it or removing it to avoid clutter.

3. **Missing comparison to ratio matching in density estimation.** RMwGGIS (Liu et al., 2023) — the most closely related MCMC-free method — is included in graph generation (Table 2) but not in the density estimation experiments (Table 1). Including it would strengthen the claim that ED is the best MCMC-free approach. (Note: the baselines already present — PCD, ALOE, EB-GFN — are the standard ones from Zhang et al., 2022a, so this is a comparative gap rather than a flaw.)

4. **No hyperparameter sensitivity analysis.** The method depends on \(\epsilon\) (Bernoulli noise rate), \(\tau\) (gradient temperature), \(M\), and \(w\) (stabilisation). No ablation or sensitivity study is provided for any of these. Given that some choices (e.g., \(\epsilon\) controlling the bias-variance trade-off) are known to be critical, this limits reproducibility.

### Trivial
None.

## Nice-to-Haves

- Quantitative Ising recovery metric (e.g., Frobenius norm error of learned \(J\) vs. ground truth) would strengthen Figure 1 beyond qualitative heatmaps.
- Wall-clock time comparison with contrastive divergence methods would substantiate the efficiency claims.
- Individual MMD breakdowns (degree, clustering, orbit) for graph generation, rather than just the average.

## Removed Points

These points from reviews were verified against the paper and found to be inaccurate, speculative, or non-substantive:

- **"Gradient-informed proposal's Taylor expansion is not well-defined on discrete space"** (Harsh Critic, Point 1, later discussion): The paper explicitly acknowledges this limitation (line 154: "the Taylor series is technically not well-defined for discrete data") and justifies the linear approximation as meaningful. The criticism adds nothing beyond what the paper already concedes.
- **"MNIST misstatement"** (Harsh Critic, Section-by-Section): The critic claims the paper says there is a gap on MNIST while ED-\(\nabla\)Bern outperforms baselines. Checking Table 3: on MNIST, DULA achieves 73.28 NLL vs. ED-\(\nabla\)Bern's 83.02 — a real gap. The paper's statement is correct; the reviewer misread the table.
- **"Generation quality conflates training and sampling"** (Harsh Critic, Point 4): This is a generic concern applicable to nearly all EBM papers. The paper separates clean evaluations (Ising recovery, NLL via AIS) from generation metrics, and the wording is appropriately cautious.
- **"Weak baselines in graph generation"** (Harsh Critic, Point 3, second part): GraphVAE (2018), DeepGMG (2018), GraphRNN (2018) are standard baselines in the graph generation literature. The paper also includes more recent methods (EDP-GNN 2020, RMwGGIS 2023, GWG 2021). The comparison framework is standard and fair.
- **"Missing appendix content"** (Harsh Critic, Missing Parts): Parser-stripped content — not an author error.
- **"Weak baselines in density estimation"** (Harsh Critic, first part of Point 3): The baselines (PCD, ALOE, EB-GFN) are the standard set from Zhang et al. (2022a). The omission of RMwGGIS is noted above as minor, not a structural weakness.

## Novel Insights

The reviewer synthesis surface one insight worth highlighting: the gradient-informed proposal for the grid-neighbourhood perturbation (ED-\(\nabla\)Grid) empirically fails to improve over the uninformed version (ED-Grid), and sometimes performs worse (Table 3 on Caltech Silhouettes). The paper attributes this to the proposal "get[ting] trapped in local modes as it only flips one bit for each negative sample." This suggests a fundamental limitation of single-bit-flip gradient proposals for ED — unlike in CD where multi-step MCMC can escape local modes, the one-shot ED perturbation inherits the proposal's locality without the corrective iterations. This observation is useful for future work on discrete ED. None beyond the paper's own contributions.

## Suggestions

1. **Clarify the gradient-informed proposal implementation.** Provide the exact formula used for \(\log w_{\mathbf{y}}(\mathbf{x}_{-})\) in the loss (15) for both Bernoulli and grid-neighbourhood cases. If the normalization constant is dropped, explain why the resulting gradient direction is unaffected (or correct the paper's claim). If it is included, show the derivation.

2. **Add importance weight diagnostics.** Report effective sample size (ESS) or importance weight variance for the uninformed vs. gradient-informed proposals across different dimensions to ground the variance-reduction claims.

3. **Consider adding RMwGGIS to the density estimation tables** (or explain why it cannot be included) to make the MCMC-free comparison complete.

4. **Include hyperparameter sensitivity** for \(\epsilon\), \(\tau\), and \(M\) — even a brief ablation on a single dataset would significantly improve reproducibility.
