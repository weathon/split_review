- Decision: Reject
- Avg Score: 4.25
- Scores: 6, 3, 5, 3
Now I have all the information I need. Let me construct the final meta-review.

## Summary

HiReview proposes a two-stage framework for automatic literature review generation (LRG) that first retrieves a relevant citation subgraph via graph-context-aware scoring (BM25 with neighbor aggregation), then jointly learns a hierarchical taxonomy tree through soft-to-hard graph clustering and a fine-tuned LLM topic generator, and finally generates review content guided by that taxonomy. The core idea—using citation network structure to produce a hierarchical organization before generating text—is well-motivated and the ablation study convincingly demonstrates that removing the graph retrieval, clustering, or taxonomy each degrades performance.

## Strengths

- **Graph context-aware retrieval (Section 4.1).** The paper proposes a simple but effective extension of BM25 that aggregates neighbor relevance scores via a weighted sum. The ablation study (Table 2) shows that removing this module causes Coverage to drop from 0.9163 to 0.6705 and Relevance from 0.9428 to 0.7073, demonstrating its critical role in filtering out irrelevant papers.

- **Hierarchical clustering with soft-to-hard transition (Section 4.2.1).** The method addresses the specific structure of scientific taxonomies by allowing overlapping clusters at the base level (since a paper can belong to multiple subtopics) and enforcing disjoint clusters at higher levels. Table 3 shows this approach substantially outperforms K-means and LLM-based clustering alternatives.

- **Taxonomy-then-generation framework (Sections 4.3–4.4).** The paper demonstrates that generating a hierarchical taxonomy from citation structure before content generation produces better reviews than the outline-then-generation paradigm (AutoSurvey). Table 1 shows improvements on Coverage (0.9163 vs. 0.8646), Structure (0.9484 vs. 0.9122), and Relevance (0.9428 vs. 0.9093), all with lower variance.

- **Curated dataset (Section 5.1).** The paper constructs and releases a dataset of 518 literature reviews with extracted hierarchical taxonomies and 2-hop citation networks (averaging ~6,658 papers, ~11,633 edges), providing a benchmark and training resource for the community.

## Weaknesses

### Fatal
None.

### Major

1. **No human evaluation or factuality verification for claims of "factual accuracy."** The paper's central claim includes "superior hierarchical organization, content relevance, and factual accuracy" (abstract, line 4). The evaluation relies entirely on LLMScore (an LLM judge, including GPT-4o—the same model used as HiReview's content generator) and BERTScore. No human evaluation, citation grounding metric, or factuality-specific verification is provided. While the paper cites AutoSurvey's finding that LLMScore correlates with human preferences, a claim of *factual accuracy* requires direct evidence. Additionally, the "Human-written" row in Table 1 is set to 1.0000 across all metrics with no explanation of how these normalized scores are computed, making the absolute scale of the reported numbers uninterpretable. This combination of evaluation gaps weakens the paper's strongest claims.

### Minor

2. **Clustering accuracy metric undefined (Table 3).** The column heading reads "Accuracy" with no definition—it is unclear whether this measures exact tree match, cluster purity, hierarchical NMI, or some other criterion. Without a defined metric, the clustering contribution (a core component of the paper) cannot be rigorously assessed.

3. **Missing key hyperparameters for reproducibility.** The following parameters appear in the method but are never reported: α (Eq. 1, neighbor relevance weight), p_τ (Eq. 4, edge connection threshold), λ_l (Eq. 9, level-specific loss weight), τ (Eq. 9, temperature), number of hierarchy levels L, GNN depth, hidden dimensions, learning rate, and LoRA rank. These gaps hinder reproducibility.

4. **Ambiguous training description.** The sentence "After pre-training GNN_θ, we fix θ, φ and then jointly fine-tune GNN_θ and PLM_Θ" (line 181) is contradictory—fixing θ and then fine-tuning GNN_θ cannot both hold. The intended two-stage procedure (pre-train clustering → fine-tune for generation) is clear in spirit, but the notation needs correction.

