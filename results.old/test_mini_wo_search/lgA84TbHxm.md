Now I have a thorough understanding of the paper and both reviews. Let me produce the final consolidated review.

## Summary

The paper proposes DySTreSS, a cosine-based dynamic temperature scaling function for the InfoNCE loss in self-supervised contrastive learning. Instead of a fixed temperature hyperparameter, the temperature varies as a function of the cosine similarity between sample pairs — high at extreme similarities (±1) and low near the middle. The method is motivated by a gradient-based theoretical analysis that derives slope conditions for the temperature function, and evaluated on vision benchmarks (ImageNet100/1K, CIFAR10/100, long-tailed variants) as well as NLP sentence embedding (SimCSE). The paper reports consistent but modest improvements over the prior temperature-modulating method MACL and larger gains over vanilla SimCLR.

## Strengths

- **Consistent improvements across benchmarks and modalities.** DySTreSS outperforms MACL (the closest prior temperature-modulating method) on ImageNet100 (78.78% vs. 78.28%), ImageNet1K (65.21% vs. 64.3%), CIFAR10 (85.68% vs. 84.85%), and CIFAR100 (56.57% vs. 56.15%) under comparable settings (Tables 1a, 1b, 2a). The same framework generalizes to sentence embedding via SimCSE (Table 8: average STS 76.37 vs. 74.62). This breadth of validation across vision and language strengthens the contribution.

