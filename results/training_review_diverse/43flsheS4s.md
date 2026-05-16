Now I have all the information I need. Let me verify each claim against the actual paper content and produce the final review.

## Final Consolidated Review

---

## Summary

This paper proposes ROAD (Retrospective Online Adversarial Distillation), a single-stage adversarial distillation method that eliminates the need for a pre-trained robust teacher. ROAD replaces the teacher with (i) self-distillation from the student's own predictions on adversarial examples from the last epoch, and (ii) collaborative learning with a concurrently trained natural model. The method is evaluated on CIFAR-10/100 across multiple architectures (ResNet-18, MobileNetV2, WRN-28-10), achieving state-of-the-art or competitive robustness (AutoAttack) while simultaneously improving natural accuracy and requiring roughly half the training cost of prior AD methods.

## Strengths

- **Novel single-stage AD that removes the pre-trained robust teacher.** ROAD replaces the expensive two-stage pipeline of conventional AD with self-distillation from the student's past epoch plus a lightweight co-trained natural model. Figure 5(c,d) shows roughly half the GPU memory and training time versus ARD and AdaIAD, making the efficiency claim verifiable and concrete.

- **Consistent state-of-the-art on both robustness and natural accuracy across architectures.** On CIFAR-100 with ResNet-18, ROAD achieves 58.72% natural accuracy (best among 11+ baselines) and 28.13% AutoAttack accuracy (best or tied-best). This pattern holds across CIFAR-100/10 with ResNet-18, MobileNetV2 (Table 1, 2), and WRN-28-10 (Table 3), where ROAD dominates the robustness-accuracy Pareto frontier — a rare achievement given the well-known trade-off.

- **Theoretical motivation plus empirical calibration evidence.** Proposition 1 derives a gradient rescaling factor showing that ROAD down-weights examples whose prediction confidence increases sharply, preventing over-confidence. Figure 3 independently validates this via reliability diagrams: ROAD achieves notably lower expected calibration error (ECE) than PGD-AT, label smoothing, and AKD, linking the design directly to improved calibration.

- **Comprehensive ablations validate every design choice.** Figure 4(a–c) systematically isolates the contributions of sine scheduling, asymmetric knowledge transfer, and the two soft-label terms; removing any component degrades either robustness or accuracy, confirming the necessity of the full framework. The ablation of asymmetric versus symmetric knowledge transfer (Figure 4b) is particularly informative.

- **Robustness across model scales and attack types.** ROAD is effective on compact models (ResNet-18, MobileNetV2) and larger ones (WRN-28-10), and its robustness is evaluated under white-box (PGD-20, AutoAttack) and black-box (CW) attacks, consistently ranking first or second.

## Weaknesses

### Fatal

None.

### Major

None.

### Minor

- **Training attack parameters are not specified.** The paper does not state the perturbation budget ε, PGD step count, or step size used for crafting adversarial examples during training or evaluation (beyond the standard AutoAttack reference). While experienced readers can infer typical values (ε=8/255, 10-step PGD), these details must be explicit for reproducibility. The paper also does not specify whether the same attack parameters are used for all methods.

- **No standard deviations or multiple seeds reported.** The results in Tables 1–3 appear to be single-run. Given known variability in adversarial training outcomes, reporting mean and standard deviation over at least 3 seeds would strengthen confidence that ROAD's advantage is statistically significant.

- **Natural model architecture is not explicitly stated.** The paper trains "a natural model collaboratively with the student" and gives its learning rate schedule, but does not specify whether it uses the same architecture as the robust model (e.g., ResNet-18 when the robust model is ResNet-18). This should be clarified for reproducibility and to allow accurate compute comparison.

- **Hyperparameter discrepancies between ROAD and AD baselines.** ROAD (and AT methods PGD-AT, TRADES, MART) use 120 epochs with weight decay 3.5e-3, while AD baselines use 200 epochs with weight decay 5e-4, following their original papers. While this is standard practice, it means the comparison is not fully controlled. Notably, AD baselines receive *more* epochs (200 vs. 120), which does not favor ROAD, but the different weight decay and learning rate schedules make it difficult to isolate method-level advantages from training configuration effects. A controlled subset experiment would increase confidence.

- **β hyperparameter not ablated.** The robust factor β is fixed at 6.0 (taken from TRADES) without any ablation or justification for ROAD. While γ is ablated (Figure 5a,b), β controls the robustness-accuracy trade-off and its sensitivity in the ROAD framework is unexplored.

### Trivial

- The phrase "revealed both theoretically and empirically" in the abstract slightly overstates the theoretical contribution, as Proposition 1 is presented without a full step-by-step derivation. The paper could simply say "motivated theoretically and validated empirically."
- The caption in Section 3.1.2 ("Predictions on adversarial examples are collected along with their respective confidence levels") could clarify whether these are training-time or test-time adversarial examples (it is clear from context that they are test-time, but an explicit statement would avoid ambiguity).

