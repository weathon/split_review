Now I have a thorough understanding of the paper. Let me synthesize the review.

---

## Summary

This paper studies conformal prediction (CP) for time-dependent PDE surrogate models, where non-stationarity breaks the exchangeability assumption required for standard coverage guarantees. The authors make two theoretical contributions: (1) a proof that in function space, the distributions of PDE solutions at different times are mutually singular (maximal TV distance), making CP guarantees impossible in the infinite-dimensional setting (Theorem 4.1); and (2) a derivation showing that under discretized linear PDEs with Gaussian initial conditions, the solution at any time is Gaussian with explicitly computable mean and covariance (Theorem 4.2). Building on Theorem 4.2, they propose likelihood-weighted conformal prediction using the ratio of marginal densities of the discretized solution at different times (Equation 1). Experiments on synthetic PDEs show the method maintains target coverage where naïve CP and LSCI baselines fail.

## Strengths

- **Theorem 4.1 — A crisp negative result in function space.** The proof that Gaussian measures induced by the heat equation at different times are mutually singular, with TV distance exactly 1, provides a principled explanation for why CP methods relying on exchangeability or distributional similarity must fail in the infinite-dimensional setting. This result is clean, well-scoped, and motivates the shift to a discretized perspective. The proof is deferred to the appendix but the statement is clear.

- **Theorem 4.2 — Exact closed-form distributions for discretized linear PDEs.** The derivation of the Gaussian law of the discretized solution (mean and covariance via matrix exponential) is correct and self-contained. This provides the computational machinery — exact density ratios without estimation — that enables the weighting scheme. The result is stated with appropriate generality (linear spatial operator, Gaussian initial conditions) and the proof is given in the main text.

- **Compelling empirical demonstration of coverage maintenance.** Across multiple instability levels and PDE parameterizations (Figure 3, Table 1), the proposed weighted CP consistently stays near the 90% target coverage over up to 20 time steps, while naïve CP and LSCI coverage degrade severely in unstable regimes. The experiments are well-parameterized (three values of $a$, three values of $c$, multiple prediction horizons) and use substantial sample sizes (5000 calibration and test points each). The transparent reporting of $n_\infty$ (fraction of samples receiving infinite bands) is a good practice.

## Weaknesses

### Major

