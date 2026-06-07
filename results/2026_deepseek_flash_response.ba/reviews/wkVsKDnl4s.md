Now let me write the final consolidated review.

## Summary

HighClass is a metagenomic classification framework that replaces sequence alignment with hash-based token-to-taxon lookups. Using pre-trained QA-Token vocabularies, quality-weighted scoring, and gradient-based sparsification, the method achieves 85.1% F1 on CAMI II (within 1.5pp of MetaTrinity) with 4.2× speedup and 68% memory reduction. The paper claims three co-equal contributions: theoretical foundations for token-based classification, algorithmic innovation (hash-based mapping), and empirical validation.

## Strengths

- **Transparent component-wise ablation (Table 3).** The ablation decomposes each component's contribution nearly additively: variable-length tokens (+6.8pp over k-mers), quality weighting (+1.9pp), and sparsification (99.5% relative accuracy preservation). Crucially, it reports that the hash-mapping replacement costs 1.1pp F1 relative to using the same QA-Token vocabulary with full MetaTrinity alignment (86.2% → 85.1%), honestly revealing the trade-off.

- **Statistical rigor beyond typical bioinformatics papers.** The evaluation uses 10 independent runs, 95% bootstrap CIs (10,000 resamples), Wilcoxon signed-rank tests with Holm-Bonferroni correction, Cohen's *d* effect sizes, and post-hoc power analysis. Table 2 reports CIs for every method, enabling proper comparison.

- **F1/hour as a composite metric (Table 6).** The accuracy-normalized throughput metric (170.2 F1/hour vs. MetaTrinity's 41.2 and Kraken2's 140.0) captures the paper's central engineering claim without cherry-picking speed or accuracy alone.

- **Scalability demonstration (Table 4).** Throughput and memory are reported across database sizes from 100 to 10,000 genomes, showing that the method maintains 689K reads/s even at the largest scale.

## Weaknesses

### Major

**1. Theory-method disconnect undermines a claimed core contribution.** The paper presents three theoretical results (generalization bound via Rademacher complexity, concentration inequalities under α-mixing, consistency of maximum likelihood classification) and explicitly lists them as co-equal contributions (Section 1.3, line 66: "Theoretical Foundations" as contribution 1). However, the actual method is an indexing/lookup scheme — it pre-computes token-to-taxon frequency tables from a reference database and classifies reads by aggregating hash-lookup evidence. It does not train a classifier from i.i.d. training samples via empirical risk minimization. The bound "excess risk of approximately 0.021 with 95% confidence" (Section 4.3, line 174) is stated with concrete numbers (V=32,000, |Y|=100, n=10^6) but it is never explained what constitutes a "training sample" or how the hypothesis class maps to the actual algorithm. The prose-level description (Section 4) sketches the results without showing the derivation; the appendix (stripped) would contain proofs, but even the main text does not bridge the gap between the theoretical framework and the deployed method. This disconnect means one of the paper's three claimed contributions is unsupported.

**2. Numerical inconsistency in sparsification claims.** The abstract (line 13) states "Gradient-based sparsification retains 32% of genomic regions while preserving 94% accuracy." Section 5.4.3 (line 260) states "Retaining 32% of features preserves 99.5% relative accuracy." Table 1 shows F1 dropping from 85.8% to 85.1%, which is (85.1/85.8) ≈ 99.2% relative preservation. The value "94%" does not match any computation in the paper and conflicts with the other stated values. This is a clear factual error in the presentation.

**3. Unexplained QA-Token benchmark discrepancy.** The paper (Section 2.1, line 100) states that QA-Token (Gollwitzer et al., 2025) "achieves 0.917 taxonomic F1 on CAMI II." HighClass, which adopts QA-Token's pre-trained vocabularies, achieves 85.1% F1 — a 6.6pp gap. The paper never explains whether this discrepancy stems from a different evaluation protocol, a different taxonomic level, a different subset of CAMI II, or some other factor. Without clarification, a reader cannot assess whether HighClass is competitive with methods whose own components it uses.

**4. "Metalign" is undefined.** Table 4 introduces "Metalign" as a scalability comparison baseline, but this method is never defined, cited, or described anywhere in the main text. This makes the scalability comparison unverifiable.

### Minor

- **Limited baseline set.** The experimental comparison includes only MetaTrinity (2023), Kraken2 (2019), and Centrifuge (2016). No comparison against Bracken, KrakenUniq, Kaiju, CLARK, or other widely-used metagenomic classifiers. This narrow set weakens the "state-of-the-art" claim, especially since MetaTrinity and QA-Token share overlapping authors.

- **Quality sensitivity parameter η is described as "learned" (η≈1.8) but no learning procedure, validation data, or sensitivity analysis is presented.** The paper does not show how results vary with η or how this parameter was estimated.

- **The language exceeds the evidence.** Terms like "paradigm shift," "fundamental transformation" (Abstract), and "first comprehensive theory of token-based genomic classification" (line 15) are disproportionate for a method that combines existing components with a hash-index replacement and whose ablation honestly shows a 1.1pp accuracy cost for the core innovation.

