I've now read and verified all the key claims. Let me produce the final consolidated review.

---

## Summary
This paper introduces CALM, a framework for Automatic Heuristic Design (AHD) that jointly evolves heuristic populations through prompt-based evolutionary operators ("verbal gradients") and fine-tunes the underlying LLM via GRPO reinforcement learning ("numerical gradients"). CALM is the first AHD method to co-evolve both the prompt generation process and the LLM itself. Using a quantized 7B model (Qwen2.5-7B-Instruct-INT4) on a single 24GB GPU, CALM discovers heuristics that surpass GPT-4o-mini-based SOTA baselines on four challenging optimization tasks (OBP, TSP, CVRP, OP).

## Strengths
- **Novel co-evolution paradigm**: CALM is the first AHD framework that jointly optimizes both the prompt generation process (via novel evolutionary operators including fine-granularity injection/replacement and diversity-aware crossover) and the LLM itself (via GRPO). This dual-gradient approach is genuinely new and well-motivated (Section 4, Figure 1).

- **Strong empirical results under tight resource constraints**: Using a quantized 7B model on a single 24GB GPU, CALM consistently beats GPT-4o-mini-based SOTA baselines (MCTS-AHD, EoH, FunSearch) across four tasks. The margins are substantial on OBP (0.71% vs 0.89% for MCTS-AHD) and CVRP (3.83% vs 5.44% at N=50). The EvoTune baseline, which also fine-tunes the same 7B model (via DPO), performs dramatically worse (2.40% on OBP), confirming CALM's GRPO-based approach is key.

- **Thorough ablation study**: Table 4 systematically ablates every component (GRPO, reward design, collapse mechanism, individual operators). The results demonstrate that GRPO is the single largest contributor to performance, that the relative-credit reward function (Eq. 3–4) outperforms simpler alternatives, and that each evolutionary operator provides measurable benefit.

- **Competitive verbal-gradient design standing alone**: Even without RL, CALM's verbal-gradient components paired with GPT-4o-mini match or exceed MCTS-AHD (e.g., 0.82% vs 0.89% average OBP gap; TSP N=200 at 13.56% vs 13.71%). This demonstrates the prompt-engineering design itself is strong and complementary to the RL contribution.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor
- **Modest improvement margins on TSP**: On TSP, CALM's advantage over MCTS-AHD narrows to 0.30 percentage points at N=200 (13.41% vs 13.71%) and CALM trails MCTS-AHD at N=50 (10.04% vs 9.69%). While the overall trend favors CALM (it wins on 2 of 3 TSP scales and all CVRP/OBP/OP out-of-domain scales), the TSP-specific evidence for the headline claim is weaker than for the other tasks. This does not invalidate the overall contribution but should be acknowledged.

- **Table 3 contains a duplicated HSEvo row** (lines 218–219): two rows with different numbers are both labeled "HSEvo" under the GPT-4o-mini section of Table 3. One likely corresponds to ReEvo, which is listed as a baseline (line 152) but absent from the CVRP/OP tables. This is a presentation error that should be corrected.

### Trivial
- Standard deviations are deferred to Appendix I rather than appearing alongside the main results (Tables 1–3), which would strengthen the reader's immediate confidence in the reported differences. (The paper does state that p-values and running time are in Appendix I, line 276.)
- The query-budget discussion (line 152) could state more clearly that for non-OBP tasks, baselines were re-evaluated under a matched budget of 1,000 heuristic evaluations.

## Nice-to-Haves
- Running a prompt-based AHD method (e.g., MCTS-AHD) using the same Qwen2.5-7B-Instruct-INT4 model would provide a direct controlled comparison isolating the effect of RL from the effect of CALM's prompt design. The existing EvoTune baseline and "local, w/o GRPO" ablation provide strong indirect evidence, but a direct same-model/same-framework comparison would be cleaner.
- An ablation on the GRPO group size G would help readers understand the sensitivity of performance to this critical hyperparameter.
- Reporting total GPU-hours for GRPO training alongside API costs of baselines would enrich the practical cost discussion.

## Removed Points
These points are flagged to be removed, treat them with caution:

- **"Missing resource-cost comparison is a methodological gap"**: The paper states running time details are in Appendix I (line 276). The parser strips appendices; this information exists in the original submission. Removed per rule: criticisms about missing appendix content are parser artifacts.

- **"On OP, CALM is slightly worse than MCTS-AHD at the in-domain scale (N=50)"**: Factually incorrect. CALM (local w/ GRPO) achieves 15.054 Obj., 24.22% Gap vs MCTS-AHD's 14.847 Obj., 25.27% Gap. Lower gap and higher objective are both better for OP. CALM *beats* MCTS-AHD at N=50.

- **"Query-budget inconsistencies inflate CALM's apparent efficiency"**: The paper explicitly discloses that for OBP, CALM uses 2,000 queries while prior methods used 4,000+. This budget asymmetry works *against* CALM (fewer resources), not in its favor. For non-OBP tasks, all methods are aligned with consistent settings. The transparency here is a strength, not a weakness.

- **"Missing baseline: prompt-based AHD with the same local model" as a structural/fatal gap**: The paper includes EvoTune (same Qwen2.5-7B-Instruct-INT4 model, fine-tuned via DPO) as a direct comparison, and the "local, w/o GRPO" ablation. EvoTune scores far worse than CALM (2.40% vs 0.71% on OBP), and "local, w/o GRPO" at 1.78% shows the frozen local model is weak. These provide sufficient evidence that RL, not just prompt design, drives the improvement. Adding more local-model baselines would be a nice-to-have, not a structural requirement.

