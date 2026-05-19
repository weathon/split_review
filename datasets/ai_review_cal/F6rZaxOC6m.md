- Decision: Reject
- Avg Score: 6.00
- Scores: 6, 6, 6, 6
Now I have a thorough understanding of the paper and can verify the reviewer claims. Let me compose the final consolidated review.

---

## Summary

KnowTrace proposes a structured RAG paradigm for multi-hop question answering that treats the LLM as an active knowledge organizer. Rather than accumulating unstructured text or performing costly restructuring decoupled from reasoning, KnowTrace iteratively builds a question-specific knowledge graph through an explore-then-complete loop. It additionally introduces a knowledge backtracing mechanism that leverages the acquired KG to filter irrelevant generations from correct trajectories, enabling more effective self-taught finetuning. Experiments on HotpotQA, 2WikiMultihopQA, and MuSiQue show consistent improvements over strong baselines across two LLMs and three retrievers.

## Strengths

- **Novel integration of knowledge structuring with iterative reasoning.** Unlike restructuring-based RAG methods (SG-Prompt, ERA-CoT) that separate structuring from reasoning, KnowTrace interleaves them in a coherent explore-then-complete loop (Section 3.2). This design eliminates the need for a separate, costly restructuring phase and retains question-specific reasoning guidance during KG construction. Table 1 shows KnowTrace outperforms ERA-CoT by 4.3 % (LLaMA3) and 4.5 % (GPT-3.5) average absolute EM.

- **Backtracing-guided self-improvement is empirically effective.** Section 3.3 describes a post-hoc mechanism that uses the acquired KG to trace back from entities in the verified correct chain-of-thought, filtering out irrelevant retrievals and completions. Figure 2(a–c) shows KnowTrace* (with backtracing) steadily improves across self-training iterations, while the vanilla self-improvement baseline degrades. The FA ratio analysis (Figure 2(d–f)) reveals that >10 % (up to 26.7 %) of tokens in correct trajectories are irrelevant, quantifying a previously underexplored problem in multi-step self-training.

- **Consistent gains across diverse configurations.** Table 1 demonstrates KnowTrace surpasses six baselines (IRCoT, ReAct, Self-Ask, Iter-RetGen, SG-Prompt, ERA-CoT) on three datasets using both LLaMA3-8B-Instruct and GPT-3.5-turbo-instruct. Table 2 extends this to BM25, DPR, and Contriever, showing the approach is robust to retriever choice.

- **Systematic analysis of KG prompting strategies.** Table 3 compares KG-to-Triplets, KG-to-Paths, and KG-to-Text. The structured triplet format outperforms both path-based (which duplicates information) and natural-language-converted formats, providing direct evidence that the KG's structured presentation matters for LLM reasoning—not just the information content. This is a clean ablation that supports a core design claim.

## Weaknesses

### Fatal

None.

### Major

- **No statistical significance measures or confidence intervals.** The test set contains 500 randomly sampled questions per dataset (Section 4.1.1). With 500 samples, a 5–7 % EM difference could arise from sampling variance, yet the paper reports only point estimates without confidence intervals, bootstrap estimates, or significance tests (e.g., McNemar). The consistent gains across datasets/LLMs/retrievers and the use of greedy decoding (temperature 0) partly mitigate this concern, but the lack of any error bar means the reader cannot assess how much of the reported advantage is statistically reliable. This is an evidential gap that weakens confidence in the headline numbers.

- **The causal role of the structured KG presentation is not fully disentangled from the iterative retrieval procedure.** The paper claims the explicit KG "directly facilitates LLM's inference" (abstract), but the only ablation isolating structure from content is the KG-to-Text comparison in Table 3, which uses an additional LLM call for conversion (introducing a confound). The paper does not report triplet extraction accuracy (precision/recall against ground-truth knowledge or the retrieved passages), nor does it analyze whether the KG causally shifts the LLM's reasoning patterns vs. being ignored in favor of raw passage text. The improvement could partly arise from the iterative retrieval strategy itself, the fine-grained decomposition into entity-relation queries, or the additional LLM calls for extraction—not solely from the *structured* nature of the KG. A cleaner ablation (e.g., feeding the same triplets as unstructured text without an extra LLM call) would strengthen the core causal claim.

### Minor

