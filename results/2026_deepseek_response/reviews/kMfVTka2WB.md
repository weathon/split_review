Now I have enough calibration data. Let me write the final review.

## Summary

This paper proposes Covariance-Adjusted SVM (CSVM), which applies class-specific Cholesky whitening before SVM training, derives two input-space classifiers for binary problems (Lemma 2.2), and proposes an iterative algorithm (SM) to estimate population covariances without test labels. Experiments on five datasets compare CSVM to standard SVM kernels and PCA/ZCA whitening.

## Strengths

1. **The mathematical derivation linking class covariance to SVM margin is algebraically sound.** Equations (1)–(14) correctly show that applying Cholesky whitening before SVM and then reversing the transformation yields a margin expression \(1/\sqrt{\theta^T \Sigma^{-1} \theta}\) in the input space (Eq. 9), and the margin ratio between classes depends on their respective covariances (Eq. 14). This provides a clean explanation for why whitening can affect SVM behavior.

2. **Lemma 2.2 correctly identifies that class-specific whitening leads to two distinct classifiers in the input space.** For binary problems with different class covariance matrices \(\Sigma_1\) and \(\Sigma_{-1}\), the optimization problems (10)–(13) are genuinely different, which is a valid observation and goes beyond standard pooled-whitening approaches.

3. **Empirical results show CSVM outperforming standard baselines on most metrics.** On 4 of 5 datasets (Breast Cancer, Pulsar, Red Wine, Diabetes), CSVM achieves the highest accuracy, recall, and F1 scores. For example, Breast Cancer accuracy reaches 0.974 vs. linear SVM's 0.956 (Table 1), and AUC reaches 0.97 vs. next best 0.95 (Fig. 1).

4. **The paper explicitly acknowledges its own limitations.** Section 6 states that the SM algorithm is "a heuristic algorithm" with no guarantee of perfect classification, and questions whether the performance gain justifies the added computational cost. This transparency is commendable.

## Weaknesses

### Major

1. **The "non-Euclidean space" framing is conceptually misleading and creates confusion about the actual contribution.** The paper claims the input space is "non-Euclidean" because Mahalanobis distance is more appropriate than Euclidean distance (lines 15–16, 45). This is a category error: \(\mathbb{R}^n\) with the standard inner product is a Euclidean vector space regardless of which distance metric one chooses to use. Mahalanobis distance is simply Euclidean distance after a linear transformation (whitening) — it does not make the underlying space non-Euclidean. The mathematical derivations (Eq. 1–14) are algebraically correct *as operations*, but the "non-Euclidean" framing is unnecessary and distracts from the paper's actual contribution, which is an empirical study of class-specific whitening for SVM. This framing is not fatal to the paper's mathematical content, but it misrepresents what is being done.

2. **The class-specific whitening transformation creates an unaddressed geometric inconsistency.** The paper applies *different* Cholesky transformations per class (Eq. 3): points from class 1 are transformed by \(\Psi_1^{-1}\) and points from class -1 by \(\Psi_{-1}^{-1}\). SVM is then trained on the union of these transformed sets (Section 3, steps b–c), treating them as if they live in the same Euclidean space. But they have been mapped to *different* spaces — the Euclidean distance between a \(\Psi_1^{-1}\)-transformed point and a \(\Psi_{-1}^{-1}\)-transformed point is not a geometrically meaningful quantity. The paper does not justify why this union makes sense, which undermines the theoretical grounding of the algorithm.

3. **No hyperparameter tuning or model selection is described.** The paper reports results for SVM with linear, RBF, polynomial, and sigmoid kernels (Tables 1–4), but provides no information about kernel hyperparameters (e.g., \(C\), \(\gamma\), degree), how they were chosen, or whether a search was performed. For the proposed CSVM method, no regularization parameter \(C\) is mentioned. Without this, it is impossible to know whether the comparisons are fair — the baselines may be under-tuned while CSVM benefits from the whitening pre-processing.

4. **No confidence intervals or statistical significance tests are reported.** All metrics (accuracy, precision, recall, F1, AUC) are reported as point estimates from a single 80/20 train-test split. Given that the reported improvements are often small (e.g., Red Wine AUC 0.75 vs. ZCA 0.74; Diabetes AUC 0.74 tied with linear/PCA/ZCA), it is unclear whether any differences are statistically significant. This is a standard expectation for empirical work, and its absence makes the claimed "marked improvement" difficult to assess.

5. **The SM algorithm is presented as a major contribution but has no convergence guarantees or error analysis.** The algorithm (Section 3) is essentially a self-training heuristic that iteratively labels test data, retrains, and updates covariance estimates until "convergence" (lines 149–152). The paper provides no analysis of when this process converges, whether it can diverge, how errors propagate through iterations, or whether the fixed point corresponds to a meaningful solution. The authors acknowledge it is "a heuristic algorithm" (line 319), which is honest, but this does not remedy the lack of validation for a claimed contribution.

