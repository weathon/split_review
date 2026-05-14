Now I have a thorough understanding of the paper and anchor papers. Let me compose the final review.

---

## Summary

This paper proposes a Covariance-Adjusted Support Vector Machine (CSVM) that incorporates per-class data covariance into SVM classification. The key idea is to whiten each class separately using Cholesky decomposition of the class covariance matrix, perform SVM in the resulting "Euclidean space," and then reverse-transform to derive class-specific margin relationships in the original input space. To handle the unknown population covariance, the authors propose an iterative SM Algorithm that assigns pseudo-labels to test data, expands the training set, and recomputes covariances until convergence. The method is evaluated on five binary classification datasets against standard SVM kernels and PCA/ZCA whitening approaches.

## Strengths

- **Well-motivated problem.** The observation that standard SVM ignores per-class covariance structure and that different classes may have substantially different dispersions is valid and important. The idea of adjusting the margin to account for class-specific covariance is intuitively compelling and addresses a genuine gap in standard SVM practice.

- **Practical direction is clear.** Despite theoretical imprecision, the core algorithmic idea — per-class Cholesky whitening followed by SVM, with iterative covariance refinement — is straightforward and implementable. The paper connects Mahalanobis distance, whitening, and SVM in a way that could inspire further work.

- **Acknowledges own limitations.** The conclusion section (Section 6) honestly notes that the SM algorithm is heuristic, that computational complexity is higher than standard linear SVM, and that perfect classification is not yet achieved. This self-awareness is commendable.

## Weaknesses

### Fatal

None. The core idea (class-specific covariance adjustment for SVM) is not fundamentally invalid, and the problems below, while serious, are addressable with major revisions.

### Major

- **Test-data leakage invalidates the experimental evidence.** The SM Algorithm (Section 3) iteratively assigns pseudo-labels to test data (step f), adds those instances to the training pool (step g), recomputes covariances, and repeats until test-label assignments stabilize. The final classifier is then evaluated on this same test data (Section 5). This is a transductive procedure — the model has unrestricted access to the test distribution during training. The comparison against standard inductive SVMs (linear, RBF, sigmoid, polynomial, PCA-SVM, ZCA-SVM) that never see test data is fundamentally unfair. Any apparent performance gain could be entirely attributable to this leakage rather than to any merit of the covariance-adjustment formulation. The paper provides no truly held-out test set and no cross-validation strategy that isolates the test data from the SM iteration. This renders the empirical claims in Section 5 untrustworthy as evidence for the method's superiority.

- **The theoretical derivation has a significant gap.** Equations 3 define two separate transformations using different per-class Cholesky factors, mapping data from each class into two distinct coordinate systems. The paper then writes a single SVM optimization in "the Euclidean space" (Eqs. 4–7) without defining how these two transformed datasets are unified into one common coordinate system. In practice, one can concatenate the separately whitened class data — and the SM algorithm implicitly does this — but the paper never justifies or even acknowledges this step. Lemma 2.2 correctly observes that reverse-transforming yields two separate optimization problems, but the paper does not explain how the SM algorithm resolves this into a single decision rule beyond the heuristic bias-adjustment in step (e). The gap between the claimed "methodology to perform Support Vector Classification in Non-Euclidean Spaces by incorporating data covariance into the optimization problem" (Abstract) and the actual heuristic algorithm is substantial.

### Minor

- **The SM algorithm's bias-adjustment step lacks justification.** Step (e) of the algorithm retains the weight vector θ_input from a standard linear SVM on the original data and adjusts only the bias θ_0 to match a margin ratio computed from θ_Euclidean. There is no derivation or argument for why the weight vector should remain unchanged or why bias-only adjustment is sufficient. The link between θ_Euclidean (obtained in whitened space) and the final classifier (in input space) is asserted rather than derived.

- **No error bars or multiple splits.** All results in Tables 1–4 and Figures 1–3 are from a single 80/20 split with no standard deviations, confidence intervals, or cross-validation. The accuracy differences between CSVM-Cholesky and the best baseline are often small (e.g., 0.974 vs. 0.956 on Breast Cancer; 0.744 vs. 0.738 on Red Wine) and could fall within the noise of a single random split, even setting aside the test-leakage problem.

- **Terminology imprecision.** The paper repeatedly refers to the input/statistical space as "non-Euclidean." However, ℝ^n equipped with a Mahalanobis inner product is still an inner product (hence Euclidean) space — it just uses a non-standard metric. The practical point (standard SVM's L2 metric is suboptimal when the data's natural metric is covariance-scaled) is valid, but the theoretical framing as "SVM is invalid in non-Euclidean space" overstates the case and conflates metric choice with geometric structure. Lemma 2.3's claim that "KKT boundary conditions are not valid in the input space" is similarly imprecise: KKT conditions are properties of convex optimization problems and remain valid under any choice of metric; the metric merely changes the geometry of the margin being maximized.

### Trivial

- **Threshold for SM convergence unspecified.** The convergence criterion (Section 3, step 3a) states "changes in test data labels are below a certain threshold" without specifying the threshold value, making exact reproduction difficult.

## Nice-to-Haves

- A comparison against transductive SVMs or semi-supervised methods that also have access to unlabeled test data would be essential for a fair evaluation, if the SM algorithm's transductive nature is to be preserved.
- A derivation showing whether the SM algorithm's bias-only adjustment can be motivated from first principles (e.g., as a partial solution to a joint optimization) would strengthen the theoretical contribution.

