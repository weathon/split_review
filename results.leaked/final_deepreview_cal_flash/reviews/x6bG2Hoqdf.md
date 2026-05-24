Now I have sufficient calibration anchors. Let me finalize my assessment and write the review.

**Round 1 bracket:** Between 4.5 and 7.0 (CALM is clearly stronger than the weak 2.5-3.4 anchors in the low band, but has evaluation concerns that keep it from the 7.5+ band).

**Round 2 narrowing:** Compared to Hercules (5.25), LLM-LNS (5.25), and FunBO (5.80), CALM has stronger novelty and more comprehensive ablation. Compared to REvolve (6.00, Accept) and EvoPrompt (6.50, Accept), CALM's core contribution is at least as novel, but the budget ambiguity is a weakness those papers don't share. MoLLEO (7.00, Accept) has a cleaner evaluation but its novelty (LLM as genetic operator) is less fundamental.

**Final score:** 6.0 — a solid contribution with genuine novelty that is held back by a clearly identifiable evaluation issue (budget comparability) that should be fixable.

Now let me write the full review.

---

Let me also re-verify the harsh critic's claim about the API variant on CVRP. The paper says "matches MCTS-AHD and outperforms all other baselines on every CVRP test set." 

Looking at Table 3:
- N=50: CALM (API) 5.81% vs MCTS-AHD 5.44% — CALM is worse
- N=100: CALM (API) 7.46% vs MCTS-AHD 6.98% — CALM is worse
- N=200: CALM (API) 5.72% vs MCTS-AHD 4.70% — CALM is worse

So on CVRP, CALM (API) is consistently worse than MCTS-AHD. Claiming "matches" is not accurate. The claim should be "competitive with" or "close to but slightly behind."

This is a minor overclaim but the harsh critic is correct that it should be fixed.

OK, now let me draft the full review.## Summary

This paper introduces CALM, a framework for LLM-based automatic heuristic design that goes beyond prior work by enabling the underlying LLM to be fine-tuned via reinforcement learning (GRPO) during the evolutionary search process. The key innovation is combining *verbal guidance* (prompt manipulation through evolutionary operators) with *numerical guidance* (RL-based model fine-tuning using heuristic performance as reward). CALM runs locally on a single 24GB GPU with an INT4-quantized 7B model and demonstrates consistent improvements over state-of-the-art baselines across four challenging optimization benchmarks (OBP, TSP, CVRP, OP), with the ablation study confirming that the RL fine-tuning component is the most critical factor.

## Strengths

- **Co-evolution via RL fine-tuning is the first demonstration of on-the-fly LLM adaptation for AHD.** Prior LLM-based AHD methods keep the LLM frozen and only manipulate prompts. CALM treats the evolutionary loop as a source of training data and uses GRPO to adapt the LLM itself. The ablation study (Table 4) provides direct evidence: disabling GRPO causes the largest performance drop among all modifications, and a local INT4-quantized 7B model with RL outperforms the same prompt operators using GPT-4o-mini without RL. This is a genuine advance over the existing paradigm.

- **Comprehensive ablation isolates every component's contribution.** Table 4 systematically tests removal of GRPO, the collapse mechanism (with four hyperparameter settings), the reward design (two alternatives), crossover, injection, replacement, simplification, and the diversity-aware crossover. All degrade performance when removed. This level of thoroughness is a significant strength and makes the paper's mechanistic claims credible.

- **Consistent superiority across four diverse optimization tasks with a weaker model.** CALM (local, with GRPO) achieves the best average optimality gap on OBP (0.71% vs 0.89% for MCTS-AHD), best results on CVRP across all scales (3.83%/5.44%/3.95% vs next-best 5.44%/6.98%/4.70%), best results on OP at N=100 and N=200, and competitive results on TSP — all while using an INT4-quantized 7B model that is explicitly weaker than the GPT-4o-mini used by baselines. This breadth and the directional consistency support the claim that the framework generalizes.

