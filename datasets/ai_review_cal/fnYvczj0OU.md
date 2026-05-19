- Decision: Reject
- Avg Score: 4.33
- Scores: 5, 3, 5
Now I have a thorough understanding of the paper. Let me produce the final consolidated review.

## Summary

The paper introduces Equal Long-term Benefit Rate (ELBERT), a long-term fairness notion for sequential decision-making that measures group well-being as the ratio of cumulative group supply to cumulative group demand. This avoids the "false sense of fairness" problem in prior metrics that naively sum step-wise biases or cumulative rewards without accounting for varying temporal importance across time steps. The paper's key theoretical contribution is showing that the policy gradient of this ratio-based objective can be reduced to a standard policy gradient with a fairness-aware advantage function, making existing RL algorithms (e.g., PPO) directly applicable for bias mitigation. Experiments across three sequential decision-making environments (lending, infectious disease control, attention allocation) show that ELBERT-PO achieves the lowest bias among compared methods while maintaining competitive reward.

## Strengths

- **Clear identification of a genuine limitation in prior long-term fairness metrics.** The Figure 1 loan-approval example is compelling and concrete: prior metrics return zero bias despite group blue receiving a 100/101 acceptance rate and group red 1/101, because they ignore that time steps differ in demand. ELBERT correctly captures the bias as |1/101 − 100/101|. This is not a strawman — the paper explicitly shows how both the sum-of-stepwise-bias (Yin et al., 2023) and cumulative-reward-difference (Chi et al., 2021; Wen et al., 2021) metrics yield zero on this example.

- **Principled theoretical reduction to standard policy gradients (Propositions 3.1 and 3.2).** The paper analytically derives that the gradient of the ELBERT objective equals the standard policy gradient with a fairness-aware advantage function. This is a non-trivial result — ratio-based objectives do not fit the standard cumulative-reward form, and computing their policy gradient was previously unclear. The reduction means existing RL libraries and algorithms (e.g., PPO) can be used directly for bias mitigation, which significantly lowers the barrier to adoption.

- **General framework adaptable to multiple static fairness notions.** Section 5.1 demonstrates that three different fairness criteria used in prior work (Equal Opportunity for lending, vaccination ratio for disease control, discovery ratio for attention allocation) are all special cases of ELBERT via customization of group supply and demand functions. This adaptivity goes beyond prior work that defined only fixed long-term metrics.

- **Consistent empirical reductions in bias.** Across all three environments, ELBERT-PO achieves the lowest bias values (0.02 lending, 0.01 infectious disease, ~0.005 attention allocation) while maintaining reward competitive with or exceeding baselines. In the lending environment, bias is reduced by 87.5% compared to the greedy G-PPO baseline.

## Weaknesses

### Fatal
None.

### Major

- **Lack of statistical rigor in experimental evaluation.** No error bars, confidence intervals, or mention of multiple random seeds are present in the reported results (Figures 3 and 4). RL experiments are notoriously stochastic, and single-run results make it impossible to assess whether observed differences between methods are meaningful or due to noise. The paper makes strong empirical claims ("consistently achieves the lowest bias") that are not fully supported without information about variance. This weakens the empirical validation of an otherwise sound theoretical contribution.

### Minor

- **Multi-group solution not specified in the main text.** Section 3.3 identifies the non-smoothness caused by the max/min operator in multi-group bias but does not provide a concrete, reproducible solution. The 5-group attention allocation experiments use this multi-group setting, yet the reader cannot verify what algorithmic approach was taken (softmax/softmin smoothing, top-k averaging, or something else). The solution details are presumably deferred to the appendix (which is stripped from this PDF extraction), but the main text is incomplete on a point that is central to one of the three experimental environments.

- **Estimation of η_g^D(π) and η_g^S(π) is underspecified.** Proposition 3.2's fairness-aware advantage function requires estimates of the expected total supply and demand under the current policy. The paper states that "one only needs to estimate" these quantities (line 73) but does not explain how they are computed during training (e.g., running averages, separate critics, trajectory-level Monte Carlo). While this can be addressed in a few sentences, its absence is a reproducibility gap — a practitioner implementing the method would not know a standard or recommended estimation strategy.

- **Modifications to environment settings not described.** The paper states it modifies the infectious disease and attention allocation environments "to be more challenging" but does not specify how. This makes comparisons to results from prior work on the same environments not directly interpretable.

### Trivial
None.

## Nice-to-Haves

- **Add a direct test of the "false sense of fairness" claim.** The paper's motivating example (Figure 1) is clean and conceptual. A controlled experiment where a method optimizing a flawed metric (e.g., sum-of-stepwise-biases) demonstrably fails while ELBERT-PO succeeds — on a simple 2-state environment matching the Figure 1 scenario — would directly validate the paper's central motivation and make the empirical case much stronger.

- **Include a baseline that optimizes one of the criticized prior metrics.** While the paper compares against A-PPO (a fairness-aware RL method from prior work) and reasonable heuristics (G-PPO, R-PPO), demonstrating that a method explicitly optimizing a flawed metric (e.g., sum of step-wise biases or return parity) underperforms ELBERT-PO on the same environments would further isolate the value of the ELBERT formulation itself.

- **Discuss potential gradient instability.** The fairness-aware advantage function involves terms with η_g^D(π) in the denominator; when group demand is very small, the gradient could become arbitrarily large. A brief discussion of whether clipping or normalization is needed would be helpful.

## Removed Points

- **Baseline comparison supposedly unfair** (Harsh Critic #3: "Baseline selection creates a weak comparison.") — Removed because the paper compares against A-PPO (a published fairness-aware RL method) and reasonable baselines (G-PPO, R-PPO). The claim that the paper "does not compare ELBERT-PO against methods that optimize those metrics (e.g., from Wen et al. 2021, Yin et al. 2023)" overstates the requirement: Wen et al. and Yin et al. define fairness metrics, not training algorithms, and implementing them as training objectives would require non-trivial new method design. The existing comparisons are adequate for the central claims.

- **Criticisms about missing appendix content, missing proofs, format/style nitpicks** — Removed per hard rules (parser strips appendices from all papers; formatting artifacts are parser errors, not author errors).

- **Strength Finder's generic strengths** (e.g., "addresses an important problem") — Removed per filtering rules. Strengths kept only when specific and evidence-backed.

- **"The ablation with varying α... is puzzling"** — Removed because the paper's explanation is coherent: larger α reduces bias but slows convergence, and the observation that fairness may help reward is a reasonable (if tentative) observation, not a flaw.

## Novel Insights

None beyond the paper's own contributions. The theoretical reduction of ratio-based fairness objectives to standard policy gradients is the paper's primary novel insight.

## Suggestions

1. **Report results from at least 5 random seeds** with shaded confidence intervals or box plots for all main results (Figures 3 and 4). This is standard practice for RL experiments and would significantly strengthen the empirical claims.

2. **Add a few sentences to Section 3.2 explaining how η_g^D(π) and η_g^S(π) are estimated in practice** (e.g., "we maintain running averages of the cumulative supply and demand over recent trajectories" or "we learn value functions for supply and demand using TD learning").

3. **Complete Section 3.3 with the concrete multi-group solution used in experiments** — specify whether softmax/softmin smoothing, top-k averaging, or another approach was used, and ideally provide an ablation comparing approaches.

4. **Describe the environment modifications** (or refer to the appendix where they are described) so readers can compare against prior work.

5. **Consider adding a simple 2-state experiment** (like the Figure 1 example) where the "false sense of fairness" is directly demonstrated and ELBERT-PO corrects it while a method based on prior metrics fails.
