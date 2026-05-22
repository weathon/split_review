Now I have all the information I need. Let me compose the consolidated review.

---

## Summary

This paper introduces Ambig-SWE, a benchmark that extends SWE-Bench Verified by synthesizing underspecified variants of GitHub issues and equipping an agentic evaluation framework with a simulated user proxy. The core contribution is a structured decomposition of handling underspecification into three measurable stages: detecting missing information (RQ2), asking targeted clarification questions (RQ3), and leveraging interaction to solve tasks (RQ1). The paper evaluates six LLMs (proprietary and open-weight) across these stages, finding that forced interaction recovers a large fraction of fully-specified performance, that models default to non-interactive behavior without explicit prompting, and that question quality and integration strategy matter more than extraction volume.

## Strengths

- **Clean three-stage evaluation framework with paired ground truth.** The paper creates synthetically underspecified variants of SWE-Bench Verified issues (Section 2.1) paired with the original full specifications, enabling causal measurement of how interaction recovers missing information. The decomposition into detection, questioning, and task completion (RQs 1–3) provides a diagnostic lens that pinpoints where models fail — e.g., Qwen 3 Coder's 100% false-negative rate in detection (Table 2) and Llama 3.1's low information gain (Figure 5). This structured design is the paper's strongest methodological contribution.

- **Rigorous comparative analysis with complementary metrics.** Six modern LLMs spanning both proprietary (Claude Sonnet 4, Sonnet 3.5, Haiku 3.5) and open-weight families (Llama 3.1 70B, Deepseek-v2, Qwen 3 Coder) are evaluated across three prompt conditions for detection (Table 2) and with statistical significance testing (Wilcoxon Signed-Rank) for resolve-rate differences (Section 3.1). The dual metrics for question quality — cosine distance and LLM-as-judge (Figures 5, 6) — provide convergent evidence that Llama 3.1 underperforms while Claude Sonnet 4 achieves information gain comparable to Qwen 3 Coder with ~50% fewer questions.

- **Actionable qualitative insights into question-asking strategies.** The dissection of question patterns (Section 5.3, Figure 4, Table 7) reveals three distinct approaches — exploration-first (Claude Sonnet), template-rigid (Haiku), and high-volume extraction (Qwen/Deepseek) — and connects these to downstream performance, showing that question quality and adaptive integration, not extraction volume, drive gains from interaction.

- **Clear empirical demonstration that detection is the bottleneck.** RQ2 (Table 2) shows that without explicit prompting, models almost never interact even for severely underspecified inputs, and that Qwen 3 Coder completely fails to interact under any prompt condition. The finding that prompt engineering provides limited and model-dependent improvement for detection is both surprising and practically important.

## Weaknesses

### Fatal

None.

### Major

- **Synthetic underspecification distribution differs systematically from naturally vague issues.** The paper's own distributional analysis (Section 2.1) reveals that the GPT-4o-generated Hidden issues are systematically more stripped-down than real vague GitHub issues — natural underspecified reports typically retain concrete technical details (stack traces, error messages, file references) even when incomplete. The paper argues that some natural issues are similarly bare and that the paired ground truth is necessary for causal measurement. Both points are reasonable, but the distributional gap has concrete consequences: (a) the Hidden baseline is likely harder than most real-world underspecification, making the measured benefit of interaction an upper bound; and (b) the detection task contrasts fully-detailed vs. nearly-blank issues, which may inflate the apparent difficulty of detection relative to real-world settings where missing information is more subtle. The paper would be stronger if it discussed how these distributional differences qualify the quantitative claims, particularly for detection accuracy.

### Minor

- **Turn budget asymmetry confounds efficiency comparisons across models.** Claude Sonnet 4 and Qwen 3 Coder receive up to 100 turns while other models get 30 (Section 3.1). The paper notes this is "to account for their greater reasoning and planning capacity," but since step counts are later used to comment on efficiency (e.g., "interaction yields no efficiency gains"), the unequal budgets make cross-model efficiency comparisons unreliable. Reporting results under equalized turn limits, or at minimum justifying the asymmetry with evidence that the constrained models would be unfairly penalized otherwise, would strengthen the analysis.

