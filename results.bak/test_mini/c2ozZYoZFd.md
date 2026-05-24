Now I have sufficient calibration data. Let me construct my final review.

**Round 1 bracket:** The paper sits between moderate critique papers (4.0–5.0) and strong meta-evaluation papers (6.5). Initial bracket: 4.5–6.5.

**Round 2 narrowing:** Compared to "Beyond the Heatmap" (5.00), "Inference Scaling" (5.50), and "PU Learning Benchmark" (6.50), the paper is stronger than the 5.0-level critique papers (more thorough, multi-faceted, novel Best-of-N methodology, discovered omitted data, retracted community claims) but not as strong as the 6.5-level papers that propose genuinely new evaluation frameworks from scratch. The paper sits at ~6.0.

---

## Summary

This paper is a meta-scientific case study that re-examines the four lines of evidence presented in the ICLR 2025 Oral min-p sampling paper (Nguyen et al., 2024). Through re-analysis of human evaluations (discovering omitted data, applying correct statistical tests), extensive NLP hyperparameter sweeps (introducing a Best-of-N methodology to control for tuning volume), scrutiny of LLM-as-a-Judge evaluations (finding methodological ambiguity and selective reporting), and investigation of unsubstantiated community-adoption claims, the paper concludes that the original claims of min-p's superiority are unsupported. It derives general methodological lessons for rigorous empirical ML research.

## Strengths

- **Novel Best-of-N hyperparameter-control methodology (Section 3.1, Figures 4–5):** The paper introduces a principled subsampling technique to equalize hyperparameter tuning volume across methods before comparing maximum performance. This is a genuine methodological contribution that the community can adopt to detect cherry-picking. The analysis is backed by ~6000 A100-hours of experiments across 9 models, 31 temperatures, 6 hyperparameters per sampler, and 3 seeds.

- **Rigorous re-analysis of human evaluations with correct statistical testing (Section 2, Table 1):** The paper conducts 12 one-sided paired t-tests with Bonferroni correction and an Intersection-Union Test, exposing that only 1 of 12 comparisons survives correction. This directly refutes the original claim of "consistent" superiority. The visualization in Figure 1 with overlapping 95% CIs is clear and effective.

- **Discovery of omitted human-evaluation data (Section 2.1):** The paper reveals that one-third of the collected human scores (the "basic" sampling condition) were excluded without justification, and that including them changes the conclusions. This was confirmed with the original authors and publicly posted.

- **Detection of selective reporting in LLM-as-a-Judge results (Section 4.3):** The paper identifies that the original Table 3(b) reported the higher win rate for min-p (52.01 for p=0.05) but the lower win rate for top-p (50.07 for p=0.9), while higher scores existed for top-p (50.43 for p=0.98).

- **Empirical refutation of unsubstantiated community-adoption claims (Section 5):** The paper shows the claimed 1.1M GitHub stars / 54k repositories are impossible (leading LM repositories total ~453k stars). The authors retracted these numbers. This directly supports the paper's lesson to scrutinize bold claims.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

- **NLP benchmark analysis limited to GSM8K only (Section 3):** The original min-p paper reported results on both GSM8K (CoT) and GPQA (5-shot). The present paper's extensive hyperparameter sweep only covers GSM8K (under two prompt formats). The abstract states "Extensive hyperparameter sweeps on NLP benchmarks show min-p's claimed superiority vanishes" — this overstates the scope, as only one benchmark was tested. The authors acknowledge the compute constraint (~6000 A100-hours), but the claim should be qualified. This does not invalidate the overall conclusion, but it weakens a central piece of evidence. The paper's overall conclusion is still supported by the human evaluations, LLM-as-a-Judge critique, and community-adoption refutation.

- **No statistical testing or confidence intervals on Best-of-N differences (Section 3.1, Figures 4–5):** The Best-of-N plots show performance differences across samplers, but there are no error bars or statistical tests indicating whether the observed differences are significant. The paper averages over 150 subsamples and 3 seeds, but does not report uncertainty. The human evaluation section uses rigorous statistics; the NLP section should follow suit (e.g., confidence intervals on the difference at each N).

- **Selective reporting evidence relies on an external link (Section 4.3):** The claim that Table 3(b) selectively reported scores is backed by data from a public Telegram link. While the specific numbers are quoted in the text (52.01 vs 50.14 for min-p; 50.07 vs 50.43 for top-p), the paper would benefit from including a static table showing the full comparison for direct verification, given the gravity of the allegation.

- **Best-of-N methodology's subtle assumption about basic sampling (Section 3.1):** The subsampling procedure treats each temperature × hyperparameter combination as independent. "Basic" sampling has only temperature as a hyperparameter (31 combinations), while top-p and min-p have 186 combinations each. When subsampling to N=100, basic is forced to resample with replacement from only 31 unique combinations. This could bias results. The paper notes this in the caption but does not discuss the potential bias or run a sensitivity analysis (e.g., varying the number of hyperparameter values per sampler). This is a reasonable first attempt but not definitive.

