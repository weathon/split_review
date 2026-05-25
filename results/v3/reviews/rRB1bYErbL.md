Now let me compose the final review.

## Summary

This paper proposes R-HORIZON, a method for constructing multi-step reasoning tasks by concatenating existing single-step problems with lightweight arithmetic dependencies. The authors build an evaluation benchmark spanning math, code, and agent tasks (6 datasets), evaluate 26 LRMs, and document systematic performance degradation as the reasoning horizon increases. Rich analysis of failure modes — effective reasoning length, localized reflection, unbalanced thinking budget allocation — provides genuinely useful diagnostics. The paper additionally uses R-HORIZON to construct training data for GRPO-based reinforcement learning and reports improvements on both multi-step and single-step math tasks, most notably +7.5 points on AIME2024.

## Strengths

1. **Large-scale, multi-task evaluation with consistent findings.** 26 LRMs across 6 datasets (MATH500, AIME24/25, AMC23, Live-CodeBench, WebShaper) all show the same degradation pattern. For instance, DeepSeek-R1 on AIME25 drops from 87.3% (n=1) to 24.6% (n=5). The breadth of this evaluation makes the core observational finding robust. (Section 4.2, Figure 3)

2. **In-depth mechanistic analysis goes beyond surface accuracy.** The paper quantifies *why* models fail: limited effective reasoning length (error positions plateau at 4–6k tokens for 7B, 8–10k for 32B), highly localized reflection (more than half of problems lack cross-problem reflection), and systematically biased thinking budget allocation toward early problems. These findings are novel and well-supported by Figures 5–8.

3. **Simple, low-cost construction method that can be applied to any existing benchmark.** The pipeline (seed filtering → key-variable verification → dependency chain construction via Algorithm 1) requires only integer extraction and a verification model. This scalability is a real practical strength — it enables creating long-horizon evaluation and training data from any single-step dataset without manual annotation.

4. **Training with composed data shows promise for improving both multi-step and single-step reasoning.** The finding that GRPO with R-HORIZON training data improves not only composed-task performance (+17.4 on AIME24 n=2) but also standard single-query benchmarks (+7.5 on AIME24 n=1) is practically significant and goes beyond what prior work has demonstrated. (Table 1, Figure 4)

## Weaknesses

### Major

1. **RL experiments lack multiple seeds and variance reporting.** All training results (Table 1, Figures 4, 9, 10) come from a single run on a single 7B model. No standard deviations or multiple seeds are reported. Because RL training is inherently noisy — the non-monotonic behavior observed in the evaluation table (e.g., DeepSeek-R1 on AIME24 n=4 → n=5 jumping from 52.8→67.3) hints at variance that is never discussed — it is impossible to determine whether the observed improvements are statistically reliable or whether they generalize across runs. This undermines the paper's central training claim. The training curves in Figure 4 provide some reassurance of consistent trends, but without multiple seeds the concern cannot be resolved.

2. **Missing independent-concatenation baseline in evaluation.** The paper correctly distinguishes R-HORIZON from NEST and GSM-Infinite, yet never includes a baseline where the same problems are concatenated *without* dependencies. The error-type analysis (Figure 5) shows that "Dependency Reasoning Error" is a small fraction of total errors, while "Problem Reasoning Error" dominates. This pattern suggests that most degradation comes from the increased cognitive load of solving multiple problems, not from the dependency structure itself. Without an independent-concatenation baseline, the paper's emphasis on "interdependent problems" as the key construct is not fully supported by the data. Including such a baseline would clarify whether the dependency structure amplifies failures beyond what a simple multi-problem prompt already induces.

3. **No controlled comparison for training confounds.** The comparison between "naive training data (n=1)" and "composed queries (n=2/4)" is not controlled for the number of training examples seen per step, total token budget, or density of reward signal. Because each composed example packs multiple problems, the model receives a denser reward signal per gradient update. The improvement on single AIME24 (57.9→65.4) could therefore come from seeing more math problems per step rather than from the sequential dependency structure. A controlled baseline (e.g., matching the number of problems seen, or packing unrelated problems per prompt) is needed to attribute the improvement to the compositional structure.

### Minor

