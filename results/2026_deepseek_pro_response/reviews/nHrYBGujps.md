Now I have strong comparative anchors. Let me summarize my calibration:

**Round 1 bracket: 6.0 - 7.5**

| Anchor | Score | Comparison |
|--------|-------|------------|
| Spider 2.0 | 8.00 | Cleaner, no notable weaknesses. BIRD-INTERACT is below this |
| DialSim | 5.00 | Data contamination concerns, weaker methodology. BIRD-INTERACT well above |
| DB-GPT-Hub | 3.75 | Limited novelty, integration work. BIRD-INTERACT well above |

**Round 2 narrowing:**

| Anchor | Score | Comparison |
|--------|-------|------------|
| MINT | 6.75 | Multi-turn interaction benchmark, GPT-4 simulated feedback. Similar in spirit. BIRD-INTERACT has stronger simulator methodology, purpose-built tasks, human alignment validation. Comparable to slightly better |
| ToolDial | 6.67 | Multi-turn dialogue dataset for tool-augmented LMs. BIRD-INTERACT has stronger methodology (real execution, principled construction) |
| WildBench | 7.33 | Real user queries benchmark, different domain |

BIRD-INTERACT has more novel contributions than MINT (function-driven simulator with USERSIM-GUARD validation, dual evaluation settings revealing model-mode interactions, ambiguity taxonomy, state-dependency) but also has more open presentation issues (ITS Law naming, memory grafting confound, single-run limitation, missing failure taxonomy). Overall, BIRD-INTERACT is comparable to slightly better than MINT (6.75) and well above ToolDial (6.67), but notably below Spider 2.0 (8.00).

**Final score: 7.0**

Now let me finalize the review with all the required elements.Now I have all the calibration data I need. Let me finalize the review.

---

## Summary
BIRD-INTERACT introduces a benchmark for interactive text-to-SQL evaluation featuring 900 tasks across two settings (conversational c-Interact and agentic a-Interact), a function-driven user simulator that constrains responses to prevent ground-truth leakage, and executable test cases spanning the full CRUD spectrum. The benchmark converts single-turn LIVESQLBENCH tasks into multi-turn interactive scenarios through principled ambiguity injection and state-dependent follow-up sub-tasks. Results across 7 frontier LLMs show that even the strongest models struggle (GPT-5 achieves only 8.67% end-to-end SR in c-Interact and 17% in a-Interact on the full set), and model rankings flip across settings, revealing that interaction mode is a decisive factor in performance.