- **Thorough ablation of the temperature design space.** The paper systematically explores temperature range (Table 9: four \[τ_min, τ_max\] settings), shifted temperature profiles (Table 10: five shift/scale combinations), and alternative functional forms (Table 5: cosine vs. linear vs. exponential on CIFAR10/100). This level of empirical analysis on the temperature function design is more extensive than prior works (MACL, Kukleva et al.'s cosine scheduling).

- **Novel inter-class uniformity metric and representation analysis.** The paper introduces an inter-class uniformity metric (Eq. 12) measuring class-centroid separability, and shows DySTreSS achieves lower (better) values than SimCLR, MoCoV2, DCL, and DCLW on CIFAR10/100 and ImageNet1K (Table 11). This provides quantitative evidence about *why* the learned representations improve, beyond just reporting accuracy.

- **Effective on long-tailed distributions.** DySTreSS outperforms Kukleva et al.'s dedicated temperature scheduling on CIFAR10-LT (64.98 vs. 62.91), CIFAR100-LT (31.71 vs. 30.20), and ImageNet100-LT (46.1 vs. 45.3), showing the dynamic scaling principle works better than a pre-defined schedule under class imbalance.

## Weaknesses

### Fatal

None.

### Major

- **Baseline SimCLR temperature is not specified.** The paper never states what fixed temperature τ was used for the vanilla SimCLR baseline in any experiment. Since SimCLR's performance is known to be sensitive to τ (the original paper uses τ=0.5 for ImageNet, τ=0.1 for CIFAR), the reader cannot verify whether the reported gains over SimCLR reflect the dynamic scaling mechanism itself or simply a different effective temperature range. For example, on ImageNet1K the paper reports SimCLR at 63.2% (via the lightly-ai library benchmarks), while the original SimCLR paper reports ~64.3% at 100 epochs with τ=0.5 — a gap that could affect the relative comparison. The comparison against MACL (which also uses temperature scaling) is less affected by this issue, but the SimCLR comparison is the primary anchor throughout the paper.

- **No variance or statistical significance reported.** No error bars, standard deviations, or multiple-seed results are provided for any experiment. Given that the improvements over MACL are modest (~0.5–0.9% on major benchmarks), it is impossible to determine whether these differences are statistically significant. This is especially important because multiple shifted-temperature variants are tested and the best results are reported, raising the possibility of selection bias.

- **Theoretical derivation does not uniquely motivate the cosine function.** The paper solves a first-order ODE (Eqs. 13–23) to obtain τ_ij = s_ij / log(δ·K·s_ij − c), then discards this solution and "adopts" a cosine function (Algorithm 1) because it satisfies the same slope properties (positive slope for s>0, negative for s<0). The connection between the ODE and the chosen function is loose: (a) the ODE derivation relies on approximations (treating K as constant w.r.t. s_ij, assuming N→∞ to drop a term) that are not justified for practical batch sizes; (b) the ODE solution is not a cosine; (c) the slope property used to justify the cosine is satisfied by many other functions (including linear and exponential, which the paper's own ablation in Table 5 shows perform similarly). The paper presents the theoretical analysis as supporting the design, but the practical gap between the derived function and the adopted cosine weakens the claimed theoretical grounding. A more honest framing would present the ODE analysis as providing qualitative intuition (slope conditions) rather than a derivation of the specific functional form.

### Minor

- **Overclaim in transfer learning comparisons.** The abstract claims the method "outperforms the contrastive loss-based SSL algorithms" in general, but the transfer learning table (Table 7) shows DySTreSS underperforms DCL on 2 of 7 datasets (ISIC2016, MHIST). While the paper text honestly reports "5 out of 7," the abstract-level claim is broader than the evidence supports.

- **The "first exhaustive attempt" claim is imprecise.** The introduction states this is "the first exhaustive attempt to design a temperature function that can be adaptively tuned based on local and global structures." However, MACL (cited) already proposes a temperature function dependent on alignment, and IsogCLR (cited) individualizes temperature per sample. While the paper's framing around "local and global structures" is somewhat different, the claim as stated could be seen as overlooking related adaptive-temperature work. This is a minor presentational issue.

- **Shifted temperature profile search may overfit.** The sentence embedding experiments (Table 8) test 16 shifted temperature variants (combining multiple τ_min/τ_max ranges, shifts Δs, and scales k), and the best results are highlighted. While reporting multiple variants is transparent, the extensive search combined with the absence of held-out validation or error bars raises the risk of test-set overfitting.

### Trivial

None.

## Nice-to-Haves

- The paper could explicitly note that the per-pair temperature computation is O(1) and adds negligible overhead to the contrastive learning pipeline. (The current paper does not discuss computational cost at all.)
- An ablation comparing DySTreSS against simply using a fixed temperature set to τ_min, τ_max, and (τ_min+τ_max)/2 would help isolate whether the dynamic scaling itself or just the temperature range drives the improvement.

## Removed Points

These points were flagged for removal; treat them with caution:

- **"The comparison to negative-free methods uses 400-epoch pretraining while other tables use 200 epochs — inconsistency not explained."** REMOVED because the paper explicitly states: "We used the same training conditions as in [ZeroCL] and [ARB], for a fair comparison" (Sec. 5.5). This is a principled choice, not an inconsistency.

- **"Temperature ablation shows small differences; shifted ablations show similar accuracy across variants."** REMOVED because these are actually positive findings demonstrating robustness. That (τ_min=0.07, τ_max=0.1) gives 77.28% while (0.1, 0.2) gives 78.76% is a meaningful difference. The shifted variants showing similar performance (±0.3%) across diverse settings indicates the method is not brittle to hyperparameter choice — a strength, not a weakness.

- **"First exhaustive attempt claim is inaccurate because MACL and IsogCLR exist."** REMOVED as debatable and not central. The paper's phrasing specifically references "local and global structures" as the basis, which differs from MACL's alignment dependence and IsogCLR's per-sample optimizable parameter.

- **"Incomplete URL for code should be fixed."** REMOVED because truncated URLs are a PDF-extraction artifact, not a paper problem.

- **"Inter-class uniformity metric requires ground-truth labels."** REMOVED because this is an evaluation metric (not used in training), and the paper transparently describes it as measuring class centroids for analysis purposes only.

- **"Theoretical derivation inconsistency about N→∞ approximation dropping terms that are retained."** REMOVED because the approximation only drops the "1" relative to the sum K·exp(-s_ij/τ_ij) (which scales as O(N)), while the s_ij dependence is fully retained in the remaining ODE and its solution. The critic's specific technical objection is not supported by the paper's equations.

## Novel Insights

None beyond the paper's own contributions. Neither review surfaces insights that meaningfully extend or reframe the paper's own contributions; they primarily identify gaps in evaluation rigor and theoretical framing.

## Suggestions

1. **Report the fixed τ used for SimCLR baselines** in every experiment. If benchmark results from the lightly-ai library are used directly, state what temperature those benchmarks use. Include an ablation that compares DySTreSS against fixed temperature set to τ_min, τ_max, and their midpoint to isolate the effect of dynamic scaling.

2. **Add standard deviations over at least 3 seeds** for the main results (Tables 1–3), especially where margins over MACL are <1%. This would substantially strengthen the empirical claims.

3. **Reframe the theoretical contribution.** Remove the claim that the cosine function is "derived" from the ODE. Instead, present the ODE analysis as providing qualitative slope conditions (Proposition 1), and state clearly that the cosine is one of several functions that satisfy these conditions. The ablation showing linear and exponential functions perform similarly (Table 5) supports this more honest framing.

4. **Tone down the abstract-level claim** about "outperforming" to be specific about which baselines and on which metrics/settings.

5. **Add a brief computational cost note** stating the O(1) per-pair cost of the cosine temperature computation.

## Score and Decision

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>