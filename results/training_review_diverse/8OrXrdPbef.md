Now I have a thorough understanding of the paper and can verify each claim. Let me compose the final consolidated review.

## Summary

FLAG proposes a clustered federated learning algorithm that combines a weighted class-wise data similarity metric (using principal vectors from truncated SVD) with gradient cosine similarity to build a proximity matrix for agglomerative hierarchical clustering. The method also includes a one-shot procedure to determine the optimal number of clusters via a lightweight validation search before full training begins. Experiments on CIFAR-10, FMNIST, SVHN, and CIFAR-100 show accuracy improvements over several baselines under combined label skew and quantity shift.

## Strengths

- **Consistent accuracy gains across multiple datasets and heterogeneity settings.** Tables 2 and 3 show FLAG achieving the highest test accuracy across all four datasets under two levels of label skew (20%, 30%) and two levels of quantity shift (α′=1 and α′=0.25). On CIFAR-10 with 20% label skew and low quantity shift, FLAG reaches 81.9%, outperforming the next best method (IFCA) by notable margins.

- **Ablation study confirms the necessity of combining data and gradient.** Table 4 demonstrates that using both data and gradient similarity (G+D) yields substantially higher accuracy than either component alone (e.g., 81.9% vs. 63.5% for data-only and 65.2% for gradient-only on CIFAR-10), directly validating the core algorithmic contribution.

- **One-shot clustering with an efficient optimal-cluster search (Algorithm 3).** FLAG determines the clustering threshold α and the number of clusters before full FL training begins, using a lightweight validation procedure on a subset of clients. This avoids the iterative reclustering needed in methods like IFCA or CFL and is a practical contribution.

- **Weighted class-wise data similarity metric (Eq. 4–6) explicitly accounts for quantity imbalance.** The weighting scheme (Eq. 4) increases dissimilarity when class sizes differ between clients, which is a principled mechanism for handling quantity shift that prior data-only methods (e.g., PACFL) do not incorporate. The use of principal angles with class-level granularity is a genuine refinement over per-client subspace methods.

## Weaknesses

### Fatal
None.

### Major

- **No variance or statistical significance reporting.** Tables 2–4 and Figure 2 report accuracy numbers without any measure of variance (standard deviation, confidence intervals, or multiple-run results). In federated learning with non-IID data and random client sampling, results can vary substantially across runs. Without variance estimates, the claim that FLAG "consistently outperforms" baselines is not statistically substantiated. This is the most significant evidential gap in the paper.

- **Incomplete specification of baseline configurations, compromising fairness of comparison.** The paper lists seven baselines (FedAvg, FedProx, PerFedAvg, PACFL, IFCA, CFL, FedSoft) but provides no details on how they were configured or tuned:
  - IFCA requires the number of clusters as input — was this set to the ground-truth number (which FLAG does not know) or tuned? The paper is silent.
  - PACFL, CFL, and FedSoft have critical hyperparameters (subspace dimensions, pruning thresholds, proximal/soft clustering terms) with no mention of tuning.
  - FedProx's proximal term μ and PerFedAvg's meta-learning hyperparameters are not reported.
  Without this information, the reader cannot assess whether the comparisons are fair or whether the gains reflect suboptimally tuned baselines.

- **Model architecture for the main experiments is not specified.** The paper never states what neural network architecture (CNN? ResNet? MLP?) was used for training across CIFAR-10, FMNIST, SVHN, and CIFAR-100. This is a fundamental reproducibility gap — the results cannot be independently reproduced or compared against without knowing the model backbone.

### Minor

- **Experimental scope does not match the breadth of claims in the motivation.** The paper motivates the method by listing four limitations of prior work, including the failure to handle concept shift, concept drift, and feature skew (Section 1, Limitations 1–4). The abstract and conclusion claim FLAG "addresses a broader range of data heterogeneity issues." However, the experiments test *only* label skew combined with quantity shift. Concept shift, concept drift, and feature skew are not evaluated. While the method's design may plausibly handle some of these, the current evidence does not support the breadth of the claimed generality.

- **Ablation study does not isolate the class-wise weighting contribution.** Table 4 compares data-only vs. gradient-only vs. combined, but does not ablate the *class-wise weighted* data similarity specifically. A comparison to a simpler data similarity (e.g., principal angles on the entire client dataset without class separation, or without the log-based weighting) is missing. Without this, the contribution of the weighted class-wise design is not isolated from the baseline data similarity method.

