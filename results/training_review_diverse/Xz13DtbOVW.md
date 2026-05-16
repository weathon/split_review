Here is my consolidated final review based on careful verification against the paper.

---

## Summary

This paper proposes CEAG (Constrained Excess Accuracy Gaps), a constrained optimization approach to mitigate the disparate impact of model pruning. The key idea is to directly bound per-group accuracy changes between the dense and sparse models (rather than using surrogate loss-based metrics), and solve the resulting non-convex, non-differentiable constrained problem using proxy constraints with replay buffers for variance reduction. Experiments on FairFace, UTKFace, and CIFAR-100 show that CEAG reliably satisfies disparity constraints on the training set across architectures and sparsity levels, and generally achieves competitive or best test-set disparity.

---

## Strengths

- **Direct, interpretable formulation of pruning-induced disparity.** Defining constraints on excess accuracy gaps (EAGs) — the difference between per-group and global accuracy changes from pruning — is a meaningful advance over surrogate loss-based approaches (Tran et al. 2022). The tolerance ε has a clear interpretation (e.g., ε=1% bounds per-group accuracy degradation relative to the average), enabling algorithmic accountability with a well-defined feasibility criterion (§3.1–3.3).

- **Reliable training-set disparity reduction across diverse settings.** CEAG consistently achieves the smallest maximum EAG and pairwise disparity on the training set across all evaluated tasks (FairFace at 99% sparsity, UTKFace with race and intersectional groups, CIFAR-100 with 100 groups) and architectures (ResNet-34, MobileNet-V2, CifarResNet-56), while maintaining comparable aggregate accuracy. The results are reported with mean±std across 5 seeds, demonstrating low variance (§5.2–5.3).

- **Scalability to large numbers of groups.** The method handles up to 100 sub-groups (CIFAR-100) and intersectional groups (UTKFace race×gender) with the same per-iteration cost as ERM — one forward pass and one backward pass. Replay buffers provide a practical mechanism for variance reduction in constraint estimation without increasing the per-iteration computational budget (§4, Table 3).

- **Novel technical components for stochastic constrained optimization.** The combination of proxy constraints (for non-differentiable accuracy-based constraints) with replay buffers (for variance reduction in mini-batch constraint estimates) is well-motivated and demonstrated to improve training dynamics for both CEAG and the equalized loss baseline (Table 3, App. B.3). The algorithm is general and applicable beyond the specific disparity setting.

- **Transparent documentation of limitations.** The paper repeatedly and prominently acknowledges that all mitigation methods (including CEAG) fail to generalize disparity constraints to unseen data (§1, §5.3, §6, Ethics Statement). This candor is a strength of scientific integrity and identifies a concrete open problem for the community.

---

## Weaknesses

### Fatal

None. The paper's core technical contributions — the EAG-based formulation, the proxy-constraint + replay-buffer algorithm, and the experimental demonstration of reliable training-set control — are valid and supported by the evidence. The generalization gap is a genuine limitation but is transparently documented and does not invalidate the core claims.

### Major

1. **Generalization gap undermines practical deployment claims.** The paper candidly states that "all methods considered in this paper (including ours) fail to mitigate pruning-induced disparities on unseen data" (§1). While CEAG reliably satisfies constraints on the training set and generally achieves better test-set disparity than baselines, the central promise implied by the title and framing ("Constraining Disparate Impact in Sparse Models") is delivering sparse models with controlled disparity for deployment. The constraints serve as a training-time diagnostic tool, but their failure to transfer means the method does not (yet) provide a deployable solution. This is the most significant weakness and limits the practical impact of the contribution.

2. **Incomplete baseline comparison.** The baselines are limited to naive fine-tuning, early-stopped fine-tuning, and the equalized loss method of Tran et al. (2022). Missing are simpler fairness-aware fine-tuning approaches such as group-weighted loss reweighting, group distributionally robust optimization (DRO), or directly adding per-group accuracy gap terms as penalties rather than constraints. These are directly applicable to the same problem (post-pruning fine-tuning) and would help establish whether CEAG's constrained formulation offers advantages over simpler alternatives. Without these, it is unclear whether the complexity of the constrained optimization is justified.

### Minor

1. **On CIFAR-100, ELGRB outperforms CEAG on test disparity.** The paper reports that "the best accuracy and the smallest max_g ψ_g on the test set are obtained by ELGRB" (§5.3, Table 3). This directly undercuts any claim that CEAG is uniformly the best method, and the paper does not analyze why the advantage reverses on this larger-group setting.

2. **Only upper bounds on ψ_g are constrained, not the full disparity range.** The formulation only imposes ψ_g ≤ ε (positive EAGs/hyper-degraded groups), not lower bounds. As the paper acknowledges (§3.2), this means the pairwise disparity ψ_max − ψ_min can still grow if some groups improve dramatically while others degrade. The operational shift to max_g ψ_g as the metric is a reasonable practical choice, but the paper would benefit from clearer discussion of what disparity patterns the formulation does and does not control.

