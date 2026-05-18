Now I have enough calibration data. Let me write the final consolidated review.

## Summary

This paper trains Sparse Autoencoders (SAEs) on attention layer outputs (the pre-projection z-vectors) of transformers, demonstrating that these "Attention Output SAEs" produce sparse, faithful, and interpretable feature decompositions. The authors introduce weight-based head attribution, which allows features extracted from a layer-level SAE to be attributed to individual attention heads. Using this tool, they survey all 144 heads in GPT-2 Small, estimate polysemanticity prevalence, and make two novel empirical discoveries: (1) the resolution of seemingly redundant induction heads into long-prefix vs. short-prefix specialists, and (2) the identification of an "and"-token-based positional signal in the IOI circuit, causally validated via noising experiments. The paper also introduces Recursive Direct Feature Attribution (RDFA) and releases a tool for it.

## Strengths

1. **Weight-based head attribution is a novel and practically useful technique.** By splitting each SAE feature direction into per-head vector norms (Section 2, Equation 3), the method enables per-head analysis without training per-head SAEs. This cleanly bridges layer-level SAEs and head-level analysis, and is deployed effectively throughout the paper.

2. **Discovery of long-prefix vs. short-prefix induction specialization (Section 4.2) is a concrete advance over prior understanding.** The paper uses SAE features to hypothesize that head 5.1 specializes in long-prefix induction while 5.5 does short-prefix induction, then independently confirms this with synthetic data experiments (Figure 4a) and intervention experiments on real examples (Figure 4b). This resolves part of the open question about why models have many seemingly redundant induction heads.

3. **Causal identification of the "and"-based positional signal in the IOI circuit (Section 4.3) goes beyond prior head-level analysis.** The noising experiment (Figure 6) showing that preserving the "and"-relative position recovers 93% of logit difference while corrupting only "and" recovers only 43% is a clean, non-SAE validation that SAE features have pointed to a causally meaningful intermediate variable. This resolves a mystery left open by Wang et al. (2023).

4. **SAEs are evaluated systematically across multiple models and up to 2B parameters (Table 1).** The evaluation uses standard metrics (L0, loss recovered, interpretability) and shows that Attention Output SAEs achieve favorable numbers across GPT-2 Small, Gemma-2B, and GELU-2L. The release of trained SAEs and feature dashboards is a practical contribution to the community.

5. **The catalog of head motifs across all 144 GPT-2 Small heads (Section 4.1) is a useful reference,** identifying extant motifs (induction, successor, previous-token, duplicate-token heads) and discovering novel ones (preposition mover heads).

## Weaknesses

### Major

1. **The "at least 90% of heads are polysemantic" claim (Section 4.1.1, Abstract) is not well-supported by the evidence presented.** The estimate derives from classifying heads based on whether the *top-10* attributed features are "closely related" (14 monosemantic candidates out of 144 → ~90% polysemantic). This has multiple issues: (a) using only the top-10 features means a head could have many additional unrelated features beyond the top-10, making the estimate potentially an *underestimate* of polysemanticity — or, if the top-10's relatedness is judged too leniently, an *overestimate*; (b) "closely related" is a subjective binary classification made by the authors with no systematic protocol, inter-rater reliability check, or quantitative similarity metric; (c) the validation on head 10.2 (Figure 3) is convincing for that one head but does not calibrate the method across the full head set. The paper's core contributions (induction specialization, IOI analysis) do not depend on this number. The claim should be replaced with a qualitative statement ("many heads appear polysemantic, with a small minority appearing monosemantic based on their top features") or supported with a more rigorous evaluation.

2. **RDFA (Recursive Direct Feature Attribution) is introduced as a contribution but never used to obtain a result in the paper.** Section 2 describes RDFA and the authors release a visualization tool, yet the long-prefix induction analysis uses synthetic data + interventions, the IOI analysis uses zero-ablation + noising, and the head survey uses weight-based head attribution. RDFA is not applied to discover or confirm any finding. A method that is presented but not exercised feels like an incomplete contribution. Either a brief demonstration (e.g., showing RDFA recovering a known attention-to-attention circuit on a simple example) would justify its inclusion, or its prominence should be reduced.

### Minor

1. **The interpretability percentages in Table 1 are based on a sample of 30 features per layer.** For a dictionary of thousands of features (4×d_model ≈ 3,000 for GPT-2 Small), 30 features is <1% of the dictionary. The paper acknowledges this and references confidence intervals in the appendix. This does not threaten the paper's core claims (the qualitative case studies are more convincing evidence of interpretability), but the headline ">80% interpretable" claim should be presented with appropriate hedging rather than as a definitive quantitative result.

2. **The noising experiment in Section 4.3 lacks experimental detail and error bars.** The main text describes the noising setup briefly and cites heimersheim2024activation for the definition, but does not state the number of prompts used, whether the 93%/43% figures are averages with associated variance, or how many random seeds/trials were run. The description "noising from a distribution that just changes 'and' to 'alongside'" is ambiguous — it is unclear whether the model is re-run on a perturbed prompt or whether activations from a perturbed distribution are patched in. This needs clarification for reproducibility.

