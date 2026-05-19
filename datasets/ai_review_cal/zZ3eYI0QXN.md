- Decision: Reject
- Avg Score: 3.00
- Scores: 3, 3, 3, 3
Now I have all the information needed. Let me produce the final consolidated review.

## Summary

This paper proposes ProuDT, a probabilistic (soft) decision tree that maintains axis-aligned splits by assigning a single deterministic feature to each decision node via a simple strategy: pre-rank features by mutual information, then assign them cyclically to nodes from root to leaves. Only the split thresholds and leaf class scores are learned via gradient descent. This replaces the dense feature-weight matrix used by the main competitor, GradTree, with a much more parameter-efficient design. Experiments on 12 UCI datasets compare ProuDT against CART and GradTree, showing competitive or superior accuracy (particularly on high-dimensional multi-class datasets like SEMEION) with substantially reduced training and inference time.

## Strengths

- **Simple, well-motivated design that reduces parameters.** By fixing the feature per node via pre-ranked cyclic assignment and learning only thresholds and leaf scores, ProuDT eliminates the dense per-node feature-weight matrix used by GradTree. This is a genuinely clean approach — the ablation study (Fig. 2) confirms that the ranking accelerates convergence at shallow depths, and the runtime results (e.g., 13s vs. 240s on BANK MARKET) demonstrate the practical payoff.

- **Strong empirical results on high-dimensional multi-class datasets.** On SEMEION (256 features, 10 classes), ProuDT achieves 88.05% accuracy vs. 58.27% for GradTree (a ~30-point gain) and 72.45% for CART. On PROTEIN, ProuDT reaches 67.66% vs. 52.01% for GradTree. These are large, unambiguous improvements that go well beyond "marginal" differences.

- **Consistent univariate splits during both training and testing.** Unlike Silva et al. (2020), which uses multivariate splits during training and converts to univariate splits at test time (creating a train–test discrepancy), ProuDT uses the same single-feature split throughout. This is a principled design choice that supports both efficiency and interpretability claims.

- **Ablation studies validate key design choices.** The feature-positioning ablation (Fig. 2) shows that MI-ranked features improve accuracy at shallow depths compared to the original (arbitrary) feature order. The loss-function ablation (Tables 2–3) shows focal loss converges faster than cross-entropy without sacrificing accuracy.

- **Default hyperparameters are validated across two separate dataset collections.** The preliminary study on 12 UCI datasets and the formal experiment on another 12 datasets both use fixed default depths (8 for low-dim, 11 for high-dim), supporting the claim of ease of deployment.

## Weaknesses

### Fatal
None.

### Major

- **Overstated novelty claim.** The paper asserts (Section 1, Contribution 1) that this is *"the first method to directly utilize univariate splitting for probabilistic tree induction."* However, DNDT (Yang et al., 2018) — which the paper itself cites — uses per-feature soft binning (univariate/axis-aligned splits) within a probabilistic tree framework. While DNDT has scalability limits (Kronecker product beyond ~12 features), this does not negate its status as a prior univariate probabilistic tree. The claim should be bounded to reflect the specific technical differences (e.g., explicit tree structure with per-node thresholds vs. implicit tree via Kronecker product).

- **Evaluation scope is too narrow to fully support the headline claims.** The experimental comparison includes only two baselines: CART (a greedy standard) and GradTree (the single most recent gradient-based univariate competitor). The paper claims ProuDT achieves *"superior accuracy"* and is *"state-of-the-art among univariate trees,"* but with only one non-greedy competitor tested, these claims rest on a thin evidence base. In particular:
  - No other soft/neural decision tree methods (e.g., TAO, the method of Hehn et al. 2020, or Zantedeschi et al. 2021) are compared against, even on datasets where they are applicable.
  - Gradient-boosted tree ensembles (XGBoost, LightGBM, CatBoost) are outside the paper's single-univariate-tree scope, so demanding them would be scope creep, but the paper should not claim "state-of-the-art" status without a broader competitor set within its own category.

- **Key experimental details are missing from the paper text, harming reproducibility.** The following are not specified: the focal loss focusing parameter γ value used in experiments, the optimizer (and its learning rate), batch size, number of training epochs, and the early stopping patience/criterion. The authors state they provide source code, which mitigates this concern, but these details should be in the paper itself for self-contained reproducibility.

### Minor

- **Depth hyperparameter is not controlled across methods.** ProuDT uses depths of 8 (low-dim) and 11 (high-dim), selected from its own preliminary study. GradTree uses its suggested default depth of 10 (from its paper). Since tree depth directly affects accuracy and the comparison is central to the paper's claims, this asymmetry should be analyzed — e.g., by running both methods at multiple depths on a subset of datasets.

