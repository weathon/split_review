Here is my consolidated review:

## Summary

This paper identifies and characterizes an interpretability illusion in subspace activation patching. It shows that a 1-dimensional subspace found via methods like DAS can produce the intended behavioral change by combining a *causally disconnected* direction (in the kernel of an MLP's down-projection) with a *dormant* direction (not normally activated but causally potent), making the patch appear to localize a feature to that subspace when in fact it activates a dormant pathway. The phenomenon is demonstrated convincingly in a toy model, GPT-2 Small on the IOI task, and GPT-2 XL on factual recall. The paper also provides a positive case study (faithful subspace in the residual stream), links the illusion to rank-1 weight editing (ROME), and offers prevalence arguments and actionable recommendations.

## Strengths

- **Rigorous mathematical decomposition of the illusion mechanism**: The paper formalizes the illusion as the sum of a causally disconnected direction (in ker W_out) and a dormant direction, with equations (5)–(8) and the derivation of the patched MLP output (Equation 9) providing a transparent algebraic account of how the intervention succeeds despite involving a component provably irrelevant to the model's output.

- **Empirical demonstration on the IOI task with controlled ablation**: Table 1 shows that patching the DAS-found direction v_MLP in MLP8 yields 46.7% FLDD, but its rowspace component alone drops to 13.5% while its nullspace component gives 0.0% — directly confirming that the effect is driven by the causally disconnected part. Figure 3 further shows the patch activates a dormant pathway through the MLP.

- **Contrast with a faithful subspace in the residual stream**: The paper shows that v_resid (found by DAS in the residual stream) does *not* rely on a nullspace component: patching v_resid gives 140.7% FLDD, and its rowspace component alone gives 127.5% — nearly the same effect. The 0.78 cosine similarity to the gradient direction v_grad further validates faithfulness.

- **Formal and empirical linkage between subspace activation patching and rank-1 model editing**: Section 6 shows that rank-1 edits (ROME) are approximately equivalent to 1-dimensional subspace interventions in layers 20–35 of GPT2-XL, with rewrite scores that closely correlate (Figure 7). This provides a mechanistic explanation for prior work (Hase et al., 2023) finding that ROME works even in layers where the fact is not stored.

- **Distilled toy example with full transparency**: The 3-neuron linear network (Figure 2) isolates the illusion in a simple setting where the causally disconnected (h1), dormant (h2), and faithful (h3) directions are explicit and the algebra shows that patching along the sum of h1 and h2 has the same effect as patching along h3.

- **Actionable recommendations for practitioners**: The discussion advises running subspace search in activation bottlenecks (residual stream) rather than inside MLP layers and using validations beyond end-to-end FLDD (e.g., checking that removing the nullspace component does not destroy the effect).

## Weaknesses

### Fatal
None.

### Major
None. The paper's core claims are well-supported by the theoretical framework and empirical evidence. None of the issues below threaten the central contribution.

### Minor
- **Lack of uncertainty quantification across all experiments**: The paper reports FLDD, interchange accuracy, fraction of facts changed, rewrite scores, cosine similarities, and variance ratios without error bars, confidence intervals, or any measure of variability. For Table 1, the differences (e.g., 46.7% vs 13.5%) are large and the qualitative pattern is clear, so this does not undermine the core claim. However, for the factual-recall bar plot and ROME comparisons (Figures 7–10), the absence of spread makes it harder to assess reliability, especially since these data come from multiple edits and layers. Standard errors or bootstrapped intervals would strengthen the presentation.

- **Incomplete reporting of factual-recall experiment details**: Section 5.1 reports a bar plot of "Fraction of facts changed" for three interventions but does not state the number of facts used, the specific per-fact metric (e.g., logit-difference decrease analogous to FLDD), or the variance across facts. The full-MLP intervention is described as having "negligible effect" but exact supporting numbers are not given. While the qualitative pattern is consistent with the IOI findings, the lack of detail makes it harder to evaluate the strength of the illusion in this setting. (Some implementation details likely reside in the appendix, which is stripped by the parser; even so, the main-text presentation would benefit from more quantitative specificity.)

- **Proxy definition for the causally disconnected subspace of the residual stream**: In Section 4.1, the paper uses the nullspace of the stacked query matrices of the three Name Mover heads as a proxy for the causally disconnected subspace of the residual stream. The paper acknowledges this is a proxy (and that using more heads would give a "vacuous" definition), and the nullspace is large (~3/4 of the space). The rowspace intervention still shows a slight drop (140.7% → 127.5%). While the paper partially mitigates this with the gradient-direction comparison, the claim about "strongly causally connected" is somewhat weakened by this proxy choice. This is a genuine limitation of the residual-stream setting, not an oversight.

- **The subspace intervention used to approximate ROME is zero-setting rather than standard activation patching**: The paper acknowledges this departure and argues the same illusion applies. However, no demonstration of the illusion for this zero-setting intervention in the IOI task is provided, which would have tightened the analogy.

### Trivial
None.

## Nice-to-Haves
- Adding error bars to quantitative results (FLDD, rewrite scores, fraction of facts changed) via bootstrapping over examples or edits would increase confidence in the comparisons.
- Reporting the factual-recall experiments with the same level of detail as the IOI experiments (exact numbers, per-fact metrics, variance across facts) would make the generalization claim more solid.
- A brief discussion of whether the illusion could be avoided with more sophisticated subspace interventions (e.g., respecting the model's computational graph) would address a natural reader question.
- Demonstrating the zero-setting subspace intervention for the IOI task would tighten the ROME-to-subspace analogy.

## Removed Points
These points are flagged to be removed — treat them with caution:
- "The paper does not discuss whether the illusion could be avoided by using more sophisticated subspace interventions (e.g., non-linear, or patching along a subspace that respects the model's computational graph)." — This is a nice-to-have suggestion, not a weakness. The paper's scope is to identify and characterize the illusion, not to exhaustively explore every possible mitigation.
- "The connection to copy-suppression or negative heads is mentioned in passing but not explored." — This is a scope observation, not a weakness. Exploring these connections would be a different paper.
- "The paper uses DAS to find subspaces, and shows that it can find both faithful (residual stream) and illusory (MLP) subspaces. This suggests the problem is not with DAS itself but with the location. That is a nice feature of the study." — This is a strength, but it is already covered by Strengths #2 and #3 above more concretely.

## Novel Insights
None beyond the paper's own contributions.

## Suggestions
- Add bootstrapped error bars or confidence intervals to all quantitative results (FLDD, rewrite scores, fraction of facts changed, variance ratios) to give readers a clearer sense of reliability.
- In the factual-recall section (Section 5), report the exact number of facts, the mean logit-difference decrease (or analogous metric) per intervention, and the standard deviation across facts to match the level of detail in the IOI section.
- Consider an alternative validation for the residual-stream "causally disconnected" subspace: compute the subspace that is least correlated with the model's logit difference for the IOI vs. S prediction, rather than relying solely on the Name Mover query matrices.
- Explicitly note in Section 4.1 that the residual-stream nullspace definition is a rougher proxy than the MLP kernel definition, and that the real evidence for faithfulness comes primarily from the gradient-direction similarity and the near-equivalence of the full and rowspace patches.

## Score and Decision

This paper makes a clear, novel, and important contribution to the mechanistic interpretability community. It identifies a concrete mechanism by which subspace activation patching can produce misleading results, demonstrates it across multiple settings, provides a counterexample of a faithful subspace, and links the finding to rank-1 model editing — offering an explanation for previously puzzling observations in the literature. The theoretical framing is rigorous, the experimental evidence is sufficient to support the core claims, and the presentation is clear and well-structured. The weaknesses identified are all minor or addressable and do not threaten the paper's central thesis.

MY FINAL SCORE: <pineapple>7.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>