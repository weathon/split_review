Here is my synthesized review.

---

## Summary

SUPERMERGE proposes a gradient-based model merging method that learns per-layer, per-task scaling weights (bounded to [−1,1] via tanh) by optimizing on a tiny validation set, replacing the single hyperparameter λ used by Task Arithmetic, TIES, and DARE. The method is evaluated on 11 generative NLP tasks (T0-3B with IA³) and 8 predictive CV tasks (ViT-B/32), showing consistent improvements. A hierarchical variant reduces peak memory by ~75% while maintaining performance.

## Strengths

- **Well-motivated per-layer design, supported by empirical analysis**: Figure 3 shows convincingly that task-vector magnitudes vary substantially across layers and across tasks within the same layer, providing direct evidence that a single global λ is inadequate. The tanh ablation (Table 4) confirms the design choice is consequential — removing it drops in-domain accuracy from 69.6% to 64.8% and out-of-domain from 69.0% to 67.1%.

- **Strong and consistent empirical gains on both generative and predictive tasks**: SUPERMERGE ranks first in 8 of 11 generative NLP tasks and 5 of 8 predictive CV tasks (Section 6.1). The out-of-domain results on ROPES are particularly striking: SUPERMERGE achieves ~49% accuracy vs. 19% for DARE+TIES (a ~30 percentage point gap), exceeding what even the raw "average improvement" headline suggests.

- **Extreme parameter and data efficiency quantified concretely**: The method introduces only 2,112 trainable parameters (vs. 2.85B for full fine-tuning) and uses just 352 validation data points. FLOPs are ~1000× lower than full fine-tuning (Table 5, Section 6.2). These numbers are explicitly reported and contextualized.

- **Hierarchical merging that substantially reduces memory without apparent performance degradation**: The hierarchical variant cuts peak memory from 130.4 GB to 32.7 GB when merging 11 T5-3B models (Table 5) while achieving "similar performance" in both in-domain and out-of-domain settings (Section 6.1). This directly addresses the practical limitation of the standard version.

- **Interpretable weight visualizations that reveal structural patterns**: Figure 5a shows SUPERMERGE learns dense weights spanning [−1,1] (enabling active de-emphasis of layers), whereas AdaMerging learns sparse weights restricted to [0,1]. Figure 5b further shows decoder FFN weights are predominantly positive while self-attention weights span the full range, suggesting the method discovers meaningful task-specific structure.

## Weaknesses

### Fatal
None.

### Major

- **No variance or confidence information reported for any experimental result**: Tables 1–3 report a single accuracy number per method per task with no standard deviations, confidence intervals, or information about repeated runs. Given that the validation set is only 32 samples per task (352 total), the merging-weight optimization could be sensitive to the specific validation split. Without error estimates, it is impossible to assess the statistical significance of the reported improvements. This is a standard expectation for experimental ML papers and a meaningful omission.

### Minor

- **The headline improvement numbers (5.8% average, 49.4% per-task) are stated without specifying the reference baseline**: The abstract (line 26) claims "an average accuracy improvement of 5.8% across all tasks, while the per-task improvement is up to 49.4% over well-established and recent baseline techniques." The paper never specifies which baseline is the reference for these aggregated figures — the best-performing baseline? The average over all baselines? The second-best? The full tables are provided, so the data is not hidden, but the headline is uninterpretable on its own and risks being perceived as cherry-picked.

- **The hierarchical merging strategy does not specify how "similar tasks" are identified for grouping**: Line 93 states the hierarchical approach "begins by merging models fine-tuned for similar tasks" but provides no metric, procedure, or ablation study for determining similarity. Is similarity measured by task-vector cosine distance? Validation-loss correlation? Hand-curated task categories? The hierarchical variant's results may depend critically on this unspecified grouping choice, and no robustness analysis is provided.

- **T0-3B / T5-3B naming inconsistency**: The paper refers to the base model as T0-3B (line 109, the correct name for the prompted multitask model) but then switches to T5-3B in Table 5 and line 164. While T0-3B is built on T5-3B, they are not the same model, and this inconsistency creates ambiguity about what was actually used.

- **The comparison with AdaMerging conflates two differences simultaneously**: SUPERMERGE differs from AdaMerging in both the loss function (supervised vs. unsupervised entropy) and the weight formulation (tanh-bounded [−1,1] vs. softmax-weighted [0,1]). The paper acknowledges AdaMerging is unsupervised (line 113), but the experimental setup does not isolate which of these two differences drives the performance gap. Running AdaMerging with the same supervised loss (which its framework permits, since the loss is pluggable) would cleanly separate the effect of the weighting formulation from the effect of the supervision signal.

### Trivial

- Line 64 states that DARE's performance "drop[s] significantly on both sides of the optimal λ=0.3" without providing the numerical values behind this qualitative claim. Fig. 2 is referenced but does not give absolute numbers.

## Nice-to-Haves

- An ablation showing performance as a function of validation set size would be informative, given that 32 samples per task is unusually small. If performance degrades with fewer samples, that is important for practitioners; if it is robust, that is a publishable finding in itself.
- Comparing against Task Arithmetic with per-task λ values (k λs instead of one) would help isolate the value of per-layer granularity from per-task granularity, which are confounded in the current comparison set.

## Removed Points

These points were identified by reviewers but are retained here (with justification) for completeness:

- **Fisher Merging / RegMean omission** (Harsh Critic, Section 2): The paper explicitly states these are "known to be sub-optimal as compared to the recent baselines" (line 113). Including every older baseline is not standard practice when the most competitive baselines (TIES, DARE, Task Arithmetic, AdaMerging) are already present. **Removed**: not a genuine weakness, as the paper provides a justification and includes the strongest comparators.

- **Layer definition ambiguity** (Harsh Critic, Section 3): The critic asks whether "layers" refer to individual weight matrices or transformer blocks. The paper's visualization in Figure 5b distinguishes between "FFN layers in the decoder" and "self-attention layers," making it clear that layers correspond to individual weight matrices. **Removed**: the paper is sufficiently clear.

- **Unbounded sum of task vectors concern** (Harsh Critic, Section 5): The critic notes that if tanh(w) ≈ 1 for all tasks, the sum of task vectors could be large. This is a theoretical possibility that the optimization would naturally avoid (since large weights would increase validation loss), and the tanh ablation (Table 4) shows the bounded formulation helps. **Removed**: the concern is speculative and contradicted by the empirical evidence.

- **"State-of-the-art" claim** (Strength Finder): One strength claimed SUPERMERGE "achieves state-of-the-art performance." The paper uses this phrasing (line 26) but the claim is relative to the included baselines, not to all possible methods. **Removed**: kept as a minor phrasing observation, but the empirical results genuinely support strong claims within the comparison scope.

## Novel Insights

None beyond the paper's own contributions. The key insight — that per-layer, per-task merging weights bounded by tanh can be learned on a tiny validation set — is well-articulated by the authors themselves and supported by the task-vector variation analysis (Figure 3). The reviews raise important methodological concerns but do not add a fundamentally novel lens to the contribution.

## Suggestions

1. **Add variance information** — report means and standard deviations over multiple validation splits or repeated optimization runs for at least the main tables. This is the single most important improvement the paper could make.

2. **Anchor the 5.8% headline** — explicitly state which baseline(s) the aggregated improvement is computed against (e.g., "5.8% average improvement over the best-performing baseline, Task Arithmetic").

3. **Specify the task-similarity metric** used for hierarchical grouping, and show that the results are robust to alternative grouping choices.

4. **Clean up the T0-3B / T5-3B naming** for consistency throughout.

## Score and Decision

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>