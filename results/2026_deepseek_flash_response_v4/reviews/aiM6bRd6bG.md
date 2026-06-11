Now let me write the final review with all anchors reported and the score calibrated.

## Summary

This paper introduces the problem of PPI candidate ranking — prioritizing novel interaction candidates for a target protein given its known partners — and proposes a two-stage framework. First, it uses D-SCRIPT or Topsy-Turvy's predicted contact maps to identify active residue regions on known interactors, then computes cosine similarity restricted to those regions between candidates and known partners. Second, the top-10 candidates are re-ranked using up to ten additional signals (interaction scores, structural plausibility via pDockQ, functional annotations, LLM-based semantic similarity). The evaluation uses a prospective design: known interactions from STRING v11 serve as anchors, and 279,568 novel interactions appearing only in STRING v12 are the ground truth.

## Strengths

- **Prospective evaluation design using successive STRING releases (v11→v12)**: The paper identifies that existing PPI benchmarks are "largely static and retrospective" and addresses this by constructing a testbed where known interactions from STRING v11 define the retrieval basis and novel interactions appearing only in STRING v12 serve as ground truth (Section 5.1). This setup directly tests whether a method can anticipate future experimental discoveries, which is more practically relevant than within-release evaluation.

- **Substantial empirical gains over raw prediction scores**: Table 1 shows that the interpretability-guided retrieval dramatically improves ranking metrics relative to raw D-SCRIPT/Topsy-Turvy probabilities. For D-SCRIPT, Recall@10 rises from 0.0124 to 0.2641 (~21×), Precision@5 from 0.0080 to 0.1924 (~24×), and MRR from 0.0340 to 0.1685 (~5×). These are practically meaningful improvements for experimental screening.

- **Comprehensive pairwise rank-shift analysis across 10 evidence sources**: Table 2 systematically compares cosine, IS, pDockQ, TF-IDF, token/location/key-term Jaccard, BioBERT, BioMedRoBERTa, and PubMedBERT, showing which signals are complementary (PubMedBERT improves or maintains 75–80% of rediscoveries) and which are not (pDockQ underperforms for direct ordering at 47.2%). This provides actionable insight for practitioners designing multi-source prioritization pipelines.

- **Large-scale evaluation with rigorous preprocessing**: The dataset is built from 279,568 novel interactions in STRING v12, with CD-HIT clustering at 40% identity, length filtering (50–800 residues), and a 10:1 negative-to-positive ratio (Section 5.1). At this scale, the retrieval improvements are substantial and unlikely to be artifacts of small-sample evaluation.

## Weaknesses

### Fatal

None.

### Major

- **Exaggerated "two orders of magnitude" claim (lines 25, 279)**: The paper states it "improve[s] ranking metrics by two orders of magnitude" and "improving early ranking performance by up to two orders of magnitude over existing models." Two orders of magnitude = 100× improvement. The best improvements in Table 1 are Recall@5 (~26× for D-SCRIPT) and other metrics in the 5–26× range. These are substantial and practically meaningful, but the claim is inflated relative to what the data supports. The improvements should be stated plainly and accurately.

