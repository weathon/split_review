Now I have a complete picture of the paper and can verify all claims against the source text. Here is the consolidated review.

---

## Summary

BIRD-INTERACT converts the single-turn LIVESQLBENCH into a multi-turn interactive text-to-SQL benchmark of 900 tasks (600 FULL + 300 LITE). It introduces a function-driven user simulator that restricts responses to three symbolic actions (`AMB()`, `LOC()`, `UNA()`) to prevent ground-truth leakage — a demonstrated problem with prior LLM-based simulators. Two evaluation settings are defined: *c*-Interact (protocol-guided conversational turns) and *a*-Interact (autonomous agentic planning with 9 discrete actions). Seven frontier LLMs are evaluated, with the best model (GPT-5 in *a*-Interact) achieving only 17.00% end-to-end success on the full set. Additional analyses (memory grafting, interaction test-time scaling, action distributions) probe why models fail.

---

## Strengths

1. **Function-driven user simulator with demonstrated leakage prevention (Section 3.3, Section 6).** The two-stage strategy (semantic parser → action classification → controlled response) is a genuine technical contribution. The USERSIM-GUARD evaluation (Figure 6) shows baseline LLM simulators fail on Unanswerable questions up to 67.4% of the time, while the function-driven approach reduces this to 2.7%. The human alignment study (Table 3) reports that the function-driven GPT-4o simulator achieves Pearson correlation of 0.84 (p=0.02) with human user behavior versus 0.61 (p=0.14) without function calling — a large, statistically meaningful improvement on 100 tasks across 7 models.

2. **Two evaluation settings that surface differential model capabilities (Section 4, Table 2).** *c*-Interact and *a*-Interact define distinct interaction paradigms with separate budget structures, and the results reveal non-obvious patterns: GPT-5 is worst in *c*-Interact (14.50% SR) but best in *a*-Interact (29.17% SR), whereas Qwen-3-Coder-480B shows the opposite trend. This demonstrates the benchmark can differentiate interaction-mode-specific abilities that single-setting evaluations would miss.

3. **Challenging task suite covering the full CRUD spectrum (Section 3.2, Table 1).** The benchmark spans both BI (analytical) and DM (operational) tasks with state-dependent follow-up sub-tasks, injected ambiguities organized into a principled taxonomy (superficial, knowledge, environmental), and an average of 3.89–5.16 ambiguities per task. Even the strongest models achieve only 8.67–17.00% end-to-end success, confirming substantial headroom for future work.

4. **Memory grafting experiment cleanly isolating interaction strategy from SQL generation (Figure 5).** Providing GPT-5 with O3-Mini's interaction history raises GPT-5's success rate from 13.8% to 20.5%, using GPT-5's own SQL generator. This is a clean ablation that supports the paper's central thesis that interaction skill, not SQL generation capacity, is a primary bottleneck.

5. **Comprehensive model evaluation (Table 2).** Seven frontier LLMs (both open- and closed-source) are benchmarked with breakdowns by BI/DM, sub-task (priority vs. follow-up), and normalized reward alongside success rate, providing a rich empirical picture.

---

## Weaknesses

### Fatal
None. The paper's core claims are not invalidated by any single verified flaw. The weaknesses below are addressable limitations, not fatal errors.

### Major

1. **The "dynamic interaction" framing is overstated relative to the simulator's constrained action space (Section 3.3).** The user simulator maps every system question into exactly three actions: `AMB()` (tied to pre-annotated ambiguity points), `LOC()` (AST-based retrieval for other reasonable questions), and `UNA()` (rejection). The paper repeatedly claims "dynamic interactions" (Abstract, Introduction), a "high-fidelity interactive environment" (Section 1), and that models require "strategic interaction skills" (Conclusion). However, the simulator cannot express its own confusion, initiate new topics, negotiate, or provide open-ended feedback beyond these three actions. The interaction fundamentally reduces to a structured resolution of pre-specified ambiguity points. This does not invalidate the benchmark — the controlled design has clear merit for preventing leakage and ensuring fairness — but the paper would benefit from a more measured framing that accurately describes what the benchmark measures: **a model's ability to ask the right clarification questions about known ambiguity categories within a well-defined, rule-governed interaction protocol.** Statements about "dynamic interaction" should be calibrated to match this scope.

2. **The "ITS Law" claim is weakly supported (Section 5.2, Figure 4).** The paper tests only 4 patience levels (0, 3, 5, 7), and the claimed scaling behavior is not monotonic across all models. For example, GPT-4o in *c*-Interact shows a dip between patience 5 and 7. Claude-3.7-Sonnet is the only model with a clean monotonic trend. Calling this an "ITS Law" overstates the strength of the evidence. A more conservative claim — "some models benefit from additional interaction opportunities under this benchmark's specific budget structure" — would be better supported. Additionally, the term conflates user patience with model compute (it is not "model test-time scaling" but rather "varying the number of allowed user turns").

### Minor

3. **No human performance baseline on the benchmark tasks (Section 5).** The paper repeatedly emphasizes low model success rates (8.67–17.00%) as evidence of challenge, but without a human baseline, it is difficult to disentangle whether tasks are genuinely hard but solvable versus poorly designed, unnatural, or with flawed test cases. The single-turn "idealized" performance (Figure 4, 20–40% for many models) provides partial validation that the underlying SQL tasks are solvable, but does not calibrate the *interaction* difficulty. Adding a human performance baseline on a 50–100 task subset would strengthen confidence in the benchmark's validity.

