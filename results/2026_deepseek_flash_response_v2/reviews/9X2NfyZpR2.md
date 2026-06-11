Now I have sufficient calibration data. Let me write the final review.

## Summary

This paper introduces TbLTA, the first framework for dense long-term action anticipation (LTA) trained exclusively from video transcripts — ordered action lists without timing or duration information — eliminating the need for expensive frame-level annotations. The model uses a transformer encoder-decoder architecture with temporal alignment (ATBA) to generate pseudo-labels, cross-modal attention to ground video features with transcript semantics, and a combination of CTC, CRF, and self-supervised duration losses. On the Breakfast benchmark at 30% observation, the deterministic model (29.03 avg MoC) surpasses the best fully-supervised method ActFusion (28.45), demonstrating that transcript-only supervision can be viable for dense LTA on datasets with strong procedural regularities.

## Strengths

- **First transcript-only weakly-supervised dense LTA framework with a genuine contribution.** The paper convincingly demonstrates that dense LTA is feasible without any frame-level labels. On Breakfast, TbLTA's deterministic model (29.03 avg MoC) outperforms the best fully-supervised method ActFusion (28.45) at 30% observation, and at several individual horizons it exceeds all supervised baselines (Table 1, lines 213-219). This is a nontrivial result that validates the core thesis.

- **Rare-class performance on EGTEA exceeds supervised methods despite overall gap.** On EGTEA, TbLTA achieves 60.11 mAP on rare classes, outperforming both supervised Timeception (59.70) and Anticipatr (55.10) (Table 2, lines 239-243). This suggests that transcript-based semantic supervision provides a distinctive advantage for data-imbalanced classes, a finding worth highlighting.

- **Thorough ablation study isolating each component.** Tables 3-4 (lines 247-269) show clear, monotonic degradation when removing the CRF (drops of ~4-5 points on longer horizons), cross-attention (~1.3-5.7 points), and duration loss (~0.2-3.3 points). The controlled comparison between simplex cross-attention and the proposed masked variant provides fine-grained evidence for design choices.

- **Principled integration of multiple training signals under weak supervision.** The combination of CTC loss for frame-to-label marginalization (Section 3.2.2), a self-supervised duration loss using momentum-based class priors (Section 3.2.3), and a CRF for temporal coherence (Section 3.2.3) is technically sound and each component's contribution is empirically validated.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

- **Limited weakly-supervised comparison.** The only prior weakly-supervised LTA method (WS-DA, Zhang et al., 2021) is compared at a single setting per dataset (Obs 30%, β=10% horizon) because those are the only settings WS-DA reported. However, the paper's claim that TbLTA "consistently surpasses" WS-DA (Section 4.2, line 227) is stronger than a single data point per dataset supports. The paper is transparent about the dashes in Table 1 (lines 209, 216), but should more explicitly acknowledge that the weakly-supervised comparison rests on thin evidence and that re-implementing WS-DA across all horizons would be needed for a definitive claim.

- **No variance or confidence intervals reported.** Results are averaged over 4 (Breakfast) or 5 (50Salads) standard splits (Section 4.1, line 194), but no per-split standard deviations are reported. Without this, readers cannot assess whether observed differences — such as TbLTA's 0.58-point lead over ActFusion on Breakfast average — are statistically meaningful. This is standard practice in the field and should be included.

- **Stochastic sampling details deferred to supplementary.** The stochastic Top1 results (gray rows in Table 1) are clearly distinguished visually, and the asterisk notation is explained. However, the number of stochastic samples used and how Top1 is selected from the sampled set are not stated in the main text (Section 4.2, line 227 simply references "stochastic protocol of Abu Farha & Gall (2019) in the supp. mat."). Since the stochastic numbers (e.g., 37.15 on Breakfast average) are 28% higher than deterministic results (29.03), readers would benefit from knowing the sample budget in the main paper.

- **CTC loss notation inconsistency.** The text (Section 3.2.2, line 160) defines the segmentation head's predictions as π = [π₁, ..., π_{αT}] for the observed portion only, but Equation 4 (line 162) sums over t=1 to T (full video). The intended behavior is clear, but the notation should be consistent.

### Trivial

- **ATBA adaptation details.** The paper adopts ATBA (Xu & Zheng, 2024) for temporal alignment and states it "partition[s] the full transcript Y into observed and future sub-transcripts" (Section 3.1, line 126). However, the mechanism by which ATBA handles the boundary between observed and predicted video portions during alignment is not fully described. Since this is an adopted module, a brief clarification would suffice.

## Nice-to-Haves

- Expand the WS-DA comparison to all anticipation horizons by re-implementing under the same protocol, or clearly state this as a limitation of the current evidence.
- Add per-split standard deviations for all main results.
- Provide quantitative analysis (e.g., action segment length distributions, transition entropy across datasets) to explain why transcripts work well for Breakfast but poorly for 50Salads, beyond the current qualitative explanation.
- Add an ablation that replaces ATBA pseudo-labels with random/uniform labels to quantify dependence on alignment quality.

## Removed Points

The following points from inputs were removed with justification:

