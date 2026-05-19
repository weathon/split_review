- Decision: Accept
- Avg Score: 7.00
- Scores: 6, 6, 8, 8
Now I have a verified picture of the paper. Let me compile the consolidated review.

---

## Summary

RAPTOR introduces a tree-based retrieval system that recursively embeds, clusters, and summarizes text chunks to build a hierarchical index with multiple abstraction levels. At query time, it retrieves from this tree to provide context spanning both broad themes and granular details. Controlled experiments show modest but consistent gains over flat retrieval (SBERT, BM25, DPR) across NarrativeQA, QuALITY, and QASPER when using the same LLM. The paper also reports state-of-the-art results by pairing RAPTOR with GPT-4.

## Strengths

1. **Consistent controlled improvements across retrievers and datasets (Tables 1–3).** Augmenting SBERT, BM25, and DPR with the RAPTOR tree improves performance in nearly every condition tested with UnifiedQA-3B. Gains on NarrativeQA reach +4.4 ROUGE (BM25), and improvements on QuALITY (+1.6–2.2 points accuracy) are directionally consistent. This cross-retriever generality is the paper's strongest evidence — it shows the tree structure itself, not a specific retriever, drives improvement.

2. **Systematic selection of the collapsed-tree retrieval method.** Figure 2 compares tree traversal (varying top-k) against collapsed tree (varying token limits) on 20 QASPER stories and identifies collapsed tree at 2000 tokens as the best performer. The paper then uses this strategy throughout, demonstrating a principled design choice backed by pilot data rather than an ad-hoc decision.

3. **Qualitative illustration of multi-scale retrieval (Figure 3).** The Cinderella example concretely shows how RAPTOR selects nodes from different tree layers to answer thematic vs. detail-oriented questions, while DPR retrieves only leaf chunks. This provides intuitive support for the paper's motivation, even if the example is limited to one story.

4. **Novel and well-motivated approach.** The idea of grouping text chunks by *semantic similarity* (via clustering) rather than by *textual adjacency* (as in prior recursive summarization work) is a genuine conceptual advance, and the use of soft clustering to allow nodes to appear in multiple summaries is a thoughtful design choice for content that spans multiple topics.

## Weaknesses

### Fatal
None. The controlled experiments do demonstrate a real (if modest) signal, and the core idea is not invalidated by any single flaw.

### Major

1. **Misleading state-of-the-art claims that conflate RAPTOR's contribution with GPT-4's raw capability.** The paper claims SOTA on QuALITY (82.6% RAPTOR+GPT-4 vs. 62.3% CoLISA with DeBERTaV3-large) and QASPER (55.7% RAPTOR+GPT-4 vs. 53.9% CoLT5 XL). These comparisons do not control for the LLM — the previous SOTA systems used models orders of magnitude smaller than GPT-4. The 20-point jump on QuALITY is virtually certain to come primarily from GPT-4's reasoning ability, not from RAPTOR's retrieval. The paper's own controlled experiments (where LLM is held fixed) show gains of 1–5 points, which is the honest signal. Claiming "state-of-the-art" without disaggregating the LLM's contribution is misleading and undermines the reader's ability to assess the method itself. (Verifiable from Tables 4–5 vs. Tables 1–3; the SOTA tables use different LLMs across systems.)

2. **The layer-contribution analysis (Table 6) is run on a single story with no variance or statistical testing.** The paper presents results for "Story 1 from the QuALITY dataset" — one story — and concludes that "full-tree search outperformed retrieval strategies that focused only on specific layers." No sample size, confidence interval, or significance test is reported. The central claim of the paper (that multi-level summaries help) depends on this evidence, and one story is insufficient to support it. (Verifiable: Table 6 caption and surrounding text on lines 333–354.)

3. **No statistical significance measures or confidence intervals anywhere in the paper.** The controlled-experiment gains are generally modest (e.g., QASPER with UnifiedQA: <1 F1 point for all retrievers; QuALITY: 1.6–2.2 points accuracy). Without error bars, significance tests, or multi-run variance, the reader cannot determine whether these differences are meaningful or within noise range. This is particularly concerning for the smallest improvements (e.g., SBERT with RAPTOR on QASPER: 36.23% → 36.70%). (Verifiable: all tables report point estimates only.)

### Minor

1. **The clustering algorithm's `n_neighbors` variation is described without a concrete schedule.** The paper states "our algorithm varies `n_neighbors` to create a hierarchical clustering structure: it first identifies global clusters and then performs local clustering within these global clusters" (line 94). No specific values, ranges, or selection criteria for `n_neighbors` are provided, making this step irreproducible from the description alone. Combined with UMAP's stochasticity and the absence of code, key details of the tree construction are not replicable.

