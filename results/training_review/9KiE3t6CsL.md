## Summary

This paper proposes ALBAR, an adversarial training framework that mitigates both background and foreground biases in video action recognition. Unlike prior work requiring attribute labels or separate critic models, ALBAR constructs a static clip (by repeating a single video frame) and applies a combination of adversarial cross-entropy loss, entropy maximization, and gradient penalty to discourage reliance on spatial cues. The method achieves state-of-the-art contrasted accuracy on HMDB51 SCUBA/SCUFO benchmarks (53.02%, a **12% absolute improvement** over the prior best), and identifies/fixes a background leakage issue in the UCF101 bias evaluation protocol by replacing bounding boxes with segmentation masks.

## Strengths

- **Strong headline result on HMDB51 bias benchmarks.** The 12% absolute improvement in contrasted accuracy (from ~41% prior best to 53.02%) is substantial and directly demonstrates that the method successfully reduces both background and foreground spatial biases. This result is the paper's core contribution and is well-supported by Table 1.

- **Clean adversarial framework requiring no bias attribute labels or external critic models.** Prior debiasing methods in action recognition require scene/object classifiers, salient frame detectors, or other external models. ALBAR operates with a single 3D encoder and a self-constructed static clip, making it more scalable and eliminating dependence on the accuracy of external critics. This design choice is a genuine practical advantage.

- **Identification and correction of background leakage in the UCF101 SCUBA/SCUFO protocol.** The paper correctly identifies that bounding-box-based masks leak surrounding background into the bias evaluation, creating a shortcut for background-reliant models. Using SAMTrack segmentation masks to tightly bound the actor is a sound methodological contribution that improves the validity of future bias evaluations (Section 4.2, Figure 2).

- **Thorough ablation validating each loss component.** Table 3 systematically ablates each of the three loss terms (adversarial, entropy maximization, gradient penalty), showing that all three are necessary for best performance. The frame selection ablation (Table 4) is also informative, showing that the middle frame (where the action is occurring) is the most effective static input.

- **Compatibility with existing augmentations.** ALBAR can be combined with StillMix to push contrasted accuracy to 53.68%, demonstrating complementarity with augmentation-based debiasing approaches.

## Weaknesses

### Fatal

None.

### Major

None. The core claim (12% improvement in HMDB51 contrasted accuracy) is empirically well-supported and not undermined by any verified weakness.

### Minor

- **Downstream task evidence is weak and lacks statistical rigor.** Table 5 reports improvements of 0.51 AUC (anomaly detection) and 0.5 mAP (temporal action localization) — differences well within typical run-to-run noise for these tasks. No error bars, variance, or statistical tests are reported. The paper's phrasing ("demonstrating the benefit of our debiasing method across downstream video understanding tasks") overstates what this evidence supports. This does not invalidate the core contribution (the HMDB51 result stands independently) but the downstream claim needs tempering or stronger evidence.

- **The gradient penalty's contribution is empirically marginal and its explanation is post-hoc.** In Table 3, the gradient penalty alone (row d) shows almost no effect on its own, and the paper explains it "likely prevents the static clip gradients from offsetting proper learning from the motion clip gradients" — a speculative explanation that is not empirically validated. The connection to GAN training (Gulrajani et al., 2017) is also loosely drawn: ALBAR minimizes the gradient norm toward 0, whereas the GAN formulation pushes it toward 1 (Lipschitz constraint). The paper does not analyze why minimizing (rather than constraining) the norm is appropriate for debiasing.

- **Qualitative evidence of debiasing is speculative.** Figure 3 shows integrated gradients attributions, but the claim that the baseline model "likely uses the baseball uniform" (i.e., foreground bias) is not supported by the attribution maps — both baseline and ALBAR show similar attention patterns. Controlled experiments (e.g., swapping backgrounds or subject appearance attributes) would be more convincing than post-hoc speculation.

- **Manual verification of UCF101 segmentation masks lacks reproducibility guarantees.** Section 4.2 states that "each testing video is manually checked for accurate segmentation" but does not report inter-annotator agreement, criteria for rejection, or how many videos required correction. This limits the reproducibility of the improved protocol.