- **Detection experiment details are thin.** RQ2 (Section 4) does not specify the class balance (presumably 50/50 given the randomized presentation), the number of runs per prompt condition, or whether results are averaged across multiple seeds. These details matter for interpreting the accuracy, FPR, and FNR numbers in Table 2.

- **Idealized interaction protocol inflates observed benefit.** The Interaction setting requires compulsory interaction (the agent is explicitly prompted to ask) and uses a GPT-4o user proxy that provides perfectly information-bounded, cooperative answers. The paper acknowledges this in Section 7 ("simulated user proxy may be more cooperative than real users"), and RQ2 already demonstrates that models rarely choose to interact unprompted. But the abstract's "up to 74% improvement" and the main text's framing of the interaction benefit would be more precise if they explicitly noted that these gains represent an upper bound under near-ideal conditions, since real deployments must contend with both the detection gap and less cooperative users.

### Trivial

- **The "74%" in the abstract is ambiguous.** It is unclear whether this is a relative percentage improvement over the Hidden baseline or a recovery rate toward the Full setting. The paper uses several normalized metrics across sections, and a reader cannot tell from the abstract alone what the number refers to. Clarifying would prevent misinterpretation (e.g., mistaking a relative gain for an absolute percentage-point gain).

- **The efficiency framing could be more precise.** Section 3.2 states "interaction yields no efficiency gains" based on comparing average steps in Hidden vs. Interaction settings. Since interaction adds question-asking turns by construction, the fact that total steps do not decrease is unsurprising; the more informative framing would be that interaction adds overhead without reducing the core coding effort.

- **LLM-as-judge rubric is only sketched in the main text.** Section 5.1 describes the scoring as "1-5 scale based on specificity and novelty of information" but does not provide example anchors or criteria that distinguish a score of 3 from a 4. Details are presumably in the (stripped) appendix but at least a one-sentence operationalization in the main text would improve interpretability.

## Nice-to-Haves

- **Bridging RQ1 and RQ2 with an opt-in interaction experiment.** Running the Interaction setting without compulsory interaction (using the Neutral prompt from RQ2) and measuring the resulting resolve rates would directly quantify how much performance is lost because models fail to detect underspecification, grounding the detection findings in the task-completion results without relying on a separate detection-only experiment.

- **Sensitivity test with partially informative Hidden issues.** Keeping some diagnostic information (e.g., error messages) in a subset of Hidden issues would probe how the distributional gap between synthetic and natural underspecification affects the measured interaction benefit and detection difficulty.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **[REMOVED] "Missing appendix / not in main text" criticisms about LLM-as-judge rubric details, statistical test p-values, and concrete examples.** The parser strips appendix sections; these exist in the original submission. The main text provides sufficient high-level description.

- **[REMOVED] "The claim that prior work focuses on only a single missing detail might overstate novelty."** The paper appropriately scopes this claim and the distinction (multi-step agentic tasks with interdependent gaps vs. single-detail disambiguation) is substantive and well-supported.

- **[REMOVED] Speculation that the detection difficulty is "inflated" beyond real-world settings.** The distributional gap is real, but the claim that this specifically inflates detection difficulty is speculative — the paper shows that even Claude Sonnet 4 only achieves 89% accuracy under Strong Encouragement, suggesting detection is genuinely hard. The distributional concern is retained as a Major weakness but the speculative inflation claim is removed.

- **[REMOVED] Concerns about model availability, release status, or existence of cited systems.** All cited models, tools, and benchmarks are assumed to exist as referenced.

## Novel Insights

The paper's most genuinely novel insight is the disconnect between information extraction volume and task-completion benefit. Qwen 3 Coder extracts the most information (highest cosine distance) and asks the most questions, yet achieves worse resolve rates than Claude Sonnet 4, which extracts slightly less information with far fewer, more strategically chosen questions. Even more striking, Qwen's performance *worsens* when it receives navigational information (Table 1), because it rigidly follows a predetermined protocol and re-discovers the same information from the codebase, wasting interaction turns. This finding — that integration strategy and behavioral flexibility dominate extraction volume — goes beyond the expected "interaction helps" result and provides concrete guidance for training agents that can adaptively incorporate user feedback rather than treating it as an add-on to a fixed workflow.

