Now let me run the calibration search:Now I have enough information to write the final consolidated review.

---

## Summary

This paper introduces two complementary improvements to constructive hyperbolic tree embeddings. First, MS-DTE replaces the Hadamard-based hyperspherical point placement from Sala et al. (2018) with a PGD-based Maximal Hyperspherical Separation (MHS) objective that explicitly maximizes the minimum pairwise angle between child embeddings. Second, HypFPE reformulates the construction using floating-point expansion (FPE) arithmetic, enabling higher-precision computation using only standard GPU tensor operations, unlike arbitrary-precision libraries that are incompatible with accelerated hardware. Experiments on small synthetic trees and phylogenetic datasets show distortion improvements over prior constructive and optimization-based methods.

---

## Strengths

- **Novel MHS objective with clear empirical benefit.** The proposed Eq. (14) maximizes the minimum pairwise angle on the hypersphere rather than average pairwise energy, and Figure 1a demonstrates a consistent improvement in minimum pairwise angle over both the Hadamard and precomputed-points baselines across all point counts tested. Table 1 confirms this translates to lower distortion (D_ave, D_wc, MAP) in embedding a binary tree of depth 8.

- **HypFPE delivers dramatic precision improvements while maintaining GPU compatibility.** Figure 1b shows D_wc falling from >9.42 with float64 to ~1.1 using a 2-term FPE, a difference that would clearly affect downstream use. The framework is implemented in PyTorch using only standard tensor operations, making the GPU compatibility claim concrete and not merely aspirational.

- **Removal of Hadamard's dimensionality constraint is a genuine, practical advantage.** The Hadamard construction requires the embedding dimension to be a power of 2 and at least deg_max. MHS has no such constraint, enabling use in downstream tasks where dimension is set for task reasons (e.g., matching backbone feature dimensions). This is a real gain for practical applicability.

- **h-MDS failure mode is rigorously documented.** Figure 2 makes visually explicit that h-MDS collapses entire subtrees (white squares in the pairwise-distortion heatmap), making D_wc undefined/extremely large. This honestly motivates why D_ave alone is insufficient to evaluate embedding quality, which is a useful contribution to the field's evaluation methodology.

- **Theoretical grounding.** Theorem 1 bounds the MHS optimization cost at O(√N) via caching; Theorems 2 and 3 and Propositions 1 and 2 establish that FPE arithmetic linearly extends the effective radius of the Poincaré ball, providing a rigorous link between t-term FPE and the achievable distortion regime.

---

## Weaknesses

### Fatal
None.

### Major

- **No downstream evaluation despite pervasive deep learning framing.** The introduction dedicates two paragraphs to deep learning applications (action recognition, zero-shot learning, image segmentation, knowledge graph completion, etc.) and Sec. 2.2 surveys the deep learning literature at length. Yet every experiment measures standalone distortion (D_ave, D_wc, MAP) on small isolated trees. The central practical claim — that MS-DTE + HypFPE enables *better deep learning* via lower-distortion, GPU-compatible embeddings — is never tested. Given that distortion reductions on abstract metrics do not always translate to task gains in the embedding literature, and given that the paper explicitly frames its contribution as enabling deep learning pipelines, this is a material gap between the stated motivation and the provided evidence.

- **Experimental scale is limited to small trees; scalability is undemonstrated.** The m-ary tree experiments use depth ℓ=8 (at most a few hundred nodes), and the phylogenetic trees are similarly small. The paper never tests on large hierarchies (e.g., WordNet with ~80k nodes, ImageNet label tree, large ontologies) that are the natural use case for the deep learning applications discussed. The caching result (Theorem 1, O(√N) optimizations) is stated but never validated empirically. Computational runtime and distortion at scale are both uncharacterized, leaving the scalability claim theoretically motivated but empirically hollow.

- **No runtime or memory benchmarks for GPU compatibility claim.** "GPU compatible" is a primary contribution framing. However, FPE arithmetic requires significantly more floating-point operations per scalar — even the basic two-sum primitive doubles FLOP count, and nonlinear operations (tanh⁻¹, cosh⁻¹) require Taylor approximations. The paper provides no wall-clock timing or memory comparison between float64 and 2-term/3-term FPE variants, nor any comparison to CPU-based arbitrary-precision alternatives. Without this data it is impossible to assess whether the FPE overhead is acceptable in practice, particularly at the batch sizes used in deep learning.

