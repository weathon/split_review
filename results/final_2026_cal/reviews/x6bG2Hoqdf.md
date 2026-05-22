Now let me write the final review.

## Summary

This paper proposes CALM, a framework for LLM-based Automatic Heuristic Design (AHD) that fine-tunes the underlying language model via GRPO (a score-based RL algorithm) during the evolutionary search, rather than keeping the LLM frozen as in prior work. The method introduces fine-granularity mutation operators (injection, replacement), a diversity-aware crossover, and a probabilistic collapse mechanism to escape local optima. Using only an INT4-quantized 7B model running locally on a 24GB GPU, CALM consistently outperforms stronger API-based baselines (GPT-4o-mini with MCTS-AHD, EoH, ReEvo, etc.) across Online Bin Packing, TSP, CVRP, and the Orienteering Problem, including out-of-domain scales. The ablation study cleanly isolates the RL fine-tuning component as the single most impactful contributor.

## Strengths

- **RL fine-tuning is cleanly shown to be the decisive component.** Table 4 ablations demonstrate that removing GRPO causes the largest performance drop on both OBP (0.71% → 1.78%) and OP (17.41% → 19.89%), larger than removing any operator or the collapse mechanism. This directly validates the paper's central claim that numerical gradients from RL are more impactful than verbal guidance alone.

- **A quantized 7B model with CALM surpasses GPT-4o-mini baselines across diverse tasks.** Tables 1–3 show that CALM's local setup achieves lower optimality gaps than all prior API-based methods on OBP (0.71% vs. 0.89% next-best), CVRP (3.83% vs. 4.70% next-best across scales), and OP (12.58% vs. 15.10% next-best on out-of-domain). This is a striking result given the large gap in base-model capability.

- **Thorough, multi-task ablation isolating every component.** Table 4 systematically ablates GRPO, each collapse variant, and each operator separately on two tasks. The ablation reveals non-obvious findings (e.g., crossover without diversity hurts more than having no crossover at all) that deepen confidence in the design.

- **Diversity-aware crossover with a principled formulation.** The hybrid performance/diversity selection (definition via token-set overlap in Section 4.1) is clean, and the ablation confirms the diversity mechanism is essential — a rare level of validation for operator design in this literature.

- **Generalization to larger out-of-domain instances is demonstrated consistently.** Across CVRP and OP, CALM's heuristics hold up at 2×–4× the training size, which is non-trivial for learned heuristics and strengthens the practical claim.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

- **Missing numeric values for reward and GRPO hyperparameters.** The paper defines α₁, α₂ ∈ (0,1) and r_invalid ∈ (−1,0) for the reward function (Eq. 4), and ε, β for GRPO (Eq. 1), but does not report their specific numeric values in the main text. While hyperparameter sensitivity analyses are referenced as deferred to Appendix I (stripped), the main paper should at minimum state the chosen defaults. This is a reproducibility gap, not a fatal flaw — it can be addressed in a rebuttal by stating the values.

- **The collapse probability formula (Eq. 2) is unvalidated.** The analytical approximation E[c_n | collapse, C > 1/δ₀] ≈ √(π/(2δ₀)) is presented as a theoretical aid for hyperparameter selection, but no experiment checks whether empirical collapse times match this distribution. A histogram of collapse rounds from logged runs would sharpen the contribution.

- **HSEvo appears twice in Table 3 with no explanation.** Two rows labeled "HSEvo" show different numbers (e.g., gap 7.54% vs. 6.11% on CVRP N=50). The caption and surrounding text do not explain whether these are two separate runs, different seeds, or different variants. This is a presentation oversight that needs clarification.

- **Evaluation budgets overlap but are not perfectly matched.** Baselines use 1,000 heuristic evaluations while CALM uses 2,000 LLM queries (mostly mapping to heuristic evaluations), and for OBP prior methods use ~4,000 queries for 2,000 evaluations. The paper acknowledges this asymmetry honestly and the performance gaps are large enough that it is unlikely to reverse conclusions, but a compact summary table of query counts, evaluation counts, and wall time across methods would strengthen the resource-efficiency claim.

### Trivial
- The variable name \hat{r}_{i,t} is used for the probability ratio in the GRPO objective (Eq. 1), while r simultaneously denotes reward. Minor notation clash — no functional confusion.

## Nice-to-Haves
- An empirical check of the collapse formula (Eq. 2), e.g., a histogram of collapse times across runs.
- Brief examples of discovered heuristics directly in the main paper (currently deferred to the stripped appendix).
- A single summary table of computational cost (LLM queries, heuristic evaluations, GPU hours) for all methods.
- A sensitivity analysis or reported values for GRPO's ε and β.

## Removed Points
- "Potential confound in the reward comparison" — this concern was raised by the harsh critic but the paper's own ablation (Table 4, comparing alternative reward schemes) directly examines this and shows the proposed reward design outperforms alternatives. The concern is acknowledged by the paper and addressed experimentally.
- "Catastrophic forgetting" — raised by the harsh critic but not supported by evidence. The ablation "w/o collapse" shows a performance drop, suggesting the system maintains learned behaviors appropriately. A direct test would be nice-to-have but is not a weakness.
- "Concurrent fine-tuning approaches not properly differentiated" — the paper explicitly discusses Surina et al. (2025) and Liu et al. (2025), distinguishing its use of GRPO and specialized operators. The claim "one of the first" is appropriately scoped.

## Novel Insights
None beyond the paper's own contributions.

## Suggestions
- Report the specific numeric values for α₁, α₂, r_invalid, ε, and β used in the experiments. These can be included in a brief new table or footnote.
- Add a brief explanation for the two HSEvo rows in Table 3 (e.g., whether they reflect different seeds, different configurations, or reruns).
- Include a validation experiment for the collapse probability formula (Eq. 2) — even a simple histogram from logged runs would suffice.
- Add a small "computational cost" table summarizing queries, heuristic evaluations, and GPU hours per method.

## Score and Decision

**Bracket (Round 1):** Weak anchors (score <3.5) — EvoPH (2.0), QUBE (2.0), TPD-AHD (3.0). Middle anchors (3.5–7.5) — MoH (5.0), HeuriGym (6.0), RFTHGS (6.0), AutoEP (6.5). Strong anchors (>7.5) — unrelated topics (oral papers on verifiers, multi-turn conversation, etc.). The paper is clearly far above the weak band and sits in the middle band.

**Narrowing (Round 2):** Compared to MoH (5.0, Poster): CALM has broader evaluation (4 problems vs. 3, with out-of-domain testing), a cleaner methodology, and did not raise the fairness concerns that MoH faced. Compared to RFTHGS (6.0, Poster): both use RL fine-tuning for heuristic design, but CALM covers 4 separate optimization problems with different solver frameworks (ACO, step-by-step construction, online bin packing) versus RFTHGS's single-operator, single-problem (CVRP crossover) setting, and CALM uses a weaker base model (INT4 7B vs. 14B). Compared to AutoEP (6.5, Oral): CALM's methodology is more directly about co-evolving the LLM with the search rather than zero-shot hyperparameter control; the empirical scope is broader. CALM sits slightly above RFTHGS in breadth and evidence strength, and is comparable to AutoEP.

**Final Score:** 6.5

**Decision:** Accept

<score>6.5</score>
<decision>Accept</decision>