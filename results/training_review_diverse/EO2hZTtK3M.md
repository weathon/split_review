Now I have thoroughly verified the paper's content against all reviewer claims. Let me produce the final consolidated review.

## Summary

This paper proposes CM², a framework for Audio-Visual Speech Enhancement (AVSE) that integrates two types of contextual information—semantic context (via visual speech recognition or pre-trained AV models) and signal context (via bidirectional Mamba sequence modeling)—inspired by the phonemic restoration phenomenon in human hearing. The method also explicitly models correlations between visual features and audio frequency characteristics through a Cross-Context Fusion Module (CCFM) with both time-domain and frequency-domain fusion. The paper reports strong results on the LRS3+DNS4 dataset, particularly under very low SNR conditions.

## Strengths

- **Novel integration of dual contextual cues grounded in a cognitive principle.** Drawing a direct parallel between phonemic restoration in human auditory processing and the need for both semantic-level and signal-level context in AVSE is a genuinely novel framing. The paper's architecture (SeCM for semantic context, SiCM for signal context) operationalizes this insight in a concrete, nontrivial way.

- **Explicit modeling of visual–frequency correlations, an underexplored direction in AVSE.** The paper correctly identifies that most prior AVSE methods fuse modalities only along the temporal dimension. The CCFM's design, with separate time-domain and frequency-domain fusion blocks that operate on the upsampled semantic context, addresses this gap.

- **Strong empirical results on the reported dataset.** On LRS3+DNS4, CM² achieves substantial improvements over prior SOTA across all metrics and SNR levels. The improvements at −15 dB SNR (SDR +63.6%, PESQ +58.1%, STOI +20.3% relative) demonstrate that the contextual modeling is most beneficial where it is most needed.

## Weaknesses

### Major

- **Results on only 1 of 4 claimed datasets are presented, undermining the generality claim.** The abstract states "Comprehensive evaluations across various datasets" and the third contribution claims "Comprehensive evaluations on four composite datasets clearly show the advantages of our work." Section 4.1.1 lists four dataset pairs (LRS3+DNS4, GRID+CHiME3, TCD-TIMIT+NTCD-TIMIT, MEAD+DEMAND), but Section 4.1.1 admits "Due to space constraints, we only present the experimental results on the widely-used LRS3+DNS4 dataset here." No results for the other three datasets appear anywhere in the submission. The advertised claim of multi-dataset evaluation is therefore unsupported in this submission. This is the single most significant gap: without evidence that the method generalizes beyond one dataset, a core claim of the paper is unverifiable.

- **Potential comparison unfairness from mismatched training conditions.** The method is trained on SNR −15 to 0 dB and evaluated at −15, −10, −5, 0 dB—the training and test ranges are identical. Baseline methods may have been trained on substantially different ranges (e.g., −5 to 20 dB), which would put them at a systematic disadvantage at extreme SNRs, especially −15 dB where the largest gains are reported. The paper does not state whether baselines were retrained under matched conditions or whether published numbers are taken as-is. Given the 63.6% relative SDR improvement at −15 dB, this is not a minor concern—it is necessary to establish whether the gains reflect architectural merit or a home-field advantage in training distribution.

### Minor

- **Ablation for semantic context does not isolate the "semantic" component from visual features generally.** Table 2 compares an AOSE baseline (no visual input) against SeCM variants (with visual features). The improvement attributed to "semantic context" conflates the benefit of any visual information with the benefit of semantically-structured visual features. Table 1 already shows CM² outperforming prior AVSE methods that use standard visual features, which provides indirect support, but the dedicated ablation (Table 2) does not include a comparison against a version with a standard visual front-end (e.g., 3D Conv + ResNet without the SeCM architecture) to isolate the semantic-specific contribution.

- **Signal context ablation compares two sequence models, not the presence vs. absence of signal context.** Table 4 compares BiMamba vs. Conformer within SiCM. This tests which sequence model works better, but does not test whether "signal context as a distinct conceptual type" adds value beyond what a standard temporal processing block already provides. A comparison against a version with no explicit sequence modeling (e.g., purely convolutional temporal processing) would substantiate the claim that signal context is a distinct and necessary component.

