Now I have all the information needed. Let me write the consolidated review.

## Summary

BIRD-INTERACT is a benchmark for interactive text-to-SQL evaluation that addresses two key gaps in prior work: (1) reliance on static conversation transcripts rather than dynamic interaction, and (2) narrow SELECT-only task scope. The benchmark introduces a function-driven user simulator that prevents ground-truth leakage, two evaluation settings (c-Interact protocol-guided and a-Interact agentic), and 900 tasks spanning the full CRUD spectrum with state-dependent follow-up sub-tasks. Experiments on 7 frontier LLMs show that even GPT-5 achieves only 8.67% success in c-Interact and 17.00% in a-Interact, demonstrating a significant gap in interactive capabilities.

## Strengths

- **Function-driven user simulator with strong reliability evidence.** The two-stage strategy (Section 3.3) maps system clarification requests to three predefined actions (AMB, LOC, UNA) before generating responses. Figure 6 shows this reduces inappropriate feedback on unanswerable questions from 67.4% (baseline) to 2.7%, directly supporting the claim that the simulator prevents ground-truth leakage. This is a genuine methodological contribution over naive LLM-based simulators.

- **Human alignment validation for the simulator.** Table 3 reports Pearson correlations of 0.84 (GPT-4o, p=0.02) and 0.79 (Gemini-2.0-Flash, p=0.03) between simulator-driven and human-driven success rates on 100 tasks, while baseline simulators drop to 0.61 (p=0.14) and 0.54 (p=0.21). This provides concrete (though moderate-scale) evidence that the simulator produces realistic interaction patterns.

- **Memory grafting experiment isolates communication from generation.** Section 5.2 provides GPT-5 with interaction histories from better-performing models. Figure 5 shows GPT-5's success rate improves from 13.8% to 18.8% (Qwen-3-Coder history) and 20.5% (O3-Mini history), providing causal evidence that GPT-5's poor c-Interact performance stems from communication deficiency rather than SQL generation capability.

- **Two complementary evaluation settings reveal mode-dependent model behavior.** Table 2 shows GPT-5 is worst in c-Interact (14.50% SR) but best in a-Interact (29.17% SR), while Qwen-3-Coder-480B shows the opposite pattern (22.00% c-Interact vs. 13.33% a-Interact). This empirical divergence supports the claim that interaction mode matters and that different models have different interaction aptitudes.

- **Full CRUD coverage with state-dependent sub-tasks.** Section 3.2 describes a 5-category follow-up taxonomy, and Table 1 confirms 190 DM tasks (out of 600) with state-dependent follow-ups. This directly addresses the narrow SELECT-only scope of prior interactive benchmarks like SParC and CoSQL.

- **Action distribution analysis reveals trial-and-error bias.** Section 5.2 reports that *submit* and *ask* actions account for 60.87% of all actions, while systematic exploration (knowledge/schema retrieval) is underused. This provides specific diagnostic insight into LLM behavior in agentic settings.

## Weaknesses

### Major

- **The c-Interact vs. a-Interact comparison confounds interaction mode with tool availability, weakening aptitude claims.** The paper concludes (Section 5.1) that "interaction mode emerged as the decisive factor" and that models show "varying aptitudes for different interaction paradigms." However, c-Interact restricts the system to asking clarification questions and submitting SQL, while a-Interact provides a full 9-action toolbox including schema retrieval, knowledge lookup, and execution. These settings differ on multiple dimensions simultaneously (tool availability, information access, initiative structure), not just the interaction paradigm. GPT-5's strong performance in a-Interact (29.17% SR) may simply reflect that it is a strong SQL generator once it can freely explore the environment, rather than revealing anything about "interaction mode" per se. The memory grafting experiment (Figure 5) more cleanly isolates communication from generation, but the broad claim about "interaction mode as the decisive factor" conflates setting constraints with interaction paradigm. This does not invalidate the benchmark—both settings are independently useful—but the paper should sharply qualify these comparative conclusions.

- **The "ITS Law" claim is not supported by the evidence.** Section 5.2 defines an "Interaction Test-Time Scaling Law" and claims a model satisfies it if performance can match or surpass idealized single-turn performance given enough turns. Figure 4 shows that only Claude-3.7-Sonnet exhibits clear monotonic improvement with increasing patience. Most other models show flat or erratic curves, and none (other than Claude-3.7-Sonnet) approach the single-turn idealized performance even at the highest patience setting. Calling this a "law" suggests a general phenomenon, but the evidence supports at most an observation that *some* models benefit from more turns under specific conditions. The language should be substantially toned down.

### Minor

- **Memory grafting experimental setup is underspecified.** The paper reports that GPT-5's performance improves when given interaction histories from Qwen-3-Coder and O3-Mini (Figure 5), but the numbers (13.8% baseline, 18.8%/20.5% grafted) do not match any entries in Table 2 (e.g., GPT-5 c-Interact priority SR is 14.50% on the FULL set). This suggests a different task subset was used (likely LITE), but this is not stated. The paper should clarify which set and which baseline condition was used, as this directly affects interpretation of the improvement magnitude.

