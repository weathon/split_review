Now I have all the information I need. Let me compile the final consolidated review.

---

## Summary

This paper introduces the problem of PPI candidate ranking — prioritizing novel protein-protein interaction candidates for experimental validation — and proposes a two-stage framework. The first stage uses interpretability-guided retrieval: contact maps from D-SCRIPT/Topsy-Turvy identify "active" embedding regions of known interaction partners, and cosine similarity over those regions ranks candidate proteins. The second stage re-ranks top-10 candidates using complementary signals (interaction scores, pDockQ, semantic features, and a PubMedBERT cross-encoder). Evaluation uses STRING v11→v12 as a pseudo-prospective benchmark, showing substantial improvements over raw interaction-probability baselines (e.g., Recall@10 from ~1.2% to ~26% for D-SCRIPT).

## Strengths

- **Well-defined and practically motivated problem formulation.** The paper clearly operationalizes PPI candidate ranking using successive STRING releases, constructing a large-scale pseudo-prospective benchmark with 279,568 novel positives. The problem directly addresses the experimental bottleneck in interactome mapping and is clearly scoped (Section 3, Section 5.1).

- **Substantial quantitative improvements in retrieval.** Table 1 demonstrates large gains over probability-based baselines: for D-SCRIPT, Recall@10 rises from 0.012 to 0.264 (a ~22× improvement) and MRR increases by roughly 6–8×. Topsy-Turvy shows similarly strong gains, and the method generalizes to xCAPT5. These are practically meaningful improvements that would matter for experimental follow-up.

- **Comprehensive comparison across models and re-ranking signals.** The paper evaluates three model backbones (D-SCRIPT, Topsy-Turvy, xCAPT5) revealing useful trade-offs (xCAPT5's high early precision vs. Topsy-Turvy's broader coverage), and integrates six distinct re-ranking signals (IS, pDockQ, TF-IDF, token/location/key-term overlap, BioBERT, BioMedRoBERTa, PubMedBERT) — providing a systematic view of which complementary evidence sources help.

- **Transparent runtime characterization.** Figures 2–3 and Appendix A.2 honestly characterize the computational bottleneck (retrieval dominates at hundreds of hours, SpeedPPI is ~13 min/pair making it prohibitive), offering practical guidance for scaling.

- **Generalization evidence on PiNUI.** Appendix Table 4 shows the method generalizes to a stricter benchmark with different positive/negative definitions, substantially outperforming raw D-SCRIPT probabilities (Rediscovery Ratio 0.3849 vs. 0.0080), suggesting the approach is not overfitted to STRING-specific patterns.

## Weaknesses

### Major

- **Overclaimed quantitative improvements ("two orders of magnitude").** Both the abstract (line 92) and conclusion (line 731) claim ranking metrics improve by "two orders of magnitude" (i.e., ~100×). The actual improvements in Table 1 are roughly 5–26× depending on the metric (e.g., Recall@10 improves ~22×, MRR ~6–8×). These are substantial gains, but they are not two orders of magnitude. This overstatement appears in the paper's most prominent claims and misleads about the practical impact. The authors should correct the language to reflect the actual magnitude (e.g., "one order of magnitude" or specific fold improvements).

- **Re-ranking evaluation uses an insufficient metric.** Re-ranking is evaluated only through pairwise rank-shift analysis within the top-10 candidates (Table 2) — reporting what fraction of interactions maintained or improved their position when switching between re-rankers. No end-to-end retrieval metrics (Recall@k, MAP@k, nDCG@k, MRR) are reported for the re-ranked lists, even on the restricted candidate set. This makes it impossible to judge whether re-ranking actually elevates true positives in a way that would matter to a user. The 75.5% "maintain-or-improve" rate for PubMedBERT, for instance, could mean genuine improvements or merely that already-highly-ranked positives stay near the top. Without standard retrieval metrics, the re-ranking contribution remains unsubstantiated.

- **Missing ablation: does active-region selection add value over whole-embedding similarity?** The core methodological contribution is using contact-map-guided active regions to focus cosine similarity. The paper never compares this against a simple baseline that computes cosine similarity over the entire protein embedding (using the same known-partner anchor strategy). Without this ablation, it is impossible to know whether the reported gains come from the contact-map-guided region selection or simply from the anchor-based retrieval strategy itself. This is the most important missing experiment.