4. **Ambiguity injection realism is not validated (Section 3.2).** The three-category ambiguity taxonomy is systematic and well-documented, but there is no study evaluating whether the injected ambiguities resemble natural user confusion in real-world database querying. The inter-annotator agreement of 93.33% likely measures annotation consistency (agreement on which ambiguity to inject and which clarification source to pair it with), not the naturalness of the resulting tasks. This weakens the claim that the benchmark tests "realistic" interaction scenarios. A small human judgment study comparing injected ambiguities to naturally-occurring ambiguous queries would address this.

5. **No breakdown of success by ambiguity type.** The paper reports overall results but does not analyze which ambiguity types (superficial, knowledge chain-breaking, environmental) pose the greatest difficulty. Such an analysis would reveal whether the benchmark primarily tests interaction skills or knowledge retrieval, and would strengthen the paper's conclusions about "communication effectiveness."

6. **Missing failure mode categorization.** The paper claims communication effectiveness is the key bottleneck (via the memory grafting experiment), but does not systematically categorize model failures into specific types (failed to ask, asked wrong thing, asked correctly but generated wrong SQL, generated correct SQL but failed the follow-up). This would provide stronger evidence for the paper's central thesis.

### Trivial
7. The budget parameters (B_base=6, cost multipliers for actions in *a*-Interact) are presented without justification or sensitivity analysis. A brief note on why these values were chosen would improve reproducibility.

8. The "Inter-Agreement" row in Table 1 (93.33%, 93.50%) does not state what is being measured (ambiguity type annotation? clarification source identification? follow-up sub-task categories?), reducing interpretability.

---

## Nice-to-Haves
- An analysis of budget utilization (do successful models use fewer/more turns? ask the right questions early or explore broadly?)
- A concrete interaction trace (model questions → simulator responses → SQL submissions) for one successful and one failed task, to help readers assess whether the interactions look natural.

---

## Removed Points

The following points from the input reviews were removed with brief justifications:

- **"The two evaluation settings are incomparable by design, yet compared directly"** (Harsh Critic, Point 3). The paper does not claim a controlled comparison isolating a single variable. It presents c-Interact and a-Interact as different evaluation paradigms and observes which models perform better in each — a descriptive finding, not a causal claim about interaction modes. The settings are intentionally different; that is the design.

- **Criticisms about missing release details, missing appendix content, or reproducibility concerns** (e.g., "the paper does not detail whether the test answers are publicly available"). Removed per Hard Rules: the cited benchmark/infrastructure exist, appendix content was stripped by the parser, and reproducibility nitpicks about undisclosed hyperparameters or large artifacts are disallowed.

- **Claims that the memory grafting experiment has a "weak control" because "GPT-5 interacting with its own history is not a clean baseline."** This misinterprets the experiment: the design compares GPT-5 without grafting (GPT-5's own interaction) to GPT-5 with O3-Mini's interaction history. The improvement shows that GPT-5's own interaction strategy is suboptimal — which is exactly the point. The experiment does not claim to identify *why* O3-Mini's strategy is better, only that the primary bottleneck is interaction, not SQL generation.

- **Generic framing that "the evaluation lacks rigor" or that "findings might be due to confounders" without specific anchors in the paper.** Removed as noise per Filtering Discipline.

---

## Novel Insights

The two reviews, taken together, surface an interesting tension: the paper's most rigorous contribution (the leakage-proof, human-aligned simulator) is somewhat at odds with its most ambitious claim (that the benchmark evaluates rich "dynamic" interaction). The simulator's strength — controllability — is also what limits its expressiveness. This suggests a design trade-off that the paper does not fully acknowledge: preventing leakage and ensuring fairness comes at the cost of constraining the interaction space to pre-enumerated ambiguity points. The memory grafting experiment is the cleanest evidence for the "interaction skill matters" thesis precisely because it sidesteps this trade-off — it grafts interaction history from one model and measures generation from another, isolating the communication variable. Future work extending this paradigm might benefit from viewing the simulator not as a general-purpose human proxy but as a specific operationalization of *ambiguity resolution within a known taxonomy*, and scaling the taxonomy rather than opening the interaction space.

---

## Suggestions
1. Tone down the "dynamic interaction" and "high-fidelity" framing to match the simulator's constrained action space. Use precise language: "a controlled ambiguity-resolution benchmark with a leakage-free simulated user."
2. Add a human performance baseline on a representative subset (50–100 tasks) to calibrate the low success rates.
3. Add breakdowns of success by ambiguity type and failure mode analysis to strengthen the claim that interaction skill is the bottleneck.
4. Replace the "ITS Law" claim with a more measured observation about some models benefiting from additional turns, and clarify that the variable being scaled is user patience, not model compute.
5. Validate ambiguity naturalness through a small human judgment study.

---

## Score and Decision

This paper addresses a real gap (interactive text-to-SQL evaluation), makes a solid technical contribution (the leakage-preventing user simulator is convincingly evaluated), runs a comprehensive model comparison (7 LLMs × 2 settings), and provides useful analyses (memory grafting, action distributions). The weaknesses are real — the simulator is more constrained than the "dynamic" framing suggests, the ITS analysis is thin, and several important breakdowns (by ambiguity type, by failure mode) are missing — but none are fatal. The core contributions are sound and the benchmark is likely to be useful to the community.

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>