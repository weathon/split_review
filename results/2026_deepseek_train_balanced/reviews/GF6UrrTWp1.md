## Summary

The paper proposes the "Invariance Starvation Hypothesis" — the idea that deep networks learn spurious correlations not because of an inherent simplicity bias alone, but because they are "starved" of sufficient invariant data. The authors present empirical evidence across reasoning tasks (LEGO, PVR), vision (CelebA), and language (MultiNLI). In reasoning tasks, scaling up data while maintaining the proportion of spurious samples eliminates spurious reliance. In vision/language, the same scaling can worsen worst-group accuracy, which the paper attributes to "atypical" samples. The paper claims a remedy for the complex-distribution case inspired by reasoning tasks.

## Strengths

1. **Empirical demonstration that data quantity can overcome spurious correlations in reasoning tasks while keeping spurious proportion fixed**: Section 4 (Fig. 4, line 88) shows that on all three reasoning tasks, simply increasing dataset size — maintaining the proportion of samples containing the spurious rule — enables the model to reach perfect accuracy on test sets that break the spurious rule. This is a clean, controlled demonstration that challenges the simplistic view that spurious correlations are inevitable at any data scale.

2. **Counterintuitive finding of a qualitative asymmetry between reasoning and vision/language**: Section 5.3 (Fig. 6, lines 121–132) documents that on CelebA and MultiNLI, worst-group accuracy *decreases* as the training set is doubled from the same distribution. This non-obvious result, contrasting with the reasoning-task findings, suggests the interaction between data scale and spurious correlations is domain-dependent — an observation prior work had not highlighted.

3. **Cross-domain evaluation spanning reasoning, vision, and language**: The paper tests across three domains using both encoder-only transformers (BERT) and convolutional networks (ResNet-50), providing evidence that the phenomenon is not limited to a single architecture or input modality.

4. **Margin/confidence analysis offering mechanistic intuition**: Figure 5 and lines 90–95 compare model confidence trained with both invariant and spurious rules versus only the invariant rule, showing that in the low-data regime the network uses the spurious rule to increase confidence but abandons it as data scales. While qualitative, this analysis provides a plausible link between data quantity and spurious-feature abandonment.

## Weaknesses

### Fatal
None.

### Major

1. **The "remedy" promised in the abstract and conclusion is never presented or evaluated.** The abstract (line 4) states: "Taking inspiration from reasoning tasks, we present an effective remedy to this problem to ensure that drawing more samples from the distribution always overcomes spurious correlations." The conclusion (line 139) reiterates: "we show that in such settings, if one carefully draws samples with easier invariant features from the training distribution, one can overcome invariance starvation and mitigate spurious correlations." However, the main text contains *no* section, experiment, figure, or analysis implementing or evaluating this remedy. The paper transitions directly from Section 5 (documenting the exacerbation) to Section 6 (conclusion). This is a structural flaw: the paper claims a contribution it does not deliver. The authors must either include the remedy experiments or remove these claims from the abstract and conclusion.

2. **The mechanism claimed for the vision/language exacerbation is stated without evidence.** The paper asserts (line 16, lines 128–132) that exacerbation occurs because "new samples contain general features that are not well represented in the original training set but also contain the spurious feature." No evidence supports this: which samples are "atypical," how typicality is quantified, whether removing these samples eliminates the effect, or whether alternative explanations (e.g., suboptimal hyperparameters at larger scales, artifacts of extremely small starting datasets, optimization dynamics) are ruled out. The central explanatory claim for the paper's most surprising result is untested.

### Minor

1. **Overclaimed "refutation" of prior simplicity-bias literature.** The paper (lines 14, 27) frames its findings as a refutation: "Past works simply state that since deep neural networks are biased toward simpler predictive features, they are certain to learn and rely on spurious correlations. We refute this claim." This mischaracterizes the cited works. Shah et al. (2020) prove a specific result about gradient descent converging to the simpler of two *fully predictive* features in the infinite-data limit — a different regime from this paper's finite-sample setting with *weakly predictive* spurious features. The paper's findings are consistent with standard statistical learning and do not contradict Shah et al.'s result. The framing should be recalibrated from "refutation" to "extension showing data quantity interacts with simplicity bias."

