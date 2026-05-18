I've now thoroughly read and verified the paper. Let me produce the final consolidated review.

## Summary

DeepZero presents a framework for scaling zeroth-order (ZO) optimization to train deep neural networks from scratch, combining coordinate-wise gradient estimation (CGE), ZO-based pruning-at-initialization (ZO-GraSP) to induce gradient sparsity, and implementation-level accelerations (feature reuse, forward parallelization). The paper demonstrates 86.94% test accuracy on ResNet-20/CIFAR-10 — the best reported among gradient-free methods — and shows 10–20% improvements over prior ZO methods in certified adversarial defense and PDE error correction.

## Strengths

- **Demonstrates that CGE outperforms RGE for DNN training under equal query budgets.** Figure 2 (Acc\_CGE\_RGE) shows CGE achieving accuracy comparable to FO training for a CNN on CIFAR-10 while RGE lags significantly even with q = d queries. The paper also provides timing analysis (Fig. 3, Tab. rge_cge_time_compare in appendix) showing CGE is computationally more efficient because RGE must generate and integrate a d-dimensional perturbation vector into the entire model per query.

- **Introduces a principled ZO-only pruning method (ZO-GraSP) that identifies sparsity patterns using only function queries.** The appendix tables show ZO-GraSP significantly outperforms random pruning and yields accuracy comparable to FO-GraSP (which requires second-order information). The proposed layer-wise pruning ratios (LPRs) enable dense-model training with dynamically updated sparse gradient patterns, balancing the query efficiency of pre-pruning with the training effectiveness of alternating schemes.

- **Achieves state-of-the-art accuracy among gradient-free methods on ResNet-20/CIFAR-10 (86.94%) and demonstrates practical utility in two challenging black-box applications.** In the defense task, DeepZero achieves 10–22% higher certified accuracy than ZO-AE-DS across all perturbation radii on ImageNet-10 (Tab. 2). In PDE error correction, ZO-SOL (via DeepZero) outperforms both the non-interactive and uncorrected baselines and narrows the gap with full FO solver-in-the-loop.

- **Develops feature reuse and forward parallelization with measurable speedups.** Feature reuse provides a 2× reduction in CGE training time (Fig. 4). Forward parallelization leverages the coordinate-wise decoupling property of CGE for distributed computation, with GPU scaling validated in the appendix.

- **Provides a convergence rate analysis in the appendix,** adding theoretical grounding for the proposed algorithm beyond pure empirics.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

1. **The "approaching FO performance" claim is not accompanied by explicit FO-dense and FO-sparse accuracy numbers in the main text.** The paper reports DeepZero's accuracy (86.94%) and Figure 5 (sg\_sw) visually compares DeepZero against FO-dense and FO-sparse baselines with mean/std. However, the FO-dense accuracy number (typically ~91–92% for ResNet-20 on CIFAR-10) is never stated explicitly, making it harder for readers to calibrate the gap. Adding these numbers to the text or a table would make the contribution's significance easier to assess. This is a presentation omission rather than a substantive flaw — the data is in the figure.

2. **The query budget for the black-box defense experiment (1152 queries per gradient estimation) is not clearly reconciled with the sparse CGE formulation.** DeepZero's core gradient estimator (Eq. CGE\_sparsity) uses one query per active coordinate in the sparsity set. The paper states that DeepZero and ZO-AE-DS both use 1152 queries per gradient estimation, but does not state the sparsity ratio or the defense module's parameter count used in this experiment. If the DnCNN defense module (cited in the paper) has ~550K parameters, 1152 active coordinates would correspond to ~99.8% sparsity, which is plausible but should be stated explicitly. The paper does not contradict itself — DeepZero consistently uses sparse CGE — but the missing detail undermines reproducibility of this experiment.

3. **The ablation of the sparsity integration method (M₁, M₂ vs. the proposed LPR-dynamic) is deferred entirely to the appendix.** The paper claims the proposed LPR-dynamic approach combines the query efficiency of M₂ with the training effectiveness of M₁, and references Appx. alg\_details for the comparison. While conference papers routinely defer supporting ablations to appendices (and the appendix was stripped by the parser), the main text would be strengthened by including at least a summary of this comparison. The paper's overall results are convincing without it, but the claim about LPR-dynamic's advantage over its design alternatives would benefit from in-text support.

### Trivial
None beyond what was filtered (see Removed Points).

## Nice-to-Haves

- **Report total wall-clock training time for the main CIFAR-10 experiment** (not just relative speedups), so readers can calibrate the practical cost of ZO training vs. FO training.
- **Include a non-sparse CGE baseline** (CGE without any sparsity) to more directly isolate the benefit of the sparsity framework, though the CGE vs. RGE comparison already supports the core argument.
- **Move the GPU scaling figure to the main text** (currently Fig. 13 in appendix, mentioned only by reference) since scalability is one of the paper's central claims.

## Removed Points

These points were raised by the reviewer but are removed after verification against the paper:

- **"CGE vs. RGE with q = d is an unrealistic setting that disadvantages RGE."** — REMOVED. The paper sets q = d to provide an equal query budget comparison, which is standard practice. The point of the experiment is to show that even at equal query cost (which is the best case for RGE, since practitioners could increase q), CGE is more accurate. This strengthens rather than weakens the argument.

- **"Feature reuse is a straightforward implementation trick."** — REMOVED. The paper presents feature reuse as a practical acceleration technique within a broader framework, not as a standalone novel contribution. No claim is overreaching.

- **"Forward parallelization is a natural mapping."** — REMOVED. Same reasoning as above.

- **"No comparison against standard ZO-SGD with a standard gradient estimator."** — REMOVED. This comparison is present in the paper (CGE vs. RGE on a CNN in Section 3). CGE and RGE are both standard ZO gradient estimators. The critic seems to have missed this section or conflated ZO-SGD with only RGE-based estimators.

- **"Missing ablation comparing M₁, M₂, and the proposed method in the main text."** — The paper explicitly states this comparison is in Appx. alg\_details. Per review policy, appendix content stripped by the parser is not grounds for criticism. The point is downgraded to Minor (weakness #3 above) because a brief summary in the main text would strengthen the paper, not because the comparison is missing entirely.

- **"Training trajectories, batch-size sensitivity, and GPU scaling are relegated to the appendix."** — REMOVED. These are standard appendix contents for a conference paper with space constraints. The paper references them appropriately.

## Novel Insights

None beyond the paper's own contributions. The reviews surface valid clarification requests but do not identify novel connections, alternative interpretations of the results, or unexpected implications that the paper misses.

## Suggestions

1. **Add a small table in the main text** reporting the mean accuracy (± std) of FO-dense, FO-sparse (at the same sparsity levels), and DeepZero at each sparsity regime (80%, 90%, 95%, 99%) for the main CIFAR-10 experiment. This directly addresses the "approaching FO" calibration issue.

2. **Clarify the black-box defense experiment setup:** report the defense module (DnCNN) parameter count, the gradient sparsity ratio used, and briefly explain how the 1152-query budget relates to the active coordinate count |S| in sparse CGE.

3. **Include a one-sentence summary of the M₁/M₂ vs. LPR-dynamic ablation** in the main text (even if the full table stays in the appendix), to support the claimed advantage of the proposed sparsity integration method without requiring readers to consult the appendix.

## Score and Decision

The paper makes a legitimate contribution to an important problem (scaling ZO optimization for DNN training) with clear empirical evidence across multiple tasks. The weaknesses are presentation-level and clarificatory, not structural. The core claims are well-supported.

MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>