## Summary

This paper introduces PPI candidate ranking—given a target protein and its known interactors, rank novel candidate proteins by likelihood of interaction—using a two-stage framework: (1) interpretability-guided retrieval that identifies active residue regions via predicted contact maps from D-SCRIPT/Topsy-Turvy and ranks candidates by cosine similarity of these active embedding regions; (2) a re-ranking module incorporating interaction scores, structural plausibility (pDockQ), semantic annotations, and LLM-based features applied to top-10 candidates. Evaluation is conducted prospectively using the STRING v11→v12 transition, with ~279,568 newly appearing v12 interactions as ground truth.

## Strengths

- **Prospective temporal evaluation design**: Rather than standard random train-test splits within a single database release, the paper trains on STRING v11 interactions and tests on genuinely novel interactions appearing in v12 (Section 5.1). This directly tests whether methods can anticipate future experimental discoveries—far more aligned with real-world utility than retrospective evaluation. The evaluation covers 279,568 newly confirmed v12 interactions.

- **Substantial improvements in early-rank retrieval**: Table 1 shows that exploiting active embedding regions dramatically reshapes rankings versus raw model probabilities. For D-SCRIPT: Recall@10 rises from 1.24% to 26.41% (~21×), MRR from 0.034 to 0.1685 (~5×). For Topsy-Turvy: Recall@10 jumps from 0.117% to 11.06% (~95×). These gains directly support the central claim that raw interaction probabilities are suboptimal for candidate ranking.

- **Insightful multi-signal re-ranking analysis**: Table 2's pairwise rank-shift analysis across 10 re-ranking signals reveals that lightweight semantic features (PubMedBERT: 75.5% maintain-or-improve rate, KeyTerm Jaccard: 69.3%) outperform the structurally expensive pDockQ (47.2%). This is a practically important finding for the field, suggesting annotation-based signals are more effective than computationally intensive docking for refining candidate lists.

- **Leakage-aware experimental protocol**: The cross-encoder uses GroupKFold split by protein identity so no protein appears in both training and validation (Section 4.2), and all final evaluation uses STRING v12 interactions entirely disjoint from v11 training data.

- **Comprehensive evaluation**: Table 1 reports eight standard ranking metrics at six cutoffs (k ∈ {5, 10, 50, 100, 200, 500}) against three baselines (D-SCRIPT, Topsy-Turvy, xCAPT5) with two backbone variants, and Table 2 provides a full 10×10 pairwise comparison matrix.

- **Honest limitation acknowledgment**: Section 6 explicitly identifies key limitations: the method relies on known partners and degrades for underexplored proteins, and the embeddings remain a black box despite leveraging interpretability structurally.

## Weaknesses

### Fatal
None

### Major

- **Overstated "two orders of magnitude" claim**: The paper claims improvements of "two orders of magnitude" in both the abstract (line 25: "we improve ranking metrics by two orders of magnitude") and conclusion (lines 278–279: "improving early ranking performance by up to two orders of magnitude"). From Table 1, the most favorable comparison is Topsy-Turvy Recall@10: 0.00117→0.1106 (~95×, ≈1.98 orders of magnitude). D-SCRIPT Recall@10 shows ~21× (~1.3 orders of magnitude) and D-SCRIPT MRR shows ~5× (~0.7 orders of magnitude). Two orders of magnitude requires ≥100×; the claim is not achieved for any metric/baseline combination. Since the paper's value is primarily empirical, the headline improvement magnitude must be reported accurately.

- **Missing ablation isolating the active-region mechanism**: The baselines in Table 1 (D-SCRIPT, Topsy-Turvy, xCAPT5 prediction probabilities) rank all candidates purely by predicted interaction probability without access to known partners KP(p), while the proposed method conditions explicitly on known partners. Without an ablation—e.g., (a) averaging embeddings of all known partners without contact-map filtering, (b) random contiguous windows of known partners' embeddings, (c) full-sequence similarity to known partners—it is impossible to determine how much improvement is attributable to the specific active-region selection mechanism versus the general benefit of conditioning on known partners. This is the paper's core contribution distinction and must be demonstrated.

### Minor

