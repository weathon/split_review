Now I have all the information I need. Let me verify my understanding of the paper and produce the final review.

**Verification notes:**

1. **Missing comparison to prior work** — CONFIRMED. The Related Work (lines 45-47) discusses JPEG_Compliant, Salamah2024 (frozen DNN, optimized tables) and Yang2021 (multi-branch topology). Tables 1-3 only compare to "Baseline" (standard training). No experimental comparison to any of these methods.

2. **Flowers outlier** — CONFIRMED. Table 2 shows +20.90% (DenseNet-121) and +11.63% (ResNet-18) vs. gains of 1.86%-5.64% on other datasets. No analysis or discussion of why.

3. **Adversarial robustness** — CONFIRMED. Section (lines 203-212) uses only FGSM and PGD, no adaptive attacks. Since the JPEG layer is differentiable (Eq. 3-4), adaptive attacks are feasible. The paper does not discuss gradient masking or obfuscation.

4. **α parameters not trained** — CONFIRMED. Lines 133-134: "we choose not to train over α in our framework... fix α_m = 5." For ImageNet (line 138): α derived from q via α = ℏ/q². Eq. (4) optimizes over α, but in practice α is frozen or tied to q.

5. **Sensitivity-based initialization** — CONFIRMED (line 140). Uses a pretrained model of the same architecture.

6. **CIFAR-100 baselines without error bars** — CONFIRMED. Table 1: baseline results from Tian2019, no std dev reported.

7. **No computational overhead reported** — CONFIRMED. "Negligible increase" refers only to parameter count (128 params), not training time or FLOPs.

---

## Summary

The paper proposes JPEG-DL, a framework that prepends a trainable JPEG compression layer (with a differentiable soft quantizer based on a closed-form CPMF) to any DNN, enabling end-to-end joint optimization of quantization tables and model weights for improved classification accuracy.

## Strengths

- **Novel differentiable soft quantizer as a technical enabler.** The paper derives an analytical conditional expectation (Eq. 3–4) that converges to uniform quantization as α→∞ while remaining fully differentiable, enabling gradient-based optimization of quantization parameters — a clean solution to a known differentiability problem. This is the paper's core technical contribution.

- **Consistent accuracy improvements across a wide range of settings.** JPEG-DL improves top-1 accuracy on all 14 tested model–dataset combinations (CIFAR-100: +0.67% to +1.55%, fine-grained: +1.86% to +20.90%, ImageNet: +0.23% to +0.51%). The direction of improvement is uniform, not cherry-picked.

- **Negligible parameter overhead and practical utility.** Only 128 trainable parameters are added (64 for Y, 64 for CbCr), yet gains are competitive. The ablation study (Table 4) further shows that the learned tables, when combined with hard quantization at test time, preserve accuracy while achieving 1.85–2.92× compression — a practical dual benefit.

- **Interpretability evidence supports the mechanism.** Feature map visualizations (Fig. 4) and GradCAM++ (Fig. 5) show that JPEG-DL produces sharper foreground/background separation, connecting the "compression helps" hypothesis to observable model behavior.

## Weaknesses

### Fatal
None.

### Major

- **No experimental comparison to prior work the paper explicitly positions itself against.** The Related Work contrasts JPEG-DL with (i) methods that optimize JPEG tables for a frozen DNN (JPEG_Compliant, Salamah2024) and (ii) the multi-branch topology of Yang2021. Yet the experiments compare only to standard training (no JPEG preprocessing). Without comparing against a baseline where the quantization tables are fixed (e.g., from sensitivity-based initialization or JPEG_Compliant) and *only* the DNN is retrained, the central claim that joint training is the source of improvement remains unsubstantiated. The ablation in Table 4 shows the *tables* matter (hard quantization preserves accuracy), but does not test whether these tables would be equally effective if learned separately. This is the paper's most consequential gap.

- **The Flowers result (+20.90% with DenseNet-121, +11.63% with ResNet-18) is an unexplained outlier.** Gains on the other three fine-grained datasets range from 1.86% to 5.64%. A 20.9% gain on a standard benchmark is extraordinary and demands analysis: is the baseline (51.32%) unusually low? Does JPEG-DL fix a pathological failure mode? Is the result robust across seeds beyond three runs? Reporting this as the headline "up to 20.9%" without discussion gives a misleading impression of typical gains and weakens the paper's central evidentiary claim.

- **The adversarial robustness claims are not supported by the evidence provided.** The paper uses only standard FGSM and PGD attacks with small budgets (ε = 1–4/255, 5 PGD steps). Since JPEG-DL's JPEG layer is differentiable, an adaptive attacker can backpropagate through it (Athalye et al. 2018). The claimed 15% improvement against FGSM may reflect gradient masking or obfuscation rather than genuine robustness. The paper must either evaluate against adaptive attacks or substantially temper the robustness claims and discuss the limitation explicitly.

### Minor

- **The α parameter (presented as trainable) is either frozen or deterministically tied to q in all experiments.** The formulation (Eq. 4) optimizes over both Q and α, but for CIFAR-100 and fine-grained tasks α is fixed to 5 (line 134), and for ImageNet α = ℏ/q² with ℏ fixed to 0.7 (line 138). The paper notes that training α "won't cause a significant change" — but this undermines the framing of the differentiable soft quantizer as the key enabler, since a straight-through estimator or additive noise proxy might have worked equally well.

