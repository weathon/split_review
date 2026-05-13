Now I have a thorough understanding of the paper. Let me synthesize my final review.

## Summary

This paper investigates whether RNNs and INNs can logically extrapolate—i.e., solve harder instances of a task after being trained on easy ones—in the context of maze solving. It introduces two new axes of difficulty beyond maze size: `deadend_start` (whether the start position has degree 1) and percolation (which introduces cycles into mazes). The authors evaluate two pretrained models (DT-Net, an RNN; PI-Net, an INN) and find that while both extrapolate well along the size axis, they fail along both new axes. A second contribution uses topological data analysis (TDA) to characterize latent dynamics, showing that DT-Net exhibits limit cycles (two-point and two-loop) rather than fixed points, while PI-Net always converges to fixed points.

## Strengths

- **The deadend_start experiment is a genuinely novel and well-defined test of out-of-distribution generalization.** DT-Net accuracy drops from 1.00 to 0.72 on 9×9 mazes when `deadend_start=False`, and the monotonic decrease with start-position degree (Figure 4) is a clean, interpretable finding that directly challenges prior claims about robust logical extrapolation.

- **The TDA framework for characterizing limiting behavior is a principled and novel methodological contribution.** Using Betti numbers [B₀, B₁] to quantitatively classify latent dynamics as fixed points [1,0], two-point cycles [2,0], or two-loop cycles [2,2] provides a systematic vocabulary beyond binary "converges or doesn't." The discovery that DT-Net predominantly exhibits two-point cycles across all maze sizes is a genuine empirical finding.

- **The paper is commendably transparent about PI-Net's performance degradation on larger mazes and the ill-posed nature of the percolation task.** The discussion explicitly acknowledges that percolation makes the task "ill-posed" (Section 4, paragraph 1) and that PI-Net's diminished performance on larger mazes does not contradict prior work.

- **The finding that DT-Net can correctly solve mazes while exhibiting limit cycles rather than fixed points is interesting and challenges prior assumptions.** Figure 7 explicitly labels both the two-point cycle and two-loop cycle examples as "Both mazes were solved correctly," providing direct evidence that non-fixed-point dynamics are compatible with correct solutions.

## Weaknesses

### Major

- **The percolation axis conflates a task specification failure with a generalization failure, yet is presented as co-equal evidence for extrapolation failure.** When `p > 0`, mazes contain cycles and have no unique solution path, yet models were trained to find unique paths. The paper acknowledges this in the Discussion ("the task, as framed by the training data given to the model, ill-posed"), but the abstract, introduction, and conclusion all present percolation alongside `deadend_start` as evidence that models "fail to generalize along axes of difficulty other than maze size." This framing overstates the generality of the finding: percolation reveals that the task becomes ill-defined, not that the model fails to extrapolate. The `deadend_start` finding is far more compelling because the task remains well-defined, and the paper would be stronger if it clearly separated these two fundamentally different phenomena rather than grouping them together as equivalent demonstration of the same claim.

- **Claims about RNN and INN architecture classes rest on a single trained model per class.** The abstract states "models that are explicitly trained to converge to a fixed point (e.g. the INN we test) are likely to do so when extrapolating, while models that are not (e.g. the RNN we test) may exhibit more exotic limiting behaviour." But only one trained model per architecture type is evaluated (DT-Net and PI-Net), and the dynamic behaviors (two-point cycles, two-loop cycles) could be artifacts of specific training procedures (progressive loss for DT-Net, contractivity losses for PI-Net) rather than inherent to architecture classes. The paper acknowledges this in a single sentence in Limitations, but the framing throughout the paper (including the abstract) makes architectural-level claims. This matters because readers may draw incorrect conclusions about what is universal versus training-procedure-specific.

### Minor

- **No analysis connecting dynamics type to per-instance accuracy.** Table 1 characterizes latent dynamics (fixed point vs. two-point cycle vs. two-loop cycle) but never correlates these with whether the model correctly solved the specific maze. While the paper does note (in Figure 7 caption) that two specific non-fixed-point examples were solved correctly, it lacks the systematic per-instance correlation. The paper itself raises the question in Section 4 ("it is unclear how this correlates with (i) overall model accuracy") but does not answer it—this leaves the TDA analysis as a descriptive observation weakly connected to the paper's core concern with extrapolation performance.

- **The "Other" category in Table 1 (up to 4% of instances) is unexplained and unanalyzed.** These represent dynamics that don't fit any of the three classified categories, and the reader is left without any characterization of what these dynamics look like or what they might mean.

## Trivial

None.

## Nice-to-Haves