- **"The non-GRPO row uses CALM's own prompt scheme, not a separate baseline designed for a frozen model"**: The "CALM (API, w/o GRPO)" variant using GPT-4o-mini already outperforms or matches MCTS-AHD, demonstrating CALM's prompt design is strong independent of the model. This is a feature, not a bug.

- **"GRPO's credit assignment due to fine-granularity operators is not empirically verified"**: The ablation shows that removing injection, replacement, or simplification operators each degrades performance (Table 4). While the specific mechanism (credit isolation) is not directly tested, the empirical evidence for the operators' importance is clear. The credit-isolation claim is a plausible interpretation, not an unsupported factual assertion.

## Novel Insights
The paper's key insight — that the heuristic search process in AHD naturally generates prompt-response-performance triplets suitable for RL fine-tuning, enabling a "numerical gradient" that complements traditional "verbal gradient" prompt manipulation — is genuinely novel and opens a new dimension for LLM-based AHD research. The finding that a quantized 7B model, when co-evolved with the search process through GRPO, can outperform frozen GPT-4o-mini-based systems is both surprising and practically significant, since it suggests that task-specific fine-tuning can compensate for a substantial gap in base model capability.

## Suggestions
- Fix the duplicate HSEvo row in Table 3 (CVRP/OP). One of the two rows likely belongs to ReEvo or another baseline listed in the text but missing from these tables.
- Move standard deviations from Appendix I into the main tables to strengthen the reader's immediate confidence in the reported differences.
- Explicitly discuss the TSP case where CALM trails MCTS-AHD at N=50 and the margins are modest at N=100 and N=200, to give a balanced picture of where the method excels and where gains are incremental.

---

## Anchor Comparison

| Anchor | Path | Avg Score | Round | Comparison |
|--------|------|-----------|-------|------------|
| LLM4Solver | XTxdDEFR6D | 3.40 | R1 | CALM has more novel methodology (RL co-evolution) and much more comprehensive experiments. Clearly stronger. |
| MHRE | sUywd7UhFT | 2.50 | R1 | Far weaker than CALM in novelty, evaluation, and clarity. |
| Symbolic vs BB | MpA6HMD7Wq | 3.00 | R1 | Different domain; CALM is substantially more polished and empirically grounded. |
| LLIT | zEhTnQZB3D | 2.33 | R1 | Different domain; CALM significantly stronger. |
| Hercules | 0fwJMANq9P | 5.25 | R1 | Similar domain. Hercules is more incremental over prior work; CALM's RL co-evolution is a more substantial contribution. CALM is clearly stronger. |
| HeurAgenix | xxSK3ZNAhh | 3.80 | R1 | Multi-agent approach with limited evaluation; CALM's contribution is more focused and better validated. |
| LLM-LNS | Usk4KzBxLW | 5.25 | R1 | Similar domain but different task; CALM has more thorough ablations and clearer contribution. |
| Q-shaping | DlqRpj68xe | 5.67 | R1 | Different domain. CALM comparable in execution quality. |
| MaestroMotif | or8mMhmyRV | 7.75 | R1 | Strong paper with LLM+RL for skill design. CALM is comparable in novelty but slightly less polished in presentation. |
| LLAMBO | OOxotBmGol | 8.00 | R1 | Exceptionally well-executed paper. CALM is somewhat below this level in presentation and evaluation rigor. |
| GenSim | OI3RoHoWAN | 8.00 | R1 | Very strong paper; CALM is below this tier. |
| LLM-SR | m2nmp8P5in | 8.00 | R1 | Very strong paper; CALM is below this tier. |
| REvolve | cJPUpL8mOw | 6.00 | R2 | Different domain; CALM's contribution is comparably novel but with more comprehensive experiments. CALM is stronger. |
| EvoPrompt | ZG3RaNIsO8 | 6.50 | R2 | Both combine LLMs with EAs. CALM adds RL fine-tuning which is a more novel contribution. Comparable. |
| MOLLEO | awWiNvQwf3 | 7.00 | R2 | LLM-enhanced EA for molecular discovery. Similar paradigm of LLM-as-operator. CALM is comparable in quality but MOLLEO has slightly more polished multi-objective experiments. |
| CADO | pbDqZBn2X2 | 5.75 | R2 | Different approach (diffusion models); CALM is stronger in novelty and experimental scope. |
| LLaMoCo | EKCubxFdOs | 5.75 | R2 | Instruction tuning for optimization code. Most similar in the fine-tuning aspect, but LLaMoCo applies standard SFT while CALM introduces a novel RL-based co-evolution paradigm. CALM is clearly stronger. |
| STOP | 1gkePTsAWf | 6.20 | R2 | Self-improving code generation. CALM has more comprehensive experiments and clearer contribution. CALM is stronger. |

**Round 1 bracket**: 5.5 – 7.5. CALM is clearly above the Hercules/LLaMoCo tier (~5.25–5.75) and below the LLAMBO/MaestroMotif tier (~7.75–8.0).

**Round 2 narrowing**: Direct comparison with EvoPrompt (6.50) and MOLLEO (7.00) places CALM within this band. CALM matches MOLLEO in experimental comprehensiveness and exceeds EvoPrompt in methodological novelty. However, minor presentation issues (duplicate HSEvo row, deferred standard deviations) and modest TSP improvements prevent a higher score.

**Final score**: **6.5** — a solid contribution with a genuinely novel co-evolution paradigm, comprehensive experiments, and strong results, held back only by minor presentation and evaluation clarity issues.

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>