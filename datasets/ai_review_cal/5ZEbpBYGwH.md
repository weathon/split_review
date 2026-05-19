- Decision: Accept
- Avg Score: 7.25
- Scores: 5, 8, 8, 8
I have now carefully read the paper and verified all claims against the actual content. Here is my consolidated review.

---

## Summary

COPER proposes an end-to-end deep multi-view clustering framework that combines view-specific autoencoders, a CCA-based correlation loss, a clustering head with multi-view pseudo-labeling, and a novel within-cluster permutation scheme that creates artificial correspondences across views. The paper provides a theoretical link showing that CCA with within-cluster permutations approximates supervised LDA, and an error bound for how pseudo-label noise degrades this approximation. Experiments across 10 benchmarks show COPER achieves the highest ACC on all datasets and highest ARI on 9/10 compared to recent end-to-end MVC methods (DSMVC, CVCL) and several two-stage baselines.

## Strengths

1. **Novel and well-motivated technical idea**: The within-cluster permutation mechanism for CCA-based MVC is original. By permuting samples with the same pseudo-label across views before computing the CCA objective, the method injects discriminative (cluster-relevant) information into what would otherwise be a purely correlational representation. This is a clever way to bridge unsupervised representation learning with clustering.

2. **Strong empirical performance**: COPER achieves the highest ACC on all 10 datasets and highest ARI on 9/10 (Table 1). The improvements are substantial on several datasets — e.g., ACC on Caltech101-20 is 54.83 vs. 48.18 (DCCA-AE); ARI on MSRVC1 is 82.26 vs. 64.27 (CVCL). Results are reported as mean±std over 10 runs, which is more rigorous than the best-run reporting in the original DSMVC and CVCL papers.

3. **Controlled case study validates the mechanism**: The F-MNIST experiment (Figures 1-2 in the paper) systematically varies the fraction of permuted samples and shows that increasing permutation fraction monotonically improves ARI, shrinks the eigenvalue gap to LDA, and reduces inter-class correlation. This provides direct causal evidence for the claimed mechanism, not just correlational evidence from end results.

4. **Ablation isolates component contributions**: On METABRIC, removing within-cluster permutations drops ACC from 49.13 to 45.82 and removing pseudo-labels drops it to 45.39 (Table 2). The ablation is limited to one dataset (discussed below), but for that dataset it cleanly attributes gains to the permutation and pseudo-label components.

5. **Honest limitations section**: The paper openly acknowledges the large-batch requirement, sensitivity to many clusters, suboptimal loss weighting, and the bijective-correspondence assumption — which strengthens reader trust.

## Weaknesses

### Fatal
None.

### Major

1. **Missing implementation details that prevent reproduction.** The paper does not specify: (a) autoencoder architectures (number of layers, dimensions, activations), (b) optimizer type (only "SGD" is mentioned; no learning rate, momentum, or schedule), (c) batch size, (d) number of epochs, (e) the threshold λ used for filtering pseudo-labels (introduced at line 150, never given a value or selection procedure), or (f) the hyperparameter β for weighting the correlation loss on permuted data (introduced at line 181, never quantified). These are not trivial omissions — the method involves multiple loss components (MSE × N_views, cross-entropy × N_views, correlation × N_views choose 2, on both original and permuted data) and a multi-step pseudo-label filtering pipeline. Without these details, the experiments cannot be reproduced, and it is impossible to assess whether the comparisons against DSMVC and CVCL (which the authors apparently re-ran, see Weakness 4 below) were conducted under fair and matched conditions.

2. **Ablation on a single dataset is insufficient to support general claims.** The ablation study (Table 2) is conducted only on METABRIC. The paper explicitly claims that "the results indicate that the pseudo-label procedure slightly improved assignment accuracy over K-means [and] the new permutation scheme boosted performance by more than 10%." But with one dataset, there is no evidence that these conclusions generalize across different data types, numbers of views, sample sizes, or cluster counts. The main evaluation uses 10 diverse datasets, so ablating on at least 3 (e.g., one image-based, one text-based, one with many views) would be straightforward and would substantially strengthen the claims.

### Minor

3. **Zero variance on MNIST-USPS for ACC and ARI is unexplained.** COPER achieves ACC 99.88±0.0 and ARI 99.73±0.0 over 10 runs. A zero standard deviation on two metrics over 10 independent runs with different random seeds is unusual and warrants comment. The most benign explanation is that all 10 runs converged to the same near-perfect solution, but the paper does not provide this or any other explanation. (NMI has a small nonzero standard deviation of 0.1, which mitigates concern about a seed-leakage artifact, but the point remains.)

4. **Baseline comparison protocol is ambiguous.** The paper states (lines 296-297): "the results of Chen_2023_ICCV, tang2022deep are different from the values reported by the authors since we report the mean over ten runs while they report the best result." This sentence strongly implies that the authors re-ran DSMVC and CVCL, but it never states this explicitly. If the baselines were re-run, the hyperparameters and settings used for those methods should be reported alongside those for COPER. If the values are taken from the original papers in some transformed way, that should be clarified. The reader currently cannot assess whether the headline comparison is apples-to-apples.

