## Summary

LPFQA is a benchmark of 505 questions derived from professional technical forums across 20 academic and industrial fields. Questions are collected via web crawling, transformed into multiple-choice or short-answer format using MLLMs, and verified by human experts. The paper evaluates 12 mainstream LLMs and reports that (a) all models score in a relatively narrow band (32–47), (b) adding a code interpreter generally hurts performance, and (c) web-search augmentation also tends to degrade accuracy, which the authors attribute to retrieval noise on long-tail topics.

## Strengths

- **Real-world grounding**: Questions originate from genuine user discussions on professional forums, which is a sound strategy for capturing authentic professional discourse and reducing artificial question design artifacts.
- **Informative ablations**: The code interpreter and web-search ablation experiments produce a concrete and counter-intuitive finding—external tool augmentation consistently degrades performance on long-tail knowledge—which is a potentially useful empirical observation for the community.
- **Broad coverage attempt**: Spanning 20 disciplines with expert verification is a genuine effort toward interdisciplinary evaluation.

## Weaknesses

### Fatal

- **Evaluation methodology for short-answer questions is never explained.** The paper states that short-answer items include "key knowledge points" as evaluation criteria, but never describes who or what grades model responses against those criteria—a human grader, an LLM judge, or string matching. For a benchmark paper, this is a fundamental omission that makes the reported scores uninterpretable.

- **Internal inconsistencies undermine reliability.** The abstract states "502 tasks," while Section 3.1 states "505 questions." The LPFQA<sup>=</sup> definition (Section 4.2.1) references "LPFQA<sup>+</sup>" as the base for exclusion, but LPFQA<sup>+</sup> is never defined anywhere in the paper. Figure 5 table has a clearly garbled entry ("2121") for the CS field under LPFQA<sup>-</sup> and LPFQA<sup>+</sup>. These errors collectively cast doubt on the correctness of reported numbers.

- **Performance analysis directly contradicts Table 1.** Section 4.1 states "DeepSeek-V3 demonstrates the most balanced and consistent performance across disciplines…and can thus be regarded as the overall best-performing model," yet Table 1 places DeepSeek-V3 second from the bottom (32.60), far below GPT-5 (47.28), Gemini-2.5-Pro (44.42), and o3-high (43.03). This contradiction suggests errors in the analysis or confusion between per-field radar charts and overall scores.

### Major

- **Dataset scale is too small for reliable per-field evaluation.** Several fields contain extremely few questions: Data Science (3 items), Aerospace (8), AI (8), ICE (7), Energy (9), EIE (10). Statistical conclusions about 3-item fields are meaningless. The benchmark does not report confidence intervals, so all per-field comparisons are potentially noise.

- **Score metric is undefined.** Tables 1–4 report "Score" values in the range 23–54 without ever defining the unit or aggregation method. Is this accuracy (%)? A weighted sum? A normalized rubric score? This must be clearly defined for the benchmark to be usable.

- **No evidence that LLM-generated questions are reliably valid.** The pipeline uses an MLLM to generate QA pairs from screenshots and another LLM to generate distractors. The paper does not report inter-annotator agreement for the expert verification step, nor the fraction of automatically generated questions that experts rejected or corrected.

### Minor

- The claim that forums yield "long-tail" knowledge is asserted but not empirically verified. Some professional forums may be heavily crawled during LLM pre-training. Without a contamination analysis, the long-tail claim is unsubstantiated.
- Fine-grained evaluation dimensions (knowledge depth, reasoning, terminology, contextual analysis) are advertised as a key contribution but no per-dimension breakdown is reported in experiments.
- The LPFQA<sup>-</sup> filtering (removing questions no model answered correctly) removes 69 items (~14%), and LPFQA<sup>=</sup> (removing questions all models answered correctly) removes another 15. Reporting both filtered and full results without clear motivation for the filtering makes the experimental section hard to interpret.

### Trivial

- Figure 2's y-axis label "Quality of items" should read "Number of items."

## Nice-to-Haves

- A contamination study showing that forum threads were not present in training corpora of evaluated models.
- Inter-annotator agreement statistics for the expert verification stage.
- A direct comparison showing LPFQA is more discriminative (e.g., by effect size or ranking-consistency metrics) than MMLU or HLE on the same set of models.

## Novel Insights

The ablation showing that both code-interpreter and web-search augmentation consistently degrade performance on forum-derived professional questions is a moderately interesting empirical finding: it suggests current retrieval strategies are misaligned with long-tail knowledge tasks. However, this insight is limited to a single (unverified) dataset of only 505 questions and lacks mechanistic analysis, so its generalizability is unclear.

## Suggestions

1. Clearly define the exact scoring formula for both multiple-choice and short-answer items, including the judge model/prompt if LLM-grading is used.
2. Reconcile all internal inconsistencies (502 vs. 505, undefined LPFQA<sup>+</sup>, the DeepSeek-V3 ranking contradiction) before resubmission.
3. Either expand the smallest fields (Data Science: 3, ICE: 7) to at least 20–30 items or merge them and refrain from drawing per-field conclusions.
4. Add a contamination analysis to validate the long-tail claim.
5. Report per-dimension scores (knowledge depth, reasoning, terminology, contextual analysis) to justify the fine-grained evaluation design as a contribution.

## Score and Decision

The paper addresses a genuine need (benchmarking LLMs on authentic professional long-tail knowledge), but its execution has critical methodological gaps: the scoring methodology for short-answer items is absent, multiple internal inconsistencies raise reliability concerns, the dataset's per-field sample sizes are too small for the claims made, and a major textual analysis claim directly contradicts reported numerical results. These are not minor presentation issues but substantive problems that prevent the reader from trusting the reported results.

MY FINAL SCORE: <score>3</score>
MY FINAL DECISION: <decision>Reject</decision>