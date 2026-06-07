Now let me synthesize the calibration results.

**Round 1 Bracket:** 4.0–5.5

**Round 2 Narrowing:** I compared PELICAN against:
- **TestAgent** (4.75): PELICAN is clearly stronger — more complete two-stage system, cleaner ablation studies, larger human evaluation (169 vs unspecified volunteers), and more principled technical design (Simulated Teaching Tree vs. simpler adaptive question selection).
- **KCQRL** (5.33): KCQRL is stronger on empirical breadth (15 KT models, two large datasets) and has no credibility issues. PELICAN is more ambitious (full tutoring pipeline) but has significant credibility gaps (unverifiable abstract claims, unexplained table discrepancy). PELICAN is slightly weaker than KCQRL.
- **"Students Rather Than Experts"** (5.00): Very comparable. Both are LLM-in-education papers with simulation-based main evaluation + a human study, both share GPT-evaluation circularity concerns. PELICAN has a more sophisticated technical system but has the abstract credibility issue that SOE doesn't. Roughly equal.

**Final Calibration:** PELICAN sits at approximately **5.0** — comparable to "Students Rather Than Experts," better than TestAgent, worse than KCQRL. The core contribution is real and the human study is meaningful, but the unverifiable abstract claims and unexplained table discrepancy are significant credibility problems that prevent a higher score.

---

## Summary

PELICAN proposes a two-stage LLM-based tutoring framework: Stage 1 performs collaborative cognitive diagnosis using a successor-first questioning strategy with an expert-assistant-verifier pipeline to assess student knowledge, and Stage 2 delivers adaptive tutoring using a dual-system (fast/slow thinking) strategy selection mechanism that builds a Simulated Teaching Tree to anticipate dialogue outcomes. The paper reports results on the Gaokao math dataset (184 questions) with both LLM-simulated students and a human evaluation of 169 real high school students across 1,335 tutoring reports.

## Strengths

- **Well-specified cognitive diagnosis pipeline with demonstrated improvements.** The successor-first questioning strategy with the expert-assistant-verifier pipeline is a concrete, principled mechanism. Table 1 shows PELICAN achieves 94.93% precision / 94.29% recall, substantially above Free-Prompt (84.40/67.60) and CoT (84.64/75.55) baselines, with the pipeline contributing ~1.2 F1 points over the No-Pipeline ablation (93.08 → 94.31).

- **Principled slow-thinking strategy selection via Simulated Teaching Tree.** Section 3.3.3 formalizes iterative node expansion, dialogue simulation, and depth-penalized state evaluation (Equations 3–5) — a search-based approach to strategy choice that goes beyond single-step prompt-based methods. Table 2 shows R_coverage of 72.36 vs. 64.47 (Socratic) and Inspiration of 4.21 vs. 3.99 (Socratic).

- **Substantial human evaluation with real students.** The study with 169 high school students (1,335 reports, Table 6) provides external ecological validation. PELICAN achieves the highest success rate (86.8%) and overall score (4.39), and the human results are directionally consistent with GPT-based evaluations (e.g., R_coverage: 70.04 human vs. 72.36 GPT), providing cross-validation between automated and human judgments.

- **Cognitive-level stratified analysis supports adaptation claims.** Table 5 shows low-cognitive students achieve 75% success rate with only a 7.5 percentage-point gap from high-cognitive students (82.5%), while average dialogue rounds decrease sensibly with ability (9.00 → 8.10 → 6.97). Figure 4 shows interpretable strategy distributions (analogies at 22% for low-level vs. 15% for high-level students), demonstrating non-random, level-appropriate strategy selection.

- **Clean ablation and backbone studies.** Table 3 isolates component contributions: removing cognitive diagnosis drops R_coverage from 54.84 to 47.76; removing slow thinking drops Suitability from 4.17 to 4.00. Table 4 demonstrates the framework functions across four different backbone models (Llama-3.1-8B, GLM-4-PLUS, Qwen-max, GPT-4o), supporting generalizability.

## Weaknesses

### Fatal

None.

### Major

