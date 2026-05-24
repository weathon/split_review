Now I have all the information I need. Let me compose the consolidated review.

## Summary

BIRD-INTERACT introduces a benchmark for evaluating LLMs on interactive text-to-SQL tasks, replacing static conversation transcripts with a dynamic environment featuring a function-driven user simulator, two evaluation settings (protocol-guided c-Interact and agentic a-Interact), and a 600-task suite spanning CRUD operations with injected ambiguities and state-dependent follow-ups. The paper's key deliverables are a user simulator that demonstrably reduces ground-truth leakage (2.7% vs. 67.4% baseline UNA failure rate), a dual-setting evaluation framework that reveals qualitatively different model capabilities, and an empirical finding that even GPT-5 succeeds on only 8.67% of tasks in c-Interact and 17.00% in a-Interact.

## Strengths

1. **Function-driven user simulator with rigorous validation.** The two-stage action-mapping mechanism (AMB/LOC/UNA) is a principled solution to ground-truth leakage and unanswerable-question failures that plague prior LLM-based simulators (MINT, etc.). Figure 6 shows the failure rate on UNA questions drops from 67.4% to 2.7%, and Table 3 reports 0.84 Pearson correlation (p=0.02) with human users — substantially higher than the baseline simulator (0.61, p=0.14). This is the strongest empirical validation of any user simulator in the interactive text-to-SQL literature.

2. **Dual evaluation settings revealing distinct interaction capabilities.** The c-Interact vs. a-Interact contrast is well-motivated and yields non-trivial findings: GPT-5 achieves the worst c-Interact success rate (14.50%) but the best a-Interact rate (29.17%), while Qwen-3-Coder shows the opposite pattern. This demonstrates the benchmark captures genuine interaction-mode-specific abilities, not just a single-turn SQL skill proxy.

3. **Challenging, realistic task suite covering full CRUD spectrum.** The 600 FULL tasks average 3.89 ambiguities and ~13 interactions per task, spanning both BI and DM operations. The systematic ambiguity injection (superficial, knowledge chain-breaking, environmental) with paired clarification sources is well-designed, and the 93.33% inter-annotator agreement confirms annotation quality. The low success rates across all models confirm this is a genuinely hard benchmark, not a saturated leaderboard.

4. **Memory grafting experiment provides causal evidence for communication as a bottleneck.** GPT-5's success rate improves from 13.8% to 18.8% (Qwen-3-Coder history) and 20.5% (O3-Mini history) when grafted with other models' interaction histories, while those same histories do not improve the original models. Since GPT-5 performs the SQL generation in all cases, this cleanly separates SQL capability from interaction strategy.

## Weaknesses

### Major

None.

### Minor

1. **"Interaction Test-Time Scaling" framing overreaches the evidence (Section 5.2, Figure 4).** The paper defines an "ITS Law" as "a model satisfies this law if, given enough interactive turns, its performance can match or even surpass that of the idealized single-turn task." In Figure 4, only Claude-3.7-Sonnet shows a clear upward trend approaching the idealized dotted line in c-Interact; the other three models show flat or ambiguous scaling, and in a-Interact the trends are flat or slightly decreasing across all models. The core observation that "performance improves monotonically with additional interaction opportunities" (stated in the Introduction) is supported for c-Interact, but calling this a "law" and defining it in terms of matching idealized single-turn performance overstates what the data shows. The authors should either remove the "law" terminology or provide systematic evidence across more settings.

2. **Single-run evaluations with no variance estimates (Section 5).** The paper acknowledges "conducting single runs due to cost." With success rates below 20% for most conditions, a single run provides no information about variance. Rankings like GPT-5 at 14.50% vs. Deepseek-Chat-V3.1 at 18.50% in c-Interact BI could easily be within noise. While this does not undermine the paper's main conclusions (the benchmark is hard; the simulator works), it weakens the reliability of cross-model comparisons. Running multiple trials on at least the LITE subset or reporting bootstrapped confidence intervals would substantially strengthen the empirical contribution.

3. **Memory grafting experiment would benefit from a cleaner control (Figure 5).** The experiment provides GPT-5 with interaction histories from Qwen-3-Coder and O3-mini — models that achieved higher c-Interact success rates. Since these histories contain successful clarification trajectories, it is unclear whether GPT-5's improvement comes from adopting better *communication strategies* or simply from receiving the *correct answers* embedded in those histories. A control giving GPT-5 its *own* successful interaction history (when available) would isolate the communication-strategy effect. This does not invalidate the finding (the experiment is still informative) but weakens the precision of the claim that "a more effective communication schema is required."

### Trivial

- Figure 6 uses "AMG" as a label without explanation in the main text (likely an abbreviation or rendering artifact for the Gemini backbone model referenced in Table 3). This should be clarified.

## Nice-to-Haves

