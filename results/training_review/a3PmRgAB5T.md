Now I have all the information needed to write the authoritative review.

## Summary

This paper introduces Self-Play Preference Optimization (SPPO), an iterative algorithm for LLM alignment that frames the problem as a two-player constant-sum game and targets the Nash equilibrium via a multiplicative-weight-update framework. The core methodological contribution is a simple square-loss objective that regresses each response's log-probability ratio toward its centered win rate against the previous policy. Empirically, SPPO achieves strong results on AlpacaEval 2.0 (28.53% LC win rate for Mistral-7B, 38.77% for Llama-3-8B), MT-Bench, Arena-Hard, and the Open LLM Leaderboard, using only a 0.4B PairRM preference model and 60k prompts without any GPT-4 supervision.

## Strengths

- **Novel, simple, and effective loss objective**: The SPPO loss (square loss on the log-ratio minus centered win rate) is clean, easy to implement, and avoids the pairwise cancellation issue of DPO/IPO. The paper shows that SPPO not only widens the winner-loser gap but also separately increases the winner's likelihood and decreases the loser's, addressing the "only losers lose" phenomenon identified in prior work (Pal et al., 2024). This is demonstrated in Section 4.5 with clear algebraic comparison to DPO, IPO, and KTO.

- **Strong empirical results with clean experimental design**: SPPO achieves state-of-the-art results on AlpacaEval 2.0 (28.53% LC win rate for Mistral-7B) using only 60k prompts, a 0.4B PairRM reward model, and no GPT-4-generated responses or preferences. The design cleanly delineates the source of improvement (the SPPO loss + self-play loop) from confounding factors. The Llama-3-8B results (38.77% LC win rate) further demonstrate scalability and robustness.

- **Consistent gains across iterations and benchmarks**: Unlike DPO and IPO, which plateau or degrade on several metrics (AlpacaEval 2.0 LC win rate: DPO drops from 23.81%→22.30%, IPO drops from 23.78%→20.06%), SPPO shows monotonic improvement across three iterations on AlpacaEval 2.0 (17.11%→24.79%→26.89%→28.53%), Arena-Hard (12.6→18.7→20.4→23.3), and MT-Bench second-turn scores. This consistent trajectory is a genuine advantage.

- **Moderate output length growth**: SPPO's average output length grows modestly (1676→2163 over three iterations) compared to DPO (1676→2189) and IPO (1676→2760). This suggests better regularization and reduced reward hacking, which the paper plausibly attributes to the multiplicative weights framework.

- **Good breadth of evaluation**: The paper evaluates on four distinct benchmarks (AlpacaEval 2.0, MT-Bench, Arena-Hard, Open LLM Leaderboard), includes length-controlled metrics, and provides PairRM heatmap analysis. The inclusion of best-of-16 reranking results also strengthens the analysis.

## Weaknesses

### Fatal

None.

### Major

- **Theory-practice disconnect in the convergence guarantee**: Theorem 1 proves convergence to Nash equilibrium for the exact multiplicative-weight update (Eq. 4), which requires computing the log-partition function $\log Z_{\pi_t}(\xb)$. The practical algorithm (Eq. 8) replaces this with a constant $\eta/2$, justified by a footnote that assumes win probabilities are either 0 or 1 with equal chance — an assumption that does not hold in practice. The paper provides no proof or argument that the constant approximation preserves the convergence properties. While the paper acknowledges this as a limitation (Section 7: "Approximating the log-partition factor with a constant can help reduce variance only when it is close to the soft value function"), this framing understates the issue: the approximation changes the algorithm, and the claim "*provably* approximate the Nash equilibrium" (abstract) is not substantiated for the method actually evaluated. This does not invalidate the empirical contribution, but the paper should either caveat or remove the provability claim for the practical algorithm.

### Minor

- **The DPO/IPO baselines are weaker than the Snorkel checkpoint, muddying the comparison**: The authors' iterative DPO (22.30% LC, Iter3) is substantially worse than Snorkel (26.39% LC), a pre-existing DPO model trained on the same base model, dataset splits, and PairRM judge. The authors do not explain this gap. The paper's headline numbers still position SPPO above Snorkel (28.53% > 26.39%), so the main claim holds, but the ~2% margin over a well-tuned DPO is more modest than the ~6% margin over the authors' own DPO. The paper should acknowledge this discrepancy and discuss why their DPO underperforms Snorkel.

- **Non-monotonic MT-Bench behavior is unexplained**: SPPO's MT-Bench average drops below the base model at Iter1 (7.51→7.21) and Iter2 (7.49) before recovering at Iter3 (7.59). The paper states "we are not certain why the MT-Bench performance drops" (line 797). This is an honest admission but a genuine interpretability gap: for a method claiming improved alignment, degrading multi-turn conversation ability for two iterations before recovery is a concern that warrants at least a hypothesis (e.g., overfitting to single-turn PairRM signals). The two-turn breakdown shows SPPO's first-turn score recovers faster than second-turn, which could inform future analysis.