- **Practical resource efficiency.** The entire pipeline runs on a single 24GB GPU, avoiding reliance on commercial API access. This lowers the barrier to adoption and enables reproducible research on modest hardware.

## Weaknesses

### Fatal
None.

### Major

- **Evaluation budget is described in incommensurate units, making the headline comparisons harder to interpret.** The paper states that baselines receive "1,000 heuristic evaluations" while CALM operates under "a fixed budget of 2,000 LLM queries." These are different units. For the API variant (G=1, setting stated), 2,000 queries = 2,000 heuristic evaluations, which is 2× the baseline budget. For the local GRPO variant, the number of responses per prompt G is not reported, so the total number of heuristic evaluations is unknowable from the main text (2,000 × G). Because G is a critical parameter that directly affects both the method's cost and the fairness of comparisons, it must be reported. The authors should either equalize the *heuristic evaluation* budget across conditions or clearly state G and explain why the comparison is meaningful despite the asymmetry. This does not invalidate the paper's contributions — the ablation study (Table 4) is internally controlled, and the asymmetric comparison (weaker model vs. stronger API models) partially justifies a budget difference — but it prevents a clean reading of the central empirical claims.

### Minor

- **The claim about the API variant "matching" MCTS-AHD on CVRP is slightly overstated.** The paper states that the API-based CALM (without GRPO) "matches MCTS-AHD and outperforms all other baselines on every CVRP test set." The data in Table 3 show that CALM (API) is consistently *worse* than MCTS-AHD on CVRP at N=50 (5.81% vs 5.44%), N=100 (7.46% vs 6.98%), and N=200 (5.72% vs 4.70%). While the gaps are small and the API variant is certainly competitive, the phrasing should be corrected to accurately reflect the direction of the comparison. The broader claim that the API variant is "on par with or superior to" MCTS-AHD overall is reasonable across tasks, but the CVRP-specific statement needs refinement.

- **The ablation comparison between "local, w/ GRPO" and "local, w/o GRPO" (Table 4) does not explicitly confirm equal heuristic evaluation budgets.** If these two conditions use different numbers of total evaluations (due to different settings of G or T), the large performance gap could partly reflect differential search effort rather than the presence/absence of RL. The paper should state the evaluation counts for each condition so the reader can verify the comparison is controlled on this dimension.

### Trivial
None.

## Nice-to-Haves

- The collapse mechanism's analytical approximation (Equation 2) is a nice theoretical touch, though its derivation is deferred to the appendix. A brief sketch or intuition in the main text would help readers assess its validity without hunting the appendix.
- Including standard deviations or confidence intervals for the main results (Tables 1–3) would improve interpretability, especially for the close comparisons (e.g., OBP 0.71% vs 0.82%).
- Since the paper uses Unsloth for efficient fine-tuning, specifying which fine-tuning method (LoRA, DoRA, etc.), rank, alpha, and target modules are used would aid reproducibility, though these details may already be in the stripped appendix.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **Missing value of G and fine-tuning hyperparameters as a standalone weakness:** The harsh critic claimed that G and fine-tuning details are missing. These may be reported in Appendix H (stripped by the parser). Per the hard rules, weaknesses about content potentially present in the stripped appendix are removed. The budget-related concern about G is subsumed by the Major weakness above.
- **Collapse mechanism's analytical derivation is unverifiable (Criticism #4):** The derivation is in Appendix G (stripped). The empirical results in Table 4 do support the paper's claims about the collapse mechanism generally helping. This criticism was grounded in the missing appendix, not in the paper as presented.
- **Duplicate HSEvo row in Table 3:** The harsh critic noted this as a parser artifact. Per the rules, formatting artifacts from PDF extraction are ignored.
- **GRPO description lacks concrete mapping:** The paper does provide this mapping in Section 4 (prompt q = operator output, response o = LLM output, reward based on heuristic quality). The mapping is clear from the context.
- **Statistical significance missing from main paper:** The paper states that p-values and significance tests are in Appendix I. Per the rules, deferred appendix content is not a missing-element weakness.
- **Overstated claim about collapse mechanism's empirical support:** The critic claimed the numbers are "messy" and contradict the paper's claims. Re-examining Table 4, the collapse mechanism improves results in most configurations (e.g., OBP 0.77% vs 0.98% without collapse), and the paper's conclusions are reasonable given the data.

