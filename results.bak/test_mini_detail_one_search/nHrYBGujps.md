Now I have all the information I need. Let me construct the final consolidated review.

## Summary

BIRD-INTERACT introduces a benchmark for evaluating LLMs on dynamic, interactive text-to-SQL tasks that go beyond static-conversation benchmarks like CoSQL and SParC. It contributes (1) a function-driven user simulator that prevents ground-truth leakage, (2) two evaluation settings (*c*-Interact for conversational and *a*-Interact for agentic interaction), and (3) 900 tasks spanning full CRUD operations with injected ambiguities and state-dependent follow-up sub-tasks. Experiments on 7 frontier LLMs show low success rates (GPT-5: 8.67% *c*-Interact, 17% *a*-Interact), with further analysis via memory grafting and interaction test-time scaling.

## Strengths

1. **Function-driven user simulator with strong empirical validation.** The two-stage strategy (parse to AMB/LOC/UNA actions, then generate response) is a clear improvement over naive LLM-based simulators. Figure 6 shows baseline simulators fail on Unanswerable (UNA) questions 67.4% of the time (leaking ground-truth information), while the proposed approach reduces this to 2.7%. Table 3 further shows the function-driven simulator achieves a Pearson correlation of 0.84 (p=0.02) with human users versus 0.61 (p=0.14) for the baseline — a concrete, measured improvement. (Verified: Section 3.3, Figure 6, Table 3)

2. **Dual evaluation settings with budget-constrained awareness.** *c*-Interact (protocol-guided) and *a*-Interact (autonomous, 9-action tool set) capture qualitatively different interaction paradigms. The budget formulas (τ_clar = m_amb + λ_pat; B = B_base + 2m_amb + 2λ_pat) with adaptive constraints and per-action cost multipliers (Figure 3) go well beyond existing static-conversation benchmarks that do not distinguish interaction modalities or impose resource constraints. (Verified: Section 4, Figure 3)

3. **Comprehensive CRUD task suite with state-dependent follow-ups.** Unlike all prior multi-turn text-to-SQL benchmarks (CoSQL, SParC, LEARN-TO-CLARIFY) which are SELECT-only, BIRD-INTERACT covers the full Create/Read/Update/Delete spectrum (410 BI + 190 DM tasks on FULL). The systematic ambiguity injection taxonomy (superficial, knowledge chain-breaking, environmental) and follow-up sub-tasks that depend on modified database states are principled additions. (Verified: Sections 2, 3.2, Table 1)

4. **Memory grafting experiment cleanly isolates interaction from SQL generation.** Figure 5 shows GPT-5's *c*-Interact success rate jumps from 13.8% to 20.5% when provided with O3-mini's interaction history, while its own history yields only 13.8%. This provides causal evidence that GPT-5's failures stem from communication deficits rather than SQL generation ability — directly supporting the paper's central thesis. (Verified: Section 5.2, Figure 5)

## Weaknesses

### Major

1. **Missing single-turn baselines on the FULL set conflate interaction difficulty with base SQL difficulty.** The paper asserts that BIRD-INTERACT measures "strategic interaction capabilities" and that low success rates demonstrate a "critical gap" in interaction skills. However, Table 2 (the main results on FULL) contains no column for single-turn (ambiguity-free) performance. The only single-turn reference is the "Idealized Performance" dotted line in Figure 4, shown for only 4 models on the LITE set — and that idealized performance is already quite low (~20% for most models). Without this baseline for all models on FULL, the headline results cannot be attributed to interaction deficits rather than inherent SQL difficulty of the underlying tasks. The memory grafting experiment (Figure 5) partially addresses this but only for GPT-5. This is the paper's most significant evidential gap. (Verified: Table 2 has no single-turn column; Figure 4 shows idealized performance only for 4 models on LITE; Section 5.2 discusses memory grafting for GPT-5 only)

2. **The "ITS Law" is overstated relative to the evidence.** The paper defines an "ITS Law" (Section 5.2) stating a model can "match or even surpass" idealized single-turn performance given enough interaction turns. The evidence for this claim is weak: (a) Claude-3.7-Sonnet in *c*-Interact is the only clear case of scaling that crosses the idealized threshold; (b) O3-Mini in *c*-Interact barely scales (remains flat around 15%); (c) in *a*-Interact, most models show flat or decreasing trends (Figure 4). Calling this a "law" based on one model's behavior in one setting is an overclaim that should be significantly tempered. (Verified: Figure 4; Section 5.2: "Claude-3.7-Sonnet exhibits clear scaling behavior" — only one model named; the ITS Law definition is general but not supported by most tested models)

### Minor

1. **Single-run experiments without variance/confidence intervals.** The paper acknowledges "conducting single runs due to cost" (Section 5, line 177). While temperature=0 makes single runs a common practice in LLM evaluation, several model comparisons in Table 2 differ by small margins (e.g., GPT-5 at 14.50% vs. Claude-Sonnet-3.7 at 18.00% on *c*-Interact priority). The paper draws conclusions about model-specific strengths across interaction modes (Section 5.1, bullet 4) from these small differences. Confidence intervals or a stability estimate would substantially strengthen the claims. (Verified: Section 5, line 177; Table 2)

