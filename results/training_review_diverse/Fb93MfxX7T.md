Now I have all the information needed. Let me synthesize the final review.

## Summary

This paper presents a systematic empirical study of 14 parameter-efficient transfer learning (PETL) methods for Vision Transformers across low-shot (VTAB-1K), many-shot (CIFAR-100, RESISC, Clevr-Distance), and distribution-shift (CLIP + ImageNet variants) settings. Its core contributions are a unifying evaluation framework, empirical recommendations for practitioners, and new insights about PETL's complementary predictions, many-shot effectiveness, and robustness preservation. The paper is explicitly positioned as a benchmark/empirical study rather than a technical novelty contribution.

## Strengths

- **Unified hyperparameter tuning reveals similar accuracy across diverse PETL methods, overturning prior claims of inferiority for simple methods.** Table 1 reports low relative standard deviations across 14 methods within each VTAB-1K group (0.54% Natural, 0.94% Specialized, 1.09% overall), and shows that simple methods like BitFit and NLP-originated methods like LoRA/Adapter are competitive with vision-specific PETL approaches under careful tuning. This provides the community with a reliable accuracy reference.

- **PETL methods make diverse predictions despite similar average accuracy, enabling consistent ensemble gains.** Prediction similarity matrices (Figure 3) show ~20-35% prediction differences across methods on DTD, Retinopathy, and DMLab. The ensemble experiment (Figure 4) demonstrates consistent gains, and the Venn analysis (Figure 3b) shows limited overlap in high-confidence correct and low-confidence wrong predictions among LoRA, Adapter, and SSF. This opens up a novel direction for complementary PETL learning.

- **PETL matches or beats full fine-tuning in many-shot regimes with far fewer parameters.** Figure 6 shows that on CIFAR-100 (50K images), RESISC (25K images), and Clevr-Distance (70K images), PETL methods with only 2-5% of ViT-B/16 parameters achieve accuracy comparable or superior to full fine-tuning. PETL notably outperforms full fine-tuning on CIFAR-100, suggesting it better preserves pre-trained knowledge even with ample data.

- **PETL better preserves robustness to distribution shifts than full fine-tuning.** Table 2 reports that on 100-shot ImageNet fine-tuned from CLIP ViT-B/16, PETL methods achieve 54.7-56.9 average distribution-shift accuracy vs. 42.5 for full fine-tuning — a 12-14 point gain. This supports the claim that PETL preserves pre-trained robustness by updating only a small fraction of parameters.

- **Conceptual analysis of why PETL works through two distinct regimes.** Section 6 identifies case (1) where full fine-tuning beats linear probing (backbone needs updating) and case (2) where linear probing beats full fine-tuning (pre-trained features are strong). PETL outperforms both in low-shot settings, matches full fine-tuning in many-shot case (1), and exceeds it in case (2), supporting the interpretation of PETL as a "high-capacity regularizer." Domain affinity analysis (Figure 2) further provides practical guidance on when to use simpler vs. more complex PETL methods.

## Weaknesses

### Fatal
None.

### Major
None. The identified weaknesses are addressable in revision and do not invalidate the paper's core contributions.

### Minor

- **WiSE robustness analysis lacks tabular results for PETL+WiSE.** The paper claims that weight-space ensembles (WiSE) can be applied to PETL and that "full fine-tuning with WiSE can achieve even higher accuracy ... than PETL" (Section 7), but Table 2 shows only non-WiSE results. Figure 1(b) appears to show PETL+WiSE and Full+WiSE data points visually, but without numerical values in the table, readers cannot independently verify the magnitude of the claimed effect. The main claim about WiSE overturning PETL's robustness advantage needs tabular support to be fully credible as a reference result. This is the paper's weakest evidential point.

- **Hyper-parameter search ranges are not specified in the main paper.** The paper states that learning rate, weight decay, drop path rate, and method-specific parameters were tuned, and that a ≤1.5% parameter cap was used (Section 3). However, the search ranges for learning rate and weight decay, the specific drop path choices beyond "e.g., 0.1," and how method-specific parameters (e.g., bottleneck dimension, rank) were explored within the cap are deferred to supplementary material. As a benchmark paper intending to serve as a reference, summarizing the search space in the main text would better support the "careful tuning" premise.

- **The "similar accuracy" claim is not qualified regarding the parameter cap.** The paper concludes that PETL methods achieve "quite similar accuracy" based on low relative standard deviations. This claim is conditioned on the ≤1.5% parameter cap, yet the discussion briefly acknowledges that more parameters help in specialized/structured groups (Figure 2 ranking analysis). The paper should explicitly note that similarity holds under the chosen budget and that relaxing the cap might widen gaps, especially on far-domain tasks.

- **Ensemble baseline inflates apparent gain.** The ensemble experiment (Figure 4) uses the worst PETL method as the baseline (explicitly stated in the text). While this choice is transparent, it overstates the practical gain a practitioner would see from ensembling. A baseline using the average or best single method would give a more calibrated picture.

- **Prediction diversity analysis does not control for within-method variance.** The similarity analysis (Figure 3) compares predictions across different PETL methods but does not compare against the diversity produced by training the same method with different random seeds. Without this control, it is unclear how much of the observed diversity is genuinely due to different inductive biases vs. stochastic training noise. This weakens the complementarity conclusion.

