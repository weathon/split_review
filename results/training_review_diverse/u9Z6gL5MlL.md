Now I have a thorough understanding of the paper and can verify each claim against the actual content. Let me produce the consolidated review.

## Summary

This paper challenges the widespread practice of using artificial memorization (noisy labels/noisy inputs) as a proxy for natural memorization in deep learning. The authors re-examine two findings from the artificial memorization literature—that over-parameterization and longer training increase memorization—by running analogous experiments on natural memorization (using the Feldman & Zhang 2020 approximation with 2,000 models per architecture). They report the opposite effects: more capable models memorize fewer natural points, and memorization follows a three-stage dynamic (none → peak → decline) over training. They also identify "transient memorization" (points memorized by small models/early epochs but generalized by larger models/later epochs) and report a high correlation (Pearson 0.99) between memorization and train-test gap.

## Strengths

- **Important and timely research question.** The paper targets a genuine methodological gap: the artificial memorization proxy is widely used (Zielinski et al., Chattejjee, Cheng et al., others), yet its validity for real-world natural memorization is largely untested. Challenging this assumption is valuable for the field.

- **Consistent trend across three architecture families.** The finding that more capable models (deeper/wider VGGs, ResNet50 vs. 18, ViT-Small vs. Tiny) memorize fewer natural points is reproduced independently across VGG, ResNet, and ViT families on three datasets. The consistency lends credibility to the general claim even though the designs do not isolate parameter count as the sole causal factor.

- **Discovery and characterization of transient memorization.** The paper identifies two forms of transient memorization (model-wise and temporal-wise) and quantifies that transient points belong to smaller sub-populations (average memorization score 44.99% for model-wise vs. dataset average 11.17%, Section 4.3). This is a genuinely novel observation that reveals a mechanism through which increasing capacity reduces memorization: the model learns features for rare sub-populations rather than memorizing them.

- **Substantial empirical methodology.** Training 2,000 models per architecture across three datasets (CIFAR-10, CIFAR-100, Tiny ImageNet) with multiple architecture families is a significant computational investment that provides robustness beyond single-architecture studies.

## Weaknesses

### Fatal
None. The paper has real contributions and the core question is valid, but the weaknesses below significantly limit its claims.

### Major

- **The "memorization is not necessary for generalization" conclusion does not follow from the presented evidence.** Feldman & Zhang's (2020) necessity claim is about a model of *fixed capacity*: given a model at a given capacity, memorizing low-support points is required to achieve good test accuracy. The paper shows that *increasing* capacity reduces memorization and improves generalization, but this is consistent with the view that memorization is a fallback when capacity is insufficient—it does not disprove necessity for models of fixed capacity. The paper would need to show that a fixed model can reach its maximum accuracy *without* memorizing points it otherwise would. The transient memorization results come closest, but even there, the model that eventually generalizes the points initially memorized them. This is the most consequential logical gap in the paper and directly affects one of its headline claims.

- **The over-parameterization experiment confounds parameter count with architectural differences.** The paper compares models that differ in depth, width, and structural innovations simultaneously (e.g., SmallVGG2 vs. VGG19 differ in depth *and* width; ResNet18 vs. ResNet50 differ in depth, block structure, *and* parameter count; ViT Tiny vs. Small differ in hidden size, layers, and heads). The claim that "parameter count *per se*" reduces memorization is not supported—the variable "over-parameterization" covaries with depth, residual connections, attention head count, and other architectural features known to affect learning dynamics. The consistency across three families suggests the general trend (more capable models memorize fewer points) is real, but the paper's framing as an "over-parameterization" finding overstates what can be concluded. A cleaner design (varying width alone within a fixed-depth architecture) is needed to isolate the role of parameter count.

- **The central thesis—that artificial memorization is an invalid proxy—lacks a direct, controlled side-by-side comparison.** The paper compares its natural memorization results against claims from prior artificial memorization work (different labs, architectures, training setups). While the direction of the effects differs, the paper never runs artificial memorization experiments within its own controlled pipeline. This opens the door to alternative explanations: the observed differences could stem from methodological variations (different architectures, learning rates, thresholds) rather than the type of memorization per se. A direct comparison—injecting artificial points into the same datasets and measuring both natural and artificial memorization with the same pipeline—would substantially strengthen the core argument.

- **The Pearson correlation of 0.99 lacks proper statistical reporting.** The paper states this score (Section 4.4, Figure 3) but does not report the number of data points, confidence intervals, or p-values. With a small number of points (likely 7–9 per dataset, corresponding to the number of architectures), a correlation of 0.99 is fragile and potentially driven by a single influential point or ceiling effects. This is particularly problematic because the paper uses this correlation to support the "memorization is not necessary" conclusion. Standard statistical reporting is needed before this evidence can be relied upon.

### Minor

