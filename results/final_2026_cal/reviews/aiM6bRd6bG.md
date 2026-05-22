Now I'm ready to write the final consolidated review.

## Summary

This paper introduces the problem of PPI candidate ranking — prioritizing novel interaction candidates for experimental validation — and proposes a two-stage framework. First, "interpretability-guided retrieval" uses predicted contact maps from D-SCRIPT/Topsy-Turvy to identify active residue regions in known interaction partners, then ranks candidates by cosine similarity between those active regions and sliding windows in candidate sequences. Second, a re-ranking module integrates interaction scores, structural plausibility (pDockQ), functional annotations, and LLM-based semantic similarity. The evaluation uses a prospective setup: known interactions from STRING v11, novel interactions from STRING v12 as ground truth.

## Strengths

- **Prospective evaluation with successive STRING releases is genuinely novel and well-executed.** Constructing the test set from interactions that appear only in STRING v12 (not v11) directly addresses a documented limitation of retrospective PPI benchmarks. The filtering pipeline (binding-only interactions, CD-HIT at 40%, length filtering) is careful, yielding 279,568 novel positive pairs. This design provides credible evidence of practical utility for guiding experimental validation.

- **Substantial improvements over raw prediction scores.** The interpretability-guided retrieval with D-SCRIPT raises Recall@10 from 0.0124 to 0.2641 (~21×) and MRR from 0.0340 to 0.1685 (~5×) relative to direct interaction probabilities. At k=500, Success@k reaches ~60% — nearly 60% of query proteins have a novel partner in the top 500. These are practically meaningful gains even accounting for the missing ablation (see below).

- **Systematic comparison of ten re-ranking signals on a shared prospective set (Table 2).** Comprehensive analysis showing which signals are complementary — PubMedBERT cross-encoder maintains/improves 75.5% of rediscoveries vs. the baseline cosine ranking, and even simple heuristics like KeyTerm Jaccard achieve 75.2% vs. token overlap. This provides useful guidance for practitioners.

- **Large-scale, carefully filtered dataset is a resource for the community.** The preprocessing protocol (experimental support > 0, CD-HIT at 40%, 10:1 negative ratio) is rigorous and reproducible.

## Weaknesses

### Major

1. **Missing ablation: the central claim that "interpretability-guided active-region selection" drives the improvement is not validated.** The method uses two things simultaneously: (a) known partners as anchors, and (b) active residues extracted from contact maps. The baseline (raw interaction probability) uses neither. The paper provides no control that uses known partners as anchors *without* active-residue selection — e.g., ranking candidates by maximum cosine similarity between any known partner's *full embedding* and the candidate's full embedding. Without this ablation, the reader cannot tell whether the dramatic gains come from (a), (b), or both. If full-embedding anchor-based ranking already captures most of the improvement, the core methodological contribution (the "interpretability-guided" component via contact maps) is not supported. This is not a speculative concern — it is a structural omission that prevents attribution of the paper's key results to its claimed technical innovation.

2. **The "two orders of magnitude" claim is inaccurate.** The abstract states "we improve ranking metrics by two orders of magnitude" and the conclusion says "up to two orders of magnitude." The largest improvement in Table 1 is ~26× (MAP@5: 0.2714 vs. 0.0103; Recall@5: 0.1832 vs. 0.0071). This is roughly 1.4 orders of magnitude, not 2 (which would require ≥100×). Other metrics like MRR improve only ~5×. This is a clear overstatement that should be corrected regardless of whether the missing ablation is addressed.

### Minor

3. **The active-residue extraction procedure is underspecified.** The method scans the activation profile and identifies "maximal contiguous segments of highly activated residues" but provides no threshold for "highly activated." The paper selects the segment with the highest average score, but it does not specify how segments are initially delineated (e.g., activation > 0.5? > 0.9? any rising above background?). This makes the method difficult to reproduce precisely.

4. **Sliding-window similarity assumes contiguous binding interfaces.** Equation 3 searches for a contiguous window in the candidate that best matches the active region of the known partner. Many protein-protein binding interfaces are discontinuous in sequence. The paper does not discuss this assumption, validate selected windows against known interface annotations, or acknowledge cases where this assumption might fail.

5. **Re-ranking contribution is not quantified end-to-end.** Table 2 reports pairwise rank-shift fractions within top-10 candidates, but these lists are already heavily shaped by the initial retrieval step. The paper should report end-to-end ranking metrics (e.g., Recall@k, MRR) with and without each re-ranking component to show whether re-ranking actually changes practical outcomes. The modest improvement rates (e.g., PubMedBERT maintains/improves 75.5% but worsens 40.9% relative to cosine) leave the practical value of re-ranking unclear.

6. **Annotation temporal alignment is not controlled.** The PubMedBERT cross-encoder and semantic scores use current UniProt/Swiss-Prot annotations (GO terms, domains, pathways). These annotations may reflect knowledge added after STRING v11, potentially giving the re-ranker information not available at the time the predictions would have been made. While this does not directly leak v12 interaction labels, it affects the reproducibility of the claimed setup if a practitioner wanted to run the pipeline using only v11-era data.

