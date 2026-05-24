Now I have good calibration data. Let me write the final consolidated review.

## Summary

The paper presents CALM, a framework for automatic heuristic design (AHD) that combines LLM-based evolutionary search with reinforcement learning (GRPO) fine-tuning of the LLM itself. This enables the LLM to co-evolve with the heuristic population — a novel coupling of "verbal guidance" (prompt manipulation) with "numerical guidance" (RL-based model updates). Across four challenging optimization tasks (OBP, TSP, CVRP, OP) using only a local INT4-quantized 7B model on a single 24GB GPU, CALM consistently matches or outperforms state-of-the-art baselines that rely on larger API-based models.

## Strengths

1. **Novel and well-motivated framework**: CALM is one of the first AHD frameworks that jointly optimizes both the prompt generation process and the LLM itself via RL, moving beyond the fixed-model paradigm of prior work. The paper clearly articulates the distinction between verbal and numerical guidance, and the RL-based fine-tuning mechanism (GRPO) is well-integrated into the evolutionary loop.

2. **Consistent empirical advantages across diverse tasks**: Tables 1–3 show that CALM (local 7B INT4 model) outperforms SOTA API-based methods (GPT-4o-mini) across nearly all test scales on OBP, TSP, CVRP, and OP. For example, on CVRP N=50 (Table 3), CALM achieves a 3.83% gap vs. the best baseline (MCTS-AHD) at 5.44%. On OBP (Table 1), CALM's 0.71% average gap beats MCTS-AHD's 0.89% and achieves zero gap on the 1k_500 test set.

3. **Verbal gradient design is independently competitive**: Section 5.2 shows that even without RL (using GPT-4o-mini with G=1), CALM's operators alone match or exceed prior SOTA on most benchmarks. This cleanly separates the contribution of the prompt operators from the RL component.

4. **Informative ablation study**: Table 4 systematically decomposes the contribution of each component (GRPO, collapse mechanism, each operator). The largest single drop comes from removing GRPO (OBP: 0.71% → 1.78%), confirming the RL fine-tuning as the most impactful element. The ablation also explores alternative reward designs and collapse hyperparameters.

## Weaknesses

### Major

1. **Missing variance in all main result tables**: Tables 1, 2, and 3 report only mean performance over 3 runs with no standard deviations, confidence intervals, or any measure of dispersion. This is a critical evidential gap. Many of the claimed advantages are numerically small (e.g., TSP N=100: CALM 11.58% vs. MCTS-AHD 11.79% — a 0.21pp gap), and the reader cannot assess whether these differences are statistically reliable. Figure 2 does include shaded standard deviations for training curves, but the headline final results — the numbers that support every major claim — lack this treatment entirely. The paper mentions p-values are in Appendix I (omitted during parsing), but basic uncertainty reporting belongs in the main tables. **This must be addressed for the evidence to be convincing.**

### Minor

2. **Sampling budget G is not reported for the main experiments**: The paper specifies G=1 for the API-based variant (without GRPO), but the value of G for the core RL experiments is never stated in the main text. Since GRPO samples G responses per prompt, and total LLM queries = T × G = 2,000, the value of G determines T (the number of evolutionary rounds). This interacts with the collapse mechanism's counter (which tracks rounds without improvement) and affects how one interprets "2,000 LLM queries" relative to the baselines' 1,000 heuristic evaluations. The authors should report G (and thus T) explicitly for all main experiments.

3. **Evaluation budget units are not perfectly matched**: The paper states baselines get 1,000 heuristic evaluations while CALM gets 2,000 LLM queries. These are different units — an LLM query may produce an invalid response that does not count as a heuristic evaluation. The paper does not report the invalid/valid response rate for CALM, making the budget alignment ambiguous. On OBP, the paper notes prior methods use 4,000+ queries for 2,000 evaluations (~50% valid rate), so CALM's 2,000 queries would yield ~1,000 valid evaluations under similar conditions — actually less than the baselines' 1,000. But without this data, the claim of "comparable evaluation budgets" is not fully verifiable. Reporting the valid response rate would resolve this.

### Trivial

4. **Theoretical approximation for collapse timing (Eq. 2) is not validated or used**: Equation (2) provides an analytical approximation for the expected rounds before collapse, but it does not guide any hyperparameter choices in the experiments (δ₀=0.0005, C=15 are simply checked in ablation). The approximation adds little to the paper.

