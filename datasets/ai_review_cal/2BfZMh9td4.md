- Decision: Reject
- Avg Score: 4.25
- Scores: 5, 1, 6, 5
Now I have a thorough understanding of the paper and both reviews. Let me construct the final consolidated review.

---

## Summary

This paper introduces MODPO (Multi-Objective Direct Preference Optimization), an RL-free extension of DPO that aligns language models with multiple objectives (e.g., helpfulness, harmlessness) by integrating linear scalarization into the reward modeling step. Instead of training separate reward models and running MORLHF with PPO for each preference weighting, MODPO trains language models directly via a cross-entropy loss that incorporates margin rewards from other objectives. The authors prove theoretical equivalence to the MORLHF objective and demonstrate Pareto fronts on safety alignment and long-form QA tasks, reporting competitive or better performance with approximately 3× less computation.

## Strengths

1. **Theoretically grounded extension of DPO to multi-objective alignment.** Section 3.1 provides a clean derivation (culminating in Eq. 14) showing that the MODPO loss yields the exact optimal LM under the true collective rewards, matching the MORLHF objective with no RL. This is a principled and non-trivial extension of DPO that was not immediately obvious from prior work.

2. **Demonstrated computational advantage.** Table 1 quantifies the GPU-hour savings, and the argument in Section 3.2 (margin reward models trained once and amortized) makes clear why MODPO reduces per-LM cost to essentially that of single-stage DPO—approximately 3× less than MORLHF. This is a practically meaningful improvement.

3. **Consistent empirical results across multiple settings.** MODPO produces competitive Pareto fronts in synthetic safety alignment (Figure 2), real safety alignment evaluated via GPT-3/4 (Figure 4), and long-form QA where it "consistently surpasses MORLHF" (Figure 3). The results are directionally consistent: MODPO matches or beats MORLHF while costing less.

4. **Works with off-the-shelf multi-dimensional preference datasets.** The method operates directly on BEAVERTAILS (safety) and QA-FEEDBACK (long-form QA) without requiring new data collection, demonstrating practical applicability.

5. **Training stability retained from DPO.** Section 3.2 notes that the MODPO loss differs from DPO only by a weighting term and a margin, and the appendix shows similar monotonically increasing training accuracy—indicating that multi-objective training does not introduce the instability often seen in MORLHF.

## Weaknesses

### Fatal
None.

### Major

1. **No statistical significance or variance reporting.** The paper reports single runs for each method at each weighting $w$, with no confidence intervals, no error bars on the plotted fronts, and no mention of multiple random seeds. For MORLHF in particular, which is known to be sensitive to random seeds and hyperparameters, this makes it unclear whether observed differences (e.g., MODPO slightly better on helpfulness, MORLHF slightly better on harmlessness in Figure 2) are meaningful or are within the noise. The paper states "We execute multiple training runs for each method" but these are runs with different $w$ values, not replications. *(Lines 207–208)*

2. **Limited disclosure of MORLHF hyperparameter tuning.** The paper does not report the hyperparameter search space, tuning procedure, or budget used for the MORLHF (PPO) baseline. PPO is sensitive to learning rates, clipping parameters, and reward scaling; without evidence of fair tuning, the comparison risks reflecting an undertuned baseline rather than an inherent advantage of MODPO. *(Section 4.1)*

### Minor

3. **Long-form QA evaluation reuses the same reward models used in training (acknowledged).** The paper explicitly states that for long-form QA, it "directly reuse[s] $r_{\phi}$ trained on $\mathcal{D}$ as a proxy of $r^*$ to evaluate each front" and notes that "[t]his may lead to biased evaluation." The authors use a larger $\beta=0.5$ to partially mitigate over-optimization. While this is a real limitation, it applies equally to both MODPO and MORLHF, and MODPO is less directly optimizing the evaluation metric than MORLHF (which explicitly maximizes $\mathbf{w}^T\mathbf{r}_{\phi}$ via RL). The paper should be commended for flagging the issue rather than hiding it, but the concern about reward over-optimization is not fully resolved. *(Lines 200–201)*

