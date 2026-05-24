Now I have all the evidence I need. Let me write the consolidated review.

## Summary

This paper presents a thorough, systematic re-analysis of "Turning Up the Heat: MIN-P Sampling for Creative and Coherent LLM Outputs" (Nguyen et al., 2024, ICLR 2025 Oral). The authors scrutinize four lines of evidence from the original paper — human evaluations, NLP benchmarks, LLM-as-a-Judge evaluations, and community adoption claims — and find that none support the claim that min-p consistently outperforms existing samplers. The paper introduces a novel "Best-of-N" methodology for fairly comparing methods with unequal hyperparameter tuning, and distills six actionable lessons for more rigorous empirical ML research.

## Strengths

1. **Thorough, multi-evidence critique of a high-profile paper.** The paper investigates four independent lines of evidence (human eval, NLP benchmarks, LLM-as-a-Judge, community adoption). Each investigation is carefully executed, and the convergent result — that the original paper's central claims are unsupported — is convincingly established. This sets a high bar for post-publication scrutiny.

2. **Novel "Best-of-N" methodology for controlling hyperparameter volume.** Section 3.1 introduces a principled approach to comparing methods when one has received more hyperparameter search effort. The analysis subsamples equal numbers of hyperparameters per sampler (150 trials per N) and tracks max performance as search budget grows. This is a practical, reusable tool for detecting cherry-picking, and it is clearly explained and demonstrated across 9 models × 2 stages on GSM8K (~6000 A100-hours).

3. **Concrete documentation of scientific malpractice and its consequences.** The paper shows exactly how omitted data (1/3 of human eval scores), incorrect statistical tests (pooled single t-test for a "consistent across all settings" claim, no correction for multiple comparisons), mischaracterized qualitative feedback, and selective reporting in LLM-as-a-Judge evaluations can invert a headline result. Section 5 further demonstrates that unsubstantiated community-adoption claims (54k repos, 1.1M stars) were retracted but had already influenced three reviewers and the Area Chair. This provides actionable, evidence-grounded warnings for reviewers and researchers.

4. **Honest about limitations.** The paper explicitly acknowledges that its NLP sweep is only on GSM8K CoT, that conclusions are based on available evidence, and that new evidence could change them. It also notes min-p remains a valid method to try.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

1. **The NLP benchmark analysis is limited to a single task (GSM8K CoT).** The paper acknowledges this limitation (line 208: "Due to our compute budget, we only evaluated GSM8K CoT"), but it means the central claim that min-p does not outperform when controlling for hyperparameter volume is established only for math reasoning. The original paper's NLP benchmarks also included GPQA. Extending to at least one more task domain would strengthen the generality of this finding. *Why it matters: The paper's title and framing suggest broad lessons about fair comparison, but the strongest quantitative evidence for the Best-of-N finding comes from one task type.*

2. **The selective-reporting evidence for LLM-as-a-Judge (Section 4.3) relies on a single unarchived communication (a Telegram link).** The paper documents that min-p's higher score (52.01 for p=0.05) and top-p's lower score (50.07 for p=0.9) were selectively reported, with alternative values available. However, the source is described as "the first author publicly shared a Telegram link" — an ephemeral communication channel. While the inconsistency is documented and the authors are transparent about the source, this particular piece of evidence is less robust than the other lines of evidence in the paper. *Why it matters: The "selective reporting" lesson in the discussion is important, but this specific data point could be disputed by the original authors. The other evidence in the section (under-specification, indirect comparison, unequal hyperparameter tuning) stands on firmer ground.*

3. **The manual annotation of qualitative preferences (Fig. 2) lacks inter-annotator agreement and procedural details.** The paper states responses were "manually annotated" and annotations were publicly posted, but does not describe the annotation process, criteria for resolving ambiguous responses, number of annotators, or inter-annotator agreement. *Why it matters: A core claim is that "Basic was the most preferred sampler, not min-p." Without reliability metrics, readers cannot assess whether the annotation is subjective or replicable.*

4. **The new human evaluation (Section 2.4) involves multiple methodological changes relative to the original study**, including different sampler implementation, participant pool, hyperparameters, reading time, and rubric. The paper uses the (null) result from this new study to support its conclusion that min-p does not improve quality or diversity. However, because so many variables changed simultaneously, it is unclear whether the null result is due to min-p's inherent lack of advantage or due to the specific changes in experimental design. *Why it matters: The converging evidence from Sections 2.1-2.3 (re-analysis of original data) is already sufficient to conclude the original claims are unsupported. The new study is a bonus but cannot bear disproportionate weight.*

5. **Confidence intervals or error bands are not shown on the Best-of-N curves (Figures 4 and 5).** The paper averages over 150 subsamples per N, so variance estimates were readily available. Without error bands, it is difficult to visually assess whether the small apparent advantage of min-p in a few model panels is meaningful or due to sampling noise. *Why it matters: The visual claim that "min-p is largely indistinguishable from other samplers" would be strengthened by showing uncertainty in the curves.*

### Trivial
- The parenthetical "(ongoing work to publish)" in line 247 is informal and unnecessary in a research paper.

## Nice-to-Haves
- Extend the Best-of-N controlled hyperparameter analysis to at least one more benchmark (e.g., GPQA or MMLU) and perhaps to a text generation task with different metrics.
- Add formal statistical tests (e.g., effect sizes or pairwise significance tests) to the LLM-as-a-Judge win-rate comparisons in Fig. 6 (right), rather than relying on visual inspection of overlapping confidence intervals.
- Provide box plots or individual score distributions for the human evaluator scores in Fig. 1 to reveal outliers or bimodality.
- Test whether the "no advantage when controlling for tuning" finding generalizes to other sampling methods (e.g., typical sampling, mirostat).

