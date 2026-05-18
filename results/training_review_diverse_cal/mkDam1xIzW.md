Now I have a thorough understanding of the paper. Let me produce the final consolidated review.

---

## Summary

This paper introduces Probabilistic Geometric Principal Component Analysis (PGPCA), a generalization of Probabilistic PCA (PPCA) designed for data distributed around a nonlinear manifold. The key idea is to augment PPCA's generative model by replacing the mean with a manifold function φ(z) and incorporating a distribution coordinate system K(z) — either Euclidean (EuCOV) or geometric (GeCOV) — to capture deviations from the manifold. The paper derives a tractable EM algorithm with closed-form M-step updates for the loading matrix C and noise variance σ², and shows that PGPCA can simultaneously perform dimensionality reduction, learn the distribution on the manifold, and test between alternative coordinate systems. Experiments on simulated loops/tori and on real mouse head-direction neural data demonstrate that PGPCA with the correct coordinate system yields higher log-likelihood than PPCA.

## Strengths

- **Principled generalization of PPCA to nonlinear manifolds with a tractable EM algorithm.** The paper defines a generative model (Eq. 1) that decomposes each observation into a manifold component, a deviation term captured by a distribution-coordinate-dependent loading matrix, and isotropic noise. It derives an ELBO (Eq. 5), discretizes the latent state distribution via landmarks (Eq. 9), and obtains closed-form M-step updates for C and σ² (Eqs. 14-15) that mirror the PPCA solution — a non-trivial extension given the nonlinear geometry. This preserves theoretical guarantees while incorporating any orthonormal coordinate system K(z).

- **Empirical validation showing PGPCA recovers the true model and outperforms PPCA.** In simulations (Figure 2A), PGPCA with the correct distribution coordinate visually recovers the true data distribution far better than PPCA. Quantitative log-likelihood comparisons (Figure 2B, Table 2) show that PGPCA with the correct coordinate achieves significantly higher log-likelihood than PPCA (paired t-test p<1.7×10⁻¹²), and the same superiority holds for loops embedded in ℝ¹⁰ (Figure 2D). This directly demonstrates that incorporating the nonlinear manifold improves modeling fidelity.

- **Demonstration of hypothesis testing between coordinate systems and dimensionality reduction.** PGPCA can distinguish between EuCOV and GeCOV coordinates by comparing trial-average log-likelihood (Figures 2B, 2D, 4B, 4D), and this holds across model dimensions m (Figure 2C). This establishes PGPCA as a tool for both coordinate selection and dimensionality reduction simultaneously.

- **Joint learning of the manifold-state distribution p(z).** The EM algorithm learns the discretized weights ωⱼ (Eq. 11) alongside C and σ². In Section 4.3 and Figure 3, PGPCA recovers the true data distribution whether p(z) is given or learned, and the log-likelihood advantage for the correct coordinate persists — showing PGPCA captures both the distribution around and on the manifold.

- **Application to real neural data demonstrates practical utility.** On head-direction firing rates from mice (Figures 4A, 4C), the data clearly lie around a loop manifold. PGPCA (GeCOV) consistently yields higher log-likelihood than PGPCA (EuCOV) and PPCA across all tested dimensions (Figures 4B, 4D), demonstrating practical value for neuroscience datasets where data deviate from a nonlinear manifold.

## Weaknesses

### Fatal

None.

### Major

- **Unacknowledged topological restriction: the method requires a global orthonormal frame, which limits applicability to parallelizable manifolds.** The model (Eq. 1) defines K(z) as an n×n orthonormal matrix for every z on the manifold (Section 3.1). This means the manifold must admit a global orthonormal frame field — a strong topological condition equivalent to requiring the manifold to be parallelizable. The paper tests on S¹ (loop) and T² (torus), both parallelizable, but the method would not be well-posed for a sphere (S²) or any non-parallelizable manifold, because no continuous global orthonormal frame exists. The paper presents PGPCA as a tool for "a given nonlinear manifold" (abstract, Section 1) without qualifying this restriction. The entire EM derivation (notably the step that the determinant |Ψ(z)| becomes independent of z, enabling the PPCA-like closed form) depends on K(z) being square and orthonormal. This limitation is never acknowledged, and no alternative (e.g., local frames with transition functions, or explicitly restricting to parallelizable manifolds) is discussed. While the paper's experiments are on practically relevant parallelizable manifolds (loops for head direction, tori for hippocampus), the scope is narrower than advertised, and the paper should state this assumption clearly.

### Minor

- **Landmark selection and discretization of p(z) are underspecified.** The paper chooses M landmarks {z₁,…,z_M} and discretizes p(z) via Dirac deltas (Eq. 9), but never explains how these landmarks are placed on the manifold (uniform grid? random subset? dependent on data?). The number M and placement can affect both approximation quality and computational cost. Since the pseudo-code (Algorithm 1) was likely in the appendix (stripped by the parser), the main text should at least briefly state the strategy for landmark selection.

- **Manifold fitting uncertainty is ignored.** The manifold φ(z) is "first fitted from data" and then treated as known without error in PGPCA (Section 1, Section 3.2). In the real data analysis (Section 4.4), a 1D loop is fitted to neural firing rates in ℝ¹⁰; the quality of this fit directly influences the subsequent log-likelihood comparisons. The paper does not discuss how manifold fitting error propagates into the hypothesis test or whether conclusions are robust to this. (This is a common limitation of two-stage pipelines and is worth acknowledging.)

