Now I have a thorough understanding of the paper and can verify the reviewer claims. Let me compile the final consolidated review.

## Summary

This paper proposes HCDC (Hyperparameter-Calibrated Dataset Condensation), a method that preserves validation-performance rankings of architectures/hyperparameters when replacing the original dataset with a condensed synthetic set. Instead of the standard condensation goal (preserving generalization for a single architecture), HCDC aligns hypergradients (gradients of validation loss with respect to hyperparameters) between the original and synthetic datasets. The synthetic validation set is learned to minimize cosine distance between these hypergradients, while the synthetic training set is fixed via standard condensation. Experiments on image (CIFAR-10/100 with NAS-Bench-201) and graph (Cora, Citeseer, Ogbn-arxiv, Reddit) benchmarks show dramatic improvements in Spearman rank correlation (e.g., 0.74 vs. near-zero for baselines on CIFAR-10) and near-optimal selected architecture performance.

## Strengths

1. **Novel formulation for ranking preservation via hypergradient alignment.** The paper formalizes the problem of preserving hyperparameter performance rankings during condensation (Definition 1, Hyperparameter Calibration) and proves equivalence to aligning hypergradients in a connected extended search space (Theorem 1, Section 3). This provides a principled framing that prior condensation methods lack.

2. **Dramatic improvement in ranking correlation over all baselines on image data.** On CIFAR-10, HCDC achieves a Spearman correlation of **0.74 ± 0.21**, while the next best baseline (K-Center coreset) reaches at most **0.19 ± 0.12**, and all standard condensation methods (DC, DSA, DM, KIP, TM) show negative correlations (Table 1). This is a qualitative jump — only HCDC produces a positive, practically useful correlation for hyperparameter search.

3. **Consistent gains on graph datasets across multiple compression ratios.** On Cora, Citeseer, Ogbn-arxiv, and Reddit, HCDC outperforms all baselines (Random, GCond-X, GCond) in both correlation and final test performance at every compression ratio (Table 2), with correlations above 0.8 even at the smallest ratios. The GCond baselines also learn synthetic data, making this a stronger comparison than the image experiments.

4. **Efficient hypergradient computation via IFT and Neumann series.** The method uses the implicit function theorem with Neumann series approximation to compute hypergradients with constant memory and complexity scaling linearly with the size of the hyperparameter search space (Section 5.1), making the approach tractable.

5. **Speed-up for off-the-shelf NAS algorithms while maintaining high accuracy.** Combined with DARTS-PT and REINFORCE on CIFAR-10, HCDC reduces search time to ~35–119 seconds (vs. 229–1492 seconds on original data) while achieving test performance within 0.8–0.7% of the oracle (Table 3). Prior condensation methods (DC) lose over 7% in the REINFORCE setting.

## Weaknesses

### Fatal
None.

### Major

1. **No report of condensation creation time, leaving the efficiency claim incomplete.** The paper's title and narrative emphasize "faster hyperparameter search" (Table 3 shows speed-ups for NAS algorithms on the condensed set). However, the time required to *create* the HCDC condensed dataset — which involves per-hyperparameter Hessian approximation, hypergradient computation, and iterative updates of the synthetic validation set — is never reported. If condensation takes hours, the speed-up during search may be moot, especially if the search space changes. The paper should report condensation wall-clock time and compare it to the time savings it enables.

2. **Evaluation is only on the architectures/hyperparameters used during condensation, not on unseen ones.** The Spearman correlation on 100 architectures from NAS-Bench-201 (or 80 sampled configurations for graphs) is computed on the *same* set of architectures that appear in the condensation loss via the hypergradient alignment objective (Algorithm 1 iterates over all λ in Λ). The paper does not test whether HCDC preserves rankings for architectures *not seen during condensation*. The paper acknowledges this as a limitation ("how the differentiable NAS model used for condensation generalizes to unseen architectures") but does not quantify it. This means the method is validated for *ranking a pre-specified candidate set* — which is a useful capability — but should not be presented as a general proxy for arbitrary search without evidence. The authors should clearly scope this claim and ideally provide an experiment holding out some architectures during condensation.

### Minor

1. **Gap between the theoretical equivalence and the practical approximation.** Theorem 1 establishes equivalence between hypergradient alignment and hyperparameter calibration on a *connected, compact continuous extension* of the search space. In practice, (a) the "HPO trajectories" used to construct the extended space are a heuristic with no guarantee of connectedness or differentiability for discrete spaces, and (b) the method samples only a *subset* of points along these trajectories rather than aligning over the entire continuous set. The paper does not analyze the approximation error. The theory motivates the method well but does not provide a rigorous guarantee for the practical algorithm. The paper should be more measured in its theoretical claims.

