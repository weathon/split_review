Now I have sufficient calibration data to finalize my score. Let me compose the review.

**Calibration Summary:**

**Round 1 (Bracketing):**
- Weak band (<3.5): LLM4Solver (3.40), Unifying All Species (2.50), LLMatic (3.40) — papers with limited novelty, weak evaluation, or incremental contributions built on existing LLM+EA frameworks
- Middle band (3.5–7.5): Hercules (5.25), LLM-LNS (5.25), LLM-LNS (5.25), Q-shaping (5.67) — papers in the LLM+optimization space with meaningful but incremental contributions
- Strong band (>7.5): WizardMath (8.00), MaestroMotif (7.75), LLAMBO (8.00) — papers with clear, significant novel methodology and thorough evaluation

**Round 1 Bracket:** 4.5 to 7.5

**Round 2 (Narrowing):**
- Hercules (5.25, very similar domain) — uses LLM for heuristic generation but only prompt-level changes; CALM's RL fine-tuning is genuinely more novel. However, Hercules didn't have a budget fairness issue.
- EVOPROMPT (6.50) — LLM+EA for prompt optimization; scored 6,8,6,6, accepted at ICLR. CALM has a stronger novelty dimension (RL on the LLM itself rather than just replacing GA operators). CALM is comparable or slightly stronger.
- LLM-LNS (5.25) — LLM+EA for MILP LNS; criticized for unclear novelty. CALM is clearly stronger.
- MOLLEO (7.00) — LLM+EA for molecular discovery; scored 6,6,8,8. Different domain, but similar methodology. CALM's core novelty (RL fine-tuning the LLM itself) is actually stronger than MOLLEO's (replacing GA operators with LLMs), but CALM has the budget asymmetry concern.

**Final Score:** 6.5 — Stronger than Hercules/LLM-LNS (mid-5s) due to genuine novelty of RL fine-tuning and thorough ablation, comparable to EVOPROMPT (6.5) in overall quality, but below the MOLLEO (7.00) / WizardMath (8.00) range due to the unresolved budget fairness question and missing variance in main tables.

Now let me write the consolidated review.

For the weaknesses, let me apply my filtering:

**From Harsh Critic:**

1. **Asymmetric evaluation budgets** → Keep as MAJOR. The paper acknowledges it but doesn't fully address it. Table 4 and the API variant partially mitigate it but don't fully resolve the concern.

2. **Missing statistical significance** → Keep as MINOR. The main tables report only means. But the appendix has p-values per line 276, and Figure 2 shows std dev. So partial info exists but not in main tables.

3. **Inconsistent baseline API model selection** → REMOVE. The paper reports BOTH GPT-3.5-turbo and GPT-4o-mini for baselines on TSP. This is comprehensive, not cherry-picking.

4. **Group size G not specified** → Keep as TRIVIAL. Stated to be in the appendix.

5. **Computational cost** → Move to NICE-TO-HAVE.

6. **Why GRPO over DPO** → Partially addressed in related work (line 56 mentions EvoTune uses DPO and this work uses GRPO as different approach). Move to NICE-TO-HAVE as brief discussion would help.

**From Strength Finder:**
All strengths seem valid with concrete evidence. Let me keep them but compress.

Let me now write the final review.## Summary

This paper proposes CALM, a framework for automatic heuristic design (AHD) that co-evolves an LLM with the heuristic search process by combining verbal guidance (evolutionary prompt operators) with numerical guidance (RL fine-tuning via GRPO). Unlike prior work that keeps the LLM frozen and only manipulates prompts, CALM fine-tunes a quantized 7B model locally on a 24GB GPU using performance data generated during the evolutionary loop. The method is evaluated across four optimization tasks (OBP, TSP, CVRP, OP) and shown to outperform prior SOTA methods including those using more powerful API-based models (GPT-4o-mini). The core insight—that the evolutionary process naturally produces prompt-response-performance triplets usable as RL training data—is clean and practically impactful.

## Strengths

1. **Genuinely new methodological dimension for LLM-based AHD.** Prior LLM-based AHD methods keep the underlying LLM frozen and only manipulate prompts. CALM is one of the first frameworks to jointly optimize both the prompt generation process and the LLM itself via RL fine-tuning. The ablation (Table 4) confirms that RL provides the largest single performance gain across all ablated components (OBP: 0.71% vs. 1.78% without GRPO; OP: 17.41% vs. 19.89% without GRPO).

2. **A quantized 7B model with GRPO outperforms GPT-4o-mini-based baselines.** Tables 1–3 show that CALM using Qwen2.5-7B-Instruct-INT4 + GRPO achieves better average optimality gaps than methods powered by GPT-4o-mini (e.g., OBP avg 0.71% vs. MCTS-AHD 0.89%; CVRP N=200: 3.95% vs. MCTS-AHD 4.70%; OP N=100: 15.43% vs. HSEvo 16.13%). This is notable given the substantial gap in raw model capability and the fact that CALM runs entirely on consumer hardware.

