Now I have sufficient information. Let me write the consolidated review.

## Calibration Analysis

**Round 1 (Bracketing)**:
- Weak band (<3.5): anchors at 3.00 — clearly weaker papers on KG+LLM topics
- Middle band (3.5-7.5): KBLaM at 5.80 (direct predecessor), HiP at 6.25 (hierarchical pruning for attention), SubgraphRAG at 6.00 (KG-based RAG)
- Strong band (>7.5): anchors at 8.00+ — clearly stronger papers with fuller empirical validation

**Round 1 bracket**: 4.5 to 6.5

**Round 2 (Narrowing)**:
- KBLaM (5.80): Direct predecessor. AtlasKV improves on KBLaM in data diversity (KG2KV) and scaling (sub-linear vs linear), but has a wider gap between the headline claim (1B triples) and the experimental evidence (up to 1K triples for accuracy).
- HiP (6.25): Hierarchical pruning for efficient attention — methodologically related. Better validated at its claimed scale. AtlasKV has stronger novelty on the data side (KG2KV) but weaker validation of its central efficiency claim.
- SubgraphRAG (6.00): KG-based RAG paper accepted at ICLR. Similar evaluation scope. AtlasKV's parametric approach is more novel but SubgraphRAG has fuller experimental coverage.

**Final position**: AtlasKV is comparable to KBLaM (5.80) — the technical contributions (KG2KV + HiKVP) are meaningful advances, and the OOD accuracy results are strong. However, the billion-scale claim is not empirically validated, and Figure 4 has a presentation issue. I score it at **5.5**, slightly below KBLaM due to the evidence gap on the paper's central selling point, but still a solid paper with genuine contributions.

---

## Summary

This paper proposes AtlasKV, a parametric framework for augmenting LLMs with knowledge graph triples through two innovations: (1) KG2KV, which naturally converts KG triples into query-key-value (QKV) training data by rewriting relations and masking entities, producing diverse training data; and (2) HiKVP (Hierarchical Key-Value Pruning), which organizes KGKV embeddings into a 3-level hierarchy (leaf, inter, root) and prunes to the top-k relevant keys during inference, achieving O(∛M) memory and time complexity. The paper reports strong OOD knowledge grounding accuracy on three evaluation datasets and projects GPU memory below 20GB even at billion-scale KG sizes.

## Strengths

- **KG2KV is a clever, well-motivated data construction pipeline.** The observation that KG triples naturally decompose into QKV-like structures is insightful. Converting triples into diverse query-key-value training data by masking head/tail entities and rewriting relations produces 7.864% diversity ratio vs. 0.003% for the synthetic baseline (Table 1). This directly addresses a real limitation of the prior KBLaM paradigm.

- **Strong OOD accuracy gains over KBLaM across multiple datasets.** Table 3 shows AtlasKV (w/o HiKVP) achieves 92.7% ACC@1 on ATLAS-Pes2o-QKV at 10² triples vs. KBLaM's 16.4% (both at 3K steps) — a gap of 67.2 points. On the harder ATLAS-CC-QKV, AtlasKV achieves 96.4% vs. KBLaM's 21.8%. These are substantial improvements, not incremental.

- **HiKVP delivers sub-linear complexity without large accuracy drops.** AtlasKV with HiKVP (128-64-16) maintains strong performance close to the full model — for example, 89.1% vs. 96.4% on ATLAS-CC-QKV at 10² triples — while achieving O(∛M) memory. The accuracy degradation from pruning is modest, suggesting the learned projection heads do enable effective hierarchical retrieval.

- **Training efficiency with fewer optimization steps.** AtlasKV at 3K tuning steps consistently outperforms KBLaM at 20K steps on the harder datasets (e.g., 82.3% vs. 25.5% on ATLAS-Pes2o-QKV at 10² triples), demonstrating that KG2KV provides a more effective training signal.

## Weaknesses

### Major

- **The central "billion-scale" claim is not empirically validated.** The paper's title and abstract position billion-scale KGs in 20GB as a headline contribution. However, the largest KG used in accuracy experiments (Table 3) is 10³ triples, and Figure 4's billion-scale memory projection appears to be analytical extrapolation — no actual measurements at 1M, 10M, or 1B triples are reported. For a paper where scalability is the primary selling point, the six-order-of-magnitude gap between the claim (10⁹) and the evidence (10³) is substantial. No latency, throughput, or accuracy results are provided for any KG above 10⁴ triples.

- **Figure 4's ICL memory comparison is not adequately explained, creating an internal inconsistency.** Table 2 gives ICL's complexity as O((MT+N)²·D), which models placing ALL M triples into context. But Figure 4 shows ICL with near-constant low memory (~20GB) across KG sizes up to 10⁹. If ICL in Figure 4 uses a small retrieved subset rather than the full KG (which would be the practical RAG usage), this is a reasonable comparison, but the paper never clarifies this, and the x-axis "# of KG Triples" becomes misleading for ICL. The paper should explicitly state what ICL is doing in Figure 4 and how the x-axis applies to it.

### Minor

