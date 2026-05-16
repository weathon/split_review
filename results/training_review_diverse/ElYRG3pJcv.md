Now I have all the information I need. Let me construct the final consolidated review.

---

## Summary

This paper proposes Retrieval-Augmented Reflection (RaR), a zero-shot prompting method that iteratively retrieves external information to verify and revise each intermediate chain-of-thought reasoning step before proceeding to the next. The core idea is to use retrieval not just once upfront but progressively — querying for each reasoning step, reflecting on whether the step contains errors, and refining it — then iterating on the full response. The method is evaluated across code generation (ClassEval, HumanEval, MBPP), mathematical reasoning (GSM8K, GSM-Hard), embodied task planning (Minecraft), and question answering (TriviaQA), showing consistent improvements over CoT, RAG, and several combined baselines.

## Strengths

- **Consistent and substantial empirical gains across diverse benchmarks**: Across tasks the paper reports double-digit relative improvements (e.g., +16.4% on ClassEval, +11.6% on GSM8K, +29.1% on embodied task planning in the abstract; +16.44% on TriviaQA). These gains hold across multiple base models (GPT-3.5, GPT-4, DeepSeek-Coder, Llama-3, Gemma), demonstrating the method is not narrowly task-specific.

- **Progressive, step-by-step revision mechanism is validated by ablation**: Tables 2 and 3 show that (a) RaR's iterative query refinement outperforms both single-retrieval (RAG-1) and full-CoT retrieval (CoT+RAG), and (b) causal (step-by-step) reasoning outperforms non-causal reasoning by 11.9 points in pass@1 on HumanEval. These ablations directly support the paper's stated design intuition.

- **Comprehensive scaling analysis across three dimensions**: Figure 2 systematically examines performance when scaling model parameters (2B → 70B), inference-time tokens (0–8k), and computation cost (API pricing). The token-scaling curve (Figure 2b) shows that RaR continues to improve with more tokens while self-consistency and RAG plateau or degrade, supporting the claim that RaR avoids long-context degradation.

- **Smaller models closing the gap with larger ones via inference-time computation**: Figure 2a shows RaR applied to an 8B model outperforming a 27B model using direct generation on TriviaQA, and Figure 2c shows RaR with GPT-4 exceeding OpenAI o1 at lower cost. This supports the paper's broader thesis about inference-time scaling as an alternative to parameter scaling.

## Weaknesses

### Fatal
None.

### Major

1. **Retrieval corpora for code and math benchmarks are not disclosed.** The paper specifies the retrieval source for QA (wiki pages) and embodied planning (Minecraft Wiki), but is silent on what corpus was indexed for code generation (ClassEval, HumanEval, MBPP) and mathematical reasoning (GSM8K). A brief footnote-reference to Guo et al. (2024) for "contamination risk" is not sufficient — the reader cannot assess whether the retrieval corpus could have contained solutions to or descriptions of the exact benchmark problems. If the corpus included the test sets, the method could be effectively cheating. This is a reproducibility and validity concern that needs explicit disclosure.

2. **Inconsistency between the abstract's headline numbers and the paper's reported results.** The abstract claims "+29.1% on embodied task planning," but the introduction reports "+2.2% on accuracy" for Minecraft (the only embodied planning task evaluated). The scaling experiments later report up to "+16.2%" for task planning with more tokens. The 29.1% figure in the abstract does not clearly correspond to any experiment described in the paper, and may mislead readers about the method's typical gains. The claim that "a small LM can surpass the performance of the LM with more than 10 times the parameters" is also not fully supported by the evidence presented (RaR on 8B outperforms Direct on 27B — a ~3.4× ratio, not 10×).

### Minor

3. **Token consumption is not controlled in the main results table.** Table 1 reports "best results under the given maximum token limitation," which means all methods share the same ceiling on tokens. However, actual token consumption within that ceiling is not reported. If RaR uses substantially more tokens than baselines within the same max budget, the improvements could partly reflect greater computation rather than superior reasoning per token. The token-scaling experiment (Figure 2b) partially addresses this on one benchmark, but the main table lacks this control. The paper's own data in Figure 2b shows RaR underperforming IRCoT at <2k tokens and only surpassing it at >4k, which reinforces this concern.

4. **Novelty delineation relative to existing iterative retrieval+reasoning methods is blurry.** IRCoT (Trivedi et al., 2022) already uses CoT to generate retrieval queries, and Self-RAG (Asai et al., 2023) retrieves and reflects on segments. The paper states its differences (step-by-step revision rather than full-CoT retrieval) but does not include a targeted controlled comparison showing RaR's specific design choices outperform reasonable variants of these closest competitors under equal token budgets. The general baselines in Table 1 are welcome but do not isolate the incremental design decisions.

5. **Causal-mask parallelism claim is unclearly supported.** The paper claims (Section 3.2) that "retrieval based on intermediate reasoning steps is parallelized through causal mask... enabling the generation of queries for different reasoning steps simultaneously." If each step's refined output depends on the previous step's refinement (as the causal design dictates), the queries cannot be generated in parallel — they must be sequential. This claim either needs clarification or removal.

6. **Ablation studies are limited to code benchmarks.** Tables 2 and 3 only cover HumanEval/HumanEval+. No ablation is conducted on math reasoning, embodied planning, or QA — tasks central to the paper's claims about general-purpose improvement. The ablation evidence is therefore narrower than the paper's scope.

