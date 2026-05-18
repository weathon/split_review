Now I have all the information needed. Let me write the consolidated review.

## Summary

RAPTOR proposes a novel retrieval-augmented method that recursively embeds, clusters, and summarizes text chunks to construct a hierarchical tree. At inference time, it retrieves from this tree to provide LLMs with context at multiple levels of abstraction. Controlled experiments on NarrativeQA, QASPER, and QuALITY show consistent improvements over flat retrieval baselines (BM25, DPR) when the language model is held fixed (1–10 points). When paired with GPT-4, it achieves new state-of-the-art results on QASPER (55.7% F1) and QuALITY (82.6% accuracy).

## Strengths

- **Novel retrieval architecture via recursive clustering + summarization**: The idea of building a tree by recursively clustering semantically (not adjacency-based) and summarizing text chunks is well-motivated and clearly described (Section 3, Figure 1). This directly addresses the limitation that flat retrieval misses multi-scale discourse structure. The qualitative Cinderella example (Figure 3) concretely illustrates how the tree adapts to different query types.

- **Consistent empirical gains across multiple retrievers and LMs in controlled settings**: The paper's controlled experiments (Tables I–III) compare each retriever (SBERT, BM25, DPR) with and without RAPTOR using the same reader and context length. RAPTOR outperforms its non-hierarchical counterpart in every configuration — e.g., on NarrativeQA, SBERT+RAPTOR achieves 30.87% ROUGE vs 29.26% without (Table I); on QASPER with UnifiedQA, DPR+RAPTOR gets 36.6% F1 vs 32.1% (Table III). These clean ablations isolate the retrieval structure's contribution.

- **System-level SOTA results on two of three benchmarks**: RAPTOR + GPT-4 achieves 82.6% on QuALITY (vs prior SOTA 62.3%) and 55.7% on QASPER (vs CoLT5 XL at 53.9%), representing genuine improvements on challenging QA benchmarks that require multi-step reasoning and whole-document understanding.

- **Principled comparison of two querying strategies**: The paper evaluates both tree traversal and collapsed tree retrieval on a QASPER subset (Figure 2), provides a clear rationale for why collapsed tree is more flexible (it retrieves at the correct granularity per question), and selects the better approach for main experiments.

## Weaknesses

### Major

- **No comparison against existing hierarchical retrieval/summarization methods that use adjacency-based grouping**: The paper claims (line 56) that adjacency-based methods like LlamaIndex "may still overlook distant interdependencies" and that RAPTOR's clustering addresses this. But the controlled experiments compare only against flat retrievers (BM25, DPR). The more informative comparison — RAPTOR vs a hierarchical method using adjacency-based grouping (e.g., LlamaIndex's recursive summarization of adjacent chunks, or a comparable variant) — is absent. The paper does compare against wu2021recursively on NarrativeQA, but that method uses only the root summary, so the comparison tells us that multiple layers help, not that clustering beats adjacency for the intermediate layers.

- **The linear scaling claim is unsubstantiated**: The paper states (line 70) that the system "scales linearly in terms of both build time and token expenditure" without any complexity analysis, wall-clock measurements, or empirical runtime data. Given that building the tree involves multiple rounds of embedding, UMAP dimensionality reduction, GMM clustering with BIC selection, and LLM-based summarization across the full corpus, this claim needs evidence. A potential adopter cannot assess feasibility for a corpus larger than the paper's datasets without cost information.

- **GPT-3 / GPT-4 experiments do not control for context token budget between RAPTOR and baselines**: The paper clearly controls for context length in the UnifiedQA experiments (400 tokens for all methods, line 159). However, for the GPT-3 and GPT-4 experiments (Table III on QASPER), the paper specifies that RAPTOR uses a collapsed tree with up to 2000 tokens but does not state the token budget for BM25 and DPR baselines in those same experiments. If the baselines get fewer tokens, the comparison conflates the effect of hierarchical structure with the effect of simply having more total context. This matters because the QASPER RAPTOR gains with GPT-3/4 (1.8–6.5 points over DPR/BM25) could partly reflect a token-count advantage.

- **Layer contribution ablation is shown for only one story from QuALITY**: Table VI reports a full-tree vs single-layer comparison for "Story 1" from QuALITY. The paper mentions an appendix (line 354), which was stripped by the parser, but the main paper's evidence that the tree hierarchy drives gains rests on this single data point. Without reporting — across the full dataset — how many layers the tree typically has, what fraction of retrieved nodes come from each layer, or whether higher-level summaries capture thematic information that leaf nodes miss, the claim that the tree structure (rather than just having more text or better leaf retrieval) is responsible for improvements remains inadequately tested.

### Minor

- **NarrativeQA SOTA claim is metric-selective**: The paper states it achieves "state-of-the-art results on three QA tasks" (line 30) and specifies "new state-of-the-art METEOR score" (line 292) for NarrativeQA. However, Table IV shows RAPTOR+UnifiedQA trails the prior best system (Retriever+Reader) on ROUGE-L (30.8 vs 32.0), BLEU-1 (23.5 vs 35.3), and BLEU-4 (6.4 vs 7.5). The METEOR gain (19.1 vs 11.1) is notable, but the broader framing of "state-of-the-art results" for NarrativeQA is misleading since 3 of 4 standard metrics are below prior best.

