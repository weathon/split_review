Now I have a good comparative picture. Let me finalize:

**Round 1 bracket**: 5.5–7.0

**Round 2 narrowing**: The paper sits above "How to Probe" (6.25) and comparable to "QPM" (6.67), slightly below "On the Foundations of Shortcut Learning" (6.80). It has stronger theoretical contributions than the 6.25 anchor and more diverse experiments, but falls short of the foundational depth of the 6.80 anchor. I place it at **6.0**.

Now let me write the final consolidated review.

---

## Summary

This paper identifies a theoretical limitation of HiResCAM explanations — they are not uniquely determined due to softmax invariance, admitting an arbitrary additive shift matrix M — and proposes ContrastiveCAMs, which are invariant to this shift. Building on this, the paper introduces Core-Focused Cross-Entropy (CFCE), a training loss that penalizes non-core region contributions using ContrastiveCAMs, thereby encouraging models to rely on intended object regions rather than spurious background cues. Experiments on Hard-ImageNet, Oxford-IIIT Pets, and PASCAL VOC demonstrate that CFCE-trained models substantially increase reliance on core regions (measured via IoU with core masks and accuracy degradation under core-region ablation) while maintaining competitive clean accuracy.

## Strengths

- **Rigorous theoretical identification of a HiResCAM limitation**: Theorem 3.2 proves that HiResCAM explanations are only determined up to an additive matrix M that shifts all class CAMs identically — a consequence of softmax shift-invariance that, to my knowledge, has not been previously formalized. This is a clean, verifiable theoretical observation.

- **ContrastiveCAMs provide an elegant, invariant solution**: Definitions 3.3–3.4 and Theorem 3.5 establish that pairwise CAM differences are M-invariant. This is a natural fix that additionally provides class-versus-class explanations, enabling granular analysis of which image regions drive specific pairwise discriminations (demonstrated qualitatively in Figure 2).

- **Well-motivated training method with theoretical grounding**: Proposition 4.2 cleanly reformulates cross-entropy in terms of ContrastiveCAMs and a binary core mask H, showing that standard CE does not distinguish core from non-core regions — a crisp theoretical basis for why feature misalignment occurs. CFCE (Definition 4.5) follows naturally, and Theorem 4.6 establishes that it is classification-calibrated with respect to the core-constrained risk.

- **Strong empirical results on feature alignment**: On Hard-ImageNet (Table 2), CFCE+KL achieves 93.39% ContrastiveCAM IoU and reduces accuracy under core-region ablation from 76.53% (CE baseline) to 45.49%, demonstrating that the model has been forced to rely predominantly on core regions. GradCAM IoU also improves substantially (16.25% → 51.52%), providing an independent metric not directly optimized by the loss.

- **Robustness to approximate supervision**: On Oxford-IIIT Pets (Table 3), CFCE trained with SAM auto-masks or bounding boxes achieves IoU of 85.16% and 84.61% respectively while maintaining >99% validation accuracy, showing the method does not require pixel-perfect core annotations.

## Weaknesses

### Fatal

None.

### Major

- **No out-of-distribution or robustness evaluation**: The paper's core motivation is preventing shortcut learning and improving feature alignment so that models generalize better. However, all evaluations are in-distribution — core-ablation tests measure exactly what the loss was designed to optimize, and the segmentation transfer experiment uses the same dataset (PASCAL VOC) for both classification pre-training and segmentation fine-tuning. An evaluation on a distribution-shift benchmark (e.g., ImageNet-R, ImageNet-Sketch, or a background-swap test set) is needed to verify that improved core-region reliance actually translates to robustness against spurious feature shifts. This is the single most important missing piece of evidence.

- **Scalability concerns unaddressed**: CFCE requires computing C−1 gradient-based ContrastiveCAMs per training sample. For datasets with many classes (e.g., full ImageNet with 1000 classes), this would be computationally prohibitive. The paper evaluates only on datasets with modest class counts (Hard-ImageNet subset, 37-class Pets, 20-class VOC) and provides no discussion of computational cost, memory requirements, or possible approximations. This limits the method's demonstrated applicability and should be addressed.