- **Key hyperparameters undisclosed or underspecified:**
  - δ in Eq. 5 (normalization range) is described as "can be regularized by the server" but no default value or tuning is given.
  - The grid-search range and step size for β are not reported.
  - The "lightweight model with simple architecture" used in Algorithm 3's optimal clustering search is not described at all.
  These gaps impair reproducibility.

- **Convergence analysis is partial.** Figure 2 shows accuracy over 80 rounds (under a "limited communication budget") without error bars. While FLAG appears to converge faster (20–30 rounds), it is unclear whether other methods would catch up given more rounds. Longer runs are needed.

- **Optimal clustering analysis (Figure 1) shown for only one heterogeneity setting (30% label skew, α′=1).** The stability of the elbow-determined α across different random seeds or different skew levels is not examined.

- **No discussion of limitations or costs.** The paper does not discuss the computational burden of per-class SVD on resource-constrained clients, the communication overhead of sending principal vectors in addition to gradients, or the sensitivity of the method to its hyperparameters (δ, β, p). Including this would strengthen the paper's credibility.

### Trivial
None.

## Nice-to-Haves

- A communication and computation cost comparison between FLAG and baselines (principal vector overhead vs. gradient-only approaches) would help practitioners assess the practical trade-off.
- A bootstrap or sensitivity analysis of the optimal α selection across multiple random seeds would strengthen the clustering validity claim.
- A simple synthetic experiment on concept shift or feature skew, even if preliminary, would substantially strengthen the generality claims.

## Removed Points

These points are flagged to be removed — treat them with caution.

- **"FLAG performs clustering only once before training begins is somewhat misleading"** — The paper fully describes the lightweight validation step in Algorithm 3. The claim is accurate as stated; the reviewer misread this as claiming the search is cost-free, which the paper never asserts.
- **"t′ is not specified"** — The paper states in Section 5 Setup: "the server selects 30 clients at random and runs 5 communication rounds of clustered FL," which specifies t′ = 5. The reviewer missed this.
- **"Evaluation metric concern"** — The reviewer acknowledges baselines are measured the same way and the comparison is fair. This is not actually a weakness.
- **"No link provided (expected for blind review)"** — Standard for double-blind submission; not a weakness.
- **Criticism about "simple linear combination" of V̂ and Ĝ lacking principled fusion discussion** — The paper uses min-max normalization before combining, which is a standard and reasonable approach. This is a design choice, not a flaw.
- **The reviewer's concern about "p is ambiguous because feature dimension matters"** — The paper specifies p ≈ 1% of |D_{i,c}|, which is a clear specification relative to sample count. While technically the SVD on the transpose produces at most min(features, samples) vectors, the paper's specification is sufficient for reproduction.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. **Add variance reporting.** Run each experiment at least 5 times with different random seeds for data partitioning and client selection, and report mean ± std. This is essential for credibility in FL.
2. **Document all baseline hyperparameters.** For each baseline (FedProx μ, IFCA cluster count, PACFL settings, CFL threshold, FedSoft proximal term, PerFedAvg meta-stepsize), report the values used and how they were chosen. For IFCA, clarify whether the number of clusters was set to the ground truth or estimated.
3. **Specify the model architecture** used for all experiments (main training and lightweight validation model).
4. **Tighten the ablation.** Compare FLAG (weighted class-wise) against an unweighted class-wise version and a version that computes principal angles on the entire client data without class separation, to isolate the contribution of the class-wise weighting.
5. **Disclose the missing hyperparameters** (δ value, β grid-search range and step, lightweight model architecture) and ideally add a sensitivity analysis for β and δ.
6. **Acknowledge the scope limitation** honestly — the paper tests label skew + quantity shift but not concept shift/drift or feature skew — and either add a preliminary experiment on one of these or explicitly scope the claims.

## Score and Decision

The paper addresses a genuine problem in clustered FL with a sensible algorithmic idea — combining data and gradient similarity via a class-wise weighted metric. The reported accuracy improvements are consistent across multiple datasets and skew settings, and the ablation study cleanly validates the core design choice. However, the paper has significant evidential and reproducibility weaknesses: (i) complete absence of variance/statistical reporting, (ii) no specification of how baselines were tuned, (iii) the main model architecture is never described, and (iv) the experimental breadth falls short of the motivational claims. These gaps prevent the current evidence from being fully convincing. The paper needs major revisions before it can be accepted.

MY FINAL SCORE: <pineapple>5.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>