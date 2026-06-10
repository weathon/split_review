Now I have all the information needed. Let me produce the final consolidated review.

## Summary

This paper proposes SEK (Self-Explained Keywords), a training-free prompting technique for code generation. SEK uses an LLM to extract and explain low-frequency keywords from a problem description, ranks them using a frequency-based algorithm (KeyRank), and appends them to the prompt before code generation. Experiments across HumanEval(+), MBPP(+), and APPS with five LLMs show consistent gains (e.g., DeepSeek-Coder-V2 from 85.4% → 93.3% on HumanEval).

## Strengths

- **Compute-controlled comparison against Beam Search isolates the semantic benefit of SEK.** SEK requires two LLM invocations per problem. The paper compares against Beam Search with beam size 2 — which also generates two outputs per problem — and shows SEK outperforms it by 4.0% on HumanEval (Section 3.1, line 166). This controls for the extra compute budget and demonstrates the gains come from semantic enrichment, not broader decoding.

- **Ablation cleanly separates the contribution of KeyRank from the core extraction step.** Removing KeyRank causes a 2.4% performance drop on HumanEval for Mixtral-8×22B, yet even without ranking SEK still outperforms Default by 2.5% (Section 4.2, line 200). This two-level decomposition allows precise attribution of each component's contribution.

- **Three-tier keyword taxonomy grounded in empirical analysis.** The authors examined keywords extracted by two LLMs from APPS problems and found three categories (function 22.5%, general 59.9%, abstract 17.7%), giving the KeyRank ranking algorithm a data-driven foundation (Section 2.2).

- **Robustness tested across multiple demonstration sets and TF-IDF corpora.** The method consistently outperforms Default across three randomly generated demonstration sets and different corpora, showing the approach is not brittle to specific exemplar choices (Section 3.2, lines 201–202).

- **Diverse model selection.** The evaluation spans 5 LLMs across architectures (dense/MoE), sizes (21B–70B active), and openness (open/proprietary), supporting claims of generality.

## Weaknesses

### Fatal
None.

### Major

1. **Central causal mechanism (low-frequency keywords → failures → SEK fixes by explaining them) is asserted but not directly tested.** The paper never measures (a) whether problems that improve under SEK actually contain low-frequency terms, (b) whether the keywords SEK extracts are actually low-frequency, or (c) whether improvements correlate with the presence of such terms. The attention analysis (Section 4.2, line 203) examines one cherry-picked example ("nonagonal") and provides no aggregate evidence. The ablation shows that even without KeyRank, SEK outperforms Default — which is consistent with the simpler explanation that *any* relevant appended text helps. The paper does not run the control that would distinguish these explanations (e.g., appending generic paraphrases vs. keyword explanations). This disconnects the motivating narrative from the evidence, though it does not invalidate the practical contribution.

2. **SelfEvolve baseline comparison is unfair.** The paper removes the self-refinement module *and* benchmark-specific prompt templates from SelfEvolve (Section 3.1, line 133) — i.e., the core mechanisms of the original method. It then claims "SEK demonstrates a notable and consistent performance advantage over SelfEvolve" (Section 4.1, line 168). Comparing against a stripped-down variant of SelfEvolve and attributing the advantage to SEK's focus on low-frequency keywords is misleading. The authors should either run SelfEvolve as designed (including its refinement loop) or explicitly acknowledge the comparison is against an ablated variant and temper the claims accordingly.

### Minor

3. **GPT-4o-mini's performance degradation on HumanEval(+) is dismissed with an ad hoc explanation.** The paper attributes the decline to "built-in prudence" making the model "select more generic keywords" (Section 4.1, line 164), but provides no evidence for this conjecture. A method claiming general effectiveness should either analyze such failures with data (e.g., examining whether the extracted keywords are indeed different for GPT-4o-mini) or document the failure as a genuine limitation. The observation that CoT similarly fails contextualizes the issue but does not explain it.

4. **Variance not reported for APPS results.** Only 300 of ~5000 APPS test problems are sampled. The paper mentions "multiple experiments with different sample seeds" but reports no standard deviations or confidence intervals (Section 3.2, lines 120–122). A single point estimate on a sampled subset is insufficient.

5. **Full prompt templates for KeyExtract & Explain are not disclosed in the text.** Since the method is prompting-based, the prompts *are* the method. Figure 3 (Section 2) shows an overview but its caption states "The details in each step are omitted" (line 73). The actual prompts and few-shot examples should be fully specified for reproducibility.

6. **KeyRank heuristic ordering is justified only by intuition.** The ranking (abstract > general > function) is not tested against alternatives such as reverse order, alphabetical ordering, or a learned ranking (Section 2.2, line 91).

### Trivial

- No statistical significance tests for smaller differences (e.g., 0.8% on MBPP+). Standard for the field, but worth noting.

## Nice-to-Haves

- Add a control experiment where appended text is (a) a generic rephrasing of the problem or (b) plausible but irrelevant keywords, to distinguish "SEK helps via low-frequency keyword explanation" from "any relevant text helps."
- Provide a rough cost analysis (tokens/time) for the two-invocation overhead, so practitioners can weigh improvement against cost.
- Analyze GPT-4o-mini's extracted keywords to understand the failure case rather than speculating.

## Removed Points

- **"The main results table is not visible in the parsed text"**: A parsing artifact (the table is produced via `\input{Tables/main}`). The paper includes the table; it is not missing. Removed as a parser-error nitpick.
- **Criticism that the long-tail distribution claim lacks citations**: The paper cites multiple references for this (chen2024large, li2024dawn). Removed as factually incorrect.
- **"The paper needs an ablation where irrelevant or generic keywords are appended"**: This is a valid suggestion but was listed as a "Critical Issue" when it is more appropriately a nice-to-have control experiment. Moved to Nice-to-Haves.
- **Generic/misaligned concerns from the Strengths Finder**: None were generic enough to remove; all strengths were concrete and evidence-anchored.
- **Speculation that variance across APPS seeds "is expected"**: The paper's own text says "multiple experiments with different sample seeds" but reports no numbers, so the criticism is valid and retained as Minor.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. Directly test the causal mechanism: for each benchmark problem, measure whether improvement under SEK correlates with the presence of low-frequency terms in the problem description.
2. Either restore SelfEvolve's refinement module and run the comparison as designed, or clearly demarcate the ablated variant and adjust the comparative claims.
3. Release the full prompt templates in the paper for reproducibility — the prompts are the method.
4. Report variance across seeds for the APPS results.

## Score and Decision

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>