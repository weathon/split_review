Now I have all the information I need. Let me compose the final consolidated review.

---

## Summary

This paper proposes AutoScale, a two-phase pipeline that bridges multi-task optimization (MTO) algorithms and linear scalarization. It first shows empirically (on CityScapes) that high-performing linear scalarization weight sets systematically correlate with certain MTO metrics (high gradient magnitude similarity, low condition number, balanced loss scale). Leveraging this insight, AutoScale runs an MTO (e.g., IMTL-G) for a short exploration phase (α=0.2 of iterations), collects gradient/loss information to optimize scalarization weights—specifically by minimizing a cost function that encourages equal gradient magnitude across tasks—then switches to fixed-weight linear scalarization for the remaining training. Results across CityScapes, NYUv2, and Nuscenes show AutoScale consistently outperforms prior MTOs and approaches grid-searched weight performance while reducing training time by over 45% relative to gradient-manipulating MTOs.

## Strengths

- **Novel insight connecting MTO metrics to linear scalarization quality.** Section 3.2 and Figures 2–3 empirically demonstrate across 19 weight sets on CityScapes that good scalarization weights systematically correlate with high gradient magnitude similarity, low condition number, and low variance in relative loss scale. This is a genuinely useful observation that bridges two previously opposed strands of MTL research. The paper appropriately qualifies the claim as "for the first time according to our knowledge" (line 20).

- **AutoScale consistently outperforms prior MTOs and approaches oracle grid-search performance.** Tables 1 and 2 show AutoScale ranks second only to the expensive grid-searched upper bound on Nuscenes and achieves best or near-best results among all MTOs on CityScapes and NYUv2. This is demonstrated across three diverse benchmarks including a large-scale autonomous driving dataset, which strengthens generalizability.

- **Systematic ablation study validates key design choices.** Section 5.1 ablate the exploration ratio α (Figure 6), MTO selection (Table 3), cost function F(w) (Table 4), and weight predictor f({w}) (Table 5). The results show IMTL-G and FAMO are robust exploration-phase MTOs, equal-gradient-magnitude cost function works best across datasets, and linear extrapolation is the most consistent weight predictor. This level of empirical grounding adds credibility to the pipeline design.

- **Clear efficiency advantage.** Figure 5 quantifies that AutoScale (with α=0.2) adds minimal per-iteration overhead over plain linear scalarization while gradient-manipulating MTOs (GradNorm, MGDA, PCGrad, IMTL-G, Aligned-MTL) require roughly 3× the training time.

## Weaknesses

### Fatal

None.

### Major

None.

### Minor

- **Weight optimization procedure is underspecified.** The paper defines the optimization `w* = argmin_w E[F(w|{G},{L})], s.t. sum w_i = K` (Eq. 1) and tests three cost functions (Table 4), but never specifies the algorithm used to solve this inner optimization. Is there a closed-form solution (e.g., for equal gradient magnitude, solving w_i·||g_i|| = constant yields w_i = K·(1/||g_i||)/Σ_j(1/||g_j||))? Is it solved by gradient descent on w at each window? What is the computational cost of this inner step? The paper also does not specify whether the gradients and losses used as input are from a single batch, averaged over multiple batches, or aggregated across a window. This is a genuine reproducibility gap in the core method description (lines 113–120, 220).

- **Missing comparison to efficient weight-search methods.** The paper motivates AutoScale as addressing "the problem of costly search" for linear scalarization weights (line 62) and mentions Royer et al. (2024) as proposing "more efficient search methods." Yet the only search baseline evaluated is a full grid search over 20 trials—the most expensive approach. Without comparison to any efficient search baseline (e.g., Bayesian optimization over weight space, continuous search from Royer et al., or random search with early stopping), the paper's central efficiency claim is incompletely supported. AutoScale may well be competitive, but the evidence is not provided.

- **Correlation study lacks statistical rigor.** The "clear correlation" claim in Section 3.2 (Figures 2–3) is supported only by visual inspection of 19 weight sets on a single dataset (CityScapes). No correlation coefficients (Pearson's r, Spearman's ρ), significance tests, or confidence intervals are reported. The weight sets were chosen to span good/medium/bad performance, which can inflate perceived trends. The paper later relies on these correlations to motivate the entire AutoScale pipeline, so the evidence here should be stronger. Showing similar correlations on at least one more dataset (e.g., NYUv2) and reporting quantitative correlation measures would substantially strengthen the motivation.

- **No standard deviations reported in main results.** Tables 1 and 2 state results are "average of 3 random trials" for most methods, but no variance indicators (standard deviations, confidence intervals) are reported. This makes it impossible to assess whether the observed performance differences between methods are meaningful, particularly when methods are close (e.g., AutoScale vs. FAMO on CityScapes and NYUv2 in Table 2).

