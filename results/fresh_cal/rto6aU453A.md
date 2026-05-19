Now I have a thorough understanding of the paper. Let me compose the final consolidated review.

## Summary

This paper addresses high-dimensional action selection in online deep RL. It defines sufficient and minimal sufficient action sets, then proposes a knockoff-sampling (KS) method that uses the policy's own diagonal Gaussian distribution to generate exact knockoff features — bypassing the usual challenge of constructing knockoffs from unknown distributions. The method is integrated into deep RL via a binary hard mask on the Q-function and policy log-probability, avoiding model reinitialization. Theoretical guarantees show modified FDR control under stationarity and exponential β-mixing, and experiments on MuJoCo locomotion tasks and a MIMIC-III sepsis treatment allocation task demonstrate that KS consistently outperforms using all actions and closely approaches the performance of using ground-truth actions.

## Strengths

- **Exact knockoff features generated from the policy network (Section 3.2, Algorithm 2)**. The paper exploits that in online RL with diagonal Gaussian policies, the conditional distribution of actions given states is known and can be directly re-sampled. This bypasses the central challenge of model-X knockoffs — constructing faithful knockoff features without knowing the full covariate distribution — and is a genuinely novel and elegant adaptation of the knockoff framework to the RL setting.

- **Theoretical FDR control under dependent, temporally-correlated data (Theorem 4.3, Section 4)**. The paper proves that the proposed KS method, combined with sample splitting and majority vote, controls the modified FDR to within α plus a vanishing term under stationary exponential β-mixing conditions, which is stronger than what typical threshold-based variable selection methods provide and is a principled contribution to the action-selection literature in RL.

- **Practical hard-mask integration (Section 3.1, Algorithm 1, Equations 3–4)**. The binary mask mechanism zeros out non-selected actions in the Q-function input and the policy log-probability while blocking gradients during backpropagation, allowing seamless integration of variable selection into existing deep RL pipelines without reinitializing the network. This is computationally lightweight (the paper reports under 20 seconds for selection) and algorithm-agnostic.

- **Empirical validation on a real-world medical task (Table 2, Figure 5)**. The treatment allocation experiment on MIMIC-III sepsis data shows KS consistently achieving the highest reward with lower variance compared to exploration-focused baselines (Lattice, gSDE), demonstrating practical applicability beyond simulated robotics.

## Weaknesses

### Fatal
None.

### Major

- **Theory–practice gap: stationarity assumption does not match the online training setting.**  
  Theorem 4.3 and Definition 4.2 assume that the process $\{(\mathbf{S}_t,\mathbf{A}_t,R_t)\}_{t\ge 0}$ is **stationary and exponentially β-mixing**, which requires a fixed policy $\pi$ that does not change over time. However, the method is applied during online RL training (first 4,000–10,000 steps in experiments, line 178), where the policy is updated every few steps and the data distribution shifts. The paper acknowledges focusing on "stationary environments" (line 75), but this refers to environment dynamics, not the action distribution. The theory as stated does not cover the usage scenario, and the paper does not discuss whether the guarantees degrade gracefully under non-stationarity or clarify that the theory applies to a fixed-policy data collection scenario while the experiments demonstrate empirical robustness. This is a structural gap between theoretical claims and empirical practice.

### Minor

- **The variable-selection (VS) baseline in Figure 2 is not described.**  
  Figure 2 shows learning curves comparing KS against "traditional Variable Selection (VS)" and claims KS outperforms VS, but the paper never specifies what VS method was used (LASSO with threshold? t-statistic selection? something else?), does not report FDR/TPR/FPR values for VS in tables, and does not provide standard errors for the comparison. The VS comparison is used to motivate the need for FDR control, but without specifying the method and providing numerical results, the comparison cannot be assessed or reproduced.

- **Nature of artificially added redundant actions in MuJoCo is unspecified.**  
  The paper states it "artificially add[s] extra $p$ actions to the raw action space" (line 176) but never describes what these extra actions are — independent random noise, linear combinations of existing actions, constant zeros, or something else. The difficulty of selection and the interpretability of FDR/TPR/FPR results depend on this choice, and omitting it makes the experimental design opaque.

