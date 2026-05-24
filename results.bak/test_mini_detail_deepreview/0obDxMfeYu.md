Now I have the full picture. Let me synthesize the final review.

## Summary
2-3 sentence summary of the paper's contribution.

This paper introduces Medix, a median-centric framework that uses element-wise median (EWM) of gradients to filter outliers from unlabeled wild data for OOD detection. The approach is motivated by the observation that adding OOD samples monotonically increases the L2 deviation between the InD mean gradient and the EWM of wild gradients, and a greedy algorithm iteratively removes samples causing the largest drop in this deviation. The paper provides provable error bounds on the filtering stage (Theorems 4.1, 4.2) and demonstrates state-of-the-art performance across 11 InD-OOD pairs against 20 baselines, with average FPR95 of 0.80% on CIFAR-10 and 5.42% on CIFAR-100.

## Strengths
- **Provable two-sided error bounds for median-based filtering**: Theorems 4.1 and 4.2 bound both the inlier misclassification rate (ERR_in) and the outlier misclassification rate (ERR_out) of the EWM filtering rule in terms of contamination, concentration, and separation effects. This is a genuinely novel theoretical contribution that goes beyond the existing literature on wild-data OOD detection. The bounds are clean and interpretable: contamination remains controlled as long as π < 0.5, and the paper also provides a looser version (Theorem C.3) under only bounded second moments, showing the analysis does not rest entirely on the sub-Gaussian assumption.

- **State-of-the-art empirical performance**: Tables 1 and 2 show Medix achieving the best average FPR95 (0.80% on CIFAR-10, 5.42% on CIFAR-100) and AUROC (99.74%, 98.96%) among 20 baselines across 11 InD-OOD pairs. The improvements are substantial — e.g., FPR95 of 2.98% vs. WOODS's 10.19% on CIFAR-10/PLACES365, and 15.99% vs. WOODS's 21.87% on CIFAR-100/PLACES365. Performance is reported with standard deviations over 5 runs.

- **Relaxation of batch-level mixing assumption**: The paper explicitly notes that prior wild-data methods (WOODS, Du et al. 2024a) assume batch-level structure where each batch has a fixed InD/OOD ratio, while Medix operates at dataset-level mixing — a more realistic setting for outsourced wild data where no such structure exists (Section 6). This is a genuine practical advancement.

- **Extensive and fair baseline comparison**: The evaluation covers 20 baselines spanning both InD-only methods (MSP, ODIN, Mahalanobis, Energy, KNN, ReAct, DICE, ASH, CSI, KNN+) and wild-data methods (OE, Energy w/OE, WOODS, CONJ, DRL), all under the same experimental protocol. This thoroughness strengthens confidence in the reported gains.

## Weaknesses

### Fatal
None.

### Major

- **Computational complexity of the greedy filtering algorithm is unresolved in the main paper**. Algorithm 1 is a greedy leave-one-out procedure: at each iteration, for every remaining sample i ∈ S, the EWM of S\{i} must be recomputed to obtain δ_i. For 25,000 samples and a gradient dimension d (penultimate layer of WideResNet-40-2), this yields a per-iteration cost of Θ(|S|²d) — approximately 6.25×10^8 × d operations per iteration — and the algorithm may run for multiple iterations. While the paper defers efficiency analysis to Appendix A.6 (removed in this extract), the main text provides no complexity analysis, runtime numbers on the reported A100 hardware, or discussion of approximations (e.g., incremental median updates or stochastic subsampling). This raises practical viability concerns for scaling beyond the current 25k-sample wild set. The paper acknowledges that the exact optimization (Eq. 4) is "computationally prohibitive" but does not establish that its greedy approximation is tractable at meaningful scale.

- **The main evaluation equates wild OOD source and test OOD source, limiting support for "open-world" claims**. The protocol in Section 5.1 constructs wild data by combining InD CIFAR with the same OOD dataset used at test time (e.g., wild = CIFAR + PLACES365, test = PLACES365). While this is the standard protocol in this sub-field (used by Katz-Samuels et al. 2022a and all wild-data baselines), the paper's abstract and introduction claim Medix is superior "across the board in open-world settings," which implies robustness to novel OOD distributions. The paper does have an unseen-OOD experiment in Appendix A.4 (P_out^test ≠ P_out), but the main text's headline claims and Tables 1-2 are entirely built on same-source evaluation. The mismatch between the claimed scope and what is primarily demonstrated should be addressed by moving the unseen-OOD experiment to the main text or qualifying the claims.

