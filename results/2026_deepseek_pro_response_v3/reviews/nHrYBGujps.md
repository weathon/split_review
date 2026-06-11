Now I have a clear calibration picture. Let me write the final review.

**Round 1 Bracket:** 5.0 – 7.5
**Round 2 Comparison:** BIRD-INTERACT is comparable to τ-bench (6.50, Accept) — both are interactive benchmark papers with LLM-simulated users, but BIRD-INTERACT's function-driven simulator is more principled. It sits slightly below MINT (6.75, Accept) which has broader task coverage. It is clearly above SQL-GEN (5.67, Reject) and TrustSQL (4.00, Reject). It is below Spider 2.0 (8.00, Accept) which has enterprise-scale real data.

**Final Score: 6.5**

---

## Summary
BIRD-INTERACT introduces a benchmark for evaluating LLMs on interactive, multi-turn text-to-SQL tasks. It builds on LIVESQLBENCH by injecting ambiguities and follow-up sub-tasks, and provides a novel function-driven user simulator, two complementary evaluation settings (conversational c-Interact and agentic a-Interact), and 900 tasks covering full CRUD operations. Headline results show GPT-5 achieves only 8.67% end-to-end success in c-Interact and 17% in a-Interact on the full suite.

## Strengths
- **Function-driven user simulator with compelling anti-leakage validation**: The two-stage approach (symbolic action mapping → controlled response generation) reduces ground-truth leakage on unanswerable questions from 67.4% (baseline) to 2.7% on USERSIM-GUARD (Figure 6), and achieves Pearson correlations of 0.79–0.84 with human user success rates (Table 3). This is a principled solution to a known problem in LLM-based user simulation.
- **Memory grafting experiment cleanly isolates communication vs. generation capability**: Providing GPT-5 with interaction histories from better-communicating models raises its c-Interact priority SR from 13.8% to 20.5% (Figure 5), nearly matching the donor model's own performance. This directly demonstrates that GPT-5's SQL generation is adequate but its communication strategy is the bottleneck — a well-designed diagnostic experiment.
- **Dual evaluation settings reveal genuine model-specific interaction aptitudes**: GPT-5 ranks worst in c-Interact (14.50% priority SR) but best in a-Interact (29.17%), while other models show the opposite pattern. This consistent inversion across models (Table 2) validates the need for both settings and constitutes an empirical discovery about how different interaction paradigms interact with model capabilities.
- **State-dependent follow-up sub-tasks advance beyond prior benchmarks**: Unlike COSQL/SParC which treat conversation history as static context, BIRD-INTERACT requires reasoning over database states modified by preceding queries (Section 3.2), a concrete architectural advance reflected in consistently lower follow-up SR across all models.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor
- **Memory grafting experiment lacks dataset specification**: Figure 5 reports baseline numbers (GPT-5: 13.8%, Qwen-3-Coder: 18.5%, O3-Mini: 18.5%) that differ substantially from the corresponding FULL-set results in Table 2 (14.50%, 22.00%, 24.00%). The paper never states whether this experiment uses FULL, LITE, or a subset. If it uses LITE, the baseline numbers should be cross-referenced with the LITE results (Table 10, in appendix). This is a clarity issue that undermines the interpretability of an otherwise strong experiment.
- **Inter-annotator agreement metric undefined**: Table 1 reports "Inter-Agreement" of 93.33–93.50% without specifying what the annotators were agreeing on — ambiguity classification, clarification annotations, test-case correctness, or something else. This makes the 93% figure uninterpretable.
- **ITS Law framing is aspirational, not supported by data**: The paper defines an "ITS Law" (Section 5.2) — a model satisfies it if interaction turns enable matching idealized single-turn performance — but Figure 4 shows no model reaches the idealized performance line even at patience=7. The paper does not claim any model satisfies it, but the framing conflates the monotonic improvement trend (which is real) with the stronger claim implied by calling it a "law." The data actually shows that additional interaction turns provide only marginal gains and never close the gap — an interesting negative result that should be highlighted rather than wrapped in aspirational framing.
- **Human-alignment study validates outcome ranking, not turn-by-turn behavior**: The 100-task study (Table 3) shows simulator-evaluated success rates correlate with human-evaluated ones (r=0.79–0.84), but does not validate that the simulator's per-turn responses (clarification quality, error tolerance, feedback specificity) resemble a human's. A systematically lenient simulator could produce correlated SR while distorting absolute performance estimates.
- **Single-run evaluation with temperature=0**: The paper runs each model once citing cost (Section 5). While temperature=0 makes runs largely deterministic and single-run evaluation is common in benchmark papers, very small differences in rankings (e.g., Deepseek 18.50% vs Claude-Sonnet-3.7 18.00%) are within potential noise. The granular ranking conclusions would be stronger with even a small-sample variance estimate on a subset.

### Trivial
- **Budget formula rationale is thin**: The a-Interact budget constants (base=6, multiplier=2 in Section 4.2) are stated without justification for these specific values.
- **Knowledge chain breaking prevalence not quantified**: The paper describes this ambiguity type qualitatively (Section 3.2) but doesn't report what fraction of tasks it affects.

