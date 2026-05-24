Now I have a thorough understanding of the paper. Let me produce the final consolidated review.

## Summary

This paper re-analyzes four lines of evidence from the high-profile ICLR 2025 Oral paper on min-p sampling (Nguyen et al., 2024) and demonstrates that the original claims are invalidated by its own data. The re-analysis covers human evaluations (where one-third of data was omitted and statistical tests were applied incorrectly), NLP benchmarks (where a novel Best-of-N analysis controlling for hyperparameter volume shows min-p does not outperform), LLM-as-a-Judge evaluations (where methodology was under-specified and results appear selectively reported), and community adoption claims (which were unsubstantiated and retracted). From this case study, the paper derives six actionable lessons for more rigorous empirical ML research.

## Strengths

- **Novel Best-of-N analysis for fair hyperparameter comparison (Section 3.1, Figures 4–5):** The paper introduces a principled method to equalize the volume of hyperparameter tuning across samplers, directly addressing a common cherry-picking problem. This is a methodological contribution that extends beyond this case study and is convincingly demonstrated across 9 models × 2 stages × 4 samplers × 31 temperatures × 6 hyperparameters × 3 seeds (~6000 A100-hours).

- **Rigorous statistical re-analysis exposing multiple errors in the original human evaluation (Section 2, Table 1):** The discovery that the original paper omitted one-third of collected human evaluation data without justification is a clear smoking gun. The paper's correct re-analysis (one-sided paired t-tests with Bonferroni correction across 12 comparisons, plus an Intersection-Union Test) shows that only 1 of 12 comparisons survives correction — directly invalidating the original claim of "consistent" superiority.

- **Identification of selective reporting in LLM-as-a-Judge results (Section 4.3):** The paper documents that the original reported the higher of two scores for min-p (p=0.05 → 52.01%) but the lower of two for top-p (p=0.9 → 50.07%), while omitting the higher top-p value (p=0.98 → 50.43%). This is a concrete, verifiable instance of inconsistent reporting that favored the proposed method.

- **Manual annotation of qualitative feedback contradicting the original summary (Section 2.3, Figure 2):** The paper manually annotated and visualized human evaluators' qualitative responses, showing that Basic sampling was preferred by 21 evaluators vs. only 12 for min-p — directly contradicting the original paper's narrative. The annotations are publicly posted.

- **Demonstration that community-adoption claims were unsubstantiated and retracted (Section 5):** The paper shows that the combined GitHub stars of major LM repositories (453k) are less than half the claimed 1.1M stars for min-p alone, and notes that 3 of 4 ICLR reviewers cited this retracted claim as justification for acceptance.

- **Clear articulation of six actionable lessons grounded in concrete evidence:** Each lesson (fair hyperparameter comparison, correct statistical testing, data transparency, scrutiny of qualitative summaries, methodological clarity, avoidance of selective reporting) is directly motivated by the preceding analysis, providing a reusable blueprint.

## Weaknesses

### Fatal
None.

### Major
None. The paper's core claims are well-supported by its evidence.

### Minor

- **NLP benchmarks limited to GSM8K CoT (Section 3):** The original paper also evaluated on GPQA, but the present paper's sweep covers only GSM8K CoT due to compute budget (~6000 A100-hours). While this is a practical constraint and the paper is transparent about it, readers cannot assess whether min-p might show different patterns on the other benchmark. This does not undermine the critique of the original paper's GSM8K claims, but it slightly limits the scope of the negative result.

- **Statistical tests use t-tests on ordinal data (Section 2, Table 1):** The human evaluation scores are on a 2–10 ordinal scale, and paired t-tests assume interval-level measurement. The violations of normality are unlikely to reverse the clear pattern (only 1/12 comparisons survive Bonferroni correction), but the paper does not discuss this assumption or report a non-parametric sensitivity check.

- **Corrected NLP results reported only in appendix (Section 3.1):** After the original authors noted a prompt-formatting bug, the paper re-ran experiments and states results were "nearly identical" with one exception (2 of 12 models). Showing the corrected results alongside the original in the main text would strengthen transparency, especially given the original authors' own admission of a bug.

- **LLM-as-a-Judge analysis lacks formal statistical testing for win-rate differences (Section 4):** The paper visualizes 95% confidence intervals (Figure 6) but does not conduct explicit bootstrapped significance tests for whether win rates differ from chance or from each other. This would modestly strengthen the argument.

### Trivial
None.

## Nice-to-Haves

- The Best-of-N analysis could also report median (not just maximum) differences to give a fuller picture of typical performance.
- A brief quantitative re-analysis showing how the original paper's reported test statistics would change under correct statistical practices would sharpen the lesson about statistical rigor.
- Reporting inter-annotator agreement for the qualitative response coding would strengthen the annotation methodology.

## Removed Points

These points are flagged to be removed; treat them with caution:

- **"Lessons not novel in isolation"** — Removed because the paper's contribution is the concrete demonstration through a case study, which gives these well-known principles evidentiary weight. A critique of a case study for not being novel in its abstract lessons misunderstands the genre.
- **"Does not address min-p being genuinely useful on other tasks"** — Removed because the paper explicitly acknowledges this as a limitation ("new evidence might lead to different conclusions") and carefully scopes its claims.
- **"Could have reported agreement among annotators for qualitative coding"** — Demoted to nice-to-have; the annotations are publicly available and the core pattern is clear without this.
- **"Raw qualitative annotations should be in main text"** — Removed because Figure 2 visualizes the annotated categories and counts in the main text; the raw data is publicly posted.
- **"Some readers might wish for additional benchmarks beyond GSM8K"** — This is acknowledged as a compute-budget limitation and is inherent to the case study scope.

