- Decision: Accept
- Avg Score: 5.75
- Scores: 6, 3, 8, 6
Now I have all the information needed. Let me compose the final consolidated review.

## Summary

This paper proposes a backdoor-based model watermarking method that uses a single out-of-distribution (OoD) image — instead of any original training data — to construct a surrogate dataset for trigger injection. An adversarial weight perturbation procedure is applied during fine-tuning to improve robustness against removal attacks (fine-tuning, pruning, model extraction). The paper's core empirical finding is that OoD-injected watermarks survive removal attacks substantially better than traditional in-distribution (ID) watermarks, and that weight perturbation provides an additional gain.

## Strengths

1. **Data-free watermark injection using a single OoD image.** The method eliminates the need for any original training data during watermarking or verification (Section 3.1, Equation 1). The surrogate dataset is constructed entirely from one OoD image via strong augmentation, and only that image (kept secret) is needed for verification — a practical advance for settings where training data is private or inaccessible.

2. **Clear demonstration that OoD watermarks are more robust than ID watermarks.** Table 3 (tab:id_ood) directly compares ID and OoD injection under the strongest attack (RT-AL) on CIFAR-10: OoDWSR drops to 57.52% and 24.19% for OoD injection versus 4.13% and 3.42% for ID injection. This distributional finding — that fine-tuning on ID data has less effect on OoD-triggered decision boundaries — is the paper's most compelling empirical contribution.

3. **Weight perturbation provides a meaningful robustness improvement.** Table 5 (tab:wp) shows that under RT-AL on CIFAR-10, weight perturbation raises OoDWSR from 19.94% to 57.52% (trojan_wm) and from 12.81% to 24.19% (trojan_8x8), while maintaining similar utility. This ablation is clean and attributable specifically to the proposed technique.

4. **Sample- and time-efficient procedure.** The method requires only a single OoD image and completes injection in 20–30 fine-tuning epochs, achieving stable OoDWSR of 95.66% on CIFAR-10 with under 3% accuracy degradation (Section 4.1). This is substantially more efficient than data-free distillation approaches requiring hundreds of epochs.

5. **Broad experimental scope.** The evaluation covers three datasets (CIFAR-10, CIFAR-100, GTSRB), three attack families (fine-tuning with three variants, pruning at two levels, model extraction), six trigger patterns, and multiple OoD source images. Ablations on OoD image type (Table 4/tab:ood_image) provide actionable guidance (dense images outperform sparse).

## Weaknesses

### Fatal
None.

### Major

1. **Missing comparison to the closest data-free baseline (Li et al., 2022).** The paper explicitly discusses Li et al. (2022) as a data-free distillation-based method that also avoids original training data (Section 2, lines 80–82), and positions its own efficiency (20–30 epochs) against that method's slowness (hundreds of epochs). Yet Li et al. (2022) is never evaluated experimentally. Without this comparison, the paper cannot substantiate its claim to "fill the gap of backdoor-based IP protection without training data" (line 48) as an advance over the existing state of the art in the same category. The paper's independent contributions (OoD robustness discovery, weight perturbation) are not invalidated, but a reader cannot judge whether the proposed method is better, worse, or comparable to the closest prior work in watermark success rate, utility preservation, or attack robustness. This is a significant evidential gap.

2. **"Robustness" framing is overstated for several worst-case settings.** Under the strongest attack (RT-AL: re-initialize last layer + fine-tune all), several results are too low to suggest practical reliability: CIFAR-100 trojan_8x8 OoDWSR falls to 7.00% (Table 2, line 315); CIFAR-100 l0_inv to 12.32% (line 321); GTSRB trojan_wm to 6.84% (line 335); and CIFAR-100 l0_inv under model extraction to 6.22% (Table 5, line 429). While the paper correctly notes these are above the non-watermarked baselines (e.g., 0.01%–2.20%), the blanket claim that the watermark is "robust against" removal attacks (title, abstract, conclusion) overpromises. For a deployed IP protection system, a 6–12% detection rate is not robust in a practical sense. The paper would benefit from a more precise characterization — e.g., "survives under statistical verification" vs. "reliably verifiable" — and from acknowledging that several scenarios yield borderline results.