### Minor

- **HiResCAM motivation is somewhat overclaimed**: Theorem 3.2 shows that HiResCAM explanations admit an additive shift M while preserving softmax probabilities. However, in any trained model, the logits (and thus the HiResCAM) are deterministically computed from the input. The M-shift is inherent to the model's own representation, not an external "corruption." The paper's framing that HiResCAMs "may be misleading" or "fail to guarantee a faithful interpretation" (lines 148, 76) is stronger than what the mathematics supports — the shift represents redundancy in the explanation, not necessarily unfaithfulness. The contrastive formulation is still valuable, but the motivation should be reframed around removing redundancy rather than fixing a "misleading" explanation.

- **No ablation separating CFCE from the KL divergence regularizer**: CFCE and CFCE+KL are both evaluated, but the contribution of the KL term alone is not isolated. On Hard-ImageNet, CFCE+KL shows a large GradCAM IoU jump (18.88% → 51.52%) compared to CFCE alone, while ContrastiveCAM IoU improves more modestly (89.22% → 93.39%). Understanding whether the KL term or the core-focused loss drives the independent GradCAM IoU improvement would strengthen the attribution of gains.

- **Clean accuracy trade-off not discussed**: CFCE models lose non-trivial accuracy compared to cross-entropy baselines: 93.69% → 90.53% (Hard-ImageNet), 95.5% → 92.96% (Pets multiclass). While some trade-off is expected, the paper does not analyze when this trade-off is acceptable, whether it can be tuned, or whether the accuracy gap narrows with different hyperparameters. This context matters for practitioners.

### Trivial

- The consistency proof for Theorem 4.6 is only cited as deferred to the appendix (standard practice, but the claim of classification calibration is central; a sketch in the main text would be helpful).

## Nice-to-Haves

- Comparison against a simple baseline that explicitly masks out non-core regions in the input during training (e.g., training with masked images), to test whether the CFCE loss offers advantages over explicit input-space masking.
- Experiments with additional backbone architectures beyond ResNet-50 to demonstrate generality.
- A discussion of how the bias-free classifier constraint (b = 0) affects standard classification performance, and whether it is a realistic assumption.

## Removed Points

*These points are flagged to be removed; treat them with caution.*

1. **Harsh Critic: "The ContrastiveCAM IoU evaluation is circular"** — While ContrastiveCAM IoU is indeed directly optimized by CFCE, the paper also reports GradCAM IoU (an independent metric that improves from 16.25% to 51.52%) and core-ablation accuracy. The core-ablation test, while aligned with the training objective, is a standard evaluation in this literature (Moayeri et al., 2022) and provides meaningful evidence. The circularity concern is partially valid but was exaggerated; I've reframed it as the need for OOD evaluation.

2. **Harsh Critic: "The reported redundancy ratios (γ in Table 1) are not alarming"** — This is a subjective judgment about whether γ=0.20 or γ=0.37 is significant. The paper uses these to motivate the contrastive formulation; whether one finds them "alarming" is not a substantive weakness.

3. **Harsh Critic: "The segmentation transfer experiment limits generality"** — The paper acknowledges this by doing the experiment on the same dataset. It is still a valid demonstration that core-focused backbones benefit downstream tasks. Not a weakness per se.

4. **Strength Finder: generic/superficial strengths removed** — All retained strengths are concrete and anchored in specific theorems, definitions, or experimental results. None were removed.

5. **Harsh Critic: "Comparison to simpler masking-based approaches"** — The paper already compares against CORM (Singla et al., 2022), which is a core-region masking approach. Explicit input masking is a reasonable additional baseline but its absence does not constitute a major weakness. Moved to Nice-to-Haves.

## Novel Insights