## Strengths
- **Function-driven user simulator is a genuine methodological advance:** The two-stage design (LLM semantic parser → constrained symbolic action → controlled response) reduces inappropriate answer rates from 67.4% (baseline) to 2.7% on USERSIM-GUARD (Section 6, Figure 6). This directly addresses a known failure mode of LLM-based simulators leaking ground truth or hallucinating responses, and the human alignment study (Table 3, r=0.84, p=0.02) provides credible evidence that the simulator's behavior correlates with real human users.
- **Dual evaluation settings reveal non-trivial model×mode interactions:** GPT-5 flips from worst in c-Interact (14.50% priority SR) to best in a-Interact (29.17% SR), while Claude-Sonnet-4 improves from 22.33% to 27.83% (Table 2). These rank instabilities validate that the two settings measure genuinely distinct capabilities and that a single evaluation protocol would miss model-specific interaction strengths.
- **Principled ambiguity taxonomy with concrete operationalization:** The three-category taxonomy (superficial query ambiguities, knowledge ambiguities with chain breaking, environmental ambiguities) is operationalized through specific mechanisms — e.g., masking intermediate DAG nodes in the knowledge base to break inferential chains (Figure 2). The knowledge chain breaking design forces models to recognize missing dependencies rather than applying a single clarification strategy.
- **State-dependency between sub-tasks is a genuinely novel feature:** Follow-up sub-tasks depend on modified database states or newly created objects from preceding queries. This is a non-trivial departure from prior multi-turn benchmarks (SParC, CoSQL) that present independent turns.
- **Substantial benchmark scale with execution-grounded evaluation:** 900 total tasks, 191 distinct test cases, up to 11,796 dynamic interactions across the FULL set (Table 1). The execution-based evaluation (test cases rather than exact string match) provides functional correctness guarantees.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor
- **Single-run evaluation limits result reliability:** The paper explicitly states "conducting single runs due to cost" (Section 5). While temperature=0 mitigates most non-determinism, some API providers exhibit residual non-determinism even at temperature=0, and close comparisons (e.g., Claude-Sonnet-3.7 at 18.00% vs. Deepseek-Chat-V3.1 at 18.50% in c-Interact overall SR) cannot be confidently interpreted as genuine differences. The paper acknowledges this limitation and the cost argument has merit, but for a benchmark whose primary value is providing reliable performance comparisons, this is a notable gap. Multi-run evaluation on at least the LITE set would substantially strengthen the contribution.
- **"ITS Law" naming is an overclaim:** The paper defines "ITS Law" as "A model satisfies this law if, given enough interactive turns, its performance can match or even surpass that of the idealized single-turn task" (Section 5.2). The data in Figure 4 shows Claude-3.7-Sonnet clearly exhibiting this pattern in c-Interact, but the other three models show weaker or flat scaling, and the pattern largely disappears in a-Interact. The paper does not claim all models satisfy the law — it defines a criterion and shows one model meeting it — but the capitalized "Law" framing overstates the generality of the finding. Re-framing as an empirical observation would be more appropriate.
- **Memory grafting experiment has a partial confound:** Section 5.2 grafts ambiguity-resolution histories from stronger models into GPT-5 before SQL generation, showing SR improvement from 13.8% to 18.8–20.5%. This demonstrates that GPT-5 can generate correct SQL given good clarifications, supporting the hypothesis that communication is the bottleneck. However, the experiment cannot fully disentangle whether GPT-5's original failure was due to asking poor questions (and receiving unhelpful responses) versus receiving adequate clarifications but then generating wrong SQL. The paper's conclusions ("a more effective communication schema is required") are appropriately measured, but the causal interpretation should be tempered slightly.
- **No systematic failure taxonomy:** For a benchmark aiming to guide future research, the paper lacks a breakdown of why models fail. The action distribution analysis (60.87% submit+ask actions) and BI vs. DM comparison are starts, but there is no categorization into failure modes such as clarification failures, SQL generation errors, state-dependency issues, budget exhaustion, or debugging failures. This limits the benchmark's diagnostic value for researchers deciding where to focus improvement efforts.
- **Patience scaling only on LITE with 4 models:** Figure 4 shows ITS results on LITE (not FULL) with only 4 of the 7 benchmarked models. The paper never demonstrates whether the model rankings in Table 2 are stable across patience levels — a concern given that Table 2 uses λ_pat=3 as default.
- **LITE simplification and inter-annotator agreement are underspecified:** The paper states LITE has "simplified databases" without defining what simplification entails (fewer tables? cleaner data? shorter schemas?). Table 1 reports inter-annotator agreement of 93.33%/93.50% without specifying what metric this is measured on (ambiguity classification? SQL correctness? task validity?).

### Trivial
- The c-Interact and a-Interact settings use fundamentally different budget formulations (turn-based vs. cost-based with action-specific costs), making Table 2's side-by-side placement potentially misleading for readers who might attempt direct cross-mode comparison. The paper correctly treats them as complementary, but the visual layout invites misinterpretation.
- The abstract's claim that "each task features ambiguous and follow-up sub-tasks" could more precisely say "each task features an ambiguous initial priority sub-task and a follow-up sub-task," since the ambiguity is injected into the first sub-task, not distributed across both.

## Nice-to-Haves
- Running models at least 3 times on the LITE set with different seeds and reporting mean ± std would substantially strengthen the benchmark's reliability claims.
- A failure taxonomy categorizing a sample of failed trajectories (clarification failure, SQL generation failure, state-dependency failure, budget exhaustion, debugging failure) would dramatically increase the benchmark's diagnostic utility.
- Experiments in a "free-mode" (no budget constraints) for a-Interact, which the paper mentions as future work, would help distinguish whether poor a-Interact performance stems from budget pressure or fundamental strategy limitations.

## Removed Points
These points are flagged to be removed, treat them with caution.

- **Harsh Critic: "simulator fundamentally operates with access to ground-truth SQL, clarifications are always precisely correct" as a weakness.** The function-driven design constraining what the simulator can reveal is a feature, not a bug — it prevents leakage while ensuring correctness. The paper acknowledges this design choice and validates against humans (Table 3). REMOVED because this is an explicit, intentional design decision, not a hidden flaw.

- **Harsh Critic: "missing discussion of conversational recommendation or dialogue state tracking benchmarks."** REMOVED per instructions — I cannot verify the existence or relevance of unspecified related work.

