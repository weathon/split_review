- Decision: Accept
- Avg Score: 7.00
- Scores: 5, 8, 8, 6, 8
Now I have all the information needed. Let me produce the final consolidated review.

## Summary

This paper introduces Intersort, an algorithm that recovers the causal order (topological ordering) from datasets containing many single-variable interventions. The key contributions are: (1) the ε-interventional faithfulness assumption, which links the existence of directed paths to detectable marginal distribution shifts under intervention; (2) a score function on permutations whose optimum provably recovers a valid causal order under this assumption; (3) theoretical upper bounds on expected ordering error under incomplete interventions, including scaling behavior in high dimensions; and (4) the Intersort algorithm that approximately optimizes the score via greedy initialization followed by local search. Empirical results on four synthetic data types (linear, RFF, NN, GRN) show Intersort achieving lower D_top error than PC, GIES, DCDI, and EASE across most intervention ratios.

## Strengths

- **Novel problem formulation with theoretical backing**: The paper is the first to formulate causal order as the explicit target from interventional data, rather than treating it as a byproduct of graph recovery. The theoretical guarantees (Theorem 1 for full intervention, Theorem 2 with ancestor-set bounds, Lemma 6 for scaling behavior) are non-trivial and clearly stated.

- **Strong empirical performance across diverse synthetic domains**: In Figure 4, Intersort achieves lower median D_top than four baselines across linear, RFF, NN, and GRN domains at most intervention ratios. The paper also shows (line 284) transparent acknowledgment of the two settings where baselines win (GIES on linear, DCDI on NN at 25-50%). The consistent monotonic improvement with more interventions demonstrates effective utilization of interventional data.

- **Empirical validation of optimization quality**: For d=5, Intersort's approximation and the exact score optimum yield nearly identical D_top scores with overlapping 95% confidence intervals (Figure 2), validating that the two-step heuristic introduces negligible suboptimality in small settings.

- **Scalable theoretical bound**: Lemma 6 proves that under a sparse Erdős–Rényi graph (constant expected edges per variable), the expected normalized error remains bounded by a constant independent of dimensionality, supporting applicability to large-scale settings.

## Weaknesses

### Major

- **The ε-interventional faithfulness assumption is stronger than the paper's "lighter" framing suggests, and its scope is not fully characterized.** The paper states (line 23) that ε-interventional faithfulness is "a lighter version of many of the existing assumptions in causal discovery literature," but the assumption is structurally different from standard faithfulness: it requires that *every* directed path (i.e., if there is a directed path from i to j) produces a marginal shift above ε. This rules out path cancellation, which can occur in nonlinear systems. Lemma 4 covers linear SCMs with continuous coefficients (non-zero path coefficients almost surely prevent exact cancellation), but this is a relatively narrow characterization. The relaxation in Section 5 handles the worst case (only direct children detected), but the resulting bound depends only on parent sets, losing the ancestor-structure leverage that is the paper's main theoretical insight. The paper acknowledges this ("We leave further theoretical work to characterize how large the class of ε-interventionally faithful tuples is as future work"), but this gap between the assumption's scope and the claimed generality remains a material limitation.

- **Finite-sample gap between theory and practice.** All theoretical results (Theorems 1–3, Lemmas) are stated for population distributions. Section 7 (lines 242–244) discusses that in practice Wasserstein distances must be estimated from samples, but offers no analysis of how estimation error propagates into ordering error. The algorithm's score function sums O(d²) noisy distance estimates, and the sign of (D − ε) determines ordering decisions — threshold-crossing errors near ε are likely at n=100 samples per intervention, but this is not analyzed. The paper does not report confidence intervals on the distance estimates, does not ablate sample size, and does not justify why 100 samples per intervention is sufficient for the theoretical premises to approximately hold. This gap is acknowledged as future work (line 290), but it weakens the connection between the clean theoretical guarantees and the empirical validation.

### Minor

- **Lack of sensitivity analysis for key hyperparameters.** The ε parameter is set to 0.3 for linear, RFF, and NN domains, and 0.5 for GRN, with no justification for these specific values or analysis of sensitivity. The c=0.5 parameter in the score (Equation 1) is likewise stated without justification. The paper acknowledges this limitation (line 290) but an ablation would substantially strengthen reproducibility and trust in the method's robustness.

- **Baselines comparison, while reasonable, has uneven footing.** PC and EASE are observational-only methods; converting their outputs to a total order adds extra processing steps that weaken them. The paper correctly notes this challenge (line 281: "choosing appropriate baselines to compare to is not trivial") and Intersort still wins on most settings. However, the two strongest competitors that natively handle interventional data (GIES, DCDI) are given default hyperparameters without documentation of tuning effort. GIES uses Gaussian BIC score while some data types (RFF, NN) may not satisfy Gaussian assumptions. The comparison would be stronger with additional interventional-order-specific baselines and documented hyperparameter selection for DCDI and GIES.

