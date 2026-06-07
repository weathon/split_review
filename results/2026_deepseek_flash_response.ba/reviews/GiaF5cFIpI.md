Now I have sufficient calibration data to finalize. Let me write the complete review.

## Summary
The paper proposes a streaming framework for adaptive stimulation of latent neural dynamics, integrating (i) streaming latent space construction via sjPCA, (ii) nonparametric kernel regression for learning stimulus-response mappings, (iii) constrained optimization to design high-dimensional stimulation patterns, and (iv) parallel evaluation of multiple latent representations. The method is demonstrated on synthetic data and real neural recordings (calcium imaging, electrophysiology) with synthetic AR(1) perturbations standing in for actual stimulation responses.

## Strengths
- **Nonparametric kernel regression demonstrably tracks non-stationary stimulus-response mappings**: Fig 2e provides quantitative evidence that the estimator recovers from a 180° flip in the ground-truth map within ~15s and continuously tracks a rotating map (1 revolution/30s), with 50-run error bars. The temporal kernel K₃ is the mechanism enabling this, and the contrast against a non-adaptive baseline is clear.
- **Constrained optimization reliably aligns stimuli with feasible latent directions**: Section 4.2 reports concrete counts — 517/600 optimizations achieve <1° misalignment for feasible targets, 508/600 for Q₀ — and the Designed stimuli substantially outperform Single/Multiple/Shuffled baselines on alignment angle (Fig 4a). These are directly measured quantities against well-defined alternatives.
- **End-to-end runtime is concretely benchmarked**: The paper measures <10ms average and <100ms maximum per timepoint on a specified hardware configuration (i9-12900K, 128GB RAM, NVIDIA 3060 Ti), providing a quantitative latency bound rather than a vague "real-time" claim.
- **Streaming sjPCA with Orthogonal Procrustes stabilization is a clearly described algorithmic addition**: Section 2.1 introduces the Procrustes step to stabilize jPCA planes across streaming updates, and Fig 1a shows convergence to the offline fit on a simulated circular system, addressing a real issue (subspace jitter) that would affect downstream control.

## Weaknesses

### Major
- **The optimization sparsity formulation (Eq 8) is unclear and likely does not do what the paper claims**: The objective includes the term λ₁(‖u‖₀^max − ‖u‖₁) with u ∈ [0,1]ᴺ. In a minimization, −‖u‖₁ rewards large ‖u‖₁, pushing uᵢ toward 1 — the opposite of a sparsity-inducing penalty. The paper states this "encourage[s] a solution with the number of non-zero elements close to n," but the regularizer constrains the L1 sum, not the L0 count. With u ∈ [0,1], having ‖u‖₁ ≈ n can be achieved by n entries at 1, but equally by 2n entries at 0.5. The mechanism does not match the description. The authors should clarify whether this is a sign error, an unconventional formulation requiring justification, or whether the regularizer works in practice through interaction with the cosine term — and provide evidence.

- **No experiment uses real stimulation responses**: All "real neural data" experiments (Section 3, Fig 3) add synthetic AR(1) perturbations to neural traces rather than using actual optogenetic or electrical stimulation responses. While the paper is transparent about this in the methods ("we simulated stimulations," line 178) and discussion ("performed offline," line 258), the abstract and framing imply more. Whether the method works when stimulation effects are nonlinear, network-mediated, and state-dependent (as in real biological tissue) is untested. This limits the strength of the evidence for the paper's central claim.

### Minor
- **The "blind" baseline comparison is too weak to be informative**: In Figs 2e and 3c, the primary comparison is against a model that simply ignores stimulations. The paper does include stronger baselines (random Single/Multiple/Shuffled in Fig 4, open-loop in Fig 5), but the central claims about the kernel regression estimator's superiority rely on the blind baseline. An ablation comparing the kernel regression estimator to a simple linear model of stimulation effects would be far more informative.

- **Parallel latent representation selection is claimed but never evaluated**: Section 2.2 and Fig 1c describe running sjPCA, proSVD, and mmICA in parallel with adaptive selection, but no experiment tests whether this switching improves stimulation performance over any fixed choice. This capability is described as a contribution but remains unsubstantiated.

