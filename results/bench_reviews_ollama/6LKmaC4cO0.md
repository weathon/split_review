Now I have a thorough understanding of the paper. Let me synthesize the final review.

Key issues to verify from the harsh critic:

1. **Unfair baseline comparison** - The critic claims GoR retrieves from a corpus that includes LLM responses while baselines only have original chunks. Looking at the paper, Eq. 3 (line 117-120) confirms: GoR expands the retrieval corpus with previously generated responses. Baselines (BM25, Contriever, DPR, etc.) only retrieve from original document chunks. However, Thought-Retriever also "saves the historical responses...to expand the retrieval corpus for future user queries" (line 360). So there IS one baseline that also expands the corpus. The question is whether a "flat" expansion baseline (Contriever + responses, no graph) is missing. This is a legitimate concern - it's hard to attribute improvements to the graph/GNN vs. the simple benefit of having a richer corpus.

BUT, looking more carefully, Thought-Retriever IS a baseline that expands the retrieval corpus with historical responses (as thoughts). It just doesn't model the graph correlations. So GoR vs Thought-Retriever already partially isolates whether the graph structure helps beyond just expanding the corpus. However, Thought-Retriever is not a direct "flat corpus expansion with full responses" - it saves "high-level thoughts" not full responses. So the criticism that a simple "Contriever over expanded corpus" baseline is missing has some merit, though it's partially addressed by Thought-Retriever's presence.

2. **Misleading characterization of supervision** - The abstract says "enabling seamless supervision signal backpropagation between reference summaries and node embeddings" (line 11). But the actual training uses BERTScore between nodes and source chunks (not reference summaries) for simulated queries. The paper does explain this in Section 3.3 (lines 143-144): the supervision comes from simulated query-chunk pairs. The abstract language is misleading. However, looking at line 392 (conclusion): "self-supervised reference summaries" - this clarifies it's self-supervised, not global reference summaries. The abstract phrasing is ambiguous at best.

3. **No evidence that graph structure provides benefit** - The "w/o train" ablation uses untrained GNN, not flat retrieval. There's no ablation testing whether simply adding responses to a flat retrieval corpus (no graph) matches GoR. Thought-Retriever partially addresses this but uses "thoughts" not full responses. This is a legitimate concern.

4. **GraphRAG not included as baseline** - The paper acknowledges this but excuses it due to computational cost. This is a fair weakness to note but the paper explicitly discusses why.

5. **ROUGE-only evaluation** - Legitimate minor concern about limited metrics.

6. **LLaMA-2-7b-chat as generator** - Minor concern about generator quality.

7. **Historical responses vs. simulated responses framing** - The intro talks about "historical user queries" but the method simulates them. This is noted in the paper itself (line 25 says "historical user queries" but line 44 says "leverage LLMs to simulate some user queries"). The framing is slightly misleading but the paper is transparent about simulation.

Let me now write the review.</think>Now I have a comprehensive understanding of the paper. Let me synthesize the final review.

## Summary

The paper proposes Graph of Records (GoR), a method that enhances RAG-based long-context global summarization by constructing a graph connecting retrieved text chunks to LLM-generated responses, then training a GNN (GAT) over this graph using a BERTScore-based self-supervised objective. The graph is built by simulating queries from random document chunks, performing RAG with those queries, and connecting each response to its retrieved chunks. At inference, the trained GNN produces node embeddings over this graph for retrieval. GoR is evaluated on four summarization datasets with ROUGE metrics.

## Strengths

- **The core idea of structuring LLM responses and document chunks into a graph is sensible and well-motivated**: The retrieve-then-generate paradigm naturally creates edges (query→retrieved chunks→response), and modeling these connections via GNNs is a reasonable way to capture multi-hop relevance for global summarization. As evidenced by consistent improvements over Thought-Retriever (Table 1), which also expands the retrieval corpus with responses but doesn't model inter-response correlations, there appears to be genuine value in the graph structure.

- **Insightful analysis of self-supervised vs. supervised training**: Section 4.4 and Figure 5 provide a meaningful explanation for why local simulated queries outperform global reference summaries as supervision—global summaries are semantically relevant to many nodes, causing high entropy and confused optimization. This empirical insight (further confirmed in Table 2 "w/ sup" rows) is a solid contribution.

- **Comprehensive ablation study**: Table 2 systematically removes training, contrastive loss, ranking loss, and in-batch negatives, showing that each component contributes. The GNN architecture comparison (Figure 3) across five architectures is also informative.

- **Lightweight training**: Only a 2-layer GAT is trained, running on a single RTX 3080, which contrasts favorably with heavier alternatives like GraphRAG.

## Weaknesses

### Fatal
None.

### Major

- **Missing critical ablation conflating corpus expansion with graph contribution**: GoR retrieves from a corpus that includes both original document chunks AND LLM-generated responses (Eq. 3, line 117-120), while all standard retriever baselines (BM25, Contriever, DPR, etc.) retrieve only from original chunks. This means headline improvements (e.g., 15% Rogue-L on WCEP) conflate the benefit of an enriched retrieval corpus with the benefit of graph-based retrieval. Thought-Retriever expands the corpus with "thoughts" (condensed representations), so GoR vs. Thought-Retriever partially isolates this, but it's not a direct comparison since Thought-Retriever modifies the representation, not just the corpus. The missing ablation—**Contriever retrieval over the same expanded corpus (original chunks + full LLM responses, no graph)**—would clarify whether the graph/GNN architecture itself provides meaningful value beyond simply having richer retrieval content. Without this baseline, attributing improvements to "sophisticated correlations" modeled by the graph (lines 30-31, 109) is not well-supported.

