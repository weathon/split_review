Now I have enough information to calibrate. Let me synthesize the final review.

My initial bracket was (4.5, 7.0). The paper is clearly stronger than: TextCAM (3.67), ClusCAM (4.67), Subset Selection Attribution Regularization (4.00), and Shapley-based paper (5.00). It has genuine theoretical contributions and strong empirical results. However, it falls short of the 6.5-7.0 papers in terms of evaluation breadth and completeness. I'll place it at **6.0**.

---

## Summary

This paper identifies a theoretical flaw in HiResCAM explanations — that they are not uniquely determined because adding an arbitrary matrix *M* to all class CAMs leaves the softmax probabilities unchanged. To address this, the authors propose **ContrastiveCAMs**, which are invariant to this spurious shift and provide class-versus-class explanations. Analyzing ContrastiveCAMs reveals that models often rely on non-core (background) regions. The paper then leverages this insight to design **Core-Focused Cross-Entropy (CFCE)**, a loss function that penalizes attention on non-core regions during training. Experiments on Hard-ImageNet, Oxford-IIIT Pets, and PASCAL VOC show large improvements in IoU alignment and downstream segmentation performance.

## Strengths

1. **Novel theoretical discovery about HiResCAMs (Theorem 3.2).** The paper proves that HiResCAM explanations are not uniquely determined — adding an arbitrary matrix *M* to all class-level CAMs preserves the predicted probabilities while changing the explanations. This is a genuine and non-obvious theoretical finding about a widely-used interpretability method.

2. **ContrastiveCAMs provide M-invariant explanations (Theorem 3.5).** The proposed ContrastiveCAMs provably eliminate the redundancy identified in Theorem 3.2, and additionally offer granular class-versus-class explanations that reveal regions hidden by standard HiResCAMs (Figure 2). This is a principled fix backed by formal guarantees.

3. **Strong empirical alignment gains (Table 2).** On Hard-ImageNet, CFCE+KL raises ContrastiveCAM IoU from 30.27% to 93.39% and relative foreground sensitivity (RFS) from negative to positive (+0.236), demonstrating that the model shifts dependence from non-core to core regions. The GradCAM IoU improvement from 18.44% to 51.52% under KL regularization is particularly striking.

4. **Consistency theorem for CFCE (Theorem 4.6).** The paper proves that optimizing Core-Focused Cross-Entropy is classification-calibrated with respect to the core-constrained risk minimization objective, providing a theoretical guarantee that minimizing CFCE leads toward the desired alignment behavior.

5. **Transfer of alignment to downstream segmentation (Figure 4).** Backbones trained with CFCE+KL improve mean IoU on PASCAL VOC segmentation in both fine-tuning and end-to-end settings, showing that the alignment benefit transfers to dense prediction tasks beyond classification.

6. **Robustness to mask quality (Table 3).** CFCE achieves competitive IoU even with coarse supervision (bounding boxes) or automatically generated masks (SAM), reducing the practical barrier to using the method.

## Weaknesses

### Fatal

None.

### Major

- **Narrow comparison with existing feature-alignment methods.** The paper compares only with CORM and DFR on Hard-ImageNet, and only with cross-entropy baselines on other datasets. Multiple prior approaches to background suppression and saliency regularization are cited in the related work (Kc et al., Aniraj et al., Ismail et al.) but never evaluated as baselines. Given the paper's central goal of improving feature alignment, this limits the reader's ability to assess whether CFCE offers a meaningful advance over simpler or prior alternatives.

- **Only ResNet-50 is tested.** All experiments use a single architecture. The method's assumption of a linear classifier (Eq. 1) is standard in modern ConvNets, but the paper does not test whether CFCE transfers to other backbones (e.g., VGG, DenseNet, ConvNeXt) or to architectures without a simple single-layer classifier. Architecture generality is left entirely unexplored.

### Minor

- **Training procedure with CAM-based losses is underspecified.** The loss functions (Eqs. 15, 18) depend on ContrastiveCAMs, which in their general form involve gradients of logits with respect to feature maps. The paper assumes a linear classifier (Eq. 1), under which HiResCAMs simplify to a weighted sum of feature maps (making them differentiable and training straightforward). This assumption and its implications for architectures without a linear classifier should be stated explicitly rather than left implicit.

- **Practical significance of HiResCAM non-uniqueness is not demonstrated.** Theorem 3.2 is mathematically correct, but the paper does not show a concrete case where the *M*-redundancy leads to a misleading interpretation in a real trained model (as opposed to the toy illustration in Figure 1). The γ redundancy measure in Table 1 captures one specific quantity (average CAM relative to target CAM), not the full space of possible *M*. The theoretical motivation would be more compelling with a practical demonstration of misleading HiResCAMs that ContrastiveCAMs correct.

- **No hyperparameter sensitivity analysis.** The KL regularization introduces λ₁, λ₂, λ₃ with no ablation or sensitivity study. Even a brief analysis (e.g., varying λ₁ over one order of magnitude) would significantly strengthen confidence in the method's robustness.