4. **Construct validity of the math composition.** The dependency function \(v_{i+1} = a_i + (m_{i+1} - a_i)\) collapses to the original integer \(m_{i+1}\) once \(a_i\) is known. This means each sub-problem is entirely self-contained except for a single propagated numeric value. While this construction reveals real failure modes (early stopping, localized reflection), it is a stretch to characterize it as testing "deeply interdependent reasoning" in the sense of planning or multi-step deduction where intermediate conclusions transform the subsequent problem state. The code and agent tasks likely involve more natural dependencies, but the paper's analysis and all training experiments are confined to math. The narrative should be tempered to match what the construct actually measures: multi-problem stress with lightweight dependency stitching.

5. **Key methodological details are underspecified.** (a) The verification model \(M\) used to identify key variables (Equation 2) is not named and its accuracy is not reported, affecting reproducibility of the pipeline. (b) The selection of which key variable \(m_{i+1}\) to use when multiple candidates exist is not described (random? difficulty-based?). (c) The main evaluation table (Figure 3) does not specify whether numbers are pass@1, avg@k, or single-run; the mention of "avg@8" in Figure 4 suggests averaging is done somewhere, but it is not stated for the full benchmark. (d) The size of the training data pool and number of composed examples generated are not reported.

6. **The rollout efficiency analysis (Figure 10) conflates a mechanical property with a claimed efficiency improvement.** The "effective" percentage is mechanically higher for n>1 because multi-problem queries naturally yield partial success/failure, providing a gradient signal at every step. Single-problem queries are either all-right or all-wrong. This does not necessarily mean the training signal is *better* — it is a necessary property of the construction, not an empirical finding of improved efficiency.

### Trivial

7. There is a clear parser artifact of "127.6" in the main table (Qwen3-32B, Math500 n=4) which should be corrected.
8. The conclusion describes R-HORIZON as "a novel and efficient approach," which overstates the methodological novelty of simple concatenation with arithmetic substitutions. The contribution lies more in the evaluation and training findings.

## Nice-to-Haves

- Run the RL experiments with at least 3 random seeds and report means ± std for the key numbers in Table 1.
- Add an independent-concatenation baseline (NEST-style) for at least one math dataset and one model size, comparing degradation curves.
- Add a controlled training baseline: either match total problems seen (train n=1 for twice as many steps when comparing to n=2), or pack unrelated problems per prompt to isolate the effect of dependencies.
- Provide a qualitative comparison of reasoning traces between models trained with single vs. composed data to illustrate how the thinking strategy changes.

## Removed Points

- **"The +7.5 gain stated prominently but context clarified later could mislead casual readers"** — this is a presentation nitpick about ordering. The paper clarifies the relevant context (comparison to naive training data).
- **"Training details deferred to appendix"** — standard practice; the main text provides the key setup (Table 1, Figure 4).
- **"Reproducibility: does not state release of dataset/code"** — per filtering rules, cannot question existence/release status.
- **"Missing comparison with NEST and GSM-Infinite results"** — these are related works with different scopes (long input context); comparing degradation slopes would be nice-to-have but is not a missing requirement.
- **"The method is straightforward concatenation; the contribution is more in evaluation than the method itself"** — the paper describes the method as "simple yet effective" which is accurate; this is a matter of framing, not a concrete weakness.
- Several other minor presentation/style nitpicks from the harsh reviewer are removed as formatting artifacts or style preferences.

## Novel Insights

Beyond the paper's own contributions, the most novel observations emerging from the reviews are: (1) the finding that LRMs' effective reasoning length is surprisingly bounded and model-size-dependent (4–6k tokens for 7B, 8–10k for 32B) — this is a concrete, actionable metric for practitioners. (2) The reflection analysis showing that more than half of problems lack long-range reflection even as composed query count grows is a striking indictment of current models' inability to integrate information across reasoning segments. (3) The thinking budget analysis revealing that models allocate disproportionately more tokens to early problems, with even DeepSeek-R1 failing to distribute budget evenly — this connects "overthinking" to a structural allocation failure, which is a finer-grained diagnosis than prior work. (4) The observation that training with composed data simultaneously reduces response length (counters overthinking) while improving both multi-step and single-step accuracy suggests that long-horizon training induces a genuine reorganization of the reasoning strategy, not just better pattern matching.