- **Querying strategy comparison uses only 20 stories from QASPER**: The choice of collapsed tree over tree traversal (Figure 2) is based on a single experiment on 20 stories. The paper does not report whether this advantage is statistically significant or replicates on other datasets. Given that all main results depend on this choice, a broader validation would strengthen confidence.

- **Clustering algorithm choices are not ablated**: The paper uses UMAP + GMM with BIC, acknowledges that the Gaussian assumption is not ideal for text data (line 107), but provides no experiment comparing against simpler alternatives (e.g., agglomerative clustering or k-means on raw SBERT embeddings). Since clustering is a core component, the method's sensitivity to this choice is unknown.

- **Summarization quality analysis is superficial**: The paper reports a 4% hallucination rate and claims "no discernible impact on question-answering tasks" (line 113) without any measurement or experiment to support this. Replacing GPT-3.5-turbo with a smaller open-source summarizer to quantify dependence on summarization quality would be informative.

### Trivial

- None — no formatting, typo, or presentation issues detected from the paper content.

## Nice-to-Haves

- A comparison of RAPTOR against a variant that uses adjacency-based grouping (e.g., LlamaIndex-style summarization of consecutive chunks with retained intermediate nodes) under the same experimental conditions would directly test the paper's core claim that semantic clustering beats adjacency.
- Running the layer ablation across the full dataset (not one story) with token-count-controlled comparisons (all-leaf retrieval at the same token budget as collapsed tree) would strengthen the claim that hierarchy, not just more context, drives gains.
- Reporting wall-clock tree-build time and token expenditure for at least one dataset would substantiate the linear-scaling claim.
- Statistical significance tests (or confidence intervals) for the main controlled comparisons would help assess whether the 1–5 point improvements are reliable.

## Removed Points

The following criticisms from the Harsh Critic were evaluated against the paper text and removed per review guidelines:

- **"SOTA claims inflated by a language model confound"** — The paper clearly separates controlled experiments (same LM, same token budget) from system-level SOTA results. The 20% QuALITY improvement is explicitly attributed to "RAPTOR retrieval with the use of GPT-4." The controlled experiments (Tables I–III) isolate the retrieval contribution cleanly. The criticism conflates two types of claims the paper already distinguishes.

- **"The paper never reports whether RAPTOR + UnifiedQA beats CoLISA on QuALITY / CoLT5 XL on QASPER"** — These are cross-system comparisons with different architectures and model sizes. The paper's SOTA claims on QuALITY and QASPER are specifically with GPT-4. The UnifiedQA controlled experiments serve to isolate the retrieval contribution against fixed-LM baselines, not to claim SOTA. Asking for RAPTOR+UnifiedQA vs CoLISA is asking for a comparison outside the paper's stated scope.

- **"The controlled UnifiedQA gains could come simply from having more text"** — This is directly contradicted by line 159: "For experiments with the UnifiedQA model, we provide 400 tokens of context... We provide the same amount of tokens of context to RAPTOR and to the baselines." Token budget is explicitly controlled.

- **"Improvement could wholly reflect having more contextual text"** — For UnifiedQA experiments, this is factually wrong (token budget controlled). For GPT experiments, the concern is valid and is kept in the Major section above as a qualified version of this criticism.

- **"Missing hyperparameters: n_neighbors ranges, BIC threshold, etc."** — These are trivial implementation details impractical to include in a submission (parser artifact rule applies).

- Various formatting/reproducibility nitpicks that violate the hard rules about parser artifacts, missing appendix, etc.

## Novel Insights

None beyond the paper's own contributions. The reviews surface the predictable tension between system-level SOTA results (which are attention-getting but conflate multiple factors) and controlled ablations (which are clean but show smaller gains). This does not reveal anything about the paper's specific method beyond what the authors already report.

## Suggestions

1. **Add a direct comparison against an adjacency-based hierarchical baseline** (e.g., LlamaIndex-style recursive summarization of consecutive chunks, with intermediate nodes retained). This directly tests the paper's central claim that semantic clustering is superior to adjacency-based grouping.
2. **Report the token budget for BM25 and DPR baselines in the GPT-3/GPT-4 experiments**, or run a token-controlled ablation that matches RAPTOR's 2000-token context for flat baselines on a subset.
3. **Provide empirical runtime and token-cost measurements** for tree construction on at least one dataset to support the linear-scaling claim.
4. **Expand the layer ablation to the full test set** (not one story) with a token-controlled comparison — e.g., all-leaf retrieval at the same token budget vs. collapsed tree — to confirm that hierarchy, not just more tokens, drives the improvement.
5. **Adjust the NarrativeQA framing** to state clearly that SOTA is achieved on METEOR specifically (which the paper does in the body) and avoid implying blanket SOTA.

## Score and Decision

MY FINAL SCORE: <pineapple>5.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>