7. **No variance or confidence intervals for most results.** Only the Minecraft result reports ±8.02%. For code generation (pass@k) and math accuracy, variance across samples is known to be non-trivial, and the absence of any uncertainty quantification weakens the reliability assessment.

8. **Query generation procedure is underspecified.** Algorithm 1 uses $\texttt{p}_{\texttt{query}}$ to generate retrieval queries from the input and intermediate thoughts, but it is unclear whether this is a separate LLM invocation, what prompt template is used, and how the query is formatted. This matters for reproducibility.

### Trivial

- The paper uses inconsistent notation in Algorithm 1 (mixing "$I$" and "$x$" for input, "$T$" and "$y^{\text{thought}}$" for thoughts).
- Partial notation errors appear in equations (e.g., "enb" instead of "emb" in the similarity formula).

## Nice-to-Haves

- A plot showing RaR performance as a function of the number of reflection rounds (1, 2, 3, ...) for each task class would directly support the paper's central scalability claim.
- A failure analysis discussing cases where retrieval degrades performance (e.g., misleading retrieved information) would add depth.
- Reporting standard deviations over multiple runs (e.g., 3 seeds) for the main results would strengthen statistical reliability.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **Criticism about missing creative writing results**: The paper mentions creative writing in the task list but does not present results. Per the guidelines, creative writing results could have appeared in a section stripped by the PDF parser (the parser removes appendices), so this criticism cannot be verified as an author error.
- **Criticism about missing prompts in appendix**: Similarly, full prompt templates may have been in a stripped appendix section.
- **Criticism that the repeated sentence in the limitations section is an author error**: The duplicated sentence about retrieved knowledge quality (appearing twice at line 178) is a parser artifact from PDF extraction, not an error in the original submission.
- **Criticism about QA results not appearing in Table 1**: The paper clearly states that Table 1 covers code, math, and planning, while QA results are separately reported in Figure 2(a). This is an intentional organizational choice, not a missing result.
- **Criticism that Figure 2b shows RaR underperforming IRCoT at <2k tokens without discussion**: The paper already explicitly discusses this trade-off in Section 4.3 ("RaR performs worse than methods like IRCoT when the number of tokens used is less than 2k...").
- **Strength from Strength Finder about "smaller models outperforming larger ones through inference-time scaling"**: The abstract's "10× parameters" framing overstates what the data shows (8B > 27B is ~3.4×). The core finding is valid but the 10× claim is not supported, creating a conflict between this strength and verified weakness #2. The underlying evidence (Figure 2a) remains positive, but the strength is moved here due to the overstatement conflict.

## Novel Insights

None beyond the paper's own contributions. The reviews surface the key tension between the paper's ambitious framing (abstract-level claims of +29.1% and 10× parameter ratios) and the more modest evidence in the main results (+2.2% on Minecraft, ~3.4× parameter outperformance). The most interesting unresolved question is whether RaR's advantage is primarily a matter of spending more tokens (as Figure 2b suggests — RaR only surpasses IRCoT above a 4k token threshold) or reflects genuinely better reasoning per token. The paper would benefit from explicitly characterizing this threshold rather than presenting the token efficiency as an unqualified strength.

## Suggestions

1. **Disclose the retrieval corpus for every task.** For code generation, state explicitly what repository of code was indexed and whether any HumanEval/ClassEval/MBPP problems appear in it. For math, state the source and whether GSM8K solutions are present. Without this, the results are not verifiably clean.
2. **Resolve the abstract inconsistency.** The +29.1% figure for embodied task planning does not match the +2.2% (main) or +16.2% (scaling) reported in the text. Ensure all numbers in the abstract are directly traceable to a specific table/experiment.
3. **Add a controlled token-budget comparison.** Re-run RaR and the closest baselines (IRCoT, Self-RAG, CoT+RAG) at several fixed token budgets (e.g., 1k, 2k, 4k, 6k) on at least one code, one math, and one planning benchmark, and report both performance and actual token consumption.
4. **Clarify the causal-mask parallelism claim.** Either explain how parallel query generation is compatible with causal step dependencies, or remove the parallelism claim.
5. **Extend ablation to at least one non-code task** (e.g., GSM8K or TriviaQA) to verify that the causal step-by-step design choice generalizes.

## Score and Decision

The paper addresses a genuine problem and presents a method that shows consistent improvements across diverse tasks with reasonable ablations. However, the evaluation has two serious unresolved issues: (1) the retrieval corpora for code and math benchmarks are undisclosed, creating an unquantified contamination risk, and (2) the abstract contains headline numbers that are inconsistent with or not clearly traceable to the reported experiments, suggesting overclaimed framing. These issues are fixable but require explicit correction rather than simple clarification. The token-budget concern and limited ablation scope are secondary but meaningful. The paper's core contribution — progressive stepwise retrieval-augmented revision — is plausible and supported by the ablation studies, but the evidence as presented falls short of fully convincing.

**Score**: 5.5

**Decision**: Reject (with encouragement to revise and resubmit after addressing the retrieval corpus disclosure, abstract consistency, and token-budget control)

MY FINAL SCORE: <pineapple>5.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>