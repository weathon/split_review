Now I'll write the final synthesized review.

## Final Review

**Bracket determination:**

Round 1 bracket: Between 3.5 and 5.5. The paper is substantially stronger than EDU-RAG (2.33) and Dual-Fusion CD (3.25), but has verifiable issues that prevent it from reaching the quality of papers scoring 5+.

Round 2 narrowing: Compared against anchors at 4.00 (Adaptive Testing for LLMs), 5.00 (Students Rather Than Experts), and 5.33 (Automated KC Annotation). PELICAN has a more coherent framework and stronger human evaluation than the 4.00 anchor, but has more serious evidential issues (numerical discrepancy, untraceable abstract claims) than the 5.00 and 5.33 anchors. 

Final score: **4.0**. The paper proposes a well-motivated architecture and includes a genuine human evaluation, but is held back by an unexplained ~17-point numerical discrepancy between its main results and ablation tables, and abstract claims that cannot be verified from the reported data.

---

## Summary

PELICAN proposes a two-stage adaptive tutoring framework: (1) collaborative cognitive diagnosis using a successor-first strategy with an expert-assistant-verifier pipeline to model a student's knowledge state, followed by (2) adaptive tutoring that selects teaching strategies from a pool, using a dual-system (fast/slow thinking) approach where slow thinking activates a simulated teaching tree search when students face difficulties. Evaluation is conducted on the Gaokao dataset with simulated students, supplemented by a human study with 169 real high school students.

## Strengths

- **Two-stage architecture is coherent and well-motivated.** The framework cleanly separates cognitive diagnosis from adaptive tutoring, with each stage having a clear purpose. The successor-first diagnostic strategy leverages knowledge-point dependencies efficiently, and the fast/slow thinking division for strategy selection is conceptually sound.

- **Expert-Assistant-Verifier pipeline is validated by ablation.** Table 1 shows that removing this quality-control mechanism drops diagnostic F1 from 94.31 to 93.08 (No-Pipeline), providing concrete evidence that the consistency check improves diagnostic accuracy.

- **Human evaluation with 169 real high school students (1,335 tutoring reports).** Section 4.6 and Table 6 provide genuine real-world evidence with strong ethical protocols (informed consent, anonymization, teacher supervision). PELICAN achieves the highest success rate (86.8%), R_coverage (70.04), and human-rated scores across all five dimensions.

- **Success-rate analysis across cognitive levels.** Table 5 provides granular evidence that even low-cognitive-level students achieve a 75% success rate (only 7.5% below high-level students), with appropriate reduction in tutoring rounds (9.00 → 6.97), supporting the claim of effective adaptation.

## Weaknesses

### Major

- **Unexplained numerical discrepancy between Table 2 and Tables 3/4.** In Table 2 (main results), PELICAN achieves R_coverage = 72.36 and F_frequency = 72.06. In Table 3 (module ablation), PELICAN achieves R_coverage = 54.84 and Frequency = 61.47. In Table 4 (backbone ablation), "Ours(GPT-4o)" again shows R_coverage = 54.84 and Frequency = 61.47. The same method under the same name differs by ~17.5 points on R_coverage with no explanation in the paper. The standard deviations in Table 2 (±4.69 for R_coverage) do not account for this gap. Until this is resolved, confidence in all quantitative claims is undermined. (Verifiable from lines 298–306 vs lines 316–321 vs lines 327–332.)

- **Abstract claims (+18.7%, +22.4%) cannot be traced to any metric in the paper.** The abstract states: "significant improvements in critical thinking stimulation (+18.7%) and task completion rates (+22.4%) compared to baseline models." These precise percentages do not correspond to any metric or comparison presented in the body. The closest proxy—Inspiration in Table 2—shows PELICAN at 4.21 vs the best baseline at 3.99 (~5.5% relative), and Success Rate in Table 6 is 86.8% vs 85.2% for Free-Prompt (~1.9% relative). These numbers appear only in the abstract and are never referenced again.

### Minor

- **M=1 threshold undermines the dual-system framing.** Slow thinking (the computationally expensive simulated teaching tree) activates after just 1 dialogue round on each sub-task (line 278). With this threshold, the system resorts to the tree-search approach from nearly the start of every sub-task. The "fast thinking" component that embodies the dual-system analogy is used for at most one round before being replaced. The method is better characterized as a tree-search strategy selector than as a dual-system approach. (Verifiable from lines 224, 278.)

- **Strategy distribution shows suspicious uniformity across cognitive levels.** In Figure 4/table (lines 342–353), 7 out of 9 strategies show *identical percentages* across all three cognitive levels (e.g., Suggestion 2% everywhere, Confirmation 5%, Correction 8%, Open Question 5%, Closed Question 5%, Simplification 10%, Decomposition 12%). Only Explanation (30–33%) and Analogies (15–22%) vary. If the system genuinely adapts strategies to cognitive levels, one would expect more variation. This either reflects low statistical power, aggregation artifacts, or limited actual adaptation.