- **The paper's conclusion that min-p "offers no apparent advantage" is stronger than strictly warranted (Section 6):** Given that the NLP analysis only tested GSM8K, the conclusion should be more carefully scoped: the evidence does not demonstrate an advantage, rather than definitively asserting none exists. The paper's own note that min-p produced higher scores for 2 of 12 models when the correct prompt format was used (Section 3.1) undermines a blanket "no advantage" claim.

### Trivial
None.

## Nice-to-Haves
- A small static table in Section 4.3 showing the two scores for each sampler and indicating which was reported, to avoid relying on an external link.
- Running the same hyperparameter sweep on GPQA (or another dataset) to broaden the NLP claim, or explicitly narrowing the claim to GSM8K with an explanation of why this suffices.
- A sensitivity analysis of the Best-of-N methodology varying the number of hyperparameter values per sampler.
- Error bars or confidence intervals on the Best-of-N difference plots.

## Removed Points
These points are flagged to be removed, treat them with caution:
- **"The list of references is extensive and may be overkill"** — Style/formatting nitpick, removed.
- **"The claim that the paper is a 'blueprint' is somewhat grandiose"** — Subjective opinion about framing, not a substantive weakness.
- **"The paper would be stronger if it acknowledged these are standard practices"** — The paper does acknowledge this (line 31: "the errors made in evaluating min-p are common in empirical machine learning research"). Already addressed.
- **"The paper does not report on variation across random seeds"** — The paper averages over 3 seeds and 150 subsamples (Section 3.1). This is factually incorrect about the paper's content.
- **"The paper does not discuss a limitation of its own approach"** — The paper has a dedicated "Key Limitation" paragraph (Section 6, line 322–323). Already addressed.
- **"The paper should be more transparent about the exception [2 of 12 models]"** — The paper explicitly mentions this (line 223). Already included in the paper.
- **"The paper's own new human evaluation study is somewhat rushed"** — The paper presents the data and identifies a potential numerical error; this is appropriately brief given it is secondary evidence.
- **"min-p might have value in specific use cases"** — Speculative; the paper's conclusion is about whether the original claims are supported, which is a separate question.

## Novel Insights
None beyond the paper's own contributions. The meta-scientific insights (need for fair hyperparameter comparison, proper multiple-comparison correction, full data transparency) are well-known best practices that the paper demonstrates through a concrete case study rather than claims as novel discoveries. The primary novelty is the **demonstration** through a detailed, multi-faceted case study and the **Best-of-N methodology** itself.

## Suggestions
1. Add error bars/confidence intervals to Figures 4 and 5, and ideally report whether the differences between min-p and the best other sampler are statistically significant at each N.
2. Qualify the abstract's NLP claim (e.g., "NLP benchmarks" → "GSM8K") or add GPQA results.
3. Include a small static table in Section 4.3 directly showing the scores for min-p and top-p at each hyperparameter value, rather than relying on an external link.
4. Discuss the Best-of-N subsampling assumption about basic sampling's limited hyperparameter space and add a sensitivity analysis.
5. Slightly soften the conclusion language from "offers no apparent advantage" to "the evidence examined does not demonstrate an advantage."

## Score and Decision

**Final Score: 6.0**

**Decision: Accept**

**Calibration Anchors:**

| Path | Avg Score | Round | Comparison |
|------|-----------|-------|------------|
| Is Memorization Actually Necessary (eAVPivm2jv) | 4.0 | R1 | Weaker: less thorough, fewer evidence lines, no novel methodology, smaller compute scale |
| On the (In)Significance of Feature Selection (FRp8cu1aKF) | 4.67 | R1/R2 | Weaker: single evidence line, mixed reviews, less rigorous |
| Beyond the Heatmap (H6PLJnnK6e) | 5.0 | R2 | Weaker: comparable critique structure but less multi-faceted, lower compute investment |
| The Limits of Inference Scaling (j8H84v6AZ1) | 5.50 | R1 | Comparable: both critique empirical claims, similar rigor; min-p paper is broader with methodology contribution |
| Accessible Fair Evaluation PU Learning (5R11h5o44C) | 6.50 | R2 | Stronger: first comprehensive benchmark for a subfield, more thorough systematic comparison |
| How Reliable is Micro-Benchmarking (cReExMQLiK) | 6.50 | R1 | Stronger: proposes genuinely novel meta-evaluation measure (MDAD) with broader applicability |

The paper is a thorough, multi-faceted critique with a novel methodological contribution (Best-of-N) and real-world impact (retracted community-adoption claims). It is substantially stronger than other critique papers at the 4.0–5.0 level but falls slightly short of papers proposing entirely new evaluation frameworks at the 6.5 level due to bounded coverage of the NLP analysis and some missing statistical details. Score of 6.0 reflects this positioning.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>