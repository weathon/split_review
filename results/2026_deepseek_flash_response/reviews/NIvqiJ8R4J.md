## Summary

PELICAN proposes a two-stage LLM-based tutoring framework that first diagnoses a student's cognitive state via collaborative cognitive diagnosis (successor-first questioning with an expert-assistant-verifier pipeline), then selects tutoring strategies using a fast/slow thinking mechanism where slow thinking constructs a simulated teaching tree for lookahead planning. Evaluated on the Gaokao dataset with both simulated and real human experiments.

## Strengths

1. **Cognitive diagnosis is demonstrably effective (Table 1).** PELICAN achieves 94.31 F1 in only 5.83 average rounds, substantially outperforming Free-Prompt (74.18 F1, 7.21 rounds) and CoT (79.83 F1, 8.79 rounds). The No-Pipeline ablation (93.08 F1) confirms the verifier contributes, and the successor-first ordering reduces rounds vs. S-Independent (90.70 F1, 6.17 rounds). These are clean, well-controlled results.

2. **Slow-thinking ablation provides causal evidence (Table 3).** Removing slow thinking drops R_coverage from 54.84→49.44 and Suitability from 4.17→4.00, isolating the contribution of the lookahead simulation from the strategy pool. This directly supports the paper's central claim about the dual-system approach.

3. **Real human evaluation with 169 high school students (Section 4.6, Table 6).** A genuine human-in-the-loop study with 1,335 tutoring reports. PELICAN leads on R_coverage (70.04 vs. next-best Socratic at 63.91) and scores highest on all five human-rated dimensions. This is meaningful validation beyond automated metrics.

4. **Backbone-agnostic performance (Table 4).** The framework generalizes across four LLMs (Llama3.1-8B, GLM-4-PLUS, Qwen-max, GPT-4o), showing the system design, not just the base model, contributes to gains.

## Weaknesses

### Major

1. **Abstract headline claims (+18.7% / +22.4%) are completely untraceable.** The abstract asserts "significant improvements in critical thinking stimulation (+18.7%) and task completion rates (+22.4%)." These numbers appear *nowhere* in any result table. The closest available metrics are Inspiration in Table 2 (PELICAN 4.21 vs. best baseline 3.99 = ~+5.5%) and Success Rate in Table 6 (PELICAN 86.8% vs. best baseline 86.5% = ~+0.3%). The paper does not define "critical thinking stimulation" or "task completion rates" as operational metrics. These claims are unsupported by the presented data. This is a serious reporting integrity issue — a paper cannot make bottom-line quantitative claims that are not traceable to specific measurements.

2. **Unexplained numerical discrepancy between Table 2 and Table 3.** PELICAN's R_coverage is reported as **72.36** in Table 2 (main results) but as **54.84** in Table 3 (ablation) — a ~17-point difference for the same method on the same metric. Table 4 (backbone ablation) also reports 54.84 for GPT-4o, consistent with Table 3. The paper provides no explanation for why Table 2 values are so different. This undermines the interpretability of both the main results and the ablations: if the evaluation conditions differ across tables, the comparisons within each table may not be meaningful, and if they don't differ, the numbers should be consistent.

3. **Main experiments rely on LLM-simulated students without acknowledging limitations.** The slow-thinking simulation uses Φ_Sim_S (Eq. 4) to generate student responses, and the cognitive-level analysis initializes simulated students with different levels. The paper references "Design details of the student role (Appendix G)" but never explicitly states in the main text that the core evaluations (Tables 1, 2, 4, 5) use an LLM playing the student — nor does it discuss the limitations of this closed-loop evaluation (LLM teacher → LLM student → LLM judge). GPT-rated quality metrics in this setting conflate tutoring quality with the judge's stylistic preferences, and LLMs are known to exhibit self-enhancement biases. The paper's central empirical claims about effectiveness are therefore based on a paradigm whose validity is not established.

### Minor

4. **Human evaluation gains over the strongest baseline are marginal for the primary metric.** PELICAN's success rate (86.8%) is only 0.3% above Sepwise (86.5%). No confidence intervals or significance tests appear in the main text (ANOVA analysis is in the stripped appendix). The R_coverage advantage is substantial (70.04 vs. 63.91), but the paper's most interpretable outcome metric shows at best a tiny improvement that may not be statistically significant.

5. **Most strategies show zero variation across cognitive levels (Figure 4).** Seven of nine strategies (Suggestion, Confirmation, Correction, Open Question, Closed Question, Simplification, Decomposition) are used at *exactly the same rate* across all three cognitive levels. Only Explanation (32/33/30%) and Analogies (22/18/15%) vary. This substantially weakens the claim that the system adapts its tutoring to the diagnosed cognitive state — the adaptation appears limited to only two strategies.

6. **Naming inconsistency: "Sepwise" vs. "Stepwise."** The baseline is "Stepwise" in Table 2 and Section 4.1 but "Sepwise" in Table 6 and Figure 5. While likely a typo, this indicates editorial carelessness that matters when interpreting cross-table comparisons.

### Trivial

