Now let me also quickly read the PASTA paper (5.50) and the Clever Hans paper (5.00) more carefully to firm up the comparison.

Based on my analysis of all anchors:

- **Clever Hans (5.00):** Interesting motivation but disappointing empirical execution — reviewers found results lacking depth. Our paper has substantially stronger empirical execution.
- **PASTA (5.50):** Shallow analyses across limited data, methodological issues. Our paper has more rigorous statistical treatment and novel methodology.
- **Human Feedback (6.50):** Clean critique paper, well-executed methodology, some ad-hoc elements. Our paper has more dramatic findings but less disciplined claims.
- **Beyond Correlation (6.75):** Clean novel metric, well-justified. Our paper is broader but has more significant overclaiming issues.
- **Training on Test Task (8.00):** Fundamental concept with broad implications, clean methodology. Our paper is narrower as a case study.

**Final score: 6.0.** The paper's genuine strengths — discovering omitted data, rigorous statistical re-analysis, and the novel Best-of-N methodology — are substantial. But the two major weaknesses (overclaiming on NLP benchmarks with different models, and thin evidence for the selective reporting allegation) pull it down from the 6.5-7.0 range.

---

## Summary
This paper presents a critical case study re-examining the evidence behind min-p sampling (Nguyen et al., 2024, ICLR 2025 Oral). Through re-analysis of human evaluations, NLP benchmarks, LLM-as-a-Judge evaluations, and community adoption claims, the paper argues that the original paper's data does not support min-p's claimed superiority and derives six methodological lessons for rigorous empirical ML research.

## Strengths
- **Discovery of omitted human evaluation data (Section 2.1):** The paper identifies that one-third of collected human evaluation scores (basic sampling baseline) were excluded from the original paper without mention. The authors publicly confirmed this omission. The excluded data changes the conclusions — basic sampling was preferred by more evaluators than min-p (Fig. 2).

- **Rigorous statistical re-analysis of human evaluations (Section 2.2, Table 1):** The paper demonstrates that the original paper's single pooled t-test was methodologically inappropriate. The re-analysis using 12 separate one-sided paired t-tests with Bonferroni correction and an Intersection-Union Test provides the correct framework, showing only 1/12 comparisons remain significant after correction — directly invalidating the "consistently outperforms" claim.

- **Novel Best-of-N hyperparameter-volume control methodology (Section 3.1):** The paper introduces a principled approach for fair comparison: subsampling equal numbers of hyperparameter configurations per method, computing the maximum over each subset, and repeating to obtain expected best performance as a function of hyperparameter budget. The two complementary analyses (Figs. 4 and 5) across 9 models, 2 training stages, 4 samplers, and 31 temperatures (~6000 A100-hours) operationalize the concern that methods with larger hyperparameter spaces can appear superior simply due to more tuning.

- **Quantitative falsification of community adoption claims (Section 5):** The paper demonstrates that the claimed 1.1M GitHub stars for min-p exceeds the combined stars of all major LM repositories, making the claim numerically implausible. The original authors retracted both numbers from the Camera Ready.

- **Concrete, evidence-grounded methodological lessons:** Rather than vague criticism, each of the six lessons in Section 6 is directly tied to specific evidence from preceding sections, giving them practical weight beyond generic advice.

## Weaknesses

### Fatal
None.

### Major

- **NLP benchmark analysis does not replicate the original paper's setup while claiming to refute its conclusions:** The paper evaluates only GSM8K (not GPQA, which the original paper also evaluated) and uses entirely different models (Qwen 2.5, Mistral 7B, Llama 3.1/3.2, Gemma 2) from those in the original paper. The paper never specifies which models the original used, making it impossible for readers to assess whether this is a replication or an extension. The abstract and section titles use sweeping language ("min-p's claimed superiority vanishes") that goes beyond what these experiments can support — they show the claim does not generalize to new models on GSM8K, which is a weaker and importantly different finding. The Limitations section acknowledges this obliquely, but the mismatch between strong headline claims and what the experiments actually demonstrate remains a structural weakness.

- **The selective reporting allegation (Section 4.3) rests on evidence too thin to assess:** The paper claims the original paper's Table 3(b) reported the higher of two scores for min-p and the lower for top-p. The evidence is a Telegram link with no details about what data the link contained, how scores were computed, or what the two min-p settings correspond to. The win-rate differences are tiny (52.01 vs. 50.14 for min-p; 50.07 vs. 50.43 for top-p) — all within a few points of random chance. Alternative explanations (pre-registered hyperparameter choice, sloppy summary rather than selective reporting) are not considered. The claim is the paper's most serious allegation but its weakest evidential link.

### Minor

- **The six blueprint lessons (Section 6) are individually sensible but mostly restate well-known principles:** Controlling for hyperparameter tuning, correcting for multiple comparisons, demanding data transparency, scrutinizing qualitative claims, ensuring reproducibility, and avoiding selective reporting are standard practices. The one genuinely novel contribution — the Best-of-N methodology — receives insufficient technical treatment (no analysis of statistical properties, no discussion of when it may mislead vs. alternatives). The "blueprint" framing inflates what is essentially a case study with lessons appended.

