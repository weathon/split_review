I now have all the information needed to verify the reviewers' claims. Let me synthesize the final review.

## Summary

This paper proposes Retrospective Online Adversarial Distillation (ROAD), a single-stage adversarial distillation method that avoids the expensive two-stage pipeline of conventional AD. ROAD uses two cheap teachers — the student's own predictions from the last epoch (self-distillation) and a collaboratively trained natural model — instead of a pre-trained robust teacher. The key claims are: (1) self-distillation from past predictions penalizes overconfidence, improving robustness; (2) collaborative learning with a natural model recovers natural accuracy; (3) the method achieves strong robustness and accuracy at roughly half the training cost of prior AD methods. Experiments on CIFAR-10/100 with ResNet-18, MobileNetV2, and WRN-28-10 support these claims.

## Strengths

- **Novel single-stage AD framework that eliminates pre-trained robust teacher**: ROAD replaces the costly two-stage AD pipeline (teacher pre-training via AT + student distillation) with a single-stage approach using the student's own past predictions and a co-trained natural model as teachers. This cleanly addresses a genuine limitation of prior AD methods. The computational savings (roughly 50% reduction in GPU memory and training time vs. ARD and AdaIAD, Figure 5c-d) are clearly demonstrated.

- **Consistent state-of-the-art results across architectures and datasets**: Tables 1–3 show ROAD achieving the best or runner-up performance in both natural accuracy and AutoAttack robustness across ResNet-18, MobileNetV2, and WRN-28-10 on CIFAR-100 and CIFAR-10. The improvements are especially notable on natural accuracy (e.g., +2.27% to +8.53% on WRN-28-10 vs. competitors), supporting the claim that collaborative learning mitigates the robustness-accuracy trade-off.

- **Comprehensive ablation studies isolating each design choice**: Figures 4(a)–(c) systematically test scheduling strategies, asymmetric vs. symmetric knowledge transfer, and the contribution of each soft-label component. These ablations demonstrate that each of ROAD's components (self-distillation, collaborative learning, asymmetric transfer) contributes positively, and that the sine-increasing schedule is critical.

- **Theoretical insight supported by empirical calibration analysis**: Proposition 1 provides a clean derivation showing that self-distillation from the last epoch induces a gradient rescaling factor that downweights examples with sharply increased confidence. Figure 3 validates this mechanism empirically — ROAD achieves substantially lower ECE (≈0.01) than PGD-AT, label smoothing, and AKD on adversarial examples.

## Weaknesses

### Fatal
None.

### Major

- **Hyperparameter inconsistency between method groups undermines clean comparison**: In Section 4.1, AT methods (PGD-AT, TRADES, MART) and ROAD are trained with 120 epochs and weight decay 3.5e-3, while AD methods are trained with 200 epochs and weight decay 5e-4 — a 7× difference in weight decay. Although the paper states it follows original implementations for AD methods (standard practice), and although ROAD is compared against AT methods under the same protocol, the different training settings make it difficult to fully attribute ROAD's advantage over AD methods to the method itself rather than to favorable hyperparameter choices. This is partially mitigated by the WRN-28-10 experiment (line 140), where ROAD also uses wd 5e-4 (matching AD settings) and still outperforms competitors, but a controlled experiment with a unified hyperparameter grid across all methods would substantially strengthen the paper's empirical claims.

- **PGD-AT baseline in calibration analysis uses different settings than the main comparison**: The paper notes (line 126) that "the PGD-AT model is trained with different settings with the one mentioned in Section 3.1" — meaning the PGD-AT used for the calibration analysis (Figure 3) was trained differently from the PGD-AT baseline in Table 1. This limits the informativeness of the calibration comparison, as the reader cannot tell whether ROAD's superior calibration is relative to a differently-tuned baseline.

### Minor

- **Theoretical analysis is heuristic and does not formally prove the robustness benefit**: Proposition 1 derives a gradient rescaling factor showing that examples with sharply increased confidence receive smaller gradient updates. However, the paper does not provide a theorem connecting this rescaling to bounded generalization error, flatness of the loss landscape, or any formal robustness guarantee. The connection to improved robustness is argued verbally and supported empirically (Figure 3), which is common in this field, but the theory as presented is more of an intuitive explanation than a rigorous proof.

- **Missing comparison to simpler baselines**: ROAD's self-distillation is a form of soft-label training. The paper does not compare directly against TRADES with label smoothing (scheduled or fixed), which would help isolate whether the past-epoch teacher adds value beyond a straightforward regularization trick. Similarly, a comparison against robust self-distillation with a fixed teacher (from a single prior epoch) would clarify the benefit of the retrospective design.

- **No statistical significance or variance reporting**: Tables 1–3 report single numbers without error bars or standard deviations over multiple seeds. Given the sharp differences in some comparisons (e.g., natural accuracy ranging from 66.47% to 72.10% in Table 3), reporting variance would help assess the reliability of the claimed improvements.

