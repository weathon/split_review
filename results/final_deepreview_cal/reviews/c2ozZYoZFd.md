Now I have enough information to synthesize the final review. Here is my consolidated assessment:

---

## Summary
This paper conducts a meticulous re-examination of Nguyen et al. (2024), an ICLR 2025 Oral paper that introduced `min-p` sampling. Through re-analysis across four lines of evidence — human evaluations, NLP benchmarks, LLM-as-a-Judge evaluations, and community adoption claims — the authors demonstrate that the original paper's own data invalidate its central claim that `min-p` consistently outperforms baselines. The paper additionally contributes a novel "Best-of-N" methodology for fairly comparing methods while controlling for hyperparameter tuning volume, and distills six general lessons for rigorous empirical ML research.

## Strengths
- **Discovery of omitted human evaluation data (Section 2.1):** The paper reveals that one-third of the collected human ratings (the *basic* sampler) were excluded from the original analysis without mention or justification. When restored, the data show human evaluators preferred *basic* more than *min-p*, and corrected statistical tests (Bonferroni correction, IUT) no longer support the original "consistently outperforms" claim (Table 1).

- **Rigorous NLP benchmark sweep with novel Best-of-N methodology (Section 3.1):** The extensive GSM8K hyperparameter sweep across 9 models, 3 seeds, 6 hyperparameters per sampler, and 31 temperatures uses a novel Best-of-N analysis to equalize hyperparameter tuning effort. Figures 4 and 5 convincingly show that `min-p`'s performance advantage vanishes when hyperparameter volume is controlled — a methodological contribution that generalizes beyond this case study.

- **Exposure of unsubstantiated and retracted community-adoption claims (Section 5):** The paper traces back the original manuscript's claim of 54K GitHub repositories and 1.1M stars, finds them unsupportable, and documents that the authors subsequently retracted both numbers. The paper further notes that 3 of 4 ICLR reviewers and the Area Chair cited these numbers as justification for their endorsement.

- **Correct statistical practice demonstrated as a worked example (Section 2.2–2.3):** The re-analysis applies Bonferroni correction, Intersection-Union Tests, and proper visualization with 95% confidence intervals, serving as a teachable demonstration of how incorrect pooling and multiple-comparison neglect can produce false conclusions in human evaluation studies.

- **Clear, well-structured presentation:** The paper is organized around four independent lines of evidence, each systematically dismantled, with conclusions that directly support the six distilled lessons. Figures are informative and well-designed.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor
- **Selective-reporting claim in LLM-as-a-Judge section relies on an unarchived Telegram link (Section 4.3):** The paper claims that the original Table 3(b) reported the higher of two `min-p` scores but the lower of two `top-p` scores, citing a Telegram link shared by the first author. The link content is not archived or independently verifiable in the paper. The broader critique of that section — unequal hyperparameter tuning (~2× more for `min-p`), underspecified methodology, and small win-rate differences — stands without this claim, but the selective-reporting allegation carries a different weight and should be either substantiated with permanent evidence or softened.

- **NLP benchmark scope limited to GSM8K:** The abstract states that sweeps on "NLP benchmarks" (plural) demonstrate `min-p`'s superiority vanishes, but the analysis is conducted only on GSM8K. The paper acknowledges this compute limitation in Section 3.1 and includes a prompt-formatting rerun as a robustness check, and the limitation is honestly noted in Section 6. The abstract should be more precisely scoped to GSM8K to match what is demonstrated.

### Trivial
- **No formal statistical test on the new human evaluation study (Section 2.4):** The analysis of the authors' second human experiment relies on visual inspection of Figure 3 without a formal hypothesis test. Given that the paper's own rigorous re-analysis of the original data already carries the argument, and that this second study is the original authors' follow-up experiment, the absence of a test here is not a meaningful gap — figures suffice to show no advantage for `min-p`. Nevertheless, applying the same statistical standard here would improve consistency.

## Nice-to-Haves
- Expanding the NLP Best-of-N analysis to at least one additional benchmark (e.g., GPQA) would strengthen the generality of the conclusion beyond GSM8K, though the compute requirement (~6000 A100-hours already spent) makes this a substantial ask.
- A brief discussion of how the identified flaws (pooled tests, omitted data) might be caught during peer review — beyond the general lessons already provided — would add practical value for reviewers.
- Archiving the evidence for the selective-reporting claim in Section 4.3 with permanently accessible documentation.

## Removed Points
These points were flagged by reviewers but are removed from the final review:

- **"The selective-reporting allegation could call the fairness of the whole section into question"** — Overstated. The section's other findings (unequal tuning, underspecified methodology) are independently verifiable; the Telegram-based claim is a supporting detail, not the section's foundation. Retained as Minor with appropriate scoping.