- **The abstract oversimplifies the training-iteration finding.** The paper claims that "increased training time reduces natural memorization" (abstract, line 4), but the data (Figure 2, Section 4.2) show a clear three-phase pattern: no memorization initially, then a long ramp-up to a peak (~epoch 77), followed by a decrease. For the majority of training, memorization is *increasing*. The paper's detailed text characterizes this accurately, but the headline framing is misleading and obscures the non-monotonic relationship.

- **The transient memorization analysis is descriptive rather than mechanistic.** The paper identifies transient points and characterizes their memorization scores, concluding they belong to smaller sub-populations. This is consistent with the Feldman & Zhang framework but is not independently verified by, e.g., directly examining the data characteristics (class frequency, image difficulty) of these points. A direct characterization would strengthen the mechanistic explanation.

- **No sensitivity analysis on the 25% memorization threshold.** The number of memorized points is threshold-dependent. Showing that the main results hold across a range of thresholds (e.g., 10%, 25%, 50%) would increase confidence that the patterns are not artifacts of a single cutoff.

- **No discussion of whether the Feldman & Zhang approximation (r=0.7 subsampling) might introduce differential bias across architectures.** If different architectures have different generalization behavior under different training set fractions, the approximation's accuracy could vary across models, potentially affecting the comparison of memorization counts.

### Trivial
None.

## Nice-to-Haves

- Running artificial memorization experiments within the same pipeline (same architectures, datasets, training setup) to enable a direct controlled comparison.
- Varying only the width of a fixed-depth architecture (e.g., a single VGG-like CNN) to isolate the effect of parameter count from depth and structural innovations.
- Training models beyond 100 epochs to see whether memorization eventually increases again (consistent with a double-descent analogy).
- Proper statistical reporting for the Pearson correlation: sample size, confidence intervals, per-dataset breakdown.
- Sensitivity analysis across memorization thresholds (10%, 25%, 50%).

## Removed Points

- **Criticism about the use of "over-parameterization" being inconsistent with the literature definition (parameters > data points).** The paper uses the term consistently to mean "having more trainable parameters," which is a common usage in the discussion of memorization. This is a terminological preference rather than a substantive flaw.
- **Criticism that the paper only cites "a few examples" for the claim about artificial memorization prevalence.** The paper does not rely on a precise prevalence estimate for its core argument; it only needs to establish that the proxy *is used*, which the cited examples do.
- **Strength Finder claim that "Section 1 lists four reasons that are then empirically validated by the results."** This overstates: the experiments directly address reasons (3) and (4) but reasons (1) and (2) about unstructured outliers and mislabeled data are argued conceptually, not experimentally tested.

## Novel Insights

The most interesting observation beyond the paper's own claims is that "transient memorization" provides a natural resolution to the apparent contradiction between the paper's results and Feldman & Zhang's necessity claim. Points memorized by smaller models but generalized by larger ones are exactly the low-support points that Feldman & Zhang identified as requiring memorization—but the paper shows that with sufficient capacity, these same points can be learned properly. This suggests that memorization is a *capacity-dependent* phenomenon: whether a point "requires" memorization depends on the learner's ability to extract its features. The paper does not develop this insight fully, but it is a potentially productive direction.

## Suggestions

1. **Clarify what claim exactly is being disputed.** Acknowledge that Feldman & Zhang's necessity claim operates at fixed capacity and that the paper's across-model design addresses a related but distinct question. Either reframe the conclusion more modestly ("memorization is not necessary for generalization *when capacity is sufficient*") or design an experiment that isolates a fixed-capacity scenario.

2. **Add a cleaner over-parameterization experiment.** Vary only the width of a single VGG-like architecture (holding depth constant) and confirm the trend. This would remove the confound between parameter count and architectural innovations and substantially strengthen claim 2.

3. **Report full statistical details for the Pearson correlation.** Provide the number of data points, confidence intervals (bootstrapped), p-values, and per-dataset scatter plots. Consider reporting Spearman rank correlation as a robustness check.

4. **Include an explicit artificial-vs-natural comparison in the same pipeline** as a secondary experiment. Even a smaller-scale version (one dataset, one architecture family, injecting noisy labels) would directly test the proxy assumption and move the paper's claim from assertion to demonstration.

## Score and Decision

This paper tackles an important question with substantial empirical effort, and the transient memorization finding is genuinely interesting. However, the core logical gaps (the "memorization not necessary" conclusion not following from the evidence, the over-parameterization confound, the lack of direct artificial-vs-natural comparison) significantly limit what the paper can claim. The results are suggestive and point in a useful direction, but in their current form the paper's headline conclusions overreach the experimental design. Major revisions—especially cleaner experimental controls and more careful framing of conclusions—are needed before the paper's contribution is fully credible.

MY FINAL SCORE: <pineapple>4.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>