### Minor

- **Optimization baselines are explicitly under-tuned, weakening the comparison.** Section 5.2 states: "This performance could be increased through hyperparameter tuning and longer training. However, the results will not come close to those of the other methods." The second sentence is asserted without evidence. Distortion Optimization (Yu et al., 2022b), which directly minimizes the distortion objective, would likely close the gap substantially under proper tuning and sufficient dimension, particularly on the small trees tested. The comparison's validity rests on an unverified claim.

- **FPE ablation conducted on a single tree.** Figure 1b, which motivates HypFPE, is derived from only the mosses phylogenetic tree (max path length ℓ=30). A single tree selected because it exposes the precision bottleneck acutely may not represent the range of tree structures where FPE gains are relevant or where they are negligible.

- **The error bound ε* in Theorem 2 is qualitative.** Theorem 2 guarantees an approximation error bounded by "some small ε* > 0" without an explicit expression in terms of t and b. This leaves the precision guarantee difficult to reason about quantitatively, though Figure 1b provides empirical grounding.

### Trivial

- MHS is non-smooth (the min operator in Eq. 14 has subgradient discontinuities at ties). The paper does not discuss subgradient behavior or sensitivity to initialization. Reporting variance across PGD random seeds in Table 1 would strengthen reliability claims.

---

## Nice-to-Haves

- Embedding a standard benchmark hierarchy (e.g., WordNet mammals or ImageNet label tree) with MS-DTE + HypFPE and evaluating in a hierarchical classification downstream task would directly validate the paper's primary motivation.
- A table comparing actual runtime (CPU vs. GPU) for float64 vs. FPE variants would make the GPU compatibility story empirically complete.
- Showing explicitly, for a given tree, the τ required by Hadamard/precomputed vs. MHS to achieve similar distortion would make the "smaller τ → fewer bits" argument quantitative rather than qualitative.
- Testing FPE on 2–3 trees with different depth-to-branching-factor ratios would make the precision ablation more general.

---

## Removed Points

*These points are flagged to be removed, treat them with caution.*

- **[Harsh Critic — Tammes problem literature]** The critic notes the MHS objective is a variant of the Tammes problem and criticizes the lack of citation to that literature and discussion of the Tammes problem solvers. This is scope creep: the paper does not claim to solve Tammes optimally, only to improve on prior heuristics, which Figure 1a confirms. Removed.

- **[Harsh Critic — h-MDS as straw man for D_wc]** The critic argues h-MDS was not designed to minimize D_wc, so using it as a foil is unfair. However, the paper correctly shows that h-MDS collapses nodes, making D_wc undefined. The comparison is used to demonstrate why D_wc matters, not to attack a fairly-constructed baseline. Removed.

- **[Harsh Critic — τ=5 as "unchosen hyperparameter advantage"]** The paper uses τ=5 uniformly for constructive methods and h-MDS, which is a consistent setup, not an advantage for MS-DTE specifically. The τ ablation is a separate, valid minor issue about demonstrating the bit-reduction benefit, retained as a nice-to-have.

- **[Strength Finder — "theorems provide rigorous bounds"]** Theorem 1 is elementary (a number-theoretic bound on distinct degrees), and Theorems 2/3 use a qualitative ε* without explicit bound. The strength as stated is too strong; the theoretical grounding is supportive but limited. Softened to "theoretical grounding" with appropriate caveats in the main Strengths section.

- **[Strength Finder — the paper addresses an important problem, hyperbolic ML is promising]** Removed as generic/non-specific.

---

## Novel Insights

The paper's most genuinely novel observation, which the reviewers partially surface but do not fully articulate, is that the choice of *which* distributional objective to use for hyperspherical placement has asymmetric consequences for worst-case vs. average distortion. Hyperspherical energy objectives (Liu et al., 2018) minimize average pairwise repulsion, which tolerates a small minimum angle — but it is precisely that minimum angle that determines how closely two subtree roots are placed, creating local worst-case distortion. Targeting the minimum angle directly (MHS) re-aligns the optimization objective with the distortion metric that actually matters for downstream hierarchical tasks. This observation about objective misalignment has implications beyond hyperbolic embeddings, potentially relevant to any method that places prototypes on a hypersphere for hierarchical learning.

---

## Suggestions

