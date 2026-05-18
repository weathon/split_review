Now I have all the information I need. Let me compose the final consolidated review.

## Summary

This paper proposes higher-order pointwise distance distribution invariants (PDD^{h}) for periodic crystal structures. The key contributions are: (1) proving Lipschitz continuity of these invariants under atomic perturbations, (2) demonstrating that PDD{2} distinguishes all known homometric counter-examples that fooled earlier descriptors (PDD, PDF), (3) a complete solution to Problem 1.2 for 1D periodic sequences via the Pointwise Shift Distribution (PSD), (4) asymptotic analysis relating PDD^{h} columns to the point packing coefficient, (5) polynomial-time computability bounds, and (6) large-scale detection of thousands of near-duplicates across the five largest crystal databases (CSD, COD, ICSD, MP, GNoME) in under 8.5 hours on a desktop — a task that would take years with traditional alignment-based methods.

## Strengths

- **Lipschitz continuity under noise (Theorem 4.1)**: The paper proves that both PDD^{h} and PDM[l] change by at most 2ε when each point is perturbed up to ε. This formalizes the essential continuity condition that past cell-based descriptors violated, directly addressing the discontinuity problem shown in Fig. 1 where tiny atomic perturbations can arbitrarily scale a unit cell.

- **Distinguishes all known homometric counter-examples**: Example 3.6 (Fig. 4) shows PDD{2} and PDD{3} distinguish the infinite family of Pauling crystals P(±u) with EMD > 0, while past descriptors (PDF, PDD) gave identical values. Example 3.3 demonstrates the same for the 2D family from Pozdnyakov & Ceriotti. This is a concrete advance in discriminative power over prior invariants.

- **Ultra-fast detection of thousands of near-duplicates across five major databases**: Table 2 reports the first large-scale detection of near-duplicates across CSD, COD, ICSD, MP, and GNoME using PDA. Table 3 shows all comparisons completed in under 8.5 hours on a desktop, compared to extrapolated years for COMPACK (Table 4). This provides verifiable evidence of scalability and practical impact.

- **Asymptotic analysis guides parameter choice (Theorem 4.4)**: The theorem bounds PDD^{h} columns by the point packing coefficient, justifying why small k (here k=100) is most discriminative and motivating the deviation-from-asymptotic invariants (ADA, PDA). This prevents arbitrary cut-off choices.

- **Polynomial-time computability (Theorem 4.5)**: The complexity bound is polynomial in motif size m for fixed dimension and h, with N linear in k. This establishes feasibility for large databases, confirmed by the experiments.

- **Moment-based PDM[l] enables hierarchical filtering**: Definition 3.4 introduces fixed-size vectors (such as AMD) that maintain Lipschitz continuity and allow fast kd-tree nearest-neighbor search, reducing the need for expensive EMD comparisons in a multi-stage pipeline.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

- **The "all known counter-examples" claim could be more precisely scoped.** The paper repeatedly asserts that PDD{2} distinguishes "all known counter-examples to the completeness of past descriptors" (abstract, lines 55, 102, 194). The evidence shown covers the two infinite families (Fig. 2 family — which PDD itself already distinguishes; Fig. 3/Pozdnyakov & Ceriotti family; Pauling crystals), which are indeed the most prominent examples. However, the claim is stated as global without a systematic enumeration of what constitutes "all known" counter-examples. The paper would be stronger if it explicitly listed which homometric families from the literature had equal PDD and confirmed PDD{2} distinguishes each. As written, the reader cannot verify whether the claim covers all known cases or only the ones shown. The substance of the claim is likely correct given what is demonstrated, but the presentation overreaches slightly.

- **No proof sketch for the 1D completeness result (Theorem 4.3) in the main text.** Theorem 4.3 asserts that PSD solves Problem 1.2 (invariance, completeness, metric axioms, Lipschitz continuity, reconstructability, polynomial-time computability) for all 1D periodic sequences and finite sets in ℝ. The main text gives only Definition 4.2 (PSD) and then the theorem statement, with no sketch of how completeness or reconstructability is achieved. For a result described as "finally solved" after being "open even in dimension n=1," the absence of even a brief justification in the main text weakens the reader's ability to assess the claim. While full proofs belong in the appendix (which exists in the original submission), a one-paragraph sketch — e.g., explaining how shift-distance lists uniquely determine inter-point distances up to cyclic permutation and how continuity is maintained — would substantially improve the paper's credibility on this point.

