Now let me write the final consolidated review.

## Summary

This paper proposes LiCE, a method that encodes a Sum-Product Network (SPN) into a Mixed-Integer Optimization (MIO) formulation to generate counterfactual explanations. The key technical contribution is an MIO-compatible bounded approximation of SPN computation (replacing log-sum-exp with a max whose error is ≤ log|children|), which allows integrating likelihood-based plausibility directly into the optimization alongside validity, similarity, sparsity, actionability, and causality constraints. The paper evaluates LiCE on three datasets (GMSC, Adult, German Credit), comparing against DiCE, VAE, C-CHVAE, FACE, and PROPLACE.

## Strengths

- **Novel SPN-to-MIO encoding** (Section 3, Eqs. 1–7): The paper formulates the exact computation of an SPN in MIO-compatible linear constraints through a log-space transformation and a bounded max-approximation for sum nodes (error ≤ log|children|). This goes beyond prior MIO-based plausibility methods (e.g., PlaCE's GMM) which cannot handle categorical features or non-linear classifiers. The encoding is a clean, non-trivial contribution of independent interest.

- **100% validity and actionability for MIO variants** (Table 1): LiCE(opt) and MIO achieve 100% valid and 100% actionable counterfactuals on all three datasets, compared to e.g., DiCE's 3.4% actionable on Credit or C-CHVAE's 8.8%. The MIO-based guarantee of constraint satisfaction by design is a measurable reliability advantage over sampling-based or heuristic approaches.

- **Strong combined performance on plausibility, similarity, and sparsity** (Table 2): LiCE achieves the best negative log-likelihood on all three datasets while matching or beating baselines on similarity (MAD distance) and sparsity (number of changed features). For example, on Credit, LiCE(opt) achieves NLL 30.26 vs. MIO(+spn) 47.54 and DiCE(+spn) 51.64, while changing only 2.79 features on average versus DiCE's 8.66. On GMSC, LiCE(med) achieves NLL 18.04 vs. the next-best VAE at 23.13.

- **Correction of a categorical-feature encoding bug** (lines 236–237): The paper identifies and fixes an issue in Russell et al. (2019)'s mixed-polytope encoding where the first categorical value mapped to the continuous variable would produce non-binary outputs for non-monotone neural networks, replacing it with a standard one-hot encoding.

## Weaknesses

### Fatal

None.

### Major

- **The plausibility metric is aligned with what LiCE optimizes, and no independent validation is provided.** The paper operationalizes plausibility as SPN-estimated log-likelihood, LiCE optimizes to maximize SPN-estimated log-likelihood (either in the objective or as a constraint), and the primary evaluation metric (Table 2, NLL column) is also SPN-estimated log-likelihood. While the evaluation uses 5-fold CV (evaluation SPN ≠ optimization SPN), both are trained on the same data distribution. This raises a concern about whether LiCE finds genuinely plausible counterfactuals that lie on the data manifold, or merely counterfactuals that score well on a specific density estimator. The paper does not provide independent validation — such as NLL estimated by a fundamentally different density estimator family (KDE, normalizing flow), a non-parametric plausibility proxy (distance to nearest training neighbors), or human evaluation. The claim that LiCE generates more "plausible" counterfactuals would be substantially stronger with such evidence. *This concern is partially mitigated by the fact that LiCE also excels on non-circular metrics (similarity/sparsity in Table 2) and the combined claim (plausibility + proximity + sparsity) is supported by multiple metrics, but the plausibility component specifically lacks independent verification.*

- **Confounded comparison across differing subsets of factuals.** The paper acknowledges (Table 2 caption, line 368, and line 398) that different methods generate valid CEs for different subsets of factuals, and that "direct comparison between methods is non-trivial." The main results table (Table 2) nonetheless reports aggregate means over whatever factuals each method succeeded on. This can be actively misleading: a method that succeeds on only 3.4% of factuals (DiCE on Credit actionable) solves only the easiest cases, potentially making its metrics look deceptively good (or bad). Conversely, LiCE(opt) succeeds on 100% of factuals including hard ones. The paper does not address this by e.g., reporting results restricted to factuals that all methods solve, or by per-factual matched comparisons. This is especially problematic for LiCE(med), which only succeeds on 53.6% of GMSC factuals while achieving the best NLL — a result that could partly reflect selection bias rather than method quality.

### Minor

- **Max-approximation for sum nodes is not empirically analyzed.** The paper replaces the sum-node computation (log-sum-exp) with a max over children (Eq. 6), provides an analytical error bound (≤ log|children|), and notes that hard EM training would make it exact (lines 226-228). However, it does not empirically quantify the approximation error on actual trained SPNs (e.g., comparing exact vs. approximate log-likelihoods on held-out data). Since the approximation changes the semantics from a weighted mixture to a selection model, the reader cannot assess whether the error is negligible or material in practice, or how it interacts with the likelihood-threshold constraint in LiCE(med).

- **Only one classifier architecture is tested.** The experiments use a 2-hidden-layer neural network with ReLU activations (line 314). While the OMLT library supports gradient-boosted trees and other architectures, no results are shown for different classifier types. The Table 1 claim of "model-agnostic" (with star: "as long as the classifier can be expressed using MIO") is technically qualified but empirically thin.

- **No runtime or solver statistics are reported.** The paper mentions a 2-minute time limit and notes computational overhead (lines 407-408, 415), but provides no actual solve times, iteration counts, or distribution of solution times across factuals. For practical deployment, understanding whether typical solve times are seconds or minutes is essential.

- **Limitations discussion is too brief** (lines 406-408): only mentions computational overhead. It does not discuss the potential evaluation concerns, the max-approximation issue, or the confounded comparison — issues that a reader should be aware of when interpreting the results.

### Trivial

- The α=0.1 selection is heuristically justified in the text (line 285: "since features are normalized to [0,1] and log-likelihood often takes values in the [-100, -10] range") but no sensitivity analysis is provided. A sweep over α would strengthen confidence in the choice.

## Nice-to-Haves

- **Statistical testing:** Reporting paired tests (e.g., Wilcoxon signed-rank) on the subset of factuals that all methods can solve would help address the confounded-comparison concern.
- **Ablation analysis on difficult factuals:** The comparison of MIO(+spn) vs LiCE(opt) (Table 2) already serves as an ablation; deeper analysis showing where the SPN integration helps most (e.g., on specific factuals) would clarify the value of the contribution.
- **Independent plausibility validation:** Using a different density estimator (KDE, normalizing flow) or a non-parametric proxy (distance to k nearest neighbors) as an additional evaluation metric would substantially strengthen the core claim about plausibility.
- **Varying the MIO time limit** to show the trade-off between solution quality and computational cost.

## Removed Points

These points are flagged to be removed, treat them with caution:

- **"500 testing samples vs 100 factuals inconsistency" (from Harsh Critic, Section-by-Section notes):** Removed because these numbers are consistent under 5-fold cross-validation: 5 folds × 100 factuals per fold = 500 testing samples evaluated across all folds. This is a natural reading given the 5-fold CV setup stated in the table caption.
- **"The choice of α=0.1 is not justified" (from Harsh Critic, Places to Improve):** Removed because the paper does provide a justification (line 285: range normalization to [0,1] and typical log-likelihood range). A sensitivity analysis would strengthen the paper but the absence is not a weakness.
- **"Test set size is described as '500 testing samples'... the reader cannot determine how many factuals were actually evaluated" (from Harsh Critic):** Removed as factually incorrect — the numbers are consistent under 5-fold CV as noted above.
- **Generic strengths from Strength Finder:** The strength "addresses an important problem" is dropped as generic. All other strengths verified against the paper are retained in the Strengths section above.

## Novel Insights

None beyond the paper's own contributions. The reviews did not surface a perspective on the work that the authors themselves do not articulate.

## Suggestions

1. **Address the confounded comparison:** Report results on the subset of factuals solvable by all methods (or at least by all MIO-based methods), enabling a fairer comparison. Include per-factual matched comparisons where possible.
2. **Provide independent plausibility validation:** Evaluate CEs using a different density estimator family (e.g., KDE or a normalizing flow) that LiCE does not optimize against. Alternatively, use a non-parametric proxy such as average distance to k nearest training-set neighbors.
3. **Empirically analyze the max-approximation error:** Compare exact SPN log-likelihoods against the max-approximated values on held-out data to show the approximation is negligible in practice.
4. **Report runtime statistics:** Provide median solve times and the distribution of solution times across factuals to help readers assess practical applicability.
5. **Test on at least one additional classifier architecture** (e.g., gradient-boosted trees or a larger network) to substantiate the model-agnostic claim empirically.

## Score and Decision

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>