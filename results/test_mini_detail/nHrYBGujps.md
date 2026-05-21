Now I have a solid understanding of the calibration landscape. Let me produce the final consolidated review.

### Round 1 Bracket: Between 4.5 and 7.5

The paper is clearly above the weak band (avg 1.67–3.0, mostly withdrawn/reject) and below the top tier (Spider 2.0 at 8.0). The most plausible range is between 5 and 7.

### Round 2 Narrowing: Between 5.5 and 6.5

Comparing against SOTOPIA (6.67, spotlight), GameArena (6.5, poster), and IVCR-200K (4.67, withdrawn), the paper is comparable to GameArena but below SOTOPIA due to the simulator leakage gap and overclaiming of the ITS Law.

**Final score: 5.5**

Now let me write the consolidated review, carefully filtering the harsh critic's points against the paper.

Let me verify a few specific claims from the harsh critic against the paper before writing:

1. "LOC() uses AST-based retrieval to locate the relevant SQL fragment" — Lines 96-98 confirm this: "LOC() handles reasonable clarification requests... the simulator uses an AST-based retrieval step to locate the relevant SQL fragment (detailed in Appendix N)."

2. "The paper does not analyze whether the information provided by the simulator in LOC() cases would be available from a knowledgeable but non-oracular human user" — Verified. The USERSIM-GUARD evaluation (Figure 6) tests action classification accuracy, not content leakage.

3. "Single-run experiments" — Line 177 confirms: "conducting single runs due to cost."

4. "ITS Law based on insufficient evidence" — The paper shows 4 models in Figure 4. Only Claude-3.7-Sonnet clearly shows the pattern. The paper defines the ITS Law in lines 221-222.

5. "Budget formulas lack justification" — Verified. Lines 139 and 147 give formulas without sensitivity analysis.

Now let me also verify the strength finder's claims:

1. "Function-driven user simulator that prevents ground-truth leakage" — The paper says it reduces leakage. Figure 6 shows UNA failure rate reduced to 2.7%. But "prevents" is too strong. I'll weaken this.

2. "Task suite covering the full CRUD spectrum" — Table 1 and Section 3.4 confirm this.

3. "Two evaluation settings" — Section 4 and Table 2 confirm this.

4. "Inter-annotator agreement of 93.33%" — Table 1 confirms this.

5. "Alignment with human behavior (Pearson 0.84)" — Table 3 confirms this.

Now let me check which of the harsh critic's points can be REMOVED based on the hard rules:

- "The paper does not discuss whether the system is informed of the budget (the 'awareness' mechanism) or how that is implemented in the prompt." — The paper says on line 123: "systems are informed of the remaining budget." So the paper DOES discuss this. The critic is wrong. REMOVE this.

- "No qualitative examples of user-simulator conversations in the main paper" — The paper has Figure 1 showing a conversation diagram. This is a minor presentation point, not really a weakness. But the critic is technically correct that there's no actual dialogue transcript in the main paper. However, this is a minor point and the paper has prompts in Appendix R (removed). I'll move this to removed points as a minor nitpick.

- "The action cost table for a-Interact is not in the main paper" — The costs are shown visually in Figure 3 as "cost multipliers" and the paper says "Further details of action costs are provided in Appendix J" (line 147). Since the appendix is removed, this is a parser issue. REMOVE.

- "No discussion of potential non-determinism in the user simulator" — Temperature=0 is used. This is a reasonable concern but fairly minor.

Let me think about the strengths from the Strength Finder more carefully:

Strength: "Function-driven user simulator that prevents ground-truth leakage" — The paper does show it reduces UNA failure to 2.7%, and the human correlation study supports it. But the harsh critic's point about LOC() content leakage is legitimate. So the strength is real but overstated by the strength finder. I'll keep a weakened version.

Let me now write the review.Now let me write the consolidated review.

## Summary

BIRD-INTERACT is a benchmark for evaluating text-to-SQL systems in dynamic, multi-turn interaction settings. It contributes: (1) a function-driven user simulator that maps model queries to three constrained actions (AMB, LOC, UNA) before generating responses, designed to prevent ground-truth leakage; (2) 600 interactive tasks spanning the full CRUD spectrum (SELECT, INSERT, UPDATE, DELETE) across both business-intelligence and data-management domains; and (3) two evaluation modes — c-Interact (conversational protocol) and a-Interact (agentic, with a budget-constrained action space). Experiments on 7 frontier LLMs show that even GPT-5 achieves only 17.00% task success, demonstrating a significant gap between single-turn SQL ability and interactive problem-solving.

