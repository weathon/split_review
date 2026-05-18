I now have a thorough understanding of the paper and have verified all the reviewer claims against the actual paper text. Let me produce the final consolidated review.

## Summary

This paper presents a comprehensive empirical study of activation sparsity scaling in decoder-only Transformer-based LLMs. It proposes a new metric (PPL-p% sparsity) that links sparsity to a controllable level of perplexity degradation, then uses it to study how sparsity scales with training data amount, activation function (ReLU vs SiLU), width-depth ratio, and parameter scale. The main findings are: (1) ReLU and SiLU exhibit opposite sparsity trends with training data (decreasing vs increasing activation ratio), both converging to limits; (2) deeper architectures yield higher sparsity up to a bottleneck point; (3) the limit activation sparsity is surprisingly insensitive to parameter scale when width-depth ratios are similar.

## Strengths

1. **Novel performance-aware sparsity metric (PPL-p%)**: The paper proposes a principled metric that ties activation sparsity directly to a controllable perplexity increase, overcoming the inflexibility of global thresholds and the non-performance-awareness of CETT. Section 3.1 defines the binary-search procedure over CETT values, and Figure 3 demonstrates that PPL-p% achieves a better PPL-sparsity trade-off compared to Straightforward ReLU, Top-k, and FAT-ϵ baselines across model scales. This is a genuine methodological contribution.

2. **First quantitative scaling laws for activation sparsity with training data**: The paper discovers that ReLU LLMs follow a decreasing logspace power-law (Eq. 4) and SiLU LLMs follow an increasing power-law (Eq. 5) for activation ratio vs. training tokens, both convergent. Figure 4 shows fitted curves across five model scales (0.1B–1.2B). These laws are novel and enable training-time prediction of sparsity.

3. **Identification of architectural shape as a decisive sparsity factor**: The paper demonstrates that the width-depth ratio linearly affects activation ratio below a bottleneck point (~114 for 0.1B), providing actionable guidance for designing sparser architectures. The joint analysis with performance (Figure 6) identifies an optimal interval [74, 282].

4. **Weak dependence of limit sparsity on parameter scale**: The paper shows that limit activation ratios vary by ≤2.7 percentage points across model scales (0.1B–1.2B) when width-depth ratios are similar (Figure 7), and provides evidence (Figures 9–10) and a combinatorial specialization argument (Eq. 6) explaining why smaller models converge faster. This is a non-obvious finding with implications for scaling.

## Weaknesses

### Fatal
None.

### Major

1. **The claim that ReLU and SiLU achieve "comparable performance" is asserted without supporting evidence.** The abstract (line 4), Section 1 (line 25), and Section 4.2 (line 134) all state that ReLU and SiLU exhibit "comparable performance." However, the paper provides **no direct side-by-side comparison** — no table of validation loss, perplexity, or downstream task scores for ReLU vs. SiLU models at matched scales. Table 1 reports downstream scores for different p% values but without specifying the activation function used, and it is about validating the PPL-p% metric, not comparing activation functions. Figure 4 only compares sparsity curves, not performance. The training loss curves (referenced as Figure 11) are mentioned but not explicitly connected to a ReLU vs. SiLU comparison. Since the paper's practical recommendation to "replace SiLU with ReLU" (Section 5) critically depends on performance being undegraded, the absence of this comparison is a significant evidentiary gap. The authors should either provide the comparison, or qualify the claim substantially.

2. **The fitted scaling laws lack validation diagnostics.** Equations (4) and (5) were selected "after careful attempts" (line 113), but the paper reports no goodness-of-fit metrics (R², RMSE), confidence intervals on the fitted parameters (A₀, c, α), or any holdout evaluation (e.g., fitting on early checkpoints and extrapolating to later ones). The number of checkpoint data points per model is not stated. The ReLU form — an exponential of a power-law — is atypical and could be overparameterized. Given that these fitted laws and their parameters (especially A₀) are central to the paper's conclusions about sparsity limits and convergence, the lack of fit validation is a notable methodological gap.

### Minor

3. **Hyperparameter fairness of the ReLU vs. SiLU comparison is unclear.** The paper follows the "optimal batch sizes, optimal learning rates, and the WSD learning rate scheduler of MiniCPM" (line 81), which uses SiLU. No hyperparameter search is reported for ReLU models. Activation-function switches can benefit from different learning rates or initialization schemes. This does not invalidate the results, but the paper should acknowledge this caveat and ideally include a small-scale sensitivity check.

4. **PPL-p% metric stability is not examined.** The metric involves a binary search over CETT values based on a target PPL increase on a validation set. The paper defaults to p=1% but does not examine sensitivity to the choice of validation subset or how rankings change when p varies (only downstream degradation is shown in Table 1 for a few p values on one model configuration).

5. **Width-depth study is limited to one scale (0.1B) and one activation function (ReLU).** The bottleneck point (~114) and optimal interval [74, 282] are therefore specific to this setting. The paper partially acknowledges this limitation (line 138), but the generality of the architectural recommendations would benefit from confirmation at larger scales or with SiLU.

6. **The convergence-speed explanation (combinatorial argument) is intuitive but not directly tested.** Equation (6) counts specialization assignments but does not formally connect this combinatorial count to optimization difficulty. The link between assignment count and convergence speed during SGD is asserted, not derived or empirically verified.

### Trivial

7. **The width-depth ratio values for each scale in Section 4.4 are described only as "similar"** (line 211) without being explicitly listed, making the claim difficult to verify.

## Nice-to-Haves
- A small learning-rate sweep (±1 order of magnitude) at the 0.1B scale for ReLU to check whether sparsity dynamics or loss change appreciably.
- Reporting how PPL-p% sparsity varies when using different validation subsets or varying p from 0.5% to 2%.
- A discussion of whether the sparsity scaling laws might generalize to architectures beyond the MiniCPM family.

## Removed Points
- Criticisms about missing evaluation methodology details (benchmark specifics, few-shot settings) — these details could reside in a stripped appendix. By the instructions, parser-stripped content is not an author error.
- The suggestion to discuss whether sparsity scaling laws hold for other architectures — this is scope creep beyond the paper's stated scope.
- Criticisms about the number of checkpoint evaluations not being stated — this level of implementation detail is typical for an appendix.
- Several picky formatting/style nitpicks from the harsh critic that were not reproduced here per the filtering rules.

## Novel Insights

The most interesting insight is that activation sparsity trends with training data are **opposite** for ReLU and SiLU despite both being widely used activation functions — SiLU becomes *less* sparse with more data while ReLU becomes *more* sparse. The finding that limit sparsity is nearly scale-invariant (varying by ≤2.7 percentage points across 0.1B–1.2B) when width-depth ratios are matched is a genuinely non-obvious result. If validated at larger scales, this would imply that architectural choices (activation function, depth/width ratio) dominate over parameter count in determining achievable sparsity.

## Suggestions

1. **Most important: Provide direct evidence for the "comparable performance" claim.** Add a table showing validation perplexity and/or downstream benchmark scores for ReLU vs. SiLU models at matched scales (at least 0.1B, 0.4B, and 1.2B). If the claim cannot be supported, it should be substantially softened with a discussion of the performance-sparsity trade-off.
2. **Add fit diagnostics for the scaling laws:** Report R² or RMSE for each fitted curve, and ideally test predictive power by fitting on early checkpoints and extrapolating.
3. **Acknowledge the hyperparameter limitation** and add a small-scale learning rate ablation for ReLU.
4. **Explicitly list the width-depth ratios** used in the scale experiments (Section 4.4).

## Score and Decision

MY FINAL SCORE: <pineapple>5.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>