- **The chemistry/geometry distinction in duplicate detection is not addressed.** The experiments flag near-duplicates using a purely geometric threshold (EMD < 0.01Å on PDA). The paper notes in passing that "chemical elements were replaced while keeping all coordinates fixed" (line 165, citing Anosova et al. 2024) and mentions "changing atomic types" (line 47), but does not break down how many of the thousands of flagged near-duplicates in Table 2 are genuine duplicates (same chemistry + same geometry) versus geometry-only matches with different chemistry. These are materially different: the former are database curation errors; the latter are different materials that happen to share a geometric arrangement. The paper should acknowledge that geometric near-duplicates are a first-pass screening tool and that chemical filtering is needed to confirm actual duplicates.

- **Figure 8 projection method is not explained.** The caption states "projections...in the analytically defined invariant coordinates" without specifying the projection method (PCA? UMAP? MDS? t-SNE?). The reader cannot interpret whether the clustering in Fig. 8 is meaningful without knowing how the projection was computed.

### Trivial
- The caption of Fig. 8 should specify the projection method used.

## Nice-to-Haves
- A brief proof sketch for Theorem 4.3 in the main text (roughly 3-5 sentences).
- A precise enumerated list of all homometric families tested with PDD{2}, indicating source and result.
- A breakdown in Table 2 or its discussion of how many flagged near-duplicates have matching chemistry versus geometry-only.
- Expand the "Discussion of Limitations" section to address the chemistry/geometry limitation explicitly, noting that element-conditioned PDDs are a natural extension.

## Removed Points

These points are flagged to be removed, treat them with caution:
1. **Harsh critic's complaint about missing appendix (within Point 2)**: "The appendix is stripped by the parser, so the reviewer cannot verify the reasoning." — Removed per hard rule: the parser strips appendix sections from all papers; proofs exist in the original submission.
2. **Harsh critic's complaint about missing discussion of "How the invariants handle atomic types"**: This is listed under "Missing Parts and Places to Improve" as a weakness, but the paper explicitly notes at the start that atoms can be considered "with or without atomic types" (line 4) and the scope is geometric invariants. Demanding full chemical extension would expand the paper beyond its stated scope. The chemistry limitation is already noted as a Minor weakness above.
3. **Harsh critic's suggestion about comparing experiments with different k values**: This is a nice-to-have but the paper's choice of k=100 is justified by Theorem 4.4, and the claim that small k are most discriminative is logically supported by the asymptotic analysis. Not a required experiment.
4. The suggestion about "a clearer explanation of the projection method used in Figure 8" is already captured in the Minor weakness above.

## Novel Insights

None beyond the paper's own contributions. The reviewer reviews do not surface any genuinely novel insight about the work that the paper itself does not already articulate. The main insight is that higher-order pointwise distance distributions (averaging over h-tuples of neighbors) break the homometric ambiguities that plague first-order PDD, while maintaining Lipschitz continuity — enabling large-scale duplicate detection at a speed that is orders of magnitude faster than alignment-based methods.

## Suggestions

- Add a one-paragraph sketch of the proof of Theorem 4.3 (PSD completeness for 1D) in the main text, even in the current section.
- Explicitly enumerate all families of homometric counter-examples from the literature tested with PDD{2}, ideally as a short table or bullet list.
- Add a sentence or two clarifying that the geometric near-duplicates identified in Table 2 should be further filtered by composition to distinguish true database duplicates from geometry-only matches.
- Specify the projection method used in Fig. 8 in the caption.

## Score and Decision

The paper makes a solid, well-evidenced contribution: it generalizes PDD to higher orders with Lipschitz continuity, demonstrates discriminative power on known homometric counter-examples, proves polynomial-time computability, and validates scalability via an impressive large-scale duplicate detection experiment across the five largest crystal databases. The weaknesses are all presentation or precision issues that do not threaten the core claims. The 1D completeness result and the "all known counter-examples" claim could benefit from more explicit justification and scoping, but these are fixable in revision.

MY FINAL SCORE: <pineapple>8.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>