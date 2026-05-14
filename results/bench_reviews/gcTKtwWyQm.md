## Summary

This paper introduces a method for generating disentangled counterfactual explanations for unsupervised deep image anomaly detectors. Adapted from the DISSECT framework, the approach trains a concept-conditioned GAN to transform anomalous images into multiple normal-looking counterfactuals along different semantic concepts. The method is evaluated across three anomaly detectors (DSVDD, BCE/OE, HSC) and five datasets (MNIST, Colored-MNIST, CIFAR-10, GTSDB, ImageNet-Neighbors). The paper also uncovers a classifier bias phenomenon where supervised classifiers trained on limited anomaly subsets fail to generalize to unseen anomaly types.

## Strengths

- **First counterfactual explanation method for unsupervised image anomaly detection**: Section 2 confirms no prior CE methods exist for unsupervised image AD, while prior supervised approaches (Sanchez et al., 2022; Ahamed et al., 2024) require labeled anomalies. This is a genuinely novel contribution to a recognized gap.

- **Quantitative evidence that generated counterfactuals appear normal to the detector**: Table 1 shows AuROC values near 50% for BCE on CIFAR-10 (50.0%), GTSDB (49.2%), and Colored-MNIST (51.0%), meaning the detector cannot distinguish counterfactuals from normal data — directly validating the core claim that anomalies are successfully transformed into normal-looking samples.

- **Demonstrated semantic advantage over feature attribution methods**: Figure 7 compares CEs against FCDD heatmaps on Colored-MNIST. Heatmaps localize spatial features (digit strokes) but miss the color anomaly entirely, while the second CE concept successfully identifies color as an anomalous aspect by recoloring digits red. This is a concrete, well-illustrated finding.

- **Disentanglement of multiple anomalous aspects**: Table 4 demonstrates concept classifier accuracy up to 97.2% on Colored-MNIST for BCE, confirming the method generates genuinely distinct counterfactuals per concept rather than redundant outputs.

- **Discovery of supervised classifier bias in AD**: Section 4.4 identifies that supervised classifiers trained with limited anomaly subsets exhibit strong bias, with AuROC dropping from 98 to 75 when trained only on blue anomalies, and Figure 8 visually confirms this via CEs that only produce normal-looking outputs for seen anomaly colors. This is a genuine scientific finding independent of the main explanation claim.

- **Generality across detectors and datasets**: The method is evaluated on three distinct AD methods (DSVDD, BCE/OE, HSC) and five datasets including a DiffEdit-based adaptation for higher-resolution ImageNet-Neighbors images, showing the framework is not tied to a specific detector architecture.

## Weaknesses

### Fatal
None.

### Major

- **The defining "minimal changes" property of counterfactuals is never quantitatively measured**: The paper defines a CE explicitly as requiring ‖x̄* − x*‖₁ ≤ ε (Section 3.1, line 40), yet the evaluation reports no L1 distances between anomalies and their counterfactuals on test data. The reconstruction loss L_rec and cycle consistency loss L_cyc encourage minimal changes during training, but these are training objectives, not post-hoc evaluation metrics. The quantitative evaluation (Section 4.3) assesses normality (AuROC), realism (FID), and disentanglement (concept classifier accuracy) — all important — but omits proximity, which is one of the two defining properties of a counterfactual alongside normality. The qualitative figures (2–6) are visually suggestive of minimal changes, but without reported distances, a reader cannot judge whether the CEs are genuinely minimal counterfactuals or merely arbitrary normal-looking samples. This gap significantly weakens the claim that the method produces valid counterfactuals.

### Minor

- **Concept disentanglement is validated only by self-consistency**: The concept classifier *R* is trained to predict which concept index *k* was used as input. High accuracy (Table 4) confirms the generator can separate the *K* modes, but this is a self-consistency check — it does not demonstrate that the concepts correspond to semantically interpretable axes of the data. The qualitative examples (e.g., Figure 2 showing digit-change vs. color-change as separate concepts) are suggestive, and Figure 7 provides some external validation, but a more principled assessment (e.g., human judgment of whether the two concepts capture distinct meaningful aspects) would substantially strengthen the semantic-disentanglement claim.

- **No comparison with simpler counterfactual generation baselines**: The paper compares against feature attribution methods (FCDD heatmaps in Figure 7), which is valuable. However, it does not compare against straightforward alternative approaches for generating counterfactuals, such as targeted adversarial perturbations with an L1 constraint or a basic autoencoder that directly minimizes L1 while targeting a low anomaly score. Such baselines would help demonstrate that the complex GAN-based procedure with six loss terms offers advantages beyond what simpler methods could achieve. This does not invalidate the contribution but limits the persuasiveness of the method's design choices.

- **The explanation claim could benefit from stronger validation**: The paper asserts that CEs provide "semantic explanations" revealing why the detector flagged an instance as anomalous. The primary evidence is that CEs are normal (Table 1), realistic (Table 3), and capture aspects missed by heatmaps (Figure 7). However, the paper does not demonstrate that the specific modifications in the CE causally correspond to the detector's actual decision factors — as opposed to the generator exploiting any transformation that reduces the anomaly score. The counterfactual framework inherently addresses this (showing what must change to achieve normality *is* the explanation), but a simple ablation study (e.g., applying only the identified change, such as recoloring, and measuring the resulting anomaly score drop) would convert this from a plausible claim to a demonstrated one.

