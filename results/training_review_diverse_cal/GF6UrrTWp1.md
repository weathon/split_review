Now I have a thorough understanding of the paper and can verify each claim. Let me synthesize the final consolidated review.

## Summary

This paper proposes the "invariance starvation hypothesis" — the idea that deep neural networks rely on spurious correlations not because of an inherent simplicity bias, but because they lack sufficient data to encode the invariant function well. Through experiments on reasoning tasks (LEGO, PVR) and vision/language benchmarks (CelebA, MultiNLI), the paper shows that scaling data while maintaining spurious-feature proportion can eliminate spurious reliance in reasoning tasks, but can paradoxically *exacerbate* it in complex distributions. The paper claims to present a remedy for this exacerbation.

## Strengths

1. **Novel empirical finding: data quantity alone (not just proportion) drives spurious correlation behavior in reasoning tasks.** The paper carefully isolates the effect of data quantity by maintaining the proportion of spurious-to-invariant samples across scaling experiments (Section 4, Fig. 4). The finding that models achieve perfect accuracy on spurious-rule-violating test sets purely through more data — even while spurious-feature proportion is held constant — is non-obvious and directly challenges the assumption that proportion is the sole or primary determinant of spurious reliance. This is the paper's strongest contribution.

2. **Counterintuitive finding in complex distributions that more data can *worsen* worst-group accuracy.** Figure 6 shows that in CelebA and MultiNLI, doubling the training set while maintaining spurious proportion leads to a *drop* in worst-group accuracy. This is surprising and goes against the intuition that more data always helps. Identifying and documenting this failure mode is a genuine contribution to the spurious-correlations literature.

3. **Cross-domain validation strengthens the empirical basis.** The paper tests its hypotheses across reasoning (two LEGO variants + modified PVR), vision (CelebA), and language (MultiNLI) — three distinct domains with different architectures (BERT, ResNet-50). The consistency of the core data-quantity effect (even if direction varies) provides broader support than a single-domain study.

4. **Methodologically thoughtful experimental design.** Maintaining the proportion of spurious-to-invariant samples when scaling data (as opposed to naively adding samples that may shift the balance) is a careful design choice that cleanly isolates the variable of data quantity from confounding changes in spurious-feature prevalence.

## Weaknesses

### Fatal
None. The paper's core empirical findings are real and would survive revision.

### Major

1. **The paper promises a remedy that it does not deliver or evaluate.** The abstract states: "Taking inspiration from reasoning tasks, we present an effective remedy to this problem to ensure that drawing more samples from the distribution always overcomes spurious correlations." The introduction similarly claims "we use this knowledge to provide the model with samples that are generally well represented in the training distribution." The conclusion merely states "if one carefully draws samples with easier invariant features." But **the paper contains no section describing, implementing, or experimentally validating any such remedy.** There is no selection criterion, no algorithm, no empirical evaluation, no comparison with baselines. The abstract's central promised contribution is absent. This is a significant integrity gap between what is claimed and what is delivered.

2. **The claim to "refute" simplicity bias is overstated.** The paper writes: "Past works simply state that since deep neural networks are biased toward simpler predictive features, they are certain to learn and rely on spurious correlations. We refute this claim by showing that if the network is provided sufficient data to encode the invariant function well, it will no longer rely on simpler, weakly predictive spurious features." Showing that a bias *can be overcome* with sufficient data does not refute the existence of the bias; it merely identifies a mitigating condition. The existing literature (Shah et al., 2020, cited by the paper) already acknowledges that data scale matters. The paper's contribution is to show that data quantity — not just data proportion — matters, and this is a valuable *nuance* to simplicity bias, not a refutation. The framing inflates the contribution.

### Minor

3. **The explanation for vision/language exacerbation is asserted without supporting analysis.** The paper attributes the WGA drop in CelebA/MultiNLI to "the introduction of new samples which contain general features that are not well represented in the original training set" (Section 1) and samples that are "atypical or difficult for a network to generalize to" (Section 6). However, no analysis is provided to support this mechanism: no characterization of which new samples drive the degradation, no ablation removing suspected "atypical" samples, no measurement of feature typicality, and no control experiment demonstrating that the exacerbation disappears when sampling is stratified. The explanation is plausible and worth stating as a hypothesis, but it is presented as a finding rather than a conjecture.

