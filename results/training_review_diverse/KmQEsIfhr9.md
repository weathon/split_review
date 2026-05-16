Now I have all the information needed. Let me synthesize the final consolidated review.

## Summary

This paper presents a systematic empirical study of backdoor sample detection for CLIP, demonstrating that backdoor-poisoned images in CLIP training data exhibit uniquely sparse local neighborhoods in representation space — making them detectable by simple density-ratio-based outlier detectors (SLOF, DAO, k-dist) with near-perfect AUC (>97%) across diverse trigger types. The authors further show that filtering out detected outliers yields an effective defense (ASR <1% for most triggers), that detection scales to million-scale datasets (~15 min on 4 A100s for CC3M), and — most strikingly — that an unintentional natural backdoor already exists in the CC3M dataset and has propagated into a widely-used OpenCLIP model. The paper's contribution is primarily empirical: it identifies the underlying structural cause (sparsity from low poisoning rates), validates it across a wide range of attacks and architectures, and provides a practical, scalable solution.

## Strengths

1. **Systematic characterization of CLIP backdoor sample geometry.** The paper identifies and rigorously demonstrates the core insight — that CLIP backdoor samples have far sparser local neighborhoods than clean samples due to extremely low poisoning rates (~0.01%). The t-SNE visualization (Figure 1a) and controlled k-dist experiment (Figure 1b) make this finding concrete and intuitive.

2. **Near-perfect detection across diverse attacks.** Table 1 shows SLOF and DAO achieve AUC >97% across 8 attack settings (Patch, Blend, SIG, Nashville, WaNet, BLTO, multi-trigger, clean-label, TDPA) for both RN50 and ViT-B-16, vastly outperforming dedicated backdoor detection methods SafeCLIP, ABL, and CD (which range from 48–85% AUC). The comparison is thorough and the performance gap is decisive.

3. **Practical scalability.** The 15-minute runtime for CC3M (~3M images) on 4 A100 GPUs versus 4.1 hours (ABL) and 11.2 hours (CD) demonstrates order-of-magnitude efficiency gains that make real-world deployment feasible.

4. **Discovery of an unintentional backdoor in real-world data.** Section 5.3 identifies 798 near-identical images (0.03% of CC3M) with caption "the birthday cake with candles in the form of number icon" that form a natural backdoor, confirmed by trigger recovery achieving 92–99% ASR on both the authors' model and a released OpenCLIP model. This finding has significant implications for data curation practices.

5. **Defense effectiveness through simple filtering.** Removing 10% of data ranked by DAO reduces ASR to <1% for most triggers (Table 2) while maintaining clean accuracy, confirming the practical utility of detection-based purification.

6. **Label-agnostic operation.** Unlike ABL and CD, SLOF and DAO operate purely on representation distances without requiring labels, making them directly applicable to CLIP's self-supervised setting.

## Weaknesses

### Fatal

None.

### Major

None. The paper's core claims are well-supported by the experimental evidence. The weaknesses below are addressable gaps in presentation and experimental transparency, not structural flaws.

### Minor

1. **Missing variance/error bars for AUC results.** Table 1 reports point estimates of AUC without standard deviations, confidence intervals, or indication of the number of independent runs. Because the detection procedure involves random sampling ("We randomly sample a batch of data from the dataset," Section 4.3), the results have inherent stochasticity. While the performance margins are large enough (97–99% vs. 48–85%) that variance is unlikely to overturn the main conclusions, the absence of any variability measure prevents the reader from assessing the stability and reliability of the reported numbers. This should be addressed with at minimum standard deviations over multiple seeds or bootstrap estimates.

2. **Poisoning rates not reported in Table 1.** The table caption states that poisoning rates were "minimized based on a coarse grid search to guarantee a non-trivial attack success rate," but the actual rates used for each trigger are not listed in the table or its nearby text. The paper states that 0.01% is used for the patch trigger and TDPA, but the rates for Blend, SIG, Nashville, WaNet, BLTO, and multi-trigger settings are absent. Since poisoning rate directly affects detection difficulty, these should be reported alongside the AUC values in or adjacent to Table 1.

3. **Detection procedure underspecified in main text.** Section 4.3 describes the detection pipeline at a high level ("randomly sample a batch of data from the dataset and then apply outlier detection methods") but does not state the batch size used for detection experiments, whether scores are aggregated across multiple batches, or whether the 15-minute runtime includes representation extraction vs. only the detection step. Some of these details were deferred to an appendix (indicated by stripped footnote markers), but the main text should be self-contained on these crucial operational parameters. A concise algorithm or pseudocode would resolve this.