## Nice-to-Haves

- A controlled experiment where the strongest AD baselines (e.g., AdaIAD, RSLAD) are re-run using ROAD's 120-epoch schedule and weight decay (with appropriate tuning) would directly address whether ROAD's advantage is due to the method or to training configuration. This would increase confidence but is not required for the paper's core validity.
- Extending evaluation to a higher-resolution dataset (e.g., Tiny-ImageNet) would strengthen claims of scalability, though the current CIFAR-10/100 evaluation is standard and sufficient for a methods paper.

## Removed Points

*These points are flagged to be removed; treat them with caution.*

- **Theoretical derivation is "structural" / fatal.** The harsh critic framed the incomplete derivation as a structural weakness. However: (a) the derivation builds on prior work (Tang et al., 2020; Kim et al., 2021) which the paper cites; (b) the formula and its interpretation are presented; (c) the empirical calibration analysis (Figure 3) independently supports the claim; and (d) the parser strips appendices which may contain the full derivation. This is at most a minor presentation gap, not a structural flaw. *Reason for removal: over-stated severity; missing appendix issue is a parser artifact.*

- **Limited dataset scope (only CIFAR-10/100).** CIFAR-10/100 are the standard benchmarks in the adversarial robustness literature. Demanding ImageNet-scale evaluation is scope creep for a methods paper. *Reason for removal: evaluates against wrong class of expectations.*

- **No comparison to extra-data SOTA (Carmon et al., Gowal et al.).** The paper explicitly focuses on standard-data methods and acknowledges extra-data approaches in the related work. *Reason for removal: scope creep; the paper is not claiming to compete with extra-data methods.*

- **Missing mention of MAT / LBGAT / other online distillation methods.** The related work section adequately covers AD methods (ARD, IAD, RSLAD, AdaIAD, LBGAT, SEAT, etc.). The paper clearly distinguishes ROAD from these. *Reason for removal: instruction forbids manufacturing missing related work.*

- **Sine scheduling not compared to cosine.** The paper compares sine vs. linear vs. fixed scheduling (Figure 4a), which is a reasonable ablation. Asking for every possible schedule is excessive. *Reason for removal: unreasonable reviewer preference.*

## Novel Insights

The most interesting insight from the reviews is that the paper's two claimed weaknesses — incomplete theoretical derivation and unmatched hyperparameters — actually interact in a way the paper could exploit. If the theoretical claim (gradient rescaling) is what allows ROAD to benefit from *shorter* training (120 epochs instead of 200), then the hyperparameter discrepancy becomes a feature rather than a bug: ROAD converges faster because it avoids over-confidence saturation. The paper doesn't currently make this argument, but the efficiency numbers (Figure 5c,d) combined with the calibration evidence (Figure 3) suggest this narrative is latent in the data. Making it explicit would simultaneously address both criticisms.

## Suggestions

1. Add a sentence explicitly stating the training attack parameters (ε, PGD steps, step size) for both training and evaluation. This is essential for reproducibility.
2. Report results over 3 random seeds with standard deviations for the main tables (or at minimum for a representative subset like Table 1).
3. Clarify the natural model architecture — state explicitly that it uses the same architecture as the robust model if this is the case.
4. Either add a brief derivation of Proposition 1 (2–3 lines of algebra) to the main text, or soften the claim in the abstract from "revealed" to "motivated and empirically validated."
5. Add a brief note acknowledging that AD baselines use different (200-epoch) training schedules, and optionally run one controlled comparison (e.g., AdaIAD at 120 epochs) to demonstrate the method-level advantage persists.

## Score and Decision

This paper presents a genuinely novel and well-motivated method. The core idea — replacing a pre-trained robust teacher with self-distillation from the student's past epoch plus a collaborative natural model — is clean, effective, and computationally efficient. The empirical results are strong and consistent across architectures, datasets, and attack types. The weaknesses are all minor and addressable: missing reproducibility details, lack of multiple seeds, and a theoretical component that is slightly over-claimed but independently validated by calibration experiments. None of these issues threaten the core contribution.

**Originality:** High. Self-distillation with epoch-old predictions combined with collaborative natural model training is a novel combination.
**Importance:** High. Reducing AD training cost while improving both robustness and accuracy addresses a real bottleneck.
**Claims support:** Good. Strong empirical evidence; theory is suggestive but the empirical validation stands on its own.
**Soundness:** Good. Experiments are well-designed with informative ablations; minor reproducibility gaps exist.
**Clarity:** Good. The method and motivation are clearly described.
**Value:** High. Practical efficiency gains plus performance improvements make this immediately useful.

MY FINAL SCORE: <pineapple>7.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>