Now I have all the information I need. Let me synthesize the final review.

---

## Summary

R-HORIZON proposes a query-composition method that chains independent math/code/agent problems into interdependent multi-step sequences, creating a benchmark that evaluates 25+ large reasoning models (LRMs) on long-horizon reasoning. The benchmark reveals severe accuracy degradation as the number of composed queries grows. The paper also uses the same composition to construct training data for GRPO-based reinforcement learning, showing that training on composed data improves both multi-step and single-problem performance. The benchmark contribution is comprehensive and well-executed; the training contribution has methodological gaps.

## Strengths

- **Comprehensive, large-scale benchmark evaluation**: The R-HORIZON benchmark evaluates 25+ LRMs (from 1.5B to 235B parameters, both open and proprietary) across 6 task types (math, code, agentic) with varying composition lengths. The degradation patterns in Figure 3/Table are clear and consistent across models — even top models like DeepSeek-R1 and Qwen3-235B-Thinking drop dramatically (e.g., DeepSeek-R1 on AIME25: 87.3% at n=1 → 24.6% at n=5). This is a substantial, well-documented empirical contribution.

- **Rich diagnostic analysis beyond raw accuracy**: The paper quantifies effective reasoning length (Figure 6), showing that error positions plateau at model-specific token ranges (4-6k for 7B, 8-10k for 32B on MATH500). The reflection analysis (Figure 7) demonstrates that LRM reflections are predominantly local — more than half of problems lack any long-range reflection. The thinking-budget allocation analysis (Figure 8) reveals that models disproportionately spend tokens on early sub-problems. These measurements provide concrete, falsifiable explanations for why performance degrades, going well beyond "models struggle at longer horizons."

- **Simple, replicable composition method**: The dependency-chain construction (Algorithm 1) is clearly described, uses a straightforward algebraic offset function f_i(x) = x + (m_{i+1} - a_i), and can be applied to any dataset with integer-answer problems. The method is genuinely low-cost and scalable.

- **Training with composed data shows promising signals**: GRPO training on n=2 composed data yields +17.4 on AIME24 (n=2 composed) and +7.5 on standard single-problem AIME2024 compared to single-problem training (Table 1, Figure 4). The observation that composed training yields more balanced reward signals (Figure 10) and reduces overthinking (Figure 9b) is directionally interesting.

## Weaknesses

### Fatal

None.

### Major

- **Training comparison is not properly controlled**: The paper's central training claim — that composed data improves training over single-problem data — rests on comparisons where the two conditions differ on more axes than composition alone. The composed-data condition uses a filtered subset of Skywork-OR1 (problems with integer answers and key variables, filtered by expected accuracy > 0.25), while the "Naive Training Data (n=1)" baseline and the "original data" in Figure 4 appear to use the full unfiltered Skywork-OR1 pool. These conditions differ in problem set, difficulty distribution, and effective data volume. The paper does not include a baseline that trains on the *same filtered seed problems presented individually* (n=1 from the filtered pool). Without this, the +7.5 AIME2024 gain cannot be attributed to composition specifically — it could equally be explained by data filtering, the altered reward structure, or distributional effects. This undermines the claim that "training with R-HORIZON data is a highly efficient training approach" (line 30).

### Minor

- **"Effective" rollout metric is undefined for n=1**: Figure 10 reports "Effective (%)", "Solve None (%)", and "Solve All (%)" to argue that composed data yields ~20% more effective samples. For n>1, "Effective" plausibly means partially correct rollouts (not all-correct, not all-wrong). For n=1 (single-problem rollouts), there is no partial correctness — a rollout is either correct or incorrect. The paper never defines what "Effective" means in the n=1 case or how the three categories are computed, making the 20% claim unevaluable.

- **No statistical reporting on training results**: The training curves (Figure 4) and summary table (Table 1) present point estimates without error bars, confidence intervals, or disclosure of the number of independent training runs. GRPO training is sensitive to seed effects; the reported gains (e.g., +7.5 on AIME2024) could fall within run-to-run variance. This weakens the reliability of the training conclusions.

