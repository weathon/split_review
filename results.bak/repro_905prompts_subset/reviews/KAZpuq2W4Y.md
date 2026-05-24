Now I have a thorough understanding of the paper. Let me synthesize the final review.

## Summary of Key Verifications

1. **"Attention-weighted covariance" issue**: The paper says "attention-weighted covariance matrix" in Section 4.3.3 and in the architecture overview. The centering uses v^(1) which is attention-weighted (v^(1) = Σ a_k · g_k), but the outer-product sum C = Σ g̃_k g̃_k^T has no explicit attention weights. This is a minor terminology imprecision — the centering is attention-weighted but the sum itself isn't. The paper shows the equation, so the implementation is clear even if the description is slightly loose.

2. **CAMELYON16 protocol**: The paper describes the dataset's official split (270/129) in Section 5.1, then says "For both datasets, we use a unified 5-fold cross-validation setup" in Section 5.2. It never clarifies whether the official test set is included in the CV folds. All baselines are evaluated under the same protocol, so internal comparisons are fair. The ambiguity primarily affects the "state-of-the-art" claim relative to externally reported numbers. This is a meaningful but not fatal concern.

3. **Statistical significance**: No significance tests provided. The AUC improvements are small (0.35% on CAMELYON16).

4. **SE notation**: Tables report "mean<sub>SE</sub>" — it's unclear if SE means standard error or standard deviation, as the values are more consistent with SD magnitudes.

5. **Ablation Table 3**: No variance reported, making it hard to assess reliability of component contributions.

Now writing the review.

Score decision: I'll place this at 5.5. The paper has a clear contribution, solid empirical work, and practical value, but the evaluation protocol ambiguity and lack of significance testing are meaningful concerns that prevent it from being a strong Accept.## Summary

This paper proposes HOMIL, a multi-instance learning framework for whole-slide image classification that augments the standard attention-weighted mean (first-order moment) with an attention-weighted covariance matrix (second-order moment) to capture inter-feature variability. It further employs DBSCAN-based adaptive clustering to group similar patches, reducing computational cost while preserving diagnostic detail. The method is evaluated on CAMELYON16 and TCGA-NSCLC, achieving top accuracy, AUC, and F1 across nine baselines while being substantially faster than attention-based and transformer-based competitors.

## Strengths

- **Novel integration of second-order moments into MIL aggregation.** Whereas existing WSI-MIL methods (ABMIL, CLAM, TransMIL) rely on first-order (mean-based) representations, HOMIL explicitly computes a covariance matrix of cluster features to capture pairwise feature correlations. The ablation study (Table 3) confirms that removing the second-order moment module drops ACC by 1.0% and F1 by 1.6%, providing direct evidence that the second-order contribution is substantive and complementary to the first-order stream.

- **Adaptive DBSCAN clustering that jointly improves efficiency and accuracy.** The clustering is not merely a speed-up trick: it naturally forms small clusters for rare pathological regions (fine-grained processing) and large clusters for abundant normal tissue. On CAMELYON16, HOMIL runs in 310s total (5-fold CV) — faster than every non-trivial baseline (ABMIL 455s, CLAM-SB 640s, TransMIL 5175s) — while achieving the highest accuracy. The ablation shows removing clustering increases runtime by 71% and decreases ACC by 1.26%, demonstrating a genuine dual benefit.

- **Consistent state-of-the-art results across two challenging benchmarks.** HOMIL achieves best ACC (96.98%), AUC (99.23%), and F1 (96.54%) on CAMELYON16 and best ACC (93.24%), AUC (97.41%), and F1 (92.93%) on TCGA-NSCLC — leading on all metrics on both datasets. The ACC improvements over ABMIL are 2.26% and 2.19% respectively, which are practically meaningful for medical diagnosis.

