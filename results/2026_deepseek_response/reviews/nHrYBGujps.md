## Summary

BIRD-INTERACT is a benchmark for evaluating text-to-SQL systems in dynamic, multi-turn interactions. It converts single-turn tasks from LIVESQLBENCH into interactive scenarios through controlled ambiguity injection and state-dependent follow-up sub-tasks. The benchmark features a function-driven user simulator (validated via USERSIM-GUARD and human alignment), two evaluation settings (c-Interact conversational and a-Interact agentic), and 900 tasks spanning the full CRUD spectrum. Experiments on 7 frontier LLMs show very low success rates (best model < 17% end-to-end), and the memory grafting experiment isolates communication strategy as a key bottleneck.

## Strengths

1. **Function-driven user simulator with strong multi-faceted validation**: The two-stage strategy (Section 3.3) maps system clarification requests to one of three symbolic actions (AMB, LOC, UNA) before generating responses, addressing the known problem of ground-truth leakage in LLM-based simulators. USERSIM-GUARD evaluation (Figure 6) shows the function-driven approach reduces failure rate on Unanswerable questions from 67.4% to as low as 2.7%. The human alignment study (Table 3) achieves 0.84 Pearson correlation (p=0.02) with human expert judgments vs. 0.61 (p=0.14) for the baseline — this validation is more rigorous than most benchmark papers provide for their simulators.

2. **State-dependent follow-up sub-tasks as a structural contribution**: The benchmark introduces state dependency between sub-tasks (Section 3.2), where the system must reason over modified database states from preceding queries. Table 2 confirms follow-up SR is substantially lower than priority SR across all models (e.g., O3-Mini drops from 24.00% to 15.83% in c-Interact), validating that this design captures a meaningful additional challenge beyond prior multi-turn benchmarks like COSQL and SParC where turns are independent.

3. **Two evaluation settings reveal interaction-mode-specific findings**: The paper provides both a conversational protocol (c-Interact) and an open-ended agentic setting (a-Interact) (Section 4), each with adaptive budget constraints. This produces non-obvious findings — GPT-5 is worst in c-Interact (14.50% SR) but best in a-Interact (29.17% SR) — that single-setting benchmarks cannot surface, demonstrating that interaction mode is itself a decisive factor.

4. **Memory grafting experiment provides causal evidence for the core thesis**: Section 5.2 shows GPT-5's SR improves from 13.8% to 20.5% when given O3-Mini's interaction history (Figure 5), isolating the contribution of interaction strategy from SQL generation quality. This directly supports the paper's central claim that communication effectiveness, not just SQL generation ability, is the bottleneck.

5. **CRUD coverage reveals differential difficulty**: The benchmark includes both BI (analytical) and DM (operational) tasks covering Create, Read, Update, Delete (Table 1: 410 BI vs. 190 DM in FULL). DM tasks show consistently higher SR than BI tasks across all models (Table 2), a specific, measurable difference that single-turn benchmarks cannot surface and that points to where LLMs need improvement.

6. **Rigor in benchmark construction**: 12 expert annotators, multi-stage selection, 93.5% inter-annotator agreement (Table 1), and explicit quality control ensuring ambiguous queries are unsolvable without clarification yet reconstructable once clarified. This establishes a solid foundation for the benchmark's reliability.

## Weaknesses

### Fatal
None.

### Major

1. **Synthetic ambiguity injection raises ecological validity questions**: The benchmark converts clear single-turn tasks by *deliberately injecting* ambiguities — removing knowledge entries, masking intermediate nodes in knowledge chains, and introducing vague language (Section 3.2). While this enables controlled evaluation, the paper does not defend why these synthetic ambiguities generalize to naturally-occurring user underspecification. The paper acknowledges that LIVESQLBENCH databases already contain natural noise (e.g., NULL fields), but the bulk of the ambiguity burden comes from curated injections. Without external validation (e.g., a small human study comparing injected vs. natural ambiguities, or analysis showing that the injected types cover patterns observed in real user queries), the benchmark risks measuring performance on a specific, curated puzzle rather than on the open-ended challenges of real-world interactive text-to-SQL. This limitation affects the interpretation of all experimental results.

