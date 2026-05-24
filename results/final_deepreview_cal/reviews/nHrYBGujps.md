Now I have all the information needed. Let me write the final consolidated review.

---

## Summary

BIRD-INTERACT introduces a dynamic, multi-turn text-to-SQL benchmark of 900 tasks (300 LITE + 600 FULL) that covers the full CRUD spectrum, departing from the SELECT-only limitation of prior benchmarks. Its key innovations are a function-driven user simulator (two-stage AMB/LOC/UNA design that reduces ground-truth leakage) and two complementary evaluation settings: c-Interact (protocol-guided conversation) and a-Interact (agentic, open-ended planning under budget constraints). Evaluation of seven frontier LLMs reveals that even GPT-5 solves only 8.67% of tasks in c-Interact and 17.00% in a-Interact on the FULL set, demonstrating a large capability gap.

## Strengths

- **Ambitious, realistic benchmark design with broad coverage.** The benchmark encompasses 900 tasks with full CRUD operations, 5.16 ambiguities/task on LITE, and state-dependent follow-up sub-tasks (Table 1). This substantially expands beyond SELECT-only multi-turn benchmarks and captures real-world interactive complexity including ambiguity resolution and execution debugging.

- **Function-driven user simulator with demonstrated robustness.** The two-stage simulator (AMB/LOC/UNA) reduces unanswerable-question failure rates from 67.4% (baseline) to 2.7% on the USERSIM-GUARD dataset (Figure 6), and achieves Pearson correlation of 0.84 (p=0.02) with human behavior in a 100-task alignment study (Table 3). This is a genuine methodological contribution for scalable interactive evaluation.

- **Dual evaluation paradigms yield non-obvious insights.** The c-Interact vs. a-Interact distinction reveals that model ranking is not stable across modes: GPT-5 ranks worst in c-Interact (14.50% SR) but best in a-Interact (29.17% SR; Table 2). The memory grafting experiment (Figure 5) demonstrates that GPT-5's poor c-Interact performance stems specifically from communication strategy deficits rather than SQL generation ability—a finding with practical implications for model deployment.

- **Interaction Test-Time Scaling analysis.** Varying user patience (Figure 4) reveals that some models (e.g., Claude-3.7-Sonnet) exhibit clear scaling with additional interaction turns, while others plateau. This empirical characterization of the interaction–performance relationship is valuable for understanding model behavior.

- **Well-structured paper with clear motivation.** The taxonomy of ambiguity injection (superficial, knowledge-chain breaking, environmental) is well-conceived, and Figure 1 effectively illustrates the interactive process. The benchmark is built on the open-source LIVESQLBENCH infrastructure, supporting reproducibility.

## Weaknesses

### Fatal

None.

### Major

None.

### Minor

- **Single-run evaluation without variance estimates.** The main results (Table 2) come from single runs per model (temperature=0). While temperature=0 ensures deterministic generation and the 600-task scale provides some stability through aggregation, the absence of any variance reporting—even on a small LITE subset—makes it difficult to assess whether model ranking differences (e.g., GPT-5's 29.17% vs. O3-Mini's 19.83% SR in a-Interact) are robust to run-to-run variation in the interactive dynamics. A modest multi-run stability test on LITE would substantially strengthen confidence in the reported rankings.

- **Limited scope of user simulator human-alignment validation.** The human-alignment study covers 100 tasks and yields statistically significant correlations (Pearson 0.84, p=0.02), which is encouraging. However, 100 tasks is a modest sample relative to the 900-task benchmark, and the three-action scheme (AMB/LOC/UNA) may not capture the full richness of human clarification behavior (e.g., partial hints, counter-questions, deliberate vagueness). The paper acknowledges free-mode evaluation as future work but could include a more explicit limitations discussion for the simulator.

- **Budget parameter choices lack sensitivity analysis.** The base budget B_base=6 and default patience λ_pat=3 are stated without derivation. While Figure 4 does vary λ_pat across {0,3,5,7}, demonstrating some robustness, the a-Interact budget structure B = B_base + 2m_amb + 2λ_pat is not subjected to sensitivity analysis on B_base or the action costs in Figure 3. Without such analysis, it is not fully clear whether the finding that "models prefer trial-and-error over exploration" is robust to these parameter choices.

