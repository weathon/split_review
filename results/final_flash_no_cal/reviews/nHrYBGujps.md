Now I have all the information I need to write the consolidated review.

## Summary

BIRD-INTERACT is a benchmark that reimagines text-to-SQL evaluation by introducing a dynamic, multi-turn interactive environment with a function-driven user simulator, dual evaluation settings (c-Interact conversational protocol and a-Interact agentic mode), and a challenging task suite spanning the full CRUD spectrum. The benchmark converts 900 single-turn tasks from LIVESQLBENCH into multi-turn interactive scenarios through systematic ambiguity injection and state-dependent follow-up sub-tasks. Evaluation of seven frontier LLMs shows that even GPT-5 achieves only 8.67% success in c-Interact and 17.00% in a-Interact on the full set, demonstrating substantial room for improvement.

## Strengths

1. **Function-driven user simulator with clear reliability evidence.** Section 6 and Figure 6 show that the proposed two-stage function-driven simulator reduces unanswerable (UNA) response failures from up to 67.4% (baseline) to 2.7%. Table 3 further demonstrates a 0.84 Pearson correlation with human users (p=0.02) compared to 0.61 (p=0.14) for the baseline. These results convincingly validate that the simulator is more reliable and human-aligned than naive LLM-based alternatives.

2. **Dual evaluation settings provide diagnostic power beyond prior benchmarks.** The Memory Grafting experiment (Section 5.2, Figure 5) offers causal evidence that GPT-5's poor c-Interact performance stems from deficient communication strategy rather than weak SQL ability—providing it with interaction histories from Qwen-3-Coder and O3-Mini significantly boosts its success rate. Combined with the finding that GPT-5 achieves the lowest c-Interact SR (14.50%) but the highest a-Interact SR (29.17%) in Table 2, the benchmark demonstrates that the two settings measure qualitatively different interaction skills, a capability absent in prior static-dialogue benchmarks.

3. **State-dependent follow-up sub-tasks isolate a distinct failure mode.** The construction methodology in Section 3.2 deliberately designs follow-up sub-tasks that depend on modified database states from preceding queries, differentiating this from prior multi-turn datasets like SParC and CoSQL. The empirical finding that follow-up success rates are uniformly lower across all models (Table 2) confirms that state-tracking is a measurable bottleneck.

4. **Diagnostic action-distribution analysis reveals systematic model behavior.** The action analysis in Section 5.2 quantitatively shows that *submit* and *ask* together comprise 60.87% of actions in a-Interact, identifying a systematic trial-and-error bias over cheaper exploration actions like *knowledge* or *schema* retrieval. This is a concrete behavioral diagnosis that static benchmarks cannot provide.

5. **The benchmark is timely, well-constructed, and will drive community progress.** The gap between existing static-transcript evaluations and the dynamic interaction evaluated here is real and well-motivated. The systematic annotation pipeline (12 expert annotators, inter-annotator agreement of 93%+, controlled ambiguity injection) demonstrates methodological rigor.

## Weaknesses

### Fatal
None.

### Major

1. **The "ITS Law" is overclaimed and weakly supported.** Section 5.2 introduces an "Interaction Test-Time Scaling (ITS) Law" defined conditionally ("A model satisfies this law if, given enough interactive turns, its performance can match or even surpass that of the idealized single-turn task"). This is a tautological definition rather than a falsifiable law. Moreover, the evidence is model-dependent: Figure 4 shows Claude-3.7-Sonnet exhibits clear scaling in c-Interact, but GPT-4o and Qwen-3 show much weaker improvement, and in a-Interact performance is flat or declines for most models. The paper should soften the "law" framing to a descriptive observation (e.g., "ITS phenomenon") and acknowledge the model-dependence and mode-dependence of the pattern.

2. **Baseline user simulators are underspecified.** Section 6 reports a dramatic improvement in reliability over "baseline" simulators (UNA failure dropping from 67.4% to 2.7%), but never describes what the baselines are. Figure 6 labels them "Baseline (AMG)" and "Baseline (GPT)" — the acronym "AMG" is never defined anywhere in the main text, and the prompt/design of the baseline simulators is not stated. Without this information, the reader cannot interpret the reported improvement, assess whether the comparison is fair, or reproduce the baseline condition. The authors should explicitly document how each baseline simulator was constructed and prompted.

### Minor

1. **Memory grafting experiment subset not specified.** Section 5.2 describes the memory grafting experiment without stating whether it was run on BIRD-INTERACT-LITE or BIRD-INTERACT-FULL. Figure 5's caption also omits this information. Comparing the reported numbers (GPT-5 baseline at 13.8%; Qwen-3-Coder and O3-Mini at 18.5%) against Table 2 (on FULL: GPT-5 at 14.50%, Qwen-3-Coder at 22.00%, O3-Mini at 24.00%) strongly suggests the experiment was on LITE, but this should be stated explicitly. Additionally, the experiment does not control for increased context length per se — GPT-5 with a *random* interaction history of equal length would strengthen the baseline.

2. **CRUD operation breakdown is missing.** The paper repeatedly claims "full CRUD spectrum" coverage but Table 1 only reports BI vs. DM counts. No distribution of SELECT vs. INSERT vs. UPDATE vs. DELETE operations is provided, so the reader cannot assess whether the coverage is actually balanced or representative. This should be reported for both BI and DM subsets.

3. **Reward weighting (70/30) is not stated where it belongs.** The normalized reward uses a 70% / 30% split between priority and follow-up sub-tasks. This is only mentioned in passing in Section 5.1 (line 173) and hinted at in Figure 3's diagram. It should be stated explicitly in Section 2 where the metrics are formally introduced.