- **Real-data analysis shows only 2 of 6 mice individually.** The paper notes it recorded from six mice (Section 4.4) and Table 2 aggregates results, but Figures 4A-D show only two mice as examples. To fully support the biological claim that GeCOV better captures neural firing rates, individual results for all six mice (or a group-level statistic) would be more convincing.

- **General construction procedure for K(z) is not fully specified.** While the paper describes GeCOV qualitatively for loops and tori (Figure 1 caption), a concrete, general procedure for constructing K(z) for an arbitrary parallelizable manifold is missing. For example, one could Gram–Schmidt the tangent vectors from φ(z) to obtain an orthonormal basis and then complete the frame with normal directions. The paper should state this explicitly and discuss whether the choice of normal completion matters empirically.

### Trivial

- The paper uses "first fitted from data" and "first ftited from data" (line 15) — a minor typo/parser artifact.
- The pseudo-code for Algorithm 1 is referenced but not present in the extracted text (likely due to parser stripping); if it was omitted from the submission itself, the authors should ensure it is included.

## Nice-to-Haves

- A discussion of computational complexity (each EM iteration computes p(yᵢ|zⱼ) for all i,j and performs an eigenvalue decomposition of an n×n matrix) would help readers assess scalability.
- A sensitivity analysis on the number of landmarks M would strengthen the methodological presentation.
- While PPCA is the natural baseline (being the method being generalized), future work could also compare against methods that project deviations onto the tangent space and run PPCA there.

## Removed Points

These points were flagged by reviewers but are removed or downgraded per the review guidelines:

- **"Comparison set is too narrow (GP-LVM, VAE)"**: The paper explicitly discusses GP-LVM (Section 2) and explains that it treats latent states as parameters rather than random variables for categorization, serving a different purpose. The primary comparison against PPCA — the method being generalized — is appropriate and standard. The claim "PGPCA outperforms PPCA" is not trivial; it validates that incorporating the nonlinear manifold structure is beneficial.
- **"Paired t-test within a single mouse"**: The reviewer claimed a t-test is reported in Fig 4B/D "within a single mouse across dimensions." The paper reports t-tests only for simulations (Fig 2B/D), not for Fig 4. This criticism is factually incorrect.
- **"Missing pseudo-code / appendix details"**: Algorithm 1 is referenced in the paper; any missing detail is attributable to the parser stripping supplementary sections, per the review guidelines.
- **"Initialization and convergence criteria not discussed"**: These are standard implementation details of the type the guidelines classify as trivial/removable.
- **"Computational complexity not mentioned"**: A nice-to-have, not a weakness.
- **"Manifold fitting procedure for real data not summarized"**: The paper properly cites prior work (Chaudhuri et al., 2019) for the fitting procedure, which is standard practice.

## Novel Insights

None beyond the paper's own contributions. The reviews surface the parallelizability constraint as a significant unacknowledged limitation of the method's generality, which is a genuinely useful observation for the authors and for readers evaluating the method's applicability.

## Suggestions

1. **Explicitly acknowledge the parallelizability requirement.** State in Section 3.1 and Section 5 that K(z) being a global n×n orthonormal matrix requires the manifold to be parallelizable. Either restrict scope claims to parallelizable manifolds (loops, tori) or discuss possible extensions (e.g., local coordinate patches with transition functions).

2. **Provide a concrete general procedure for constructing K(z).** For a parallelizable manifold, describe how to obtain an orthonormal frame: compute the Jacobian of φ(z), Gram–Schmidt to get an orthonormal tangent basis, then complete the frame with orthonormal normal vectors (e.g., from the embedding space after projecting out the tangent space). Discuss whether the choice of normal completion affects the log-likelihood.

3. **Describe the landmark selection scheme** (uniform grid for low-dimensional l, or random sampling) and include a brief sensitivity analysis showing results are stable over a range of M values.

4. **Show individual results for all six mice** (or report a group-level statistic like a paired t-test across mice) in the real-data analysis to strengthen the biological claim that GeCOV outperforms EuCOV for head-direction data.

5. **Acknowledge the two-stage limitation** (manifold fitting precedes PGPCA) and briefly discuss how fitting error might propagate, even if a formal treatment is deferred to future work.

## Score and Decision

**Originality:** Good — extending PPCA to incorporate nonlinear manifolds with a coordinate-based deviation model is a novel contribution.

**Importance of research question:** High — many real-world datasets, especially neural population recordings, exhibit structure around nonlinear manifolds.

**Claims support:** Partially. The paper's claims are supported for the tested manifolds (S¹, T²), but the scope is overclaimed due to the unacknowledged parallelizability restriction.

**Soundness of experiments:** Adequate for a proof-of-concept. Simulations are clean; real-data analysis is limited in scope (2 of 6 mice shown individually).

**Clarity of writing:** Generally clear on the probabilistic model and EM derivation, but underspecified on implementation details (landmark selection, K(z) construction).

**Value to community:** Potentially useful for neuroscience applications where data lie around loops (head direction) or tori (hippocampus), but the topological restriction must be clearly communicated.

The paper presents a mathematically sound generalization of PPCA with a working EM algorithm, validated on practically relevant manifolds. The main weakness is the unacknowledged parallelizability requirement, which limits the method's generality but does not invalidate the results on the tested manifolds. A careful revision that honestly delimits the scope and provides missing implementation details would make this a solid contribution.

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>