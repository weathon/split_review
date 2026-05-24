Now I have all the calibration context I need. Let me write the consolidated review.

---

## Summary

This paper proposes CV-imputation, a cross-validation method for graphon models. The core idea is to partition node pairs into K folds, replace validation-set entries with independent Bernoulli(θ) draws, estimate the graphon from this imputed adjacency matrix, and then apply an affine correction (Eq. 6) to recover predictions for the original probability matrix. Lemma 1 shows the imputed training matrix has expectation that is an affine transformation of the true P, and Theorem 1 establishes that the CV score is asymptotically parallel to the true MSE (up to a constant), so minimizing it asymptotically minimizes the estimation error. Empirically, the method is compared to edge cross-validation (ECV) across four graphon types, four estimators (NS, SAS, USVT, ICE), and three real networks, showing consistent MSE improvements and substantial computational speedups (e.g., 241 seconds vs. 6,021 seconds on the Yeast network).

## Strengths

1. **Novel and principled CV method for network data.** The imputation + affine correction (Lemma 1, Eq. 5–6) is a clever solution to a genuine problem: standard node-splitting CV breaks network structure, and edge-splitting CV changes the data distribution. The method preserves edge independence in the training set while maintaining a tractable relationship to the original probability matrix.

2. **Asymptotic model-selection guarantee (Theorem 1).** The paper proves that the proposed validation score \(V_K(M)\) differs from \(L(M)+\Lambda\) by \(O_p(1/n \vee 1/K^{(1+\alpha)/2} \vee 1/K^\alpha)\) uniformly over candidate models, where \(\Lambda\) is constant in \(M\). This means the minimizer of \(V_K\) asymptotically minimizes the true MSE — a non-trivial theoretical justification that goes beyond heuristic CV.

