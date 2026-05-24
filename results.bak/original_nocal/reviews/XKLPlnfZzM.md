Now I have enough to write the consolidated review. Let me compose it.

## Summary

The paper proposes TDDM (Temporal Deaggregation Diffusion Model), a framework that factorizes trajectory generation into spatial occupancy priors (marginal distributions over geography, denoted as *H*) and temporal dynamics learned by a diffusion model. A similarity-transform canonicalization makes the model location- and orientation-invariant, enabling cross-region generalization. Experiments across three cities (Beijing, Porto, San Francisco) with standardized metrics show strong distributional alignment, and zero-shot transfer to unseen regions and cities is demonstrated.

## Strengths

1. **Spatial-temporal factorization yields large-margin gains in distributional alignment.** Table 1 shows TDDM achieves KL_sym of 0.277 vs. 1.153 for Diffusion-TS and JS of 0.059 vs. 0.198 – roughly 4× improvement on the main distributional metrics averaged over three cities.

2. **Zero-shot generalization is demonstrated across cities.** Table 3 shows that a model trained on Porto generates trajectories for other cities with competitive metrics (KL_sym 0.335, JS 0.071), often outperforming a model trained on only 25% of the target city (KL_sym 0.545). This supports the claim that canonicalization + spatial priors enable transfer.

3. **Standardized multi-city benchmark with consistent protocol.** The paper evaluates across three continents using a harmonized set of six measures (TSTR, KL divergences, Density/Trip/Length errors, Pattern score), providing a reproducible evaluation framework that prior work lacked.

4. **Ablation cleanly isolates the role of spatial priors.** Table 2 shows removing *H* degrades KL_sym from 0.277 to 1.334 (≈5×) and Pattern from 0.917 to 0.833, confirming that the gains come from the conditioning mechanism rather than the diffusion backbone alone.

5. **Visual quality corroborates quantitative results.** Figure 2 shows TDDM produces road-aligned trajectories with clear density holes (matching the real data), while baselines generate off-road artifacts or exhibit mode collapse.

## Weaknesses

### Fatal
None.

### Major

1. **Zero-shot generalization lacks baseline comparisons (Table 3).** The paper reports TDDM's intra-city and city-to-city transfer results but does not compare against any baselines under the same protocol. For intra-city, an unconditional model trained on 25% could be applied (naively) to the remaining 75% to measure how much worse it performs. For city-to-city, unconditional models trained on one city and evaluated on another would provide a natural lower bound. Without these comparisons, it is unclear whether TDDM's generalization numbers are strong in absolute terms or simply reflect that H provides enough spatial information to make even a mediocre generator look reasonable. This is the most significant experimental gap.

2. **KL-based metrics are intentionally aligned with what H encodes, making the large margins partly expected.** The spatial prior *H* is a discretized marginal occupancy distribution, and KL(R∥S), KL(S∥R), JS, Density error, and Trip error all measure alignment of the *spatial marginal* — exactly the quantity the model is conditioned to match. The ablation (Table 2) confirms this: removing *H* collapses KL_sym from 0.277 to 1.334 (worse than Diffusion-TS at 1.153). The paper should more explicitly acknowledge that the headline KL improvements are a direct consequence of the conditioning design, and that the more independent evidence of temporal quality comes from TSTR, Pattern, and Length error — where TDDM's advantages are smaller (e.g., Pattern 0.917 vs. 0.907, TSTR 0.011 vs. 0.013). This does not invalidate the method (the method *is* the conditioning), but the current framing risks overstating the significance of the KL-margin relative to the baselines' temporal dynamics.

### Minor

1. **No error bars on most metrics.** Table 1 reports standard deviations only for TSTR; KL, JS, Density, Trip, Length, and Pattern are reported as single values from one run per dataset. Without multiple seeds, the statistical significance of the reported improvements cannot be assessed.

2. **DiffTraj adaptation for unconditional generation is not explained.** DiffTraj (Zhu et al., 2023) is originally a conditional model conditioned on start/end points. The paper treats it as an unconditional baseline but does not describe any architectural or procedural adaptation. If DiffTraj was used unconditionally without its intended conditioning, it may perform artificially poorly.

3. **Coordinate normalization discrepancy.** The method description (Section 3, Canonicalization) states normalization to *[-1, 1]^D*, but Algorithm 1 line 6 and Algorithm 2 line 11 use *[0, 1]^D*. This must be resolved for reproducibility.

### Trivial
None.

## Nice-to-Haves

- Conditioning a baseline (e.g., Diffusion-TS) on the same spatial prior *H* would provide the most direct test of whether TDDM's deaggregation architecture adds value beyond simply injecting *H* as a condition.
- Reporting sensitivity to grid resolution (32×32, 128×128) would justify the 64×64 choice.
- Concrete trajectory visualizations from the zero-shot settings would help assess whether generated trajectories preserve road-following behavior.

## Removed Points

- **"Unfair baseline comparison (TDDM gets H, baselines don't)"** — Removed. This is the paper's core contribution: showing that conditioning on *H* improves quality. Comparing a conditioned method to unconditioned baselines is standard experimental practice. The paper is transparent via the ablation (Table 2) about what happens without *H*. The critic's framing of this as "unfair" is not valid; the comparison favors neither side asymmetrically in a deceptive way.
- **"H computed from training data raises overfitting concerns"** — Removed. Computing aggregate statistics (marginals) from the training set is standard practice for any generative model. This is not a structural concern.
- **"Zero-shot uses target H, not truly zero-shot"** — Weakened and subsumed into Major weakness #1. The paper defines "zero-shot" as "no gradient updates or fine-tuning on target trajectories" (line 224), which is a reasonable usage. The real gap is the lack of baselines, not the definition.
- **"Missing related works"** — Removed per policy (cannot verify without external knowledge).
- **"Length/Pattern definitions not explained"** — Removed. The paper references DiffTraj and states (line 292) "See Appendix E for details on all six measures"; the appendix is stripped by the parser.

## Novel Insights

The most interesting finding to emerge from the review process is the asymmetry in the ablation results: TDDM's architecture without *H* is *worse* than Diffusion-TS on several metrics (KL_sym 1.334 vs. 1.153, Density 0.067 vs. 0.029, Pattern 0.833 vs. 0.907), yet with *H* it substantially surpasses all baselines. This cleanly decomposes the contribution: the diffusion backbone is not particularly strong on its own; the gains come from the conditioning framework. This is not a weakness — it precisely validates the paper's core claim that the factorization, not the denoiser, drives performance. However, it means the method is only useful when spatial priors are available, and the paper could be more explicit about this dependency.

## Suggestions

1. **Add baseline comparisons for the zero-shot experiments.** At minimum, evaluate unconditional models (Diffusion-TS, DiffTraj) trained on 25% of a city and applied to the remaining 75%, and train them on one city and evaluate on another. Even if baselines perform poorly, documenting the gap would strengthen the paper's claims.

2. **Report error bars (≥3 seeds) for all metrics in Table 1.** This is the most actionable improvement for establishing statistical reliability.

3. **Clarify the DiffTraj adaptation.** Describe how DiffTraj was used in the unconditional setting, or note that its original conditioning was removed/dropped.

4. **Harmonize the coordinate normalization** between the method description ([-1,1]^D) and the algorithms ([0,1]^D), and explain which is correct.

5. **Discuss the dependency on H more explicitly.** The paper should state plainly that the large KL improvements are a direct consequence of conditioning on H, and that the more important evidence for temporal quality is in TSTR, Pattern, and Length metrics, where the margins are smaller but still positive.

## Score and Decision

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>