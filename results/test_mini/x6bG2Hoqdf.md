Now I have all the information I need. Let me compile the final review.

## Summary

This paper proposes CALM, a framework for automatic heuristic design (AHD) that integrates evolutionary heuristic search with reinforcement learning (GRPO) fine-tuning of a local LLM, enabling co-adaptation of both the prompt generation process and the LLM itself. Running on a single 24GB GPU with a quantized 7B model, CALM outperforms API-dependent baselines (including those using GPT-4o-mini) across online bin packing, TSP, CVRP, and orienteering problems, and includes thorough ablation studies validating each component.

## Strengths

1. **First framework to co-evolve LLM parameters with evolutionary heuristic search for AHD.** The idea of using GRPO to fine-tune the LLM based on performance feedback from generated heuristics is novel and well-motivated. The paper correctly identifies that prior work keeps the LLM frozen and only manipulates prompts ("verbal gradients"), leaving the model's generative capability unadapted. CALM closes this gap through "numerical gradients" from RL (§1, §4).

2. **Strong empirical results across four diverse optimization tasks.** CALM consistently outperforms or matches all LLM-based AHD baselines on OBP, CVRP, and OP (Tables 1–3), with particularly large margins on CVRP (3.83% vs 5.44% for MCTS-AHD at N=50) and OP (12.58% vs 15.10% for HSEvo at N=200). Out-of-domain generalization (e.g., OBP on 10k instances, TSP at N=200) is demonstrated across multiple scales.

3. **Comprehensive ablation study validates every component.** Table 4 systematically ablates GRPO, each operator (injection, replacement, crossover, simplification), diversity-aware selection, collapse mechanism, and three reward variants. GRPO removal causes the largest drop (OBP gap from 0.71% → 1.78%), and each operator contributes positively. The collapse mechanism and diversity-aware crossover are each shown to outperform their ablations.

