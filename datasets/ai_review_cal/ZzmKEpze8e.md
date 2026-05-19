- Decision: Accept
- Avg Score: 6.50
- Scores: 6, 6, 6, 8
Now I have a thorough understanding of the paper. Let me compose the final consolidated review.

---

## Summary

This paper proposes a Bayesian online continual learning method that combines a deep neural representation with a state-space model over the linear predictor weights. Non-stationarity is captured via a "parameter drift" transition density controlled by a learned forgetting coefficient γ, with inference via efficient Kalman filter recursions ($O(m^2)$ per step). The method is extended to classification through a Gaussian approximation to the softmax likelihood, an online-learned calibration parameter α, and SGD fine-tuning of the representation. Experiments on CIFAR-100 (stationary and non-stationary variants) and CLOC (a large-scale 37M-image geolocation benchmark) are presented.

## Strengths

- **Online adaptation of the forgetting coefficient γ is a clean, principled mechanism for capturing non-stationarity.** The paper derives an SGD update for γ based on the log predictive probability (Section 3.3), and the toy example (Figure 1, left) empirically demonstrates that γ drops sharply at change points in an artificial time series. On non-stationary CIFAR-100, γ drops at task boundaries (Figure 2), confirming the intended behavior. This goes beyond prior Kalman-filter-based online learning that uses fixed forgetting.

- **Computationally efficient inference via shared covariance matrices.** Section 3.2 explicitly states that the covariance matrices $(A_n^-, A_n)$ are shared among all $K$ classes, keeping per-iteration cost at $O(Km + m^2)$ and dominated by $O(m^2)$ when $m > K$. This design choice makes the method scalable while retaining exact Kalman updates, and is a concrete technical contribution.

- **Online calibration parameter α improves predictive probability estimates.** Section 3.4 introduces a learnable scaling parameter that rescales logits before the softmax, optimized jointly with the representation via online SGD. This directly addresses the approximation error from the Gaussian-likelihood trick and provides a practical mechanism for improving the approximate posterior quality.

## Weaknesses

### Fatal
None.

### Major

1. **No error bars, confidence intervals, or variance estimates for any experimental result.** All reported numbers (Table 1) are single-point estimates. The method involves Monte Carlo sampling for gradient estimation and prediction, stochastic minibatch processing, and random initialization of the backbone. Without any measure of variability, the reader cannot assess whether reported differences (e.g., 16.9% vs. 16.4% on stationary CIFAR-100 with backbone finetuning; 51.2% vs. 50.5% for learned vs. fixed γ) are meaningful or due to noise. This weakens all empirical claims in the paper.

2. **CLOC results are reported only in a plot, without numerical values.** The flagship large-scale experiment (Figure 3) shows line charts but provides no final accuracy numbers in a table or caption. The paper claims "Kalman filter provides very strong performance" and "replay-free Kalman filter matches the performance of Online SGD with replay" — but the reader cannot verify claimed advantages quantitatively. Combined with the lack of variance estimates (Weakness 1), the central experimental evidence for the method's real-world utility is insufficiently supported.

3. **External baseline comparisons are not adequately controlled.** The CLOC experiments use a version of the dataset that "is similar" to that of prior work but with acknowledged downloading differences and a different number of images (~37M vs. the original). Baseline results (ER, ACE, Online SGD) are taken from published papers rather than reproduced under a common experimental framework. The paper acknowledges the potential differences (Section 4.3: "we are mindful of potential small differences due to the downloading errors") but does not discuss the threat to validity or argue why the comparisons remain informative. For non-stationary CIFAR-100, external baselines are entirely absent from the table (the paper explains the cited protocol only considered stationary CIFAR-100, but this means the non-stationary results lack external context).

### Minor