2. **Missing implementation detail: how hypergradients w.r.t. discrete architectures are computed.** For the image experiments on NAS-Bench-201, λ is a discrete architecture index, yet Algorithm 1 uses the update `λ ← λ − η_λ ∇_λ L^*_S(λ)`. The paper mentions "differentiable NAS methods like DARTS" in the related work section but does not specify what continuous relaxation or architecture embedding is used to enable gradient-based optimization over discrete architectures. This detail is essential for reproducibility, though it may be in the (stripped) appendix.

3. **No ablation study of key components.** The paper does not ablate components such as: how correlation changes if hypergradients are aligned at fewer trajectory points, if the synthetic training set is learned via a different SDC method, or if the Neumann series truncation varies. This limits understanding of which design choices drive the performance.

### Trivial
None.

## Nice-to-Haves

- A study of generalization to held-out architectures: hold out a subset of architectures during condensation and measure Spearman correlation on the held-out set.
- Condensation wall-clock time and total time-to-accuracy analysis (condensation + search) to quantify the break-even point.
- Statistical significance tests (e.g., whether HCDC's correlation significantly differs from the best baseline).

## Removed Points

These points were flagged by the reviewers but are either factually incorrect, speculative, or misread the paper:

- **"The method is evaluated unfairly because baselines use random split of condensed data while HCDC learns a separate validation set."** This is the point of the method — the contribution is precisely that learning a validation set for ranking is better than not doing so. The comparison is fair; no baseline was ever designed to preserve rankings. REMOVED as a misunderstanding of the contribution.

- **"The specific SDC method for the synthetic training set is not specified."** The paper states it uses the gradient matching formulation (Eq. sdc-gm), which is a specific, well-known method (Zhao et al., 2020). REMOVED as factually incorrect.

- **"Baseline verification: KIP and TM correlations should be checked against literature."** This is speculative and not a concrete weakness of the paper. If the results are reported honestly, there is no problem. REMOVED.

- **Missing appendix content / missing proofs in appendix.** The parser strips these from all papers; they exist in the original submission. REMOVED per instructions.

- **Figure 4 visualization criticism about black-and-white readability.** This is a minor formatting nitpick. REMOVED.

- **Requests for more models/datasets beyond what is standard for this task.** The paper already evaluates on 2 image datasets + 4 graph datasets, which is a reasonable scope. REMOVED.

## Novel Insights

The two reviews together highlight a tension that the paper itself does not fully resolve: the theoretical framing (alignment over a continuous extended space) suggests a general-purpose proxy dataset, while the empirical validation is restricted to the candidate architectures used during condensation. This gap between the theory's implied scope and the experiments' demonstrated scope is the paper's most important limitation. A novel observation is that the paper's graph experiments partially mitigate this concern — because the convolution filter search space is intrinsically continuous, the "unseen architecture" question is less relevant there, and the results on graphs are uniformly strong across multiple datasets and compression ratios.

## Suggestions

1. Report condensation wall-clock time and include a total time comparison (condensation + search) for the NAS experiments.
2. Add an experiment that holds out a subset of architectures during condensation and tests Spearman correlation on the held-out set. This would directly address the generalization concern.
3. Clarify how the continuous extension is constructed for discrete architecture spaces (NAS-Bench-201) — specifically, the relaxation or embedding used to enable gradient-based optimization over λ.
4. Scope the claims more precisely: HCDC preserves rankings for a pre-specified candidate set, and generalization to unseen architectures is not yet demonstrated.
5. Add an ablation study isolating the value of the trajectory-based continuous extension vs. aligning hypergradients only at the discrete points.

## Score and Decision

The paper introduces a well-motivated, novel formulation for dataset condensation aimed at preserving hyperparameter rankings. The empirical results are unusually strong: HCDC is the first condensation method to achieve positive Spearman correlations on cross-architecture evaluation, and the gains over baselines are large and consistent across both image and graph domains. The method is technically sound, with a clear theoretical motivation and efficient implementation.

The major weaknesses are (a) the missing condensation time reporting, which undermines the efficiency claim, and (b) the lack of testing on held-out (unseen during condensation) architectures, which limits the demonstrated scope. Neither weakness invalidates the core contribution; both are addressable in revision. The minor weaknesses (theory-practice gap, missing ablation, missing implementation detail) are standard for a conference paper.

MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>