## Suggestions

1. **Most critical:** Run all RL experiments with at least 3 random seeds and report variance. This is the single change that would most strengthen the paper.
2. Add an independent-concatenation baseline (NEST-style) to the evaluation for at least one math task (e.g., MATH500 with R1-Qwen-7B) to directly test whether the dependency structure causes the observed degradation or whether multi-problem length suffices.
3. Add a controlled training condition where n=1 data is packed (two unrelated problems per prompt) to isolate whether the improvement comes from multi-problem exposure or from the dependency structure.
4. Disclose the verification model M and its accuracy on the key-variable detection task.
5. Specify the evaluation protocol for the main table (pass@1? avg@k? temperature?).
6. Temper the framing: the math composition tests multi-problem stress with lightweight dependencies, not deeply interdependent reasoning. Adjust the narrative in Section 1 and Section 6 accordingly.

## Score and Decision

### Calibration Report

**Round-1 bracket:** 5.0 – 6.5 (based on topic-anchored and weakness-anchored queries).

**Anchor list:**

| Anchor | Avg Score | Source | Comparison to this paper |
|--------|-----------|--------|-------------------------|
| Planning in Strawberry Fields (jOuHjFw71C) | 3.00 | round1-topic-low | Much weaker — evaluates only 2 models on existing benchmarks. |
| Exploring & Benchmarking Planning (koza5fePTs) | 2.00 | round1-topic-low | Much weaker — small-scale evaluation without novel method. |
| CLR-Bench (ToVvoHpk4L) | 4.33 | round1-topic-mid | Weaker — limited to multiple-choice, less analysis depth. |
| KOR-Bench (SVRRQ8goQo) | 7.00 | round1-topic-mid | Stronger — cleaner conceptual contribution, rigorous eval. |
| LogicBench (71kocBuhNO) | 5.40 | round1-topic-mid | Comparable — similar scope but no training component. |
| FACTOR (eNCyY81aW6) | 5.00 | round1-topic-mid | Slightly weaker — less comprehensive model evaluation. |
| MathEval (DexGnh0EcB) | 4.20 | round1-weakness | Weaker — aggregation of existing benchmarks without novel construction. |
| MathHay (QO4bF6MHza) | 4.17 | round1-weakness | Weaker — limited to 8 models, quality control issues. |
| Continual Task Learning (upV91V0Big) | 4.75 | round1-weakness | Similar weakness (single-seed RL) but narrower scope. |
| Can LLMs Solve Long Math (C9ju8QQSCv) | 4.75 | round2 | Slightly weaker — narrower scope (only math word problems). |
| LV-Eval (WQwy1rW60F) | 6.00 | round2 | Comparable — similar benchmark ambition but fewer models. |
| NovelQA (uMEsKEiB7J) | 6.40 | round2 | Slightly stronger — careful construction, but no training. |
| I-PHYRE (1bbPQShCT2) | 6.50 | round2 | Stronger — thorough experimental design, human baseline. |

**What the low-band anchors failed at:** Papers in the 2–4 range either had limited model evaluations (2–8 models), proposed no novel method/construct, or had quality control issues that undermined their findings. The paper under review is clearly stronger than these — it evaluates 26 models, proposes a concrete construction method, provides rich analysis, and includes training experiments.

**What the weakness-anchored hits reveal:** Papers that share the "single-seed RL without variance reporting" weakness (e.g., Continual Task Learning at 4.75) or "missing critical baseline" weakness tend to score in the 4–5.5 range. The paper under review's training claims are in the same territory — promising but not yet rigorous.

**Final score justification:** The paper has genuine strengths — a comprehensive evaluation, novel analysis, and a useful construction method — that place it well above the 2–4 range. However, two major weaknesses (no multiple seeds for RL, no independent-concatenation baseline) prevent its central claims from being fully supported. The training results are the most eye-catching contribution but rest on insufficient experimental controls. The score of 5.5 reflects a paper with substantial merit that falls short of the rigor expected for acceptance at a top venue in its current form.

### MY FINAL SCORE: 5.5
### MY FINAL DECISION: Reject