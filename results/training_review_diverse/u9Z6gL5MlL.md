Now I have all the evidence I need. Let me compose the final consolidated review.

---

## Summary

This paper studies "natural memorization" (memorization of real training points) as opposed to "artificial memorization" (memorization induced via noisy labels/inputs). It replicates the expensive Feldman & Zhang leave-one-out approximation across VGG, ResNet, and ViT families on CIFAR-10/100 and Tiny ImageNet, and reports that: (1) over-parameterization *reduces* natural memorization (the opposite of prior artificial-memorization findings), (2) memorization across training follows a three-stage pattern (none → increase → decrease), (3) "transient memorization" exists where points memorized under one condition are generalized under another, and (4) memorization and train-test gap are correlated at r=0.99. The paper argues that artificial memorization is not a valid proxy for natural memorization.

## Strengths

1. **Directly studies natural memorization at scale.** The computational expense of the Feldman & Zhang leave-one-out approximation is well-documented (thousands of models per architecture), and few papers carry it out on this scale. The experiments across three datasets and three architecture families (VGG, ResNet, ViT) provide a solid empirical foundation for characterizing natural memorization behavior.

2. **Introduces and characterizes transient memorization.** The observation that many memorized points are not permanently stored — they become generalized when model capacity or training time increases — is genuinely novel. The quantitative characterization (model-wise transient points: 44.99% average memorization score vs. 11.17% dataset average; temporal-wise: 35.71% vs. 11.17%) provides concrete evidence that memorization is not always persistent and that increasing capacity can "unlearn" memorized points. This is the paper's most distinctive finding.

3. **Demonstrates a clear within-family trend.** Within the VGG family (SmallVGG → MedVGG → LargeVGG → VGG19) and within the ResNet family (ResNet18 → ResNet50), the paper shows that increasing depth/parameters consistently reduces the number of memorized points. These within-family comparisons (trained from scratch, same architecture family) are the cleanest evidence in the paper and stand regardless of the ViT pre-training issue.

## Weaknesses

### Fatal
None.

### Major

1. **No controlled within-paper comparison between artificial and natural memorization.** The paper's central thesis is that artificial memorization is a misleading proxy for natural memorization. But the evidence for this claim is indirect: the paper studies natural memorization and compares its trends against *prior published findings* from artificial memorization — findings that come from different datasets, architectures, training schedules, and often different definitions of memorization. The paper never runs its own artificial-memorization experiments using the same architectures, datasets, and training setup used for its natural-memorization experiments. Without a controlled head-to-head comparison (e.g., injecting noisy labels/inputs into one condition of the same experimental pipeline), the observed differences cannot be cleanly attributed to the proxy-vs-natural distinction rather than to the many confounding differences between the present setup and prior work. This significantly weakens the paper's core argument.

2. **Triangular learning rate confounds the training-time three-stage pattern.** The paper uses a triangular learning rate schedule (line 77) and observes that memorization peaks at Epoch 77 and then declines (Stage 3). With a triangular schedule, the learning rate ramps up, then ramps down. The decline in memorization after Epoch 77 may be driven by the learning rate decay (which stabilizes the model and reduces the need to memorize) rather than by "more training iterations" per se. The paper does not control for this (e.g., by using a constant learning rate, a cosine schedule, or analyzing memorization under a held learning rate). Without such controls, the claim that "increased training iterations reduce memorization" — which the paper presents as a general property of natural memorization — is confounded with the specific learning rate dynamics. This is a structural issue for one of the paper's two main experimental findings.

### Minor

3. **The 0.99 Pearson correlation lacks supporting details.** A correlation of 0.99 across what appears to be approximately 8 models per dataset is suspiciously high. The paper does not provide a scatter plot, confidence intervals, a significance test, or any description of how many points went into the calculation. Given the small number of data points, a high correlation can arise from a single influential observation or a trivial mathematical relationship (e.g., if memorization count and train-test gap are both computed from the same training runs in a way that guarantees a monotonic relationship). Without seeing the actual scatter plot and having some measure of uncertainty, the reader cannot evaluate whether this is a meaningful discovery or an artifact. This matters because the paper uses this correlation to argue that memorization is not necessary for generalization.

4. **No uncertainty quantification on the number of memorized points.** The paper trains 2,000 models per architecture, which ought to enable bootstrapping or computation of standard errors on the memorization counts. Yet all results in Figures 1, 2, and 4 are presented as point estimates without error bars or confidence intervals. It is impossible to judge whether observed differences (e.g., SmallVGG vs. VGG19 memorization counts, or the peak at Epoch 77 vs. Epoch 99) are statistically significant or within the noise of the approximation. This weakens the reliability of the quantitative comparisons.

