Now I have all the evidence needed. Let me synthesize the final review.

---

## Summary

This paper tackles semi-supervised and weakly-supervised domain generalization for object detection (SS-DGOD and WS-DGOD) by applying the Mean Teacher learning framework. The authors show that training with EMA updates and pseudo-labels leads to flatter minima in parameter space, which theoretically supports better generalization to unseen domains. Based on this interpretation, they introduce a simple output-level regularization that further improves flatness and detection performance. Experiments on an artistic-style dataset demonstrate that the framework approaches fully-supervised DGOD performance, and the paper is the first to formulate the WS-DGOD setting.

## Strengths

1. **Clear empirical demonstration that Mean Teacher works for SS-DGOD and WS-DGOD.** Table 1 is the paper's strongest evidence: WS-DGOD with regularization reaches 62.9 mAP50 on the watercolor target, closely approaching the fully-supervised Oracle upper bound of 62.6. The ablation isolating EMA, pseudo-labeling (PL), and regularization shows each component adds non-trivial gains (e.g., EMA alone lifts Single-DGOD from 50.5 to 55.5).

2. **First formulation of WS-DGOD as a distinct problem setting.** The paper introduces a new, practically motivated setting where only image-level labels are available for additional domains, and proposes a principled refinement step (Eq. 3) that zeros out class predictions inconsistent with the weak labels. This creates a foundation for future work.

3. **Simple, well-motivated regularization that improves flatness and accuracy.** The proposed regularization (Eqs. 7–9) is clean: it adds a loss term using weak augmentation and raw teacher outputs (no post-processing) to force the student to mimic the teacher on the same input. Table 1 shows consistent gains across SS-DGOD, WS-DGOD, and UDA-OD (e.g., watercolor: 58.2→58.2 for SS-DGOD, 59.7→62.9 for WS-DGOD). Figure 2 directly verifies that the regularized model has lower loss change under parameter perturbation—i.e., flatter minima.

4. **Quantitative flatness evaluation supporting the interpretation.** Figure 2 measures loss change under random parameter perturbations for both training and test losses, showing that EMA, pseudo-labeling, and regularization each contribute to flatter minima. This evidence connects the proposed method to the well-established finding that flat minima improve domain generalization.

## Weaknesses

### Fatal

None.

### Major

None.

### Minor

1. **The theoretical link between pseudo-labeling and flat minima has logical gaps.** Section 5.4 argues that (a) the teacher has flat minima via EMA, (b) pseudo-label training aligns student outputs with teacher outputs, (c) similar outputs → similar loss values (Proposition 1), therefore (d) the student reaches flat minima. Step (d) does not follow directly from the argument presented. Proposition 1 establishes that *loss values at two different points* are close when the outputs are close—but this does not imply that the *loss landscape around a single point* has low curvature. The paper would need to show that pseudo-label training pulls the student toward the teacher in *parameter space* (not just output space) or that the training dynamics introduce a regularizing noise that biases toward flat regions. The paper acknowledges some of these limitations (Section 7), but the interpretation section still claims a causal link it does not fully substantiate.

2. **Experimental validation is limited to one dataset type in the main paper.** All main-paper experiments use artistic-style images (natural, clipart, comic, watercolor) from a single dataset. The introduction cites weather and time-of-day domain shifts (Li et al.) as motivating examples, but no experiments on those shift types are presented in the main paper (supplementary results on another dataset are mentioned but not accessible in this review). For a paper whose interpretive claims about flat minima are meant to carry across diverse domain gaps, this scope is narrow. The conclusions would be considerably strengthened by demonstrating the same effects on qualitatively different domain shifts (e.g., synthetic→real, daytime→nighttime).

3. **No statistical significance or variance reported.** Results are single-run with no error bars. Given that the improvements over baselines are in the 1–3 mAP range and test set sizes are modest (1,000–2,000 images), it is difficult to assess whether the gains are reliable. This is a standard expectation for empirical papers, even analysis-oriented ones.

4. **Absence of SWA/SWAD comparison weakens the "EMA → flat minima" claim.** The paper acknowledges that SWA and SWAD establish weight averaging → flat minima, then claims "we found that a simple EMA also leads to flat minima." But EMA is a form of weight averaging, so this is consistent with existing knowledge rather than a new discovery. Without comparing EMA to SWA/SWAD under the same conditions, the paper cannot show whether EMA has any distinctive advantage or whether any averaging scheme would suffice. This undercuts the novelty of the "interpretation" component.

