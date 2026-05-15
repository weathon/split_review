Now I have all the information I need. Let me compile the final review.

---

## Summary

This paper presents a detailed case study re-examining the evidence behind Nguyen et al. (2024), a high-visibility ICLR 2025 Oral paper that claimed min-p sampling was superior to existing methods. Through careful re-analysis of the original paper's human evaluations, new NLP benchmark sweeps, scrutiny of LLM-as-a-Judge evaluations, and investigation of community adoption claims, the authors demonstrate that the original paper's four lines of evidence do not support its central claim. The paper distills six actionable lessons for rigorous empirical ML research and introduces a novel "Best-of-N" methodology for fairly comparing methods when hyperparameter tuning volume differs.

## Strengths

- **Convincing re-analysis of human evaluation data with proper statistical rigor.** The paper demonstrates that the original study omitted one-third of collected data (the basic sampling baseline), applied a misleading pooled t-test, and failed to correct for multiple comparisons. Table 1 shows that after Bonferroni correction for 12 comparisons, evidence supports min-p's superiority in only 1 of 12 tests at α = 0.05 and 0 of 12 at α = 0.01. An Intersection-Union Test further fails to support the claim of consistent superiority. This re-analysis alone is sufficient to invalidate the original paper's headline claim.

- **Novel "Best-of-N" methodology for controlling hyperparameter tuning volume.** The paper introduces a principled subsampling procedure (150 repetitions, N = 1 to 100 hyperparameters per sampler) that measures how maximum performance scales with hyperparameter search budget. Applied across 9 models, 2 stages, 4 samplers, and 31 temperatures on GSM8K (~6000 A100-hours), this analysis shows min-p's claimed advantage vanishes when all samplers receive equal tuning (Figs. 4, 5). This is a genuinely useful methodological contribution that other researchers can adopt.

- **Well-documented exposure of unsubstantiated community adoption claims.** The paper demonstrates that the original claims of "54,000 GitHub repositories" and "1.1 million stars" were unverifiable and were subsequently retracted from the Camera Ready manuscript. The paper notes that 3 of 4 ICLR reviewers and the Area Chair cited these metrics as justification for acceptance—a sobering real-world example of how such claims can influence peer review.

- **Constructive blueprint with six specific, actionable lessons** (Section 6). Each lesson is explicitly anchored to concrete errors uncovered in the case study, covering hyperparameter tuning control, statistical testing, data transparency, qualitative claim verification, methodological clarity, and selective reporting. This elevates the paper beyond a mere critique into a reusable guide for the community.

- **Clear, well-organized presentation** with each line of evidence addressed separately and conclusions explicitly tied back to the original claims.

## Weaknesses

### Fatal

None. The core human evaluation re-analysis is rigorous and independently sufficient to demonstrate that the original paper's central claim is unsupported.

### Major

None. The paper's main conclusions are well-supported by converging evidence across multiple independent lines of analysis.

### Minor

- **NLP benchmark sweep lacks uncertainty quantification despite the paper's own methodological prescriptions.** The Best-of-N analysis uses 150 subsampling repetitions but only plots averaged curves (Figs. 4, 5) without confidence bands, standard deviations, or any formal summary statistic comparing samplers. Given that the paper itself advocates for "visualizing data with appropriate uncertainty estimates" (Lesson 2), this omission is a notable self-inconsistency. While the visual evidence directionally supports the paper's conclusion (min-p does not consistently outperform), a reader cannot assess whether observed differences are reliable or within sampling noise. Adding confidence bands or reporting the mean difference with a 95% CI at representative N would substantially strengthen this section.

- **The selective-reporting claim in Section 4.3 rests on thin, informal evidence.** The allegation that the original Table 3(b) reported the higher of two min-p scores and the lower of two top-p scores is serious and, if true, strongly supports the paper's argument. However, the evidence provided is a prose description referencing a Telegram link from the original first author. No table, screenshot, or direct data excerpt is included in the paper, making independent verification difficult for readers. The paper would benefit from presenting this evidence in a self-contained, reproducible format (e.g., a table with the two scores for each sampler drawn from the public repository).

### Trivial

- The NLP sweep is limited to a single benchmark (GSM8K CoT) and one set of hyperparameter grids. While the paper notes compute constraints (~6000 A100-hours), explicitly acknowledging that the conclusion on NLP benchmarks is drawn from this specific scenario would improve precision. The paper partially addresses this in the limitations section but could be more direct about the scope of this particular analysis.

## Nice-to-Haves

- A brief sensitivity analysis of the NLP sweep to the chosen hyperparameter grids (e.g., varying grid density or range) would strengthen the argument that the conclusion is robust to reasonable alternative grid choices.
- A short discussion of conditions under which the Best-of-N procedure could mislead (e.g., when the hyperparameter grid does not adequately cover the space) would improve its utility as a general methodological tool.
- Figure 6 (left) could be made more self-explanatory by labeling bars with exact hyperparameter counts.

## Removed Points

These points from the input reviews were considered but removed or weakened:

- **"The conclusion that min-p does not outperform other samplers on GSM8K is drawn from visual inspection... without any formal test"** — Partially kept (moved to Minor). The core concern about missing uncertainty quantification is valid and retained. However, the framing that this "leaves the strength of that subsection ambiguous" overstates the issue, since the paper's main claim does not rest solely on this analysis—the human evaluation re-analysis and the multiple converging lines of evidence provide independent support.