- **Manual annotation of qualitative responses (Section 2.3) lacks methodological rigor:** The annotation was performed by the authors of this paper (with an obvious stake in the outcome) without inter-annotator agreement metrics or blinding to the paper's hypothesis. This weakens the force of the finding that more evaluators preferred basic sampling.

- **The community adoption section (Section 5) has limited scientific contribution:** The claims were already retracted by the original authors. The assertion that the revised statement "remains misleading" is made without explanation.

### Trivial

- **The possible data error claim (Section 2.4) is presented as "we believe" without confirmation:** The statement about the 7.80 vs. 5.80 discrepancy in the original authors' Table 15 is stated as belief rather than verified fact.

## Nice-to-Haves
- Conducting even a small-scale GPQA replication would substantially strengthen the NLP benchmark critique beyond the single-benchmark evidence.
- Adding blinded, multi-annotator coding with inter-annotator agreement for the qualitative response analysis (Section 2.3) would make that finding more robust.
- The Best-of-N methodology deserves a deeper technical treatment: analyzing its statistical properties, discussing when it is appropriate vs. when it might mislead, and comparing it to alternatives like Bayesian optimization with matched budgets.
- Specifying which models the original paper evaluated would help readers assess whether the new GSM8K experiments constitute a replication or an extension.

## Removed Points
These points are flagged to be removed, treat them with caution.

- **Harsh Critic: "The NLP benchmark re-analysis does not replicate the original paper's experiments and therefore cannot directly refute its claims"** — Retained as a Major weakness; the core concern is valid but the framing was softened. The paper does demonstrate that min-p's advantage does not generalize to new models under controlled conditions, which has some value.

- **Harsh Critic: "The gap between the 'blueprint' framing and the actual methodological depth makes the paper read as a case study with lessons appended"** — Retained as a Minor weakness with softened framing; the Best-of-N methodology provides some methodological novelty.

- **Harsh Critic section-by-section notes on abstract overstatement** — Merged into the Major weakness about NLP benchmark analysis.

- **Strength Finder: "Documented instance of asymmetric selective reporting in LLM-as-a-Judge results"** — Removed as a strength because the same claim is identified as a Major weakness. The evidence is too thin to present as a verified strength.

- **Strength Finder: "Careful delineation of scope and limitations"** — Removed as a standalone strength. While the paper has a limitations section, the overclaiming in the abstract and section titles undermines this.

- **Harsh Critic: "GPQA replication missing"** — Moved to Nice-to-Haves. The paper acknowledges compute constraints; demanding a second benchmark is scope creep for a case study already spending ~6000 A100-hours.

## Novel Insights
The Best-of-N subsampling methodology for controlling hyperparameter volume is a genuinely useful contribution that could be adopted beyond this case study. By repeatedly subsampling equal-sized hyperparameter subsets and computing expected maximum performance, it provides a principled way to compare methods with differently-sized hyperparameter spaces — a problem that arises frequently in empirical ML but is rarely addressed head-on. The point about LLM-judge preference non-transitivity (Section 4.1) and its implications for indirect comparison designs is also underappreciated and worth developing further.

## Suggestions
- **Either substantiate or drop Section 4.3.** The selective reporting allegation is the paper's most explosive claim and its weakest evidential link. If stronger evidence exists, present it fully. If not, the paper is stronger without this claim than with a thinly supported version of it. At minimum, discuss alternative explanations and acknowledge the thinness of the evidence.

- **Narrow the NLP benchmark claims to match the evidence.** Rather than claiming to refute the original paper's results, frame the GSM8K sweep as testing whether the claimed advantage generalizes to new models under controlled hyperparameter tuning. The paper would be stronger for the honesty.

- **Deepen the Best-of-N methodology.** This is the paper's most novel contribution. A brief discussion of statistical properties, when it works vs. fails, and relationship to hyperparameter sensitivity would elevate it from a straightforward procedure to a genuine methodological contribution.

---

## Calibration Anchor Summary

| Anchor | Path | Score | Round | Comparison |
|---|---|---|---|---|
| Clever Hans | PtnttTKgQw | 5.00 | R1 | Our paper has substantially stronger empirical execution and more concrete findings |
| PASTA | 6KZ80APcxf | 5.50 | R1 | Our paper has more rigorous statistical treatment and novel methodology |
| Human Feedback is not Gold Standard | 7W3GLNImfS | 6.50 | R2 | Similar critique paper but cleaner methodology; our paper has more dramatic findings but less disciplined claims |
| Beyond Correlation | E8gYIrbP00 | 6.75 | R2 | Cleaner contributions; our paper is broader but has significant overclaiming issues |
| Training on the Test Task | jOmk0uS1hl | 8.00 | R1 | Fundamental concept with broad implications; our paper is narrower as a case study |

**Round 1 bracket:** 5.0 to 7.5. **Round 2 narrowing:** the paper is most comparable to the 6.50 anchor but with additional overclaiming issues, placing it at **6.0**.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>