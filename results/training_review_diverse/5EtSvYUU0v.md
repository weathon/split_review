## Summary

This paper proposes a Markov Proximal Learning (MPL) framework for noisy gradient-based learning dynamics in infinitely wide deep neural networks. It introduces the Neural Dynamical Kernel (NDK), a time-dependent generalization of the NTK, and derives closed-form integral equations for the mean predictor dynamics. The framework unifies NTK and NNGP as two limits of a single stochastic process: NTK emerges at short times in the gradient-driven phase, while NNGP emerges at long times as the equilibrium of the diffusive phase. The theory is illustrated with numerical evaluations on synthetic data, MNIST, and CIFAR-10, and applied to early stopping and representational drift.

## Strengths

1. **Unified theoretical connection between NTK and NNGP as two limits of a single Langevin dynamics** — The paper derives exact analytical expressions showing that the NTK solution (Eq. 15) describes the initial gradient-driven phase, while the NNGP solution emerges as the long-time equilibrium (Sec. 4.1‑4.2). The key result is that both frameworks arise from the same underlying stochastic process, with the NDK interpolating between them. This is demonstrated mathematically, not just claimed.

2. **Introduction of the Neural Dynamical Kernel (NDK) with explicit recursive computation** — The NDK (Eqs. 7‑11) is a principled time-dependent generalization of the NTK. The paper provides closed-form recursive expressions for its evaluation for ReLU and error-function nonlinearities (Sec. 3), enabling analytical tracking of learning dynamics beyond stationary kernels.

3. **Exact analytical mean-predictor dynamics via integral equations** — The theory yields deterministic integral equations for the mean predictor on training and test points (Eqs. 13‑14). These are not approximate; they are exact in the infinite-width limit under the MPL framework, and the paper shows one explicit comparison with finite-width Langevin simulations (Fig. 1c) that supports the theory.

4. **Characterization of two distinct learning phases and the role of hyperparameters** — The paper identifies gradient-driven and diffusive phases with time scales set by noise level \(T\), initialization \(\sigma_0^2\), and regularization \(\sigma^2\) (Sec. 4.3, Figs. 1‑3). The ratio \(\sigma_0^2/\sigma^2\) is shown to qualitatively change test-predictor dynamics, including non-monotonic behavior and optimal early stopping in the diffusive phase.

5. **Novel predictions about early stopping in the diffusive phase** — The theory demonstrates that optimal early stopping can occur *after* zero training error is achieved (Fig. 3), depending on depth and \(\sigma_0^2/\sigma^2\). This offers a new perspective beyond the usual gradient-driven early stopping and is a concrete, falsifiable prediction of the framework.

6. **Mechanistic insights into representational drift** — Section 5 uses the framework to model how hidden-layer weights drift while readout weights realign via the loss-gradient signal, and identifies drift-invariant features (e.g., input norms under ReLU) that can preserve classification accuracy after complete decorrelation. The analysis of the mean kernel \(K_\text{mean}^L\) (Eq. 19) provides a clean theoretical handle on when performance survives drift.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

1. **Experimental validation in the main text is limited.** The paper prominently advertises "remarkable agreement with computer simulations" (abstract/introduction), but the main text shows only one explicit theory-vs-simulation comparison — Fig. 1(c) on the synthetic orthogonal dataset. This plot is a visual overlay without error bars, without a quantitative discrepancy measure, and without a systematic convergence study across increasing network widths. The benchmark dataset figures (MNIST, CIFAR-10) appear to show theory predictions alone, without simulation overlays. Additional comparisons are deferred to the SI. For a paper making strong quantitative claims about the "complete trajectory" of learning dynamics, the experimental substantiation is thinner than one would hope, and the reader cannot assess how well the theory holds on real data. This does not threaten the core theoretical contribution (which stands or falls on its mathematical derivation), but it does weaken the paper's claim that the theory is empirically validated.

2. **The representational drift analysis (Section 5) is not tightly integrated with the core framework.** The frozen-readout scenario is introduced without an explicit derivation from the MPL dynamics in the main text — the derivation is entirely deferred to the SI. The main text presents the results (Eqs. 17‑19) without showing how they follow from the same replicated-field formalism. Furthermore, the classification accuracy is evaluated via a separately trained linear classifier on the predictors (line 547‑548), which is a post-processing step not derived from the theory. While the drift analysis is interesting in its own right, it reads as a separate application grafted onto the paper rather than a natural consequence of the unified framework. This reduces internal coherence.

3. **Some experimental hyperparameters are underspecified.** The paper states "we fix the scalar factor \(\sigma_0^2/\sigma^2\) as a constant as we vary \(\sigma_0^2, \sigma^2\) and \(T\) respectively" and notes "\(\sigma_0^2, \sigma^2 \sim \mathcal{O}(1)\)," but does not state the actual numerical values used. Similarly, the finite network widths used in Langevin simulations are not given in the main text. While these details may reside in the SI, their absence from the main text makes it difficult for a reader to assess the figures or reproduce the results without consulting supplementary material.

4. **The novelty framing slightly overstates the gap being filled.** The introduction and discussion claim "first theoretical understanding of the complete trajectory" and describe NTK and NNGP as "disparate" frameworks whose "relation has remained elusive." While the paper's specific contribution — the explicit NDK, the integral equations, and the analytical characterization of the diffusive phase — is genuinely novel, the general idea that gradient flow with weight decay interpolates between min-norm (NTK-like) and ridge-regression (NNGP-like) solutions has been discussed in the implicit bias and kernel regression literature. The paper would benefit from more carefully articulating what is genuinely new (the dynamical kernel, the diffusive-phase analysis, the closed-form integral equations) rather than claiming to close a completely open gap.

