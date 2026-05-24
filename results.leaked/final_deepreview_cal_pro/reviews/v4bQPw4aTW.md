Now I have sufficient information to produce the final consolidated review. Let me organize my analysis.

**Round 1 Bracket:** Based on the initial calibration search, the paper sits between ~5.0 and ~6.5, with the most directly comparable anchor (Damani et al., 6qUUgw9bAZ) at 6.50.

**Round 2 Narrowing:** The additional anchors confirm the bracket. VNckp7JEHn (5.75) is a related empirical study on inference scaling; shgx0eqdw6 (7.00) is a stronger paper with external validation. AdaBoN is stronger than the 5.75 anchor (more methodological novelty, broader coverage) but weaker than the 7.00 anchor (lacks external validation and competitive baselines). It is comparable to Damani et al. (6.50) — simpler and more practical but with similar gaps.

**Final Score:** 6.0, Accept.

---

## Summary
AdaBoN proposes a simple, training-free two-stage method for adaptively distributing a Best-of-N sampling budget across prompts. It uses Gaussian KDE to estimate per-prompt reward distributions from a small exploration budget, then greedily allocates the remaining budget based on estimated marginal gains. The method is evaluated across 12 LM-RM pairs, 3 datasets, and 50 prompt batches, consistently beating uniform allocation and remaining competitive with uniform allocations using 20% larger budgets.

## Strengths
- **Practical, training-free design**: AdaBoN requires no auxiliary model training, works out-of-the-box for any LM-RM pair, and adapts to the inference budget — a clear advantage over Damani et al. (2024), which requires training separate MLPs per LM-RM pair and budget. The method uses only Gaussian KDE with an automatic bandwidth selector, leaving one hyperparameter (exploration budget $d$), for which $d=0.75B$ works well across all experiments (Table 3 in Appendix G.1).

- **Broad and rigorous empirical evaluation**: The paper tests 12 LM-RM pairs (4 LMs × 3 RMs), 50 distinct prompt batches, and 3 datasets (AlpacaEval, HH-RLHF, PKU-SafeRLHF). Tables 1–2 show AdaBoN achieves median BWRs up to 0.62 and outperforms uniform allocation on >75% of batches across all pairs. EST values around 150 indicate competitiveness with uniform allocations at 20–33% larger budgets. This scale far exceeds prior adaptive-allocation work.

- **Well-motivated evaluation metrics**: The Batch Win Rate (BWR) and Expected Survival Time (EST) respect the comparative nature of Bradley-Terry-trained reward models — where only relative comparisons are meaningful, not absolute scores. These metrics directly quantify the advantage over uniform allocation and computational savings respectively, and are clearly defined (Equations 3–5).

- **Clean theoretical grounding**: Proposition 3.1 proves concavity of the expected-max function, guaranteeing optimality of the greedy allocation under true distributions. This provides a principled foundation for the allocation step.

- **Scalability and robustness demonstrated**: Figure 3 shows average BWR increases with batch size $K$ across all LM-RM pairs. Appendix ablations (varying $B \in \{80,100,120,140,160\}$ and $K \in \{3,5,10,15,20\}$) demonstrate robustness to budget and batch size choices.

## Weaknesses

### Fatal
None.

### Major
- **No external validation of response quality**: The evaluation relies entirely on reward model scores. While the paper correctly argues that RM comparisons are meaningful under the Bradley-Terry model, an adaptive method that reallocates budget toward prompts where the RM is easier to score highly could, in principle, win more often on the reward metric without producing genuinely better outputs. A side-by-side comparison of responses from uniform vs. adaptive allocation judged by a strong LLM (e.g., GPT-4) or human raters on a subset of prompts would directly address this concern. This is the most significant gap in the current evidence, as the paper's central claim is about improving alignment quality, not just RM scores.

- **No adaptive baseline beyond uniform allocation**: The paper positions itself against the uniform (non-adaptive) allocation, but the core contribution is to *adapt* the budget. A basic adaptive heuristic — e.g., allocating remaining budget inversely proportional to the maximum reward seen during exploration, or a simple bandit strategy — would test whether the full KDE+greedy pipeline is necessary. Without such a baseline, it is unclear whether the estimation machinery adds value over a trivial rule a practitioner might use. This weakens the evidence for the method's novelty and practical advantage.

### Minor
- **Practical significance of BWR improvements could be better contextualized**: Median BWRs are 0.56–0.62, with some batches reaching 0.70. The paper does not report the *magnitude* of reward gains (e.g., expected cumulative reward difference) alongside win rates. While the EST metric shows AdaBoN can match uniform with ~20% more budget, reporting the expected reward advantage per batch would help readers assess whether a BWR of 0.56 translates to meaningful downstream improvements.

- **No statistical significance assessment**: The paper reports median BWRs with [Q1, Q3] intervals across batches and standard errors in Figure 3, but does not test whether the overall win rate is significantly above 0.50 across all batches and runs. This makes it harder to assess the reliability of the reported improvements, particularly for LM-RM pairs where performance is weaker (e.g., Qwen-Armo at 0.54 median BWR, 78% of batches > 0.50).

