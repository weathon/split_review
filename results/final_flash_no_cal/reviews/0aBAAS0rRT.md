## Summary

This paper proposes SigMap, a wireless localization foundation model with two main innovations: (1) a cycle-adaptive masking strategy for self-supervised pre-training that dynamically adjusts mask patterns based on detected CSI periodicity, and (2) a "map-as-prompt" framework that encodes 3D building geometry via a GNN into soft prompt tokens for parameter-efficient fine-tuning. Experiments on simulated ray-tracing data (DeepMIMO, WAIR-D) show strong improvements over four baselines in single-BS and multi-BS localization, requiring fine-tuning of only 0.7% of parameters on ~100 target samples per new environment.

## Strengths

- **Geographic prompt tuning yields large, consistent gains across all tasks.** The map-driven prompt improves MAE by 31% in single-BS (1.564 m vs. 2.275 m, Table 1) and 14.7% in multi-BS (0.673 m vs. 0.789 m, Table 2), with even a 2‑D bird's-eye view retaining most of the benefit (Table 4). The ablation cleanly isolates the contribution of the map information.

- **Strong empirical results against competitive baselines on simulated data.** SIGMAP (with map) outperforms the best baseline (LWLM) by 34.4% in single-BS MAE and 18.7% in multi-BS MAE. The gains are consistent across eight metrics in the radar chart (Figure 5). Generalization to unseen scenarios (DeepMIMO O2, WAIR-D Scenario-2) shows 44–53% MAE improvements over LWLM with only ~100 labeled samples.

- **Extreme parameter efficiency during fine-tuning.** Only 0.085 M parameters (0.7% of total) are updated, with the full 1000-epoch fine-tuning completing in 30 minutes (Table 5). This makes the approach practically appealing for deployment in new environments.

- **The map-as-prompt idea is conceptually clean and well-motivated.** Using Delaunay triangulation over building vertices and BS positions to construct a spatial graph, then encoding it via a shallow GCN into soft prompt tokens, is a natural way to inject geometric constraints into a pre-trained model without modifying its backbone.

## Weaknesses

### Major

- **Zero-shot vs. few-shot contradiction in the framing.** The abstract and contribution list claim "strong zero-shot generalization in unseen environments," but Section 4.5 explicitly fine-tunes task heads on ~100 labeled samples per target scenario and calls it a "few-shot learning setup." This is a direct misrepresentation of the evaluation protocol. The core technical contributions do not depend on zero-shot capability, but the abstract overreaches and does a disservice to what is actually demonstrated (few-shot adaptation with a frozen backbone). The claims must be corrected.

- **The cycle-adaptive masking mechanism is underspecified to the point of irreproducibility.** Equation (6) defines a mask pattern parameterized by a periodicity shift \(d_{\text{final}}\), but the paper never explains how \(d_{\text{final}}\) is derived from cross-correlation analysis. The phrases "compute shift patterns using cross-correlation analysis" and "detect dominant periodicities" are not accompanied by any algorithm, pseudocode, or formal description of the detection process. Since cycle-adaptive masking is one of the two core claimed contributions, the lack of detail prevents anyone from implementing, evaluating, or building upon this component. This is a significant methodological gap.

### Minor

- **The evidence for cycle-adaptive masking is mixed.** In Table 3, adaptive masking achieves the best MAE (0.673 m) and CDF@1 m (84.5%) but the *worst* RMSE (1.099 m) among the three masking strategies — strip-masking has RMSE 0.972 m. The paper asserts "the best trade-off" without statistical testing or explanation of the worse tail behavior. For localization, large-error events are critical, so this anomaly weakens the claim that adaptive masking is uniformly beneficial.

- **No real-world experimental validation.** All experiments are on simulated ray-tracing data (DeepMIMO, WAIR-D). The paper claims relevance for autonomous driving, XR, and smart manufacturing, but provides no evaluation on measured CSI from live networks. The sim-to-real gap in wireless localization is known to be substantial (hardware impairments, synchronization errors, environmental dynamics). This limits the support for the paper's broader practical claims. (The paper does not need real-world data to be a valid contribution, but the gap should be acknowledged and discussed as a limitation.)

