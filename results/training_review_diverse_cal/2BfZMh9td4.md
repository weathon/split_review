Now I have a thorough understanding of the paper. Let me produce the final consolidated review.

## Summary

This paper introduces Multi-Objective Direct Preference Optimization (MODPO), an RL-free extension of DPO that handles multiple alignment objectives by integrating linear scalarization into the reward modeling step. MODPO derives a DPO-style loss that incorporates margin reward models for non-primary objectives, producing policies that are theoretically equivalent to those from MORLHF while requiring only a simple cross-entropy loss. Empirically, MODPO matches or outperforms MORLHF across safety alignment and long-form QA tasks with approximately 3× less per-LM computation.

## Strengths

1. **Clean theoretical derivation connecting MODPO to the MORLHF objective.** The paper provides a rigorous derivation (Section 3.1, Eq. 10–14) showing that optimizing the MODPO loss recovers the optimal policy for the KL-constrained scalarized reward objective — the same target as MORLHF. This establishes that MODPO is not a heuristic approximation but an exact alternative under the assumption of known margin rewards.

2. **Consistent empirical superiority or parity with MORLHF at lower cost.** Across both synthetic and real-feedback settings for safety alignment (Figures 2, 4) and long-form QA (Figure 3), MODPO produces Pareto fronts that match or dominate MORLHF. Table 1 confirms a 3× reduction in per-LM GPU hours (~6 vs. ~18), directly supporting the paper's central efficiency claim.

3. **Evaluation across diverse tasks and objective types.** MODPO is validated on two tasks (safety alignment with BEAVERTAILS, long-form QA with QA-FEEDBACK) covering four distinct objective pairs, including both preference-only and mixed (preference + meta-labeled) feedback settings. This breadth supports the claim of broad applicability to real-world multi-dimensional feedback pipelines.

4. **Minimal overhead over single-objective DPO.** The MODPO loss (Eq. 14) differs from the standard DPO loss only by a scalar weighting \(1/w_k\) and a pre-computed margin term from the fitted margin reward model. This keeps the per-LM training pipeline simple, stable, and comparable in cost to single-objective DPO.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

1. **Unspecified reward model training procedure for meta-labeled (non-preference) data.** The paper states (line 160) that margin reward models are trained "with MLE on their corresponding datasets." For preference datasets this is clear (Eq. 3), but for the long-form QA setting, the meta datasets $\{\mathcal{D}_{\mathrm{rel}},\mathcal{D}_{\mathrm{fact}},\mathcal{D}_{\mathrm{comp}}\}$ are described as having "meta labels of fine-grained errors" — it is not specified whether these are scalar ratings, binary indicators, or something else, and how the MLE procedure (Eq. 3, which requires pairwise comparisons) is applied to them. The paper says "rewards can be defined" (line 187) but does not state the actual training objective. This does not affect the core methodological contribution (the MODPO loss derivation is agnostic to how margin rewards are obtained), but it is a reproducibility gap for the long-form QA experiments. Adding one paragraph clarifying how each meta dataset yields a trained reward model (e.g., constructed pairwise preferences, regression loss, or direct use of scores) would resolve this.

2. **Long-form QA evaluation uses the same learned reward models for both training and evaluation, introducing potential bias.** The paper acknowledges this ("This may lead to biased evaluation," line 200) and mitigates with a larger $\beta=0.5$, but the concern remains that the evaluation rewards may favor methods whose training signal is more aligned with those same metrics. The safety alignment experiments use GPT-3/4 as an independent evaluator (Figure 4), which avoids this issue — the absence of an analogous independent evaluation for long-form QA weakens the evidence for that task somewhat. The core results (safety alignment) are not affected.

3. **No analysis of sensitivity to margin reward model approximation error.** The theoretical equivalence (Section 3.1) assumes exact margin rewards $r_{-k}^*$, but the practical method substitutes estimated models $r_{\phi,-k}$. While this is the same limitation faced by MORLHF (which also uses estimated reward models), the paper does not discuss whether MODPO's sensitivity to reward model errors differs from MORLHF's, nor does it provide experimental analysis (e.g., varying reward model quality). This is a standard omission in reward-model-based alignment papers, but noting it would strengthen the paper's rigor.