## Suggestions

- Add a sentence to the abstract clarifying what the "74%" refers to (e.g., "up to 74% relative improvement over the non-interactive Hidden setting, measured as recovery toward fully-specified performance").
- Include a brief discussion in Section 3 of how the turn budget asymmetry (30 vs. 100) may affect efficiency comparisons, and if possible, report a robustness check with equalized limits.
- In Section 5.1, provide a one-sentence operational anchor for the LLM-as-judge scale (e.g., "Score 1 = no new information beyond the original prompt; Score 5 = provides specific file paths, function signatures, and expected behavior").
- Expand the discussion of the synthetic-vs-natural underspecification gap in Section 2.1 or Section 7 to explicitly address how it qualifies the quantitative detection and interaction-benefit claims.

## Score and Decision

**Originality:** The paper introduces a novel benchmark variant and a clean three-stage evaluation framework for interactive handling of underspecification in agentic software engineering. The decomposition into detection, questioning, and integration is a genuinely useful lens not present in prior work.

**Importance:** As AI agents are increasingly deployed for software engineering tasks with underspecified instructions, understanding when and how they should interact with users is both timely and practically significant. The finding that detection is the bottleneck and prompt engineering is insufficient has direct implications for model training and system design.

**Claims supported:** The core claims — that interaction recovers performance, that detection is poor without prompting, and that question quality trumps quantity — are well supported by the experiments. The synthetic underspecification limits external validity of exact numbers but does not undermine the qualitative findings.

**Soundness:** The experimental design is rigorous: three controlled settings, statistical significance testing, complementary metrics for question quality, and qualitative trajectory analysis. The main methodological concern is the distributional gap between synthetic and natural underspecification, which the paper acknowledges and discusses.

**Clarity:** The paper is well-written and well-structured, with clear RQ-driven organization. Minor ambiguities (the "74%" figure, the LLM-as-judge rubric) are addressable.

**Value to community:** The benchmark, framework, and empirical findings will be useful for both model developers (to improve interaction capabilities) and system builders (to understand when and how to prompt for interaction). The three-stage decomposition provides a blueprint that can extend beyond software engineering.

**Calibration:**

| Anchor | Score | Round | Comparison |
|--------|-------|-------|------------|
| DataSciBench (BltaWJZMeR) | 3.20 | R1 | Ambig-SWE is substantially stronger — cleaner methodology, clearer contributions, more rigorous evaluation |
| SWE-bench original (VTF8yNQM66) | 6.25 | R2 | Ambig-SWE builds on SWE-bench and adds interactive evaluation; clearly more insightful and better structured |
| MINT (jp3gWrMuIZ) | 6.75 | R2 | Similar in spirit (simulated user interaction) but Ambig-SWE has tighter focus, more actionable findings |
| Commit0 (MMwaQEVsAg) | 6.67 | R1/R2 | Both are benchmark papers building on existing frameworks; Ambig-SWE's structured RQ decomposition is stronger |
| Multi-Turn Code Gen (Zk9guOl9NS) | 7.00 | R2 | Both are strong empirical evaluations; Ambig-SWE has more novel framework contribution |
| Active Task Disambiguation (JAMxRSXLFz) | 7.33 | R1/R2 | Topically closest anchor; Ambig-SWE uses more realistic/complex tasks (SWE-Bench vs. 20-questions) and has more thorough evaluation |
| MLE-Bench (6s5uXNWGIh) | 8.00 | R1 | MLE-Bench is more ambitious in scope and scale; Ambig-SWE is more focused with cleaner analytical framework |

Round 1 bracket: 6.5–8.0. Round 2 narrowed to the 7.0–7.5 range by comparison with JAMxRSXLFz (7.33) and MLE-Bench (8.0). Ambig-SWE is stronger than JAMxRSXLFz (more realistic tasks, more comprehensive evaluation) but below MLE-Bench (less ambitious scale, synthetic underspecification limitation). Final score: 7.5.

MY FINAL SCORE: <score>7.5</score>
MY FINAL DECISION: <decision>Accept</decision>