1. **Missing reproducibility details for core experimental parameters.** Algorithm 1 and the experimental description do not specify: the optimizer used for fine-tuning θ and α, the learning rate schedule (including for the γ-update), the number of Monte Carlo samples $S$ for prediction and γ-gradient estimation, or the clipping strategy for δ_n. The paper states hyperparameters were "selected by choosing the variant with highest cumulative log probabilities" (Section 4.2) but does not report the chosen values. While some of these are standard tuning choices, the Monte Carlo sample size $S$ and optimizer configuration are non-trivial for reproducibility.

2. **No analysis of the Gaussian approximation quality.** The paper replaces the softmax likelihood with a Gaussian to keep Kalman recursions tractable (Section 3.1), citing prior use in Gaussian process classification and meta-learning. However, the quality of this approximation — which directly affects the posterior over weights and thus all downstream predictions — is never analyzed, even on a small proxy. The calibration parameter α is introduced to compensate, but no ablation isolates how much the approximation degrades performance without it.

### Trivial
None.

## Nice-to-Haves

- An ablation study isolating the effect of learning γ vs. fixing various constant values would strengthen the claim that online adaptation is driving the gains, especially on CIFAR-100 where the learned-γ variant only marginally outperforms fixed-γ=0.999 in several settings (e.g., 55.5% vs. 55.5% with replay).
- An ablation showing the impact of the Monte Carlo sample size $S$ on predictive quality and computational cost would be useful.

## Removed Points

These points are flagged to be removed; treat them with caution.

1. **Commented-out sections (`\comm{...}`) as a structural flaw.** The raw text extraction shows two `\comm{...}` sections (an algorithm placeholder and "Open-class Classification" / "A generative approach using the Chinese restaurant process") with TODOs. In the compiled PDF, these sections are suppressed by the `\comm` command and would not appear. The extraction artifact does not reflect the actual submission. *Removed: parser artifact, per hard rule on formatting artifacts.*

2. **Transition model justification.** The harsh critic claimed the justification for variance-preserving diffusion was not discussed. The paper explicitly states (lines 108–111) that the transition is a variance-preserving diffusion and explains why this keeps $\sigma_w^2$ constant. *Removed: factually incorrect — the paper does discuss this.*

3. **Missing related work comparisons (deep state-space models, Bayesian NNs with temporal structure).** The hard rules forbid mentioning missing related works without external confirmation. *Removed: per hard rule.*

4. **Strength: "Strong empirical results on CLOC with a pretrained backbone."** While the paper claims strong CLOC performance, this strength conflicts with Verified Weakness 2 (CLOC results only in a plot without numerical values) and is weakened by Weakness 3 (uncontrolled baselines). The qualitative description is insufficient to serve as strong evidence. *Demoted from kept strengths per the rule that when a strength and weakness disagree, the weakness wins.*

## Novel Insights

The harsh critic's most valuable observation — that the CLOC experimental evidence is weakened by being plot-only — interacts interestingly with the strength finder highlighting the same CLOC results as the paper's strongest selling point. This tension reveals a pattern common in OCL papers: a large-scale, expensive benchmark is run only once (or without budget for multiple runs), and the resulting single trajectory is presented as conclusive. The meta-insight is that the field needs evaluation standards that match the cost of large-scale experiments (e.g., bootstrapped accuracy from chunk-level splits). The paper's actual technical novelty — learning γ as an online parameter via SGD on the log predictive density, combined with a shared-covariance Kalman filter — is well-motivated and clearly presented, and is decoupled from the CLOC reporting issues.

## Suggestions

1. Report all CLOC results in a table with numerical accuracy values at the end of the stream (and preferably at intermediate points). Add a column for the Kalman variants alongside the baselines under a single footnote describing dataset differences.
2. Add error bars (e.g., standard deviation over 3–5 runs with different random seeds) to the CIFAR-100 results. For CLOC, if multiple runs are prohibitively expensive, report bootstrapped confidence intervals from chunk-level splits.
3. Add an ablation that compares the learned γ against a grid of fixed γ values on non-stationary CIFAR-100 to quantify the benefit of online adaptation independently.
4. Report the optimizer, learning rate schedule, Monte Carlo sample size $S$, and final chosen hyperparameter values for all reported experiments.
