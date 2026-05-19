- Decision: Accept
- Avg Score: 6.00
- Scores: 6, 6, 6, 6
Now I have a thorough understanding of the paper. Let me construct the final consolidated review.

## Summary

This paper introduces Self-Play Preference Optimization (SPPO), an iterative LLM alignment algorithm that formulates the problem as a constant-sum two-player game aiming for the Nash equilibrium. The method derives from multiplicative-weight updates to a practical square-loss regression objective, where the policy is iteratively updated to improve its win rate against its previous self. Empirically, SPPO achieves a length-controlled win rate of 28.53% on AlpacaEval 2.0 (Mistral-7B) and 38.77% (Llama-3-8B) against GPT-4-Turbo, using only 60k prompts and a 0.4B PairRM preference model with no GPT-4 supervision, outperforming iterative DPO and IPO baselines.

## Strengths

- **Provable convergence to Nash equilibrium**: Theorem 1 provides a finite-sample convergence rate of \(O(1/\sqrt{T})\) for the duality gap of the average policy under the squared-loss regression objective, directly supporting the paper's claim that the iterative framework approximates the Nash equilibrium.

- **State-of-the-art empirical results**: Table 1 shows Mistral-7B-SPPO Iter3 achieves a length-controlled win rate of 28.53% on AlpacaEval 2.0, outperforming Snorkel (iterative DPO, 26.39%) and iterative IPO (max 23.78%) under the same data and preference model. Llama-3-8B-SPPO Iter3 reaches 38.77%.

- **Strong performance without external supervision**: SPPO uses only 60k prompts from UltraFeedback and PairRM-0.4B, with no GPT-4 generated responses or preferences, yet achieves competitive or superior results to models trained with substantial external supervision.

- **Addresses the "relative likelihood gap" problem of DPO**: Section 4.4 demonstrates that SPPO pushes both the winner log-ratio toward positive values and the loser log-ratio toward negative values, unlike DPO which only widens the gap between them — a known issue documented in prior work (Pal et al., 2024).

- **Robustness to estimation noise**: The ablation study (Fig. 5) shows that using only K=2 samples for win rate estimation yields competitive results (Iter3 LC 28.26% vs 28.53% for K=5), indicating the method is not brittle to the number of sampled responses.

- **Connection to policy gradient theory**: Section 4.3 provides a clean derivation showing the SPPO square-loss objective connects to a semi-online variant of policy gradient, where the win rate acts as reward and the log-partition function serves as the optimal baseline.

## Weaknesses

### Fatal
None.

### Major

- **Constant approximation of the log-partition function lacks thorough validation.** The paper replaces \(\log Z_{\hat\pi_t^K}(\mathbf{x})\) with the constant \(\eta/2\) based on a heuristic assumption ("winning probability between any given pair is either 1 or 0 with equal chance") that is unrealistic in practice. This is the key bridge between the theoretical guarantee (Theorem 1, which relies on the exact exponential update) and the practical algorithm. While the policy gradient connection (Section 4.3) provides a secondary justification that this constant acts as a variance-reducing baseline, the paper does not ablate this design choice (e.g., comparing against estimating \(\log Z\) from samples, or studying sensitivity to the value of \(\eta/2\)). The concurrent work REBEL, mentioned in the paper, avoids this approximation by regressing on the win rate difference to cancel the partition function — a direct comparison would have been illuminating. This is a **methodological gap**; it does not invalidate the empirical results, but it undermines how tightly the theory and practice are connected.

### Minor

- **Statistical significance is not assessed.** All results (AlpacaEval 2.0, MT-Bench, Arena-Hard, Open LLM Leaderboard) are single runs without confidence intervals, standard deviations, or multiple seeds. Given known variance in LLM-based evaluations (AlpacaEval 2.0 win rates can fluctuate by several percent), the reader cannot assess whether the reported margins over baselines are reliable. For instance, the 2% gap between SPPO Iter3 (28.53%) and Snorkel (26.39%) could fall within evaluation noise. This weakness is shared with most papers in the field, but it nevertheless weakens the evidential strength of the comparisons.

- **The theory-practice gap regarding the average vs. last iterate is not discussed.** Theorem 1 guarantees convergence for the *average* policy \(\bar\pi_T\), but the algorithm outputs the *last* iterate \(\pi_T\). The paper does not comment on whether the last iterate inherits the guarantee or how large the gap could be. Similarly, the realizability assumption (the optimization in Eq. 13 is exactly solvable) is unrealistic for neural policies. These are common in theoretical papers but deserve acknowledgment.