4. **Inter-annotator agreement metric is ambiguous.** Table 1 reports "Inter-Agreement" values of 93.33 and 93.50 but does not specify whether this is percentage agreement, Cohen's kappa, Fleiss' kappa, or another metric. This matters because chance-corrected agreement can differ substantially from raw agreement, especially for multi-class annotation tasks.

5. **Ambiguity realism claims are unvalidated.** The paper positions the benchmark as modeling "real-world" usage (abstract, introduction), but the ambiguities are injected through a controlled procedure (Section 3.2) with no validation that they resemble naturally occurring ambiguities in real database interactions. This does not invalidate the benchmark — a controlled test suite is valuable—but the paper should either provide validation evidence (e.g., a small human study comparing injected to naturally-occurring ambiguities) or explicitly position the benchmark as measuring performance under a specific, controlled class of ambiguities.

6. **Default patience parameter λ_pat = 3 is not justified.** Section 4.1 introduces λ_pat = 3 as the default user patience parameter. While Figure 4 provides an ablation over different values, the choice of 3 as the default is not motivated. A brief justification would help users calibrate their own evaluations.

7. **Single-run evaluations and limited statistical characterization.** All model evaluations are conducted as single runs. While temperature=0 reduces variance, some nondeterminism remains (API-level differences, floating-point effects). Running a subset (e.g., BIRD-INTERACT-LITE) multiple times to estimate variance would strengthen the results. Similarly, the human-alignment study (100 tasks) is a reasonable start but confidence intervals for the correlation estimates would improve interpretability.

### Trivial
- The acronym "AMB", "LOC", "UNA" are introduced (Section 3.3) but the corresponding full forms (Ambiguity, Location/AST-based, Unanswerable) should be spelled out more clearly on first use in the main text for readers who skip the figure captions.

## Nice-to-Haves
- **Memory grafting control condition:** Adding a condition where GPT-5 receives a *random* interaction history of matched length would control for the possibility that any additional context (not just effective communication) aids performance.
- **Cost-performance analysis:** Table 2 reports average cost per task but does not discuss the trade-off (e.g., GPT-5 a-Interat costs $0.24 at 29.17% priority SR vs. Claude-Sonnet-4 at $0.51 at 27.83%). A brief cost-efficiency analysis would be useful for practitioners.
- **Free-mode experiments:** The paper acknowledges plans for "free-mode" settings without budget constraints (Section 8). Including even a preliminary free-mode analysis (e.g., on BIRD-INTERACT-LITE with a subset of models) would enrich the characterization of model behavior.
- **Error taxonomy:** A breakdown of *why* models fail (failure to ask for clarification vs. irrelevant questions vs. correct SQL but state confusion) would greatly increase the benchmark's utility for guiding future research.

## Removed Points

These points were identified in the inputs but are excluded from the main review for the reasons stated. Treat them with caution.

- **Harsh Critic: "Missing breakdown of CRUD operations"** point about the missing breakdown — kept as Minor (#2 above).
- **Harsh Critic: "Single-run evaluations with temperature=0 are acceptable…should note that some nondeterminism may still affect results"** — downgraded to Nice-to-have because single-run with temperature=0 is standard in this setting.
- **Harsh Critic: "Cost-performance analysis would be useful"** — moved to Nice-to-haves.
- **Strength Finder: ITS claim of "strong evidence" for construct validity** — partially conflicts with verified weakness about ITS Law overclaim; retained as a more modest observation in strengths but the "strong evidence" framing is dropped.
- **Harsh Critic: "The experiment design also does not control for the effect of additional context length—GPT-5 with a random interaction history of the same length would be a fairer baseline"** — moved to Nice-to-haves as a constructive suggestion rather than a flaw.
- **Hard Rule removals:** Any speculation about "unreleased" models, "cannot be independently verified" claims, or reproducibility concerns about cited entities are removed per the hard rules.
- **Formatting/style nitpicks** and complaints about the parser-stripped appendix are removed per the hard rules.

## Novel Insights

None beyond the paper's own contributions. The key insights — that (1) GPT-5's poor c-Interact performance is remedied by grafting interaction histories from better models, causally demonstrating that interaction strategy matters independently of SQL ability, and (2) that the two evaluation settings reveal a near-complete reversal of model rankings (GPT-5 worst in c-Interact, best in a-Interact) — are already clearly articulated in the paper.

## Suggestions
1. **Add the missing baseline simulator description** (prompts, design choices) to Section 6 so readers can interpret the reported improvement.
2. **Renamed "ITS Law" to "ITS observation" or "ITS phenomenon"** and explicitly note the model-dependent and mode-dependent nature of the scaling pattern.
3. **State the benchmark version used in the memory grafting experiment** (presumably LITE) directly in the main text and in Figure 5's caption.
4. **Report CRUD operation distributions** (SELECT/INSERT/UPDATE/DELETE counts) in addition to the BI/DM breakdown.
5. **Specify the inter-annotator agreement metric** (e.g., "percentage agreement" vs. "Cohen's κ").
6. **Move the reward weighting specification (70/30) to Section 2** where metrics are introduced.
7. **Add a brief acknowledgment** that the ambiguity types are controlled/injected rather than validated against naturally-occurring distributions, and position the benchmark's claim accordingly.

## Score and Decision

This is a strong benchmark paper that makes a genuine contribution. The function-driven user simulator, dual evaluation settings, and state-dependent task design represent real advances over static-transcript benchmarks. The memory grafting experiment is particularly compelling causal evidence. The main issues are overclaims (ITS "Law") and methodological underspecification (baseline simulators, CRUD breakdown), all of which are fixable. No fatal flaws undermine the core contribution.

MY FINAL SCORE: <score>7.5</score>
MY FINAL DECISION: <decision>Accept</decision>