- **No combined re-ranking results despite integration claims**: Section 4.2 describes multiple re-ranking signals evaluated individually in Table 2. The paper claims to "integrate complementary sources of evidence" (abstract) and proposes a "refinement step" incorporating "additional signals, including interaction scores, structure-derived features, and semantic or language-model-based evidence" (line 23), but never demonstrates combined re-ranking. Without combining top-performing signals (e.g., PubMedBERT + IS + KeyTerm via rank fusion), it is impossible to assess whether signals are truly complementary or largely redundant—central to the re-ranking module's stated value.

- **IS definition inconsistency**: Section 3 (line 55) describes IS as resulting from "Convolutional and pooling operations [that] identify consistent local contact patterns... Finally, a logistic activation compresses these features into a single scalar interaction probability." Equation 6 (line 113) defines IS simply as max_{i,j} C(p,p_c)_{ij}—the raw maximum of the contact map. These are different computations. The paper should reconcile them.

### Trivial

- **Projected dimensionality not stated**: Section 3 describes a projection module (linear layer + ReLU + dropout) reducing dimensionality from d=6165 but never states the output dimensionality, which affects interpretation of cosine similarity computations in Section 4.1.

## Nice-to-Haves

- Report the fraction of true novel partners appearing in the top-10 of the initial retrieval ("recall at 10 of the first stage") to clarify the ceiling for re-ranking effectiveness.
- Add per-protein distributional analysis (e.g., histogram of per-protein MRR or breakdown by number of known partners) to assess whether improvements are concentrated among well-studied proteins.
- Report base rate of positives among candidates to allow readers to calibrate precision figures (e.g., "13% at rank 10").

## Removed Points
These points are flagged to be removed; treat them with caution.

- **"LLM-based re-ranking potentially contaminated by pretraining data"**: The harsh critic flagged potential data leakage from PubMedBERT's pretraining on PubMed abstracts. However, the paper honestly acknowledges this concern (lines 262–264) and the cross-encoder is trained with GroupKFold by protein identity on v11 with evaluation on entirely disjoint v12 interactions. The concern is speculative and unquantified.

- **"Missing evaluation statistics (confidence intervals, significance tests)"**: While distributional information would strengthen the paper, single-run evaluation on a 279K-interaction prospective set is standard for large-scale benchmarks in computational biology. This is a nice-to-have, not a core flaw.

- **"Re-ranking operates on only top-10 candidates"**: This is an explicit design choice stated in the paper (line 109: "due to the heavy processing of some of the techniques"), and the k=10 cutoff is within the evaluation metrics of Table 1. Not a flaw.

- **"The 'interpretability-guided' framing is misleading"**: The paper explicitly addresses this at line 21 ("we do not frame interpretability here as a means to generate explanations for users; rather, we leverage interpretable model structures as a methodological device"). The naming is justified by this clarification.

- **"Garbled text and editing artifacts"**: Multiple references to formatting issues (line 53, line 89, lines 169-170). These are parser artifacts, not paper problems.

## Novel Insights

The paper's most genuinely novel contribution is the framing of PPI candidate ranking as a prospective task evaluated through database version transitions (STRING v11→v12), rather than the more common retrospective evaluation within a single release. This evaluation paradigm directly tests the ability to anticipate future discoveries and is underexplored in the PPI prediction literature. The finding that lightweight semantic features (PubMedBERT, KeyTerm Jaccard) outperform expensive structure-based signals (pDockQ via AlphaFold2/SpeedPPI) for re-ranking is a practically important observation for the field.

## Suggestions

- Add an ablation comparing active-region similarity against simpler known-partner baselines (e.g., full-sequence embedding averaging without contact-map filtering) to isolate the contact-map mechanism's contribution.
- Show combined re-ranking with the top-2 or top-3 signals (e.g., PubMedBERT + IS + KeyTerm) using even a simple rank-fusion approach.
- Correct the "two orders of magnitude" claim to "up to ~25×" or specify which metric/cutoff the largest improvement applies to.
- Clarify the IS definition to reconcile Section 3 (convolutional pipeline + logistic activation) with Equation 6 (max of contact map).

## Calibration Report

