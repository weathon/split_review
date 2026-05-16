Now I have a thorough understanding of the paper. Let me synthesize the final review.

## Summary

This paper proposes higher-order pointwise invariants (PDD\(^{\{h\}}\)) for periodic crystals, proves their Lipschitz continuity, establishes completeness for 1D periodic sets (Theorem 4.3), derives asymptotic bounds and time complexity, and reports detection of thousands of near-duplicates across five large crystal databases. The paper also formalizes Problem 1.2 — a comprehensive set of desiderata (invariance, completeness, metric axioms, Lipschitz continuity, reconstructability, polynomial-time computability) for crystal descriptors.

## Strengths

- **Provable Lipschitz continuity under bounded perturbations (Theorem 4.1).** Both PDD\(^{\{h\}}\) and PDM\([l]\) change by at most \(2\varepsilon\) under perturbations up to the packing radius, satisfying condition 1.2(d) that was previously unresolved for periodic crystals. This is a genuine theoretical contribution.

- **Higher-order invariants PDD\(^{\{h\}}\) distinguish all known counter-examples that fool PDD and PDF.** Example 3.6 and Figure 4 demonstrate that Pauling's homometric crystals \(P(\pm u)\) — which have identical PDF and PDD for all \(u\) — are separated by PDD\(^{\{2\}}\) and PDD\(^{\{3\}}\) with EMD > 0. Example 3.3 proves that PDD\(^{\{2\}}\) distinguishes the infinite 1-periodic family from Example 2.5 that has equal PDD for all \(k\). Figure 5 shows continuous EMD response over the parameter range.

- **Complete invariant for 1D periodic sets (Theorem 4.3).** The Pointwise Shift Distribution (PSD) solves all six conditions of Problem 1.2 for \(n=1\), a problem previously open even in one dimension. This is a clean, self-contained theoretical result.

- **Ultra-fast near-duplicate detection across five major databases.** The pipeline (ADA → PDA, using first-order invariants) completes all-vs-all comparisons across the CSD, COD, ICSD, Materials Project, and GNoME in 8.5 hours on a desktop, finding over 28,000 near-duplicates at EMD ≤ 0.01 Å (Tables 2–3). Median time per pair is 7.48 ms for PDA vs. ~117 ms for COMPACK alignment.

- **Explicit polynomial-time complexity bounds (Theorem 4.5).** Extends earlier PDD complexity bounds to PDD\(^{\{h\}}\), linear in \(k\) and polynomial in motif size \(m\) for fixed dimension \(n\) and order \(h\).

- **Rigorous formal problem statement (Problem 1.2).** Unifies invariance, completeness, metric axioms, Lipschitz continuity, reconstructability, and computability into a single framework that can guide future work on crystal descriptors beyond this paper.

## Weaknesses

### Fatal
None.

### Major

- **The large-scale duplicate detection experiment does not demonstrate the paper's claimed novelty (higher-order invariants).** The headline results in Tables 2–3 use ADA and PDA — derived from first-order PDD (Definition 5.1) — not the higher-order PDD\(^{\{h\}}\). The paper explicitly states that PDD\(^{\{2\}}\) "is used only in rare cases to confirm exact duplicates." No experiment measures how many additional near-duplicates are found by using PDD\(^{\{2\}}\) instead of or in addition to PDA on these databases. The "ultra-fast" detection is a property of existing first-order invariants (PDD/PDA), not of the new contributions. While the paper separates its contributions in Section 1 (line 55: "(1) new higher-order invariants... (2) ultra-fast detection"), the abstract's phrasing ("we designed the invariants that distinguish... and detect thousands") conflates them in a way that overpromises on experimental backing for the higher-order invariants. **Why it matters:** A reader evaluating the paper's central methodological novelty cannot tell from the main experiment whether PDD\(^{\{h\}}\) provides practical benefit over PDD/PDA at scale. The small-scale counter-example tests (Figs 4–5) demonstrate discriminative power in isolation, but the paper's strongest empirical claim — database-scale detection — tests only the first-order stage.

### Minor

- **No manual or independent validation of claimed near-duplicates.** Table 2 reports thousands of crystals as near-duplicates at EMD < 0.01 Å (e.g., 37.3% of ICSD). The threshold is physically motivated (experimental noise), but no examples, RMSD measurements, or expert checks are provided to confirm that these pairs are indeed geometrically near-identical versus coincidentally similar under the PDA metric. The COMPACK comparison (Tables 3–4) addresses only runtime, not agreement on which pairs are duplicates. A small validation study (e.g., inspecting 20–100 flagged pairs) would substantially strengthen the practical claim.

- **Completeness status for \(n>1\) could be clearer.** The paper accurately states that PDD\(^{\{h\}}\) "distinguishes all known counter-examples" and cites prior work showing PDD distinguishes all sets in general position (line 196). However, the introduction and discussion sections sometimes blur the distinction between "solves Problem 1.2 for \(n=1\)" (proven) and "distinguishes all known counter-examples for \(n=2,3\)" (empirically demonstrated, but completeness unproven). Explicit statements that "for \(n>1\), completeness remains open" (as opposed to being implied by the examples) would prevent overestimation.

- **COMPACK runtime extrapolation is not rigorous.** The "years" claim in Tables 3–4 extrapolates from a median of 117 ms on 500 random pairs, assuming linear scaling. COMPACK alignment likely scales superlinearly (pairwise \(O(n^2)\) or worse in motif size), so the extrapolation to millions of pairs is a rough ballpark, not a precise estimate. This should be acknowledged.

