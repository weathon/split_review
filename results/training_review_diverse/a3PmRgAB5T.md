Now I have all the information needed. Let me formulate my final consolidated review by carefully cross-referencing each reviewer claim against the paper.

---

## Summary

This paper proposes Self-Play Preference Optimization (SPPO), a method for LLM alignment that formulates the problem as a constant-sum two-player game and aims to find the Nash equilibrium. The algorithm is derived from multiplicative weight updates, approximated by a square-loss objective that regresses log-ratios against win rates. Empirically, SPPO fine-tuned from Mistral-7B-Instruct-v0.2 achieves a 28.53% length-controlled win rate on AlpacaEval 2.0, outperforming iterative DPO (Snorkel, 26.39%) and IPO (25.45%), all without GPT-4 supervision. The paper also provides a theoretical convergence guarantee (Theorem 1) and connects the SPPO objective to policy gradient theory and token-level optimal value learning.

## Strengths

- **Provable convergence framework.** Theorem 1 provides a formal guarantee that the average policy from the idealized exponential-weight update converges to the Nash equilibrium at a rate of O(1/√T), grounding the algorithm in established game-theoretic machinery (following Freund & Schapire, 1999).

- **Novel regression objective that addresses a known limitation of DPO.** The SPPO loss directly regresses each response's log-ratio to its win rate minus 1/2, rather than only maximizing the winner-loser gap. Section 4.5 explains that DPO's pairwise loss "does not necessarily drive up the likelihood of the preferred responses" (citing Pal et al. 2024). The empirical evidence is consistent with this: SPPO shows steady gains across iterations (LC win rate 24.79% → 26.89% → 28.53%) while iterative DPO peaks and declines (23.81% → 24.23% → 22.30%), and the analysis of output lengths suggests SPPO does not simply exploit length bias.

- **Strong empirical results without GPT-4 supervision.** SPPO outperforms iterative DPO (Snorkel) and IPO on AlpacaEval 2.0 using only PairRM-0.4B and 60k prompts. The improvement is consistent across multiple benchmarks (MT-Bench, Arena-Hard, Open LLM Leaderboard), and results are replicated on a second base model (Llama-3-8B-Instruct, reaching 38.77% LC win rate).

- **Connection to policy gradient provides intuitive grounding.** Section 4.3 shows that the SPPO square-loss objective is interpretable as a semi-online policy gradient with the win rate as reward and the log-partition function as the optimal baseline, linking game-theoretic and RL perspectives.

## Weaknesses

### Fatal
None.

### Major

- **The convergence guarantee (Theorem 1) applies to the idealized update (Eqn. 9), not the actual loss minimized in practice (Eqn. 10).** Theorem 1 proves convergence for the objective using the full log-partition function log Z. The practical algorithm replaces log Z with η/2 (Eqn. 10). The justification for this replacement — "assuming the winning probability between any given pair is either 1 or 0 with equal chance, when K → ∞" — rests on strong assumptions unlikely to hold for real preference distributions, which are often stochastic. The paper acknowledges the approximation (lines 271–273, limitations in Section 6) but presents the convergence proof as a primary motivation (abstract: "provably approximate the Nash equilibrium"; line 39: "enjoys provable guarantees"). This creates a gap between the advertised theoretical property and what the algorithm actually delivers. The paper would benefit from either a modified convergence argument for the practical loss or a clearer separation between the idealized theory and the practical method, with empirical validation that the constant approximation does not harm convergence.

### Minor

- **No confidence intervals or statistical significance measures.** All win rates, LC win rates, and benchmark scores are single point estimates without error bars, bootstrap intervals, or multiple seeds (Tables 1–4, Figures 2–3). Given that AlpacaEval 2.0 uses only 805 prompts and the margin between SPPO Iter3 (28.53%) and Snorkel (26.39%) is 2.14 percentage points, it is difficult to assess whether the improvements are statistically reliable. Additionally, hyperparameter selection uses the same PairRM signal used for training, creating a potential feedback loop. Adding bootstrap confidence intervals (the AlpacaEval 2.0 repository provides a script) would significantly strengthen the empirical claims.

- **Missing ablation of the η/2 constant approximation.** The paper ablates the mini-batch size K (2 vs. 5) but does not compare the constant-replacement loss (Eqn. 10) against estimating log Z from samples (Eqn. 8). This is the most directly informative experiment for validating the central theoretical-to-practical transition. Such an ablation would either confirm that the constant is a harmless simplification or reveal that performance depends on it, in which case the theoretical framing would need revision.

