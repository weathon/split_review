Now I have a clear picture of the paper and the calibration anchors. Let me write the final consolidated review.

**Calibration Synthesis:**

**Round 1 (Bracketing):** Three bands searched.
- **Weak band (avg < 3.5):** Retrieved papers with avg scores 2.0–3.0 — these had withdrawn decisions or fundamental issues like task misalignment or insufficient evaluation. TbLTA is clearly stronger.
- **Middle band (3.5–7.5):** Retrieved anchors with scores 4.0–5.8. I read EVA (5.75, Reject), VAP (5.8, Reject), InterAct (5.0, Reject), FBSVP (4.75), RISE (5.25), and the Weakly Supervised Skilled Activity paper (4.75).
- **Strong band (avg > 7.5):** Retrieved papers with scores 7.6–8.5 — these were strong accepts with exceptional rigor. TbLTA is not at this level.

**Initial bracket:** 4.5–6.5.

**Round 2 (Narrowing):** Searched specifically for papers with scores 4.0–6.5 and 3.5–5.5. Read additional anchors: InterAct (5.0, multi-scale action segmentation, limited novelty), Weakly Supervised Skilled Activity (4.75, weak supervision but evaluation concerns), RISE (5.25, first generative approach for zero-shot action recognition, split reviews).

**Comparison to anchors:** TbLTA is stronger than InterAct (5.0) and FBSVP (4.75) — it has clearer novelty as the first work of its kind. It is comparable to EVA (5.75) and VAP (5.8) — these papers have stronger evaluation but less clear novelty. TbLTA is slightly weaker than RISE (5.25 avg, but with one 8 and one 3) — the RISE paper had a stronger evaluation but serious presentation issues. TbLTA falls between 5.0 and 6.0.

**Final score:** 5.5 — a borderline paper with a real contribution (first weakly-supervised LTA) that is undermined by thin weakly-supervised baselines, missing training details, and somewhat imprecise claim framing. The contribution is salvageable with revisions, but in its current form falls short of the ICLR acceptance threshold.

---

## Summary

This paper introduces TbLTA, the first framework for dense Long-Term Action Anticipation (LTA) trained exclusively from video transcripts — ordered action lists without timestamps, boundaries, or durations. The approach uses a temporal alignment module (ATBA) to generate pseudo-labels from transcripts, a cross-modal attention mechanism to ground video features with transcript semantics, and a CTC+CRF+duration loss framework. Experiments on Breakfast, 50Salads, and EGTEA show that the deterministic TbLTA model achieves competitive results with fully supervised methods on Breakfast (29.03 avg MoC vs. 28.45 for ActFusion), while trailing on 50Salads and EGTEA.

## Strengths

1. **First weakly-supervised framework for dense LTA using only transcripts.** The paper is the first to demonstrate that dense long-term action anticipation can be trained without any frame-level annotations, using only ordered action lists. This is a genuine novelty relative to all prior LTA work, which requires either full dense labels or at least some temporally-localized weak labels. The abstract, Section 2 (last paragraph), and Section 5 all clearly establish this claim.

2. **Competitive results on Breakfast at 30% observation.** In Table 1, deterministic TbLTA achieves 40.28 MoC at Obs 30%/10% horizon, surpassing all fully supervised baselines (best: ActFusion 35.79). The average MoC across all horizons at Obs 30% is also highest (29.03 vs. 28.45 for ActFusion). This is a meaningful result that demonstrates transcript-only supervision can match dense annotation on a standard benchmark.

3. **Well-motivated architectural design with informative ablation study.** The ablation study (Table 4) shows that each component — cross-modal attention (drop of ~5.7 on Breakfast, ~1.3 on 50Salads), CRF loss (drop of ~4.1–5.3 at longer horizons), and duration loss (drop of ~3.3 on Breakfast) — contributes positively. The cross-modal attention with local masking (Eq. 1–2) is a specific architectural innovation that demonstrably improves over the unconstrained cross-attention variant.

