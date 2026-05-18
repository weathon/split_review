Now I have a thorough understanding of the paper and the reviews. Let me produce the consolidated review.

---

## Summary

This paper diagnoses instability in existing continual learning (CL) methods that use pre-trained models with random ReLU features (RanPAC, min-norm ICL), tracing it to ill-conditioned feature matrices and the emergence of extremely small eigenvalues. The authors propose ICL-TSVD, which continually truncates small singular values before solving the minimum-norm least-squares problem, and provide both theoretical guarantees (Theorems 1 and 2 bounding training and generalization errors) and extensive empirical validation (8 datasets, multiple increment sizes including challenging Inc-1). The method establishes a rare connection between principled CL theory and state-of-the-art practice.

## Strengths

1. **Clear diagnosis of instability with supporting spectral analysis.** The paper identifies the root cause of failure in existing methods (ill-conditioned random ReLU features with eigenvalues as small as ~10⁻⁵) and directly links this to both numerical instability and double-descent phenomena. Figure 1(a,b,c) shows the correlation between the emergence of tiny eigenvalues and accuracy collapse, which is then confirmed in the training loss explosion (Figure 2). This diagnostic analysis is clean and motivates the TSVD remedy naturally.

2. **State-of-the-art empirical performance across diverse CIL settings.** ICL-TSVD consistently outperforms RanPAC and other baselines on 8 datasets under B-0 and B-q₁, Inc-{5,10,20} settings (Table 1). In the challenging Inc-1 setting (Table 3), ICL-TSVD achieves 77.65% average final accuracy vs. 66.00% for RanPAC, with particularly dramatic gains on StanfordCars (1.19% → 74.44%). These gains are backed by stability improvements confirmed by accuracy matrices (Figure 5).

3. **Stability with respect to hyperparameters.** Figure 3a shows ICL-TSVD maintains stable performance across a wide range of truncation percentages (0–100%), and Figure 3b shows that the TSVD-extended ridge version is practically immune to changes in the regularization parameter λ (10⁻⁵ to 10⁴). This contrasts sharply with RanPAC (Figure 2) and the original min-norm ICL (Figure 1c), providing compelling evidence that TSVD addresses the underlying instability.

4. **Novel theoretical guarantees for a continual truncation setting.** The paper proves Theorem 1 (estimation bound) and Theorem 2 (generalization bound) that control error in terms of the eigenvalue gap ratio γ_t and accumulated truncated eigenvalues a_t. The authors explicitly connect these quantities to observable spectral properties (line 270: a_t ≈ 10⁻³ for hundreds of tasks when truncating eigenvalues of order 10⁻⁵), making the bounds meaningful in practice. Importantly, the analysis covers the *continual* truncation setting rather than the static PCR setting studied in prior work, and makes fewer distributional assumptions than prior theory.

5. **Scalable and efficient continual implementation.** Algorithm 1 requires O(E(k_{t-1}+m_t)²) complexity per task compared to RanPAC's O(E³), enabling ICL-TSVD to use a larger embedding dimension (E=10⁵ vs. E=10⁴ for RanPAC). Figure 4 shows speedups of up to 1000× at equal E.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

1. **Lack of a direct same-embedding-dimension accuracy comparison with RanPAC.** The main empirical comparison (Table 1) uses E=10⁵ for ICL-TSVD vs. E=10⁴ for RanPAC. The paper argues this is fair because ICL-TSVD's efficiency justifies larger E, and provides runtime evidence at equal E (Figure 4). However, this confounds the benefit of the method itself with the benefit of larger E. While the paper's core claims about stability and theoretical guarantees do not hinge on beating RanPAC by a margin, the claim of "uniformly outperforming" RanPAC would be strengthened by a direct accuracy comparison at the same embedding dimension (e.g., E=10⁴ for both). The scaling-law evidence (referenced as Figure acc-inc5-E) partially addresses this but is cited rather than shown in the main paper.

2. **The theoretical bounds depend on quantities that are not directly computable (the ground-truth weight matrix ‖W_gt‖_F and noise ‖ε‖_F).** The paper is transparent about this (line 255) and argues that the bounds become small for suitable truncation regardless of specific values. However, no empirical validation of bound tightness is provided (e.g., estimating the unknown quantities from learned weights and residuals on one dataset to verify the bound is within an order of magnitude of the actual loss). This limits the practical force of the theoretical guarantees.

3. **No explicit validation of the linear model assumption (Y = W_gt H + ε) on real features.** The paper notes that the joint linear classifier LC(H_{1:T}) achieves accuracy close to ICL-TSVD (Table 1), which indirectly supports the assumption. However, a more direct diagnostic — e.g., measuring the reconstruction error of a linear fit on all tasks jointly — would be valuable for assessing whether the theory's core premise holds for the actual pre-trained+ReLU features.

4. **The choice of truncation percentage ζ could be discussed more practically.** The paper shows insensitivity across a wide range (Figure 3a), which is a strength, but provides no practical guidance on how to set ζ beyond the truncation threshold interpretation. Is ζ tunable by cross-validation? Is a fixed percentage always appropriate across datasets with different spectral properties?

### Trivial
None.

## Nice-to-Haves

- **Empirical validation of theoretical bound tightness.** Estimating the terms in Theorems 1 and 2 on one dataset (e.g., CIFAR100 Inc-5) and comparing the bound value to actual training/test MSE would demonstrate non-vacuousness.
- **Brief empirical check of MSE vs. cross-entropy equivalence** on one dataset, to confirm that the MSE loss used throughout does not incur a systematic accuracy penalty.
- **A direct same-E accuracy comparison** (e.g., E=10⁴ for both methods on StanfordCars Inc-5 and ImageNet-A Inc-5) to separate the benefit of the method from the benefit of larger embedding dimension.

## Removed Points

- **Criticism about the continual SVD approximation quality lacking quantitative analysis in the main paper.** The paper references a theorem and figures in the appendix (Theorem eigenvalue-eigenspace-bound, Figures eigenvalues-continual, normalized-ev-diff) which provide the quantitative analysis. The parser strips appendix content; these exist in the original submission.
- **Comment about large blocks of commented-out material visible in the raw extract.** This is a PDF parsing artifact, not an author error.
- **Criticism about varying y-axis scales in runtime comparison (Figure 6).** This is a minor presentation preference; the data is clearly communicated.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. Add a same-E accuracy comparison (E=10⁴) on at least 2-3 datasets to cleanly separate the benefit of the method from the benefit of larger embedding dimension.
2. On one dataset, provide a rough empirical estimate of the bound quantities in Theorem 1/2 to demonstrate non-vacuousness.
3. Add a sentence of practical guidance on selecting ζ (e.g., "in practice, any ζ in [10%, 90%] yields near-identical results, so cross-validation over a coarse grid suffices").
4. Explicitly note that LC(H_{1:T})'s strong performance supports the linear model assumption underlying the theory.

## Score and Decision

This paper makes a genuine contribution: it diagnoses a real instability in state-of-the-art CL methods, proposes a principled and scalable fix (continual truncated SVD), provides novel theoretical guarantees for the continual setting, and validates the approach extensively. The weaknesses are minor — the comparison confound with E is acknowledged and partially justified, the theoretical bounds depend on unknown quantities (standard in learning theory), and the remaining suggestions are incremental improvements. The work bridges an important gap between theory and practice in CL with pre-trained models and should be accepted.

MY FINAL SCORE: <pineapple>8.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>