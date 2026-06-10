## Summary

This paper proposes using counterfactual explanations to generate adversarial examples, with the goal of reducing privacy leakage in models trained on those examples. The method identifies the nearest neighbor from a different class, generates its counterfactual explanation, and uses the result as the adversarial example for the original sample. On MNIST, the approach achieves 50.00% membership inference attack (MIA) accuracy (chance level), compared to 82.96% for PGD-trained models, while maintaining competitive accuracy.

## Strengths

- **Novel generation paradigm.** The idea of generating adversarial examples via counterfactual explanations of the nearest neighbor from a different class (Section 3.1, Eq. 2–3) is genuinely novel. This is, to the paper's credit, the first work bridging counterfactual explanations and adversarial example generation in this specific way.
- **Design choices are explicitly motivated by privacy mechanisms.** The decoupling of adversarial example generation from model training (Section 3.2.1), the preference for autoencoders over GANs (Section 2), and the prototype-based loss over individual-sample loss (Section 3.2.2) are each connected to specific privacy leakage pathways (generalization gap, generative model vulnerabilities, individual data memorization).
- **MIA results show a large and meaningful improvement over PGD and AdvGAN baselines.** Assuming the MIA follows the standard Song et al. (2019) protocol for models trained on adversarial examples (which the 82.96% PGD result confirms is non-trivial), the proposed method's 50.00% is a substantial privacy improvement.
- **Systematic variation of the adversarial example fraction.** Table 3 varies the proportion of counterfactual adversarial examples from 0% to 100% and measures accuracy and MIA, providing a useful empirical map of the accuracy–privacy trade-off.

## Weaknesses

### Major

- **Robustness is central to the paper's framing but is never measured.** The terms "robustness" or "robust" appear over 20 times throughout the abstract, introduction, method, and experiments. Section 4.5 is titled "The Best Balance and Trade-Off between Accuracy, Robustness and Privacy" and asserts that "robustness notably increases" and "robustness is highly reinforced" as the proportion of counterfactual adversarial examples grows. Yet the paper presents **zero** evaluations of model accuracy under any adversarial attack (PGD, FGSM, CW, AutoAttack). Table 3 reports only training accuracy, test accuracy, and MIA accuracy — no robustness metric. The "trade-off" analysis is missing one of its three axes, and the claim that these are "robust models" is unsupported by evidence. This is not a missing ablation; it is the absence of a core measurement that the paper's narrative depends on.

- **All experiments are on a single, simple dataset (MNIST).** MNIST (28×28 grayscale, 10 well-separated classes) is widely considered insufficient for supporting general claims about privacy-robustness trade-offs. The paper states in the conclusion that "we have improved the method for other kinds of training datasets and obtained certain effects" but provides no results, metrics, or even which datasets. At minimum Fashion-MNIST or CIFAR-10 would establish that the findings are not artifacts of MNIST's simplicity.

### Minor

- **The MIA setup is described too briefly to dispel natural confusion.** The model is trained on adversarial examples (not original images) and the MIA evaluates on original images. The paper cites Song et al. (2019), which defines a proper MIA protocol for this setting, but the paper itself does not explain how queries are constructed or how membership is defined. The fact that PGD yields 82.96% confirms the MIA is non-trivial, but a reader unfamiliar with Song et al. cannot verify this from the paper alone.

- **"Semantic perturbations" are asserted without evaluation.** The paper claims generated perturbations are "semantic" and "meaningful" (contributions list, conclusion) but provides no human evaluation, no perceptual similarity metric (FID, LPIPS), and no analysis of which features are modified. The only evidence is a single qualitative figure (Figure 1).

- **No variance or confidence intervals.** Results in Tables 2 and 3 are point estimates without standard deviations or significance testing. Given the small numerical differences in some comparisons (50.00% vs. 50.46% MIA), this is a notable omission.

- **t-SNE is the sole explanatory tool.** The t-SNE visualizations (Figures 3–4) are qualitative and depend on hyperparameter choices. Quantitative distributional metrics (FID, MMD, Wasserstein distance) would provide stronger support for the claim that the method reduces distributional distinguishability.

### Trivial

- References to "supplementary materials" for loss function details — the parser strips these; they are assumed to exist in the original submission.

## Nice-to-Haves

- Comparison with DP-SGD or PATE, though outside the paper's stated scope of adversarial-example-based methods, would help situate the privacy claims in the broader literature.

## Removed Points

The following criticisms were assessed against the paper and removed with justification:

1. **"MIA evaluation is structurally flawed / a tautology"** (Harsh Critic): This criticism assumes the MIA is asking whether an original image was *literally* in the training set. The paper cites Song et al. (2019), which defines a proper MIA for models trained on adversarial examples — testing whether the model leaks information about which original images were *used* (indirectly) in training. The fact that PGD achieves 82.96% MIA accuracy confirms the MIA is not a tautology; the proposed method's 50.00% is a meaningful improvement over this non-trivial baseline. The critic's reading misinterprets the evaluation setup.

2. **"No comparison against differential privacy"** (Harsh Critic): The paper's scope is adversarial-example-based training; its baselines (PGD, AdvGAN, non-robust) are appropriate. DP is a different methodological paradigm. Demanding it as a baseline constitutes scope creep.

3. **"Method is underspecified / missing loss function definitions"** (Harsh Critic): Loss terms are named in Eq. 7 and the paper states "More details about loss function in supplementary materials." The parser strips appendices; these are assumed to exist in the original submission.

4. **Strength about 50% MIA being a core strength** (Strength Finder): Partially retained (see Strengths section) with qualification about MIA clarity, which is noted as a Minor weakness.

## Novel Insights

None beyond the paper's own contributions. The reviewers did not produce any synthesis that goes beyond what the paper claims or that offers a new perspective not already present in the paper.

## Suggestions

1. **Measure robustness directly:** Report model accuracy under PGD-40, FGSM, and AutoAttack for all compared methods. Without this, the "accuracy-robustness-privacy trade-off" that structures the paper's narrative cannot be evaluated.
2. **Clarify the MIA setup:** Explain exactly what distribution the MIA attacker is queried on and how membership is defined. This is essential for the paper's central empirical result.
3. **Add at least one additional dataset:** Fashion-MNIST or CIFAR-10.
4. **Evaluate "semantic" perturbations quantitatively:** Report FID, LPIPS, or a human evaluation.
5. **Report variance:** Include standard deviations for Tables 2 and 3.

## Score and Decision

The paper introduces a genuinely novel idea with promising privacy results. However, the evaluation has significant gaps: robustness — a property central to the paper's framing and repeatedly invoked — is never measured; all experiments use only MNIST; and the MIA setup is insufficiently described. The paper's core contribution is interesting and may prove valuable, but the evidence as presented does not meet the standard for a top venue.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>