### Minor

1. **No false positive analysis for the verification procedure.** Ownership verification uses a T-test (p<0.05) comparing suspect vs. non-watermarked model output logits. However, the paper does not evaluate how often an independently trained (non-stolen) model would be falsely flagged as a copy. Since p-values depend on sample size and can be tiny even for small effect sizes, a false positive rate or ROC analysis over the verification dataset would substantially strengthen the practical credibility of the verification claim. This is a standard omission in many watermarking papers, but noting it would improve the work.

2. **No sensitivity analysis for key hyperparameters.** The perturbation constraint $\gamma$ (set to 0.1 for CIFAR-10/GTSRB, 0.05 for CIFAR-100) and the KL trade-off $\beta$ (fixed at 6 for all datasets) are chosen without any ablation or justification (Section 4.1). Since $\gamma$ controls the perturbation magnitude — too large risks detectability, too small erodes robustness — a sensitivity analysis would clarify the method's robustness to design choices.

3. **Threat model assumption is underexplored.** The paper assumes the attacker has only 10% of the original training data for fine-tuning and pruning (line 261). This is a defensible setting but differs from the common assumption in the watermark removal literature (full data access). The paper does not discuss how results would change with more attacker data or provide an experiment varying this fraction, which would be informative.

### Trivial
None.

## Nice-to-Haves

- A direct experimental comparison to Li et al. (2022) or a similarly data-free watermarking baseline would resolve the most significant gap.
- False positive rate analysis (ROC curve) for the T-test verification procedure.
- Sensitivity analysis for $\gamma$ and $\beta$ across a range of values.
- An experiment varying the attacker's data fraction (e.g., 10%, 50%, 100%) to probe the threat model sensitivity.
- A deeper analysis (e.g., feature-space distance or gradient overlap) of why OoD triggers survive fine-tuning when ID triggers do not — currently the paper speculates (lines 361–364) but does not provide direct evidence.

## Removed Points

These points from the reviewers were checked against the paper and removed with justification:

- **"Safe" is undefined/unevaluated** — The paper consistently defines "safe" in context: safe = uses public OoD data instead of private training data (lines 8, 41, 119–122). The broader security interpretation raised by the harsh critic is scope creep. **Removed.**

- **"Single-image learning is borrowed from prior work"** — The paper properly cites Asano et al. (2019, 2022) and applies the technique to the novel problem of watermarking. Application to a new problem is standard practice, not a weakness. **Removed.**

- **"Weight perturbation is standard adversarial training"** — The paper cites Wu et al. (2020) and adapts the method for watermarking. This is an appropriate adaptation, not a flaw. **Removed.**

- **Only 3 OoD images tested** — The method only needs one image; testing three types is a reasonable ablation for a proof-of-concept. **Removed.**

- **Model extraction accuracy on ImageNetDS not reported** — The paper reports suspect model accuracy on the original task (the relevant metric), not on the proxy dataset. Requesting the latter is non-standard. **Removed.**

- **Claim that "6.22% is barely above 0.02%"** — 6.22% is ~311× higher than 0.02%. This is not "barely above"; the characterization is misleading. **Removed.**

## Novel Insights

None beyond the paper's own contributions. The key insight — that OoD-triggered decision boundaries are substantially less affected by ID fine-tuning than ID-triggered ones — is already the paper's main contribution, and the reviews do not surface an independent novel observation.

## Suggestions

1. Add an experimental comparison to the closest data-free baseline (Li et al., 2022). This addresses the most significant evidential gap and would allow the paper to substantiate its claim of advancing the state of the art.
2. Temper the "robust" framing: replace blanket claims with more precise characterizations (e.g., "statistically verifiable after attack" for low-WSR cases), or explicitly discuss which attack/dataset combinations yield practical reliability vs. marginal statistical detection.
3. Add a false positive analysis for the verification protocol (ROC curve or FPR at relevant thresholds).
4. Include a sensitivity study for $\gamma$ and $\beta$ to demonstrate robustness to hyperparameter choices.
5. Add an experiment varying the attacker's data fraction (e.g., 10%, 50%, 100%) to probe how the threat model assumption affects results.
