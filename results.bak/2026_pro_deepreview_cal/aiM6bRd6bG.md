Now I have sufficient context to produce the final consolidated review. Let me synthesize everything.

---

## Summary

This paper introduces the problem of PPI candidate ranking: given a protein and its known interaction partners, rank novel candidates by their likelihood of interacting with the target. The key methodological contribution is an interpretability-guided ranking framework that uses contact-map activations from D-SCRIPT and Topsy-Turvy to identify active residue regions of known partners, then scores candidates via sliding-window cosine similarity over those regions. A re-ranking module integrates complementary signals (interaction scores, structural pDockQ, semantic overlaps, and LLMs). Evaluation uses a prospective temporal split: STRING v11 as training/known interactions and v12 newly confirmed interactions as the test set (279K additional positives), demonstrating substantial improvements over raw interaction probabilities.

## Strengths

- **Prospective, temporally-split evaluation that directly addresses the discovery bottleneck**: The paper evaluates on the STRING v11→v12 transition, asking whether computational methods can anticipate interactions that will only be experimentally confirmed in the future. This design (Section 4, Equations 1–2; Section 5.1) is a meaningful advance over static retrospective benchmarks and directly targets the experimental prioritization challenge.

- **Interpretability-guided ranking produces dramatic improvements at early ranks**: Using contact-map activations to extract active residue regions and computing embedding similarity over those regions lifts true novel partners substantially. Table 1 shows Recall@10 improving from 1.24% (raw D-SCRIPT interaction probability) to 26.41%, MRR from 0.034 to 0.169, and Success@10 from 0.4% to 12.8%. These are genuine, large-effect improvements that make the rankings practically useful for experimental screening.

- **Rigorous leakage prevention in the re-ranking module**: The cross-encoder fine-tuning uses GroupKFold splits by protein identity (Section 4.2), ensuring no protein appears in both training and validation, with final evaluation on entirely disjoint STRING v12 interactions. This is careful experimental design that eliminates a common failure mode in biological ML.

- **Careful data curation aligned with prior work**: The preprocessing pipeline follows D-SCRIPT/Topsy-Turvy conventions (length 50–800, CD-HIT 40%, 10:1 negative ratio, experimental binding support >0), ensuring the evaluation is on high-confidence physical interactions and comparable to existing benchmarks (Section 5.1).

- **Well-defined problem formulation**: The candidate ranking problem is expressed mathematically with clear notation (Equations 1–5, Figure 1), making the framework reproducible.

## Weaknesses

### Fatal

None.

### Major

- **Overstated quantitative claims**: The introduction states "we improve ranking metrics by two orders of magnitude" and the conclusion says "up to two orders of magnitude." Inspection of Table 1 shows the largest improvement factor is approximately 32× (D-SCRIPT Success@10: 0.004 → 0.128), while most metrics improve by factors of 5–25×. Two orders of magnitude (100×) is not achieved by any reported metric. This mischaracterization damages credibility and should be corrected to reflect the actual (still substantial) gains.

- **Missing ablation for the central mechanism**: The method's key novelty is using contact-map-derived active residue intervals to guide embedding similarity. The paper compares only against scalar interaction probabilities from D-SCRIPT, Topsy-Turvy, and xCAPT5. It does *not* compare against a simpler embedding-similarity baseline using whole-protein (e.g., mean-pooled) embeddings without contact-map guidance. Without this ablation, it is unclear whether the gains stem from (a) moving from scalar probabilities to the richer embedding space, or (b) specifically from the interpretability-guided interval selection. Since the paper's core claim is that exploiting interpretable structure improves ranking, this missing comparison leaves the contribution's origin uncertain. The improvement could plausibly be explained by the embedding space alone.

### Minor

- **Re-ranking evaluation lacks standard retrieval metrics**: The re-ranking module is evaluated only via a pairwise rank-shift matrix (Table 2) tracking how many true positives move up/down within the top-10. Standard metrics (Recall@k, nDCG@k, MRR) after re-ranking are not reported. A method that shifts a true positive from rank 9 to rank 8 improves the pairwise statistic but does not change top-1 or top-5 hit rates — the quantities that matter for candidate screening. Without these metrics, the practical benefit of re-ranking remains incompletely quantified. The pairwise analysis is informative but should be supplemented.

- **Under-specified active-segment extraction procedure**: Section 4.1 describes scanning for "maximal contiguous segments of highly activated residues" and selecting the segment with "the highest average activation score," but no threshold for "highly activated" is given. While the paper states that segment length is data-driven, the absence of a threshold or precise segment-finding algorithm makes the procedure difficult to reproduce exactly as described.

- **Handling of missing xCAPT5 predictions not discussed**: Table 1 shows xCAPT5 has substantially lower prediction coverage (0.8088 vs. 0.9544 for D-SCRIPT), but the paper does not explain how missing predictions were treated in ranking computation, which affects comparability of the xCAPT5 numbers.

### Trivial