- **Abstract claims cannot be verified from the paper body.** The abstract states "+18.7%" improvement on "critical thinking stimulation" and "+22.4%" on "task completion rates." These specific percentages cannot be traced to any metric in Tables 1–6. The closest metrics — Inspiration (a GPT-based 1–5 rating) and success rate — yield different percentage improvements against any baseline. For instance, Inspiration for PELICAN (4.21) vs. Free-Prompt (2.42) yields ~74% relative improvement, and vs. Socratic (3.99) yields ~5.5%. Success rate in the human evaluation (Table 6) shows PELICAN at 86.8% vs. Free-Prompt at 85.2% — a negligible gap. The headline quantitative claims are the paper's most prominent assertions and must be traceable to specific results. This undermines credibility.

- **Unexplained large discrepancy between Tables 2 and 3 for PELICAN.** PELICAN's R_coverage is 72.36 in Table 2 but 54.84 in Table 3 — a 24% relative drop for the same method on ostensibly the same metric. Other scores also shift (e.g., Suitability: 4.27 → 4.17; Reliability: 4.51 → 4.44). No explanation is provided for why the ablation experiments use a different configuration or data subset. Without this explanation, the reader cannot reconcile the two tables, which undermines confidence in both sets of results.

- **Main evaluation relies on LLM-simulated students without bounding simulation fidelity.** The results in Tables 1–5 come from one LLM (GPT-4o as teacher) interacting with another LLM (as student), with the student role design relegated to a stripped appendix. The human evaluation (Table 6, 169 students) covers only the tutoring stage — not cognitive diagnosis — and uses different subjective metrics (Appropriateness, Sentiment rather than Suitability, Logic), preventing direct cross-validation of the main results. While LLM-simulated evaluation is a pragmatic choice, the paper's central claims about personalized education for human students need the simulation's fidelity to be transparently bounded.

- **GPT-based evaluation is circular.** The tutoring stage is evaluated using GPT-based scores on five dimensions (Suitability, Logic, Inspiration, Reliability, Overall), but the system itself is GPT-4o. Using the same model family to evaluate its own outputs creates a self-assessment concern, particularly for subjective dimensions like "Inspiration" (used as a proxy for critical thinking). The human evaluation partially mitigates this by showing directional consistency, but uses different dimensions (Appropriateness, Sentiment), so it does not directly validate the GPT-based scores used in the main results.

### Minor

- **M=1 makes fast thinking nearly vestigial.** Slow thinking activates after M=1 rounds (line 278), meaning fast thinking is used exactly once per sub-task before slow thinking takes over. Yet the paper presents this as a meaningful dual-system design. The paper should acknowledge that slow thinking dominates the tutoring process in practice.

- **Counterintuitive Inspiration result in ablation not discussed.** In Table 3, the "w/o. Diagnosis & slow" ablation scores Inspiration at 4.56, which is higher than full PELICAN (4.30). The paper claims removing components degrades performance, yet this GPT-based metric improves when both are removed. This anomaly deserves discussion.

- **Small dataset (184 math questions).** The paper draws conclusions about personalized education broadly, but the Gaokao dataset contains only 184 high school math questions. This is a narrow evidential base, particularly for the conclusion's reference to "students across various subjects" (line 442).

- **Human evaluation success rate gaps are small and lack statistical testing.** In Table 6, PELICAN's success rate (86.8%) is only marginally higher than Free-Prompt (85.2%) and Stepwise (86.5%). No confidence intervals or significance tests are reported for these comparisons, making it unclear whether the observed differences are meaningful.

- **Conclusion overclaims subject coverage.** Line 442 states PELICAN serves "students across various subjects," but only math questions were used in experiments.

- **No limitations section.** The paper lacks a dedicated limitations section. Key limitations include the simulation-based evaluation, circular GPT evaluation, small dataset, high token cost (~580K per interaction, with ~40% for slow thinking), and math-only scope.

### Trivial

- The abstract contains "Code is available at [here](#)" with a placeholder link — this should be a real URL in the final version.

## Nice-to-Haves

- Cross-validate GPT-based evaluation scores against human judgments on a shared subset using the same dimensions (Suitability, Logic, etc.) to directly assess the circularity concern.
- Report variance/confidence intervals for the human evaluation success rates and conduct statistical significance tests between methods.
- Discuss the counterintuitive Inspiration result in the ablation and investigate whether it reflects a genuine effect or noise in the GPT-based metric.
- Expand the dataset beyond math to support the "various subjects" claim, or narrow the claim to math.

## Removed Points

These points are flagged to be removed, treat them with caution.

- **Harsh Critic: "Thin related work (Section 2)."** REMOVED per rules — DO NOT mention missing related works. The paper cites relevant work; evaluating completeness of literature review is outside scope.

