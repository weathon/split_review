Now let me compile the final review with calibration reporting.

## Summary
AtlasKV proposes a framework for integrating billion-scale knowledge graphs into LLMs through two innovations: KG2KV, which converts KG triples into query-key-value training data with substantially higher diversity than synthetic methods (~2,600×), and HiKVP, a hierarchical pruning algorithm that reduces inference complexity from linear to sub-linear. The paper demonstrates strong accuracy improvements over KBLaM on hard OOD datasets at scales up to 1,000 triples and memory scalability to 1B triples in ~20GB VRAM.

## Strengths
- **Large accuracy improvements over KBLaM on hard OOD datasets**: Table 3 shows AtlasKV (with HiKVP) achieves 82.3 vs. 16.4 ACC@1 on ATLAS-Pes2o-QKV at 10² triples, and 89.1 vs. 21.8 on ATLAS-CC-QKV. These improvements are consistent across all tested KG sizes (10⁰–10³) and both hard datasets.
- **Dramatic memory scalability demonstrated at billion scale**: Figure 4 shows AtlasKV uses ~20GB VRAM at 1B triples while KBLaM exceeds 40GB at 100K triples. Backed by the theoretical complexity reduction in Table 2: from O((M+N)·N·D) to O((C_t·∛M + N)·N·D).
- **KG2KV provides substantially higher training data diversity at lower cost**: Table 1 shows a diversity ratio of 7.864% vs. 0.003% (~2,600× improvement) with fewer tokens per sample (165.7 vs. 349.9), directly validating the insight that KG triples have a natural Q-K-V structure.
- **Training efficiency from high-quality data**: AtlasKV at 3K steps outperforms KBLaM at both 3K and 20K steps on the hard OOD datasets (Table 3), demonstrating data quality matters more than training volume.
- **Well-designed ablation on entity types**: Table 4 shows both named and event entities contribute with complementary roles, validating the specific design choice in Section 4.1.

## Weaknesses

### Fatal
None.

### Major
- **Accuracy at billion scale is untested — the headline claim is only half-validated**: The title and abstract promise "billion-scale knowledge graphs (e.g. 1B triples)," but all accuracy evaluations (Table 3, Table 4) top out at 10³ triples; GPTScore (Figure 5) reaches only 10⁴. Only GPU memory is evaluated at 10⁹ (Figure 4). With M=10⁹ and HiKVP settings (k_R=128, k_I=64, k_L=16), only ~16 leaf keys are retained out of 10⁹ — an extremely aggressive pruning ratio. The degradation pattern visible in Table 3 (e.g., on ATLAS-Pes2o-QKV, HiKVP causes increasing accuracy drops: ~10pt at 10³, ~10pt at 10², ~21pt at 10¹, ~31pt at 10⁰) suggests accuracy may degrade further at larger scales, but this is entirely unknown. The paper should evaluate AtlasKV's own accuracy at 10⁵, 10⁶, and beyond, even without baselines.

- **GPTScore does not evaluate the full system (with HiKVP)**: Figure 5 evaluates only "AtlasKV w/o HiKVP" for answer quality, meaning the end-to-end effectiveness of the complete pipeline on actual answer relevance is never measured. Combined with the proxy nature of the attention-based grounding metric (measures whether the correct triple gets high attention, not whether the LLM actually incorporates that knowledge into its answer), the paper lacks evidence that the full deployed system produces good answers.

### Minor
- **No limitations discussion**: The conclusion omits acknowledgment of the untested accuracy at billion scale, the proxy nature of the attention metric, or dependence on sentence encoder quality.

### Trivial
None.

## Nice-to-Haves
- Include at least one scalable graph-based RAG baseline (e.g., E² GraphRAG or LinearRAG) in direct comparisons. The paper argues these "still follow the ICL-based RAG paradigm," but a direct comparison would strengthen the parametric superiority claim.
- Report GPTScore for AtlasKV with HiKVP to validate end-to-end answer quality.
- Vary HiKVP top-k settings at large scales (10⁵–10⁹) to characterize the accuracy-memory tradeoff.

## Removed Points
These points are flagged to be removed, treat them with caution:
- Missing E² GraphRAG and LinearRAG comparisons: The paper explicitly notes they follow the ICL-based RAG paradigm and compares against ICL as representative. Moved to nice-to-have.
- Strength finder's "minimal accuracy degradation from pruning" claim: Data actually shows 10–31 point drops from HiKVP at smaller KG sizes. Kept in attenuated form — AtlasKV with HiKVP still outperforms KBLaM substantially.
- Table 4 column labels ($10^3$, $10^2$, $10^3$, $10^4$): Parser formatting artifact, not a paper problem.

