Here is the consolidated review:

---

## Summary

EnvBridge proposes a framework for cross-environment knowledge transfer in embodied AI. It stores successful robot control codes from source environments, retrieves them by instruction similarity, adapts them to the target environment using an LLM, and uses them as in-context examples during replanning. Experiments across RLBench, MetaWorld, and CALVIN show consistent improvements over code-generation baselines and simple replanning methods.

## Strengths

- **Consistent quantitative gains on RLBench**: EnvBridge achieves 69.0% average success rate, outperforming the code-generation baseline (36.5%) and Self-Reflection (62.5%) across 10 tasks (Section \ref{rlbench_experiments}, Figure \ref{rlbench-figure}). Several individual tasks show large jumps (e.g., TakeLidOffSaucepan: 0% baseline → 85%; OpenWineBottle: 15% → 95%).

- **Cross-environment transfer verified on MetaWorld**: Using only memory from RLBench (transferred knowledge), EnvBridge reaches 37% average success—above the 25% baseline—and with unified memory (RLBench + MetaWorld) reaches 56% (Section \ref{metaworld_result}, Figure \ref{metaworld-figure}). This directly demonstrates that knowledge sourced from a different benchmark improves performance in an unseen environment.

- **Ablations validate key components**: Removing Knowledge Transfer drops RLBench success from 69.0% to 61.5%, and random memory retrieval performs worse than similarity-based retrieval (Section \ref{knowledge_transfer}, Figure \ref{KT-figure}). These controlled comparisons confirm both design choices are essential.

- **Instruction-robustness evidence on CALVIN**: Under paraphrased instructions, EnvBridge achieves 63.0% while Retry drops to 57.5% (Table \ref{calvin-table}). Under single instructions the methods are essentially tied (60.5% vs 61.0%), but the paraphrase robustness is a practically relevant improvement.

## Weaknesses

### Fatal
None.

### Major
None. All identified issues are addressable in a revision and do not undermine the paper's core claims.

### Minor

1. **Knowledge transfer component is underspecified.** Section \ref{knowledge_transfer} describes the core cross-environment adaptation in one paragraph: "code examples from the target environment are provided as prompts, and the retrieved code is adapted to suit the target environment by LLMs" (line 180). The actual prompt template, the structure of the target environment examples, and how the LLM is instructed to differentiate environment-specific from general code are not given. Since this component is central to the method's novelty, omitting these details limits reproducibility and prevents independent assessment of the adaptation quality. The figure provides a conceptual illustration but no concrete specification.

2. **The "no human-initiated prompt adjustments" claim is unclear with respect to target environment examples.** The contribution list states EnvBridge operates "without relying on pre-training or human-initiated prompt adjustments" (line 43). However, the knowledge transfer process requires "code examples from the target environment" as references for the LLM (line 180, Figure \ref{kt_figure}). The paper does not specify whether these target examples are hand-crafted, automatically retrieved, or generated — leaving ambiguity about whether this constitutes a "human-initiated prompt adjustment" by another name.

3. **No uncertainty quantification for main results.** All experiments use 20 trials per task, but no confidence intervals, standard errors, or significance tests are reported. This matters because several individual RLBench tasks show Self-Reflection outperforming EnvBridge (BeatTheBuzz: 90% vs 65%; CloseDrawer: 85% vs 75%; LampOff: 80% vs 65%), and the CALVIN single-instruction result shows EnvBridge (60.5%) marginally below Retry (61.0%). Without confidence intervals, the reader cannot assess whether the aggregate 6.5-point RLBench gap is statistically reliable or driven by a few outlier tasks. Adding Wilson-score intervals or bootstrapped confidence intervals would substantially strengthen the claims.

4. **Memory comparison experiment has uncontrolled confounds.** The memory comparison table shows CALVIN memory (69.0%) outperforming RLBench in-domain memory (65.5%) on RLBench tasks. The paper attributes this to "smaller variation" in stored codes and the number of planner codes (26 for CALVIN vs 50 for RLBench). However, the experiment does not control for code quality (e.g., success rate of the stored executions, whether memories were generated with the same LLM or the same number of trials). This makes it difficult to isolate whether the performance difference stems from cross-environment benefits or from unmeasured differences in memory quality. A controlled analysis (e.g., equalizing code counts, comparing code complexity) would clarify the result.