## Nice-to-Haves
- A failure taxonomy (qualitative analysis of common failure modes) would make the benchmark far more actionable for researchers, especially given that models fail 83–91% of the time.
- Discussion of the artificiality of ambiguity injection: surgical removal of knowledge by annotators who know the answer may produce different interaction dynamics than naturally occurring ambiguity. Acknowledging this would temper claims about "restoring missing realism."
- Clarifying whether LITE tasks are a subset of FULL or separate tasks, since results from each are reported in different parts of the paper (Table 2 for FULL, Figure 4 for LITE).

## Removed Points
These points are flagged to be removed, treat them with caution:

**From Harsh Critic — removed or demoted:**
- "Single-run evaluation without variance estimates (structural)" — demoted from structural/fatal to Minor. At temperature=0, deterministic runs are standard for large-scale benchmarks; the paper acknowledges cost constraints. Not a structural flaw.
- "Data inconsistencies between experiments (evidential)" — demoted to Minor. The discrepancy between Figure 5 and Table 2 likely reflects use of different datasets (LITE vs FULL). The issue is lack of explicit specification, not evidence of fabricated data.
- "ITS law framing misrepresents the evidence" — demoted to Minor. The paper defines the law conditionally ("satisfies this law if...") rather than claiming any model satisfies it. The framing is slightly misleading but not a data misrepresentation.
- "Ambiguity injection may produce artificial rather than ecologically valid interactions (structural)" — moved to Nice-to-Haves. The methodology is explicitly a controlled experiment; the "restoring missing realism" claim is about moving beyond static transcripts, not perfectly naturalistic ambiguity.
- "User simulator validation is underpowered (evidential)" — demoted to Minor. N=100 with p=0.02–0.03 and r=0.79–0.84 is a strong result. The concern about turn-by-turn validation is a genuine limitation, not evidence of underpowering.
- "Abstract claims 'up to 11,796 dynamic interactions' inflates apparent horizon length" — removed. Table 1 confirms ~13 interactions/task, and the 11,796 figure is accurate for the FULL set's total interaction count.
- "Follow-up difficulty attribution to 'longer context' is untested" — removed. The paper hedges appropriately ("likely because") and this is a reasonable interpretation for a benchmark paper.
- "Action distribution claim about pre-training biases is speculative" — removed. The paper uses appropriately hedged language ("suggests," "likely due to").

**From Strength Finder — removed:**
- "ITS Law formulation provides a useful conceptual lens and is supported by the comparison against the idealized line" — removed. The data shows no model reaches the idealized line; presenting the law as a supported strength is incorrect.

## Novel Insights
The memory grafting experiment is genuinely novel: rather than simply reporting that a model performs poorly, it surgically transplants interaction histories from better models to show that the deficit is in communication strategy rather than SQL generation capability. This diagnostic methodology isolates capability dimensions (generation vs. communication) in a way that could be productively applied in other interactive AI benchmark domains.

## Suggestions
- Specify the dataset used for the memory grafting experiment (Figure 5) and report the corresponding baseline numbers from that dataset for cross-reference.
- Define what "Inter-Agreement" in Table 1 measures — at minimum, state whether it refers to ambiguity classification, clarification annotation, or test-case correctness.
- Reframe the ITS Law discussion to foreground the finding that additional interaction turns provide only marginal gains and no model closes the gap to idealized performance — this is an interesting negative result.
- Consider adding even a small qualitative failure analysis (e.g., 10–20 representative cases) to help researchers understand where models break down.

## Calibration Anchors

| Anchor Paper | Avg Score | Round | Comparison |
|---|---|---|---|
| DB-GPT-Hub (NmILZXKcOi) | 3.75 | 1 | BIRD-INTERACT is substantially stronger: more scope, novelty, and experimental depth |
| TrustSQL (7ZeoPg3eTA) | 4.00 | 1 | BIRD-INTERACT is clearly stronger: larger scale, more principled methodology |
| EVOSCHEMA (NfUHBaZdLw) | 4.25 | 1 | BIRD-INTERACT has broader scope and more novelty |
| LAIA-SQL (WYdpjwKQma) | 5.00 | 2 | BIRD-INTERACT is stronger: more comprehensive benchmark design |
| SQL-GEN (RaSLSUCKz0) | 5.67 | 1/2 | BIRD-INTERACT is comparable or slightly stronger: more scope, but different contribution type |
| τ-bench (roNSXZpUDN) | 6.50 | 2 | Comparable: both interactive benchmarks with LLM-simulated users; BIRD-INTERACT's function-driven simulator is more principled |
| MINT (jp3gWrMuIZ) | 6.75 | 2 | Slightly below: MINT has broader task coverage and more model evaluation, but BIRD-INTERACT's user simulator is more carefully controlled |
| Spider 2.0 (XmProj9cPs) | 8.00 | 1 | BIRD-INTERACT is clearly below: Spider 2.0 has enterprise-scale real data and more comprehensive evaluation |

Round 1 bracket: 5.0–7.5. Round 2 narrowed this by comparison with τ-bench (6.50) and MINT (6.75). BIRD-INTERACT is comparable to τ-bench in quality and scope — both are solid benchmark papers with some clarity/scope limitations — and slightly below MINT which covers broader tasks. Final score: 6.5.

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>