- **Misleading phrasing in the abstract about the supervision mechanism**: The abstract (line 11) claims the BERTScore-based objective enables "seamless supervision signal backpropagation between reference summaries and node embeddings." In reality, training uses BERTScore between node content and the source text chunk c_i^s that generated the simulated query—not global reference summaries. The paper itself shows that using global reference summaries as supervision degrades performance (Table 2, "w/ sup"). While Section 3.3 explains the mechanism correctly and the conclusion (line 392) uses "self-supervised reference summaries," the abstract's phrasing strongly implies a direct connection between global reference summaries and node embeddings that does not exist in the actual mechanism. This misrepresents the method's contribution.

### Minor

- **Train-test distribution gap**: The model is trained on simulated local queries (generated from single chunks) but evaluated on global summarization queries. While the paper argues self-supervised training works better than supervised training with global summaries, the fundamental question of how well local-query-trained models transfer to global summarization is not directly analyzed—e.g., evaluating retrieval accuracy on local queries vs. global queries separately.

- **Evaluation limited to ROUGE metrics**: No semantic metrics (e.g., BERTScore for output evaluation) or faithfulness/hallucination checks are reported, which is relevant for summarization. This is a minor gap given that ROUGE is standard in the field but insufficient for assessing semantic quality.

- **Simulated queries vs. real historical responses framing gap**: The introduction (line 25) frames the problem as leveraging "historical user queries and LLM-generated responses" from "a running RAG system," but the method simulates all queries from random chunks using Mixtral (line 103). This is a valid methodological choice, but the introductory framing implies a deployment scenario that differs from the actual setup.

### Trivial

- None.

## Nice-to-Haves

- A flat corpus baseline (Contriever over original chunks + LLM responses without graph structure) to isolate the graph's contribution from the corpus enrichment benefit, and/or an analysis of what fraction of retrieved nodes are original chunks vs. LLM responses at inference time.
- Evaluation with a stronger generator to test whether GoR's benefits persist when the base LLM is more capable.
- Inclusion of GraphRAG as an experimental comparison (acknowledged by authors as future work due to computational cost, but reporting cost trade-offs would be informative).

## Removed Points

These points are flagged to be removed, treat them with caution.

- **"GraphRAG must be included as a baseline"**: The harsh critic flags GraphRAG's exclusion as a structural weakness. While noting GraphRAG as a missing comparison is fair as a nice-to-have, the paper explicitly discusses this (lines 380-381) and GraphRAG operates under a fundamentally different paradigm (community detection + multi-stage summarization) making direct comparison a convenience, not a necessity. Downgraded to nice-to-have.

- **"LLaMA-2-7b-chat is a weak generator"**: Requesting stronger generators is a generic one-size-fits-all suggestion that doesn't threaten the core claims about retrieval improvement. Downgraded to nice-to-have.

- **"Lack of saturation analysis for number of queries"**: Figure 4 already provides scaling curves across four datasets; demanding saturation analysis is a detail beyond the paper's scope.

- **"ROUGE-only evaluation"**: Downgraded from harsh critic's framing; this is minor rather than major, as ROUGE remains the standard metric in summarization literature.

- **Strength Finder claim that GoR outperforms "12 baselines"**: This is technically true but partly reflects the enriched corpus confound noted above; adjusted in the strengths to acknowledge the caveat.

- **Strength Finder claim that the BERTScore objective "bridges the gap between reference summaries and node embeddings"**: This repeats the misleading framing from the abstract; removed as a strength since the actual mechanism uses source chunks, not reference summaries.

## Novel Insights

The paper's most interesting empirical finding is that self-supervised training with local chunk-level signals outperforms supervised training with global reference summaries (Table 2, Figure 5)—not because global supervision is conceptually wrong, but because global summaries are too semantically broad, creating high-entropy similarity distributions that confuse contrastive learning. This suggests a broader insight for retrieval-based summarization: localized, focused supervision signals may be more effective than global ones even when the target task is global, because they provide cleaner gradient signal for distinguishing relevant from irrelevant content.

## Suggestions

- Add a "Contriever + expanded corpus" baseline that retrieves from the same enriched corpus (original chunks + LLM responses) without the graph structure. This directly tests whether the GNN contributes beyond corpus enrichment and would significantly strengthen (or importantly qualify) the paper's claims.
- Revise the abstract to accurately describe the supervision mechanism—"self-supervised training signal between simulated query-chunk pairs and node embeddings" rather than "between reference summaries and node embeddings"—since the actual mechanism does not use global reference summaries for backpropagation.

## Score and Decision

The paper presents a well-motivated and reasonably executed approach, but its central claim—that graph structure and GNN-based correlation modeling improve summarization—is undermined by the absence of a flat corpus expansion baseline. Thought-Retriever partially addresses this but uses a different representation ("thoughts" vs. full responses), leaving the attribution of improvements to graph structure uncertain. The misleading abstract framing compounds this concern. The method may well work as claimed, but the evidence is currently insufficient to separate the benefit of a richer retrieval corpus from the benefit of the graph architecture. These are addressable issues—adding one critical baseline and correcting the abstract—but they are substantive enough to warrant revision.

MY FINAL SCORE: <pineapple>5.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>