- **Missing runtime comparison.** Intersort is simple and likely fast, but the paper provides no wall-clock time comparison with the baselines (DCDI, which requires gradient-based optimization, is presumably much slower). A runtime table would be informative for practitioners.

### Trivial

- The notation in Lemma 2 uses "ANⱼ^𝒢 \ ANᵢ^𝒢" which requires careful reading — a small illustrative example would help readability.

## Nice-to-Haves

- A finite-sample analysis (e.g., a union bound over pairs showing how sample size affects the probability that the estimated distance matrix preserves the correct ε-threshold relationships) would bridge the theory-practice gap discussed above.
- A data-driven heuristic for choosing ε (e.g., using the smallest non-zero distance in the matrix, per Remark 3) would reduce the need for domain-specific tuning.
- An additional baseline constructed by sorting variables by a simple interventional statistic (e.g., mean shift magnitude) would strengthen the comparison set.
- An ablation on the c parameter would clarify how it trades off false positives vs. false negatives in the ordering.

## Removed Points

These points from the reviewers are removed (with justification):

- **"The claim 'we are the first to propose an algorithm to infer the causal order from interventional data' should be softened"** — The paper already phrases this as "To our knowledge, we are the first..." (line 30), which is appropriately cautious. The novelty lies in treating causal order (not graph) as the primary target from interventional data, which is genuinely different from GIES recovering a CPDAG (partial order).

- **"The lemma for linear SCMs (Lemma 4) is straightforward and well-known; it adds little depth"** — This is an opinion about theoretical contribution weight, not a weakness. The lemma serves as a necessary building block showing the assumption's coverage; its simplicity is a feature, not a bug.

- **"For d=30, the algorithm's error is above the theoretical bounds (Figure 2 right), confirming suboptimality... the paper does not analyze how much of the gap is due to the algorithm versus the looseness of the bound"** — The paper acknowledges this explicitly (line 239: "we can observe room for improvement, as the error is above the upper-bounds for many settings"). This is transparent disclosure, not an omission.

- **"PC and EASE are clearly mismatched... this is a low bar... dilutes the claimed superiority"** — The paper notes (line 281) that no direct baselines exist for this new setting and includes these methods as reasonable reference points. The paper never claims superiority over these specific methods as the main result; the comparison is comprehensive coverage of available causal discovery tools.

- **"The baselines are methods designed to recover the full causal graph... using them as baselines for causal order from interventional data is natural but the paper should note that these methods' primary objective is different"** — The paper does note this (line 281: "our setting of predicting the causal order from interventional data has not been considered in the literature").

- **"The paper does not report error bars or statistical tests for the main results (Figure 4)"** — The paper uses violin plots for Figure 4, which display the full distribution of D_top scores across 10 runs. This is strictly more informative than simple error bars.

- **Various concerns about whether specific baselines' internal assumptions match the data distributions** — These are speculative; the paper follows standard practice in using GIES with Gaussian BIC and DCDI as published.

## Novel Insights

None beyond the paper's own contributions. The two reviews largely agree on the paper's strengths and weaknesses, with the harsh critic providing more granular methodological scrutiny of the assumption scope and finite-sample gap, while the strength finder correctly identifies the core contributions. The key insight that emerges from synthesis is that the paper's clean theoretical framework (population regime, ε-interventional faithfulness) sits somewhat uncomfortably between a fully rigorous analysis and a practical algorithm, with neither the assumption scope fully characterized nor the finite-sample regime theoretically analyzed. The paper's empirical success suggests the approach is genuinely useful, but the theoretical contributions are bounded by these gaps rather than providing the complete picture the paper seems to aim for.

## Suggestions

1. **Address the finite-sample gap**: Even a simple analysis (union bound over O(d²) pairs, showing how n affects the probability of distance estimates being on the correct side of ε) would substantially strengthen the paper. Alternatively, a thorough empirical ablation on sample size (n=50, 100, 500, 1000) would help validate that the 100-sample regime is sufficient.

2. **Add ε and c sensitivity analysis**: Show how performance varies with ε and c across at least one domain, and provide a data-driven heuristic for choosing ε (the paper hints at this in Remark 3 but doesn't implement it).

3. **Document baseline hyperparameters**: Report the specific hyperparameters used for DCDI (architecture, learning rate, training steps) and GIES, and note any tuning performed.

4. **Add runtime comparison**: A simple table showing wall-clock time for Intersort vs. DCDI and GIES for d=30 would help practitioners assess the practical trade-offs.
