I now have complete information. Let me produce the final consolidated review.

## Summary

This paper proposes IMTNAS, an interleaving multi-task neural architecture search framework that avoids the need to tune loss-weight tradeoffs between tasks. Instead of minimizing a weighted sum of task losses, tasks are learned sequentially in a loop (over multiple rounds) with knowledge transfer via distribution matching between consecutive tasks. The framework is formulated as a multi-level optimization problem where architecture search happens at the outermost level after all interleaving rounds complete. Experiments on heterogeneous tasks (classification + detection) and homogeneous tasks (three classification datasets) show improvements over MTNAS baselines.

## Strengths

- **Eliminates training loss-weight tuning.** The paper directly addresses a well-known difficulty in MTNAS — balancing competing loss terms. The interleaving design (each task minimizes its own loss alone) genuinely sidesteps this problem, and Figure 1 (Left) empirically validates the tradeoff issue in the MTL-SWS baseline. This is the paper's core contribution and is clearly motivated.

- **Multi-level optimization formulation unifies the interleaving process.** The formulation in Section 3.1.4 (Eq. 5) nests each task's weight training as subproblems dependent on the shared architecture \(A\), then optimizes \(A\) using validation losses from all tasks. This goes beyond simple sequential fine-tuning and provides a principled end-to-end framework.

- **Distribution-matching knowledge transfer is ablated against reasonable alternatives.** Table 3 directly compares the proposed approach against L2-Weights, L2-Embedding, and Example-Similarity — all of which also use the previous encoder's signal. Distribution matching outperforms all three (e.g., 2.16 vs. 2.91 on CIFAR-100), providing clear evidence that the distribution-level mechanism adds value beyond simpler proximity or example-level similarity losses.

- **Strong empirical results across heterogeneous and homogeneous settings.** In the classification+detection setting (Table 1), IMTNAS achieves 37.4 mAP on COCO and 75.6% top-1 accuracy on ImageNet, outperforming MTL-NAS (36.8/74.3) and BMTAS (27.1/72.4). In the three-classification-task setting (Table 2), IMTNAS applied to PC-DARTS reduces test errors across all three datasets vs. PC-DARTS alone and all multi-task baselines.

- **Ablation studies on key design choices.** The paper studies the number of interleaving rounds (Figure 2, showing clear benefit from \(M=1\) to \(M=2\)), task order (Table 4, showing robustness), and knowledge transfer method (Table 3). These ablations directly support the claims about the interleaving mechanism.

- **Unified framework handles both same-type and different-type tasks.** The method is evaluated on two heterogeneous tasks (classification + detection) and three homogeneous tasks (all classification), demonstrating generality beyond prior MTNAS work that focuses on one setting.

## Weaknesses

### Fatal

None.

### Major

- **Optimization algorithm is underspecified for a method paper.** The sentence "The optimization algorithm for solving the problem in Eq." (line 132) is incomplete, and the paper does not provide a concrete algorithm describing how the multi-level optimization is solved in practice. Key questions left unanswered: Are the inner minimization problems (Eq. 1–3) solved to convergence, via a fixed number of gradient steps, or by some approximation? How are the gradients of the validation loss with respect to \(A\) computed through the inner optimization trajectories — via implicit differentiation, truncated unrolling (as in DARTS), or a different scheme? How many gradient steps are taken per inner stage? While the overall sequential procedure is described and the experimental section mentions SGD/Adam optimizers, the lack of an explicit algorithm (even a concise description of how inner and outer steps interleave) is a significant clarity gap for a contribution that centers on a multi-level optimization formulation.

- **Missing sensitivity analysis for newly introduced hyperparameters.** The method introduces several hyperparameters: the MMD threshold \(\tau=5\), the number of augmentation sets \(C=20\), and the RBF kernel scale parameter (0.1). The paper only studies sensitivity for the number of rounds \(M\) and task order (which partially addresses practical tuning concerns). Without analysis of how performance varies with \(\tau\), \(C\), and kernel parameters, it is unclear how robust the method is to these choices. This is particularly relevant because \(\tau\) directly controls the binary labeling that drives the knowledge transfer loss.

### Minor

