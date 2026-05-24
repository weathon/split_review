## Summary

This paper identifies a redundancy in HiResCAMs: adding the same matrix \(M\) to every class's CAM leaves softmax probabilities unchanged (Theorem 3.2). It proposes **ContrastiveCAMs** (class-difference CAMs) that are invariant to this shift and provide granular class-versus-class explanations. Using the fact that ContrastiveCAMs directly relate to probabilities for bias-free linear classifiers (Proposition 4.1), the paper derives **Core-Focused Cross-Entropy (CFCE)**, a loss that penalizes contribution from non-core image regions, and a KL-regularized variant that encourages ContrastiveCAMs to match the shape of a core-region mask. Experiments on Hard-ImageNet, Oxford-IIIT Pets, and PASCAL VOC show that CFCE-trained models shift reliance toward core regions (accuracy under core ablation drops from ~76% to ~42%) and improve downstream segmentation performance.

## Strengths

- **Theoretical identification of HiResCAM redundancy and ContrastiveCAM fix**: Theorem 3.2 proves that HiResCAMs admit an unknown additive matrix \(M\) common to all classes, and Theorem 3.5 proves ContrastiveCAMs are invariant to this shift. This provides a principled justification for class-difference explanations, which prior CAM methods did not offer.

- **Correctness guarantee linking ContrastiveCAMs to predictions**: Proposition 4.1 shows that softmax probabilities can be expressed directly as a function of ContrastiveCAMs and the bias. This property is then leveraged to decompose cross-entropy into core and non-core contributions (Proposition 4.2) and derive the CFCE loss — a clean theoretical chain from interpretability to a training objective.

- **Compelling evidence from core-region ablation on Hard-ImageNet**: Table 2 shows that CFCE+KL reduces accuracy under Gray Mask ablation from 75.94% (CE) to 45.49%, and under Tile ablation from 67.38% to 39.47%. These metrics are not directly optimized by the loss and provide strong independent evidence that the model genuinely relies less on non-core regions.

- **Downstream segmentation improvements**: Figure 4 demonstrates that CFCE-KL-trained backbones improve per-class IoU on PASCAL VOC segmentation over CE-trained backbones, especially in end-to-end fine-tuning. This shows the method transfers to dense prediction tasks.

- **Practical robustness to imprecise masks**: Table 3 shows that SAM-generated masks and bounding boxes achieve competitive IoU compared to ground-truth masks (e.g., 85.26% vs. 92.72% in multiclass), indicating the method does not require expensive pixel-level annotations.

- **Consistency guarantee**: Theorem 4.6 proves that minimizing the CFCE risk converges to the Bayes-optimal core-constrained risk, providing theoretical validation for the loss design.

## Weaknesses

### Major

- **ContrastiveCAM IoU metric is circular for the primary claim**: The CFCE loss (Eq. 15) explicitly penalizes non-core ContrastiveCAM contributions, and the KL variant (Eq. 18) directly encourages ContrastiveCAMs to match the core mask shape. The high ContrastiveCAM IoU values (89–93% in Table 2) are therefore expected and do not constitute independent evidence of improved feature alignment. The paper reports these numbers more prominently than the independent metrics. This circularity is partially mitigated by: (a) the GradCAM IoU improvement (18.44% → 51.52%), which is based on a different explanation method not optimized by the loss, and (b) the core-region ablation results, which are convincing. The paper would be strengthened by de-emphasizing the ContrastiveCAM IoU and anchoring the alignment claim on the independent ablation metrics.

### Minor

- **Overstatement of the HiResCAM limitation**: The paper claims that HiResCAMs "fail to guarantee a faithful interpretation" (line 148) because "there are infinitely many possible logit outputs \(f\), hence infinitely many HiResCAMs" (line 128) for the same probability output. The mathematics (Theorem 3.2) is correct: the CAM→probability mapping is not injective. However, for any fixed trained model and fixed input, the HiResCAM is deterministically computed from the activations and gradients. The "non-uniqueness" is a property of the mathematical relationship between CAMs and probabilities, not an ambiguity in what the model actually computes. The paper's valuable insight is that HiResCAMs are affected by a class-common redundancy that ContrastiveCAM removes; this framing would be more precise than claiming HiResCAMs are "unfaithful."

- **No hyperparameter sensitivity analysis**: The loss (Eq. 18) introduces three hyperparameters (\(\lambda_1, \lambda_2, \lambda_3\)), but the paper does not state their values or provide any sensitivity ablation. This makes it difficult to assess how robust the method is to these choices and hinders reproducibility.

- **Linear classifier assumption**: The analysis and loss are derived under the assumption that the classifier is a single linear layer \(h(\mathbf{z}) = W\mathbf{z} + \mathbf{b}\) (Eq. 1). While this covers ResNet, ConvNeXt, EfficientNet, and DenseNet backbones, it does not apply to architectures with MLP heads. The paper should discuss this scope limitation.

