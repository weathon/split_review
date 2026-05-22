Now I have all the information I need. Let me write the consolidated review.

**Round 1 bracket:** Based on comparison with weak-band anchors (avg 2.5-3.0, rejected), middle-band anchors (avg 4.0-6.0, rejected), and strong-band anchors (avg 8.0, accepted), the paper clearly sits above the 4-5 range critique papers. It's significantly stronger than "Is Memorization Actually Necessary" (avg 4.40), "Autoencoders for Anomaly Detection" (avg 4.50), and "Pathologies of OOD Detection" (avg 4.75). It's comparable to or slightly better than "Rethinking Graph Classification Datasets" (avg 6.00). The initial bracket is 5.5 to 7.5.

**Round 2 narrowing:** Compared to anchors in (4.5, 6.5) and (6.0, 8.0), the paper is clearly stronger than the 5.25-5.75 papers (ObjectNet Captions, ARIES) which are solid but not as rigorous. It's comparable in quality to "Dissecting Sample Hardness" (avg 6.20, accepted) and better than "Rethinking Graph Classification" (avg 6.00, rejected) — both of which re-evaluate existing practices with new experiments. The paper's evidence is cleaner, more comprehensive, and more directly tied to its core claim than those papers. **Final score: 6.5.**

---

## Summary

This paper presents a rigorous, multi-faceted re-analysis of "Turning Up the Heat: Min-P Sampling for Creative and Coherent LLM Outputs" (Nguyen et al., 2024), a high-profile ICLR 2025 Oral paper. The authors systematically examine the original paper's four lines of evidence — human evaluations, NLP benchmark evaluations, LLM-as-a-Judge evaluations, and community adoption claims — and demonstrate that none of them actually support min-p's claimed superiority. The re-analyses include: discovering that 1/3 of human evaluation data was omitted, correct statistical testing showing min-p does not consistently outperform baselines, an extensive hyperparameter sweep (~6000 A100-hours) with a novel Best-of-N methodology showing min-p's advantage vanishes when controlling for hyperparameter tuning volume, evidence of selective reporting in LLM-as-a-Judge results, and documentation of retracted community adoption claims. From this case study, the paper derives six general lessons for rigorous empirical ML research.

## Strengths

- **Novel Best-of-N hyperparameter control methodology (Section 3.1, Figures 4 and 5):** The paper introduces and executes a method to equalize the number of hyperparameters swept across samplers before comparing maximum performance. This directly addresses the common practice of cherry-picking hyperparameters and provides a generalizable toolkit for fair method comparison. The analysis covers 9 models × 2 stages × 4 samplers × 31 temperatures × 6 hyperparameters × 3 seeds, requiring ~6000 A100-hours — a genuinely massive and thorough evaluation.

- **Correct multi-comparison correction with Intersection-Union Test (Section 2.2, Table 1):** The re-analysis applies Bonferroni correction and an IUT to test the original claim of "consistent" superiority across 12 comparisons. This corrects the original paper's flawed pooling and single t-test, and demonstrates a transparent statistical standard that is applicable beyond this specific case.

- **Discovery of omitted data changing conclusions (Section 2.1):** The paper finds that scores for the "basic" sampler — comprising 1/3 of all collected human evaluation data — were excluded without justification. Inclusion of this data changes the conclusions. This finding is concrete, verifiable, and sets a clear precedent for demanding complete data releases.

- **Detection of selective reporting in LLM-as-a-Judge results (Section 4.3):** The paper identifies that the higher of two scores was reported for min-p (52.01 vs. 50.14) while the lower of two was reported for top-p (50.07 vs. 50.43), using evidence from a publicly shared Telegram link. This is a specific, documented instance of selective reporting.

- **Verification of unsubstantiated community adoption claims (Section 5):** The paper cross-checks claimed 54k repositories and 1.1M GitHub stars against public data for major LM repositories (totaling 453k stars), finding the claims unsupported and subsequently retracted. The fact that 3 of 4 ICLR reviewers and the AC cited these retracted numbers as justification for acceptance makes this finding particularly impactful.

- **Well-structured evidence and clear writing:** Each section of evidence is presented systematically, with clear figures, statistical tests, and direct quotations from the original paper being critiqued. The six general lessons are well-motivated by the specific findings.

## Weaknesses

### Fatal
None.

### Major
- **Limited NLP benchmark scope (Section 3):** The re-analysis only covers GSM8K (CoT), while the original paper also reported results on GPQA. The authors acknowledge this limitation and cite compute constraints (~6000 A100-hours), and they are careful not to over-claim ("does not outperform other samplers when controlling for hyperparameter volume" — referencing GSM8K experiments). However, the claim that min-p does not outperform on *any* benchmark would be stronger with GPQA coverage. A skeptical reader could point to this gap. This is the most significant limitation of the paper's evidence.

