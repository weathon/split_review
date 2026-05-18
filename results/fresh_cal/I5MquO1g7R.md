Now I have all the information needed. Let me compose the final consolidated review.

## Summary

This paper proposes TV-HMM, a Hidden Markov Model variant with a time-varying transition matrix that directly models change point locations (start/end times of regimes). The method uses variational EM with a stochastic approximation for scalability, includes a theoretical consistency result (Theorem 1) showing exponential convergence rates under a specific initialization scheme, and extends to a semi-parametric variant using Maximum Mean Discrepancy. Experiments compare against five baselines on three synthetic models and a real-world Well-log dataset.

## Strengths

- **Novel modeling formulation.** The time-varying transition matrix Π_k (Section 2.1) has size N×N rather than K×K, where π_{k,i,j} directly encodes the probability that the k-th regime runs from time i to j. This is a genuine departure from standard HMM-based CPD (Chib 1998; Ko et al. 2015), which models N-step state-to-state transitions. The structure naturally enables an automatic relevance determination (ARD) mechanism: redundant regimes produce diagonal-concentrated Π_k values that can be thresholded away. Figure 2(c,d) empirically validates this sparsification effect.

- **Consistency result with explicit convergence rates.** Theorem 1 (Section 2.3) provides a formal statement that marginal probabilities Q(t_i(n)=1) converge to 1 at true change point locations and decay exponentially elsewhere as N grows. The rates are given in terms of distance from true locations (O(exp(-N^{|n-T_k|/T})) for non-junction points). Figure 2(a,b) validates this with Monte Carlo simulations showing the estimated number of change points stabilizing and MAE decreasing with N.

- **Comprehensive empirical comparison against five baselines.** Table 1 compares TV-HMM with WBSL, SW, ECP3O, KCP, D_m-BOCD, and DPHMM on three simulation models covering changes across distribution families (binomial/Poisson/normal), multi-dimensional Gaussian mean/covariance shifts (5-dim and 10-dim). TV-HMM achieves the highest Rand index on Model 2 and competitive performance on Models 1 and 3, demonstrating consistent accuracy across diverse settings.

- **Explicit theoretical connection between parametric and MMD variants.** Section 4 shows that under a Gaussian likelihood with fixed variance, the parametric message term reduces to a linear-kernel MMD form: -(n-m+1)·∥√Λ_k 𝔼[y] - √Λ_k 𝔼[u_k]∥², establishing that the MMD extension generalizes the parametric case. This is a conceptually clean bridge between the two variants.

## Weaknesses

### Fatal
None.

### Major

- **Theorem 1 is narrower than the paper's framing suggests, and the gap between theory and claims is not acknowledged.** The consistency result depends on Assumption A3: the algorithm initializes with change points at equal-distance segments, and these segments are pre-categorized as "junction" or "non-junction" relative to true change points. This proves that *if you already have a coarse grid covering each true location, the variational posterior will concentrate at the correct sites*. It does *not* establish that the method discovers correct locations from an agnostic over-specified initialization without such structured prior knowledge. The abstract and conclusion claim "statistical consistency of the change point location estimation" and "we prove that our algorithm consistently selects the true number and locations of change points" without qualifying the initialization requirement. This is a structural overclaim: the reader naturally interprets these as guarantees for the full algorithm under arbitrary over-specification, which Theorem 1 does not prove. (See Theorem 1 statement at lines 128-146, and the unqualified claims at lines 4-5 and 243.)

- **Algorithmic description of the stochastic approximation is insufficient for reproducibility.** The paper's scalability claim (O(K S²) per iteration) depends critically on the stochastic approximation variant described in one paragraph (lines 113) and Algorithm 1. However: (1) How the message-passing formalism (which operates over all N time indices via recursive sums over forward/backward messages) adapts to a random chronological subset of size S is not explained. The transition matrix over a subgrid and the "retrospective order set Ω" are not defined. (2) Algorithm 1 lines 5-7 contain garbled/incomplete references ("by Equation 3 based on sampled S observations, with; ..." with placeholder ellipses). (3) The conditions under which subsampling the E-step yields a consistent estimator (beyond a generic citation to Robbins & Monro 1951 for convex problems) are not provided. Without this detail, neither the complexity claim nor the algorithm's correctness can be verified from the paper as written.

- **MMD extension (Section 4) is evaluated without any baseline comparison.** The semi-parametric variant is presented as a contribution ("Generalize the parametric likelihood... free of distribution assumptions"), but its experimental evaluation reports Rand indices (0.9447, 0.8686, 0.8911) on three non-Gaussian examples with no comparison to any other distribution-free CPD method (e.g., KCP, ECP, or kernel-based alternatives). Without a baseline, the reader cannot assess whether these numbers represent a meaningful improvement or are simply within the range any reasonable method would achieve. This is a significant gap for a claimed contribution.

### Minor

- **No statistical significance or variability measures reported for the main benchmark (Table 1).** Rand indices are reported as point estimates without confidence intervals, error bars, or significance tests. Given that TV-HMM is competitive but not dominant (slightly behind DPHMM on Model 1, comparable to ECP3O on Model 3), the absence of uncertainty quantification makes it impossible to assess whether the differences are meaningful.

- **Well-log comparison is qualitative without ground truth.** The paper claims an advantage at timestamp 1540 where TV-HMM detects a change point that D_m-BOCD misses (Section 3.3, Figure 3). However, ground truth for this dataset is not available, so the claim that TV-HMM is "better" at this location is speculative — the other method's estimate could equally be correct. The comparison demonstrates a difference but not superiority.

