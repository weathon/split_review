Here is my consolidated final review:

---

## Summary

This paper analyzes face recognition features through orthogonal decomposition: given a superior model (ArcFace) and an inferior one (CosFace), the "innovation" sub-feature (orthogonal to the inferior model's features) retains strong discriminative power, and recombining it with adjusted modulus can outperform the original superior model. Motivated by this geometric analysis, the paper proposes an Intra-class Incoherence Constraint (IIC) within a knowledge-distillation framework: a student network (same architecture as the teacher) is trained to both recognize faces and minimize cosine similarity with the teacher's embeddings of the same identity. Experiments show consistent improvements over ArcFace, CosFace, MagFace, and AdaFace on standard benchmarks, with notable gains on IJB-C at low false-positive rates.

---

## Strengths

1. **Novel discovery that the orthogonal "innovation" component retains discriminative power (Table 1).** The paper shows that the sub-feature of ArcFace orthogonal to CosFace's feature space achieves higher accuracy than CosFace itself on several benchmarks. This is a genuine insight about feature geometry in FR.

2. **Demonstration that modulus-adjusted recombination of innovation and pro-feature can surpass the original model (Table 2).** With coefficient c=2, the synthesized feature outperforms the original ArcFace on multiple benchmarks (e.g., CPLFW 78.45% → 79.13%), providing the motivation for the IIC approach.

3. **Consistent improvements across multiple SOTA methods and architectures (Tables 3, 4).** Adding IIC improves ArcFace, CosFace, MagFace, and AdaFace across seven benchmarks with ResNet50 on CASIA, and extends to ResNet100 on MS1MV2. The gains are systematic, not cherry-picked.

4. **Substantial gains at low FPR on IJB-C (Table 5).** At FPR=1e-6, ArcFace+IIC improves TAR from 80.64% to 85.23%, and AdaFace+IIC from 84.87% to 86.71%. This is practically relevant for high-security applications.

5. **Ablation isolating IIC as the source of improvement (Table 7).** Initializing the student with teacher weights but training without IIC yields no improvement or slight decline, confirming that IIC — not re-initialization or extra epochs — drives the gains.

6. **Exploration of applying IIC at multiple network stages.** The paper tests constraints at different block outputs and shows single-layer application is sufficient, providing practical guidance.

---

## Weaknesses

### Fatal
None.

### Major

1. **Loose connection between the geometric motivation and the actual IIC method.** The paper's central analysis (Sec. 3.1) decomposes features into orthogonal "innovation" and parallel "pro-feature" components and motivates IIC as a way to learn innovation. However, IIC simply minimizes cosine similarity between teacher and student embeddings of the same image — a soft dissimilarity constraint, not an orthogonality constraint. The student could satisfy this by rotating or scaling features without learning anything structurally analogous to the orthogonal innovation from the analysis. The paper does not validate that IIC actually learns features with an orthogonal innovation component: while Sec. 4.3 mentions performing orthogonal decomposition on IIC-learned features, **it provides no quantitative accuracy numbers from that decomposition** — only a vague statement that "it shows the learned innovation does have certain facial feature representation abilities" (line 181). The geometric analysis is interesting on its own but the method is not demonstrably connected to it.

2. **Missing comparison against simpler regularization baselines.** The IIC loss is a cosine dissimilarity term added to a standard FR loss. The paper does not compare against straightforward alternatives such as adding Gaussian noise to features, feature decorrelation losses (e.g., Barlow Twins-style redundancy reduction), or explicit feature perturbation during training. The paper itself speculates that IIC acts as "feature augmentation" (Sec. 4.2) but does not test this by comparing against explicit data augmentation. Without these baselines, it is unclear whether the improvement comes from the specific dissimilarity constraint or from any additional regularization that prevents overfitting to the teacher's distribution (especially since the student is initialized with teacher weights and trained on the same data). The existing baselines do use dropout (p=0.4, line 139), but comparisons against other distinct regularization strategies are needed to establish IIC's unique contribution.

### Minor

1. **Modest absolute gains on near-saturated benchmarks.** On LFW (99.8%+), improvements are 0.1–0.3%. While the IJB-C gains at low FPR are substantive, the narrative leans heavily on improvements that are, on many standard benchmarks, very small. No confidence intervals or multi-run statistics are reported, so the variability of these gains is unknown.

2. **No analysis of why multi-layer IIC degrades performance.** The paper notes that applying IIC to all layers simultaneously worsens accuracy, offering only a brief speculation ("too many restrictions would affect recognition," line 179) without experimental exploration (e.g., varying γ across layers). A deeper investigation of this trade-off would strengthen the paper.

### Trivial
None.

---

## Nice-to-Haves

- Report IJB-C results across multiple random seeds or at least include confidence intervals to establish statistical significance of the gains.
- Discuss the computational cost: using a teacher and student of identical size roughly doubles training memory and compute relative to standard FR training.
- Extend the analysis of multi-layer IIC with a small experiment varying γ across layers.

---

## Removed Points

- **Criticism about missing related work on feature decorrelation methods (Barlow Twins, redundancy reduction):** Removed per policy — do not cite external missing references that cannot be verified as relevant from the paper text alone.
- **Formatting/style complaints about tables being image references and the garbled footnote about IoT devices in Fig. 1(a):** These are PDF extraction artifacts, not author errors.
- **Claim that "the paper does not provide numerical values in the text for key results":** Tables are legible in the original submission; the parser strips them to images. This is a known artifact.
- **Suggestion to compare against "training from scratch with more epochs or different initialization":** Already addressed by Table 7, which shows training without IIC (with teacher initialization) does not improve performance.
- **Suggestion to compare against dropout baseline:** The paper already uses dropout (p=0.4) in the baseline model (line 139), so this comparison is partially embedded in the existing setup.
- **Criticism that the method "reduces to a minor engineering modification" without acknowledging the geometric analysis contribution:** The paper has two distinct contributions (the innovation analysis and the IIC method); dismissing both is an overstatement.

---

## Novel Insights

None beyond the paper's own contributions. The reviewers' comments do not surface an insight about the work that the paper itself does not already state.

---

## Suggestions

1. **Bridge the motivation-method gap.** Either (a) modify IIC to more directly enforce an orthogonal relationship (e.g., project the student feature onto the teacher-orthogonal subspace), or (b) provide post-hoc quantitative evidence that IIC-learned features contain an orthogonal innovation component — specifically, decompose the trained student's features using the teacher's features as the reference direction and report the innovation-only accuracy, analogous to Table 1. This single addition would substantially strengthen the paper's narrative.

2. **Add two key baselines:** (a) training with feature-level Gaussian noise as a regularization control, and (b) training with a feature decorrelation loss (e.g., minimizing batch-level feature covariance). If IIC matches or surpasses these, its specific design is validated; if not, the paper's claim of a distinct mechanism is undermined and should be reframed.

3. **Report IJB-C results with at least 2–3 runs** to demonstrate that the low-FPR gains are statistically robust.

---

## Score and Decision

This paper makes two contributions: a genuinely interesting geometric analysis of FR feature spaces (innovation retains discriminative power) and an empirically effective training procedure (IIC) that improves multiple SOTA methods. The experiments are solid and the improvements are consistent. However, the two contributions are loosely coupled — the method does not demonstrably realize the geometric mechanism that motivates it — and the paper lacks critical baselines that would establish what IIC uniquely adds over generic regularization. The geometric analysis is publishable as an insightful finding, but the IIC method as presented is insufficiently differentiated from simpler alternatives. For a top venue, these gaps are material.

**MY FINAL SCORE:** <pineapple>5.0</pineapple>
**MY FINAL DECISION:** <orange>Reject</orange>