## Novel Insights

The paper's central contribution is not in any single finding but in demonstrating how several well-known methodological failure modes (omitted data, improper pooling, selective reporting, unsubstantiated claims) compounded within a single high-profile paper, each amplifying the others. The most novel concrete insight is the Best-of-N analysis as a methodological tool: by subsampling equal numbers of hyperparameter configurations across methods and tracking how maximum performance grows with search budget, the paper provides a general-purpose diagnostic for detecting whether a method's reported superiority is genuine or an artifact of more extensive tuning. This is a practical contribution that could become standard practice in method comparison papers.

## Suggestions

- Report a non-parametric sensitivity check (e.g., Mann-Whitney U) for the human evaluation comparisons to address the ordinal-scale concern.
- Include the corrected NLP prompt-formatting results in the main text alongside the original results for full transparency.
- Consider adding a brief worked example showing how the original paper's single pooled t-test would change under correct statistical practice (multiple-comparison correction), to sharpen Lesson 2.

## Score and Decision

**MY FINAL SCORE: <score>6.5</score>**
**MY FINAL DECISION: <decision>Accept</decision>**

### Calibration Report

**Round 1 — Bracketing.** Three queries for re-analysis / methodological-critique papers:

| Band | Anchor | Avg Score | Round | Comparison |
|------|--------|-----------|-------|------------|
| Low (<3.5) | x8mr9zGkpr — "Attributing Model Behavior" | 3.00 | R1 | Much weaker; limited analysis, unclear contribution. Current paper is far stronger. |
| Low (<3.5) | 2wwPG1wpsu — "LST-Bench" | 2.50 | R1 | Benchmark paper with weak methodology. Not comparable. |
| Low (<3.5) | aoW5Sm8Op8 — "Benchmarking Survival Models" | 2.33 | R1 | Weak analysis with limited scope. Not comparable. |
| Low (<3.5) | u8L1zzGXRq — "Molecular Representations" | 3.00 | R1 | Limited contribution benchmark analysis. Not comparable. |
| Middle (3.5–7.5) | GbEmJmnQCz — "Is Memorization Actually Necessary for Generalization?" | 4.40 | R1 | **Most comparable anchor.** A re-analysis paper debunking published claims. The current paper is notably stronger: more thorough evidence across four lines, novel Best-of-N methodology, clearer writing, and more actionable lessons. |
| Middle (3.5–7.5) | lf8QQ2KMgv — "Is Memorization Actually Necessary for Generalization?" (variant) | 3.75 | R1 | Same re-analysis, different review population. Similar assessment: current paper is substantially stronger. |
| Middle (3.5–7.5) | X8aFMdXk3N — "Ensuring Fair Comparisons in TSF" | 4.25 | R1 | Dataset quality critique paper. Comparable in genre but narrower in scope. Current paper is more thorough and provides a novel method (Best-of-N). |
| Middle (3.5–7.5) | RW37MMrNAi — "Class-wise Autoencoders" | 5.60 | R1 | Method paper, less directly comparable. Current paper is similarly strong within its genre. |
| High (>7.5) | EUSkm2sVJ6 — "Quantitative Data Usage Inference" | 7.60 | R1 | Strong method paper with novel algorithm. Higher technical contribution, different genre. |
| High (>7.5) | PdaPky8MUn — "Never Train from Scratch" | 8.00 | R1 | Strong empirical paper showing fair comparison methodology. Different genre but shares the "fair comparison" theme. Current paper is less technically novel. |

**Round-1 bracket:** The paper clearly sits in the 4.5–7.0 range, well above the re-analysis anchors at 3.75–4.40 but below the 7.5+ method contributions.

**Round 2 — Narrowing (4.5–7.0).** Searched for similar re-analysis and methodology critique papers:

| Anchor | Avg Score | Round | Comparison |
|--------|-----------|-------|------------|
| icTZCUbtD6 — "Dissecting Sample Hardness" | 6.20 | R2 | Method/benchmark paper with taxonomy contribution. Similar score range but different genre. Current paper is comparably rigorous. |
| 9nUBh4V6SA — "Hierarchically Encapsulated Representation" | 6.50 | R2 | Applied ML paper. Current paper is similarly well-executed but in a different genre (critique vs. method). |
| vyflgpwfJW — "DiscoveryBench" | 7.00 | R2 | Benchmark paper with large-scale contribution. Higher novelty in creating a new benchmark, but current paper's methodological contribution (Best-of-N) is also novel. |
| kz5igjl04W — "Approaching an unknown communication system" | 5.50 | R2 | Different genre (interpretability). Current paper is stronger. |
| bwZ9xh178a — "Exploiting Negative Samples" | 6.00 | R2 | Healthcare analytics method paper. Different genre. |

**Final calibration:** The paper is clearly stronger than the most directly comparable re-analysis papers (the "Memorization" papers at 3.75–4.40) — its evidence is more thorough, its novel Best-of-N analysis is a genuine methodological contribution, and its lessons are more actionable. It is comparable in quality to papers scoring 6.0–6.5, though it operates in a genre (position/re-analysis) that typically receives lower scores than method papers. I place it at **6.5** — well-executed, important, and accepted.