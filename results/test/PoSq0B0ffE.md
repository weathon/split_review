Now I have thoroughly read and verified the paper against the reviewer claims. Let me compose the final consolidated review.

---

## Summary

This paper proposes SHAQ (Safe Haven Activation Quantization), a regularization method for quantized neural networks that pushes pre-quantization activations toward the centers of quantization bins ("safe havens") to improve noise robustness. The paper also introduces the Quantized Helmet (QH), a module of quantized layers that can be prepended to unquantized networks to improve their robustness. On CIFAR-10 with 2-bit VGG16 under FGSM (ε=8/255), the full SHAQ pipeline achieves 73.11% accuracy. The core insight — that quantization-bin-center values tolerate more noise — is intuitive and well-motivated.

## Strengths

1. **Novel and intuitive idea with clear empirical support.** The safe haven concept is a simple observation with practical value: values near quantization-bin centers tolerate more noise than those near boundaries. The paper demonstrates this concretely (Figures 1-2) and translates it into a tractable regularization loss. SHAQ alone improves FGSM accuracy of a 2-bit QNN from a baseline level to 60.83%, a meaningful gain (Table 2 / Section 3.3.1).

2. **Competitive state-of-the-art performance for QNNs.** The combined pipeline (SHAQ + DQ + adversarial training) achieves 73.11% FGSM accuracy on CIFAR-10 with 2-bit VGG16, substantially ahead of prior QNN methods DQ (65.52%) and QANS (58.12%) reported in Table 1. The paper evaluates against six attack types (Random, FGSM, R+FGSM, PGD-20, CW2, DDN2) across two datasets (CIFAR-10, SVHN) and two architectures (VGG16, ResNet-18).

3. **Systematic ablation study.** Table 2 and Section 3.3.1 transparently decompose the contribution of each component: SHAQ alone (60.83%), SHAQ + DQ (70.53%), SHAQ + DQ + Adv (73.11%). This allows readers to assess the marginal benefit of each piece.

4. **Cross-architecture generality.** The QH module improves FGSM accuracy of a standard VGG16 from 42.39% to 64.34% (Table 4) and is demonstrated on both VGG16 and ResNet-18, showing the approach is not architecture-specific.

## Weaknesses

### Fatal
None.

### Major

1. **Quantized Helmet evaluation lacks a critical controlled baseline.** The paper compares VGG16+QH (64.34% FGSM) against vanilla VGG16 (42.39% FGSM), but the QH is trained with an augmented loss that includes adversarial components and fine-tuning. To isolate the helmet structure's marginal contribution, one must compare against the same backbone trained with the *same training procedure* (adversarial training, same epochs, same loss weighting) *without* the helmet. It is unclear whether the 21.95% improvement comes from the helmet's quantization properties, the adversarial training in the loss, or the additional learned parameters. Without this baseline, the claim that QH is what provides the robustness gain is unsubstantiated. (Verified: Section 3.3.2, Table 4 — no adversarially-trained-without-helmet baseline is reported.)

2. **Hyperparameters c₁, c₂, and k are unreported.** The loss functions (Equations 12–13) introduce weighting coefficients c₁ (for SHAQ loss) and c₂ (for QH loss). The NC-safety distance function (Equation 10) introduces coefficient k. None of these values, search ranges, or selection procedures are given anywhere in the paper. This is a genuine reproducibility issue, especially since the overall result depends on tuning the regularization strength. (Verified: grep confirms no mention of these values in the paper.)

### Minor

3. **SOTA claim in abstract conflates SHAQ with the full pipeline.** The abstract states: "Our methods achieve state-of-the-art, 73.11% accuracy... under FGSM attacks." This 73.11% result is from SHAQ + DQ + adversarial training (as the ablation honestly discloses in Section 3.3.1). While the ablation makes the breakdown clear, the abstract and introduction do not qualify that this SOTA result combines SHAQ with prior techniques (DQ regularization and adversarial training). This risks misleading readers into attributing the entire gain to the proposed method alone.

4. **Theoretical contribution is thin.** Theorem 1 is a standard Lipschitz continuity bound offering no quantization-specific insight. Theorem 2's proof is sketchy — it establishes periodicity of d_Q but the leap from periodicity to the closed-form distance function (Equation 10) is asserted without rigorous justification. The paper's value is empirical, not theoretical, and the theorems do not meaningfully strengthen the contributions. (Verified: Theorem 1 at lines 54–60; Theorem 2 "proof" at lines 78–86.)

5. **E-safety guarantee is overstated.** The paper claims values below c_min or above c_max+1/(2T) "will always converge to either c_min or c_max after quantization, regardless of the added noise" (line 94). This is not unconditional: if a value y < c_min receives positive noise δ large enough such that y+δ > c_min, the clamped+quantized output will not be c_min. The guarantee depends on the noise magnitude relative to the distance to the boundary, which the paper's own framework assumes is bounded by ε. The statement should be qualified. (Verified: lines 94–100.)

