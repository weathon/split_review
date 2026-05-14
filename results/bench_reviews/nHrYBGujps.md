Now I have all the information needed. Let me write the final review.

---

## Summary

BIRD-INTERACT reimagines text-to-SQL evaluation by introducing a dynamic, multi-turn benchmark with 900 tasks covering the full CRUD spectrum. Its core innovation is a two-stage function-driven user simulator (parser → constrained symbolic actions → response generator) that enables models to solicit clarifications, resolve ambiguities, and recover from errors without human supervision. The benchmark exposes a stark performance gap: even GPT-5 achieves only 8.67% success in the conversational setting and 17.00% in the agentic setting, demonstrating that current LLMs lack the strategic interaction skills required for realistic database querying.

## Strengths

- **Compelling benchmark design addressing a real gap.** Existing multi-turn text-to-SQL benchmarks use static dialogue transcripts; BIRD-INTERACT is the first to combine dynamic user simulation, dynamic environment state, multiple ambiguity sources (user-query, knowledge-chain, environmental), and executable CRUD operations in a unified framework. The comparison in Table 4 (Appendix E) substantiates this distinctiveness.

- **Principled function-driven user simulator with strong validation.** The two-stage design (parser → AMB/LOC/UNA → generator) dramatically reduces ground-truth leakage: on USERSIM-GUARD, failure rates on unanswerable (UNA) questions drop from 67.4% (baseline) to 2.7% (Figure 6, Table 11). The simulator also correlates more strongly with human success rates (Pearson 0.84) than an unconstrained LLM baseline (0.61), though sample size caveats apply (see Weaknesses).

- **Rigorous annotation and quality control.** Twelve expert annotators were recruited through a multi-stage selection process (Appendix C); ambiguity annotations use double-blind checking with 93.33% inter-annotator agreement (Table 1); human evaluation of 300 randomly sampled data points yields 97.3% overall acceptance and 98.7% SQL correctness (Appendix Q). This level of quality control is uncommon in benchmark papers.

- **Informative empirical findings.** The starkly low success rates (8.67%–17.00% for GPT-5) convincingly demonstrate that strong single-turn SQL performance does not translate to interactive settings. Memory grafting (Figure 5) shows that communication skill, not SQL-generation ability, is the bottleneck for GPT-5. The interaction test-time scaling analysis (Figure 4) reveals monotonic improvement with interaction budget for several models.

- **Full CRUD coverage with state-dependent follow-ups.** Unlike read-only benchmarks, tasks span INSERT/UPDATE/DELETE/DDL operations, and follow-up sub-tasks depend on database state modified by preceding queries (Section 3.2, Table 1), mirroring real operational scenarios.

## Weaknesses

### Fatal

None.

### Major

- **LOC action introduces structural ground-truth dependency.** The LOC() action handles clarification questions outside pre-annotated ambiguities by performing AST-based retrieval on the ground-truth SQL to locate the relevant fragment and generate a response (Section 3.3, Appendix N). When a model asks about implementation details (formatting, formula choice, join type), the simulator answers by inspecting the correct solution. While the paper frames this as a feature ("without leaking the entire query"), it injects information that a real user—who has a high-level intent but not the exact SQL—may not be able to provide with such precision. This is a genuine structural concern because it means interaction histories used in the memory-grafting experiment and elsewhere contain simulator answers derived from the oracle. The magnitude of this issue depends on how frequently LOC is triggered versus AMB (which uses pre-annotated clarification sources), but the paper does not report LOC invocation frequency. The USERSIM-GUARD evaluation shows that LOC accuracy is high (the function-driven approach does retrieve correctly), but it does not address the underlying concern that LOC is answering from the ground truth. Mitigating factors: (1) LOC is a fallback for questions outside pre-annotated ambiguities; the primary interaction mode is AMB. (2) Many LOC-type questions (e.g., "what precision should I use?") are things a domain-expert user *would* know, so the realism gap is not uniform across all LOC invocations. (3) The future work section explicitly plans a post-trained human-aligned simulator, acknowledging that the current design has room for improvement. Nonetheless, this structural feature means the benchmark's difficulty and the memory-grafting results should be interpreted with some caution about the realism of LOC-mediated answers.

