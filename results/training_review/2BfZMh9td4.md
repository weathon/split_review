Now I have a thorough understanding of the paper and can verify the reviewer's claims directly. Let me write the consolidated review.

## Summary

This paper proposes Multi-Objective Direct Preference Optimization (MODPO), an RL-free extension of DPO for multi-objective LM alignment. The key idea is to fold linear scalarization of multiple reward objectives into the DPO-style loss by using a pre-trained margin reward model for auxiliary objectives while training the policy on a primary preference dataset. The method is theoretically motivated (analytically equivalent to MORLHF under exact margin rewards) and empirically evaluated on safety alignment and long-form QA tasks. MODPO demonstrates competitive or superior Pareto fronts compared to MORLHF while requiring ~3× less GPU time.

## Strengths

- **Theoretically grounded derivation:** The paper derives the MODPO loss (Eq. 14) from the KL-constrained multi-objective reward maximization objective (Eq. 7) using the same analytical mapping that DPO uses for single-objective alignment. Under exact margin rewards, MODPO produces the same optimal policy as MORLHF without requiring reinforcement learning (Section 3.1, Eq. 10–14). This is a clean and principled theoretical contribution.

- **Demonstrated computational efficiency:** MODPO requires roughly 3× less GPU time than MORLHF per LM (Table 1: 0.5 vs. 1.5 GPU hours), with margin reward models trained once and amortized across all preference weightings. This directly supports the paper's claim of being a practically more efficient alternative.

- **Versatility across tasks and feedback types:** MODPO works with both pairwise preference datasets (BEAVERTAILS for safety alignment) and meta-labeled datasets (QA-FEEDBACK for long-form QA). The method handles multiple objective combinations and is shown to work with both synthetic and real human feedback (Sections 4.1–4.2).

- **Clean Pareto fronts:** Across multiple settings (synthetic safety alignment with two β regimes, real safety alignment evaluated by GPT-3/4, and three long-form QA objective combinations), MODPO produces Pareto-optimal fronts that are at least competitive with and often better than MORLHF (Figures 2, 3, 4).

## Weaknesses

### Fatal
None.

### Major

- **MODPO loss is undefined at w=0, yet w=0.0 datapoints are plotted.** The MODPO loss (Eq. 14, line 155) contains the factor \(1/w_k\). In the two-objective experiments, \(\mathbf{w}=[1-w, w]\), \(\mathcal{D}_k = \mathcal{D}_2\), so \(w_k = w\). At \(w=0\), the loss is undefined due to division by zero. The paper reports \(w \in \{0.0, 0.2, 0.4, 0.6, 0.8, 1.0\}\) (line 207) and annotates datapoints with \(w=0.0\) on the figures. The paper never explains how this endpoint is handled. If DPO on \(\mathcal{D}_1\) is used instead, the front is not produced by a single consistent method; if a numerical kludge is used, this should be stated. Either way, the claimed continuous interpolation via MODPO is not clearly substantiated at the endpoints. This is a significant methodological gap, though the core method for \(w \in (0,1)\) remains valid.

- **No statistical uncertainty reported for any experiment.** All results are presented as single trajectories per \((w, \beta)\) configuration without error bars, confidence intervals, or multiple seeds. DPO training is sensitive to random seeds, batch ordering, and early stopping; MODPO adds additional dependencies on the estimated margin reward model. The observed differences between MODPO and MORLHF are sometimes small (e.g., Figure 2, where fronts cross), and without variance estimates it is impossible to assess whether these differences are robust or within the noise. This weakens the headline claim that MODPO "consistently yields one of the best LM fronts."

- **Long-form QA evaluation reuses reward models used in training.** For long-form QA, the same reward models \(\mathbf{r}_\phi\) that guide MODPO's margin term and MORLHF's reward signal are also used as the evaluation proxy for ground-truth rewards (lines 200–201). The paper acknowledges this ("may lead to biased evaluation") and uses a higher \(\beta=0.5\) to mitigate over-optimization. However, this asymmetry affects MODPO more than MORLHF: MODPO's loss explicitly includes the margin reward model \(r_{\phi,1}\) as a direct additive term, creating a tighter coupling to the evaluation metric. While the paper's corrective measure is reasonable, the evaluation still falls short of ideal standards (held-out reward models, human evaluation, or alternative architectures). The consistent MODPO > MORLHF result in Figure 3 should therefore be interpreted with caution.

### Minor

- **No sensitivity analysis for the choice of \(k\).** The paper sets \(k=2\) (using \(\mathcal{D}_2\) as the primary preference dataset and \(\mathcal{D}_1\) as the margin) without testing whether swapping the roles changes the Pareto fronts (lines 189–190). The derivation is symmetric, but empirical verification would strengthen the results.

- **Optimal policy claim conflates theory and practice.** The abstract states that "the LMs optimized against the MODPO objective are analytically the exact solutions" of the MORLHF objective. This is only true when the margin reward models \(r_{\phi,-k}\) are exact. In practice, they are estimated, so the theoretical guarantee does not strictly hold. The derivation (line 158) notes this indirectly ("under the true collective rewards"), but the main text could more clearly separate the ideal theoretical claim from the practical approximation.