4. **No error bars, confidence intervals, or multi-seed results are reported for any experiment.** Given the modest starting dataset sizes (1,000 for CelebA, 6,000 for MultiNLI, 4,000–37,500 for reasoning tasks), variance across runs could be substantial. Without any measure of variability, it is difficult to assess the reliability of the reported effects, particularly the subtle WGA changes in Fig. 6.

5. **Key concepts are not formally defined.** "Invariant information," "invariance starvation," and "atypical samples" are used throughout but never given formal definitions. This makes the hypothesis difficult to falsify or compare with alternative explanations. For example, it is unclear whether "invariant information" is measurable independent of the model's performance, or whether the claim is tautological (the network fails when it doesn't have enough information to succeed).

### Trivial
None.

## Nice-to-Haves
- Comparisons with existing spurious-correlation mitigation methods (group DRO, reweighting, data augmentation) would help contextualize the findings, but the paper is a hypothesis/analysis paper and this is not required for its core contribution.
- Extending the confidence/margin analysis (Fig. 5) to the vision/language experiments would strengthen the mechanistic story.
- More datasets within each domain (e.g., additional vision and language benchmarks) would broaden the empirical scope but are not necessary for the current claims.

## Removed Points
These points were raised by reviewers but removed after verification against the paper:

- **"Paper does not report training set sizes for reasoning tasks"** — REMOVED (factually incorrect). Section 3.3 explicitly reports: "In Task 1, Task 2 and Task 3, we maintain the training set size as 30,000, 4,000 and 37,500, respectively." The scaling x-axes in Fig. 4 also show the sizes.
- **"Group definitions for CelebA/MultiNLI are questionable"** — REMOVED. Eyeglasses→Male for CelebA and negation→contradiction for MultiNLI are standard benchmarks established by Sagawa et al. (2020a) and widely used in the spurious-correlations literature. Criticizing their validity is a reviewer preference issue, not a paper flaw.
- **"Vision/language experiments contradict the starvation hypothesis"** — REMOVED as strawman. The paper explicitly documents the exacerbation finding as part of the hypothesis (not a contradiction) and offers an explanation. The phenomenon is presented as a surprising but consistent part of the overall story about data quantity effects.
- **"Paper's empirical scope is too narrow"** — DOWNGRADED and moved here. Covering reasoning (3 tasks), vision, and language — three domains with different architectures — is a reasonable scope for a single paper. The claim "comprehensive" is slightly generous but not misleading enough to constitute a weakness.
- **"Existing methods already acknowledged data scale mitigates bias"** — REMOVED. Without the specific Shah et al. 2020 reference accessible for verification, this claim cannot be confirmed. The paper's specific finding (maintaining spurious proportion while scaling) goes beyond generic "more data helps."

## Novel Insights

The most interesting insight from the reviews — beyond the paper's own findings — is the asymmetry between the well-controlled reasoning-task experiments (where the data-quantity effect is clean and monotonic) and the complex-distribution experiments (where it is non-monotonic). This asymmetry, if validated with mechanistic analysis, could reveal a fundamental difference in how neural networks generalize on combinatorial/symbolic versus perceptual tasks — a distinction that current spurious-correlation theory does not adequately capture. The paper identifies the phenomenon but does not yet leverage it into a theoretical distinction.

## Suggestions

1. **Align the abstract and claims with what the paper actually delivers.** Either add a proper remedy section with experimental validation, or remove the remedy claim from the abstract. Similarly, replace "refute" with more precise language like "qualify" or "reveal a mitigating condition for."
2. **Provide a formal or operational definition** of "invariant information" — even a simple one tied to the experimental setup (e.g., features that are necessary and sufficient for the task across all environments). Without this, the hypothesis risks being unfalsifiable.
3. **Add error bars or multi-seed results** for all experiments, especially the CelebA and MultiNLI WGA plots where the effect sizes are modest.
4. **Characterize the "atypical" samples** that allegedly drive the exacerbation in vision/language. Simple analyses — e.g., identifying which specific added samples cause the WGA drop, measuring their feature-space distance from the original set, or demonstrating that removing them restores monotonic improvement — would transform a speculation into a validated mechanism.
5. **Tone down the rhetoric.** The paper's empirical contributions are genuinely interesting and do not need overclaimed refutations or unredeemed promises to be publishable.

## Score and Decision

MY FINAL SCORE: <pineapple>5.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>