### Trivial

- Table 2 caption has incomplete formatting: the "‡" symbol is defined but the text is cut off (parser issue).

## Nice-to-Haves

- Validate selected active regions against known binding interfaces (e.g., PDB complexes, 3did) to check biological plausibility.
- Report performance stratified by number of known partners per target protein to quantify limitations for under-explored proteins.
- Add confidence intervals or bootstrapped variances to Table 1.
- End-to-end ablation showing contribution of each pipeline stage (raw IS → full-embedding anchor → active-residue anchor → +re-ranking).

## Removed Points

- **"Foundation model cited may not exist" type critique**: Not applicable — no cited entity is questioned.
- **"Formatting nitpicks"**: The "†/‡" caption issue is a PDF extraction artifact, not an author error.
- **"Reproducibility about missing code/hyperparameters"**: The paper references Appendix A.1 for details; appendix content is stripped by the parser.
- **"Fatal temporal leakage" claim**: The critic's concern about annotation-based leakage is plausible but speculative — the paper uses STRING v11 labels, and the critic provides no concrete example of a co-updated annotation leaking a v12 interaction. Demoted from Major to Minor.
- **"pDockQ underperforms, xCAPT5 discussion lacking"**: The paper does discuss xCAPT5's precision/decay trade-off (Section 5.3) and pDockQ's suitability for filtering rather than ordering. These are acknowledged in the text.
- **Strength Finder's generic strengths**: Removed generic praise ("important problem," "timely topic") — only concrete, paper-specific strengths are retained.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. **Add the critical ablation** — rank candidates using maximum cosine similarity between full (non-active) embeddings of known partners and full embeddings of candidates. This separates the anchor-based contribution from the active-residue contribution.
2. **Correct the "two orders of magnitude" claim** to the actual best improvement factor (~26×) and report it transparently as "up to 26× improvement on early-precision metrics."
3. **Specify the threshold** used for "highly activated" residues in the active-region extraction.
4. **Add end-to-end metrics** showing the cumulative contribution of the interpretability-guided step and the re-ranking step separately (e.g., raw IS → anchor+full-embedding → anchor+active-residue → +re-ranking).
5. **Validate a sample of selected active regions** against known binding site annotations to address the contiguity assumption concern.

---

## Calibration Report

**Round 1 (bracketing):** Searched three bands for topically similar papers:
- Low band (<3.5): anchors on protein function prediction, antibody conversion scored 1.3–3.0 — our paper is clearly stronger.
- Mid band (3.5–7.5): RaftPPI (5.0, Accept Poster), ColdDTI (4.0, Reject), LiveProteinBench (4.0, Reject), Drug-ProGO (5.0, Reject) — our paper is comparable but has a more significant validation gap.
- High band (>7.5): no topically related papers found.

**Initial bracket:** (4.0, 6.0)

**Round 2 (narrowing):** Searched inside (4.0, 6.0) for PPI retrieval/ranking papers and (3.0, 5.0) for STRING/temporal evaluation papers. Read RaftPPI (5.0, scores 4/6/4/6), TCR-pMHC interpretability (5.5, scores 6/6/6/4), Drug-ProGO (5.0, scores 4/4/6/6), and ColdDTI (4.0, scores 2/6/4/4) in full.

**Comparison to RaftPPI (5.0, Accept Poster):** RaftPPI also had limited novelty (clever integration of existing techniques) but its core computational contribution was directly validated by runtime measurements. Our paper has a larger validation gap because the central design choice (active-residue vs. full-embedding) is not ablated. Our paper is stronger on evaluation design (prospective STRING split) and breadth of analysis (re-ranking comparison), but the missing ablation is a more fundamental concern. Score: **4.5** — weaker than RaftPPI.

**Comparison to ColdDTI (4.0, Reject):** ColdDTI was critiqued for missing recent baselines and insufficient novelty. Our paper has a clearer problem formulation and stronger evaluation setup, making it somewhat better. Score above 4.0.

**All anchors considered:** Dp1RM3gPg8 (RaftPPI, 5.0, Round 1&2), xtdPwCp5mi (ColdDTI, 4.0, Round 1), ACroNFU7Do (LiveProteinBench, 4.0, Round 1&2), fz1Gnrv9Wx (Drug-ProGO, 5.0, Round 2), S3kSOFhs5m (TCR-pMHC interpretability, 5.5, Round 2), uS5rA4fDJp (RankFlow, 4.0, Round 2), KjyQhJUobQ (3.0, Round 1), JwWaFaH86M (1.33, Round 1), 2wshkCgNYk (3.0, Round 1), DdGCjvrFs0 (2.5, Round 1).

MY FINAL SCORE: <score>4.5</score>
MY FINAL DECISION: <decision>Reject</decision>