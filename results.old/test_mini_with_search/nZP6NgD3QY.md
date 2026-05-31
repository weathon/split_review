Now let me write the final consolidated review.

## Summary

AdaMerging introduces an unsupervised approach to learn per-task or per-layer merging coefficients for task-vector-based multi-task model merging. The method uses entropy minimization on unlabeled test samples as a surrogate objective to optimize these coefficients automatically, eliminating manual grid search. Experiments on eight image classification tasks with ViT-B/32 and ViT-L/14 backbones show that Layer-wise AdaMerging achieves 80.1% average accuracy — an 11% improvement over Task Arithmetic (69.1%) and a substantial narrowing of the gap to traditional MTL (88.9%).

## Strengths

1. **Clear, well-motivated idea with strong quantitative results on a standard benchmark.** Table 1 shows Layer-wise AdaMerging achieves 80.1% on eight tasks with ViT-B/32, compared to 69.1% (Task Arithmetic) and 72.4% (Ties-Merging). The improvement is large and consistent across both ViT-B/32 and ViT-L/14 backbones. This directly supports the paper's central claim that learnable per-layer coefficients substantially outperform a shared coefficient.

2. **Generalization and robustness gains are demonstrated across multiple settings.** Table 2 shows AdaMerging improves average accuracy on unseen tasks by up to 9.1% over Task Arithmetic/Ties-Merging. Table 4 (robustness) evaluates seven types of corruption and shows AdaMerging outperforms Task Arithmetic on every corruption type, with improvements from +5.8% to +11.2%.

3. **The correlation analysis (Spearman ρ = 0.87 between entropy and loss) provides empirical grounding for the unsupervised objective.** Figure 2's binning analysis shows that lower-entropy groups correspond to lower average prediction loss across all eight tasks, which motivates why minimizing entropy is a reasonable proxy for minimizing task loss during coefficient optimization.

4. **Layer-wise coefficient analysis reveals interpretable and meaningful patterns.** Figure 4 shows shallow layers learn smaller coefficients and deep layers learn larger ones, consistent with the intuition that lower layers capture general features while deeper layers are more task-specific. This qualitative result supports the claim that the method learns meaningful coefficients rather than arbitrary values.

5. **The method is practical and lightweight.** The approach requires only unlabeled test samples (no original training data, no labels), operates as an automatic optimization procedure, and avoids the combinatorial cost of per-task or per-layer grid search.

## Weaknesses

### Fatal

None.

### Major

1. **Missing optimization hyperparameters impede reproducibility.** The paper describes the entropy-minimization objective but does not specify the optimizer, learning rate, number of gradient steps, batch size per task, initialization of coefficients, or whether coefficients are updated jointly or sequentially. The statement that "extra training time is also very cheap" is too vague to reconstruct the method. This is a concrete reproducibility gap: without these details, independent verification is substantially harder.

2. **No error bars or variance estimates are reported for any main result.** The coefficient optimization is a learning process that may be sensitive to the specific test batches used, yet all results (Tables 1–4) are reported as single numbers without standard deviations over multiple runs or seeds. Given the unsupervised nature of the optimization, this omission makes it difficult to assess the reliability and stability of the reported improvements.

### Minor

1. **The evaluation compares an adaptive method to static baselines without a control that isolates the effect of adaptation.** The paper optimizes merging coefficients on unlabeled test samples; baselines (Task Arithmetic, Ties-Merging) use a fixed λ selected by grid search. This confounds two factors: the benefit of per-layer/per-task coefficients and the benefit of adapting to the test distribution. The paper partially addresses this through its own ablation — Task-wise AdaMerging (71.1%) is actually *worse* than Ties-Merging (72.4%), showing that adaptation alone does not explain the large gains of Layer-wise AdaMerging (80.1%). However, a baseline that tunes a single λ on test data via the same entropy objective would more cleanly isolate the contribution of per-layer granularity.

2. **The claim that "even if only 0.1% or 1% of unlabeled tests are available, our method can have significant performance improvements" is stated but never empirically validated.** This is a single sentence in Section 3.2.2 with no supporting experiment. A simple ablation subsampling the test data would verify or refute this claim.

3. **The entropy-as-proxy analysis is informative but does not directly validate that gradient-level alignment between entropy and loss holds during optimization.** The correlation (ρ = 0.87) is computed on the final merged model's predictions. It does not show that the *gradients* of entropy predict the *gradients* of loss with respect to coefficient changes — the actual signal used during optimization. The empirical results (Tables 1–4) ultimately serve as the validation, but the paper frames the correlation analysis as stronger evidence than it is.

### Trivial

None.

## Nice-to-Haves

- Comparing Layer-wise AdaMerging to a version where coefficients are learned by directly minimizing the true loss on a small labeled validation set (or by a random search) would validate whether entropy minimization's proxy quality is tight.
- Comparing to a baseline where Task Arithmetic's single λ is also tuned via entropy minimization on unlabeled test data would isolate the effect of coefficient granularity from adaptation.
- A discussion of limitations would strengthen the paper: the method requires access to unlabeled test data from the target tasks, which may not always be available; and entropy minimization could be misleading in degenerate scenarios (e.g., extremely imbalanced classes, confident wrong predictions).

