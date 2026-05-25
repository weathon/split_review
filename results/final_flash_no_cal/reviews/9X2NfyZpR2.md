Now I have a thorough understanding of the paper. Let me synthesize the final consolidated review.

## Summary

This paper introduces TbLTA, the first long-term action anticipation (LTA) framework trained exclusively from video transcripts — ordered action lists without temporal boundaries or durations. The architecture uses an encoder-decoder with a weakly-supervised temporal alignment module (ATBA) to generate dense pseudo-labels, cross-modal attention to ground video features in transcript semantics, and multiple structured losses (CTC, CRF, duration) to learn anticipation without frame-level supervision. Results on Breakfast, 50Salads, and EGTEA show that transcript-only supervision can be competitive with fully-supervised methods on certain benchmarks, and substantially outperforms the only prior (semi-)weakly-supervised LTA method.

## Strengths

- **First transcript-only LTA approach with competitive results.** The paper proposes the first method for dense LTA that requires only transcript-level annotations (no boundaries, no durations). On Breakfast, the deterministic TbLTA achieves an average MoC of 29.03 vs. the best fully-supervised method (ActFusion, 28.45), and at 30% observation / 10% horizon it reaches 40.28 vs. ActFusion's 35.79 (Table 1). These results demonstrate that transcript-based supervision can, in certain settings, match or exceed fully-supervised performance.

- **Thorough ablation study validates each architectural component.** Table 4 systematically ablates the CRF loss, cross-attention, and duration loss, showing non-trivial contributions from each (e.g., removing CRF causes a ~5.3-point drop on 50Salads at 50% horizon; removing cross-attention drops ~5.7 on Breakfast average). The ablations establish a clear hierarchy: w/o cross-att < cross-att simplex < full TbLTA.

- **Substantial improvement over prior weakly-supervised LTA.** On Breakfast at 30% observation, TbLTA achieves 40.28 vs. WS-DA (Zhang et al., 2021) at 15.65 — a >24-point gap. This firmly establishes a new state-of-the-art for the weakly-supervised LTA setting.

- **Competitive rare-class performance on EGTEA.** TbLTA achieves 60.11 mAP on rare classes, outperforming fully-supervised Timeception (59.70) and Anticipatr (55.10) (Table 2), demonstrating that transcript-level semantic supervision can mitigate data imbalance.

- **The CTC + pseudo-label combination for LTA is novel and empirically useful.** Applying CTC to supervise the TAS head against transcript-level pseudo-labels, as a bridge between weak and dense supervision, is a clean design. The ablation confirms a ~0.6–0.8 point drop when removed.

## Weaknesses

### Major

- **The ATBA temporal alignment module is critically underspecified.** The paper states that ATBA "partition[s] the full transcript Y into observed and future sub-transcripts" (Section 3.1) and obtains pseudo-labels "via dynamic programming over candidate boundaries" (Section 3.2.1), but it never explains: (a) whether the known observation proportion α is used as a hard split or if the boundary k* is estimated purely from video-transcript alignment, (b) how ATBA behaves at inference when only X_obs is available — does it still generate pseudo-labels for the observed portion to drive the cross-modal attention mask and TAS head? (c) what accuracy the boundary estimation achieves. Since the entire pipeline (pseudo-labels, cross-attention mask, CTC supervision) depends on this module, the lack of specificity makes the core methodology difficult to fully evaluate and reproduce.

- **The full-video encoder training creates a training/inference gap that is acknowledged but never analyzed or ablated.** The encoder processes the entire video X = [X_obs, X_pred] during training (line 122) but only X_obs at inference. The ATBA module uses the full video features to generate future pseudo-labels Y_hat_pred, which then supervise the decoder. The paper notes this follows Gong et al. (2024), but this design choice has different implications in the weakly-supervised setting: the decoder is trained to match pseudo-labels that were informed by future video features, while at inference it must anticipate without them. The paper does not ablate this protocol (e.g., training the encoder only on X_obs), leaving open the question of how much of the reported performance depends on this future-informed training signal. This is a meaningful gap that should be addressed with a diagnostic experiment.

### Minor

- **No oracle upper bound or pseudo-label quality analysis.** The paper relies entirely on ATBA pseudo-labels but never measures their frame-wise accuracy against ground truth. Without this, the reader cannot assess whether transcript-only supervision is genuinely driving performance or the pseudo-labels are approaching ground-truth quality. An oracle experiment (TbLTA trained with ground-truth dense labels instead of pseudo-labels) would clarify whether the method's remaining gap relative to fully-supervised methods is due to pseudo-label noise or architectural constraints.

- **Stochastic results reported without variance.** The stochastic (Top-1 MoC) results in Tables 1 and 4 have no standard deviation, confidence intervals, or any indication of how many samples were drawn and how stable the Top-1 metric is. This makes it impossible to assess whether the reported advantages are reliable or driven by outlier samples.

- **The "competitive with fully-supervised" framing is uneven across datasets.** On Breakfast the deterministic model is genuinely competitive (avg 29.03 vs. ActFusion 28.45). On 50Salads the deterministic model is far behind (20.92 vs. ActFusion 28.39), which the paper acknowledges but still foregrounds the "competitive/superior" narrative. The EGTEA results show TbLTA trailing by 9–11 points on All and Freq metrics. The claim is technically accurate (it is competitive in some settings) but the presentation could more prominently caveat the settings where it is not.