**Round 1 anchors retrieved:**
| Path | Avg Score | Round | Comparison |
|------|-----------|-------|------------|
| 8QTpYC4smR | 1.00 | R1 | Unrelated LLM survey — much weaker |
| nSDOkm0SKo | 1.00 | R1 | Unrelated finance paper — much weaker |
| gwZ90hFSL2 | 1.00 | R1 | Unrelated NLP paper — much weaker |
| 5kMwiMnUip | 1.40 | R1 | Unrelated jailbreaking paper — much weaker |
| IEZjjDX0iC | 3.00 | R1 | PPI pLM comparison — weaker, no novel method |
| N4lUNwEn1c | 3.00 | R1 | Chemical property prediction — weaker |
| 1JgWwOW3EN | 2.50 | R1 | MRL benchmarking platform — weaker |
| jqx5XI4Yr3 | 3.40 | R1 | Protein adapter — weaker contribution |
| uKB4cFNQFg | 5.00 | R1 | BEND benchmark — similar scope but weaker |
| wCwz1F8qY8 | 5.00 | R1 | PPI contacts (DeepSSInter) — incremental, weaker |
| Et0SIGDpP5 | 4.25 | R1 | Protein LM — weaker |
| 8O9HLDrmtq | 5.00 | R1 | Genomics benchmark — comparable |
| eh1fL0zw8o | 6.00 | R1 | LLaPA PPI prediction — closest anchor, reject at 6.0 |
| opv67PpqLS | 5.67 | R1 | DNALONGBENCH — comparable scope |
| itGkF993gz | 5.67 | R1 | MAPE-PPI — accept at 5.67, comparable quality |
| C81bqFCmMf | 5.75 | R1 | COMET multi-omics benchmark — comparable |
| iOltCu4TPS | 5.00 | R1 | Single-cell retrieval benchmark — weaker |
| jsQPjIaNNh | 5.25 | R1 | ProtIR protein function — similar issues |
| ZkpDdCQUC4 | 4.60 | R1 | NovoBench protein ranking — weaker |
| GDDqq0w6rs | 4.75 | R1 | Gene properties benchmark — weaker |
| nWO75tVjfp | 3.00 | R1 | Molecular docking assessment — weaker |
| 1S8ndwxMts | 3.00 | R1 | Protein generative metrics — weaker |
| n4SLaq5GhM | 3.25 | R1 | Medical NLP — weaker |
| zMPHKOmQNb | 8.00 | R1 | Discrete Walk-Jump Sampling — much stronger |
| jOmk0uS1hl | 8.00 | R1 | Training on test task — much stronger |
| XmProj9cPs | 8.00 | R1 | Spider 2.0 — much stronger |
| tyEyYT267x | 8.00 | R1 | SAR diffusion LMs — much stronger |
| A3YUPeJTNR | 8.00 | R1 | Hidden cost of predictions — much stronger |
| ja4rpheN2n | 8.00 | R1 | GeSubNet — much stronger |
| uQnvYP7yX9 | 6.50 | R1 | ReNovo (retrieval proteomics) — accept at 6.5, comparable |
| JbOsMrwjZ3 | 6.25 | R1 | BioCoder — reject at 6.25, comparable |
| 760br3YEtY | 5.60 | R1 | PEEP enzyme promiscuity — comparable |

**Round 1 bracket: 5.5–6.5.** The paper is clearly above the reject cluster (5.0-5.25) given its stronger empirical design, larger improvements, and more comprehensive evaluation. It's comparable to LLaPA (6.0, Reject) which had fairness and baseline issues similar to our missing ablation, and MAPE-PPI (5.67, Accept) which had strong method but high reviewer variance. The paper's prospective evaluation design and large gains place it at the top of this range, but the overclaimed headline and missing ablation keep it below 7.0 where papers have resolved all major concerns.

**Final score: 6.0** — The paper offers a genuinely useful problem formulation with a rigorous prospective evaluation paradigm and shows large improvements, but the "two orders of magnitude" overstatement and missing ablation (which is critical to isolating the core contribution) prevent it from scoring higher. Comparable to LLaPA (6.0) with better empirical results but similar structural gaps.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>