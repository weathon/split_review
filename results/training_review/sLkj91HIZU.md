Now I have enough information to write a thorough, cross-verified review.

## Summary

The paper studies whether transformers can learn optimal predictors for mixtures of linear regressions, a setting where each prompt comes from one of several linear subpopulations. It provides a constructive proof (Theorem 1) that an autoregressive transformer can represent the Bayes-optimal posterior mean predictor, and presents experiments across varied numbers of components (m=5–30), noise levels (σ=0,1), and prompt lengths (k=1–60) showing that trained transformers achieve near-oracle MSE. A distance-based analysis (Section 4.3) provides evidence that the trained transformer's outputs are closest to the posterior mean among candidate algorithms.

## Strengths

- **Constructive proof of representability (Theorem 1).** The paper proves that the Bayes-optimal posterior mean predictor for mixtures of linear regressions lies within the function class of an autoregressive transformer. This is a non-trivial theoretical guarantee that goes beyond mere approximation — it shows exact representability of the optimal procedure. The accompanying arithmetic circuit (Figure 1) gives intuition for how the computation decomposes across layers.

- **Empirical demonstration of near-optimal prediction across diverse settings.** The MSE results (Section 4.1, 4-panel figure) show that across m=5,20 components and σ=0,1 noise, the transformer's normalized MSE closely tracks the oracle posterior mean and substantially outperforms ordinary least squares. This holds across prompt lengths k=1–60, spanning the regimes from very few examples to many.

- **Inference-time distance analysis (Section 4.3) identifies the learned algorithm.** The squared-distance metric \(d_k^{\text{sq}}\) comparing transformer outputs to six candidate algorithms consistently shows the smallest distance to the posterior mean with oracle weights, across all tested numbers of components (m=5,10,20,30). This provides mechanistic insight beyond raw MSE curves — it tells us *what* the transformer has learned, not just that it performs well.

- **Distribution shift experiments add practical value.** Covariate scaling (κ=0.33–3), weight scaling (α=0.33–3), and additive weight shifts (ε=0–1.0) probe the transformer's robustness beyond the exact training distribution. The finding that the transformer tolerates moderate shifts (κ∈{0.33,0.5,2}, ε=0.25) is practically relevant and goes beyond what model-specific methods typically evaluate.

## Weaknesses

### Fatal
None. The paper's core claims are supported by evidence; no identified issue invalidates the results.

### Major
None. No weakness rises to the level of seriously threatening acceptance.

### Minor

- **Representation-learning framing gap.** Theorem 1 proves representability (a transformer *exists* that computes the optimal predictor), but the paper's title and framing ("Transformers can optimally learn") blur the distinction between representation and learning. This is not a fatal flaw — the paper has independent empirical evidence that trained transformers approximate the optimal predictor, and representation theorems are standard in this literature (e.g., Garg et al. 2022, von Oswald et al. 2023). However, the paper would benefit from sharper language distinguishing "the optimal predictor is representable" from "training finds it." The experiments already address the latter; the framing should reflect this division of labor.

- **No variance or error bars on MSE plots.** The MSE curves in Section 4.1 appear to show single-run results without confidence intervals or standard deviations across training seeds or evaluation prompts. Given the known variance in transformer training and in MSE estimation, this omission makes it impossible to assess whether observed differences (e.g., between transformer and posterior mean) are statistically significant. Plots with error bars (over at least 3 seeds and many evaluation prompts) would substantively strengthen the empirical claims.

- **Depth requirements of the construction are not justified in the main text.** The paper states that generalizing the arithmetic circuit from k=2, m=3 to arbitrary (k,m) is "straightforward" and that the proof amounts to showing each operation is implementable by a transformer. While the full construction is deferred to the appendix, the main text provides no analysis of how depth scales with k or m, or whether the fixed 12-layer architecture used in experiments is sufficient to realize the construction. This disconnect between the theoretical construction and the actual experimental setup is worth discussing.

