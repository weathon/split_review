- Decision: Reject
- Avg Score: 4.00
- Scores: 3, 3, 5, 5
Now I have all the information I need. Let me compose the final consolidated review.

## Summary

This paper introduces PAS, a plug-and-play system that automatically generates complementary prompts (rather than rewriting the original prompt) by fine-tuning a small LLM on a quality-curated dataset of ~9,000 (prompt, complementary prompt) pairs. The pipeline uses clustering, quality filtering, and few-shot learning with golden examples to construct the dataset. The paper reports improvements over no-APE baselines and the prior BPO method across six LLMs on Arena-Hard, AlpacaEval 2.0, and its length-controlled variant, and includes a human evaluation across eight categories.

## Strengths

- **Novel formulation of prompt complementing instead of rewriting.** To my knowledge, existing APE methods modify/optimize the original prompt; PAS appends a complementary hint without altering the user's input. This is a genuinely new perspective in the automatic prompt engineering space.

- **Data efficiency is well-supported.** Section 4.3.1 and Figure 3 show PAS achieves its results with 9,000 fine-tuning pairs versus 14,000 (BPO), 77,000 (PPO), and 170,000 (DPO). The computed efficiency ratios (1.56×, 8.56×, 18.89×) are concrete and demonstrate a meaningful reduction in data requirements.

- **Flexibility is convincingly demonstrated.** Table 3 shows PAS satisfies all three criteria (no human labor checkmark, LLM-agnostic, task-agnostic), while BPO and all other APE methods checked fail at least one criterion. This is a clean, tabular comparison that supports the flexibility claim.

- **Ablation study is informative and well-executed.** Table 5 isolates the prompt selection module (degradation of −1.78 points when replaced with random selection) and the regeneration module (−3.80 points when removed). These are clear, directional results that confirm both components contribute to overall performance.

- **Fair-comparison results are positive.** Table 2, which uses the same base model (LLaMA-2-7B-Instruct) for both PAS and BPO, shows PAS outperforms BPO by an average of 3.41 points across all six target LLMs, with improvements in every individual case. This is the methodologically sound comparison and it still shows consistent gains.

## Weaknesses

### Fatal

None.

### Major

1. **The "no human labor" claim is significantly overstated and contradicted by details in the method section.**  
   The paper repeatedly asserts PAS requires "no human labor" (Contributions: "first to construct a curated prompt complementary dataset without human labor"; Table 3 checkmark; line 60: "our data generation process is entirely automatic and requires no human labor"). However, Section 3.2 (Algorithm 1) relies on "golden data" from BaiChuan Inc. — 4–5 few-shot examples per category that are human-curated — and Section 3.1 fine-tunes a classifier on 60,000 internally labeled human-annotated data points from BaiChuan Inc. The abstract uses the more careful phrasing "without requiring **additional** human labor," but the contributions and Table 3 drop this qualifier, making an absolute claim that the paper's own pipeline contradicts. A reader cannot assess the generalizability of the approach without understanding how much prior human effort went into these resources. This is the paper's central distinguishing claim next to BPO, and it is not accurately represented.

2. **The headline performance claim (6.09 points over BPO) is inflated by comparing different base models for PAS and BPO.**  
   Table 1 (the main results table) compares PAS fine-tuned on **Qwen2-7B-Instruct** against BPO fine-tuned on **LLaMA-2-7B-Instruct** — different base models with different capabilities. The paper itself acknowledges this choice (line 294: "We used Qwen2-7B-Instruct as the base model due to its outstanding performance"). The fair comparison using the same base model (Table 2) yields a more modest 3.41-point average improvement. Presenting 6.09 as the headline number in the abstract, introduction, and Table 1 caption while deferring the fair comparison to a separate table is misleading. The paper would be stronger if Table 2 were the primary result and the 6.09 figure were contextualized as "PAS with a stronger base model vs. BPO with a weaker one."

3. **The "state-of-the-art" claim is unsupported by insufficient baselines.**  
   The paper compares PAS to exactly one prior method (BPO). Other APE methods discussed in the related work — OPRO, APE, APO, ProTeGi, Auto-CoT — are never quantitatively compared on the same benchmarks. The paper dismisses some as "not task-agnostic" (line 357) but this is about data efficiency comparisons only; it does not excuse the absence of any performance comparison. Claiming "SoTA" requires demonstrating superiority over more than one prior method. The field would benefit from knowing how PAS compares to, e.g., APE or OPRO on these benchmarks.

### Minor

1. **Reproducibility is limited by reliance on proprietary data.**  
   The golden few-shot examples and the 60k-label classification training data are from BaiChuan Inc. and are not publicly available. The classification model fine-tuned on this internal data is not released. No code, model weights, or data release is mentioned. While some reliance on existing APIs/models is acceptable, the scientific contribution would be substantially stronger if the pipeline's key dependencies were reproducible by third parties.

