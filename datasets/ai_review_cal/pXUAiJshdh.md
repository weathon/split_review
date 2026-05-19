- Decision: Reject
- Avg Score: 5.50
- Scores: 5, 6, 5, 6
Here is the consolidated final review.

## Summary

SciKnowEval introduces a large-scale benchmark (70,203 questions across biology, chemistry, physics, and materials science) for evaluating LLMs across five progressive levels of scientific knowledge: memory, comprehension, reasoning, discernment, and application. The authors evaluate 26 LLMs (proprietary, open-source general-purpose, and scientific) under zero-shot and few-shot settings, revealing that even the strongest proprietary models struggle with scientific reasoning and application tasks.

## Strengths

- **Systematic five-level evaluation framework covering abilities most prior benchmarks miss.** Table 2 (comparison with 11 benchmarks) shows SciKnowEval is the only benchmark covering all five levels simultaneously. Competing benchmarks typically cover at most three levels, and none jointly cover knowledge memory, comprehension, reasoning, safety discernment, and application across four scientific domains. This is a genuine gap that the paper fills.

- **Large-scale dataset with multi-source construction and deliberate quality control.** The dataset (70,203 questions) is substantially larger than comparable scientific benchmarks (SciEval: 15,901, ChemBench: 7,059, SciAssess: 1,579). The three-stage quality control pipeline (LLM screening → 5% human evaluation by two domain experts → LLM post-screening with failure-type analysis), described in Section 3.3, goes beyond typical crowd-sourced or single-pass generation.

- **Comprehensive evaluation of 26 LLMs with fine-grained per-task, per-level, and per-domain analysis.** Tables 3–6 and the accompanying discussion (Section 4.2) surface specific, actionable findings — e.g., GPT-4o achieves >85% on L1/L2 but struggles with SMILES and protein-sequence tasks; safety-level L4 reveals that GPT-4o often fails to reject harmful questions; Gemini1.5-Pro shows strong safety refusal rates (81.9% chemistry, 100% biology). This granularity is a genuine strength over benchmarks that report only aggregate scores.

- **Few-shot analysis demonstrates the benchmark's sensitivity to prompting strategies.** Table 5 shows 3-shot gains of 27–29% on fluorescence prediction for GPT-4o and Claude3-Sonnet, and similar large gains on β-lactamase prediction and other L3 tasks. These results provide concrete evidence that SciKnowEval can measure reasoning improvements beyond simple knowledge retrieval, confirming the benchmark's discriminative power.

## Weaknesses

### Fatal

None.

### Major

- **GPT-4o serves as both an evaluated model and the evaluator for protocol design generative tasks, creating a conflict of interest.** The paper acknowledges this in the conclusion (line 414: "we aim to optimize the assessment methods, such as by substituting GPT-4o with an open-source scientific LLM evaluator"), but treats it as a future cost-optimization, not a current validity concern. Specifically, for protocol design tasks in biology and chemistry (a non-trivial subset of L5 generative questions), the paper states: "we prompt GPT-4o to rate results from 1 to 5" (line 348). GPT-4o ranks #2 overall (Table 4, line 293), making it a direct competitor to the models it evaluates. While most generative tasks use objective metrics (BLEU/ROUGE for captioning, Tanimoto similarity for molecule generation, Smith-Waterman for protein design), the protocol design results are unreliable as presented. The paper should either replace GPT-4o with a neutral evaluator (validated against human judgments) or clearly separate protocol-design analyses from the rest.

- **OpenAI o1 evaluated on a non-representative, biased subset, with only qualitative findings in the main text.** The paper selects 1,775 questions "that GPT-4o-mini fails to answer correctly" (line 406). This selection strategy systematically biases toward questions where GPT-4o-mini is weak, and says nothing about o1's performance on the full benchmark or on questions GPT-4o-mini answers correctly. While quantitative results may exist in the appendix (referenced as Figure 4, stripped by the parser), the main text reports only qualitative findings and makes broad claims (e.g., "improvement of o1 in scientific knowledge memory, knowledge understanding, and knowledge application is limited"). Without full-benchmark results or at minimum a directly comparable subset (e.g., o1 vs. GPT-4o on the same 1,775 questions), these claims are not supported. This section weakens rather than strengthens the paper.

### Minor

- **Data contamination risk from refactored existing benchmarks is acknowledged but not addressed.** The paper refactors questions from MedMCQA, SciEval, MMLU, PubMedQA, and HarmfulQA using "question rewriting and option reordering" (line 136). These are surface-level transformations; models trained on the original benchmarks (which many evaluated models almost certainly were) may still recognize preserved factual content or reasoning patterns. The paper mentions this risk in one sentence without testing it. Quantifying the overlap (e.g., measuring performance drop when original vs. refactored versions are compared) would substantially strengthen the contamination defense.