### Trivial
None.

## Nice-to-Haves

- **Error bars and width-convergence studies:** Adding error bars over multiple random seeds and showing convergence of finite-width simulations to the infinite-width prediction as width increases (e.g., widths 128, 512, 2048) would substantially strengthen the empirical case without changing the theory.
- **Sharper positioning vs. DMFT:** The paper compares to DMFT (Bordelon et al., Mignacco et al.) in the Discussion but does not explain in the main text what new phenomena the MPL framework captures that DMFT cannot. Since DMFT is a prominent alternative for analyzing noisy gradient dynamics in wide networks, a more detailed comparison would help readers assess the contribution.
- **Computational cost of solving the integral equations:** The two-time kernels scale as \(P \times P\) over time. A brief note on the computational cost and any discretization/approximation used would aid reproducibility and set expectations for practitioners.

## Removed Points

These points were flagged by a reviewer but are removed (or moved here) with justification:

- **"The paper does not state the form of the noise in the equivalent Langevin equation"** — This is factually incorrect. The paper explicitly states the noise covariance in Eq. 5 (line 164): \(\langle \eta(t)\eta(t')^\top \rangle = 2IT\delta(t-t')\). Removed.
- **"The paper does not clarify what 'large λ' means relative to other parameters"** — The paper states that in the large λ limit, weight updates become infinitesimal and discrete time maps to continuous time as \(t = \text{discrete time} / \lambda\). This is the standard presentation of a continuous-time limit and is sufficiently clear. Removed.
- **"The NDK does not reduce to the NNGP kernel; the long-time equilibrium predictor involves the NNGP kernel"** — The paper does not claim the NDK "reduces to" the NNGP kernel directly. It says "the NNGP kernel can also be evaluated from the NDK (see Sec. 4.2)," and Eq. 15 shows that the time-integral of the NDK yields the NNGP kernel. The critic mischaracterizes the paper's claim. Removed.
- **"The derivation of the MGF is given without explanation of the replica method"** — The paper briefly explains the replica method (lines 89‑95) and cites standard references. For a theoretical paper with SI, this level of explanation is appropriate. Removed.
- **"The claim about extending to discrete dynamics is over-optimistic"** — The paper explicitly frames this as future work ("These possibilities are being explored as part of our ongoing research"), not as a demonstrated result. Removed.
- **"Systematic numerical validation on benchmark datasets" (Strength Finder claim)** — This strength conflicts with the verified weakness that experimental validation is limited (only one explicit comparison in the main text). Dropped per conflict rule.
- **"Generality of MPL framework beyond DMFT" (Strength Finder claim)** — The paper claims potential generality but does not demonstrate it. The statement is about future work, not a validated strength. Dropped.

## Novel Insights

Two observations from the review process stand out beyond the paper's own contributions. First, the structural tension between the representational drift section and the core theory is worth the authors' attention as a deeper issue: the drift analysis introduces a *disjoint* dynamical scenario (readout frozen, hidden weights still diffusing) that breaks the joint Langevin dynamics the MPL framework was designed to analyze. The paper does not explain why the same prior statistics (Eqs. 7‑8) should still apply when only a subset of weights evolve, which is a genuine gap in the theoretical chain — not merely a presentation issue. Second, the paper's most underappreciated contribution may be the explicit two-time kernel recursion (Eq. 9), which shows that the NDK at depth \(L\) can be computed from the NDK at depth \(L-1\) via a layerwise recursion that depends only on the two-time statistics \(m(t,t')\). This recursive structure is algorithmically valuable and could be the basis for efficient numerical schemes, but the paper does not emphasize its practical implications.

## Suggestions

1. Add at least one quantitative theory-vs-simulation comparison on a real benchmark dataset (e.g., MNIST) in the main text, with error bars over random seeds and a brief convergence check across two or three widths. This would address the most serious empirical concern without requiring a lengthy empirical section.

2. Restructure Section 5 to either (a) derive the frozen-readout scenario as a controlled limit of the full MPL dynamics (e.g., taking the readout learning rate to zero at \(t_0\)) and show how the result follows from the same replicated-field path integral, or (b) clearly delineate it as an independent extension with its own assumptions and refer the reader to the SI for the full derivation. The current middle ground is unsatisfying.

3. Tone down the "first" and "closes the gap" language in favor of more precise claims about what is new (the NDK, the explicit characterization of the diffusive phase, the integral equations). The paper's genuine contribution is strong enough to stand on its own without rhetorical inflation.

4. Include a brief table in the main text (or reference an SI table) with the key hyperparameter values used in simulations: network widths, number of training points, values of \(T\), \(\sigma^2\), \(\sigma_0^2\), and the discretization/time-stepping scheme for solving Eqs. 13‑14.

## Score and Decision

This paper makes a genuine theoretical contribution. The derivation of the NDK, the unification of NTK and NNGP as two regimes of a single Langevin dynamics, and the closed-form integral equations for the mean predictor are substantive and well-grounded. The weaknesses identified — limited experimental validation, the structural looseness of the drift analysis, underspecified hyperparameters, and slightly inflated novelty claims — are all addressable and do not threaten the core theoretical contribution. The paper is clearly above the acceptance threshold for a theoretical venue.

MY FINAL SCORE: <pineapple>7.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>