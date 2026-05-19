- Decision: Accept
- Avg Score: 6.00
- Scores: 5, 8, 5
Now I have a thorough understanding of the paper and can verify all reviewer claims against the source text. Let me produce the final consolidated review.

---

## Summary

This paper introduces the problem of attributing *global* properties (e.g., Inception Score, demographic diversity entropy, aesthetic percentile) of diffusion models to *data contributors* (rather than individual data points). The authors propose an efficient Shapley-value-based framework that uses magnitude pruning followed by subset fine-tuning (sparsified fine-tuning) to approximate the prohibitively expensive retraining needed for Shapley estimation. Experiments across three settings—DDPM on CIFAR-20, LDM on CelebA-HQ, and Stable Diffusion LoRA on ArtBench—show that sparsified-FT Shapley substantially outperforms existing attribution methods such as D-TRAK and Journey-TRAK in terms of Linear Datamodeling Score (LDS) and counterfactual validity.

## Strengths

1. **Novel and well-motivated problem formulation.** The paper is the first to explicitly target *global* property attribution to *data contributors* for diffusion models, identifying two gaps in prior work (local vs. global, datum vs. contributor) that are clearly scoped in Section 1. This is a genuinely new problem framing with practical relevance to data compensation and incentive design.

2. **Efficient computational trick with significant speedups.** The sparsified fine-tuning approach (prune → full-dataset fine-tune → subset fine-tune) reduces runtime by 5.3×, 10.4×, and 18.6× relative to full retraining on the three datasets (Table 2). Figure 2 further shows that under equal compute budgets, sparsified-FT Shapley achieves higher LDS than existing methods.

3. **State-of-the-art attribution accuracy across all three benchmarks.** Table 1 reports that sparsified-FT Shapley achieves the highest LDS in all settings: 61.48% on CIFAR-20 (vs. next best 30.66%), 26.34% on CelebA-HQ (vs. next best 6.70%), and 61.44% on ArtBench (vs. next best 22.64%). The improvement over baselines on CIFAR-20 and ArtBench is large and consistent across random initializations.

4. **Counterfactual validation supports the attributions.** Removing the top 40% of contributors identified by sparsified-FT Shapley causes larger drops in global properties than all baselines on CIFAR-20 (−23.23% vs. −14.95%) and CelebA-HQ (−7.83% vs. −6.64%). Retaining only top 60% of contributors yields similarly larger improvements on those datasets.

5. **Generality across models, properties, and contributor counts.** The method is evaluated on three different architectures (DDPM, LDM, Stable Diffusion LoRA), three distinct global properties (Inception Score, demographic entropy, aesthetic percentile), and varying numbers of contributors (20, 50, 258), demonstrating broad applicability (Section 4.2, Table 1).

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

1. **No direct empirical validation of the sparsified approximation (Equation 6).** The paper claims that sparsified fine-tuning approximates full retraining ($\mathcal{F}(\tilde{\theta}^{\mathrm{ft}}_{S,k}) \approx \mathcal{F}(\theta^*_S)$), and Propositions 1–2 provide asymptotic theoretical motivation for this claim. However, the experiments never directly compare $\mathcal{F}(\tilde{\theta}^{\mathrm{ft}}_{S,k})$ against $\mathcal{F}(\theta^*_S)$ for the same subsets. The LDS metric tests whether *final attribution scores* predict held-out model properties, which is an end-to-end validation but does not isolate the fidelity of the approximation itself. A positive LDS could arise from a consistent bias that preserves relative rankings. Directly reporting correlation or absolute error between $\mathcal{F}(\tilde{\theta}^{\mathrm{ft}}_{S,k})$ and $\mathcal{F}(\theta^*_S)$ for even a small number of subsets (e.g., 20–50) would substantially strengthen the empirical foundation for the method's central design choice.

2. **Small counterfactual effect on ArtBench without adequate discussion.** On ArtBench (Post-Impressionism), removing the top 40% of contributors changes the aesthetic score by only −1.86% for sparsified-FT Shapley (with other baselines near zero). The LDS for ArtBench is excellent (61.44%), so the method ranks contributors well—but the tiny absolute effect raises an interpretive question that the paper does not address. Is the aesthetic property inherently insensitive to individual artist identity? Is the 90th-percentile-aesthetic metric low-variance across artists? The paper should at minimum discuss why the effect is small and what this implies about the method's utility in settings where global properties are not contributor-dominated.

