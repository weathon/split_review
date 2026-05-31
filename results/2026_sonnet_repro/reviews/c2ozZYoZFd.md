Now let me perform calibration searches to anchor the score.Round 1 bracket: **6 to 8**. The paper clearly exceeds the middle tier (rejected papers at 3-5 scoring range) and has substantial empirical contributions, documented findings, and a novel methodology. Let me narrow with round 2.Now I have enough to write the final review. Let me synthesize everything.

---

## Summary

This paper presents a comprehensive re-examination of "Turning Up the Heat: MIN-P Sampling for Creative and Coherent LLM Outputs" (Nguyen et al., 2024, ICLR 2025 Oral), systematically investigating four lines of evidence — human evaluations, NLP benchmarks, LLM-as-a-Judge evaluations, and community adoption metrics. The authors demonstrate, using the original paper's own data and extensive new experiments (~6000 A100-hours), that min-p's claimed superiority over existing samplers is not supported by the evidence. As a secondary contribution, the paper proposes the "Best-of-N" hyperparameter equalization methodology and derives six lessons for more rigorous empirical ML research.

---

## Strengths

- **Confirmed omission of one-third of human evaluation data (Section 2.1)**: The paper identifies that basic sampling scores — one-third of all collected human evaluation data — were excluded from the original paper's methodology, analysis, and results "without mention or justification." This omission was publicly confirmed by the original authors. Inclusion of this data changes the paper's conclusions.

- **Rigorous statistical reanalysis with Bonferroni correction (Table 1)**: Using the original paper's own data, the authors conduct 12 one-sided paired t-tests and show that after Bonferroni correction, only 1 of 12 comparisons survives at α=0.05 and 0 of 12 at α=0.01. This directly and specifically contradicts the claim that min-p "consistently scored higher across all settings" via a single pooled t-test.

- **Novel Best-of-N hyperparameter equalization methodology (Section 3.1, Figs. 4–5)**: The methodology equalizes the number of hyperparameter configurations swept per sampler before comparing peak performance. Applied across 9 models, 4 samplers, 31 temperatures, 6 hyperparameters per sampler, and 3 seeds, the results consistently show that min-p's apparent advantage dissolves under fair comparison. The methodology is generically applicable beyond this case study.

- **Retraction of unsubstantiated community adoption claims (Section 5)**: The original paper claimed 54k GitHub repositories and 1.1M stars. The authors show the combined stars of the 8 largest LM repositories sum to only 453k — less than half of the 1.1M claimed for min-p alone. Both figures were subsequently retracted from the Camera Ready. This matters because 3 of 4 ICLR 2025 reviewers and the AC cited these figures as their primary justification for endorsement.

- **Independent corroboration from the original authors' own new experiment (Section 2.4)**: The original authors conducted a new human evaluation in response to the critique. Fig. 3 shows all three samplers cluster together in both quality and diversity with no apparent advantage for min-p, constituting independent corroboration from the original authors themselves.

- **Qualitative response annotation reveals basic sampling preferred (Section 2.3, Fig. 2)**: Manual annotation of open-ended participant responses shows basic sampling was preferred by 21 evaluators vs. min-p preferred by 12, contradicting the original paper's claim that "participants frequently noted that outputs generated with min-p were more coherent and creative."

---

## Weaknesses

### Fatal
None.

### Major

- **GPQA benchmark gap (Section 3)**: The paper explicitly states "Due to our compute budget, we only evaluated GSM8K CoT." The original paper claims "min-p sampling achieves superior performance across benchmarks" and evaluated both GSM8K and GPQA. The benchmark critique addresses only one of two benchmarks, leaving the claim partially refuted. The paper is transparent about this, but it is a genuine residual gap that a reviewer of the original paper might correctly note.

### Minor

- **Section 4.3 framing (selective-reporting allegation)**: The selective-reporting finding — that the original paper reported the higher of two min-p scores (52.01% at p=0.05) and the lower of two top-p scores (50.07% at p=0.9) — rests on a Telegram message from the first author as the source of the alternative values. The paper's phrasing ("appear to have reported results inconsistently") appropriately stops short of a direct accusation, but the implied inference of intent is thinner than the evidence in Sections 2 and 3. This finding should be more clearly framed as an unexplained inconsistency requiring clarification from the original authors.