## Strengths

1. **Function-driven user simulator with validated improvements.** The two-stage design (Section 3.3) constrains responses to three symbolic actions — AMB, LOC, and UNA — before generation. This demonstrably improves controllability: on USERSIM-GUARD, UNA failure rates drop from up to 67.4% (baseline) to as low as 2.7% (Figure 6). The human-correlation study (Table 3) further validates that this simulator aligns better with actual human behavior (Pearson ρ = 0.84, p = 0.02) than the baseline (ρ = 0.61, p = 0.14). This is a concrete, measured improvement over prior LLM-as-user-simulator approaches.

2. **Comprehensive task suite covering the full CRUD spectrum.** Unlike existing multi-turn text-to-SQL benchmarks (CoSQL, SParC) limited to SELECT-only, BIRD-INTERACT includes both BI (410 tasks) and DM (190 tasks) queries spanning Create, Read, Update, and Delete operations, unfolding into 11,796 dynamic interactions (Table 1). The state-dependency between sub-tasks (e.g., a follow-up query that depends on a table created in the previous sub-task) adds a realistic dimension absent from static-conversation benchmarks.

3. **Dual evaluation settings reveal meaningful model-specific interaction patterns.** The two settings (Section 4) — c-Interact (protocol-guided conversational) and a-Interact (agentic with tool-use and budget) — produce distinct model rankings. GPT-5 is worst in c-Interact (14.50%) but best in a-Interact (29.17%), while Gemini-2.5-Pro leads in c-Interact (25.00%) but trails in a-Interact. This demonstrates that the benchmark captures genuine differences in interaction strategy, not just SQL ability. The budget-constrained design also enables stress-testing under resource limits.

4. **High annotation quality.** Inter-annotator agreement of 93.33% (Table 1) on both LITE and FULL sets, achieved through a rigorous multi-stage annotator selection process (Appendix C), supports the reliability of the task annotations.

## Weaknesses

### Fatal
None.

### Major

1. **Potential information leakage through LOC() responses is not analyzed.** The user simulator uses the ground-truth SQL to generate responses for both AMB() and LOC() actions (Section 3.3). While UNA() is designed to reject inappropriate requests, LOC() performs "AST-based retrieval to locate the relevant SQL fragment" for reasonable clarification questions. The paper does not analyze whether the content of LOC() responses could reveal more information than a knowledgeable human user would provide — e.g., whether a targeted sequence of LOC() queries could extract partial SQL fragments that make the task substantially easier. The USERSIM-GUARD evaluation (Figure 6) only tests action classification accuracy, not information leakage through legitimate LOC() responses. Since the validity of the benchmark as a measure of interactive capability depends on the simulator not being an oracle, this is a significant gap that should be addressed either by (a) an empirical audit quantifying what information LOC() can reveal, or (b) a redesign that removes ground-truth SQL from the response generation pipeline.

2. **The "Interaction Test-Time Scaling Law" is overclaimed given the evidence.** The paper introduces an "ITS Law" stating that a model can match or surpass single-turn performance given enough turns. However, Figure 4 shows this pattern clearly for only one of four models shown (Claude-3.7-Sonnet, and only in c-Interact). The other three models do not exhibit clear scaling, and in a-Interact the trends are flat or slightly decreasing. The paper should either (a) present this as a preliminary observation about Claude-3.7-Sonnet rather than a general "law," or (b) provide systematic evidence across all 7 models and both settings.

### Minor

1. **Single-run experiments without variance estimates.** The main results (Table 2) are from single runs at temperature=0 (line 177), acknowledged as "due to cost." While deterministic decoding reduces model stochasticity, differences of 2–5 percentage points between models (or between BI vs. DM sub-groups) cannot be assessed for significance. Conclusions like "Gemini-2.5-Pro ... capture only 20.92%" would benefit from bootstrap confidence intervals across the 600 tasks, which is feasible even from a single run.

2. **Budget formulas and action costs lack empirical justification.** The c-Interact budget (τ_clar = m_amb + λ_pat) and a-Interact budget (B = 6 + 2m_amb + 2λ_pat) are given without sensitivity analysis. The base budget of 6 and the cost multipliers for actions (Figure 3) are design choices that could affect which models succeed or fail. Without analysis (e.g., varying the base budget, testing different λ_pat values), it is unclear whether the rankings are robust to these choices.

