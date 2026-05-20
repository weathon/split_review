## Summary

This paper proposes PELICAN, a two-stage adaptive tutoring framework that first performs collaborative cognitive diagnosis (using a successor-first traversal through a hierarchical knowledge graph, with an expert-assistant-verifier pipeline ensuring question accuracy) and then uses a fast-and-slow thinking mechanism (with a simulated teaching tree for strategy selection when students face persistent difficulties) to tailor instruction to individual cognitive states. Evaluation on the Gaokao math dataset includes automated metrics, GPT-based assessments, ablation studies, and a real-world human evaluation with 169 students.

## Strengths

- **Novel integration of collaborative cognitive diagnosis with adaptive tutoring.** The two-stage design — diagnosing the student's knowledge state via a successor-first hierarchical traversal before selecting tutoring strategies — is well-motivated and sound. Table 1 shows PELICAN achieves the highest diagnostic accuracy (F1=94.31) with the fewest rounds (Avg. Round=5.83), substantially outperforming Free-Prompt (F1=74.18, 7.21 rounds) and CoT (F1=79.83, 8.79 rounds). This validates the successor-first strategy and the expert-assistant-verifier pipeline.

- **Clear evidence that cognitive-state-aware tutoring improves coverage of non-mastered knowledge.** Table 2 shows PELICAN achieves substantially higher R_coverage (72.36 vs. next-best 64.47) and F_frequency (72.06 vs. 66.71) over all baselines, directly supporting the claim that modeling cognitive state leads to more targeted instruction.

- **Ablation studies support the key design choices.** Table 3 shows that removing the diagnosis module drops R_coverage from 54.84 to 47.76, and removing the slow-thinking module drops Suitability from 4.17 to 4.00, confirming that both components contribute to the method's performance.

- **Real-world human evaluation with 169 students.** Table 6 reports a practical deployment, with PELICAN achieving the highest scores across most subjective metrics (Appropriateness 4.23, Sentiment 4.42, Inspiration 4.33, Overall 4.39) while also leading on R_coverage (70.04) and F_frequency (70.07).

## Weaknesses

### Fatal
None.

### Major

- **The abstract makes unsupported quantitative claims.** The abstract states "significant improvements in critical thinking stimulation (+18.7%) and task completion rates (+22.4%) compared to baseline models." These percentage values **appear nowhere else in the paper** — no table, metric definition, or textual passage explains or supports them. The closest reported metrics are: (a) Inspiration scores in Table 2 (PELICAN 4.21 vs. best baseline Socratic 3.99, a ~5.5% relative gap); (b) success rates in Table 6 (PELICAN 86.8% vs. best baseline Sepwise 86.5%, a 0.3% absolute gap). Neither corresponds to +18.7% or +22.4%. This is a significant accuracy and transparency issue: a reader cannot verify the headline claims. The paper must either remove these numbers or clearly trace them to specific metrics and computation formulas.

### Minor

- **Strategy distribution shows limited evidence of dynamic adaptation.** Figure 4 reports that 7 of 9 teaching strategies are used at *identical* percentages across all three cognitive levels (Suggestion 2%, Confirmation 5%, Correction 8%, Open Question 5%, Closed Question 5%, Simplification 10%, Decomposition 12%). Only Explanation (32/33/30) and Analogies (22/18/15) vary. The paper's claim that the system adapts strategies per cognitive state is only weakly supported by these data — the near-uniform distribution across seven strategies suggests either small sample sizes or limited actual adaptation. The authors should discuss this limitation explicitly.

- **No variance reported for baseline methods.** Table 2 reports standard deviations only for PELICAN (e.g., R_coverage ±4.69) but none for any baseline method. This makes it impossible to assess whether PELICAN's lead over the best baseline (e.g., R_coverage 72.36 vs. Socratic 64.47) is statistically significant. Table 6 similarly lacks variance or significance testing (the paper references an ANOVA in the stripped Appendix K).