### Trivial

None.

## Nice-to-Haves

- Sensitivity analysis for η and other hyperparameters
- Additional baselines (Bracken, KrakenUniq, Kaiju)
- Explanation of why positional information from alignment can be dropped for taxonomic classification

## Removed Points

- The harsh critic's claim that the theoretical constants (γ≈0.15, variance inflation factor 31.7) "read as post-hoc numbers that could come from any dependent-data model" — this is speculative. The paper does state empirical validation of γ≈0.15 on CAMI II data (Section 4, line 53), so the claim goes beyond what can be verified from the main text.
- The critique about vocabulary size (32,000) not being "shown to arise from or constrain the algorithm" — this is not a claim the paper makes. The vocabulary size comes from QA-Token's pre-trained vocabulary, as stated.
- The strength about "clear positioning of what is novel vs. adopted from prior work" — this is standard academic practice, not a distinguishing strength for ICLR.
- The harsh critic's point that "the paper's language exceeds the contribution" regarding "paradigm shift" etc. is kept in Minor (it's valid), but the framing as a separate critical issue is downgraded from Fatal to Minor.
- The strength about "explicit characterization of the accuracy-efficiency Pareto frontier" is generic since the F1/hour metric already captures this.

## Novel Insights

The paper's cleanest insight — and the one best supported by its evidence — is that alignment operations in metagenomic classification can be largely replaced by hash-based token lookups while incurring only a small accuracy penalty (~1.1pp). The ablation study (Table 3) provides unusually transparent evidence for this trade-off, showing that the contribution from variable-length QA-Token tokens (+6.8pp) is orthogonal to and larger than the cost of replacing alignment (-1.1pp). This suggests that for the taxonomic classification task, precise alignment positions contribute less discriminative information than the presence/absence patterns of learned tokens, which is a non-obvious finding worth further investigation.

## Suggestions

1. **Drop or substantially reframe the theoretical contribution.** Either remove the theory section entirely and present the paper as an engineering contribution, or (if the authors believe the theory genuinely applies) explicitly define the hypothesis class, training procedure, and loss function in terms of the actual algorithm, then show how the bound constrains or explains observed behavior.

2. **Fix the numerical inconsistency.** Align the sparsification accuracy claim across abstract, main text, and Table 1. If 94% refers to a different metric, define it and explain the discrepancy.

3. **Explain the QA-Token benchmark gap.** If QA-Token's 0.917 F1 uses a different protocol, taxonomic level, or benchmark subset, state this clearly in the main text.

4. **Define Metalign** (or replace the scalability comparison with a cited baseline).

5. **Tone down the framing.** Replace "paradigm shift" and "first comprehensive theory" with language that accurately reflects the engineering trade-off.

## Score and Decision

**Calibration anchors (all rounds):**

| Anchor | Avg Score | Round | Comparison to HighClass |
|--------|-----------|-------|------------------------|
| IEZjjDX0iC (Phage protein LMs) | 3.00 | R1 weak | Weak — pure benchmark, no method. HighClass stronger. |
| PN3i4b6NED (OpenMeta) | 3.50 | R2 narrow | Weak — pure benchmark, no method. HighClass stronger. |
| BvQkjCnXXr (FastLSH) | 4.50 | R1 mid | Comparable — both have theory-method concerns and narrow comparisons. |
| NPViqdhTIi (Gzip molecular) | 4.75 | R1 mid | Comparable — both apply simple methods to domain problems with incomplete baselines. |
| 9klRFLY2TT (DNABERT-S) | 5.67 | R2 narrow | Stronger — DNABERT-S has cleaner methodology and stronger empirical results without numerical errors. |
| STUGfUz8ob (Transformer reasoning) | 7.60 | R1 strong | Much stronger — deep theoretical contribution at top-venue level. HighClass not comparable. |

**Round 1 bracket:** Between ~3.5 (OpenMeta) and ~5.67 (DNABERT-S). Narrow plausible range: (4.0, 5.5).

**Round 2 narrowing:** Compared against OpenMeta (3.50, HighClass is clearly stronger — it has an actual method), FastLSH (4.50, similar issues but HighClass has cleaner ablation), Gzip (4.75, similar level), and DNABERT-S (5.67, HighClass is weaker due to the theory-method disconnect and numerical inconsistencies). HighClass sits in the 4.0–5.0 range, closer to FastLSH (4.5) than to DNABERT-S (5.67).

**Final score: 4.5.** The paper has a genuine engineering contribution validated by a clean ablation study, and the F1/hour metric effectively captures the speed-accuracy trade-off. However, the theory-method disconnect, numerical inconsistency, unexplained QA-Token gap, and undefined baseline are significant issues at ICLR standards. The paper would need major revisions (at minimum resolving items 1–4 in Suggestions) to be competitive.

MY FINAL SCORE: <score>4.5</score>
MY FINAL DECISION: <decision>Reject</decision>