- **Missing ablation isolating the contact-map-guided component**: The proposed retrieval method combines two elements: (a) using known partners as anchors, and (b) restricting similarity computation to active residues identified from contact maps. There is no ablation comparing the proposed active-region similarity against full-embedding similarity that also uses known partners as anchors (i.e., computing cosine similarity between full embeddings of candidates and known partners, without the contact-map-guided selection). Without this, it is impossible to determine whether the improvement comes from the interpretability-guided active-residue selection (the paper's claimed contribution) or simply from the fact that known partners provide useful signal. This is the most critical missing experiment.

### Minor

- **No confidence intervals or variance estimates**: All results in Table 1 are point estimates with no indication of variance across proteins. Bootstrap confidence intervals or per-protein statistics would substantially strengthen the evidence.

- **Active-region selection assumes contiguous binding interfaces (Section 4.1)**: The method selects a single contiguous segment with the highest average activation. But protein binding interfaces are often discontiguous — residues involved in binding can be spread across the sequence. The method would miss signal from secondary interaction regions. This is a design limitation worth discussing.

- **"Prediction Coverage" metric definition is inconsistent**: The prose (line 223) defines it as "Total number of true novel partners that are successfully retrieved," which should be a count, but Table 1 reports values like 0.9544, suggesting it is actually a fraction. The definition and reporting should be aligned.

- **Re-ranking evaluation limited to top-10 candidates (Section 4.2)**: The re-ranking analysis only considers r=10 candidates per target protein, covering a narrow slice of the problem. The paper does not discuss how this threshold affects conclusions.

### Trivial

None.

## Nice-to-Haves

- Analysis stratified by the number of known interactors per protein would illuminate the method's failure regime for under-studied proteins.
- A simple baseline that ranks candidates by maximum D-SCRIPT score to any known partner would help contextualize the improvement (related to the missing ablation but simpler to implement).

## Removed Points

The following points from the reviewer inputs were filtered out per verification against the paper:

- **"Unfair comparison — baselines don't use known partners"**: The paper frames the task as "given known partners, rank novel candidates." The baselines (raw PPI probabilities) are not designed for this task. The paper's contribution IS a method that uses known partners. This is a valid task framing, not an unfair comparison. The specific concern about isolating the active-residue contribution is preserved as a Major weakness (missing ablation).

- **"xCAPT5 undercuts the narrative"**: xCAPT5 has marginally higher Precision@5 (0.1943 vs 0.1924, a 0.0019 difference — essentially a tie), but the proposed method substantially outperforms xCAPT5 on Recall@5 (4×), MAP@5 (1.8×), MRR (5.3×), Success@5 (13×), and essentially all other metrics. The claim of comparable performance is not supported by Table 1.

- **"Re-ranking analysis uninterpretable / ‡ undefined"**: The ‡ is a parser artifact from PDF extraction. The metric is clearly defined in lines 227–228 as tracking whether rank positions maintain, improve, or worsen. The concept is standard for pairwise rank-shift analysis.

- **"Prediction Coverage circularity with structure-based predictions"**: The paper clearly states (lines 193–194) it retains interactions with experimental support > 0, discarding indirect associations. The mention of "structure-based predictions" describes what drives the increase in STRING v12, not what was used as ground truth.

## Novel Insights

The pairwise rank-shift analysis in Table 2 reveals a consistent hierarchy: PubMedBERT > BioBERT/BioMedRoBERTa > lightweight annotation heuristics (TF-IDF, token/location/key-term overlap) > interaction score (IS) > pDockQ. The finding that simple term-overlap signals achieve ~70% maintain-or-improve rates suggests that much of the signal comes from coarse functional annotations rather than deep representations, and that the marginal value of sophisticated LLM-based re-rankers (beyond PubMedBERT) may be limited. The paper's explicit discussion of whether LLM gains reflect "semantic generalization or latent knowledge of interactions from the training data" (lines 262–264) shows appropriate caution about the source of these improvements.

## Suggestions

1. **Recalibrate the "two orders of magnitude" claim** to accurately reflect the actual gains (~5–26× depending on the metric). The improvements are impressive and practically meaningful when stated plainly.
2. **Add the critical ablation**: Compare active-region similarity against full-embedding similarity (both using known partners as anchors). This is essential for demonstrating that the contact-map-guided selection adds value beyond simply using known partners.
3. **Add confidence intervals** (bootstrap) to Table 1 to quantify variance across proteins.
4. **Align the Prediction Coverage definition** with the values reported in Table 1 (clarify whether it is a fraction or a count).
5. **Add stratification by known partner count** to characterize the method's failure regime for under-studied proteins.

## Calibration Anchors

**Round 1 (Bracketing)** — All queries on "protein-protein interaction prediction ranking candidate prioritization":

| Path | Avg Score | Round | Comparison |
|------|-----------|-------|------------|
| 44IKUSdbUD.md | 3.00 | R1 low | Weaker — fundamental flaws, clear reject |
| S2WHlhvFGg.md | 3.00 | R1 low | Weaker — fundamental flaws |
| An87ZnPbkT.md | 3.00 | R1 low | Weaker — incremental contribution |
| jqx5XI4Yr3.md | 3.40 | R1 low | Weaker — limited evaluation |
| nWO75tVjfp.md | 3.00 | R1 low | Weaker — noisy evaluation |
| Y9yQ9qmVrc.md | 2.50 | R1 low | Weaker — incomplete method |
| eh1fL0zw8o.md | 6.00 | R1 mid | Stronger avg but Rejected due to fundamental comparison issues |
| itGkF993gz.md | 5.67 | R1 mid | Slightly stronger — clearer technical novelty, accepted |
| jsQPjIaNNh.md | 5.25 | R1 mid | Comparable — similar missing-baseline issues, rejected |
| xcMmebCT7s.md | 5.80 | R1 mid | Slightly stronger — solid dataset+model contribution, accepted |
| xNDydjYBmC.md | 4.60 | R1 mid | Weaker — unclear methodology |
| ZkpDdCQUC4.md | 4.60 | R1 mid | Weaker — dataset-only contribution |
| ja4rpheN2n.md | 8.00 | R1 high | Much stronger — clean execution, strong acceptance |
| A3YUPeJTNR.md | 8.00 | R1 high | Much stronger — top-tier analysis |
| zMPHKOmQNb.md | 8.00 | R1 high | Much stronger — strong generative model |
| Fk5IzauJ7F.md | 8.00 | R1 high | Much stronger — strong theory+experiments |
| kJFIH23hXb.md | 8.00 | R1 high | Much stronger — clean flow matching |
| KbetDM33YG.md | 8.00 | R1 high | Much stronger — strong evaluation framework |

**Round 2 (Narrowing)** — Targeted queries to narrow within (4.5, 7.5):

| Path | Avg Score | Round | Comparison |
|------|-----------|-------|------------|
| itGkF993gz.md (MAPE-PPI) | 5.67 | R2 low | Slightly stronger — novel method, accepted despite mixed reviews |
| wCwz1F8qY8.md (DeepSSInter) | 5.00 | R2 low | Weaker — incremental model, unclear novelty |
| ZkpDdCQUC4.md (NovoBench) | 4.60 | R2 low | Weaker — dataset-only, less method |
| jsQPjIaNNh.md (ProtIR) | 5.25 | R2 low | Comparable — similar contribution level, rejected for missing baselines |
| xNDydjYBmC.md (PPBind) | 4.60 | R2 low | Weaker — unclear design choices |
| uQnvYP7yX9.md (ReNovo) | 6.50 | R2 high | Stronger — clear contribution, accepted |
| IxmWIkcKs5.md (ΔΔG Predictor) | 6.75 | R2 high | Stronger — well-executed, accepted |
| jJCeMiwHdH.md (BioBridge) | 7.00 | R2 high | Stronger — clean framework, accepted |
| 8CKgS18uWx.md (SEPIT) | 6.25 | R2 high | Stronger avg but rejected for novelty concerns |
| HAwZGLcye3.md (BioDiscoveryAgent) | 6.40 | R2 high | Stronger — well-executed agent, accepted |

**Score Determination**: Round 1 placed the paper between 3.5 and 7.5 (above the clear rejects around 3.0, well below the 8.0 papers). Round 2 narrowed this: the paper is roughly comparable to ProtIR (5.25, reject) and MAPE-PPI (5.67, accept), slightly below MAPE-PPI in technical novelty but above ProtIR in clarity of contribution and evaluation. The most similar accepted papers (MAPE-PPI at 5.67, PPIformer at 5.80) have stronger technical contributions but comparable evaluation rigor. The paper's two major issues — an exaggerated claim and a missing ablation — are fixable but weigh against it. Final score: 5.5.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Accept</decision>