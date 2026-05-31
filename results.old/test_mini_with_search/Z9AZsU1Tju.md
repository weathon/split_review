Now I have a solid calibration. Let me write the final review.

**Round 1 bracket:** I placed the paper between 4 and 7 after the bracketing pass.

**Round 2 narrowing:** The paper is closest to HiTNet (5.00, Reject) — both are neuroscience-inspired multimodal methods tested on similar benchmarks, with similar concerns about loose biological connection and evaluation gaps. It is slightly weaker than DecAlign (5.33, Accept) which had stronger ablation coverage, and weaker than TCMax (5.50, Accept) which had a cleaner theoretical contribution. It is clearly above DSRF (2.50) and the other low-end anchors. It is clearly below CLIB (6.50, Accept) which had a more polished evaluation.

**Final score: 5.0**

---

## Summary

This paper proposes the Information-Theoretic Hierarchical Perception (ITHP) model for multimodal learning, which applies the information bottleneck principle in a hierarchical fashion. The model designates a prime modality and compresses information through a chain of latent states, where each state is encouraged to retain information about the next modality while discarding redundancy. Experiments on MUStARD (sarcasm detection), CMU-MOSI, and CMU-MOSEI (sentiment analysis) show consistent improvements over existing baselines, with a headline claim of outperforming human-level performance on all four CMU-MOSI metrics.

## Strengths

- **Consistent improvements across three diverse datasets.** On MUStARD, ITHP improves F-score by ~4% absolute over MSDM (71.5 → 75.2). On CMU-MOSI, ITHP-DeBERTa achieves 88.7% BA vs. the best prior DeBERTa-based model at 86.1% (MAG_d). On CMU-MOSEI, ITHP reaches 87.3% BA vs. 86.0% (MMIM_b). These gains are consistent and non-trivial.

- **Systematic analysis of the two Lagrange multipliers (β, γ) on MUStARD.** Figure 3 maps performance across a grid of β and γ values, showing that best results occur at β=32, γ=8, that higher β is more beneficial than higher γ, and that the model is sensitive to poor choices (performance collapses at β=2, γ=2). This provides genuine insight into the information flow and goes beyond a single best-result table.

- **Novel formulation of hierarchical IB for multimodal fusion.** Equations (2)–(4) formalize the problem of compressing through a chain of latent states with asymmetric modality ordering, which differs from standard flat-fusion or symmetric-IB approaches. The Lagrangian in Eq. (4) and its neural-network variational approximation (Eqs. 5–6) provide a concrete optimization framework that extends naturally to N modalities.

## Weaknesses

### Major

- **Headline claim of outperforming human-level benchmarks lacks a citation for the source of the human numbers.** Table 1 lists human performance as 85.7% BA, 87.5% F1, 0.710 MAE, 0.820 Corr but provides no reference. For a claim as strong as "the first work, based on our knowledge, to outperform human-level benchmarks on all evaluation metrics" (Conclusion), the provenance of these human benchmarks must be explicitly cited and the conditions (same test set, same annotation protocol) should be stated. Without this, the paper's central significance claim is incompletely supported.

- **Inclusion of Self-MM_d (55.1% BA) in the comparison table without adequate caveat.** The paper correctly notes that Self-MM "heavily relies on the feature extraction process performed by BERT," explaining its catastrophic failure with DeBERTa. However, including this broken variant alongside ITHP's 88.7% gives a misleading visual impression of the performance margin. A footnote, asterisk, or separate row category would be more appropriate. The remaining baselines (MMIM_d at 85.8%, MAG_d at 86.1%) still show ITHP leading, so the issue is presentational rather than substantive, but it should be addressed.

- **Unexplained loss scaling factor 2/(β+γ).** In Eq. (8), the overall hierarchical loss is scaled by 2/(β+γ) before adding the task loss. The paper provides no motivation for this specific scaling, and β and γ already control trade-offs within the IB losses. This makes the loss function appear engineered rather than derived from the optimization problem. An ablation or justification is needed.

### Minor

- **No confidence intervals, standard deviations, or multi-seed results reported.** Given that MOSI has ~686 test utterances, variance could be non-trivial. Reporting results from at least 3–5 seeds with mean and std would strengthen reliability claims.

- **The neuroscience inspiration is evocative but does not constrain the architecture in a falsifiable way.** The claim that the brain processes modalities hierarchically does not uniquely determine the ordering mechanism (text > audio > video for sentiment), the specific IB formulation, or the number of hierarchy levels. The paper would be better served by foregrounding the information-theoretic formulation as the contribution and treating the neuroscience connection as motivational context rather than as part of the technical contribution.

- **Data splits for MOSI/MOSEI are not specified.** The paper should state the train/validation/test partition used (e.g., the standard 60%/20%/20% split or leave-one-subject-out) to ensure reproducibility.

### Trivial

- The sentence "Detailed derivations of the Eqns." on line 140 cuts off abruptly (parser artifact in the provided text, but the original should be checked for completeness).

## Nice-to-Haves

