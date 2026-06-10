## Summary

OMNI-EPIC proposes a framework that uses LLMs to generate complete, executable RL environments—including world physics, reward functions, and termination conditions—as Python code within the PyBullet simulator, guided by models of interestingness (MoI) and a growing task archive. The aim is to move beyond the narrow, manually predefined parameter spaces of prior open-ended learning systems (OMNI, POET) toward the ability to generate any simulatable learning task.

## Strengths

- **Full environment code generation demonstrated.** The paper shows that an LLM can generate executable PyBullet environments (including `reset`, `step`, `reward`, and `terminated` functions) from natural language task descriptions, with an automatic error-correction loop that iterates on compilation failures. This is a concrete technical advance over methods that only generate reward functions (Eureka) or select from predefined parameter spaces (OMNI). *Evidence: Section 3.3, the error-correction mechanism described at line 76.*

- **Concrete examples of adaptive curriculum from agent failures.** The paper documents specific cases where OMNI-EPIC adjusted task difficulty based on RL outcomes: when the agent failed to push a box on a dynamic platform (task 9), subsequent platform tasks removed the pushing requirement (tasks 11, 14, 15); when the agent failed a terrain-with-obstacles task (task 12), a simpler obstacle course was generated (task 13). These examples provide direct evidence that the system responds to agent capability. *Evidence: Section 5, lines 141–143.*

- **Long-run diversity visualization is genuinely compelling.** The long-run with simulated learning (Section 4, 200 iterations) produces tasks spanning ball-kicking, object retrieval, navigation, and terrain traversal—diverging substantially from the seed tasks. The qualitative diversity shown in Figure 1 is non-trivial for an automatic generation system. *Evidence: Section 4, lines 116–122.*

## Weaknesses

### Fatal

None.

### Major

- **No comparison against prior open-ended learning methods.** The quantitative comparison in Section 6 pits OMNI-EPIC only against ablated versions of itself (w/o archive, w/o MoI). The paper positions itself as an advance over OMNI (Zhang et al., 2023), POET (Wang et al., 2019, 2020), and Voyager (Wang et al., 2023), yet never compares against any of these. OMNI is the most directly relevant baseline—the system is named OMNI-EPIC—and a comparison would directly test whether code-based generation adds value over parameterized generation within a comparable domain and compute budget. Without such comparisons, the reader cannot assess whether the added complexity of code generation improves outcomes or introduces new failure modes. *Evidence: Section 6 (lines 159–167) discusses only ablations; no prior methods are included.*

- **The ANNECS-OMNI metric is partially aligned with the method's internal filtering, weakening the quantitative claim.** ANNECS-OMNI adds an FM-based interestingness criterion (line 165). OMNI-EPIC's pipeline already contains a post-generation MoI filter that rejects tasks an FM deems uninteresting. The control "OMNI-EPIC w/o MoI" removes this filter. The metric therefore measures, in part, whether removing a filter produces tasks that the same type of filter would have rejected—which is nearly tautological. The p < 0.05 result shows that the MoI component causes the output to pass an FM-based interestingness check, not that the tasks are independently verified as more interesting. *Evidence: Lines 78–83 describe the post-generation MoI filter; lines 165–166 define ANNECS-OMNI's interestingness criterion using "an FM."*

- **The "new high watermark" claim (line 167) is unsupported.** The paper states "That is a new high watermark in our field's longstanding quest to create open-ended algorithms" based solely on OMNI-EPIC outperforming its own ablations on a self-defined metric. No comparison to any prior open-ended system, no external benchmark, and no independent validation supports this claim. This is an overclaim relative to the evidence presented. *Evidence: Line 167; the surrounding text only discusses comparisons against the two ablations.*

- **The specific LLM, prompt templates, temperature, and retrieval mechanism are not disclosed.** The paper refers generically to "an LLM" or "FMs" throughout, but never specifies which model is used for task generation, environment code generation, or the MoI. Prompt templates, temperature settings, and the retrieval mechanism (embedding model, distance metric, number of neighbors for RAG) are also absent. Since the entire system's behavior depends on the stochastic outputs of a specific FM, these details are essential for reproducibility. *Evidence: The paper contains no mention of GPT-4, Claude, Llama, or any specific model; the RAG description at line 55 says "retrieval-augmented generation" without specifying implementation details.*