### Trivial
None.

## Nice-to-Haves

- Report the values of c₁, c₂, and k, along with how they were selected (grid search, validation-based, etc.).
- Add a QH controlled experiment: train the same backbone with the same adversarial loss and regularization strength but without the helmet layers, and report the comparison.
- Clarify in the abstract that the SOTA result combines SHAQ with DQ and adversarial training (or qualify "state-of-the-art" as applying to the full pipeline).
- Provide a clean, self-contained geometric explanation of the safe-haven distance function rather than the current theorem structure, which oversells a simple idea.
- Add a small table reporting the computational overhead of QH (added parameters, FLOPs, inference latency).

## Removed Points

These points are flagged to be removed; treat them with caution.

- **Criticism that "SHAQ alone underperforms DQ" (Harsh Critic Point 1, partial).** SHAQ alone (60.83%) vs. DQ (65.52%) is a comparison of two different regularization approaches under potentially different experimental conditions. The meaningful comparison is SHAQ+DQ (70.53%) vs. DQ alone (65.52%), which shows additive benefit. The critic's framing of SHAQ alone as "below DQ" is a misapples-to-oranges comparison.

- **Criticism that "Theorem 1 adds no value" / "theoretical analysis adds little value."** This is an empirical methods paper, not a theoretical one. The theory serves as motivation for the loss function, which is sufficient for this paper class. The critic is evaluating against the wrong expectation. However, I kept a weakened version as Minor #4 noting the theorems are indeed thin — this is a downgraded version of the same point.

- **"Plug-and-play terminology issue."** The term "plug-and-play" for QH is defensible: the helmet can be added to any model architecture without modifying the original network's weights (the text says "we preserve the integrity of the target neural network"). Training the added module is standard for such modules. This is a terminology nitpick, not a substantive weakness.

- **"TPAP combination shows modest improvement."** This is a subjective assessment of the results' impressiveness, not a flaw in the paper. The combination shows consistent improvements across all noise settings (Table 5).

- **"The derivation of the distance function for NC-safety values is ad hoc."** The paper provides a clear rationale (lines 102–106): values in [c_min, c_min+1/T] are partially safe due to floor quantization, so a linear penalty is introduced. Whether one finds this "ad hoc" is a matter of taste, not a concrete flaw.

- **Strength Finder's generic strengths** (e.g., "addresses an important problem"). Removed for lack of specific, citation-grounded content.

## Novel Insights

None beyond the paper's own contributions. The reviews do not surface any novel observation that the paper itself does not already make.

## Suggestions

1. **Run the missing QH baseline.** Train the same backbone (e.g., VGG16) with the same training procedure (same epochs, same adversarial augmentation, same loss weighting) *without* the helmet layers. Report FGSM accuracy. This will either confirm QH's marginal benefit or reveal that the improvement comes from the training procedure rather than the helmet structure.

2. **Report hyperparameters c₁, c₂, k.** Add a short table or paragraph describing the values used and the selection procedure. Even a single setting with a note that it was chosen via validation will substantially improve reproducibility.

3. **Qualify the SOTA claim.** In the abstract and introduction, add a brief qualification such as "when combined with DQ and adversarial training" or "in a full pipeline."

4. **Rewrite the theoretical section as a clear, informal motivation.** Remove the theorem formalism, which invites rigor expectations the paper does not satisfy, and replace it with a compact geometric explanation of why bin-center values are safer. The current Theorem 1–Theorem 2 structure oversells a simple idea.

5. **Clarify the QH training procedure.** State explicitly whether the backbone network weights are frozen or fine-tuned during QH training. If frozen, this strengthens the plug-and-play claim.

## Score and Decision

- **Originality:** Good — the safe haven insight is simple but novel in the QNN robustness literature.
- **Importance:** Moderate — adversarial robustness in QNNs is a practically relevant problem for edge AI.
- **Claims support:** Partially — the SHAQ claims are well-supported; the QH claims lack a controlled baseline.
- **Soundness:** Adequate — experiments cover multiple attacks/datasets/architectures, but missing hyperparameters and baselines weaken reproducibility.
- **Clarity:** Acceptable — the core idea is clearly explained, but the theoretical section is over-engineered for what it delivers.
- **Value:** The safe haven concept and the combined SHAQ+DQ pipeline results are likely useful to the community.

The paper has a genuinely useful idea and strong empirical results for the QNN setting. However, the QH evaluation gap and missing hyperparameters are significant issues that prevent full acceptance as-is. With the controlled baseline for QH and hyperparameter reporting, the paper would be substantially stronger.

**Overall:** Borderline. The paper's core contribution (SHAQ regularization) is valid and well-supported, but the QH claims are incompletely verified, and reproducibility is hindered by unreported hyperparameters. Suitable for acceptance conditioned on addressing the two major weaknesses.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>