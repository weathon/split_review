Now I have sufficient calibration data. Let me produce the final review.

## Summary

HighClass replaces sequence alignment with hash-based token mapping for metagenomic classification, using variable-length tokens from QA-Token, quality-weighted scoring, and gradient-based sparsification. On CAMI II it achieves 85.1% F1 (within 1.5 pp of MetaTrinity's 86.6%) with 4.2× speedup and 68% memory reduction.

## Strengths

1. **Systematic ablation with nearly additive decomposition (Table 3).** The paper sequentially ablates fixed k-mers (78.3% F1), QA-Token without quality weighting (83.2%), QA-Token without sparsification (84.7%), and full HighClass (85.1%). Gains decompose as: 6.8 pp from variable-length tokens, 1.9 pp from quality weighting, with interaction effects <0.5 pp. The QA-Token + MetaTrinity alignment row (86.2%) cleanly isolates the 1.1 pp cost of replacing alignment with hash indexing.

2. **Per-operation cost breakdown bridging complexity to measured speedup (Table 5).** MetaTrinity's containment search (3.2 ms), seeding (2.8 ms), and chaining (1.9 ms) are eliminated; HighClass's token extraction (0.8 ms), lookup (0.7 ms), and scoring (0.4 ms) sum to 1.9 ms/read. The 8.8→2.1 ms total (4.2×) directly supports the claimed O(|T|) complexity reduction.

3. **Accuracy-normalized efficiency metric (F1/hour, Table 6).** HighClass achieves 170.2 F1/hour vs MetaTrinity's 41.2 (4.1×), explicitly accounting for the 1.5 pp accuracy gap. The derivation is shown (line 300), preventing the common pitfall of claiming speedup without quality normalization.

4. **Rigorous statistical validation.** The paper reports 10 independent runs, 95% bootstrap CIs (10,000 resamples), Wilcoxon signed-rank tests with Holm-Bonferroni correction, Cohen's d effect sizes (including d=−0.9 for accuracy vs SOTA), and post-hoc power analysis (80% power). This exceeds typical standards in computational biology.

5. **Scalability across 100× database range (Table 4).** HighClass throughput degrades only ~2× (1.42M→689K reads/s) from 100 to 10,000 genomes while the comparison method goes OOM at 10,000, supporting the O(|T|) complexity claim for large databases.

6. **Clear architectural contrast with deep-learning tokenization (Section 2.4).** The paper explicitly distinguishes HighClass from neural encoder pipelines: tokens are mapping primitives matched against inverted indices, not features for parametric encoders, explaining why the complexity and concentration analyses apply.

## Weaknesses

### Major

1. **Undefined baseline in scalability comparison (Table 4).** The table compares HighClass against "Metalign," which is never defined, cited, or mentioned anywhere else in the paper (not in Related Work, not in Experimental Setup Section 5.3, not among the listed baselines in Section 5.3: MetaTrinity, Kraken2, Centrifuge). A comparison table with an unidentified baseline is uninterpretable. This is a clear methodological omission that must be rectified: the authors must either identify the method with a proper citation or remove the column.

2. **Unexplained accuracy gap between QA-Token (91.7%) and HighClass (85.1%).** Section 2.1 reports that QA-Token achieves 0.917 taxonomic F1 on CAMI II, and that HighClass adopts QA-Token's pre-trained vocabulary. Yet HighClass achieves only 85.1% F1. The ablation shows QA-Token + MetaTrinity alignment reaches 86.2%, still well below 91.7%. The paper never explains what classification pipeline yields 91.7% with QA-Token tokens. If QA-Token is a full classification pipeline, the paper's framing of "near-parity with state-of-the-art" (against MetaTrinity's 86.6%) is misleading because the true SOTA among related methods is 91.7%. If the 91.7% uses a different classifier, that classifier should be a baseline and the gap must be explained.

### Minor

3. **Numerical example in the generalization bound is inconsistent with the stated rate (Section 4.3).** The paper states the excess risk bound is O(√(V|Y|/n)) and gives V=32,000, |Y|=100, n=10^6, yielding "approximately 0.021." But √(32,000×100/10^6) ≈ 1.789. For 0.021 to follow, the implied constant would need to be ~0.012, which is atypically small for a Rademacher complexity bound. While the full bound (deferred to the appendix) may contain additional structure that produces this value, the main-text presentation is confusing and should be clarified.

4. **Theoretical framework not explicitly connected to the implemented algorithm.** Section 4 discusses Rademacher complexity, α-mixing concentration, and MLE consistency for a "token-based classifier," but the paper never specifies the hypothesis class h_W that Theorem 6's bound applies to, nor explains how the bound relates to HighClass's concrete hash-based scoring function (quality-weighted log-odds aggregation via hash lookups). The theory reads as a parallel contribution about a generic class of token-based classifiers. A single explicit sentence linking the hypothesis class to HighClass's scoring function would resolve this.

### Trivial

5. **Imprecise speedup claims.** The Abstract states "4.2× speedup and 68% memory reduction compared to state-of-the-art methods." The speedup is specifically vs MetaTrinity; HighClass ties Kraken2's runtime (0.5 h). The claim should be qualified.

## Nice-to-Haves

- Characterize accuracy loss from hash-based mapping at different taxonomic ranks (genus, family), not just species-level F1.
- Analyze the 1.5% of cases where HighClass disagrees with MetaTrinity to test whether positional information is genuinely unnecessary there.
- Report token extraction time for k-mer baselines to make the runtime comparison fully symmetric.

## Removed Points

- **Missing key baselines (KrakenUniq, Bracken, CLARK).** The paper compares against Kraken2, Centrifuge, and MetaTrinity, which is a reasonable set. The criticism is a generic one-size-fits-all request that does not undermine the core claim. The paper does not claim exhaustive benchmarking.
- **"Alignment-free methods sacrificing accuracy is an oversimplification."** Framing critique that does not affect technical validity.
- **"Only three traditional methods listed in Related Work."** Related Work sections are necessarily selective; not a technical weakness.
- **"Too many deferrals to the appendix."** The appendix is stripped by the parser; it exists in the original submission.
- **"The paper overclaims novelty."** Subjective framing judgment, not a verifiable technical issue.
- **Various formatting/style nitpicks.** Not author errors.
- **Generalization bound numerical inconsistency treated as "fatal."** The issue is real but explainable (hidden constants in full bound). Demoted from fatal to minor.

## Novel Insights

None beyond the paper's own contributions. The reviews surface real methodological gaps (undefined baseline, unexplained accuracy discrepancy) but do not contribute conceptually novel observations about the work.

## Suggestions

1. **Identify and cite "Metalign"** in Table 4, or explain what method it refers to and why it is a relevant comparison. If it is a renamed version of another method, state this explicitly.
2. **Explain the QA-Token accuracy gap.** Clarify whether QA-Token (91.7%) is a full classification pipeline or a tokenizer whose output is fed to a classifier. If the former, include it as a baseline and justify HighClass's design (lower accuracy for speed/memory). If the latter, identify the classifier and state why HighClass is preferable despite lower accuracy.
3. **Reconcile the bound example** in Section 4.3 by showing which constants in the full bound (from the appendix) yield 0.021, or correct the number.
4. **Add one sentence** connecting the theory to HighClass: specify the hypothesis class and explain how the Rademacher bound applies to HighClass's scoring function.
5. **Qualify speedup/memory claims** by stating which method each compares against.

## Score and Decision

**Round 1 bracket:** 4.0–6.5, determined by comparison against:
- Weak anchors (<3.5): rejected bioinformatics benchmarks (avg 2.3–3.4) — HighClass is clearly stronger.
- Middle anchors (3.5–7.5): DNABERT-2 (6.50, Accept), MeToken (5.80, Accept), DNABERT-S (5.67, Reject), bio2token (5.00, Reject), dnaGrinder (4.50, Reject) — HighClass falls in the middle of this range.
- Strong anchors (>7.5): theory-heavy ML papers (avg 8.00) — HighClass is clearly below this bar.

**Round 2 narrowing (4.0–6.5):**
- CLIBD (4.50, Accept) — comparable, but CLIBD's weaknesses (missing baselines, limited novelty) are less structural than HighClass's undefined baseline.
- COMET (5.75, Reject) — benchmark paper, different type.
- UnitigBin metagenomic binning (4.33, Accept) — had unclear problem formulation but was accepted; HighClass has clearer strengths (ablation, statistical rigor) but more specific methodological gaps.
- dnaGrinder (4.50, Reject) — HighClass has more novel core idea and better ablation.
- bio2token (5.00, Reject) — comparable overall quality, both have gaps.

**Final calibration:** HighClass is weaker than MeToken (5.80) and DNABERT-2 (6.50) due to the two structural issues (Metalign, QA-Token gap). It is slightly stronger than dnaGrinder (4.50) due to a more novel core idea and better ablation, but the methodological gaps are more specific and verifiable. It is comparable to bio2token (5.00, Reject). The paper's core idea is interesting and the ablation is well-executed, but the undefined baseline and unexplained accuracy discrepancy are structural issues that prevent acceptance in the current form.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>