4. **Operators alone (API variant without RL) are competitive with prior SOTA.** CALM with GPT-4o-mini (G=1, no GRPO) achieves performance on par with or exceeding MCTS-AHD across most benchmarks (e.g., OBP avg gap 0.82% vs MCTS-AHD's 0.89%). This isolates the contribution of the verbal-gradient design (evolutionary operators) from the RL component.

5. **Practical resource footprint.** CALM fine-tunes only 1.15% of a quantized 7B model's weights on a single 24GB GPU, contrasting with API-dependent baselines. This makes the method accessible to researchers without access to expensive API budgets.

## Weaknesses

### Fatal
None.

### Major

1. **Evaluation budget units are not directly comparable, and G is undisclosed.** The paper states "1,000 heuristic evaluations for baselines and a fixed budget of 2,000 LLM queries for CALM" (§5, baseline paragraph). For CALM, each LLM query generates G response candidates that are all evaluated. The value of G for the main (local, with GRPO) experiments is never stated in the visible portion (only the API ablation mentions G=1). If G > 1, CALM evaluates 2,000×G heuristics vs. the baselines' 1,000 — a substantial multiple. While the paper frames these as "comparable" budgets, the units (LLM queries vs. heuristic evaluations) differ, making the comparison non-transparent. The authors should either (a) state G explicitly and match the number of evaluated heuristics, or (b) present results where CALM is limited to G=1 and the same total number of evaluations. The API ablation (G=1, GPT-4o-mini) partially addresses this concern, but it uses a much stronger backbone model, so it does not resolve the budget issue for the main local-model result.

2. **Missing statistical significance in main results tables.** All main results (Tables 1–3) report averages over 3 runs without standard deviations, confidence intervals, or p-values. Figure 2 does show std. dev. for one training curve, and Appendix I is referenced for p-values, but the core comparative tables lack variance information. With only 3 runs, some differences could be within noise. For a paper claiming to outperform SOTA, this omission weakens the evidence.

### Minor

1. **Value of G for the main experiments is not reported.** The paper never specifies how many responses are sampled per prompt (G) when using the local model with GRPO. This is essential for understanding the total number of heuristics evaluated, for reproducibility, and for assessing the budget fairness concern above.

2. **Non-stationarity of prompt distribution during RL training not addressed.** The prompts used for GRPO training evolve as the heuristic pool changes, creating a non-stationary training distribution. While the collapse mechanism partially resets this, the paper does not analyze whether this causes instability, reward hacking, or overfitting to a narrow prompt distribution. Some analysis (e.g., tracking prompt diversity over time, evaluating on a fixed held-out prompt set) would strengthen the evidence that observed improvements reflect genuine learning.

### Trivial
None.

## Nice-to-Haves

- **Operator ablation in the no-GRPO (API) setting.** Currently Table 4 ablates operators only in the full CALM (with GRPO). Adding a column for the API variant (no GRPO) would directly test whether the injection/replacement operators enhance the RL benefit specifically, as argued in §4.1.
- **Headline computational cost in main text.** Appendix I reportedly includes runtime, but a headline number (e.g., "fine-tuning adds X hours") in the main paper would help contextualize the method's efficiency.
- **Sensitivity to seed heuristics.** The paper uses seed heuristics from Zheng et al. (2025); an experiment starting from a different set would demonstrate robustness.

## Removed Points

- **Non-stationarity as a fatal/structural flaw:** The harsh critic claimed GRPO assumes i.i.d. prompts, but GRPO (like standard RL for LLMs) does not require i.i.d. prompts — the prompts come from whatever distribution the policy is deployed on. The evolutionary feedback loop is an inherent property of the method, not a flaw. The collapse mechanism was explicitly designed to handle prompt stagnation. This criticism is speculative — there is no evidence of actual instability — and does not rise to a major weakness. Demoted to Minor.

- **"Verbal gradient claim is misleading":** The harsh critic claimed the paper's statement that "even without RL… CALM's verbal guidance remains highly effective" could mislead readers into thinking the operators work well on the local model. However, the passage (§5.2) explicitly says "switching the backend to the GPT-4o-mini API, setting G=1" — the scope is clearly the API setting. The paper is accurate in context. Removed.

- **Competitive advantage due to more evaluations:** The harsh critic asserted the budget issue is "structural" and "invalidates the primary empirical claim." This overstates the case. The API ablation (G=1, GPT-4o-mini) shows that the operators themselves are competitive even without RL and with fewer evaluations per query. The local CALM with RL uses a *weaker* backbone model; its advantage comes from RL adaptation, not just raw evaluation count. Demoted from Fatal to Major since the paper is transparent about budget units, and the API variant provides a relevant (though imperfect) control.

- **Formatting/style nitpicks** and comments about proofs being in the appendix (which was stripped by the parser). Removed.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. State the value of G explicitly for the main (local + GRPO) experiments. If G>1, compare against baselines with the same total number of evaluated heuristics, or at minimum provide an analysis showing performance vs. budget for varying G.
2. Add standard deviations (or 95% CI) to the main results tables (Tables 1–3). With only 3 runs, this is essential for readers to assess reliability.
3. Include an analysis of prompt diversity over the training trajectory to address the non-stationarity concern — at minimum, note that the collapse mechanism resets the distribution.
4. Add a dedicated limitations section discussing: reliance on a simulation environment, sensitivity to reward hyperparameters, and the non-stationary training setting.

## Score and Decision

**Bracketing (Round 1):** Queried for similar LLM-for-AHD papers. Weak anchors (score < 3.5): TPD-AHD (3.00, Reject), EvoPH (2.00, Reject) — both rejected primarily for limited novelty and weak methodology, unlike CALM. Middle anchors (3.5–7.5): RFTHGS (6.00, Accept) — RL fine-tuning for CVRP heuristics, similar contribution; MoH (5.00, Accept) — meta-optimization for AHD, but weaker novelty; HeuriGym (6.00, Accept) — benchmark paper; HELIX (5.00, Accept) — evolutionary RL for scientific problems. Strong anchors (>7.5): all on different topics (geometry LLM, RL world models, etc.).
→ **Bracket: 5.0–7.0.**

**Narrowing (Round 2):** Within the bracket, queried for the closest methodological match: RFTHGS (6.00) is the most comparable — both use RL fine-tuning of an LLM for heuristic generation. CALM is stronger in breadth (4 tasks vs. 1) and ablation thoroughness, and weaker only in budget transparency. MoH (5.00) and HELIX (5.00) have weaker novelty or less rigorous evaluation. CALM is clearly above these.
→ **Final: 6.0.**

**Calibration anchors:**

| Path | Avg Score | Round | Comparison |
|------|-----------|-------|------------|
| TPD-AHD (VEMknlIPtM) | 3.00 | R1 weak | Much weaker — limited novelty, no RL fine-tuning |
| EvoPH (oD9RwlFqEE) | 2.00 | R1 weak | Much weaker — co-evolution claimed but no RL fine-tuning |
| RFTHGS (aITKXFeivk) | 6.00 | R1 middle | Comparable — RL FT for CVRP; CALM broader but less budget-transparent |
| MoH (tIQZ7pVN6S) | 5.00 | R1 middle | Weaker — meta-optimization at prompt level, less novel than RL FT |
| HeuriGym (HWxHUO15Yy) | 6.00 | R1 middle | Different contribution (benchmark paper) |
| HELIX (2CHz6NYBmd) | 5.00 | R2 narrow | Similar concept (GRPO+evolution) but less rigorous evaluation |
| RedAHD (6f8qlK7wN4) | 5.33 | R1 middle | Different approach (reduction-based), less thorough ablation |

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>