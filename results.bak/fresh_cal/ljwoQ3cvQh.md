I have all the information I need from the paper. Let me now produce the final consolidated review.

---

## Summary

This paper documents a specific, repeatable pattern in how trained neural networks behave on out-of-distribution (OOD) inputs: predictions converge toward the optimal constant solution (OCS)—the best input-independent prediction under the training loss. The authors support this with experiments across 8 datasets, 3 loss functions (cross-entropy, MSE, Gaussian NLL), and both CNN and Transformer architectures (ResNet, VGG, DistilBERT). They provide a mechanistic explanation: OOD features have smaller norms and lie increasingly outside weight-matrix subspaces, causing bias-dominated outputs that approximate the OCS. This is supported by both empirical analysis (feature norm ratios, subspace alignment, bias accumulation) and a theoretical treatment in deep homogeneous ReLU networks. Finally, they demonstrate a practical application: choosing a loss function whose OCS aligns with cautious behavior yields automatic risk-sensitive decision-making on OOD inputs.

---

## Strengths

1. **Extensive empirical validation of the reversion-to-OCS hypothesis across diverse settings.** The paper demonstrates that neural network predictions converge toward the OCS on OOD inputs across 8 datasets (CIFAR10-C, ImageNet-R/S, OfficeHome, BREEDS, etc.), 3 loss functions, multiple architectures, and both natural and synthetic distribution shifts. Figure 3 (fig:experiments1) shows a clear monotonic decrease in distance-to-OCS as the OOD score increases. This goes substantially beyond prior work (e.g., Hendrycks et al.'s observation about softmax confidence) by generalizing to arbitrary loss functions and continuous outputs.

2. **Mechanistic explanation supported by direct empirical evidence.** The paper identifies a concrete mechanism: OOD features have smaller norms (Fig. 4, first column), lie increasingly outside the span of weight matrices (Fig. 4, second column), and the accumulation of bias terms closely approximates the OCS (Fig. 4, third/fourth column). This decomposition explains *why* predictions revert to a constant, going beyond a purely descriptive finding.

3. **Theoretical analysis in a simplified setting that corroborates the mechanism.** Propositions 1–2 and Theorem 1 (Section 4.2) provide formal bounds for deep homogeneous ReLU networks, showing that training-data features maintain high norm while OOD features can collapse because they lie outside a narrow rank-1 subspace. The authors are transparent that this is a simplified setting, and the theory is presented as supporting evidence rather than a proof of the general phenomenon.

4. **Practical demonstration of controllable OOD behavior via loss design.** Section 5 shows that by choosing a loss function whose OCS corresponds to a cautious action (e.g., abstention in selective classification), the model automatically makes risk-averse decisions on OOD inputs. Figures 6–7 show reward prediction (MSE) increasingly abstains and outperforms standard classification on OOD inputs. The authors are appropriately measured in their claims, stating they are not aiming for SOTA.

---

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

1. **The discriminator-based OOD score used in the cross-dataset comparison (Fig. 2/fig:experiments1) is a potential confound.** The paper measures "how OOD" an input is using a low-capacity discriminator trained to distinguish train from evaluation data. This conflates distributional shift with the ease of discrimination by a particular model. While the within-dataset experiments with explicit shift parameters (rotation, noise) in Figs. 1 and 3 partially mitigate this concern—they show the same trend using controlled, interpretable shifts—the paper would benefit from either (a) complementing the discriminator score with a standard distribution distance metric (e.g., MMD, FID, likelihood under a density estimator), or (b) discussing the limitations of the learned score more explicitly. The paper does not specify the architecture or training details of the discriminator model (line 101).

2. **The theoretical analysis does not directly cover the full experimental scope.** Propositions 1–3 and Theorem 1 are derived for deep homogeneous ReLU networks with binary labels, exponential loss, and gradient flow. The authors acknowledge this is a "simplified setting" (lines 22, 139). However, the gap between this setting and the experiments (ResNets, Transformers, cross-entropy, MSE, Gaussian NLL, continuous outputs) is large. The theory provides *plausible* support for the mechanism but does not constitute a proof for the general phenomenon. The paper would be stronger if it explicitly mapped which empirical findings the theory covers and which require additional assumptions.

3. **The reward structure for the MSE models (+1, -4, 0) is not tested for sensitivity.** The selective classification demonstration relies on a manually defined reward function. The paper does not discuss whether the results would hold under different reward ratios, or at what point the OCS-based abstention behavior would break down. This limits the generality of the decision-making application demonstration.

4. **Statistical quantification of the main trend is missing.** Figure 3 shows a clear visual trend with error bars over 5 runs, but no correlation coefficient, slope estimate, or confidence interval is reported. A simple quantitative measure (e.g., Spearman rank correlation between OOD score and distance-to-OCS) would sharpen the claim and facilitate comparisons across settings.

### Trivial

1. **The title "Deep Neural Networks Tend To Extrapolate Predictably" is broader than the paper's scope.** The paper studies one specific form of predictability (reversion to the OCS), not all dimensions of extrapolation behavior. The abstract and hypothesis box (line 17) clarify the scope immediately, so this is a framing issue only. A more precise subtitle (e.g., "… Predictably: Reversion to the Optimal Constant Solution on OOD Inputs") would better match the content.

---

## Nice-to-Haves

- **A counterexample or discussion of when reversion fails.** The paper shows that reversion holds across many settings but does not characterize negative cases. A single example where predictions *diverge* from the OCS (e.g., under adversarial perturbations, or with certain architectures/shift types) would sharpen the claim and increase credibility. The authors already acknowledge this gap in the conclusion (lines 224–226).

- **Bias ablation experiment.** Training models *without* bias terms and testing whether reversion to the OCS still occurs would directly test the proposed mechanism. If it still occurs, the explanation is incomplete; if it does not, this strongly supports the mechanism.

- **Broader architecture coverage.** The paper tests CNNs and DistilBERT. Including a vision transformer (ViT) or a purely MLP-based architecture would help show the phenomenon is not tied to convolutional inductive biases.

---

## Removed Points

These points were flagged in the reviews but are removed or downgraded for the following reasons:

- *"Cannot assess the proofs without the appendix"* — Removed per hard rule: appendix sections are stripped by the parser and exist in the original submission. This not a valid criticism of the paper as presented.
- *"The y-axis scales are clipped/trimmed"* — Removed as a PDF extraction artifact, not an author error.
- *"The paper does not need a major overhaul" / "Accept with minor revisions"* — This is an overall assessment in the reviewer's voice, not a weakness. Absorbed into the main review's tone.
- *"The paper should include a negative example"* — Moved to Nice-to-Haves; it is a suggestion for improvement, not a flaw in the current evidence.
- *"The theoretical analysis could be made more directly testable"* — Moved to Nice-to-Haves; this is a suggestion, not a verified weakness.
- Strength Finder's characterization of the paper as "surprisingly good results" — Retained only the concrete strengths; generic enthusiasm removed.
- *"The evaluation lacks rigor"* (no concrete anchor) — Removed; no specific sentence, equation, or figure in the paper supports this claim.

---

## Novel Insights

None beyond the paper's own contributions.

---

## Suggestions

1. In the evaluation protocol (Section 3), add a standard distribution distance metric (e.g., MMD, FID) alongside the discriminator-based OOD score, or at minimum discuss the limitations of the learned score and specify the discriminator architecture.
2. Report a quantitative correlation measure (e.g., Spearman's ρ or a slope estimate) for the trend in Figure 3.
3. Add a brief sensitivity analysis for the reward structure (+1/-4/0) used in the selective classification experiments to show how robust the OCS-based abstention behavior is to different reward ratios.
4. Consider softening the title or adding a qualifying subtitle, and add an explicit sentence in the introduction or conclusion about the scope of "predictability" studied.

---

## Score and Decision

MY FINAL SCORE: <score>7.5</score>
MY FINAL DECISION: <decision>Accept</decision>