1. Add a downstream experiment: use MS-DTE + HypFPE to embed a standard label hierarchy (ImageNet or WordNet), then measure hierarchical classification accuracy on a visual model that uses these as fixed prototypes. This directly validates the stated motivation with minimal additional implementation (the embedding framework is already built).
2. Add a runtime table: time float64 vs. 2-term FPE on a moderately sized tree in GPU batch mode; this makes the GPU-compatibility claim actionable.
3. Test on at least one large hierarchy (>10k nodes) and report wall-clock time alongside distortion. Theorem 1 predicts O(√N) optimizations; verify this empirically with a scaling plot.
4. Report standard deviation over multiple PGD initializations in Table 1 to characterize MHS robustness.
5. Explicitly report the τ used by each method (MS-DTE vs. Hadamard vs. precomputed) for a given target distortion, to quantify the bit-reduction benefit of better hyperspherical separation.

---

## Score and Decision

**Anchor comparison:**

| Path | Avg Human Score | Comparison to this paper |
|------|----------------|--------------------------|
| `zbKcFZ6Dbp.md` (Shadow Cones) | 6.33 (Accept) | Similar: new constructive hyperbolic hierarchy embedding with theoretical support; stronger: includes downstream experiments across multiple datasets |
| `ekz1hN5QNh.md` (Fully Hyperbolic CNN) | 6.00 (Accept) | Similar: new hyperbolic geometry tool for DL; stronger: downstream vision task evaluation |
| `83le3arfeA.md` (Balanced Hyperbolic Embeddings) | 5.50 (Reject) | Similar: hyperbolic embedding method; stronger: 13 downstream datasets; weaker: some methodological issues in comparison setup |
| `Iy0WQ0c75x.md` (Alignment/Isotropy Hyperbolic GCL) | 4.75 (Reject) | Similar: contribution to hyperbolic representation quality; weaker: no novel algorithmic framework |
| `KmdwGYbMv0.md` (Binary Hyperbolic Embeddings) | 4.50 (Reject) | Similar: technical improvement to hyperbolic precision/efficiency; comparable experimental scope; theory present but no downstream tasks |
| `feZ7RpTLRy.md` (Bridging ML/algorithms: hyperbolic comparison) | 4.25 (Reject) | Weaker: survey/comparison with no novel method |
| `tdbK3TGFl1.md` (Asymmetric Embedding for Hierarchical Retrieval) | 3.50 (Reject) | Partially similar problem; weaker method |
| `q6WtaLj8O1.md` (Fully Hyperbolic KG) | 3.00 (Reject) | Weaker: no novel theoretical contribution |
| `4wpqmhh05N.md` (Mutual Information in Hyperbolic Embedding) | 3.50 (Reject) | Weaker: generalization bounds without strong methodology |

**Calibration reasoning:**

The paper offers two genuine technical contributions with supporting theory and consistent distortion improvements. Compared to Shadow Cones (6.33, accepted), which similarly proposes a new constructive framework with theoretical support *and* tests on several datasets with downstream grounding, this paper lacks downstream evaluation and large-scale experiments—dropping it below acceptance threshold. Compared to Binary Hyperbolic Embeddings (4.50, rejected), this paper has stronger theory, clearer practical motivation (GPU compatibility), and better-designed ablations, placing it above that mark. The absence of downstream evaluation and runtime benchmarks despite heavy DL framing, combined with small-scale-only experiments, aligns this paper with the 5.0 boundary—technically sound and incremental, but with an evidence base insufficient to support its stated framing.

**Originality:** Moderate. Both contributions are refinements of existing frameworks (Sarkar/Sala constructive method; Joldes/Popescu FPE routines), but the specific combination and application to hyperbolic tree embeddings is new.

**Importance of research question:** Moderate-high. GPU-compatible, low-distortion hyperbolic embeddings are genuinely useful infrastructure. The question is well-posed.

**Support for claims:** Weak-moderate. Distortion improvements are well-supported for the tested scales; GPU-compatibility is demonstrated structurally but not benchmarked; deep learning utility is unsupported.

**Soundness of experiments:** Fair. Experimental designs are internally consistent but limited in scope and scale.

**Clarity of writing:** Good. The method is clearly explained and the two contributions are well-separated.

**Value to research community:** Moderate. Would be higher with downstream validation. As written, useful infrastructure paper for the hyperbolic ML sub-community.

**Final Score: 5.0 — Borderline Reject**

MY FINAL SCORE: <pineapple>5.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>