5. **The claim "memorization is not necessary for generalization" overreaches the evidence.** The paper shows that memorization can decrease as capacity increases and that some memorized points become generalized. But it also acknowledges (Figure 4b) that "higher iterations lead to points with extremely high memorization scores (between 90%–100%)" that persist. For those points, memorization may indeed be necessary. The current absolute claim should be qualified: memorization may be *reduced* without harming generalization, but some points (especially extreme outliers) may always require memorization. The paper's own evidence supports a more nuanced conclusion than the blanket statement in Section 5.

6. **Pre-trained ViTs introduce a confound for cross-family comparisons.** The paper states it uses "pre-trained ViTs" while VGG and ResNet models are trained from scratch. However, this issue is limited: the main over-parameterization trends are demonstrated within the VGG family and within the ResNet family (both trained from scratch), where no confound exists. The ViT results are supplementary. Still, claims about cross-family trends (e.g., "ResNet18 memorizes fewer points than VGG19 even with fewer parameters") should note that ViTs have the additional benefit of pre-training, or better, the paper should state the training regime for each model explicitly.

### Trivial

7. **No limitations paragraph in the conclusion** acknowledging the lack of controlled artificial-memorization experiments, the learning rate confound, or the limitations of the Feldman & Zhang definition.

## Nice-to-Haves

- A sensitivity analysis of the memorization threshold (25%) and sampling fraction (r=0.7) to show that the main trends are robust to these arbitrary choices.
- Experiments with alternative learning rate schedules (constant, cosine) to disentangle the role of training iterations from the triangular schedule.
- A scatter plot of memorization vs. train-test gap for each dataset, with confidence bands.
- Error bars on the memorization counts in Figures 1 and 2, bootstrapped from the 2,000 trained models.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **Missing related work section / missing appendix / missing proofs.** The parser strips supplementary sections from all papers; they exist in the original submission. Removed per instructions.
- **"No discussion of computational cost."** The paper explicitly discusses computational cost in Section 3.2 ("prohibitively expensive," "computationally intractable," "a few thousand models"). Removed as factually incorrect.
- **"Results from 8–12 models per dataset" — the correlation sample size.** The actual number of models is ~8 per dataset, which is a valid concern but belongs in the Minor weakness above, not a separate point. Merged.
- **"The paper should also cover LLMs / other domains."** Scope creep beyond the paper's stated scope (classification under the Feldman & Zhang definition). Removed.
- **Generic formatting/style nitpicks.** Removed per instructions.

## Novel Insights

The most useful insight from the reviews concerns the triangular learning rate confound: the paper's three-stage memorization pattern may be an artifact of the specific learning rate schedule rather than a general property of natural memorization across training. This is a genuinely helpful observation that the authors should address experimentally. Beyond this, the reviews do not produce novel insights beyond what the paper itself contributes.

## Suggestions

1. **Add a controlled artificial-memorization arm to the experiments.** Run the exact same architectures, datasets, and training procedure, but inject a small fraction of noisy labels (e.g., 1–5% label corruption). Show that under this artificial setup, over-parameterization *increases* memorization (replicating prior work), while under the identical setup without label corruption, it *decreases* memorization. This single experiment would make the paper's central argument airtight.

2. **Disentangle training iterations from the learning rate schedule.** Repeat the training-time experiment (Section 4.2) with a constant learning rate or a cosine schedule, and show whether the three-stage pattern (especially the decline in Stage 3) persists. If it does, the claim about training iterations is robust; if not, the paper must re-scope that finding.

3. **Provide a scatter plot and confidence interval for the 0.99 correlation.** Report the number of points, the Pearson r with confidence bounds (e.g., via Fisher z-transformation), and a significance test. If the correlation is genuine, this will strengthen the paper; if it is an artifact of small sample size, better to discover it now.

4. **Add error bars to the memorization counts.** The 2,000 models can be bootstrapped to produce standard errors for the number of memorized points in Figures 1 and 2. Without them, the reader cannot tell if reported differences are meaningful.

5. **Qualify the "memorization is not necessary for generalization" claim.** Acknowledge that some high-score points persist and may require memorization even in large models, and rephrase to: "memorization is not *universally* necessary for generalization; increasing capacity can reduce reliance on memorization for many points."

## Score and Decision

The paper tackles an important question and produces interesting observations — transient memorization is a genuinely novel finding. However, the two major weaknesses (lack of a controlled artificial-vs-natural comparison and the learning rate confound) significantly undermine the paper's strongest claims. The 0.99 correlation is reported without the supporting detail needed to assess it. The paper would need major revisions — especially the addition of controlled artificial-memorization experiments and a disentanglement of training iterations from the learning rate schedule — before its central thesis can be considered convincingly supported. As it stands, the contribution is insufficient to warrant acceptance.

MY FINAL SCORE: <pineapple>4.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>