Now I have thoroughly verified the paper's content against the reviewer claims. Let me produce the final consolidated review.

---

## Summary

This paper introduces higher-order invariants PDD^{h} for periodic crystals, extending the authors' prior PDD/AMD work. The invariants are proven Lipschitz continuous with constant 2 (Theorem 4.1), solve the full completeness Problem 1.2 for the 1D case (Theorem 4.3), are polynomial-time computable (Theorem 4.5), and empirically distinguish all known homometric counter-examples (Pauling crystals, Pozdnyakov–Ceriotti sets). The paper also runs a large-scale duplicate detection experiment across the five largest crystal databases, reporting thousands of previously unrecognized near-duplicates in under 8.5 hours on a desktop.

## Strengths

- **Lipschitz continuity with explicit constant**: Theorem 4.1 proves that perturbing each point by up to ε changes both PDD and PDM by at most 2ε in EMD and L∞ metrics, satisfying condition 1.2(d). This is a genuine theoretical advance — prior invariants either lacked continuity or had no proven bound — and it provides formal robustness guarantees missing from most crystal descriptors.

- **Complete solution for n=1**: Theorem 4.3 proves that PSD solves all conditions of Problem 1.2 for 1D periodic sequences, a case noted as open in prior work. This provides a rigorous baseline for higher-dimensional extensions and is clearly delimited.

- **Discrimination of all known homometric counter-examples**: The paper demonstrates that PDD^{2} distinguishes infinite families (Pauling's crystals, Pozdnyakov–Ceriotti sets) that are known to be confounded by PDD and diffraction. Figure 4 (right) shows EMD > 0 for Pauling's P(±u) for all u∈(0,0.25), directly validating the core discriminative claim.

- **Polynomial-time computability guarantee**: Theorem 4.5 proves an O(m N log N) bound with N polynomial in m for fixed n,h,ν(U). The empirical scaling in Figure 7 (left) confirms near-linear scaling with motif size, backing the theory with data.

- **Large-scale speed demonstration**: Computing ADA/PDA across all five databases (CSD, COD, ICSD, MP, GNoME) completes in under 8.5 hours on a desktop. Even ignoring the COMPACK comparison, the raw scaling result is a genuine practical achievement — no prior method has been demonstrated at this scale.

- **Hierarchical filtering pipeline**: The ADA → PDA → PDD^{h} cascade is a well-designed practical strategy that uses cheap vector invariants first (KD-tree search) and progressively stronger invariants only where needed.

## Weaknesses

### Fatal

None. The theoretical contributions (Lipschitz continuity, 1D completeness, polynomial-time bounds, discrimination of known counter-examples) are well-supported and survive regardless of experimental gaps. No weakness invalidates the paper's core claims.

### Major

- **Detected near-duplicates are unvalidated against any ground truth.** The paper's headline empirical claim — thousands of near-duplicates in Table 2 — rests on a geometric threshold (EMD < 0.01Å on PDA) that is physically motivated but never externally verified. The Lipschitz continuity (Theorem 4.1) guarantees that close structures produce close invariants, but it does **not** guarantee the converse (that close invariants imply close structures). Without checking a random subset (e.g., computing RMSD via pymatgen's StructureMatcher on 100–200 pairs, or comparing against known duplicate annotations from ICSD/CSD), the numbers in Table 2 could include false positives from incomplete discriminability of the invariants, or the threshold could be too strict and miss real duplicates. This does not undermine the theoretical contributions, but it means the paper's **main empirical claim is not yet supported by sufficient evidence**. The authors should treat this as the priority for revision.

### Minor

- **COMPACK speed comparison is extrapolated from a small sample with high variance.** The comparison (Tables 3 vs 4) extrapolates from median time on 500 random CSD pairs, but the large gap between median (117ms) and mean (582ms) indicates that COMPACK times have high variance (large cells, large motifs). Extrapolating a single number to "years" is unreliable. The qualitative conclusion (hours vs years) would likely survive, but the specific numbers in Table 4 are not robust. The paper would be stronger if it either (a) benchmarks the runtime on a representative stratified sample, or (b) simply presents the scaling result as a standalone achievement without the COMPACK extrapolation.

- **No reporting of hierarchical filter rates.** The paper describes a three-stage cascade (ADA → PDA → PDD^{h}) but never reports how many pairs survive each stage. Knowing the elimination rates would demonstrate that the fast filters are doing meaningful work and would help readers understand the efficiency of the pipeline.

- **No sensitivity analysis on k.** All experiments use k=100 with no ablation showing how the duplicate counts change for, say, k=50 or k=200. Theorem 4.4 motivates why large k adds diminishing information, but an empirical sensitivity check would strengthen confidence.