- **Efficiency analysis reports per-iteration time but not total wall-clock cost.** Figure 5 compares per-iteration training time, but does not report total training time including the exploration phase. Since the exploration phase uses a gradient-manipulating MTO (3× per-iteration cost), the total cost should also be reported to give a complete picture. The α=0.2 setting means 20% of iterations run at 3× cost and 80% at 1× cost, yielding approximately 1.4× overall — this is still favorable but should be explicitly stated.

- **Why IMTL-G is the preferred exploration MTO is not explained.** Table 3 shows IMTL-G and FAMO perform best as the exploration-phase MTO, but the paper provides no analysis of *why* these succeed while PCGrad and unitary scalarization underperform. This matters because the method's generality depends on finding a good exploration MTO; if the choice is unpredictable, users may need to try several MTOs before obtaining good results with AutoScale.

### Trivial

- **The constraint `sum w_i = K` is used without justification.** Standard practice is to normalize weights to sum to 1. The choice `sum w_i = K` (making the average weight 1) is not explained and may interact with learning rate scaling. A brief justification (even in a footnote) would help readers.

- **The ablation on cost function (Table 4) is limited to three options on three datasets.** The claim that equal gradient magnitude is "robust" would benefit from a larger ablation (more cost functions, more datasets), though the existing evidence is reasonable.

## Nice-to-Haves

- A limitations section discussing when the correlation hypothesis may break down, how sensitive the method is to the choice of exploration MTO, and potential failure modes.
- Analysis of failure cases: on which weight sets or datasets does AutoScale perform poorly compared to the MTO baseline?
- An experiment isolating the benefit of the two-phase approach: compare AutoScale to (a) running the exploration MTO for the full T iterations, and (b) running linear scalarization from scratch with the *same* predicted weights but no MTO exploration phase.
- Reporting standard deviations or error bars for all main results.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **"First time" claim overreach:** The paper uses "for the first time according to our knowledge" (line 20), which is appropriately qualified. Removed because it is not a genuine weakness.
- **Related work too long / Section 3.1 could be shortened:** Style preferences, not substantive criticisms. Removed.
- **Searched weights treated as competitor:** The paper does not claim to outperform searched weights; it presents them as an oracle upper bound ("trailing only the searched weights," line 239). The comparison is standard in MTL papers. Removed.
- **"State-of-the-art" claim overreach:** The paper's conclusion says "trailing only the searched weights," which accurately qualifies the SOTA claim. Removed.
- **Open-source code not provided:** The paper promises code upon publication (line 24), which is standard. Per hard rules, removed.
- **Specific criticisms about Roc searching / formatting nits:** Removed as style issues or parser artifacts.

## Novel Insights

A genuinely novel observation that emerges from the interaction between the correlation study and the ablations is that the equal-gradient-magnitude cost function (which encourages task gradients scaled by weights to have equal norms) implicitly optimizes for multiple favorable MTO properties simultaneously—low condition number, balanced convergence, and balanced loss scale—as noted in line 224: "AutoScale exhibits favorable trends across different metrics, including a low condition number, balanced convergence speed, balanced loss scale, and equal angles to the final aggregated gradient, even when using the default cost function of equal gradient magnitude." This suggests the MTO metrics are not independent, and a single well-chosen cost function may suffice to capture multiple optimization desiderata. None beyond the paper's own contributions.

## Suggestions

1. **Specify the weight optimization algorithm precisely.** Provide the closed-form solution for the equal-gradient-magnitude cost function or describe the iterative procedure, its convergence properties, and its computational cost. Also specify how gradients/losses are aggregated per window (single batch vs. multi-batch average).
2. **Add comparison to at least one efficient weight-search baseline** (e.g., random search with few trials, Bayesian optimization, or the continuous search method of Royer et al. 2024). This directly addresses the paper's efficiency motivation.
3. **Strengthen the correlation evidence.** Report Pearson/Spearman correlation coefficients and p-values for Figure 3. Show at least one additional dataset to demonstrate the relationship is not CityScapes-specific.
4. **Report standard deviations** for the main results in Tables 1 and 2.
5. **Report total wall-clock training time** (not just per-iteration time) for AutoScale variants and baselines.
6. **Justify the sum w_i = K constraint** and discuss any implications for learning rate scaling.

## Score and Decision

The paper tackles a timely question and makes a genuine contribution by demonstrating that MTO metrics can guide linear scalarization weight selection, with solid experimental evidence that AutoScale consistently outperforms prior MTOs. The main weaknesses—an underspecified optimization step, missing comparison to efficient search baselines, and lack of statistical rigor in the correlation analysis—are addressable and do not invalidate the core contribution. I recommend acceptance with minor revisions.

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>