- **MORLHF implementation details are underspecified.** The paper does not state which RL algorithm (e.g., PPO) was used for the MORLHF baselines, nor does it report key hyperparameters (KL penalty coefficient, number of PPO steps, etc.). This makes reproducibility harder and raises the question of whether MORLHF was well-tuned.

- **"By far the best" overstates the visual evidence in Figure 2.** In the synthetic safety alignment results, MODPO's fronts cross MORLHF's (MODPO better on helpfulness, MORLHF slightly better on harmlessness). The paper's own description (line 212–213) acknowledges this: "MODPO is generally better on the helpful dimension, MORLHF is slightly better on the harmless dimension." The claim of "by far the best" front is not supported by the evidence presented.

- **Best-of-\(n\) selection for \(\beta=0.1\) is ad hoc.** For \(\beta=0.1\), the paper uses "the largest \(n\) we can afford" (128) rather than the KL-matched formula used for \(\beta=0.5\). This inconsistent treatment weakens the Best-of-\(n\) baseline comparison for that setting.

### Trivial

- The phrase "This may lead to biased evaluation" (line 201) is a run-on sentence missing a connecting clause, but this is a parser artifact.

## Nice-to-Haves

- **Multi-objective scalability experiments.** The paper mentions exploring more than two objectives but provides no results. An experiment with 3+ objectives (e.g., helpfulness, harmlessness, and honesty) would strengthen claims of scalability.
- **Ablation on margin reward model quality.** Training MODPO with an oracle margin reward (via synthetic data where true \(r^*_{-k}\) is known) versus estimated margin would clarify how approximation error propagates.
- **Comparison with reward-model merging.** Comparing MODPO to approaches that interpolate reward model weights before DPO training would help isolate the benefit of MODPO's training-time integration.

## Removed Points

These points were identified in the provided reviews but are removed or downgraded for the following reasons:

- **"Circular evaluation invalidates claimed superiority" (as fatal weakness):** The paper acknowledges the issue and uses both a higher β and, for the safety alignment task, orthogonal GPT-3/4 evaluation. Both MODPO and MORLHF use the same reward models for training and evaluation, so any bias is symmetric across methods. This concern is legitimate but not fatal; it is already placed under Major.

- **"MODPO loss is undefined at w=0 invalidates core claims":** While the w=0 issue is real, it only affects the single endpoint datapoint. The core method for \(w\in(0,1)\) is well-defined and the derivation is sound. This is a significant oversight but does not "invalidate" the paper's central contribution; it is placed under Major.

- **"Out-of-distribution evaluation of margin models on preference pairs from D_k":** The reviewer speculates this could be an issue but provides no evidence it actually occurred. The paper does not need to preemptively address every hypothetical distribution shift without evidence.

- **"Missing appendix/proofs":** The parser strips these sections; they exist in the original submission.

- **"Related work gaps":** As per instructions, missing related works are not included since external sources cannot confirm their existence.

- **"Speculative explanation for DPO LW being worse":** The paper's hypothesis about multi-stage vs. concurrent training is clearly flagged as a hypothesis ("partially because... potentially impeding learning"). This is reasonable analysis, not a weakness.

- **"Excluding suboptimal checkpoints could inflate fronts":** This is standard Pareto front visualization — only Pareto-optimal points are shown. The paper describes the procedure transparently (line 207).

- **"Formatting/style nitpicks":** Removed as per instructions.

## Novel Insights

None beyond the paper's own contributions. The reviews do not surface a genuinely novel observation about the method or problem that the authors themselves did not already articulate.

## Suggestions

1. **Clarify endpoint handling.** Explicitly state how \(w=0\) and \(w=1\) are treated (e.g., using standard DPO on the relevant single-objective dataset). If a small epsilon is used numerically, report the value.
2. **Add error bars.** Report results from at least 3 random seeds with mean ± std for key metrics (rewards, KL) to establish significance.
3. **Provide held-out evaluation for long-form QA.** Use GPT-4 evaluation or a separate set of reward models with different architectures for at least a subset of the long-form QA conditions to break the circularity.
4. **Swap \(k\) in one experiment.** Repeat the safety alignment experiment with \(k=1\) (using helpfulness as the primary dataset and harmlessness as margin) to demonstrate symmetry.
5. **Tone down "by far the best" language.** The empirical results show MODPO is competitive or slightly better in most settings; the language should match the evidence.

## Score and Decision

This paper makes a clean, principled contribution: extending DPO to multi-objective alignment by integrating linear scalarization into the DPO loss with a margin reward model. The theoretical derivation is sound, the computational savings are concrete, and the experimental results are generally supportive. However, the experimental validation has notable gaps — the undefined loss at the w=0 endpoint, absence of any statistical uncertainty quantification, and the partially circular long-form QA evaluation — that collectively prevent the paper from strongly establishing its empirical claims. These are addressable weaknesses (they do not undermine the theoretical contribution), but they are real and should be fixed. The paper falls in the "weak accept / borderline" range.

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>