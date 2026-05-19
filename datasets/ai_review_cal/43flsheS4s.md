- Decision: Reject
- Avg Score: 4.75
- Scores: 5, 6, 3, 5
Now I have all the evidence I need. Here is the consolidated review:

## Summary
The paper proposes ROAD (Retrospective Online Adversarial Distillation), a single-stage adversarial distillation method that avoids the expensive pre-trained robust teacher used in conventional AD. Instead, ROAD uses two cheap sources of guidance: the student's own predictions from the previous epoch (retrospective self-distillation) and a collaboratively trained natural model. The method is shown to simultaneously improve both robustness and natural accuracy while requiring roughly half the training time and memory of prior AD methods.

## Strengths
- **Outstanding robustness–accuracy trade-off across multiple benchmarks (Tables 1–3, Sec. 4.2–4.3):** ROAD consistently achieves the best or second-best robust accuracy (e.g., 24.11% AutoAttack on ResNet-18 CIFAR-100) while also improving natural accuracy over all AT and AD baselines (e.g., +1.56% on ResNet-18 CIFAR-100). This directly addresses the robustness–accuracy trade-off that prior AD methods have not resolved.
- **Substantially reduced computational cost (Figures 5(c)–5(d), Sec. 4.5):** ROAD requires roughly half the GPU memory and training time of leading AD methods (ARD, AdaIAD) by eliminating the need to pre-train a robust teacher. This is a practical strength supported by concrete wall-clock and memory measurements.
- **Theoretical grounding with empirical verification (Proposition 1, Sec. 3.1.1; Figure 3, Sec. 3.1.2):** The paper derives a gradient rescaling factor that explains how retrospective self-distillation penalizes over-confident updates, and confirms this with calibration analysis (ECE of 0.046 vs. 0.115 for PGD-AT).
- **Well-designed ablation studies (Figure 4, Sec. 4.4):** Controlled experiments separately remove the self-distillation soft labels, the collaborative soft labels, and the asymmetric knowledge transfer, providing direct evidence for the necessity of each design choice.
- **Consistency across architectures and datasets (Tables 1–3):** ROAD's improvements hold for ResNet-18, MobileNetV2, and WRN-28-10 on both CIFAR-100 and CIFAR-10, showing the method is not architecture- or dataset-specific.

## Weaknesses

### Fatal
None.

### Major
None. The core claims are well-supported by the experiments.

### Minor
- **Theoretical derivation of Proposition 1 is not self-contained (Sec. 3.1.1).** The paper states the gradient rescaling factor and its interpretation, but the derivation relies on citations to Tang et al. (2020) and Kim et al. (2021) without showing how those prior results are adapted to this specific setting. A few lines of derivation starting from the soft-label loss would make the paper self-contained and strengthen the credibility of the theoretical claim. The empirical calibration analysis (Figure 3) partially compensates, but the gap between the stated proposition and the provided reasoning is noticeable.

- **Collaborative learning mechanism is not deeply analyzed (Sec. 3.2).** The paper attributes natural accuracy gains to "friendly knowledge" from the natural model, but no analysis (e.g., representation comparison, examination of when the natural model's outputs diverge from one-hot labels) is provided to substantiate what this knowledge consists of or why it helps the robust model. The ablation in Figure 4(b) shows that asymmetric knowledge transfer outperforms a symmetric KL-KL variant, but this does not isolate *what* the natural model contributes. This is a gap in mechanistic understanding, not in empirical support for the final result.

- **The asymmetric ablation (Figure 4(b)) compares only against symmetric KL-KL, not against symmetric soft-label transfer.** The paper's conclusion that asymmetry is beneficial would be strengthened by testing a symmetric soft-label variant where both models receive soft labels from each other. As it stands, the design choice is not fully disentangled from the choice of loss function (KL vs. cross-entropy).

- **MAT (Mutual Adversarial Training) is cited in related work (Sec. 2) but never compared experimentally.** MAT also trains two models collaboratively. While ROAD trains one robust and one natural model (vs. MAT's two robust models), the paper does not explain why MAT is not included as a baseline or discuss the practical implications of this design difference.

- **RSLAD and IAD are omitted from the computational complexity comparison (Sec. 4.5).** The paper compares only ARD, AdaIAD, and LBGAT for cost. Since computational efficiency is a central claim, including or at least discussing the expected cost of these omitted methods would strengthen the evidence.

- **No variance or confidence intervals reported.** Results are reported as single numbers without multiple seeds, making it impossible to assess whether the gaps between ROAD and the next-best methods are statistically meaningful. While single-run reporting is common in this subfield, given the known variance in adversarial training results, this is a limitation.

- **Limited to CIFAR-10/100.** The computational efficiency claim would be strengthened by a demonstration on a larger dataset (e.g., Tiny ImageNet or ImageNet subset). The current results are convincing on these benchmarks but leave open questions about scaling.

- **Reproducibility details are incomplete.** Random seed, number of trials, and exact data augmentation (beyond standard crops/flips) are not specified.

### Trivial
None.

## Nice-to-Haves
- Run AD baselines under a matching 120-epoch schedule (or ROAD under 200 epochs) to rule out training budget effects on the comparison.
- Analyze the natural model's outputs over training relative to the robust model (e.g., how its predictions diverge from one-hot labels, and whether this correlates with robust model uncertainty).
- A direct comparison where the natural model is trained from scratch on clean data (static) while the robust model uses KL to this static model, to rule out trivial explanations for the natural accuracy gain.

## Removed Points
- *"Gradient rescaling factor phrasing is unclear (the factor itself decreases when γ_{t-1}/γ_t > 1)"* — The paper says "γ_{t-1}/γ_t becomes larger" (the ratio), not "the factor becomes larger." The paper then correctly states that the method "assigns relatively smaller weights." This is a clear misreading of the text.
- *"Strengthening the Paper" suggestions* — These are nice-to-haves, not weaknesses. Moved to the Nice-to-Haves section.

## Novel Insights
None beyond the paper's own contributions. The reviews do not surface any observation that the paper itself does not already articulate or imply.

## Suggestions
1. Add 2–4 lines of derivation for Proposition 1 in the main paper so the theoretical claim is self-contained.
2. Include MAT in the experimental comparison or clearly explain why it is not directly comparable (different setting: two robust models vs. robust + natural).
3. Report mean and standard deviation over at least 3 random seeds for the main results.
4. Extend the asymmetric ablation (Figure 4(b)) to include a symmetric soft-label variant.
