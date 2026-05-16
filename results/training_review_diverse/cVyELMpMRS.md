Now I have a thorough understanding of the paper. Let me construct the final consolidated review.

## Summary

This paper introduces REFUEL, a multi-turn RLHF algorithm that eliminates the need for a separate critic network by reparameterizing Q-values as log-policy ratios and regressing relative future returns from paired rollouts sharing a common prefix. It addresses covariate shift via on-policy data collection: at each iteration, the policy generates its own conversation histories (rollins) and independent completions (rollouts), ensuring the training distribution matches the deployment distribution. The paper provides theoretical guarantees (Theorem 1) showing REFUEL competes with any policy covered by the training distribution under weaker conditions than NPG, and presents empirical results on UltraInteract and Anthropic HH where REFUEL consistently outperforms DPO and REBEL variants, especially on later conversation turns — including a Llama-3-8B-it model fine-tuned with REFUEL outperforming Llama-3.1-70B-it on multi-turn dialogues.

## Strengths

- **Novel critic-free formulation for multi-turn RLHF.** REFUEL's core contribution — using the difference of two trajectory-level rewards from a shared prefix as an unbiased estimate of the Q-value difference, then regressing log-policy-ratios against this target — is technically sound and genuinely useful. It eliminates the memory and stability overhead of a separate critic network (SAC, DDPG-style methods) while extending beyond the single-turn bandit setting that DPO and REBEL are limited to. The derivation from the KL-constrained RL objective (Eq. 1) through the closed-form solution to the regression loss is clean and well-motivated (Section 3).

- **Stronger theoretical guarantees under weaker conditions.** Theorem 1 provides a formal performance guarantee (competes with any covered policy), and Propositions 1–2 in Remark 1 (Section 4) establish that REFUEL's Approximate Policy Completeness (APC) condition is strictly weaker than the Q-function approximation error condition required for NPG convergence in the log-linear setting. This is a meaningful theoretical advance over prior policy gradient theory.

- **Consistent empirical advantage over DPO/REBEL baselines, especially on longer conversations.** In the primary UltraInteract experiment (Table 1), REFUEL achieves the highest average winrate (56.64%), and its winrate rises with conversation length while all baselines (including 70B-parameter Llama) degrade — demonstrating that on-policy multi-turn optimization is practically beneficial. The controlled ablation comparison between on-policy vs. offline rollin variants (LastTurnOnline vs. LastTurnOffline vs. LastTurnMixed) cleanly isolates the effect of on-policy data collection, supporting the paper's central narrative about covariate shift. The second experiment on Anthropic HH and UltraInteract with pre-sampled questions (Table 2) confirms the trend: REFUEL achieves the best winrate on both datasets.

- **Explicit framing and mitigation of covariate shift.** The paper clearly identifies why standard single-turn RLHF methods fail on multi-turn tasks (Section 2.1): training on offline-generated histories creates a distribution mismatch when the learned policy generates its own histories at test time. The algorithm directly addresses this through iterative on-policy data generation, and the empirical comparison between on-policy and offline rollin algorithms quantitatively validates the importance of this design choice.

- **Connection to policy gradient theory.** The paper explicitly connects REFUEL to PSDP, CPI, NPG, and vanilla PG, showing that it inherits the theoretical properties of the former while maintaining the computational efficiency of the latter. This contextualization helps practitioners understand where REFUEL sits in the broader RL landscape.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

- **Theory-practice gap in initialization assumption.** Theorem 1 explicitly assumes π₁ is a uniformly random policy (line 168), but experiments initialize from a pretrained LLM (Llama-3-8B-it). The theoretical guarantee — that REFUEL competes with any covered policy after T iterations — relies on the uniform policy's full coverage, while a pretrained LLM has strong but limited coverage. The paper mentions in the coverage discussion (line 164) that "initialization π₀ — typically is a pre-trained LLM, is informative in terms of covering a high quality policy," which partially acknowledges the gap, but the theorem as stated does not apply to the actual experimental setting. This is a common simplification in RL theory papers, so it does not invalidate the contribution, but the paper would benefit from discussing how the theory could be adapted (e.g., a warm-start version where the initial policy already provides bounded concentrability).

- **Limited iterations weaken iterative-improvement evidence.** The main experiment uses only 2 iterations (line 249). The improvement from iteration 1 to iteration 2 is marginal (winrate 56.32 → 56.64). For an iterative policy optimization method with theoretical O(1/T) convergence, demonstrating stable improvement over more iterations (e.g., 5+) would substantially strengthen the empirical case. Without more iterations, the reader cannot tell whether the algorithm converges, plateaus, or risks overfitting. This is particularly relevant because the paper's theoretical framing emphasizes iterative improvement.

- **No confidence intervals or measures of uncertainty.** The reported winrates (Tables 1 and 2) are point estimates without standard errors or confidence intervals. With 500 evaluation samples, binomial confidence intervals could be computed and would directly affect the reader's confidence in the rankings — e.g., the difference between REFUEL (56.64) and REBEL-LastTurnOnline (54.24) may or may not be statistically significant. This is a routine reporting expectation for empirical ML papers.