4. **Trigger recovery adaptation not explained.** Section 5.3 describes the recovery method only as "an adapted trigger recovery method based on Neural Cleanse" without specifying the adaptation. Given that Neural Cleanse was designed for supervised classification with discrete labels, its adaptation to the multi-modal contrastive setting is non-trivial and should be described. This is important because the unintentional backdoor finding is one of the paper's most noteworthy contributions.

5. **Missing discussion of adaptive adversaries.** The paper does not discuss the scenario where an adversary, knowing about sparsity-based detection, deliberately spreads backdoor representations (e.g., by using multiple distinct triggers or varying the trigger's location/appearance across poisoned samples). This could potentially violate the sparsity assumption that underlies the method. A brief limitations paragraph addressing this would strengthen the paper.

### Trivial

- The connection between the formal LID definition (Theorem 1) and the MLE estimator used in experiments is not made explicit. A brief bridging sentence would help.

## Nice-to-Haves

- An ablation on the choice of representation layer (e.g., confirming that the encoder output layer is not critical and early-layer features do not show the same sparsity) would strengthen the understanding of why the method works.
- Showing that the detected "birthday cake" images are consistently scored as extreme outliers by SLOF/DAO, and that removing them reduces the learned backdoor upon retraining, would further solidify the unintentional backdoor finding.
- An ablation on batch size used during detection would demonstrate that the method does not require careful tuning of this hyperparameter.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **Criticism about missing appendix/footnoted details (batch size, experimental settings):** The paper contains stripped footnote markers (".1", ".2", etc.) referencing an appendix/footnotes with experimental details that existed in the original submission. The parser stripped these. Criticisms that rely on information that was deferred to the appendix are not attributable to the authors.
- **Criticism about the "0.9999^{1023}" probability calculation assuming independence:** The critic acknowledges this is "fine for intuition" and the paper does not present it as rigorous proof — it is an illustrative example in the motivation section. Not a genuine weakness.
- **Nitpick about "Clean-label" being labeled as a separate row in the table:** This is a presentation formatting preference that does not affect the paper's substance.
- **Criticism that Figure 3(a) only shows patch trigger:** The paper states other triggers show consistent results (with references to stripped appendix figures). The main text claim that "removing 5% is sufficient" is supported by the appendix reference.
- **Strength Finder generic strengths about "addressing an important problem"** (not present in the actual Strength Finder output — all listed strengths are substantive).

## Novel Insights

None beyond the paper's own contributions. The reviews did surface the interesting observation that while existing detection methods (SafeCLIP, ABL, CD) — designed for supervised learning — struggle with CLIP (48–85% AUC), simple local outlier detectors from classical data mining achieve near-perfect performance (97–99% AUC). The reviewers correctly note that this creates an interesting tension: the "dedicated" methods are more complex but underperform because they rely on assumptions (class-level signal, label-based loss tracking) that do not transfer to CLIP's contrastive learning paradigm. The paper's own insight — that the extremely low poisoning rates characteristic of CLIP attacks (0.01%) create sparsity that makes the problem *easier* for density-based detectors — is the key contribution here, and it is well-supported.

## Suggestions

1. Add standard deviations or confidence intervals to all AUC figures in Table 1, reporting the number of independent runs.
2. List the exact poisoning rate used for each trigger type directly in Table 1 or in a companion table column.
3. Clarify the detection protocol in Section 4.3: state the batch size, whether the full dataset is processed in one pass or in multiple batches, how scores are aggregated, and what the 15-minute runtime includes (representation extraction vs. detection only). A short algorithm box would be ideal.
4. Describe the Neural Cleanse adaptation used for trigger recovery (Section 5.3).
5. Add a Limitations paragraph discussing the adaptive adversary scenario (different triggers per sample, varying trigger placement) and how it might affect the sparsity assumption.

## Score and Decision

This is a solid empirical study with a significant practical contribution. The core findings — that CLIP backdoor samples are reliably detectable via simple local outlier detectors, that detection-based filtering is an effective defense, and that unintentional backdoors already exist in real-world datasets — are well-supported and have clear implications for safe data curation. The weaknesses are presentation gaps and missing experimental transparency items that can be straightforwardly addressed. No structural or methodological flaw undermines the central claims.

**Score:** 7.0  
**Decision:** Accept

MY FINAL SCORE: <pineapple>7.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>