3. **Limited hyperparameter sensitivity analysis.** The tolerance ε and buffer size k are critical hyperparameters, but no sensitivity analysis is presented in the main text. The choice of ε values is justified conceptually (§3.3) but not empirically explored (e.g., how does the train/test trade-off change with ε?). The buffer ablation for CIFAR-100 is informative but limited to a single experiment.

4. **No analysis of why the generalization gap occurs.** The paper documents the generalization failure but provides no analysis of its causes — e.g., whether it stems from distribution shift, overfitting to noisy constraint estimates, insufficient buffer sizes, or fundamental limitations of the training-set objective. This analysis would significantly strengthen the paper even without a full solution.

### Trivial

None.

---

## Nice-to-Haves

- Sensitivity analysis for ε and buffer size k across multiple settings.
- Simpler baseline methods (group-weighted loss, DRO, or penalty-based approaches) to isolate the benefit of the constrained formulation.
- Analysis of the generalization gap: does it correlate with dataset size, group representation frequency, or model capacity? Is the gap reduced by validation-set-based early stopping on disparity?
- The FairGRAPE comparison on FairFace (Table 1) uses a different architecture and is quoted from the original paper without re-running; the paper acknowledges this, but the comparison adds limited information given the confounds.

---

## Removed Points

These points are flagged to be removed from the harsh critic's review; treat them with caution:

- **"The method's central claim is flatly contradicted by the paper's own evidence."** Overstated. The paper's central claim is about directly constraining disparity via accuracy gaps; this is achieved on training data. The generalization caveat is stated prominently and transparently. The claim is not "contradicted" — it is qualified. The paper would benefit from sharper framing but does not contradict itself.

- **"FairGRAPE comparison is problematic and misleading."** The paper transparently notes it quotes from the original publication and does not re-run FairGRAPE due to cost. This is standard practice for comparison with expensive prior methods. The comparison is imperfect but not misleading.

- **"Computational overhead claim not substantiated in main paper."** The main paper provides a clear technical argument (§4.3): one forward + backward pass, same as ERM, plus O(|G|) constraint evaluation. The appendix is referenced for empirical confirmation. This is standard practice and substantiated.

- **"The paper would be more honest as an empirical study."** The paper has a genuine methodological contribution (the formulation and algorithm). Reconceptualizing it as purely an empirical study would discard this contribution. The current framing as a method paper with honest limitation documentation is appropriate.

- **"The method only constrains positive ψ_g — the full range of disparity is not bounded."** The paper explicitly discusses and justifies this design choice (§3.2), defines an operational metric (max_g ψ_g), and uses both max_g ψ_g and pairwise disparity in evaluations. The issue is acknowledged.

- **"No statistical significance testing."** Reporting mean ± std across 5 seeds is standard for this type of empirical work. This is not a meaningful gap.

---

## Novel Insights

The reviews surface an interesting tension that the paper itself embodies: CEAG introduces a clean, principled formulation for controlling pruning-induced disparity, but its central finding (from the transparent evaluation) is that training-set disparity control does not transfer to test sets. The most novel insight to emerge from the reviews is that **the very directness and interpretability of the EAG formulation might be contributing to the generalization gap** — accuracy-based constraints are non-smooth and may cause the model to overfit to training-set accuracy patterns in a way that loss-based surrogates (like ELGRB) partially avoid (consistent with ELGRB's better CIFAR-100 test performance). This hypothesis is not in the paper but is worth investigating. Beyond this, the reviews do not contribute insights beyond the paper's own documented findings.

---

## Suggestions

1. **Sharpen the framing.** The paper claims to "reliably mitigate the disparate impact of pruning" (Contributions, line 53) and then immediately states "all methods fail on unseen data" (line 56). This juxtaposition is confusing. The paper should clearly scope its central claim as *training-time disparity control* and frame the generalization failure as a secondary finding (which is already valuable).

2. **Add simpler baselines.** Including group-weighted loss or DRO fine-tuning would establish whether the constrained optimization machinery is necessary, or whether simpler reweighting suffices.

3. **Investigate the generalization gap.** Even without solving it, an analysis (correlating the gap with group size, buffer parameters, or model capacity) would substantially increase the paper's impact. If the gap is related to accuracy-as-constraint non-smoothness, the paper could suggest specific remedies.

4. **Ablate ε and k in the main text.** Even one figure showing how test-set disparity and accuracy vary with ε across sparsity levels would significantly strengthen the empirical evaluation.

---

## Score and Decision

The paper proposes a novel and well-motivated formulation for a real problem, provides a working algorithm, evaluates across multiple tasks/architectures, and is transparent about its limitations. The generalization gap and incomplete baselines are real weaknesses that limit the practical contribution, but the technical advances (EAG-based constraints, proxy-constraint + replay-buffer optimization, demonstrated training-set control and scalability) are genuine. In its current form the paper is above the acceptance threshold but would be strengthened by addressing the major and minor concerns.

MY FINAL SCORE: <pineapple>6.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>