### Trivial

None.

## Nice-to-Haves

- **Ablation of the full-video training protocol.** Training the encoder on X_obs only (both for the TAS head and the decoder supervision) would isolate the contribution of this design choice directly.
- **Pseudo-label accuracy analysis.** Reporting frame-wise accuracy of ATBA pseudo-labels against ground truth (on the training set) would clarify the gap between weak and strong supervision.
- **Oracle experiment with ground-truth labels.** Training TbLTA with dense ground-truth labels in place of pseudo-labels would establish an upper bound and reveal how much room for improvement remains from pseudo-label noise alone.
- **Variance reporting for stochastic protocol.** Standard deviation or inter-quartile range across runs/samples for the stochastic results.
- **Analysis of the cross-attention mask.** The binary local mask M is constructed from pseudo-labels — how sensitive are results to the mask bandwidth? A brief sensitivity study would strengthen the cross-attention contribution.

## Removed Points

These points from the inputs are removed with justification:

- **"Information leak invalidates the fully-supervised comparison" (Harsh Critic #1).** Removed because: (a) the paper explicitly cites Gong et al. (2024) — the strongest supervised baseline (ActFusion) — as precedent for full-video training (Section 1, line 29); (b) the decoder operates exclusively on observed features $\tilde{F} \in \mathbb{R}^{T_{obs} \times d_{TAS}}$ (Section 3.1, Anticipation Decoder), so it does not receive future features directly; (c) the training/inference gap is real and should be studied, but characterizing it as a "structural flaw that invalidates" the comparison is an overstatement — the comparison follows standard protocol in the field and the paper acknowledges the design choice. This is retained as a **Major** weakness (above) in a properly contextualized form.

- **"Evaluation mixes incompatible protocols across tables" (Harsh Critic #2, part about protocol switching).** The paper is transparent: Table 1 separates deterministic (main) and stochastic (supplementary) results with clear labels and a footnote. The ablations use stochastic Top-1 as noted ("for clarity, we adopt this choice Top-1 MoC for ablations as it provides a stable reference point"). This is a reasonable methodological choice for relative comparison. The lack of variance on stochastic results is kept as a Minor weakness.

- **"Table formatting overstates results" (Harsh Critic, Table 1 complaint).** The bolding follows the caption rule ("highest accuracy under a deterministic framework is indicated in bold"). TbLTA is bolded where it achieves the best score, which is factually accurate. No visual overstatement.

- **"The encoder is trained over the entire video sequence... baselines do not have this" (part of Harsh Critic #1).** ActFusion (Gong et al., 2024), the strongest baseline, unifies TAS and LTA and thus processes the full video during training — the paper explicitly follows this protocol. The critic's claim that all baselines "train their encoder solely on the observed portion" is not verifiable for ActFusion given the paper's citation.

- **"Strawman about pseudo-label quality" (Strength Finder #1, "competitive with fully-supervised").** The strength is factually supported by Table 1 data; the critic's suggestion that the comparison is invalid due to information leak is addressed above.

- **Generic/superficial strengths from Strength Finder.** Points like "this paper addressed an important problem" are removed as non-specific.

## Novel Insights

None beyond the paper's own contributions. The review does not surface a genuinely novel observation about the method that the paper itself does not make.

## Suggestions

1. **Specify the ATBA boundary estimation procedure.** Clarify whether αT is used as a hard constraint for the observed/predicted split, how the boundary k* is estimated during training and inference, and provide quantitative analysis of boundary prediction accuracy.
2. **Ablate the full-video training protocol.** Run a variant where the encoder is trained only on X_obs (disabling future-frame access during training) to quantify the contribution of this design choice.
3. **Add an oracle upper bound.** Replace pseudo-labels with ground-truth dense labels in TbLTA's training pipeline and report the resulting performance — this tells the reader how much of the gap to fully-supervised methods is due to pseudo-label noise vs. architecture.
4. **Report variance for stochastic results.** Add standard deviation or confidence intervals for the Top-1 MoC metric across multiple stochastic samples.
5. **Tone down the "competitive with fully-supervised" framing slightly.** The paper already qualifies this in Section 4.2 (the 50Salads discussion), but the abstract and conclusion could more explicitly note that the advantage is dataset/horizon-dependent.

## Score and Decision

This paper makes a genuine contribution by introducing the first transcript-only dense LTA framework. The experimental validation is broad (three benchmarks, multiple observation/horizon settings), the ablations are thorough, and the core idea (transcript-based pseudo-labeling + cross-modal attention + structured prediction losses) is well-motivated and effective in certain settings. However, the paper has two significant methodological gaps: (1) the critical ATBA boundary estimation procedure is underspecified, and (2) the full-video training protocol's implications for the weakly-supervised setting are not analyzed. These do not invalidate the contributions but do prevent full evaluation of the method's soundness. The paper would benefit from addressing these before publication.

Score: 6.5

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>