6. **No comparison with class-weighted SVMs.** A natural baseline for adjusting margins based on class distributions is a cost-sensitive or class-weighted SVM. The paper compares against standard SVM kernels and PCA/ZCA whitening but omits this directly relevant baseline. Given that the paper's motivation is about unequal class dispersion, this is a noticeable gap.

### Minor

1. **Improvements over baselines are small and inconsistent.** On several datasets/metrics, CSVM ties with or performs worse than baselines (e.g., OSHA accuracy: CSVM 0.752 vs. RBF 0.760; Pulsar precision: CSVM 0.954 vs. linear SVM 0.962; Diabetes AUC: CSVM ties at 0.74 with linear/PCA/ZCA). The claimed "marked improvement" is not uniformly observed.

2. **The paper does not explain how the two classifiers from Lemma 2.2 are combined for prediction.** Lemma 2.2 states there are two unique linear classifiers — but the experimental section reports a single accuracy value per dataset. It is unclear whether both classifiers are used and, if so, how their outputs are fused.

3. **The write-up contains several unclear phrasings and imprecise mathematical statements.** For instance, Lemma 2.3 states the margin is "given by \(1/\Sigma^{-1}\)" which is ambiguous (the correct expression is \(1/\sqrt{\theta^T \Sigma^{-1} \theta}\) from Eq. 9). The phrase "Each data point (other than support vectors) contributes to \(\Sigma^{-1}\)" conflates the covariance matrix (estimated from data) with the margin expression.

### Trivial

1. Several grammatical issues and minor typos (e.g., "iteratively iteratively" in line 164, missing spaces in citations like "( Vapnik (2013))").

## Nice-to-Haves

- Investigating whether global whitening (same transformation for both classes) already captures most of the performance gain would help isolate the effect of the class-specific aspect.
- An analysis of computational cost vs. benefit would strengthen the practical discussion the paper already begins in Section 6.
- Adding the soft-margin formulation (slack variables \(\xi_i\)) would connect the theory more closely to the actual implementation.

## Removed Points

Points removed for factually incorrect or speculative reasons:
- **Harsh Critic: "The central claim—that input/statistical space is 'non-Euclidean' and that standard SVM is invalid there because it uses Euclidean distance—is simply wrong... SVM can use any valid kernel, including Mahalanobis-based kernels, without invoking a different vector space."** — This criticism is kept as a reframed weakness (see Major 1 above) but not in its original form. The claim that "the entire derivation that follows from this premise (Lemmas 2.1–2.3, the two-classifier result) is therefore built on a false premise" is an overstatement. The mathematical derivations in Eqs. 1–14 are algebraically sound *as operations*; the "non-Euclidean" framing is the problem, not the math itself.
- **Strength Finder: "The derivation shows that the margin in the input space becomes \(1/\sqrt{\theta^T \Sigma^{-1} \theta}\) (Eq. 9), directly linking margin to intra‑class covariance. This goes beyond prior work by explaining *why* whitening improves SVM performance."** — Overclaimed. The connection between whitening and improved SVM performance is well-known (whitening decorrelates features and equalizes variance); this paper provides a specific algebraic expression for the margin, which is a contribution, but the "explanation" is not fundamentally novel.
- **Strength Finder: "This shows KKT boundary conditions are invalid in non‑Euclidean spaces"** — This claim is entangled in the problematic "non-Euclidean" framing and is removed as a strength for the same reason.
- **Strength Finder: Generic/superficial strengths** — Several generic-sounding strengths (the problem is important, the paper addresses a gap) removed as standard filler.
- **Harsh Critic: "the paper also does not compare to simple class-weighted SVMs"** — This is a valid criticism and is kept in Major 6.
- **Harsh Critic: "the paper does not compare to MCVSVM"** — Actually the paper cites and discusses MCVSVM in the introduction (line 21), stating its claimed gaps with it. The criticism is removed because the paper explicitly addresses this related work.
- **Harsh Critic: speculative claims about "not yet released" or missing appendix content** — Removed per hard rules; the paper cites what it cites, and appendix content was stripped by the PDF parser.

## Novel Insights

None beyond the paper's own contributions. The main observation that survives filtering is that class-specific whitening before SVM produces an input-space margin that depends on class covariance, and that this leads to two distinct classifiers (for binary) rather than one. However, this is a relatively direct algebraic consequence of applying different Cholesky transforms per class and then reversing the transformation. The more interesting question — whether this geometric formulation is theoretically superior to simply using a Mahalanobis kernel in a standard SVM — is not addressed.

## Suggestions