- **Model M for key-variable verification is unspecified**: Equation (2) and the surrounding text describe using a model M to verify whether each integer in a problem is a key variable, but M is never identified. Was this GPT-4, a fine-tuned classifier, or a heuristic? The accuracy of this verification step directly affects the validity of dependency chains, yet no validation is provided.

- **"Breadth and depth" never operationally defined**: The title and introduction invoke "breadth and depth" as organizing concepts, but these terms are never given operational definitions. The investigated horizon is primarily sequential depth of dependent mathematical problems; breadth (parallel or branching reasoning) is not systematically studied. This creates a mismatch between framing and content.

- **Over-interpretation of synthetic composition as general "long-horizon reasoning"**: The composition method uses a specific algebraic dependency (f_i(x) = x + (m_{i+1} - a_i)). While this is a clean, controllable testbed, the paper often equates performance on this construct with general long-horizon reasoning capabilities. The findings may not extrapolate to other forms of extended reasoning (open-ended planning, multi-turn tool use, or long-form argument). The paper would be stronger by presenting the benchmark as a diagnostic stress-test rather than a direct proxy for all multi-step reasoning.

### Trivial

- The "error position" text in Section 5.1 states that "error position … gradually declines and stabilizes," which is inconsistent with Figure 6's description (which shows an initial increase then stabilization). The description should be corrected to match the data.

- Three composition types (Directly Compose, Sequential Compose, Graphic Compose) are shown in Figure 2 but only the sequential case is detailed in the main text; the others are deferred to the appendix. A brief summary of how the other modes work and when they are used would improve the main text.

## Nice-to-Haves

- A proper controlled baseline: train on the same filtered seed problems presented as single-problem prompts, with matched training steps and comparable problem-exposures, to isolate the effect of composition from data filtering.
- An ablation on problem ordering (e.g., random vs. difficulty-ordered) to assess whether degradation is sensitive to how problems are sequenced.
- A discussion of whether models overfit to the specific offset-based composition pattern during training.

## Removed Points

These points are flagged to be removed, treat them with caution:

- **Harsh critic's claim that training comparisons are not controlled because composed data uses filtered subset**: Partially removed as an independent "fatal" flaw because the paper's Table 1 does include a "Naive Training Data (n=1)" baseline, and the composed-query variants (n=2, n=4, mixed) are constructed from the same filtered pool. However, the relationship between "Naive Training Data (n=1)" and the filtered pool is genuinely ambiguous — it is unclear whether this baseline uses filtered or unfiltered data. Retained as a Major weakness due to this ambiguity, but demoted from "fatal" because the paper partially addresses the concern through the n=2/n=4/mixed comparisons within the filtered pool.

- **Harsh critic's suggestion about "code and agentic task composition methods entirely absent from main text"**: The paper explicitly states these are provided in Appendix A. Deferring construction details to the appendix for secondary task types is standard practice. Removed.

- **Harsh critic's concern about "the appendix may specify X but…" regarding training details**: The paper clearly signals "Details are in Appendix F" and "More training dynamics are provided in Appendix C." Removed as speculative.

- **Strength Finder's "Higher rollout efficiency" with evidence from Figure 10**: This strength is weakened by the undefined "Effective" metric for n=1. Kept in the review but noted with the corresponding weakness.

## Novel Insights

The paper's finding that models exhibit a bounded *effective reasoning length* — an error position that plateaus at a model-specific token range independent of how many problems are composed — is genuinely novel. This suggests that LRMs have a hard reasoning horizon (not just a context-length limit) beyond which additional problems are essentially ignored or answered incorrectly regardless of the model's single-problem capability. Combined with the observation that thinking budget is disproportionately allocated to early sub-problems, this points to a structural limitation in current LRM architectures that goes beyond simple "models get worse at longer contexts." The training finding that composed data can reduce overthinking (shorter responses for the same accuracy) is also a potentially important observation about how the training data distribution shapes reasoning behavior.