- The Table 2 caption is difficult to parse — the roles of † and ‡ are ambiguous and the coloring rule ("more than an half of the fraction that worsened … improved") is confusing.
- The runtime of hundreds of hours is mentioned (Figure 2) but practical scalability implications are not discussed in the main text.

## Nice-to-Haves

- Adding the whole-protein embedding similarity baseline (mean-pooled or max-similarity over full sequences) to isolate the contribution of the contact-map guided interval selection.
- Extending the re-ranking evaluation with Recall@k, nDCG@k, and MRR after each re-ranking strategy.
- Providing the dataset statistics (candidate pool size, number of true positives per protein) explicitly in the main text to help readers interpret absolute magnitudes.
- A more precise specification of the activation-threshold and segment-finding algorithm, including any smoothing or minimum-length constraints.

## Removed Points

*These points are flagged to be removed; treat them with caution.*

- **Harsh critic's claim that the missing ablation makes the paper's results "unsupported"**: REMOVED as a fatal characterization. While the missing ablation is a genuine gap (retained as Major), the comparison against raw interaction probabilities is itself a meaningful and non-trivial baseline. The improvement from 1.24% to 26.41% Recall@10 is substantial regardless of whether the contact-map guidance or the embedding space drives it. The ablation gap weakens the attribution of the gain to interpretability specifically, but does not invalidate the demonstrated improvement.

- **Harsh critic's demand for explicit formulae for activation score and segment selection**: The paper provides a textual description of the procedure. While a formula would improve clarity, the process is described in enough detail to understand the approach. This is a presentation preference, not a weakness.

- **Harsh critic's note about "missing appendix"**: The parser strips appendices; the original submission includes them. REMOVED.

- **Harsh critic's request for handling of missing UniProtKB accession mappings**: This is a minor implementation detail. The paper describes the general approach; exact handling of edge cases is a reproducibility detail beyond what is expected in the main text.

- **Strength Finder's "Formal problem statement" as a standalone strength**: While the problem is well-defined, clear problem statements are a baseline expectation, not a distinguishing contribution. MERGED into the methodology description rather than listed separately.

## Novel Insights

The paper's most novel insight is the observation that raw interaction probabilities from state-of-the-art PPI predictors bury true partners deep in the rankings (average rank ~480), while leveraging the same models' internal embedding activations — specifically, contact-map-guided residue-level similarity — can surface those partners to practically useful ranks. This decoupling of "which residues matter" (from the contact map) from "are these proteins similar" (from embedding similarity) is a conceptually clean way to extract value from interpretable model internals without requiring the model's scalar output to be well-calibrated as a ranking score.

## Suggestions

- Correct the "two orders of magnitude" claim throughout. Report the actual multiplicative factors (e.g., "Recall@10 improves by a factor of ~20, MRR by ~5×") and let the numbers speak for themselves — they are already impressive without inflation.
- Add the whole-protein embedding similarity ablation. This is the single most important experiment to add, as it would directly test whether the contact-map guidance contributes beyond simply using embeddings. Even a preliminary result on a subset would substantially strengthen the paper.
- Report standard retrieval metrics (Recall@k, nDCG@k, MRR) for the re-ranking stage, at minimum for the best-performing method (PubMedBERT cross-encoder), to demonstrate practical improvement in hit rates.
- Clarify the active-segment extraction algorithm, including the activation threshold or how "highly activated" is operationalized.

## Score and Decision

**Calibration summary:**

Round 1 bracketing placed the paper between ~4.5 and ~7.0, based on: weak-band anchors at 3.0–3.4 (fundamentally flawed or thin contributions), middle-band anchors at 4.6–6.0 (solid work with notable limitations), and strong-band anchors at 8.0 (clear accepts with strong evidence).

Round 2 narrowing pulled anchors at 4.6–6.0:
- NovoBench-100K (4.60): protein dataset paper, rejected — this paper is substantially stronger in evaluation design and contribution.
- Illuminating Protein Function (5.25): retrieval-based protein function prediction, rejected for missing baselines and unclear details — this paper is stronger, with a more compelling evaluation setup.
- PEEP (5.60): enzyme promiscuity prediction, rejected for limited novelty — comparable in contribution level but this paper has a more innovative evaluation design.
- MAPE-PPI (5.67): microenvironment-aware PPI prediction, accepted with mixed reviews — comparable; MAPE-PPI has more methodological novelty, this paper has a more compelling evaluation paradigm.
- LLaPA (6.00): LLM for PPI, rejected for data leakage concerns — this paper has cleaner evaluation but weaker methodological novelty.

The paper under review sits in the 5.0–6.0 range. It is stronger than the ~5.0–5.25 anchors due to its genuinely clever prospective evaluation design and large-effect improvements. It is comparable to MAPE-PPI (5.67) and PEEP (5.60). The "two orders of magnitude" overclaim and the missing ablation for the central mechanism keep it from reaching the 6.0+ level. The paper makes a real contribution — the prospective evaluation paradigm and the demonstration that embedding-based ranking dramatically outperforms scalar probabilities — but the missing ablation leaves the attribution of the gain to the contact-map mechanism uncertain, and the overclaim damages trust.

**Score: 5.5**

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>