## Summary

AetherCode is a competitive programming benchmark that sources 456 problems exclusively from premier contests worldwide (IOI, ICPC series, USACO, CCPC), targeting a higher difficulty ceiling than existing platforms like LeetCode/Codeforces-centric benchmarks. Its main technical contribution is a hybrid test-case construction pipeline — a Generator-Validator (G-V) agent system augmented by 67 expert annotators — that achieves 100% TPR and 100% TNR on a corpus of 30,000+ human submissions. The paper also provides a comprehensive evaluation of 17 models (11 reasoning, 6 non-reasoning) across difficulty, algorithm category, and Pass@N metrics.

---

## Strengths

- **Novel problem source.** Sourcing problems from premier offline competitions (IOI, ICPC World Finals, NOI, regional championships) is genuinely distinct from every prior benchmark, which draws overwhelmingly from online judges. These competitions enforce richer problem-design space (multi-file implementations, week-long contest durations, complex data structures), yielding problems qualitatively different from Codeforces rounds.

- **Principled test-case quality framework.** Reframing the test suite as a binary classifier and reporting TPR/TNR against a large labeled solution corpus (≥5 correct, ≥20 incorrect per problem, 30,000+ total) is more principled than mere count-based metrics. The G-V agent achieving 89.9% TNR, and the expert annotation layer closing the remaining gap, is a concrete and credible methodology.

- **Unusually rigorous expert validation.** The curation involves 67 CP experts (majority CF >2000, some >2600 International Grandmasters) for test case generation, plus an elite audit team holding ICPC gold medals with problem-setting experience. Few benchmarks approach this level of domain-expert involvement.

- **Comprehensive evaluation.** Testing 17 frontier models across difficulty bands, 10 algorithmic categories, Pass@1/2/4, and failure-mode decomposition (Wrong Answer / TLE / Runtime Error / Compile Error) provides genuine diagnostic value. The finding that even o4-mini-high solves only 35.5% Pass@1 is a meaningful empirical contribution.

- **Self-contained, open-source test cases.** Unlike CodeELO and LiveCodeBench Pro (which rely on Codeforces's judging API, raising compliance concerns and frequency limits), AetherCode ships its own test suites, enabling flexible offline evaluation.

---

## Weaknesses

### Fatal
None.

### Major

1. **Circularity of the 100% TNR claim.** The 100% TNR is measured exclusively on the *collected* set of incorrect submissions; it says nothing about incorrect solutions not in this corpus. The paper acknowledges this risk for problems with fewer than 50 incorrect solutions but does not report how many such problems exist or how much expert intervention was required to compensate. The central quality guarantee is therefore conditional on corpus completeness, which is opaque to readers.

2. **Absent decontamination analysis.** The paper flags temporal metadata as enabling "decontamination," but Section 3 presents no decontamination procedure or contamination analysis. All 456 problems are from 2024–2025, yet several models evaluated were trained on data potentially overlapping this window. Without contamination controls, it is unclear whether the leaderboard reflects generalization or partial memorization, which is a core validity concern for any benchmark paper.

3. **Severe OI/ICPC imbalance (76 vs. 380 problems).** ICPC problems differ structurally from OI problems (team vs. individual, time pressure per problem, implementation style). With 83% of problems from ICPC, the benchmark substantially under-represents OI-style problems despite IOI being a stated motivation. This limits claims about "premier programming competitions worldwide."

### Minor

1. **Expert annotation quantity not reported.** Section 2.3.3 describes expert annotation but never reports how many test cases experts added, or for what fraction of problems the G-V agent's 89.9% TNR was insufficient. This information is necessary to assess the practical importance of the expert stage.

2. **Pass@4 analysis overfits small N.** Conclusions about "exploration potential" and "diversity" drawn from comparing Pass@1 to Pass@4 (with 4 samples per problem) are statistically thin. Pass@4 with 4 total draws is a noisy estimator, and the 11.1% improvement for o4-mini-high vs. 7.6% for Qwen3-32B may reflect sampling variance rather than a meaningful behavioral difference.

3. **Human difficulty vs. LLM difficulty not analyzed quantitatively.** The paper explicitly acknowledges that human difficulty may not map to LLM difficulty, but presents no analysis of this discordance (e.g., correlation coefficients, or examples where LLMs do better/worse than human rankings predict). This limits the diagnostic utility of the difficulty labels.

### Trivial

- Table 3 contains apparent typos: "Ssed-1.6-Thinking-0715" and "Claude-4-Sonnet-nothingking."

---

## Nice-to-Haves

- A quantitative contamination analysis (e.g., n-gram overlap between problem statements and known training corpora) would substantially strengthen validity claims.
- Reporting the fraction of problems requiring expert intervention to reach 100% TNR would clarify how dependent the benchmark is on expert labor vs. the automated pipeline.
- A Spearman correlation between human difficulty rank and LLM solve rate would make the difficulty labels more actionable for benchmark users.

---

## Novel Insights

The most genuinely novel insight is the framing of test-suite quality as a binary classification problem with explicit TPR/TNR metrics validated against a large labeled solution corpus, rather than treating quantity as a proxy for quality. This is a clean and actionable framework that could be adopted by future benchmark papers. A secondary insight is the failure-mode observation that Claude models disproportionately produce TLE errors (roughly 50% of failures) compared to other models (~20–30%), suggesting these models preferentially commit to correct-but-inefficient algorithms rather than incorrect-but-fast ones — a qualitatively distinct failure mode worth investigating in future work.

---

## Suggestions

- Report the number of problems for which expert annotation was required (i.e., where G-V TNR < 100%) and how many test cases experts contributed on average.
- Provide decontamination details: date cutoffs applied per model, and any evidence that results are stable on the most recent (post-training-cutoff) subset.
- Consider reporting the OI and ICPC sub-benchmarks separately in the main results table to make the source imbalance transparent to users.

---

## Score and Decision

AetherCode addresses a real and well-motivated gap: existing code benchmarks are saturated and sourced from a narrow set of platforms. The hybrid test-case construction pipeline is methodologically sound and unusually well-validated. The core weaknesses — circular TNR guarantee, absent decontamination analysis, OI/ICPC imbalance — are real but do not invalidate the contribution. The benchmark provides genuine discriminative power (top models at ~35% Pass@1), comprehensive algorithmic coverage, and open-source test cases. These collectively represent meaningful value to the community.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>