- **Reward overoptimization risk not discussed**: An adaptive method that concentrates budget on prompts where the RM yields higher scores could amplify reward overoptimization relative to uniform sampling. The paper acknowledges limitations around discrete RMs and dynamic refinement (Section 5) but does not address this risk, which matters for practical deployment.

### Trivial
- The claim that "only two calls to the base LM need to be made" (p. 5) is imprecise — the first "call" involves $dK$ individual generations. While the two-stage structure does minimize latency rounds, the phrasing could mislead readers about the total number of LM queries.

## Nice-to-Haves
- Reporting expected cumulative reward differences alongside BWR/EST would give a fuller picture of the improvements.
- Experiments at substantially larger budgets (e.g., $B=500, 1000$) would strengthen the claim that the method works in the "large per-prompt budget" regime, though the current $B \in [80,160]$ sweeps partially address this.
- Discussion of how the method might be extended to discrete or binary reward settings (which the paper notes as a limitation) would broaden its applicability.

## Removed Points
These points are flagged to be removed, treat them with caution.

**From Harsh Critic:**
- *"The experimental configuration is narrow and the budget justification is missing"* — The paper does vary $B$ (80–160) and $K$ (3–20) in Appendix ablations, and the B=120 choice is reasonable given the "small batch, large budget" regime. The criticism overstates a minor gap.
- *"The claim that per-prompt reward distributions are 'smooth and easy to learn' … may not generalise; it should be presented as an empirical observation"* — The paper already presents this as an empirical finding ("We find that the per-prompt reward distributions … are smooth"), tested across 12 LM-RM pairs and 3 datasets. This criticism is a strawman.
- *"The omission of any reference to simple adaptive heuristics or bandit-based allocations as baselines is a noticeable gap"* — This is captured in the Major weakness about missing adaptive baseline, but the part about missing *references* is removed per the hard rules (do not mention missing related work).
- *"The paper does not discuss the statistical variability of the median BWR across this finite set of batches"* — The paper reports [Q1, Q3] intervals for all median values and standard errors in Figure 3, so this claim is factually incorrect.

**From Strength Finder:**
- *"Comprehensive and rigorous empirical evaluation"* — Retained as a strength but note: the evaluation is broad in coverage but lacks external validation, so "rigorous" is only partially true.
- *"Practical latency minimization"* — Retained. This is a genuine strength of the two-stage design, though the phrasing about "only two calls" is slightly imprecise (noted in Trivial).

## Novel Insights
The paper's core insight — that per-prompt reward distributions are smooth enough for simple KDE to enable effective adaptive allocation, without any auxiliary model training — is genuinely useful. The empirical finding that a fixed exploration budget of $d=0.75B$ works robustly across 12 LM-RM pairs and 3 datasets is a practical contribution that could simplify future work in this area. The BWR and EST metrics provide a clean framework for evaluating adaptive allocation methods that respect the comparative nature of reward models.

## Suggestions
- The single most impactful addition would be a small-scale external quality assessment (GPT-4 judge or human evaluation on, say, 200 prompt-responses from uniform vs. adaptive). This would directly address the disconnect between RM scores and response quality.
- A simple adaptive baseline (e.g., allocate remaining budget proportionally to the maximum reward observed during exploration) would cost very little to implement and would substantially strengthen the evidence that the KDE+greedy pipeline is necessary.
- Clarify the "only two calls" phrasing to "only two *rounds* of parallel LM calls" to avoid misleading readers.

## Score and Decision

**Round 1 bracket:** The paper falls between ~5.0 and ~6.5 based on comparison with anchors from three score bands.

**Anchor comparison:**
| Anchor | Avg Score | Round | Comparison |
|--------|-----------|-------|------------|
| 6qUUgw9bAZ (Damani et al. 2024) | 6.50 | Round 1 | Directly comparable; AdaBoN is simpler (no training) with broader coverage, but lacks adaptive baseline |
| VNckp7JEHn (Inference Scaling Laws) | 5.75 | Round 2 | Empirical study of inference strategies; AdaBoN has more methodological novelty |
| shgx0eqdw6 (ARGS) | 7.00 | Round 2 | Stronger paper with GPT-4 eval and broader baselines; AdaBoN is below this |
| 77gQUdQhE7 (Inference-Aware FT for BoN) | 5.67 | Round 1 | Different approach (fine-tuning); AdaBoN has broader coverage and simpler deployment |
| 0xUEBQV54B (Large Language Monkeys) | 5.00 | Round 1 | Empirical BoN study; AdaBoN is clearly stronger methodologically |

**Round 2 narrowing:** AdaBoN sits between the 5.75 and 7.00 anchors. It is stronger than the Inference Scaling Laws paper (more novel method, broader evaluation) but weaker than ARGS (lacks external validation and competitive baselines). It is comparable to Damani et al. (6.50): AdaBoN is simpler and more practical, with broader empirical coverage, but Damani et al. has a more sophisticated framework and more task diversity.

The paper is a solid contribution with a clean, practical method, broad empirical coverage, and well-motivated metrics. The lack of external validation and an adaptive baseline are genuine gaps, but they do not invalidate the core contribution. Score: 6.0.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>