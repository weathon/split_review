## Summary

This paper proposes NeuRulLs, an end-to-end differentiable framework for learning rule lists — interpretable if-then-else classifiers — that jointly learns feature discretizations, conjunctive rules, and rule ordering in a single architecture. The key technical innovations are (1) a soft binning function that learns interval thresholds on continuous features during training (avoiding pre-discretization), (2) a relaxed logical conjunction that prevents vanishing gradients when predicates are inactive, and (3) a Gumbel-Softmax mechanism with temperature annealing for learning rule priority ordering that converges to a strict rule list at inference. The method is evaluated on 20 real-world datasets and synthetic benchmarks against 7 baselines including combinatorial (CORELS, SBRL) and neuro-symbolic (RLNet, DRNet) methods.

## Strengths

- **End-to-end learning of feature discretizations.** The soft binning function (Eq. 4) lets the model learn continuous thresholds during training rather than relying on fixed pre-discretization — a genuine limitation of prior neuro-symbolic and combinatorial rule learning methods. The Ring dataset result (+0.13 F₁ over the next best method) provides specific evidence that this capability matters when rules depend on continuous biomarkers.

- **Relaxed logical conjunction solving vanishing gradients.** The paper identifies a concrete gradient pathology in prior neuro-symbolic conjunctions (Eq. 5: derivatives vanish when any predicate is zero) and proposes a principled relaxation via a weight-dependent slack parameter η (Eq. 7). The ablation (Section 4.2.2) validates this design choice: relaxed conjunction improves average F₁ by 0.3 points and never underperforms the strict version across any dataset.

- **Extensive and competitive evaluation.** The method is tested on 20 real-world datasets covering medicine, finance, and criminal justice — a broader evaluation than most comparable rule-learning papers. Eight baselines span both combinatorial and neuro-symbolic approaches. The average rank of 2.30 and the specific result on the all-continuous Ring dataset provide reasonable evidence of consistent superiority.

- **Clear problem motivation and honest limitations.** The paper situates itself well against both combinatorial (pre-discretization bottleneck, restricted rule size) and neuro-symbolic (same bottleneck plus unstable optimization) prior work. The limitations section is candid about no causal claims, no optimality guarantees, fixed number of rules, and restricted rule language.

## Weaknesses

### Major

- **No explicit regularization for short, interpretable rules.** The paper claims that predicate weights \(\andweight_i\) allow the model to "disable predicates and thus obtain more succinct rules" (line 208), but there is no sparsity penalty (L1, L0 relaxation, or pruning) that drives these weights to zero. The objective (cross-entropy + minimum-support penalty) provides no incentive for short rules — a rule using many predicates that fits the data well will not be penalized. Since rule lists are only interpretable if individual rules are short and few in number, this is a gap between the claimed interpretability contribution and what the method actually enforces. The paper does not report average rule length per method or compare against baselines that explicitly bound rule complexity (e.g., CORELS with max rule size).

- **The default-rule case is not handled.** In standard rule lists, when no rule's antecedent applies, a default (usually the last) rule provides the prediction. In the proposed formulation, if all rules have \(\rulehead_j = 0\) for a sample, all active priorities are zero and the Gumbel-Softmax / argmax has no principled fallback. The paper does not discuss this case, nor how the model handles samples outside the union of all rule conditions.

### Minor

- **Rule-list property after annealing is not verified.** The paper uses temperature annealing so that the Gumbel-Softmax argmax converges toward hard selection, but does not empirically verify that the final model actually satisfies the rule-list property: (a) what fraction of test samples have exactly one rule strongly selected (≈1 weight), (b) whether the selected rule is consistent with a global priority ordering, (c) whether ties in learned priorities cause unstable predictions. Since the method's interpretability claim depends on convergence to a strict rule list, this analysis should be provided.

- **Experimental reporting lacks statistical detail.** The paper reports mean F₁ over 5-fold CV but does not provide standard deviations, confidence intervals, or significance tests (e.g., Wilcoxon signed-rank) for the pairwise comparisons. The ablation reports average improvement but not per-dataset variability. While this is common in the rule-learning literature, the strong claim of "consistently outperforms" would benefit from more rigorous statistical backing.

- **Soft binning function justification is thin.** The function in Eq. 4 is presented as a soft interval indicator with three exponential terms, cited to Yang et al. 2018. The specific coefficients (1, 2, 3 on \(x\) in the denominator) are not derived or justified, and the function's behavior under feature rescaling is not discussed. A brief analysis of why this specific parameterization is chosen over simpler alternatives (e.g., a product of two sigmoids) would improve the method section.

- **One-hot encoding of categorical features is treated as an afterthought.** The paper states categorical features are "one-hot encoded into binary features" (line 302) and then processed by the same soft binning function with learned \(\lowerbound, \upperbound\). On binary {0,1} features, this is unnecessary and can learn spurious thresholds. A dedicated binary predicate (or an explicit note that the soft binning gracefully reduces to a threshold on 0.5) would be cleaner.

### Trivial

- The gradient approximation \(\partial\softrule/\partial\softpred(x_j) \approx \andweight_j / \sum\andweight_i\) (line 235) is stated without showing the exact expression for the relaxed version; providing it would aid reproducibility.
- Hyperparameter values (\(\coverage_{\min}, \coverage_{\max}, \lambda\), temperature schedules) are not specified in the main text, though they may appear in supplementary material not visible in the extraction.

