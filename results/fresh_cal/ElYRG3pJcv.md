Now I have all the information needed to produce the consolidated review.

## Summary

The paper introduces Retrieval-Augmented Reflection (RaR), a zero-shot prompting strategy that interleaves retrieval-augmented generation with step-by-step chain-of-thought revision. RaR generates an initial CoT, then iteratively retrieves external knowledge to revise each intermediate reasoning step, followed by overall response refinement. The method is evaluated on code generation (ClassEval, HumanEval, MBPP), math reasoning (GSM8K, GSM-Hard), embodied task planning (Minecraft), and question answering (TriviaQA), showing consistent improvements over standard baselines on GPT-3.5-turbo and across other model families in smaller-scale comparisons.

## Strengths

- **Consistent improvements across diverse long-horizon tasks**: Table 1 (GPT-3.5-turbo) shows RaR outperforming all baselines on every benchmark reported — ClassEval (+16.4% pass@1), HumanEval (+4.7% pass@5), GSM8K (+11.6%), GSM-Hard (+3.0%), and Minecraft (+2.2% accuracy). The breadth of improvement across qualitatively different reasoning demands (code, math, planning) provides credible evidence that the method generalizes rather than excelling on a single task.

- **Superior scaling with inference-time computation**: Figure 2(b) (DeepSeek-Coder 6.7B on ClassEval) demonstrates that as inference tokens increase from ~2k to ~4k, RaR's performance continues to rise, while self-consistency and RAG plateau or decline. The paper's explanation — that RaR avoids long-context degradation by iteratively retrieving and reflecting rather than packing all tokens into a single context — is well-supported by the data.

- **Smaller models with RaR match or exceed much larger models**: Figure 2(a) shows RaR applied to Llama-3-8B achieving higher TriviaQA accuracy than the direct output of Gemma-2-27B and Llama-3-70B. This directly supports the paper's claim that RaR can substantially bridge the gap between model scales through inference-time computation alone.

- **Ablation confirms advantage of dynamic step-wise retrieval over static retrieval**: Table 2 shows RaR's iterative query construction outperforms both RAG-1 (query = question only, +8.7% pass@1 on HumanEval) and CoT+RAG (query = full CoT, +7.9% pass@5). This cleanly isolates the contribution of using evolving partial reasoning states as retrieval queries.

## Weaknesses

### Fatal
None.

### Major

- **Creative writing claimed as an evaluated task but no results are presented.** The abstract (line 4), introduction (line 19), related work (line 23), and conclusion (line 182) all list "creative writing" alongside code generation, math reasoning, and task planning as an evaluated domain. However, the entire experiments section evaluates only code generation, math reasoning, embodied task planning, and question answering. No creative writing benchmark, results, or analysis appears anywhere in the paper. This is a clear overclaim that undermines credibility. The claim should either be removed from all non-experimental sections, or creative writing results must be provided.

- **The o1 comparison is not adequately supported.** Figure 1 states RaR (with GPT-4) "achieve[s] better performance with less inference-time computation" than OpenAI o1, and Section 4.3 (line 161) repeats that RaR "exceed[s] that of openai o1." This comparison rests on a single benchmark (ClassEval). The paper provides no description of how o1 was configured (temperature, reasoning effort, max tokens, number of attempts), no discussion of whether o1 was used with its default reasoning budget, and no comparison on additional tasks. The cost calculation (Figure 2c) is also opaque regarding prompt vs. generation token pricing differences. A single-datapoint comparison of this kind does not support the conclusion drawn, and the claim is prominently featured in the paper's framing.

- **The "causal vs. non-causal" ablation (Table 3) does not isolate causal reasoning as claimed.** The causal method performs step-by-step iterative retrieval and revision. The "non-causal" method performs a single retrieval based on the initial thought, then generates the final answer in one pass (line 171). The comparison therefore confounds two factors: (1) iterative multi-step retrieval vs. single retrieval, and (2) causal (past-only) conditioning vs. non-causal conditioning. To isolate whether the *causal masking* matters, one would need to compare iterative revision with causal conditioning against iterative revision where each step can access future steps (the true non-causal variant). As presented, this ablation primarily demonstrates that multi-step iterative retrieval outperforms single-step retrieval — useful information, but not evidence for the causal reasoning mechanism the paper claims.

- **The main results table (Table 1) uses only GPT-3.5-turbo.** The abstract and introduction claim RaR works across "a various set of language models" (GPT-3.5, GPT-4, DeepSeek-Coder, Llama-3, Gemma). Evidence for other models is scattered: Figure 2(a) covers QA only across different model scales, and Figure 2(b) uses DeepSeek-Coder 6.7B on one benchmark (ClassEval). There is no main-table showing consistent improvements across the core benchmarks for a second model family. This weakens the claim of model-agnostic generality.

### Minor