- **"Ongoing work" citation in Section 4.2**: Section 4.2 opens with "Closely scrutinizing (ongoing work to publish) the data revealed two more insights." Invoking unpublished work from the same group as implicit evidentiary support is methodologically awkward. This parenthetical should either be incorporated as supplementary evidence or removed.

### Trivial

- **Blueprint lessons are largely standard**: The six methodological lessons in Section 6 (correct multiple comparison testing, full data release, hyperparameter volume control, scrutinize qualitative claims, methodological clarity, consistent reporting) are largely established best practices. The case-study grounding makes them valuable, but the "blueprint" framing in the title and abstract slightly oversells their novelty as a standalone contribution.

- **Table 15 value discrepancy unelaborated (Section 2.4)**: The paper asserts "we believe one value is incorrectly reported: the average score of min-p at p=0.05 and temperature T=2 is reported as 7.80, but based on the authors' publicly posted data, we believe the correct numerical value should be 5.80." No derivation or explanation is provided. A brief clarification of how the discrepancy was identified would strengthen this claim.

---

## Nice-to-Haves

- A self-contained specification of the Best-of-N hyperparameter equalization method as a standalone procedure (independent of the min-p case study) would increase its uptake as a general-purpose tool for the community.
- Extending the benchmark analysis to GPQA, if compute budget permits, would fully close the benchmark critique.
- A brief analytical paragraph in the Discussion distinguishing error categories (honest oversight vs. careless statistical practice vs. motivated reporting) would sharpen the "blueprint" framing and help readers recognize which risk applies to their own work.

---

## Removed Points

*These points were considered but removed; treat with caution.*

- **IUT test ambiguity**: The harsh critic notes ambiguity in whether the Intersection-Union Test is the appropriate test given that "consistently" is used as ordinary language rather than a precise statistical claim. This is a minor methodological nuance; the Bonferroni correction alone is fully sufficient to make the point, and the IUT augmentation is conservative rather than incorrect. Removed as a weakness.

- **Generalizability of "blueprint" lessons**: The harsh critic notes the six lessons are not novel. Retained as a trivial weakness (framing), but not as a substantive criticism since the value lies in case-study grounding, not in the originality of the lessons.

- **Strength about "provides reproducible blueprint"**: The Strength Finder lists this as a major strength, but the six lessons are standard practices. Downgraded to Nice-to-Have (the methodology section is genuinely useful, but the lessons themselves are not independently novel).

---

## Novel Insights

The Best-of-N hyperparameter equalization methodology is the paper's most transferable technical contribution. By subsampling equal numbers of hyperparameter configurations per method and measuring the best achievable score across subsampled sets, it isolates whether a method's advantage reflects genuine superiority or merely a larger implicit search budget. This is a clean, reusable diagnostic that applies beyond sampling methods to any comparison where competing approaches have different numbers of tunable knobs. The broader sociological observation — that 3 of 4 ICLR reviewers explicitly grounded their endorsement in community adoption figures that turned out to be unsubstantiated and retracted — is a striking concrete data point about how non-technical claims propagate through peer review, independent of the min-p specifics.

---

## Suggestions

1. Frame Section 4.3 as an unexplained inconsistency in reported values rather than as apparent selective reporting — explicitly invite the original authors to clarify the selection criterion rather than implying intent.
2. Either incorporate the "(ongoing work to publish)" reference as concrete supplementary material in this submission or remove the citation from Section 4.2.
3. Add a brief methods box or algorithm block formalizing the Best-of-N procedure for standalone use.
4. Clarify the derivation of the 5.80 vs. 7.80 discrepancy in Section 2.4 with a short footnote or sentence.
5. If feasible within compute budget, add a GPQA analysis to close the benchmark gap identified in Section 3.

---

## Score and Decision — Calibration

**All retrieved anchors:**

