Now I have enough information for calibration. Let me write the final consolidated review.

Based on my reading and calibration:
- **Round 1 bracket**: The paper sits between the weak anchors (1.5-2.5) and the middle anchors (3.5-5.3). It's clearly below the papers scoring 4-5+ which have rigorous theory or thorough experiments. It's closer to the 1.5-3.5 range.
- **Round 2 narrowing**: Compared to FINDER (2.50) — CSVM has a less rigorous mathematical foundation with a genuine conceptual gap, and weaker experimental methodology. Compared to Spatial Sign LDA (3.33) — CSVM lacks theoretical guarantees and has a less polished derivation. The paper is most comparable to the 2.0-2.5 anchor papers.

**Final score: 2.5** — Below the ICLR acceptance threshold.

Now let me write the review.

## Summary
2-3 sentence summary.

## Strengths
Filtered from strength finder. I need to:
- Remove generic strengths
- Keep concrete, evidenced strengths
- Resolve conflicts with weaknesses

## Weaknesses
Verified against the paper.

## Removed Points
Points removed with justification.

---

Let me draft this.

Removed strengths from Strength Finder:
1. "Principled derivation of class-specific optimization problems" — This is partially valid but weakened by the conceptual issue about how differently-transformed classes are handled. I'll demote this and not list it as a separate strength.

2. "Empirical outperformance" — The improvements are very small and without statistical significance testing. The margins are 0.002 to 0.026. These could easily be noise. Also the strength conflicts with the verified weakness about weak experiments. REMOVE.

3. "Demonstration that margin ratio depends on class covariance" — This is basically stating a mathematical consequence of Eq 14, which follows straightforwardly from the definitions. Not particularly novel or insightful. REMOVE (generic).

4. "Iterative SM algorithm" — The strength says it "addresses a key practical limitation" but the paper itself acknowledges it's a heuristic. The algorithm is essentially self-training without convergence guarantees. This is more of a claimed contribution that doesn't fully deliver. REMOVE (conflicts with weakness about no convergence analysis).

5. "Vector-space explanation of why whitening improves SVM performance" — The paper does provide this explanation (whitening transforms to Euclidean space where SVM is valid). This is a genuine strength that is concrete and specific. KEEP.

So the one real strength is:
- The paper provides a clear vector-space explanation of why whitening improves SVM performance: whitening transforms data from non-Euclidean statistical space to Euclidean space, where SVM's distance-based formulation is valid.

Let me also consider if there are other genuine strengths I missed. The paper does acknowledge its own limitations clearly, which is a positive signal. But that's more of a presentation quality than a strength of the contribution itself.

Actually, I think the strength about "principled derivation" has some merit even if flawed. The paper does mathematically derive that separate optimization problems emerge for each class when covariance is considered. The derivation itself (Eq 8-13) is mathematically valid as a formal manipulation, even if the interpretation is problematic. Let me keep a qualified version of this.

Revised strengths:
1. The paper provides a vector-space explanation of why whitening improves SVM, framing it as a transformation from non-Euclidean statistical space to Euclidean space.
2. The formal derivation showing that incorporating class-specific covariances into SVM optimization leads to distinct optimization problems per class (Eq 8-13) is a clear conceptual contribution, even if its practical implications need further development.

Now for weaknesses:

**Fatal**: None. The conceptual issue is major but not fatal — the method is well-defined enough to be implemented and tested (as the paper does).

**Major**:
1. Conceptual gap in handling class-specific transformations — The paper transforms each class with its own Cholesky factor (Eq 3) but doesn't explain how SVM operates on pooled data from different transformation spaces. The algorithm's step 2c is ambiguous.
2. No comparison against the most relevant baselines (MCVSVM, MD-TSVM, etc.) despite citing them.
3. Experimental evaluation lacks statistical rigor — no confidence intervals, no error bars, single 80:20 split.
4. No hyperparameter details reported (C, kernel parameters, tuning procedures).
5. SM algorithm presented as heuristic with no convergence analysis.

**Minor**:
1. Claim about KKT conditions not being valid in non-Euclidean spaces is overstated/misleading.
2. Performance improvements are very small and may not be practically significant.

**Trivial**:
- Notation inconsistencies

Let me now write the final review.## Summary