5. **NMI on Caltech101-20 is lower than basic baselines.** COPER achieves NMI 49.25 on Caltech101-20, while Raw (K-means on concatenated raw features) achieves 61.77 — a >12 point gap that is not discussed. Since NMI is reported alongside ACC and ARI, readers will notice this. The paper's limitations section notes sensitivity to many clusters (20 for Caltech101-20), and ACC/ARI are indeed the strongest for COPER on this dataset, so the NMI gap may be a metric-specific artifact, but it deserves an explicit explanation.

6. **Theoretical contribution is modest.** Proposition 1 (CCA with permutations → LDA) follows from the analysis of Kursun (2011), as the paper acknowledges. The error bound (|λ̂_i − λ_i| ≤ ‖D‖₂) is a direct application of Weyl's inequality from perturbation theory, again correctly attributed. The paper's value lies more in the empirical instantiation and the controlled experiments showing the mechanism works, rather than in novel theoretical results. This is not a flaw per se — the paper is honest about attributions — but the theoretical framing in the title and abstract may set expectations of deeper theoretical novelty.

7. **Pseudo-label filtering justification is unclear.** The procedure (Section 3.3) selects top N_mb/K samples per cluster by probability, computes cluster centers, then selects again by cosine similarity with threshold λ, then merges across views. The paper never justifies why both probability-based and similarity-based selection are needed, nor how λ should be chosen. Is λ a fixed constant or tuned per dataset?

### Trivial

- The NMI value for "COPER w/o permutations" in Table 2 reads "22.41±31.3.1", which appears garbled.
- The introduction (line 23) uses "inter-class (within class)" which is internally contradictory ("inter-class" means between classes, while the permutation is within a class; should read "intra-class").
- The NMI section in Table 1 for CCV shows "26.32$\pm$0.}7" with a misplaced closing brace (likely a parser artifact but worth fixing).

## Nice-to-Haves

- **Expand the ablation** to at least 3 datasets varying in size, dimensionality, and number of views, to support the claim that permutations are consistently beneficial.
- **Add sensitivity analysis** for the fraction of permuted samples per mini-batch (currently implied to be all reliable pseudo-labels) and for the λ and β hyperparameters.
- **Clarify how the LDA connection transfers** from the linear CCA setting (used in the F-MNIST case study) to the deep nonlinear autoencoder setting (used in the main method). A brief analysis or discussion would bridge this gap.
- **Add statistical significance tests** (e.g., paired bootstrap or corrected t-test) between COPER and the best baseline on each dataset, given that many reported standard deviations overlap.
- **Provide a code release statement** to increase confidence in reproducibility.

## Removed Points

These points from the reviewers were removed, with justifications:

- *"Critique of prior end-to-end methods as 'limited to specific domains' is not strongly supported"* (Harsh Critic) — This is a scope-creep criticism of a brief contextual claim in the introduction; the paper's experiments show strong general-domain performance which supports the claim.
- *"The introduction and related work..." narrative criticisms* — These are subjective stylistic opinions with no concrete error.
- *"Table formatting" and "presentation" nitpicks* — Formatting artifacts from PDF extraction and style preferences, not substantive issues.
- *"Missing appendix/proofs" style concerns* — Parser strips appendices; these are assumed to exist in the original submission.
- *Strength finder's claim that removing permutations causes ">10% relative decline"* — The actual relative decline in ACC on METABRIC is (49.13−45.82)/49.13 ≈ 6.7%, not >10%. The claim is factually inflated; the correct figure still supports the point.
- *Strength finder's generic/self-congratulatory strengths* (e.g., "this paper addresses an important problem") — Generic and not specific to this paper's contributions.

## Novel Insights

None beyond the paper's own contributions. The two reviews surface a tension: the harsh critic identifies several genuine gaps (missing implementation details, single-dataset ablation, zero-variance result) that are verifiable from the paper, while the strength finder correctly identifies the novelty and empirical strength. Neither review surfaces issues beyond what the paper itself documents.

## Suggestions

1. **Add a reproducibility appendix** specifying: autoencoder architectures (layer sizes, activations) for all 10 datasets, optimizer (SGD with which learning rate and schedule, or switch to Adam), batch size, max epochs, early stopping criteria, the λ and β values used (and whether they were tuned per dataset or fixed).
2. **Explicitly state the baseline protocol**: "We re-ran DSMVC and CVCL using the authors' publicly released code with the following hyperparameters: …" If the code is not public, state this and explain how the comparisons were conducted.
3. **Address the MNIST-USPS zero-variance result** with a brief explanation (e.g., "the embedding space was perfectly separated in all 10 runs" or "a near-deterministic convergence occurred; the small NMI variance (±0.1) confirms that runs were not identical").
4. **Expand ablation to at least 2-3 more datasets** (e.g., one high-dimensional image dataset, one text dataset like Reuters, and one with many views like Caltech5V-7).
5. **Add a paragraph discussing the Caltech101-20 NMI result**, noting that ACC and ARI are high while NMI lags, and explaining why (e.g., NMI's sensitivity to cluster imbalance or the specific class structure of that dataset).
6. **Clarify the pseudo-label filtering**: why both probability-based and similarity-based selection are needed, and how λ is determined.
