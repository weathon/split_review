- Decision: Reject
- Avg Score: 4.33
- Scores: 5, 3, 5
Now I have all the information needed. Let me construct the final consolidated review.

## Summary

This paper proposes SEArch, a framework that grows a student CNN from a minimal 2-node structure by iteratively identifying bottlenecks (via a modification value score combining imitation loss and degree ratio) and splitting edges (widening or deepening), guided by a teacher model's feature maps. The approach combines elements from pruning, knowledge distillation, and architecture search. Experiments on CIFAR-10, CIFAR-100, and ImageNet show the method can produce compact networks that match or exceed teacher accuracy, with an ablation study demonstrating that the bottleneck-guided splitting is critical.

## Strengths

- **Bottleneck identification via the modification value score is empirically critical.** The ablation in Table 1 Exp (A) shows that replacing the score with raw imitation loss ($R_{\text{inner}}$ alone) causes a **−0.80% accuracy drop**, while the full score yields **+0.87% gain** on CIFAR-10 ResNet-56. This controlled experiment cleanly isolates the contribution of the degree-ratio adjustment term.

- **Bottleneck-guided edge-splitting strongly outperforms random splitting.** In Table 1 Exp (C), random edge-splitting causes a **−2.16% accuracy drop** for ResNet-56 and **−1.22%** for ResNet-110, while the proposed selection yields **+0.87%** and **+0.97% gains** respectively. The gap is large and consistent, providing direct evidence that the selection mechanism — not simply growing a larger network — drives the improvement.

- **Robust to the teacher-layer assignment hyperparameter $c$.** Ablation in Table 1 Exp (B) tests $c=0.25$, $c=0.50$, and $c=0.75$; accuracy differences are within **0.1%**, showing the framework is not sensitive to this choice.

- **KD comparison at a matched parameter budget shows clean advantage.** Under the same 0.27M parameter budget as ResNet-20, SEArch achieves 93.58% on CIFAR-10, outperforming fixed-architecture KD methods. This comparison controls for capacity, isolating the benefit of architecture optimization during distillation.

## Weaknesses

### Fatal
None. The core mechanism is validated internally (ablation study), and no verifiable error invalidates the paper's central claims.

### Major

- **Pruning comparisons do not control for parameter/FLOPs budgets, weakening the "state-of-the-art" claim.** The paper sets SEArch's target at **0.40M parameters** on CIFAR-10 (line 202), while pruning baselines in Table 2 range from 0.17M (HRank) to 0.47M (SFP). A method using more capacity naturally tends toward higher accuracy. The paper does not present results at matched budgets, making it unclear whether SEArch's accuracy advantage over pruning methods reflects superior architecture optimization or simply a larger network. This issue also affects Tables 3 and 4. The relative "accuracy drop" comparison partially mitigates this, but the core claim of state-of-the-art performance over pruning methods is not cleanly supported.

- **The student retraining procedure across iterations is not specified.** The paper says "We split the training dataset into two subsets for these two stages" (line 74) but never states: (1) whether the student is **retrained from scratch** at each iteration or **fine-tuned** from the previous iteration's weights, (2) the dataset-split ratio, or (3) the number of training epochs per iteration. If retrained from scratch, cumulative cost is enormous; if fine-tuned, comparisons with pruning methods (which prune once and fine-tune) become apples-to-oranges. This is a reproducibility gap that affects the interpretation of all experimental results.

- **The efficiency claim is unsupported by any quantitative runtime data.** The paper repeatedly claims efficiency over NAS (lines 4, 16, 18, 23, 47, 228) but provides **zero** GPU-hours, search iterations, or wall-clock time for any experiment. Without this, "efficient" is an unsubstantiated qualitative label. Reporting search cost is standard for methods claiming efficiency advantages.

- **The widening-vs-deepening threshold $B_{op}$ is never specified.** Line 149 states "we first use the deepening modification until the number of stacked operations reaches a predefined number $B_{op}$," but no experimental value for $B_{op}$ is reported, nor is there any analysis of how it affects results. This parameter directly controls the depth-width trade-off and is needed for reproducibility.

### Minor

- **The modification value score derivation is heuristic, not theoretically justified.** The paper acknowledges modeling learning "as an information gain process" (line 114) and makes strong assumptions (equal contribution from each incoming edge, reducibility of $R_{\text{inner}}$ to zero). The ablation shows the score works, but the paper does not test simpler alternatives beyond $R_{\text{inner}}$-alone and random (e.g., out-degree only, in-degree only, gradient-based sensitivity), which would strengthen the argument that the specific formula is meaningful.

- **The attention module $f_a$ is described only at a conceptual level.** The paper states it computes $\text{Atten}(v_i, \hat{v}_{q_i}, \hat{v}_{q_i})$ for channel-space feature projection (lines 85-89), but provides no architectural details (e.g., number of parameters, number of layers, whether it is trained jointly or separately). This is needed for exact reproducibility.

- **No statistical significance reported for ImageNet results.** In Table 4, SEArch's Top-1 accuracy (72.32%) is close to baselines (e.g., HRank 71.98%, SFP 71.83%) with differing FLOPs/param budgets. Without confidence intervals or multiple-run statistics, these differences may not be meaningful.

