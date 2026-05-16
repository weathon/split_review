Now I have a thorough understanding of the paper. Let me synthesize the final consolidated review.

## Summary

This paper proposes a gradient-free adversarial attack on time series regression XAI explanations using Particle Swarm Optimization (PSO) with a Dynamic Time Warping (DTW)-based objective function and an explanation-based local attack strategy. The approach is designed to attack non-differentiable XAI methods (LIME, SHAP) and is evaluated across LSTM, TCN, and Transformer models on two time series datasets. The paper identifies a genuine gap — no prior work addresses gradient-free attacks on time series XAI explanations.

## Strengths

- **First gradient-free attack targeting time series XAI explanations.** The paper correctly identifies that existing gradient-free attacks (GA-based) have only been applied to image and tabular data (Section 2, line 42), while time series regression explanations remain unaddressed. The proposed PSO-based method works with non-differentiable XAI methods (LIME, SHAP) without requiring gradient information. This fills a specific and meaningful gap.

- **DTW-based objective function adapted for time-series explanation discrepancies.** The paper argues that existing discrepancy measures (top-k, center of mass) are suboptimal for time series because explanations themselves form a time series. DTW captures alignment-based dissimilarity more naturally for this domain (Section 4). The experiments (Table 2) show DTW performs comparably to top-k and better than center-of-mass.

- **Explanation-based local attack strategy.** Rather than perturbing all time points, the method selects the top-20% most important time points based on the XAI explanation. Visualizations (Figures 2, 3) show this preserves the overall time series shape while still altering explanations. This is a practical design choice for the time series setting where global perturbations are more easily detected.

- **Reasonably broad evaluation scope.** The experiments cover 3 black-box models (LSTM, TCN, Transformer) × 4 XAI methods (SM, SG, LIME, SHAP) × 2 datasets, providing a systematic view of which XAI-model combinations are more or less vulnerable.

## Weaknesses

### Fatal
None.

### Major

- **No comparison against any existing attack baseline, despite claiming superiority.** The paper cites GA-based gradient-free attacks as the closest prior work (Huang et al., 2023; Baniecki and Biecek, 2022) but never compares PSO against GA, random search, or any other optimizer on the same task. The abstract states "by comparing our approach with existing attack methods, we demonstrate the superiority of our proposed objective function and local attack strategy" (line 12), yet the experiments only compare different objective functions (DTW vs. top-k vs. center-of-mass) — all variations of the authors' own method — and local vs. global attack. There is no comparison with any previously published attack method. This overclaim is unsupported by the evidence presented.

