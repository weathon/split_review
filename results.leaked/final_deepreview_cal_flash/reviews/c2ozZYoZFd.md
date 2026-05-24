## Summary

This paper presents a detailed case-study audit of "Turning Up the Heat: Min-P Sampling for Creative and Coherent LLM Outputs" (ICLR 2025 Oral). It re-examines the original paper's four main lines of evidence—human evaluations, NLP benchmarks, LLM-as-a-Judge evaluations, and community adoption claims—and argues that none support the claimed superiority of min-p sampling. From the case study, it distills six general lessons for more rigorous empirical machine learning research. The central finding—that the original paper's own data, when correctly analyzed, do not show min-p consistently outperforming baselines—is well supported by the re-analysis.

## Strengths

1. **Rigorous re-analysis of human evaluations exposes omitted data and incorrect statistics (Sections 2.1–2.2, Table 1, Figure 1).** The paper discovers that one-third of human evaluation scores (for the "basic" sampler) were excluded without justification. After including those data and applying a Bonferroni correction for 12 comparisons, only 1 of 12 tests remains significant, and an Intersection-Union Test further confirms insufficient evidence for the "consistent outperformance" claim. This is the strongest piece of evidence in the paper and directly undermines the original paper's central claim.

2. **Novel Best-of-N analysis for controlling hyperparameter volume, applied to an extensive NLP benchmark sweep (Section 3.1, Figures 4–5).** The paper spends ~6000 A100-hours sweeping 9 models × 2 stages × 4 samplers × 31 temperatures × 6 hyperparameters × 3 seeds. The Best-of-N subsampling methodology is a clean and transparent way to equalize hyperparameter search volume across methods. The consistent result—min-p is indistinguishable from or worse than baselines when tuning is equalized—provides strong independent evidence against the original claims.

3. **Documentation of retracted community-adoption claims (Section 5).** The paper shows that the original paper's claims of 54,000 GitHub repositories and 1.1M stars were unsubstantiated and subsequently retracted. It further notes that 3 of 4 ICLR reviewers cited these numbers as a justification for acceptance, which is an important illustration of how unverified claims can influence peer review.

4. **Methodological contribution of the Best-of-N framework itself.** Beyond the specific case study, the Best-of-N analysis is a practical tool that the field can adopt for fair hyperparameter comparisons and for detecting cherry-picking. The paper demonstrates its utility concretely.

5. **Overall clarity and data-driven approach.** The paper is well-structured, each critique is grounded in specific evidence (figures, tables, quotes from the original data), and the connections between specific findings and general lessons are explicitly drawn.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

1. **The selective reporting claim (Section 4.3) is not independently verifiable from the paper as written.** The paper states that "the first author publicly shared a Telegram link" showing that the higher of two scores was reported for min-p and the lower for top-p, but provides no URL, screenshot, or stable archival reference. For a paper that centrally advocates transparency and reproducible evidence, this is an ironic gap. While the specific numbers are stated (52.01 vs. 50.14 for min-p; 50.07 vs. 50.43 for top-p), a reader cannot verify the claim without access to the Telegram link. The paper's overall thesis does not depend on this claim—the human evaluation re-analysis and NLP sweeps are sufficient to challenge the original conclusions—but the allegation of selective reporting is presented as a finding and deserves proper documentation.

2. **The NLP benchmark sweep is limited to GSM8K.** The original paper also claimed superiority on GPQA (5-shot). The current paper acknowledges this limitation ("Due to our compute budget, we only evaluated GSM8K CoT"), but the title and abstract convey a broader refutation of min-p's benchmark performance. The authors should either explicitly bound their benchmark conclusions to GSM8K, or include a discussion of why the GPQA results are likely affected by the same unequal-tuning issue (which the paper partially does for the LLM-as-a-Judge setting but not for GPQA).

3. **The qualitative response annotations (Figure 2) are a single-annotator effort.** The paper manually categorizes 53 human evaluators' open-ended responses into preference categories. No inter-annotator reliability is reported, and the subjectivity of this step is not discussed. The raw annotations are said to be publicly posted, which mitigates the concern, but the paper should either acknowledge the limitation or report reliability from a second annotator.

4. **The "blueprint" lessons (Section 6) are sensible but generic.** Lessons such as "apply statistical tests rigorously and transparently" or "demand and practice full data transparency" are well-supported by the case study but are not novel—they appear in many existing guidelines on research rigor. The paper would be stronger if it offered more specific, operationalized protocols (e.g., a concrete procedure for applying Best-of-N analysis, a checklist for auditing qualitative summaries) rather than high-level warnings.

