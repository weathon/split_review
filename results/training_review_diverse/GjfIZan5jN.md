Now I have all the information needed. Let me produce the final consolidated review.

## Summary

This paper proposes the Inherent Interpretability Score (IIS), a metric that quantifies a pre-trained representation's interpretability by measuring how well task-relevant semantics survive when the representation is projected into a sparse concept space. Using IIS, the authors empirically investigate the relationship between interpretability and classifiability across diverse models, datasets, and concept libraries, discovering a **positive correlation** — representations with higher classification accuracy tend to preserve more semantic information in their concept-based interpretations. The paper then demonstrates two applications: (1) fine-tuning with an IIS-maximization term can (modestly) improve classification accuracy, and (2) higher-accuracy pre-trained representations yield more faithful interpretable predictions.

---

## Strengths

1. **Novel, principled interpretability metric (IIS)**. The IIS is well-motivated: it operationalizes interpretability as the ability of a representation to retain accuracy when predictions are made solely through sparse concept-based interpretations. By integrating over sparsity levels (area under the sparsity-ARR curve), it avoids dependence on a single, arbitrary sparsity threshold. This provides a task-agnostic way to compare interpretability across models.

2. **Consistent empirical evidence for a positive correlation between interpretability and classifiability**. Figures 3 and 4 show a clear, visually consistent positive trend across **four distinct concept libraries** (Prototype, Cluster, End2End, Text) and **four datasets** (ImageNet, CUB-200, CIFAR-10, CIFAR-100). The trend holds both across models of different sizes within the same architecture family (dotted lines linking ViT-B → ViT-L, etc.) and across architectures. This directly challenges the conventional belief in an inherent interpretability-classifiability trade-off (Mori & Uchihira, 2019; Zarlenga et al., 2022) — at least for *classifiability-oriented* pre-trained representations.

3. **Robust validation across diverse settings**. The paper uses both visual concept libraries (Prototype, Cluster, End2End) and a textual library (GPT-3 + CLIP), experiments span coarse-grained (CIFAR) to fine-grained (CUB-200) classification, and includes models from multiple architecture families (ResNet, ViT, ConvNeXt, Swin). This breadth reduces the concern that the observed correlation is an artifact of a single interpretation methodology.

4. **Factor-level decomposition (sparsity and ARR)**. By disentangling IIS into sparsity and ARR, Section 3.3 provides mechanistic insight into why better classifiability yields higher IIS: higher-accuracy representations exhibit higher ARR across all sparsity levels (Figure 7), meaning sparser concepts suffice to retain task-relevant semantics. This strengthens the causal narrative underlying the correlation.

---

## Weaknesses

### Fatal
None.

### Major

1. **Missing control baseline for the fine-tuning experiment (Section 4.1, Table 1).** The paper fine-tunes pre-trained models with a combined objective (cross-entropy + IIS maximization) and reports small accuracy gains (e.g., ResNet-50: 78.50% → 78.58%; ConvNeXt-T: 81.14% → 81.23%). The comparison is against the *frozen* pre-trained accuracy (linear probe). **There is no control condition where the same model is fine-tuned for the same number of epochs using *only* the cross-entropy loss (the first term of Equation 8).** Without this baseline, the improvement cannot be attributed to the IIS term — it could equally come from simply updating the backbone via fine-tuning, or from the auxiliary linear head acting as a regularizer. The tiny magnitude of the gains and the absence of error bars / multiple seeds further weaken the causal claim. This does **not** invalidate the paper's core discovery (the positive correlation), but it undermines the application claim that "improving interpretability can further promote classifiability."

2. **No statistical quantification of the claimed correlation (Section 3.2, Figures 3, 4).** The paper states that "a positive correlation between classifiability and interpretability can be observed" but reports no correlation coefficients (Spearman's ρ, Pearson's r) or significance tests. The figures show 5–8 models per plot with trend lines, and while the visual pattern is compelling, the lack of formal quantification is a gap for an empirical claim that is central to the paper. This is especially relevant because the relationship is not strictly monotonic across all architectures (the paper itself notes architecture-dependent variations, e.g., ViT-B vs. Swin-T).

### Minor

1. **Early training dynamics (Figure 5) are non-monotonic and deserve fuller discussion.** The paper notes that IIS is high at epoch 0 (because both interpretations and original representations have low accuracy), drops around epoch 10, then rises. The paper acknowledges this as a ratio artifact but dismisses it too quickly ("This phenomenon does not affect the application of IIS"). The non-monotonic behavior means the positive correlation claim is restricted to later training stages / sufficiently accurate models. Explicitly discussing a minimum accuracy threshold for the correlation to hold would strengthen the analysis.

2. **The comparison in Section 4.2 (Tables 4, 5) against interpretability-oriented methods is informative but incomplete.** The paper compares its interpretable predictions (linear probe on concept-projected *pre-trained* features) against methods like ECBM that train entire models from scratch with interpretability constraints. This comparison supports a practical claim ("you get better accuracy by starting from pre-trained features"), which is valid. However, the paper would benefit from also comparing against post-hoc concept-based methods (e.g., a Concept Bottleneck Model) applied to the *same frozen pre-trained features* to isolate whether the accuracy advantage is specifically due to the classifiability–interpretability synergy or simply the strength of the pre-trained backbone. Several cited interpretability-oriented methods may also permit pre-trained initializations, so clarifying this would improve rigor.