## Nice-to-Haves

- A comparison against ablated versions with pre-discretized features (equal-width bins) would isolate the benefit of learned thresholds.
- Training time / convergence comparison against baselines would be useful for practitioners.
- A sensitivity analysis for key hyperparameters (temperatures, annealing schedule, \(\lambda\)).

## Removed Points

These points are flagged to be removed, treat them with caution:

1. **"Experimental evidence is not verifiable in the provided text"** (Harsh Critic #1, part) — Removed because the figures and tables are loaded via `\input{...}` commands from separate files; they exist in the compiled PDF. The extracted text is a parser artifact, not a paper flaw. The statistical-rigor sub-concern is retained above as a Minor weakness.

2. **"Missing related works" and "missing appendix/proofs"** — Removed per hard rules: these are parser artifacts (appendix/content stripped) or cannot be verified externally.

3. **Missing decision tree comparison** (CART) — Removed. The paper's baselines already cover rule sets and rule lists from the combinatorial and neuro-symbolic literature. Adding decision trees is not necessary given the paper's stated scope.

4. **Criticism about computational complexity** and training time — Removed as a nice-to-have; the paper does not claim runtime efficiency as a contribution.

5. **"Gumbel-Softmax for rule ordering does not guarantee a valid rule list"** (Harsh Critic #3) — Partially removed. The general concern about annealing convergence is retained as Minor (point 3 above). The specific worry about exact floating-point ties is removed as speculative (continuous-valued learned priorities make exact ties astronomically unlikely).

6. **Strengths that are generic or conflict with validated weaknesses** — Removed generic strengths like "addressed an important problem" and "well-motivated" without specific evidence. The remaining strengths are concrete and evidenced.

## Novel Insights

None beyond the paper's own contributions. The reviewers raised useful technical scrutiny (sparsity enforcement, default rule, rule-list verification) but did not uncover a fundamentally different interpretation of the method or its results.

## Suggestions

1. **Add a sparsity penalty** (e.g., L1 on \(\andweight_i\) or a budget constraint on active predicates) to the training objective and report average rule length alongside accuracy. This directly addresses the interpretability gap.

2. **Explicitly handle the default-rule case** — either by adding a default rule with no antecedent conditions as the last rule, or by defining the prediction for samples where no rule applies (e.g., a learned fallback distribution).

3. **Provide a post-training analysis** showing (a) the fraction of test samples where the Gumbel-Softmax argmax weight for the selected rule ≥ 0.99, (b) whether the learned priorities define a consistent global ordering (i.e., sorting by priority and using first active rule matches the model output), and (c) that coverage constraints hold for the hardened model.

4. **Report standard deviations** over CV folds in the main table and include a statistical significance test (Wilcoxon signed-rank) for the pairwise comparison against the next-best method.

5. **Address categorical features more explicitly** — either treat them with an equality predicate instead of the soft binning, or justify why the soft binning on binary one-hot features works correctly.

## Score and Decision

### Round 1 — Bracketing
I queried for weak (≤3), middle (4–7), and strong (≥8) anchors. The weak anchors (scores 1.5–3.0) are papers with fundamental flaws or incomplete evaluations; this paper is clearly stronger. The strong anchors (score 8.0) are about entirely different topics (LLM training, multimodal reasoning) and not comparable. The middle anchors (scores 4.0–5.0) include relevant neuro-symbolic and rule-learning papers. **Initial bracket: between 4.5 and 6.5.**

### Round 2 — Narrowing
I queried for anchors in [4.5, 6.5] and [5.5, 7.5] on differentiable rule learning and neuro-symbolic optimization.

**Anchors read in full:**

| Paper | Avg Score | Round | Comparison |
|---|---|---|---|
| vBEbUTS81u (Explainable Mixture Models) | 4.50 | R2 | Weaker — evaluation on fewer datasets, less novel technical contribution. |
| xD0ivsbBf6 (L-FMLC) | 4.00 | R2 | Weaker — only 3 datasets, post-hoc interpretability, overclaiming claims. |
| 1SnYCZuXnP (γILP) | 5.00 | R2 | Comparable strength — tackles harder problem (visual rule learning) but with significant caveats (LLM oracle, limited baselines). |
| 26Msp6pV5i (NS-FCN) | 5.50 | R2 | Similar strength — clear technical contribution, broad evaluation, similar concerns about evaluation rigor and hyperparameter sensitivity. |
| QBZoAChPv5 (FCNN) | 4.50 | R2 | Weaker — limited novelty (incremental over prior neural ILP), narrow evaluation on small benchmarks. |

The paper under review is clearly stronger than the 4.0–4.5 anchors (more extensive evaluation, clearer technical contribution, better writing). It is comparable to the 5.5 anchor (NS-FCN) — both have well-motivated methods with clear innovations, both have limitations in evaluation rigor and some unaddressed technical gaps. The NeuRulLs paper has a broader evaluation (20 datasets vs. NS-FCN's mix) but the NS-FCN tackles a harder problem (missing value imputation + rule discovery jointly).

**Final score: 5.5.** The paper makes genuine contributions (learned discretization in rule lists, relaxed conjunction) and provides reasonably strong empirical evidence, but the gaps around sparsity regularization and rule-list verification prevent a higher score.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Accept</decision>