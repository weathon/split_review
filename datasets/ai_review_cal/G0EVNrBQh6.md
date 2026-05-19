- Decision: Reject
- Avg Score: 3.80
- Scores: 5, 5, 5, 3, 1
Now I have a thorough understanding of the paper and can verify each reviewer claim. Let me construct the final consolidated review.

---

## Summary

This paper investigates whether adversarial perturbations contain human-identifiable features (such as object contours) hidden by noise and incomplete information. By averaging perturbations from 270 diverse models (with Gaussian noise copies per model) for the same input image, the authors show that structured, human-recognizable patterns emerge — a phenomenon they call the "masking effect" in untargeted attacks. They quantify recognizability (80.7% human accuracy, 56% machine accuracy for BIM), show that contour regions of averaged perturbations are far more effective at attacking models than background regions, and report notable cross-algorithm cosine similarity (0.43–0.64). The paper also provides speculative explanations for transferability, adversarial training interpretability, and non-robust features. The core observation — that averaging perturbations over many diverse models reveals coherent semantic structure — is novel and empirically demonstrated.

---

## Strengths

1. **Systematic demonstration that averaging perturbations across many diverse models reveals human-identifiable features.** The paper averages 2,700 perturbations (270 models × 10 noise copies per image) and shows clear object contours (shark, cat, hen) that are entirely invisible in single-model perturbations (Figure 3, Section 5.2). This is a concrete empirical advance over prior perturbation studies that examined only single models or small ensembles.

2. **Quantitative human and machine evaluation confirms high recognizability.** Human evaluators achieved 80.7% accuracy (random baseline = 5%) on BIM MM+G perturbations (Section 5.2.1), and a held-out VGG-16 reached 56.0% (vs. 5.5% in SM). These numbers directly validate that the averaged perturbations contain features that humans and machines can reliably associate with the correct class.

3. **Contour-only perturbations are dramatically more attack-effective than background-only perturbations.** Using ImageNet-S pixel-level annotations to extract contour regions, the paper shows that contour-only perturbations reduce accuracy from 81.8% to 32.2–37.0%, while background-only perturbations only reduce to 60.6–69.0% (Section 5.2.3, Figure 4) — despite the contour having a smaller area (area ratio 0.83). This is causal evidence that the human-identifiable structure in the perturbation drives misclassification.

4. **Cross-algorithm similarity of averaged perturbations.** Cosine similarities between perturbations from BIM, CW, and DeepFool range from 0.43 to 0.64 (Section 5.2.5, Figure 6) — a novel quantitative result showing that the masking effect is not algorithm-specific, supporting the claim that the revealed features reflect shared semantics across attack methods.

5. **Clear writing and logical structure.** The paper is well-organized, the assumptions are stated upfront, the MM+G methodology is clearly explained, and the distinction between the masking effect (untargeted) and generation effect (targeted) is conceptually helpful.

---

## Weaknesses

### Fatal
None.

### Major

1. **The paper's central claim — that human-identifiable features are "inherently embedded in a large class of adversarial perturbations" (Conclusion) — is supported only indirectly.** Every main experiment (recognizability, attack strength, contour extraction, cosine similarity) is performed on *averaged* perturbations (MM+G setting). The paper never shows that an individual (single-model) perturbation, when independently denoised (e.g., via spatial filtering, wavelet denoising, or self-smoothing), reveals similar features. The inference that averaging *reveals* pre-existing structure rather than *creating* structure from uncorrelated partial information is plausible but not tested. An "emergence curve" showing how feature quality changes with the number of averaged models (1, 5, 10, 50, 100, 270) would directly support the claim. Without it, the paper overreaches from "averaged perturbations contain human-identifiable features" to "every individual perturbation inherently contains them." The paper would be more defensible if reframed as a study of properties of *averaged* perturbations, which is itself a genuine contribution.

2. **No ablation of the MM+G averaging parameters.** The method uses 270 models, 10 noise copies per model, and specific noise standard deviations (0.02 for BIM, 0.05 for CW/DeepFool) with no ablation varying these parameters. The reader cannot assess whether 10 noise copies are sufficient, whether 270 models are necessary, or whether model diversity matters more than the number of noise copies. A plot of feature quality versus (a) number of models, (b) number of noise samples, and (c) noise level would substantially strengthen the paper's mechanistic claims about noise reduction and feature completeness.

3. **Two of three claimed datasets (MNIST, CIFAR-10) have no results in the main paper body.** The abstract states "three datasets, including MNIST, CIFAR-10, and ImageNet" and claims to "demonstrate our finding" across them, yet the entire experimental section reports results only for ImageNet. If MNIST and CIFAR-10 results exist in a stripped appendix, the main text should at minimum reference them. As presented, the generality claim across datasets is unsubstantiated.

4. **No statistical reporting of variance.** Key numbers — the 80.7% human evaluation accuracy (over 48 participants), the attack success rates (81.8% → 13.2% for BIM), the contour/background accuracy differences, and the cosine similarity values — are reported as point estimates without error bars, confidence intervals, or per-model breakdowns. Given the modest sample of 200 images from 20 classes, variance reporting is essential.

### Minor

