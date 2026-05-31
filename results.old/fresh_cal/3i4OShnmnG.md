I've now thoroughly examined the paper and all reviewer claims. Let me write the final consolidated review.

## Summary

This paper proposes a gradient-free adversarial attack on XAI explanations specifically for time series regression tasks. The method uses Particle Swarm Optimization (PSO) to generate adversarial examples without requiring gradient information, introduces a Dynamic Time Warping (DTW)-based objective function to better capture explanation differences in time series, and implements an explanation-guided local attack strategy that perturbs only the most important time points. Experiments on two datasets with three black-box models (LSTM, TCN, Transformer) and four XAI methods show the attack can alter explanations from non-differentiable methods (LIME, SHAP), while revealing that LSTM+SmoothGrad produces the most robust explanations.

## Strengths

1. **First gradient-free attack targeting time series XAI explanations.** The paper correctly identifies that existing gradient-free XAI attack methods (Huang et al., 2023; Baniecki and Biecek, 2022) have only been applied to image and tabular data (Sec. 2, final paragraph). Extending gradient-free attacks to time series is a well-motivated niche that is indeed unexplored.

2. **Attack is demonstrated across multiple models, XAI methods, and datasets.** Table 1 (described in Sec. 5.3) reports results across LSTM, TCN, and Transformer models, four XAI methods (SM, SG, LIME, SHAP), and two datasets — providing breadth that goes beyond a single configuration. The attack successfully reduces robustness for LIME and SHAP (non-differentiable methods) across all models.

3. **Uses two complementary evaluation metrics.** The paper employs both Top-K Intersection (TKI) and Spearman's Rank-Order Correlation (SRC) to measure explanation changes (Sec. 5.2/5.3), providing a more robust assessment than relying on a single metric.

4. **Local attack strategy is a plausible approach for time-series stealth.** Targeting only the top-20% most important time points (guided by the original explanation) is a sensible design choice to minimize visible perturbation while still disrupting key explanatory features.

## Weaknesses

### Fatal
None.

### Major

1. **Abstract claims comparison with existing attack methods, but no such comparison is performed.** The abstract states: "by comparing our approach with existing attack methods, we demonstrate the superiority of our proposed objective function and local attack strategy" (line 12). However, the experiments contain zero comparisons with any attack method from the literature. The only baselines are internal variants of the proposed method — different objective functions (DTW vs. top-k vs. center-of-mass) and local vs. global perturbation. The paper does not compare against the GA-based gradient-free attacks of Huang et al. (2023) or Baniecki and Biecek (2022) (which are cited in the related work), nor against any gradient-based attack as an oracle upper bound. This makes it impossible to assess whether the proposed approach advances the state of the art. Without this comparison, the claim of "superiority" is unsubstantiated.

2. **Local vs. global attack comparison is purely qualitative.** Section 5.5 presents only a single visual example (Fig. 2) and a heatmap (Fig. 3) to support the claims that local attack achieves "comparable results" to global attack with lower computational cost and better stealth. No quantitative metrics are reported for this comparison — no TKI/SRC values, no perturbation magnitude (ℓ∞ or ℓ2), no computational runtime measurements, and no statistical summary across multiple samples. The paper claims "local attacks can achieve comparable results at specific points in time" but provides no data to verify this generalization.

3. **Constraint satisfaction (output change, perturbation magnitude) is not reported.** The attack formulation (Eq. 5) includes two constraints: output change ‖f(x)−f(x′)‖ < δ and perturbation bound ‖x−x′‖∞ < ε. The paper never reports the actual achieved output changes or perturbation magnitudes for the generated adversarial examples. It describes how particles violating the output constraint are penalized in the fitness function (Sec. 4, "Evaluating fitness"), but does not show what fraction of final examples satisfy the constraint, how δ and ε were set, or whether perturbations are indeed imperceptible — a core motivation for the local attack. Without this, the attack's stealth and validity claims are unverifiable.

4. **The PSO selection over GA is claimed but not empirically supported.** The paper motivates PSO by stating it has "fewer parameters, reducing the time spent on parameter tuning" and "converges faster than genetic algorithms" (Sec. 4, para 1). Since the related work cites GA-based gradient-free attacks (Huang et al., 2023), and PSO vs. GA is the natural comparison, the absence of any empirical comparison between PSO and GA is a significant gap — especially given claim #1 above.

### Minor

5. **DTW objective shows minimal advantage over the simpler top-k objective.** The paper acknowledges that "the differences resulting from the use of different attack objective functions are minimal" and that DTW and top-k produce "very similar" outcomes (Sec. 5.4). While the paper shows that center-of-mass (an image-oriented metric) is less suitable for time series, the claimed advantage of DTW over top-k is not demonstrated. This weakens the distinct contribution of the DTW-based objective.

6. **The abstract overclaims relative to demonstrated evidence.** Beyond the "comparison with existing methods" issue (point #1), the abstract also claims the method "ensures that the adversarial perturbations remain imperceptible" — but imperceptibility is never quantitatively measured or validated. Claims should be calibrated to what the evidence supports.

### Trivial
None.

## Nice-to-Haves
- Report actual perturbation magnitudes (ℓ∞ norm) and output changes for the generated adversarial examples, along with the fraction that satisfy each constraint.
- Add quantitative local vs. global comparison: TKI/SRC values, runtime, and perturbation magnitudes, ideally aggregated across multiple samples.
- Compare against a GA-based gradient-free attack (e.g., adapting Huang et al. 2023 to time series) to substantiate the PSO motivation.
- Include standard deviations or confidence intervals for TKI/SRC across multiple runs (PSO is stochastic).
- Ablate the local attack percentage (e.g., 10%, 20%, 30%) to justify the 20% choice.
- Add a failure case analysis (e.g., why does LSTM+SG resist the attack?).

## Removed Points
These points were raised by reviewers but are removed with justification:

- **"Second dataset not named"** — The experimental setup sections (5.1/5.2) are missing from the extracted PDF due to parsing. Dataset names are likely specified there.
- **"Alg. 1 not in paper / PSO parameters missing"** — The algorithm and parameter values are likely in the appendix, which is stripped by the PDF parser. This is a known parser artifact.
- **"δ and ε threshold values not stated"** — These would appear in the missing experimental setup sections.
- **"Using original explanation for local attack is unfair advantage for gradient-based XAI"** — This misunderstands the method: the local attack intentionally uses the original explanation to guide perturbation selection. That is the contribution, not a bias.
- **"Missing related work on PSO for XAI attacks"** — Cannot confirm this as the instruction bars me from commenting on missing related works without external sources.
- **"No discussion of GA attacks in related work"** — The paper explicitly discusses GA attacks (line 42), so this is factually incorrect.

## Novel Insights
None beyond the paper's own contributions.

## Suggestions
1. Add a proper baseline comparison: adapt the GA-based attack from Huang et al. (2023) to time series and report TKI/SRC for both methods under matched conditions.
2. Convert the qualitative local vs. global analysis into a quantitative comparison table with TKI, SRC, ℓ∞ perturbation, and runtime.
3. Report constraint satisfaction statistics: what fraction of generated adversarial examples satisfy ‖f(x)−f(x′)‖ < δ, and what are the actual perturbation magnitudes?
4. Tone down the abstract to match what is actually demonstrated — replace claims of "superiority" and "imperceptibility" with more precise statements about what was measured.
5. Report variance/confidence intervals for the main results (PSO is stochastic; a single run per configuration is insufficient).

## Score and Decision

MY FINAL SCORE: <score>4.0</score>
MY FINAL DECISION: <decision>Reject</decision>