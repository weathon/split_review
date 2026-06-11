## Summary

This paper is a systematic re-analysis of a high-profile ICLR 2025 Oral paper on min-p sampling (Nguyen et al., 2024). It re-examines four lines of evidence from the original paper (human evaluations, NLP benchmarks, LLM-as-a-Judge evaluations, and community adoption claims) and demonstrates that the original paper's own data and methodology do not support its central claims. It also contributes a Best-of-N methodology for controlling hyperparameter tuning volume in empirical comparisons. The paper derives six general lessons for rigorous ML research, each concretely anchored to a specific failure uncovered in the case study.

## Strengths

1. **Best-of-N hyperparameter control methodology (Section 3.1, Figures 4–5):** The paper develops a principled method — subsampling equal numbers of hyperparameters across samplers and comparing best achievable scores, repeated 150 times — that controls for the confound of unequal hyperparameter tuning. This is a genuinely reusable methodological tool that goes beyond the specific case study.

2. **Comprehensive, multi-model benchmark re-evaluation (Section 3.1, ~6000 A100-hours):** The GSM8K sweep covers 9 model families (Qwen 2.5, Mistral, Llama, Gemma), 2 model stages (base and instruct), 4 samplers, 31 temperatures, 6 hyperparameters per sampler, and 3 random seeds. This far exceeds the original evaluation and provides convincing evidence that min-p's apparent advantage disappears when tuning volume is equalized.

3. **Correct statistical re-analysis of human evaluations (Sections 2.2–2.3, Table 1, Figures 1–2):** The discovery that 1/3 of the human evaluation data (basic sampling scores) was omitted is a clear and important finding. The re-analysis with Bonferroni correction and the Intersection-Union Test shows that only 1 of 12 comparisons survives correction at α=0.05 (0 of 12 at α=0.01), and the IUT for "consistent" outperformance fails entirely (largest p-value = 0.378). Manual annotation of qualitative responses further contradicts the original paper's characterization of human preferences.

4. **Verification and documentation of retracted community adoption claims (Section 5):** The paper demonstrates that the claimed 54k GitHub repositories and 1.1M stars are impossible (the sum of all major LM repositories is 453k stars), documents that the authors retracted both numbers from the camera-ready, and notes that 3 of 4 reviewers and the AC cited these unsubstantiated numbers as justification for acceptance — a striking finding about the review process.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

1. **NLP benchmark analysis covers only GSM8K, not GPQA.** The paper states (Line 150) that the sweep was limited to GSM8K CoT due to compute budget. This means one of the original paper's two benchmark claims was not independently re-examined. The paper acknowledges this limitation candidly, and the central argument about hyperparameter tuning volume is cleanly demonstrated on GSM8K alone, so this narrows the scope of the benchmark evidence but does not undermine the core contribution.

2. **Paired t-tests on ordinal Likert-type data (Table 1).** The re-analysis uses one-sided paired t-tests on scores from an ordinal rating scale (2–10). Strictly speaking, a t-test assumes normally distributed interval data, while Likert-type items are ordinal. While this is standard practice in NLP/ML and the Central Limit Theorem provides some cover at n=53, the paper's own emphasis on rigorous statistical methodology makes this a minor inconsistency. A non-parametric alternative (e.g., permutation test) would close this vulnerability. The paper's main conclusions are robust to this concern — the overlapping confidence intervals in Figure 1 and the Intersection-Union Test are less affected.

3. **Selective reporting claim (Section 4.3) rests on thin evidence.** The allegation that the original paper reported the higher of two scores for min-p but the lower for top-p is based on a Telegram link shared by the first author — not an independently verifiable archival source. The broader critique of the LLM-as-a-Judge evaluations (unequal tuning volume, methodological underspecification, indirect comparison design) is independently sufficient to raise serious concerns about this line of evidence. This specific claim would benefit from stronger documentation or should be de-emphasized.

### Trivial
None.

## Nice-to-Haves