- **No ablation removing the frequency-domain fusion block from CCFM.** The paper claims that incorporating visual information in the frequency domain is critical, yet there is no experiment comparing the full CCFM against a version with time-domain fusion only.

- **No controlled re-implementation of baselines.** The paper does not clarify whether competing methods were retrained under the same data splits, training budget, and loss functions, or whether numbers are taken from published tables. Differences in training setup can produce large gaps independent of architectural contributions.

- **No variance or confidence intervals reported.** Given the magnitude of the claimed improvements (63.6% SDR increase), reporting single-run results without variance is insufficient to assess reliability.

- **No discussion of computational cost.** The paper does not report model size, FLOPs, or inference speed, which matters for practical applicability given the complex multi-module architecture.

### Trivial

- **Imprecise claim about surpassing DualAVSE at 0 dB.** Section 4.2.1 states "Our enhancement results at −15 dB even surpass those achieved by the DualAVSE method at 0 dB." According to Table 1, SDR at −15 dB (9.33) does not surpass DualAVSE at 0 dB (9.68); only PESQ and STOI do. The statement should be qualified to reflect which metrics surpass.

- **Loss weights (α=0.9, β=0.1, γ=0.05) reported without sensitivity analysis.** The paper states these are "chosen to achieve equal importance" without supporting analysis.

- **Varying optimal SeCM encoder layer across metrics and SNRs (Table 3).** The paper notes the variation and suggests combining layers but does not test this, leaving the design choice ambiguous.

## Nice-to-Haves

- Results on the three omitted dataset pairs (GRID+CHiME3, TCD-TIMIT+NTCD-TIMIT, MEAD+DEMAND) would substantiate the generality claim.
- A controlled re-implementation of at least one prior method under the paper's training setup would clarify whether the reported gains are architectural or due to training conditions.
- An ablation with a standard AVSE visual front-end (no SeCM) to isolate the semantic-context contribution.
- An ablation that removes the frequency-domain fusion path from CCFM.
- Reporting variance across multiple runs for at least one SNR level.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **"Garbled text in phrasing":** The critic notes `"currently unobtainable metrics – currently unobtainable"` as garbled. This is a parser artifact, not an author error. → Removed per formatting artifact rule.

- **"Strength: Systematic ablation validation of each proposed component":** The Strength Finder claims the ablation is systematic. Since verified weaknesses show the ablations do not fully isolate the claimed contributions, this strength conflicts with verified weaknesses. Per rules, the weakness wins. → Moved to Removed Points.

- **"Strength: Adoption of a modern sequence-modeling architecture (Bidirectional Mamba)":** Using BiMamba is an architectural choice but the claim of superiority is supported only by a comparison with Conformer, not against a no-sequence-modeling baseline. The strength is generic and lacks an isolated evidence chain. → Moved to Removed Points.

- **"Strength: Careful design of the Cross-Context Fusion Module (CCFM)":** This describes the method rather than evaluating its demonstrated effectiveness. No evidence beyond the method description itself supports this as a distinct strength. → Moved to Removed Points.

## Novel Insights

None beyond the paper's own contributions. The reviews surface useful concerns about experimental rigor but do not identify novel scientific insights about the work that the paper itself does not already articulate.

## Suggestions

1. Add the results on the three missing dataset pairs. This is the single most important improvement—it directly addresses whether the method generalizes.
2. Retrain at least one baseline method under the same training SNR range (−15 to 0 dB) to control for training distribution effects.
3. Add an AVSE ablation baseline without the SeCM (standard visual front-end) to isolate the semantic-context contribution.
4. Add an ablation that removes the frequency-domain fusion block from CCFM.
5. Report variance (e.g., 95% CI or std across 3+ runs) for at least one SNR level.
6. Report model size (parameters) and FLOPs for practical context.

## Score and Decision

The paper introduces a well-motivated architecture with a novel cognitive inspiration and achieves strong results on the one dataset it reports. However, the paper claims comprehensive evaluation on four datasets but presents results for only one, making the generality claim unverifiable in this submission. Combined with the potential training-distribution advantage at low SNRs and the incomplete ablation isolation, the paper as submitted does not provide sufficient evidence to support its strongest claims. The core ideas are promising, but the experimental validation is substantially incomplete.

**Score:** 4.5/10
**Decision:** Reject

MY FINAL SCORE: <pineapple>4.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>