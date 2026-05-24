Now I have enough calibration data. Let me write the consolidated review.

**Round 1 Bracket**: I bracketed the paper against weak anchors (2.5–3.0), middle anchors (4.0–6.0), and strong anchors (8.0). The paper clearly doesn't belong in the strong band (8.0, unrelated topics). It sits in the weak-to-middle range.

**Round 2 Narrowing**: I compared it against RaftPPI (5.00, well-evaluated PPI retrieval, accepted), HIPPO (3.50, PPI prediction, withdrawn/rejected), Drug-ProGO (5.00, drug screening, rejected), and LiveProteinBench (4.00, benchmark, rejected). The current paper has a more novel problem framing than HIPPO and LiveProteinBench but has evaluation gaps that make it weaker than RaftPPI. The missing ablation for the core methodological contribution and the xCAPT5 table inconsistency are significant concerns.

Let me write the final review.

## Summary

This paper introduces the problem of PPI candidate ranking for experimental prioritization and proposes a two-stage framework: (1) interpretability-guided retrieval using activated embedding regions from D-SCRIPT/Topsy-Turvy's contact maps to measure cosine similarity, and (2) re-ranking using interaction scores, structural plausibility (pDockQ), functional annotations, and LLM-based semantic similarity. The evaluation uses a temporal holdout (STRING v11→v12), where 279K new interactions from v12 serve as ground truth. The approach shows improved early retrieval metrics (e.g., Recall@10 from 0.0124 to 0.2641 with D-SCRIPT backbone).

## Strengths

1. **Novel problem formulation with prospective temporal evaluation**: The paper formalizes PPI candidate ranking using STRING v11→v12 as a temporal holdout (Section 5.1), creating a realistic test of whether methods can anticipate interactions confirmed in a later release. This goes beyond static, within-release benchmarks that dominate the PPI literature.

2. **Interpretability-guided retrieval is a creative methodological device**: Instead of using interpretability post-hoc for explanation, the paper exploits the contact-map structure of D-SCRIPT/Topsy-Turvy as a retrieval tool — selecting active residues from predicted contact maps to guide embedding alignment (Section 4.1, Equation 3). This repurposing of model internals for a non-classification task is technically interesting.

3. **Multi-source re-ranking reveals complementary signals**: Table 2 provides a comprehensive rank-shift analysis across 10 evidence sources (cosine, IS, pDockQ, TF-IDF, Token, Location, KeyTerm, BioBERT, BioMedRoBERTa, PubMedBERT). The finding that PubMedBERT improves/maintains 75.5% of rediscoveries over the cosine baseline, while lightweight annotation overlap heuristics achieve ~70%, is practically informative for screening design (Section 5.3, Table 2).

4. **Large-scale, carefully preprocessed dataset**: The pipeline processes 279,568 new positive interactions from STRING v12, with CD-HIT clustering at 40% identity, length filtering, and a 10:1 negative ratio, ensuring methodological alignment with prior work (Section 5.1).

5. **Honest limitation analysis**: Section 6 explicitly identifies the reliance on known interaction partners and the lack of biological interpretability in the final rankings — genuine self-assessment that helps scope the claims.

## Weaknesses

### Major

1. **Missing ablation: activation masking vs. full-embedding cosine similarity**. The paper's core methodological claim is that focusing on *activated* embedding regions (guided by contact-map interpretability) produces better rankings. However, there is no comparison against the simplest possible baseline: computing cosine similarity over *full* embeddings (no activation masking). Without this ablation, the observed improvements (21× Recall@10) cannot be attributed to the interpretability-guided component rather than the switch from a classification score to *any* embedding-alignment score. This is a critical gap in the evidence chain for the main contribution. (Section 4.1 vs. Table 1)

