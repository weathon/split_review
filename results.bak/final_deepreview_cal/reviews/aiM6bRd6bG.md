Now I have a solid calibration. Let me write the final consolidated review.

**Bracket analysis:**
- Round 1 bracket: 4.5–6.0. The paper's prospective evaluation is stronger than typical 3.0 reject papers, but the exaggerated claim and missing ablation prevent it from reaching the 7+ band.
- Round 2 comparison: MAPE-PPI (5.67, Accept) had similar missing-baseline issues but its central claim was not overstated. Our paper has a cleaner evaluation design (prospective STRING) but the "two orders of magnitude" exaggeration and the central ablation gap make it weaker than MAPE-PPI. SEPIT (6.25, Reject) was better presented but had data leakage concerns. I place the paper around 5.0.

---

## Summary

This paper introduces the problem of **PPI candidate ranking** — prioritising novel interaction candidates for experimental testing — and proposes a two-stage pipeline: (1) interpretability-guided retrieval that uses contact-map-derived active regions from known interaction partners to rank candidates via cosine similarity on those regions, and (2) a re-ranking module that integrates interaction scores, structural plausibility (pDockQ), functional annotations (GO terms, domains, pathways), and LLM-based semantic similarity (BioBERT, PubMedBERT). Evaluation on a prospective STRING v11→v12 benchmark (279,568 new positives) shows large improvements in early-ranking metrics over direct model interaction probabilities.

## Strengths

- **Prospective temporal evaluation.** The test set is constructed from interactions that appear only in STRING v12 but not v11 — a principled, non-retrospective benchmark that directly tests whether models can *anticipate* future discoveries. This is a genuine strength over static train/test splits common in PPI work.

- **Large and practically meaningful improvements in early ranking.** On the D-SCRIPT backbone, Recall@10 rises from 1.24% (direct IS) to 26.41%, and MAP@5 from 0.0103 to 0.2714 — roughly 20–25× improvements. Even accounting for the exaggerated claim (see Weaknesses), these are practically significant hit rates for experimental screening.

- **Systematic multi-signal re-ranking analysis.** Table 2 compares ten evidence sources (cosine, IS, pDockQ, TF-IDF, token overlap, localization, key terms, BioBERT, BioMedRoBERTa, PubMedBERT) on pairwise rank shifts. The finding that PubMedBERT improves or maintains 75.5% of rediscoveries over the cosine baseline, and that lightweight annotation signals (location overlap, key terms) also yield solid gains, is informative and practically useful.

- **Rigorous cross-encoder training protocol.** The GroupKFold split by protein identity (Section 4.2) prevents protein-level leakage between training and validation for the PubMedBERT re-ranker.

## Weaknesses

### Major

1. **"Two orders of magnitude" claim is quantitatively wrong.** The abstract, introduction, and conclusion state the approach yields improvements *"by up to two orders of magnitude over existing models."* Two orders of magnitude means ~100×. The largest improvement in Table 1 is ~26× (MAP@5: 0.0103 → 0.2714). Several metrics show more modest gains (MRR: 0.0340 → 0.1685, ~5×). This is not a phrasing quibble — it is a factual error in a headline quantitative claim that appears three times in the paper. The results are impressive enough without exaggeration, and this should be corrected.

2. **Missing ablation: full-embedding similarity baseline.** The paper's core technical contribution is *active-region selection* from contact maps. However, Table 1 compares the proposed method (known partners + active-region cosine similarity) against direct model interaction probabilities (IS). These differ in two ways: (a) using known partners at all, and (b) restricting similarity to predicted active regions. The obvious ablation — rank candidates by maximum full-embedding cosine similarity to any known partner, *without* contact-map filtering — is absent. Without it, the reader cannot tell whether the gains come from the specific active-region mechanism or simply from the trivial signal of using known partners as anchors for nearest-neighbor search. This is the single most important missing experiment for supporting the paper's claimed novelty.

3. **Re-ranking evaluation does not measure whether ranking quality improves.** The re-ranking analysis (Table 2) reports only pairwise rank-shift fractions within the existing top-10 set. Because re-ranking operates on a fixed top-10 candidate set, Recall@k for k≤10 cannot change. The paper never reports whether re-ranking actually improves standard ranking metrics (nDCG@10, MAP@10, MRR) on the full test set. The pairwise shift table describes *what moves* but not *whether the final ordering is better*. This is an evaluative gap for the re-ranking module.

### Minor

4. **Active-residue extraction threshold is underspecified.** Section 4.1 states: *"We then scan the resulting activation profile along the sequence of p_k and identify all maximal contiguous segments of highly activated residues."* The criterion for "highly activated" (a threshold, statistical cutoff, or selection rule) is never stated in the main text. While this detail may appear in the (stripped) appendix, the main text is insufficient for a reader to understand or reproduce the method without it.

