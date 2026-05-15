Now I have thoroughly analyzed the paper and all reviewer claims. Let me produce the final consolidated review.

## Summary

LiNeS is a post-training technique that linearly scales parameter updates (task vectors) with layer depth—preserving shallow-layer changes close to pre-trained values while allowing deeper-layer changes to remain. The method is motivated by the well-supported observation that shallow-layer updates minimally impact target-task accuracy but cause most of the zero-shot generalization loss. LiNeS is applied as a plug-in on top of existing model merging pipelines (Task Arithmetic, Ties-Merging, Consensus Merging) and also applied to robust fine-tuning, model soups, and RLHF policy merging. The strongest evidence is in multi-task vision merging, where LiNeS yields consistent +2–4% gains across architectures and task-set sizes. The method is simple, has only one or two hyperparameters, and requires no additional training.

## Strengths

- **Simple, well-motivated, and broadly applicable post-training technique.** The paper cleanly demonstrates (Section 3) that shallow-layer updates are the primary driver of catastrophic forgetting while being largely unnecessary for target-task accuracy—an empirical finding that is independently useful. LiNeS operationalizes this insight with a single linear scaling schedule and integrates with existing merging pipelines in one line of code, requiring no re-training.

- **Consistent and meaningful gains in multi-task vision merging.** Across 3 vision architectures (ViT-B/32, ViT-B/16, ViT-L/14), 3 task-set sizes (8, 14, 20 tasks), and 3 baseline merging methods (Task Arithmetic, Ties-Merging, Consensus Merging), LiNeS improves every combination (Table 1). Gains range from +2.1% to +4.5%, which are meaningful for multi-task merging where even 1% improvements are nontrivial (e.g., +4.0% for Ties-Merging on 20 tasks with ViT-L/14).

- **Generality across diverse post-training scenarios.** Beyond multi-task merging, LiNeS produces a dominating Pareto front for robust fine-tuning (WiseFT, Figure 2) over 5 OOD datasets, improves model soups (Table 4), and Pareto-dominates rewarded soups for merging LLM policies (Figure 3). This breadth is rare for such a simple method.

- **Computationally negligible compared to training-based alternatives.** Unlike Ada-merging and aTLAS, which require multiple training epochs and storing all checkpoints, LiNeS is a single-pass post-training scaling. The paper shows LiNeS achieves scaling profiles close to those learned by these methods (Figure 3), underscoring the value of the inductive bias.

## Weaknesses

### Fatal

None.

### Major

- **Missing ablation: uniform scaling vs. depth-dependent scaling.** The paper's core claim is that the *depth-dependent* aspect of LiNeS drives improvement. However, no experiment compares LiNeS (varying scaling across layers) against uniform scaling (α = β, constant λ across all layers). Without this ablation, the improvement could partly come from global regularization (reducing overall task-vector magnitude) rather than the depth-specific element. This is the single most important missing experiment: it is needed to support the claimed mechanism, and it is straightforward to run.

- **NLP results partially undermine the claim of "consistent improvements with notable margins."** Several NLP entries in Table 2 are near-zero: Ties-Merging + LiNeS on 7 NLP tasks improves only +0.4%, and Consensus Merging + LiNeS on 11 NLP tasks gives exactly 0.0% improvement. The paper's language ("notable margin," line 226) overstates these results. While the vision results are strong, the NLP evidence does not support the claim that LiNeS "consistently" improves with notable margins, and the 0.0% case directly contradicts it.

### Minor

- **Single-task forgetting mitigation evaluated under an oracle protocol.** In Section 3, LiNeS selects γ using validation accuracy on control tasks (the 7 or 19 tasks the model will be tested on). This assumes knowledge of the test distribution during hyperparameter selection — unrealistic for practical deployment. The headline 97.9% control-task normalized accuracy is therefore an upper bound under oracle conditions. The paper does not report performance under more practical selection criteria (e.g., tuning γ on a small general-domain set or using a fixed default). This does not invalidate the phenomenon but limits the strength of the practical claim.

- **Rewarded soups experiment (Section 5.4) uses α=β=1, which applies no downscaling to shallow layers (scale 1) and amplifies deep layers (scale up to 2).** The paper explains this as "for computational reasons" without elaboration. This setting does not follow the paper's motivating story of downscaling shallow layers—it preserves shallow layers at their merged value and amplifies deep ones. While the relative principle (shallow < deep) is maintained, the mechanism differs from the rest of the paper. The lack of either properly tuned hyperparameters or a clearer justification weakens the otherwise interesting result.

- **Model soups gains are tiny (0.48% for uniform, 0.15% for greedy) without reported variance or statistical significance.** Given that the greedy soup baseline already selects the best ordering on a validation set, a +0.15% gain is likely within noise. The paper should at minimum report standard deviations or confidence intervals for these results.