2. **xCAPT5 results in Table 1 appear internally inconsistent**. The xCAPT5 row reports Precision@5=0.1943 and Success@5=0.0059. With standard metric definitions: Precision@5 of 0.1943 means ~19.4% of top-5 positions are true positives, requiring ~0.97N true positives across N proteins. But Success@5=0.0059 means only 0.59% of proteins have *any* true partner in the top-5, which caps total true positives at 0.0059N×5=0.0295N — roughly 30× fewer than needed. These numbers cannot simultaneously hold. Either the metrics are computed differently from what is stated, or there is a data-processing error. This undermines confidence in the entire table, not just the xCAPT5 rows, and the paper does not discuss this discrepancy. (Table 1, lines 179-184)

3. **"Two orders of magnitude" claim is unsupported**. The abstract and conclusion state that the method improves ranking metrics "by two orders of magnitude" (100×). The largest improvement in Table 1 is Recall@5 for D-SCRIPT (0.0071 → 0.1832 ≈ 26×). MRR improves ~5×. Neither approaches 100×. This claim should be corrected or explicitly qualified. (Abstract, line 283; Table 1)

### Minor

4. **Activation threshold for "highly activated residues" is underspecified**. Section 4.1 states that the method scans for "maximal contiguous segments of highly activated residues" but never defines what threshold determines "highly activated." Is it absolute (contact probability > 0.5)? Relative (top X% of residues)? Without this detail, the method is not reproducible, and the results could depend sensitively on an unstated hyperparameter. (Section 4.1, lines 93-94)

5. **No comparison against simple ranking/retrieval baselines**. The baselines are raw interaction probabilities from PPI classifiers (D-SCRIPT, Topsy-Turvy, xCAPT5). The paper does not compare against straightforward ranking methods such as BLAST-based sequence similarity, k-NN over protein embedding space, or even full-embedding cosine similarity (see point 1). While comparison against PPI classifiers is a reasonable starting point, the absence of any non-classifier ranking baseline makes the headline improvement numbers hard to contextualize. (Table 1)

6. **Re-ranking analysis covers only a highly selected subset**. The re-ranking module (Section 4.2) operates on top-10 candidates only — 2,280 protein-candidate pairs. For the D-SCRIPT backbone used in re-ranking, Success@10 is 0.1277, meaning ~87% of target proteins have no true partner in the top-10 and are excluded from re-ranking analysis entirely. The paper acknowledges this but does not discuss what fraction of total novel interactions is captured by the top-10 lists, nor whether re-ranking trends would generalize to deeper candidate pools. (Section 4.2, Section 5.3)

7. **No statistical significance or variance reported**. With a large dataset, per-protein metrics could be computed and summarized with confidence intervals or standard deviations. The absence of any variance measure makes it impossible to assess whether the reported differences between methods are reliable. (Table 1, Table 2)

8. **LLM data leakage concern acknowledged but not addressed**. The paper notes that BioBERT and BioMedRoBERTa "are pretrained on large biomedical corpora, [so] it is uncertain if their gains reflect not only semantic generalization but also latent knowledge of interactions from the training data" (lines 266-268). This is a real confound, but the paper does not construct a control (e.g., removing protein names/free-text from profiles, or comparing against a model trained only on structured GO/Pfam terms). The PubMedBERT cross-encoder mitigation (trained on v11 only, evaluated on v12) is reasonable but still leaves the base pretrained model potentially memorizing interaction descriptions. (Section 5.3)

### Trivial

9. Some repeated/awkward phrasing in Section 5.3 (e.g., "Topsy-Turvy achieving the broadest achieves the broadest prediction coverage") — minor presentation issues from the PDF extraction that were likely clean in the original.

## Nice-to-Haves

- Report median rank improvement (not just fraction maintained/improved/worsened) in the re-ranking analysis (Table 2). Since the candidate set is only top-10, even a 1-position shift changes classification; knowing the *magnitude* of shifts would clarify practical significance.
- Include a computational cost comparison of re-ranking methods (Section 4.2) — the paper mentions runtime bottlenecks qualitatively but provides no quantitative comparison.
- Compare against the method itself with different backbones for re-ranking (e.g., Topsy-Turvy instead of D-SCRIPT), given that Topsy-Turvy has better prediction coverage.
- For LLM re-ranking, construct a control condition that removes protein names and free-text descriptions, keeping only structured GO/Pfam/pathway terms.