3. **No error bars or multiple-run statistics on any quantitative result.** All tables (1, 2, 3, 4, 5) report single numbers without standard deviations or confidence intervals. For the fine-tuning results in particular (where gains are tiny), this makes it impossible to assess whether the improvements are statistically significant.

### Trivial

- The ARR ratio artifact at very low accuracy (where both numerator and denominator are small) is acknowledged but could benefit from a brief explicit caveat in the metric definition section.
- The paper does not discuss the computational cost of computing IIS (which requires training a linear classifier per sparsity ratio), though this is a minor omission for an empirical study.

---

## Nice-to-Haves

- A control experiment for the fine-tuning: fine-tune with cross-entropy only for the same epochs, then compare.
- Reporting Spearman's ρ and p-values for Figures 3 and 4.
- Including a post-hoc concept bottleneck baseline on the same frozen features for Section 4.2.
- Reporting means and standard deviations over 3+ seeds for the main tables.
- A brief discussion of minimum accuracy thresholds for the IIS correlation to hold robustly.

---

## Removed Points

The following points from the raw reviews are removed or downgraded with justification:

- **"Unfair comparison in Section 4.2 — apples-to-oranges"** (Harsh Critic, Critical Issue #2). This criticism is **overstated**. The paper's comparison between interpretable predictions derived from pre-trained features and interpretability-oriented methods trained from scratch is a *practical* comparison: the claim is that using pre-trained classifiability-oriented representations yields better interpretable predictions than training an interpretable model from scratch. This is a legitimate evaluation of a real practical choice. The paper explicitly notes that "we only take the classification head as the trainable module, in contrast to interpretability-oriented methods training the entire model," highlighting an efficiency advantage. Calling this "unfair" mischaracterizes the comparison; it has been downgraded to Minor (point 2) with a suggestion for an additional baseline rather than retained as a structural flaw. The original criticism's severity is not supported.

- **"Should also cover domain Y / additional tasks"** — generic scope-creep demands not applicable to the paper's stated scope.

- **"The paper should also include X"** demands for unrelated tasks/methods that would change the paper's nature.

- Generic strength finder items that were superficial or redundant (e.g., "this paper addressed an important problem") have been filtered out. Only concrete, evidence-backed strengths are retained.

- Questions about code/model release status or existence of cited references are removed per policy — all cited entities are assumed to exist.

---

## Novel Insights

The most interesting observation to emerge across the reviews — beyond the paper's own contributions — is that the IIS metric itself could serve as a *diagnostic tool* for model architecture design: since the correlation is positive but not strictly monotonic across architectures (ViT-B vs. Swin-T with similar accuracy have different IIS), the metric may capture aspects of representation structure that accuracy alone does not. This suggests IIS could be used to evaluate architectural choices, not just pre-training quality, though the paper only hints at this direction (last sentence of Section 3.2). A second insight from the cross-examination is that the fine-tuning experiment (Section 4.1) is the weakest link in the paper's chain of evidence, yet it is also the least central to the paper's main empirical finding — the positive correlation stands on the evidence of Figures 3–5 independent of whether the fine-tuning claim holds.

---

## Suggestions

1. **Add the missing control to Section 4.1.** Fine-tune each model with only the cross-entropy loss (Equation 8, first term) for the same number of epochs, report mean and std over 3 seeds. If the IIS-term models still outperform, the causal claim would be well-supported. If not, reframe the claim as a suggestive observation.

2. **Quantify the correlation statistically.** Report Spearman's ρ for each dataset×concept-library combination in Figures 3 and 4, and consider showing the relationship after filtering low-accuracy models (< e.g., 20%) to address the ratio artifact.

3. **Add a post-hoc concept bottleneck baseline to Section 4.2** that uses the same frozen pre-trained features and concept library — this would cleanly isolate whether the advantage comes from the classifiability→interpretability relationship or simply from using a stronger backbone.

4. **Include error bars** for at least the main quantitative results (Tables 1, 4, 5) over multiple runs.

---

## Score and Decision

The paper makes a genuine contribution: the IIS metric is well-motivated, and the empirical discovery of a positive correlation between interpretability and classifiability for pre-trained representations is novel, consistently observed across diverse settings, and directly challenges a widely held assumption. The application demonstrations add value.

However, the fine-tuning application claim (Section 4.1) suffers from a missing control baseline that prevents causal attribution, and the correlation analysis lacks statistical quantification. These are significant but not fatal — they do not undermine the core correlational finding, which is well-supported visually and across many settings. The paper needs targeted revisions (especially the fine-tuning control) to fully support its claims.

The paper is a solid empirical contribution that would benefit from tighter experimental design in one sub-component. I recommend **weak reject** in its current form — the missing baseline is a genuine methodological gap for the fine-tuning claim — but the paper is close and could become acceptable with the proposed controls.

MY FINAL SCORE: <pineapple>5.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>