- **Exceptional computational efficiency.** On CAMELYON16, HOMIL is 17× faster than TransMIL and 23× faster than MambaMIL while outperforming them. On TCGA-NSCLC, it is 13× faster than TransMIL and 7× faster than MambaMIL. This combination of top accuracy and practical speed is a concrete differentiator.

- **Clean ablation isolating each component's contribution.** The controlled removal of clustering (CM) and second-order moments (SOM) shows both contribute positively. The full model outperforms all ablated variants, providing clear evidence for the claimed contributions.

## Weaknesses

### Major

- **Ambiguous evaluation protocol for CAMELYON16.** The paper describes the dataset's official split (270 training, 129 testing) in Section 5.1, but then states "For both datasets, we use a unified 5-fold cross-validation setup" (Section 5.2) without clarifying whether the official test set is included in the CV folds. If the 129 held-out test slides are absorbed into CV folds, the results are not directly comparable to externally published numbers that use the official test split. Since all baselines are implemented in-house and evaluated under the same protocol, the *internal* comparison is fair, but the paper's claim of "state-of-the-art" cannot be verified against prior published results. This ambiguity must be resolved (e.g., by either using the official split for reporting or explicitly stating that cross-validation results are for internal comparison only).

- **No statistical significance testing for the claimed improvements.** On CAMELYON16, the AUC improvement over ABMIL is 0.35% (98.88 → 99.23) and HOMIL's own SE is 0.62 — the improvement is well within one standard error. On TCGA-NSCLC, the AUC improvement over Mean Pooling is 0.44% (96.97 → 97.41). While the ACC and F1 improvements are larger (2.26% and 2.94%), no significance test (e.g., paired bootstrap, Mann-Whitney across folds) is provided for any comparison. Without this, it is difficult to assess whether the gains are reliable or could arise from fold-level noise.

### Minor

- **The term "attention-weighted covariance matrix" is imprecise.** The paper (Section 4.3.3) calls the covariance matrix "attention-weighted" and "weighted," but the equation C = Σ_k g̃_k g̃_k^T has no attention-weight factors in the sum — the outer products are summed equally. The centering uses the attention-weighted first-order vector v^(1) = Σ a_k g_k, which makes the *centering* attention-weighted, but the outer-product aggregation itself is unweighted. This does not invalidate the method (the equation is clearly written), but the terminology misaligns with the implementation. The authors should either remove "attention-weighted" from the description of C or add explicit weights to the sum.

- **Ablation study (Table 3) reports only means without variance.** This makes it impossible to assess whether the observed drops from removing CM (1.26% ACC) or removing SOM (1.0% ACC, 1.6% F1) are meaningful relative to fold-to-fold variation. All other tables report mean±SE; Table 3 should do the same.

- **Ambiguity in the "SE" notation.** Tables report "mean<sub>SE</sub>" but do not specify whether SE denotes standard error or standard deviation. The magnitudes (e.g., SE=2.43 for HOMIL ACC on CAMELYON16, SE=8.50 for Mean Pooling ACC) are more consistent with standard deviations. Standard error across 5 folds (which would imply even larger fold-to-fold variance) is an unusual choice. This should be clarified.

- **No comparison with other second-order or covariance-based MIL methods.** The paper compares against first-order (ABMIL, CLAM) and sequence-based (TransMIL, MambaMIL) methods, but does not include approaches that also use second-order statistics in MIL (e.g., DS-MIL, DTFD-MIL, or bilinear pooling variants). Adding at least one such baseline would strengthen the claim that the specific second-order design matters.

### Trivial

- None.

## Nice-to-Haves

- A brief qualitative analysis of the DBSCAN clusters (e.g., how many clusters per slide on average, whether they correspond to coherent tissue regions) would substantiate the claim of "adaptive granularity for pathological vs. normal regions."
- Providing confidence intervals or error bars in Figure 2 (fusion weight evolution) would clarify whether the observed divergence between α^(1) and α^(2) is systematic.
- A short justification for the specific 1D-convolution-with-max-pooling vectorization of the covariance matrix, as opposed to simpler alternatives (flatten-then-project or eigenvalue pooling), would improve methodological transparency.