- **The user simulator's behavioral alignment is validated on a moderate scale.** The human evaluation (Section 6, Table 3) uses 100 tasks. While the correlations (0.84, 0.79) are encouraging, the small sample means confidence intervals are wide, and the evaluation only measures correlation of *final success rates* per task—a coarse aggregate. It does not validate whether the simulator produces *realistic conversational trajectories* (e.g., whether it responds to clarification questions in the same order or with the same helpfulness as a human). The USERSIM-GUARD results strongly support reliability, but the direct evidence that the simulator behaves like a human user is suggestive rather than conclusive. The paper should report confidence intervals for the correlations and discuss this scope limitation.

- **High ambiguity density is a design choice that should be acknowledged as such.** Table 1 reports 3.89–5.16 ambiguities per task on average. The minimum budget in c-Interact is set to the number of ambiguities, effectively requiring one clarification question per ambiguity. In real-world database interactions, a single user request rarely contains this many distinct points of ambiguity requiring one clarification turn each. The paper's design ensures tasks are "unsolvable without clarification," which is a valid stress-testing choice, but it means the benchmark tests a specific kind of interactive capability (systematic ambiguity resolution) rather than the full range of natural ambiguity-handling. The paper should add a brief discussion of why this density was chosen and what it implies about generalizability.

### Trivial

- The cost analysis in Table 2 (Avg. Cost column) varies from $0.04 to $0.60 across models, but without controlling for API pricing differences (which vary by model and fluctuate over time), these numbers are hard to interpret as efficiency metrics. The paper should clarify that cost is reported for transparency, not as a controlled comparison, and could supplement with token counts.

## Nice-to-Haves

- Report the budget consumption patterns: what fraction of agents exhausted their budget before completing, and how many unnecessary actions were taken?
- Analyze follow-up sub-task difficulty conditionally: success rate of sub-task 2 given success vs. failure of sub-task 1 would clarify whether difficulty stems from cumulative error or inherent complexity.
- An ablation on the user simulator's impact on model rankings (e.g., run 2-3 models with baseline vs. function-driven simulator) would show whether the benchmark is robust to simulator choice.

## Removed Points

These points are flagged to be removed; treat them with caution:

- **Missing analysis of why follow-up sub-tasks are harder** (Harsh Critic). This is a suggestion for additional analysis, not a weakness of the current benchmark. The paper already reports that follow-ups are harder and provides a plausible explanation (longer context).
- **"The 'Distinct Test Cases 135/191' is puzzling"** (Harsh Critic). This is a clarification question. Multiple tasks can share the same test case when they operate on the same database environment; there is no indication this is a flaw.
- **Cost analysis is not actionable** (Harsh Critic). Moved to Trivial above; the core issue is presentation clarity, not a substantive weakness.
- **Generic strengths** (Strength Finder): "Addresses important gap in text-to-SQL evaluation" and similar framing statements are generic praise for any benchmark paper, not specific evidence-backed strengths.
- **"Budget-constrained awareness for stress-testing"** (Strength Finder #4). This describes the design rather than showing it leads to interesting findings. The ITS experiment is the actual evidence; I've kept that as a separate strength.

## Novel Insights

None beyond the paper's own contributions. The two reviews largely converge on the same strengths and weaknesses; no reviewer identified a capability of the benchmark or a structural flaw that the paper itself does not address or acknowledge.

## Suggestions

1. **Qualify the cross-mode comparison.** Explicitly acknowledge that c-Interact and a-Interact differ not only in interaction paradigm but also in the information and tools available to the system. Use the two settings to ask more precise questions (e.g., "How much does direct SQL execution ability improve performance over pure conversational interaction?").
2. **Tone down the ITS Law claim.** Frame it as an observed pattern in some models rather than a general "law."
3. **Expand the human alignment evaluation.** Report confidence intervals for the correlations, and consider a larger sample (300+ tasks) to strengthen the claim of behavioral realism.
4. **Clarify the memory grafting setup.** State which task set (FULL or LITE) was used and which baseline condition was compared.
5. **Acknowledge the ambiguity density scope.** Add a brief discussion of why 3.89–5.16 ambiguities per task was chosen and what this means for generalizability.

## Score and Decision

**Round 1 Bracket:** 5–7 (based on initial comparison to EHR-ChatQA at 4.00, SPARTA at 5.00, VitaBench at 5.50, and "LLMs Get Lost" at 8.00).

**Round 2 Narrowing anchors read in full:**
- SPARTA (5.00) — BIRD-INTERACT has more human annotation, a more novel core contribution, and stronger validation. Better.
- EHR-ChatQA (4.00) — BIRD-INTERACT has more tasks, a more principled simulator, and full CRUD coverage. Clearly better.
- VitaBench (5.50) — Comparable benchmark quality, but BIRD-INTERACT has stronger simulator validation (USERSIM-GUARD). Slightly better.
- WideSearch (6.00) — Both are well-constructed benchmarks; BIRD-INTERACT has broader task scope and more novel core contribution. Comparable.
- Squirrel Benchmark (5.00) — BIRD-INTERACT is more original, less synthetic-dependent. Clearly better.
- "LLMs Get Lost" (8.00) — Broader and more fundamental; BIRD-INTERACT is more domain-specific. Not comparable.

**Final score rationale:** The paper is a solid, well-motivated benchmark with a genuine contribution (function-driven simulator), strong construction methodology, and interesting empirical findings. It sits clearly above the 4–5.5 tier papers and is broadly comparable to the stronger accepted benchmarks in the 6.0 range. The major weaknesses (confounded comparison, overclaimed ITS law) are real but correctable. I assign a score of 6.0.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>