- **α heuristic in Equation 2 is presented without justification or ablation.** The choice α = (1/num_models) × (||τ_sum|| / ||τ_MTL||) is motivated heuristically but not ablated — e.g., what happens if α is fixed to a constant like 0.1 or 0.5 across all settings? Since only β is tuned, the sensitivity to the α heuristic is relevant for understanding robustness and reproducibility.

- **The paper does not discuss limitations.** There is no section or paragraph on when LiNeS might fail, how results depend on validation splits, or practical constraints on tuning α/β across different settings. This is standard practice for mature submissions and should be added.

### Trivial

None — the paper is generally well-written and free of significant presentation issues.

## Nice-to-Haves

- An experiment applying LiNeS to individual task vectors *before* merging (vs. only the merged vector reported in the paper). The paper acknowledges this as an alternative but does not compare. This would help isolate whether the benefit comes from pre-task regularization or post-merger interference reduction.

- Per-task breakdown of multi-task merging results (vision and NLP), especially to identify cases where LiNeS hurts individual tasks while improving the average.

- A recommended default setting for α/β that works reasonably without validation data, making LiNeS truly plug-and-play.

## Removed Points

These points are flagged to be removed, treat them with caution:

- **Criticism that LiNeS could simply be acting as a global regularizer, not depth-specific, without acknowledging** that the paper does include a clear demonstration (Figure 1) that shallow downscaling outperforms deep downscaling. However, the missing uniform-scaling ablation (kept as a Major weakness above) is the proper way to address this, not the reviewer's speculative phrasing. The criticism is retained in a more constructive form as the missing ablation.

- **"Comparison with Ada-merging and aTLAS — if the optimal scaling is learned to be similar to LiNeS, why not just use the learners?"** The paper directly addresses this by noting LiNeS achieves similar profiles without training. The comparison (Section 6) is a strength, not a weakness.

- **The claim that Section 2's statement about computational cost is "not quantified."** The claim that modifying fine-tuning is "orders of magnitude more computationally expensive" is a qualitative comparison that is clearly true for large-scale settings. This is a generic complaint that does not harm the paper.

- **"Figure 1 shows that even deep-layer downscaling improves control-task performance"** — the paper does not claim deep downscaling doesn't help, only that shallow downscaling helps *more*, which the figure clearly shows. This is a correct reading of the paper, not a flaw.

- **"No statistical significance for model soups"** — retained as Minor (not removed), but softened relative to the reviewer's tone since single-run evaluation on standard benchmarks is the norm for this setting.

## Novel Insights

None beyond the paper's own contributions. The key insight — shallow-layer updates cause forgetting and can be aggressively downscaled post-training — is empirically demonstrated and operationally applied. The reviewer criticisms largely concern missing controls and overclaims rather than uncovering new phenomena.

## Suggestions

1. **Add the uniform-scaling ablation.** Compare LiNeS (α=γ, β=1-γ) against uniform scaling (α = c, β = 0) with c matched to produce the same average scaling magnitude. If LiNeS outperforms uniform scaling, the depth-dependent mechanism is supported. This should be done for both the single-task forgetting experiment (Section 3) and the multi-task vision merging (Section 5.2), as it is the central mechanistic claim.

2. **Tone down the NLP claims.** Replace "notable margin" (line 226) with a more measured statement that acknowledges the near-zero gains for Ties+LiNeS on 7 tasks (+0.4%) and Consensus+LiNeS on 11 tasks (0.0%). The vision results alone are strong enough to support the paper's contribution.

3. **Acknowledge the oracle tuning protocol in Section 3.** Add a sentence clarifying that γ is selected on held-out control-task data, and discuss how LiNeS might be used in practice when the test distribution is unknown (e.g., default γ or tuning on a general-domain set).

4. **Explain or fix the Rewarded Soups α=β=1 choice.** Either tune β properly and report results, or provide a clear analytic justification for why α=β=1 is the correct setting in this scenario despite differing from the paper's main motivation.

5. **Add a limitations paragraph.** Discuss: (a) when LiNeS might degrade individual task performance while improving averages, (b) sensitivity to validation splits, (c) the cost of tuning β, (d) the limitations of the linear scaling assumption.

## Score and Decision

This paper presents a simple, well-motivated post-training technique with strong vision multi-task merging results. The method is practical and easy to adopt. However, the missing uniform-scaling ablation leaves the claimed mechanism partially unsupported, the NLP results are weaker than the paper's rhetoric suggests, and the rewarded-soup hyperparameter choice is unexplained. These issues are addressable in revision but reduce confidence in the paper's strongest claims. I rate this as a solid empirical contribution with room for improvement.

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>