- **Sensitivity-based initialization uses a pretrained DNN of the same architecture, conflating warm-start with joint-training benefits.** An ablation with random quantization-table initialization is needed to separate the effect.

- **CIFAR-100 baseline standard deviations are not reported** (taken from Tian2019). While the *consistency* of gains across 7 architectures mitigates this, the *magnitude* of improvement for individual models cannot be assessed against run-to-run variation.

- **The gradient scaling scheme for ImageNet (ℏ_m = α_m q_m² fixed to 0.7) is presented without sufficient justification** for why this specific functional form or constant is appropriate, or what happens with standard ADAM optimization on ImageNet.

- **No analysis of what the learned quantization tables do in frequency space.** The paper visualizes tables (Fig. 4) but does not interpret them — e.g., are high frequencies being suppressed differentially? Which DCT frequencies matter most for which dataset?

- **Training-time computational overhead is not reported.** The soft quantizer computes a softmax over 2^(b-1) values (b=8→255 classes) for each DCT coefficient. The paper's "negligible increase" claim refers only to parameter count (128), not FLOPs or training-time slowdown.

### Trivial

- The compression ratios (1.85–2.92×, from 8.22–12.98 bpp vs. 24 bpp uncompressed) represent mild compression. The paper should clarify that JPEG-DL is not optimizing for compression as its primary objective — the compression capability is a byproduct of the learned quantization tables being quantizable at test time.

## Nice-to-Haves

- Evaluation on object detection or segmentation, if the "generality for various tasks" claim is to be substantiated beyond classification.
- An analysis of whether simpler differentiable proxies for rounding (e.g., straight-through estimator, additive uniform noise) would yield similar gains — this would clarify whether the soft quantizer formulation is necessary or incidental.
- Random initialization ablation for the quantization tables to isolate initialization effects.

## Removed Points

- **Criticism about "missing appendix content" (appendices mentioned in paper but stripped by parser):** The paper references Appendices \ref{app:fine_grained} and \ref{app:transformer-based_settings}. These were removed by PDF parsing and exist in the original submission. Removed per hard rule.
- **Criticism about "no evaluation on detection or segmentation" as a structural weakness:** The paper's core experiments are on classification, which is the stated scope. Demanding broader tasks is scope creep. Moved to Nice-to-Haves.
- **"Gains are within run-to-run variation" claim:** The paper shows positive gains across *all 7* CIFAR-100 models and *all 14* total model-dataset combinations. The probability of this being random is negligible (~0.5^7 ≈ 0.008). The concern about exact *magnitude* is valid (moved to Minor), but the claim that gains aren't real is incorrect.
- **Adversarial robustness listed as a strength by Strength Finder:** Conflicts with the verified weakness about adaptive attacks. Per rules, weakness wins. Robustness is mentioned as a secondary benefit with the noted caveat.
- **"Compression is a byproduct" criticism:** The paper frames compression as a joint benefit in the ablation study (line 214: "achieve both compression and accuracy improvement simultaneously!"). The reviewer's framing as a "byproduct" is a disagreement on emphasis, not a concrete error.

## Novel Insights

The reviews surface a useful meta-point: the paper's framing ("differentiable soft quantizer enables joint training") is somewhat at odds with its actual experimental regime (α frozen or derived, only q trained). This creates a credibility gap — the claimed *mechanism* (end-to-end differentiability through the soft quantizer's α parameter) is not actually exercised. What is really being tested is whether *q alone* can be effectively optimized via the soft gradient signal of a near-hard quantizer (α=5). This distinction matters because it means a simpler differentiable approximation (e.g., straight-through estimator) might suffice, which would change the nature of the contribution from "novel differentiability mechanism" to "empirically demonstrating that learned quantization tables improve accuracy." Future work should clarify whether the soft quantizer's specific form is necessary or whether any differentiable proxy for rounding produces the same gains.

## Suggestions

1. **Add the critical missing baseline:** Fix the quantization tables (from sensitivity-based initialization or JPEG_Compliant) and retrain *only* the DNN. If JPEG-DL outperforms this, the gain is attributable to joint optimization. If not, the contribution is better table selection, not joint training.
2. **Analyze the Flowers outlier systematically:** Report whether the baseline is unusually low, run additional seeds, and investigate what the learned tables are suppressing to produce such a large gain.
3. **Replace the adversarial robustness section** with an evaluation that includes adaptive attacks (PGD with gradients through the JPEG layer), or explicitly state the limitation and temper the claims.
4. **Run baselines in-house or report standard deviations** for CIFAR-100 to enable statistical comparison.
5. **Include a random initialization ablation** for the quantization tables to separate initialization from joint-training benefits.
6. **Report training-time overhead** (wall-clock time per epoch with and without JPEG-DL) to substantiate the "negligible increase" claim.

## Score and Decision

The paper has a clear and sensible core idea — learning JPEG quantization tables jointly with a DNN — and demonstrates consistent accuracy improvements across many settings. However, the evaluation has structural gaps: the most important baseline (fixed-table + DNN retraining) is missing, one headline result is an unexplained outlier, and the adversarial robustness claims are not backed by appropriate methodology. These gaps prevent full confidence in attributing the gains to joint optimization rather than better table selection. The paper is on the right track but needs significant revision to substantiate its central claims.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>