This paper argues that standard SVM is valid only in Euclidean spaces while the input (statistical) space is non-Euclidean due to data covariance. It proposes to transform data to Euclidean space using class-specific Cholesky decompositions of covariance matrices, perform SVM there, and reverse-transform to obtain classifiers in the original space. The paper derives two separate optimization problems per class, shows the margin ratio depends on class covariances, and proposes an iterative SM algorithm to estimate population covariances without test labels. Experiments on five datasets compare CSVM against linear, RBF, sigmoid, polynomial SVMs, and PCA/ZCA whitening.

---

## Strengths

- **Vector-space explanation for why whitening improves SVM performance.** The paper provides a clear geometric rationale (Section 2, Equations 1–3): whitening via Cholesky decomposition transforms data from the covariance-dependent "statistical space" to a Euclidean space where SVM's distance-based formulation is valid. This explanation (Section 4) goes beyond the usual empirical observation that whitening helps, and explicitly connects Mahalanobis distance to a change of vector space. The framing of whitening as a space transformation rather than just a preprocessing trick is a useful conceptual lens.

- **Formal derivation of class-specific optimization problems.** The paper mathematically works through the implication of using class-specific covariances in SVM optimization (Equations 8–13), showing that doing so yields two distinct optimization problems rather than one. Lemma 2.2 (N classes → N classifiers in input space) and Lemma 2.3 (margin ratio depends on intra-class covariance) draw a clean logical chain from the Mahalanobis distance definition to the structural consequence that the standard SVM's single-classifier construction need not hold when class covariances differ. Whether or not the practical implementation fully delivers on this insight, the derivation itself is a legitimate conceptual exercise.

---

## Weaknesses

### Fatal

None. The method is implementable and produces concrete outputs; the conceptual issues are significant but the paper does not collapse completely.

### Major

- **Unresolved ambiguity in how the class-specific transformations are reconciled for SVM training.** The paper transforms each class with its *own* inverse Cholesky factor (Equation 3), producing points in two different coordinate systems. Step 2c of the SM algorithm states "Perform support vector classification on Train_1 and Train_{-1} data in the Euclidean space" without specifying how SVM operates on pooled data that have undergone different linear transformations. Since SVM relies on a common inner product between all pairs of points, the paper needs to explain what inner product is being computed between a point transformed by Ψ₁⁻¹ and a point transformed by Ψ_{-1}⁻¹, and why this is valid. The algorithm instead resorts to running a separate linear SVM on the original data (step 2d) and only using the Euclidean-space SVM to compute the margin ratio (step 2e), yet the connection between the two SVMs is never formally justified. This is not a fatal flaw — the procedure is concrete enough to run — but it is a significant conceptual gap that undermines the paper's claim of having a principled mathematical foundation.

- **No comparison against the most directly relevant baselines.** The paper cites four variance-adjusted SVM variants (MCVSVM — Zafeiriou et al. 2007, MD-TSVM — Peng & Xu 2012, MD-BLSSVM — Ke et al. 2018, maxi-min margin machine — Huang et al. 2004) and states that prior work has "gaps in application of appropriate vector spaces and dimensional inconsistencies." Yet none of these methods are included as baselines in the experiments. The comparisons are against standard linear/RBF/sigmoid/polynomial SVMs and PCA/ZCA whitening — baselines that do not use label information in preprocessing, whereas CSVM uses class labels to compute class-specific covariance matrices. Including at least MCVSVM (the most cited prior work on class-variance-adjusted SVM) is essential to support the claim that CSVM addresses limitations of prior methods.

- **Experimental evaluation lacks statistical rigor.** All reported metrics (accuracy, precision, recall, F1, AUC) are point estimates from a single 80:20 train-test split, with no confidence intervals, error bars, or significance tests. The claimed improvements are very small (e.g., Breast Cancer accuracy 0.974 vs. 0.956; Pulsar accuracy 0.981 vs. 0.979; Red Wine AUC 0.75 vs. 0.74 for ZCA). On the OSHA dataset, CSVM's accuracy (0.752) is *lower* than RBF (0.760). Without multiple trials or cross-validation, these differences could easily arise from a favorable data split. A single train-test split with no variance estimate is below the standard expected for a machine learning methods paper.

