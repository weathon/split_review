Now I have sufficient calibration. Let me write the final review.

## Summary
HighClass proposes replacing alignment-based seed-and-extend operations with hash-based token mapping for metagenomic taxonomic classification, leveraging pre-trained QA-Token vocabularies, quality-weighted scoring, and gradient-based sparsification. The paper claims 4.2× speedup and 68% memory reduction over MetaTrinity while staying within 1.5% F1 (85.1% vs 86.6% on CAMI II Marine).

## Strengths
1. **Granular per-operation cost breakdown (Table 5)**: Decomposes both MetaTrinity and HighClass into individual operations with standard errors, tracing the 4.2× speedup to specific eliminated operations (containment search, seeding, chaining — ~85% of MetaTrinity's runtime). This is a concrete, well-evidenced engineering contribution.

2. **Component-wise ablation with near-additive decomposition (Table 3, Section 5.4.3)**: Isolates each component's F1 contribution: +6.8 pp from variable-length tokens over fixed k-mers, +1.9 pp from quality weighting, and only 1.1 pp gap between hash-based and alignment-based versions of the same token vocabulary. Interaction effects are reported as <0.5 pp. This is arguably the paper's strongest empirical contribution.

3. **Multi-metric sparsification evaluation (Table 1)**: Reports five metrics (index size, load time, query time, F1, cache misses) for the sparsified index, covering memory, speed, accuracy, and hardware-level behavior. This is more thorough than typical sparsification reports.

4. **Controlled contrast with deep-learning tokenization (Section 2.4)**: Clearly distinguishes HighClass's use of tokens as *mapping primitives* matched against inverted indices from the common paradigm of tokenization as features for neural encoders. This clarifies what is architecturally different about the approach.

## Weaknesses

### Major
1. **Missing results for 3 of 4 listed benchmarks**: The paper lists four evaluation datasets (CAMI II Marine, CAMI II Strain, HMP Mock communities, Zymo Standards) at lines 214–215, but only reports full results for CAMI II Marine (Table 2). No results appear for strain-level classification or mock communities. The paper claims "comprehensive evaluation" and "empirical excellence" but substantiates this claim on only one dataset. This leaves open critical questions: does HighClass degrade more sharply on strain-level tasks where closely related taxa differ subtly? How does it perform on defined-abundance communities where quantitative metrics matter?

2. **Unexplained "Metalign" baseline in scalability comparison (Table 4)**: Metalign appears as a comparison method for scalability with no citation, description, or prior mention anywhere in the paper. The reader cannot assess whether Metalign is a reasonable baseline, how it was configured, or how it relates to the methods compared in the accuracy evaluation (MetaTrinity, Kraken2, Centrifuge). This makes the scalability results — a core contribution claim — uninterpretable.

3. **Excess risk bound arithmetic inconsistency (Section 4.3)**: The paper states that with V=32,000, |𝒴|=100, n=10⁶, the bound yields "excess risk of approximately 0.021" (line 174). However, the stated formula *O(√(V|𝒴|/n))* gives √(32,000·100/10⁶) = √3.2 ≈ 1.79, not 0.021. This is not a small rounding error — the discrepancy is two orders of magnitude. The paper neither provides the missing normalization/constant factors nor explains how 0.021 is derived. For a paper that prominently features "rigorous theoretical foundations" as a headline contribution, this is a serious issue. It undermines confidence that the theoretical results are correctly specified.

### Minor
4. **QA-Token F1 gap unexplained (Section 2.1 vs Table 3)**: The paper states QA-Token achieves "0.917 taxonomic F1 on CAMI II" (line 100), yet the paper's own QA-Token + MetaTrinity alignment configuration achieves only 86.2% species-level F1 (Table 3). The 5.5 pp gap is never discussed. It may be explainable (different taxonomic rank, dataset subset, or protocol), but the paper does not provide that explanation, making it hard to understand the baseline against which the 1.5% gap to "state-of-the-art" is measured.

5. **Theoretical contributions overstated (Section 4, Conclusions)**: The paper claims "the first comprehensive theory of token-based genomic classification" and "rigorous theoretical framework." What is actually presented is: (a) a standard finite-hypothesis-class Rademacher bound, (b) standard α-mixing concentration inequalities, and (c) standard MLE consistency — none exploiting properties of genomic sequences or token representations. These are not wrong, but the novelty claim is significantly inflated.

6. **Sparsification method underdescribed (Section 5.2)**: The sparsification component — responsible for 68% memory reduction — is described in approximately two sentences. No details are given about how gradient-based importance scoring is trained, what objective it optimizes, whether masks are per-taxon or global, or how the 32% retention threshold was chosen.

### Trivial
7. The ψ function in the quality-aware scoring formula (line 142) is never defined in the main text.
8. The abstract claims *O(|𝒯|)* complexity but the full pipeline includes *O(|𝒯||𝒞|)* scoring over candidate sets, acknowledged only at line 148.

## Nice-to-Haves
- Report results for CAMI II Strain, HMP Mock, and Zymo Standards.
- Add a citation and brief description of Metalign, or replace it with a baseline introduced in the experimental setup.
- Provide full details of the sparsification training procedure.
- Clarify the QA-Token F1 discrepancy (specify taxonomic rank, dataset subset, or protocol difference).
- Correct or clarify the excess risk bound computation.
- Either tone down the "first comprehensive theory" claim or show how the theory exploits genomic-specific structure.

## Removed Points
- *Reliance on external components "under-discussed"*: The paper explicitly cites what it builds on (QA-Token, MetaTrinity, gradient-based sparsification) in lines 87–90 and 98–104. Adequately transparent. Removed.
- *Reproducibility/code availability concerns*: Per hard rules, remove nitpicks about "will release" code status. Standard for conference submissions. Removed.
- *Complexity claim O(m log n + k log k) without derivation*: This is a standard description for alignment-based methods; no derivation is expected. Removed.
- *O(|\mathcal{T}|) complexity "only half the story" in the abstract*: The scoring term *O(|\mathcal{T}||𝒞|)* is acknowledged in Section 3.5. Minor omission from the abstract; standard practice. Demoted from kept weakness to removed.

## Novel Insights
None beyond the paper's own contributions.

## Suggestions
1. Report results for all four listed benchmarks before claiming comprehensive evaluation.
2. Cite and describe Metalign, or replace it with a properly introduced baseline.
3. Correct the excess risk bound formula and/or its numerical value.
4. Add 3–5 sentences describing the sparsification training procedure.
5. Clarify the taxonomic rank and protocol underlying the cited QA-Token F1 to resolve the 91.7% vs 86.2% gap.

## Score and Decision

**Bracket calibration:**

Round 1 bracketing searched the human-review corpus for papers on metagenomic/genomic classification across three bands. The paper clearly fell below the strong band (avg 8.0, all accepts) and above the very-weak band (avg 3.0–3.4, all rejects), placing it in the 3.5–7.5 bracket.

Round 2 narrowed within this bracket by searching for computational biology method papers. Key anchors:
- **dnaGrinder** (4.50): Lightweight genomic foundation model with minimal innovation and no ablation. HighClass has a more novel core idea and better ablation but worse evaluation completeness.
- **Gzip for Molecular Classification** (4.75): Simple adaptation of an existing method with weak baselines. HighClass has stronger empirical methodology (ablation, per-operation breakdown) but similar evaluation gaps.
- **DNABERT-S** (5.67): More thorough evaluation (23 datasets) but comparable methodological novelty concerns. HighClass is clearly weaker in evaluation breadth.
- **Genomic Foundationless Models** (4.25): Thorough experiments but narrow contribution. HighClass has broader scope but more evaluation gaps.

HighClass sits near the lower end of this range. Its core engineering idea (replacing alignment with hash-based token mapping) is genuinely interesting and the ablation study is well-executed. However, the evaluation is substantially incomplete (1/4 benchmarks reported), the scalability comparison is undermined by an unexplained baseline, and the theoretical claims — which the paper explicitly headlined as a core contribution — contain a significant arithmetic inconsistency in the claimed excess risk bound. These issues collectively prevent acceptance at a top-tier venue.

**Final score: 4.5** — a paper with a promising core idea and good ablative experiments, but whose evaluation incompleteness, unexplained baseline, and mathematical inconsistencies prevent acceptance in its current form. A major revision addressing these gaps could produce a solid contribution.

MY FINAL SCORE: <score>4.5</score>
MY FINAL DECISION: <decision>Reject</decision>