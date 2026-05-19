Now I have a thorough understanding of the paper and have verified the reviewer claims against the actual text. Let me produce the final consolidated review.

---

## Summary

ProtoNMF proposes a post-hoc method to convert a trained black-box image classifier into a prototype-based interpretable model. The approach has two steps: (1) per-class Non-negative Matrix Factorization (NMF) of the backbone's spatial features to obtain parts-based prototypes, and (2) reconstruction of the black-box classification head as a linear combination of those prototypes plus a residual prototype that guarantees exact accuracy recovery. The core innovation is exploring the "reverse direction" — turning a black box into a prototype model rather than training a prototype layer from scratch — while guaranteeing recognition performance on par with the original black box.

## Strengths

- **Guaranteed accuracy preservation**: The reconstruction procedure (convex optimization + residual prototype) recovers the original black-box classifier exactly. Table 2 shows ProtoNMF matches ResNet34's 75.1% top-1 accuracy on ImageNet while the leading prior prototype model (ProtopNet) drops to 65.5%. This is the paper's central claim and is mathematically proven, not empirically approximated.

- **More comprehensive prototypes than prior work**: Table 1 quantitatively demonstrates that NMF prototypes yield lower feature reconstruction error than ProtopNet's selected prototypes across multiple training cycles. Figure 2 provides qualitative confirmation that ProtoNMF's prototypes consistently cover distinct parts (head, belly, wing) and remain diverse across training cycles, whereas ProtopNet's prototypes converge to similar semantics.

- **Cross-architecture and cross-dataset applicability**: Section 4.2 shows ProtoNMF works with ResNet, ViT, and CoC on ImageNet, producing parts-based prototypes in all three (Figure 3). The method succeeds on both fine-grained (CUB) and large-scale (ImageNet) datasets without architecture-specific modifications beyond zero-clipping negative features.

- **Interpretable coefficients reveal model biases**: The case study on "sled dog" (Section 4.2) shows that ProtoNMF's transparent reasoning can expose undesirable model behavior: CoC-tiny places nearly equal weight on human and dog prototypes (0.016 vs 0.019), suggesting a correlation bias, while ResNet and ViT rely more on the dog prototype. This demonstrates a practical benefit of the transparent reasoning process beyond what post-hoc saliency methods provide.

- **Novel post-hoc direction for prototype-based models**: The paper explicitly identifies and pursues the reverse direction — constructing a prototype-based model from a trained black box post-hoc — which it correctly notes is distinct from all prior works that build prototype layers during training (Section 2).

## Weaknesses

### Fatal

None.

### Major

- **Interpretability evaluation is primarily qualitative and lacks standard metrics**: The paper's main selling point is interpretability via prototype-based reasoning, yet the evidence relies almost entirely on qualitative visualizations (Figures 2–4) and one case study. No standard interpretability metrics are reported: no part-purity scores against CUB part annotations (which are available for this dataset), no faithfulness/comprehensiveness measures, no pointing-game accuracy, and no user study comparing explanation quality with existing prototype models. The paper does provide a quantitative metric — feature reconstruction error (Table 1) — as a proxy for prototype comprehensiveness, but this measures coverage of the feature space, not interpretability per se. For a paper whose raison d'être is interpretability, this gap is significant. It does not invalidate the method's contribution, but it means the claim of "meaningful prototypes" and "transparent reasoning" is not supported as rigorously as it should be.

### Minor

- **Limited baseline comparisons for interpretability**: The only experimental baseline is ProtopNet. The accuracy comparison (Table 2) is informative context but somewhat trivially favors ProtoNMF (which inherits black-box accuracy by construction). More importantly, there is no comparison of explanation quality with other prototype-based models (e.g., ProtoPShare, ProtoPool, ProtoTree) or with other post-hoc interpretability methods (e.g., TCAV, concept bottleneck models). The paper acknowledges its specific scope, but since interpretability is a core claimed benefit, a broader comparison would substantially strengthen the evidence.

- **Ad-hoc handling of negative features is not analyzed**: For ViT and CoC (which produce negative feature values due to GeLU activations), the paper sets negative values to zero before applying NMF (Section 3.1). This discards potentially useful information. The paper acknowledges the existence of alternatives like semi-NMF and convex-NMF but provides no analysis of information loss from zero-clipping, no comparison with these alternatives, and no quantitative evidence that the non-negative portion captures "most information." The qualitative results (Figure 3) are suggestive but not sufficient to establish that this truncation is harmless.

- **Residual distribution choice is presented without justification or alternatives**: Equation 8 distributes the residual prototype uniformly across NMF prototypes. This choice is arbitrary, and the paper does not discuss whether alternative distribution strategies (e.g., weighted by prototype importance) would yield more interpretable augmented prototypes. The impact of this design decision on interpretability is unexplored.