- **The hypernetwork's training objective is not explicitly stated.** Section 3.1.4 describes the hypernetwork architecture in detail but does not clearly state through which loss its parameters \(V\) are trained or how this interacts with the multi-level optimization. While it can be inferred that \(V\) is optimized via gradient descent through the same losses that use the generated weights, this should be stated explicitly.

- **The total computational cost of the interleaving process is not concretely reported.** The paper states the cost is "comparable with baselines" (line 188) but does not provide the total number of forward-backward passes or wall-clock time for the full \(M \times K\) sequential procedure vs. standard multi-task training. Given that the interleaving loop multiplies training stages, a concrete cost analysis would help readers assess practical tradeoffs.

- **The knowledge transfer ablation could be strengthened with a "no transfer" baseline.** While Table 3 compares against three reasonable alternatives that all leverage the prior encoder, adding a baseline that simply initializes the current encoder from the previous one (with no explicit transfer loss) would isolate whether the MMD-based labeling provides further benefit over trivial weight reuse. The existing comparisons are informative but this would make the case tighter.

### Trivial

None that would affect evaluation.

## Nice-to-Haves

- Sensitivity analysis for \(\tau\), \(C\), and kernel scale parameter.
- Comparison with a simple sequential fine-tuning baseline (train task 1, fine-tune on task 2, fine-tune back on task 1, etc.) without distribution matching — this would directly test whether the interleaving structure itself provides the benefit independent of the knowledge transfer and NAS components.
- Brief discussion of whether the interleaving framework could be adapted to non-differentiable NAS (e.g., using validation performance as a reward signal), given the acknowledged limitation to differentiable methods.

## Removed Points

These points were flagged by reviewers but removed after cross-checking against the paper. Treat them with caution:

1. **"The multi-level optimization is not solved" as a fatal flaw.** The paper describes the full sequential procedure (Sections 3.1.1–3.1.3) and the experimental section specifies optimizers (SGD for network weights, Adam for architecture variables). The multi-level formulation follows the standard bi-level pattern in differentiable NAS (DARTS-style alternating optimization). While specific algorithmic details are underspecified (kept as a Major weakness above), calling this "fatal" overstates the gap.

2. **"Standard deviations are promised but not shown in Table 2."** The paper states "Mean and standard deviation of classification errors obtained from 10 random runs are reported" (line 212). The table is an image not rendered in the text extraction; we cannot verify its absence from the parsed text alone. The claim of a reporting flaw is based on incomplete parsing.

3. **"The knowledge transfer method's value is not isolated from the fact that the previous encoder provides a training signal."** Table 3 compares against L2-Weights, L2-Embedding, and Example-Similarity — all of which use the previous encoder's signal. The comparison does isolate the distribution-matching mechanism. This criticism is factually incorrect.

4. **"The method shifts tuning burden to validation loss weights / normalization."** The paper explicitly scopes its claim: "our method focuses on alleviating the burden of tuning the weights of tasks' training losses. As for the validation losses, we follow the standard practice of the multi-task learning literature, which treats each task's validation performance (after normalization) equally" (line 122). The criticism ignores this explicit clarification.

5. **Figure readability complaints.** Criticisms about data values being "not readable" are parser artifacts from PDF-to-text conversion, not issues in the original submission.

6. **Complaints about the cut-off sentence as a separate criticism.** The underlying concern (underspecified algorithm) is kept in Major; the cut-off sentence itself is a parser artifact.

## Novel Insights

None beyond the paper's own contributions. The reviews raise useful points about methodological clarity and sensitivity analysis but do not identify any novel interpretation, limitation, or future direction that the authors themselves did not discuss or that changes how the contribution should be understood.

## Suggestions

1. Add an explicit optimization algorithm (pseudocode or a clear description) showing how the multi-level problem is solved — specifying the number of inner gradient steps per stage, how architecture gradients are computed, and how the hypernetwork parameters are trained.

2. Add sensitivity analysis for \(\tau\), \(C\), and the kernel scale parameter. A simple plot showing performance over a range of values would substantially strengthen the paper.

3. Report concrete computational cost (e.g., total GPU hours) alongside Table 1 and Table 2.

4. Include a "no transfer" or "direct weight initialization" baseline in the ablation study to fully isolate the benefit of the distribution-matching loss.

5. Ensure Table 2 clearly shows standard deviations (if not already visible in the original figure) and briefly discuss whether reported improvements are statistically significant.

## Score and Decision

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>