Now I have sufficient calibration. Let me write the consolidated review.

## Summary

BIRD-INTERACT introduces a benchmark for evaluating interactive text-to-SQL systems through dynamic multi-turn interactions, addressing the gap left by existing benchmarks that rely on static conversation transcripts or SELECT-only operations. The benchmark comprises 600 tasks (300 in a LITE set) spanning full CRUD operations with ambiguous priority sub-tasks and state-dependent follow-ups. Key contributions include: (1) a two-stage function-driven user simulator that prevents ground-truth leakage, (2) dual evaluation settings (c-Interact for protocol-guided conversations, a-Interact for agentic planning), and (3) extensive analysis including memory grafting, interaction test-time scaling, and human-alignment validation. Experiments across 7 frontier LLMs show that even the best models achieve <20% end-to-end success, demonstrating substantial room for improvement in interactive database reasoning.

## Strengths

- **Function-driven user simulator with empirically-demonstrated reliability gains.** The two-stage design (semantic parsing into AMB/LOC/UNA actions → constrained response generation) is a principled solution to a known problem. Figure 6 shows that this approach reduces UNA (unanswerable) failure rates from 67.4% (baseline LLM simulator) to 2.7%, while maintaining high accuracy on AMB and LOC queries. This is a concrete, measurable improvement over the standard LLM-as-simulator approach used in prior work (e.g., MINT).

- **Dual evaluation settings reveal complementary interaction capabilities.** Table 2 shows that GPT-5 is the *worst* model in c-Interact (14.50% SR) but the *best* in a-Interact (29.17% SR), while other models show different relative rankings. This demonstrates that the benchmark captures distinct skill dimensions (structured conversation vs. autonomous planning) that a single setting would miss, and that these differences are not reducible to SQL generation ability alone.

- **Memory grafting experiment provides causal evidence for the communication bottleneck.** Figure 5 shows that grafting O3-Mini's interaction history onto GPT-5 raises its success rate from 13.8% to 20.5% — surpassing O3-Mini itself (18.5%). This controlled experiment isolates communication skill from SQL generation skill, going beyond mere benchmarking to produce a genuine insight about *why* models fail.

- **Full CRUD coverage with state-dependent follow-ups.** The benchmark covers Create, Read, Update, and Delete operations (410 BI + 190 DM tasks), and explicitly introduces state dependency where follow-up sub-tasks require reasoning over modified database states. This contrasts with prior multi-turn benchmarks (CoSQL, SParC) that model only read-only interactions without state changes.

- **Human-alignment validation provides quantitative evidence for simulator realism.** Table 3 reports Pearson correlations with human behavior: 0.84 (p=0.02) for the function-driven GPT-4o simulator vs. 0.61 (p=0.14, not significant) for the baseline. The baseline correlations are *not* statistically significant, making the improvement meaningful — not merely incremental over an already-adequate baseline.

## Weaknesses

### Fatal

None.

### Major

None.

### Minor

- **The relationship between tasks and distinct test cases is not explained.** Table 1 reports 135 distinct test cases for 300 LITE tasks and 191 for 600 FULL tasks — roughly 2.2–3.1 tasks per test case. The paper does not clarify whether this overlap is a design choice (e.g., multiple queries testing the same SQL expectation) or an artifact, nor does it discuss how overlapping test cases affect claims about task diversity. Since the benchmark's difficulty argument rests partly on diversity of query patterns, this warrants a clear explanation. (The paper reports the statistic but does not discuss it.)

- **The "ITS Law" is defined but not empirically verified.** The paper defines the ITS Law as a model satisfying that its performance can "match or even surpass" the idealized single-turn baseline given enough turns (Section 5.2). However, Figure 4 shows that at the tested patience levels (max 7), most models' performance remains well below the idealized line. No model is explicitly shown to satisfy the condition, and the specific patience threshold at which the condition might hold is not identified. The claim that the "law" is observed is thus not well-supported by the presented data.

- **The memory grafting experiment's setting is underspecified.** The experiment (Figure 5) appears to be run on the LITE set in c-Interact mode, but the paper does not explicitly state the exact setting, sample size, or whether multiple trials were conducted. Given that memory grafting is one of the paper's most insightful analyses, these details matter for reproducibility.

- **The a-Interact budget multiplier (×2) lacks explicit justification.** The a-Interact budget is set to *B_base + 2m_amb + 2λ_pat* (Section 4.2), while c-Interact uses *m_amb + λ_pat*. The paper states this is for "consistency" but does not explain why a multiplier of 2 (rather than, say, 1.5 or 3) was chosen, or whether it was empirically calibrated to make budgets approximately equal in effective tightness across the two settings.

- **Human-correlation sample size is not precisely specified.** The paper reports using 100 tasks and 7 models (Section 6) but does not state whether the Pearson correlation is computed across tasks (n=100) or across models (n=7). The significant p-values (0.02, 0.03) strongly imply n=100 (which is adequate), but stating the units of analysis explicitly would improve clarity. This is a presentation issue, not a methodological flaw.

### Trivial

- Figure 3 is information-dense and hard to parse in print; the action cost values are deferred to the appendix.
- Table 2's caption states "Follow Ups (Success Rate %)" which equals overall SR in this setup (since follow-ups are only attempted after priority success), but this relationship is not made explicit in the caption.

## Nice-to-Haves