### Trivial
None.

## Nice-to-Haves

- A dialogue transcript example in the main paper would help readers intuitively assess whether the simulator's responses are realistic and non-oracular.
- The claim that "GPT-5 possesses robust SQL generation capabilities" (from the memory grafting experiment, Figure 5) is reasonable but the improvement from 13.8% to 20.5% with O3-mini's history still leaves absolute performance low; the claim could be more precisely stated as "GPT-5's SQL generation can benefit substantially from better interaction histories."
- Non-determinism in the LLM-as-parser stage of the simulator could be measured, even at temperature=0.

## Removed Points

- **"The paper does not discuss whether the system is informed of the budget"** — The paper explicitly states (Section 4): "systems are informed of the remaining budget." The critic's claim is incorrect.
- **"Action costs not in the main paper"** — Costs are shown visually as multipliers in Figure 3, and detailed costs are in Appendix J (removed by the parser). This is a presentation choice, not a missing element.
- **"No qualitative examples of user-simulator conversations"** — Figure 1 provides an illustrated interaction diagram; full prompts are in Appendix R (removed by parser). Reasonable for a main paper to summarize rather than include full transcripts.
- **"Missing related works"** — Removed per policy; cannot verify existence of unmentioned works.
- **Strength Finder: "prevents ground-truth leakage"** — Overstated; the paper shows *reduced* leakage (2.7% vs 67.4% for UNA), not complete prevention. Kept as a real strength but rephrased more carefully.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. **Audit LOC() leakage.** Run an experiment where a probing agent attempts to reconstruct SQL fragments solely through LOC() queries, and measure whether the information provided exceeds what a domain-knowledgeable human (without the SQL) could give. If leakage is minimal, report this as a validation; if significant, restrict LOC() to only HKB-available information.

2. **Add confidence intervals.** Bootstrap the 600-task results to produce interval estimates, even from single runs. This adds credibility to model comparisons without additional API cost.

3. **Clarify ITS claims.** Show all 7 models for the scaling analysis, and present the ITS Law as a hypothesis or observation about specific models rather than a general claim.

4. **Sensitivity analysis on budget parameters.** Vary B_base and λ_pat at a few levels (e.g., λ_pat ∈ {1,3,5}) for a subset of models to check whether the reported rankings are stable.

## Score and Decision

After calibration against the human review corpus:

**Round 1 (bracketing):** Three queries on "text-to-SQL benchmark dataset interactive multi-turn" retrieved anchors in the weak band (avg 1.67–3.0, all withdrawn/reject), middle band (avg 3.75–5.0, mix of withdraws and rejects), and strong band (avg 8.0–9.0, accepts). Spider 2.0 (8.0, oral) is the closest top-tier comparator. The paper is clearly above the weak band and below Spider 2.0. Initial bracket: 4.5–7.5.

**Round 2 (narrowing):** Two queries for interactive benchmarks retrieved SOTOPIA (avg 6.67, accept spotlight), GameArena (avg 6.5, accept poster), WildBench (avg 7.33, accept spotlight), Learning to Clarify (avg 6.25, accept poster), IVCR-200K (avg 4.67, withdrawn), LAM Simulator (avg 6.0, reject), PlatoLM (avg 6.5, withdrawn), Talking Turns (avg 5.8, accept poster).

**Anchor comparisons:**
- *Spider 2.0 (8.0)*: More polished benchmark with cleaner methodology and no leakage concerns. BIRD-INTERACT has a more novel interactive component but weaker empirical validation. Clearly below.
- *SOTOPIA (6.67)*: Similar contribution type (interactive benchmark + simulator). SOTOPIA had cleaner evaluation design. BIRD-INTERACT has larger scale and CRUD coverage but the leakage gap pulls it slightly below.
- *GameArena (6.5)*: Comparable quality — both have small methodological concerns (GameArena: small samples; BIRD-INTERACT: single runs, no CI) and some overclaiming. Roughly on par.
- *IVCR-200K (4.67)*: Much weaker data construction methodology. BIRD-INTERACT is clearly above.
- *DB-GPT-Hub (3.75)*: Lacked novelty as a benchmark. BIRD-INTERACT is substantially stronger.

The paper makes genuine contributions but has a meaningful gap in analyzing simulator leakage and overclaims the ITS Law. Combining the strength of the task suite and the simulator validation against the leakage concern and statistical weakness, the paper sits at the lower end of the solid-acceptable range.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>