- **Hyperparameter selection may leak test information**. The paper states hyperparameters ϵ and k are selected from sets with "the objective of maximizing OOD performance" (Section 5.2) without specifying a held-out validation set. Since k is selected from {4k, 7k, 10k, 20k} — values that are significant fractions of the total dataset — and the selection criterion is OOD performance on the test OOD datasets, this risks overfitting to the specific test distributions. The paper should report results with a proper validation split.

### Minor

- **The theoretical bounds address only the filtering stage, not the final OOD detector**. Theorems 4.1 and 4.2 bound ERR_in and ERR_out (misclassification rates of the filtering algorithm), but the paper does not connect these to the reported FPR95/AUROC metrics of the downstream OOD detector. A low filtering error does not automatically translate to good OOD detection — the binary classifier (borrowed from Du et al. 2024a) could amplify or attenuate filtering mistakes. While bounding the sub-component is standard and valuable, an empirical correlation analysis (e.g., ERR_in vs. final FPR95 across settings) would bridge this gap.

- **The synthetic 2D Gaussian example (Figure 2) is too simple to provide meaningful insight**. InD and OOD clusters are separated by a Euclidean distance >20 units in 2D space (InD means within [-2,2] range, OOD mean at [20, 2√3]), making the problem trivial. Replacing this with a real-data visualization (e.g., t-SNE of penultimate-layer features showing which wild points are flagged as outliers) would be far more informative about how Medix behaves with neural network gradients.

- **No ablation on the contamination proportion π**. The theoretical bounds require π < 0.5, and the experiments use π = 0.5 exclusively. Given Theorem 4.1's dependence on π via the contamination term π/[2(1-π)], it would be informative to see results for π ∈ {0.1, 0.3, 0.5} and perhaps π = 0.6 (where the bound no longer holds but the method might still work).

- **The greedy algorithm design is heuristic**. The choice to remove the top-k samples with largest δ_i each iteration is a reasonable greedy approximation, but k must be pre-specified and the convergence criterion (|δ_max| < ϵ) is sensitive to the scale of gradient norms. The paper provides no guidance on how to set these hyperparameters in a new domain beyond the specific evaluated values.

### Trivial
None.

## Nice-to-Haves
- An empirical analysis connecting ERR_in/ERR_out to final FPR95/AUROC across varying π and OOD sources would strengthen the theoretical-empirical bridge.
- Analysis of pseudo-label quality effects (claimed in Appendix A.5) should be summarized in the main text, as it addresses a structural concern about the method's reliance on predicted labels for OOD samples.
- Reporting the runtime of Algorithm 1 on the reported hardware (NVIDIA A100) would alleviate computational complexity concerns, even without formal analysis.

## Removed Points
These points are flagged to be removed, treat them with caution:

1. **"The theoretical guarantees do not connect to the final OOD detection metrics, and the bounds rely on strong unverified assumptions" (from Harsh Critic, Issue 3, partly)** — The strong version of this criticism that asserts "the paper's theoretical contribution's practical relevance is unclear" is weakened. The theorems clearly bound what they claim to bound (filtering-stage misclassification rates), and the sub-Gaussian assumption is standard for concentration bounds. The paper provides empirical support (Figure 4) and a looser bounded-second-moment version. What remains is retained as a minor weakness above. The claim that the bounds are "unverified" is removed because: (a) Figure 2 shows 12.5% extraction error which aligns with theory; (b) theoretical assumptions are explicitly stated and partially validated.

2. **"The method depends on predicted labels for wild samples, but the effect of pseudo-label noise is not analyzed" (Harsh Critic, Issue 4)** — Partially removed. The paper explicitly states in Section 5.2 (Additional studies) that Appendix A.5 evaluates pseudo-label quality and shows resilience to noisy labels. However, this analysis is deferred to the appendix, so the main paper could benefit from a summary. What remains: the theoretical analysis assuming fixed gradient distributions does not model pseudo-label bias — kept as a minor point. But the claim of "no evidence" is removed since the paper does state the appendix addresses it.

