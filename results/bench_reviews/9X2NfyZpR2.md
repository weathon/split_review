Now I have thorough calibration. Let me produce the final review.

## Summary

This paper introduces TbLTA, the first framework for dense long-term action anticipation (LTA) trained exclusively from video transcripts — ordered action lists without timing or duration information — eliminating the need for frame-level annotations. The architecture combines a transformer encoder with learnable class tokens, a weakly-supervised temporal alignment module (ATBA) for pseudo-label generation, cross-modal attention between transcript and video features, and an anticipation decoder with CRF-based sequence coherence. The model is evaluated on Breakfast, 50Salads, and EGTEA, establishing the first transcript-only LTA baseline and showing competitive results compared to fully supervised methods.

## Strengths

- **First transcript-only weakly-supervised LTA framework.** The paper is genuinely novel in proposing dense LTA under full weak supervision using only transcripts (ordered action lists without boundaries/timing). Prior work such as WS-DA (Zhang et al., 2021) still required frame-level labels for the observed segment. This is a well-motivated direction that could meaningfully reduce annotation costs.

- **Principled multi-component architecture.** The paper integrates several complementary mechanisms (CTC loss for global transcript consistency, ATBA-based alignment for pseudo-label generation, cross-modal attention for feature grounding, CRF-based coherence loss, self-supervised duration loss) into a coherent pipeline. The ablation discussion (though with missing tables) indicates each component contributes.

- **Establishment of transcript-only baselines on three benchmarks.** The paper provides the first results for transcript-only LTA on Breakfast, 50Salads, and EGTEA, creating a reproducible foundation for future work in this direction. Results on 50Salads (28.5 avg MoC) are competitive with fully supervised methods like ActFusion (28.39 avg).

## Weaknesses

### Fatal
None.

### Major

- **Missing TbLTA Breakfast results in the main comparison table (Table 1).** The paper claims "On Breakfast, TbLTA exhibits a pronounced gain at 30% observation, outperforming all supervised baselines," yet the Breakfast section of Table 1 (lines 484–489) contains rows only for Cycle Cons., FUTR, ActFusion, and WS-DA — no TbLTA row. The paper's central claim about competitiveness with, and superiority over, fully supervised methods on Breakfast cannot be verified from the presented data. This is not a parser artifact: the table structure is intact, and the TbLTA row is simply absent for Breakfast (the only TbLTA row shown is for 50Salads at lines 589–591, in what appears to be a separate ablation table). The text's quantitative claims about Breakfast are essentially unverifiable from the main paper.

### Minor

- **No fully supervised upper bound of the same architecture.** The comparison against fully supervised methods (ActFusion, FUTR) uses different architectures and training protocols. Without ablating the same TbLTA architecture with dense frame labels, it is unclear how much of the observed performance is attributable to the transcript-based supervision paradigm versus architectural design choices (pyramid hierarchical attention, CRF, cross-modal attention, etc.). A fully supervised ablation of TbLTA would cleanly isolate the cost of weak supervision.

- **Stochastic results claimed but not shown in the main paper.** The text states "we also report stochastic results, where TbLTA achieves substantially higher accuracy by capturing multiple plausible futures" and references a stochastic protocol "in the supp. mat." While deferring results to supplementary is acceptable, the main paper asserts "substantially higher accuracy" with no quantitative support, which weakens the in-paper experimental evidence.

- **Complex 3-stage training protocol not ablated.** The training involves pre-training (10 epochs), segmentation+alignment (30 epochs), and end-to-end optimization, with re-initialization of optimizer and schedule at each stage. The contribution of each stage and the necessity of re-initialization are not analyzed, making it difficult to assess the stability and necessity of this complex protocol.

- **Potential feedback loop in the affinity-based duration loss (Eq. 7).** The duration loss uses per-class duration estimates derived from the segmentation head's predicted pseudo-labels, which are themselves noisy. If the pseudo-labels have systematic alignment errors, the duration estimates could reinforce those errors. The paper does not analyze the sensitivity of this loss to pseudo-label quality.

### Trivial
None.

## Nice-to-Haves

- A fully supervised upper bound of TbLTA (retrained with dense frame labels) would cleanly decompose the supervision gap from the architecture gap.
- An analysis of pseudo-label quality (e.g., frame-wise pseudo-label accuracy vs. ground truth at different training stages) would clarify how alignment errors affect downstream anticipation.

## Removed Points
- **Missing ablation tables (Tables 3 and 4) and EGTEA results (Table 2) / missing qualitative figures (3a, 3b).** These are parser/stripping artifacts from the PDF extraction process. The original submission likely includes these; they are not author omissions.
- **Criticism that EGTEA results contradict the competitive claim.** The paper explicitly states that on EGTEA "supervised models retain a clear edge overall" and only claims competitiveness "on rare classes." The paper is honest about the EGTEA gap; the criticism misrepresents the paper's actual claim.
- **Formatting/style nitpicks and missing appendix content.** These are parser artifacts, not author errors.

## Novel Insights
None beyond the paper's own contributions.

## Suggestions

1. **Show TbLTA's Breakfast results in the main table.** This is the single most important fix. The current Table 1 must include a TbLTA row for Breakfast so that the central claim (competitive with/outperforming supervised methods on Breakfast) can be verified by readers. Without this, the paper's headline result remains unverifiable.

2. **Add a fully supervised TbLTA ablation.** Training the same architecture with dense frame labels would isolate the supervision gap and make the comparison with published fully supervised methods more rigorous.

3. **Show the stochastic results in the main paper, or refrain from making quantitative claims about them in the main text.** If the stochastic results are important enough to claim "substantially higher accuracy," they should appear in a main-paper table.

## Score and Decision

**Calibration anchors** (all from ICLR 2026 human-review corpus):

| Path | Avg Score | Comparison |
|------|-----------|------------|
| uKFVZMPppq (Action-Guided Attention for Video Action Anticipation) | 5.50 | Stronger experimental completeness; similar topic (action anticipation); had complete results in all tables |
| 3Genv8DQgf (EAST: Early Action Prediction) | 5.00 | Stronger experimental section; simpler method with clean evaluation; more thorough baselines |
| Vgh30npuN3 (CurvSeg: Skeleton Action Segmentation) | 5.00 | Thorough ablation experiments; clearer demonstration of each component's contribution |
| ENwxBjOlAR (VLPO: Weakly-Supervised Action Localization) | 4.00 | Withdrawn/Reject; less novelty than TbLTA; TbLTA's contribution is more novel (first vs. incremental) |
| xPBsWooORO (ActDR: Action Difference Reasoning) | 2.00 | Clear Reject; fundamental novelty and comparison issues; TbLTA is substantially stronger |

TbLTA's core contribution (first transcript-only LTA) is more novel than several accepted papers (AGA at 5.50, EAST at 5.00), but the missing Breakfast results in Table 1 represent a meaningful evidentiary gap that prevents full verification of a central claim. The paper sits below fully complete evaluations (5.00–5.50) but above papers with fundamental novelty or rigor issues (2.00–4.00).

MY FINAL SCORE: <pineapple>4.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>