## Removed Points

These points were flagged by reviewers but are removed from the main assessment with justification:

- *"Evaluation conflates test-time adaptation with static model merging (structural/fatal)"* — Removed as not fatal. The paper's own ablation provides partial disentanglement: Task-wise AdaMerging (71.1%) is worse than Ties-Merging (72.4%), showing that adaptation alone does not drive the large gains. The critic's framing that this is a "structural" flaw overstates the issue; it is a minor weakness (see Weaknesses Minor #1).

- *"Correlation analysis does not justify the proxy under distribution shift"* — Removed as a major concern. The robustness experiments (Table 4) empirically demonstrate that the method works under distribution shifts. The correlation analysis is motivational, not the sole evidence. The critic's demand for per-step gradient alignment analysis goes beyond what is standard for empirical deep learning papers.

- *"Reproducibility limited by missing optimization details (severe)"* — Downgraded from severe to Major (see Weaknesses Major #1). Missing hyperparameters are a genuine reproducibility gap but not a structural flaw in the method itself.

- *"Fisher Merging and RegMean require training data, creating mismatch"* — Removed as noted by the harsh critic themselves as minor. The paper does not claim to beat these on the same footing; they are included as reference points.

- *"Strength: addressed an important problem"* — Generic strength, removed.

- *"Strength: comprehensive experiments"* — Generic, removed in favor of specific strengths.

## Novel Insights

None beyond the paper's own contributions. The reviews did not surface any insight about the paper that goes beyond what the authors already articulate.

## Suggestions

1. **Add a dedicated reproducibility section** reporting the optimizer (Adam/SGD), learning rate, number of iterations, batch size, coefficient initialization strategy, and whether coefficients are updated jointly or sequentially. Even a brief paragraph would substantially raise confidence in the results.

2. **Report all main results with standard deviations** over at least 3 random seeds or test-set splits. This is especially important because the optimization is unsupervised and may be sensitive to batch composition.

3. **Add an ablation** where Task Arithmetic's single λ is optimized via the same entropy objective on unlabeled test data. This would cleanly separate the effect of having more coefficients from the effect of test-time adaptation, addressing the most common likely critique.

4. **Empirically validate the data-efficiency claim** about 0.1%/1% of test data by including a subsampling experiment (e.g., accuracy vs. fraction of test data used for coefficient optimization).

5. **Include a limitations paragraph** in the conclusion discussing settings where the method may struggle (e.g., when test data is unavailable or when entropy minimization could be a misleading objective).

## Score and Decision

**Round 1 (Bracketing):** I queried three bands on model merging / test-time adaptation / unsupervised coefficient learning. Low-band anchors (scores 2–3) were papers with fundamental flaws (poor writing, invalid methods, missing baselines). Middle-band anchors (scores 4–5.5) included AdaRank (4.5, accepted poster), Expert Merging (5.0, accepted poster), DisTaC (5.5, accepted poster), and MetaMerging (4.5, rejected). High-band anchors (score 8) were on unrelated topics (RL, text-to-3D, navigation). Based on this, I placed the paper in the [5.0, 7.0] bracket.

**Round 2 (Narrowing within bracket):** I retrieved additional anchors specifically in the 5.0–7.5 range on adaptive model merging and task-vector methods. I read Expert Merging (5.0 avg, accepted poster), DisTaC (5.5 avg, accepted poster), and GMF-Mean (5.33 avg, rejected) in full.

- **Expert Merging** (5.0): Also learns layer-wise coefficients on unlabeled data for model merging, but uses hidden-state/logit alignment instead of entropy. Reviewers found it somewhat incremental. AdaMerging has a cleaner method (entropy minimization is simpler than alignment objectives) and was earlier/novel. **AdaMerging is stronger.**

- **DisTaC** (5.5, accepted poster): Pre-conditions task vectors via knowledge distillation before merging. Well-executed but narrow (vision-only). AdaMerging shows similar breadth but a different and comparably clean contribution. **Comparable strength.**

- **GMF-Mean** (5.33, rejected): Closed-form hyperparameter-free merging. Elegant but had theoretical concerns about Gram matrix assumptions. AdaMerging is a different paradigm (learning-based vs. closed-form). **AdaMerging is stronger in empirical results.**

AdaMerging is cleaner and more impactful than papers scoring in the 4–5 range, with larger and more consistent improvements. However, the missing optimization details and lack of error bars are tangible weaknesses that papers scoring 6.5+ typically do not have. Comparing against DisTaC (5.5, accepted poster), AdaMerging is comparably strong in contribution but has weaker exposition on reproducibility.

**Final score: 6.0** — A solid paper with a clear, practical contribution. The method is well-motivated, the results are strong, and the idea is influential (as shown by its role as a foundation for later work like AdaRank and Expert Merging). The key weaknesses (reproducibility details, error bars, the adaptation-vs-granularity confound) are addressable but prevent the paper from reaching a higher score.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>