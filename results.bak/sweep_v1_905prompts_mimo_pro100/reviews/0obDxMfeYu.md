Now I have all the information I need. Let me compose the final review.

## Summary

This paper introduces Medix, a median-centric framework for OOD detection from unlabeled wild data. It proposes using the element-wise median (EWM) of gradient deviations to identify OOD samples in a wild data mixture, then training a binary OOD detector on the filtered outliers plus labeled InD data. The paper provides theoretical bounds on inlier/outlier misclassification rates for the EWM filtering rule and demonstrates consistent improvements over 20 baselines across 11 InD-OOD pairs.

## Strengths

- **Theoretical contribution with two-sided guarantees**: Theorems 4.1 and 4.2 provide concrete upper bounds decomposed into contamination, concentration, and separation effects, establishing that EWM filtering remains robust when the OOD proportion π < 0.5. This is one of few works providing formal guarantees for the wild data OOD detection setting.

- **Empirically validated core hypothesis**: Figure 1 provides direct evidence that the L2-norm deviation between the InD gradient mean and the EWM of wild gradients increases monotonically as OOD samples are added, motivating the optimization objective in Equation 4 and the stopping criterion in Algorithm 1.

- **Consistent SOTA results across all benchmarks**: Tables 1 and 2 show Medix achieves the best FPR95 and AUROC across all five OOD datasets for both CIFAR-10 and CIFAR-100. On CIFAR-10, average FPR95 is 0.80% vs WOODS 3.40%; on CIFAR-100, 5.42% vs 6.74%. These gains are consistently distributed across OOD datasets rather than concentrated on one.

- **Most directly comparable prior work (SAL/Du et al., 2024a, scored 6.50)**: Medix proposes a different filtering mechanism (EWM vs. top singular vector) that achieves comparable or better results, with a cleaner theoretical analysis. The median-based approach is arguably more standard and interpretable.

- **Rigorous experimental design**: Following the exact protocol of Katz-Samuels et al. (2022a) ensures fair comparison; 20 baselines across two categories (InD-only vs. InD+wild); 11 InD-OOD pairs; standard WRN-40-2 architecture; standard metrics (FPR95, AUROC, InD Acc).

## Weaknesses

### Fatal

None.

### Major

- **Theory-algorithm gap — theorems do not directly analyze Algorithm 1**: The theorems bound properties of the EWM filtering rule applied to a mixture (i.e., the median of a mixture with contamination π remains close to the InD mean). However, Algorithm 1 is a greedy iterative leave-one-out procedure that removes k samples per iteration based on which removal causes the largest L2 distance drop. The paper never proves that this greedy procedure converges to a good solution of the combinatorial problem in Equation 4, nor bounds the approximation error. The paper consistently states "we provide a theoretical foundation that guarantees minimal error, which is further validated through experiments" (line 29) and "confirming the validity of our theoretical insights" (line 13), positioning the theory as validating the algorithm. This claim is not fully supported — the theory validates the EWM estimator property, not the greedy procedure. This is the most significant weakness because C2 (theoretical guarantees) is positioned as a core contribution.

- **Inflated headline claim comparing against InD-only baselines**: The abstract prominently states "an average of 40.98% improvement over KNN+" in FPR95 on CIFAR-100. KNN+ is an InD-only method without access to wild data, while Medix fundamentally relies on wild data. This comparison demonstrates that using wild data helps, not that Medix's median-based filtering is effective. The meaningful comparisons are against WOODS (1.32% on CIFAR-100, 2.60% on CIFAR-10) and other wild-data methods, which are real but modest improvements. The 40.98% figure reappears in the conclusions (line 266), creating a misleading impression of contribution magnitude.

### Minor