- **No hyperparameter details reported.** The paper does not state the SVM regularization parameter C, kernel parameters for RBF/sigmoid/polynomial baselines, or whether any hyperparameter tuning was performed for any method. This makes the results impossible to reproduce and raises concerns about fair comparison — if baselines used default parameters while CSVM was tuned (or vice versa), the comparison is invalid.

- **SM algorithm is presented without convergence or correctness analysis.** The iterative SM algorithm (Section 3) relabels test data using the current classifier, then recomputes class covariances from the augmented training set. This is a self-training procedure with no analysis of convergence properties (the stopping criterion in step 3 is specified but not validated experimentally — e.g., how often does it converge, to what solution?), no comparison against standard semi-supervised approaches (transductive SVM, Laplacian SVM), and no check on a held-out set to verify that the iterative covariance estimation actually improves the classifier rather than reinforcing its own biases. The paper itself acknowledges in the conclusion that the algorithm is "heuristic," but does not provide the empirical investigation that a heuristic requires (e.g., tracking covariance estimates or label assignments across iterations).

### Minor

- **The claim that KKT boundary conditions are "not valid" in non-Euclidean spaces is overstated.** KKT conditions are properties of convex optimization problems, not of the geometry of the input space. SVM's optimization problem is convex regardless of the feature representation. The paper's actual point — that the *margin ratio* depends on class covariances, so the *interpretation* of the margin changes — is worth making, but framing it as a validity issue with KKT conditions is misleading.

- **The reported performance improvements are very small in absolute terms and may lack practical significance.** On 4 of 5 datasets, CSVM's accuracy advantage over linear SVM is 0.2–2.6 percentage points. On the Diabetes dataset, CSVM, linear SVM, RBF SVM, PCA whitening, and ZCA whitening all report AUC = 0.74 — identical. The practical value of such marginal gains, especially given the added complexity of the SM algorithm, is unclear.

- **The paper does not characterize the datasets** — no sample sizes, feature dimensions, or class balance information is provided — making it difficult to assess the scope and generalizability of the results.

- **Algorithm pseudocode is ambiguous at steps 2c and 2d.** Step 2c performs SVM on differently-transformed data (see major weakness 1), while step 2d performs a *separate* linear SVM on the original data. The relationship between the two is given only as a ratio adjustment for θ₀, but it is unclear why both SVMs are needed and how they interact theoretically.

### Trivial

- Some notation is used inconsistently (e.g., θ appears in both Euclidean-space and input-space contexts without explicit redefinition).
- The text contains several minor grammatical issues (e.g., "iteratively iteratively" on page 5).

---

## Nice-to-Haves

- The iterative SM algorithm would benefit from a thorough empirical analysis showing convergence behavior across datasets (number of iterations needed, whether the covariance estimates stabilize, comparison against a non-iterative baseline using only training-data covariances).
- Adding widely-used benchmark datasets with reported sample sizes and dimensionalities would improve reproducibility assessment.
- A discussion of when class-specific whitening is expected to help versus when a pooled covariance (as in LDA) would suffice would strengthen the paper's practical guidance.

---

## Removed Points

*These points were flagged during review but removed with justification:*

- **"ROC curves appear to be hand-drawn or schematic"** (Harsh Critic): The AUC values are reported in clear tables below each figure. Without examining the actual image files (which are embedded in the PDF as standard figures), the claim that they are hand-drawn is speculation. Removed as factually unverifiable from the text.
- **"No code or dataset details given for reproducibility"** (Harsh Critic): The paper cites standard public datasets (Breast Cancer Wisconsin, Diabetes, Pulsar, etc.) and the 80:20 split is stated. Criticisms about code release are reasonable but belong in Nice-to-Haves, not as a weakness — code is not typically required at submission time. Removed as a non-standard requirement for double-blind review.
- **"The KKT conditions being about convexity, not Euclidean geometry — the paper's claim is misleading"**: While I agree the claim is overstated, the criticism framed it as though the paper has no valid point. The margin-ratio insight (Lemma 2.3) is a real observation even if the KKT framing is imprecise. I have downgraded this to a Minor weakness rather than removing it; but the harsh critic's more extreme framing ("misleading" as a critical issue) is removed here in favor of the calibrated version.
- **Strength Finder strength about "principled derivation"**: While the derivation is mathematically valid as formal manipulation, it suffers from the unresolved conceptual gap about differently-transformed classes (see Major weakness 1). A derivation that glosses over this gap is not a genuine strength. Removed.
- **Strength Finder strength about "empirical outperformance"**: The improvements are tiny and not assessed for statistical significance. The point estimate comparisons could be noise. Removed as the claimed strength conflicts with verified weaknesses about experimental rigor.
- **Strength Finder strength about "margin ratio depends on covariance"**: This is a straightforward algebraic consequence of Equation 14, not a novel or surprising theoretical insight. The paper's contribution is in *noticing* this consequence for the SVM context, which is already captured under the strengths I kept. Removed as generic.
- **Strength Finder strength about "SM algorithm addresses practical limitation"**: The paper itself calls the SM algorithm a heuristic, and the algorithm's convergence and correctness are unanalyzed. Listing it as a strength while also listing it as a weakness (no convergence analysis) would be contradictory. Removed.
- **"Computational complexity not measured"** (Harsh Critic): The paper explicitly discusses complexity as a limitation in the conclusion section. This is a self-acknowledged limitation, not a missed point. Reclassified as Nice-to-Have.