- **Figure 5 presentation is ambiguous.** The bars labeled "Qwen-3-Coder" and "O3-Mini" both show identical "With" and "Without" values (18.5%), since these are the donor models' standalone performance. Readers may mistakenly interpret these as grafting results on those models. The caption and labeling should clarify that the first two groups are reference baselines, not grafting targets.

- **"ITS Law" terminology is overstated.** The paper defines an "ITS Law" as the property that, given enough interaction turns, a model can match or surpass idealized single-turn performance. This is an empirical observation on a handful of models, not a law. Reframing as a "desirable scaling property" or "ITS pattern" would be more appropriate.

### Trivial

- **Table 2 notation.** The "+n" values in parentheses (e.g., "14.50 (+0.67)") indicate debugging gains but are easily misread. A separate column or explicit "debugging gain" notation would improve clarity.

- **Normalized reward formula is entirely in the appendix.** The main text (Section 2) defines NR only as "normalized scoring according to priority weighting as designed in Appendix F." A one-sentence sketch of the weighting scheme in the main body would make reward values interpretable without chasing appendices.

## Nice-to-Haves

- A fine-grained failure analysis (e.g., breakdown into incorrect clarification, wrong SQL, debugging failure, budget exhaustion) would substantially enrich the benchmark's diagnostic value.
- Human-performance calibration (experienced SQL users on a subset of tasks) would anchor the difficulty scale and help interpret the 17% absolute success rate.
- A limitations paragraph for the user simulator explicitly acknowledging scenarios where it may be less realistic (e.g., never volunteering unrequested information).
- Multi-run stability test on the LITE set (e.g., 3 runs of top-3 models).

## Removed Points

These points were raised in the inputs but removed from the final review with justification:

- **"SELECT-only is an overstatement"**: The paper's characterization of existing benchmarks as SELECT-only is a reasonable high-level claim. Whether some versions of CoSQL/SParC include basic DML is a minor factual nuance that does not affect the paper's contribution. Removed.
- **"p-values (0.02 and 0.03) are weak given the small sample size"**: This is factually incorrect. p=0.02 and p=0.03 are statistically significant at the conventional α=0.05 threshold. The harsh critic confused statistical significance with effect size or power. Removed.
- **"Were these models accessed via stable APIs under deterministic settings?"**: This questions the existence/availability of cited models (GPT-5, Claude-Sonnet-4). Per evaluation rules, all cited models are assumed to exist and be accessible. Removed.
- **Missing related work (CHASE-SQL) and related work section suggestions**: Per evaluation rules, we do not flag missing related works since we lack external sources to confirm their relevance. Removed.
- **"Naive LLM without function calling is a strawman baseline"**: The paper fairly compares against a standard LLM-as-simulator approach, which is a reasonable baseline for demonstrating the function-driven design's improvements. The clarity of improvement is the point. Removed.
- **Formatting/style concerns about appendix placement**: The paper uses appendices for detailed methodology; this is standard practice. The key results are in the main body. Removed.

## Novel Insights

The most striking insight from the BIRD-INTERACT evaluation is the *mode-dependent ranking reversal*: GPT-5 performs worst in the constrained conversational setting (c-Interact) but best in the open-ended agentic setting (a-Interact). The memory grafting experiment provides a mechanistic explanation—GPT-5 has strong SQL generation capability but poor communication strategy, which is fatal in c-Interact but compensated for in a-Interact by its ability to explore the environment autonomously. This suggests that benchmarking interactive systems requires careful attention to the interaction paradigm, and that model selection for deployment should be conditioned on the expected interaction mode. The observation that current LLMs overwhelmingly prefer trial-and-error execution (submit + ask = 60.87% of actions) over systematic knowledge/schema exploration is another finding with practical design implications for agent scaffolds.

## Suggestions

