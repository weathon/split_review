Now I have everything I need. Let me produce the final review.

## Summary

The paper proposes the "invariance starvation hypothesis" — the claim that deep networks rely on spurious correlations not because of an inherent simplicity bias, but because they are starved of sufficient training data to encode the invariant function. Through reasoning tasks (LEGO, PVR), the paper shows that scaling data while preserving the proportion of spurious samples eliminates spurious reliance. In vision (CelebA) and language (MultiNLI), the same scaling can *exacerbate* spurious correlations. The paper attributes this discrepancy to "atypical samples" in complex distributions and claims an effective remedy.

## Strengths

1. **Counterintuitive empirical discovery in vision/language**: The finding that more data (at constant spurious proportion) *worsens* worst-group accuracy on CelebA and MultiNLI (Fig. 6) is genuinely interesting and challenges the naive assumption that scaling always helps. This is a novel empirical observation that the community should be aware of.

2. **Clean demonstration in reasoning tasks**: Figures 3 and 4 convincingly show that in low-dimensional reasoning tasks (LEGO Tasks 1–2, PVR Task 3), scaling training data while maintaining the spurious proportion drives spurious test accuracy from ~60% to 100%. The effect is clear and the design is controlled.

3. **Confidence/margin analysis provides mechanistic insight**: Figure 5's analysis of logit margins shows that in the low-data regime the network uses spurious rules to boost confidence, while in the high-data regime it no longer needs to. This offers a mechanistic window into *why* more invariant data reduces shortcut reliance.

4. **Three-domain evaluation**: Studying reasoning, vision, and language with consistent methodology lends breadth to the empirical contribution and helps scope the hypothesis.

## Weaknesses

### Fatal
None. The paper's core empirical observations (the data-scaling effects in both reasoning and vision/language settings) survive scrutiny, even if the overarching hypothesis framing is problematic.

### Major

1. **The central hypothesis is stated too broadly and the discrepancy with vision/language results is explained by an untested mechanism.** The paper claims in the abstract and introduction that "if the network has sufficient data to encode the invariant function appropriately, it no longer learns and relies on spurious correlations present in the training data… regardless of its *strength*." Section 5 then shows that in vision/language, scaling data *exacerbates* spurious correlations. The paper attributes this to "atypical samples" that force spurious reliance, but **this explanation is never tested or quantified**: no analysis of which samples are atypical, no controlled experiment removing them, no measure of typicality. The abstract itself is confusing — it states "We observe the same results in settings with more complex distributions" and then immediately "However, we find that in such settings, drawing more samples… can exacerbate spurious correlations." This unresolved tension between the broad claim and the evidence undermines the paper's central argument.

2. **The promised remedy is asserted but never described, implemented, or validated.** The abstract states: "Taking inspiration from reasoning tasks, we present an effective remedy to this problem to ensure that drawing more samples from the distribution always overcomes spurious correlations." The conclusion repeats: "if one carefully draws samples with easier invariant features from the training distribution, one can overcome invariance starvation and mitigate spurious correlations." However, **no algorithm, experimental validation, or concrete description of this remedy appears anywhere in the paper**. The paper's framing promises a solution it does not deliver. This is not a minor omission — the abstract and introduction frame the paper as offering a remedy, making this a broken commitment at the paper's core framing level.

3. **The "refutation" of simplicity bias is overstated and partially a straw man.** The paper claims: "Past works simply state that since deep neural networks are biased toward simpler predictive features, they are *certain* to learn and rely on spurious correlations. We refute this claim..." The standard simplicity bias literature does *not* claim that spurious correlations will *always* form regardless of data scale — it identifies a bias that operates given a *fixed* dataset, and many existing works already show that sufficient data can overcome this bias. The paper's observation that scaling helps in reasoning tasks is interesting but does not constitute a refutation of prior work. This inflates the claimed novelty.

### Minor

1. **"Invariant starvation" is not quantitatively defined**, making the hypothesis difficult to falsify. The paper never provides a measurable definition of "enough invariant information" or a testable criterion for "starvation." It is used descriptively rather than as a formal claim. A tighter definition (e.g., in terms of sample complexity or a measurable confidence gap) would substantially strengthen the paper's scientific contribution.

2. **No statistical significance or variance reporting.** The paper presents trends in Figures 4 and 6 without mentioning the number of random seeds, error bars, or confidence intervals. For an empirical study whose central claims rest on trends (scaling helps vs. hurts), variance information is important for robustness.