The paper's connection between softmax shift-invariance and HiResCAM non-uniqueness (Theorem 3.2 → ContrastiveCAMs) is genuinely novel. Beyond the paper's own contributions, a cross-cutting observation emerges: the same softmax invariance that causes the HiResCAM ambiguity is also what makes standard cross-entropy blind to whether predictions come from core or non-core regions (Proposition 4.2). This dual role — softmax invariance as both an explanation failure mode and a training blind spot — suggests a deeper principle: interpretability flaws and training pathologies in softmax-based classifiers may share a common algebraic root, and fixing one (via contrastive formulations) can naturally enable fixes for the other (via spatially-aware loss modifications). This is a productive lens for future work connecting interpretability and robust training.

## Suggestions

- Add at least one OOD robustness evaluation (ImageNet-R, ImageNet-Sketch, or a synthetic background-swap test) to directly validate the claim that improved core-region reliance prevents shortcut learning in practice.
- Provide a concrete analysis of computational cost for CFCE (FLOPs, wall-clock time compared to standard CE) and discuss possible approximations (e.g., subsampling contrastive classes, or using a single softplus bound) that could make the method tractable for datasets with more classes.
- Reframe the HiResCAM motivation from "misleading explanations" to "redundancy removal" — the mathematical content is correct, but the practical claim of misleadingness is stronger than the evidence supports.
- Add an ablation that isolates the effect of the KL divergence regularizer from CFCE itself, particularly to understand what drives the GradCAM IoU improvement.

## Score and Decision

**Anchor comparison summary:**

| Anchor | Score | Round | Comparison |
|--------|-------|-------|------------|
| "Coloring Deep CNN Layers" (6u6GjS0vKZ) | 4.25 | 1 | Under review is clearly stronger — more theory, broader experiments |
| "Feature Accompaniment" (oKglS1cFdb) | 5.67 | 2 | Under review is stronger — tighter theory-practice connection, more complete evaluation |
| "A Simple Interpretable Transformer" (bkdWThqE6q) | 6.00 | 1 | Under review is stronger — more theoretical grounding, quantitative metrics, broader experiments |
| "How to Probe" (57NfyYxh5f) | 6.25 | 2 | Under review is comparable or slightly stronger — similar mix of theory + empirical findings, but broader experimental scope |
| "QPM" (GlAeL0I8LX) | 6.67 | 1 | Under review is comparable — both have strong theoretical frameworks and good experiments; QPM has a more elegant optimization, under review has more diverse evaluation |
| "On the Foundations of Shortcut Learning" (Tj3xLVuE9f) | 6.80 | 2 | Under review is slightly below — the anchor is more foundational with deeper theoretical analysis |
| "Don't trust your eyes" (OZWHYyfPwY) | 7.00 | 1 | Under review is below — the anchor is more surprising and paradigm-challenging |

The paper is a solid contribution with real theoretical novelty, a well-motivated method, and convincing (though not comprehensive) experiments. The major weaknesses — lack of OOD evaluation and unaddressed scalability — are significant but addressable. Positioned between the 6.25 and 6.67 anchors, I assign a score of **6.0**, reflecting a paper that makes a clear contribution but has gaps that prevent it from being a standout acceptance.

**Originality**: Good — the HiResCAM non-uniqueness identification and the contrastive-CAM-to-training-loss pipeline are novel.

**Importance**: Moderate — feature alignment and shortcut learning are important problems, and the method provides a new angle, but the limited demonstrated scale and lack of robustness evidence temper the impact.

**Claims supported**: Mostly — the feature alignment claims are well-supported by the Hard-ImageNet and Pets experiments; the robustness/generalization claims are not yet supported.

**Soundness**: Good — the theoretical derivations appear correct, and the experimental setup is reasonable.

**Clarity**: Good — the paper is well-structured and the mathematical exposition is clear.

**Value to community**: Moderate — the contrastive formulation and CFCE loss are potentially useful tools for researchers working on interpretability-guided training.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>