- **Main experiments use LLM-simulated students, not real ones.** The paper's primary results (Tables 1–5) evaluate the system's ability to tutor an LLM-based simulated student (Appendix G). This is a fundamentally different setting from real tutoring. While the human evaluation (Table 6) partly addresses this, the paper's strongest quantitative claims are based on the simulated setting.

- **GPT-as-judge confound.** The tutoring system is built on GPT-4o (line 278), and the GPT-based evaluation metrics (Suitability, Logicity, Inspiration, Reliability, Overall) are also rated by GPT-4o (Section 4.1). LLMs tend to rate their own outputs or structurally similar outputs more favorably. No calibration or human-baseline comparison is provided for these ratings.

- **No outcome-based learning metrics.** The paper measures process metrics (R_coverage, F_frequency—whether the teacher addresses non-mastered knowledge points) and subjective quality ratings, but never measures actual learning gains (e.g., pre/post test performance). A system could score well on coverage without improving student learning.

### Trivial

None.

## Nice-to-Haves

- Comparison or discussion of the simulated teaching tree's relationship to Monte Carlo Tree Search (MCTS), which is structurally similar.
- Ablation with larger M values to demonstrate when fast thinking suffices and to validate the dual-system framing.
- Full statistical testing (p-values, effect sizes) in the main body rather than deferred to an appendix.

## Removed Points

These points are flagged as removed—treat them with caution:

- **"Human evaluation results are nearly identical to baselines"** (Harsh Critic). PELICAN's human eval R_coverage (70.04) substantially beats Socratic (63.91) and all other baselines. The claim of "near identity" is not accurate.
- **"Slow thinking consumes 40% of tokens, suggesting pervasive use"** (Harsh Critic). 40% of tokens means 60% are still fast thinking. This is substantial but does not support the "pervasive" characterization.
- **"Strategy distribution shows questioning strategies increase for higher-level students"** (Strength Finder). The data shows Open Question and Closed Question are both exactly 5% across all three cognitive levels. This claimed pattern does not exist in the data.
- **Missing comparison with MCTS / missing related works** (Harsh Critic). These are either not verifiable or not central flaws.
- **Formatting/style nitpicks and complaints about stripped appendix content** (Harsh Critic). Parser artifacts and missing appendix sections affect all papers equally.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. **Explain or correct the Table 2 vs Table 3/4 discrepancy.** This is the single most important thing the authors need to address. If different experimental conditions or subsets were used, state this explicitly. If the numbers are corrected, present the corrected tables.

2. **Substantiate or remove the abstract's +18.7%/+22.4% claims.** Map these to specific metrics, baselines, and tables, or remove the numbers.

3. **Run an ablation with larger M values** (e.g., M=3, M=5) to demonstrate the conditions under which fast thinking suffices and validate the dual-system framing.

4. **Add a learning-outcome metric** (pre/post test) to at least the human evaluation, even if on a subset of students.

## Score and Decision

**Calibration anchors (all rounds):**

| Anchor | Avg Score | Round | Comparison |
|--------|-----------|-------|------------|
| EDU-RAG (a2rSx6t4EV) | 2.33 | R1 | Much weaker: simple benchmark, minimal novelty |
| Dual-Fusion CD (iucVyVC8jQ) | 3.25 | R1 | Weaker: less evaluation, limited innovation |
| Adaptive Testing for LLMs (s6X3s3rBPW) | 4.00 | R1 | Comparable quality but different type of issues |
| GAOKAO-Eval (1tZLONFMjm) | 4.00 | R2 | Different focus (benchmarking vs tutoring), similar quality |
| Students Rather Than Experts (BzvVaj78Jv) | 5.00 | R1 | Stronger in novelty, weaker in human eval depth |
| Automated KC Annotation (M4fhjfGAsZ) | 5.33 | R2 | Stronger: cleaner evaluation, no numerical discrepancies |
| TestAgent (lXwhR7uci1) | 4.75 | R2 | Comparable quality |
| MathGAP (5ck9PIrTpH) | 7.00 | R1 | Much stronger: rigorous evaluation methodology |
| Reliable Amortized Eval (mIl15VP7vt) | 6.50 | R1 | Much stronger |

**Round 1 bracket:** 3.5–5.5 (paper is clearly above 3.25 anchors but below 5.33 anchors).

**Round 2 narrowing:** Compared against GAOKAO-Eval (4.00), Students Rather Than Experts (5.00), Automated KC Annotation (5.33), and TestAgent (4.75). PELICAN has a more practical contribution and stronger human evaluation than the 4.00 anchors, but the numerical discrepancy and untraceable abstract claims are more serious issues than those in the 5.00-range papers. The paper sits between 4.00 and 5.00 anchors, closer to the 4.00 side due to the verifiable evidential problems.

MY FINAL SCORE: <score>4.0</score>
MY FINAL DECISION: <decision>Reject</decision>