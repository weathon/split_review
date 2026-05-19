- Decision: Accept
- Avg Score: 8.00
- Scores: 8, 8, 8
Now I have all the information I need. Let me produce the final consolidated review.

## Summary

This paper studies the expressivity of Higher-Order Message-Passing (HOMP) on combinatorial complexes, identifies limitations via a topological covering criterion, and proposes two new model families — multi-cellular networks (MCN) and scalable multi-cellular networks (SMCN). Key contributions include: (1) a covering-based indistinguishability criterion for HOMP, (2) examples where HOMP cannot detect diameter, orientability, planarity, or homology, (3) a comparison showing HOMP can outperform hypergraph networks, (4) the MCN architecture with a claimed full-expressivity result, (5) the SMCN architecture with theoretical guarantees for specific invariants, and (6) a synthetic Torus benchmark. The paper is well-structured and tackles an important question.

## Strengths

1. **Sound construction of diameter and orientability/planarity counterexamples.** Propositions 4.2 and 4.3 provide concrete HOMP-indistinguishable CC pairs that provably differ in diameter (two tori with different cycle lengths but equal total cell counts) and orientability (cylinder vs. Möbius strip). The covering arguments for these cases are valid because both CCs in each pair are connected, so Theorem 1 applies cleanly. These examples establish a genuine limitation of HOMP.

2. **SMCN architecture with well-motivated design and theoretical guarantees for specific invariants.** The paper constructs SMCN by adapting expressive graph architectures (PPGN, subgraph GNNs) to combinatorial complexes via augmented Hasse graphs. Propositions 7.1–7.4 provide explicit proof sketches that SMCN can compute diameter, distinguish Möbius strips from cylinders, compute zeroth homology, and separate 2D manifolds by homology — all with complexity analysis. These proofs do not depend on the problematic covering theorem.

3. **Proven advantage of HOMP over hypergraph networks.** Proposition 4.7 exhibits a pair of CCs with cell features that HOMP (using both adjacency and incidence neighborhoods) can distinguish while the expressive EHNN cannot. The construction is concrete and the reasoning is sound, providing a clear expressivity benefit of HOMP over hypergraph models that had not been explicitly demonstrated.

4. **Empirical validation on a novel synthetic benchmark.** The Torus dataset (223 pairs) is the first synthetic benchmark specifically designed to measure TDL expressivity. The results — SMCN distinguishes all 223 pairs while HOMP distinguishes 0 — cleanly validate SMCN's practical expressivity advantage. Even though the theoretical foundation for some pairs in the dataset is weakened by the covering theorem gap (see Weaknesses), the empirical finding that SMCN universally outperforms HOMP on this controlled benchmark is still informative.

5. **Multi-cellular cochain space framework.** The formalization of \(\mathcal{C}^{\mathbf{k}}\) spaces (Section 5.1) unifies cell features, adjacency/incidence matrices, and higher-order tensors under a single notation, enabling principled use of equivariant linear layers and borrowing of expressive graph architectures for TDL. This provides a clean foundation for future work.

## Weaknesses

### Fatal
None.

### Major

1. **The covering criterion proof (Theorem 4.1) does not adequately handle the mixed connected/disconnected case.** The proof sketch (lines 271–283) explicitly states it covers "the case where both C and C\* are connected" and relies on the connectedness to establish uniform fiber size (\(|\rho^{-1}(x)| = |\tilde{S}|/|S|\)). The homology example (Proposition 4.4) involves a connected torus vs. two disconnected tori, and the lifting/pooling example (Proposition 4.5) involves a connected CC vs. a disconnected union of two components. The theorem's condition only requires a common covering space for each *connected component* individually, but the counting argument used to equate the multisets does not cleanly extend when the target CCs differ in connectivity structure and the fiber sizes differ across components. The paper asserts the conclusion but does not resolve this technical gap. This means two of the paper's three categories of HOMP limitations (homology-based invariants; lifting/pooling) are not fully substantiated by the provided proof. The diameter and orientability examples are unaffected because both CCs in each pair are connected. *(Verification: Theorem 1 statement at lines 255–270; proof sketch at lines 271–283; homology proof at lines 576–586; lifting proof at lines 617–619.)*