5. **The numerical error claim (7.80 vs. 5.80, Section 2.4) is asserted without a side-by-side reproduction.** The paper states that a value in the original Table 15 is incorrect based on "the authors' publicly posted data," but does not reproduce the relevant rows of the original table alongside the corrected value. This would be easy to add and would make the claim more transparent.

### Trivial

- The statistical tests use one-sided paired t-tests on ordinal (2–10 Likert) scores. While non-parametric alternatives (e.g., Wilcoxon signed-rank) would be more conservative, the authors acknowledge this would not change the conclusions, and the strong null results after Bonferroni correction make this a non-issue.

## Nice-to-Haves

- Include a screenshot or archived URL of the Telegram evidence for the selective reporting claim, or restructure Section 4.3 to note that the claim cannot be independently verified from the paper alone.
- Add a side-by-side table showing the original Table 15 entry and the recalculated value for the 7.80/5.80 discrepancy.
- Report effect sizes (e.g., Cohen's d) for the human evaluation comparisons, which would help readers assess practical significance.
- The Best-of-N methodology could be presented as a standalone protocol or checklist that other researchers can directly apply, rather than described only in the context of this case study.

## Removed Points

These points are flagged to be removed; treat them with caution:

- **Harsh critic's point about "no direct response from the original authors."** Requiring the original authors' engagement is outside the paper's scope and not a standard expectation for case-study critiques.
- **Strength Finder's framing of the selective reporting claim as "concrete evidence."** Given the Telegram link is not reproduced in the paper, characterizing this as "concrete evidence" overstates the documentation. The point is retained as a Minor weakness above to mark the gap.
- **Harsh critic's suggestion that the paper should include a reproducibility statement with links.** The paper mentions at multiple points that data and annotations are publicly posted (lines 98, 121, 328). The full links were likely in the appendix (stripped by the parser).
- **Various formatting and presentation nitpicks** (font size, grammar, etc.)—these are parser artifacts or are too minor to affect evaluation.

## Novel Insights

None beyond the paper's own contributions. The insight that hyperparameter-volume asymmetry can create spurious performance advantages, and the Best-of-N method to control for it, are the most novel methodological takeaways. The broader observation that a high-profile Oral paper's central claims are invalidated by its own data, across multiple independent lines of evidence, is a useful cautionary tale for the field but follows from careful application of existing best practices rather than a new conceptual framework.

## Suggestions

1. **Provide an archival reference for the Telegram evidence** in Section 4.3 (screenshot in appendix or stable URL). Without this, the selective reporting claim is weaker than the rest of the paper's evidence and distracts from an otherwise rigorous critique.
2. **Explicitly bound the NLP benchmark conclusions.** Either add a small-scale GPQA sweep (even 2–3 models would help) or state clearly in the abstract and title that the benchmark refutation covers GSM8K, and explain why the original GPQA results are suspect due to the same methodological issues documented for the LLM-as-a-Judge evaluation.
3. **Add a side-by-side comparison** for the numerical error claim (Table 15 of the original paper vs. the recalculated value).
4. **Acknowledge the single-annotator limitation** for the qualitative response classification (Section 2.3) or report a second annotation.
5. **Strengthen the "blueprint"** by converting one or two lessons into specific, reusable protocols (e.g., a step-by-step Best-of-N template, a checklist for auditing human evaluation claims). The case study evidence is rich enough to support more actionable guidance.

## Score and Decision

### Calibration

**Round 1 — Bracketing:**
- *Weak band* (avg <3.5): Papers like "Attributing Model Behavior" (3.00), "Questioning Simplicity Bias Assumptions" (2.50). These are weaker rejects.
- *Middle band* (avg 3.5–7.5): "Is Memorization Actually Necessary for Generalization?" (4.40, 3.75) — critique papers with less thorough experimentation; "Re-Evaluating the Impact of Unseen-Class Unlabeled Data on SSL" (6.00, accepted) — re-evaluation paper with new framework; "Rethinking Graph Classification Datasets" (6.00, rejected); "Reevaluating Theoretical Analysis Methods for Optimization" (5.75, rejected).
- *Strong band* (avg >7.5): MLE-Bench (8.00), "How much of my dataset did you use?" (7.60). These are different in kind (new benchmarks/methods).

The paper under review is clearly stronger than the weak-band papers and the simpler critique papers (4.4–5.75). It is most comparable to the 6.00-level re-evaluation papers, but with broader scope and more extensive original experiments.

**Round 2 — Narrowing (bracket 5.0–7.0):**
- "Re-Evaluating the Impact of Unseen-Class Unlabeled Data on SSL" (6.00, accepted): identifies evaluation flaw + proposes new framework + thorough experiments. The current paper is comparable in quality and ambition but has the Telegram documentation gap that the SSL paper does not.
- "Rethinking the Effectiveness of Graph Classification Datasets" (6.00, rejected, scores 5/6/8/5): re-evaluation of benchmarks with new metrics. The current paper has stronger primary evidence (the human evaluation re-analysis alone is compelling) but shares the pattern of a mixed review due to uneven documentation.
- "Does Calibration Affect Human Actions?" (4.67, rejected): HCI study with methodological concerns. The current paper is substantially stronger.

The paper sits between the 5.75–6.00 anchors. It has more experimental scope and a clear methodological novelty (Best-of-N) that the critique anchors lack, but also has documentation gaps that the best-practice anchors (like the SSL re-evaluation paper) do not.

**Final position:** The paper is clearly stronger than the 4.40–5.75 critique anchors but has documentation issues that prevent it from reaching the 7+ range. It is most comparable to the 6.00-level re-evaluation papers, with a slight edge in scope and experimentation offset by the Telegram evidence gap.

### Anchors Considered

| Anchor | Avg Score | Round | Comparison |
|--------|-----------|-------|------------|
| x8mr9zGkpr | 3.00 | R1 | Much weaker — thin critique, low relevance |
| bU0JMHJ8zL | 2.50 | R1 | Much weaker — literature review, not critical re-analysis |
| fM1ETm3ssl | 3.00 | R1 | Much weaker — different topic |
| lvHHWDJCcr | 3.40 | R1 | Much weaker — metrics proposal, not case study |
| RrIjnSMhMZ | 2.50 | R1 | Much weaker — unrelated topic |
| GbEmJmnQCz | 4.40 | R1 | Weaker — critique paper with less thorough experiments and some methodological issues of its own |
| rSAPrQzoQa | 5.00 | R1 | Less relevant — method paper |
| X8aFMdXk3N | 4.25 | R1 | Comparable type (benchmark quality critique) but less experimental depth |
| pwIGnH2LHJ | 3.75 | R1 | Weaker — dataset quality paper |
| lf8QQ2KMgv | 3.75 | R1 | Weaker — critique paper with less thorough experiments |
| EUSkm2sVJ6 | 7.60 | R1 | Stronger — different type (data usage inference), polished execution |
| 6s5uXNWGIh | 8.00 | R1 | Stronger — MLE-Bench, polished benchmark paper |
| RvUVMjfp8i | 8.00 | R1 | Stronger — SSL evaluation, polished and thorough |
| KbetDM33YG | 8.00 | R1 | Stronger — GNN evaluation, different type |
| KIgaAqEFHW | 8.00 | R1 | Stronger — theorem proving, different type |
| XM7INBbvwT | 4.67 | R2 | Weaker — HCI study with limited experimentation |
| 4GfEOQlBoc | 5.25 | R2 | Different type — perception, less relevant |
| 6KZ80APcxf | 5.50 | R2 | Different type — XAI benchmark |
| rpbzBXdo4x | 5.00 | R2 | Different type — CoT prompting study |
| NPDnRLFhc0 | 5.50 | R2 | Different type — biomedical evidence extraction |
| qtqvuBmhxU | 5.75 | R2 | Less relevant — medical image benchmark |
| **WPsnH6875d** | **6.00** | **R2** | **Most comparable — re-evaluation paper identifying evaluation flaws, accepted. Current paper has more scope but less polished documentation.** |
| **om5z1n0mXA** | **6.00** | **R2** | **Comparable — graph dataset re-evaluation, rejected on split reviews. Current paper has stronger primary evidence.** |
| JslyktsKMY | 5.75 | R2 | Weaker — optimization theory critique |
| GqI4fTVUXC | 6.00 | R2 | Comparable — theory-practice critique, but less experimental |

### Final Score and Decision

The paper makes a valuable contribution to research rigor by conducting a thorough, multi-faceted audit of a high-profile publication. Its core evidence—the human evaluation re-analysis showing omitted data and failed statistical tests, and the Best-of-N controlled NLP sweeps—is strong and well-executed. The main weakness is the insufficient documentation of the selective reporting claim (Section 4.3), which is ironic for a paper advocating transparency but does not undermine the central thesis.

**Score: 6.0** — A solid paper with clear contributions and addressable weaknesses.

**Decision: Accept**

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>