- **IPO results omitted from MT-Bench and Arena-Hard tables.** The abstract states that SPPO "outperforms the (iterative) DPO and IPO on MT-Bench, Arena-Hard, and the Open LLM Leaderboard," but the MT-Bench table (Figure 3 left) and Arena-Hard table (Figure 3 right) only compare SPPO against the base model, Snorkel (iterative DPO), and iterative DPO — IPO is absent from both. IPO is compared on AlpacaEval 2.0 and Open LLM Leaderboard, but the omission on two of the four claimed benchmarks makes the sweeping claim in the abstract partially unsupported by the presented data.

- **Limitations section is brief on the theory-practice gap.** The limitations paragraph (Section 6) mentions the log-partition approximation but does not discuss the strength of the assumptions underlying the constant replacement or the reliance on a single preference model (PairRM). A more thorough discussion would strengthen the paper's scientific candor.

### Trivial
None.

## Nice-to-Haves

- Adding bootstrap confidence intervals to the main AlpacaEval 2.0 results would address the statistical significance concern without requiring multiple training runs.
- A log-ratio analysis (as suggested in Section 4.5) showing distributions of log(π_θ(y_w|x)/π_ref(y_w|x)) and corresponding quantities for losers would directly illustrate SPPO's claimed advantage over DPO.
- A small hyperparameter sensitivity study (varying η) on a validation set would demonstrate robustness.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **"PairRM is external supervision making the 'no external supervision' claim misleading."** The paper explicitly says "without additional external supervision (e.g., responses, preferences, etc.) **from GPT-4 or other stronger language models**" (line 8, emphasis added). PairRM is a 0.4B model that the paper openly acknowledges using; the claim is specifically about not using GPT-4 or similarly large generative models as supervisors. The criticism misreads the paper's actual statement.

- **"The O(K²) query cost is expensive."** The paper already states that "In total, O(K²) queries will be made" (line 319) for K=5, which is acceptable. This is an acknowledged design choice, not an omission.

- **"The policy gradient equivalence is approximate."** The paper presents the connection as "an alternative interpretation" (line 325) and a "semi-online variant" — the derivation is mathematically sound for the given reward, and the paper does not claim exact equivalence to standard online policy gradient. The criticism overstates what the paper claims.

- **"The ablation difference between K=2 and K=5 is small and likely noise."** While true that the Iter3 difference is 0.27%, the paper's conclusion is that "the performance of SPPO is robust to the noise in estimating PP" — which is actually supported by the small difference. The paper is not claiming a strong advantage of K=5 over K=2 at Iter3; it's claiming robustness.

- **"Comparing concurrent methods DNO and REBEL."** The paper explains why these comparisons are not apples-to-apples: DNO uses GPT-4 responses as supervision and GPT-4 as judge (line 93). Excluding methods with fundamentally different supervision budgets from head-to-head comparison is standard practice.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. **Ablate the η/2 constant.** Compare three variants: (i) using the estimated log Z from samples (Eqn. 8), (ii) using the constant η/2 (Eqn. 10), and (iii) using a learned baseline. This experiment directly tests whether the constant approximation is justified and would either validate the theoretical simplification or reveal a need for revision.

2. **Add bootstrap confidence intervals** to the AlpacaEval 2.0 results (the repository provides a script). This addresses the evidential concern with minimal additional computation.

3. **Include IPO results on MT-Bench and Arena-Hard** in the tables, or qualify the abstract's claim to reflect the benchmarks where IPO was actually compared.

4. **Expand the limitations discussion** to explicitly address the strength of assumptions behind the constant η/2 approximation and the reliance on PairRM as the sole preference model.

## Score and Decision

The paper proposes a well-motivated algorithm with strong theoretical grounding and convincing empirical results across multiple benchmarks. The main concern — the gap between the convergence guarantee (for the idealized update) and the practical algorithm (with the constant approximation) — is real but acknowledged by the authors and does not invalidate the empirical contribution, which stands on its own. The remaining weaknesses (missing confidence intervals, incomplete IPO comparison, absent ablation) are addressable. Overall, this is a solid contribution to the LLM alignment literature.

**Score: 7.0**

MY FINAL SCORE: <pineapple>7.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>