7. **No sensitivity analysis for key hyperparameters.** M=1 (slow thinking activates after one round), k=2, m=2, λ=0.4 are presented without any analysis of how they affect results. With a tree depth of 2 and branching factor 2, the "search" is extremely shallow, yet slow thinking consumes ~40% of the token budget (~230k tokens). Whether this cost is justified cannot be assessed without sensitivity analysis.

8. **Knowledge hierarchy construction is not described.** The paper says "we begin by extracting the relevant points from each problem" but does not explain how this hierarchical structure is built. This is critical for reproducibility and for understanding the method's scalability.

## Nice-to-Haves

- Pre/post testing in the human evaluation to measure learning gain rather than success rate during a single interaction
- Sensitivity analysis on M, k, m, and λ to demonstrate robustness
- Human agreement study on the GPT-based evaluation dimensions
- Validation of the simulated student's behavior against real student responses

## Removed Points

- **"The paper doesn't define abbreviations like Cot"** — Removed: Section 4.1 lists baselines and references Appendix D.2 for details; standard practice.
- **"Ten strategies only described in appendix"** — Removed: Deferring a long strategy list to an appendix is normal.
- **"Missing related works"** — Removed per system rules.
- **"Formatting/style nitpicks"** — Removed per system rules (parser artifacts).
- **"Strength: strategy distribution shows genuine adaptation"** — Removed: the strength finder's claim is contradicted by the data itself (7 of 9 strategies show zero variation).
- **"Slow thinking is activated too early (M=1)"** — Demoted to trivial: this is a design choice, not an error; the paper simply lacks sensitivity analysis.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. **Correct or remove the untraceable abstract numbers.** Every quantitative claim in the abstract must be directly traceable to a specific operational metric, table, and baseline. Currently +18.7%/+22.4% cannot be connected to any reported result.
2. **Reconcile the Table 2 vs. Table 3 discrepancy.** If these are from different evaluation conditions, state the conditions explicitly. If they should be the same, correct the error.
3. **Acknowledge the simulated-student evaluation paradigm explicitly** in the main text and discuss its limitations, including LLM self-enhancement bias in GPT-rated metrics.
4. **Add confidence intervals or significance tests** for the human evaluation's primary metrics in the main text (not just a deferred appendix).
5. **Discuss the strategy uniformity** in Figure 4 — the fact that 7/9 strategies are identical across levels should be acknowledged as a limitation rather than presented as evidence of adaptation.

## Score and Decision

**Calibration anchors (all rounds):**

| Path | Avg Score | Round | Comparison |
|------|-----------|-------|------------|
| `iucVyVC8jQ.md` (Dual-Fusion CDM) | 3.25 | R1 | Weaker than PELICAN — no human evaluation, not directly comparable |
| `dp1BH2bK4Y.md` (Re-TASK) | 3.00 | R1 | Weaker — different domain |
| `a2rSx6t4EV.md` (EDU-RAG) | 2.33 | R1 | Weaker — simpler benchmark paper |
| `whXHZIaRVB.md` (Dynamic Skill Adaptation) | 4.00 | R1 | Comparable — has methodology issues but no reporting integrity problems |
| `s6X3s3rBPW.md` (Adaptive Testing) | 4.00 | R1 | Comparable — similar mixed reviews on evaluation paradigm |
| `BzvVaj78Jv.md` (SOE/LVSA Student Sim.) | 5.00 | R1 | Slightly stronger — similar human evaluation but fewer integrity issues |
| `M4fhjfGAsZ.md` (Auto KC Annotation) | 5.33 | R1 | Slightly stronger — cleaner evaluation |
| `lXwhR7uci1.md` (TestAgent) | 4.75 | R2 | Slightly stronger — similar method and human eval, but has fewer reporting integrity issues |
| `NgaLU2fP5D.md` (PSI-KT) | 6.75 | R2 | Much stronger — accepted, methodologically rigorous |
| `x1nlO1d1iG.md` (CogMath) | 4.33 | R2 | Slightly stronger — cleaner evaluation |
| `ma4SUzeCLR.md` (Problematic Q Detection) | 5.33 | R2 | Different sub-area |

**Bracketing**: Round 1 placed PELICAN between 3.5 and 5.5. Round 2 narrowed this by comparing against TestAgent (4.75, reject) and PSI-KT (6.75, accept). PELICAN is weaker than TestAgent because it has specific reporting integrity problems (untraceable abstract numbers, table inconsistency) that TestAgent does not, despite similar human-evaluation strengths. PELICAN is clearly weaker than PSI-KT, which was accepted for its rigorous methodology and clean evaluation.

**Final score**: 3.5 — The paper has genuine methodological contributions (successor-first cognitive diagnosis, dual-system strategy selection, real human evaluation), but two serious reporting issues (untraceable abstract claims, unexplained table discrepancy) prevent the reviewer from accepting the empirical claims at face value. The combination of an unevaluated evaluation paradigm (LLM-in-a-loop) with untraceable headline numbers and internally inconsistent results means the paper does not currently support its advertised claims.

MY FINAL SCORE: <score>3.5</score>
MY FINAL DECISION: <decision>Reject</decision>