### Minor

- **Single-run evaluation without variance estimates.** All experiments use one run per model with temperature=0 and top_p=1 (Appendix I.3). While the paper cites cost constraints—which are reasonable for 600 tasks × 7 models × 2 settings—and deterministic decoding does reduce variance, API-based models can exhibit non-determinism even at temperature=0. With success rates in single digits, a shift of a few tasks can meaningfully change percentages. The main finding (models perform poorly) is robust, but model-to-model comparisons and rankings would benefit from even a second run or a discussion of expected variance.

- **Underpowered correlation analyses.** The human-simulator alignment study (Table 3) computes Pearson correlations across n=7 models using 100 tasks. While a correlation of 0.84 (p=0.02) is nominally significant, n=7 provides limited statistical power, and the claim of "significantly stronger alignment" compares p-values (0.02 vs. 0.14) rather than directly testing the difference between correlations. Similarly, the action-distribution correlation analysis (Pearson r≈0.41, Spearman ρ≈0.54) in Appendix J is based on the same 7 data points—these coefficients should be treated as suggestive observations, not statistical evidence of causation.

- **LOC retrieval accuracy not independently evaluated.** Appendix N describes the AST-based retrieval pipeline but provides no quantitative evaluation of retrieval accuracy: how often does the semantic search correctly identify the relevant AST node? The USERSIM-GUARD LOC accuracy numbers (Table 11) evaluate the full pipeline end-to-end but do not decompose retrieval errors from generation errors. A failure analysis would strengthen confidence in the LOC mechanism.

### Trivial

- **Reward weighting could be better motivated.** The 0.7/0.5 weighting for sub-task 1 and 0.3/0.2 for sub-task 2 (Appendix F.2) is reasonable—sub-task 1 is more important since failure terminates the session—but the specific values are not empirically justified. Since Success Rate is the primary metric and Normalized Reward is secondary, this is a minor presentation issue.

## Nice-to-Haves

- Reporting LOC invocation frequency (how often LOC is triggered vs. AMB) would help readers assess the scope of the ground-truth dependency concern.
- A controlled ablation replacing LOC responses with a "no information" baseline on a subset of tasks would quantify the performance impact of LOC-derived answers.
- Error bars or a second run for the main results table would strengthen the quantitative claims.

## Removed Points

*These points are flagged to be removed; treat them with caution.*

1. **"DM test scripts insufficiently validated — if any script contains a bug, the metric would be biased" (Harsh Critic, Critical Issue 2).** The paper documents a thorough quality-control process: 12 expert annotators with multi-stage selection, double-blind annotation with 93.33% inter-annotator agreement, and human evaluation yielding 98.7% SQL correctness. While independent verification of test scripts would be ideal, the same criticism applies to virtually every benchmark with custom test cases. The rigor already demonstrated is above the field's standard. Removed as disproportionately demanding.

2. **"User Simulator Relies on Ground-Truth SQL... this structural feature erodes the claim that the benchmark faithfully simulates real-world interactive text-to-SQL and weakens all subsequent quantitative conclusions" (Harsh Critic, Critical Issue 1, characterization that it invalidates all conclusions).** The core of this concern is retained as a Major weakness, but the harsh critic's characterization that this "erodes...all subsequent quantitative conclusions" is an overstatement. The primary interaction path (AMB) uses pre-annotated clarification sources, not ground-truth SQL. LOC is a fallback. Retained the substantive concern, removed the absolutist conclusion.

3. **"Missing experiments: Simulator Leakage Audit, DM Test Script Verification, Multi-run Results" (Harsh Critic, Missing Parts).** These are suggestions for improvement, not weaknesses. The simulator leakage audit is captured under Nice-to-Haves. The DM test script verification demand is removed (see point 1). Multi-run results are captured as a Minor weakness.

