Now let me read a bit more of the paper and then proceed to calibration searches.Now I have enough information to write the final consolidated review. Let me put it together.

---

## Summary

CALM (Co-Evolution of Algorithms and Language Model) is a new framework for Automatic Heuristic Design (AHD) that combines "verbal guidance" (specialized evolutionary operators for prompt generation) with "numerical guidance" (online RL fine-tuning of the LLM via GRPO). Running locally on a single 24GB GPU with a quantized 7B model, CALM is the first AHD framework to jointly adapt both prompt generation and the LLM itself, enabling a weaker local model to surpass frozen API-based methods (GPT-4o-mini) on four combinatorial optimization benchmarks.

---

## Strengths

- **RL fine-tuned local model beats frozen API-based methods.** On OBP (Table 1), CALM achieves a 0.71% average optimality gap versus MCTS-AHD's 0.89%, using half the query budget. On CVRP at all three scales, CALM dominates all GPT-4o-mini baselines: N=50 (3.83% vs. 5.44% for MCTS-AHD), N=100 (5.44% vs. 6.98%), N=200 (3.95% vs. 4.70%). These margins support the paper's central claim that RL-fine-tuning over a weaker local model can compensate for—and surpass—a stronger frozen model.

- **Ablation cleanly isolates RL as the dominant driver.** Table 4 shows that removing GRPO is the single largest performance hit across both ablation tasks: OBP gap degrades from 0.71% to 1.78%, and OP gap from 17.41% to 19.89%. Among the three alternative reward functions tested, only the paper's proposed design succeeds, confirming the importance of the relative-improvement credit assignment.

- **New operators improve search efficacy independently of RL.** Ablation results (Table 4) show that CALM without crossover raises OBP gap to 0.88%, removing injection raises it to 1.11%, and removing simplification gives the largest single-operator drop (1.35% OBP). The diversity-aware crossover is also shown to be essential: using only performance-based crossover performs worse than no crossover at all, establishing the specific design contribution of the diversity-aware mechanism.

- **Collapse mechanism has measurable benefit and is analytically grounded.** Disabling collapse degrades OBP gap from 0.71% to 0.98% and OP gap from 17.41% to 19.57% (Table 4). Equation (2) provides an analytical approximation for expected collapse timing, enabling principled hyperparameter selection.

- **The cleanest same-model comparison (CALM vs. EvoTune, both Qwen2.5-7B-INT4 + RL) consistently favors CALM.** Across all four tasks and all test scales, CALM outperforms EvoTune, often by large margins (e.g., OP N=200: 12.58% vs. 20.32%; TSP N=200: 13.41% vs. 16.60%). Since EvoTune also uses RL fine-tuning, this gap reflects CALM's specialized operator and reward design rather than the presence of RL alone.

---

## Weaknesses

### Fatal
None.

### Major

None verified. The budget comparison issue is real but does not invalidate the core contribution.

### Minor

- **Budget comparison is not transparently documented.** Section 5 states "1,000 heuristic evaluations for baselines and a fixed budget of 2,000 LLM queries for CALM." The distinction between "LLM queries" and "heuristic evaluations" is not explained (the former includes invalid responses that generate no heuristic). For non-OBP tasks where CALM's margin over MCTS-AHD is tighter—e.g., TSP N=50 in-domain CALM (10.04%) vs. MCTS-AHD (9.69%), and OP N=50 in-domain CALM (24.22%) vs. MCTS-AHD (25.27%)—the budget relationship matters. The GRPO group size G is not stated in the main text, making it impossible for a reader to compute the total number of heuristics CALM evaluates per run. The OBP comparison actually favors the *baselines* (they receive ≥4,000 queries vs. CALM's 2,000), which is the paper's clearest win. For non-OBP tasks, a single sentence clarifying that G × T_rounds = 2,000 total response generations (or equivalent) would resolve the ambiguity.

- **Two unexplained rows for HSEvo in Table 3.** Lines 206–207 of the parsed paper show two rows both labeled "HSEvo" with materially different numbers (CVRP N=50: 7.54% vs. 6.11%; OP N=50: 23.98% vs. 24.08%). No explanation is provided. This matters because CALM (24.22%) is *worse* than both HSEvo rows on OP N=50 in-domain, even though the abstract claims to "outperform SOTA baselines across various optimization tasks." The paper body correctly qualifies this ("it still outperforms EoH and the most recent approach, MCTS-AHD and EvoTune"), but the table anomaly should be explained—e.g., whether these are two separate configurations of HSEvo.

