Now I have a clear picture of the paper and the reviews. Let me synthesize the final review.

## Summary

This paper proposes AVUA, an LLM-based agent for long-form video understanding that combines query-adaptive dynamic frame sampling with self-reflective reasoning (evaluator + refiner feedback) and long-term memory. The agent uses a policy generated per query to decide which frames to sample, then iteratively refines its reasoning based on feedback. Evaluated across four benchmarks (Egoschema, Ego4D NLQ, MovieChat, NextQA), the method reports state-of-the-art accuracy while accessing substantially fewer frames than uniform-sampling baselines.

## Strengths

- **Significant accuracy improvement with drastically fewer frames across multiple benchmarks.** On Egoschema, AVUA achieves 66.98% accuracy using 14.27 frames (0.26% of total), surpassing the best agent baseline LifelongMemory (62.4% with 180 frames). On Ego4D NLQ (IoU@0.5), it achieves 17.1% vs. VideoAgent's 7.47%, accessing 98 vs. 487 frames. These consistent patterns across diverse benchmarks provide strong evidence that query-adaptive sampling combined with feedback-driven reasoning jointly improves both efficiency and accuracy.

- **Ablation studies confirm the necessity of each proposed component.** Removing the evaluator, refiner, sampler, or long-term memory consistently degrades accuracy across benchmarks (e.g., Egoschema accuracy drops from 66.98% to as low as 50.1% without the evaluator, and to 42.02% with plain ReAct). These controlled experiments validate that the architectural components are individually essential, not merely additive.

- **Demonstration of query-adaptive behavior via textual-cue analysis.** On NextQA, the paper shows that questions with textual temporal cues (e.g., "at the end") lead to fewer frames accessed (10.56 vs. 12.26) and concentrates sampled frames around the relevant temporal region (Figure 6). This provides direct empirical evidence for the claimed adaptive attention mechanism.

- **General evaluation across both long-form and short-form videos.** Including NextQA (44 sec avg) alongside longer benchmarks (Egoschema 3 min, MovieChat 9.4 min, Ego4D 8.7 min) demonstrates that the framework is not limited to long-context settings.

## Weaknesses

### Fatal
None.

### Major

1. **MovieChat open-ended evaluation lacks validation and has significant methodological concerns.** The paper uses Claude-3.5-Sonnet as an automated judge to evaluate open-ended answers, counting only instances where the judge's confidence exceeds 80/100 as correct. This has several issues: (a) using the same model family (Claude) for the evaluator that powers the agent introduces potential systematic bias; (b) the 84.8% accuracy figure is dramatically higher than all baselines (MovieChat itself gets 62.3%), yet the paper provides zero human validation, correlation analysis, or even qualitative examples demonstrating judge reliability; (c) the phrasing "counting only the instances with confidence over 80 as correct" is ambiguous — if low-confidence judgments are excluded rather than counted as wrong, this inflates accuracy on a self-selected subset not comparable to baselines. The MovieChat result is the most extreme reported gain (22% absolute improvement) and it rests entirely on this unvalidated evaluation. **Mitigating factor:** The paper's core contributions are also supported by multiple-choice benchmarks (Egoschema, NextQA) and temporal localization (Ego4D) that use standard, non-controversial evaluation protocols. However, the MovieChat claims as presented are not credible without validation.

2. **Method description is too vague for reproducibility and for assessing architectural novelty.** Section 3 describes the policy generation, sampler, evaluator, and refiner at a high level but omits critical details: (a) how is the policy generated — what goes into the prompt, what constitutes a "sampling strategy"? (b) how does the sampler interact with the planner beyond "suggest[ing] which frames to select" — what is the communication protocol? (c) how is the evaluator's binary judgment with confidence used to trigger refinement — is there a threshold? (d) how is long-term memory indexed by "semantic similarity of question types" — what embedding model, what retrieval mechanism, how many memories? The paper provides an example trajectory (Figure 2) but no algorithmic sketch, pseudocode, or prompt templates. For a method paper whose primary contribution is a system architecture, this level of ambiguity prevents the reader from reconstructing or building upon the work.

### Minor

3. **Frame-percentage error in the Ego4D table.** The main Ego4D NLQ table reports "avg 98 (0.002%)" for the proportion of frames accessed. For an 8.7-minute video at 30 fps (~15,660 frames), 98 frames is roughly 0.63% of total, not 0.002%. The ablation table reports "98 (.002)" (as a proportion), which has the same numerical error (should be ~.0063). The Egoschema proportions are internally consistent and correct; this error appears isolated to Ego4D. While the core efficiency claim holds even at the correct value (~0.6% is still very efficient), the error suggests insufficient auditing of the reported numbers.