3. **Verbal guidance alone (without RL) already matches or exceeds prior SOTA.** The API-based variant of CALM (GPT-4o-mini, G=1, matching prior query budgets) delivers competitive performance across all tasks, demonstrating that the operator design itself (fine-granularity injection/replacement injection, diversity-aware crossover) is a meaningful contribution independent of the RL component.

4. **Thorough ablation with 11 settings isolating each component's contribution.** Table 4 systematically evaluates the impact of RL, collapse mechanism (including hyperparameter sweeps), reward design variants, and each evolutionary operator. This provides strong internal validity for the architectural choices.

5. **Fair comparison with concurrent fine-tuning approach (EvoTune).** CALM is compared against EvoTune using the same base model (Qwen2.5-7B-Instruct-INT4), providing a clean head-to-head between GRPO and DPO-based fine-tuning for AHD. CALM outperforms EvoTune on all tasks (e.g., TSP N=100: 11.58% vs. 12.99%; CVRP N=50: 3.83% vs. 5.82%).

## Weaknesses

### Fatal
None.

### Major

- **Asymmetric evaluation budget between CALM and baselines weakens the headline "outperforms SOTA" claim.** The paper states that baselines use 1,000 heuristic evaluations while CALM uses 2,000 LLM queries (with G responses per query, each evaluated) for TSP, CVRP, and OP. Since each CALM query generates G ≥ 1 responses that are all evaluated, the total number of heuristic evaluations for CALM can be substantially larger than the baselines' 1,000. The paper acknowledges this disparity but does not control for it in the main comparisons (Tables 1–3). The impact is partially mitigated by: (a) the API-based variant (Section 5.2), which uses G=1 and matching query budgets and already performs competitively, and (b) the OBP setting where CALM uses fewer queries than baselines (2,000 vs. 4,000+) yet still wins. However, the central claim that "a local 7B model with RL outperforms API-based SOTA" would be more convincing with a controlled budget comparison (e.g., running the strongest baselines at 2,000 queries or CALM at 1,000).

### Minor

- **Main results tables report only means without variance.** All main results (Tables 1–3) are reported as averages over three runs without standard deviations, confidence intervals, or statistical tests. Several comparisons are close (e.g., TSP N=50: CALM 10.04% vs. MCTS-AHD 9.69%; TSP N=100: 11.58% vs. 11.79%), and without variance the reader cannot assess stability or significance. The paper mentions p-values in Appendix I (line 276) and Figure 2 shows std. dev. shaded for training curves, but the primary evidence tables should include variance information.

### Trivial

- **Key hyperparameter G (GRPO group size) is not stated in the main text.** The value of G is referenced throughout the methodology (Sections 3.2, 4, 4.2) but its specific value is deferred to the appendix. Since G directly affects the number of heuristic evaluations per round and thus the evaluation budget, it should appear in Section 4 or 5.

- **The collapse mechanism is described verbally and via an analytical approximation (Eq. 2), but the hard cap C and rate δ₀ values used in experiments are not given in the main text.** They appear only in ablation configurations in Table 4 for OBP/OP; the actual default values for main experiments are unclear.

## Nice-to-Haves

- **Wall-clock time and computational cost.** A breakdown of runtime (e.g., hours per task on a 24GB GPU) would help readers assess practical deployability.
- **Brief discussion of why GRPO is preferred over DPO for this setting.** The related work notes EvoTune uses DPO, but an explicit rationale for GRPO (e.g., avoids training a reward model, works with scalar rewards) would strengthen the positioning.
- **Controlled-budget comparison.** Running the strongest baselines (MCTS-AHD, EoH) at 2,000 queries (or CALM at 1,000) on one representative task would directly resolve the primary fairness concern.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **"Inconsistent baseline API model selection (cherry-picking)."** The paper reports BOTH GPT-3.5-turbo and GPT-4o-mini results for baselines on TSP (Table 2). Reporting multiple backends is comprehensive, not cherry-picking. The reader can see both comparisons. **Removed as factually incorrect.**
- **"Missing statistical significance entirely."** The paper explicitly mentions in line 276 that statistical significance (p-values) is reported in Appendix I. Figure 2 shows std. dev. shaded. The criticism is better reframed as "variance is missing from main tables" (now under Minor). **Downgraded from general claim to specific presentation issue.**

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. **Add standard deviations to all main results tables (Tables 1–3).** With three runs, a simple mean ± std format would let readers assess which comparisons are reliable.
2. **Run one controlled-budget experiment** where the strongest baseline (e.g., MCTS-AHD) is evaluated at CALM's query budget, or CALM is evaluated at the baseline budget, on a representative task such as TSP N=100. This would directly address the primary fairness concern.
3. **Move key hyperparameters (G, C, δ₀) into the main text** — they are needed to understand the method's resource footprint.
4. **Add a brief wall-clock cost table in the main text** (even 2–3 lines) to help readers assess practical feasibility.

## Score and Decision

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>