- **Harsh Critic: human alignment study "SR values being quite low, which could inflate correlation artificially."** Speculative and not grounded in the paper. Many models having low SR on hard tasks would typically deflate, not inflate, correlation coefficients. REMOVED as speculative.

- **Harsh Critic: "the idealized performance baseline... is a fundamentally different, easier task, not a performance ceiling."** The paper explicitly calls this "idealized" and acknowledges it represents a scenario where "all necessary context is provided" — it is explicitly framed as an upper-bound reference, not an apples-to-apples comparison. REMOVED because the paper already addresses this framing.

- **Strength Finder: memory grafting is a "clean causal manipulation."** The harsh critic identifies a genuine confound (included above as a minor weakness). REMOVED as overstated.

- **Strength Finder: ITS shows "a reproducible empirical pattern."** Only one model (Claude-3.7-Sonnet) clearly exhibits the pattern in one setting. REMOVED as overstated; the actual finding is more nuanced.

- **Harsh Critic: demand for train/val/test splits.** The benchmark is designed for zero-shot evaluation of LLMs, not for training. The absence of splits is consistent with how LLM benchmarks (BIRD, Spider) are structured. REMOVED.

- **Harsh Critic: concern about "test case reuse (135 distinct test cases for 300 tasks)."** Without evidence that this causes false positives, this is speculative. REMOVED as speculative.

- **Harsh Critic: notes about stripped appendices (C, E, F, H, J, N, O, P, R).** REMOVED per instructions — these are parser artifacts, not author errors.

- **Strength Finder: "addressed an important problem" / "targeted an interesting question."** REMOVED as generic/superficial.

## Novel Insights
The most genuinely novel insight from this work is the demonstration that interaction mode acts as a decisive factor orthogonal to raw SQL generation capability: GPT-5, a state-of-the-art model, ranks worst in protocol-guided interaction (c-Interact) but best in open-ended agentic interaction (a-Interact). This pattern, combined with the memory grafting result showing GPT-5 can generate correct SQL given others' clarifications, suggests that current LLM evaluation in text-to-SQL systematically conflates communication strategy with generation capability — and that these are separable dimensions requiring distinct evaluation protocols. The function-driven simulator design, which dramatically reduces inappropriate responses (67.4% → 2.7%), also provides a template for how future interactive benchmarks can achieve controllability without sacrificing response diversity.

## Suggestions
- Re-frame the "ITS Law" as an empirical observation (e.g., "interaction scaling behavior") rather than a named law, and explicitly note which models exhibit it and in which settings.
- Define what "simplified databases" means for the LITE set and specify the inter-annotator agreement metric.
- Temper the memory grafting conclusions slightly: acknowledge that the experiment demonstrates GPT-5 can leverage good clarifications for SQL generation, but does not isolate whether GPT-5's own communication could have obtained equivalent clarifications.

## Score and Decision

### Calibration Anchors Used

| Round | Paper | Path | Score | Comparison |
|-------|-------|------|-------|------------|
| 1 | Spider 2.0 | XmProj9cPs.md | 8.00 | Cleaner benchmark, no notable weaknesses. BIRD-INTERACT is below this |
| 1 | DialSim | W1x77vRucB.md | 5.00 | Data contamination concerns, weaker methodology. BIRD-INTERACT well above |
| 1 | DB-GPT-Hub | NmILZXKcOi.md | 3.75 | Limited novelty, integration work. BIRD-INTERACT well above |
| 2 | MINT | jp3gWrMuIZ.md | 6.75 | Multi-turn interaction benchmark with simulated feedback. Most comparable anchor. BIRD-INTERACT has stronger simulator methodology and purpose-built tasks, comparable overall |
| 2 | ToolDial | J1J5eGJsKZ.md | 6.67 | Multi-turn TALM dataset. BIRD-INTERACT has stronger methodology (real execution, principled construction) |
| 2 | WildBench | MKEHCx25xp.md | 7.33 | Real user queries benchmark, different domain |

**Round 1 bracket:** 6.0 – 7.5  
**Round 2 narrowed to:** 6.5 – 7.0  

BIRD-INTERACT is comparable to MINT (6.75) — both are solid interactive benchmarks with real contributions and some minor issues. BIRD-INTERACT has stronger methodological contributions (function-driven simulator with 67.4→2.7% failure reduction, dual settings, ambiguity taxonomy, state-dependency) but also more open presentation issues (ITS naming, missing failure taxonomy, underspecified details). Overall, the paper lands at the upper end of this narrow range due to the scale and novelty of its contributions.

MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>