- **No analysis of false negatives.** The paper does not check whether the invariants miss known duplicate pairs that have been identified by other methods (e.g., the duplicates reported in Anosova et al. 2024). Reporting precision and recall on a small labeled set would substantially strengthen the empirical claims.

- **COMPACK is a molecule-oriented alignment tool, not a periodic-structure comparator.** While it is the traditional tool used in practice, a fairer speed baseline for periodic crystals would include tools designed for this setting (e.g., pymatgen's StructureMatcher). The paper should either include such a comparison or explicitly discuss the limitations of the chosen baseline.

### Trivial

None.

## Nice-to-Haves

- A brief discussion of how many database pairs that have identical/near-identical PDD are distinguished by PDD^{2} would directly demonstrate the added value of the higher-order invariants in practice (beyond the synthetic homometric examples).
- Reporting the number of pairs that pass each hierarchical stage (ADA → PDA → PDD^{h}) would help readers calibrate the efficiency of the cascade.
- A small-scale validation study on 100–200 detected pairs (checking RMSD with a standard tool) would transform the experimental section from a "scale demonstration" to a verified result.

## Removed Points

The following criticisms from the reviewers were checked against the paper and found to be inaccurate, misread, or inapplicable:

- **"The paper's language around completeness creates an inflated impression that PDD^{h} solves Problem 1.2 for n≥2."** — The paper is actually precise on this point. Theorem 4.3 is explicitly scoped to n=1. The abstract says "distinguish all known counter-examples" (not "solves Problem 1.2"), and the introduction says "contributions to Problem 1.2" (not "solutions"). The paper states: "The full completeness of continuous invariants was open even in dimension n=1...now complete by Theorem 4.3." This is accurate. Removed as a strawman misreading.

- **"The threshold 0.01Å is chosen arbitrarily."** — The paper explicitly motivates this: "Since the smallest inter-atomic distances are about 1Å, atomic displacements up to 0.01Å are considered experimental noise." This is physically grounded, not arbitrary. However, the deeper concern (lack of external validation of detected pairs) is retained in Major weaknesses above.

## Novel Insights

The most insightful observation from the reviews is the dissociation between the **theoretical guarantee** (Lipschitz continuity: close structures → close invariants) and the **experimental inference** (close invariants → close structures). The Lipschitz bound gives one direction; the reverse direction requires injectivity (or at least a uniform modulus of continuity on the inverse), which the paper does not prove for n≥2. This means the detected "near-duplicates" could include pairs that are genuinely non-isometric but happen to produce nearby invariant values. An explicit validation step is needed to bridge this gap.

## Suggestions

1. **Highest priority**: Validate 100–200 detected pairs from Table 2 using a standard geometric alignment tool (pymatgen StructureMatcher, or explicit RMSD after optimal rigid alignment). Report the fraction that are genuinely near-isometric. This would turn the experimental section from an impressive-but-unverified scaling demonstration into a credible result.

2. Replace the extrapolated COMPACK comparison with either (a) a benchmark on a stratified sample by motif size/cell volume, or (b) a stand-alone runtime scaling statement without the "years" extrapolation. The raw scaling result is strong enough on its own.

3. Report the number of pairs surviving each stage of the ADA → PDA → PDD^{h} cascade to show filter efficiency.

4. Add a brief sensitivity study varying k (e.g., k=50, 100, 200) for a representative subset to confirm duplicate counts are stable.

## Score and Decision

**Originality**: High. The PDD^{h} invariants and the Lipschitz continuity proof are genuinely novel.

**Importance**: High. The problem of detecting duplicates in crystal databases has significant practical implications for scientific integrity and machine learning.

**Claims support**: Moderate. Theoretical claims are well-proven. The main empirical claim (thousands of near-duplicates) is not externally validated.

**Soundness**: Good for theoretical results; moderate for experiments due to the validation gap and methodological concerns about the COMPACK comparison.

**Clarity**: Good. The paper is well-structured and careful about scope, though verbose in places.

**Value**: High. The invariants are practically useful and theoretically grounded. The validation gap is addressable.

The paper makes genuine theoretical contributions (Lipschitz continuity, polynomial-time bound, 1D completeness, discrimination of all known counter-examples) that stand independently of the experimental validation gap. The unvalidated duplicate detection is a real weakness in the experimental section but does not invalidate the theoretical core. With a validation study, the paper would be strong. In its current form, it is borderline but acceptable.

MY FINAL SCORE: <pineapple>5.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>