- **Accuracy-alignment trade-off is noted but not discussed.** Table 2 shows unablated accuracy dropping from 94.25% (CE) to 90.35% (CFCE+KL). The paper acknowledges this cost but does not discuss its practical implications or when the trade-off is acceptable.

### Trivial

- No computational cost analysis (training time compared to cross-entropy is not reported).

## Nice-to-Haves

- A discussion of when weaker masks (e.g., bounding boxes) remain acceptable would help practitioners decide what supervision is sufficient.
- A failure case analysis (e.g., images where CFCE degrades accuracy without improving alignment) would strengthen the discussion of limitations.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **Harsh Critic Point 4 (architecture modifications not in main text):** The paper states the interpretability-motivated modifications are detailed in Appendix C. Per policy, parser-stripped appendices are not a valid criticism.
- **Harsh Critic Point 5 (asymmetric metric — ContrastiveCAM IoU for proposed method vs GradCAM IoU for baselines):** The paper explicitly acknowledges this asymmetry (lines 316-317) and justifies it: GradCAMs have been shown to be unfaithful, and GradCAM IoU is also reported for proposed methods. The GradCAM IoU improvement (16.25 → 51.52) independently corroborates the result.
- **Strength Finder strengths about "important problem" / generic praise:** Removed as generic or sycophantic. The retained strengths are concrete and evidence-based.
- **Harsh Critic claim that Proposition 4.1 "does not directly yield a tractable loss unless the CAMs are differentiable":** Under the paper's stated assumption of a linear classifier (Eq. 1), HiResCAMs are a weighted sum of feature maps (fully differentiable). This concern is addressed by the paper's architectural assumption.

## Novel Insights

Beyond the paper's own contributions, a noteworthy meta-point emerges from comparing the harsh critic and the strength finder: the harsh critic correctly identifies the gap between the theoretical non-uniqueness result (Theorem 3.2) and its practical demonstration, but underestimates the paper's primary empirical contribution — which is not about better explanations *per se*, but about using better explanations to *train better models*. The most impactful result (89-93% ContrastiveCAM IoU vs 30% baseline) remains impressive even if one sets aside the debate about whether HiResCAMs are "corrupted" in practice. The paper's contribution stands on the strength of CFCE as a training method, not solely on the critique of HiResCAMs.

## Suggestions

1. **Expand baseline comparisons.** Include at least 2-3 prior alignment methods (e.g., region masking, saliency regularization) on the same datasets to demonstrate that CFCE offers advantages over simpler alternatives.
2. **Test on at least one additional architecture** (e.g., DenseNet-121, ConvNeXt-T) to show the method is not specific to ResNet-50.
3. **Add a hyperparameter sensitivity study** for λ₁, λ₂, λ₃ — even a single ablation varying λ₁ over one order of magnitude would add confidence.
4. **Explicitly state in Section 4** that under the linear classifier assumption, HiResCAM reduces to a weighted sum of feature maps, making the loss fully differentiable.
5. **Add a brief discussion** of the accuracy-alignment trade-off observed in Table 2 and when practitioners should expect it to be acceptable.

## Score and Decision

### Calibration

**Round 1 — Bracketing (three bands):**
- *Weak anchors (avg < 3.5):* TextCAM (3.67), MI-Grad-CAM (3.00), Interpretability-Guided Alignment (2.50), Structure-based Interpretability (2.50) — all clearly reject quality.
- *Middle anchors (3.5-7.5):* ClusCAM (4.67), X-AIGD (5.00), MICLIP (4.50), TextCAM (3.67), Subset Selection Attribution Regularization (4.00), Shapley-based (5.00).
- *Strong anchors (>7.5):* Permutation-equivariant learning (8.00), Multimodal Meta-Reasoner (8.00), Rotation estimation (8.50), Text-to-3D (8.00) — about unrelated topics, not directly comparable.

**Initial bracket:** The paper sits clearly above all weak anchors and the mid-4.xx papers. It has stronger theory and empirical results than ClusCAM (4.67), MICLIP (4.50), and the Subset Selection Attribution Regularization paper (4.00). It is comparably novel to the 5.00 papers but with stronger empirical validation. Thus my initial bracket is (5.0, 7.0).

**Round 2 — Narrowing within bracket:**
- *Lower band anchors (3.5-6.0):* Subset Selection Attribution Regularization (4.00), Shapley-based Structured Explanations (5.00). The paper under review is *clearly stronger* than both: it has multiple theoretical theorems vs. their mostly empirical/heuristic designs, and larger-scale experiments.
- *Upper band anchors (6.0-8.0):* Distributional V-L Alignment (6.50), Low-Pass Filtering Behavioral Alignment (7.00), RecA Reconstruction Alignment (6.50), Tversky Neural Networks (7.00). These papers have broader experiments and/or more thorough analysis. The paper under review is *weaker* than these due to limited architecture testing, narrow baselines, and missing ablation/analysis.

**Final score:** After narrowing, the paper sits between the 5.0-level papers (where it's clearly stronger) and the 6.5-7.0 papers (where it falls short in evaluation breadth). **Score: 6.0** — a solid accept with meaningful contributions and fixable weaknesses.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>