- **Sensitivity to key hyperparameters is not explored.** The method introduces several tuning knobs (learning rate η, subset size S, number of EM iterations I, and for the MMD variant, the constant G and kernel choice). None of these are analyzed for sensitivity. The paper reports a single set of results without investigating how performance varies with these choices.

### Trivial
None.

## Nice-to-Haves

- The paper could discuss additional limitations beyond the piecewise i.i.d. setting (mentioned in the conclusion), such as reliance on the equal-distance initialization grid, the worst-case O(K N²) complexity without subsampling, the need to specify S, and the absence of a stopping criterion for EM iterations.
- Experimental comparison of wall-clock time for the full and stochastic versions would strengthen the scalability claim.
- A formal statement or proof sketch for the ARD mechanism (diagonal convergence implying vanishing redundant regimes) would complement the location consistency result.

## Removed Points

These points were flagged for removal; treat them with caution:

- **Criticism that parameter estimation (Table 2) lacks baselines (Harsh Critic Point 3, bullet 2).** The paper shows TV-HMM's MSE for mean and precision estimates as a demonstration of *capability* — the claim is that the method simultaneously estimates regime parameters, not that it outperforms baselines at this task. No baseline is needed for a capability demonstration. **Removed.**

- **Criticism that the paper "misrepresents the state of the art" by claiming the number of change points is "unidentified" in prior HMM work (Harsh Critic, "Missing Parts and Places to Improve").** The paper uses "unidentified" in the abstract as a general description of a challenge ("computational intensity... particularly when the number of change points is unidentified"). The related work section explicitly cites Ko et al. (2015) (DPHMM) which handles unknown state numbers. No misrepresentation. **Removed.**

- **Criticism that the model's difference from standard HMM-CPD is "one of parametrization, not a new capability" (Section-by-Section notes on Section 2.1).** The paper's contribution is the explicit N×N time-varying transition matrix that directly parameterizes start/end times, which is a fundamentally different design from K×K state-transition matrices. This is a genuine modeling innovation, not a cosmetic change. **Removed.**

- **Criticism about missing derivation details for variational EM (Section-by-Section notes).** It is standard for papers to present message-passing equations without full derivations; the equations themselves specify the algorithm. **Removed.**

- **Criticism about "missing appendix, missing proofs in appendix" content.** The parser strips appendices from all papers; these sections exist in the original submission. **Removed.**

- **Formatting nitpicks about garbled notation, broken text, etc.** These are parser artifacts, not author errors. **Removed.**

- **Strength Finder claim about Well-log robustness.** This conflicts with the verified weakness that the comparison is qualitative without ground truth. The paper detects a different change point but cannot claim superiority. **Removed.**

## Novel Insights

The most interesting observation that emerges from cross-referencing the reviews is the disconnect between the theory and the method's practical mode of operation. Theorem 1 assumes an equal-distance initialization grid with pre-categorizable junction/non-junction points, yet the paper's core selling point is the ARD mechanism that *discovers* the number and locations from over-specification. The theorem effectively analyzes a warm-started procedure where the grid already covers each true location, while the ARD dynamics it is meant to justify operate before convergence to that grid. Neither review surfaces this tension explicitly, but reading the theory and the experiments together — where the experiments deliberately "fulfill A3" (Section 3, line 156) — suggests the theoretical analysis and the method's advertised capabilities are operating at different levels of specificity.

## Suggestions

1. **Revise the claims around Theorem 1.** State clearly what the theorem does and does not guarantee: that under an equal-distance initialization covering all true change points, the variational posterior concentrates at the correct locations. Qualify the abstract and conclusion accordingly (e.g., "under a reasonable over-specified initialization, our method yields consistent location estimates").

2. **Flesh out the stochastic approximation.** Provide a self-contained description of how message passing operates on the sampled subset Ω, how the transition matrix is restricted to the subgrid, and how updated probabilities are propagated back to the full index set. Without this, the scalability claim is unverifiable.

3. **Add baselines for the MMD extension.** Compare against at least one distribution-free CPD method (e.g., KCP with RBF kernel, ECP) on the same three non-Gaussian examples. Report sensitivity to the kernel choice and the constant G.

4. **Include variability measures for Table 1.** Report standard deviations or confidence intervals for the Rand indices across multiple runs so the reader can assess whether TV-HMM's performance differences relative to baselines are meaningful.

5. **Acknowledge limitations about hyperparameter sensitivity.** Briefly discuss the role of η, S, and the initialization grid, and how robust results are to these choices.

## Score and Decision

**Originality:** 7/10 — The time-varying transition matrix formulation is a genuinely novel modeling choice for CPD, distinct from standard HMM parametrizations.

**Importance of research question:** 8/10 — Offline CPD with unknown number of change points is a well-motivated and practically relevant problem.

**Claims supported:** 5/10 — The theory is narrower than claimed; the MMD extension lacks baseline validation; the scalability claim is not backed by reproducible algorithmic details.

**Soundness of experiments:** 6/10 — Reasonable breadth (5 baselines, 3 synthetic models, real data) but lacks significance testing and the MMD evaluation is incomplete.

**Clarity of writing:** 5/10 — Core ideas are understandable but the theory section is ambiguous, the algorithm pseudocode is incomplete, and several claims are overstated relative to evidence.

**Value to community:** 7/10 — The modeling framework is likely to inspire follow-up work if the gaps in presentation are resolved.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>