- **Many-shot results lack variance information.** Figure 6 appears to plot single data points per condition without error bars or multiple seeds. Given the importance of the many-shot claim, the absence of variance information reduces the reliability of the plateau observation (diminishing returns after 2-5% parameters).

- **Limited many-shot dataset coverage.** Only three datasets are used, all from VTAB-1K (CIFAR-100, RESISC, Clevr-Distance). The paper notes this implicitly but could more clearly acknowledge that the many-shot findings are preliminary and would benefit from verification on larger-scale settings (e.g., full ImageNet-1K fine-tuning).

- **Distribution-shift results report only average accuracy.** Table 2 shows the average across ImageNet-V2, -R, -S, -A. Per-dataset numbers would allow readers to assess whether PETL's robustness advantage is consistent across shift types or driven by a subset.

### Trivial
None.

## Nice-to-Haves

- Add PETL+WiSE numerical results to Table 2 (or a companion table) to fully substantiate the WiSE claims.
- Report variance over multiple seeds (e.g., 3 runs) for key tables and figures, especially the many-shot and VTAB-1K results.
- Add a short paragraph in Section 3 summarizing the hyper-parameter search space (learning rate range, weight decay range, key method-specific parameter choices).
- Include per-dataset distribution-shift accuracy (V2, R, S, A) either in Table 2 or as supplementary.
- Compute a quantitative diversity metric (e.g., pairwise prediction disagreement rate) for the complementarity analysis and compare it to within-method seed variation.
- Add an explicit qualifier that the "similar accuracy" claim is conditional on the ≤1.5% parameter budget.

## Removed Points

These points are flagged to be removed; treat them with caution.

1. **"Figure 1a caption should note that the range comes from the 14 PETL methods, not from all possible configurations."** — The caption already states "red ●-● for the range from the most to the least accurate methods." Already addressed in the paper.

2. **"The color-coded cell grouping in Table 1 is explained only in the caption and Section 6; it would help to flag the meaning in the table itself."** — Pure presentation nitpick; the caption and Section 6 reference provide adequate explanation.

3. **"The observation that drop path is important is mentioned but not quantified. A small ablation would strengthen the claim."** — Nice-to-have, not a weakness. The paper is a broad benchmark, not an ablation study on a single technique.

4. **"Venn diagrams are suggestive but qualitative."** — The paper already provides the quantitative similarity matrices (Figure 3a); the Venn diagrams are a complementary visualization.

5. **"Missing analysis of computational cost (FLOPS, memory)"** — The paper explicitly scopes this out ("What do we not investigate?", line 85). Evaluating against wrong expectations.

6. **"Strength Finder's claim about WiSE for PETL"** — This strength (that the paper "investigates WiSE for PETL and reveals WiSE further improves PETL robustness") conflicts with the verified weakness that PETL+WiSE results lack tabular support. Per rules, the weakness prevails. The paper does discuss WiSE conceptually but provides insufficient numerical evidence for the strength claim.

7. **"No significance tests"** — Not standard for large-scale benchmark papers in this setting; single-run evaluation is the norm for VTAB-1K.

8. **"Limited many-shot coverage (3 datasets)"** — Already retained as a minor weakness; the Harsh Critic's additional framing as a major gap is scope creep since covering more datasets would be a different paper.

## Novel Insights

The most novel finding to emerge from the review process (and one that the paper communicates clearly) is the combination of two observations that initially appear contradictory: PETL methods achieve near-identical accuracy when tuned carefully, yet they systematically disagree on individual predictions. This tension — uniform performance, diverse behavior — is genuinely interesting and opens up practical ensemble strategies and theoretical questions about inductive bias in fine-tuning. The domain-affinity rule (simple methods for close domains, complex methods for distant domains) is also a practically useful guideline distilled from the ranking analysis. The observation that PETL's many-shot effectiveness rivals full fine-tuning with far fewer parameters is valuable for practitioners but less surprising given similar findings in NLP.

## Suggestions

1. **Add a table or table rows showing PETL+WiSE and Full+WiSE numerical results** to fully support the WiSE claims in Section 7. This is the single highest-leverage improvement for credibility.

2. **Add a brief "Hyper-parameter Search Protocol" paragraph in Section 3** listing search ranges for learning rate, weight decay, and method-specific parameters, to support the "careful tuning" premise and strengthen the paper's value as a reference.

3. **Add a diversity control experiment**: compute prediction disagreement between runs of the same PETL method with different random seeds, and compare it to cross-method disagreement. This would substantially strengthen the complementarity claim.

## Score and Decision

This is a solid and well-scoped empirical study that provides genuine value to the vision community as a reference for PETL methods. The experimental design is generally sound, the coverage (14 methods across 27+ datasets) is impressive, and the main findings are well-supported. The most significant weakness — missing tabular results for the WiSE analysis — is addressable in revision and does not undermine the paper's core contributions (unified comparison framework, complementarity insight, many-shot effectiveness, robustness preservation). The paper is clearly written and honestly scoped.

I recommend acceptance. The weaknesses are all in the minor-to-nice-to-have range; none threaten the central claims.

MY FINAL SCORE: <pineapple>7.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>