## Suggestions

- Add a baseline where the filtered seed problems are trained on individually (n=1 from the filtered pool, same data as the n=2/n=4 conditions). This is the single most important experiment to add.
- Define the "Effective" metric precisely for all n values, including what it means for n=1.
- Run at least 3 training seeds and report error bars on Table 1 and Figure 4, or explicitly disclose single-run reporting.
- Specify which model M was used for key-variable verification and report its accuracy on a validation subset.
- Tone down claims about general "long-horizon reasoning" by clarifying that the composition is a specific synthetic construct; frame the benchmark as a diagnostic stress-test.

## Score and Decision

### Anchor Comparison

**Round 1 anchors:**

- **koza5fePTs** (2.00, round1-topic-low): Planning benchmark evaluating existing models. Very limited contribution — R-HORIZON is substantially stronger, with novel composition method, richer analysis, larger-scale evaluation.
- **jOuHjFw71C** (3.00, round1-topic-low): Evaluating o1 on planning benchmarks. Limited to evaluating existing models on established benchmarks — R-HORIZON introduces a new benchmark and training method.
- **MK6E6IgROl** (3.75, round1-topic-mid): ProcBench — 23 synthetic tasks for procedural reasoning, 7 models evaluated. R-HORIZON is stronger: broader task coverage (6 types vs. string/list operations), more models (25+ vs. 7), richer analysis, plus training experiments.
- **DZBFchnM3b** (3.67, round1-topic-mid): Navigating Labyrinth — search problems, benchmark + A* prompting. R-HORIZON has more comprehensive evaluation and richer analysis.
- **eNCyY81aW6** (5.00, round1-topic-mid / round2): FACTOR — factoring complexity and context length. Clean framework but narrow task. R-HORIZON has broader task coverage and adds training, but FACTOR had cleaner analytic framework. Comparable quality.
- **71kocBuhNO** (5.40, round2): LogicBench — 25 logical reasoning patterns, comprehensive evaluation. R-HORIZON has richer analysis (reflection, thinking budget) and adds training experiments. Comparable or slightly stronger.
- **SVRRQ8goQo** (7.00, round1-topic-high): KOR-Bench — knowledge-orthogonal reasoning. Cleaner concept, well-executed. R-HORIZON has a similar evaluation scale but training issues pull it below KOR-Bench.

**Weakness-anchored hits:**
- Training comparison issues: papers scored 3.0-4.4
- Missing error bars: papers scored 4.2-5.25
- Undefined metrics: papers scored 2.5-5.25

**Round 1 bracket:** 4.5–6.5 based on topic-anchored comparisons.

**Round 2 narrowed to 5.0–6.0**, with R-HORIZON sitting above FACTOR (5.00) and roughly comparable to LogicBench (5.40), but below KOR-Bench (7.00).

**What did the low-band anchors fail at, and does R-HORIZON share those failures?** The low-band anchors (2.00–3.00) failed primarily on lack of novelty (just evaluating existing models on established benchmarks, no new methodology) and insufficient analysis. R-HORIZON does NOT share these failures — it introduces a novel composition method, builds a new benchmark, and provides rich diagnostic analysis. However, R-HORIZON *does* share a key failure mode with the 3.67–3.75 range papers: the training-method contribution has uncontrolled comparisons that undermine the claimed benefits. This is what separates it from the 7.0+ papers that had clean, well-controlled experiments throughout.

**Final score: 5.5.** The benchmark contribution is solid and would independently warrant a score in the 5.5–6.5 range. The training experiments are directionally promising but have genuine methodological issues (uncontrolled comparison, undefined metric, no statistical reporting) that prevent the paper from reaching accept-level quality. These issues are addressable but substantial.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>