- **Theoretical gap in the justification of the weighting scheme (Equation 1).** The paper uses the ratio of *marginal* densities of the discretized solution $u_t$ to compute weights for weighted CP (Equation 1). However, the CP nonconformity scores depend on the full data pairs — the surrogate prediction (a function of the initial condition $u_0$) and the true solution. In the discretized setting, the joint distribution of $(u_0, u_t)$ is a degenerate Gaussian supported on an $n$-dimensional affine subspace of $\mathbb{R}^{2n}$, and these subspaces differ for different $t$, making the joint distributions mutually singular. The paper does not address why reweighting by the marginal density ratio of $u$ alone should yield valid coverage guarantees when (a) the score depends on both $u_0$ and $u$, and (b) the function mapping $u$ to the nonconformity score itself changes between calibration and test time (because the surrogate model's predictions and the PDE solution operator both differ). The claim of "exact coverage guarantees" (Abstract, Section 4.4) is therefore not adequately supported. The method may work as a well-motivated heuristic — and the empirical results suggest it does — but the theoretical foundation as presented is incomplete. This is the central claim of the paper and requires rigorous justification or appropriately hedged language.

- **Overclaimed guarantees in the abstract and introduction.** The abstract states the method provides "exact coverage guarantees… by reweighting calibration scores," and the introduction claims the method "enables exact coverage guarantees for PDEs without limiting assumptions." Given the theoretical gap described above, these claims are too strong. The method provides empirically reliable coverage in the tested settings, which is valuable, but the jump to "exact guarantees" is not justified by the analysis presented.

### Minor

- **Infinite-band mechanism not described in the main text.** The paper states that when "distributional dissimilarity… is too large, our WCP method predicts infinite bands" (Section 5, Evaluation), but the mechanism by which this decision is made is not described in the main paper. How does the method determine that the shift is too large? Is this based on a threshold on the weights, or some other criterion? This matters for understanding the method's behavior and for reproducibility.

- **Conditional coverage reporting could be clearer.** The paper reports empirical coverage only for samples that do *not* receive infinite bands, separately tracking $n_\infty$. While this transparency is appreciated, the paper could strengthen its presentation by also reporting unconditional coverage (treating infinite bands as trivially covering) to give a complete picture, and by more explicitly discussing the implications of this conditional reporting for the practical interpretation of the guarantees.

### Trivial

- None.

## Nice-to-Haves

- A discussion of what happens when the surrogate model's approximation error itself shifts over time (e.g., error accumulation in long-horizon rollouts) would strengthen the practical relevance. The method relies on the true solution distribution, but the surrogate's error characteristics may also drift.
- Extending the analysis to provide a bound on the coverage gap induced by using marginal rather than joint density ratios would be valuable for situating the method within the broader weighted CP literature.
- The real-world thermography experiment is described only via an appendix reference; a brief summary in the main text (one paragraph with key numbers) would help readers assess the practical applicability claim.

## Removed Points

These points were flagged by reviewers but removed from the main review after verification:

- **"The joint distributions are mutually singular, so the likelihood ratio is undefined — fatal flaw."** → While the joint distributions of $(u_0, u_t)$ are indeed mutually singular (degenerate Gaussians on different subspaces), the paper uses the *marginal* densities of $u$ which are non-degenerate and have a well-defined ratio. The issue is not that the ratio in Equation (1) is undefined — it is well-defined. The issue is whether marginal reweighting suffices for valid CP when the score depends on the full pair. This is reclassified as a Major weakness about insufficient justification, not a fatal mathematical error.

- **"The real-world experiment is only in the (unavailable) appendix — cannot assess validity."** → The appendix is not available due to parser stripping, not author omission. The paper states it exists and describes its high-level outcome. Removed as a parser artifact.

- **"The treatment of infinite bands is entirely unexplained."** → Downgraded to Minor. The paper does mention the mechanism exists and reports $n_\infty$; the missing detail is a presentation issue, not a methodological one.

- **Strength: 'The paper addressed an important problem.'** → Generic; removed as per instructions.

- **Strength: 'Real-world validation on pulsed-thermography data.'** → Kept only as context; cannot be independently verified without the appendix, but the paper claims it.

## Novel Insights

The paper's sharp formulation of the function-space singularity result (Theorem 4.1) is genuinely insightful: it shows that even for the elementary heat equation with a natural Gaussian prior, the solution measures at distinct times are mutually singular with TV distance 1. This crystallizes why the "neural operator on function space" perspective — while mathematically elegant — creates an insurmountable barrier for distribution-shift-aware CP, and why discretization is not merely a computational convenience but a *necessity* for recovering coverage guarantees. This tension between infinite-dimensional theory and finite-dimensional practice is clearly articulated and likely to be useful to researchers working at the intersection of operator learning and uncertainty quantification.

## Suggestions

- The authors should either (a) provide a rigorous argument connecting the marginal density ratio in Equation (1) to the validity of weighted CP for the specific score function used, or (b) temper the claims from "exact coverage guarantees" to "empirically achieves target coverage" and clearly state the assumption under which the weighting is expected to be valid (e.g., that the conditional distribution of the score given $u$ is approximately invariant across time steps). Option (b) is likely more achievable and would still leave a valuable paper.
- Describe the infinite-band decision rule explicitly in the main text, even if briefly.
- Consider adding a short paragraph to the main text summarizing the real-world thermography results with numerical coverage values.

## Score and Decision

**Round 1 bracket:** Based on comparison with anchors cF6OoaYcRa (4.50, CP for PDE UQ — weaker theory and experiments), LgfaMR6Sst (6.80, PDE active learning — stronger empirical depth but comparable novelty), and the 7.5+ anchors (clearly stronger papers), the paper plausibly sits in the **5.0–7.0** range.

**Round 2 narrowing:** Compared to aJ3tiX1Tu4 (6.67, Wasserstein-regularized CP under distribution shift — accepted, with rigorous theoretical bounds and practical algorithm), this paper has a less complete theoretical justification for its core claim. Compared to MxHgnYbxly (5.67, CP with temperature scaling — empirical study, moderate novelty) and GQhlM0Mavg (5.00, OOD-CP link), this paper has stronger theoretical contributions (Theorems 4.1, 4.2) and more substantive experiments. The paper is weaker than aJ3tiX1Tu4 but stronger than MxHgnYbxly and GQhlM0Mavg, placing it at approximately **5.5**.

**Anchor comparison summary:**
- cF6OoaYcRa (4.50, Reject): CP for PDE UQ — this paper has substantially stronger theory and more systematic experiments.
- GQhlM0Mavg (5.00, Reject): OOD-CP link — this paper has more original theoretical content.
- MxHgnYbxly (5.67, Reject): CP with temperature scaling — comparable empirical depth, this paper has more novel theory.
- aJ3tiX1Tu4 (6.67, Accept): Wasserstein CP under distribution shift — stronger theoretical foundations, our paper has a more focused application domain.
- LgfaMR6Sst (6.80, Reject): Flexible active learning for PDEs — comparable in ambition and scope but with different strengths.

The paper makes genuine contributions (Theorems 4.1 and 4.2, strong empirical validation) but the central claim of exact coverage guarantees through Equation (1) is not adequately justified. This is a significant but addressable weakness — the method is empirically valuable and the theoretical pieces are largely correct, but the connection between them needs either stronger proof or more modest claims.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>