### Minor

- **LLM memorization concern is acknowledged but unaddressed.** The paper correctly notes (Section 5.3) that PubMedBERT's gains "may reflect not only semantic generalization but also latent knowledge of interactions from the training data." The training data (STRING v11) and test data (STRING v12) could share interactions described in PubMed, creating potential data leakage through the LLM's pretraining corpus. No control experiment is performed (e.g., restricting to pairs without explicit interaction mentions in text). The paper's own hedging limits how strongly the LLM re-ranking results can be interpreted, but this does not invalidate the non-LLM re-ranking signals or the retrieval results.

- **STRING v11→v12 as a prospective benchmark has limitations.** Interactions that appear in STRING v12 but not v11 may have been known in the literature or other databases before v11's release; delayed integration into STRING does not guarantee genuine novelty. This is a limitation of any retrospective pseudo-prospective benchmark, and the paper does not discuss or characterize it. The PiNUI evaluation partially mitigates this concern, but a brief discussion of what fraction of v12 additions were "truly new" would strengthen the paper.

- **The active-region algorithm lacks precision.** Section 4.1 describes identifying "maximal contiguous segments of highly activated residues" and selecting the one with "highest average activation," but the threshold for "highly activated" is never specified, nor is the procedure for scanning activation profiles formalized. This hurts reproducibility of the core method.

### Trivial

- Equation (7) for pDockQ is garbled in the extracted text and appears to mix pDockQ with a description meant for functional enrichment. This is a PDF-parsing artifact but makes the structural plausibility section hard to follow in the current rendering.

## Nice-to-Haves

- Extending the re-ranking evaluation to report standard retrieval metrics (Recall@k, MRR, nDCG@k) for the re-ranked lists would substantially strengthen the re-ranking claims.
- A control for LLM memorization (e.g., evaluating on protein pairs whose text annotations contain no explicit interaction-partner mentions) would make the LLM re-ranking results more trustworthy.
- Biological validation of active regions against known binding-site databases (PDB, PPIsite) would strengthen the interpretability claim.
- A staged re-ranking approach (re-rank top-100, then top-20) could be evaluated to explore the efficiency–quality trade-off beyond the current top-10 restriction.

## Removed Points

These points are flagged to be removed, treat them with caution:

- **"SpeedPPI takes ~13 minutes per pair... could be feasible only on top-3 candidates" (from Harsh Critic, re-ranking runtime):** The paper already discusses this limitation in Appendix A.2 and acknowledges SpeedPPI is "prohibitive" for adoption. The critic's suggestion is reasonable but the paper already covers this ground.

- **"Table 1 is confusingly formatted" (from Harsh Critic):** This is a parser artifact. The original PDF table is likely well-formatted; the garbled rendering in the extracted text is not an author error.

- **"pDockQ definition is garbled (equation 7 is unparseable)" (from Harsh Critic):** This is a PDF-parsing artifact. The equation is likely correctly rendered in the original submission.

- **"Filtering interactions with experimental support >0 conflates low-confidence direct binding with indirect evidence" (from Harsh Critic):** The paper explicitly retains only binding interactions with experimental support >0, discarding indirect association channels (co-expression, homology, text mining). The STRING experimental channel reflects actual biochemical evidence and is a reasonable filter for physical interactions.

- **Criticism about "missing comparison with alternative similarity-based retrieval on whole embeddings without contact-map guidance":** The harsh critic claims this should have been a baseline, but the paper's method is explicitly the contact-map-guided approach. This is better categorized as a missing ablation (listed above) rather than an unfair comparison.

- **"LLM-based re-ranking is likely contaminated by memorized interaction knowledge" as a fatal criticism:** The paper itself acknowledges this limitation ("it is uncertain if their gains reflect not only semantic generalization but also latent knowledge of interactions"). This is an acknowledged limitation, not an undisclosed flaw.

- **Strength Finder generic strengths (e.g., "this paper addresses an important problem"):** Removed as generic/superficial.

- **"The paper does not justify why using the interpretability of D-SCRIPT/Topsy-Turvy is the natural choice" (from Harsh Critic, Introduction):** The paper provides a clear motivation in the Introduction: "The underlying idea is that novel interactions of a target protein should follow similar mechanisms to already observed interactions." This is a reasonable argument.

