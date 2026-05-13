## Summary
The paper presents two contributions for embedding trees in hyperbolic (Poincaré ball) space: (i) MS-DTE, which replaces the Hadamard/precomputed hyperspherical point sets in Sarkar/Sala's combinatorial construction with an optimization that maximizes the minimum pairwise angle on the sphere, and (ii) HypFPE, a PyTorch implementation of modern (Popescu-style) floating-point expansion arithmetic specialized for hyperbolic distance computation (cosh⁻¹ and tanh⁻¹). Experiments on m-ary and phylogenetic trees show lower distortion than optimization-based baselines and prior combinatorial constructions, especially when HypFPE supplies precision beyond float64.

## Strengths
- **Diagnosis of the Hadamard limitation is sharp and supported.** Sec. 3 correctly identifies that the inscribed-hypercube/Hadamard placement requires the dimension to be a power of two and ≥ deg_max, and that suboptimal placement directly inflates the required τ. Figure 1a quantifies this: MHS yields a larger minimum pairwise angle than both Hadamard and the Lovisolo–Da Silva precomputed set across point counts.
- **Empirical link from "better separation → lower distortion" is concretely demonstrated.** Table 1 shows MS-DTE reduces D_ave from 0.152 (precomputed) / 0.078 (Hadamard) to 0.044 and D_wc from 2.06/1.80 to 1.67 on a binary depth-8 tree at matched τ.
- **HypFPE materially extends usable precision on GPU.** Figure 1b shows that float64 (53 bits) yields D_wc ≈ 9.42 on the moss phylogeny, whereas 2-term float64 FPE (~100 bits) pushes D_wc near 1, and Table 3 shows MS-DTE+HypFPE is the strongest combination across four phylogenetic trees.
- **Caching argument is practically useful.** Theorem 1's O(√N) bound on unique optimizations, exploiting that MHS depends only on the degree, addresses a natural scalability worry.
- **Dimension is unconstrained.** Unlike Hadamard, MS-DTE works at arbitrary n, which is what downstream applications actually need.

## Weaknesses

### Fatal
None. The methodological core (MHS + FPE) is sound and supported by the intrinsic experiments.

### Major
- **The "GPU-compatible hyperbolic deep learning" framing is not exercised by any experiment.** The introduction and conclusion repeatedly motivate the work as enabling hyperbolic tree embeddings "on top of neural networks" ("paving the way for highly accurate hyperbolic neural networks"), and Sec. 4 justifies HypFPE because arbitrary-precision arithmetic "renders the embeddings useless on GPUs in deep learning settings." Yet every experiment in Sec. 5 is an intrinsic distortion measurement on small static trees — no neural network, no downstream task (classification/retrieval/HKE), and no GPU wall-clock or memory comparison vs. an MPFR baseline. The contribution as evaluated is "lower-distortion tree embeddings"; the deep-learning pitch is currently unsupported.
- **No head-to-head comparison with the prior GPU FPE library (Yu & De Sa 2021; Yu et al. 2022a).** Sec. 2.2 explicitly identifies Yu et al.'s PyTorch FPE library as the closest prior work and motivates HypFPE by the fact that they use older Priest/Shewchuk routines whereas this work adopts Popescu (2017). The natural ablation — same tree, same precision budget, HypFPE vs. Yu et al.'s library, on distortion and GPU runtime — is missing. Figure 1b only contrasts HypFPE with single-format float32/float64. Without the FPE-vs-FPE comparison, the marginal contribution of HypFPE over the existing GPU FPE baseline is unestablished.
- **Title overclaims "distortion-free."** The construction yields a (1+ε) worst-case bound *conditional on* sufficient precision and ideal separation; reported D_wc values are always > 1 (e.g., 9.42 with float64 on mosses; non-unit MS-DTE+HypFPE numbers in Table 3). The accurate framing is "low-distortion." The body actually uses "low-distortion" — the title and abstract should match.

