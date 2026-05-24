Now I have a solid calibration picture. Let me summarize what I've found:

**Round 1 Bracket**: The paper sits clearly above "Is Memorization Actually Necessary for Generalization?" (3.75, a narrower re-examination with methodological gaps) and plausibly in the 5.5–7.5 range.

**Round 2 Narrowing**: 
- "Evaluating the Quality of Hallucination Benchmarks" (5.50): an audit-of-benchmarks paper criticized for limited novelty. Our paper is stronger — more rigorous, more impactful findings, and develops novel methodology.
- "One slice is not enough" (7.33): a rigorous evaluation methodology paper with large-scale annotations and a new metric. Stronger than our paper — contributes new artifacts, not just critique.
- "FFB: A Fair Fairness Benchmark" (6.75): comparable in methodological rigor but contributes a new benchmark.

Our paper sits in the **6.0–6.5 range**. Let me now write the final consolidated review.

---

Now, let me compile the final review, applying all the filtering rules.

**Verification of Harsh Critic weaknesses:**

1. **Abstract overstates NLP benchmark scope** — VERIFIED. The abstract says "NLP benchmarks" (plural) but only GSM8K was evaluated. The paper explicitly states "Due to our compute budget, we only evaluated GSM8K CoT." KEEP as a Minor weakness.

2. **Lack of formal statistical tests on new human evaluation data** — VERIFIED. Section 2.4 relies on Fig. 3 without formal testing. KEEP as a Minor weakness (the original data already has rigorous testing; this is supplementary).

3. **Section 4.3 lacks quantitative comparison** — INCORRECT. The paper does provide specific numbers (52.01 vs 50.14 for min-p; 50.07 vs 50.43 for top-p). REMOVE this criticism.

**Verification of Strength Finder strengths:**
All seem well-grounded and supported by the paper. I'll keep them but consolidate.

**Applying filtering rules:**

- The Harsh Critic's "Section 4.3 lacks elaboration" — REMOVED (factually wrong; the paper does provide numbers)
- The critique about missing GPQA — the paper explicitly acknowledges this limitation. The abstract overstatement is the real issue, not the omission of GPQA.
- The "strengthening suggestions" about adding formal tests to new human eval, revising abstract, and reporting both win rates numerically — these are already partially addressed (win rates are reported). The abstract revision and formal test suggestions are good nice-to-haves.

Let me now write the final review.Now let me write the final consolidated review.

---

## Summary

This paper conducts a meticulous re-examination of "Turning Up the Heat: MIN-P Sampling for Creative and Coherent LLM Outputs" (Nguyen et al., 2024), an ICLR 2025 Oral paper. Through re-analysis of the original paper's own data across four lines of evidence — human evaluations, NLP benchmarks, LLM-as-a-Judge evaluations, and community adoption claims — the authors demonstrate that the original claims of `min-p`'s superiority are not supported. The paper further distills six actionable lessons for rigorous empirical ML research, grounded in the specific errors uncovered.

## Strengths

- **Rigorous statistical re-analysis of human evaluations reverses the original conclusions**: The paper discovers that one-third of the original human evaluation data (basic sampler scores) was omitted without justification. Using the complete data with proper one-sided paired t-tests and Bonferroni correction across 12 comparisons (Table 1), the paper shows evidence for `min-p` superiority in at most 1 of 12 comparisons at α = 0.05, directly refuting the original claim of consistent outperformance. The Intersection-Union Test further confirms insufficient evidence.

- **Novel "Best-of-N" hyperparameter sweep methodology for fair comparison**: The paper develops a controlled methodology that equalizes hyperparameter tuning volume across samplers, executing ~6000 A100-hours of sweeps across 9 models, 2 model stages, 4 samplers, 31 temperatures, and 3 random seeds. Figures 4 and 5 convincingly demonstrate that `min-p` does not outperform baselines when hyperparameter volume is controlled — a finding that generalizes beyond this case study as a methodological contribution.

- **Exposes selective reporting in LLM-as-a-Judge evaluations with specific evidence**: The paper documents that `min-p` received ~2× more hyperparameter tuning than `top-p` and ~10× more than `basic` (Fig. 6). Section 4.3 provides a specific, documented instance: the higher of two `min-p` scores (52.01 vs. 50.14) and the lower of two `top-p` scores (50.07 vs. 50.43) were reported, with the evidence linked to a publicly shared Telegram message from the original first author.

- **Systematic verification and documentation of retracted adoption claims**: Section 5 traces the original 54k GitHub repositories and 1.1M stars claims to a naive GitHub search producing false positives, documents their retraction from the camera-ready, and notes that 3 of 4 ICLR reviewers cited these numbers in their endorsements — a vivid cautionary tale.

- **Concrete, evidence-grounded lessons for the community**: The six lessons in Section 6 (control hyperparameter volume, apply statistical tests correctly, demand data transparency, scrutinize qualitative summaries, ensure methodological clarity, watch for selective reporting) are each directly tied to specific errors uncovered in the case study, making them actionable rather than platitudinous.

## Weaknesses

### Fatal

None.

### Major

None.

### Minor

- **Abstract overstates the NLP benchmark evidence**: The abstract claims "Extensive hyperparameter sweeps on NLP benchmarks show `min-p`'s claimed superiority vanishes," but the sweeps were conducted *only on GSM8K CoT* — GPQA, the other benchmark in the original paper, was not re-analyzed. The paper is transparent about this in Section 3 ("Due to our compute budget, we only evaluated GSM8K CoT"), but the abstract's plural "benchmarks" inflates the evidentiary scope. This should be corrected to reflect the single-benchmark reality, as the human evaluation and LLM-as-a-Judge analyses already provide sufficient independent evidence.

