Now I'll produce the final consolidated review.

## Summary
This paper presents two algorithms, ACRE and OHARE, for producing non-trivial lower bounds (certificates) on the number of samples that must be removed to change the sign of a linear regression coefficient along a specified direction. The core technical contribution is a reduction of the robustness auditing problem to bounding the Maximal Subset Norm (MSN) of certain Gram matrices, combined with a novel dynamic programming approach (OHARE) that handles one-hot encoded categorical features by decomposing the problem across buckets and bounding category-wise reaveraging effects. Experimental results on 14 landmark econometrics regressions (n up to ~23k, d up to 209) produce the first known non-trivial lower bounds for any dataset with dimension ≥ 4.

## Strengths

- **First practical algorithms for non-trivial lower bounds on OLS robustness at realistic scale.** Prior work either gave only upper bounds (AMIP, KZC) or required exponential time or very strong assumptions. The paper produces concrete certificates for datasets with hundreds of dimensions and tens of thousands of samples — e.g., on Nightlights (d=209, n=3895), OHARE certifies that no subset of ≤29 samples can flip the sign, whereas no non-trivial lower bound was previously known for any dataset with d ≥ 4.

- **Provably near-tight certificates under mild distributional assumptions.** Theorem 1 (ACRE tightness) gives a multiplicative gap of 1 + Õ((d + k√d)/n) for k up to Õ(min(n/√d, n²/d²)) under subgaussian features and Gaussian noise. Theorem 2 (OHARE tightness) gives gap 1 + O(1/√log n) under bucket-size conditions |Bⱼ| > n^ε√d and n ≥ d^{5/4+o(1)}. These are the first tightness results for this problem in practice-relevant regimes, and the proof introduces genuinely novel matrix concentration arguments (Lemmas 7.1–7.3) to handle reaveraging dependencies.

- **Clean algorithmic framework with modular architecture.** The decomposition of the removal effect into first-order and higher-order terms (Equation 2), the reduction to three MSN subproblems, and the separation of the continuous and one-hot feature analysis are technically elegant. The RTI and spectral MSN-bounding subroutines are interchangeable, and the OHARE dynamic programming combination (Algorithms 4, 6) is a principled solution to the category-aware certification problem.

- **Demonstrated scalability on real-world data.** Experiments in Table 1 show runtimes from seconds to under 10 minutes on a single CPU core, with memory under 64 GB, across datasets with n up to ~23,000 and d up to 209. The OHARE bounds are within a factor of 1–5 of known upper bounds, providing meaningful certificates that were previously unavailable.

- **Potential downstream impact beyond robustness auditing.** The paper explicitly discusses applications to data attribution (identifying brittle predictions) and connections to differential privacy (Section 1.2). The framework could extend to other regression methods (logistic regression, LASSO) as noted in the future directions.

## Weaknesses

### Fatal
None.

### Major
None — the core contributions are valid and the algorithms work as claimed. The weaknesses below are addressable in revision.

### Minor

1. **Overstated empirical tightness claim.** The paper states (Section 1.1) that lower bounds "match known upper bounds up to a factor of 2 or 3." The actual ratios from Table 1 show that several exceed this range: Nightlights (136/29 ≈ 4.7), OHIE Health notpoor (149/40 ≈ 3.7), OHIE Not bad days mental (118/31 ≈ 3.8), and others in the 3.3–3.8 range. While "in many cases" is true (7 of 14 ratios are ≤ 3), the maximum is ~4.7, not 3. The claim should be qualified with the actual range of observed ratios.

2. **Assumptions for theoretical tightness are not verified on experimental datasets.** Theorems 3 and 4 give tightness guarantees under distributional assumptions (subgaussian features, Gaussian noise; for OHARE additionally requiring |Bⱼ| > n^ε√d, n ≥ d^{5/4+o(1)}). The paper does not check whether these assumptions hold, even approximately, for the real econometrics datasets used in experiments. While the algorithms themselves are valid unconditionally (Theorem 1), the theoretical justification for the experimental bounds relies on unverified assumptions. Adding a brief discussion of assumption consistency (e.g., reporting bucket sizes and checking whether they exceed √d thresholds) would strengthen the paper.

