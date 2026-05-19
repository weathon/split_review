- Decision: Reject
- Avg Score: 4.50
- Scores: 3, 6, 6, 3
Here is my consolidated review:

## Summary

This paper investigates whether training language models to win debates via self-play improves judge accuracy, compared to non-adversarial consultancy training. Using information-asymmetric reading comprehension questions from QuALITY, the authors find a 4% absolute improvement in judge accuracy after debate training (p < 10⁻⁶), with no such relationship for consultancy models. They introduce stronger consultancy baselines (ensembled and double consultancy) and analyze learned policies, finding that debaters increase evidence use while consultants become repetitive and judge-specific.

---

## Strengths

- **First demonstration that training models to win debates improves judge accuracy**: The paper shows a statistically significant positive relationship between debater win rate and judge accuracy (4% absolute increase, Figure 3), directly validating the core hypothesis. Prior work (Radhakrishnan et al., 2023) had failed to find this effect. (Section 4.2, Abstract)

- **Non-adversarial baselines isolate debate's mechanism**: Consultancy models exhibit no positive relationship between consultant skill and judge accuracy, and the novel ensembled/double consultancy baselines help attribute debate's advantage to adversarial pressure and side-by-side comparison rather than mere information asymmetry. (Section 3.3, Section 4.2–4.3)

- **Policy analysis shows divergence in learned strategies**: The fully trained debate model uses 96% more quoted words (evidence) than the SFT model, while the consultant uses 70% fewer quotes and becomes repetitive (98% of second-speech quotes repeated from the first). Debate strategies transfer to an untrained GPT-4o judge (Pearson r=0.98) while consultancy strategies do not (r=0.51), suggesting debate encourages more generally informative argumentation. (Section 4.4/5.1, Figure 4)

- **Judge calibration mitigates known confounds**: The finetuned GPT-4T judge addresses sycophancy and calibration issues that plagued prior debate experiments, enabling a cleaner comparison between debate and consultancy. (Section 3.1, Figure 2)

---

## Weaknesses

### Fatal
None.

### Major

- **Incomplete statistical reporting for the central claim**: The paper reports p < 10⁻⁶ for the positive trend between debater skill and judge accuracy (Section 4.2) but does not specify what statistical test was used, how the p-value was computed, or whether it accounts for the non-independence of self-play debates (the same model generates both sides). Judge accuracy per checkpoint appears to be a single point estimate over 433 questions; no confidence intervals or standard errors are provided for any of the accuracy values in Figure 3, making it impossible to assess the variability or stability of the reported trend. Given that the trend line is drawn through a small number of checkpoints (3–5 visible in Figure 3), the apparent strength of the p-value could be misleading without knowing the test details. This is the paper's most significant weakness because it concerns the core empirical claim.

### Minor

- **Policy analysis significance claims are uneven**: The consultancy quote reduction (70% fewer) is explicitly described as "barely significant due to high variance" (Section 4.4), yet it is presented alongside the much stronger debate evidence trend without clearly distinguishing the evidential weight. The repetition claim (98% of quotes repeated) is presented without a significance test or a baseline repetition rate from earlier checkpoints, so the reader cannot evaluate whether this is a genuine training-induced shift or an artifact. These do not undermine the core debate-accuracy claim but weaken the supporting narrative about *why* debate succeeds.

- **Pearson correlations with only 5 data points**: The transfer-to-GPT-4o analysis reports Pearson correlations of 0.98 (debate) and 0.51 (consultancy) based on five checkpoints (Section 4.4). With five data points, a single outlier can dramatically change the correlation. Spearman rank correlation or a bootstrap interval would provide a more robust assessment.

- **Double consultancy trend claim without error intervals**: The paper states that double consultancy "fails to exhibit a positive trend between model skill and judge accuracy" (Section 4.3), but this is based on the same small set of checkpoints without confidence intervals. A lack of detected trend is not evidence of no trend, and the paper's strongest consultancy baseline merits more careful statistical treatment.

### Trivial
None.

---

## Nice-to-Haves

- **Cross-model debate accuracy**: The paper already collects head-to-head matchups for the round-robin tournament (Section 3.4). Reporting judge accuracy when evaluating asymmetric debates (e.g., SFT vs. DPO) would directly test whether debate training causes the judge to become more accurate regardless of opponent symmetry, rather than only in self-play.

- **Per-debate evidence use with confidence intervals**: Rather than aggregated quote counts, showing that within individual debates the increase in quotes correlates with correct debater success under the judge would more directly link policy changes to accuracy improvements.

- **Clarify the number of checkpoints**: The text is vague about exactly how many checkpoints appear in the trend analysis figures.

---

## Removed Points

*These points are flagged to be removed; treat them with caution.*

- **Reward function appendix detail**: The critic notes that Section 3.2.2 refers readers to the appendix for details on reward formulation comparisons. Per the removal rules, missing appendix content is a parser artifact — the appendix exists in the original submission. The paper already provides in-text summary of the comparison ("logit or log...narrowly lose to directly using the judge's confidence").

- **Judge initialization / alternative initialization speculation**: The critic suggests the paper should explore whether alternative judge initialization (e.g., SFT consultant win rate near 50%) would change the conclusions. The paper already acknowledges the distribution shift between judge training data and Llama3-8B debaters (Section 4.1). Speculation about alternative experimental choices is not a concrete weakness in what the paper actually did.

- **Cross-model accuracy analysis** (from "Strengthening the Paper on Its Own Terms"): This is a suggestion for additional analysis, not a criticism of the existing work. Moved to Nice-to-Haves.

- **Generalizability from self-play discussion**: The critic asks the paper to add a paragraph arguing why self-play is a meaningful proxy for scalable oversight. The paper already has a limitations section (Section 5.2) discussing this issue, including the caveat about asymmetric debaters.

---

## Novel Insights

None beyond the paper's own contributions. The reviews surface the importance of proper statistical reporting (error bars, test specification, small-N correlation fragility) but do not reveal any structural flaw or unconsidered alternative explanation that the paper's authors had missed.

---

## Suggestions

1. **Add confidence intervals / error bars to all main accuracy figures** (especially Figure 3) using bootstrapping over the 433 questions.
2. **Specify the statistical test** used to obtain p < 10⁻⁶, including how the non-independence of self-play debates was handled.
3. **Provide a table** of exact judge accuracy values per checkpoint with standard errors and sample sizes.
4. **Report Spearman rank correlation or bootstrap intervals** for the GPT-4o transfer analysis (currently Pearson r with N=5).
5. **Add a significance test or baseline comparison** for the 98% repetition rate claim about consultancy models.

---
