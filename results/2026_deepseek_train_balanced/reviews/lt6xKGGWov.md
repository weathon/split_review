## Summary

MINERVA proposes a filter-based feature selection method that uses neural estimation of mutual information (MINE) to evaluate subsets of features as an ensemble, rather than scoring features one at a time. The key idea is to learn per-feature weights p via a loss function combining the negative MINE estimate (of I(p⊙X; Y)) with L1 sparsity and L2 norm regularization, and select features whose weights survive. The paper proves (Lemma 1) that pairwise methods necessarily fail on equality-based dependencies (Y = 𝟙{X_{k0}=X_{k1}}) and shows empirically that MINERVA succeeds on two synthetic problems where sklearn mutual information, HSIC Lasso, and Boruta all fail.

## Strengths

- **Lemma 1 provides a clean formal proof of a genuine limitation of pairwise feature selection methods.** Lines 196–208 prove that for the dependence Y = 𝟙{X_{k0}=X_{k1}}, each individual feature has zero mutual information with Y while the pair (X_{k0}, X_{k1}) jointly has positive MI. This shows the failure is in-principle, not just empirical, and motivates the paper's ensemble-based approach. This is the paper's strongest contribution.

- **The loss function design with scale-invariant L1 regularization is principled.** Equation (5) uses ‖p/‖p‖₂‖₁ as the sparsity term — the L1 norm of the *normalized* weight vector — which decouples the sparsity penalty from the overall scale of p. Combined with the (‖p‖₂ − a)² term that prevents weights from diverging, this addresses both sparsity and stability in a specific, motivated way.

- **Exact selection is demonstrated on two synthetic problems where three strong baselines all fail.** Tables 1 and 2 (lines 165 and 212) show MINERVA achieving exact selection in both experiments while sklearn's mutual information, HSIC Lasso (pyHSICLasso), and Boruta produce non-exact selections. Table 3 (line 216) further shows that a gradient boosting model trained on MINERVA's selected features outperforms models trained on the baselines' selections on the same synthetic problem. This provides concrete evidence that the method solves the identified problem.

## Weaknesses

### Fatal
None.

### Major

- **The evaluation tests only one type of dependency structure (equality-based), making it impossible to assess the method's generality.** Both Experiment A and Experiment B are built around the same core dependence (Y depends on whether X_{k0} = X_{k1}). The paper claims MINERVA "captures sophisticated relationships between features and targets" (abstract, line 17) and "is capable of performing an exact selection, whereas other existing methods fail" (line 18), but only demonstrates this for one specific failure mode of pairwise methods. No other interaction patterns (XOR, parity, AND/OR gates on binary features, multiplicative interactions, hierarchical dependencies) are tested. No real-world benchmarks with known relevant feature sets are included. The paper acknowledges using synthetic data (line 152), but the gap between the scope of the claims and the breadth of the evidence is substantial. This limits the paper's contribution to a proof-of-concept for one family of dependencies rather than a validated general-purpose method.

- **The comparison does not test whether MINERVA retains performance on problems where pairwise methods *can* work.** Because Lemma 1 establishes that pairwise methods *provably* fail on the tested problems, MINERVA's success on these problems is a necessary sanity check but not evidence that it is generally useful. A critical missing experiment is to test MINERVA on standard feature selection problems where individual features carry information about the target, to verify that the ensemble formulation and regularization do not degrade selection quality in ordinary settings.

### Minor

- **Inconsistency between Algorithm 1 and the textual description of the stopping criterion.** Algorithm 1 (lines 133–144) uses "until convergence" for both training phases with no threshold, patience, or quantitative condition specified. The text (line 124) gives a specific criterion: "stop when the estimated mutual information between the weighted features and the targets becomes smaller than the mutual information that corresponds to the minimiser θ̂." The algorithm should reflect this criterion. Additionally, the return statement `{i: |\overline{p_i}| > 0}` (line 145) uses `\overline{p_i}` which is undefined — the text says "non-null entries of p" (line 124), and since L1 regularization pushes weights toward zero but rarely to exactly zero, a practical threshold must be specified.

- **No hyperparameter sensitivity analysis.** The loss function (equation 5) has three hyperparameters (c₁ for L1 sparsity strength, c₂ for L2 norm penalty, and the target norm a set to √d). The paper reports results for a single setting with no ablation or sensitivity study. Because the L1 and L2 terms interact through the normalization ‖p/‖p‖₂‖₁, the optimization landscape is non-trivial, and the reader cannot assess whether the reported results are robust or require careful tuning on each problem.

- **No computational cost reporting.** MINE requires training a neural network via gradient ascent, which is substantially more expensive than the histogram-based KSG estimator or the closed-form HSIC Lasso. The paper does not report runtime, iteration counts, sample complexity, or convergence speed. For a method positioned as a practical filter, this omission makes it difficult for readers to assess the practical trade-off.

### Trivial
- The text has a few typographical errors (e.g., "fundmentals" line 19, "featurte" line 19, "threhsold" line 184, "implmented" line 235, "bechmark" line 233) that should be corrected.

## Nice-to-Haves

- Adding a controlled ablation that compares MINERVA against a version using MINE to estimate I(X_i; Y) individually (i.e., MINERVA reduced to a pairwise method) would directly attribute the success to the ensemble formulation rather than to MINE itself.
- Testing on 2–3 structurally different interaction patterns (e.g., XOR, multiplicative interactions) would broaden the evidence base considerably.
- Including at least one real-data benchmark (e.g., from the UCI repository) with known relevant features would strengthen the practical case.

## Removed Points
These points were flagged by reviewers but removed or downgraded after verification against the paper:

- *"Baselines are set up to fail by construction"* — This is the paper's thesis, not a flaw. Lemma 1 proves pairwise methods *cannot* succeed on these problems; the experiments confirm this. A paper demonstrating that its method solves a problem others provably cannot is not committing an unfair comparison.
- *"Overstated claims about existing methods"* — Lines 194 and 237 state that baselines failed on *these specific experiments*, which is factually accurate. The abstract says "we give examples... and demonstrate" — in context of the examples shown. No overclaim.
- *"Missing related work"* — Removed per policy: not verifiable without external sourcing.
- *"No discussion of limitations"* — The paper frames the work as proof-of-concept on synthetic data (line 152); this is an acknowledgment of scope rather than a missing limitations section.

## Novel Insights

None beyond the paper's own contributions. The paper cleanly identifies a specific failure mode of pairwise feature selection (equality-based dependencies), gives a formal proof, and proposes a plausible neural solution. This is the central contribution; the reviews do not surface insights beyond what the paper itself provides.

## Suggestions

1. **Broaden the evaluation to at least 2–3 structurally distinct interaction patterns** (e.g., XOR, multiplicative interactions, hierarchical dependencies) to demonstrate that MINERVA solves a class of problems rather than one specific case.
2. **Fix the inconsistency between Algorithm 1 and the text** — replace "until convergence" with the specific stopping criterion described in line 124, and clarify the return condition for feature selection (including any threshold used for near-zero weights).
3. **Add a hyperparameter sensitivity study** for c₁ and c₂ (e.g., grid search over a range of values) to assess robustness.
4. **Report wall-clock time or iteration counts** for MINERVA relative to baselines, so readers can assess the computational overhead.
5. **Include at least one experiment where individual features carry information about the target** (a standard setting where pairwise methods work) to verify MINERVA does not lose performance in the ordinary case.

## Score and Decision

MY FINAL SCORE: <score>4.5</score>
MY FINAL DECISION: <decision>Reject</decision>