- **Standard deviations / confidence intervals not reported for main MuJoCo results.**  
  Table 1 reports final rewards for PPO and SAC across three tasks and two added-dimension scenarios averaged over 10 runs, but does not include any measure of variance. For several entries (e.g., Ant $p=20$ with PPO: KS 1891 vs All 1871), the margins are small, and without standard deviations or confidence intervals it is impossible to assess whether the differences are statistically significant. (Table 2 for the medical task does report Std, which is good.)

- **Number of sample splits $K$ used in experiments is not reported.**  
  The theory specifies $K = k_0 \log(NT)$ (line 157) and the method description (Algorithm 2) requires $K$, but the experiments section (line 174) does not state what $K$ value was used. This parameter affects both the practical behavior of majority voting and the validity of the theoretical guarantee.

- **The paper mentions "Supporting Analyses" for variation of action distributions during training (line 194) but defers the content to the appendix**, which is not available in this version. If these analyses are important for understanding the method's behavior (e.g., whether the policy's action distribution over irrelevant dimensions collapses after masking), they should be summarized in the main text.

### Trivial
None.

## Nice-to-Haves

- An ablation study comparing the mask mechanism against reinitializing a new network on the selected action dimensions would strengthen the claim that masking is more efficient than reinitialization.
- If the theoretical scope were clarified — e.g., stating explicitly that the theory covers offline data collected under a fixed policy, while the experiments test online robustness — the paper's contributions would be more cleanly separated.
- A sensitivity analysis with different types of added actions (independent noise, correlated noise, constant values) would make the experimental story more robust.

## Removed Points

- **Stationarity of process vs. stationarity of environment (from Harsh Critic's "Shared network layers" and "splitting modulo justification" concerns)**: The paper already addresses the gradient blocking property for the mask (line 87: "it will block the gradient when doing backpropagation") and provides justification for the modulo-K splitting via β-mixing literature (lines 129–130). These criticisms are based on misreading or are already addressed in the paper.

- **"Proof is only sketched; the appendix is not available"**: Removed per hard rule — the parser strips appendix sections from all papers; they exist in the original submission.

- **"Variation of action distributions during training mentioned but no results shown"**: Removed per hard rule — this content is in the appendix which was stripped by the parser.

- **"Shared network layers and mask" concern**: The paper explicitly states the mask "will block the gradient when doing backpropagation" (line 87), which addresses the concern about network parameters drifting through shared representations. Removed as already addressed.

- **Missing related works review**: Removed per hard rule — the reviewer should not speculate about missing references without external sources.

- **Generic strengths from Strength Finder**: Several generic strengths ("addressed an important problem," "targeted an interesting question") removed as lacking concrete evidence specific to the paper.

## Novel Insights

None beyond the paper's own contributions. The two reviewer reports largely converge on the same key points (theory-practice gap, need for clearer baselines, missing experimental details), with no truly novel observation that the paper itself does not surface.

## Suggestions

1. **Clarify the scope of the theory.** Either (a) add a remark that the theory applies to data collected under a fixed behavior policy, and the online experiments demonstrate empirical robustness beyond the theoretical scope, or (b) derive a more general bound that accounts for slowly-changing policies. Most reviewers will accept (a) as an honest scoping.

2. **Specify the VS method used in Figure 2** and add FDR/TPR/FPR values for it to the tables or a supplementary table. Without this, the claimed advantage over traditional VS is unverifiable.

3. **Describe the construction of the artificially added actions** in MuJoCo (e.g., "i.i.d. $\mathcal{N}(0,1)$ independent of states and rewards").

4. **Add standard deviations or confidence intervals to Table 1** for the MuJoCo results, and report the number of sample splits $K$ used.

5. **Move the supporting analyses summary into the main text** if they show meaningful insights (e.g., whether action distributions over irrelevant dimensions collapse after masking).

## Score and Decision

This paper tackles a relevant problem with a clever and novel method (using the policy's own distribution to construct exact knockoffs), provides theoretical FDR guarantees, and validates the approach on both simulated and real-world tasks. The main weakness is the gap between the stationarity assumption in the theory and the online training setting in the experiments — a common issue in RL theory papers that is addressable by clarifying the scope. The missing experimental details (nature of added actions, VS baseline specification, standard deviations, $K$ value) are fixable in a revision. The paper's core contributions are solid and well-supported by evidence.

MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>