## Summary

InnoGym is a benchmark framework designed to evaluate the *innovation potential* of AI agents, not just answer correctness. It introduces two complementary metrics — Performance Gain (G) and Novelty (N) — and formalizes each task as a quadruple (P, S, V, D). The benchmark (iBench) contains 18 carefully curated improvable tasks from real-world engineering and scientific competitions, paired with iGym, a unified agent execution environment. Experiments on three agent frameworks reveal that while agents generate novel approaches, their solutions consistently fall far below human state-of-the-art, highlighting a gap between creativity and robustness.

---

## Strengths

- **Addresses a genuine and underexplored gap.** All compared benchmarks (Table 1: MLE-Bench, MLAgentBench, DSBench, etc.) evaluate performance but not novelty. The paper is correct that measuring *how* a solution is obtained, not only *what* it achieves, is missing from existing evaluation frameworks. The formalization as (P, S, V, D) with G and N is principled and clean.

- **Rigorous benchmark curation pipeline.** Starting from 197 candidate tasks and reducing to 18 via two-stage filtering (resource availability, evaluator quality/domain balance), the paper's methodology is documented and transparent. The requirement for Pearson ≥ 0.9 and Kendall-τ ≥ 0.8 for evaluator normalization provides a quantitative anchor for evaluator quality.

- **Domain diversity beyond Kaggle.** Tasks drawn from ROADEF, NeurIPS competitions, KDD Cup, GMCM, and classical NP-hard problems span combinatorial optimization, biological, financial, mathematical, and systems domains. This breadth is a notable improvement over ML-only Kaggle-centric benchmarks.

- **Interesting empirical analysis.** The temperature ablation revealing a clean exploration-exploitation trade-off (Fig. 6c), the complex-plane representation of solution trajectories (Fig. 5b), and the temporal dynamics of G and N are genuinely illuminating. These analyses demonstrate the metrics' ability to capture iterative refinement dynamics.

- **Taxonomy of innovative task types.** The three-way categorization (Solved, Improvable, Exploratory) in Section 2.3 is conceptually clean and provides a useful ontology for the broader field evaluating creative AI.

---

## Weaknesses

### Fatal
None.

### Major

- **Novelty metric validity is undemonstrated in the main paper.** The entire differentiating contribution of InnoGym over existing benchmarks is the Novelty metric N. Its instantiation relies on LLM-as-judge (Codex for strategy extraction, GPT-5 for pairwise dissimilarity rating across 6 rubric dimensions). For domain-specialized problems like bin-packing, molecular property prediction (Belka), or action localization (PTTALC), the question of whether a general-purpose LLM can reliably judge "methodological dissimilarity" in terms of domain-appropriate novelty is critical. The paper defers all validation of D to Appendix F. The main paper provides no inter-rater reliability, consistency check, or example that builds confidence in this metric. This is the benchmark's key distinguisher, and the evidence in the main text is insufficient to evaluate its soundness.

- **No agent achieves positive performance gain on any task.** All measured G(s) values in Table 2 are strictly negative, meaning the benchmark is currently in a regime where the innovation taxonomy (breakthrough, performance, conceptual) cannot be demonstrated in practice. The framework's full value — differentiating these three types of innovation — is never instantiated in the experiments. The benchmark may be useful for future, stronger agents, but the current experiments cannot validate the most important use case.

- **Small experimental scale with optimistic reporting.** Main experiments cover 10 of 18 tasks (with up to 7 "/" failures per task-agent pair). Results are reported as best-of-3 runs, which is an optimistic estimator. For a benchmark paper that makes broad claims about agent innovation capabilities, this scope limits the reliability of the findings. The circle packing ablations use a single task.

### Minor

- **GPT-5 appears as a backbone in ablations (Fig. 6b, Sec. 4.3)**, described in the text as a backbone for experimentation. It is unclear whether GPT-5 is publicly available at submission time, which reduces reproducibility of that specific ablation.

- **Circular evaluation concern.** GPT-5 (or Codex) is used to extract solution features *and* to judge novelty of solutions submitted by GPT-5-backed agents. This creates a potential blind spot where the judge may under-report novelty of strategies it natively generates.

- **The iGym execution environment is described but not compared against alternatives.** The claim that existing SDKs (OpenHands, AutoGen, LangGraph) "lack crucial features" is stated without benchmark evidence showing that iGym actually improves agent performance over these alternatives.

### Trivial

- The complex-plane representation (Fig. 5b) is visually appealing but the angle-as-novelty mapping is arbitrary and not compared against simpler representations.

---

## Nice-to-Haves

- A human expert study calibrating the LLM-as-judge novelty scores against domain expert assessments on a subset of tasks would substantially strengthen the paper's core claim.
- Reporting median or mean-of-3 alongside best-of-3 would give a more complete picture of agent reliability.
- Including at least one example where G(s) > 0 (even from a privileged oracle agent) would demonstrate that the benchmark's full innovation taxonomy is reachable in principle.

---

## Novel Insights

The paper's most genuinely novel insight is the empirical observation that novelty and performance are decoupled in current agents: agents consistently achieve mid-range novelty scores (40–70 out of 100) while failing to translate this into positive performance gains. This suggests the bottleneck is not ideational diversity but execution robustness — novel ideas without reliable implementation are valueless in engineering/scientific optimization contexts. The temperature ablation (Fig. 6c) formalizes this as an exploration-exploitation trade-off and identifies 0.5–0.75 as an empirical sweet spot. The complex-plane representation of solution trajectories is a useful visualization device that could inspire future trajectory analysis in iterative refinement settings.

---

## Suggestions

- Provide at least a condensed validation of the Novelty metric D in the main paper: a small human study or inter-rater agreement statistic comparing LLM-judge novelty ratings against domain expert ratings on 2–3 tasks.
- Discuss the sensitivity of the overall benchmark conclusions to the choice of D (e.g., what if D were an embedding-based cosine distance instead of LLM-judge?).
- Consider releasing iGym as a standalone tool for reproducibility, with a brief empirical comparison showing it enables configurations that fail under existing SDKs.
- Report mean-of-3 alongside best-of-3 so readers can assess agent consistency, which is directly relevant to the paper's robustness narrative.

---

## Score and Decision

InnoGym addresses a genuine and timely gap: measuring methodological novelty alongside performance in AI agent benchmarks. The formal framework is principled, the curation is rigorous, and the empirical findings — while limited in scope — are revealing. The main weakness is that the paper's core differentiator (the novelty metric D) is not validated within the main text, and the experimental scope cannot demonstrate the benchmark's full utility (no positive G is ever observed). These are significant gaps for a benchmark paper but not fatal ones; the framework's conceptual contribution is clear and the community need is real.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>