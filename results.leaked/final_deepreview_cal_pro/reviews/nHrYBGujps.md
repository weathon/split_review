Now let me write the final consolidated review.

---

## Summary

BIRD-INTERACT introduces a benchmark for evaluating interactive text-to-SQL systems that moves beyond static multi-turn datasets. It provides a dynamic environment with a function-driven user simulator, two evaluation settings (protocol-guided *c*-Interact and open-ended *a*-Interact), and 900 tasks spanning the full CRUD spectrum with injected ambiguities and state-dependent follow-up sub-tasks. Evaluation of seven frontier LLMs reveals that even the strongest models complete only 8.67–17.00% of tasks end-to-end, demonstrating a substantial gap between current SQL generation capabilities and the interactive skills needed for real-world database assistants.

## Strengths

- **Function-driven user simulator effectively prevents unreliable behavior.** Section 6 (Figure 6) demonstrates that baseline LLM-based simulators fail up to 67.4% of the time on unanswerable questions, while the proposed two-stage approach (classifying requests into AMB/LOC/UNA actions before generating controlled responses) reduces the failure rate to 2.7%. Table 3 further shows stronger alignment with human users (Pearson r = 0.84 with function-driven design vs. 0.61 without).

- **Task design incorporates realistic and diverse ambiguity types.** Section 3.2 details three structured ambiguity injection strategies — superficial query ambiguities (intent-level and implementation-level), knowledge ambiguities (one-shot and chain-breaking), and environmental ambiguities — plus follow-up sub-tasks with explicit state dependency on prior queries. This creates a benchmark that genuinely requires interaction rather than rewarding models that can guess through ambiguity.

- **Dual evaluation settings expose contrasting model–mode aptitudes.** Table 2 shows that GPT-5 ranks worst in *c*-Interact (14.50% priority-question SR) but best in *a*-Interact (29.17%), while other models show the reverse pattern. This demonstrates that different interaction paradigms favor different model capabilities and that evaluating only one mode would give an incomplete picture.

- **Empirical results convincingly demonstrate the benchmark's difficulty.** Table 2 shows that no model exceeds 16.33% end-to-end success in *c*-Interact or 17.00% in *a*-Interact on the FULL set, with most models substantially lower. Follow-up sub-tasks are uniformly harder than priority sub-tasks, and BI queries prove more challenging than DM queries, confirming that BIRD-INTERACT stresses capabilities beyond single-turn SQL generation.

- **The memory grafting experiment provides insight into model-specific bottlenecks.** Figure 5 shows that providing GPT-5 with clarification histories from better-communicating models (Qwen-3-Coder, O3-mini) significantly improves its success rate, supporting the claim that GPT-5's deficit is in interactive communication rather than core SQL generation.

## Weaknesses

### Fatal

None.

### Major

None.

### Minor

- **Human-correlation validation of the user simulator relies on a small effective sample.** Table 3 reports Pearson correlations computed across 7 model–system pairs (success rates aggregated over 100 tasks). With N=7, the correlations (0.84, 0.79) could be sensitive to a single outlying model, and per-task agreement metrics (e.g., whether the simulator and human agree on which clarifications are needed) are not reported. The USERSIM-GUARD experiment provides strong independent validation of action-routing reliability, but the direct evidence that simulator-mediated rankings match human-mediated rankings would benefit from a larger-scale study or finer-grained agreement measures.

- **The memory grafting experiment does not fully disentangle asking from answering.** Figure 5 shows that GPT-5 improves when given clarification histories from better models, which supports the claim that communication is the bottleneck. However, the experiment compares GPT-5's own interaction histories against those of other models without controlling for the information content of the clarifications themselves. A more controlled design (e.g., comparing GPT-5's own dialogue turns against those of others while measuring what information each turn actually elicited) would strengthen the conclusion.

- **The "ITS Law" framing overstates what is shown.** The paper defines a law ("performance can match or even surpass that of the idealized single-turn task") but no model is demonstrated to satisfy it — Figure 4 shows performance increasing with patience but generally remaining below the idealized baseline. The observation is better characterized as an interaction scaling trend, and the current framing implies a generality the evidence does not yet support.

- **The normalized reward metric is not fully specified in the main text.** Section 2 references Appendix F for the complete definition, and while Section 5.1 mentions the 70/30 priority-vs-follow-up split, the debugging penalty structure and exact normalization procedure are not described, making the Reward* column in Table 2 partially opaque to readers of the main text alone.

### Trivial

- The inter-annotator agreement values in Table 1 (93.33, 93.50) are reported without an explanation of what was measured or how agreement was computed, though the methodology is presumably in the (stripped) appendix.

- No confidence intervals or bootstrapped ranges are reported for success rates, making precise model comparisons difficult. With temperature=0 the evaluation is deterministic, but task-level bootstrapping would clarify whether modest score differences between models are meaningful.

## Nice-to-Haves

- A dedicated failure analysis for follow-up sub-tasks (categorizing why second queries fail even when the first succeeded) would leverage the unique state-dependency aspect of the benchmark and provide actionable insights for model developers.

- Extending the human-correlation study to a larger set of tasks with per-turn agreement metrics would substantially strengthen confidence in the simulator as a human proxy.

- Reporting action-distribution patterns broken down by model identity and correlating them with task success would make the *a*-Interact action analysis (Section 5.2) more diagnostic.

## Removed Points

These points are flagged to be removed, treat them with caution:

- **"The user simulator validation is too fragile to carry the conclusions"** — This overstates the concern. The USERSIM-GUARD experiment (Figure 6) provides strong evidence that the function-driven approach correctly routes clarification requests, and the human-correlation study, while thin (N=7), yields statistically significant results in the expected direction. The simulator architecture is structurally more reliable than pure LLM-based alternatives. The concern is retained as a Minor weakness above with appropriate scope.

- **"Single-run evaluation makes it impossible to tell whether model differences are meaningful"** — With temperature=0 and deterministic evaluation, stochastic variation from the model side is eliminated. Task-sampling uncertainty exists but standard errors for proportions with 600 tasks are modest (~1.5pp for rates around 15%). Retained as Trivial.

- **"The ITS Law is never actually tested"** — The paper defines ITS Law as a conceptual property and shows models exhibiting scaling behavior consistent with approaching it. It does not claim any model satisfies the law. Retained as a Minor concern about grandiose framing, not a factual error.

- **"Comparison with existing interactive benchmarks is limited to a statistical table in Appendix E"** — The appendix is stripped by the parser; the original submission likely contains this material. Removed.

- **"Interaction Mode Emerged as the Decisive Factor is speculative"** — The paper explicitly labels the causal attribution as a hypothesis ("we hypothesize stem from differences in training data distributions and architectural inductive biases"), which is appropriate for an empirical observation paper. Removed.

- **"Failure analysis for follow-up sub-tasks is absent"** — May be present in stripped appendices; cannot verify from main text alone. Moved to Nice-to-Haves.

## Novel Insights

None beyond the paper's own contributions. The key finding — that frontier LLMs excel at SQL generation in single-turn settings but collapse when required to conduct clarification dialogues and recover from errors in an interactive loop — is well-demonstrated and carries important implications for the deployment of text-to-SQL systems in practice. The observation that a model (GPT-5) can be simultaneously worst in one interaction mode and best in another is a genuinely non-obvious result that should influence how the community evaluates and develops interactive systems.

## Suggestions

- Add a concise definition of the normalized reward (including the debugging penalty and how it is weighted relative to the 70/30 priority/follow-up split) to Section 2 or 4 so that Table 2 is fully interpretable from the main text.

- Reframe the "ITS Law" as "interaction scaling trends" or similar, and explicitly note that no evaluated model yet satisfies the idealized condition, to avoid implying stronger conclusions than the data support.

- Consider reporting bootstrapped 95% confidence intervals for aggregate success rates (even as a small table in an appendix) to give readers a sense of task-sampling uncertainty when comparing models.

## Score and Decision

**Calibration summary:**

| Anchor | Avg Score | Round | Comparison |
|--------|-----------|-------|------------|
| `lMW9d1AqC9` (R-KinetiQuery) | 1.67 | R1 | Much weaker — niche, poorly validated |
| `wwO8qS9tQl` (ALMANACS) | 3.00 | R1 | Much weaker — smaller scope, less rigorous |
| `BltaWJZMeR` (DataSciBench) | 3.20 | R1 | Weaker — less principled construction |
| `Avg6hmtgHE` (Wikipedia Graph QA) | 3.40 | R1 | Weaker — narrower scope |
| `NmILZXKcOi` (DB-GPT-Hub) | 3.75 | R1 | Weaker — primarily an engineering integration |
| `7ZeoPg3eTA` (TrustSQL) | 4.00 | R1 | Weaker — limited domains, thinner contribution |
| `NfUHBaZdLw` (EvoSchema) | 4.25 | R1 | Weaker — narrower scope, less impactful |
| `WYdpjwKQma` (LAIA-SQL) | 5.00 | R2 | Weaker — method paper, less ambitious |
| `RaSLSUCKz0` (SQL-GEN) | 5.67 | R2 | Weaker — method paper, narrower |
| `BAglD6NGy0` (ROUTE) | 6.25 | R2 | Weaker — method paper, different category |
| `CvGqMD5OtX` (CHASE-SQL) | 6.25 | R2 | Different category (method), but BIRD-INTERACT has broader contribution |
| `roNSXZpUDN` (τ-bench) | 6.50 | R2 | Similar concept (interactive benchmark with user simulator), but BIRD-INTERACT has more principled simulator design and richer task construction |
| `XmProj9cPs` (Spider 2.0) | 8.00 | R1 | Stronger — more direct real-world grounding, essentially flawless reviews |

**Round 1 bracket:** 4.25 (EvoSchema) to 8.0 (Spider 2.0). The paper is clearly above the 3.0–4.25 cluster of weaker benchmarks and below Spider 2.0's 8.0.

**Round 2 narrowing:** BIRD-INTERACT is stronger than τ-bench (6.50) — it has a more principled function-driven simulator with validation (USERSIM-GUARD), dual evaluation settings, and more comprehensive task construction covering full CRUD. It is somewhat below Spider 2.0 (8.0) — Spider 2.0 had essentially no weaknesses raised by any reviewer and directly grounded tasks in real enterprise use cases, while BIRD-INTERACT has some thin spots in simulator validation and a few underdeveloped analyses.

**Final score:** 7.0. This reflects a strong benchmark paper that fills a genuine gap, is well-constructed, and produces valuable empirical findings. The minor weaknesses (thin human-correlation study, slightly overclaimed ITS framing, opaque reward metric in main text) are addressable and do not undermine the core contributions.

MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>