- **Cross-model comparison conflates model quality with RL adaptation.** Headline numbers compare CALM's GRPO-fine-tuned Qwen2.5-7B-INT4 against frozen GPT-4o-mini baselines. The paper acknowledges in Section 5 that "GPT-4o-mini-based baselines retain a clear advantage in raw accuracy." Because the model quality gap and the RL adaptation work in opposite directions, the cross-model comparison—while technically supported—requires a more careful framing in the abstract and introduction to avoid being read as a pure method comparison.

### Trivial

- **Collapse hyperparameter guidance is implicit.** Table 4 shows that δ₀=0.005, C=15 (aggressive collapse) badly hurts OP (27.22% vs. 17.41%). The paper discusses this in Section 5.2 but does not provide guidance on safe tuning ranges. A brief rule of thumb or practical recommendation tied to Equation (2) would improve the utility of this mechanism.

- **Reward function edge case is unaddressed.** The duplicate-heuristic penalty (Eq. 4, first case) triggers when `g(h_new) = g(h_t_base)` for *any* base heuristic, meaning structurally novel heuristics that happen to match a base heuristic's training-set performance (plausible on the small CVRP training set of 10 instances) receive a small negative reward. This is a minor theoretical edge case but not discussed.

---

## Nice-to-Haves

- **Equal-budget comparison.** Running MCTS-AHD and EvoTune at 2,000 heuristic evaluations (matching CALM's stated budget) for at least one task would make the cross-model comparison conclusive. If CALM still wins, the evidence is airtight.

- **Cross-problem transfer experiment.** CALM fine-tunes a fresh model for each problem from scratch. Testing whether fine-tuned weights transfer across tasks (e.g., initializing CVRP fine-tuning from OBP-fine-tuned weights) would either reveal positive transfer (strengthening the "co-evolution" framing) or clarify the contribution as per-problem adaptation.

- **Sensitivity analysis for G.** A brief study varying GRPO group size G would characterize the trade-off between exploration diversity and training efficiency.

---

## Removed Points

*These points are flagged to be removed; treat them with caution.*

- **Wall-clock efficiency absent from main body.** The harsh critic notes the runtime comparison is in Appendix I but not in the main paper body. Per review rules, appendix content is stripped from all parsed papers and should not be penalized.

- **AlphaEvolve / OpenEvolve availability concerns.** The harsh critic implicitly flags these; per review rules, if the paper cites them, they exist.

- **Generic "model quality conflation is fatal."** The harsh critic frames this as a potential "structural flaw," but the paper explicitly discloses the model quality hierarchy in Section 5 and the same-model comparison (CALM vs. EvoTune) is clean. This is not a structural flaw.

- **OP in-domain SOTA overclaim (abstract).** While technically the abstract's "outperforms SOTA" is slightly overreaching for OP N=50 in-domain (where HSEvo beats CALM), the paper body text correctly qualifies this. The abstract claim is slightly imprecise but not a core scientific error; retained only as a Minor issue.

- **Budget issue elevated to "fatal."** The harsh critic calls the budget comparison "evidential" and suggests CALM may merely be exploring longer. However, (a) the same-model comparison (CALM vs. EvoTune) is budget-neutral and strongly favors CALM, (b) for OBP CALM wins with strictly fewer queries than baselines, and (c) on CVRP CALM's margins are substantial, not marginal. Demoted to Minor.

---

## Novel Insights

CALM demonstrates that online GRPO fine-tuning can be effectively integrated into an evolutionary LLM-based heuristic search loop, yielding a model that progressively improves its own generation capability from the reward signal provided by heuristic evaluations. The ablation evidence is especially instructive: GRPO is the single most impactful component (larger effect than any individual operator or the collapse mechanism), and the reward design—specifically the relative-to-parent improvement scoring—is critical; performance-proportional alternatives actually degrade below the no-RL baseline on OP. This suggests that credit assignment in RL for code generation is highly sensitive to prompt confounders, and that normalizing by parent performance is a principled design choice worth generalizing to other AHD and program synthesis settings.

---

## Suggestions

1. **Clarify the budget.** In Section 5's implementation details (main text), state explicitly: (a) the value of G, (b) the total number of heuristics CALM evaluates per run (= G × number of rounds), and (c) the corresponding count for each baseline. This turns the current ambiguity into a transparent and favorable comparison for OBP and a known-bounded comparison for other tasks.

2. **Explain or remove the duplicate HSEvo rows.** Either label the second row (e.g., "HSEvo†" with a footnote about the configuration) or remove it if it is a parser/transcription artifact.

3. **Soften the abstract.** Replace "outperforms state-of-the-art baselines" with a more precise claim such as "achieves best-or-second-best performance across all tested optimization tasks" or note that CALM beats MCTS-AHD—the most recent prior SOTA—on all tasks.

4. **Report p-values or confidence intervals for the key cross-model comparisons** in the main text, especially for TSP N=50 in-domain where the gap between CALM (10.04%) and MCTS-AHD (9.69%) is small.

---

## Score and Decision

**Calibration anchors retrieved:**

| Paper | Path | Avg Score | Round | Comparison |
|---|---|---|---|---|
| LLM4Solver | XTxdDEFR6D.md | 3.40 | R1 weak | Simpler contribution, weaker experiments than CALM |
| LLM-based Hyper-Heuristics (MHRE) | sUywd7UhFT.md | 2.50 | R1 weak | Multi-objective but much weaker contribution |
| Efficient Heuristics Gen. (Hercules) | 0fwJMANq9P.md | 5.25 | R1 mid | Similar domain (LLM + AHD), less novel (no RL fine-tuning), more contested experiments |
| LLM-LNS | Usk4KzBxLW.md | 5.25 | R1 mid | LLM-guided LNS for MILP, solid but narrower contribution |
| LLM-SR | m2nmp8P5in.md | 8.00 | R1 strong | LLM for scientific equation discovery, highly rigorous, accepted broadly |
| LLAMBO | OOxotBmGol.md | 8.00 | R1 strong | LLMs for Bayesian optimization, very polished |
| EvoPrompting | ZG3RaNIsO8.md | 6.50 | R2 | LLMs + EAs for prompt optimization; CALM is more technically sophisticated and practically important |
| Learning Code Perf. Edits | ix7rLVHXyY.md | 7.25 | R2 | Code performance optimization via LLM fine-tuning; larger dataset and cleaner evaluation than CALM |
| Multi-turn Code Gen. | Zk9guOl9NS.md | 7.00 | R2 | Prompting strategies for code; different domain |
| REvolve | cJPUpL8mOw.md | 6.00 | R2 | LLMs for reward function design via evolution; similar spirit, accepted |

**Round 1 bracket:** 5.5–7.5

**Round 2 narrowing:** CALM is clearly stronger than the 5.25 papers (Hercules, LLM-LNS) because: it introduces a genuinely new mechanism (GRPO online fine-tuning for AHD), has more thorough ablations, evaluates on more tasks, and achieves practically significant results. It is comparable to EvoPrompting (6.5) and REvolve (6.0) in terms of "solid contribution with some evaluation gaps," but CALM's novelty is arguably higher (first to combine GRPO with evolutionary AHD, unlike EvoPrompting which uses frozen LLMs with existing EA operators). CALM is below the code-editing paper (7.25) because of the budget comparison ambiguity, the unexplained HSEvo table anomaly, and the slightly overclaimed abstract. The cleanest verdict: CALM sits between 6.5 and 7.0, closer to 6.5 due to the evaluation transparency issues.

**Originality:** High — first to integrate GRPO into evolutionary AHD  
**Importance:** High — practical local execution, addresses key limitation of fixed-model AHD  
**Claims well-supported:** Moderate-high — same-model comparison is conclusive; cross-model comparison has budget opacity  
**Soundness of experiments:** Good — four tasks, three runs, comprehensive ablations  
**Clarity:** Good  
**Value to community:** High — open-source, runs on consumer GPU, reusable framework

**Final score: 6.5 — Weak Accept.** The contribution is real and non-trivial; the same-model comparison leaves no doubt that CALM's design choices improve over the RL-only baseline (EvoTune). The cross-model headline claim is slightly hampered by evaluation transparency issues but these are addressable in a revision and do not undermine the paper's core findings.

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>