- Decision: Reject
- Avg Score: 5.00
- Scores: 5, 5, 5, 5
Now I have all the information needed. Let me write the comprehensive consolidated review.

## Summary

The paper proposes Wavelet Optimal Transport (WOT), a method that combines spectral graph wavelets with optimal transport for unpaired dataset alignment, targeting single-cell multi-omics integration. WOT decomposes each dataset's structure across multiple wavelet scales and incorporates filters (entropy-based E-WOT and learned L-WOT) to down-weight noisy or uninformative scales. Experiments on toy bifurcation data, 3D shape correspondence (SHREC20), and two real single-cell benchmarks (scGEM, SNARE-seq) show WOT outperforming prior methods. The core idea—multi-resolution wavelet discrepancies as the intra-domain cost in GW-OT—is genuinely novel and well-motivated by the noise and non-isometry challenges of single-cell data.

## Strengths

1. **Principled and novel framework.** WOT generalizes Gromov-Wasserstein OT by replacing a single geodesic-RBF kernel with a multi-scale spectral graph wavelet representation. Remark 1 formalizes this connection: WOT reduces to standard geodesic-RBF GW-OT in the single-scale heat-kernel limit, situating the new method within existing theory rather than presenting it as an unrelated heuristic. The two filter strategies (E-WOT, L-WOT) are cleanly motivated.

2. **Demonstrated robustness to noise and dropout on controlled toy data.** Section 4.1 / Figure 3 compares vanilla-WOT against GW-OT on a bifurcation-matching task with increasing additive noise and dropout, with ten repetitions per condition. WOT maintains significantly lower FOSCTTM than GW-OT above ~0.065×avg-distance noise and above ~0.2 dropout fraction, while both perform similarly in low-noise regimes. This provides direct evidence that the multi-scale wavelet view itself (before filtering) improves robustness, and the results include error bars (25th/50th/75th percentiles).

3. **Consistent improvements on real single-cell benchmarks.** Table 2 reports label transfer accuracy on scGEM (177 samples) and SNARE-seq (1047 samples). The best WOT variant exceeds the best prior method (SCOTv2) on both datasets: E-WOT (heat kernel) achieves 0.961 vs. 0.826 on SNARE-seq; L-WOT (simple tight) achieves 0.616 vs. 0.509 on scGEM. The improvement is consistent across multiple kernel/filter combinations, all of which match or exceed prior state-of-the-art.

4. **Computationally scalable via Chebyshev approximation.** Section 3.1 notes that Chebyshev polynomial approximation (Hammond et al., 2011) is used to avoid full eigendecomposition of the graph Laplacian, which is important for scaling to single-cell datasets with many cells.

## Weaknesses

### Fatal
None.

### Major

1. **Shape experiment includes baselines that make the comparison uninformative.** Section 4.2 compares WOT against SCOT, SCOTv2, UnionCom, Pamona, MMD-MA, and cross autoencoders on 3D shape correspondence (SHREC20). These methods were designed for high-dimensional single-cell data, not 3D shapes. Their poor performance on this task is unsurprising and does not constitute meaningful evidence of WOT's advantage. To the paper's credit, GW-OT *is* included as a baseline (Figure 4 reports both GW-OT and WOT curves on the same shapes, and Table 1 includes GW-OT alongside the single-cell methods), so the comparison is not entirely hollow. However, the paper's framing and the inclusion of the single-cell baselines inflate the apparent improvement. The central comparison should be WOT vs. GW-OT (and other general-purpose OT variants such as entropic GW, unbalanced GW), which would directly test whether the wavelet machinery adds value over standard OT for non-isometric alignment. As presented, this experiment supports the claim less convincingly than it could.

2. **No measure of variability on the main real-data results.** Table 2 reports label transfer accuracy as single point estimates for both WOT variants and all baselines. With only 177 (scGEM) and 1047 (SNARE-seq) samples, the reported numbers could be sensitive to initialization, hyperparameters, or sample splits. The toy experiments (Figure 3) include error bars from ten repetitions, but this statistical rigor is absent where it matters most—the central real-data claims. Without confidence intervals, replication across random seeds, or cross-validation, the reader cannot assess whether the reported gains (e.g., 0.961 vs. 0.852 on SNARE-seq) are stable or might reverse under different conditions.