- **Negative coefficients complicate the "this looks like that" narrative**: The linear coefficients \(C^c_{opt}\) can be negative (as shown in the sled dog case study). While the paper discusses this and interprets negative coefficients as "less likely if it looks like this," this complicates the clean additive-contributions intuition typically associated with prototype-based reasoning. The paper does not discuss whether constraining coefficients to be non-negative is feasible or what accuracy trade-off it would entail.

### Trivial

- None (all identified issues are at least Minor in significance).

## Nice-to-Haves

- A strategy for automatically selecting the number of prototypes \(p\) per class (e.g., based on an elbow in the reconstruction error curve) would be a practical addition beyond fixing \(p=3\).
- Reporting runtime/computational cost of per-class NMF decomposition (especially for ImageNet's 1000 classes) would help practitioners assess practical feasibility.
- A discussion of failure cases (e.g., classes without clear part structure where NMF prototypes may not correspond to interpretable parts) would strengthen the paper's honesty and help users understand limitations.

## Removed Points

*These points were flagged in the reviews but are removed from the main weaknesses after verification against the paper. Treat them with caution.*

1. **"Paper does not state maximum iteration count or convergence tolerance"** (Harsh Critic): Factually incorrect. The paper explicitly states: "The update will stop when the relative error change is small enough (e.g., \(10^{-4}\)) or maximum iteration times (e.g., 200) is reached" (line 74).

2. **"CUB training checkpoint provenance unclear"** (Harsh Critic): The paper states checkpoints are "trained using the same learning rate schedule as ProtopNet" and are "under the same epochs of ProtopNet." This is sufficiently clear for a paper in this field.

3. **"Missing appendix content"** (Harsh Critic, implicit): The parser strips appendix sections from all papers; they exist in the original submission. Not a valid criticism.

4. **Strength Finder's generic strengths** (e.g., "addressed an important problem"): Removed as generic/superficial; the retained strengths are concrete and evidence-grounded.

5. **"This is the first work constructing a prototype-based model in a post-hoc manner"** as a standalone strength: Retained as part of the "novel direction" strength above; the standalone phrasing was redundant.

## Novel Insights

The most interesting observation that emerges from the review process is the diagnostic value of the coefficient analysis. The sled dog case study (Section 4.2) reveals that different architectures learn different biases: CoC-tiny gives almost equal weight to the human prototype and the dog prototype (0.016 vs 0.019), while ResNet and ViT focus primarily on the dog prototype. This suggests that ProtoNMF's transparent coefficients could serve as a lightweight architecture debugging tool — exposing spurious correlations that would otherwise remain hidden in the black-box weights. This use case (model debugging via coefficient inspection) is arguably at least as valuable as the claimed "interpretable classification" framing, and the paper could foreground it more prominently. The systematic difference in coefficient patterns across architectures is a genuinely novel empirical finding that the paper does not fully exploit.

## Suggestions

1. **Add quantitative interpretability metrics on CUB**: Report part-purity or IoU scores against CUB part annotations. This is the single most impactful addition — it directly measures the "parts-based" claim with an objective, reproducible metric.
2. **Compare explanation quality with at least one other prototype model**: A small-scale comparison with ProtopNet on faithfulness (e.g., comprehensiveness/sufficiency) would substantially strengthen the interpretability claims without expanding the paper's scope.
3. **Analyze the impact of zero-clipping negative features**: Report reconstruction fidelity with vs. without zero-clipping, or compare with semi-NMF on a subset of classes, to quantify information loss.
4. **Discuss or experiment with non-negative coefficient constraints**: Address whether constraining \(C^c_{opt} \geq 0\) is feasible and what accuracy trade-off it entails, since negative coefficients complicate the prototype reasoning narrative.
5. **Foreground the model-debugging application**: The coefficient analysis revealing architecture-specific biases is a strong selling point that the paper currently underplays relative to the "interpretable classification" framing.

## Score and Decision

The paper proposes a genuinely novel approach (post-hoc prototype construction with accuracy guarantee), the methodology is sound and clearly presented, and the core claim (accuracy parity) is mathematically proven and empirically demonstrated. The main weakness is that the interpretability evaluation — the paper's other central claim — relies too heavily on qualitative evidence and lacks standard quantitative metrics. This is a significant gap but not a fatal one: the method's contribution (guaranteed accuracy + post-hoc prototype discovery) remains valuable even with imperfect interpretability validation, and the evidence provided (reconstruction error, qualitative parts-based decomposition, coefficient interpretability) is suggestive and directionally correct.

**Score**: 6.0 — A borderline-to-weak accept. The contribution is real and the method is sound, but the evaluation of the interpretability claim needs strengthening to fully deliver on the paper's thesis. With the suggested additions (particularly quantitative interpretability metrics on CUB), this could be a strong paper.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>