- **A failure-mode taxonomy** (errors due to insufficient clarification vs. incorrect SQL logic vs. state-propagation failures vs. budget exhaustion) would increase the benchmark's utility for guiding future work. The paper currently reports only aggregate success rates.
- **Multiple-trial variance reporting** for key experiments (even 2–3 runs) would strengthen confidence, especially given the stochastic nature of LLM outputs. The single-run limitation is acknowledged as a cost constraint, which is reasonable for a 600-task × 7-model sweep.
- **A "free-mode" a-Interact setting** (no budget constraint) is planned as future work but would complement the stress-mode results nicely if included now.
- Reporting the number of distinct database schemas used across tasks would help assess domain coverage.

## Removed Points

These points are flagged to be removed; treat them with caution:

- *"Insufficiently validated user simulator alignment — the baseline already achieves moderate positive correlation"* — The baseline correlations (0.61, 0.54) are *not statistically significant* (p=0.14, p=0.21), while the proposed simulator's correlations (0.84, 0.79) are significant (p=0.02, p=0.03). The improvement is from non-significant to significant, not from moderate to strong on an already-adequate baseline. The critic's framing misrepresents the evidence.

- *"The human-correlation sample size would be 7 (far too small) if computed per-model"* — This is speculation unsupported by the paper. The significant p-values (0.02 with 100 tasks) make n=7 extremely unlikely. The paper's description ("computing correlations between success rates achieved by human users versus our simulators across the same tasks") most naturally reads as per-task correlation (n=100). This is a clarity issue, not a validity issue.

- *"Why exactly two sub-tasks (n=2)"* — A reasonable design choice consistent with the paper's stated goal of having a priority + follow-up structure. Not every hyperparameter choice needs a multi-paragraph justification.

- *"The ITS claim that performance can match or surpass idealized performance is not convincingly established"* — Kept as a minor weakness above (the law is defined but unverified). The critic's stronger framing ("not convincingly established") is accurate.

- *"Single runs only" / reproducibility concerns about hyperparameters* — Standard practice for benchmarks of this scale, explicitly acknowledged in the paper. Not a real weakness.

- *"Missing appendix content or proofs"* — The parser strips these; they exist in the original submission.

- *"Number and diversity of databases not reported"* — A nice-to-have but not a core weakness given the already-reported task counts and BI/DM breakdown.

## Novel Insights

The conjunction of the memory grafting result (communication skill can be cleanly separated from SQL skill and transferred across models) and the dual-setting evaluation (models show almost opposite rankings in c-Interact vs. a-Interact) jointly suggests that interactive text-to-SQL capability is not a single axis — it decomposes into at least two distinct skill dimensions that current LLMs master very unevenly. Existing single-turn benchmarks fundamentally cannot detect this. This observation, which emerges from the paper's experimental design rather than being asserted upfront, points toward a more nuanced research agenda for the field than "improve accuracy on one more benchmark point."

## Suggestions

1. **Clarify the task-to-test-case relationship.** Add a brief explanation of why test cases are fewer than tasks (e.g., do shared database schemas or identical sub-task SQL expectations cause the overlap?). Even a sentence acknowledging the overlap and explaining its implications would suffice.

2. **Either verify the ITS Law or rephrase the claim.** Identify the specific patience threshold at which any tested model crosses the idealized performance line, or rephrase the "law" as a hypothesis for future work rather than an observed phenomenon.

3. **Explicitly state the units of analysis for the human correlation** (per-task, n=100) in Table 3's caption.

4. **Specify the exact setting (LITE/FULL, c/a-Interact) and sample size** for the memory grafting experiment in the main text or figure caption.

5. **Briefly justify the ×2 multiplier** in the a-Interact budget formula (e.g., "to account for action costs being roughly twice the cost of clarification turns").

## Score and Decision

**Calibration anchors (all from the ICLR review corpus):**

| Path | Avg Score | Comparison |
|------|-----------|------------|
| `/home/wg25r/split_review/datasets/deepreview_13k_calibration/XmProj9cPs.md` (Spider 2.0) | 8.00 | Stronger benchmark with real-world enterprise workflows and unanimous praise; BIRD-INTERACT has comparable construction quality but a narrower scope and more scrutiny on the simulator |
| `/home/wg25r/split_review/datasets/deepreview_13k_calibration/roNSXZpUDN.md` (τ-bench) | 6.50 | Most structurally similar — both benchmarks with user simulators for interactive agents. BIRD-INTERACT has more thorough simulator validation (USERSIM-GUARD, human correlation) and larger scale |
| `/home/wg25r/split_review/datasets/deepreview_13k_calibration/CvGqMD5OtX.md` (CHASE-SQL) | 6.25 | Method paper (not benchmark). BIRD-INTERACT's benchmark contribution is comparatively stronger in originality |
| `/home/wg25r/split_review/datasets/deepreview_13k_calibration/NmILZXKcOi.md` (DB-GPT-Hub) | 3.75 | Much weaker — seen as lacking novelty. BIRD-INTERACT has clearly greater originality, evaluation depth, and community value |
| `/home/wg25r/split_review/datasets/deepreview_13k_calibration/Avg6hmtgHE.md` (multi-entity QA paper) | 3.40 | Much weaker contribution with insufficient validation. BIRD-INTERACT is substantially stronger on all axes |

BIRD-INTERACT is situated between τ-bench (6.50) and Spider 2.0 (8.00). It shares τ-bench's limitation of depending on an LLM-based simulator, but addresses it more thoroughly with the function-driven design and two validation experiments. The benchmark construction is careful, the analysis insightful, and the empirical results stark. The weaknesses are minor and addressable.

**Score: 7.0** — A solid, well-motivated benchmark contribution that fills a genuine gap in interactive text-to-SQL evaluation. The function-driven simulator and dual evaluation settings are genuine innovations. The main weaknesses (test-case overlap, unverified ITS Law claim, underspecified experimental details) are all addressable in revision.

**Decision: Accept**

MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>