- **The policy gradient and Q* connections are suggestive but not rigorous**: Section 4.3 frames SPPO as a "semi-online variant of policy gradient method" and Section 4.4 draws a connection to token-level Q* learning. These analogies require strong assumptions (fixed reward function for policy gradient, Bradley-Terry-compatible reward for Q* learning) that are not fully satisfied in the SPPO setting where the "reward" (win rate against π_t) changes every iteration. The paper is appropriately qualified (calling it "semi-online" and noting the Value Function is replaced), but the framing in the abstract ("deep connection to policy gradient theory") overstates what is an interpretation, not a derivation.

- **Textual inconsistency for IPO best result**: Line 740 states "IPO's rate of 25.45%" but the table shows IPO's best LC win rate is 23.78% (Iter1). No number 25.45 appears in the data. This appears to be a reporting error.

### Trivial

- None of note (formatting issues are parser artifacts).

## Nice-to-Haves

- **Ablation on the partition function approximation**: A comparison between the constant-η/2 version and an explicit estimation of log Z (e.g., via importance sampling or a learned value function as in REBEL) would disentangle whether the constant hurts or helps, and would clarify the theoretical claim.
- **Larger K values in the ablation**: Testing K=10 or K=20 would more directly probe whether the multi-response win-rate estimate is a meaningful source of advantage over pairwise methods.
- **Analysis of why SPPO produces shorter outputs**: The paper notes this but does not analyze the mechanism — the constant approximation may implicitly penalize length or act as reward shaping.

## Removed Points

These points were considered and removed for the stated reasons:

1. **"Win probabilities are never exclusively 0 or 1" (Critic Point 1 elaboration)**: This is already acknowledged by the paper as a limitation. The criticism that the assumption is "absurd" is overly harsh and ignores that approximations in theoretically-grounded algorithms are standard practice. The core issue (lack of proof that the approximation preserves convergence) is retained in Major.

2. **"SPPO's policy gradient claim is overclaimed" (Critic Point 3)**: The paper explicitly calls the method "semi-online" (line 325) and states the off-policy nature: "it collects samples from π_θ_t at the start of iteration t, rather than perform on-policy sampling at each gradient step" (lines 325–326). The connections are presented as interpretations, not rigorous theorems. The critic's characterization of the derivation as "misleading" is not supported by the paper's own qualifying language.

3. **"Ablation on batch size is incomplete" (Critic Point 4)**: The paper shows K=2 and K=5 perform similarly (28.26% vs 28.53% LC). This demonstrates robustness, which is a strength, not a weakness. The central claim of SPPO is the self-play + square-loss framework, not the multi-response advantage. If anything, the paper's argument is strengthened by showing K=2 works nearly as well.

4. **"BT modeling is a strawman"**: The paper cites established literature (Tversky, 1969; Munos et al., 2023) to motivate non-transitivity as a concern. This is a standard motivation in the Nash-equilibrium-based RLHF literature and not a strawman.

5. **"DNO characterization is factually wrong"**: Without access to the DNO paper, this cannot be verified. The claim about DNO's practical implementation is a specific factual assertion that should be checked against the original source.

6. **"Short outputs are speculative"**: The paper provides supporting evidence (length numbers from Table 1: IPO 2760 vs SPPO 2163) for its claim that IPO exploits length bias. This is a reasonable inference from the data.

## Novel Insights

The most striking observation across reviews is that SPPO's success may stem from a mechanism the paper does not foreground: by regressing each response's log-ratio toward an individual target (win rate minus 1/2) rather than a pairwise gap, the loss separately governs winners and losers. This changes the optimization dynamics in a way that pairwise losses (DPO, IPO) cannot replicate. The ablation (K=2 vs K=5) further suggests that the loss structure matters more than the precision of the win-rate estimate — a finding that, if confirmed, would shift attention from data quantity to loss design in iterative alignment methods. The paper's theoretical apparatus (game theory, policy gradient, Q* learning) is best understood as three different lenses that all point to the same square-loss objective, rather than a single tight derivation; the empirical success of the objective is the paper's strongest contribution.

## Suggestions

1. **Caveat the convergence claim for the practical algorithm.** Either remove "provably" from the abstract and Section 4.1 when referring to Eq. 8, or explicitly state that Theorem 1 applies to the exact update and that the practical algorithm is an approximation without a proven convergence guarantee. The paper already has the right language in the Limitations section; it should be carried forward into the main claims.

2. **Investigate and explain the DPO implementation gap against Snorkel.** If the gap is due to hyperparameter choices (e.g., tuning PairRM win rate rather than AlpacaEval 2.0), say so. If the authors' SPPO hyperparameters were applied asymmetrically to DPO/IPO, this should be corrected or justified. At minimum, add a paragraph discussing the discrepancy.

3. **Add a brief analysis of the MT-Bench dip.** Even a qualitative inspection of responses from Iter1 vs base model would help readers understand whether the dip reflects a genuine capability loss or a benchmark-specific artifact.

4. **Fix the IPO best rate (25.45%) textual inconsistency** (line 740) to match the table.

## Score and Decision

The paper makes a real contribution: a novel, simple, empirically effective loss function for iterative alignment. The main weakness is the gap between the provable guarantee (for the exact update) and the practical algorithm (with the constant approximation), but this does not undermine the empirical contribution — the SPPO loss works, it's well-motivated, and the results are competitive. With honest caveating of the theoretical claim and a brief investigation of the DPO baseline discrepancy, the paper would be strong. The contribution is sufficient for acceptance.

MY FINAL SCORE: <pineapple>7.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>