### Minor
- **"Maximally separated" is asserted but not proven.** Eq. 13 is non-smooth (min over neighbors) and non-convex; the authors solve it with 450 PGD steps at lr 0.01. Figure 1a shows MHS exceeds prior baselines on the minimal-angle criterion, but there is no comparison to known Tammes-problem optima or any optimality certificate. The name encodes a claim the method does not formally deliver; "near-maximal" or "minimum-angle-maximizing separation" would be more honest.
- **Theorem 2/3 leave ε\* unspecified.** Without a quantitative dependence of ε\* on t and b, a practitioner cannot pick t to hit a target distortion; the theorems become qualitative existence statements. Even a coarse rate (e.g., ε\* = O(2^{−t(b−1)})) in the main text would close this gap.
- **No variance/seed reporting on the non-convex MHS.** Tables 1–3 and Fig. 1a report point estimates. Since MHS is non-convex and solved by PGD, a small std over a handful of seeds (and over τ-perturbations) would strengthen the empirical claims with little cost.
- **Optimization baselines (PE, HEC, DO) are dismissed without a tuning sweep.** Sec. 5.2 states results "will not come close" even with tuning; for DO especially (the closest learning-based competitor) the chosen τ=1.0 and failure to converge on lichen warrant a brief sensitivity analysis rather than a verbal dismissal.
- **The tanh⁻¹ vs. cosh⁻¹ choice is justified by an asserted diagnosis.** Sec. 4.2 says tanh⁻¹ "leads to larger numerical errors … likely due to catastrophic cancellation in the dot product." A small measurement (e.g., relative error vs. MPFR ground truth on a sweep of distances near the boundary) would substantiate the choice.

### Trivial
- "Proposition 1. The range of the inverse hyperbolic *tangent* formulation…" sits inside Sec. 4.1 about cosh⁻¹; this looks like a stale label and should be checked.
- Theorem 1's O(√N) bound is a clean counting argument but probably does not need full theorem status.

## Nice-to-Haves
- At least one end-to-end downstream demonstration (e.g., hierarchical image classification with hyperbolic prototypes, or HKE completion) to support the deep-learning motivation.
- A GPU runtime/memory scaling plot of HypFPE vs. t (and vs. N) — directly relevant to the "GPU-compatible" pitch.
- A practitioner-facing guide: given a target D_wc and tree (ℓ, deg_max), how to pick t and τ.

## Removed Points
*These points are flagged to be removed; treat them with caution.*

- **"Missing related works."** Per rules, not evaluable without external sources.
- **"Empty `Proof.` bodies in Sec. 4."** Proofs are deferred to the appendix, which the parser strips; not an author error.
- **"Four phylogenetic trees, no held-out splits."** Held-out splits do not apply to intrinsic distortion evaluation of a single tree; this is scope creep for the stated setting.
- **"Per-optimization cost in n for large deg_max not analyzed."** Borderline; addressed informally in Sec. 3 ("can generally be performed in mere seconds") and not central to the contribution.

## Novel Insights
None beyond the paper's own contributions. The key observation that *mean* hyperspherical energies admit small minimum angles — and that this minimum angle is what determines the distortion bound in Sarkar's construction — is a useful and concrete diagnosis, but it is the paper's own contribution rather than an external synthesis.

## Suggestions
- Rename to drop "distortion-free"; the body already uses "low-distortion." Align the abstract/conclusion with what is shown.
- Add an FPE-vs-FPE comparison against Yu et al. (2022a)'s GPU library at matched precision, on both distortion and wall-clock GPU time. This is the right ablation for the HypFPE contribution.
- Either (a) include one downstream deep-learning experiment, or (b) re-scope the contribution as a fast, high-precision tree-embedding tool and trim the "hyperbolic neural networks" framing accordingly.
- Add seed-variance bars for MS-DTE and for the MHS minimum angle plot.
- Make ε\* in Theorems 2/3 quantitative (or restate as a rate in t,b) and either prove an optimality property for MHS or rename "maximally" → "minimum-angle-maximizing."

---

**Axis-by-axis assessment.** *Originality:* moderate — Sarkar/Sala's construction with an explicit min-angle MHS step, plus a Popescu-style FPE port; both are incremental but well-motivated. *Importance:* genuine for the tree-embedding subcommunity; the deep-learning importance is asserted not demonstrated. *Claim support:* the intrinsic-distortion claims are supported; the "GPU-compatible hyperbolic deep learning" and "distortion-free" claims are not. *Soundness of experiments:* reasonable on the intrinsic side but lacking variance and the obvious FPE baseline. *Clarity:* good; the diagnosis sections are well-written. *Value to the community:* solid as a tree-embedding tool; modest as a deep-learning enabler given current evidence.

MY FINAL SCORE: <pineapple>5.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>