4. **Absence of human evaluation for real-world preference alignment.** Given the paper's framing around "diverse human preferences," the lack of any human evaluation is a noticeable gap. The real safety evaluation uses GPT-3/4 as proxies, which is a reasonable community standard but falls short of directly validating that the Pareto front translates to actual user satisfaction across different preference groups. *(Lines 200–201)*

5. **Two-objective demonstrations only.** The paper focuses on two objectives ($n=2$) and only mentions in passing that MODPO "scales effectively" to more objectives without showing any results. Given that prior MORLHF work (Rame et al., 2023; Wu et al., 2023) demonstrates three or more dimensions, a simple three-objective example would substantially strengthen the generality claim. *(Line 185)*

6. **Brief limitations section.** Section 6 (Discussion) is very short and does not touch on the evaluation-bias concern, the sensitivity of MODPO to margin reward model quality, or the need for human evaluation. This understates the paper's known limitations. *(Section 6)*

### Trivial
None.

## Nice-to-Haves

- **Analyze the effect of margin reward model error.** The theoretical guarantee (Eq. 14 produces the exact optimal LM) depends on having perfect margin reward models $r_{-k}^*$; the paper replaces these with estimates $r_{\phi,-k}$ but does not study how degradation in margin model quality affects the final LM front. An ablation varying the size or quality of the margin reward model would clarify practical robustness.
- **Ablation on which dataset is used as $\mathcal{D}_k$.** The paper always uses $\mathcal{D}_2$ (overall preference) as the MODPO training dataset and the other objective's reward as margin. Reversing the roles could reveal asymmetries.
- **Three-objective demonstration.** Even one additional objective would significantly strengthen the claim of scalability.

## Removed Points

- **"Evaluation invalidity for long-form QA is a structural flaw."** Removed because: (1) the paper explicitly acknowledges the bias and uses $\beta=0.5$ to mitigate it; (2) the same reward models are used to evaluate BOTH MODPO and MORLHF, so the relative comparison is fair; (3) MODPO's training uses $r_{\phi,1}$ only as a margin, whereas MORLHF directly maximizes $\mathbf{w}^T\mathbf{r}_{\phi}$ in RL—so if anything, MORLHF is more directly exploiting the evaluation metric; (4) the critic's analogy to Best-of-$n$ (an unfair oracle for using reward models at inference time) does not apply to training-time use of reward models. The concern is real but correctly classified as **Minor** above.

- **"Synthetic safety evaluation is too controlled."** Removed as a standalone fatal point. The paper explicitly labels this a "well-controlled generation setting" following the standard protocol of Rafailov et al. (2023), and it also provides a **real** safety evaluation with GPT-3/4 (Figure 4) that validates the synthetic findings. The synthetic setting tests whether the optimization procedure works correctly—a standard practice.

- **"Untested post hoc hypotheses in Section 4.2."** Removed because these are exploratory explanations of observed results (e.g., why MODPO is better on helpfulness), not core claims. Speculative reasoning about observations is normal in experimental sections.

- **"Scalability beyond two objectives as a strength."** Removed from Strengths because the paper only says "we also explore MODPO with more than two objectives and found it scales effectively" without showing any results. This is a claim without evidence and cannot be counted as a demonstrated strength.

- **Various formatting/style nitpicks and missing appendix complaints.** Removed per parsing-artifact policy.

## Novel Insights

None beyond the paper's own contributions. The reviews do not surface any observation about the paper that is not already present or implied in the paper itself.

## Suggestions

1. **Add multiple random seeds with error bars** to at least the main experimental comparisons (Figures 2–4). This is the single highest-leverage improvement for establishing the reliability of the claims.
2. **Document the MORLHF hyperparameter search** (search space, tuning budget, final hyperparameters) or, better, release the tuning code to demonstrate fair comparison.
3. **Add a small-scale human evaluation** for at least one task (e.g., safety alignment with diverse labelers) to directly test whether the Pareto front translates to real user satisfaction.
4. **Run an ablation varying the quality of the margin reward model** (e.g., using different data fractions or smaller model sizes) to examine how degradation affects the final LM front.
5. **Provide at least one three-objective example** to substantiate the scalability claim beyond pairwise interpolation.