3. **The long-prefix induction plots (Figures 4a, 4b) do not show error bars or sample size information.** The paper does not state how many prompts were used in the synthetic data experiment or in the intervention on real examples. Reporting variability (e.g., confidence intervals across prompts) would make the results more convincing.

4. **The claim that induction features are "unique to attention" (Section 3.3) is stated as a hypothesis but could be read as a stronger claim.** The paper says "As we are not aware of any induction features extracted by MLP SAEs in prior work, we hypothesize that induction features are unique to attention," which is appropriately hedged. However, the surrounding prose could mislead readers into thinking this is an established finding. Clarifying that this remains unproven (MLP SAEs from prior work might find them with different methods) would be helpful.

### Trivial

None.

## Nice-to-Haves

- Apply RDFA to at least one simple case study (e.g., tracing a single feature's upstream attention inputs) to demonstrate its utility.
- Check whether other induction heads beyond 5.1 and 5.5 show the long-prefix/short-prefix distribution pattern.
- Test the "and" token hypothesis with alternative conjunctions (e.g., "or") to test generalization.
- Quantify SAE faithfulness on the IOI distribution (loss-recovered on IOI prompts) in the main text rather than deferring to the appendix.

## Removed Points

- **Criticism that the 90% claim "extrapolates from one head"** — The critic wrote "extrapolating from one head to claim a 90% rate across 144 heads is an enormous leap." This misreads the paper: the 90% figure comes from classifying all 144 heads (14 monosemantic candidates among them), not from extrapolating from head 10.2 alone. The head 10.2 validation is a separate sanity check. Removed due to factual inaccuracy.
- **Strength Finder's claim about RDFA enabling "prompt-level analysis not previously possible"** — Since RDFA is not used in any experiment, claiming this as a demonstrated strength overstates its validation. Moved here from Strengths.
- **Strength Finder's "systematic interpretation of all 144 attention heads... The 90% polysemanticity estimate is supported by a hand-inspection protocol"** — Since the 90% claim is a major weakness, this strength conflicts with a verified weakness. Moved here.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. **Deprecate the quantitative "≥90% polysemantic" claim.** Replace it with a qualitative statement: "We found evidence of polysemanticity in most heads; based on their top-10 attributed features, only 14/144 heads appeared potentially monosemantic." This is honest, accurate, and does not weaken the paper.

2. **Add a brief RDFA demonstration.** Show RDFA tracing a single SAE feature's upstream attention contributions on a short prompt. Even a small example would move RDFA from "untested proposal" to "working method with a demonstrated use case."

3. **Report sample sizes and error bars for Figures 4 and 6.** State the number of prompts and show bootstrap confidence intervals or standard deviations across prompts.

4. **Clarify the noising experiment description in Section 4.3.** Specify: "We replace the attention output activation at position S2 in layers 5 and 6 with an activation drawn from a forward pass on a perturbed prompt. The perturbed prompt is constructed by [explicit recipe]. Results are averaged over N prompts."

## Score and Decision

**Calibration anchors:**

| Path | Avg Score | Comparison |
|------|-----------|------------|
| `/home/wg25r/split_review/datasets/deepreview_13k_calibration/tcsZt9ZNKD.md` | 8.20 | Scaling & Evaluating SAEs — stronger methodological contribution (TopK, scaling laws, GPT-4 scale). Present paper has more empirical discoveries but weaker methodology. |
| `/home/wg25r/split_review/datasets/deepreview_13k_calibration/9ca9eHNrdH.md` | 7.00 | SAEs Do Not Find Canonical Units — cleaner claims, novel methods (stitching, meta-SAEs). Present paper has more interesting empirical findings but overclaims in spots. |
| `/home/wg25r/split_review/datasets/deepreview_13k_calibration/SUc1UOWndp.md` | 7.00 | Differentiation of Attention Heads via rLLC — solid theoretical contribution with cleaner execution. Present paper is slightly weaker due to overclaimed polysemanticity number. |
| `/home/wg25r/split_review/datasets/deepreview_13k_calibration/F76bwRSLeK.md` | 4.80 | SAEs Find Highly Interpretable Features — earlier, less rigorous SAE paper. Present paper is substantially stronger (more causal validation, more discoveries). |
| `/home/wg25r/split_review/datasets/deepreview_13k_calibration/sknUS8X9q0.md` | 4.00 | SAGE evaluation framework — unclear contributions, poor presentation. Present paper is much clearer and has more concrete findings. |
| `/home/wg25r/split_review/datasets/deepreview_13k_calibration/5IZfo98rqr.md` | 3.50 | Dark Matter of SAEs — important topic but hard to follow. Present paper is clearer and has stronger empirical contributions. |

The paper makes genuine contributions (induction specialization, IOI "and" signal, weight-based attribution) and is clearly written. However, the overclaimed polysemanticity number and the dangling RDFA contribution prevent it from reaching the upper tier. It is substantially stronger than the 4.80 and below anchors. Balanced against the ~7.0 anchors, it is comparable in overall value but has more significant overclaiming issues. A score of 6.0 reflects solid contributions tempered by these weaknesses.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>