- **Baseline set is narrow and lacks map-aware competitors.** The paper compares against only four methods (OMP, CNN, SWiT, LWLM), none of which integrate geometric map information. The map-as-prompt contribution would be better contextualized by comparison against other techniques that fuse geometry (e.g., ray-tracing-constrained methods, map-aided fingerprinting). The existing ablation (SIGMAP w/ map vs. w/o map) partially addresses this, but the field-standard baselines are missing.

- **Standard deviations / significance information is missing.** The paper states results "averaged over 5 independent runs" (Section 4.1) but reports no variance, confidence intervals, or significance tests. The magnitude of the reported improvements cannot be assessed for statistical reliability.

- **Two presentation issues.** (a) The radar chart (Figure 5) includes an undefined metric "oss_scenario" and the axes are unlabeled in the extracted description; the computation of these metrics is not specified. (b) Section 4.4 refers to "Figure 1" for a side-by-side map ablation, but Figure 1 (page 2) shows wireless propagation paths, not an ablation comparison — this is a clear referencing error.

### Trivial

- The conclusion does not discuss limitations. Adding a brief discussion of the sim-to-real gap, the reliance on a single simulated pre-training dataset, and conditions where adaptive masking may hurt RMSE would strengthen the paper.

## Nice-to-Haves

- Provide a full pseudocode or algorithmic description of the periodicity detection and mask generation pipeline to make the cycle-adaptive masking contribution reproducible.
- Report variance (e.g., standard deviations or interquartile ranges) for all main tables, especially given the claim of 5 independent runs.
- Add at least one map-aware baseline to the comparison set.

## Removed Points

*These points are flagged to be removed; treat them with caution.*

- **Missing appendix details (dataset splits, BS configurations, pre-training hyperparameters).** The critic noted these are cited to the Appendix, which was stripped by the parser. Per evaluation conventions, missing appendix content should not be counted against the paper.

- **"LWLM likely does not use geometric information, so the comparison conflates the benefit of map input with the proposed architecture."** This is speculation about a baseline's internal design. The paper's own ablation (w/ map vs. w/o map) already isolates the map contribution, so the comparison is not conflated.

- **"The 1000-epoch fine-tuning seems excessive for 'parameter-efficient' adaptation."** Only 0.085 M parameters are updated regardless of epoch count, and the total time is 30 minutes. The epoch count does not undermine the parameter-efficiency claim.

- **"The paper should confirm that the 2-D map experiment uses the same procedure."** The paper explicitly states: "Except for height, the 2-D variant follows the same pipeline as the 3-D version." The concern is addressed.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. **Fix the zero-shot overclaim.** Replace "zero-shot" with "few-shot" or "cross-scenario" in the abstract and introduction, and clearly state the fine-tuning budget (~100 samples) alongside generalization claims.

2. **Write out the periodicity-detection algorithm.** Provide a short pseudocode showing how \(d_{\text{final}}\) is computed from the CSI cross-correlation, how the mask pattern in Eq. (6) is applied per sample, and how it interacts with the reconstruction loss. Without this, the main methodological novelty is not reproducible.

3. **Address the RMSE anomaly for adaptive masking.** Either explain why the worse RMSE is acceptable (e.g., via a per-sample error distribution analysis) or provide a modified masking design that improves both MAE and RMSE.

4. **Add a limitations paragraph** to the conclusion, honestly discussing the sim-to-real gap, the scope of the baselines, and conditions where the approach may underperform.

5. **Expand the baseline set** with at least one map-aware or geometry-integration method to better contextualize the map-as-prompt contribution.

## Score and Decision

**MY FINAL SCORE:** <score>6.0</score>  
**MY FINAL DECISION:** <decision>Reject</decision>