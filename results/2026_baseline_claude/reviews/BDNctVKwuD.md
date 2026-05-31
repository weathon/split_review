## Summary

This paper makes two connected contributions. First, it identifies a theoretical limitation of HiResCAMs: the class-level attention maps are non-unique — they admit an arbitrary additive shift by a common matrix $M$ across all classes while producing identical softmax predictions. This follows directly from the translation-invariance of softmax. The authors propose **ContrastiveCAMs** (pairwise differences of HiResCAMs) as an invariant fix. Second, leveraging the clean connection between ContrastiveCAMs and cross-entropy, the authors propose **Core-Focused Cross-Entropy (CFCE)**, a loss function that penalizes contributions from non-core image regions by taking their absolute values (thereby always increasing the loss), while preserving the standard cross-entropy behavior over core regions. Experiments on Hard-ImageNet, Oxford-IIIT Pets, and PASCAL VOC show substantial improvements in IoU alignment and robustness to core-region ablation.

---

## Strengths

- **Theoretically grounded limitation of HiResCAMs.** Theorem 3.2 is a clean, non-obvious result: the shift invariance of softmax propagates to an additive matrix ambiguity in HiResCAMs, not just a scalar, because each class-level CAM sums to a scalar logit. The proof structure is correct, and γ values in Table 1 (e.g., 0.367 for Pets) show the redundancy is empirically non-negligible.

- **Clean derivation of CFCE from ContrastiveCAMs.** Proposition 4.2 dissociates cross-entropy into core and non-core contributions (for a bias-free linear head) in a mathematically tight way. CFCE (Definition 4.5) follows directly: flip the sign treatment of the non-core summand to turn it from a potential helper into a penalty. Theorem 4.6 provides classification-calibration consistency, grounding the heuristic as a proper surrogate loss.

- **Dramatic feature alignment improvements on Hard-ImageNet.** Accuracy under core-region ablation drops from 76%/69%/67% (CE) to 42%/32%/34% (CFCE), indicating the model now relies far less on non-core regions. RFS improves from −0.18 to +0.22–+0.24. GradCAM IoU improves from 18.44% to 51.52% (CFCE+KL). These are not marginal gains.

- **Practical robustness to imperfect masks.** The paper demonstrates that CFCE remains competitive with approximate supervision (SAM auto-generated masks, bounding boxes), making the method usable without pixel-perfect annotations, which is an important practical contribution.

- **Downstream segmentation improvements.** Core-focused backbone initializations improve IoU on PASCAL VOC segmentation across nearly all 20 classes (both fine-tuned and end-to-end), providing evidence that alignment benefits generalize beyond the training task.

---

## Weaknesses

### Fatal
None.

### Major

1. **Accuracy cost is not contextualized.** On Hard-ImageNet, CFCE drops accuracy from 94.25% (CE) to 90.53% — a 3.7-point gap. CORM achieves 92.91% with more modest alignment gains. The paper does not analyze whether this accuracy drop is unavoidable, how sensitive it is to the mask quality/resolution, or whether any regularization weight trade-off can recover some accuracy while preserving alignment. Without this, practitioners cannot calibrate the cost-benefit trade-off.

2. **Baseline coverage is asymmetric across datasets.** CORM and DFR are compared only on Hard-ImageNet. Tables 3 and 4 (Pets, PASCAL VOC) compare only against vanilla cross-entropy variants. Since CORM and DFR are methods specifically designed for feature alignment, their absence in the other tables makes it harder to assess whether CFCE is uniformly superior or benefits from dataset-specific properties of Hard-ImageNet.

3. **Hyperparameters of regularized CFCE are underspecified.** The divergence regularizer (Definition 4.7) introduces three hyperparameters (λ₁, λ₂, λ₃). CFCE+KL outperforms plain CFCE in some metrics (e.g., GradCAM IoU: 18.88% → 51.52%) but not others (e.g., Hard-ImageNet accuracy under Gray-Mask ablation: 41.78% → 45.49%). Sensitivity analysis or ablation over these parameters is absent, making it unclear how much engineering is needed to replicate the results.

### Minor

1. **Bias-zeroing assumption.** Setting $\mathbf{b} = \mathbf{0}$ in the classifier is necessary for the tight connection between ContrastiveCAMs and cross-entropy. The paper discusses this briefly, but does not empirically evaluate whether zeroing the bias meaningfully harms capacity or whether training recovers this through the backbone biases.

2. **Computational cost of ContrastiveCAMs.** For large $C$, computing all $C(C-1)$ pairwise ContrastiveCAMs per sample during training is expensive. The paper does not discuss training overhead versus CE baseline.

### Trivial

- Proposition 3.1 (softmax translation invariance) is presented as a theorem-style result, but it is standard knowledge; the novel contribution is its amplification to matrix-level CAM ambiguity in Theorem 3.2.

---

## Nice-to-Haves

- An ablation decomposing the effect of bias-zeroing, the CFCE penalty on non-core regions, and the KL divergence regularization individually would clarify which component drives the gains.
- A wall-clock training time comparison against CE to characterize the computational overhead of computing ContrastiveCAMs during the forward pass.
- A small experiment on a transformer-based backbone (e.g., ViT) with single-layer head to probe whether the theoretical results and empirical alignment gains extend beyond ResNet.

---

## Novel Insights

The central novel insight is that softmax's translation invariance — usually treated as a minor technical nuisance for logit calibration — has a tangible, computable impact on *post-hoc explanations*: it introduces a spatial matrix-valued ambiguity into every HiResCAM that can, in principle, completely misattribute spatial contributions. Taking pairwise differences cancels this shared ambiguity and simultaneously yields class-versus-class explanations that are better aligned with the training objective (which optimizes logit *differences*, not individual logits). The subsequent leap from this invariance property to a trainable loss function — where the same algebra that defines ContrastiveCAMs lets one algebraically separate core and non-core contributions inside cross-entropy — is technically clean and constitutes a tight, self-consistent conceptual chain from interpretability theory to loss design.

---

## Suggestions

- Include a sensitivity curve showing accuracy vs. IoU as mask resolution degrades or λ₁ is varied, to help practitioners tune the alignment-accuracy trade-off.
- Consider reporting ContrastiveCAM IoU for the CE baseline (not just CE w/ Arch) to make Table 2's comparison internally consistent.
- An explicit comparison to prior contrastive/class-discriminative CAM variants (e.g., Score-CAM, Grad-CAM++) in a focused ablation table would help readers understand exactly what the M-invariance property adds beyond simpler baselines.

---

## Score and Decision

The paper presents a clean theoretical insight, derives a practical loss function from it with a consistency guarantee, and demonstrates convincing improvements in feature alignment across three datasets and multiple evaluation protocols. The accuracy cost is real but disclosed, and the approach works with imperfect supervision. The major weaknesses — uneven baseline coverage and underspecified hyperparameters — weaken confidence in the full scope of the contribution but do not undermine the core claims.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>