- **Backtracing filtering quality is measured only by a proxy (FA ratio), not directly validated.** The FA ratio (Figure 2(d–f)) shows the fraction of tokens filtered but does not verify whether the retained subgraphs are causally responsible for the correct answer or whether the filtered tokens are genuinely irrelevant. The performance improvement of KnowTrace* over the non-backtracing version (Figure 2(a–c)) provides indirect empirical validation, but a manual inspection of filtered vs. retained content would strengthen confidence in the mechanism's correctness.

- **Self-improvement experiments are limited to one LLM (LLaMA3-8B-Instruct).** Given the paper's claim that backtracing is a general advantage (Section 3.3), evaluating on only one model leaves open whether the benefits transfer to other LLMs (e.g., GPT-3.5-turbo-instruct, which is used in the inference experiments but not in self-training).

- **No computational cost comparison.** KnowTrace uses multiple LLM calls per question (one exploration call per iteration, one completion call per entity-relation pair). A comparison of token usage or wall-clock time against the strongest baselines (IRCoT, ERA-CoT) would help readers assess the practical trade-off between accuracy gains and compute overhead.

- **No failure analysis or breakdown by question difficulty.** The paper reports only aggregate EM/F1. A breakdown by number of reasoning hops, retrieval difficulty, or question type would reveal boundary conditions where KnowTrace may underperform and would improve understanding of when the method is most beneficial.

- **No discussion of failure modes in knowledge exploration.** The exploration phase (Section 3.2) relies on the LLM to propose plausible entity-relation pairs for retrieval. The paper does not discuss what happens when the LLM hallucinates a relation that does not exist in the corpus, leading to wasteful retrievals. This is a practical robustness concern worth acknowledging.

### Trivial

- The observation that "ERA-CoT degrades with more passages" (Section 4.4) is attributed to "lack of explicit reasoning guidance," which the paper itself frames as speculative ("we attribute to"). This is a minor interpretive point, not a weakness.

## Nice-to-Haves

- Reporting confidence intervals (e.g., via bootstrap over the 500 test samples) would greatly increase confidence in the reported gains without changing the experimental setup.
- A human evaluation of a random sample of extracted triplets (precision/recall against the source passages) would directly validate KG quality.
- A breakdown of performance by question type or number of hops would reveal boundary conditions.
- A token-cost or wall-clock comparison against the strongest baselines would help practitioners assess deployment trade-offs.

## Removed Points

- **Criticism about "4 in-context examples shared across all datasets as a potential confound."** Using the same examples across all datasets is standard practice for fairness in evaluation, not a confound. The shared examples make comparisons cleaner, not less reliable. This point is removed as a strawman.

- **"The method's claimed mechanism is never validated" (from the Harsh Critic's #2).** This is overstated. The paper does provide validation via the KG-to-Text comparison in Table 3, which compares structured triplets against natural-language descriptions of the same triplets. While this ablation is not perfectly controlled (it involves an extra LLM call), it is a form of validation that the critic's framing ignores. The criticism is retained in weakened form under Major weaknesses.

- **Criticism that the backtracing mechanism has a "fundamental reliability issue" (from Harsh Critic's #3).** This concern is theoretically plausible but the paper provides strong empirical evidence that backtracing helps: Figure 2 shows KnowTrace* consistently improves while the non-backtracing version degrades. The paper also uses ground-truth answers to validate the final [t,a] before backtracing. The criticism is retained in weakened form under Minor weaknesses (regarding FA ratio as a proxy).

## Novel Insights

None beyond the paper's own contributions. The reviews converge on the paper's core contributions (structured KG tracing during iterative RAG, backtracing for self-improvement) but do not identify fundamentally new angles beyond what the paper already presents.

## Suggestions

The paper would benefit most from two targeted additions that directly address the major weaknesses without changing its scope: (1) report bootstrap confidence intervals on the test-set EM/F1 scores for the primary comparisons in Tables 1 and 2—this is a minimal addition that would substantially increase confidence in the reported gains; (2) add an ablation that feeds the same extracted triplets as natural sentences (without an additional LLM conversion step) to more cleanly isolate the benefit of structured presentation from the benefit of the triplets' content. These are depth-oriented improvements that would solidify the paper's core causal claims without requiring new datasets or experiments beyond what is already reported.