- **No sensitivity analysis on π despite theory requiring π < 0.5**: All experiments use π = 0.5 (line 178), which is at the boundary of the theoretical guarantee where the contamination term π/[2(1−π)] = 0.5. The paper does not evaluate how performance varies with π, even though the predecessor SAL paper (Du et al., 2024a) was also criticized by reviewers for not varying π. An ablation on π would test the method's practical range and validate the theoretical threshold.

- **Consistently lower InD accuracy than WOODS**: On CIFAR-100, Medix achieves 73.33% vs WOODS 73.91%; on CIFAR-10, 93.58% vs 94.74% (Tables 1-2). The paper attributes this to training on 25,000 InD samples vs. the full 50,000 (line 190), but WOODS presumably uses the same experimental setup, so this explanation is insufficient for the WOODS comparison. The trade-off between OOD detection gains and InD accuracy degradation deserves deeper discussion.

- **Marginal improvement on specific benchmarks approaches noise**: On SVHN with CIFAR-100 as InD, Medix achieves 0.16 FPR95 vs WOODS 0.17 FPR95 (Table 2) — a 0.01% difference. While the paper reports standard deviations (±0.02 for Medix), WOODS lacks reported variance, making it impossible to determine if this difference is significant. The paper's claim of outperforming "all baselines across the board" is technically true but overstates the margins in some cases.

### Trivial

None beyond formatting artifacts (which are parser issues, not paper problems).

## Nice-to-Haves

- **Direct comparison of greedy algorithm error rate against theoretical bound**: Empirically measuring the actual filtering error rate and plotting it against the theoretical bound from Theorem 4.1 would show whether the theory is informative or vacuous for the actual deployed algorithm.

- **Near-OOD vs. far-OOD analysis**: The separation assumption in Theorem 4.2 is critical. An experiment varying OOD difficulty (e.g., near-OOD vs. far-OOD datasets) and showing how filtering error rate changes would strengthen the contribution.

- **Sensitivity to InD reference gradient quality**: The method depends on computing ∇̄_in from a model trained on 25,000 InD samples. How does performance change with InD training set size?

## Removed Points

These points are flagged to be removed, treat them with caution.

- **"OE comparison is misleading" (harsh critic)**: The critic notes the comparison to OE is slightly misleading since OE also uses auxiliary data. However, the paper's distinction is valid — OE assumes the auxiliary data is "completely separable" from InD data, which is a stronger assumption than wild data mixing. The paper's characterization is reasonable.

- **"Sub-Gaussian assumption validated only for one dataset" (harsh critic)**: The critic notes Remark 4.3 validates sub-Gaussianity only for one configuration. However, the paper also provides Theorem C.3 in the appendix relaxing this to bounded second moments. This is an appendix point and not a fair criticism of the main text.

- **"Synthetic 2D example is simplistic" (harsh critic)**: While true, this is standard for motivating experiments and the paper includes comprehensive real-dataset experiments.

- **Strength Finder's claim about "NP-hard subset selection"**: The paper says "computationally prohibitive" but never claims NP-hardness. This strength was overstated.

## Novel Insights

The key novel insight is that the element-wise median of gradient representations provides a principled, theoretically motivated mechanism for separating InD and OOD samples in wild data mixtures — specifically, that the median's robustness properties (well-studied in robust statistics) translate to provable guarantees for the OOD filtering problem when the contamination ratio is below 50%. This insight, combined with the practical greedy approximation, offers a clean alternative to the singular-value-based approach of SAL.

## Suggestions

1. **Close or acknowledge the theory-algorithm gap**: Either (a) prove that Algorithm 1's greedy procedure preserves the theoretical guarantees, or (b) explicitly state that the theorems motivate the approach but do not directly certify Algorithm 1, and supplement with stronger empirical validation (e.g., plotting actual error rate vs. theoretical bound).

2. **Rebalance headline claims**: Lead with the WOODS comparison (1.32%/2.60% FPR95 improvement) rather than the KNN+ comparison (40.98%), since the latter conflates the benefit of using wild data with the benefit of median-based filtering.