2. **No error bars, confidence intervals, or random seeds for any quantitative result.** All results in Figures 3–6 are described qualitatively. Without variance estimates, it is impossible to assess whether the observed trends are statistically significant. This is especially critical for the CelebA and MultiNLI experiments, where starting dataset sizes are very small (1,000 and 6,000 respectively) and single-run results could be unreliable.

3. **No discussion of limitations.** The paper does not acknowledge that its reasoning tasks are synthetic, that the starting dataset sizes for vision/language are far smaller than standard usage of these benchmarks (CelebA normally uses ~162K training images), that hyperparameters are held fixed while data scales (potentially confounding the comparison), or that the promised remedy is absent.

### Trivial

1. **Abstract contains an internal contradiction.** The abstract states "We observe the same results in settings with more complex distributions... such as vision and language" (implying more data helps) followed by "However, we find that in such settings, drawing more samples... can exacerbate spurious correlations." These two statements are logically incompatible and should be reconciled.

## Nice-to-Haves

- Compare against group DRO, importance reweighting, or data augmentation at matched data scales to contextualize the practical significance of the observed effects.
- Report exact dataset sizes at each doubling step and the number of doublings performed.
- Validate the "atypical samples" mechanism by identifying, characterizing, and ablating these samples.

## Removed Points

The following points from the harsh critic were removed under the filtering discipline:

- **Criticism about missing baselines being a fatal omission**: The paper's goal is understanding the role of data quantity, not method comparison. Baselines are a reasonable suggestion but not a core weakness, as the paper does not claim SOTA. Moved to Nice-to-Haves.
- **"Data scaling quantities not reported" framed as major**: The paper partially reports dataset sizes and states data was "repeatedly doubled." The absence of exact step sizes is a minor reporting gap. Subsumed into Nice-to-Haves.
- **Criticism that 1,000 CelebA starting size tests a "very different regime"**: The paper is free to study any data regime; this is a scope observation, not a flaw. Removed as scope creep.
- **"Perfect accuracies" described as "suspiciously strong"**: The reasoning tasks are simple and synthetic; perfect accuracy is not surprising. This criticism is speculative, not a verified weakness. Removed.
- **Abstract contradiction framed as evidence of haste**: The contradiction is a real writing issue (kept as Trivial) but editorializing about author carelessness is removed.
- **Strength Finder's claim that the margin/confidence analysis provides strong "mechanistic evidence"**: The analysis is qualitative and lacks quantitative backing. Downgraded from "mechanistic evidence" to "mechanistic intuition."

## Novel Insights

The most striking observation from synthesizing the reviews is that the paper's two core empirical findings are in unresolved tension with each other: the "invariance starvation" hypothesis predicts that more invariant data should universally reduce spurious reliance, yet the vision/language results directly violate this prediction. The paper attempts to resolve this with an "atypical samples" explanation but does not test it. This unresolved tension is actually the paper's most interesting aspect — it suggests the phenomenon is richer than the invariance starvation framing alone captures, and that feature typicality and data geometry may matter at least as much as data quantity. A stronger paper would lean into this tension as evidence for a more nuanced theory, rather than treating the reversal as a problem requiring a separate remedy.

## Suggestions

1. Either add the remedy experiments described in the abstract and conclusion, or honestly remove those claims and scope the paper as an observational study of the asymmetric effects of data scaling.
2. Add statistical rigor: report results with error bars (multiple seeds), random seeds, and explicit dataset sizes at each scaling step.
3. Provide evidence for the claimed mechanism in the vision/language experiments — characterize "atypical" samples, show that removing them eliminates the exacerbation, or test alternative explanations.
4. Recalibrate the "refutation" framing to avoid misrepresenting prior work; position the findings as an extension showing finite-sample interactions with simplicity bias.
5. Add a limitations section acknowledging the synthetic nature of the reasoning tasks, the small starting sizes for vision/language, and the unvalidated mechanism for the exacerbation.

MY FINAL SCORE: <score>4.5</score>
MY FINAL DECISION: <decision>Reject</decision>