- **The electrophysiological dataset yields no stimulation results**: The O'Doherty (2024) data is used only for latent space visualization in Fig 1b. The abstract's claim of demonstrating the approach on "intracortical electrophysiological recordings" is therefore technically true at the data level but misleading about the scope of validation.

- **Optimization solver details are missing**: Algorithm 1 states "Solve with box constraints" without specifying the optimizer (Adam? L-BFGS-B? projected gradient?), number of iterations, learning rate, or how λ₁ was chosen. Given the non-convex objective (cosine similarity + regularizer over [0,1]ᴺ with N up to 592), these details are needed for reproducibility.

### Trivial
- Fig 3c lacks error bars; only a single run appears to be shown for the calcium imaging experiment.

## Nice-to-Haves
- Testing on actual optogenetic stimulation data, or at minimum on more realistic nonlinear generative models of stimulation effects (beyond the AR(1) additive model).
- An ablation comparing the kernel regression estimator against linear alternatives on the same prediction task.
- Substantiating the parallel latent space selection claim with an experiment showing downstream stimulation improvement.

## Removed Points
These points were flagged by the reviewers but are removed after verification against the paper:
- "sjPCA is never compared against original jPCA" — REMOVED: Fig 1a explicitly shows sjPCA converging to the offline jPCA fit (black lines).
- "Blind is the only comparison" — REMOVED: the paper also compares against Single/Multiple/Shuffled (Fig 4) and open-loop (Fig 5).
- "No ablation of sjPCA contribution" — REMOVED: scope creep; the paper's core contribution is the full pipeline.
- Generic reproducibility complaints about missing appendix content — REMOVED per instructions.
- Formatting/style nitpicks — REMOVED per instructions.

## Novel Insights
None beyond the paper's own contributions.

## Suggestions
1. Fix or clarify the optimization formulation in Eq 8. If the regularizer is λ₁(n − ‖u‖₁), explain exactly why this encourages sparsity and provide empirical evidence showing the distribution of nonzero counts in the solutions.
2. Either add real stimulation data experiments or substantially strengthen the simulated stimulation scenarios — use nonlinear generative models, model mismatch tests, or published optogenetic response models.
3. Provide optimization solver details (algorithm, hyperparameters, convergence criteria).
4. Either remove the claim about adaptive latent space selection or add an experiment demonstrating its benefit.
5. Add error bars to Fig 3c.

## Calibration Anchors

**Round 1 — Bracketing:**
- Low band (avg < 3.5): e.g., BBldjKEBlJ (avg 3.0, Reject), NPzuN3Rxi8 (avg 3.0, Reject). These papers have severe methodological issues or very weak contributions. Our paper is clearly stronger.
- Middle band (3.5–7.5): FwW3jqchtY (avg 5.00, Reject), TVnkjz4MqV (avg 5.50, Reject), WQwV7Y8qwa (avg 5.80, Accept), 4ltiMYgJo9 (avg 5.75, Reject). Our paper is comparable to the 4.5–5.5 range.
- High band (avg > 7.5): cNmu0hZ4CL (avg 8.00, Accept), RWJX5F5I9g (avg 8.00, Accept). These are strong papers with rigorous validation. Our paper is well below this level.

**Round 2 — Narrowing (4.0–5.5):**
- FwW3jqchtY (avg 5.00, Reject): Has actual interventional data with real perturbations and identifiability theory. Our paper has more novel methodology but weaker evidence and no theory. Comparable, with our paper slightly weaker → 4.5–5.0.
- LNp7KW33Cg (avg 5.00, Reject): Strong empirical evaluation across datasets. Our paper is weaker empirically. → 4.5.
- eR1119aUlL (avg 4.25, Reject): Related streaming theme but less coherent. Our paper is stronger. → above 4.25.
- WQwV7Y8qwa (avg 5.80, Accept): Strong technical contribution with thorough validation. Our paper is clearly below this. → well below 5.8.

**Final bracket:** 4.25–5.0

The paper is closest to the 4.5–5.0 range. Compared to the 5.00 anchors (FwW3jqchtY, LNp7KW33Cg), our paper has a more novel framework but weaker empirical validation and an unresolved issue with the optimization formulation. Score: 4.5.

MY FINAL SCORE: <score>4.5</score>
MY FINAL DECISION: <decision>Reject</decision>