- **Unexplained baseline failure.** REBEL-MultiTurnMixed achieves only 34.4 winrate on the UltraInteract dataset (Table 2), which is far worse than any other baseline (and worse than random). The paper does not comment on this outlier, which is surprising given that the same method performs reasonably on Anthropic HH (78.6). This could indicate instability, a tuning issue, or a fundamental incompatibility with the dataset, but the reader has no way to diagnose it.

- **Key hyperparameter values not reported.** The learning rate η, batch size, and number of gradient steps per iteration are not specified in the paper. Since η controls the KL-regularization strength and directly affects the algorithm's behavior, its value is nontrivial for reproducibility.

### Trivial

- The paper states "we note that that above" (line 146) and "Note that that" (line 142) — a minor grammatical duplication in the prose, though these are likely parser artifacts.

## Nice-to-Haves

- **Comparison to a multi-turn actor-critic (even a lightweight one).** The paper explicitly chooses not to compare against PPO due to computational cost (line 241). This is a reasonable decision, but the paper's claim that REFUEL is an "efficient alternative to actor-critic" would be strengthened by comparing to even a simple advantage actor-critic (A2C) with a small critic. Without any such comparison, the efficiency claim remains qualitative.

- **Report approximate computational cost.** The paper claims REFUEL is more efficient than actor-critic methods but does not report wall-clock time, GPU memory usage, or number of generated tokens. Reporting these would substantiate the efficiency advantage concretely.

- **Ablation: on-policy rollin vs. offline rollin within the same algorithm.** The paper compares across algorithms (REFUEL vs. DPO/REBEL variants) but does not ablate within REFUEL itself — e.g., running REFUEL with offline rollins while keeping the multi-turn regression objective, to isolate the contribution of on-policy data from the contribution of the regression formulation.

- **Variance of the regression target.** The regression target (difference of two trajectory rewards) is a single noisy sample. The paper could discuss or estimate the variance of this target and how many samples per state would be needed to control it, which would guide practitioners on data requirements.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **Harsh Critic's "Strong coverage assumption without empirical verification":** The concentrability assumption (Assumption 2) is a standard assumption in the policy gradient theory literature (the paper cites Kakade2002, Bagnell2003, Abbasi2019, Agarwal2021, Bhandari2024). Demanding empirical verification of theoretical assumptions is not standard practice for theory papers and reflects a mismatch of expectations.

- **Harsh Critic's note that "Proposition 4 and Proposition 5 are claimed but not proven in the main text (the proofs are in the appendix)":** Per instructions, missing appendix content is a parser artifact; the proofs exist in the original submission.

- **Harsh Critic's criticism that the transition from "minimizer of least squares is the conditional mean" to using a single noisy sample is "glossed over":** The paper explicitly states (lines 119–122) that this is standard practice and that the sample is an unbiased estimate. The derivation is correctly reasoned; the criticism misunderstands standard regression-based RL methodology.

- **Strength Finder's generic strengths about "addressing an important problem":** These lack specific content and are superseded by the more substantive framing below.

- **Harsh Critic's section note about "The discussion of the APC condition is helpful...":** This is not a weakness; it's a positive observation embedded in the criticism section.

## Novel Insights

None beyond the paper's own contributions. The reviews do not surface any insight about the paper that the paper itself does not already articulate.

## Suggestions

1. **Add more iterations** (at least 5) to the primary experiment, with per-iteration winrates and confidence intervals. This directly supports the iterative optimization narrative and the theoretical O(1/T) claim.
2. **Discuss or formally relax the uniform-initialization assumption** in Theorem 1 — e.g., state a corollary where the initial policy has bounded concentrability, or explicitly acknowledge the gap and explain why the analysis would still hold for informative initializations.
3. **Add confidence intervals or standard errors** to all winrate tables. With 500 evaluation samples, bootstrap intervals or binomial proportion CIs are straightforward to compute.
4. **Report hyperparameter values** (η, batch size, gradient steps, optimizer) in the experimental section or appendix.
5. **Comment on the REBEL-MultiTurnMixed failure on UltraInteract** (winrate 34.4, RM score -0.25) — is this a tuning artifact or a known failure mode? Either fix the tuning or add a discussion.

## Score and Decision

The paper presents a genuinely novel, well-motivated algorithm for an important problem. The theoretical framing is rigorous, the derivation is clean, and the empirical results consistently favor REFUEL across two experimental settings. The weaknesses are real but minor — none threaten the core contribution. The theory-practice gap in initialization is a standard simplifying assumption; the 2-iteration limit is a practical constraint that does not invalidate the observed improvements; and the missing confidence intervals are a reporting issue, not a methodological flaw. On balance, this is a solid contribution that should be published.

MY FINAL SCORE: <pineapple>7.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>