4. **Outperforms the only prior (semi-)weakly supervised LTA method.** TbLTA exceeds WS-DA (Zhang et al., 2021) by a wide margin on Breakfast at Obs 30% (28.79 vs. 15.65 at 50% horizon). This is a clear improvement over the only existing approach that reduces annotation cost.

## Weaknesses

### Major

- **Weakly-supervised baseline comparison is thin.** The only weakly-supervised competitor is WS-DA, evaluated at just two data points (Obs 30% on Breakfast and 50Salads). While the paper correctly notes that WS-DA is "the only attempt" at reducing annotation for LTA, the evaluation would be substantially stronger with additional baselines constructed from related paradigms (e.g., adapting a TAS method trained on transcripts to produce anticipation outputs, or using language-only sequence priors). Without this, it is difficult to attribute the gains specifically to the transcript-supervision paradigm versus the architectural choices.

- **Training details insufficient for reproducibility.** The paper provides layer counts, hidden dimensions, and attention heads (Section 4.1), but omits the optimizer (Adam? AdamW?), learning rate schedule, batch size, number of gradient steps in the end-to-end stage, and hardware configuration. The pre-training loss L_vid is referenced (line 202) but never defined in the main text — the reader must infer its purpose from context. These are standard inclusions for a reproducibility-conscious submission.

- **The claim of being "competitive with fully supervised methods" is qualified in the text but overreaches in the abstract and conclusion.** The abstract states results are "competitive with, and in certain settings even superior to, fully supervised methods." This is accurate for Breakfast at 30% observation, but on 50Salads the deterministic TbLTA (20.92 avg) substantially trails ActFusion (28.39 avg), and on EGTEA it underperforms both supervised baselines on All and Freq metrics. The experimental section (line 231) appropriately qualifies the claim ("occasionally superior," "on Breakfast... outperforming"), but the abstract and conclusion frame it as a general statement.

### Minor

- **No confidence intervals or variance reported.** Breakfast results are averaged over 4 splits and 50Salads over 5 splits, but no standard deviations or error bars are reported. Given that the claim of being competitive with supervised methods rests on relatively small margins on Breakfast (29.03 vs. 28.45), variance estimates would help the reader assess the reliability of this result.

- **Cross-modal mask construction is underspecified.** Equation 1 uses a binary mask M that "restricts each action a_i to a temporal neighborhood around its predicted occurrence" (line 134), but the paper does not specify how this neighborhood is defined (fixed window size? adaptive? how is the center determined from pseudo-labels?). This is needed for exact reproducibility.

### Trivial

- **Definition of L_vid is missing.** The pre-training stage uses a "video-level classification loss L_vid" (line 202) that is never defined in the main text. This is a minor omission that should be fixed.

- **"Pyramid hierarchical local attention mechanism"** is mentioned (line 126) and cited to Vaswani et al. (2017), which does not describe pyramid hierarchical local attention. This is a minor citation inaccuracy.

## Nice-to-Haves