3. **No sensitivity analysis for pruning ratio or fine-tuning steps.** The paper reports a single pruning ratio and fine-tuning step count per dataset (0.3 ratio and 1000 steps for CIFAR-20; 0.5 and 500/200 for the others) without any ablation or sensitivity study. Practitioners cannot tell whether these choices are critical or whether the method degrades gracefully with different ratios. A brief sensitivity analysis on at least one dataset would be valuable.

4. **No comparison to non-sparsified FT Shapley under equal compute.** The paper shows that sparsified-FT Shapley outperforms existing non-Shapley methods (Figure 2), but does not compare against a Shapley estimator using *full* fine-tuning (no pruning) under a matched compute budget. Such a comparison would isolate whether pruning is beneficial for attribution quality or merely a cost-saving measure. This is not a critical omission, but it would cleanly separate the contribution of the Shapley framework from the contribution of the sparsification trick.

### Trivial

None of note. The paper is generally well-written.

## Nice-to-Haves

- Directly compare $\mathcal{F}(\tilde{\theta}^{\mathrm{ft}}_{S,k})$ vs. $\mathcal{F}(\theta^*_S)$ for a sample of subsets and report Spearman correlation and MAE, bridging the gap between theory and experiment.
- Run an ablation on CIFAR-20 varying the pruning ratio (e.g., 0.1, 0.3, 0.5, 0.7) and fine-tuning steps to show sensitivity.
- Discuss why the ArtBench counterfactual changes are so small, even though the LDS is high—this would clarify the boundary conditions of the method.
- Report the LDS results for α=0.25 and 0.75 (mentioned as evaluated but only α=0.5 appears in the main table).

## Removed Points

The following points from the input reviews were removed per the filtering rules, with brief justification:

- **Theoretical justification relies on strong assumptions (Harsh Critic, Critical Issue #2):** The paper clearly states that Propositions 1–2 are "asymptotic results" and explicitly acknowledges the limitations ("we leave theoretical results incorporating finite-step bounds and Shapley value estimation for future work"). The assumptions (convexity, Lipschitz gradients, lottery ticket hypothesis) are cited as standard in prior work (Golatkar et al., 2020; Georgiev et al., 2024). The theory is transparently presented as motivation. This criticism overstates the paper's claims and ignores its own caveats.
- **Parser-artifact notation issues in Propositions 1 and 2 (ħ, μ symbols):** These are manifestly PDF-parser artifacts that do not exist in the original submission.
- **Only α=0.5 reported in main table:** The paper states that α=0.25, 0.5, 0.75 were evaluated; the appendix (stripped by parser) likely contains the full results. Per the hard rule, missing appendix content cannot be penalized.
- **Missing related work:** Per the rule, I cannot penalize missing related work without external knowledge.
- **Formatting/style nitpicks and reproducibility nitpicks about undisclosed hyperparameters for trivial components:** Removed per hard rules.
- **Several strengths from the Strength Finder that were generic or sycophantic:** All retained strengths were grounded in specific experimental evidence; none were removed.

## Novel Insights

The most interesting tension surfaced by the reviews is between the *ranking quality* (LDS) and the *practical impact* (counterfactual change magnitude) on ArtBench. The method achieves 61.44% LDS—meaning it orders contributors well—yet removing the top 40% of contributors changes the aesthetic score by only −1.86%. This decoupling suggests that sparsified-FT Shapley can identify the *correct ordering* even when the global property being attributed has inherently low variance across contributors. This is worth noting because it implies the method may work well for ranking even in settings where the absolute magnitude of contribution is small. The reviews did not articulate this distinction explicitly; it emerges from juxtaposing the LDS and counterfactual results.

## Suggestions

1. **Add a direct validation experiment** comparing $\mathcal{F}(\tilde{\theta}^{\mathrm{ft}}_{S,k})$ vs. $\mathcal{F}(\theta^*_S)$ for 20–50 subsets across datasets. Report Spearman correlation and mean absolute error. This single addition would directly test the core approximation claim (Equation 6) and close the largest evidential gap.

2. **Include a sensitivity ablation** on CIFAR-20 (cheapest to run) varying pruning ratio (e.g., 0.1, 0.3, 0.5, 0.7) and fine-tuning steps, reporting LDS for each setting. This would help practitioners understand robustness and guide hyperparameter choice.

3. **Discuss the ArtBench counterfactual results** explicitly. Explain whether the small magnitude is due to the property function (90th percentile aesthetic score), the nature of the artists' contributions, or something else. If the method still identifies the correct *ranking* (as LDS attests), state this clearly to set appropriate expectations.