## Removed Points

These points are flagged to be removed — treat them with caution.

- **Harsh Critic claim: "The proposed transformation and SVM formulation are mathematically inconsistent" (claiming fatal error).** REMOVED as a fatal-level claim. While there IS a genuine gap in how the two per-class transformations are unified, the practical approach of concatenating class-whitened data is standard and the paper's direction is not nonsensical. Downgraded to Major (theoretical imprecision) rather than Fatal.

- **Harsh Critic claim: "The SM algorithm is ad-hoc and lacks theoretical or empirical justification for its key design choices" (claiming fundamental lack of reasoning).** PARTIALLY REMOVED as a standalone fatal/major claim. The paper does provide motivation (the margin ratio from the Euclidean SVM should inform the input-space classifier), but the specific mechanism (bias-only adjustment) is under-justified. Kept as Minor.

- **Harsh Critic claim: "SVM optimization and KKT conditions are formulated in an inner-product space... This claim is overdrawn."** Downgraded from a major criticism to a Minor terminology issue. The practical point (standard SVM may be suboptimal without covariance adjustment) has merit regardless of the terminology debate.

- **Strength Finder claim: "Rigorous vector-space justification for covariance-adjusted SVM."** REMOVED. The derivation is not rigorous given the unaddressed gap of unifying two per-class transformations.

- **Strength Finder claim: "Strong empirical validation across diverse domains."** REMOVED. The empirical validation is compromised by test-data leakage.

- **Strength Finder claim: "Clarifies relationship to prior work and existing whitening practices."** RETAINED in modified form. The paper does make reasonable observations about class-wise vs. global whitening, but this is more of a discussion point than a core strength.

- **Harsh Critic claim about lacking separate held-out set for SM convergence.** Already covered by the Major test-leakage weakness.

- **Harsh Critic claim about missing related work.** REMOVED per instructions (cannot verify external sources).

## Novel Insights

The paper's most genuinely novel observation is the derivation that, after per-class Cholesky whitening followed by SVM, the margin ratio between classes in the input space depends on the ratio of inverse covariance matrices (Equation 14). This provides a concrete, testable prediction: the decision boundary should not be equidistant from the two classes but should split the margin proportionally to class dispersion. This insight is independent of the SM algorithm's issues and could be valuable even if evaluated differently.

## Suggestions

- **Fix the evaluation protocol immediately.** Either (a) keep a truly held-out test set that the SM algorithm never touches, using only training data for the iterative procedure and a separate validation set for convergence monitoring, or (b) reframe the method explicitly as transductive and compare against transductive/semi-supervised SVMs. Without this fix, no amount of additional theory or datasets can rescue the empirical claims.
- **Articulate the unification step.** Explicitly state that after per-class whitening, the transformed data from both classes are concatenated into a single dataset on which a single SVM is trained. This closes the most glaring gap in the theoretical derivation.
- **Run multiple random splits with error bars** to establish whether the observed improvements exceed sampling noise, especially given the often small margins.
- **Provide a derivation or at least a principled argument** for why adjusting only the bias (and not the weight vector) is appropriate when transferring the margin ratio from Euclidean space to input space.

## Score and Decision

**Anchor comparison:**

- **nn5Vf6GEsV (6.40, Accept Poster):** A theoretical framework for kernel regression with rigorous proofs for special cases, thorough empirical validation across large-scale datasets (CIFAR-5m, SVHN, ImageNet), and clear novelty. Our paper is substantially weaker on both theoretical rigor and experimental validation.
- **Y54P2BBPPh (5.33, Accept Oral):** High-dimensional analysis with theoretical guarantees and well-executed experiments. Our paper's theory is less rigorous and experiments less trustworthy.
- **bp9DOHb1mk (5.00, Accept Poster):** A geometric framework for linear classification with 27 datasets, clearer theoretical structure, and more convincing empirical evidence. Our paper has a weaker evaluation and less coherent theory.
- **HuuCWjlJuQ (4.29, Reject):** An empirical study on Mahalanobis-based OOD detection. Also criticized for unfair comparisons (auxiliary OOD data) and limited theoretical grounding. Our paper shares the comparison-fairness problem but through a more severe mechanism (direct test-data leakage rather than auxiliary data). Our paper is somewhat weaker.
- **Oe5Min0Na2 (2.50, Reject):** Mathematical formalism that obscures simple ideas, weak empirical evaluation, overclaiming. Our paper overclaims less egregiously and has a clearer practical direction, making it stronger.
- **zNH3Sf404X (1.33, Reject):** Fundamentally flawed with extreme class imbalance issues. Our paper is clearly stronger.

The paper's interesting core idea (per-class covariance adjustment) could, with major revisions, become a solid contribution. However, the current submission has a critical experimental flaw (test-data leakage) that invalidates the empirical evidence, coupled with theoretical imprecision in the derivation. These are not minor issues — they require substantial reworking of both the experimental protocol and the mathematical exposition. The paper falls below the 4.29 anchor (HuuCWjlJuQ) due to the more severe nature of the test-leakage problem, but above the 2.50 anchor (Oe5Min0Na2) because the core idea is clearer and more actionable.

MY FINAL SCORE: <pineapple>3.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>