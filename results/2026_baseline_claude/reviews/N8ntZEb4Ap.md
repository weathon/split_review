## Summary

AutoNFS is a neural feature selection (FS) method that jointly trains a **masking network** (based on Gumbel-Sigmoid relaxation with temperature annealing) and a **task network** (downstream predictor). The core claim is that AutoNFS automatically learns the minimal sufficient subset of features via an L1 cardinality penalty on the mask, without requiring the user to specify the number of features. It is evaluated on 11 OpenML classification/regression benchmarks under three corruption scenarios, and on 24 real-world metagenomic datasets, reportedly outperforming 10 classical and neural FS baselines in average ranking.

---

## Strengths

- **Practical automatic cardinality determination.** Most FS methods require the number of features to be a user-specified hyperparameter. AutoNFS's L1 penalty on the mask sum is a simple, end-to-end differentiable mechanism that removes this requirement, which is a genuine usability benefit.

- **Near-constant empirical scaling.** Figure 4 provides a compelling empirical analysis: AutoNFS achieves α ≈ 0.08 (time ∝ D^α) vs. α = 1.0 for filter methods and α = 1.41 for RFE. This is a substantial practical advantage for datasets with thousands of features.

- **Strong feature selection precision.** Figure 3a shows zero misselection error for random and corrupted scenarios, and Figure 3b demonstrates that each selected feature carries measurable predictive power (mean drop 0.313 when any one feature is removed), indicating the model is not padding the selected set with noise features.

- **Broad empirical coverage.** Testing across 11 OpenML datasets (classification and regression), three corruption types, and 24 biological high-dimensional datasets provides solid breadth of evaluation.

---

## Weaknesses

### Fatal
None.

### Major

1. **Unfair comparison to baselines.** The paper explicitly states that all baseline methods are constrained to select the same number of features as the pre-corruption original dimensionality, while AutoNFS is free to select far fewer. The aggregate rankings (Figure 2) are based purely on predictive accuracy, so AutoNFS benefits from its freedom to use a smaller, cleaner feature set while baselines are burdened with a larger, noisy one. A proper evaluation would either (a) run baselines with their own adaptive feature-count selection, or (b) compare methods via accuracy–sparsity Pareto curves at matched feature counts. Without this, the claim that "AutoNFS consistently outperforms competitive methods" may largely reflect the freedom to select fewer features, not superior feature identification.

2. **The "automatic" framing understates the role of λ.** While AutoNFS eliminates the need to specify the number of features directly, the final feature count is a sensitive function of the penalty weight λ. The paper simply fixes λ = 1 and reports good results, but Appendix F (referenced but unavailable) presumably shows sensitivity. If λ must be tuned per dataset to obtain a good sparsity–accuracy trade-off, then AutoNFS replaces one hyperparameter (feature count) with another (λ), and the "automatic" advantage is narrower than claimed.

3. **Masking network design lacks justification.** The masking network takes a random learnable embedding e ∈ ℝ^{D_e} and maps it to D-dimensional logits via a learned network f. This is architecturally unusual: since e is a free parameter and f is also learned, the composition f_φ(e) is functionally equivalent to directly learning a D-dimensional logit vector, unless D_e ≪ D is used as structural regularization. The dimensionality of e is never specified, the benefit of the extra network layer vs. a raw logit vector is never ablated, and the design choice is never motivated. This makes it unclear whether the masking network adds any value beyond a simpler implementation.

### Minor

1. **Metagenomic results are mixed.** In Table 2, AutoNFS MLP underperforms the full-data MLP by a non-trivial margin on several datasets (e.g., KeohaneDM_2020: 0.344 vs. 0.469; ThomasAM_2018a: 0.567 vs. 0.733; YuJ_2015: 0.417 vs. 0.653). The claim of "+0.7 pp average improvement" obscures these drops, and several cases suggest AutoNFS is discarding task-relevant features.

2. **Computational complexity comparison scope is narrow.** Figure 4 compares AutoNFS inference time against simple filter methods (ANOVA F, MI), RFE, and Delete2Vec, but omits direct neural competitors such as STG, LassoNet, or Concrete Autoencoders—the methods most relevant for a neural FS paper. The "nearly constant overhead" claim should be validated against the full set of comparators.

3. **Temperature annealing sensitivity.** The paper uses a fixed decay rate α = 0.997 across all datasets, but the final temperature achieved depends on training duration. No analysis is provided on how sensitive the selected feature set is to the annealing schedule.

### Trivial
- The misselection error metric in Figure 3a is presented as an average across datasets, making it hard to tell whether any individual dataset drives the result.

---

## Nice-to-Haves

- A controlled ablation comparing "direct logit vector" vs. "masking network + embedding" would clarify the architecture contribution.
- Pareto-front plots (accuracy vs. number of features) comparing AutoNFS and the strongest baselines at matched feature counts would greatly strengthen the experimental claims.
- Wall-clock training time comparisons (not just FS-phase time) against neural baselines (STG, LassoNet, Concrete AE) would make the efficiency claim more complete.

---

## Novel Insights

The paper's most genuinely novel element is the framing of *automatic feature count discovery* as a byproduct of a differentiable L1 cardinality penalty on Gumbel-Sigmoid masks, rather than as a distinct hyperparameter search problem. The observation that this penalty, combined with slow temperature annealing, converges to a nearly binary mask whose sparsity is self-calibrated to the task difficulty is a useful conceptual contribution. The near-constant-time scaling behavior, validated empirically across up to 10^5 features, is also a noteworthy practical finding that distinguishes AutoNFS from most neural FS methods.

---

## Suggestions

- Run all 10 baseline methods at their Pareto-optimal feature counts (using their own internal selection threshold or a sweep) and compare accuracy at the same feature budget AutoNFS chooses. This would provide the most credible demonstration of AutoNFS's advantage.
- Report the actual value of D_e used in experiments and include an ablation where f is replaced by a single affine layer (or just a raw D-dimensional learnable vector) to isolate the masking-network's contribution.
- For metagenomic experiments, include at least one baseline FS method (e.g., STG or RF importance) at the same reduced dimensionality for comparison; currently the only comparisons are full-data MLP/RF vs. AutoNFS-reduced MLP/RF.

---

## Score and Decision

AutoNFS addresses a real problem (automatic feature count determination), proposes a clean differentiable solution, and provides broad empirical evaluation. However, the central comparative claim suffers from a significant methodological fairness issue (baselines constrained to a fixed, larger feature count), the "automatic" contribution is partially offset by the undiscussed λ sensitivity, and the masking network design choice goes unjustified. These concerns collectively place the paper at borderline reject.

MY FINAL SCORE: <score>4</score>
MY FINAL DECISION: <decision>Reject</decision>