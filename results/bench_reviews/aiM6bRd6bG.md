Now I have all the information needed. Let me synthesize the final review.

---

## Summary

This paper introduces PPI candidate ranking—the task of prioritizing novel protein-protein interaction candidates for experimental validation—and proposes a two-stage framework. The first stage uses predicted contact maps from D-SCRIPT/Topsy-Turvy to identify "active residues" in known interactors, then ranks candidates by maximum cosine similarity restricted to those residue regions. The second stage re-ranks the top-10 candidates using complementary signals (interaction scores, structural plausibility via SpeedPPI, annotation overlap heuristics, and LLM-based semantic similarity). Evaluation uses a temporal split between STRING v11 (training/known) and v12 (novel interactions as ground truth), showing substantial improvements over raw interaction-probability baselines.

## Strengths

- **Prospective evaluation via temporal split is well-designed.** Using STRING v11→v12 as a forward-looking testbed directly assesses whether methods can anticipate future experimental discoveries, which is stronger than static retrospective benchmarks and maps well to the paper's motivation of guiding experimental validation.

- **Consistent improvement across two backbone models.** The interpretability-guided retrieval yields substantial gains with both D-SCRIPT (e.g., Recall@10 from 1.24% to 26.41%, MRR from 0.034 to 0.169) and Topsy-Turvy embeddings, demonstrating the approach is not tied to a single architecture.

- **Complementary re-ranking signals are thoroughly explored.** The pairwise rank-shift matrix (Table 2) provides clear evidence that semantic and annotation-based signals (PubMedBERT cross-encoder: 75.5% maintain-or-improve rate; lightweight KeyTerm overlap: 69.3%) capture information orthogonal to sequence-based embedding similarity, yielding useful guidance for future refinement strategies.

- **Computationally pragmatic design.** Restricting expensive re-ranking steps (SpeedPPI, cross-encoder inference) to the top-10 candidates per protein keeps the pipeline feasible for large-scale screening.

- **Well-motivated problem.** The framing around prioritizing candidates for costly experimental validation addresses a genuine practical bottleneck in interactome mapping.

## Weaknesses

### Fatal

None.

### Major

