Now I have a thorough understanding of the paper and can verify claims directly. Let me produce the final review.

---

## Summary

This paper re-examines a high-profile ICLR 2025 Oral paper that introduced min-p sampling for LLMs, finding that four lines of evidence presented in the original work do not support its claims of superiority. Through data recovery, corrected statistical tests, extensive hyperparameter-controlled benchmark sweeps, and scrutiny of reported LLM-as-a-Judge and community-adoption metrics, the authors demonstrate that the original paper's own data and methods fail to substantiate its central claims. The paper also introduces a "Best-of-N hyperparameter volume control" methodology and derives six general lessons for rigorous empirical ML research.

## Strengths

- **Discovery of omitted human evaluation data (Section 2.1):** The paper identifies that one-third of the original human evaluation data (basic sampling scores) was excluded without justification. This was confirmed with the original authors and the omission was subsequently corrected in the camera-ready version, but the conclusions were not updated. This is a verifiable, concrete finding of scientific malpractice.

- **Correct statistical re-analysis with multiple-comparison correction (Section 2.2, Table 1):** Applying 12 one-sided paired t-tests with Bonferroni correction and an Intersection-Union Test to the original data reveals that only 1 of 12 comparisons survives correction at α=0.05, and 0 at α=0.01 — directly refuting the original claim that min-p "consistently" outperforms baselines. This provides a concrete template for rigorous statistical practice in human evaluation studies.

- **Novel Best-of-N hyperparameter volume control analysis (Section 3.1, Figures 4–5):** The paper introduces and demonstrates a principled method for fairly comparing sampling methods with different hyperparameter spaces. Using a ~6000 A100-hour sweep across 9 models, 4 samplers, and 31 temperatures, the analysis shows min-p does not outperform other samplers when hyperparameter tuning volume is equalized. This is a genuine methodological contribution that the community can adopt for cherry-picking detection.

- **Identification of selective reporting in LLM-as-a-Judge results (Section 4.3):** The paper documents that the original Table 3(b) reported the higher of two win rates for min-p (52.01 vs. 50.14) but the lower of two for top-p (50.07 vs. 50.43), supported by evidence from a publicly shared Telegram link. This concrete instance of inconsistent reporting is well-documented.

- **Verification and retraction of unsubstantiated community-adoption claims (Section 5):** The paper shows that the original claims of 54k GitHub repositories and 1.1M stars could not be substantiated — major LM repositories total only 453k stars — and that the original authors retracted both claims. The fact that 3 of 4 ICLR reviewers cited these retracted numbers as justification for strong endorsement makes this finding particularly important.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

- **The human evaluation re-analysis of the *original* data focuses only on the high-diversity setting.** The paper gives three justifications (the min-p claim is about quality-diversity tradeoff; the original authors said to focus on high diversity; the low-diversity top-p hyperparameter was poorly chosen) and partially addresses this through a new human evaluation study (Section 2.4, Fig. 3) that covers both settings. However, the main statistical re-analysis of the *original* paper's data (Table 1) excludes the low-diversity condition, and the claim that the original "own evidence invalidates its central claim" is slightly stronger than what this selective re-analysis alone supports. The paper would be strengthened by showing — even in an appendix — that including the low-diversity condition does not change the conclusion, or by more explicitly qualifying the scope of that claim.

- **GPQA benchmark analysis is omitted.** The paper explicitly acknowledges this due to compute budget (the GSM8K sweep alone required ~6000 A100-hours). The original paper claimed superiority on both GSM8K and GPQA. While the paper does not claim to have invalidated the benchmark evidence for GPQA specifically, it does state that "Extensive hyperparameter sweeps on NLP benchmarks show min-p's claimed superiority vanishes" — a generalization that slightly over-reaches the single-benchmark evidence. This is a minor over-claim that the authors could address by qualifying "on GSM8K" or running a scaled-down GPQA sweep.