2. **Follow-up sub-task failure modes are unexplored**: Most models achieve under 10% SR on follow-ups in c-Interact; several are below 5% in a-Interact (Table 2, e.g., Qwen-3-Coder at 4.17%). Yet the paper does not decompose *why*. Possible causes include budget exhaustion before reaching the follow-up, context-length saturation from the first sub-task, state-transition reasoning failures, or poorly calibrated follow-up difficulty. The analysis in Section 5.2 focuses on the priority sub-task (memory grafting, ITS), leaving the follow-up bottleneck opaque. Since the two-sub-task structure is a claimed innovation, understanding why models fail on sub-task 2 is essential for the benchmark's diagnostic utility.

### Minor

1. **"ITS Law" overstates the evidence**: Section 5.2 defines "ITS Law" as a model matching or surpassing idealized single-turn performance given enough interaction turns. However, Figure 4 shows only Claude-3.7-Sonnet exhibits clear monotonic scaling toward the idealized baseline; O3-Mini is flat, GPT-4o is flat, and Qwen-3 declines. Calling this a "law" based on one model's behavior overstates the observation. The term should be scaled back to "ITS scaling pattern in some models."

2. **Budget asymmetry between evaluation settings is underexplored**: c-Interact budget is τ_clar = m_amb + λ_pat, while a-Interact budget is B = B_base + 2m_amb + 2λ_pat (roughly 2× more generous). The paper notes this difference but does not discuss how it confounds the comparison between settings. Since most models perform better in a-Interact, it is unclear how much is due to mode affordances vs. simply having more budget.

3. **Action distribution analysis lacks conditional breakdowns**: Section 5.2 reports aggregate action percentages in a-Interact across all models (e.g., "submit" and "ask" comprise 60.87% of actions) but does not break down by task type (BI vs. DM) or by success/failure outcomes. Such breakdowns would make the analysis more diagnostically useful — e.g., do successful trajectories use more knowledge retrieval?

### Trivial

1. The follow-up sub-task 5-category taxonomy (Section 3.2) is cited to Appendix H.5 but never summarized in the main text. A one-sentence listing of the categories would help readers assess scope without consulting the appendix.

2. Deepseek-Chat-V3.1 in c-Interact shows 15.15 normalized reward but only 8.50 SR on follow-ups (Table 2) — a divergence that is not interpreted, though the reward structure (70% priority, 30% follow-up) partly explains it.

## Nice-to-Haves

- Perform the converse memory grafting experiment: give GPT-5's interaction history to a weaker model and see whether SQL generation (rather than communication) becomes the bottleneck.
- Conduct a qualitative coding of GPT-5's interaction traces in c-Interact to understand *why* its communication fails (does it ask irrelevant questions, not ask enough, or ask the wrong type?).
- Show budget hyperparameter sensitivity on FULL for at least λ=0 and λ=5 for one or two models (currently only on LITE).
- Report number of API calls or tokens consumed alongside USD costs for better future reproducibility.
- Add a dedicated "What is the benchmark measuring?" section correlating SR with independent measures of interaction quality.

## Removed Points

These points were identified by reviewers or the strength finder but were removed or downgraded after verification:

- **"Weakness about follow-up taxonomy being in appendix"**: The harsh critic notes the 5-category taxonomy is only in appendix. This is true — but the paper states where to find it, and the parser strips appendices from all papers. Kept as a trivial point (one sentence missing in main text), not removed.

- **"Weakness about static conversation histories cited as a problem with prior work"**: The strength finder's claimed strengths about the problem being important were retained because they're grounded in specific claims the paper makes and supports.

- **"Weakness about the paper not comparing to enough baselines"**: No reviewer raised this; the paper evaluates 7 frontier models.

- **"Weakness about the paper not releasing code/data"**: The paper cites LIVESQLBENCH (BIRD-Team, 2025) as the open-source foundation. No reviewer claimed unreleased artifacts. This doesn't apply.

- **Harsh critic's "computational costs" suggestion**: Moved to Nice-to-Haves — a reasonable request but not a weakness in the current form.

- **Harsh critic's suggestion about converse memory grafting experiment**: Moved to Nice-to-Haves — an extension, not a flaw.

- **"Missing related works"**: Removed per hard rules — I cannot verify the existence of missing citations.

## Novel Insights