## Removed Points

- *"The original paper also evaluated GPQA and AlpacaEval. Without extending the controlled-comparison methodology to other tasks, the strength of the conclusion…is narrower than the paper's framing suggests."* → Demoted to Minor weakness #1 above (already partially addressed by the paper's own acknowledgment of the limitation). The paper does not claim to have tested all tasks; it is transparent about scope.
- *"The limitation paragraph is too brief"* / *"should acknowledge the task-specificity of the NLP sweep"* → The paper already acknowledges the NLP sweep limitation in lines 208 and 322 ("Conclusions here are based on that evidence. We emphasize that new evidence might lead to different conclusions."). This is sufficient.
- *"The hyperparameter values were 'lightly edited to make them more evenly distributed,' which could differ from the original paper's choices"* → The Best-of-N methodology controls for hyperparameter volume precisely because it subsamples. The choice of hyperparameter values is transparently listed. This is a non-issue.
- *"The choice of Bonferroni for 12 comparisons is conservative"* → This is a design choice, not a weakness. Bonferroni is standard and the paper also reports uncorrected p-values so readers can judge for themselves.
- *"The paper does not fully examine whether the changes in implementation, participant pool, rubric, and hyperparameters could explain the null result"* → Demoted to Minor weakness #4. The original data re-analysis (Sections 2.1-2.3) already invalidates the original claims without relying on the new study.
- *Strength Finder: "This paper addressed an important problem" and similar generic strengths* → Removed as generic. The kept strengths are specific and evidence-grounded.
- *Strength Finder: "The paper is clearly written"* → This is true but generic; the concrete strengths above implicitly convey this.
- *"Missing appendix sections"* → Parser artifact, not an author issue.
- *Various grammar/formatting nitpicks* → Parser artifacts, not author issues.
- *"The authors should run the human evaluation re-analysis on the new dataset with the same statistical rigor"* → The new data is visualized in Fig. 3; the visual result (all points clustered together) is unambiguous. Formal tests would add precision but are not necessary to support the conclusion.

## Novel Insights

Beyond the paper's own contributions, the most striking synthesis from the reviews is that this case study demonstrates a **systematic pattern** across four wholly independent evaluation modalities (human, benchmark, LLM-judge, community metrics). In each modality, the original paper's claims of min-p's superiority collapse under scrutiny — but each collapse happens for a *different* kind of methodological error (omitted data, unequal tuning, selective reporting, unverifiable claims). This suggests that the original paper did not have a single "mistake" but rather a failure of scientific culture that allowed weak evidence to compound across all four sections. The paper under review does an excellent job surfacing this, but does not explicitly name this compounding effect as an insight; a future revision could highlight that convergence of *different* error types across modalities makes the critique stronger than any single error would.

## Suggestions

1. Address the selective-reporting evidence in Section 4.3 by obtaining or citing a more permanent, independently verifiable record (e.g., archived screenshots, or a statement from the original authors) rather than an ephemeral Telegram link.
2. Add error bands to Figures 4 and 5 using the variance from the 150 subsamples. This can be done with a simple shaded region around each line.
3. Provide inter-annotator agreement (e.g., Cohen's κ) for the qualitative preference annotation in Fig. 2, or at minimum describe the annotation procedure and number of annotators.
4. Acknowledge more explicitly in Section 4 that the selective-reporting evidence is based on a communication that may be difficult to independently verify, while noting the rest of the section's claims (under-specification, indirect comparison, unequal tuning) do not depend on it.
5. Consider adding box plots or per-participant scatter plots to Fig. 1 to allow readers to assess score distributions beyond means and CIs.

## Score and Decision

**Calibration anchors** (all from the deepreview_13k_calibration set):

| Path | Avg Score | Comparison |
|------|-----------|------------|
| GbEmJmnQCz.md | 4.40 | "Is Memorization Actually Necessary for Generalization?" — similar re-analysis genre, but narrower (one line of critique vs. four), weaker methodological contribution, and mixed reviewer confidence. The min-p paper is substantially stronger. |
| lf8QQ2KMgv.md | 3.75 | Same paper, another version with lower scores. Reviewers questioned the validity of some critique arguments. The min-p paper's critiques are more airtight. |
| fXJCqdUSVG.md | 6.50 | "On Evaluating the Durability of Safeguards" — similar critical re-analysis with case studies, scored 6.50. The min-p paper has more lines of evidence, a novel methodological contribution (Best-of-N), and clearer actionable lessons. Comparable or slightly stronger. |
| 8NiTKmEzJV.md | 6.25 | NETS sampler — a methods paper, not a critique. Harder to compare directly. |
| cNmu0hZ4CL.md | 8.00 | Top-tier methods paper with theory + experiments. The min-p paper has a different contribution profile (critique + methodological tool + lessons), not quite at this level for a venue like ICLR. |
| Zr96FfaUGR.md | 5.50 | ARIES — a dataset/benchmark paper, not directly comparable. |
| CpiOUOaqh3.md | 2.00 | Epidemiological modeling — low-quality submission, not comparable. |

The min-p paper is stronger than typical re-analysis/critique papers (cf. ~4 for the memorization critiques) and comparable to or slightly stronger than the fXJCqdUSVG paper (6.50). It offers novel methodology (Best-of-N) and convergent evidence across four modalities, but is limited by scope (single NLP task) and a weak provenance for one sub-claim. I position it above the 6.50 anchor but below the top-tier 8-range papers.

MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>