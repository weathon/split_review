Now I have a thorough picture of the calibration landscape. Let me synthesize the final review.

**Round 1 bracket**: 5.0–7.5 (clearly above weak/rejected papers like DataSciBench at 3.2, CodeBenchGen at 4.0; below top-tier orals like BigCodeBench at 9.0, Spider 2.0 at 8.0).

**Round 2 narrowing**: Comparing against anchors in the 5.0–7.5 band:
- **LiveCodeBench** (avg 6.25, Accept/Poster): Larger model evaluation (50+ models), strong contamination analysis, but focused on competitive programming rather than real-world SE. Comparable in quality to Ambig-SWE.
- **ScienceAgentBench** (avg 6.0, Accept/Poster): Expert-validated tasks, small set (102). The current paper has a stronger experimental decomposition (three capacities) but less human-annotation rigor.
- **SOTOPIA** (avg 6.67, Accept/Spotlight): More polished and comprehensive interactive evaluation framework. The current paper is slightly less polished but has a tighter experimental design.
- **CodeMMLU** (avg 5.5, Accept/Poster): Data leakage concerns, mixed reviews. The current paper is cleaner methodologically.

The paper sits near the upper end of the 5.5–6.5 range — comparable to LiveCodeBench (6.25) and ScienceAgentBench (6.0), with a focused contribution and well-designed experiments. The detection confound tempers but doesn't invalidate the core contributions. Score: **6.0**.

---

## Summary

This paper introduces **Ambig-SWE**, an underspecified variant of SWE-Bench Verified, and an interactive evaluation framework that decomposes the resolution of underspecification into three capacities: detection of missing information, asking clarification questions, and leveraging interaction for task completion. Using a GPT-4o-based user proxy, the authors evaluate six proprietary and open-weight LLMs across three settings (Full, Hidden, Interaction). The central finding — that interaction can substantially recover performance lost to underspecification (up to 74% improvement) — is well-supported and practically significant.

## Strengths

1. **Clear three-capacity decomposition with dedicated experiments.** The paper cleanly separates detection (RQ2), question quality (RQ3), and task integration (RQ1) — each with its own metrics, analysis, and actionable takeaways. This framework is novel relative to prior work that evaluates only end-task completion, enabling finer-grained diagnosis of where models fail. (Sections 3-5, Figures 3-6)

2. **Insightful empirical findings about interaction patterns.** The paper documents specific, actionable behaviors: (a) Qwen 3 Coder's complete non-responsiveness to interaction prompts (100% FNR across all prompt conditions, Table 2), (b) the discovery that navigational information *hurts* Qwen 3 Coder's performance due to rigid protocol-following (§3.3, Table 1), and (c) the qualitative analysis showing Claude Sonnet 4 achieves comparable information gain with ~50% fewer questions than Qwen 3 Coder through exploration-first strategies (§5.3). These go beyond generic "models are bad at X" claims.

3. **Well-designed controlled experimental setup.** The three-setting design (Full → Hidden → Interaction) with a GPT-4o user proxy that strictly limits responses to information in the original issue enables clean causal attribution of interaction's impact. The distributional analysis comparing synthetic underspecification to natural underspecified issues (§2.1) shows awareness of the dataset's limitations.

## Weaknesses

### Major

1. **The RQ2 detection experiment conflates detection ability with action selection, undermining the strongest claims about detection capacity.**

The dependent variable in RQ2 is whether the agent *chooses to interact*, not whether it *recognizes* underspecification. The paper's abstract and Section 4.3 claim that models "struggle to distinguish between well-specified and underspecified instructions" and "struggle to detect missing information even in obvious cases." But the design cannot separate true detection failure from a model having a strong non-interactive policy that overrides detection capability. Qwen 3 Coder's 100% FNR could equally reflect a training-induced non-interaction policy rather than an inability to detect underspecification. A forced-choice classification experiment ("Is this issue missing information?") would be needed to isolate detection.

The paper partially acknowledges this in the Limitations section ("detection is measured only within the first three turns"), but the acknowledgment is about the turn window, not about the conflation of detection with action. The main claims in Sections 1, 4, and 7 still frame the results as about *detection ability*, not *willingness to interact under prompt variation*. This is not a fatal flaw — the interaction-choice data is still informative — but the conclusions need to be revised to match what the experiment actually measures.

2. **The synthetic underspecification lacks validation against natural underspecification, limiting the dataset's external validity.**

The paper's own distributional analysis (§2.1) shows that GPT-4o-generated underspecified issues differ systematically from natural underspecified issues (fewer code snippets, error messages, file references, reproducibility information). The authors argue this makes the task *harder*, which is reasonable, but they do not validate that performance on Ambig-SWE correlates with performance on naturally underspecified issues. Without a human judgment study or a small-scale validation experiment that maps synthetic underspecification to real underspecification severity, it is unclear whether the empirical findings generalize beyond this specific synthetic artifact. This is a scope limitation that could be addressed in the rebuttal by at least discussing what validation would look like.

### Minor