- **MT-Bench performance shows an unexplained dip.** SPPO Iter1 (7.21) and Iter2 (7.49) score *below* the base model (7.51) on MT-Bench, only recovering at Iter3 (7.59). The paper says "we are not certain why" but does not investigate. This weakens the claim of monotonic improvement, even though the final iteration does outperform the base model.

- **The claim about avoiding over-optimization is suggestive but not definitive.** The paper argues SPPO avoids over-optimization against PairRM because best-of-16 reranking still improves AlpacaEval 2.0 performance. This is reasonable evidence (if the policy had collapsed to exploit PairRM, reranking would not help), but no analysis is provided on whether the judge (GPT-4-Turbo vs. GPT-4-0613 vs. other LLM judges) affects the conclusion. Given that IPO shows a larger length increase and stronger PairRM win rate but worse GPT-4-judged performance, the paper's interpretation is plausible but not conclusive.

- **Hyperparameter selection uses PairRM as the criterion.** The paper selects models by their average PairRM win rate on a hold-out subset of UltraFeedback, then evaluates on GPT-4-based benchmarks. This creates a potential confound: the method that better optimizes for PairRM may be favored in selection, then evaluated on a different judge. The paper should acknowledge this more explicitly.

### Trivial
None.

## Nice-to-Haves
- An ablation comparing the constant \(\eta/2\) approximation against estimating \(\log Z\) from samples would directly validate the key approximation.
- A sensitivity analysis on \(\eta\) would strengthen the method's robustness claims.
- Reporting training time, GPU-hours, and number of preference queries would allow a practical cost comparison with iterative DPO/IPO.

## Removed Points

- **Weakness about Policy Gradient connection not being exact**: The paper carefully describes it as an "alternative interpretation" and "connection" — not an equivalence. The reviewer's concern about over-claiming is unfounded given the paper's measured language (line 325: "provides an alternative interpretation for SPPO as a semi-online variant of policy gradient"). **Removed: misreading of the paper.**

- **Weakness about missing related works**: Per instructions, I cannot comment on missing related works as I lack external sources to confirm their existence. **Removed: per policy.**

- **Weakness about the Open LLM Leaderboard decline contradicting game-theoretic framing**: The paper's game-theoretic framing is about the *preference game* (with PairRM), not about improving on all benchmarks. The paper discusses this decline explicitly as "alignment tax" (line 846) and notes it affects DPO and IPO equally. The decline is consistent across all methods and does not contradict SPPO's core claims. **Removed: scope creep / not a genuine weakness of the method.**

- **Weakness about missing computational cost comparison**: The reviewer notes the paper does not report training time or GPU-hours. This is a nice-to-have rather than a weakness affecting the validity of results. **Moved to Nice-to-Haves.**

- **Weakness about evaluation on held-out preference data**: The reviewer asks for evaluation on held-out preference data (comparing predicted vs. actual win rates). This is an interesting analysis but outside the paper's stated scope (benchmark-based evaluation). **Removed: scope creep.**

- **Weakness about the ablation being too limited (not exploring η sensitivity, iterations effect)**: The paper does ablate mini-batch size K, which is the most relevant variable for their core argument about win rate estimation. The η ablation is a reasonable request but fits as a nice-to-have. **Demoted to Nice-to-Haves.**

## Novel Insights

None beyond the paper's own contributions. The strengths and weaknesses identified by the reviews are largely convergent with the paper's self-presentation — the reviews add little that the paper's own discussion of limitations (lines 915-918) does not already gesture toward, aside from the concrete suggestion to ablate the constant baseline.

## Suggestions

1. **Ablate the constant baseline**: Compare the current \(\eta/2\) approximation against a version that estimates \(\log Z_{\pi_t}(\mathbf{x})\) from additional samples (as referenced in Eq. 8, line 251). This would directly validate the key approximation that bridges theory and practice.
2. **Report confidence intervals or multiple seeds**: For the main AlpacaEval 2.0 results, running 3 seeds or reporting bootstrap confidence intervals would substantially strengthen the reliability of the claims.
3. **Acknowledge the average-iterate vs. last-iterate gap** in the theory section, and note that the last iterate may not inherit the theoretical guarantee.
4. **Investigate the MT-Bench dip** in Iter1/Iter2 to understand whether it reflects a genuine tradeoff or an artifact of model selection.