- **Distribution shift comparison to posterior mean is described but not shown.** The paper states that the posterior mean procedure was evaluated under the same shifts and provides a high-level comparison (less sensitive to covariate scaling, similar on label shifts), but the corresponding plots are not included in the main text. Showing these figures would allow readers to directly assess how much robustness is lost by using the transformer versus the optimal procedure.

- **Sample-efficiency comparison lacks discussion of training dynamics.** The fixed-training-set-size comparison (Section 4.2) is a reasonable approach to measuring sample efficiency, and the paper's claim that the transformer is "close to" specialized algorithms is appropriately measured. However, the paper does not discuss the fact that the transformer undergoes iterative training (multiple epochs) while EM and subspace algorithm make direct use of the data — this is a meaningful methodological difference worth acknowledging, even if the comparison is standard practice.

### Trivial

- The claim that squaring can be implemented by a feedforward network with GeLU activation is stated without references to the universal approximation literature or a construction sketch. A brief citation or comment would suffice.

- The layer normalization definition used in the paper (mean-centering followed by division by ℓ₂ norm, without learnable scale/shift) is non-standard. The paper could note this difference explicitly.

## Nice-to-Haves

- An analysis of the prompt-length regime where the transformer deviates from the posterior mean and the distance to the argmin procedure is comparable (Figure 4, small k). This could shed light on whether the transformer uses a simpler algorithm when data is scarce.

- A comparison of attention patterns to the posterior mean's exponential weighting scheme would strengthen the mechanistic story — currently the analysis probes only outputs, not internal representations.

- Testing on nonlinear component functions (e.g., ReLU networks) would broaden the scope toward the "general-purpose" claim, though the paper explicitly scopes this as future work.

## Removed Points

These points were flagged during review but are removed for the following reasons:

1. **"The construction requires depth scaling with k"** — This misunderstands how attention works: a single attention head can aggregate over variable-length sequences in constant depth regardless of k. The softmax is over m components, not k examples. There is no technical basis for the claim that depth must scale with k.

2. **"EM and SA are single-pass algorithms"** — EM is inherently iterative (multiple E/M steps); the claim is factually incorrect. The sample-efficiency comparison on fixed training set size is standard.

3. **"No experiments test nonlinear components or transfer"** — The paper explicitly scopes itself to linear mixtures and discusses nonlinear extensions as future work. This is scope creep.

4. **"The layer normalization likely breaks the residual pathway"** — Speculative, no evidence or analysis provided. The paper defines the specific normalization used; whether it works is answered by the experimental results.

5. **"The transformer could simply be overfitting or memorizing"** — Unsupported speculation contradicted by the paper's main results (the transformer generalizes to unseen prompts at inference time and tracks the oracle across increasing prompt lengths).

6. **Pure formatting/style nitpicks and comments about missing appendix content** — These are either parser artifacts or sections stripped from the PDF (the proof is in the appendix, which exists in the original submission).

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. Report MSE curves with standard deviations over at least 3 training seeds to establish statistical significance. This single change would substantially strengthen the empirical core of the paper.

2. Reframe the title and key claims to more precisely separate the representation theorem ("transformers *can* represent the optimal predictor") from the empirical finding ("trained transformers *do* approximate it"). For example: "Transformers can represent and empirically approximate the optimal predictor for mixtures of linear regressions."

3. Include the posterior mean distribution-shift comparison figures (currently only described textually) in the main text or supplement to concretely support the robustness claims.

4. Add a brief discussion of depth requirements: how many layers does the construction use for the largest (k,m) tested, and how does this compare to the 12-layer architecture?

## Score and Decision

The paper makes a solid contribution: it provides the first theoretical and empirical evidence that transformers can handle mixture-of-regressions problems near-optimally. The constructive proof and the distance-based mechanistic analysis are genuine strengths. The weaknesses are presentation issues (no error bars, framing imprecision, deferred justification) rather than fatal methodological flaws. The claims are well-supported by the experimental evidence, and the experiments cover a reasonable range of settings. The paper is clearly written and addresses an important problem.

MY FINAL SCORE: <pineapple>7.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>