3. **"The filtering algorithm is computationally prohibitive as described" (Harsh Critic, Issue 2, full version)** — Retained as a Major weakness above. The removed part: the claim that the method "as presented is not reproducible in practice" is an overstatement — the experiments were run successfully on A100s, so the method IS reproducible at the demonstrated scale. The concern is about scaling, not current reproducibility.

4. **"The separation condition in Theorem 4.2 is strong; paper does not provide empirical evidence that this condition holds"** — Removed. This is a standard type of assumption in theoretical analysis. The paper is transparent about it and the exponential separation term is a typical trade-off. Empirical verification of the condition for every dataset pair is not expected.

5. **"Ablation on the choice of k is claimed in Appendix A.2, but a main-figure sensitivity analysis would strengthen"** — This is a nice-to-have request, retained as such.

6. **Strength Finder strengths that are generic** — Dropped: None of the strength finder's strengths are generic — they are all specific and evidence-backed. All retained.

## Novel Insights
None beyond the paper's own contributions.

## Suggestions
- Move the unseen-OOD experiment (Appendix A.4) to the main text as a secondary table, and qualify the abstract/conclusion to distinguish between same-source and cross-source performance claims.
- Provide an explicit computational complexity analysis of Algorithm 1 in the main paper (Big-O per iteration, total wall-clock time for the reported runs) and discuss possible approximations (e.g., stochastic sampling of candidates for EVM recomputation, or a single-pass filtering strategy).
- Add an ablation with a held-out validation set for hyperparameter selection to rule out test leakage concerns.
- Include a small summary table or paragraph on the pseudo-label robustness analysis from Appendix A.5 in the main paper, as it addresses a structural concern.

## Score and Decision

**Calibration anchors:**

| Path | Avg Score | Round | Comparison |
|------|-----------|-------|------------|
| jlEjB8MVGa.md (SAL — Du et al. 2024a) | 6.50 | R1 | Most directly comparable paper: same problem (wild OOD detection), same two-stage paradigm, similar theoretical+empirical contributions. SAL uses top singular vector for filtering; Medix uses EWM of gradients. Medix achieves stronger empirical results and operates under dataset-level (vs. batch-level) mixing, but its filtering algorithm has higher computational cost. Comparable quality; Medix slightly below. |
| kwCHcaeHrf.md (SPADE) | 5.50 | R1 | OOD detection with provable guarantees but weaker experimental results (often outperformed by baselines). Medix has much stronger empirical validation. Medix is clearly superior to this anchor. |
| uWUovmBRUq.md (Semantic or Covariate) | 4.00 | R1 | Purely theoretical OOD detection taxonomy paper with limited experiments (one real dataset). Medix has far broader empirical evaluation and a concrete algorithmic contribution. Medix is clearly superior. |
| bcWwhF8cTZ.md (Gradient norm proxy) | 5.50 | R2 | Uses gradients for OOD but for error estimation, not outlier filtering. Novelty concerns (similar to prior GradNorm). Medix has a more novel approach and stronger results. |
| voVjW1PT2c.md (ProMix) | 6.00 | R2 | Mixup-based OOD detection with theory. Innovativeness questioned (mixup not new for OOD). Medix has a more novel algorithmic contribution (median-based filtering) but some reviewers might similarly question the heuristic aspects. Similar tier. |
| nUBLhhVM1l.md (Tight Rates) | 6.33 | R2 | Pure theory paper on outlier transfer learning, no experiments. Medix has both theory and extensive experiments. Different nature but Medix is more complete. |

**Round 1 bracket**: 5.0–7.0 (clearly stronger than the ~3.0 weak anchors, comparable to the mid-range anchors around 5.5–6.5, clearly weaker than the 8.0 top-range anchors).

**Round 2 narrowing**: The paper sits between the ProMix (6.00) and SAL (6.50) anchors. It has a more novel algorithmic contribution than ProMix (which reviewers flagged as incremental) but has less clean experimental validation than SAL's (unseen OOD is deferred to appendix, computational complexity is unresolved). The empirical results are stronger than both, which is a significant plus.

**Final score**: 6.0 — a solid paper with a clear novel contribution (median-centric filtering for wild data), strong empirical results, and meaningful theoretical analysis. The main concerns are the unresolved computational complexity, the same-source OOD evaluation mismatch with the "open-world" framing, and the lack of proper validation-set separation for hyperparameter selection. These are addressable in a revision.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>