- **Negative gradient rescaling factor not discussed**: The expression $1 - \lambda_t(\gamma_{t-1}/\gamma_t)$ (Proposition 1) can become negative if $\gamma_{t-1}/\gamma_t > 1/\lambda_t$, i.e., when confidence drops substantially. The paper does not discuss this edge case or whether it occurs in practice.

- **No ablation of hyperparameter $\beta$**: The paper ablates $\gamma$ thoroughly (Figure 5a-b) but keeps $\beta$ fixed at 6.0 throughout, despite describing $\beta$ as controlling "the trade-off between robustness and natural accuracy."

### Trivial

- Typo "Robustuess Enhancement" in the equation (line 110).

## Nice-to-Haves

- Extending experiments to a larger-scale dataset (e.g., ImageNet) would test the scalability of ROAD's efficiency claims, though the CIFAR experiments are standard for robustness-focused papers.
- Including AT methods (PGD-AT, TRADES) in the computational cost comparison (Figure 5c-d) would provide a fuller efficiency picture, but the paper's efficiency claims are specifically about improvements over AD methods, so this is outside the stated scope.
- Running all baselines under a unified hyperparameter grid would be the cleanest experimental design but is expensive and goes beyond what is standard in the field.

## Removed Points

These points are flagged to be removed; treat them with caution:

1. **"The equation in Section 3.3 is incomplete — ends with 'for' and does not include the third term's definition"**: The equation on line 110 clearly contains all three terms (Self-Guidance, Robustness Enhancement, Natural Model Guidance). The word "for" is part of the descriptive text after the equation, not a missing term. This is a misreading. **Removed (factually wrong).**

2. **"ROAD uses 120 epochs though ROAD is an AD method, creating inconsistency"**: ROAD is a single-stage AD method. Using 120 epochs (its total training budget) is consistent and reasonable; it does not need a separate teacher pre-training phase like two-stage AD methods. The total compute cost comparison (ROAD: 120 epochs vs. AD: ~320 total epochs) correctly favors ROAD. **Removed (misunderstands paper).**

3. **"The second term 'Robustness Enhancement' is exactly TRADES but not cited here"**: TRADES is cited multiple times in the paper (related work, experimental setup). A citation need not appear in the equation subscript itself. **Removed (nitpick).**

4. **"Computational complexity comparison missing AT methods"**: The paper's efficiency claim is specifically about improvements over AD methods (its stated comparison class). AT methods would trivially be cheaper (no teacher at all), so including them adds nothing meaningful. **Removed (scope creep).**

5. **"Demand for ImageNet extension"**: Outside the paper's stated scope (CIFAR evaluation is standard for this subfield). **Moved to Nice-to-Haves.**

6. **"Demand for sensitivity analysis of baselines' hyperparameters"**: Following original implementations is standard practice; the paper provides this information. A full sweep would be ideal but is not a requirement for validity. **Moved to Nice-to-Haves.**

## Novel Insights

The most interesting observation emerging from the reviews is the tension between the paper's clear conceptual contribution (replacing the pre-trained robust teacher with two cheap online teachers) and the practical difficulty of cleanly benchmarking it against two-stage AD methods that require fundamentally different training protocols. The weight decay discrepancy (3.5e-3 vs 5e-4) exemplifies the challenge: two-stage AD methods were developed with longer training schedules and lighter regularization, while the single-stage AT methods ROAD builds on use heavier regularization over fewer epochs. The WRN-28-10 results (where ROAD adopts the lighter wd 5e-4 and still outperforms competitors) partially address this, but the field would benefit from a standardized evaluation protocol that controls for total compute budget and hyperparameter tuning effort across single-stage and two-stage AD methods. This is an open methodological challenge that goes beyond this paper.

## Suggestions

1. **Unify hyperparameters or justify choices more thoroughly**: Either run AD methods with the AT-style settings (120 epochs, wd 3.5e-3) or provide evidence that the chosen settings are individually optimal for each method. At minimum, show that ROAD's advantage holds when AD methods are retrained with ROAD's settings.

2. **Add TRADES + label smoothing as a baseline**: Since self-distillation via soft labels is conceptually related to label smoothing, this would help isolate whether the retrospective mechanism adds value. This is a low-cost experiment that would strengthen the contribution claim.

3. **Report results with error bars over 3–5 seeds**, especially for the key comparisons in Tables 1–3. The natural accuracy range of ~66–72% in Table 3 makes variance reporting important.

4. **Acknowledge and discuss the potential sign flip** in the gradient rescaling factor (Proposition 1) when $\gamma_{t-1}/\gamma_t > 1/\lambda_t$. This is a minor addition but shows theoretical rigor.

## Score and Decision

The paper proposes a clean, well-motivated single-stage AD framework with a plausible theoretical mechanism, strong empirical results across multiple architectures, and thorough ablations. The main weakness — hyperparameter inconsistency between method groups — is real but not fatal: ROAD is compared fairly against AT methods under identical settings, and against AD methods under their recommended settings, and the WRN-28-10 experiment partially alleviates the concern. The missing baselines and lack of variance reporting are addressable in revision.

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>