- **Optimization procedure for CAM-dependent gradients is not clarified**: The loss involves ContrastiveCAMs that depend on the classifier weights (for a linear classifier, CAM\(_c^{\text{HiRes}} = W_c \odot \mathbf{A}\)). The gradient of the loss w.r.t. weights thus involves second-order terms since the weight appears both as a multiplier and inside the CAM computation. The paper does not explain whether gradients are stopped through the CAM computation or handled differently.

### Trivial

- None beyond presentation issues that are likely parser artifacts.

## Nice-to-Haves

- An ablation study of \(\lambda_1, \lambda_2, \lambda_3\) with sensitivity curves.
- Ablation of whether stopping gradients through the CAM computation affects results.
- A comparison to a simple baseline where non-core regions are masked in the input or feature space during standard CE training, to isolate the effect of the proposed loss from simply discarding non-core information.
- Insertion-deletion faithfulness curves using the core mask as the "important" region, as additional independent validation.

## Removed Points

These points are flagged to be removed — treat them with caution:

- **Missing baseline comparisons (Ismail et al., 2021; L2-regularization on attention maps)**: Removed as this asks for specific baselines not established as standard and constitutes scope creep. The paper already compares against CORM and DFR.
- **Missing related work**: Removed per policy (reviewer cannot verify existence of missing references).
- **Reproducibility concerns about missing appendix content (e.g., number of epochs, learning rates)**: Removed — these are stripped appendix artifacts, not missing from the original submission.
- **Computational overhead criticism**: Removed — the paper is a methods paper, not a systems paper, and incremental overhead is acceptable for training-time regularization.
- **"Reductive metrics inevitably present a partial view" (Discussion section)**: This is a generic closing remark, not a meaningful weakness to retain.
- **Strength Finder's generic strengths** (e.g., "addressed an important problem," "targeted an interesting question"): Removed as superficial. Only strengths with specific, concrete content are retained.

## Novel Insights

None beyond the paper's own contributions. The harsh critic's observation about the contrast between the overclaimed theoretical motivation and the practical value of ContrastiveCAMs is useful framing guidance but not a novel scientific insight.

## Suggestions

1. **Reframe the motivation for ContrastiveCAMs**: Replace "HiResCAMs fail to guarantee faithful interpretation" with "HiResCAMs contain a class-common redundancy that ContrastiveCAM removes, providing invariant class-difference explanations." This is more precise and avoids overclaiming.
2. **Anchoring**: Present the core-region ablation results (Gray Mask, Gray BBOX, Tile) as the primary evidence for feature alignment, and demote ContrastiveCAM IoU to a sanity-check metric.
3. **Add a hyperparameter sensitivity plot** for \(\lambda_1, \lambda_2, \lambda_3\) and state their values explicitly.
4. **Clarify the gradient flow**: Explain whether gradients are stopped through the CAM computation during training or handled differently.
5. **Discuss the linear classifier assumption** and how the method could be extended to deeper classifiers.

## Score and Decision

### Calibration

**Round 1 — Bracketing** (query: "feature alignment in convolutional neural networks using interpretability or CAM explanations"):

| Anchor | Score | Round | Comparison |
|--------|-------|-------|------------|
| TextCAM (ScXx64OWus) | 3.67 | R1 | Weaker — primarily empirical, limited theory, no training-time contribution |
| MI-Grad-CAM (C5Dgtmk7ho) | 3.00 | R1 | Weaker — post-hoc only, no training component |
| Activation-Deactivation (Pf6Vbl4r9k) | 3.33 | R1 | Weaker — post-hoc explanation only |
| ClusCAM (MYGtEADPUs) | 4.67 | R1 | Weaker — empirical clustering approach with limited theoretical grounding |
| MICLIP (28Hfz8RLcD) | 4.50 | R1 | Comparable — both have theoretical and empirical contributions, but this paper has cleaner evaluation |
| Latent Feature Alignment (utObNTrbSb) | 4.50 | R1 | Different domain (face recognition bias) — not directly comparable |

**Round 1 bracket**: 3.5–7.5

**Round 2 — Narrowing** (queries for CAM methods with theoretical analysis, and interpretability-guided training):

| Anchor | Score | Round | Comparison |
|--------|-------|-------|------------|
| HiCEM (h61OIERd38) | 6.00 | R2 | Similar quality — both have theory + experiments; HiCEM has user study but concept leakage concerns |
| Low-Pass Filtering (YhgBy6jTR8) | 7.00 | R2 | Stronger — cleaner narrative, more surprising findings, extensive experiments |
| Probing Human Robustness (uhVlvT3Pk1) | 5.60 | R2 | Different domain but similar tier |
| Cross-Arch Distillation (OOiKGlYtQZ) | 5.50 | R2 | Different domain, similar tier |

**Initial bracket**: 3.5–7.5. **Narrowed bracket**: 4.5–6.5. The paper is clearly stronger than TextCAM (3.67) and ClusCAM (4.67) due to its theoretical contributions and broader evaluation. It is weaker than Low-Pass Filtering (7.00) due to the overstated motivation and metric circularity. Compared to HiCEM (6.00), the paper has similar weakness severity (circularity vs. concept leakage) but slightly less polished presentation. **Final score: 5.5**.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Accept</decision>