1. **Re-frame the paper's narrative.** Drop the "non-Euclidean space" terminology and present the method as: "class-specific Cholesky whitening as a pre-processing step for SVM, with an analysis of how the input-space margin depends on class covariance." This would be more accurate and avoid the terminological issues that dominate the current framing.

2. **Address the geometric inconsistency of class-specific whitening.** Either provide a theoretical justification for why training SVM on the union of differently-transformed points is valid, or modify the approach so that a single whitening transformation is used (or a principled combination).

3. **Strengthen the experimental evaluation.** Add hyperparameter tuning (at minimum for the SVM \(C\) parameter), report confidence intervals (e.g., bootstrapping or repeated train-test splits), and include class-weighted SVM as a baseline.

4. **Provide a rigorous analysis of the SM algorithm.** At minimum, discuss conditions under which the iterative procedure is guaranteed to converge, and provide empirical evidence about the number of iterations needed and sensitivity to initialization.

5. **Clarify how the two classifiers from Lemma 2.2 are combined for inference** — the paper currently describes the algorithm but does not explain how predictions are made from the two derived classifiers.

## Score and Decision

**Anchor calibration:**

**Round 1 — Bracketing:** Based on similarity to the paper (SVM + covariance/whitening methods), I queried three ranges:
- Weak anchors (score < 3.5): avg scores 2.50–3.25 — papers with unclear contributions, weak experiments, or flawed framing.
- Middle anchors (3.5–7.5): avg scores 4.67–6.00 — papers with sound theory and reasonable experiments but various gaps.
- Strong anchors (>7.5): avg scores 8.00 — polished, rigorous papers with extensive validation.

This paper sits squarely in the weak-to-lower-middle range. It has a clear theoretical derivation but the conceptual framing is problematic, experiments lack statistical rigor, and the SM algorithm is unvalidated.

**Round 2 — Narrowing:** I queried ranges (2.5, 5.5) and (2.0, 4.5) with specific focus on SVM whitening methods:
- Sparse Covariance VNNs (3.00): Better theory (stability analysis, convergence rates), comparable experiments, but incrementally builds on existing VNNs. This paper's conceptual framing is weaker, but its idea is somewhat more self-contained.
- Symmetric Kernels (5.00): Strong theory, targeted experiments. Clear contribution but narrower scope. This paper is clearly weaker.
- Scalable GP (3.80): Solid method but limited novelty. The current paper is comparable in quality — both have reasonable ideas but significant gaps in validation.

**Final position:** This paper is closest to the 3.00 anchors (Sparse Covariance VNNs, Manifold KRRR). The derivations in Section 2 are mathematically coherent, and the empirical results suggest the method has practical potential. However, the problematic "non-Euclidean" framing, the unaddressed geometric inconsistency of class-specific whitening, the complete absence of hyperparameter tuning and statistical significance testing, and the unvalidated SM algorithm collectively prevent the paper from meeting the bar for ICLR acceptance. The paper reads more like a workshop contribution or a specialized journal paper in its current form.

**All anchors considered:**
| Path | Avg Score | Round | Comparison |
|------|-----------|-------|------------|
| ZDoaLbOFaP (Sparse Covariance VNNs) | 3.00 | R1 | Comparable theory quality, better stability analysis, weaker novelty |
| WVIq7jYIda (Manifold KRRR) | 3.00 | R1 | Comparable overall quality |
| eS0qCQDrkG (Trace Est. for OT) | 3.25 | R1 | Clearer contribution, more rigorous |
| qcyn7ESaM8 (PCA & Neural Nets) | 2.50 | R1 | Weaker experiments, comparable framing issues |
| anek0q7QPL (Cov+Hessian) | 5.00 | R1 | Better experiments but mixed reviews; this paper is weaker |
| q1t0Lmvhty (Riemannian Cov Pooling) | 6.00 | R1 | Much stronger theory and experiments |
| usmP3muXMI (Chebyshev Risk) | 4.67 | R1 | Better theory, comparable empirical depth |
| ClixrtIHUJ (LLM Features for CIL) | 5.25 | R1 | More polished, clearer contribution |
| LjQDYcFWmN (Symmetric Kernels) | 5.00 | R2 | Stronger theory |
| VyMW4YZfw7 (GNN Low Rank) | 3.00 | R2 | Comparable — overclaimed but some insight |
| QBlegfNZNE (Language as Kernels) | 3.50 | R2 | Conceptually confused but some interesting ideas |
| xUHL8mtSUL (Scalable GP) | 3.80 | R2 | Better empirical methodology |
| PuKRVPXXpR (ResTran) | 3.50 | R2 | Comparable quality |
| x8mr9zGkpr (Attributing Model Behavior) | 3.00 | R2 | Different topic but similar rigor level |

MY FINAL SCORE: <score>3.0</score>
MY FINAL DECISION: <decision>Reject</decision>