- **Only 5% of LLM-generated questions undergo human evaluation, with no reported inter-rater agreement.** Two domain experts evaluate 5% of generated questions (Section 3.3). This is a reasonable sample size for a 70K dataset, but the paper does not report inter-rater agreement between the two domain experts or agreement between human evaluators and the LLM screening. Without these numbers, the reader cannot assess the reliability of the quality-control pipeline.

- **Level imbalance (55.93% L1) is acknowledged but not analyzed.** The overall ranking (Table 4) may simply reflect L1 performance, which dominates the dataset. A level-balanced score (weighting each level equally) would clarify whether the ranking captures genuine multi-level competence or is driven by the memory-level majority. The paper should report this alongside the current average-rank metric.

- **Average-rank metric discards magnitude information.** The paper uses average ranking across tasks as the final score (line 276). A model that is a close second on every task receives the same rank as one that is a distant second. Reporting raw scores or effect sizes alongside rankings would better inform readers about the practical significance of performance differences.

- **Claim about "incremental pre-training or fine-tuning on scientific corpus show promise" rests on only two model pairs** (Section 4.3, lines 402-403). The comparisons are uncontrolled for training data size, model family differences, and other factors. While plausible, this claim is not supported as a general finding.

### Trivial

- The few-shot table (Table 5) reports only performance deltas rather than absolute 3-shot scores, making it hard to assess the resulting performance levels. Including absolute scores alongside the deltas would be more informative.

## Nice-to-Haves

- **Provide a per-domain breakdown of the overall ranking** (e.g., separate tables for biology rank, chemistry rank, etc.). This would better serve domain-specific scientific LLMs and help readers understand specialization patterns.
- **Correlate SciKnowEval results with existing benchmarks** (SciEval, ChemBench, SciBench) to demonstrate that SciKnowEval reveals *different* or *complementary* insights rather than simply replicating the same rankings.
- **Validate the five-level taxonomy empirically** — e.g., by checking whether question difficulty (model accuracy) correlates with level as expected, or whether human experts agree with level assignments.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **"The philosophical framing (Confucius vs. Bloom's) is decorative rather than functional."** Removed because the five levels are concretely operationalized through specific task definitions (Section 3.1), evaluation criteria, and dataset construction. Whether the inspiration is Confucian or Bloom's is a stylistic choice, not a methodological weakness.

- **"Table 1 comparison is self-serving/factually unfair to other benchmarks."** Removed because the table is a factual comparison of benchmark properties. Claiming MMLU "lacks L2/L5" is not a criticism of MMLU — it is a factual statement about what MMLU covers, which is useful information for readers.

- **"Prompts are not provided in the main paper."** Removed. The parser strips appendix content from all papers; these exist in the original submission.

- **"Figure 4 (o1 results) is not in the provided text."** Removed. The figure is in the appendix, which was stripped by the parser.

- **"No quantitative results for o1 evaluation."** Removed. The paper explicitly states "Through analyzing the quantitative results and several cases" (line 407), indicating quantitative results are presented in the appendix figure. The text reports qualitative findings drawn from those results.

- **"Formatting nitpick about Table 5 improvement-column coloring."** Removed as a pure formatting issue.

## Novel Insights

The harsh critic and strength finder together surface a key tension that goes beyond the paper's own framing: the benchmark's most distinctive methodological innovation (using a five-level progressive taxonomy inspired by learning theory) is also its least-validated component. The paper assumes the levels are meaningful without testing whether they capture distinct latent abilities or simply reflect a difficulty gradient. Meanwhile, the practical evaluation — 26 LLMs, fine-grained per-task scoring, few-shot sensitivity analysis — is thorough and generates genuinely useful findings, such as the observation that proprietary models dominate knowledge memory (L1/L2) but show narrower gaps on reasoning tasks (L3), and that safety-level L4 reveals a "refusal gap" between models that correlates poorly with overall capability. The o1 analysis, despite its methodological flaws, hints that SciKnowEval may contain questions that differentiate even frontier models at the reasoning and safety levels — a property that could make the benchmark valuable for future tracking even if the current o1 evaluation is weak.

## Suggestions

1. **Replace GPT-4o as the evaluator for protocol design tasks** with a neutral evaluator (e.g., human evaluation on a sample, or an open-source LLM that is not among the evaluated models, validated against human raters). Report the correlation between the neutral evaluator and GPT-4o's ratings to characterize the bias.
2. **Run o1 on the full SciKnowEval benchmark** (or at least a random stratified subset) and report quantitative accuracy alongside GPT-4o and Claude3.5-Sonnet on the same questions. The current biased-subset analysis is uninformative.
3. **Add a level-balanced score** (weighting each of L1–L5 equally) alongside the current overall rank to address the 55% L1 imbalance.
4. **Quantify the contamination risk** by comparing model performance on original (from public benchmarks) vs. refactored versions of a sampled subset.
5. **Report inter-rater agreement** for the human quality-control evaluation and between human and LLM evaluators.
6. **Report absolute 3-shot scores** in Table 5 alongside the deltas, so readers can assess the resulting performance levels directly.