2. **Empirical support for the tree structure over a single extra summary layer is weak.** The controlled comparisons show that RAPTOR (tree with summaries) beats flat retrieval (raw chunks). But no experiment isolates whether the *multi-layer hierarchy* matters beyond simply having one additional summary layer. A simpler baseline — e.g., one layer of summaries on top of leaf chunks — would clarify whether the full tree is necessary. The single-story ablation (Table 6) attempts this but is too limited.

3. **Token budget control mechanism is stated but not fully documented.** The paper says "We provide the same amount of tokens of context to RAPTOR and to the baselines" (line 159). However, it does not specify how baselines select chunks up to this token limit (e.g., do they greedily take top-k until the limit is reached? Do they use a different procedure?). While the statement itself addresses the fairness concern, the lack of procedural detail leaves ambiguity about exactly what was done.

4. **No analysis of computational cost.** The paper asserts computational efficiency (line 70) but provides no time, token, or dollar-cost measurements for tree construction vs. standard indexing. Given that the summarization step requires API calls to GPT-3.5-turbo, a practical user needs to know whether the gains justify the cost.

### Trivial
- The hallucination rate for summaries (4%) is reported without details on annotation methodology, sample size, or definition of "minor hallucination."

## Nice-to-Haves
- An ablation where flat retrieval is given the same token budget but with raw chunks only (no summaries) to test whether RAPTOR's advantage comes from the *content* of summaries or simply from having more tokens of relevant text.
- A breakdown of QuALITY results by question type (thematic, detail-oriented, multi-hop) to test the hypothesis that higher layers primarily benefit broader questions.
- Failure-case analysis: when does RAPTOR underperform flat retrieval?
- Comparison against a long-context baseline (e.g., GPT-4 with the full document in context) to contextualize the need for retrieval at all.

## Removed Points

- **"Token budget ambiguity" as a critical concern.** The harsh critic argued that the comparison may be unfair because baselines might retrieve by chunk count while RAPTOR retrieves by token count. However, the paper explicitly states "We provide the same amount of tokens of context to RAPTOR and to the baselines" (line 159). This directly addresses the core concern. Demoted to Minor (point #3 above) for lacking procedural detail.
- **"Soft clustering justification missing."** The paper does justify soft clustering on line 80: "individual text segments often contain information relevant to various topics, thereby warranting their inclusion in multiple summaries." The critic's claim that this justification is absent is factually incorrect.
- **Generic area-of-concern sweeps.** Criticisms such as "the evaluation lacks rigor" (stated without specific anchor), "are confounders controlled?" (speculative), and "could the metric be measuring a proxy?" — these are framing questions rather than identified problems with specific evidence. Removed per filtering guidelines.
- **"LlamaIndex comparison experiments missing."** The paper discusses LlamaIndex in related work and identifies its limitation (grouping by adjacency). Requesting a direct experimental comparison is scope-creep; the paper's controlled experiments (vs. BM25, DPR, SBERT) are the appropriate evaluation for a general retrieval method. Additionally, the rule against demanding missing related-work comparisons applies.
- **Strength Finder item #2 ("new SOTA results with large margins")** — this directly conflicts with the verified Major weakness #1 above (the SOTA comparisons are not controlled for LLM). Per the rule "when a strength and weakness disagree, the weakness wins," this strength is dropped.

## Novel Insights

The reviews highlight a tension not fully resolved in the paper: the multi-layer tree is presented as the key contribution, but the controlled experiments only compare "RAPTOR (full tree)" against "flat retrieval (no tree)." No experiment cleanly partitions the benefit into (a) having summaries at all vs. (b) having a hierarchy of summaries. The single-story ablation suggests the hierarchy helps, but on too thin a basis to be convincing. This gap — between the claimed mechanism (hierarchical abstraction) and the actual evidence (RAPTOR as a black-box composite of tree construction + summarization) — is the paper's deepest weakness and would need to be addressed in a revision.

## Suggestions

1. **Reframe the SOTA claims** by either (a) including controlled SOTA comparisons with GPT-4 for both RAPTOR and DPR/BM25, or (b) clearly labeling the SOTA results as "with a much stronger LLM" and highlighting only the controlled comparisons as evidence for RAPTOR itself.
2. **Extend the layer ablation to the full QuALITY dataset** (or a substantial multi-story sample) with per-question breakdowns and statistical tests.
3. **Report confidence intervals or error bars** for all main experiments, ideally from multiple runs with different random seeds (UMAP is stochastic).
4. **Add a "one-summary-layer" baseline** — a variant with only leaf nodes + one layer of summaries (no hierarchy) — to isolate the benefit of multiple layers.
5. **Document the exact `n_neighbors` schedule** used in UMAP and release code to enable reproducibility.