3. **Missing ablation isolating the contribution of each component.** The paper introduces three tiers: (a) vanilla GW-OT (single scale), (b) vanilla-WOT (multiple scales, uniform filters), and (c) filtered WOT (E-WOT / L-WOT). Yet vanilla-WOT is only compared against GW-OT on the toy data (Figure 3), never against E-WOT or L-WOT on any dataset. On the real data (Table 2), only E-WOT and L-WOT are reported. This makes it impossible to determine whether the gains come from the multi-scale wavelet representation itself, from the specific filter mechanisms, or from an interaction of both. A simple ablation—vanilla-WOT entries in Table 2—would directly resolve this.

### Minor

4. **Baseline results on real data were not re-run.** The paper states: "We use the results reported by Demetci et al. (2022a) for competing methods" (Table 2 caption). While preprocessing follows Demetci et al. (2022b), it is not explicitly verified that the splits, preprocessing, and evaluation protocol are identical to those used in Demetci et al. (2022a). If there are discrepancies, the comparison may not be perfectly fair. The authors should clarify whether baselines were re-run under identical conditions or acknowledge the caveat.

5. **Several hyperparameters and design choices for the shape experiment are unspecified.** The paper does not state which wavelet kernel (heat, Meyer, or simple tight), which set of scales, or which aggregation function (sum, max, or mean) was used for the SHREC20 experiment. This hinders reproducibility and makes it difficult to assess whether these choices were optimized or fixed. The same information would be valuable for the single-cell experiments as well.

6. **Key optimization parameters for E-WOT and L-WOT are not given defaults.** The KDE bandwidth \(h\) (Section 3.3, Eq. 6) is mentioned as >0 but no default or selection method is provided. The L-WOT constraint parameter \(\delta\) and the Lagrangian multiplier \(\lambda\) (Section 3.4, Eq. 7–8) are introduced but not given default values or described how they are tuned. While the paper notes that most hyperparameters are fixed to default values (line 159), these defaults are not stated.

### Trivial
None.

## Nice-to-Haves

- **Error bars or cross-validation on real single-cell results.** A multi-run evaluation (e.g., 5-fold cell-wise cross-validation, bootstrap resampling, or multiple random seeds) would substantially strengthen the paper's central empirical claims.
- **A systematic ablation** adding vanilla-WOT to Table 2 would cleanly separate the contribution of the multi-scale representation from the contribution of the filters.
- **A cost/run-time comparison** between E-WOT and L-WOT would help practitioners choose between the two implementations.
- **Hyperparameter sensitivity analysis** for the number of scales and the wavelet kernel choice would demonstrate robustness.

## Removed Points

- *Claim that the shape experiment lacks any generic OT baselines.* — The paper does include GW-OT as a baseline (Figure 4, Table 1). This is a general-purpose baseline, so the strongest version of this criticism is inaccurate. The broader concern about inappropriate single-cell baselines is retained as Major weakness #1.
- *Claim that the higher variance of WOT in the additive noise experiment "is flagged but not discussed."* — The paper does discuss it (line 181: "this result could imply that our method may require further hyperparameter tuning"). The reviewer's factual claim is wrong; removed.
- *Claim that filter definitions are too vague.* — The paper describes two specific implementations (E-WOT, L-WOT) in detail. The general description "emphasize salient scales" is high-level framing for the framework, not a missing detail. Removed as strawman.
- *Criticism that Section 2 (Background) underdevelops the connection between wavelets and alignment.* — This is a subjective opinion about expository depth, not a concrete weakness. Removed.
- *Nitpick about the missing discussion of convergence for L-WOT's alternating procedure.* — This is a nice-to-have detail, not a core weakness. Moved to Nice-to-Haves implicitly.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. Re-run the shape experiment with GW-OT variants (entropic GW, unbalanced GW) as the primary baselines, and either move the single-cell method comparisons to the appendix or remove them. This directly addresses the most significant evaluation concern.
2. Add error bars to Table 2 by repeating the alignment with at least 5 different random seeds or initializations.
3. Add "vanilla-WOT" rows to Table 2 (multi-scale with uniform filters, i.e., no filtering) to ablate the filter contribution.
4. State the specific wavelet kernel, scale set, and aggregation function used in each experiment. Provide default values for \(h\), \(\delta\), and \(\lambda\).
5. Clarify whether baseline results were re-run under identical conditions or acknowledge if they were taken from the literature as-is.