- Testing whether retraining with non-deadend-start mazes in training resolves the `deadend_start` failure would distinguish architectural limitation from distribution coverage limitation—a key distinction for the paper's core claim about extrapolation failure.

- Investigating whether imposing contractivity on DT-Net changes its extrapolation profile on `deadend_start=False` mazes would connect the two main contributions (extrapolation failure and dynamics analysis).

- Analyzing per-instance correlations between dynamics type and solution correctness would strengthen the TDA contribution by connecting it to performance rather than just description.

- More clearly separating percolation (task becomes ill-defined) from `deadend_start` (task is well-defined but harder) in the framing, rather than presenting them as equivalently demonstrating the same kind of "extrapolation failure."

## Removed Points

These points are flagged to be removed, treat them with caution.

- **Error bars / confidence intervals on 100 maze experiments**: The harsh critic suggests this, but with 100 mazes per condition and binary accuracy, this is standard practice in the field. This is a statistical nicety, not a methodological flaw.

- **No analysis of *why* the model fails on non-deadend starts beyond "no clear qualitative difference"**: The paper already notes the monotonic decrease with start-position degree, which is itself an analysis. Demanding a mechanistic explanation of the failure mode goes beyond the paper's stated scope of documenting the failure.

- **Missing related works about chess, Othello, etc.**: The discussion section briefly connects to related interpretability work on spatial reasoning tasks—this is standard contextual framing, not a claim that requires exhaustive related work coverage.

- **Reproducibility concerns about hyperparameters (burn-in K, ball-radius threshold)**: These are specific parameter choices, not missing implementation details. While the threshold of 0.01 for classifying [1,0] could benefit from sensitivity analysis, this is a minor detail not central to the claims.

- **The TDA analysis should use PCA visualizations colored by correctness**: This is a nice visualization suggestion but not a substantive methodological gap.

- **Demand for multiple additional models per architecture class**: While this would strengthen architectural-level claims, evaluating the most performant model from each prior work is a reasonable starting point. The limitation is acknowledged in the paper.

## Novel Insights

The paper makes a genuinely novel observation that the type of out-of-distribution shift matters fundamentally: models that extrapolate perfectly along maze size can fail catastrophically when the distribution shift involves a different structural property (start position connectivity). This is more nuanced than simply showing "extrapolation fails"—it shows that extrapolation is axis-dependent, which is a qualitatively different and more informative finding. Separately, the discovery that DT-Net solves mazes correctly while exhibiting two-point cycles and two-loop cycles (rather than fixed points) has theoretical implications: if limit cycles can be benign for correctness, then much of the theoretical literature on convergence guarantees for RNNs/INNs may be establishing sufficient but unnecessary conditions, and the paper deserves credit for flagging this.

## Suggestions

- Reweight the presentation to treat `deadend_start` as the primary finding and percolation as a secondary qualifying observation, rather than presenting both as equivalent evidence for the same claim. The `deadend_start` result is strong on its own; the percolation result is interesting but fundamentally different in nature.

- In the abstract, qualify the architectural-level claims ("models that are explicitly trained..." → "the models we test that are explicitly trained...") to match the evidence level.

- Add a per-instance analysis (or at least a table/correlation) connecting TDA dynamics type to solution correctness, even if the result is that there is no clear correlation—this would directly address the open question the paper itself raises.

## Score and Decision Assessment

**Originality:** The deadend_start axis as a test of extrapolation and the TDA-based characterization of latent dynamics are both novel. The percolation axis is less novel as a test because it confounds task specification with generalization.

**Importance of research question:** Important—the paper challenges the narrative that logical extrapolation works robustly by showing it depends critically on the axis of difficulty.

**Well-supported claims:** The `deadend_start` finding is well-supported. The percolation finding is partially undermined by the task being ill-posed. The dynamics characterization is descriptive but not yet connected to performance outcomes. The architectural-level claims about RNNs vs INNs overreach the evidence.

**Soundness of experiments:** Experiments are sound for what they measure. The choice of models and tasks is reasonable. The TDA methodology is appropriate.

**Clarity:** The paper is well-written and honest about its limitations. The conflation of percolation with `deadend_start` in the framing is the main clarity issue.

**Value to community:** The paper makes a genuine contribution by showing axis-dependent extrapolation failure and by introducing TDA tools for latent dynamics analysis. However, the overclaiming on two fronts (percolation equivalence, architectural generality) reduces impact.

The paper makes real contributions—the `deadend_start` finding and TDA methodology are genuine advances—but overstates its claims. The core observations are sound, the analysis is incomplete rather than flawed, and the limitations are themselves informative. This is a solid paper with meaningful contributions that would benefit from more careful framing and a per-instance dynamics-accuracy analysis, but whose core findings stand.

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>