### Trivial

- The normalized FID ratio (Table 3) is presented as an intuitive score, which the paper itself acknowledges, but dividing one FID by another does not yield a percentage with a principled statistical interpretation. This is a minor presentation issue that does not affect the substantive conclusions.

## Nice-to-Haves

- Extending evaluation to standard industrial anomaly detection benchmarks (e.g., MVTec AD, VisA) to test generalization beyond semantic/category-level AD to defect-level AD, though the paper explicitly scopes itself to semantic AD and this is not a flaw.
- A user study assessing whether human judges find the CEs interpretable and whether the disentangled concepts align with human-understandable semantic axes.
- Training the generator using only normal data and pseudo-anomalies (as alluded to in Section 3.2) to test applicability in a fully unsupervised regime without outlier exposure.

## Removed Points

These points are flagged to be removed, treat them with caution:

- **"Every experiment uses OE, conflicting with the claimed unsupervised setting"**: The paper includes DSVDD, which is purely unsupervised and does not use OE. The paper also explicitly acknowledges that DSVDD performs worse than OE-based methods and attributes this to the lack of auxiliary anomaly data. The claim in the introduction that anomalies "can be rare and unlabeled" describes the general AD challenge, not a claim that the method never uses OE. The paper is transparent about its use of OE where applicable. Removed as factually inaccurate.

- **"Datasets exclude standard visual-anomaly-detection datasets such as MVTec AD"**: Section 4.1 (line 118–119) explicitly states: "Our experiments focus on semantic image-AD rather than low-level AD, where anomalies are defects instead of out-of-class (such as in datasets like MVTec-AD)." The paper deliberately scopes itself to semantic AD. Criticizing it for not addressing defect-level AD is scope creep. Removed.

- **"The framing overstates the evidence — terms like 'semantic explanation' and 'unprecedented level of abstraction' are premature"**: This is a stylistic judgment about writing tone, not a substantive methodological concern. The paper's evidence for semantic-level explanation is partial but not absent. Removed as a style nitpick.

- **"No user study, no causal intervention studies"**: These are encapsulated more precisely in the weaknesses above (minor: explanation validation). The demand for user studies is not standard for algorithmic counterfactual generation papers in this community; the demand for causal intervention is addressed as a nice-to-have validation that would strengthen but is not required to establish the contribution. The core criticism (insufficient validation of explanation claims) is retained in weakened form under Minor weaknesses.

## Novel Insights

The most genuinely novel observation in this paper is the classifier bias finding in Section 4.4: when a supervised classifier is trained for anomaly detection using only a limited subset of anomaly types (e.g., only blue anomalies), its decision boundary becomes biased toward detecting only those seen types, and counterfactuals generated for that classifier fail to produce normal-looking outputs for unseen anomaly colors. This is demonstrated through both quantitative AuROC drops and qualitative CE differences, and it provides empirical evidence supporting the value of unsupervised or OE-based AD methods over supervised classification in AD settings — a finding that goes beyond the paper's main explanation contribution.

## Suggestions

- Report L1 distances between anomalies and their CEs across all datasets and detectors. This is the single most important addition needed to strengthen the paper, as it directly addresses whether the method produces valid (proximal) counterfactuals.
- Add a simple baseline: a targeted adversarial attack with an L1 penalty/early stopping to show the GAN-based method offers advantages beyond what direct optimization can achieve.
- Include a small-scale causal ablation: select a subset of anomalies where one concept changes color and another changes shape; apply only the color change (e.g., via a simple color transfer) and measure whether the anomaly score drops. This would directly validate that the CE-identified features are causally relevant to the detector.
- Consider adding failure case analysis to provide a more complete picture of the method's limitations.

## Score and Decision

**Calibration anchors retrieved and comparison:**

| Path | Avg Score | Comparison |
|------|-----------|------------|
| gqeXXrIMr0 (Region-Constrained VCEs) | 6.00 | More rigorous evaluation with stronger baselines and clearer validation; our paper has broader detector/dataset coverage but weaker proximity validation |
| w7pMjyjsKN (CF-CBMs) | 6.75 | Stronger theoretical grounding and tighter integration of counterfactuals into model design; our paper addresses a harder unsupervised setting but with less rigorous validation |
| 9TpgFnRJ1y (CE for Real-Time) | 4.25 | Evaluated on only one dataset, weaker results; our paper has substantially broader evaluation and more compelling findings |
| WYsLU5TEEo (CE for Robustness) | 2.50 | Limited evaluation, confusing methodology; our paper is clearly stronger |
| 6hP9JcXpNk (Beyond Familiar Features) | 3.67 | Different topic (AD method, not explanation); our paper is more novel within its niche |

The paper is positioned between the 4.25 and 6.0 anchors. The core novelty (first CE method for unsupervised image AD) and the breadth of evaluation are genuine strengths. The classifier bias finding is a valuable standalone contribution. However, the omission of the L1 proximity measurement — a defining property of counterfactuals that the paper itself enumerates — is a significant evaluation gap that prevents the paper from reaching the rigor of the 6.0+ anchors. The paper's contribution is real but incompletely validated.

MY FINAL SCORE: <pineapple>5.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>