- **The core methodological contribution—active-region selection via contact maps—is not isolated by experiment.** The paper compares the proposed method only against raw interaction scores (D-SCRIPT/Topsy-Turvy IS and xCAPT5). It never tests the obvious baseline: ranking candidates by maximum cosine similarity using the *full* embedding of each known partner, without any contact-map-guided residue selection. Without this ablation, one cannot determine whether the ranking improvements in Table 1 are attributable to the contact-map mechanism or simply to the use of embedding-space similarity versus scalar interaction scores. A full-embedding cosine-similarity baseline could plausibly achieve comparable gains, and its absence leaves the central claims about interpretability-guided retrieval unverified. *(This is the single most important weakness and should be the authors' highest priority to address.)*

### Minor

- **Re-ranking evaluation uses only pairwise rank-shifts within the top-10, not end-to-end retrieval metrics.** Table 2 reports what fraction of v12 rediscoveries maintain or improve their rank when switching from one signal to another, but the paper never reports Recall@k, Precision@k, MAP, or MRR for the *combined* pipeline (first-stage + re-ranking). The claim that re-ranking "improves early ranking performance by up to two orders of magnitude" (line 283) conflates the first-stage gains (Table 1) with the re-ranking benefits (Table 2), which are not measured on the same scale. Providing end-to-end metrics for the full pipeline would strengthen the evaluation considerably.

- **"Two orders of magnitude" is a factual overstatement.** The paper states this in the Abstract, Introduction (line 29), and Conclusions (line 283). The actual improvements over D-SCRIPT interaction scores are approximately 5× (MRR), 21× (Recall@10), and 32× (Success@10)—meaningful, but not 100×. Over Topsy-Turvy the factors are smaller still (e.g., Recall@10: ~9.5×). The claim should be corrected to "over an order of magnitude" or replaced with specific ratios. This damages credibility even though the underlying results are genuinely strong.

- **Re-ranking cutoff r=10 is arbitrary and not studied.** The choice to re-rank only the top-10 candidates per protein is pragmatic (due to SpeedPPI's cost), but the paper does not examine how sensitive the re-ranking gains are to this cutoff. Performance likely depends on r, especially since the first stage's Recall@10 is only ~26%, meaning most true partners that could benefit from re-ranking are not even in the re-ranking pool.

- **Cross-encoder softmax prior is questionable.** The inference step applies a within-protein softmax over the candidate set (Eq. 12), which assumes exactly one of the top-10 candidates is the true partner. Proteins can have multiple novel interaction partners in v12, making this normalization inappropriate and potentially distorting the ranking.

- **Sensitivity to the number of known partners is not quantified.** The method fundamentally depends on having known interactors to serve as anchors. Proteins with few known partners (common for understudied proteins) are likely poorly served, yet the paper does not stratify results by |KP(p)|. This limits an understanding of the method's practical scope.

### Trivial

- The definition of "active residues" (contiguous segment with highest average contact probability) is one of several possible strategies (e.g., top-k residues, fixed-size windows). A brief sensitivity analysis would help, though the current design is reasonable.

- The "Prediction Coverage" metric is reported as a single global value without a k-dependent breakdown, making its interpretation alongside the other k-dependent metrics ambiguous.

## Nice-to-Haves

- **Standalone text-based retrieval performance.** The re-ranking module uses TF-IDF, Jaccard, and LLM embeddings as refinement signals within the top-10. Reporting how well these text-based methods perform as primary retrieval over the full candidate set would help readers assess whether the two-stage design adds value, though this is outside the paper's stated scope of evaluating a combined pipeline.

- **Embedding-space visualization.** A t-SNE/UMAP projection of candidate embeddings, annotated by active-residue regions and true-interaction status, could provide intuitive support for why the method works.

- **Contact-map quality upper bound.** Running the method with true contact maps (where available from known complexes) would provide a sanity-check upper bound on what the approach could achieve with perfect contact predictions.

## Removed Points

*These points were flagged by reviewers but are not appropriate to include as weaknesses. Treat them with caution.*

- **"No standalone performance of text- and annotation-based retrieval"** — The re-ranking module is explicitly designed as a refinement step, not as a standalone retrieval method. The paper's contribution is the two-stage framework; requiring each component to be separately validated as a primary retrieval method is scope creep. Moved to Nice-to-Haves.

- **"xCAPT5 inclusion obscures rather than clarifies"** — Including an additional baseline never obscures a comparison. xCAPT5 provides useful context about the state of the field.

- **"Table 2 legend is garbled" / runtime figures not included** — These are parser artifacts from PDF extraction; the original submission does not have these issues. Removed per formatting rules.

- **"PPI candidate ranking as a new problem is inflated — temporal link prediction exists"** — The paper's problem framing (ranking candidates for a target protein using known partners as anchors, with evaluation on prospective database releases) is sufficiently distinct from generic temporal link prediction to warrant treating it as a novel task formulation.

- **"Choice of D-SCRIPT over Topsy-Turvy lacks strong justification"** — The paper explicitly justifies this at lines 241–246: D-SCRIPT emphasizes true partners at top ranks (higher Precision, MAP, nDCG, Success), making it better suited for a pipeline that focuses on early-ranking quality.

- **"Active residues are derived from predicted contact maps, not biological ground truth"** — The paper acknowledges this limitation in the Conclusions (lines 536–539): "the embedding construction process itself remains a black-box representation. As such, we cannot directly ground the predicted interactions in specific, biologically meaningful protein properties." This self-awareness should not be treated as a hidden flaw.

- **"Missing related work on full-embedding similarity baselines"** — Per instructions, we do not flag missing related works that cannot be externally confirmed.

- **"The paper does not address how its rankings would be validated experimentally"** — The paper explicitly states its purpose is to prioritize candidates *for* experimental validation. The STRING v11→v12 temporal split serves as a retrospective proxy for this prospective validation. Demanding actual wet-lab validation is outside the scope of a computational methods paper.

## Novel Insights

The most genuinely novel insight from this work is the empirical demonstration that predicted inter-protein contact maps—originally designed as an intermediate bottleneck for interaction scoring—can be repurposed as a mechanism for identifying which residue regions drive embedding similarity between known and candidate interactors. The fact that focusing cosine similarity on these "active" regions yields 5–20× improvements in early-ranking metrics over raw interaction scores suggests that D-SCRIPT/Topsy-Turvy embeddings contain substantially more retrieval-relevant information than their scalar outputs capture, and that contact maps provide a principled (if imperfect) way to surface it. This has implications beyond the specific models tested: it hints that many sequence-based PPI predictors with interpretable internal structure may be under-exploited as retrieval engines.

## Suggestions

- **Add a full-embedding cosine-similarity baseline.** This is the single most important experiment to add. Simply compute max cosine similarity between the full (non-truncated) embedding of each known partner and each candidate, without any contact-map guidance. Report it alongside the active-region method in Table 1. This will directly isolate the contribution of the contact-map mechanism.

- **Correct the "two orders of magnitude" claim throughout.** Replace with precise factor ranges (e.g., "5× to 20× improvements") or at most "over an order of magnitude."

- **Report end-to-end ranking metrics for the combined pipeline.** Add Recall@k, Precision@k, and MRR for the first-stage + re-ranking combined output, even if only at the top-10 cutoff where re-ranking operates.

- **Stratify results by |KP(p)|.** Show how performance varies with the number of known partners per target protein, which would clarify the method's practical applicability and limitations.

---

## Score and Decision

### Anchor comparison

The following anchor papers were retrieved. I compared the paper under review against each:

| Anchor | Path | Avg Score | Comparison |
|--------|------|-----------|------------|
| RaftPPI | Dp1RM3gPg8.md | 5.00 (Accept Poster) | RaftPPI has a clearer, better-isolated methodological contribution and more complete evaluation (7 datasets, careful splits). The current paper has a more novel problem framing but a weaker core-method ablation. |
| HIPPO | kXpXKe3KnA.md | 3.50 (Withdrawn/Reject) | HIPPO was rejected largely for presentation issues and incremental contribution. The current paper is more polished, has a stronger evaluation setup (temporal split), and comparable novelty. |
| TopoScorer | QNcrdCKNa5.md | 4.00 (Reject) | TopoScorer was rejected for unclear training details and underperforming baselines. The current paper has cleaner methodology and more impressive quantitative gains, but shares the issue of incomplete isolation of its core contribution. |
| Bento | kIxAQxUZHq.md | 5.00 (Reject) | Bento is a benchmark paper with strong execution but limited novelty. The current paper has more methodological novelty but less evaluation completeness. |
| DisProtBench | WAlZ5YD1g7.md | 3.50 (Withdrawn/Reject) | Benchmark paper; less methodologically comparable. |
| LiveProteinBench | ACroNFU7Do.md | 4.00 (Reject) | Benchmark paper; less directly comparable. |
| ColdDTI | xtdPwCp5mi.md | 4.00 (Reject) | Drug-target interaction; different domain but similar multi-stage architecture. |
| HAIPR | 6cHUf3Dnxr.md | 3.50 (Reject) | Affinity prediction; different task. |
| Protap | 7cDfYiqe4X.md | 3.50 (Reject) | Benchmark paper; less comparable. |

The paper under review sits between the 4.0–5.0 range. It is stronger than the 3.5–4.0 rejected papers (HIPPO, TopoScorer, DisProtBench) in terms of evaluation design and clarity, but weaker than the 5.0 accepted-poster RaftPPI in terms of isolating its core methodological contribution. The missing full-embedding baseline is a genuine gap that prevents full verification of the central claim, but the temporal-split evaluation, consistent cross-model improvements, and thorough re-ranking analysis represent real contributions. The "two orders of magnitude" overstatement is a correctable factual error that does not invalidate the underlying results.

MY FINAL SCORE: <pineapple>4.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>