- **Table 2 results on the new UCF101 protocol are not contextualized with a direct old-vs-new comparison in the main text.** The paper states that results on the existing (old) protocol are deferred to the appendix, but the main text would benefit from at least a summary comparison to quantify how much the protocol change affects absolute numbers and the relative ordering of methods. Without this, the practical impact of the protocol improvement is asserted rather than demonstrated.

### Trivial

- The "5)" fragments appearing at lines 42 and 48 and "B." at line 81 are clearly citation or section number artifacts from the PDF extraction, not author errors.

## Nice-to-Haves

- **Controlled debiasing experiments.** Replacing backgrounds with held-out scenes or swapping subject appearance (e.g., jerseys) would provide direct causal evidence of debiasing beyond the SCUBA/SCUFO protocol.
- **Loss weight sensitivity analysis.** The relative weights ω_adv, ω_ent, ω_gp (mentioned in the combined objective) are not reported in the extracted text. A sweep over at least ω_ent would show whether the method is robust or requires careful tuning.
- **Explicit mention of computational cost.** Computing ∇_x F(x) for the gradient penalty requires a second-order backward pass through the full video encoder. Reporting training time or memory overhead relative to baseline would help practitioners assess the trade-off.
- **Evaluation on demographic bias.** The paper mentions harmful demographic biases (e.g., skin color) in the introduction and limitations but does not evaluate on any fairness benchmark, even at small scale.

## Removed Points

These points are flagged to be removed, treat them with caution:
- **"Adversarial loss formulation is missing."** Sections 3.1–3.2 (containing Eq. 1 & Eq. 2, referenced in Section 3.3) are missing from the parser-extracted text, but this is a formatting artifact — they exist in the original submission. The conceptual description is present (negative cross-entropy loss on the static clip), and the precise formulation would be recoverable from the full submission.
- **"Improved UCF101 protocol not empirically justified."** The paper states that comparison with the existing protocol is in Appendix C. The parser strips appendices, so this comparison exists in the original submission. While a summary in the main text would be helpful, this is a preference nitpick, not a missing experiment.
- **"The claim that prior work does not significantly reduce foreground bias is not quantitatively backed."** This is a motivation statement in the introduction; the quantitative backing appears in the results tables.
- **"Table 1 nearly illegible"** — parser formatting artifact.
- Various readability/presentation nitpicks about the ablation row labeling and figure quality that stem from the extracted-text format.

## Novel Insights

None beyond the paper's own contributions. The reviews surface useful suggestions (controlled debiasing experiments, statistical rigor for downstream tasks, loss weight sensitivity analysis) but do not produce a fundamentally new observation about the paper's approach or results that the paper itself missed.

## Suggestions

1. **Add error bars or statistical tests to the downstream task results (Table 5).** The reported differences (~0.5%) are small enough that a reader cannot assess whether they are meaningful without variance information. Alternatively, moderate the downstream claim to reflect the preliminary nature of those results.
2. **Include a summary comparison of old vs. new UCF101 protocol in the main text** (e.g., a single row in Table 2 showing a baseline model's performance on both protocols). This would quantify the "background leakage" and justify the protocol revision within the paper itself, not only in the appendix.
3. **Either validate the gradient penalty's role empirically** (e.g., measure gradient norms during training with/without it) or weaken the claim about its function. The current explanation is post-hoc and the component's standalone effect is negligible.
4. **Replace speculation in qualitative analysis with controlled experiments.** For example: run the baseline and ALBAR models on videos where the subject's clothing/appearance is swapped and measure whether predictions change.
5. **Report inter-annotator agreement or a statistical summary for the manual segmentation verification step** to make the improved UCF101 protocol reproducible.

## Score and Decision

The paper makes a meaningful contribution — a clean, label-free adversarial debiasing framework with a strong headline result (+12% contrasted accuracy on HMDB51) that clearly advances the state of the art. The weaknesses are real but addressable and do not undermine the core contribution. The downstream evidence is overclaimed, the gradient penalty analysis is shallow, and some evaluation details need tightening, but these are standard presentational shortcomings, not fatal flaws.

**Score: 6.0** — A solid paper with a clear contribution and addressable weaknesses. Would benefit from the suggested revisions but is acceptable in its current form based on the strength of the HMDB51 result and the novel adversarial formulation.

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>