| Path | Avg Score | Round | Comparison to paper |
|------|-----------|-------|---------------------|
| `x8mr9zGkpr.md` | 3.00 | R1 | Much weaker: shallow hyperparameter vs. data-complexity analysis with no novel methodology |
| `lvHHWDJCcr.md` | 3.40 | R1 | Much weaker: calibrated metric for deep learning model selection, underdeveloped |
| `XWfjugkXzN.md` | 1.67 | R1 | Far weaker: imperfect information game sampling, marginal contribution |
| `aoW5Sm8Op8.md` | 2.33 | R1 | Much weaker: survival model benchmark, narrow scope |
| `55EO8gSCBT.md` | 5.50 | R1 | Weaker: good experimental design paper for nonstationary optimization but less rigorously documented |
| `Q2bJ2qgcP1.md` | 6.00 | R1 | Weaker: CATE benchmark critique with observational sampling, less novel methodology |
| `kiwyQsZIGP.md` | 5.00 | R1 | Weaker: few-shot evaluation benchmark, narrower scope |
| `esh9JYzmTq.md` | 4.67 | R1 | Weaker: RL evaluation under distribution shift, less empirically complete |
| `uHLgDEgiS5.md` | 8.00 | R1 | Stronger: training data influence with trajectory-specific LOO, deeper theory |
| `EUSkm2sVJ6.md` | 7.60 | R1 | Stronger: dataset usage inference with optimal MLE algorithms and provable guarantees |
| `RvUVMjfp8i.md` | 8.00 | R1 | Stronger: rigorous SSL robustness evaluation with theory + extensive experiments |
| `KbetDM33YG.md` | 8.00 | R1 | Stronger: GNN evaluation under distributional shift, new theoretical framework |
| `yZ7sn9pyqb.md` | 6.00 | R2 | Slightly weaker: generative monoculture in LLMs, interesting empirical finding but narrower scope |
| `fN8yLc3eA7.md` | 6.00 | R2 | Slightly weaker: cultural transmission in LLMs, descriptive study with weaker evidence |
| `3OyaXFQuDl.md` | 7.00 | R2 | Comparable: compute-optimal sampling for LLM reasoning, solid empirical scope, novel insight |
| `IkmD3fKBPQ.md` | 6.75 | R2 | Slightly weaker: "LLMs Cannot Self-Correct Reasoning Yet" — similar critique spirit but relies on a single prompt, no original-author confirmation, presentation issues |
| `TzAJbTClAz.md` | 6.75 | R2 | Slightly weaker: FFB fairness benchmark, solid but narrower in impact |
| `IUmj2dw5se.md` | 7.50 | R2 | Slightly stronger: CEB benchmark for LLM bias, comprehensive multi-axis evaluation |
| `RSGoXnS9GH.md` | 7.00 | R2 | Comparable: FairMT-Bench for multi-turn dialogue fairness, solid empirical design |
| `E8gYIrbP00.md` | 6.75 | R2 | Slightly weaker: methodological paper on LLM-as-Judge evaluation with novel metrics but smaller scope |
| `7W3GLNImfS.md` | 6.50 | R2 | Weaker: human feedback reliability critique, valid but less rigorously documented than this paper |
| `rAoEub6Nw2.md` | 5.67 | R2 | Weaker: statistical framework for LLM chatbot ranking, methodological contribution only |
| `ARFRZh6pzI.md` | 6.00 | R2 | Weaker: metacognitive approach for LLM hallucination, engineering contribution |
| `ymt4crbbXh.md` | 6.25 | R2 | Weaker: AutoBencher declarative benchmark construction |

**Round 1 bracket**: 6.0 to 8.0.

**Round 2 narrowing**: The closest thematic comparators at 6.75 ("LLMs Cannot Self-Correct Reasoning Yet", "Beyond Correlation", "FFB") are all weaker than this paper: they lack the rigorous documentation via original-author confirmations, the empirical scope (~6000 A100-hours), and the verified factual findings. The paper is comparable to the 7.0 anchors ("Smaller, Weaker, Yet Better", "FairMT-Bench") in terms of empirical rigor and novelty of contribution. The GPQA gap and the primarily-critique (rather than constructive) nature of the work prevent it from reaching 7.5. The paper is better than all round-2 anchors at 6.75 and comparable to those at 7.0.

**Evaluation on key axes:**
- *Originality*: Moderate-high. The Best-of-N hyperparameter equalization is novel; the reanalysis framework is a valuable methodological contribution, though the individual lessons are standard.
- *Importance of research question*: High. Research rigor in high-visibility ML papers directly affects the field's direction.
- *Claims well-supported*: Very high. Central findings are confirmed by original authors or directly derivable from public data. The GPQA gap is the one incomplete piece.
- *Soundness of experiments*: High. Extensive sweep with strong controls; transparent about limitations.
- *Clarity of writing*: High. Well-organized, clear statistical argumentation, honest limitations section.
- *Value to research community*: High. The Best-of-N methodology and the documented case study are broadly applicable.

**Final Score: 7.0 — Accept**

MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>