- **No retrieval corpus is specified for code generation or math reasoning tasks.** Section 4.1 describes the retrieval corpus for Minecraft (Minecraft Wiki) and QA (wiki pages), but no source is given for the documents retrieved during code generation and math reasoning experiments (lines 134-135). Without this information, the experiments are not fully reproducible and it is unclear what external knowledge RaR benefits from on these tasks.

- **Abstract uses relative improvement (29.1%) for embodied task planning without clarification.** The abstract (line 4) reports "29.1% on embodied task planning." The introduction (line 19) reports "+2.2% on accuracy" for the same task, and the text (line 148) reports an absolute score of 76.67%. The 29.1% is a relative gain (2.2/≈7.6 ≈ 29%), but this conversion is not stated. Using the larger relative number without qualification is misleading, especially since all other improvements in the abstract (e.g., +16.4% on code generation, +11.6% on math) appear to be absolute percentage-point gains.

- **Most results lack variance or significance measures.** Only the Minecraft result (line 148) reports standard deviation. Without variance estimates for the remaining benchmarks, it is difficult to assess whether the reported improvements are statistically robust, particularly for smaller gains (e.g., +2.4% on HumanEval+, +2.5% on MBPP).

- **The "parallelized through causal mask" claim (line 80) is unclear.** The paper states that retrieval based on intermediate reasoning steps "is parallelized through causal mask, enabling the generation of queries for different reasoning steps simultaneously." It is not explained how causal masking enables parallel query generation for different steps in a sequential reasoning process, nor what architectural mechanism this refers to. This needs clarification.

### Trivial

- **Duplicate sentence in limitations section (line 178):** "Another limitation of this work is that the performance of RaR also relies on the quality of the retrieved knowledge" appears twice verbatim, which appears to be a copy-editing error.

## Nice-to-Haves

- **Explicitly distinguish basic RaR vs. Iterative RaR in experimental configuration.** The paper describes both in Sections 3.1 and 3.2, but it is not stated which variant is used as the default in Table 1. Reporting the average number of iterations and tokens consumed per task would sharpen the method's identity and help practitioners understand practical costs.
- **A direct comparison against Self-Refine (reflect without retrieval)** would more cleanly isolate the value of external knowledge versus purely internal iterative refinement, testing the paper's core claim.
- **A failure case analysis** showing when and why RaR degrades performance (hinted at by the low-token regime in Figure 2b) would strengthen the paper's own narrative.

## Removed Points

These points were considered but removed as either factually inaccurate, already addressed by the paper, or reflecting reviewer knowledge gaps rather than author errors:

- **"Missing ReAct baseline":** The paper cites Yao et al. (2022) in multiple locations and explicitly explains in Section 3.3 (line 110) that agent-based methods "are not directly comparable to standalone reasoning and generation methods like RaR" and are therefore excluded. This is a deliberate, justified scoping choice, not an omission.
- **"Method overstates novelty by claiming parameter-free improvement when baselines also share that property":** The paper's statement that RaR "does not require any modifications to the original model parameters" is a factual description of a property, not a novelty claim. The paper does not assert that this property is unique.
- **"Creative writing listed in related work but no experiments":** The related work mention (line 23) lists creative writing as a domain where RAG is commonly applied, not as an evaluation domain for this paper. Only the abstract, introduction, and conclusion claim creative writing as an evaluated task — this criticism is valid but belongs to the creative writing overclaim already listed as a Major weakness.
- **"Self-consistency and RAG baselines not fairly tuned":** This is speculative. The paper states (line 132) that baselines were scaled to stay within the same token limit by adjusting sample size and document count, which is a reasonable methodology. Without evidence of unfair tuning, this criticism lacks a concrete anchor.

## Novel Insights

The harsh critic's decomposition of the causal vs. non-causal ablation — specifically the observation that two factors (iterative retrieval and causal conditioning) are confounded — is a genuinely sharp methodological point that goes beyond surface-level critique. The critic correctly identifies that the paper's Table 3 tests whether *more retrieval iterations* help, not whether *causal masking in the reasoning process* helps. This insight would be useful for the authors: a properly controlled experiment would compare iterative revision with vs. without future-step visibility, holding the number of iterations constant.

None beyond the paper's own contributions.

## Suggestions

1. **Remove unsubstantiated claims**: Either remove "creative writing" from the abstract, introduction, and conclusion, or add the corresponding experimental results. Similarly, either substantially expand the o1 comparison (multiple tasks, controlled configuration, variance) or remove it.
2. **Fix the causal vs. non-causal ablation**: Relabel it as an ablation on "iterative step-by-step retrieval vs. single retrieval" or add a properly controlled experiment that isolates causal masking.
3. **Add a second model family to the main results table**: Even a subset of benchmarks run with Llama-3 or DeepSeek-Coder in the main table would substantiate the claim of model generality.
4. **Specify retrieval corpora for all tasks**: Code generation and math reasoning need a clear description of the document source used for retrieval.
5. **Convert all reported improvements to a consistent format**: Either use absolute percentage points throughout or clearly label relative vs. absolute gains.

## Score and Decision

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>