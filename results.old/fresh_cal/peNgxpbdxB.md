Now I have a thorough understanding of the paper. Let me compose the final consolidated review.

---

## Summary

This paper introduces Scalable Discrete Diffusion Samplers (SDDS), a framework with two novel training objectives for discrete diffusion models — one using policy gradients (reverse KL with RL) and one using Self-Normalized Importance Sampling (forward KL with MC) — that enable mini-batching across diffusion steps, overcoming the linear memory scaling that previously limited the number of diffusion steps. The paper further extends SN-NIS and NMCMC unbiased-sampling techniques to approximate-likelihood diffusion models in discrete domains for the first time. Experiments on 7 unsupervised combinatorial optimization benchmarks show that SDDS with reverse KL/RL training achieves the best average solution quality on most benchmarks, while on Ising-model unbiased sampling the forward KL variant outperforms autoregressive baselines.

## Strengths

1. **Novel memory-efficient training for discrete diffusion samplers.** The paper identifies a genuine limitation in prior work (DiffUCO) — backpropagation through the full diffusion trajectory imposes linear memory scaling with the number of steps — and proposes two clean, principled solutions (policy-gradient-based RL training and Monte-Carlo-estimated forward KL) that both enable mini-batching across steps. This is a well-motivated technical contribution.

2. **State-of-the-art unsupervised combinatorial optimization results.** SDDS with the reverse-KL/RL objective achieves the best average solution quality on 6 of 7 UCO benchmarks (significantly better on 4, insignificantly better on 2) and is on par on the remaining benchmark. When sampling 150 solutions per instance, both SDDS variants are the best-performing objectives in 6 of 7 cases. These results are achieved under fixed computational budgets, demonstrating a practical advantage.

3. **First extension of unbiased sampling to approximate-likelihood diffusion models in discrete domains.** The adaptation of SN-NIS and NMCMC to discrete diffusion models (where exact likelihoods are unavailable) is a novel contribution that opens a new direction. The Ising-model experiments (Table 4) show that the forward-KL diffusion model achieves lower free-energy error and higher effective sample size than the autoregressive baseline, suggesting that diffusion models offer a competitive alternative in this setting.

4. **Principled theoretical grounding.** The training objectives are derived from alpha-divergences, with clear connections between the reverse/forward KL divergences and the policy-gradient / importance-sampling estimators. This places the methods on a solid information-theoretic foundation.

## Weaknesses

### Fatal
None.

### Major

1. **No variance or statistical significance reported for any UCO result.** Tables 1–3 report only average solution quality; no standard deviations, confidence intervals, or p-values are provided. The text uses phrases like "significantly in 4 out of 7 cases and insignificantly in 2 out of 7 cases" without any supporting statistical test. Given the inherent randomness of neural network training and the use of only 30–150 samples per instance, this omission makes it impossible to assess whether the reported differences are meaningful or within noise. This substantially weakens the SOTA claims.

2. **Ablation of architectural improvements is missing.** The paper adds a cosine learning rate schedule and graph normalization to the DiffUCO baseline, stating these "improve the obtained results" (line 159). No ablation is performed to separate the effect of these modifications from the effect of the proposed training objectives. Since the "improved DiffUCO" baseline (DiffUCO with these additions) is the direct comparator to SDDS, and DiffUCO is reported as the second-best method in most cases, it is impossible to know how much of SDDS's advantage comes from the proposed training methods versus these architectural changes. This is a methodological gap in the evaluation design.

3. **Unbiased sampling evaluation lacks standard MCMC baseline and ground-truth validation.** The unbiased sampling experiments compare diffusion models only against an autoregressive (AR) baseline using the same architecture. Standard Markov Chain Monte Carlo (e.g., single-spin-flip Metropolis) — the de facto tool for Ising-model sampling that the paper itself mentions in the introduction — is not included as a baseline. Additionally, no validation against ground-truth values (e.g., exact partition sums for small Ising models like 8×8 or 10×10) is provided to confirm that the SN-NIS/NMCMC adaptations produce unbiased estimates. These gaps make it difficult to contextualize the reported results and to verify the correctness of the proposed unbiased-sampling methods.

### Minor