### Trivial

- The commented-out LaTeX tables in the source (around lines 274-306 and 317-349) contain different numerical values than the active content, suggesting the paper underwent revisions where certain tables were replaced with figures. While this does not affect the final content, it indicates some organizational roughness in the manuscript preparation.

## Nice-to-Haves

- **Knowledge transfer prompt template**: Including the exact prompt used for code adaptation would turn the method from vaguely described to fully reproducible.
- **Confidence intervals or error bars** for the main RLBench, MetaWorld, and CALVIN results.
- **Analysis of knowledge transfer failures**: The paper treats adaptation as a black box that always works. Examples of failure cases (syntactically valid but semantically wrong adapted code) would inform future work.
- **Computational cost**: No discussion of latency or LLM call count for the knowledge transfer + replanning pipeline.
- **Memory size sensitivity**: How does performance scale with memory size (10, 50, 200 codes)? Currently only three fixed-size sources are compared.
- **Clarification of target environment example provenance**: How the "code examples from the target environment" are obtained.

## Removed Points

These points were raised by the reviewers but removed for the reasons stated:

1. **"CALVIN has less diversity than RLBench, making the memory comparison contradictory"** (from Harsh Critic's Critical Issue 3). Removed because it is factually incorrect: the paper states CALVIN has 15 task types (line 403) while the RLBench evaluation uses 10 sampled tasks (line 232). 15 > 10, so the claimed "contradiction" does not exist. The remaining concern about uncontrolled confounds is retained as Weakness #4 above.

2. **Various section-by-section nitpicks** (e.g., "citation to \cite{lu2024aiscientistfullyautomated} is vague", "Could benefit from code-level similarity"). These are either overly granular or suggestions that do not detract from the paper as presented. Scope-creep requests (computational cost, memory scaling, real-world experiments) are moved to Nice-to-Haves.

3. **"Self-Reflection comparison is not apples-to-apples because it uses images"** — the critic themselves notes this is "not necessarily unfair." The paper acknowledges the difference and Self-Reflection is a reasonable baseline. This does not constitute a real weakness given the paper's stated scope.

## Novel Insights

None beyond the paper's own contributions. The reviews do not surface a new synthesis or angle that the paper itself does not already articulate.

## Suggestions

1. Provide the exact Knowledge Transfer prompt template (in an appendix or supplementary). This is the single highest-leverage improvement for reproducibility.
2. Add bootstrapped 95% confidence intervals or Wilson-score intervals to the per-task and aggregate success rates across all three benchmarks.
3. Clarify how target environment code examples are obtained for the knowledge transfer step, and whether the claim about "no human-initiated prompt adjustments" needs qualification.
4. In the memory comparison experiment, control for memory quality (equalize code counts, compare generation methodology) to support the cross-environment transfer narrative more cleanly.
5. Use error bars (even simple min/max across tasks or binomial confidence intervals) for the ablation bar charts (Figure \ref{KT-figure}), which currently lack any numerical annotation.

## Score and Decision

**Originality**: The idea of cross-environment code retrieval + LLM-based adaptation for embodied planning is a reasonable extension of existing retrieval-augmented planning methods, though the core technique (LLM adaptation with in-context examples) is not fundamentally new. **Importance of question**: The problem of transferring knowledge across environments is practically relevant for generalizable embodied AI. **Claims support**: The main claims are supported by consistent results across three benchmarks, though the lack of confidence intervals weakens the statistical claims. **Soundness**: The experimental design is generally sound; ablations validate key components. **Clarity**: The method is described at a high level but the key Knowledge Transfer step is underspecified. **Value**: The paper offers a practical, easy-to-replicate recipe that should be useful to practitioners in LLM-based robotics.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>