5. **No non-trivial baseline for WS-DGOD.** Since the paper introduces WS-DGOD, the only comparisons are to its own ablations and to Single-DGOD/DGOD/Oracle upper bounds. While Single-DGOD is a reasonable point of comparison, the paper would benefit from at least one adapted baseline—for example, applying an existing weakly-supervised object detection method to each domain independently, or a simple two-stage approach that trains a classifier on weak labels and uses it to filter detector outputs.

### Trivial

- The flatness measurement in Figure 2 (line 446) uses a perturbation radius γ in the formula but does not report the actual numeric γ value used in the experiment, making the result harder to reproduce.
- No sensitivity analysis is provided for the regularization strength β=0.5 or the EMA decay α=0.9996, though both are fixed across all experiments.

## Nice-to-Haves

- An analysis of whether the same effects hold with hard pseudo-labels (e.g., standard Faster R-CNN) rather than the Gaussian Faster R-CNN architecture would clarify whether the flatness benefits are tied to the soft-labeling design.
- A discussion of failure cases (which object classes or domain pairs see the smallest gains) would improve the paper's practical value, as the authors note this is left for future work.

## Removed Points

- **Criticism about Gaussian FasterRCNN being a "non-standard" architecture:** Removed because the paper explicitly states (line 165) that the Mean Teacher framework can be applied to any object detector, and the choice of Gaussian FasterRCNN follows prior work (Chen et al., 2022). This is a standard design choice for soft pseudo-labeling, not a limitation.
- **Criticism about CDDMSL comparison being unfair:** Removed because the paper transparently acknowledges the backbone-dependence issue (lines 426–427). The same-backbone comparison is a valid additional data point; the paper does not claim to outperform CDDMSL in its intended configuration.
- **Criticism about the regularization loss being unclear:** Removed because the paper clearly specifies the loss structure in Eq. (9) (both losses added together) and states that the same weakly augmented image is used. The description is not ambiguous.
- **Claim that Proposition 1 is "trivial and irrelevant":** Downgraded. The proposition is a simple mathematical observation, but it plays a supporting role in the argument (not a central theoretical claim). The substantive issue—that similar loss values at two points do not imply a flat landscape—is kept in Weakness 1 above.
- **Strength Finder strength about "novel interpretation" being fully novel:** Tempered to match the verified weaknesses. The interpretation is incremental rather than fundamentally new, though connecting it to the DGOD context is a useful framing.

## Novel Insights

The most interesting observation to emerge from this review is that the paper's two claims—(1) "Mean Teacher works for SS-DGOD/WS-DGOD" and (2) "it works because of flat minima"—are at different levels of support. Claim (1) is well-supported by Table 1 and the ablation. Claim (2) is plausible and consistent with prior theory (Cha et al. 2021, Izmailov et al. 2018) and with the paper's own flatness measurements in Figure 2, but the causal mechanism linking *pseudo-labeling specifically* to flatness is asserted rather than rigorously argued. The paper is strongest when read as an empirical demonstration with a plausible post-hoc interpretation, and weakest when it claims the interpretation as a novel theoretical contribution.

## Suggestions

1. **Add error bars** (at least 3 random seeds) to all main results to establish reliability of the 1–3 mAP gains.
2. **Include at least one comparison to SWA or SWAD** under the same conditions to contextualize whether EMA offers any distinctive benefit over other weight-averaging schemes.
3. **Report the numeric γ value** used in the flatness measurement (Figure 2) for reproducibility.
4. **Add a WS-DGOD baseline**, even a simple one: e.g., train a multi-label classifier on the weak labels and use it to post-filter Single-DGOD detector outputs.
5. **Strengthen the flat-minima interpretation** by either (a) showing that pseudo-label training pulls the student *parameters* toward the teacher (not just the outputs), or (b) connecting pseudo-labeling to existing theoretical results on noise-induced bias toward flat minima, or (c) reframing the interpretation as a plausible heuristic rather than a claimed causal mechanism.

---

## Score and Decision

MY FINAL SCORE: <pineapple>5.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>