### Trivial
None.

## Nice-to-Haves

- **Total amortized cost comparison.** The paper's 3× claim is for per-LM training (stage 2) after reward models are trained. Since both MODPO and MORLHF require upfront reward model training (1 model for MODPO, 2 for MORLHF), the total cost comparison across a full Pareto front would be informative context. The conclusion would still favor MODPO, but including these numbers would be more complete.

- **Acknowledgment of linear scalarization's convex Pareto front limitation.** Linear scalarization can only recover Pareto-optimal points on convex regions of the Pareto front. Since MODPO inherits this property (as does MORLHF, which the paper compares against), this is not a weakness relative to baselines, but acknowledging it as a scope condition would be appropriate.

## Removed Points
These points are flagged to be removed; treat them with caution.

- The harsh critic's framing of Issue 1 as a "structural gap that undermines the paper's claimed generality" is too strong. The missing detail affects only one experiment setting (long-form QA), not the core methodology. The safety alignment experiments (which comprise half the results) use preference datasets where the training procedure is fully specified (Eq. 3). The paper's claim about generality — that it can leverage "off-the-shelf multi-dimensional feedback" — is supported by the method's architecture, which separates margin reward acquisition from the MODPO loss. The missing detail is a clarity issue, not a structural gap in the approach.

- The critic's claim that the long-form QA evaluation is "potentially circular" in a way that favors MODPO over MORLHF overlooks that MODPO only uses $r_{\phi,1}$ as a *margin* (difference between two responses) in its loss, while MORLHF uses both $r_{\phi,1}$ and $r_{\phi,2}$ directly in its RL objective. If anything, MORLHF has more exposure to the evaluation metrics during training. The concern is acknowledged and partially addressed by the paper with a larger $\beta$.

- The critic's suggestion that the synthetic feedback experiment "has limited external validity" because ground-truth rewards are learned models is a feature of the controlled evaluation setup, not a flaw — this is standard practice following Rafailov et al. (2023) and serves to isolate the method comparison from confounding factors in human annotation.

## Novel Insights
None beyond the paper's own contributions.

## Suggestions

1. Add a short paragraph (or appendix note) specifying exactly how margin reward models are trained from the meta datasets in the QA-FEEDBACK setup — e.g., whether meta labels are scalar scores converted to preferences via pairwise comparison, or whether a regression-based reward model is used. This would resolve the main reproducibility concern.

2. Provide an independent evaluation for the long-form QA task (even a small-scale GPT evaluation, as done for safety alignment) to eliminate the bias concern, or explicitly compare the two methods using only held-out reward models trained on disjoint data splits.

3. Include a brief discussion or simple experiment analyzing sensitivity to margin reward model quality — e.g., how does MODPO's performance degrade when margin rewards are trained on smaller subsets of data?

## Score and Decision

**Originality**: Good. Extending DPO to the multi-objective setting via early integration of linear scalarization is a clean and non-trivial contribution.

**Importance of research question**: High. Customizing LMs to diverse human preferences is practically important as alignment becomes more widespread.

**Claims well-supported**: Mostly yes. The theoretical derivation is sound, and the empirical results consistently support the claimed advantages. Minor clarity gaps in experimental specification do not undermine the core claims.

**Soundness of experiments**: Good. The controlled synthetic setting and real-feedback experiments with multiple objective pairs provide solid evidence. The long-form QA evaluation has acknowledged limitations but the overall picture is consistent.

**Clarity**: Good. The paper is well-structured and the derivations are clearly presented. The main weakness is the underspecified reward training procedure for meta datasets.

**Value to community**: High. MODPO provides a practical, efficient, RL-free alternative to MORLHF that can be adopted by practitioners working with multi-dimensional feedback.

MY FINAL SCORE: <pineapple>7.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>