- Include effect sizes (e.g., Cohen's d) alongside p-values in the human evaluation re-analysis to complement the significance tests.
- Develop the Best-of-N methodology further with a discussion of its assumptions (e.g., uniform subsampling) and a sensitivity analysis on subsample size and hyperparameter range choices.
- Consider a non-parametric alternative to the t-tests (permutation test or Mann-Whitney U) for the ordinal human evaluation scores to eliminate the methodological inconsistency.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **"Echo chamber" complaint about references citing Schaeffer et al.:** Removed as a style/substance nitpick that does not affect the paper's validity.
- **"Blueprint framing overpromises":** Removed as a subjective framing preference; the paper delivers 6 specific, evidence-anchored lessons plus a new methodology, which constitutes a reasonable blueprint.
- **"Paper should include author response opportunity":** Removed because the paper already documents multiple interactions with the original authors (Lines 35, 64, 165), including confirmations of data omissions and prompt formatting corrections.
- **"No effect sizes":** Demoted to nice-to-have; the paper already provides confidence intervals and p-values that are sufficient for its conclusions.
- **"Best-of-N needs theoretical discussion":** Demoted to nice-to-have; the methodology is clearly described and applied, and further development would strengthen but is not necessary.
- **"Harsh critic's criticism about Strengthening the Paper on Its Own Terms":** These suggestions (developing Best-of-N more, tightening blueprint alignment) are constructive but reclassified as nice-to-haves since they go beyond what is needed for the paper's core contribution.

## Novel Insights

None beyond the paper's own contributions. The paper's insight is its demonstration of how multiple converging methodological errors in a single high-profile paper produce unsupported claims, paired with a reusable tool for detecting one class of those errors.

## Suggestions

- Replace the paired t-tests on ordinal human evaluation scores with a non-parametric alternative (permutation test or Mann-Whitney U) to fully align with the paper's own rigorous standards.
- Find archival evidence for the selective reporting claim in Section 4.3, or de-emphasize it in favor of the more robustly documented unequal-tuning critique (Section 4.2), which independently undermines the LLM-as-a-Judge evidence.
- Add a brief sensitivity analysis for the Best-of-N method (e.g., varying the number of subsamples N or the range of hyperparameters) to strengthen it as a standalone methodological contribution.

## Score and Decision

**Calibration Report:**

Round 1 (bracketing) — three queries for "re-analysis case study of existing paper, replication, reproducibility critique" across score bands:

| Path | Avg Score | Round | Comparison |
|------|-----------|-------|------------|
| `CpiOUOaqh3.md` | 2.00 | 1 | Parameter optimization paper; much weaker, not comparable genre |
| `FYvZCwdb6F.md` | 3.00 | 1 | Social bias paper; not comparable |
| `SaOxhcDCM3.md` | 3.20 | 1 | Self-consuming training loop; somewhat related but less systematic critique |
| `51cjeYcXjs.md` | 2.50 | 1 | Malware paper; not comparable |
| `GbEmJmnQCz.md` | 4.40 | 1 | **"Is Memorization Actually Necessary?"** — direct re-analysis critique paper. The current paper is substantially stronger: more comprehensive experiments, novel methodological tool, clearer conclusions |
| `lf8QQ2KMgv.md` | 3.75 | 1 | Same topic as above, another version. Current paper stronger on all dimensions |
| `50P9TDPEsh.md` | 4.67 | 1 | Critique ability of LLMs; different type of critique paper |
| `Xr5iINA3zU.md` | 5.75 | 1 | Collapse or Thrive? — more of a new analysis than a critique |
| `cNmu0hZ4CL.md` | 8.00 | 1 | Neural population dynamics; not comparable |
| `Xo0Q1N7CGk.md` | 8.00 | 1 | Grid cells; not comparable |
| `agPpmEgf8C.md` | 8.00 | 1 | RL auxiliary objectives; not comparable |
| `et5l9qPUhm.md` | 8.00 | 1 | Strong Model Collapse — theory-heavy paper with strong theoretical results; different genre from case-study critique |

Round 1 bracket: The paper clearly sits above the 3.75–4.40 memorization critique papers and well below the 8.0 theory papers. Narrowest plausible range: **4.5–7.5**.

Round 2 (narrowing) — three queries within the (5.0, 7.0) band:

| Path | Avg Score | Round | Comparison |
|------|-----------|-------|------------|
| `g16vmAtJ8x.md` | 6.00 | 2 | "Inadequacy of Similarity-based Privacy Metrics" — critique paper with new attack method. Current paper is more comprehensive and better organized |
| `3jXCF5dNpC.md` | 6.00 | 2 | Re-reading improves reasoning; different genre |
| `fXJCqdUSVG.md` | 6.50 | 2 | **"On Evaluating Durability of Safeguards for Open-Weight LLMs"** — critique/replication case study paper accepted at ICLR. Very similar genre and structure. Current paper is comparably strong: more comprehensive experiments, a novel methodological contribution (Best-of-N) that the safeguards paper lacks, and similarly actionable lessons |
| `Zr96FfaUGR.md` | 5.50 | 2 | ARIES dataset paper; different genre |
| `55EO8gSCBT.md` | 5.50 | 2 | Experimental design for nonstationary optimization; tangentially related |
| `Q2bJ2qgcP1.md` | 6.00 | 2 | CATE benchmark; different genre |
| `icTZCUbtD6.md` | 6.20 | 2 | Sample hardness analysis; different genre |
| `X0epAjg0hd.md` | 5.67 | 2 | **"Reassessing How to Compare and Improve Calibration"** — accepted critique/reassessment paper. Current paper is more comprehensive (single dataset vs. 9 models × 4 samplers) and has a clearer methodological contribution |
| `PCXvcULwiI.md` | 5.50 | 2 | Benchmarking structural inference; different genre |
| `0ApkwFlCxq.md` | 6.25 | 2 | Epigenetic aging clocks benchmark; different genre |
| `HBf6HFnpmH.md` | 5.50 | 2 | Scalability of causal models; different genre |
| `ox2ATRM90I.md` | 6.20 | 2 | ICU benchmark framework; different genre |

Round 2 refinement: The current paper is most comparable to the safeguards critique paper (6.50, accepted) and somewhat stronger than the privacy metrics critique (6.00, rejected) and the calibration reassessment (5.67, accepted). It has a clearer novel methodology than any of these, with more comprehensive experiments. Score: **6.5**.

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>