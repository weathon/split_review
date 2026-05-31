Now let me do the calibration search.Initial bracket: **5.5 – 8.0**. Spider 2.0 (a closely similar text-to-SQL benchmark paper) scores 8.00. BIRD-INTERACT has more novel simulator design but some evidential gaps. Let me narrow.Now I have enough material for a calibrated review. Let me compose it.

---

## Summary

BIRD-INTERACT is a benchmark for evaluating text-to-SQL systems in dynamic, multi-turn interactive settings. It extends the static LIVESQLBENCH foundation into a fully interactive evaluation by injecting structured ambiguities into queries, adding follow-up sub-tasks with state dependency, covering the full CRUD spectrum, and providing a novel two-stage function-driven user simulator. Two evaluation modes are offered: a conversational protocol (*c*-Interact) and an open-ended agentic setting (*a*-Interact). Experiments on seven frontier LLMs reveal uniformly low success rates (GPT-5 achieves at most 17%), and targeted analyses (memory grafting, Interaction Test-time Scaling) provide diagnostic insight into where current models fall short.

---

## Strengths

- **Function-driven simulator dramatically reduces ground-truth leakage.** The two-stage semantic-parsing approach (AMB/LOC/UNA) reduces the failure rate on unanswerable UNA questions from up to 67.4% (baseline LLM-only simulators) to as low as 2.7% (Figure 6). This is a concrete, quantified improvement over prior simulator designs and is the paper's strongest technical contribution.

- **USERSIM-GUARD provides objective, scalable quality assessment of user simulators.** The 2,100-question expert-labeled dataset (Section 6) decouples simulator quality evaluation from benchmark evaluation proper, which is methodologically clean and reusable.

- **Dual evaluation modes expose model-specific interaction capabilities in a non-trivial way.** GPT-5 ranks last in *c*-Interact (14.50% SR) but first in *a*-Interact (29.17% SR), a 14.67pp reversal that is verified directly from Table 2. This ranking flip is meaningful evidence that interaction modality — not just SQL generation quality — matters.

- **State-dependent follow-up sub-tasks constitute a genuine novelty over prior multi-turn SQL benchmarks.** Sub-task 2 requires reasoning over database states modified by sub-task 1 (Section 3.2), which prior static benchmarks such as CoSQL do not require. This is a concrete structural advance.

- **CRUD coverage and executable test-case grading improve evaluation validity.** Moving beyond SELECT-only evaluation with functional-equivalence test cases (not SQL-string matching) strengthens correctness measurement, as noted in Section 2 and Table 1.

---

## Weaknesses

### Fatal
None.

### Major

- **No human performance baseline — benchmark difficulty is uncalibrated.** GPT-5 achieves 8.67% in *c*-Interact and 17% in *a*-Interact (Table 2). Without a reference point showing what a skilled human database practitioner achieves within the same budget constraints, it is impossible to determine whether these numbers reflect a meaningfully hard benchmark or one that is over-constrained by the budget formula or ambiguity injection intensity. The paper's claim to "restore missing realism" (Abstract) depends on the benchmark approximating real-world difficulty, but that claim cannot be evaluated without a human anchor. Even a small human pilot study (30–50 tasks) would substantially strengthen the paper's core premise.

- **Alignment study is statistically underpowered.** The primary evidence that the function-driven simulator matches human behavior is a Pearson correlation of *r* = 0.84 (*p* = 0.02) computed across 7 system models (Section 6, Table 3). At *n* = 7, the 95% confidence interval for *r* = 0.84 spans roughly [0.18, 0.98]; the competing baseline correlation of *r* = 0.61 (*p* = 0.14) cannot be statistically distinguished from it at this sample size. The paper asserts "significantly stronger alignment," but this claim is not supported by the statistical evidence as presented. The USERSIM-GUARD results are persuasive; the correlation study is not.

### Minor

- **"ITS Law" framing overstates the evidence.** The paper defines the Interaction Test-time Scaling Law as a general principle (Section 5.2), but Figure 4 shows clear monotonic scaling in *c*-Interact for only Claude-3.7-Sonnet. The figure caption explicitly states that *a*-Interact performance is "relatively flat or slightly decreases" for all models, and the other models in *c*-Interact show noisy or non-monotonic trends. Presenting this as a "Law" rather than an observation or hypothesis attributed to one model is an overclaim that the experimental evidence does not support.