5. **Ground-truth taxonomy extraction methodology unstated.** The paper says taxonomies were "extracted" from 518 review articles (line 199) but does not specify whether this was done manually, via section-header parsing, or through some other procedure. The reliability of the ground-truth taxonomy labels—which directly supervise the clustering and topic generation—cannot be assessed without this information.

6. **Positive sampling for hierarchical contrastive loss underspecified.** The loss in Eq. 9 requires positive samples S_l(u) (nodes in the same cluster at level l). The paper does not explain how these ground-truth cluster assignments at all hierarchical levels are obtained given that only "a small portion of the citation network has been labeled" (line 171). If positive samples are derived from the clustering itself, the loss risks circularity.

7. **Baseline input parity not explicitly controlled.** It is unclear whether AutoSurvey received the same retrieved paper pool as HiReview or used its own independent retrieval. If the results reflect differences in the retrieval stage rather than the taxonomy, the source of gains is confounded. The paper should clarify whether all methods were compared on the same paper subset or, ideally, include a controlled experiment.

8. **No statistical significance tests.** Table 1 reports standard deviations but no significance tests (e.g., paired bootstrap or t-tests) are conducted for the main comparisons against AutoSurvey.

### Trivial
None.

## Nice-to-Haves

- An ablation of the neighbor-weighting parameter α to justify the chosen value (or to show that the method is robust to it).
- A qualitative example showing a generated taxonomy tree alongside the ground-truth tree from a source review for visual comparison.
- Direct retrieval accuracy metrics (e.g., precision/recall of retrieved papers relative to papers cited in human-written reviews) to independently validate the graph-context-aware retrieval design.

## Removed Points

These points were removed from the main review with brief justification:

- **"The claim that existing methods 'fail to organize papers into meaningful structures before generation' is misleading because AutoSurvey generates an outline"** — Removed. The paper's distinction is between a prompt-based outline and a structural taxonomy derived from citation topology; this is a legitimate difference, not a misrepresentation.
- **"Related Work reads as a list of references with minimal connection"** — Removed. Style judgment, not a substantive weakness.
- **"Why must the taxonomy be hierarchical? A flat taxonomy can also organize a review"** — Removed. The paper explicitly scopes the problem as hierarchical; evaluating it against a flat-taxonomy framing is scope creep.
- **"w/o retrieval collapse is so extreme it raises suspicion"** — Removed. Speculative; the paper's explanation (noise from irrelevant papers corrupts clustering and generation) is plausible.
- **"Fig. 1 caption not explained"** — Removed. Minor formatting/presentation nitpick.
- **"Three challenges presented as givens without justification"** — Removed. These are problem definitions; the paper does not claim to prove them.
- **"The approach could be strengthened by..."** (various suggestions from Strengthening section) — Moved to Nice-to-Haves or Minor weaknesses where substantive; generic suggestions removed.
- **"α not ablated"** — Moved to Nice-to-Haves (a useful experiment but not a required component for acceptance).

## Novel Insights

None beyond the paper's own contributions. The reviews surface evaluation and reproducibility concerns but do not identify systematic methodological errors or alternative explanations for the reported results that the paper itself has not considered.

## Suggestions

1. Add a human evaluation on a representative subset (e.g., 20–30 queries) where annotators rate coverage, structure, relevance, and factual correctness. This is the most impactful addition for strengthening the paper.
2. Define the clustering accuracy metric used in Table 3 and provide the definition in the main text.
3. Clarify the normalization of the "Human-written" row in Table 1 (e.g., "scores are normalized to the human-written review's score").
4. Report all missing hyperparameters (α, p_τ, λ_l, τ, L, GNN depth, hidden dimensions, learning rates, LoRA rank) in the main paper or appendix.
5. Clarify contradictory language in the training strategy (line 181): "fix θ, φ and then jointly fine-tune GNN_θ" needs correction.
6. Describe how ground-truth taxonomy trees were extracted (manual annotation, section parsing, or other).
7. Conduct a controlled experiment where AutoSurvey receives the same retrieved paper pool as HiReview.
8. Include a concrete example of a generated taxonomy tree alongside its ground-truth counterpart.