- **The KD comparison (Table 5) would benefit from more recent baselines.** The paper compares against a small set of KD methods. While the matched-budget comparison is clean, situating SEArch against a broader set of competitive KD approaches would strengthen the claim.

### Trivial
- The paper states at line 161 "Acc. Drop is the accuracy drop (smaller is better), where a negative value means the optimized model outperforms the baseline" — this notation (negative = improvement) is non-standard and briefly confusing.
- Table 5 appears to include a "student accuracy" of 71.40% for Hinton et al. 2015 (from the strength finder), which seems surprisingly low for CIFAR-10 ResNet-20 distillation and warrants clarification.

## Nice-to-Haves
- An analysis of the evolved architectures: what topologies emerge? How does depth vs. width trade off across iterations? Figure 2 shows one example, but a summary over many runs would provide insight.
- An ablation on the operation choice (currently only 3×3 separable conv). The paper cites Yang et al. (2019) that macro-structures matter more, but an experiment with a larger operation set would directly justify this design decision.
- A comparison against lightweight NAS methods (e.g., DARTS, SNAS) under similar computational budgets, which would more directly substantiate the claimed efficiency advantage.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **"Pruning comparison is conceptually questionable because SEArch grows rather than prunes."** — Removed. The paper addresses the same problem (optimizing an oversized network under a resource budget). Comparing against pruning methods for this task is standard and appropriate. The reviewer overstates a scoping concern into a methodological flaw.

- **"The initial mapping $q$ for the two-node student is not specified."** — Removed. The paper states "For example, if $q_2=m$, it means that the student node $v_2$ is supervised by the final layer $\hat{v}_m$ of the teacher model" (line 83). The initial mapping is clearly $q_2=m$ for a 2-node student.

- **"Whether the student's feature map spatial dimensions match the teacher's is not addressed."** — Removed. The paper explicitly says "student node $(v_i)$ and its corresponding teacher node $(\hat{v}_{q_i})$ can have feature maps with identical height and width dimensions" (line 85). The mapping is designed to ensure spatial alignment.

- **"The paper does not discuss the number of search iterations."** — Partially addressed; the paper states the iterative process continues "until its model size reaches the budgetary limit $B$" (line 74). The exact count depends on the budget and growth rate. While reporting the actual iteration count would be helpful, this is a minor detail rather than a missing component.

- **"Only two KD baselines in Table 5."** — Insufficiently grounded. The table image cannot be fully read, but the paper's text discusses multiple KD families. Moving this from Major to Minor as the critique may be inaccurate.

- **"The definition of the teacher's longest path and partitioning into $m$ layers is not clearly connected."** — Removed. The paper explains: "We identify the longest path originating from the input and terminating at the final feature map. The feature maps along this path constitute a list of nodes $\hat{\mathbb{V}} = \{\hat{v}_1, \hat{v}_2, ..., \hat{v}_m\}$ and the teacher model is partitioned into $m$ layers" (lines 63-72). This is clear.

## Novel Insights

The most interesting finding that emerges from combining the reviewers' analyses is the **disconnect between strong internal validation and weaker external comparisons**. The ablation study (Table 1) is well-designed: it controls for budget, tests the score vs. alternatives, and shows large, clean gaps (e.g., −2.16% random vs. +0.87% guided). Yet the headline comparisons against pruning methods (Tables 2–4) are confounded by mismatched budgets. This suggests the paper's core methodological contribution is real, but the evaluation narrative overreaches. A more measured framing — "SEArch consistently finds better architectures than random growth, and at matched budgets outperforms fixed-architecture KD" — would be more honest and likely more persuasive. The paper also does not explain the striking result that the student can *exceed* the teacher's accuracy; the limitations section touches on teacher constraint but not on why negative accuracy drop is possible, which is an interesting phenomenon worth discussing.

## Suggestions

1. **Re-run pruning comparisons at matched parameter budgets.** For each pruning baseline, either adjust the prune ratio to match SEArch's 0.40M target, or present SEArch results at each baseline's budget. This would cleanly resolve whether SEArch offers a genuine parameter-efficiency advantage.

2. **Report computational cost.** Provide GPU-hours (or equivalent) for the full SEArch pipeline. This is essential for the efficiency claim and for meaningful comparison with NAS methods.

3. **Specify the missing training details in a clearly marked reproducibility section:** (a) retrain-from-scratch vs. fine-tune across iterations, (b) dataset split ratio, (c) training epochs per iteration, (d) the value of $B_{op}$, and (e) the attention module architecture (number of parameters, layers, training procedure).

4. **Add an ablation on the degree-ratio formula.** Test variants using out-degree only, in-degree only, and a gradient-based alternative to strengthen the claim that the specific $\deg^+/\deg^-$ formula is meaningful rather than just a plausible heuristic that happens to work.

5. **Discuss why the student can outperform the teacher.** This is an interesting and non-obvious result that warrants explanation — is it due to longer effective training? Better feature supervision? Architecture flexibility?