- A no-budget (free-mode) a-Interact condition to measure whether budget constraints are the main driver of low a-Interact performance, or whether models genuinely struggle with autonomous planning. The paper lists this as future work but the infrastructure is already in place.
- A sensitivity analysis on the single-debugging-attempt limit in c-Interact (0, 1, 2, 3 attempts) to assess whether this design choice is a significant bottleneck.
- A breakdown of failure modes by ambiguity type (superficial vs. knowledge vs. environmental) to guide future research on targeted interaction strategies.
- Qualitative case studies showing successful vs. failed interactions to illustrate the gap between SQL generation and interaction skill more vividly.

## Removed Points

These points were raised by reviewers but are removed after cross-checking against the paper:

- **"AMG baseline not explained" as a major methodological gap**: The figure labels "Baseline (AMG)" appear to be a parser rendering artifact (the backbone model is identified in Table 3 as Gemini-2.0-Flash). This is a presentation issue, not a methodological gap.
- **"No validation that injected ambiguities resemble real user behavior"**: The paper reports 93.33% inter-annotator agreement on annotation quality and describes a systematic, principled ambiguity taxonomy. Demanding a separate user study to "validate naturalness" is outside the paper's stated scope and is not standard practice for benchmark construction.
- **"Baseline simulator correlations are not statistically significant"**: Table 3 shows baseline correlations of 0.61 (p=0.14) and 0.54 (p=0.21) — the paper reports these honestly and does not make strong claims about them. The comparison with the function-driven simulator (0.84, p=0.02) is valid.
- **"Missing free-mode evaluation"**: The paper explicitly scopes this as future work. The budget-constrained setting is a deliberate design choice to study stress-mode behavior, not an omission.
- **"Should test more debugging attempts"**: A reasonable extension but not a core flaw; the single-debug design is justified as budget-constrained awareness testing.

## Novel Insights

The synthesis of the two reviews surfaces a genuinely interesting tension that the paper itself does not fully articulate. In c-Interact, GPT-5 is the worst model despite being the strongest in a-Interact and on single-turn SQL benchmarks — and the memory grafting experiment shows this gap is about communication strategy, not SQL competence. Meanwhile, the ITS experiment shows that in a-Interact, more interaction budget does not help (curves are flat or decreasing), while in c-Interact, more turns reliably help. This suggests a trade-off: structured conversational protocols (c-Interact) reward interaction skill but constrain strong models like GPT-5, while open-ended agentic settings (a-Interact) reward autonomous planning but are bottlenecked by trial-and-error biases rather than interaction depth. The paper hints at these patterns but does not synthesize them into a clear takeaway about the distinct failure modes of different interaction paradigms.

## Suggestions

1. Tone down or remove the "ITS Law" framing; present it as an empirical observation ("interaction test-time scaling") rather than a law, and clearly distinguish between monotonic improvement (supported) and matching idealized single-turn performance (limited evidence).
2. Run at least 3-5 trials on the LITE subset (300 tasks) for 2-3 representative models to provide variance estimates and strengthen the reliability of cross-model comparisons.
3. Add a control condition to the memory grafting experiment: provide GPT-5 with a *random* interaction history from another model (not just successful ones) to test whether any history helps, or only successful communication strategies.
4. Add a no-budget ablation for a-Interact on the LITE subset to separate budget constraint effects from genuine autonomous planning difficulty.
5. Clarify the "AMG" label in Figure 6 and ensure all backbone model names are clearly identified in figure captions.

## Score and Decision

Calibration anchors (all from the human review corpus):

| Anchor | Avg Score | Comparison to This Paper |
|--------|-----------|-------------------------|
| Spider 2.0 (XmProj9cPs) | 8.00 | More polished execution with no overclaims; BIRD-INTERACT has a stronger focus on interaction dynamics but weaker framing discipline. |
| MINT (jp3gWrMuIZ) | 6.75 | Similar contribution level (multi-turn interaction benchmark); BIRD-INTERACT has stronger user simulator validation but more overclaims. |
| τ-bench (roNSXZpUDN) | 6.50 | Also studies tool-agent-user interaction; BIRD-INTERACT's user simulator validation is more thorough, but τ-bench is better scoped. |
| DB-GPT-Hub (NmILZXKcOi) | 3.75 | Focuses on fine-tuning benchmarks for text-to-SQL; BIRD-INTERACT is more novel in its interactive focus and has stronger empirical contributions. |
| Structure-Rich Text Benchmark (ly10tMV6cD) | 3.25 | Shallow analysis with poor presentation; BIRD-INTERACT is substantially more rigorous, better motivated, and better written. |
| FairMT-Bench (RSGoXnS9GH) | 7.00 | Multi-turn fairness benchmark with solid construction; BIRD-INTERACT is comparable in quality but addresses a different (SQL) domain. |
| WILT (Alba3Y7hcs) | 4.25 | Multi-turn reasoning benchmark with limited novelty; BIRD-INTERACT has a clearer practical motivation and stronger validation. |

This paper makes a solid contribution to interactive text-to-SQL evaluation. The function-driven user simulator is well-validated, the dual evaluation settings yield genuinely interesting results, and the task suite fills a real gap in existing benchmarks. The main weaknesses — overclaimed ITS framing, single-run evaluations without variance, and a memory grafting control that could be cleaner — are all addressable with revisions and do not undermine the core contributions.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>