- **Two of three OOD evaluation datasets share the KG2KV transformation pipeline with the training data.** ATLAS-CC-QKV and ATLAS-Pes2o-QKV are constructed via the same KG2KV pipeline from ATLAS-family KGs. This means the evaluation measures the model's ability to retrieve KGKV patterns it was trained on, which is related to but not identical to genuine factual retrieval from arbitrary KGs. The Enron evaluation partly mitigates this, but on Enron with 10² triples, KBLaM at 20K steps achieves 83.6% ACC@1 vs. AtlasKV w/o HiKVP at 3K steps at 76.4%, suggesting the claimed superiority is not universal across all settings.

- **No inference latency or throughput results are reported.** The paper emphasizes efficiency but only provides memory measurements (Figure 4). For the method to be practically meaningful, the hierarchical pruning overhead (multiple rounds of CPU↔GPU transfers, three sequential attention computations) must be fast enough to be useful. Reporting tokens/second or latency-per-query at various KG sizes is needed.

- **GPTScore evaluation protocol is underspecified.** The paper reports GPT-4o relevance scores (Figure 5) without providing the scoring prompt, whether GPT-4o was shown ground-truth answers, or whether multiple judge models were used. GPT-4o-as-judge has known biases; some calibration or human evaluation would strengthen this.

### Trivial

- The diversity ratio of 7.864% (Table 1) could be clarified — the "enquiry attribute" depends on entity-relation combinations, not just relation count, which explains the high ratio. A brief definition expansion would prevent misinterpretation.

## Nice-to-Haves

- Running even a moderate-scale experiment (1M triples) with measured memory, latency, and accuracy would significantly strengthen the scalability claim. The paper could note that 1B-scale experiments require multi-GPU setups beyond the paper's 48GB single-GPU setting.
- The UMAP + GMM preprocessing cost for billion-scale KGs is not discussed; clarifying that this is an offline cost separable from per-inference complexity would be helpful.
- An end-to-end QA evaluation on a standard benchmark (e.g., WebQSP, CWQ) would complement the attention-based accuracy metric.

## Removed Points

- **Diversity ratio implausibility (Harsh Critic)** — The critic claimed 7.864% is implausible for 100M triples by assuming "enquiry attributes" are just relations. However, the KG2KV key strings include both the rewritten relation AND the unmasked entity text ("the cause of John founded StockLemon.com"), so uniqueness depends on entity-relation combinations, not just relation variety. The criticism misunderstands the definition.
- **UMAP impracticality on 1B vectors (Harsh Critic)** — While noted, this is an offline preprocessing cost, not per-inference complexity. The paper's complexity claims are for inference only. This would be a reasonable clarification request but not a weakness of the inference method.
- **Missing latency as fatal (Harsh Critic)** — Downgraded from implied fatal to minor. Memory is the primary claimed advantage; latency is important but the paper focuses on memory scalability. Still worth noting as a missing measurement.
- **Various formatting/style nitpicks** — Removed per filtering rules.

## Novel Insights

None beyond the paper's own contributions. The two-component design (KG2KV for data quality + HiKVP for inference efficiency) is the paper's core insight and is well-articulated.

## Suggestions

1. Clarify how ICL is implemented in Figure 4. If ICL uses a fixed small retrieved set, state this explicitly and note that the x-axis represents total KG size (the knowledge the system could potentially use) rather than the knowledge actually loaded into context for each method.
2. Add at least one moderate-scale experiment (10⁶ triples) measuring actual GPU memory usage, not just analytical projection. If the paper's single-GPU setup cannot handle this, state the limitation and show what the largest measurable scale is.
3. Include inference latency / throughput measurements at multiple KG sizes to validate that HiKVP's CPU↔GPU offloading is practical.
4. Add one evaluation dataset that does not use the KG2KV pipeline for constructing QKV evaluation data, to rule out format-specific memorization.

## Score and Decision

**Round 1 bracket**: 4.5 – 6.5

**Round 2 anchors used**:
| Anchor | Avg Score | Round | Comparison |
|--------|-----------|-------|------------|
| aLsMzkTej9 (KBLaM) | 5.80 | R2 | Direct predecessor. AtlasKV has stronger technical contributions but weaker validation of its central claim. Slightly below. |
| PTcMzQgKmn (HiP) | 6.25 | R2 | Methodologically related (hierarchical pruning). Better validated at claimed scale. AtlasKV is below. |
| JvkuZZ04O7 (SubgraphRAG) | 6.00 | R2 | Same domain (KG+LLM). AtlasKV has more novel approach but weaker evaluation scope. Slightly below. |
| ds3Tcnrte8 | 3.00 | R1 | Weak baseline anchor. AtlasKV is clearly stronger. |
| WbWtOYIzIK (Knowledge Card) | 8.00 | R1 | Strong anchor with fuller validation. AtlasKV is clearly below. |

The paper makes genuine contributions (KG2KV and HiKVP) with strong OOD accuracy results. However, the headline billion-scale claim lacks experimental validation, and Figure 4 has an unresolved presentation issue. The paper is comparable to its predecessor KBLaM (5.80) but with a larger evidence gap on the central scalability claim, placing it slightly below.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>