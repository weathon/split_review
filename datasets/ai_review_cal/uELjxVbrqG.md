- Decision: Accept
- Avg Score: 7.00
- Scores: 8, 6, 6, 8
Now I have all the information needed. Let me construct the final consolidated review.

---

## Summary

This paper studies face recognition (FR) feature spaces through two lenses. First, it decomposes a superior model's feature vector into components parallel and orthogonal to an inferior model's features, discovering that the orthogonal component ("innovation") retains discriminative power — in some cases outperforming the inferior model itself. Second, motivated by this, the paper proposes an **Intra-class Incoherence Constraint (IIC)**: when fine-tuning a student network (same architecture as the teacher) on the same data, a cosine-similarity *dissimilarity* loss is added to push the student's features away from the teacher's. Experiments across multiple backbones (ResNet50/100), training sets (CASIA, MS1MV2), and benchmarks (LFW, CFP-FP, AgeDB, IJB-C, etc.) show consistent but modest improvements over ArcFace, CosFace, MagFace, and AdaFace baselines.

---

## Strengths

1. **Empirical discovery that the "innovation" component of a superior model (orthogonal to an inferior model's features) retains discriminative power.** Table 1 shows that the innovation component extracted from ArcFace by orthogonal decomposition against CosFace achieves 96.05% on LFW and 81.68% on CFP-FP — outperforming the full CosFace model (95.86% and 78.32%, respectively). This is a genuine and non-obvious finding about FR feature spaces.

2. **Consistent improvements across diverse SOTA FR methods, datasets, and backbones.** Tables 3–5 show IIC improving ArcFace, CosFace, MagFace, and AdaFace on seven benchmarks spanning both small-scale (CASIA→LFW) and large-scale (MS1MV2→IJB-C) settings, with ResNet50 and ResNet100 backbones. The consistency across this breadth is the paper's strongest empirical asset — the improvement is not an isolated fluke.

3. **Thorough ablation studies that illuminate design choices.** Section 4.3 systematically examines: the IIC weight γ (robust across 0.5–2.0, Table 6), teacher vs. random initialization (teacher wins), per-layer vs. all-layer application (all-layers degrades performance), and the "feature augmentation" hypothesis via training on 1/10 of MS1MV2 (larger relative gains on smaller data). This analysis helps practitioners adapt the method and confirms the gains come from the IIC constraint, not merely re-training.

4. **Practical simplicity.** The method requires no architectural changes, no additional data, and no modifications to the training pipeline beyond adding a cosine-similarity dissimilarity term. It works by fine-tuning any existing pre-trained FR model with the same architecture for the student.

---

## Weaknesses

### Fatal
None.

### Major

1. **The connection between the two-model decomposition and the single-model IIC method is an analogy, not a derivation.** The core geometric motivation (Section 3.1, Fig. 1a) revolves around orthogonality to an *inferior* model's features. In the single-model IIC setting (Fig. 1b), there is no inferior model. The teacher serves dually as the reference and as the "inferior" by analogy, but the paper provides no argument that minimizing cosine similarity between teacher and student features is equivalent to recovering the innovation component defined relative to a worse model. The loss function simply pushes features apart — this is a generic dissimilarity constraint. The paper's own language reveals this gap (lines 86–87: "a more practical scenario where only a single model is available... but its improved model and innovation are unknown"). The narrative would be significantly stronger if recentered: present the decomposition as an *inspiring observation*, and IIC as a *practical regularizer* that happens to work, rather than claiming IIC recovers the same "innovation" from the decomposition analysis.

2. **IIC's improvement may stem from a generic regularization effect, and this alternative explanation is not ruled out.** The paper explicitly hypothesizes that IIC acts as "feature augmentation" (line 167) and acknowledges that training on the same data without IIC leads to overfitting (line 177). The larger relative gains on smaller data (1/10 of MS1MV2) are consistent with a regularization story. However, the paper does not compare IIC against standard fine-tuning regularizers such as: (a) increased weight decay beyond the default 0.0001, (b) increased dropout beyond 0.4, (c) adding Gaussian noise to features, or (d) standard data augmentation. Without these controls, the claimed mechanism ("learning innovation" vs. "preventing overfitting") remains ambiguous. Comparing against at least one or two of these baselines would substantially strengthen the paper.

### Minor

1. **No statistical significance or variance reporting.** All results are reported as single numbers. Given that many improvements on large-scale benchmarks are fractions of a percent (e.g., ArcFace on LFW: 99.83→99.85, Table 4), confidence intervals or results from multiple runs are needed to confirm these improvements are not due to random variation.

2. **No evaluation on out-of-domain or cross-dataset generalization.** All test benchmarks are similar in domain to the training data. Evaluating on a genuinely different domain (e.g., IJB-S, TinyFace, or a cross-quality benchmark) would help establish whether IIC learns genuinely better representations or merely better separates the training distribution.

3. **The claim that IIC-learned features contain "innovation" with discriminative power is not rigorously validated.** The paper verifies (line 181–182) that features from IIC-trained models have an orthogonal component with some discriminative ability. But this is expected for essentially any feature perturbation — a properly controlled comparison would demonstrate that this orthogonal component is specifically correlated with the "innovation" predicted by the two-model decomposition, rather than being a generic byproduct of altering the feature space.

### Trivial
None.

---

## Nice-to-Haves

- Compare IIC against a few standard regularizers (larger weight decay, feature noise, stronger augmentation) to disentangle regularization from "innovation" effects. Even if the results show IIC is "just a regularizer," that is itself a useful finding.
- Report results averaged over 2–3 runs with standard deviations for the key comparisons in Tables 3–4.
- Include a cross-dataset evaluation to test whether IIC features transfer better to out-of-domain settings.

---

## Removed Points

These points were flagged during review but are removed because they are factually incorrect, already addressed in the paper, or misread the content:

- **"Equation (1) has a typo: denominator should be ||b||², not ||b|| ||b||."** — Removed. The expression `||b||·||b||` is mathematically equivalent to `||b||²`. This is a notational choice, not an error.
- **"The paper does not specify whether the student is trained on the same training set as the teacher."** — Removed. The paper explicitly states on line 177 "the data are reused and the model training may be overfitting," confirming the same training data.
- **"The comparison with SOTA methods is misleading because the baseline numbers are from original papers but the IIC student is trained with additional epochs."** — Removed. The paper includes a proper control: the FR-only ablation in Table 7, where the same student is trained for the same number of epochs without IIC and *declines* in performance. This control addresses the fairness concern.
- **"The IIC method does not control the modulus of innovation."** — Removed. This was offered as a criticism of the conceptual framing, but IIC was never claimed to control the modulus; it targets the direction. The paper's own framing acknowledges this implicitly.
- **Several of the strength finder's generic claims** (e.g., "the paper addresses an important problem") — Removed. They are superficial and lack specific evidence.
- **The strength finder's specific IJB-C numbers (ArcFace 55.16%→73.21% at FPR=1e-6)** — Cautioned. These cannot be verified from the text (the table is an image), and the harsh critic reports different numbers (4.70→12.86) for the same setting. Since neither can be confirmed from the available text, neither set is used as evidence.

---

## Novel Insights

The reviews surface a recurring tension that the paper's own authors seem aware of but do not fully resolve: the gap between a clean geometric story (orthogonal decomposition in the two-model case) and the practical method (a generic dissimilarity regularizer). The harsh critic's most useful observation is that the "innovation" narrative may be a post-hoc rationalization of what is essentially a fine-tuning regularizer that prevents overfitting when re-training on the same data. The strength finder correctly identifies that the paper's strongest asset is its *breadth and consistency* of improvement — IIC works across many baselines and settings, even if the mechanism is unclear. Neither reviewer disputes the empirical observation that innovation (as defined in the two-model case) has discriminative power; the disagreement is entirely about whether IIC recovers it. This suggests the paper's most honest contribution is twofold: (a) an interesting empirical discovery about FR feature geometry, and (b) a simple, practical fine-tuning technique whose mechanism warrants further study. The paper would benefit from reframing to match what it actually demonstrates.

---

## Suggestions

1. **Recenter the narrative.** Present the decomposition analysis in Section 3.1 as a *motivating observation* about feature spaces, and IIC as a *practical regularizer* inspired by that observation. Drop the stronger claim that IIC "recovers innovation" as defined in the two-model setting, since this is not supported by the evidence.
2. **Add at least one baseline comparison with a standard regularizer** (e.g., train the student with increased weight decay or feature噪声 without IIC, to show IIC provides benefits beyond generic regularization).
3. **Report variance** for key results where improvements are marginal (≤0.2% on saturated benchmarks like LFW).
4. **Consider evaluating on a cross-domain benchmark** (e.g., IJB-S or TinyFace) to test whether IIC features generalize better.

---