3. **Consistent and substantial computational advantage over ECV.** The complexity analysis is clear (CV-imputation adds \(O(n^2)\) per fold vs. ECV's \(O(n^3)\) matrix completion), and the empirical timings across all four graphons (Figure 3, Table 2) confirm that the savings are real and large — up to 25× faster on the Yeast network. This is a practically meaningful contribution for large-network analysis.

4. **Extensive empirical evaluation across diverse settings.** Experiments cover four graphons (dense/sparse, low-rank/full-rank), four very different estimation methods (NS, SAS, USVT, ICE), three real networks (PolBlog, NetSci, Yeast) up to 2,617 nodes, and a COVID-19 co-occurrence case study. CV-imputation matches or beats ECV in MSE in all 16 simulated scenarios and provides better or equal AUC on all three real networks.

## Weaknesses

### Major

1. **Unresolved anomaly in the ECV baseline on Graphon 1 with NS.** In Table 1, ECV (NS) on Graphon 1 yields MSE = 9.15 ± 19.25 (×100). The standard deviation is more than double the mean, and the value is ~18× larger than CV-imputation's 0.51. The default NS (M=1) itself gives 39.05, so ECV does improve on the default — but the enormous variance combined with the large gap to CV-imputation is suspicious. It suggests either that ECV's matrix completion fails on certain folds for this dense graphon, or that the ECV configuration (number of folds, completion algorithm) is suboptimal. The paper does not discuss this data point or provide diagnostics (e.g., fraction of folds where completion fails). This weakens the claim that CV-imputation "consistently" outperforms ECV — the comparison may be contaminated by a poorly tuned ECV setup.

2. **Condition 1 is stated as an assumption rather than verified or derived for the estimators used.** Theorem 1's guarantee hinges on Condition 1 (the optimism bias \(Q_K(M)\) decays at rate \(K^{-\alpha}\)). The paper states that this condition "can be verified computationally" and references Figure S.3 in the appendix, which is reasonable as far as it goes. However, no analytical link is provided between the properties of the four applied estimators (NS, SAS, USVT, ICE) and the rate \(\alpha\). The Erdős–Rényi example (\(\alpha=1\)) is helpful but trivial. Users of the method are left with no guidance on when Condition 1 might fail for their estimator of choice. This limits the practical force of the theoretical result.

### Minor

1. **Figure 3 caption contains a clear contradiction.** The parsed figure description states "In all cases, ECV is faster than CV-imputation," while the main text argues the opposite and all data (Table 2, Figure 5) show CV-imputation as faster. This is almost certainly a typo (the caption in Figure 5 says the correct thing), but it is an error that appears in the submission and undermines trust in the care with which results are reported.

2. **Missing baseline: naive edge removal without imputation.** The paper compares against ECV (which uses matrix completion) but not against a simpler baseline that simply removes validation edges (sets them to 0) and applies the estimator without any correction. Such a baseline would directly test whether the imputation step provides any benefit over "do nothing." If naive removal also works well, the imputation machinery would be unnecessary complexity. The paper would be strengthened by including this comparison.

3. **Choice and sensitivity of the imputation mean \(\theta\) are deferred entirely to the appendix.** The main text mentions \(\theta\) is a tuning parameter but says only "The selection of \(\theta\) is discussed in Section S.4." For a new method where \(\theta\) is a free parameter that could substantially affect results, a brief sensitivity analysis or clear justification in the main paper would improve confidence. Without it, readers cannot assess how robust the results are to this choice.

### Trivial

1. **Default USVT and ECV (USVT) results are numerically identical for Graphons 1–3** (e.g., both 0.60 ± 0.09 on Graphon 1), suggesting ECV simply returns the default M on those settings. This is not necessarily wrong but should be noted/explained.

## Nice-to-Haves

- A diagnostic showing the fraction of ECV folds where matrix completion converges or fails, especially for Graphon 1.
- An experiment varying the imputation mean \(\theta\) across a range (e.g., 0.1 to 0.9) to demonstrate stability.
- A direct comparison to naive edge-removal CV without imputation, to isolate the value of the imputation step.

## Removed Points

The following points from the harsh critic were removed after verification against the paper:

- **"Structural flaw: core method not justified — equivariance assumption."** The critic claimed the method implicitly assumes the estimator is equivariant under the affine transformation and that this is likely false for non-linear estimators. This is not what the method requires. The method trains the estimator on \(\mathbf{A}^{[-k]}\) (whose expectation is \(\mathbf{P}^{[-k]}\)) and then applies the inverse affine transformation to the *estimate*. This is a standard practice of estimating a transformed quantity and back-transforming. There is no equivariance requirement. Lemma 1 establishes the relationship, and Theorem 1 provides asymptotic guarantees via Condition 1. The critic's "equivariance" objection is a misreading.

- **"Theorem is circular — says the method works if the method works."** This mischaracterizes Condition 1. The condition bounds the \(K\)-fold optimism bias, which is a standard quantity in CV theory. The paper states it can be verified computationally (Appendix Figure S.3), making it a checkable condition rather than a circular assumption. Most CV theory papers require similar high-level conditions.

- **"ECV vs. CV-imputation speed claim contradiction is a basic inconsistency that undermines trust."** The contradictory sentence appears in a single figure caption that is clearly a typo — the data, main text, and Figure 5's caption all consistently show CV-imputation as faster. The severity of this criticism was inflated.

- **"Introduction does not articulate why imputation with Bernoulli(θ) preserves representativeness."** Section 3 provides Lemma 1 which directly addresses this: the imputed training matrix has an affine relationship to the original P, making the correction exact in expectation.

- **Various reproducibility nitpicks** (hyperparameters, implementation details, appendix-deferred content).

## Novel Insights

None beyond the paper's own contributions. The paper's core insight — that random Bernoulli imputation followed by affine correction enables valid cross-validation for graphon models — is itself the novel observation. The reviews do not surface a deeper insight that the authors missed.

## Suggestions

1. **Investigate and explain the ECV (NS) anomaly on Graphon 1.** If the matrix completion step is failing on certain folds, report this and either flag the comparison as imperfect or replace ECV results with a properly tuned ECV implementation. At minimum, add a caveat.

2. **Move a \(\theta\)-sensitivity experiment or clear guidance to the main paper.** Even a short paragraph stating what \(\theta\) was used (e.g., the empirical mean edge density) and a reference to the appendix showing stability across a range would suffice.

3. **Add a naive baseline** (remove validation edges → set to 0 → estimate → predict) to demonstrate that imputation is indeed the beneficial component, not just the affine correction.

4. **Fix the contradictory figure caption** — the typo is minor but harms credibility disproportionate to its size.

## Score and Decision

**Calibration.** Round 1 bracketing searched three bands with topic queries related to graphon/network cross-validation: weak anchors (avg ≤3.5), mid anchors (3.5–7.5), and strong anchors (≥7.5). The weak anchors (scores 2.60–3.33) had fundamentally flawed or incomplete contributions. The strong anchors (8.00) were extremely clean papers with theoretical depth and polished execution. The mid-range produced anchors between 3.67 and 6.75. Round 1 bracket: [5.0, 7.0].

Round 2 narrowed within (5.5, 7.5) and (6.0, 7.5). The best comparators were:
- **LCQ7YTzgRQ** (avg 6.25, "On the Role of Edge Dependency"): theoretical bounds with new generative models; mixed reception (rejected). My paper has more extensive empirical validation and a clearer practical contribution.
- **BOQpRtI4F5** (avg 6.75, "Towards Bridging Generalization"): accepted paper with solid GNN theory; experiments limited but theoretical contribution clean. My paper has broader experiments but a less tight theoretical result.
- **zwU9scoU4A** (avg 6.67, "Learning Mean Field Games"): accepted paper on graphex MFGs; clear motivation, theory, and experiments, though missing baselines. My paper has more thorough baselines but some presentation issues.
- **PdZkfSttGK** (avg 5.25, "Nonparametric Covariance Regression"): incremental contribution, marginal improvements. My paper is clearly stronger.

My paper sits below the clean 6.67–6.75 anchors due to the unresolved ECV anomaly and the abstractness of Condition 1, but above the 5.25–5.75 papers due to the genuine novelty, theoretical result, and extensive evaluation. Final score: **6.0**.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>