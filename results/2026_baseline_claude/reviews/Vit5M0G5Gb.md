## Summary

This paper presents a theoretical framework explaining simplicity bias through saddle-to-saddle dynamics for a general class of neural networks, encompassing fully-connected (linear and ReLU), convolutional, quadratic, and linear self-attention architectures. The core contributions are threefold: (1) a recursive embedding theorem showing that fixed points of narrow networks become saddle points in wider networks; (2) a characterization of invariant manifolds that constrain networks to behave as effectively narrower; and (3) an analysis of two distinct timescale-separation mechanisms — one data-induced (between directions, for linear activations) and one initialization-induced (between units, for quadratic activations) — that drive trajectories near these manifolds and produce stage-like learning.

---

## Strengths

- **Novel unifying framework with rigorous theorems.** Theorem 1 extends the fixed-point constructions of Fukumizu & Amari (2000) with two new categories (Equations 6 and 7) that are provably essential: the saddles *actually visited* during learning fall into these new categories, not the original two. Theorem 3 on invariant manifolds and Theorem 4 / Proposition 5 on timescale separation are formally proven and form a coherent theoretical ladder from landscape geometry to dynamics.

- **Principled disentanglement of two mechanisms.** The identification of data-induced saddle-to-saddle dynamics (leading to low-rank weights) versus initialization-induced dynamics (leading to sparse weights) is a conceptually clean and novel distinction. Prior work had treated these as part of a single undifferentiated phenomenon; the paper's architecture-specific predictions let this distinction be verified empirically (e.g., Figure 2A: width scaling affects linear self-attention but not linear networks).

- **Testable and validated predictions.** The framework generates specific, non-trivial predictions: (a) increasing network width shortens plateaus in linear self-attention but not in linear networks; (b) equalizing singular values of Σ_yz eliminates plateaus in linear networks but not in self-attention; (c) large low-rank initialization produces saddle-to-saddle dynamics without an initial plateau — a regime the authors report as previously unobserved. All predictions are validated in Figure 2.

- **Breadth across architectures.** Covering fully-connected linear, fully-connected ReLU, convolutional linear, convolutional ReLU, quadratic, and linear self-attention models within a single framework is a substantial organizational achievement. The unifying Equation (1) is cleanly motivated, and the self-attention case (Equation 2) is carefully accommodated.

- **Practical insight about scaling.** The paper derives a principled reason why scaling up attention heads accelerates learning while scaling up linear network width does not — an interesting theoretical result relevant to understanding transformer design.

---

## Weaknesses

### Fatal
None.

### Major

- **Dynamics analysis is restricted to two-layer networks with polynomial activations.** Theorems 1 and 3 apply to general deep networks, but the rigorous timescale-separation analysis (Sections 5.1 and 5.2) is confined to two-layer linear and quadratic networks. For ReLU networks (prominent in Figure 1D–E and the abstract), the paper demonstrates saddle-to-saddle dynamics empirically and argues via Taylor expansion near zero that early dynamics is approximately linear, but does not provide a theorem on invariant manifold trapping or timescale separation for ReLU. The claim that "ReLU networks learn solutions with an increasing number of kinks" is illustrated rather than rigorously proven, which weakens the stated universality.

- **Deep network dynamics is only conjectured.** Section 7 explicitly notes that the dynamics analysis does not extend to deep networks and provides only a conjecture (that the order of the activation in u continues to predict timescale separation type). Given that the abstract and introduction foreground a "universal mechanism across architectures," the restriction to two-layer networks for the core dynamics result is a meaningful gap between claim and theory.

### Minor

- **Proposition 5 requires asymmetric eigenvalue structure (Σ_yZ must have both positive and negative eigenvalues).** This condition is non-generic for some regression tasks and the paper does not fully characterize what happens outside this regime. The sensitivity of the initialization-induced timescale separation to this spectral condition deserves more discussion.

- **The "almost surely" qualification in Theorem 4 and Proposition 5 is important but not fully unpacked in the main text.** Both results hold with Gaussian initialization in the limit of small ε, but the approximation quality as ε increases is only addressed narratively in Figure 2D, not analytically.

### Trivial
None worth listing.

---

## Nice-to-Haves

- A quantitative characterization of how closely the gradient flow trajectory must approach an invariant manifold for the simplicity narrative to hold would sharpen the framework.
- A brief comparison of the new fixed-point constructions (Equations 6–7) to the ReLU-specific results in Boursier et al. (2022) or Wang & Ma (2023) would help readers understand how the new constructions relate to and extend prior architecture-specific work.

---

## Novel Insights

The most genuinely novel insight of this paper is the systematic disentanglement of two qualitatively distinct mechanisms for saddle-to-saddle dynamics: a data-induced mechanism (timescale separation between data directions arising from the singular value spectrum of Σ_yz) and an initialization-induced mechanism (timescale separation between units arising from the quadratic / higher-order nature of the activation in the weights). This distinction explains, from first principles, why the same phenomenon manifests differently across architectures — as low-rank weight growth in linear networks versus sparse unit recruitment in self-attention — and makes architecture-specific predictions about width scaling and data distribution effects that would otherwise appear unrelated. The observation that large low-rank initialization produces saddle-to-saddle dynamics without an initial plateau (Figure 2C), and that this regime has not been previously documented, is a concrete new empirical finding enabled by the theory. These contributions go beyond summarizing prior architecture-specific results and provide a mechanistic basis for comparing inductive biases across architectures.

---

## Suggestions

- Provide at least a sketch of a rigorous argument for why ReLU networks exhibit invariant manifold confinement during the saddle escape, or clearly delineate this as a conjecture in the main text.
- Extend Figure 2B to show the case where Σ_yZ has only positive eigenvalues for self-attention, which would test whether the plateau elimination prediction still holds when the symmetry assumption of Proposition 5 is violated.
- Consider an experiment on deep (≥3 layer) ReLU networks in the main text to demonstrate which layer recruits additional units at each transition, since this is identified as an open question of significant interest.

---

## Score and Decision

The paper makes rigorous and novel theoretical contributions at the intersection of optimization dynamics and the geometry of neural network loss landscapes. The unified framework is technically sound where it is proven (two-layer linear and quadratic networks), the predictions are precise and validated, and the conceptual distinction between data-induced and initialization-induced dynamics is a meaningful advance. The main limitation — that the formal dynamics analysis does not extend to ReLU or deep networks — is significant but is honestly acknowledged, and the empirical demonstrations credibly suggest the theory captures the right structure. The paper is likely to be influential as a reference point for future theoretical work on training dynamics.

MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>