2. **Human evaluation lacks crucial methodological details.**  
   The paper reports consistent improvements in full mark proportion, average score, and availability proportion across eight categories (Table 4), but provides no information about the number of evaluators, their qualifications, the task design, the instructions given, or inter-annotator agreement metrics. Without these, the results are difficult to interpret or compare to other works. The sample sizes implied by the percentage denominators (e.g., 24.14% suggests ~29 samples for "Analysis and Judgment") appear small, which increases the risk of annotation noise.

3. **Missing hyperparameter details.**  
   The quality threshold τ used for filtering (line 113) is never specified numerically. The number of regeneration iterations in the data generation loop is not reported. HNSW clustering parameters (number of clusters, similarity threshold) are omitted. While these are not fatal, they reduce the paper's precision and reproducibility.

### Trivial

- In Table 1, the column labeled "APE-model" has the confusing entry "PAS" for the PAS rows, but PAS is the overall system, not an APE model in the traditional sense; the base fine-tuning model (Qwen2-7B-Instruct) should be indicated here for clarity.
- Table 5's caption says "without the Prompt Selection Module and Prompt Complementary Data Regeneration Module" but the rows are labeled "wo prompt selection" and "wo regeneration" (not "wo both"), which is clear enough but the caption could be more precise.

## Nice-to-Haves

- An experiment using only publicly available data for the golden set and classification training, to establish a lower bound on performance when the proprietary resources are not available.
- Error analysis: how often does PAS degrade performance, and on which prompt types?
- Inference cost and latency analysis: the system adds a fine-tuned 7B model call before each query.

## Removed Points

- **"ProTeGi and OPRO are not task-agnostic, so they are not included in the data efficiency comparison"** — The harsh critic characterized this as a dismissive excuse. However, the paper does say this specifically about the *data efficiency* comparison (Figure 3), where the comparison is about training data volume. Methods that require task-specific training data genuinely cannot be compared on that axis. This is not a dismissal; it's a reasonable scoping. *Removed.*
- **"The ablation study does not test alternative selection strategies, e.g., random sampling"** — This is factually incorrect: Section 4.5 (line 510) explicitly states "we replace the prompt data selection module with **random prompt data selection**." The ablation does test this alternative. *Removed.*
- **"PAS sometimes matches the baseline exactly (e.g., 85.71% in 'Subjective Advice')"** — This refers to the availability proportion in one of eight human-evaluation categories. The full mark proportion and average score for that same category *do* improve. Selecting one flat sub-metric from one category and presenting it as representative is misleading. *Removed.*
- **"Missing related works"** — I cannot verify the existence of omitted citations, and the instruction prohibits mentioning missing related works. *Removed.*
- **Formatting nitpicks** (typos, grammar, whitespace, broken characters, garbled symbols) — These are parser artifacts, not author errors. *Removed.*
- **Strength Finder's generic/hollow strengths** (e.g., "this paper addressed an important problem," "the paper targets an interesting question") — These are not specific to this paper's evidence. *Moved here.*

## Novel Insights

Both reviewers identified the same core tension: the paper has a genuine technical contribution (prompt complementing as a new paradigm, a practical automated pipeline for generating complements, and strong empirical results) but systematically overstates its claims. The most interesting observation that emerges from the cross-review is that the paper's *best* argument is actually the fair-comparison Table 2 (3.41-point average improvement on the same base model) and its flexibility/ablation results — not the headline 6.09 or the "no human labor" checkmark. If the authors led with those more measured claims, the paper would be *stronger*, not weaker, because the claims would be airtight. The hype is actively hurting a solid technical contribution.

## Suggestions

1. **Recalibrate all claims.** Replace "no human labor" with "minimal prior human effort (56–70 golden examples, using an existing trained classifier)" or similar. Change the headline improvement from 6.09 to 3.41 (from the fair comparison) or clearly separate the two numbers with appropriate qualification. Replace "state-of-the-art" with "strong performance compared to BPO" unless additional baselines are added.

2. **Add at least 2–3 more baselines.** The paper must compare PAS to APE, OPRO, and/or APO on the same benchmarks to substantiate any broader "SoTA" claim. Even a subset of the benchmarks would be better than none.

3. **Release the golden data and the fine-tuned model weights.** The golden data is ~56–70 examples across 14 categories — small enough to share easily. The fine-tuned model weights would enable independent verification. This alone addresses the most serious reproducibility concern.

4. **Swap the primary and secondary results tables.** Table 2 (same-base-model comparison) should be the main results table; Table 1 can be supplementary, with clear explanation that PAS uses a stronger base model than BPO in that comparison.

5. **Report τ, regeneration iteration limits, and HNSW parameters in the main text or appendix.** These are small additions that significantly improve replicability.

6. **Add human evaluation details** (number of evaluators, instructions, inter-rater agreement, per-category sample sizes) or, failing that, downgrade the claims about human evaluation to "preliminary" or drop them.