- **"The transition from PPI candidate ranking to exploiting interpretable structure is somewhat forced" (from Harsh Critic):** This is a subjective stylistic judgment, not a substantive weakness.

## Novel Insights

The paper's most interesting finding is that using contact-map-guided active embedding regions for similarity-based retrieval substantially outperforms using the model's own interaction probability scores. This is counterintuitive: the same model (D-SCRIPT) that is explicitly trained to predict interaction probabilities produces a worse ranking than a post-hoc analysis of its internal embedding activations guided by its own contact maps. This suggests that the interaction probability score conflates signals in ways that dilute its ranking quality, while the embedding-space geometry better preserves discriminative information about interaction mechanisms. This insight has implications beyond PPI prediction for how we evaluate and use interpretable deep learning models in biology.

## Suggestions

- Replace "two orders of magnitude" throughout with accurate quantitative language (e.g., "over an order of magnitude," or specific fold improvements by metric).
- Add the whole-embedding cosine similarity baseline as an ablation. This is the single most important experiment to include and would take minimal additional computation (reuse the same embeddings without the contact-map restriction).
- For the re-ranking evaluation, report at minimum Recall@k and MRR on the re-ranked top-10 lists, so readers can assess whether re-ranking actually improves retrieval quality.
- Specify the threshold or procedure for identifying "highly activated" residues in Section 4.1 to improve reproducibility.
- Add a brief discussion of the STRING v11→v12 benchmark's limitations as a prospective test, including what is known about the novelty of v12 additions.

## Score and Decision

### Anchor Comparison

| Anchor Paper | Path | Avg Score | Comparison to Paper Under Review |
|---|---|---|---|
| RaftPPI (Fast Proteome-Scale PPI Retrieval) | Dp1RM3gPg8.md | 5.00 (Accept Poster) | Similar PPI domain; RaftPPI has a clear algorithmic contribution (factorization for speed) with rigorous evaluation. Our paper is more of an engineering framework combining existing methods; the evaluation is less complete. Weaker. |
| PepBenchmark | NskQgtSdll.md | 6.00 (Accept Poster) | A benchmark paper with comprehensive curation. Different contribution type; PepBenchmark's execution is more thorough. Our paper is clearly weaker. |
| HIPPO (Cross-Species PPI) | kXpXKe3KnA.md | 3.50 (Reject) | PPI prediction with novel contrastive approach. Rejected for presentation issues and limited novelty. Our paper has better presentation and larger empirical gains but similar "incremental combination of existing techniques" concern and more evaluation gaps. Comparable quality, possibly slightly better. |
| LiveProteinBench | ACroNFU7Do.md | 4.00 (Reject) | Contamination-free benchmark. Rejected for limited innovation and dataset issues. Our paper has more substantive empirical results but also overclaims. Comparable. |
| DisProtBench | WAlZ5YD1g7.md | 3.50 (Reject) | Structure prediction benchmark. Rejected for presentation and limited analysis. Our paper is stronger — it proposes a method, not just a benchmark, and has clearer empirical contributions. |
| Protap | 7cDfYiqe4X.md | 3.50 (Reject) | Benchmark with significant methodological flaws (data leakage). Our paper's flaws are less severe. Our paper is stronger. |
| TCR-EML | 0QPXvKE4SV.md | 3.60 (Reject) | Explainable layers for TCR-pMHC. Mixed reviews. Our paper has similar issues (acknowledged but unaddressed limitations) but larger-scale evaluation. Comparable. |
| Interpretability vs Performance (CATH) | 2wshkCgNYk.md | 3.00 (Reject) | Single-task study with limited scope. Our paper is clearly stronger in scope and contribution. |

The paper under review makes a genuine contribution — the PPI candidate ranking formulation is practically valuable, and the retrieval results are genuinely strong (20×+ improvements over baselines). However, the paper is weakened by: (1) overclaiming in the abstract and conclusion, (2) insufficient re-ranking evaluation, and (3) a missing ablation that would distinguish the contribution of the core methodological idea. These are not fatal flaws — the retrieval results remain valid and useful — but they prevent the paper from rising to the level of the accepted poster papers in this corpus. The paper sits between the 3.50 reject cluster and the 5.00 accept-poster level. I place it at 4.0: reject but with value that could be realized through revisions addressing the evaluation gaps.

MY FINAL SCORE: <pineapple>4.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>