- **The "blueprint" lessons (Section 6) are mostly standard best practices.** Lessons 2–6 (correct for multiple comparisons, practice data transparency, scrutinize qualitative summaries, ensure methodological clarity, watch for selective reporting) are well-trodden methodological advice. Only Lesson 1 (the Best-of-N hyperparameter volume control) is genuinely novel. The paper's framing as providing a "blueprint" overpromises relative to what is delivered for lessons 2–6. The lessons are useful as a concrete, case-study-grounded synthesis, but the novelty claim is overstated.

- **The limitations paragraph is too brief and does not flag specific gaps.** The paper's limitations section (one sentence) is generic ("Conclusions here are based on that evidence. New evidence might lead to different conclusions.") but does not explicitly mention the exclusion of the low-diversity condition or the omission of GPQA as caveats. The paper would benefit from a more specific limitations discussion.

- **Larger-scale models are not tested.** The NLP benchmark sweep covers models up to 8B–9B parameters. The paper does not acknowledge that behavior could differ for substantially larger models (e.g., 70B+). This is a minor gap given the compute constraints are understandable.

### Trivial

- The paper uses the phrase "we believe" when asserting the 7.80→5.80 value discrepancy (Section 2.4), which slightly undercuts the force of the finding. If the authors' publicly posted data supports this, the paper should state the discrepancy more authoritatively (e.g., "the correct value is 5.80").

## Nice-to-Haves

- Include the low-diversity condition in the original-data re-analysis (or as an appendix) to fully close the gap, even if only to confirm that the poor hyperparameter choice for top-p drives the original result.
- Run a scaled-down GPQA sweep (e.g., a subset of models or hyperparameters) to extend the benchmark refutation.
- Add a section explicitly quantifying the impact of the omitted basic-sampling data on the original paper's pooled t-test conclusion.
- Provide a systematic table comparing all LLM-as-a-Judge scores available from the Telegram data vs. those reported in the original Table 3(b).
- Present the hyperparameter volume control methodology as a standalone checklist item for reviewers.

## Removed Points

The following points were raised in the input reviews but are removed or reclassified:

- **"The list of referenced scandals in the introduction is rhetorical rather than evidentiary"** — This is a stylistic critique about framing in the introduction. The references establish context and motivation, which is appropriate for an introduction. **Removed** (stylistic nitpick).

- **"The claim about the 7.80→5.80 discrepancy is not independently verified"** — The paper explicitly states the discrepancy and attributes it to the authors' publicly posted data. The paper presents it as a claim with a source, which is appropriate for a meta-review. **Removed** (the paper does present the discrepancy and its source).

- **Strength Finder's implicit claim that the paper fully delivers on the "blueprint" framing** — This conflicts with the verified weakness that lessons 2–6 are standard advice. Per the instructions, "when a strength and weakness disagree, the weakness wins." The strength about the blueprint has been downgraded to acknowledge the limitation. The concrete strengths about specific findings (omitted data, statistical correction, selective reporting, retracted claims) are retained.

- **"Missing related works"** — Not included as per instructions (no external sources to verify).

- **"Undisclosed hyperparameters" / reproducibility nitpicks** — The paper releases analysis code and data. No such issues present.

## Novel Insights

None beyond the paper's own contributions. The harsh critic and strength finder provide useful confirmation and synthesis of the paper's strengths and gaps but do not add novel analytical perspectives beyond what the paper itself offers.

## Suggestions

1. **Include the low-diversity condition in the original-data statistical analysis** (even as an appendix) to close the completeness gap. This would make the refutation of the original paper's evidence airtight rather than conditional on the exclusion.
2. **Run a limited GPQA sweep** — even 2–3 models with the core hyperparameters — to extend the benchmark analysis. This would cost substantially less than the full GSM8K sweep and would complete the picture.
3. **Expand the limitations paragraph** to explicitly address the two gaps above, rather than using generic language. A self-critical limitations section would strengthen rather than weaken the paper.
4. **Retitle or reframe the "blueprint"** to more accurately reflect its nature: a case-study-driven set of best practices with one novel methodological tool, rather than a novel framework.

## Score and Decision

MY FINAL SCORE: <score>7.5</score>
MY FINAL DECISION: <decision>Accept</decision>