- **New human evaluation analysis (Section 2.4) lacks formal statistical testing**: The paper relies on a scatter plot (Fig. 3) to argue that the original authors' second human evaluation shows no `min-p` advantage. While the visualization is suggestive, the absence of formal statistical tests (e.g., paired t-tests with multiple-comparison correction, as applied to the original data in Section 2.2) contrasts with the paper's otherwise rigorous approach and weakens this particular conclusion. The claim would be strengthened by applying the same testing framework used in Table 1.

### Trivial

None.

## Nice-to-Haves

- A sentence in the Discussion acknowledging that GPQA was not re-analyzed and that the pattern's generalizability to that benchmark remains an open question would add intellectual honesty. The human evaluation and LLM-as-a-Judge results already independently call the overall `min-p` claim into question, so this does not weaken the paper's thesis.

- Explicitly reporting both win-rate pairs numerically in Section 4.3 text (which the paper already provides: 52.01 vs. 50.14 for `min-p`; 50.07 vs. 50.43 for `top-p`) and stating that no consistent selection criterion was applied would make the selective-reporting allegation even harder to misinterpret.

## Removed Points

*These points are flagged to be removed — treat them with caution.*

- **"Section 4.3 lacks quantitative comparison" (from Harsh Critic)**: REMOVED — factually incorrect. The paper explicitly states: "the reported win rate of 52.01 corresponds to p = 0.05, but p = 0.01 yields a lower win rate of 50.14" and "the reported win rate of 50.07 corresponds to p = 0.9, but p = 0.98 yields a higher win rate of 50.43." The quantitative comparison is present.

- **"The paper does not elaborate on the exact nature of that inconsistency" (from Harsh Critic)**: REMOVED — the inconsistency is clearly described: higher score chosen for `min-p`, lower score chosen for `top-p`, with specific p-values and win rates. The nature of the inconsistency is fully elaborated.

## Novel Insights

The "Best-of-N" hyperparameter sweep methodology introduced in Section 3 is genuinely novel and broadly applicable. By subsampling hyperparameter combinations and computing maximum scores at each budget, it provides a fair comparison framework that controls for the confounding effect of hyperparameter tuning volume — a problem that extends far beyond this case study. This methodology could serve as a standard tool for evaluating any method that requires hyperparameter search, and it simultaneously functions as a cherry-picking detection mechanism.

## Suggestions

- Revise the abstract to replace "NLP benchmarks" with "GSM8K" (or "a math reasoning benchmark") to accurately reflect the scope of the NLP evaluation.
- Apply the paired t-test framework from Section 2.2 to the new human evaluation data in Section 2.4, with Bonferroni correction across the three temperatures and two metrics. Even a null result would strengthen the paper's symmetry in rigor.
- In the Discussion (Section 6), explicitly note that GPQA was not re-evaluated and that the generalizability of the NLP findings to other benchmarks is an open question, while emphasizing that the human evaluation and LLM-as-a-Judge evidence independently undermine the original claims.

## Score and Decision

### Calibration Anchors

| Anchor | Avg Score | Round | Comparison |
|--------|-----------|-------|------------|
| `lf8QQ2KMgv` — "Is Memorization Actually Necessary for Generalization?" | 3.75 | R1 | Our paper is substantially stronger: more comprehensive (4 lines of evidence vs. 1), more rigorous statistically, and contributes novel methodology beyond fixing errors. |
| `kjVgyR3RFr` — "Evaluating the Quality of Hallucination Benchmarks" | 5.50 | R2 | Our paper is stronger: more impactful findings, more novel methodology (Best-of-N sweeps), and directly actionable lessons. |
| `C1Wp4ubvXZ` — "FairlyUncertain" | 5.60 | R2 | Our paper is stronger in contribution clarity and evidence strength. |
| `TzAJbTClAz` — "FFB: A Fair Fairness Benchmark" | 6.75 | R2 | Comparable in methodological rigor. FFB contributes a new benchmark artifact; our paper contributes a novel sweep methodology and rigorous audit. Roughly comparable quality. |
| `Im2neAMlre` — "One slice is not enough" | 7.33 | R2 | Stronger than our paper: contributes a new dataset (Gecko2K), a new metric, and >100K annotations. Our paper is primarily critique, albeit with methodological innovations. |
| `G5DziesYxL` — "Bridging the Data Provenance Gap" | 6.50 | R1 | Comparable: a large-scale audit paper. Our paper is more focused but equally rigorous. |

**Round 1 bracket**: 5.5–7.5. **Round 2 narrowing**: The paper sits between the 5.50 hallucination-benchmark audit (clearly weaker) and the 7.33 evaluation-methodology paper (clearly stronger). It is comparable to the FFB benchmark paper at 6.75 and the data-provenance audit at 6.50. The abstract overstatement and the missing formal test on the new human evaluation data pull it slightly below these comparators. **Final score: 6.5**.

This is a well-executed, scientifically important audit paper. The core contributions — uncovering data omission, correcting statistical analyses, developing a fair hyperparameter-comparison methodology, and deriving actionable lessons — are substantial and well-supported. The weaknesses are real but addressable in revision and do not undermine the central claims. The paper is a valuable contribution to the growing literature on scientific rigor in ML and deserves acceptance.

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>