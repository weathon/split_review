Now let me produce the final review.

## Summary

This paper provides a methodological blueprint for rigorous empirical ML research through a detailed case study of a high-profile ICLR 2025 Oral paper on min-p sampling. It systematically re-examines the original paper's four lines of evidence (human evaluations, NLP benchmarks, LLM-as-a-Judge evaluations, community adoption) and demonstrates that none support the claimed superiority of min-p. The paper introduces a "Best-of-N" hyperparameter control methodology and derives six generalizable lessons for researchers and reviewers.

## Strengths

- **Novel Best-of-N hyperparameter control methodology (Section 3.1, Figures 4 & 5):** A principled method for comparing sampling methods by equalizing the volume of hyperparameter tuning across contenders. Demonstrated across 9 models, 2 model stages, 31 temperatures, 6 hyperparameters per sampler, and 3 seeds (~6000 A100-hours). The figures convincingly show min-p does not outperform baselines when tuning volume is controlled. This methodology is reusable beyond this case study.

- **Exposure of omitted human evaluation data (Section 2.1):** Discovered that 1/3 of collected human evaluation data was excluded without justification. When the omitted data (basic sampling scores) are included, the conclusions change. The paper correctly credits that the original authors added this data to the Camera Ready but did not update their conclusions — a clear demonstration of why data transparency matters.

- **Corrected statistical analysis with multiple comparison correction (Section 2.2, Table 1):** Shows that the original paper's claim of "consistent" superiority was based on pooling data across conditions and omitting correction for multiple comparisons. Applying Bonferroni correction and an Intersection-Union Test reveals that only 1 of 12 comparisons survives correction at α=0.05, and 0 of 12 at α=0.01. This is a crisp, reproducible demonstration of a common statistical error.

- **Independent annotation of qualitative responses (Section 2.3, Figure 2):** Manual re-coding of the original participants' free-text preferences shows basic sampling was preferred over min-p (21 vs. 12 evaluators), directly contradicting the original paper's characterization. The annotations are publicly posted.

- **Verification via new human evaluation study (Section 2.4, Figure 3):** The original authors' own new experiment (run after receiving feedback, with corrected hyperparameters and methodology) again shows min-p offers no advantage — the scatter plot shows all samplers clustered together. This is a powerful triangulation.

- **Documentation of unsubstantiated community adoption claims (Section 5):** Traces how the original paper's claims of "54,000 GitHub repositories and 1.1 million stars" were retracted after the current authors showed they could not be substantiated. Critically, the paper documents that 3 of 4 ICLR reviewers and the Area Chair cited these numbers as the main justification for their endorsement — a significant observation about reviewing practices.

## Weaknesses

### Major

- **NLP benchmark re-analysis covers only GSM8K (Section 3):** The original paper evaluated on both GSM8K and GPQA. The current paper's conclusion that "min-p does not outperform other samplers" is based solely on GSM8K. The authors acknowledge this limitation due to compute budget (~6000 A100-hours), but this means the refutation of the original paper's NLP benchmark claims is incomplete. The paper would be stronger with a smaller-scale GPQA replication (e.g., a subset of models or hyperparameter settings).

- **Human evaluation re-analysis restricted to the "high" diversity setting (Section 2):** The authors justify this by noting the original authors called the low-diversity setting "quite experimental" and changed the top-p hyperparameter from 0.1 to 0.9 in their new study. While this justification is reasonable, the original claim was made "consistently across all settings." A complete refutation would strengthen the paper by also showing results in the low-diversity setting with appropriate corrections, or explicitly testing whether the low-diversity results drive the original claim.

### Minor

- **Selective reporting allegation in Section 4.3 relies on a Telegram link as primary evidence:** The claim that the original paper reported the higher of two win rates for min-p (52.01 vs. 50.14) but the lower for top-p (50.07 vs. 50.43) is supported only by referencing a Telegram link shared by the first author. The paper should tabulate the actual win rates from the original authors' public repository across all reported hyperparameter settings and show which ones were selected for Table 3(b). The numerical values are stated in the paper, which helps, but the provenance would benefit from being more directly verifiable.

- **No formal hypothesis tests on the Best-of-N sweep results (Section 3.1):** The Best-of-N plots (Figures 4 & 5) show mean differences with what appear to be error bars, but no formal statistical test (e.g., signed-rank test across model configurations or permutation test for cherry-picking) quantifies the evidence. Adding something like "across 16 model configurations, min-p was the best sampler in X of Y cases" would strengthen the quantitative conclusion.

- **Models in NLP sweeps are at or below 9B parameters:** The original paper may have used different model scales. This doesn't invalidate the analysis (the sweep is extensive and systematic), but it limits generalization to larger-scale models where sampling dynamics may differ.

### Trivial

- The paper's six lessons in the Discussion are sound but some (e.g., "correct for multiple comparisons") are standard practice in other fields. The value is in the concrete demonstration rather than the principles themselves.

## Nice-to-Haves

- Connect the Best-of-N analysis directly to the original paper's specific hyperparameter choices via a bootstrap or permutation test that estimates how often the original paper's results would arise by chance under equal tuning.
- Condense the six lessons into a more actionable pre-submission checklist or review rubric format.
- Add a signed-rank test across model configurations in the Best-of-N analysis.

## Removed Points

These points are flagged for removal; treat them with caution:

- **"Introduction name-dropping criticism"**: The harsh critic's claim that the list of scandals (12 citations in one sentence) "weakens the motivational punch" is a stylistic preference, not a substantive weakness. The list of citations is context-appropriate for establishing the "crisis of rigor" framing.
- **"Paper lacks independent human evaluation"**: This is inaccurate — Section 2.4 presents the original authors' new human evaluation, which the current paper visualizes and analyzes. The critique is that the paper doesn't re-collect human judgments, but re-analyzing the original paper's data (including a new study run by the original authors) is methodologically valid for the paper's claims.
- **"Selective reporting claim is hearsay"**: The paper enumerates the specific win rates numerically (Section 4.3), not just referencing a link. The values are stated: min-p at p=0.05 gets 52.01 vs. p=0.01 gets 50.14; top-p at p=0.9 gets 50.07 vs. p=0.98 gets 50.43. The weakness is that the provenance could be more robust, not that it's absent.
- **Generic strengths from Strength Finder about "importance of the problem"**: Removed as not specific enough.
- **Missing related works**: Cannot be verified without external sources; removed per instruction.

## Novel Insights

Beyond the paper's own contributions, a notable pattern emerges across the reviews: the original paper's justifications shifted retroactively. The low-diversity setting was described as "quite experimental" only after the current authors raised concerns; the community adoption numbers were retracted only after they were shown to be unverifiable; the omitted basic-sampler data was added only after it was discovered. This pattern of post-hoc scope narrowing and data supplementation — where the boundaries of a claim are adjusted to preserve it after flaws are exposed — is itself a generalizable warning sign that deserves attention from reviewers and program committees.

## Suggestions

1. **Strengthen the selective reporting evidence in Section 4.3:** Add a table listing all win rates from the original authors' public GitHub repository for both min-p and top-p across all hyperparameter settings, with clear marking of which value was reported in Table 3(b) of the original paper. This would turn a plausible claim into a verified result.

2. **Add a formal hypothesis test to the Best-of-N analysis:** A signed-rank test comparing min-p's maximum score against the best non-min-p sampler across model configurations would provide a crisp quantitative summary.

3. **Acknowledge the GSM8K-only limitation more prominently** in the abstract and conclusion, and consider a smaller-scale GPQA replication (e.g., on a subset of models or hyperparameters) if feasible.

4. **Consider condensing the six lessons** into 3-4 more actionable guidelines paired with a short pre-submission checklist, which would increase the paper's practical impact.

## Score and Decision

**Calibration Anchors (all rounds):**

| Paper Path | Avg Score | Round | Comparison |
|---|---|---|---|
| `/home/wg25r/split_review_opus_repro/datasets/deepreview_13k_calibration/x8mr9zGkpr.md` | 3.00 | R1 | Unrelated; much weaker contribution |
| `/home/wg25r/split_review_opus_repro/datasets/deepreview_13k_calibration/hv8l922Ad7.md` | 3.40 | R1 | Correcting flaws in disentanglement metrics; similar genre (methodological critique) but narrower scope and less experimental depth |
| `/home/wg25r/split_review_opus_repro/datasets/deepreview_13k_calibration/kiwyQsZIGP.md` | 5.00 | R1 | Evaluating the Evaluators (FSL); similar meta-evaluation genre but less comprehensive evidence |
| `/home/wg25r/split_review_opus_repro/datasets/deepreview_13k_calibration/JrfWj5Ae1j.md` | 5.33 | R1 | Discrimination testing case studies; similar case-study structure but shallower experiments |
| `/home/wg25r/split_review_opus_repro/datasets/deepreview_13k_calibration/E8gYIrbP00.md` | 6.75 | R2 | Beyond Correlation (human uncertainty in evaluation); similar rigor but narrower contribution — the present paper is stronger on breadth and actionable output |
| `/home/wg25r/split_review_opus_repro/datasets/deepreview_13k_calibration/tr0KidwPLc.md` | 7.33 | R2 | LLMBar (evaluating LLM evaluators); similar execution quality — the present paper has a larger experimental footprint but less novel benchmark contribution |
| `/home/wg25r/split_review_opus_repro/datasets/deepreview_13k_calibration/TlAdgeoDTo.md` | 7.25 | R2 | First-Person Fairness; similar case-study-driven methodological contribution but focused on fairness rather than evaluation rigor |
| `/home/wg25r/split_review_opus_repro/datasets/deepreview_13k_calibration/jOmk0uS1hl.md` | 8.00 | R1 | Training on the Test Task; cleaner, more novel central concept with unanimous 8s — the present paper has more acknowledged limitations |
| `/home/wg25r/split_review_opus_repro/datasets/deepreview_13k_calibration/Im2neAMlre.md` | 7.33 | R2 | One slice is not enough (T2I evaluation); similar methodological contribution level |

**Round 1 Bracket:** 5.5–7.5 (clearly above weak-anchor band, below the 8.0 unanimous-accept band)

**Round 2 Narrowing:** Compared against anchors at 6.75 (Beyond Correlation), 7.33 (LLMBar), 7.25 (First-Person Fairness), 7.33 (One slice is not enough). The paper is stronger than Beyond Correlation (6.75) due to greater breadth of evidence and an actionable methodological blueprint. It is comparable to LLMBar (7.33) in execution quality, though that paper contributes a reusable benchmark while this paper contributes a reusable methodology (Best-of-N) plus a case study. Both are accept-level contributions with identifiable limitations.

**Final Score:** 7.0 — A well-executed, comprehensive methodological critique that makes both empirical and methodological contributions. The Best-of-N analysis is a genuine methodological innovation, the human evaluation re-analysis is definitive, and the six lessons are well-grounded in evidence. The limitations (GSM8K-only NLP sweep, selective reporting evidence thinness, high-diversity focus) are real but do not undermine the central conclusion.

MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>