3. **The "atypical samples" explanation for the vision/language exacerbation is not tested.** The paper provides no experimental evidence that atypical samples are the cause. A controlled analysis (e.g., identifying atypical samples via embedding distance and checking whether removing them reverses the trend) would be needed to substantiate the claim.

4. **No limitations or discussion of alternative explanations.** The paper does not discuss the possibility that the vision/language results might have alternative explanations (e.g., increased dataset diversity introducing new spurious correlations, or the finite-reservoir effect where doubling from a limited dataset reuses samples).

5. **Missing detail on data scaling in vision/language.** Section 5.2 says it "starts with a fixed number of samples per group and repeatedly doubles that amount." It is unclear whether new data is sampled i.i.d. from an infinite source or from a finite dataset. If from a finite dataset, repeated doubling eventually reuses samples, changing the effective diversity and potentially confounding the interpretation.

6. **Hyperparameter tuning to optimize WGA** is standard practice in the spurious-correlations literature, but for an *observational* study of ERM's natural behavior (rather than a method paper), tuning for WGA may interact with dataset size in ways that affect the reported trends. This should at least be acknowledged.

### Trivial
- The abstract juxtaposes "We observe the same results" and "However... can exacerbate" without clarifying what "same results" refers to. This is confusing and should be rephrased.

## Nice-to-Haves
- A controlled experiment in vision/language where "atypical" samples are explicitly characterized and removed to test whether the exacerbation reverses.
- A formal or quantitative definition of "invariant starvation" (e.g., a measure based on the gap in prediction confidence between typical and atypical samples).
- Analysis with multiple random seeds to assess variance of the reported trends.

## Removed Points
These points are flagged to be removed; treat them with caution:
- **"Figure 6 cannot be seen"** — This is a parser artifact; the figure exists in the original submission.
- **"The spurious feature in CelebA and MultiNLI would be better tested if under the authors' control"** — Using standard benchmarks is a defensible methodological choice; demanding synthetic control is scope creep beyond what this empirical study reasonably provides.
- **"Central hypothesis is a structural failure / direct empirical refutation"** — While the hypothesis is stated too broadly, the paper *does* acknowledge the tension and offers an explanation. The real problem is overclaiming + untested mechanism, not self-contradiction. The criticism as phrased is too severe.
- **Strength from Strength Finder about "practical implication: careful sampling of typical invariant features mitigates exacerbation"** — This strength conflicts with the verified weakness that the remedy is not validated. Since weakness wins, this strength is dropped.
- **"Weaknesses about missing related works"** — Per instructions, I do not mention missing related works as I cannot verify them.

## Novel Insights
The reviews surface a genuinely novel framing opportunity: the *contrast* between reasoning tasks (where scaling monotonically helps) and vision/language (where scaling can hurt) is the paper's most robust and interesting finding. The invariance starvation hypothesis is a plausible explanation for the reasoning-task behavior, but the vision/language divergence demands a mechanism (atypical samples) that the paper does not validate. Reframing the paper as a characterization of *when* scaling helps vs. hurts — with the atypical-sample hypothesis as a testable prediction rather than a concluded explanation — would better match the evidence.

## Suggestions
1. **Reframe the paper around the central contrast.** The most robust finding is the *divergence* between reasoning and vision/language scaling behaviors. Reposition the paper accordingly.
2. **Either deliver the remedy or remove it from the abstract and introduction.** A paper that is an empirical study should not claim to present a solution it does not validate.
3. **Test the atypical-sample hypothesis** with a controlled intervention: measure feature-space distances of added samples, identify which specific samples degrade WGA, and conduct an ablation.
4. **Tone down the "refutation" of simplicity bias.** Acknowledge that prior work does not claim spurious correlations *always* form, and position the contribution as clarifying *when* data quantity modulates the effect.
5. **Add error bars or multiple-seed reporting** for all quantitative claims.
6. **Clarify the abstract's confusing juxtaposition** between "same results" and "exacerbate."

## Score and Decision

The paper makes real empirical contributions — the contrast between scaling behaviors in reasoning vs. vision/language is genuinely interesting, and the reasoning-task results are clean. However, the paper significantly overclaims in its framing (presenting a sweeping hypothesis that is not supported by its own vision/language results, claiming to refute prior work with a straw man, and promising a remedy it does not deliver). The central explanatory mechanism for the most interesting finding (atypical samples in vision/language) is not tested. In its current form, the paper promises more than it delivers. Significant revision is needed to align claims with evidence.

MY FINAL SCORE: <pineapple>5.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>