5. **Table 2 formatting is ambiguous.** The caption mentions both † (fraction maintained/improved) and ‡ (presumably fraction worsened), but each cell contains only one number. The green/red coloring helps, but the presentation is confusing.

### Trivial

- None beyond the above.

## Nice-to-Haves

- The re-ranking results would be strengthened by reporting end-to-end metrics (nDCG@10, MAP@10, MRR) after each re-ranking method, not just pairwise shifts within the top-10.
- The paper implicitly assumes the binding-interface length inferred from the known partner's active region applies to the candidate side (Eq. 3). A brief discussion of when this assumption might break (interface length mismatch) would be helpful.

## Removed Points

- *Criticism about unfair comparison favoring the author's method* — Rule: remove if the asymmetry favors the baseline. The comparison in Table 1 is against direct IS ranking, which is a reasonable baseline; the asymmetry (if any) doesn't favor the proposed method, so this is not relevant.
- *Reproducibility concerns about undisclosed hyperparameters or implementation details* — The paper references Appendix A.1 for details; the parser strips appendices. These details likely exist in the original submission.
- *"Weakness" about Table 2 missing the second value* — This is likely a parser artifact or formatting issue; one number per cell with color coding still communicates the key information. Kept as minor formatting note only.
- *Strength Finder's claim that 20-25× improvement "concretely supports the claim of 'two orders of magnitude'"* — This is factually wrong (20-25× is ~1.4 orders of magnitude, not 2). Removed as invalid.

## Novel Insights

None beyond the paper's own contributions. The reviewers identified the central tension (claimed novelty vs. missing ablation) but did not surface any novel synthesis beyond what the paper already presents.

## Suggestions

1. **Correct the "two orders of magnitude" claim** to something like "up to ~20–25× improvement" — the results are strong enough without exaggeration.
2. **Add the missing ablation**: rank candidates by maximum full-embedding cosine similarity to any known partner (no active-region selection). If the active-region method outperforms this baseline, the technical contribution is clear; if not, the paper's framing should be adjusted.
3. **Report end-to-end ranking metrics after re-ranking** (nDCG@10, MAP@10, MRR) to demonstrate that the second stage actually improves ordering quality.
4. **Specify the active-residue threshold** in the main text (or clearly reference the appendix section where it is defined).

## Score and Decision

### Calibration Anchors

| Anchor | Avg Score | Round | Comparison |
|--------|-----------|-------|------------|
| S2WHlhvFGg (DTI prediction, graph transformers) | 3.00 | R1 bracketing (weak) | Much weaker evaluation; our paper's prospective benchmark is substantially stronger. |
| IEZjjDX0iC (Phage protein LMs) | 3.00 | R1 bracketing (weak) | Narrower scope and less rigorous evaluation; our paper is clearly above this. |
| An87ZnPbkT (GNNAS-Dock) | 3.00 | R1 bracketing (weak) | Different task, weaker evaluation; our paper is above. |
| 1S8ndwxMts (Protein generative model metrics) | 3.00 | R1 bracketing (weak) | Different topic; our paper has more concrete empirical contributions. |
| ZkpDdCQUC4 (NovoBench-100K) | 4.60 | R1 bracketing (middle) | Comparable in having a prospective/ranking formulation, but our paper has a more direct biological application. Slightly below our paper in impact. |
| jsQPjIaNNh (ProtIR protein function) | 5.25 | R1 bracketing (middle) | Similar in having missing-baseline weaknesses; our paper's prospective evaluation is cleaner. Comparable quality. |
| eh1fL0zw8o (LLaPA PPI prediction) | 6.00 | R1 bracketing (middle) | Better presented but had data leakage concerns that could undermine results. Our paper's evaluation design is more rigorous. |
| wCwz1F8qY8 (DeepSSInter contact prediction) | 5.00 | R2 narrowing | Incremental architecture claim; our paper introduces a genuinely new problem formulation. Slightly stronger than this anchor. |
| itGkF993gz (MAPE-PPI) | 5.67 | R2 narrowing | Accepted, but had missing-baseline issues similar to our paper. Our paper has a stronger evaluation design but an exaggeration problem MAPE-PPI doesn't have. Our paper is slightly weaker. |
| 8CKgS18uWx (SEPIT protein instruction tuning) | 6.25 | R2 narrowing (upper) | Stronger presentation but data leakage concerns; our paper is below this on writing polish but comparable on evaluation rigor. |
| IxmWIkcKs5 (ΔΔG predictor) | 6.75 | R2 narrowing (upper) | Cleaner empirical story; our paper has a more ambitious scope but weaker support for central claim. |

**Round 1 bracket**: 4.5–6.0. **Round 2 narrowing**: The paper is slightly below MAPE-PPI (5.67) because the exaggerated claim and missing central ablation are more damaging to the paper's core thesis than MAPE-PPI's baseline gaps were to its contribution. It is slightly above DeepSSInter (5.00) because it introduces a genuinely new problem formulation and uses a prospective benchmark. **Final score: 5.0.**

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>