Beyond the paper's own contributions, the most interesting emergent finding is the sharp interaction-mode divergence: GPT-5 flips from worst in c-Interact (14.50%) to best in a-Interact (29.17%), while Claude-Sonnet-4 shows the opposite pattern (22.33% in c-Interact vs. 27.83% in a-Interact but the gap is smaller). The memory grafting experiment sharpens this: since GPT-5 can generate correct SQL when given good interaction traces from other models, its c-Interact failure is specifically about communication strategy, not SQL skill. This finding complicates the simple narrative that bigger/better models simply do everything better — communication style and mode-fit may be orthogonal to raw generation ability. This suggests that the text-to-SQL community may need model-specific interaction scaffolds rather than a one-size-fits-all protocol.

## Suggestions

1. Add a failure-mode decomposition for follow-up sub-tasks, categorizing failures into budget exhaustion, context saturation, and state-transition reasoning failures. This is the single most impactful addition you could make.
2. Explicitly discuss the ecological validity limitation of synthetic ambiguity injection. A brief human study comparing injected vs. naturally-occurring ambiguity patterns, or at minimum a clear acknowledgment and defense of the design choice, would strengthen the paper.
3. Temper the "ITS Law" claim to "ITS scaling patterns observed in some models" — only Claude-3.7-Sonnet clearly exhibits the claimed behavior.
4. Discuss the budget asymmetry between c-Interact and a-Interact as a confounding factor in mode comparisons, not just as a design choice.

## Score and Decision

**Bracketing (Round 1):** Low anchors (<3.5) include DB-GPT-Hub (3.75 avg, Reject) and TrustSQL (4.00 avg, Reject) — clearly weaker. Middle anchors (3.5–7.5) include CHASE-SQL (6.25), ROUTE (6.25), τ-bench (6.50), MINT (6.75). High anchors (>7.5) include Spider 2.0 (8.00) — a stronger benchmark contribution with real-world enterprise data. **Bracket: 5.5–7.5.**

**Narrowing (Round 2):** Compared to τ-bench (6.50, Accept) — a user-simulation benchmark with similar validation concerns — BIRD-INTERACT has stronger user-simulator validation (USERSIM-GUARD + human alignment with 0.84 Pearson) but a weaker connection to naturally-occurring user behavior. Compared to MINT (6.75, Accept) — a multi-turn interaction benchmark — BIRD-INTERACT has more domain-specific depth and a more rigorous benchmark construction process, though MINT's scope is broader. Compared to HoloBench (6.25, Accept) — another database-oriented benchmark — BIRD-INTERACT has substantially stronger construction and validation pipeline. The paper is most comparable to τ-bench at 6.50 in terms of scope, rigor, and significance, though the synthetic ambiguity issue is slightly more central to this paper's validity.

**Calibration anchors consulted:**
- `/home/wg25r/split_review_opus_repro/datasets/deepreview_13k_calibration/XmProj9cPs.md` — Spider 2.0, avg 8.00 (Round 1) — Stronger: real enterprise data, but different task scope; BIRD-INTERACT's user simulator validation is more thorough.
- `/home/wg25r/split_review_opus_repro/datasets/deepreview_13k_calibration/roNSXZpUDN.md` — τ-bench, avg 6.50 (Round 2) — Comparable: both benchmark interactive agent-user scenarios; BIRD-INTERACT has stronger simulator validation but τ-bench is cleaner in scoping.
- `/home/wg25r/split_review_opus_repro/datasets/deepreview_13k_calibration/jp3gWrMuIZ.md` — MINT, avg 6.75 (Round 2) — Slightly stronger: broader scope, more well-known impact; BIRD-INTERACT has more domain depth.
- `/home/wg25r/split_review_opus_repro/datasets/deepreview_13k_calibration/CvGqMD5OtX.md` — CHASE-SQL, avg 6.25 (Round 1) — Method paper, less directly comparable.
- `/home/wg25r/split_review_opus_repro/datasets/deepreview_13k_calibration/5LXcoDtNyq.md` — HoloBench, avg 6.25 (Round 2) — Weaker benchmark construction; BIRD-INTERACT is stronger.
- `/home/wg25r/split_review_opus_repro/datasets/deepreview_13k_calibration/NmILZXKcOi.md` — DB-GPT-Hub, avg 3.75 (Round 1) — Significantly weaker.
- `/home/wg25r/split_review_opus_repro/datasets/deepreview_13k_calibration/7ZeoPg3eTA.md` — TrustSQL, avg 4.00 (Round 1) — Weaker.

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>