- **The interpretability claim is asserted but not demonstrated.** Section 3.3 describes how feature ranking provides "transparent explanation of feature significance," but no case study, feature-importance visualization, ablation of what interpretability means in practice, or comparison with CART's Gini-based feature importance is provided. Since "maintaining interpretability" is a primary motivation (Section 1), this claim needs supporting evidence.

- **No statistical significance testing.** Results are reported as average ± std over 10 runs, but no paired statistical test (e.g., Wilcoxon signed-rank over datasets) is performed to determine whether accuracy differences between ProuDT and baselines are significant. Given that many binary-dataset differences appear small, this is needed to support the superiority claims.

- **Preliminary study datasets are not named.** The 12 UCI datasets used to determine default depths and for the feature-positioning ablation (Fig. 2) are referred to only as "12 UCI datasets." This limits the reproducibility and interpretability of these experiments.

- **Accuracy gains on binary datasets are small and not discussed.** Based on the reported Table 1, the largest gap between ProuDT and the best baseline on binary datasets is ~0.44 percentage points, and standard deviations overlap. The paper frames its results as uniformly superior but does not acknowledge or discuss this pattern.

### Trivial

- The focal loss focusing parameter γ is defined with "γ ≥ 0" (Eq. 5) but the specific value used in all experiments is not reported.

## Nice-to-Haves

- A controlled depth comparison (ProuDT and GradTree at depths 6, 8, 10, 12) on a subset of datasets would isolate the effect of the feature-assignment strategy from the depth hyperparameter.
- Brief analysis explaining why ProuDT dramatically outperforms GradTree on SEMEION (e.g., whether GradTree overfits or its default hyperparameters are particularly poor on this dataset).
- Comparison of different feature ranking methods (MI vs. random-forest importance vs. χ² vs. random order) to show robustness to the choice of ranking technique.
- Including CART training time in the runtime comparison (only test time is reported).

## Removed Points

These points were raised by one or both reviewers but removed from the main weakness list with justification:

1. **Feature ranking using labels constitutes "information leakage"** — The critic suggested that using mutual information with labels to rank features before training could leak label information. This is standard practice for feature selection and pre-processing; it is not leakage in any problematic sense. Removed because it misunderstands standard pipeline design.

2. **Demand for XGBoost/LightGBM/CatBoost baselines** — The paper is scoped to single univariate decision trees. Requiring gradient-boosted ensemble methods as baselines is scope creep and would be inappropriate for a paper whose contribution is about improving individual tree learning.

3. **Requiring a comparison of different cyclic assignment strategies (e.g., top-k only, random cyclic)** — This could be interesting but is a speculative suggestion, not a specific identified flaw. The existing ablation (ranked vs. original order) is a reasonable first step. Removed as a speculative "could have done more" critique.

4. **Criticism that quantile transform "may bias results toward ProuDT"** — No evidence or mechanism is provided for why quantile normalization would specifically favor ProuDT over GradTree (which operates on the same transformed data). Removed as unsupported speculation.

## Novel Insights

None beyond the paper's own contributions — the reviews converge with the paper's self-assessment that the cyclic MI-ranking feature assignment is a novel simplification over GradTree's dense-weight approach, but neither review surfaces an observation about the method that the authors themselves did not articulate.

## Suggestions

1. **Bound the novelty claim precisely.** Replace "first method to directly utilize univariate splitting for probabilistic tree induction" with a more precise statement, e.g., *"first gradient-optimized probabilistic tree with explicit per-node deterministic feature assignment and threshold-only learning"* — distinguishing the approach from DNDT's Kronecker-product-based soft binning.

2. **Broaden the baseline comparison.** At minimum, compare against one additional soft/neural decision tree method applicable to the datasets (e.g., TAO, or the method of Hehn et al. 2020 on datasets where it scales). If adding ensemble baselines, explicitly state that the paper focuses on single trees and include the comparison for reference.

3. **Add a depth-controlled experiment.** Run both ProuDT and GradTree at depths {6, 8, 10, 12} on a subset (e.g., 4–6 datasets) and report accuracy and runtime to decouple the effect of depth from the feature-assignment strategy.

4. **Report all missing experimental hyperparameters in the paper text:** focal loss γ, optimizer, learning rate, batch size, epochs, early stopping patience/criterion.

5. **Demonstrate interpretability concretely.** Add a feature-importance visualization comparing ProuDT's MI-ranked assignment against CART's Gini importance on a real dataset, with a brief qualitative discussion.

6. **Include statistical significance testing.** A Wilcoxon signed-rank test (or similar paired test) over datasets between ProuDT and each baseline would substantially strengthen the empirical claims.

7. **Name the preliminary study datasets.** Listing the 12 UCI datasets used for ablation/parameter selection would improve reproducibility and allow readers to contextualize Figure 2.