3. **Memory overhead beyond stated bottleneck is not discussed.** The paper states that storing three n×n matrices is the main memory bottleneck (line 216). For n≈23k, three double-precision matrices require ~12.9 GB, but Table 1 reports memory usage up to 51.53 GiB — roughly 4× higher. The additional overhead (likely from OHARE's dynamic programming tables, bucket-wise computations, and temporary matrices) is not explained. A brief discussion of this would improve reproducibility and help practitioners anticipate memory requirements.

4. **Influence score decomposition missing.** Several regressions show a gap between OHARE lower bounds and AMIP upper bounds (e.g., OHIE Health notpoor: bound 40 vs. upper 149; ratio ~3.7). The paper identifies one cause (land ownership skew in Cash Transfer) but does not systematically analyze the gap for other regressions. Understanding whether the slack comes from loose MSN bounds, bucket-wise decomposition, or fundamental hardness would be valuable.

### Trivial

1. The description of the correction terms c⁺ and c⁻ in Section 4 (OHARE) is notationally dense; a small worked example would improve clarity.

2. The RTI output characterization (line 1219) says the output squared is "the sum of k diagonal entries plus fewer than k² off-diagonal entries." This is slightly imprecise — it could be fewer than k diagonal entries — though the inequality that follows is correct regardless.

## Nice-to-Haves

- **Validation on small synthetic data.** For n ≤ 30, d ≤ 3, brute-force enumeration is feasible to verify that OHARE's lower bound does not overestimate k_sign. This would provide an end-to-end correctness check that complements the theoretical analysis.

- **Simple lower bound as baseline.** A sanity-check lower bound (e.g., removing the k samples with largest |R_i·Z_i| and recomputing the regression) would help calibrate how much value the sophisticated OHARE machinery adds over trivial approaches.

- **Bucket size reporting.** The OHARE tightness guarantee depends on bucket sizes exceeding n^ε√d. Reporting actual bucket sizes for each dataset (e.g., number of countries in Nightlights, number of instrument levels) would clarify which datasets satisfy the theoretical conditions.

- **RTI vs. spectral comparison on real data.** The paper notes that spectral bounding outperforms RTI on synthetic data but does not compare them on real datasets. A systematic comparison would reveal whether stronger MSN bounds could narrow the gap with AMIP upper bounds.

## Removed Points

These points from the reviewers are flagged for removal; treat them with caution:

- **RTI analysis gap (Harsh Critic #3):** The critic claims the paper does not prove that the simplified inequality (line 1223) holds for the actual RTI output. This is incorrect: the inequality is a valid mathematical upper bound on the sum of any k² entries of the Gram matrix with at most k diagonal entries, which is exactly what RTI's V_k² computes. The inequality holds regardless of the exact entry composition. No gap exists.
- **Missing poly(P) factors (Harsh Critic, Section 7):** The critic claims the paper states the gap as 1 + O((d+k√d)/n) without tracking poly(P) factors. This is incorrect: Claim 5 (line 1167) explicitly includes × poly(P₁,…,P₅). The final theorem absorbs these into Õ(·) since P are polylog(n), which is standard.
- **Unquantified failure probabilities (Harsh Critic, Section 8):** The critic claims the "approximate matrix Bernstein" (Lemma 4, lines 1294–1301) does not quantify failure probability. This is incorrect: the lemma explicitly states the failure probability as 2d·exp(-t²/(2(σ²+Lt/3))) + nδ.
- **Generic strengths (Strength Finder):** Several claimed strengths are generic ("potential downstream impact," "theoretical ambition") and conflict with verified weaknesses; these have been filtered for the Strengths section above.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. Correct the empirical claim in Section 1.1: replace "up to a factor of 2 or 3" with a precise summary such as "within a factor of 1–5 of known upper bounds across 14 regressions" or list the actual observed ratios.

2. Add a brief discussion of assumption consistency for the real datasets: report bucket sizes, compare against the √d thresholds required by Theorem 2, and discuss whether violations could affect bound quality in practice.

3. Acknowledge and briefly explain the memory overhead beyond the three n×n matrices, or provide a memory breakdown for the largest OHIE runs.

## Score and Decision

The paper makes a clear and important contribution: it delivers the first algorithms capable of producing non-trivial robustness certificates for OLS regression on datasets with hundreds of dimensions and tens of thousands of samples. The experiments on landmark econometrics studies are concrete and reproducible. The theoretical analysis is technically deep and provides genuine insight into the regimes where the algorithms work well. The weaknesses are minor and addressable — none undermine the core claims.

MY FINAL SCORE: <pineapple>7.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>