- **"The paper does not demonstrate that the analysis behind the selective-reporting claim is reproducible from public artifacts"** — Partially kept (moved to Minor). The concern about evidential thinness is valid. However, the criticism that the evidence "consists of a prose description referring to a Telegram link" is factual and was retained. The paper does provide specific numbers (52.01 vs 50.14 for min-p; 50.07 vs 50.43 for top-p), which makes the claim falsifiable even if the current presentation is informal.

- **"Missing experiments: discuss sensitivity of NLP sweep to chosen hyperparameter grids"** — Moved to Nice-to-Haves. This is a reasonable suggestion for strengthening the analysis but not a weakness; the current grid is well-motivated (taken from the original paper, lightly edited for evenness) and adequate for the paper's purpose.

- **"Figure 6 could be made more self-explanatory"** — Moved to Nice-to-Haves. Minor presentation improvement, not a substantive weakness.

- **Strength Finder: "The derivation of six specific, actionable lessons"** — Kept but integrated into the blueprint strength.

- **Potentially removed strength: "The investigation into the claimed community adoption metrics illustrates how unsubstantiated numbers can sway reviewer judgment"** — Kept as a core strength; well-documented and impactful.

## Novel Insights

Beyond the paper's own stated contributions, a genuinely novel insight that emerges from this work is the demonstration that **a simple subsampling-based method (Best-of-N) can serve as both a fairness diagnostic and a potential cherry-picking detector** for hyperparameter-heavy comparisons. The idea that unequal hyperparameter search volume can create illusory performance gaps is not new, but the operationalization—measuring the expected maximum performance as a function of search budget via repeated subsampling—provides a practical, assumption-light tool that other researchers can readily adopt. This transforms a known conceptual concern into an actionable empirical procedure.

## Suggestions

- Add confidence bands (from the 150 subsampling repetitions) to Figures 4 and 5, and report a quantitative summary (e.g., mean and 95% CI of max(min-p) − max(best other) at N = 6, 20, 50). This would align the NLP analysis with the paper's own Lesson 2 and resolve the most salient self-inconsistency.
- Present the selective-reporting evidence from Section 4.3 in a self-contained table showing both scores for each sampler, sourced from the public repository rather than relying on a Telegram link description. This would make the claim independently verifiable.
- Explicitly note in Section 3 that the NLP benchmark conclusions are drawn from a single benchmark (GSM8K CoT) under specific hyperparameter grids, and that generalization to other benchmarks remains to be tested.

## Score and Decision

**Calibration anchors used:**

| Anchor | Path | Avg Score | Comparison to paper under review |
|--------|------|-----------|-----------------------------------|
| "False, misleading, and unfounded statements in a recent TPAMI publication" | 1CR1MTIgmq.md | 0.00 | Pure rebuttal with no novel contribution or constructive blueprint; the paper under review is incomparably stronger with original experiments and methodology. |
| "Understanding Before Evaluation" | 9wUKBH3Tja.md | 2.50 | Narrow scope, sloppy presentation, limited contribution; this paper is far more thorough, better written, and more impactful. |
| "Hyperparameter search on the test set in the wild" | hOF6s8Yfxs.md | 2.67 | Addresses a known problem with limited novelty and narrow experiments; this paper has broader scope, more comprehensive evidence, and novel methodology. |
| "On the (In)Significance of Feature Selection" | FRp8cu1aKF.md | 4.67 | Interesting empirical critique but limited in scope and constructive contribution; this paper is more comprehensive with a well-structured blueprint. |
| "ParallelBench: Understanding the Trade-offs of Parallel Decoding in Diffusion LLMs" | OsZr5T7Cd0.md | 5.00 | Solid systems paper with good experiments; the paper under review is a different genre but comparably thorough with broader methodological implications. |
| "$p\textrm{-less}$ Sampling" | ItFuNJQGH4.md | 6.00 | Novel method with good experiments; accepted as Oral. The paper under review is comparably well-executed with its own novel methodology (Best-of-N) and broader community impact through the blueprint. |
| "Statistical Guarantees in the Search for Less Discriminatory Algorithms" | n8FKO0DIl8.md | 6.50 | Strong theoretical contribution with clear practical framing; the paper under review has less theoretical depth but broader empirical scope and actionable lessons. |

The paper under review is a thorough, well-executed case study that makes a genuine contribution through its re-analysis of human evaluation data, its novel Best-of-N methodology, and its constructive blueprint. The weaknesses (missing confidence intervals on the NLP sweep, thin evidence for the selective-reporting claim) are real but minor—they do not undermine the paper's core conclusions, which are supported by multiple converging lines of evidence. The human evaluation re-analysis alone is sufficient to demonstrate that the original min-p paper's central claim is unsupported. The paper is clearly written, well-organized, and provides actionable lessons that generalize beyond the specific case.

Comparing against anchors: the paper is substantially stronger than the 4.67 and below anchors, and comparable in quality to the 6.0 anchor (p-less Sampling, accepted as Oral), though in a different genre (critique/blueprint vs. method paper). The paper's combination of rigorous critique with constructive methodological contribution places it in solid acceptance territory.

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>