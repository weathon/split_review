- Decision: Accept
- Avg Score: 6.00
- Scores: 6, 6, 6, 6
Here is my final consolidated review.

---

## Summary

This paper identifies a practical weakness in current LLM evaluation pipelines — brittle RegEx-based answer extraction — and proposes xFinder, a small fine-tuned LLM (trained on the KAF dataset) that extracts key answers from model responses and then matches them to ground-truth answers. On the KAF generalization set, the smallest xFinder (0.5B parameters) achieves 93.42% extraction accuracy vs. 74.38% for the best RegEx baseline (OpenCompass), while costing $0.02 per 200 samples versus $4.65 for GPT-4. The paper also compares xFinder's judgment accuracy favorably against judge models (PandaLM, JudgeLM, GPT-4) and demonstrates ranking inconsistencies in existing frameworks through a real-world evaluation of 10 LLMs on 14 tasks.

## Strengths

- **Large, consistent improvement in extraction accuracy over RegEx baselines.** Table 2 shows xFinder-qwen1505 achieves 93.42% extraction accuracy on the generalization set vs. 74.38% for the best RegEx method (OpenCompass) and 52.03% for GPT-4. This gap is large and directly supports the paper's core claim that xFinder substantially reduces extraction errors.
- **Dramatically lower cost and faster evaluation.** Tables 5–6 show xFinder-qwen1505 processes 200 samples in ~13 seconds at $0.02, while GPT-4 takes ~63 seconds at $4.65. This makes the approach practical for deployment at scale.
- **Thorough dataset construction with human validation.** Section 4.2 describes semi-automated annotation with self-consistency filtering, two rounds of manual re-annotation via Label Studio, and separate training/test/generalization splits. The generalization set uses 11 "entirely new" tasks with responses from 8 different LLMs, providing a reasonable test of out-of-distribution performance.
- **Robust performance across model scales.** Tables 1–2 show the 0.5B Qwen-based model is within ~0.5% of the 8B Llama3-based model on both test and generalization sets, indicating the task is learnable with small capacity and does not require expensive models.

## Weaknesses

### Fatal
None.

### Major

- **Judge-model comparison may reflect task mismatch rather than genuine inferiority.** The paper compares xFinder against PandaLM and JudgeLM on "judgment accuracy" (Section 5.2, Table 3). PandaLM and JudgeLM are designed for pairwise preference comparisons and scoring, not for determining whether a response contains the correct answer given a reference. The paper states only that "All judge models use prompts with reference answers" (Table 3 caption) but does not justify whether this is a natural task formulation for these models, nor does it provide the specific prompts used. GPT-4-as-judge for pointwise correctness is a more standard comparison and still shows a large gap (84.2% vs. 97.61%), but the PandaLM (51.9%) and JudgeLM-33B (78.13%) results could partially reflect the models being evaluated on a task they were never designed to perform. This does not undermine xFinder's core contribution — which is the improvement over RegEx — but the claim of "outperforming judge models" is overstated without a clearer justification of task fairness. The authors should either (a) provide the exact prompts used and argue why the task is reasonable, or (b) soften the claim.

### Minor

- **Real-world evaluation demonstrates stability but does not independently validate accuracy.** Section 5.3 shows that xFinder variants produce consistent rankings across tasks while RegEx frameworks produce wildly inconsistent ones (Figure 4). This convincingly demonstrates that RegEx frameworks are unreliable (RQ1). However, for RQ2 ("Is xFinder reliable?"), the argument relies on consistency between two xFinder variants plus a backward inference from the higher extraction accuracy on the KAF generalization set. Consistency between two variants of the same method does not guarantee that the shared ranking is correct — both could share systematic biases. The paper would be significantly strengthened by annotating a subset of real-world responses with ground-truth correctness to directly validate xFinder's judgments in this setting. This is a nuance, not a fatal flaw; the evidence for xFinder's extraction accuracy on the KAF generalization set is already strong, and the inference is reasonable.

- **No error analysis or limitations section.** The paper does not discuss what kinds of responses xFinder still fails on. Are there systematic failure categories (e.g., long CoT chains, numeric answers with units, ambiguous phrasing, out-of-domain answer types)? The paper also does not discuss acknowledged dependencies such as the need to know the answer type and answer range at inference time, or potential biases from the training data composition. A brief limitations paragraph or error analysis would increase user trust and guide future work.

### Trivial
None.

## Nice-to-Haves
- An ablation showing performance without the data augmentation techniques (simulating option changes and prompt-form substitution) would help quantify their individual contributions.
- Reporting variability across multiple fine-tuning seeds (even for one model size) would give readers a sense of result stability, though the large accuracy gaps make this unlikely to change conclusions.

## Removed Points
These points are flagged to be removed; treat them with caution.

- *Missing prompts for judge models / insufficient detail on generalization set composition*: These details are deferred to the appendix, which the parser strips from all papers. The original submission contains this information; this is not a valid criticism of the paper as submitted.
- *Lack of confidence intervals or statistical significance*: Single-run evaluation on large benchmarks is standard practice in this area. These are not methodological gaps.
- *"First systematic study" overclaim*: A scope-of-contribution framing issue, not a concrete weakness about method or evidence.
- *RQ3 (alphabet options) not backed by controlled experiment*: This is presented as an ancillary observation, not a core claim. Critiquing its lack of rigor goes beyond the paper's stated scope.
- *Speculation about data overlap between training and generalization LLMs*: The paper states the generalization tasks are "entirely new" and uses different LLMs; speculation about superficial feature learning is not grounded in specific evidence from the paper.

## Novel Insights
The harsh critic's observation about the Accuracy Gap analysis (Table 4) is genuinely insightful: xFinder's judgment accuracy is only ~2.4% higher than its extraction accuracy, while RegEx frameworks show gaps of 14–22%. This cleanly quantifies how much of the unreliability in existing frameworks stems from extraction errors versus downstream framework logic, and demonstrates that xFinder's extraction improvements directly translate to judgment improvements with very little additional error. This diagnostic is a nice contribution in itself, distinct from the raw accuracy numbers.

## Suggestions

1. **Provide the exact prompts used for judge-model baselines** and justify why the task (pointwise correctness determination with reference answers) is a reasonable evaluation for pairwise-preference models. If the prompts are already in the appendix (which was stripped), simply confirm this in the final version and, ideally, add a brief justification in the main text.
2. **Add a brief error analysis or limitations paragraph.** Even a few sentences describing systematic failure modes of xFinder on the generalization set (e.g., "most errors occur on math answers with LaTeX formatting" or "the model occasionally extracts the reasoning step instead of the final answer") would substantially improve the paper's trustworthiness.
3. **Annotate a small subset of the real-world evaluation responses** with ground-truth correctness. Even 200–300 examples from the 14 tasks would allow a direct validation of xFinder's judgment accuracy in the real-world setting, turning the stability demonstration into a concrete reliability claim.
4. **Tone down the claim about outperforming judge models** or clearly separate it from the core extraction contribution. The paper's main value is the improvement over RegEx, which is well-supported; the judge-model comparison is interesting but less rigorously established.