3. **Add π sensitivity ablation**: Show how performance varies with π ∈ {0.1, 0.3, 0.5, 0.7} to validate the theoretical threshold and test practical robustness.

## Calibration Report

**Anchors retrieved:**

| Round | Anchor ID | Topic | Avg Score | Comparison |
|-------|-----------|-------|-----------|------------|
| 1 | l5ouuojPGe | Thresholding for NN monitoring | 3.00 | Weaker; lacks theoretical contribution |
| 1 | e2F0mJJeN0 | Geometric Median Matching for data pruning | 3.00 | Weaker; related (median-based) but poor experiments, limited novelty |
| 1 | i28ZjVxl81 | OOD in prediction problem | 2.50 | Weaker; shallow analysis |
| 1 | 6Z8rZlKpNT | Normalizing flows for OOD detection | 3.40 | Weaker; narrower contribution |
| 1 | VTYg5ykEGS | ImageNet-OOD benchmark | 6.50 | Similar tier; benchmark contribution vs. method contribution |
| 1 | RxhOEngX8s | Broad OOD detection | 4.25 | Weaker; narrower findings |
| 1 | hlijRgXTDK | Pathologies of OOD detection | 4.75 | Weaker; critique paper without method |
| 1 | Go8hf9wKJx | Diffusion-based outlier generation | 4.25 | Weaker; no theory |
| 1 | cJs4oE4m9Q | Deep orthogonal hypersphere compression | 8.00 | Stronger; more mature theoretical + empirical contribution |
| 1 | TTrzgEZt9s | DRO with bias/variance reduction | 8.00 | Stronger; stronger theory |
| 1 | EUSkm2sVJ6 | Dataset usage inference | 7.60 | Stronger; different domain but tighter contribution |
| 1 | KbetDM33YG | Online GNN evaluation | 8.00 | Stronger; broader impact |
| 2 | jlEjB8MVGa | SAL (Du et al., 2024a) — direct predecessor | 6.50 | Very similar contribution; Medix proposes alternative filtering mechanism |
| 2 | voVjW1PT2c | ProMix — diverse auxiliary OOD | 6.00 | Similar tier; different approach to similar problem |
| 2 | falBlwUsIH | Unlabeled OOD detection impossibility | 6.33 | Similar tier; theoretical impossibility result |
| 2 | ljwoQ3cvQh | DNNs extrapolate predictably | 7.00 | Slightly stronger; cleaner finding |
| 2 | iriEqxFB4y | DOS — diverse outlier sampling | 7.33 | Slightly stronger; more complete empirical story |
| 2 | N6ba2xsmds | Outlier synthesis via HMC | 6.75 | Similar tier |
| 2 | mUXdysoxEP | Feature separation via neural collapse | 6.75 | Similar tier |

**Round-1 bracket**: 5.5–7.5 (clearly above weak anchors at 3.0–4.5, comparable to middle anchors at 6.0–7.0, below strong anchors at 7.5+).

**Round-2 narrowing**: The most informative anchor is jlEjB8MVGa (SAL, Du et al., 2024a) at 6.50, which is the direct predecessor and closest comparison. Medix proposes an alternative filtering mechanism (EWM vs. top singular vector) with comparable empirical performance and arguably cleaner theoretical framing, but has a theory-algorithm gap and inflated headline claims that SAL did not have to the same degree. Medix is at a similar contribution level to SAL but slightly weaker due to these issues. The voVjW1PT2c anchor (ProMix, 6.00) and falBlwUsIH (6.33) are also comparable.

**Final score reasoning**: Medix is closest to the SAL anchor (6.50) in contribution type and quality, but slightly below it due to (1) the theory-algorithm gap not present in SAL, and (2) more inflated headline claims. Compared to the 6.00 anchors, Medix has stronger empirical results and theoretical backing. I position the score at 6.0, between the ProMix paper (6.00) and SAL (6.50).

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>