- **Missing loss weights (γ₁, γ₂, γ₃) and other hyperparameters**: Per hard rules, undisclosed hyperparameters that may reside in the appendix (stripped by the parser) are not valid criticisms. The paper states "More details in the supplementary material" for alignment loss specifics.
- **Duplicated tables (lines 259-269)**: Parser artifact — the original submission does not have this issue.
- **EGTEA framing criticism**: The paper accurately acknowledges the overall gap ("supervised models retain a clear edge overall") and only claims competitiveness on rare classes (60.11 vs 59.70/55.10), where the evidence supports it.
- **"Paper should ablate ATBA"**: This is a nice-to-have, not a weakness, since ATBA is an adopted module from prior work and the paper already ablates CTC, which partially tests alignment quality.
- **General reproducibility nitpicks about training details**: These fall under the hard rule removing trivial implementation nitpicks.

## Novel Insights

The merger of the two reviews surfaces an interesting tension not fully resolved by the paper itself: TbLTA works remarkably well on Breakfast (beating full supervision) but substantially worse on 50Salads and EGTEA. The harsh critic correctly notes this asymmetry, while the strength finder correctly notes the rare-class advantage. What neither review fully explores is whether the Breakfast result is a genuine advance or an artifact of the dataset's particular structure (short videos, strong procedural regularity, relatively few action classes) playing to the strengths of transcript supervision. A deeper analysis of when and why weak supervision succeeds or fails — rather than just averaging results across datasets — would substantively strengthen the paper's claims.

## Suggestions

1. Report per-split standard deviations (or error bars) for all main results in Table 1.
2. Explicitly state the number of stochastic samples used for Top1 evaluation in the main text.
3. Add a dedicated limitations paragraph that directly addresses the thin weakly-supervised comparison and the mixed results across datasets.
4. Clarify the CTC loss notation (Equation 4) to match the text-defined sequence length.
5. Provide a quantitative analysis of dataset characteristics (e.g., action segment length distributions, transition frequency) to contextualize the Breakfast vs. 50Salads performance gap.

## Score and Decision

**Calibration anchors retrieved (all rounds):**

*Round 1 — Bracketing (3 queries, 12 results):*

| Path | Avg Score | Comparison |
|------|-----------|------------|
| MSxCBXD5C8.md | 3.00 | Unrelated (anomaly recognition); clearly weaker |
| 2HdZPEQUig.md | 3.00 | Unrelated (object-centric); clearly weaker |
| bEvI30Hb2W.md | 3.00 | Unrelated (video reasoning); clearly weaker |
| TEjXRrhqtJ.md | 3.00 | Unrelated (video explanation); clearly weaker |
| Bb21JPnhhr.md (AntGPT) | 6.25 | LTA with LLMs, accepted; stronger empirical coverage |
| dl34rOnbqJ.md (Actions-to-Action) | 4.40 | Short-term anticipation, rejected; weaker novelty & ablation |
| r125wFo0L3.md | 5.00 | Unrelated (autonomous driving) |
| VYOe2eBQeh.md | 5.83 | Unrelated (robot action) |
| 9Cu8MRmhq2.md | 8.00 | Unrelated (video-language correspondence) |
| 5Ca9sSzuDp.md | 8.00 | Unrelated (CLIP interpretation) |
| weM4YBicIP.md | 8.00 | Unrelated (avatar generation) |
| QQ6RgKYiQq.md | 8.00 | Unrelated (dynamic radiance fields) |

*Round 2 — Narrowing (3 queries, 12 results):*

| Path | Avg Score | Comparison |
|------|-----------|------------|
| Bb21JPnhhr.md (AntGPT) | 6.25 | See above |
| dl34rOnbqJ.md (Actions-to-Action) | 4.40 | See above |
| GQgPj1H4pO.md (VidSGG) | 6.00 | Weakly supervised scene graphs, accepted; similar "first weakly-supervised" framing, stronger empirical results |
| HEXtydywnE.md (LASER) | 6.00 | Weakly supervised STSG, accepted; similar weakly-supervised framing with stronger results |
| f3CdjpPkSq.md (ActSeq) | 6.50 | Action anticipation data augmentation, accepted; less novel setting but stronger evaluation |
| JDd46WodYf.md (Active Planning) | 5.67 | Procedure planning, rejected; our paper has stronger empirical evidence |
| QETk0lBdVf.md | 5.80 | Unrelated (LMM long context) |
| DE2RMJVjgI.md | 4.25 | Weakly supervised TAL, rejected; clearly weaker |
| PageLgQlXz.md | 4.00 | Weakly supervised TAL, rejected; clearly weaker |
| HCoSsULNxG.md | 4.75 | Weak activity understanding, rejected; our paper stronger |
| o8SPZJaJyj.md | 4.00 | TAD domain adaptation, rejected; clearly weaker |

*Bracketing (Round 1):* Initial plausible range 3.0–8.0, narrowed by identifying the paper sits above rejected papers (4.0–4.75) but below accepted ones (6.0–6.5) on topically similar tasks.

*Narrowing (Round 2):* Comparison with accepted weakly-supervised papers (LASER 6.00, VidSGG 6.00) shows the paper is slightly weaker empirically (competitive on only 1/3 datasets at the deterministic level vs. their stronger coverage). Comparison with rejected papers (Actions-to-Action 4.40, Active Procedure Planning 5.67) confirms the paper has stronger contribution and evidence. AntGPT (6.25) achieves SOTA across all datasets with full supervision; our paper tackles a harder supervision regime but with weaker overall results.

**Final score: 5.5** — A genuine contribution (first weakly-supervised dense LTA) with compelling but incomplete evidence. The Breakfast result is impressive and the ablation is thorough. However, the thin weakly-supervised comparison, absence of variance reporting, and mixed results across datasets prevent the paper from reaching the level of the strongest accepted anchors.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Accept</decision>