## Removed Points

- **Criticism about baseline comparison being "fundamentally uninformative"**: The reviewer claims the improvement is "entirely unsurprising" because the method is compared against classifiers. While a full-embedding baseline would strengthen the paper (retained as Major weakness #1), comparing against state-of-the-art PPI classifiers is a standard and informative baseline. The claim that this makes the results "misleading" is too harsh given typical evaluation practice in the field. The criticism about "two orders of magnitude" is retained as a separate weakness.

- **Criticism that the paper doesn't compare against BLAST or k-NN**: This is valid but secondary — the paper's framing is about improving over PPI prediction methods, not generic sequence retrieval. Kept as Minor weakness #5 with weakened framing.

- **Criticism that LLM results "invalidates any claim" about semantic generalization**: Overly strong framing. The paper acknowledges the concern and the PubMedBERT cross-encoder design partially mitigates it (trained on v11, evaluated on v12). Retained as a Minor weakness with appropriate scope.

- **Strength Finder claim about "21× improvement" being a core strength**: While the improvement is real, the missing ablation (Weakness #1) means we cannot attribute it to the claimed mechanism. Retained as a qualified strength about the observed magnitude but not as evidence for the interpretability hypothesis.

- **Strength Finder claim about "honest limitation analysis"**: This is a genuine strength and retained.

## Novel Insights

None beyond the paper's own contributions. The key interesting empirical finding — that PubMedBERT re-ranking consistently improves rankings across nearly all source methods (75-80% maintain-or-improve), while pDockQ structural plausibility actually degrades rankings compared to cosine — is already reported in the paper (Table 2). The reviewers did not surface new patterns beyond what the paper presents.

## Suggestions

1. **Add the critical ablation**: Compare your interpretability-guided retrieval against full-embedding cosine similarity (no activation masking) on the same backbone. This is the single most important experiment to support the paper's core claim.
2. **Investigate the xCAPT5 discrepancy**: Verify that Precision@5=0.1943 and Success@5=0.0059 for xCAPT5 are both correct. If they are, explain how this is possible given the metrics' definitions; if not, correct the table.
3. **Correct the "two orders of magnitude" claim** to match the actual improvement ratios reported (largest ~26×).
4. **Specify the activation threshold** for "highly activated residues" in Section 4.1 to ensure reproducibility.
5. **Report variance** (confidence intervals or standard deviations) for the main retrieval metrics.
6. **Extend the re-ranking analysis** to report median rank improvement (not just fraction) and consider applying it to deeper candidate pools.

## Score and Decision

**Round 1 bracket**: Weak anchors (2.5–3.0) < paper < Strong anchors (8.0). Initial bracket: [3.0, 6.0].

**Anchor comparison**:
- RaftPPI (5.00, ICLR 2026 Poster): PPI retrieval with strong evaluation. The current paper has a more novel problem formulation (temporal evaluation) but weaker empirical support. The current paper is **weaker** than RaftPPI.
- HIPPO (3.50, Withdrawn): Cross-species PPI with presentation issues. Current paper has cleaner presentation and more novel framing. **Stronger** than HIPPO.
- Drug-ProGO (5.00, Reject): Drug screening with GO enhancement. Similar evaluation rigor but more incremental. Current paper has more novel problem framing but similar evaluation gaps. **Comparable or slightly weaker**.
- LiveProteinBench (4.00, Reject): Benchmark for protein LLMs. Current paper has more substantive methodological contribution. **Comparable**.

**Final assessment**: The paper has a genuinely novel problem formulation and interesting framework design. However, the evaluation has significant gaps: the core methodological claim lacks a critical ablation (activation masking vs. full embedding), the xCAPT5 table entries appear internally inconsistent, and the headline "two orders of magnitude" claim is unsupported by the data. These issues prevent the paper from convincingly demonstrating its contributions in its current form.

**Score**: 4.0
**Decision**: Reject

MY FINAL SCORE: <score>4.0</score>
MY FINAL DECISION: <decision>Reject</decision>