- **No verification that the output constraint is satisfied.** The attack objective (Eq. 5) includes the constraint $\|f(x)-f(x')\|<\delta$, but the paper never reports whether the generated adversarial examples actually satisfy this constraint. Without this, the reader cannot assess whether the attacks are truly "stealthy" in the intended sense (keeping model predictions nearly unchanged). The output change is a critical success condition that must be verified, not just assumed.

- **No quantitative stealthiness or efficiency metrics for the local attack.** The paper claims the local attack is more "stealthy" and "efficient" (Section 5.5) but provides no quantitative measurements: no ℓ₂/ℓ∞ perturbation magnitudes, no anomaly detection scores, no runtime comparisons. The claim rests entirely on visual inspection of a single example from one dataset. The efficiency claim (lower computational cost) is plausible but unmeasured.

- **Results reported without variance or statistical significance.** Tables 1 and 2 show single numeric values per condition with no confidence intervals, standard deviations, or multi-seed runs. The text makes general comparative statements (e.g., "LSTM with SG generates the most robust explanations") that cannot be assessed for reliability without some measure of variance.

### Minor

- **Local attack selection does not account for explanation shifts during the attack.** The method selects the top-k time points from the *original* explanation only (Section 4, lines 120-121), but the explanation changes as the attack progresses. A more principled approach might re-select based on the current adversarial explanation. This does not invalidate the method but limits its optimality.

- **Output constraint handling is vaguely specified.** The fitness function treats violation of the output constraint by setting the fitness to "a meaningless minimum" (line 136) without specifying how violation is detected, what the penalty magnitude is relative to the DTW term, or what δ threshold is used. This makes the optimization procedure hard to reproduce.

- **DTW motivation is intuitive rather than formally justified.** The paper argues DTW is more suitable for time series because "explanations can be interpreted as a time series themselves" (Section 4, line 122), which is intuitive but lacks a formal argument or illustrative example demonstrating cases where DTW succeeds and top-k fails.

- **No limitations or failure case analysis.** The paper has no limitations section. Practical constraints (e.g., the cost of repeated XAI queries, the assumption of explanation stability for local attack guidance) are not discussed.

### Trivial
None.

## Nice-to-Haves

- Adding random perturbation as a lower-bound baseline would help calibrate the reported TKI/SRC values: how much explanation change is simply from adding noise vs. from directed optimization.
- Reporting actual δ/ϵ values used and verifying constraint satisfaction for a sample of successful attacks.
- A runtime/query-count comparison between PSO, GA, and random search to support the efficiency argument.

## Removed Points

These points are flagged to be removed, treat them with caution:
- **Criticism about missing experimental setup details (model architectures, training details, dataset descriptions, hyperparameter values).** Sections 5.1 and 5.2 of the paper are missing from the parser-extracted text; these likely contained the experimental setup and would address many of these concerns. Per the instructions, parser-stripped sections should not be penalized.
- **Criticism about the second dataset not being named.** This information was likely in the parser-stripped Section 5.1.
- **Criticism about metrics (TKI, SRC) being undefined.** These were likely defined in the parser-stripped Section 5.2, where the text fragment "prehensive way to evaluate" (line 150) suggests evaluation metrics were described.
- **"Justified algorithmic choice of PSO" strength from Strength Finder.** This conflicts with the verified weakness that PSO is not experimentally compared to GA — the prose justification exists but lacks empirical support, so it does not stand as a strength.
- **Strength about "systematic evaluation" implying well-defined metrics.** While the evaluation scope is broad, the undefined metrics (in available text) and lack of variance reporting weaken this claim. The breadth aspect is retained in Strengths above.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. **Add baseline comparisons.** Compare against a GA-based attack (adapted from Huang et al., 2023 to time series) and random perturbation. This is essential to support any claim of superiority and to demonstrate that PSO offers practical advantages over the existing approach in this domain.

2. **Verify and report output constraint satisfaction.** Show that $\|f(x)-f(x')\|<\delta$ actually holds for the generated adversarial examples, and report the distribution of output changes. This is critical evidence for stealthiness.

3. **Quantify the local attack benefits.** Report ℓ₂/ℓ∞ perturbation magnitudes and wall-clock runtimes (or number of XAI queries) for both global and local attacks to substantiate the stealthiness and efficiency claims.

4. **Report variance.** Run experiments with multiple random seeds and report standard deviations or confidence intervals for the key metrics.

5. **Clarify the claim in the abstract.** If no existing attack methods are compared, the abstract should not claim superiority via comparison with existing methods. The contribution stands on its own merits (first in the time series domain) without this overclaim.

## Score and Decision

**Originality:** The paper addresses a genuine gap (gradient-free attacks on time series XAI explanations) and introduces reasonable adaptations (DTW objective, local attack). However, the core idea of gradient-free attacks on non-differentiable XAI already exists in prior GA-based work — the novelty lies in the domain transfer and specific design choices.

**Importance of research question:** The question is important. XAI robustness in time series is under-explored, and high-stakes domains (medicine, finance) demand reliable explanations.

**Claims supported:** **No.** The central claim of "superiority" is unsupported by any baseline comparison. The attack's effectiveness is demonstrated qualitatively, but the output constraint is not verified, metrics lack definitions in available text, and no variance is reported. The evidence does not meet the standard required for the claims made.

**Soundness of experiments:** **Below threshold.** The experimental design has critical gaps: no baselines, no constraint verification, no variance, qualitative comparison on a single example.

**Clarity of writing:** Adequate but with gaps. The method description is clear, but key experimental details and metric definitions are missing from the available text.

**Value to the community:** The gap identification and proposed approach are potentially valuable, but in their current form the results cannot be reliably used or built upon.

The paper identifies a real gap and proposes a reasonable methodological approach, but the experimental validation is fundamentally insufficient to support its claims. The absence of any baseline comparison, failure to verify the output constraint, lack of quantitative stealthiness/efficiency metrics, and overclaim in the abstract mean the contributions cannot be properly assessed. The core idea has merit, but the paper needs substantial revision before it meets publication standards.

MY FINAL SCORE: <pineapple>4.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>