3. **Question-quality metrics (cosine distance, LLM-as-judge) are weakly tied to downstream task success.** The paper correctly identifies the disconnect (e.g., Qwen 3 Coder extracts the most information by cosine distance but does not outperform Claude Sonnet 4 in resolve rate) and compensates with qualitative analysis in §5.3. The qualitative analysis is genuinely insightful, so this weakness is more about the metrics being cruder than the analysis itself. The paper's own Limitations section acknowledges this.

4. **Unequal turn limits across models.** Claude Sonnet 4 and Qwen 3 Coder get 100 turns vs. 30 for others. The paper mentions this (§3.1) but does not justify or analyze its potential effect. For a benchmark paper measuring interaction effectiveness, asymmetric resource budgets could confound model comparisons, particularly for the efficiency analysis in §3.2.

### Trivial

5. **The "74% improvement" figure** is mentioned in the abstract and introduction without specifying which model or comparison it refers to. (From Figure 3, it appears to be Claude Sonnet 4: (61.4-40.0)/40.0 ≈ 54%... actually let me check: for Claude Haiku 3.5, (26.8-13.4)/13.4 = 100%. The 74% seems to refer to some specific model/condition not clearly stated.)

## Nice-to-Haves

- A small forced-choice detection experiment (even on a subset) would cleanly resolve the RQ2 confound and substantially strengthen the paper's claims.
- A human validation study comparing a sample of Ambig-SWE issues to natural underspecified issues would strengthen the dataset's external validity.
- Reporting effect sizes or confidence intervals alongside the Wilcoxon tests would strengthen the quantitative claims.

## Removed Points

- **"Missing statistical reporting (effect sizes, CI)"** — The paper reports Wilcoxon tests with significance levels, which is standard for this type of benchmark evaluation. Demanding effect sizes for every comparison is a nice-to-have, not a weakness.
- **"Missing related works"** — This was flagged for removal by the hard rules. The paper covers relevant prior work adequately.
- **"Reproducibility concerns about undisclosed hyperparameters"** — The paper releases code and data, and the experimental setup is described sufficiently for reproduction.
- **"Formatting/style nitpicks"** — Parser artifacts, not author errors.
- **Strengths about "addressing an important problem"** — Generic; removed per filtering rules.
- **The claim that Qwen 3 Coder's 100% FNR "could equally reflect a strong non-interactive policy"** — This is kept in Weakness #1 but the framing has been refined. The critic's original framing treated this as a fatal confound; the paper partially addresses it in limitations, so I've downgraded it from fatal to major but retained the substance.

## Novel Insights

None beyond the paper's own contributions. The reviewers' main insights crystallize around the detection-action confound, which the paper itself does not fully address. The synergy between the harsh critic's methodological scrutiny and the strength finder's identification of the Qwen 3 Coder rigidity finding is worth noting: the rigid non-interactivity that the strength finder highlights as an actionable finding is precisely the behavior that the harsh critic argues cannot be cleanly attributed to detection failure. This tension — is Qwen 3 Coder *unable to detect* or *trained not to act on detection*? — is an open question the paper could productively explore.

## Suggestions

1. **Revise the claims in RQ2 (and the Abstract/Introduction) to explicitly state that the experiment measures *willingness to interact* under varying prompt conditions, not raw detection ability.** Use language like "models rarely choose to ask clarifying questions even when information is missing" rather than "models struggle to detect missing information." This single change would bring the claims in line with the evidence.

2. **Add a forced-choice detection experiment on a subset of Ambig-SWE issues** (e.g., 50 issues presented to each model with the explicit question "Is there enough information to fix this issue?"). This would cleanly isolate detection from action selection and either confirm or refute the current interpretation.

3. **Run a small human validation study** (even 20-30 issues) asking developers to rate underspecification severity on both Ambig-SWE and natural underspecified issues, and report the correlation. This would substantially strengthen the dataset's external validity claims.

## Score and Decision

**Round 1 bracket**: 5.0–7.5. The paper is clearly stronger than rejected/withdrawn papers scoring 2–3.25 (DataSciBench, CodeBenchGen) and clearly weaker than top-tier orals scoring 8+ (BigCodeBench, Spider 2.0).

**Round 2 anchors (used for fine-grained comparison)**:
- *ScienceAgentBench* (avg 6.0, Accept/Poster) — Comparable: both have clear benchmark contributions and solid evaluation. The current paper has tighter experimental design but no expert task validation.
- *LiveCodeBench* (avg 6.25, Accept/Poster) — Slightly stronger on evaluation breadth (50+ models) and contamination analysis; the current paper's three-capacity decomposition is a stronger framing contribution.
- *CodeMMLU* (avg 5.5, Accept/Poster) — The current paper is cleaner methodologically (no data leakage concerns) and has better-supported claims.
- *SOTOPIA* (avg 6.67, Accept/Spotlight) — More polished overall; the current paper has a tighter experimental design but is less comprehensive.

**Final calibration**: The paper's core contributions (Ambig-SWE dataset, three-capacity evaluation framework, empirical findings about interaction effectiveness) are solid and well-supported. The main weakness — the detection-action confound in RQ2 — is real and requires claim revision but does not invalidate the paper's overall contribution. The paper is comparable to LiveCodeBench (6.25) and ScienceAgentBench (6.0), and clearly stronger than rejected papers like CodeBenchGen (4.0) and Agent-as-a-Judge (5.67). Score: **6.0**.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>