- **Harsh Critic: "Under-specified methods (knowledge point extraction, validator mechanism, tutoring strategy definitions)."** REMOVED per rules — these details are deferred to the stripped appendix (Appendices B, E) and exist in the original submission. The parser strips those sections; these are not author errors.

- **Harsh Critic: "Joint ablation conflates two components."** PARTIALLY REMOVED — the paper actually reports individual ablations (w/o. Diagnosis, w/o. slow) alongside the joint ablation in Table 3, so this specific criticism is factually incorrect. The counterintuitive Inspiration result is retained as a Minor weakness.

- **Harsh Critic: "The expert-assistant-verifier pipeline assumes agreement between two LLMs implies correctness."** REMOVED — this is a methodological choice the paper explicitly describes and motivates (line 196: "if two experienced individuals provide the same answer to a question, the answer is likely correct"). Criticizing this as an "undefended assumption" without evidence that it fails in practice is speculative. The No-Pipeline ablation in Table 1 (93.08 F1 vs. 94.31) provides empirical evidence the pipeline helps.

- **Harsh Critic: "Abstract link broken."** REMOVED — parser/formatting artifact, not an author error.

- **Harsh Critic: "No-Pipeline baseline F1 gap (~1.2 points) is small and unreported variance."** REMOVED — this is speculative; the paper does report the numbers clearly.

- **Strength Finder: "This paper addresses a genuine and important problem."** REMOVED — generic, not specific to this paper's contributions.

- **Harsh Critic: "Introduction overstates gap in literature (line 106)."** REMOVED — this is a framing judgment call, not a substantive error. The paper does cite existing LLM tutoring work in Section 2.1.

## Novel Insights

The paper's integration of hierarchical knowledge structures (successor-first diagnosis) with tree-search-based strategy selection (Simulated Teaching Tree) is a genuinely novel architectural contribution for LLM-based tutoring. Unlike prior work that treats diagnosis and tutoring as separate problems or uses single-step strategy prompts, PELICAN connects them through a shared cognitive state representation that is dynamically updated during tutoring. The Simulated Teaching Tree (Equations 3–5) formalizes what effective human tutors do intuitively — anticipate how a student will respond to different teaching moves — and the cognitive-level-stratified strategy distribution (Figure 4, e.g., analogies at 22% for low-level vs. 15% for high-level students) provides concrete evidence that this formalization produces pedagogically sensible behavior rather than collapsing to a single dominant strategy.

## Suggestions

- Trace every headline claim in the abstract to a specific row and column in a specific table. If the +18.7% and +22.4% claims come from comparisons not visible in the main body, either add those comparisons explicitly or revise the abstract to use verifiable numbers.
- Add a clear statement in Section 4.3 explaining what differs between the Table 2 and Table 3 experimental setups (subset size, selection criteria, parameter differences) and why the PELICAN R_coverage drops from 72.36 to 54.84.
- Add a limitations section acknowledging the key constraints of this work.
- Report statistical significance for the human evaluation comparisons in Table 6.

## Calibration Anchors Referenced

| Anchor | Avg Score | Round | Comparison to PELICAN |
|---|---|---|---|
| DFCD (iucVyVC8jQ) — Cognitive Diagnosis Framework | 3.25 | R1 | PELICAN is clearly stronger: more complete system (diagnosis + tutoring), human evaluation, cleaner ablations |
| DSA (whXHZIaRVB) — Dynamic Skill Adaptation | 4.00 | R1 | PELICAN is stronger: more complete system, human study, better experimental rigor |
| Students Rather Than Experts (BzvVaj78Jv) | 5.00 | R1/R2 | Very comparable: similar ambition and evaluation weaknesses. PELICAN has more sophisticated technical design but has abstract credibility issues |
| TestAgent (lXwhR7uci1) | 4.75 | R2 | PELICAN is better: more complete system, cleaner ablations, larger human evaluation |
| KCQRL (M4fhjfGAsZ) | 5.33 | R2 | KCQRL is slightly stronger: broader empirical validation (15 KT models), no credibility issues. PELICAN more ambitious but has significant presentation gaps |
| CogMath (x1nlO1d1iG) | 4.33 | R2 | PELICAN is stronger: builds a system rather than just a benchmark |
| AI-Assisted Math Questions (M1CCA6UF0y) | 4.25 | R2 | PELICAN is stronger: more complete contribution, human evaluation |


MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>