4. **"Action Distribution... the reported Pearson/Spearman coefficients are not meaningful statistics and should not be presented as evidence of causation" (Harsh Critic, Section-by-Section Notes).** Partially retained as a Minor weakness about underpowered statistics, but the harsh critic's claim that they should not be presented at all is too strong—correlations with small n can be suggestive if properly caveated.

5. **Formatting/typo nitpicks:** Removed per hard rules.

## Novel Insights

The paper's most genuinely novel observation is that communication skill, not SQL-generation capability, is the binding constraint for flagship models in interactive settings. The memory-grafting experiment (Figure 5) cleanly isolates this: GPT-5, which underperforms in c-Interact despite strong single-turn SQL ability, recovers substantially when given interaction histories from better-communicating models. This suggests that future progress in text-to-SQL may depend as much on training models to ask good questions as on improving SQL generation—a non-obvious finding that the static-transcript benchmarks could never have revealed.

## Suggestions

- Quantify LOC invocation frequency in the main results and discuss the ground-truth dependency more candidly in Section 3.3. This would preempt the most significant criticism readers will raise.
- Add a brief caveat about the limited statistical power of the n=7 correlation analyses (Tables 2-3, action-distribution analysis). The correlations are suggestive and worth reporting, but the paper should not present them as confirmatory evidence.
- Consider running even a single additional seed for the top two models (GPT-5, Gemini-2.5-Pro) to provide a rough estimate of run-to-run variance. This would substantially strengthen the quantitative claims at modest additional cost.
- Report LOC retrieval accuracy separately from end-to-end LOC accuracy in the USERSIM-GUARD analysis to help readers understand whether failures stem from retrieval errors or generation errors.

---

## Score and Decision

**Anchor comparison:**

| Anchor | Avg Score | Comparison |
|---|---|---|
| MCPMark (`/home/wg25r/review_agent/human_reviews_2026/uobROwBsJm.md`) | 7.33 | Cleaner benchmark with fewer structural concerns, but narrower scope (127 tasks, tool-use focus). BIRD-INTERACT is more ambitious and has more validation but also more rough edges. |
| EHR-ChatQA (`/home/wg25r/review_agent/human_reviews_2026/hLweUPBz7k.md`) | 4.00 | Similar interactive DB-QA ambition but uses an unstructured LLM-based simulator. BIRD-INTERACT's function-driven simulator with USERSIM-GUARD validation is a clear improvement. BIRD-INTERACT is substantially stronger. |
| BIRD-Ent (`/home/wg25r/review_agent/human_reviews_2026/gXkIkSN2Ha.md`) | 3.60 | Enterprise text-to-SQL with static evaluation. BIRD-INTERACT's dynamic interaction design and simulator contribution are more novel and better validated. |
| Squirrel Benchmark (`/home/wg25r/review_agent/human_reviews_2026/8Fm6OKFuRv.md`) | 5.00 | SQL debugging benchmark with good ideas but overclaimed enterprise realism. BIRD-INTERACT has more rigorous validation and a clearer contribution. |
| ConDABench (`/home/wg25r/review_agent/human_reviews_2026/jOxfpsnDFo.md`) | 2.50 | AI-generated interactive data analysis benchmark with limited human validation. BIRD-INTERACT's human annotation rigor puts it far above this tier. |
| Octopus (`/home/wg25r/review_agent/human_reviews_2026/BdlIQGetYv.md`) | 2.50 | Auto-generated text-to-SQL benchmark without human quality measurement. BIRD-INTERACT is clearly stronger. |

BIRD-INTERACT sits between the 4.0-range papers (which it clearly surpasses on simulator design, validation rigor, and empirical depth) and the 7.33 MCPMark (which is cleaner but narrower). The LOC structural concern is real and prevents a score in the 7+ range, but the paper's strengths—principled simulator design, rigorous annotation, strong USERSIM-GUARD validation, compelling empirical findings—place it well above the 4.0-tier. A score of 6.0 reflects a solid benchmark paper with genuine contributions and addressable weaknesses.

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>