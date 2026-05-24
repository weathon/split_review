Now I have thoroughly read the paper, verified each reviewer claim against the actual text, and calibrated against human-reviewed anchors. Let me construct the final consolidated review.

## Summary

This paper introduces TbLTA, the first weakly-supervised framework for dense Long-Term Action Anticipation (LTA) that trains exclusively from video transcripts (ordered action lists without timing or duration annotations). The approach combines: (1) a temporal alignment module (ATBA) to generate frame-level pseudo-labels, (2) cross-modal attention to ground video features in transcript semantics, (3) a CTC loss for transcript-level supervision, (4) a CRF loss for coherent future predictions, and (5) a self-supervised duration loss. Experiments on Breakfast, 50Salads, and EGTEA show that transcript-only supervision yields results competitive with fully-supervised methods on some benchmarks, particularly on Breakfast where TbLTA outperforms several fully-supervised baselines at 30% observation.

## Strengths

- **First weakly-supervised LTA paradigm with competitive results.** Table 1 shows TbLTA achieving 29.03 MoC (deterministic) on Breakfast, outperforming fully-supervised ActFusion (28.45), FUTR (26.59), and Cycle Consistency (25.13). This directly validates the central claim that transcript-only supervision can be a viable alternative to frame-level annotations for dense LTA.

- **Empirical validation of key architectural components.** The ablation study (Tables 3-4) causally links each design choice to performance: removing cross-attention drops Breakfast accuracy by ~5.7 points, removing the CRF loss reduces long-horizon accuracy by ~4.1 points, and removing the CTC loss degrades performance by ~0.8 points. These ablations convincingly show that the proposed mechanisms compensate for the lack of dense labels.

- **Corpus-level semantics help with rare-class imbalance.** On EGTEA (Table 2), TbLTA achieves 60.11 mAP on rare classes, outperforming fully-supervised Anticipatr (55.10) and Timeception (59.70). This provides concrete evidence that transcript-level supervision can mitigate data imbalance — a known failure point for label-dependent methods.

- **Dual evaluation protocol (deterministic + stochastic).** Following established LTA protocols, the paper reports both deterministic Top-1 and stochastic Mean/Top-1 metrics (Table 1), providing a complete picture of accuracy and diversity. The stochastic variant reaches 37.15 MoC (Top-1) on Breakfast.

- **Qualitative outputs confirm temporal coherence.** Figure 3 shows that the model produces structurally coherent segmentations during both observed and anticipation portions, indicating the model does not collapse to trivial predictions despite weak supervision.

## Weaknesses

### Fatal
None.

### Major
None. The paper's core claims are well-supported by the experimental evidence, and no methodological flaw invalidates the contribution.

### Minor

- **CRF supervision target is underspecified.** The CRF loss (Eq. 6) is defined as the negative log-likelihood of the "target anticipate transcript" 𝒴_LTA, but the paper never explicitly states whether this target is (a) the pseudo-labels from the ATBA module on the future portion, or (b) a transcript-derived sequence obtained through some other alignment. From context (Section 3: "These pseudo-labels supervis[e]... action anticipation labels Ŷ_LTA"), it appears the CRF target is indeed the pseudo-labels, but this should be stated clearly. If the target is the pseudo-labels, the CRF loss operates on the same noisy signal that already supervises the model through cross-entropy, raising the question of whether the benefit comes purely from the structural CRF bias or from something else. The paper should clarify this to allow readers to properly interpret the CRF ablation results.

- **Cross-attention mask construction is incompletely specified.** The binary local mask M in Eq. 1 is described only as restricting "each action a_i to a temporal neighborhood around its predicted occurrence." The neighborhood size (fixed or adaptive, relative or absolute) is never quantified. Since this mask directly controls which video segments each text embedding attends to, its specification is essential for reproducibility and for interpreting the cross-attention ablation.

- **No variance reporting.** All results in Tables 1-4 are reported as point estimates without standard deviations or per-split breakdowns, despite being averaged over 4 (Breakfast) or 5 (50Salads) splits. The large gain on Breakfast at Obs30%/10% (40.28 vs. 35.79 for ActFusion) stands out, and it is unclear whether this is consistent across splits or driven by a single favorable split. Variance estimates would substantially strengthen confidence in the reported improvements.

- **Missing training hyperparameters.** The paper specifies architectural details (number of layers, hidden dimensions, etc.) and the training schedule, but does not report the optimizer, learning rate, batch size, or weight decay. These are necessary for reproducibility and should be stated in the main text or supplementary.

### Trivial

- The claim that the paper "extend[s] the use of CTC-style objectives to the task of dense long-term anticipation" (Related Work) is slightly imprecise: the CTC loss is applied to the TAS head's predictions over the full video, not directly to the anticipation decoder. The distinction is minor but the wording could be tightened.

- The partition function computation for the CRF (forward algorithm) is not mentioned, though Eq. 6 implicitly assumes it.

## Nice-to-Haves

- **Run ablations on the deterministic variant.** The ablations (Table 4) are reported using the Top-1 MoC metric (stochastic protocol). Running ablations on the deterministic variant as well would allow readers to isolate architectural contributions from the effects of sampling.

- **Error analysis on 50Salads.** The deterministic model underperforms on 50Salads compared to fully-supervised methods. A breakdown of errors (e.g., per-class accuracy, confusion between misclassification vs. duration errors) would clarify the limitations of transcript-only supervision and guide future work.

- **Baseline: fully-supervised LTA trained on pseudo-labels.** Since the pseudo-labels come from the ATBA module, a direct baseline would be to take a fully-supervised LTA method (e.g., FUTR) and train it on the ATBA pseudo-labels alone. This would isolate the benefit of the additional losses (CTC, cross-modal, CRF) beyond the pseudo-label quality.

- **Qualitative failure cases.** Figure 3 shows successful predictions; including failure cases (e.g., where durations are severely mispredicted) would provide a more complete picture.

- **Computational cost.** The ATBA module involves dynamic programming; a brief note on training runtime would be useful.

## Removed Points

- *Criticism that ATBA partitioning procedure is not spelled out.* The paper explicitly references ATBA (Xu & Zheng, 2024) for these details; this is standard practice and not a flaw.
- *Criticism that the CRF partition function computation is not described.* Standard knowledge for readers familiar with CRFs; the forward algorithm is implied by the NLL formulation.
- *Criticism about "Table 3" reference missing from parsed content.* This is a parser artifact; the reference exists in the original submission.
- *Criticism about M^T dimensions in Eq. 2.* This is an implementation detail that the paper provides sufficient context for.
- *"The CTC-style objectives" overstatement.* The CTC loss is applied to the TAS head, which processes the full video (observed + future), so it does extend CTC usage to the LTA task context. The critic's reading is overly narrow.
- *Strength Finder strengths that are generic/superficial:* None identified — all five strengths listed are concrete and evidence-based.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

- Clearly state in Section 3.2.3 that the CRF target 𝒴_LTA is derived from the ATBA pseudo-labels on the future portion, and briefly discuss the implications of training a CRF against the same pseudo-labels used for cross-entropy supervision.
- Specify the cross-attention mask neighborhood size (e.g., "set to half the estimated segment length" or "fixed to 5 frames" — whichever was used).
- Add standard deviations or per-split results to Table 1, or at minimum discuss the variance of the key results.
- Include optimizer, learning rate, and batch size in the implementation details.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>