2. **Human correlation experiment has a limited sample size.** The correlation with human users (Table 3) is based on only 100 tasks and 7 system models. The main result (GPT-4o w/ Func.: Pearson 0.84, p=0.02) is significant at α=0.05 but would not survive a strict Bonferroni correction for the four comparisons. The p-values for Gemini-2.0-Flash baseline (0.21) are not significant. While the trend is encouraging and the direction of improvement is clear, the current evidence could be stronger. (Verified: Table 3, Section 6)

### Trivial

1. **Inter-annotator agreement lacks methodological detail.** Table 1 reports agreement of 93.33/93.50 but does not state the number of annotators used for the agreement calculation or the number of overlap tasks. (Verified: Table 1, Section 3.2 — "12 expert annotators" mentioned but not linked to agreement computation)

## Nice-to-Haves

- Compare model performance on BIRD-INTERACT to static-conversation benchmarks (CoSQL, SParC) to quantify the added challenge of dynamic interaction.
- Replicate the memory grafting experiment for a second poorly-communicating model beyond GPT-5 to confirm generality.
- Report per-action success rates for debugging in *c*-Interact (what types of errors are fixable?).
- Provide qualitative case studies of interaction trajectories (e.g., do models ask irrelevant questions or fail to ask when needed?).

## Removed Points

These points are flagged to be removed; treat them with caution.

- **"Density of ambiguities is unrealistic"** (Harsh Critic): The paper pitches realism about interaction *structure*, not ambiguity density. The high density is a stress-testing design choice, consistent with the paper's framing. The paper does not claim the ambiguity density matches real-world distributions. Removed — scope creep / misreading of paper's claim.

- **"ITS Law" as a strength** (Strength Finder): Conflicts with the verified weakness (#2 above) that the law is overstated relative to evidence. Per instructions: when strength and weakness disagree, the weakness wins. Removed.

- **"Missing details about annotator count for agreement"**: Kept as Trivial, not removed.

- **"Single-turn baselines are missing"** speculation that the paper cannot disentangle factors: This is factually verified (Table 2 lacks single-turn columns) and kept as Major weakness #1. The executive summary frames this correctly.

- **"HKB knowledge chain breaking advantages/disadvantages certain models"** (Harsh Critic): Speculative concern with no evidence in the paper that any model is systematically advantaged. Removed.

- **Customization of the a-Interact budget at B_base=6 being arbitrary**: All benchmarks involve design choices; there's no evidence this specific choice biases results. Removed.

## Novel Insights

The harsh critic correctly identifies that BIRD-INTERACT's most interesting empirical finding is the *dissociation* between *c*-Interact and *a*-Interact performance: GPT-5 is worst in *c*-Interact (14.50% SR) but best in *a*-Interact (29.17% SR), while other models show different patterns. This mode-dependent variance in model capability is more informative than the aggregate low scores and deserves deeper analysis — particularly whether it stems from training data distributions (e.g., GPT-5's RLHF optimizing for agentic autonomy) or architectural inductive biases. The memory grafting experiment is a novel and clean diagnostic for isolating communication from generation, and extending it to more models and settings would be highly valuable. None of the anchor papers (Spider 2.0, MMQA, CHASE-SQL) attempt this kind of interaction-ability decomposition.

## Suggestions

1. **Add single-turn baselines to Table 2.** Report the ambiguity-free ("idealized") success rate for all 7 models on the FULL set alongside the interactive results. This single addition would allow readers to quantify how much of the observed difficulty comes from interaction demands versus base SQL complexity, directly addressing the most significant weakness.

2. **Temper the ITS Law claim.** Rename to "Interaction Test-time Scaling behavior" or "observed scaling patterns" and clearly state which models/settings exhibit it and which do not. The current framing as a "law" is unsupported by the data.

3. **Add confidence intervals or a stability analysis.** For at least the main comparisons in Table 2, compute binomial confidence intervals or report results from 2–3 seeds to establish whether model rankings are stable, especially given the small margins.

4. **Expand the human correlation study** to at least 200–300 tasks, or acknowledge the sample size limitation more prominently when interpreting the correlation results.

## Score and Decision

**Calibration anchors** (all retrieved from the corpus):

| Anchor | Avg Score | Comparison |
|--------|-----------|------------|
| Spider 2.0 | 8.00 | Stronger evaluation methodology on a related benchmark; comparable contribution scale. BIRD-INTERACT is slightly below due to weaker empirical validation. |
| MMQA | 8.00 | Cleaner evaluation pipeline on a narrower scope. BIRD-INTERACT is more ambitious but less polished empirically. |
| CHASE-SQL | 6.25 | Accepted method paper with mixed reviews. BIRD-INTERACT has a stronger contribution (new benchmark infrastructure) but similar-level empirical concerns. |
| DataSciBench | 3.20 | Rejected benchmark with weaker construction. BIRD-INTERACT is substantially stronger in novelty, methodology, and evidence. |
| TrustSQL | 4.00 | Rejected for limited scope. BIRD-INTERACT is clearly stronger across all dimensions. |
| DB-GPT-Hub | 3.75 | Rejected for lacking novelty beyond integration. BIRD-INTERACT is far stronger in original contribution. |

The paper makes genuine research contributions (user simulator design, dual evaluation settings, CRUD task suite, memory grafting diagnostic) that are clearly above the reject-level benchmarks in the corpus. However, the two major weaknesses — missing single-turn baselines on the FULL set and the overclaimed ITS Law — prevent the empirical evidence from fully supporting the paper's central claim about interaction difficulty. The paper is accept-worthy with revisions but not at the level of the strongest accepted benchmarks.

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>