## Nice-to-Haves

- A variant of CALM that directly matches the *number of valid heuristic evaluations* (not LLM queries) to the baselines would remove any ambiguity about budget fairness.
- Including variance (mean ± std) in Tables 1–3, and marking statistically significant improvements, would substantially strengthen the evidence.
- Reporting wall-clock training time and total computational cost vs. baselines would help practitioners assess the practical trade-offs.

## Removed Points

- *"Missing related works"*: Not applicable; the paper has a thorough related work section and explicitly cites concurrent work (Surina et al., 2025; Liu et al., 2025).
- *"CALM uses more evaluations than baselines"* (speculative inference): The direction of the budget gap is ambiguous without the valid-response rate, and on OBP, the paper notes prior methods use 4,000+ queries for 2,000 evaluations, suggesting CALM may use fewer valid evaluations. This cuts both ways and is not a clear weakness.
- *Strengths about "important problem" and "reproducibility commitment" are generic.*
- *"Collapse mechanism theoretical grounding as a major strength"*: The approximation is simple and not empirically validated, making this a minor point at best.

## Novel Insights

The reviews surface an interesting observation: the budget-alignment concern (#3) interacts with the GRPO group sampling (#2) in a way that neither reviewer fully developed. If G > 1 (as required by GRPO), each round generates multiple responses from the same prompt. This means that in a single round, the LLM sees one prompt but generates G heuristics. The collapse mechanism's "no-breakthrough counter" counts rounds — so with larger G, each counter increment represents more total heuristic evaluations. This creates a complex relationship between G, the collapse trigger rate, and the effective exploration budget that is worth analyzing explicitly.

## Suggestions

- Add standard deviations to all entries in Tables 1–3 and discuss whether the observed differences are statistically significant at conventional thresholds.
- Report the value of G used in the main RL experiments and the resulting number of evolutionary rounds T.
- Report the number of valid heuristic evaluations (and invalid/duplicate response rate) for CALM across all tasks, so readers can directly compare the effective evaluation budget against baselines.

## Score and Decision

### Calibration Anchors

**Round 1 — Bracketing:**
| Anchor | Avg Score | Comparison |
|--------|-----------|------------|
| LLM4Solver (XTxdDEFR6D) | 3.40 | Much weaker — unclear contribution, poor experiments. Our paper is clearly stronger. |
| Hercules (0fwJMANq9P) | 5.25 | Similar topic (LLM-based AHD) but without RL fine-tuning. Our paper has a stronger contribution and more consistent results, though both share some reporting gaps. |
| LLM-LNS (Usk4KzBxLW) | 5.25 | Similar domain (LLM + EA for optimization). Our paper is better structured with clearer methodology and stronger empirical results. |
| LLM-SR (m2nmp8P5in) | 8.00 | Much stronger — rigorous evaluation, comprehensive analysis, no significant reporting gaps. Our paper does not reach this level of polish. |

**Round 1 bracket:** 4.5 – 7.0

**Round 2 — Narrowing:**
| Anchor | Avg Score | Comparison |
|--------|-----------|------------|
| EvoPrompt (ZG3RaNIsO8) | 6.50 | Similar paradigm (LLM + EA synergy). Our paper has a stronger contribution (RL co-evolution vs. prompt-only optimization) but comparable experimental rigor. |
| REvolve (cJPUpL8mOw) | 6.00 | Similar (LLM + EA + RL for reward design). Both have genuine contributions and addressable reporting gaps. |
| EvoPress (kWtP5ZOErR) | 6.25 | Different domain (model compression). Not directly comparable. |
| LASeR (7mlvOHL6qJ) | 6.25 | Similar (LLM + EA). Both have solid contributions with minor presentation gaps. |

The paper is comparable to EvoPrompt (6.50) and REvolve (6.00) in overall quality — the contribution is genuine and well-supported, but the missing variance and budget clarity prevent it from being a strong accept. It is clearly stronger than the 5.25-group anchors (Hercules, LLM-LNS) which had more serious weaknesses. Within this band, the paper sits closer to 6.0 than 6.5 because the variance omission is a concrete reporting gap that weakens the headline claims.

**Final score: 6.0** — Accept. The paper makes a clear contribution, the experiments consistently support the core claims, and the weaknesses are bounded reporting/transparency gaps that can be addressed.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>