1. **Search-based attacks (Square, One-pixel) are treated purely qualitatively.** Section 5.2.4 shows one figure with no quantitative evaluation of recognizability or attack strength. The claim that these attacks also exhibit the masking effect remains anecdotal.

2. **Targeted attack section is underdeveloped.** Section 6 shows only two visual examples (cat→tiger, hen→cock) with no quantitative evaluation of attack success rates or recognizability. The paper acknowledges that targeted features require close source-target class pairs (limiting generality), but provides no systematic evaluation. This section feels preliminary.

3. **The Discussion section (Section 7) is speculative and untested.** The explanations for transferability, adversarial training interpretability, and non-robust features are plausible but are not experimentally verified in this paper. The linear classifier example for adversarial training (Section 7, paragraph 3) is illustrative but not connected to the actual networks studied. While these ideas are interesting, presenting them as "insights" rather than "hypotheses" overstates their empirical grounding.

4. **Human evaluation is only for one setting (BIM, MM+G) with no error analysis.** The paper reports 80.7% accuracy with no breakdown of which classes were confused or whether performance varied significantly across the four participant subsets. Machine evaluation is only on VGG-16; testing on more models would strengthen the claim.

### Trivial
- The paper states "In the ImageNet experiment" (Section 4.1) as if it is one of multiple experiments, but no other dataset experiments appear.
- Line 82 notes that ResNet-50 serves as both a source and testing model (white-box attack in SM). This is acknowledged but should also clarify whether the *same weights* are used.

---

## Nice-to-Haves
- **Ensemble attack baseline**: Comparing MM+G perturbations against an ensemble attack (averaging loss gradients across the 270 models before computing a single perturbation) would clarify whether averaging perturbations post-hoc is equivalent to ensemble attack or yields different properties.
- **Denoising of individual perturbations**: Showing that a single-model perturbation, when denoised via standard techniques (e.g., bilateral filter, wavelet thresholding), reveals similar features would directly support the "inherently embedded" claim.
- **Transferability experiments**: Since the Discussion invokes transferability, a simple experiment correlating averaged perturbation features with transferability success across testing models would ground the speculation.
- **Error bars on all quantitative results.**

---

## Removed Points

The following points from the input reviews are removed (with justification):

- **"Averaging could create structure rather than reveal it"** — This is logically unsound as a fatal critique: averaging uncorrelated noise yields zero, so structured output implies structured input. However, the *degree* to which features are present in individual perturbations versus emerge only through aggregation is a valid nuance, retained as Major weakness #1 above.
- **"Insufficient causal evidence that features are the *key* factor"** — The contour extraction experiment (Section 5.2.3) does provide causal evidence: removing contour regions degrades attack effectiveness substantially. The critic's concern about gradient-based attacks inherently weighting contour pixels is valid context but does not invalidate the finding.
- **"The paper does not control for contour having different L2 norm"** — The paper explicitly addresses this: "the areal ratio of the contour to the background stands at 0.83" (Section 5.2.3), showing contour is *smaller* yet more effective. This is a control.
- **"Missing ensemble attack baseline"** — A valid suggestion but not a weakness; moved to Nice-to-Haves.
- **"Model sourcing details insufficient"** — The paper states "274 models with diverse sets of architecture from PyTorchCV." While more detail would be nice, the description is adequate for the paper's scope. The ResNet-50 white-box concern is mentioned but acknowledged by the paper.
- **"Domain shift in machine evaluation should be quantified"** — The paper acknowledges this limitation and uses scaling (×0.5) to mitigate it. A reasonable approach for a conference paper.
- **"No participant-level analysis for human evaluation"** — Partially valid (lack of variance), retained as Minor weakness #4 with broader variance concern.
- **Search-based attacks needing quantitative evaluation** — Retained as Minor weakness #1.
- **Strength Finder's Supporting Strength #1 (Discussion explanations are "grounded in experimental findings")** — Removed because the Discussion section is indeed speculative, not experimentally verified. The Strength Finder overstates the grounding.
- **Strength Finder's Supporting Strength #2 (targeted attack demonstration)** — Partially retained: the existence of the generation effect is worth noting, but the section is too preliminary to count as a major strength.

---

## Novel Insights

None beyond the paper's own contributions. The reviews surface no novel synthesis that the paper does not already articulate.

---

## Suggestions

1. **Reframe the central claim** from "perturbations inherently contain human-identifiable features" to "averaging perturbations across many diverse models reveals human-identifiable features that are predictive of attack effectiveness." This aligns the claim with the actual evidence and is still a strong, novel contribution.
2. **Add an emergence curve experiment** showing feature quality (recognizability or cosine similarity to final averaged version) as a function of the number of averaged perturbations (m = 1, 5, 10, 50, 100, 270) at a fixed n (noise copies). This would directly support the noise-reduction narrative.
3. **Include MNIST and CIFAR-10 results** in the main text (at minimum one figure and one table per dataset), or revise the abstract to reflect the actual scope.
4. **Add error bars or confidence intervals** to all quantitative results (recognizability, attack accuracy, cosine similarity).
5. **Provide per-model breakdowns** for the four testing models in the attack strength and contour extraction experiments, rather than only reporting averages.
6. **Add quantitative results for targeted attacks** (at least attack success rates and recognizability), and discuss the limitations of the generation effect more thoroughly.

---