- Reporting stochastic results with a clear description of the sampling procedure (number of samples, selection criterion for Top-1, and whether the decoder is inherently stochastic or sampling is applied on top of a deterministic decoder) would improve interpretability. The paper references the supplementary material for the stochastic protocol, which is standard practice.
- A runtime or complexity analysis of the transformer-based architecture would be useful for practitioners.
- A per-class breakdown or confusion matrices on EGTEA would strengthen the analysis of rare-class performance.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **"Stochastic protocol not described"** — The paper states "We also report the stochastic protocol of Abu Farha & Gall (2019) in the supp. mat." (line 227). The appendix is stripped by the parser; this detail exists in the original submission. REMOVED per rule: parser strips appendices.
- **"Missing details about ATBA module"** — The paper cites Xu & Zheng (2024) and describes the module's function (dynamic programming over boundaries, soft pseudo-labels). This is standard practice for a cited module. REMOVED as a strawman weakness.
- **"Missing related works"** — As per instructions, I cannot mention missing related works. REMOVED.
- **"Mixing deterministic and stochastic results in the same table is misleading"** — The table clearly separates deterministic (bold) from stochastic (*-annotated, gray shading in caption), and the text says "deterministic for reproducibility and stochastic for diversity" (line 231). This is transparent presentation. REMOVED.
- **"EGTEA analysis is too thin"** — The paper's claim is specifically "competitive on rare classes" (60.11 vs. 59.70/55.10), which is accurate. The experiment is presented as supplementary evidence, not a core claim. DEMOTED to observation rather than weakness.
- **Weaknesses from the Strength Finder's "Strengthening the Paper on Its Own Terms" section** — These are methodological suggestions (report confidence intervals, add baselines) that are already captured as Minor weaknesses above. The specific suggestions are moved to Nice-to-Haves.

## Novel Insights

None beyond the paper's own contributions. The reviews do not surface a perspective on the paper that the authors themselves have not articulated.

## Suggestions

1. **Tone down the abstract and conclusion claims.** Replace "competitive with, and in certain settings even superior to" with a more precise statement: "competitive on Breakfast at 30% observation, though trailing on 50Salads and EGTEA." This better matches the evidence.

2. **Add training details.** Include optimizer, learning rate, batch size, number of epochs for the end-to-end stage, and hardware configuration. Define L_vid explicitly.

3. **Add weakly-supervised baselines.** Even approximate comparisons — e.g., adapting a TAS method trained on transcripts to the LTA setting, or using a language model for sequence prediction — would significantly strengthen the evaluation.

4. **Report standard deviations for the main results** (at least for the average MoC), especially given the multi-split evaluation protocol.

5. **Clarify the cross-modal mask construction.** Specify how the "temporal neighborhood" around each predicted action occurrence is defined in Equation 1.

6. **Clarify the "pyramid hierarchical local attention" citation.** Either cite the correct source or describe the mechanism briefly.

## Score and Decision

**Calibration anchors used across all rounds:**

| Path | Avg Score | Round | Comparison |
|------|-----------|-------|------------|
| OrBIjc0lMz.md (Gaze-Regularized Attention) | 4.0 | R1 | Weaker — limited novelty, thin evaluation, only one dataset. TbLTA has stronger novelty and more datasets. |
| N6SccBt3EF.md (EVA) | 5.75 | R1 | Comparable — similar novelty level but EVA has more comprehensive evaluation and a new benchmark. TbLTA has cleaner novel contribution. |
| KtqZrNjvjd.md (VAP) | 5.8 | R1 | Comparable — novel approach to keyframe selection with SOTA results. TbLTA has weaker quantitative results but clearer problem novelty. |
| sEARCNzhrP.md (InterAct) | 5.0 | R2 | TbLTA is stronger — InterAct had limited novelty claims. TbLTA's first-of-its-kind claim is better supported. |
| HCoSsULNxG.md (Weakly Supervised Skilled Activity) | 4.75 | R2 | TbLTA is stronger — better evaluation and clearer contribution. |
| IryGDUHxDE.md (RISE) | 5.25 | R2 | Comparable — RISE had split reviews (8,5,5,3) with strong novelty claims but presentation issues. TbLTA has similar profile. |
| UAiuV8Plei.md (FBSVP) | 4.75 | R2 | TbLTA is stronger — FBSVP had novelty concerns. TbLTA's contribution is more clearly novel. |

**Round 1 bracket:** 4.5–6.5. **Round 2 narrowing:** After reading additional anchors, the paper sits between 5.0 (InterAct-level) and 5.8 (VAP/EVA-level). The genuine novelty of being the first weakly-supervised LTA framework pushes it above InterAct, but the thin weakly-supervised baseline comparison and missing training details prevent it from reaching the VAP/EVA level. **Final score: 5.5.**

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>