## Novel Insights
The paper's most novel insight is that KG triples have a natural Q-K-V decomposition aligned with the self-attention mechanism's structure, producing ~2,600× more diverse training data than synthetic schema-based methods. This is a genuinely useful observation for the knowledge augmentation community. The hierarchical pruning adaptation to the rectangular attention setting is a solid technical contribution, though conceptually related to prior hierarchical retrieval work.

## Suggestions
- Add accuracy experiments at larger KG sizes (10⁴–10⁹) to validate the billion-scale claim.
- Add GPTScore for AtlasKV with HiKVP to validate end-to-end answer quality.
- Add a limitations section acknowledging the accuracy-at-scale gap.

## Calibration Reporting

**Round 1 — Bracketing anchors:**
| Anchor | Path | Avg Score | Round | Comparison |
|--------|------|-----------|-------|------------|
| IntelLLM (KV cache compression) | 4QWPCTLq20 | 3.00 | 1 | Different topic, much weaker |
| Generalization from Starvation | f7aWmxgSN4 | 3.00 | 1 | Different focus, weaker |
| QAP (KG prompting) | ds3Tcnrte8 | 3.00 | 1 | Simpler approach, weaker |
| Biomedical KG Construction | K1bv86Uvbp | 3.00 | 1 | Application paper, weaker |
| Knowledge Augmentation: In-context or In-parameter? | sl4hOq9wm9 | 5.50 | 1 | Related topic, essentially LoRA — AtlasKV is more novel |
| Seeking Neural Nuggets | mIEHIcHGOo | 6.67 | 1 | Knowledge transfer focus, less relevant |
| Understanding Interplay (Parametric vs Contextual) | t21RmVmJrT | 5.00 | 1 | Analysis paper, different contribution type |
| **KBLaM** | aLsMzkTej9 | **5.80** | 1 | **AtlasKV's direct baseline — AtlasKV is clearly better** |
| Knowledge Card | WbWtOYIzIK | 8.00 | 1 | More comprehensive evaluation, higher quality — AtlasKV not as strong |
| Synthetic continued pretraining | 07yvxWDSla | 8.00 | 1 | Different approach, strong evaluation — AtlasKV not as strong |
| FlexPrefill | OfjIlbelrT | 8.00 | 1 | Systems paper, strong evaluation — AtlasKV not as strong |
| Retrieval Head | EytBpUGB1Z | 8.00 | 1 | Mechanistic analysis, different focus |

**Round 1 bracket: 5.5–7.5** (between "In-context or In-parameter?" at 5.50 and the 8.00 papers)

**Round 2 — Narrowing anchors:**
| Anchor | Path | Avg Score | Round | Comparison |
|--------|------|-----------|-------|------------|
| Assessing Knowledge-intensive Reasoning | iSTMsye6SD | 5.25 | 2 | Benchmark paper, weaker contribution |
| KG-SFT | oMFOKjwaRS | 5.80 | 2 | KG for SFT — AtlasKV more novel, better scalability |
| Leveraging KGs for CLIP | hQY03s8rOm | 5.33 | 2 | Different domain, weaker |
| **SubgraphRAG** | JvkuZZ04O7 | **6.00** | 2 | **KG-based RAG — AtlasKV is more novel with better scalability** |
| HOMER (Hierarchical Context Merging) | ulaUJFd96G | 6.25 | 2 | Hierarchical efficiency, different application — AtlasKV comparable or slightly better |
| HiP (Hierarchically Pruned Attention) | PTcMzQgKmn | 6.25 | 2 | Hierarchical pruning for attention — conceptually related, AtlasKV more applied |
| Sparse RAG | HE6pJoNnFp | 6.60 | 2 | RAG efficiency — AtlasKV has more novel approach, comparable contribution level |
| SLM (Scalable Language Model) | mz8owj4DXu | 6.50 | 2 | Continual learning focus — less directly comparable |

**Round 2 narrowing**: Anchors clustered between 5.25–6.60. AtlasKV is:
- Clearly better than KBLaM (5.80) — addresses both key limitations with large accuracy gains
- Better than SubgraphRAG (6.00) — more novel parametric approach, superior scalability
- Comparable to Sparse RAG (6.60) — both tackle efficiency, AtlasKV is more novel
- Slightly above HOMER/HiP (6.25) — better validated on the specific task

The billion-scale accuracy gap pulls the score down from what would otherwise be ~7.0. Final score of **6.5** positions AtlasKV above SubgraphRAG (6.00) and at the level of Sparse RAG (6.60), reflecting strong technical contributions while acknowledging the significant evaluation gap.

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>