4. **SOTA claims conflate tool choice with method contribution.** The main results tables compare AVUA (using Claude-3-Sonnet as the reasoning backbone, LaViLa for captioning, Video-LLaVa for QA, etc.) against baselines that use different underlying models and tools (e.g., VideoAgent uses BLIP-2 and different captioning pipelines). The accuracy differences therefore reflect both the adaptive-sampling architecture *and* the choice of tools. The paper's framing — "more than 4% improvement over the best performing baseline method" — does not disentangle these factors. **Mitigating factor:** The ablation study (Table 5) compares the full method against a ReAct-only variant using the same tools, providing a fairer test of the architectural contribution. The claims should be qualified to reflect that the ablation rather than the main tables provides the cleanest evidence.

5. **No statistical uncertainty reported.** Results are presented as point estimates on 500-instance subsets (Egoschema, MovieChat) and larger sets, with no error bars, confidence intervals, or multiple runs. Given the stochastic nature of LLM-based agents, it is unclear whether reported differences (e.g., 66.98% vs 62.4% on Egoschema; 19.5 vs 17.38 on Ego4D IoU=0.3) are statistically significant.

### Trivial

- The paper uses "Claude-3-Sonnet" for the agent and "Cluade-3.5-sonnet" (apparent typo) for the MovieChat evaluator. The version inconsistency between the two should be clarified.

## Nice-to-Haves

- **Compare against a stronger adaptive baseline** (e.g., VideoTree or CLIP-based frame retrieval) to isolate the benefit of the full agent architecture beyond adaptive sampling.
- **Provide failure-case analysis** — for what question types does the agent struggle, and does it ever get stuck in loops or hallucinate?
- **Report wall-clock time or API cost** beyond frame count, since the multi-step agent pipeline (policy generation, planning, evaluation, refinement) may offset the efficiency gained from fewer frames.
- **Further analyze the textual-cue finding** by reporting accuracy broken down by cue presence, to clarify whether adaptive sampling primarily benefits questions with explicit temporal cues.

## Removed Points

These points were raised by reviewers but are removed for the following reasons:

- *"Related work does not adequately position the paper relative to specific works like Reveal (Ye et al., 2023)"* — The rule prohibits criticizing missing related works, as I cannot verify reviewer-specific claims about what should have been cited.
- *"No analysis of failure cases" and "no comparison of computational cost"* — These are suggestions for improvement but not core weaknesses; moved to Nice-to-Haves.
- *"Memory component is under-described"* — Subsumed by Weakness #2 (method description vagueness).
- Criticisms about formatting, typos, or parser artifacts — removed per hard rules.

## Novel Insights

The most interesting finding to emerge from cross-referencing the reviews is the tension between the paper's two strongest pieces of evidence. The ablation study (which controls for tools) shows that each component contributes meaningfully — this is the cleanest empirical support for the architecture. Yet the paper itself leads with the main tables (which do not control for tools) as its primary SOTA claims. A sharper submission would demote the cross-tool comparisons to supporting evidence and foreground the controlled ablation as the central empirical contribution. The MovieChat result, as the most extreme and least validated claim, unfortunately distracts from the method's legitimate strengths on the other three benchmarks.

## Suggestions

1. **Validate or restructure the MovieChat evaluation.** Either add human evaluation on a representative sample (e.g., 100 instances) with inter-annotator agreement, or drop the MovieChat results and focus the claims on the other three benchmarks where evaluation is standard.
2. **Audit all frame-percentage numbers** — the Ego4D value is definitely wrong (recompute to ~0.6%). Use a consistent format (proportion or percentage) across all tables.
3. **Add algorithmic detail to Section 3** — even 1–2 pages of pseudocode or prompt templates in an appendix would dramatically improve reproducibility.
4. **Qualify SOTA claims** to acknowledge that tool differences contribute to the gap in main tables, and point readers to the ablation study for the cleanest comparison.
5. **Add statistical uncertainty** — at minimum, report performance variance over a few runs on one benchmark to indicate the noise level.

## Score and Decision

The paper has a well-motivated architecture and compelling ablation results, but the unvalidated MovieChat evaluation and vague method description are significant weaknesses. The core contributions are real and supported by the non-MovieChat benchmarks, but the paper needs substantial revision — particularly around the MovieChat claims and method details — before it is ready for acceptance.

MY FINAL SCORE: <pineapple>5.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>