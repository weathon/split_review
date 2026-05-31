## Summary

CALM (Co-Evolution of Algorithms and Language Model) is a framework for Automatic Heuristic Design (AHD) that augments existing LLM-based evolutionary heuristic search with on-the-fly LLM fine-tuning via GRPO (a group-relative policy optimization algorithm). Rather than treating the LLM as a fixed oracle guided only by prompt manipulations ("verbal gradients"), CALM treats the evolutionary loop's prompt-response-performance triplets as RL training data, applying "numerical gradients" to adapt the LLM itself. The method also introduces fine-granularity mutation operators (injection, replacement), a diversity-aware crossover operator, and a probabilistic collapse mechanism for escaping local optima. Running on a single 24 GB GPU with a 7B INT4-quantized model, CALM consistently outperforms or matches state-of-the-art API-based (GPT-4o-mini) methods on OBP, TSP, CVRP, and OP benchmarks.

---

## Strengths

- **Compelling empirical outcome**: A 7B INT4-quantized local model outperforms GPT-4o-mini-based baselines (EoH, ReEvo, HSEvo, MCTS-AHD) on most benchmark tasks. This is a practically important result given the resource and cost advantages of local deployment.
- **Well-motivated core idea**: The observation that evolutionary AHD naturally produces prompt-response-performance triplets that can serve as RL training signal is clean and non-trivial. Making the LLM co-evolve with the heuristic population is a natural extension that prior work had overlooked.
- **Thorough ablation study** (Table 4): Each component—GRPO, collapse mechanism, each operator (injection, replacement, crossover, simplification)—is ablated individually, with reward-function variants and hyperparameter sensitivity also tested. The finding that GRPO is the single highest-impact component is directly quantified.
- **Reward function design is carefully considered**: The relative-improvement reward (measuring gain over the best parent, not absolute performance) is well-motivated and validated against two alternative schemes, both of which underperform.
- **Verbal gradient contribution isolated**: The API-based CALM variant (GPT-4o-mini, no GRPO) is evaluated separately and shown to be competitive with MCTS-AHD, isolating the prompt-engineering contribution from the RL contribution.
- **Diversity-aware crossover**: The ablation showing that performance-only crossover is worse than no crossover at all, while diversity-aware crossover is beneficial, is a striking and informative result.

---

## Weaknesses

### Fatal
None.

### Major

- **Evaluation budget comparability is unclear**: The paper states CALM uses "2,000 LLM queries" while baselines use "1,000 heuristic evaluations" and "typically over 4,000 queries" for some tasks. The paper's framing conflates LLM queries and heuristic evaluations inconsistently—e.g., for OBP, prior methods use 4,000+ queries while CALM uses 2,000, which actually favors CALM's budget efficiency, but for other tasks the direction is reversed. A unified budget comparison (e.g., number of heuristic evaluations across all methods) would make the fairness of comparisons unambiguous.
- **GRPO introduces a warm-up cost that is not fully accounted for**: Figure 2 shows CALM's heuristics initially lag behind baselines before eventually surpassing them. Within a fixed query budget, this transient cost may matter. The paper does not analyze at what query count CALM begins to dominate, nor whether extending baselines' budgets would close the gap.

### Minor

- **OP in-domain results are not dominant**: On the in-domain N=50 OP test set, CALM (local, w/GRPO) achieves 24.22% gap while HSEvo achieves 23.98%. The claim of consistent superiority does not fully hold at this scale/task combination, though CALM does better at out-of-domain scales.
- **Task selection is restricted to "challenging" problems**: The authors explicitly exclude tasks (TSP under ACO, KP) where existing LLM-based methods already approach optimality. While scientifically reasonable, the paper would benefit from a brief quantitative justification of why each excluded problem was excluded rather than leaving this to the reader.
- **INT4 quantization interaction with GRPO fine-tuning is under-analyzed**: Fine-tuning only 1.15% of weights in an INT4-quantized model is unusual. Appendix I contains some fine-tuning/model-choice experiments, but the effect of training in mixed precision vs. full INT4 throughout is not clearly characterized in the main text.

### Trivial

- Table 3 contains two duplicate rows for "HSEvo" under the GPT-4o-mini section (likely a formatting artifact).

---

## Nice-to-Haves

- A query-matched comparison (e.g., allow baselines to run for 2,000 queries as well) would strengthen the main claims.
- Reporting wall-clock time alongside query counts would clarify the practical cost of GRPO fine-tuning relative to simply using more API calls.
- Analysis of whether the fine-tuned LLM generalizes to new problem types (transfer) would reveal whether CALM is learning task-general heuristic design ability or purely task-specific knowledge.

---

## Novel Insights

CALM demonstrates that the evolutionary AHD loop is not merely a search procedure but also an implicit curriculum for on-policy RL: each round naturally generates a diverse set of prompt-response-performance samples, and the act of selection already provides a relative quality signal without requiring any external labels or demonstrations. The paper shows this signal is sufficient to fine-tune a 7B quantized model to surpass GPT-4o-mini-based competitors. Equally interesting is the ablation result that performance-only crossover is *worse than no crossover*, while diversity-aware crossover helps substantially—this suggests that in LLM-driven search, structural novelty of the second parent matters more than its raw performance, a finding with broader implications for evolutionary search design in open-ended heuristic spaces.

---

## Suggestions

- Report heuristic evaluations (not just LLM queries) for all methods in a unified table, with a note clarifying how these relate.
- Add an analysis of training dynamics: at what query count does the CALM (local, w/GRPO) curve cross each baseline curve? This would clarify when the RL warm-up cost pays off.
- Extend the collapse mechanism analysis to show how many collapses occur on average per run and how this correlates with final performance.
- Consider including an experiment where CALM is initialized without any seed heuristic (pure initialization operator), to show robustness to the seed choice.

---

## Score and Decision

CALM is a clearly motivated, well-executed paper with a novel integration of on-policy RL fine-tuning into LLM-based evolutionary heuristic design. The empirical evidence is broadly convincing, the ablations are comprehensive, and the practical resource efficiency (local 7B model beating API baselines) is a genuine contribution. The main concerns—budget comparability and OP in-domain performance—are real but do not invalidate the core claims. The paper sits comfortably in the upper tier of applied ML contributions.

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>