- **"The evidence should be made publicly permanent or the claim should be softened"** — Retained in substance but reclassified from Major to Minor. The paper would not collapse without this claim.

- **"The NLP conclusion overstates generality"** — Retained as Minor but demoted from the harsh critic's "Critical Issue" framing. The paper acknowledges the limitation in the body; only the abstract needs scoping.

- **"No formal statistical test on the new human evaluation"** — Retained as Trivial rather than Minor. The visual evidence is adequate for critiquing someone else's follow-up experiment, and the paper's core argument rests on its own re-analysis.

- **"The introduction's list of scandals could be shortened"** — Removed as a style preference.

- **"The lessons are mostly restatements of known best practices"** — Removed. The novelty is in the detailed demonstration and the Best-of-N technique, which the paper foregrounds. Critiquing a paper for not inventing new best practices while it explicitly positions itself as a blueprint/case study is scope creep.

- **"The LLM-as-a-Judge section's indirect comparison design criticism is problematic because LLM-judge preferences are not transitive"** — This is actually a valid point the paper makes (citing Xu et al., 2025). Removed the criticism about this criticism.

## Novel Insights
The paper's Best-of-N methodology for controlling hyperparameter tuning volume is genuinely novel and broadly applicable beyond this specific case. The insight that a method's apparent superiority across benchmarks can be an artifact of unequal hyperparameter search — and that subsampling-based "Best-of-N" curves can detect this — is a contribution that other empirical researchers can adopt. The paper also provides a uniquely thorough worked example of how omitted data, pooled statistical tests, and selective reporting can combine to create a misleading picture of superiority, even in a highly-reviewed venue paper.

## Suggestions
- Revise the abstract to say "Extensive hyperparameter sweeps on GSM8K" rather than "on NLP benchmarks" to precisely reflect what was demonstrated.
- Either archive the Telegram evidence for the selective-reporting claim (Section 4.3) with exact values and a clear statement of the inconsistency, or reframe that point as a tentative observation and shift weight to the independently verifiable unequal hyperparameter tuning finding.
- Consider adding error bars or confidence intervals to Figure 3 for completeness.

---

**Calibration anchors consulted:**

| Anchor | Path | Avg Score | Round | Comparison to this paper |
|---|---|---|---|---|
| Attributing Model Behavior | x8mr9zGkpr | 3.00 | R1 | Much weaker; narrow empirical scope with unclear contributions |
| Test Relative Fairness | tqHgSxRwiK | 3.00 | R1 | Not comparable; different domain and contribution type |
| Is Memorization Necessary (v1) | GbEmJmnQCz | 4.40 | R1 | Similar re-examination genre but weaker: narrower scope, disputed methodology, rejected |
| Is Memorization Necessary (v2) | lf8QQ2KMgv | 3.75 | R1 | Similar but rejected; less thorough than current paper |
| Curvature-Based Rewiring Revisited | EcrdmRT99M | 5.75 | R1 | Closest genre match; accepted. Current paper is broader (4 evidence lines vs 2), has novel methodology (Best-of-N), and more impactful findings |
| Rethinking Graph Classification | om5z1n0mXA | 6.00 | R1 | Rejected despite 6.0 avg; different type (benchmarking framework) |
| Hyperparameter Loss Landscapes | PlZIXgfWPH | 5.75 | R2 | Related topic (hyperparameter analysis) but less focused; rejected |
| CATE Benchmark | Q2bJ2qgcP1 | 6.00 | R2 | Large-scale critique accepted at 6.0; current paper is more impactful with dramatic findings |
| Beyond Correlation (LLM-as-Judge) | E8gYIrbP00 | 6.75 | R2 | Most comparable anchor: accepted at 6.75, human eval + LLM-judge methodology critique. Current paper is broader (4 evidence lines), more impactful findings, and better presented |
| WildBench | MKEHCx25xp | 7.33 | R2 | Strong benchmark paper; more resource-intensive but different genre |
| MLE-Bench | 6s5uXNWGIh | 8.00 | R1 | Top-tier benchmark construction; not directly comparable |

**Round 1 bracket:** 5.5–7.5 (between the curvature rewiring paper at 5.75 and strong benchmark papers at 7.5+).  
**Round 2 narrowing:** The "Beyond Correlation" paper (6.75) is the most comparable — also accepted and also critiques evaluation methodology with human and LLM-judge components. The current paper exceeds it in breadth (four independent lines of evidence), impact of findings (data omission, retracted claims), and clarity. It is weaker than the 7.33–8.0 anchors which represent major benchmark construction efforts with broader standalone contributions.  
**Final score:** 7.0 — above the best comparable critique paper (6.75) but below major benchmark/methodology papers (7.3+) that introduce broadly adopted resources. The minor weaknesses (abstract scope, Telegram evidence) prevent a higher score but do not undermine the core contribution.

MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>