2. **The full expressivity claim for MCN (Proposition 6.1) is unsubstantiated.** The paper provides no proof, proof sketch, or even an outline of an argument. It states only "Similarly to \(k\)-IGNs, by using large enough multi-cellular cochain spaces MCN can be fully expressive." For graphs, the analogous result requires tensors of order at least the number of nodes (impractical), and generalizing to CCs with multiple cell types and ranks is non-trivial. Neither the required tensor order nor any construction is specified. This claim should be downgraded to a conjecture or removed. *(Verification: Proposition 6.1 at lines 891–894; surrounding text at lines 888–896 contains no proof.)*

### Minor

3. **The Torus dataset's theoretical grounding is tied to the problematic covering argument.** The dataset description states each pair is "provably indistinguishable by HOMP" based on Theorem 4.1. Since the theorem's proof has a gap for mixed connected/disconnected pairs, and the dataset includes such pairs (differing in number of connected components), this characterization is only conditionally correct. The empirical result (HOMP fails on all 223 pairs, SMCN succeeds on all 223) still demonstrates SMCN's practical superiority, but the experiment does not *cleanly* validate the theoretical analysis for the homology-affected pairs. *(Verification: dataset description at lines 1374–1376.)*

### Trivial
None.

## Nice-to-Haves

- An ablation study on the Torus dataset comparing SMCN variants without PPCN or without SCN would clarify which architectural components drive the distinguishing power.
- A more detailed computational complexity comparison between HOMP and SMCN for representative CC sizes would help assess practical applicability.
- The paper correctly acknowledges that comparing HOMP to hypergraph networks is incomplete; characterizing the full relationship (including cases where EHNN outperforms HOMP) would strengthen the analysis but is understandably left for future work.

## Removed Points

*These are weaknesses or strengths from the inputs that were removed or demoted, with justification.*

- **Harsh critic: "The Torus dataset includes pairs that may not be provably indistinguishable" as a separate weakness.** → Merged into Minor Weakness #3 above; not a standalone point since the dataset remains useful for empirical comparison even if the theoretical basis for some pairs is conditional.
- **Harsh critic: runtime claims not formally proven, missing complexity table.** → Demoted to Nice-to-Have. The paper states asymptotic complexities for individual components; a full comparison table would be a useful addition but not a core flaw.
- **Harsh critic: "missing appendix, missing proofs in appendix, absent references" and formatting/style nitpicks about presentation.** → Removed per instructions (parser strips appendices; formatting artifacts are parser errors).
- **Strength finder: "Full expressivity of MCN" as a strength.** → Removed. The claim is stated but entirely unsupported. A claim without evidence cannot be a strength.
- **Strength finder: "Augmented Hasse graphs as a bridge to graph architectures."** → Partially retained (folded into Strength #2). The original phrasing was somewhat generic.
- **Strength finder: "Construction of a synthetic benchmark for TDL expressivity."** → Folded into Strength #4. The Torus dataset is a genuine contribution but the strength as originally written was somewhat overstated given the theoretical grounding gap.
- **Strength finder: "Multi-cellular cochain space framework" as a standalone strength.** → Folded into Strength #5. Retained but merged with a similar point.
- **Harsh critic: "the orientability/planarity example is sound"** → Not listed as a separate strength but is subsumed under Strength #1.

## Novel Insights

None beyond the paper's own contributions. The two major reviewers' perspectives converge on the key gap in the covering theorem proof, which neither reviewer fully formalized but both flagged as a concern. The observation that the proof sketch's connected-case limitation is what creates the gap — and that the diameter/orientability examples avoid it — is a synthesis that clarifies the precise scope of what the paper establishes versus what remains conjectural.

## Suggestions

1. **Fix the covering theorem proof** to handle the mixed connected/disconnected case. This can be approached either by (a) providing a careful counting argument that accounts for differing fiber sizes across components, (b) restricting the claimed examples to connected CCs only (the diameter and orientability examples are sufficient to establish that HOMP fails on basic topological invariants), or (c) using a different theoretical tool for the homology and lifting examples.
2. **Remove or substantiate the full expressivity claim for MCN** (Proposition 6.1). If the claim is kept, provide at minimum a proof sketch showing how high-order multi-cellular cochain spaces can simulate a WL-type coloring for CCs, including the required tensor orders.
3. **Clarify in the Torus dataset description** which pairs are provably indistinguishable (those where both CCs are connected) and which are empirically indistinguishable but theoretically unresolved. This would transparently communicate the current limitations to readers.