4. **Experimental design conflates the effect of step count with the effect of the training method.** The paper compares SDDS (trained with 2× steps, evaluated with 3× steps) against DiffUCO (trained and evaluated with fewer steps) under the same memory budget. This is a fair comparison for the practical claim that "SDDS achieves better results under the same budget." However, it does not isolate whether the improvement comes from (a) the proposed training objectives or (b) simply having more diffusion steps — a benefit that Sanokowski et al. (2024) already established. A control experiment training SDDS with the same number of steps as DiffUCO would cleanly separate these factors. As presented, the reader cannot attribute the gains specifically to the new objectives.

5. **Unbiased sampling experiments are limited to a single temperature and system size.** The Ising-model evaluation considers only the 24×24 system at the critical inverse temperature. Testing at multiple temperatures and system sizes would demonstrate generality and strengthen the claim that diffusion models "can outperform popular autoregressive approaches" for unbiased sampling.

6. **Hyperparameter sensitivity of the RL-based objective is not analyzed.** The paper acknowledges that "the reverse KL-based objective introduces new optimization hyperparameters" but asserts they require "minimal fine-tuning" without reporting the values used or providing a sensitivity analysis. Given that hyperparameter tuning is a known challenge for policy-gradient methods, this claim needs support.

### Trivial
None beyond what is attributable to parser artifacts.

## Nice-to-Haves

- A plot of memory usage vs. number of diffusion steps for DiffUCO and each SDDS variant would make the central memory-efficiency claim more tangible.
- Including effective sample size or similar diagnostics for the SN-NIS estimates would strengthen the unbiased-sampling evaluation.
- The paper could note that standard MCMC baselines were omitted due to scope constraints or computational cost.

## Removed Points

- **Missing Sec 3.2 content**: The harsh critic notes that the method described in Sec. 3.2 cannot be reviewed because it is missing. This content was stripped by the PDF parser (the extracted text jumps from Sec 3.1 directly to Related Work). The original submission contains this section; the criticism is not valid against the paper.
- **Criticism that DiffUCO's mode-seeking behavior is "anecdotal"**: The paper reports this observation (line 180) as an explanation for excluding DiffUCO from the unbiased sampling table, not as a central claim. This is a descriptive note about a method's behavior, not a weakness.
- **Speculation about gradient checkpointing for DiffUCO**: The critic's suggestion that DiffUCO could use gradient checkpointing to match SDDS's step count is speculative and not grounded in what the paper does or claims. The paper's comparison is under fixed computational budget, which is a standard and valid approach.
- **Generic "could the metric be measuring a proxy" phrasing**: The critic's framing of concerns as area-of-concern sweeps (general "evaluation lacks rigor") without specific concrete anchors has been replaced with specific, verifiable criticisms above.
- **Pure formatting/style nitpicks and missing related works**: Excluded per instructions.

## Novel Insights

The most interesting cross-review insight is that **the paper's strongest experimental claim (SOTA UCO) and its most novel contribution (unbiased sampling with approximate-likelihood models) have an inverse relationship in terms of evidence quality.** The UCO results are reported across 7 diverse benchmarks with clear comparison to prior work, but the evidence is weakened by missing variance and ablations. Conversely, the unbiased-sampling contribution is genuinely novel but evaluated in a narrow setting (one system size, one temperature, one baseline). The paper would be substantially strengthened by bringing the evidence quality of these two halves into balance. A second insight is that the paper's two training objectives (rKL/RL and fKL/MC) serve complementary roles — one excels at average solution quality, the other at exploration — which the paper recognizes and demonstrates, but this trade-off is not fully exploited in the experimental design.

## Suggestions

1. **Report standard deviations or confidence intervals for all UCO results** across multiple training seeds (≥3). Even a simple table footnote reporting the range or std across seeds would dramatically improve trust in the reported numbers.
2. **Add an ablation experiment** that trains SDDS *without* the cosine LR schedule and graph normalization, to isolate the contribution of the proposed training objectives from these engineering improvements.
3. **Add a standard MCMC baseline** (e.g., 10⁶ Metropolis steps) to the unbiased sampling experiments. Even if it is not competitive, it provides a reference point familiar to the statistical physics community.
4. **Add ground-truth validation for unbiased sampling** on a smaller Ising model (e.g., 8×8 or 10×10) where the exact partition sum is known, to confirm that the SN-NIS/NMCMC adaptations are correct and the estimates are unbiased.
5. **Include a controlled comparison** training SDDS with the *same* number of diffusion steps as DiffUCO, to separate the effect of the step count from the effect of the training objective.
6. **Report hyperparameter values** for the RL-based objective and, if possible, include a brief sensitivity analysis.

---

## Score and Decision

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>