- **Memory grafting conclusion is modestly overstated.** Figure 5 shows GPT-5 without grafting: 13.8%; with O3-Mini grafting: 20.5%; O3-Mini standalone: 18.5%. The 6.7pp gain is real, but inferring from this that "GPT-5 possesses robust SQL generation capabilities but lacks communication" is a strong causal claim. Alternative explanations (e.g., O3-Mini's interaction history contains incidentally better context organization, or the gain reflects the ceiling effect of the ambiguity resolution step) are not ruled out.

- **~10% AMB/LOC misclassification effect on benchmark scores is unanalyzed.** Figure 6 shows AMB and LOC classification accuracy at ~90% for both the proposed and baseline simulators. A model that asks an unusual but valid clarifying question which the parser maps to UNA() is unfairly penalized. The paper does not estimate the magnitude of this effect or discuss whether it systematically disadvantages particular model families (e.g., those that ask more creative disambiguation questions).

### Trivial

- **Budget formula constants are stated without main-text motivation.** Section 4.2 gives *B*_base = 6 with "Further details of action costs are provided in Appendix J," but no intuition for why 6 (or why user questions cost 2× DB exploration actions) appears in the main body. A single sentence motivating the key design choices would improve readability.

---

## Nice-to-Haves

- A trajectory-level analysis of action *sequences* leading to success vs. failure (not just aggregate action frequencies) would substantiate the claim that "strategic interaction is the decisive skill." Showing that successful runs reliably contain early knowledge-retrieval → clarification → submission chains while failures cluster on premature submit → error → retry loops would be compelling.
- The paper could explicitly characterize the domain distribution and schema complexity of the underlying LIVESQLBENCH databases (one or two sentences) to help readers assess generalizability.
- The paper would benefit from discussing the free-mode (unconstrained) evaluation mentioned in Section 8 as future work — even preliminary results would clarify whether the low success rates reflect budget over-constraint or genuine interaction difficulty.

---

## Removed Points

*These points are flagged to be removed; treat them with caution.*

- **Critic: Domain bias inherited from LIVESQLBENCH.** Removed because this is speculative — the paper builds on LIVESQLBENCH and any domain characteristics are inherited transparently; no specific bias claim can be substantiated from the paper as written.
- **Critic: 191 distinct test cases for 600 tasks implies shared test cases reduce discriminativity.** Removed as a standalone weakness: functional-equivalence test cases can legitimately apply across tasks that test the same SQL idiom. There is no demonstrated evidence of reduced discriminativity.
- **Critic: Temperature=0 single runs lack uncertainty estimates.** Moved to trivial/nice-to-have. Single-run temperature=0 is standard practice for large-model benchmarking; the paper acknowledges it ("due to cost"). Not a meaningful weakness for a benchmark paper.
- **Strength Finder: "LITE and FULL variants enable both comprehensive evaluation and rapid development."** Removed as generic; the existence of two subset sizes is a convenience feature, not a scientific contribution.
- **Strength Finder: "SOTA LLMs perform very poorly, leaving ample room for improvement."** Removed — this describes a property of the benchmark's difficulty level, not evidence of a contribution. Whether the difficulty is well-calibrated is precisely the open question raised by the missing human baseline.
- **Critic: CRUD adequacy for DM operations (DELETE with subqueries, etc.).** Removed — purely speculative; no evidence from the paper that DM test cases are inadequate.

---

## Novel Insights

The paper's most genuinely novel observation — supported by the data — is the ranking *reversal* between *c*-Interact and *a*-Interact (GPT-5 worst to best), combined with the memory grafting experiment showing that GPT-5's SQL generation is fine but its interaction *strategy* is the bottleneck. This suggests that interactive capability is a separable dimension from generation capability, and that current benchmarks conflate the two. The function-driven simulator design — using a semantic parser as a first-stage gatekeeper to prevent ground-truth leakage before LLM response generation — is technically novel and addresses a known flaw in LLM-as-user-simulator approaches (the leakage problem), validated convincingly by the USERSIM-GUARD results. Together these two contributions advance both the *measurement* and *understanding* of interactive text-to-SQL capability.

---

## Suggestions

1. Run a human performance pilot on ~50 tasks within the same budget constraints and report it as a calibration anchor in the main results table. Even an approximate range (e.g., 40–55% SR) would transform the interpretation of the LLM results.
2. Strengthen the alignment study by reporting bootstrap confidence intervals or a permutation test for the difference between *r* = 0.84 and *r* = 0.61, or increase the number of evaluated system models (e.g., to 12–15).
3. Soften the ITS Law framing: describe it as an empirical observation holding for Claude-3.7-Sonnet in *c*-Interact, and state as a hypothesis to be confirmed whether other models exhibit it.
4. Add a brief analysis (even a single paragraph) of how often AMB/LOC misclassification occurs in practice and its estimated effect on reported success rates.

---

## Score and Decision

**Calibration anchors:**

| Path | Avg Score | Round | Comparison |
|---|---|---|---|
| `XmProj9cPs.md` (Spider 2.0) | 8.00 | R1 | Most topically similar; both text-to-SQL benchmark papers with complex settings. Spider 2.0 uses real enterprise DBs; BIRD-INTERACT adds interactive multi-turn + principled simulator. Comparable quality; BIRD-INTERACT has more novel technical contributions but larger evidential gaps. |
| `GGlpykXDCa.md` (MMQA) | 8.00 | R1 | Multi-table SQL QA benchmark; less relevant — no interaction or simulator design. |
| `roNSXZpUDN.md` (τ-bench) | 6.50 | R2 | Agent benchmark with LLM user simulator; directly comparable design. BIRD-INTERACT's two-stage function-driven simulator, CRUD coverage, and ambiguity injection are substantially more rigorous than τ-bench. BIRD-INTERACT is clearly above τ-bench. |
| `zAdUB0aCTQ.md` (AgentBench) | 6.20 | R2 | Multi-task agent benchmark; less focused, less technically novel simulator. BIRD-INTERACT is above this. |
| `oKn9c6ytLx.md` (WebArena) | 6.33 | R2 | Web agent benchmark; comparable scope. BIRD-INTERACT's domain-specific simulator design is more rigorous. |
| `MKEHCx25xp.md` (WildBench) | 7.33 | R2 | LLM evaluation benchmark; less interactive, no simulator. BIRD-INTERACT is comparable in polish. |
| `NmILZXKcOi.md` (DB-GPT-Hub) | 3.75 | R2 | Text-to-SQL fine-tuning benchmark; much simpler scope. BIRD-INTERACT is well above this. |
| `CvGqMD5OtX.md` (CHASE-SQL) | 6.25 | R2 | Text-to-SQL generation method, not a benchmark paper. Less relevant. |

**Round 1 bracket:** 5.5 – 8.0  
**Round 2 narrowing:** BIRD-INTERACT is clearly above τ-bench (6.50) and WebArena (6.33) due to more principled simulator design, domain-specific technical depth, and richer ambiguity taxonomy. It is below Spider 2.0 (8.00) due to the missing human baseline (a critical gap for a benchmark paper), the underpowered alignment study, and the ITS Law overclaim. WildBench (7.33) is a useful middle anchor — BIRD-INTERACT is comparably polished but narrower in scope. The two major weaknesses (human baseline gap and underpowered alignment study) are real but bounded; neither invalidates the benchmark itself. The paper's core technical contributions (function-driven simulator, dual evaluation modes, CRUD + state dependency) are solid and well-validated where tested. This places BIRD-INTERACT between WildBench (7.33) and Spider 2.0 (8.00), leaning closer to WildBench given the evidential gaps.

**Axes:**
- *Originality:* High — the two-stage simulator design, budget-constrained dual evaluation, and CRUD + state dependency are novel for text-to-SQL benchmarking.
- *Importance:* High — interactive text-to-SQL is a real gap in existing evaluation infrastructure.
- *Claims supported:* Moderate — the simulator quality claims are well-supported by USERSIM-GUARD; the difficulty calibration and alignment strength claims need additional evidence.
- *Soundness of experiments:* Mostly sound — seven frontier LLMs, temperature=0, dual settings, memory grafting; main gap is human baseline absence and underpowered correlation study.
- *Clarity:* Good — paper is well-structured; main budget design rationale deferred to appendix is a minor gap.
- *Value to community:* High — BIRD-INTERACT fills a genuine gap and will likely be used by the text-to-SQL community.

**Final score: 7.0 (Accept)**

MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>