## Novel Insights

The most interesting observation from synthesizing the reviews is that the paper's strongest evidence for its core contribution (co-evolution is valuable) actually comes from the ablation study (Table 4) rather than the inter-method comparisons (Tables 1–3). This is because the ablation cleanly isolates the RL fine-tuning effect within a controlled framework, while the inter-method comparisons are confounded by model strength and evaluation budget differences. The authors would strengthen the paper by leading with this evidence rather than making the API-variant comparisons the centerpiece of their claims. The training curves in Figure 2 — showing the local RL variant starting behind GPT-4o-mini baselines and overtaking them — are also a compelling visualization of the co-evolution effect that deserves more narrative attention.

## Suggestions

1. **Report G and equalize (or clearly justify) the evaluation budget.** This is the most actionable fix. State G explicitly for the local GRPO variant. Either run baselines at the same number of heuristic evaluations as CALM, or clearly explain the trade-off (weaker model compensates with more search budget) and bound the budget ratio.
2. **Correct the CVRP claim** to say "competitive with MCTS-AHD" rather than "matches MCTS-AHD," since the data show CALM (API) is consistently worse on this task.
3. **In Table 4, report the number of heuristic evaluations used in each ablation condition** so readers can verify that the GRPO vs. no-GRPO comparison is not confounded by unequal search effort.
4. **Briefly sketch the intuition behind Equation (2)** in the main text (even one sentence on the derivation logic) so the analytical claim is assessable without the appendix.

## Score and Decision

**Calibration anchors used:**
- Low-band (score < 3.5): XTxdDEFR6D (3.40, Reject — LLM4Solver, similar AHD topic but weaker results and evaluation), iTrd5xyHLP (3.40, Reject — LLMatic, NAS with LLMs, incremental)
- Middle-band (3.5–7.5): 0fwJMANq9P (5.25, Reject — Hercules, incremental LLM-based AHD with evaluation concerns), Usk4KzBxLW (5.25, Reject — LLM-LNS, lacks ablation), DlqRpj68xe (5.67, Reject — Q-shaping, theoretical concerns), cJPUpL8mOw (6.00, Accept — REvolve, solid LLM+EA for reward design), ZG3RaNIsO8 (6.50, Accept — EvoPrompt, LLM+EA for prompt optimization)
- Upper-band (score > 7.5): awWiNvQwf3 (7.00, Accept — MoLLEO, LLM+EA for molecular discovery, stronger evaluation)

**Round 1 bracket:** 4.5–7.0 — CALM is clearly stronger than the low-band AHD papers (evaluation breadth, ablation quality) but has a budget comparability issue that papers in the 7+ range don't share.

**Round 2 narrowing:** CALM is stronger than Hercules (5.25) and LLM-LNS (5.25) — both Reject — in novelty and experimental rigor. It is comparable to REvolve (6.00, Accept): both have genuine core ideas and solid ablation, but each has a specific evaluation concern (human effort in REvolve, budget ambiguity in CALM). CALM is slightly weaker than EvoPrompt (6.50, Accept), which has a cleaner evaluation despite less fundamental novelty. The budget issue is the main factor separating CALM from the 6.5+ range.

Round 1 bracket: 4.5–7.0. Round 2 placed the paper close to REvolve (6.00). The novelty and ablation quality are solid; the budget ambiguity is a real but fixable weakness.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>