### Minor
- **LLM-as-a-Judge analysis stops short of new experiments (Section 4):** The critique of methodological under-specification, uneven hyperparameter tuning (Fig. 6, left: min-p received ~25 hyperparameters vs. top-p's ~11 vs. basic's ~2), and selective reporting is valid and well-supported by available data. However, the paper does not re-run the LLM-as-a-Judge evaluations to provide corrected estimates under a fair comparison. This makes this line of evidence less definitive than the human evaluation and NLP benchmark re-analyses. The critique is valid as-is, but an independent LLM-as-a-Judge experiment would have substantially strengthened this section.

- **Limitations section is too brief:** The discussion of limitations (Section 6) is a single paragraph. A dedicated limitations subsection covering the single-benchmark NLP analysis, the reliance on external data for the LLM-as-a-Judge analysis, the focus on the high-diversity setting in human evaluations, and the fact that the re-analysis does not prove min-p *never* works — only that the original evidence does not support it — would strengthen the paper's scientific positioning.

### Trivial
None worth listing separately.

## Nice-to-Haves
- The paper could mention effect sizes (e.g., Cohen's d) for the human evaluation comparisons (Table 1) alongside the p-values, to quantify the practical (non-)difference.
- The raw data and analysis code are mentioned as publicly posted but no specific URL is provided in the abstract/intro — for a paper about transparency, a footnote with the exact link would be appropriate.
- The implications for the ICLR review process (3 of 4 reviewers and the AC cited retracted numbers) could be discussed in more depth as a systemic lesson.

## Removed Points
- **Harsh critic's "abstract framing is a bit grand" claim about "blueprint":** This is an opinion, not a weakness. The lessons are genuinely broadly applicable.
- **Harsh critic's request for effect sizes (Cohen's d):** Moved to Nice-to-Haves as the confidence intervals in Fig. 1 already convey the practical magnitude.
- **Strength Finder's "Full data transparency revealing omitted data" strength:** This has been merged into the core strengths above.
- **Strength Finder's "Systematic verification of community-adoption claims":** Merged into strengths above.
- **Strength Finder's "Detection of selective reporting":** Merged into strengths above.

## Novel Insights
None beyond the paper's own contributions. The paper's main novel insight is the demonstration that the original min-p paper's own data invalidate its claims, coupled with the Best-of-N methodology as a general tool for fair hyperparameter-controlled comparison. The six lessons are well-articulated but are not individually novel — their value is in being grounded in a concrete, high-profile case.

## Suggestions
- Expand the NLP benchmark re-analysis to at least one additional benchmark (GPQA or similar) to close the main evidential gap. This would make the "no advantage" claim significantly harder to dispute.
- Perform an independent LLM-as-a-Judge evaluation with fair hyperparameter tuning (equal number of configurations per sampler) and direct pairwise comparisons. This would turn the critique into a positive demonstration of the correct approach.
- Expand the limitations section to explicitly address: (a) single-benchmark NLP coverage, (b) non-reproduction of LLM-as-a-Judge evaluations, (c) focus on high-diversity setting, and (d) the scope of the conclusion (the original evidence does not support min-p, not that min-p never works).

## Score and Decision

**Comparison anchors:**

| Anchor ID | Avg Score | Round | Comparison |
|-----------|-----------|-------|------------|
| 9L9j5bQPIY | 2.50 | 1 | Weak band; unrelated meta-network paper, much weaker |
| fM1ETm3ssl | 3.00 | 1 | Weak band; weaker meta-model paper |
| k0nlUXYKhX | 2.50 | 1 | Weak band; unrelated fault forecasting, much weaker |
| 0VKEJKKLvr | 3.00 | 1 | Weak band; unrelated genotype prediction, much weaker |
| GbEmJmnQCz | 4.40 | 1 | Middle band; similar meta-critique of memorization paper, but paper under review has stronger experiments and clearer evidence |
| lf8QQ2KMgv | 3.75 | 1 | Middle band; same memorization paper, weaker version |
| om5z1n0mXA | 6.00 | 1 | Middle band; graph benchmark re-analysis, comparable quality but paper under review is more focused and has cleaner evidence |
| X8XQOLjLX6 | 4.50 | 1 | Middle band; autoencoder critique, weaker — less thorough experiments |
| hlijRgXTDK | 4.75 | 1 | Middle band; OOD critique, weaker — reviewers found it lacking novelty |
| UHPnqSTBPO | 8.00 | 1 | Strong band; LLM judge paper with provable guarantees — different type of contribution, significantly more technical |
| U17KoLrXE8 | 5.25 | 2 | Captioning critique; weaker — less systematic |
| icTZCUbtD6 | 6.20 | 2 | Sample hardness analysis; accepted, comparable quality |
| Zr96FfaUGR | 5.50 | 2 | ARIES dataset; a different type of contribution |
| jw2fC6REUB | 6.40 | 2 | CURIE benchmark; different contribution type |

**Round 1 bracket:** 5.5–7.5

**Final calibration:** The paper sits solidly above the 4-5 range critique papers (which were rejected) and is comparable to or better than "Rethinking Graph Classification Datasets" (avg 6.00, rejected — less focused evidence) and "Dissecting Sample Hardness" (avg 6.20, accepted). The paper's main limitations are the single-benchmark NLP scope and the lack of new LLM-as-a-Judge experiments, which prevent it from reaching the 7.5+ range.

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>