### Minor

- **The central learnability claim rests substantially on one illustrative short run.** The paper mentions 5 short runs with RL (line 139) but provides detailed per-task analysis only for a single run (22 attempted tasks, 16 successes). The other 4 runs are not broken down. The aggregated ANNECS-OMNI metric across 5 runs (Section 6) partially addresses this, but it measures a composite of learnability + interestingness rather than directly reporting task success rates, variance, and difficulty distributions across all runs. *Evidence: Line 139 shows only one run's breakdown.*

- **Code-generation failure rate is not reported.** The long run (line 116) "excludes tasks that did not generate executable code" but never reports how many such failures occurred. If a substantial fraction of proposed tasks fail to compile, the effective diversity is much lower than the 200-successful-iterations figure suggests. The same applies to the short runs. *Evidence: Line 116.*

- **The cell-coverage diversity metric measures diversity of text embeddings, not of actual environment structure or required skills.** Cell coverage is computed on text-embedding-3-small encodings of task descriptions. Two tasks with nearly identical environments but different color schemes or task descriptions could produce different embeddings and be counted as diverse, while two genuinely different environments described similarly might appear similar. *Evidence: Line 162 describes the metric as encoding "the generated tasks" via text-embedding-3-small.*

### Trivial

- **No effect sizes are reported alongside the p < 0.05 significance tests.** The practical magnitude of the improvement is not interpretable.
- **Color domain randomization (line 90) is mentioned but not measured or controlled for in any experiment.**

## Nice-to-Haves

- A comparison against OMNI in a comparable setting would directly test whether code-based generation adds value over parameterized generation.
- Reporting the fraction of code-generation failures across all runs would calibrate the reader's understanding of the system's reliability.
- Disclosing the specific LLM model(s), prompt structures, and temperature settings would substantially improve reproducibility.

## Removed Points

- *Criticism about "no analysis of reward-function quality":* This demands a detailed analysis that is beyond the paper's stated scope (task generation, not reward optimization). Removed as scope creep.
- *Criticism that "Voyager treatment is notably thin":* The paper covers Voyager in the context of open-ended methods; the depth of treatment is a judgment call, not a factual error. Removed as a judgment-driven criticism.
- *Strength that "ANNECS-OMNI introduces a new metric":* While true that a new metric is introduced, its circularity concerns (detailed above) significantly weaken this as a strength. Downgraded to neutral observation.
- *Criticism about "agent continues training from existing policy inflating success rate":* The paper explicitly describes this as a feature (line 90, following POET's approach). It is a standard practice in this line of work, not a flaw. Removed.
- *Strength that "The problem is important":* Generic/superficial. Removed.

## Novel Insights

The reviews surface a pattern common in ambitious open-ended learning papers: the gap between the conceptual contribution (code-based environment generation is clearly a more expressive paradigm than parameterized generation) and the evaluation (which never directly compares against the paradigm it aims to supersede). The paper's methodology is well-constructed and the qualitative demonstration is genuinely interesting, but the evaluation strategy consistently avoids the strongest test—direct head-to-head comparison with prior work—while making comparative claims ("new high watermark"). The paper would be substantially stronger if it recalibrated its claims to match what it actually demonstrates (a working prototype that generates diverse PyBullet environments adaptively) rather than claiming to advance the "quest to create open-ended algorithms" without measuring against the field's existing artifacts.

## Suggestions

1. Replace the "new high watermark" claim with a more measured conclusion about the demonstrated capabilities and limitations.
2. Disclose the specific LLM model(s) and prompt structures used—this is critical for reproducibility.
3. Report the code-generation failure rate across all runs.
4. Aggregate and report the task success statistics across all 5 short runs, not just one.
5. Compare against OMNI directly, either by replicating it in the same domain or adapting OMNI-EPIC's task generation mechanism to work within OMNI's parameterized space as a controlled comparison.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>