- **An odd result in the ablation is not discussed.** Table 3 shows that removing *both* the diagnosis module and the slow-thinking module yields the *highest* Inspiration score (4.56 vs. PELICAN's 4.30). This counterintuitive result — the full system underperforming its ablated version on a key metric — is not addressed or explained.

- **Qwen-max achieves higher R_coverage than PELICAN with GPT-4o.** In Table 4, Qwen-max reaches R_coverage=64.41 while PELICAN (GPT-4o) scores 54.84. The paper does not discuss why a cheaper backbone outperforms the default on this objective metric, or what trade-off this represents.

- **Slow thinking threshold M=1 means it is almost always triggered.** The paper frames slow thinking as a "fallback for persistent obstacles" (Section 3.3.3), but M=1 (line 358) means slow thinking activates after just one round — essentially making it the default selection mechanism. This weakens the conceptual link to dual-system theory, where slow thinking should be the exception, not the rule.

- **GPT-based evaluator model is not specified.** The paper uses GPT-based assessments (Suitability, Logicity, Inspiration, etc.) but never states which model serves as the evaluator. Since the teacher model is GPT-4o, circularity is a concern if the evaluator is also GPT-4o. The human evaluation mitigates this somewhat, but the paper should state the evaluator model explicitly and discuss potential bias.

### Trivial

- The case study (Figure 5) is illustrative but cherry-picked; the baselines shown (Free-Prompt, Sepwise, Socratic) also provide reasonable explanations for "even function," and it is subjective which is pedagogically superior.
- The knowledge state update rule (Section 3.3.2) is described in one sentence without formal detail on how $\hat{K}_u^{(t)}$ is computed from $\hat{K}_u^{(t-1)}$ and response type.

## Nice-to-Haves

- Validate the student simulation model (used in the slow-thinking tree search) against real student response data to ensure the simulated dialogues are plausible.
- Ablate the slow-thinking tree search against a faster heuristic (e.g., always select the top-1 strategy without simulation) to isolate the value of the tree search itself from the value of having a strategy pool.
- Report statistical significance (e.g., bootstrap confidence intervals) for all main comparisons.
- Provide per-metric inter-annotator agreement for the human evaluation dimensions.

## Removed Points

- **"The related work limitations are asserted rather than demonstrated"** — This is a subjective characterization of writing style, not a concrete weakness. The paper cites specific papers and briefly states how they differ. This is standard practice for related work sections.

- **"Successor-first strategy doesn't specify how to choose among multiple leaf nodes"** — This is an implementation detail that is reasonable to leave underspecified in a high-level method description. The system relies on LLM prompting to determine which leaf node to test next, which is an acceptable design choice.

- **"GPT-based evaluation circularity" (framed as critical issue)** — While the evaluator model is not stated, the paper includes a real human evaluation (Table 6) that serves as an independent validation. The concern is valid but not critical, and is more appropriately classified as a minor weakness.

- **Strength Finder's claim "Strategy distribution adapts to cognitive level in pedagogically sensible ways"** — This conflicts with the verified weakness that 7 of 9 strategies are identical across levels. Per protocol, the weakness wins: the adaptation shown is limited to two strategies, so this strength is overstated. The strength is retained at a lower level as partial evidence of differentiation in Explanation and Analogies.

- **"Human evaluation shows near-ceiling success rates with minimal differentiation"** — This overstates the issue. While the success rate gap is small (86.8% vs. 86.5%), the coverage metrics (R_coverage: 70.04 vs. 63.91) and subjective ratings show clearer differentiation. The point is retained in weaker form as a minor weakness.

## Novel Insights

The harsh critic's observation about the strategy distribution (Figure 4) — that 7 of 9 strategies are used at identical rates across cognitive levels despite the system's claim of dynamic adaptation — is a genuinely useful diagnostic finding. It suggests either that (a) the per-cognitive-level sample size is too small to detect differences in low-frequency strategies, or (b) the system's adaptation primarily modulates the two high-frequency strategies (Explanation, Analogies) while the rest fire at roughly constant "background" rates determined by the strategy pool distribution rather than the student's cognitive state. This distinction is important for future work on adaptive tutoring: the paper would benefit from analyzing per-strategy frequency with confidence intervals or per-sequence trajectory data rather than aggregate proportions.

## Suggestions

1. **Fix the abstract immediately.** Remove the unsupported +18.7% and +22.4% claims, or clearly trace each to a specific metric and computation (e.g., "18.7% relative improvement in the Inspiration metric over the best baseline"). As written, these numbers are unverifiable and misleading.

2. **Report standard deviations or confidence intervals for all baselines** in Tables 2 and 6, not just for PELICAN.

3. **Address the strategy distribution finding.** Discuss why 7 of 9 strategies show identical frequencies, and whether this reflects limited adaptation or insufficient sample size.

4. **Explain the Inspiration anomaly** in Table 3 (w/o both modules gets highest Inspiration). Provide a hypothesis for why this occurs.

5. **Specify the GPT-based evaluator model** and either validate it against human judgments or acknowledge the potential circularity.

6. **Justify or raise the M=1 threshold** to better align with the dual-system theory framing.

## Score and Decision

**Calibration anchors consulted:**

| Path | Avg Score | Round | Comparison |
|------|-----------|-------|------------|
| /home/wg25r/review_agent/human_reviews_2026/DwxEIQe0XR.md | 2.50 | R1 low | Cognitive diagnosis paper — less related, much weaker empirical validation |
| /home/wg25r/review_agent/human_reviews_2026/NIhIpxykLK.md | 3.00 | R1 low | TutorBench benchmark — evaluation-only, different genre |
| /home/wg25r/review_agent/human_reviews_2026/3QmrFOiPCy.md | 3.00 | R1 low | Unrelated (AI scaling) |
| /home/wg25r/review_agent/human_reviews_2026/MBJCUQ2Iez.md | 3.33 | R1 low | Unrelated (evaluation framework) |
| /home/wg25r/review_agent/human_reviews_2026/8KeX9cW9Xa.md | 5.00 | R1 mid, R2 low | **Direct comparison:** GuideEval evaluates LLM tutoring; PELICAN builds a full system with human eval. PELICAN has stronger contribution but the GuideEval paper has no unsupported-claims issue. Comparable quality. |
| /home/wg25r/review_agent/human_reviews_2026/bMOdN4jYCZ.md | 4.00 | R1 mid | Unrelated (English standardized tests benchmark) |
| /home/wg25r/review_agent/human_reviews_2026/m3jG3GaNIj.md | 5.33 | R1 mid, R2 low | **STAT:** Cleaner presentation, well-supported claims. PELICAN is slightly weaker due to abstract claims issue. |
| /home/wg25r/review_agent/human_reviews_2026/EYkPcogJxo.md | 5.00 | R1 mid, R2 low | **CSG:** Cognitive structure generation — similar quality, PELICAN has stronger empirical evaluation (human study) but unsupported abstract claims. |
| /home/wg25r/review_agent/human_reviews_2026/ToqlKPCAPX.md | 4.50 | R2 low | **MISTAKEs:** Student error modeling — PELICAN is clearly stronger empirically. |
| /home/wg25r/review_agent/human_reviews_2026/qVadFFSfrI.md | 6.00 | R2 mid | Unrelated (LLM knowledge diagnosis, not tutoring) |
| /home/wg25r/review_agent/human_reviews_2026/0Sex2H5Jnn.md | 6.00 | R2 mid | Unrelated (benchmark) |
| /home/wg25r/review_agent/human_reviews_2026/znnA2Opw6v.md | 6.67 | R2 mid | Unrelated (knowledge editing) |
| /home/wg25r/review_agent/human_reviews_2026/14f18NoEqO.md | 6.50 | R2 mid | Unrelated (LLM adaptation) |

**Round 1 bracket:** The paper clearly sits above weak anchors (2.5–3.33) and clearly below strong anchors (8.0). Plausible range: 4.0–6.0.

**Round 2 narrowing:** Compared against the most similar papers in the 3.5–7.0 range. The paper is comparable or slightly better than "Discerning Minds" (5.0, rejected) and "CSG" (5.0, rejected), slightly weaker than "STAT" (5.33, accepted). The unsupported abstract claims prevent it from reaching the STAT level. Final score anchored at 5.0.

**Final assessment:** The paper proposes a genuinely well-motivated framework with solid empirical evaluation including a human study, and the ablation studies convincingly support the design choices. However, the abstract contains unsupported quantitative claims (+18.7%, +22.4%) that cannot be verified from any table or metric in the paper — a significant accuracy issue. Combined with several minor weaknesses (limited strategy adaptation evidence, missing variance for baselines, an unexplained ablation anomaly), the paper does not meet the acceptance bar in its current form but is close enough that major revisions could make it acceptable.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>