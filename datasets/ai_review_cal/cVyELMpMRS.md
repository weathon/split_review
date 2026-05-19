- Decision: Accept
- Avg Score: 6.50
- Scores: 6, 6, 6, 8
Now I have a thorough understanding of the paper and all the reviewers' claims. Let me construct the final consolidated review.

---

## Summary

This paper introduces REFUEL, a regression-based policy optimization method for multi-turn RLHF. The key idea is to use the log-policy-ratio as an implicit critic, avoiding a separate value network, and to train on on-policy self-generated data to mitigate covariate shift that plagues single-turn methods applied to multi-turn dialogue. The paper provides theoretical guarantees (Theorem 1) showing REFUEL can compete with any covered policy, with a weaker completeness condition than NPG (Propositions 1–2). Empirically, an 8B model trained with REFUEL achieves higher winrates at later conversation turns than both DPO/REBEL baselines and the much larger Llama-3.1-70B-it.

## Strengths

- **Theoretical guarantee against covered policies (Theorem 1):** Proves that under Assumptions 1 and 2, REFUEL matches the performance of any policy π* covered by the training distribution up to error O(H√(1/T) + H√(C_{s;π*}C_{y;π*}ε)), providing formal backing for the algorithm's effectiveness.
- **Empirical outperformance on long dialogues:** Table 1 shows REFUEL (iter 2) achieves the highest winrates at turns 3, 4, and 5 (58.8%, 57.2%, 58.6%) among all methods, and the 8B model outperforms Llama-3.1-70B-it at turn 5 (58.6% vs. 55.4%), directly demonstrating that REFUEL addresses the covariate shift that degrades single-turn baselines on longer conversations.
- **Simplicity via eliminating an explicit critic network:** REFUEL merges the actor-critic two-step procedure into a single regression objective (Eq. 3) where the log policy ratio functions as an implicit critic. This is a concrete design simplification over multi-turn actor-critic methods (e.g., Archer, Shani et al.), clearly argued in Sections 3 and 5.
- **Weaker theoretical condition than NPG:** Remark 1 and Propositions 1–2 formally establish that the Approximate Policy Completeness (APC) condition used by REFUEL is strictly weaker than the Q-function approximation error condition required for NPG convergence, a genuine theoretical contribution.
- **Empirical validation on pre-sampled questions:** Table 2 shows REFUEL achieves the highest winrate on both Anthropic HH (82.8%) and UltraInteract (79.6%) among all REBEL baselines, demonstrating the benefit extends beyond the LLM-as-user simulator setting.
- **Ablation evidence isolating contributions:** The paper's baseline taxonomy separates on-policy vs. offline rollin and last-turn vs. multi-turn optimization, experimentally validating that both factors contribute to REFUEL's gains.

## Weaknesses

### Fatal
None.

### Major

- **Missing controlled baseline to isolate the regression objective.** The paper attributes REFUEL's gains to (a) on-policy rollin, (b) multi-turn optimization, and (c) the specific regression loss. However, the baseline taxonomy never evaluates a variant that uses the *same* on-policy multi-turn data collection protocol as REFUEL but with REBEL's (or DPO's) loss function instead of REFUEL's regression loss. The existing baselines either use off-policy rollin (MultiTurnMixed) or optimize only the last turn (LastTurnOnline). A baseline with on-policy rollin *and* multi-turn optimization using REBEL's loss would isolate whether REFUEL's specific regression target contributes beyond the data collection design. Without it, the outperformance could be driven primarily by the more expensive on-policy multi-turn data generation rather than the reparameterization trick. This does not invalidate the contribution but weakens the evidence for the algorithm's unique design.

### Minor

- **Limited iterations (2) without convergence analysis.** Setting one (LLM-as-user) runs only 2 iterations (line 249). Without more iterations or evidence of convergence, it is unclear whether performance would continue to improve, plateau, or degrade. The winrate differences between iter 1 and iter 2 are small (56.32 → 56.64 avg), raising the question of how many iterations are needed.

- **No statistical uncertainty reported.** The main results lack confidence intervals, error bars, or multiple random seeds. Given the use of a fixed test set of 500 samples and GPT4 as judge (likely deterministic at temperature=0), variance from data sampling and training could still be non-negligible.

- **Simulated user is also a baseline comparator.** In Setting one, Llama-3.1-70B-it serves as both the user simulator and a baseline comparator (Table 1). While the paper acknowledges this limitation qualitatively in the Limitations section (lines 366–367), the headline claim that an 8B model "outperforms Llama-3.1-70B-it" rests on a setting where the 70B model plays both roles. An evaluation with a different model (e.g., GPT-4) as the user or with real human judges would strengthen this claim.

- **Missing KL/reward score for Setting one.** Table 1 reports only winrate; including reward model scores and KL divergence (as in Table 2) would help evaluate whether winrate improvements come at the cost of higher divergence from the base policy, especially since Table 2 shows REFUEL's KL on UltraInteract is elevated (93.19 vs. 62.85 for REBEL-LastTurnOnlineShort).

### Trivial
None.

## Nice-to-Haves

- **Computational cost comparison:** REFUEL requires two full rollouts per data point (from a sampled intermediate state to the end), while last-turn online methods generate only the final response. Reporting approximate training time or FLOPs per iteration would help practitioners assess the trade-off.
- **On-policy multi-turn REBEL ablation:** As described in the Major weakness above, this ablation (if possible) would cleanly isolate the value of the regression objective.
- **Small-scale human evaluation:** Even a limited human study (e.g., 100 conversations) would significantly strengthen the claim that REFUEL-trained 8B models outperform 70B models in realistic multi-turn dialogue.
- **Hyperparameter details:** While the paper states "appropriate η" in the theory and uses η in Algorithm 1, reporting the actual numerical value and optimization details (batch size, learning rate, gradient steps) used in experiments would aid reproducibility. *(Note: per filtering rules this is a nice-to-have rather than a criticism.)*

## Removed Points

- **Concentrability coefficients may be large/infinite:** The critic notes that C_{s;π*} and C_{y;π*} in Theorem 1 could be large, making the bound vacuous. This is a generic concern about concentrability-based bounds that applies to essentially all theoretical RL work using this approach (NPG, CPI, Politex, etc.). The paper acknowledges this is standard (line 164). It is not a specific weakness of this paper's theory and does not threaten the core claim. Removed per the "one-size-fits-all" rule.

- **Missing hyperparameters (learning rate, batch size, gradient steps):** The rules instruct to remove nitpicks about undisclosed hyperparameters and trivial implementation details. The critic's request for specific numerical hyperparameter values is removed per this rule.

## Novel Insights

None beyond the paper's own contributions. The two reviews largely converge on the same set of observations about the paper's strengths and weaknesses, with the harsh critic providing a more detailed assessment of the experimental gaps and the strength finder providing a structured summary of contributions. No reviewer-level disagreement reveals a hidden insight not already present in the paper.

## Suggestions

1. **Add an on-policy multi-turn REBEL baseline** (or DPO variant) that uses the exact same data collection protocol as REFUEL but with the base algorithm's loss. This would either validate the regression objective or reveal that the gains come from the data collection design — a useful finding either way.
2. **Report uncertainty estimates** for the main winrate results (e.g., bootstrap confidence intervals over the 500 test samples, or results across 2–3 training seeds).
3. **Run additional iterations** (3–5) for Setting one to show convergence behavior.
4. **Include reward model scores and KL divergence** in Table 1 alongside winrate for Setting one.