- Run a modest multi-run experiment (3 runs each of top 3 models on LITE) and report standard deviations. This is the single highest-impact improvement.
- Add a brief limitations paragraph for the user simulator, explicitly noting that the three-action scheme constrains response diversity and that the simulator never volunteers unrequested information.
- Rename "ITS Law" to "ITS property" or "ITS trend."
- Clarify Figure 5 by labeling the first two groups as "Reference (no grafting)" and the last two groups as "GPT-5 + donor history."
- Include a one-sentence summary of the reward weighting scheme in Section 2 rather than deferring entirely to Appendix F.
- Consider adding a fine-grained failure taxonomy (even on LITE only) to increase the benchmark's diagnostic value for the community.

## Score and Decision

**Round 1 bracket:** The initial retrieval placed BIRD-INTERACT between weak anchors (DB-GPT-Hub at 3.75, TrustSQL at 4.00) and strong anchors (Spider 2.0 at 8.00, MMQA at 8.00), giving a plausible bracket of approximately 5.0–8.0.

**Round 2 narrowing:** Inside the bracket, the most comparable anchors are:
- **Spider 2.0 (8.00)**: A text-to-SQL benchmark with 632 enterprise tasks, unanimously scored 8. BIRD-INTERACT is comparable in ambition and scale but has more evidential gaps (single-run, limited simulator validation). Somewhat below Spider 2.0.
- **WildBench (7.33)**: A general LLM benchmark with 1,024 real-user tasks and strong human correlation. BIRD-INTERACT has more novelty (user simulator, dual modes) but similar evidential gaps. Roughly comparable.
- **CHASE-SQL (6.25)**: A method paper, not a benchmark—less comparable but from the same domain.
- **OpenTab (6.67)**: A framework paper with narrower scope. BIRD-INTERACT is clearly stronger.

BIRD-INTERACT sits between WildBench (7.33) and Spider 2.0 (8.00), but closer to WildBench given the evidential gaps around single-run evaluation and simulator validation. I assign **7.0**.

**Anchors referenced across all rounds:**
- lMW9d1AqC9 (avg 1.67, Round 1): R-KinetiQuery—off-topic sign-language-to-SQL paper; much weaker.
- Avg6hmtgHE (avg 3.40, Round 1): Wikipedia multi-entity QA—tangential; BIRD-INTERACT is substantially stronger.
- wwO8qS9tQl (avg 3.00, Round 1): ALMANACS explainability benchmark—tangential; BIRD-INTERACT is substantially stronger.
- BltaWJZMeR (avg 3.20, Round 1): DataSciBench—different domain; BIRD-INTERACT is stronger.
- NmILZXKcOi (avg 3.75, Round 1): DB-GPT-Hub—text-to-SQL benchmark but narrower; BIRD-INTERACT is stronger.
- BAglD6NGy0 (avg 6.25, Round 1): ROUTE—text-to-SQL method, not benchmark; BIRD-INTERACT is a stronger contribution.
- 7ZeoPg3eTA (avg 4.00, Round 1): TrustSQL—text-to-SQL reliability benchmark with significant construction concerns; BIRD-INTERACT is considerably stronger.
- CvGqMD5OtX (avg 6.25, Rounds 1 & 2): CHASE-SQL—method paper; BIRD-INTERACT is a stronger benchmark contribution.
- WYdpjwKQma (avg 5.00, Round 2): LAIA-SQL—method paper with narrower scope; BIRD-INTERACT is stronger.
- a4sknPttwV (avg 5.50, Round 2): DCA-Bench—dataset curation benchmark; different domain; BIRD-INTERACT is stronger.
- XmProj9cPs (avg 8.00, Round 2): Spider 2.0—most comparable anchor; BIRD-INTERACT is slightly weaker due to evidential gaps.
- GGlpykXDCa (avg 8.00, Round 2): MMQA—multi-table QA; BIRD-INTERACT is comparable but MMQA has fewer evidential gaps.
- Qa0ULgosc9 (avg 6.67, Round 2): OpenTab—framework paper; BIRD-INTERACT is a stronger contribution.
- MKEHCx25xp (avg 7.33, Round 2): WildBench—comparable strength; BIRD-INTERACT scores similarly with more novelty but also more evidential gaps.

MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>