- **Ablation: hierarchical vs. flat IB fusion.** Comparing ITHP against a single-level IB that compresses all modalities jointly (concatenated input → single latent B → task prediction) would directly isolate the benefit of the hierarchical chain over flat compression. Currently, the paper only compares against non-IB baselines.

- **IB-plane visualization.** Showing I(X;B) vs. I(B;Y) for the latent states at different hierarchy levels would provide direct evidence for the claimed compression-information trade-off, beyond final task performance.

## Removed Points

These points from the reviewers were removed with justification:

1. *Missing recent baselines (M3AE, etc.)* — Removed per instructions: I cannot verify which baselines existed at submission time or whether the comparison set was standard for the paper's timeline.

2. *Baselines not reproduced under identical conditions* — Removed: reporting results from published papers is standard practice; the paper explicitly states using "the same embedding data" for MUStARD. The critic's speculation about unfair comparison is not grounded in the paper content.

3. *Gap between constrained optimization and relaxed Lagrangian is not discussed* — Removed: this is standard practice in the entire VIB/IB literature; requiring a paper to belabor this point would be scope creep.

4. *Missing derivations of variational approximations (Eqs. 5-6)* — The text broke off mid-sentence ("Detailed derivations of the Eqns."), which is a parser artifact in the provided version. Per instructions, parser artifacts are not author errors.

5. *Criticism that ITHP's performance at β=2, γ=2 is worse than unimodal* — The paper itself acknowledges and discusses this (line 218). The critic is restating what the paper already says.

6. *Data leakage between human benchmark test set and model test set* — The critic speculates that human performance might have been measured on a different subset, but provides no evidence. The paper should cite the source, which is a Major weakness I retained — but the speculation about data leakage specifically is not grounded in the paper.

7. *Generic statements about missing implementation details* — Moved here as many are standard-enough that they don't constitute weaknesses (e.g., not specifying the prior q(B₀) distribution — all VIB papers use a standard Gaussian prior).

## Novel Insights

None beyond the paper's own contributions. The reviews do not surface a higher-level insight that the paper itself missed.

## Suggestions

1. Add a citation for the human-level benchmark source (e.g., the original MOSI paper) and clarify that the same test set and protocol are used.
2. Either remove Self-MM_d from the comparison table or add a clear footnote/asterisk explaining it is a known failure case.
3. Provide a brief justification or ablation for the 2/(β+γ) scaling factor in Eq. (8), or remove it and use a simpler scaling (e.g., a learned or tunable parameter).
4. Report results over at least 3 random seeds with mean and std on all datasets.
5. Specify the data splits (train/validation/test) used for MOSI and MOSEI.
6. Add an ablation comparing hierarchical IB (ITHP) against a flat single-level IB to isolate the benefit of the hierarchy.

## Score and Decision

### Calibration Anchors

| Path | Avg Score | Round | Comparison |
|------|-----------|-------|------------|
| kLzpTy4mVl.md (DSRF) | 2.50 | R1 | Clearly weaker: limited experiments, overcomplicated optimization |
| QGejSAi7U4.md (PGLH) | 3.00 | R1 | Clearly weaker: less coherent contribution |
| dADwCplxyC.md (Multi-faceted Monosemanticity) | 3.00 | R1 | Different topic, weaker methodological contribution |
| NuYcnDYQuQ.md (Evil in Pairing) | 3.00 | R1 | Weaker: focuses on attribution, not multimodal fusion |
| JdVTWjjnR6.md (HiTNet) | 5.00 | R1/R2 | Most comparable: similar neuroscience-inspired multimodal sentiment approach, similar evaluation concerns |
| uKPdSZuvUJ.md (I²C) | 4.00 | R1 | Weaker: less novel formulation |
| 5bxmmuRhO6.md (IF MML) | 4.50 | R1 | Comparable theoretical rigor but different problem scope |
| TUKrrXWMN2.md (GIB) | 4.40 | R1 | Similar IB-based multimodal approach but for clustering, weaker evaluation |
| CULACouTam.md (CaMIB) | 4.00 | R2 | Similar IB-for-multimodal framing but weaker results |
| MbQhdzAhSl.md (TCMax) | 5.50 | R2 | Stronger: cleaner theoretical contribution, better evaluation protocol |
| LasUPe2UxG.md (DecAlign) | 5.33 | R2 | Stronger: more thorough ablations and baseline coverage |
| iedlZOdI0d.md (CLIB) | 6.50 | R2 | Clearly stronger: cleaner contribution, more polished evaluation |
| kkBOIsrCXh.md (NavFoM) | 8.00 | R1 | Different domain, much broader in scope |
| DM0Y0oL33T.md (Gen Univ Verifier) | 8.00 | R1 | Different domain, different contribution type |

**Round 1 bracket:** 4–7
**Round 2 narrowing:** Paper is closest to HiTNet (5.00) — both have a solid core idea, consistent results, but evaluation presentation issues. It is slightly below DecAlign (5.33) and TCMax (5.50) which have cleaner validation. It is well above the weak papers (2.50–3.00).

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>