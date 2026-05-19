- Decision: Reject
- Avg Score: 4.50
- Scores: 5, 5, 5, 3
Now I have a comprehensive understanding of the paper. Let me construct the final consolidated review.

## Summary

This paper introduces higher-order pointwise distance distributions (PDD^{h}) as invariants for periodic crystals. These invariants satisfy Lipschitz continuity and distinguish all known homometric counter-examples that fooled all previous geometric descriptors (including PDD). The paper proves complete invariance for n=1 (Theorem 4.3) and demonstrates practical impact by detecting thousands of near-duplicates across the five largest crystal databases in under 8.5 hours on a desktop—a task requiring years with standard alignment methods.

## Strengths

- **Higher-order invariants break homometric pairs that PDD cannot distinguish**: Example 3.6 and Fig. 4(right) show PDD^{2} and PDD^{3} give EMD > 0 for Pauling's homometric crystals P(±u), which have identical PDDs for all k. Example 3.3 further shows PDD^{2} distinguishes the 2D homometric sets from Example 2.5 that also had equal PDDs. This goes beyond a decade of prior invariants.

- **Ultra-fast near-duplicate detection at database scale**: Using PDA(S;100) with EMD ≤ 0.01Å, Tables 3–4 show that all near-duplicates across CSD, COD, ICSD, MP, and GNoME are found in under 8.5 hours on a desktop, whereas COMPACK would require years. Table 2 reports thousands of previously unknown near-duplicates, including >34% of ICSD entries, demonstrating a practical capability that was impossible before.

- **Lipschitz continuity guarantee**: Theorem 4.1 proves that PDD^{h} changes by at most 2ε under ε-perturbations (for ε < packing radius), satisfying condition 1.2(d). This provides a continuous metric essential for robust machine learning on noisy crystal data—a requirement not satisfied by cell- or symmetry-based descriptors.

- **Complete invariant for 1D periodic sequences**: Theorem 4.3 solves Problem 1.2 for n=1 via PSD(S;m), closing a long-standing gap even in the one-dimensional case.

- **Hierarchical filtering design**: Section 5 describes a pipeline using ADA(S;100) for fast kd-tree search, then PDA(S;100) for coarse EMD filtering, and only PDD^{h} for confirmation. This achieves scalability without sacrificing discriminative power.

## Weaknesses

### Fatal
None.

### Major
None. The paper's core claims are well-supported by theory and experiments.

### Minor

- **EMD base metric for comparing PDD rows is not specified**: Definition 3.5 defines EMD generically with an abstract base metric d, but never states what metric is used to compare rows of PDD (which are vectors of distances). For PDM, the paper specifies L∞ (line 112). For PDD, the base metric is left ambiguous. This affects reproducibility, as different base metrics (L1, L2, L∞) produce different EMD values.

- **Clarity on completeness status across dimensions**: The paper is honest about what is proven—the abstract says "distinguish all known counter-examples" (empirical) and the conclusion notes full completeness was open even for n=1. However, a reader could benefit from an explicit statement at the outset: "Problem 1.2(a,c,d,f) satisfied for all n; (b,e) fully satisfied for n=1; for n>1 the invariants distinguish all known counter-examples and all crystals in general position." The paper relies on the reader to piece this together from scattered statements.

- **No empirical false-positive validation at the chosen threshold**: The paper uses EMD < 0.01Å as the near-duplicate cutoff, motivated by atomic vibration scales, but does not validate false positives on a hold-out set of manually verified distinct pairs. While false positives are unlikely for random structures, highly symmetric crystals with few independent parameters could produce accidental near-matches. A small-scale validation (even 100 hand-checked pairs near the threshold) would strengthen the claim.

### Trivial

- **Theorem 4.5 mentions skewness ν(U) can be arbitrarily large for skewed cells**: The polynomial-time guarantee depends on ν(U) being bounded in practice; the paper does not discuss whether real crystals have bounded skewness. This is a minor technical point unlikely to affect practice.

## Nice-to-Haves

- A table showing which conditions of Problem 1.2 are satisfied for n=1, n=2, n=3 would improve clarity.
- A simple experiment tracking EMD under random Gaussian perturbations of a real crystal (analogous to Fig. 5) would provide empirical verification of the Lipschitz continuity.
- An explicit false-positive analysis on a hand-verified set of distinct crystals near the threshold would further strengthen the database comparison.

## Removed Points

These points were raised by reviewers but removed for the reasons stated:

- **Lipschitz proof gap regarding row merging under perturbation**: The harsh critic speculated about a gap in handling row identity changes, but acknowledged the appendix was stripped and the issue is "likely handled correctly." The theorem explicitly conditions on ε < r(S) (packing radius), which prevents topology changes in neighbor ordering. This is speculative, not a verified flaw.

- **Completeness claim as "subtly misleading"**: The paper's abstract and body consistently state "distinguish all known counter-examples," not full theoretical completeness for n>1. The paper explicitly says "full completeness of continuous invariants was open even in dimension n=1, now complete by Theorem 4.3." The framing is honest, not misleading.

- **COMPACK baseline being "unfair"**: The comparison is between the new method (hours) and the standard method used in practice (years). If anything, the asymmetry (favoring the slower baseline) makes the comparison harder on the authors. This is a valid speed benchmark.

- **Figure 8 being "speculative"**: The paper presents this as a visualization and acknowledges the limitation that random PDD^{h} may not correspond to real crystals. No strong claim is made.

- **Missing appendix content (Example 3.3 relying on Appendix B)**: The appendix was stripped by the parsing process; it exists in the original submission.

- **Code availability concerns**: Per policy, doubts about release status of cited resources are not valid criticisms.

- **Transitivity argument being "slightly overstated"**: This is a conceptual/philosophical framing choice, not a technical weakness.

- **Theorem 4.4 practical value questioned**: The paper explicitly addresses why k=100 is used and states the invariants are "most discriminative for small values of k."

## Novel Insights

The crispest finding from the two reviews is that the paper's strength lies in its practical engineering as much as its theory. While the theoretical completeness for n>1 is open (and honestly acknowledged), the database-scale experiment—screening 5 databases in 8.5 hours and finding >34% near-duplicates in ICSD—constitutes the paper's strongest contribution. The hierarchical filtering (ADA → PDA → PDD^{h}) design also reveals a noteworthy meta-insight: building faster-but-weaker preliminary invariants (ADA, PDA) that share theory with the stronger invariant (PDD^{h}) enables practical scalability that would be impossible with just the strongest invariant alone.

## Suggestions

1. **Explicitly specify the base metric** used for comparing PDD rows in EMD computation (L1, L2, or L∞).
2. **Add a small false-positive validation** by hand-checking 50–100 pairs of distinct crystals with EMD just above the 0.01Å threshold to confirm the method does not produce false alarms.
3. **Add a table or sentence** at the end of Section 3 explicitly stating which conditions of Problem 1.2 are proven for which dimensions.