- **Figure 8's projection coordinates are not explained.** The map of invariant coordinates (Figure 8) is visually striking but the paper does not specify which invariant coordinates are used or how the 2D projection is generated, making it uninterpretable as a standalone figure.

- **Claim that PDD\(^{\{2\}}\) "distinguished all known (infinitely many) counter-examples"** (line 194) is supported by exactly two families (Example 2.5 and the Pauling crystals). If other families exist in the literature, they should be referenced; if not, the phrasing could be read as claiming broader validation than shown.

- **Hyperparameter choices (k=100, l=10, EMD threshold 0.01 Å) are motivated but not ablated.** The choices are reasonable and partially justified by Theorem 4.4's asymptotics and physical reasoning, but a sensitivity analysis would clarify whether the duplicate counts are robust to these settings.

### Trivial

- The phrase "this unresolved discontinuity created a gigantic loophole" (line 47) refers to the discontinuity of **cell-based representations** (Fig. 1 right), not to PDD — the paper correctly cites prior Lipschitz-continuous PDD (Widdowson & Kurlin 2022). The harsh critic's reading that this claim "is not new" is a misunderstanding; the sentence describes the problem motivating the work, not a novelty claim about the paper's own invariants.

## Nice-to-Haves
- An experiment comparing PDD (first-order) vs. PDD\(^{\{2\}}\) on the duplicate detection task, even on a database subset, to directly show that higher-order invariants find additional pairs that first-order misses.
- A brief ablation or sensitivity analysis for the key hyperparameters (k, EMD threshold).
- Explanation of the projection in Figure 8 (coordinate definitions, dimensionality reduction method).

## Removed Points
These points are flagged to be removed; treat them with caution.

- **"The discontinuity claim is not new"** — The harsh critic claimed the paper's statement "this unresolved discontinuity created a gigantic loophole" was not new because prior work introduced Lipschitz continuous PDD. This misreads the paper: the sentence refers to the discontinuity of **cell-based representations** (Fig. 1 right), a known problem the paper is addressing; it is not claiming novelty of PDD's continuity.

- **"Section 2 notation is garbled"** — Parser artifact from PDF extraction; not present in the original submission.

- **"Proofs are absent"** — Expected in a main-track paper; proofs deferred to an appendix stripped by the parser.

- **"Missing comparison with SOAP/MACE"** — This is a demand for additional related work and baselines that would broaden the paper beyond its stated scope; it is a request for a different paper rather than a weakness of this one.

- **"Data availability and code not mentioned"** — Standard reproducibility concern that can be addressed post-acceptance; does not affect the technical evaluation of the paper's claims.

- **"Section 2 notation garbled by the parser"** — Same parser artifact as above.

## Novel Insights
None beyond the paper's own contributions.

## Suggestions

1. **Realign the large-scale experiment or reframe the narrative.** The most impactful revision would be to either (a) add a comparative experiment showing that PDD\(^{\{2\}}\) detects additional near-duplicates that PDA misses on a sampled subset of the databases, or (b) clearly separate the two contributions in the abstract and explicitly state that the large-scale detection pipeline uses first-order invariants while the higher-order invariants are validated on specific counter-examples. Option (b) requires no new experiments and would eliminate the narrative mismatch.

2. **Add validation examples for claimed near-duplicates.** Even a small set of 10–20 pairs with overlaid structures or RMSD values would transform Table 2 from a suggestive number to a convincing result.

3. **Explicitly state the completeness gap for \(n>1\)** in the discussion: "For \(n>1\), completeness remains an open problem; the new invariants distinguish all known counter-examples and are Lipschitz continuous, but a proof of full completeness is not yet available."

4. **Acknowledge the COMPACK scaling assumption.** Add a sentence noting that the runtime extrapolation assumes linear scaling and is a rough upper bound.

## Score and Decision

The paper makes genuine theoretical contributions: a family of Lipschitz continuous higher-order invariants (PDD\(^{\{h\}}\)), a completeness proof for 1D periodic sets, asymptotic bounds, and polynomial-time complexity guarantees. The small-scale experiments on Pauling crystals and other homometric families validate the discriminative power of the new invariants. The large-scale duplicate detection is practically valuable and demonstrates the pipeline's speed. However, the main experiment does not test the paper's claimed novelty (higher-order invariants) — it tests first-order invariants whose properties were already established. This gap between narrative and evidence is a real weakness but does not invalidate the theoretical contributions or the practical value of the pipeline. The paper's strongest results (Theorem 4.1, Theorem 4.3, the discriminative examples) stand on their own, and the weakness is addressable through clearer framing and/or additional targeted experiments.

**Originality:** Good — higher-order invariants are new, formal problem statement is valuable.  
**Importance of question:** High — crystal duplicate detection and complete invariants with continuity are important.  
**Claims supported:** Partially — theoretical claims are supported, but the experimental narrative overreaches.  
**Soundness:** Good — theoretical results appear sound; experiments are well-designed for what they test.  
**Clarity:** Good — well-organized despite complex notation; the gap between narrative and evidence is the main presentation weakness.  
**Value to community:** Significant — the invariants, 1D completeness result, and analysis of database duplicates are all valuable.

MY FINAL SCORE: <pineapple>6.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>