## Removed Points

These were flagged in the input reviews but are removed for the following reasons:

- *"No attention weights appear in the covariance equation"* — Moved to Minor (terminology imprecision). The equation is clearly shown; the issue is the label, not a hidden architectural error.
- *"The motivation in Section 3.2 operates at the patch level but implementation operates at cluster level"* — The paper explicitly states (Section 3.2) that this is a background/introduction; the actual method (Section 4) correctly describes the cluster-level computation. This is not an inconsistency.
- *"Covariance vectorization via 1D convolution adds learnable parameters without analysis"* — This is a design choice with no evidence of harm; the model is already faster than baselines. Demoted to nice-to-have.
- *"ϵ tuned on entire dataset before splitting leaks information"* — The 65th-percentile heuristic is a data-dependent but reasonable adaptation strategy; without evidence of leakage, this is speculative.
- *"Figure 2 adds little insight"* — The fusion weight evolution is a reasonable auxiliary analysis; removing it is not necessary.
- *"No comparison with bilinear pooling or Gram-matrix methods"* — Kept as a minor weakness (see above).
- Strength Finder claims about "significantly improving state-of-the-art" — Overstated; the ambiguity in the evaluation protocol weakens this claim. Not removed but appropriately qualified.
- Strength Finder claim of "+2.26% ACC over ABMIL on CAMELYON16" — Verified and retained correctly.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. Clarify the CAMELYON16 evaluation protocol: specify whether the official 129-slide test set is held out during 5-fold CV. If it is held out, report results on it separately; if the CV spans all 399 slides, state this explicitly and avoid claiming "state-of-the-art" relative to papers that use the official test split.
2. Add statistical significance tests (e.g., paired bootstrap across folds) for the main comparisons.
3. Rename the covariance computation: call it "covariance centered by the attention-weighted mean" rather than "attention-weighted covariance matrix."
4. Add variance estimates to the ablation study (Table 3).
5. Clarify whether the reported "SE" values are standard deviations or standard errors, and use the conventional notation.

## Score and Decision

### Calibration Anchors

**Round 1 — Bracketing:** Searched for WSI MIL papers in three bands. Weak anchors (avg < 3.5): 0yVP49SDg0 (3.25, Reject), i4ouG6Kc8M (2.50, Reject), MOCEoNsjEx (3.00, Reject), jHdsZCOouv (3.40, Reject). Middle anchors (3.5–7.5): 6xrDPHhwD3 (6.00, Accept), AZW3qlCGTe (5.67, Accept), trj2Jq8riA (5.67, Accept), lo9HMoGNwQ (4.50, Reject). Strong anchors (avg > 7.5): xriGRsoAza (8.00, Accept), 3b9SKkRAKw (8.00, Accept), HnhNRrLPwm (8.00, Accept), 3i13Gev2hV (8.00, Accept). **Initial bracket: 4.5–6.5.**

**Round 2 — Narrowing:** Searched within the bracket (4.5–6.5 and 5.0–7.0). Retrieved: 6xrDPHhwD3 (6.00), q1t0Lmvhty (6.00, covariance pooling theory paper), AZW3qlCGTe (5.67), trj2Jq8riA (5.67), RJDjSXNuAZ (5.50, weakly supervised detection), SPu6k4OZkj (5.25, clustering paper). Reading the full reviews of these anchors: the 6.00 papers (MFC, covariance pooling theory) had more serious structural issues (inconsistent descriptions, missing derivations) than HOMIL, yet were accepted. The 5.67 and 5.50 anchors (set-level labels, virus detection) are cleaner but narrower in scope. HOMIL's combination of novelty, empirical breadth, and practical efficiency places it above the 5.50 anchor but below the 6.00 anchors due to the evaluation protocol ambiguity and missing significance testing. **Final score: 5.5.**

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>