---

## Novel Insights

None beyond the paper's own contributions. The reviews raise important questions about the paper's mathematical cohesion but do not surface novel observations about the problem domain that the paper itself does not contain.

---

## Suggestions

1. **Clarify the core mathematical ambiguity.** The paper must explain, with explicit formalism, how SVM is applied when each class is transformed by a different Cholesky factor. If the Euclidean-space SVM is only used to compute a margin ratio (step 2c → step 2e), this should be stated clearly and justified. A pooled covariance (as in LDA) would avoid the issue entirely — the paper should explain why class-specific transformations are necessary rather than a single transformation.

2. **Include the most relevant baselines.** MCVSVM (Zafeiriou et al. 2007) and MD-TSVM (Peng & Xu 2012) are cited as prior work with "dimensional inconsistencies" — they must be included in the experimental comparison to substantiate this claim.

3. **Provide proper statistical evaluation.** Report results over multiple train-test splits or cross-validation folds with confidence intervals, or at minimum report per-fold results. A single 80:20 split is insufficient to establish that differences are not due to sampling variation.

4. **Report hyperparameters.** State the SVM C value and whether any tuning was performed. If baselines used default parameters, disclose this. If CSVM required tuning, describe the procedure.

5. **Validate the SM algorithm empirically.** Show convergence behavior (number of iterations, trajectory of covariance estimates) across datasets. Compare against a non-iterative version that uses only training-data covariances, to measure whether the iterative relabeling adds value. Compare against standard semi-supervised SVM methods.

---

## Score and Decision

**Bracketing (Round 1):** Three queries on "SVM + covariance adjustment + non-Euclidean" retrieved weak anchors (avg 1.50–2.50), middle anchors (4.29–6.40), and strong anchors (8.00–8.50). The paper clearly does not reach the 4+ range — papers at that level (e.g., the GDA framework at 5.00) have rigorous mathematical development, thorough experiments, or both. The paper sits below 3.5.

**Narrowing (Round 2):** Two queries targeting the 1.5–3.5 band retrieved FINDER (2.50), Spatial Sign LDA (3.33), LIFE (3.00), and several 2.00–2.67 papers. Compared to these anchors:
- **FINDER (2.50)**: Has a more developed theoretical framework (Hilbert space formalism) but is criticized for clarity and novelty. The CSVM paper has a less rigorous mathematical foundation with an identified conceptual gap, and weaker experimental methodology.
- **Spatial Sign LDA (3.33)**: Provides theoretical convergence guarantees and is more rigorously developed. CSVM is weaker across all comparison axes.
- **LIFE (3.00)**: Has a developed spectral theory framework with theoretical grounding. CSVM is less rigorous.

The CSVM paper is most comparable to the 2.0–2.5 band — it has a genuine conceptual gap in its core derivation, lacks statistical rigor in experiments, and misses the most relevant baselines. The SM algorithm is presented without convergence analysis.

**Final score: 2.5** — Below the ICLR acceptance threshold. The paper identifies a real problem and attempts a concrete solution, which prevents it from falling to the lowest scores, but the conceptual gap in the derivation, weak experimental methodology, and absence of key baselines place it well below publication quality.

MY FINAL SCORE: <score>2.5</score>
MY FINAL DECISION: <decision>Reject</decision>