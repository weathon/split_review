Now I have sufficient calibration data. Let me write the final consolidated review.

---

## Summary

AtlasKV proposes a parametric method for augmenting LLMs with billion-scale knowledge graphs by combining two innovations: (1) **KG2KV**, which converts KG triples into diverse query-key-value training data by masking entities and rewriting relations, and (2) **HiKVP**, a hierarchical key-value pruning algorithm that clusters knowledge keys into a three-level tree and prunes aggressively at inference time, reducing attention complexity from linear to sub-linear (∛M) in the KG size. The method builds on KBLaM's rectangular attention paradigm and demonstrates substantially improved knowledge grounding accuracy, better generalization, and flat GPU memory usage (~20 GB) as KG size scales to 1B triples.

## Strengths

- **Clear, significant improvement over the direct predecessor (KBLaM).** Across all three OOD datasets and KG sizes, AtlasKV substantially outperforms KBLaM in both knowledge grounding accuracy (Table 3) and generation relevance (Figure 5), while using only 3K training steps versus KBLaM's 20K. This is a well-executed technical advance over the prior state of the art in parametric KG augmentation.
- **KG2KV is a conceptually elegant data pipeline.** Converting KG triples to Q-K-V data by masking entities and using LLM-based relation rewriting yields 7.864% unique enquiry attribute diversity (vs. 0.003% for synthetic data, Table 1) and lower token cost. This directly addresses KBLaM's key weakness of poor generalization from synthetic training data.
- **HiKVP provides principled sub-linear scaling.** The hierarchical clustering with three layers and top-k pruning (128-64-16) reduces theoretical complexity from O(M) to O(∛M) (Table 2), and Figure 4 convincingly shows VRAM staying flat near 20 GB from 10⁴ to 10⁹ triples — a genuine scalability achievement over KBLaM, which exceeds 40 GB at only 10⁵ triples.
- **Well-designed ablation on entity types (Table 4).** Removing event entities causes large accuracy drops (e.g., ACC@1 from 92.7% to 49.0% on ATLAS-Pes2o-QKV at 10² triples), validating the design choice to include both named and event entities in KG2KV training data. The analysis that named entities provide easier learning while event entities add necessary semantic complexity is insightful.

## Weaknesses

### Major

- **Retrieval accuracy is never evaluated at scale.** The paper's central claim is that AtlasKV "maintain[s] high knowledge grounding accuracy during inference time" at billion-triple scale. Figure 4 validates the *memory* claim, but all knowledge grounding accuracy numbers (Table 3) are measured on KGs of at most 10³ triples — a regime where brute-force attention is already tractable and where the hierarchical pruning is barely stressed. Whether HiKVP can actually route attention to the correct triples when the pool contains 10⁶, 10⁸, or 10⁹ items is untested. The clustering quality (UMAP + GMM on high-dimensional embeddings) may degrade at extreme scale in ways that affect retrieval precision, and top-k budgets that suffice at 10³ may be inadequate at 10⁹. This gap between the memory scalability evidence and the accuracy claim substantially weakens the paper's headline contribution.

### Minor

- **OOD evaluation partially shares formatting with training data.** Two of three evaluation datasets (ATLAS-CC-QKV and ATLAS-Pes2o-QKV) are constructed using the same KG2KV pipeline (entity masking + relation rewriting) as the training data. This means the model is evaluated on the same *formatting convention* it was trained on, even though the entities, relations, and domains differ. The generalization claim is therefore partly about handling different KG content within a shared surface form rather than truly arbitrary query styles. The Enron dataset provides genuinely independent OOD evidence and AtlasKV still outperforms KBLaM there, which partially mitigates this concern, but the strongest reported results come from the KG2KV-formatted sets.

- **No comparison against a practical retrieval-based baseline.** The paper contrasts AtlasKV with RAG approaches in the introduction and related work, but the only non-parametric baseline evaluated is ICL that feeds *all* triples into the prompt — a strawman that no real RAG system uses. A comparison against a system that uses the same sentence encoder for similarity search to retrieve top-k triples and feeds them as context would clarify whether the parametric integration offers an accuracy or cost benefit over a simple retrieve-and-read pipeline. The paper's primary contribution is advancing the parametric paradigm over KBLaM, so this does not invalidate the core results, but it weakens the broader claims about superiority over RAG.

- **Preprocessing cost for hierarchical clustering is not discussed.** HiKVP requires UMAP dimensionality reduction followed by GMM clustering on the full set of key embeddings (size M, up to billions of 384-dimensional vectors). For 1B triples, this amounts to hundreds of GB of embeddings and potentially prohibitive CPU time. While the paper focuses on GPU VRAM at inference, the one-time offline cost of building the hierarchical index is a practical consideration for the claimed scale that goes unexamined.

### Trivial

- The choice of exactly three hierarchical layers is motivated as "the minimum number of layers to include all of the definitions we need" (Section 4.2), which is a thin justification. The specific top-k settings (128-64-16) are not ablated or analyzed in the main text (deferred to Appendix B.4.1).

- The complexity analysis for RAG in Table 2 uses O(M) for retrieval, while practical vector databases achieve sub-linear retrieval. This does not affect AtlasKV's own claims but makes the comparison table slightly imprecise.

## Nice-to-Haves

- A sensitivity analysis varying the top-k budgets and number of hierarchical layers at a larger KG scale (e.g., 10⁵ triples) would strengthen confidence in the pruning design.
- Reporting end-to-end latency (not just VRAM) against KBLaM and a practical RAG baseline would give a fuller picture of inference-time benefits.
- Discussing failure modes of HiKVP — e.g., cases where relevant triples are separated into different clusters and missed by pruning — would build trust in the method's robustness.

## Removed Points

These points are flagged to be removed, treat them with caution:

- **"Missing comparison with RAG is fatal"** — The paper's primary contribution is advancing the parametric KBLaM paradigm. ICL is the standard baseline in this line of work. The absence of a practical RAG comparison is a gap but not fatal; the paper competes primarily with KBLaM, not RAG. Demoted to Minor.

- **"OOD confound invalidates generalization claims"** — The Enron dataset provides genuinely independent OOD evidence, and AtlasKV outperforms KBLaM there. The confound on ATLAS-CC-QKV and ATLAS-Pes2o-QKV is real but does not invalidate all generalization evidence. Demoted to Minor.

- **"GPU memory plot conflates ICL with unrealistic all-triples setting"** — The paper explicitly acknowledges this impracticality. ICL is not the main comparison point; KBLaM is.

- **"Three layers and top-k lack justification"** — Partially valid; the paper says the appendix contains top-k ablations. Since the appendix is stripped, we cannot verify, but the criticism is minor. Kept as Trivial.

- **Strength Finder claim about 'lost-in-the-middle'"** — This is a conceptual advantage, not empirically validated in the paper. Moved to Removed Points.

- **"Training data efficiency claim hard to verify"** — The paper states "only 20K KGKV samples" which is specific enough. This is a minor presentation issue at most. Removed.

## Novel Insights

Beyond the paper's own contributions, the review process surfaces an interesting tension in this line of work: parametric knowledge injection methods (KBLaM, AtlasKV) achieve impressive memory efficiency and training-free adaptation, but their evaluation methodology inherits challenges from RAG — specifically, how to construct genuinely OOD test sets when the training data format itself is part of what the model learns. The KG2KV pipeline is both a strength (diverse training data) and a potential confound (shared formatting with evaluation). This suggests that future work in parametric KG augmentation would benefit from standardized OOD benchmarks that vary query formatting conventions, not just KG content.

## Suggestions

- **Validate retrieval accuracy at scale** by constructing KG pools of at least 10⁵–10⁶ triples from diverse domains and measuring whether HiKVP maintains Top-1/5 accuracy. An ablation varying M from 10³ to 10⁶ while reporting both accuracy and memory would directly bridge the gap between the memory claim and the performance claim.
- **Add a practical retrieval baseline**: use the same sentence encoder to embed all triples, retrieve top-k via maximum inner-product search, feed those triples as context to the same LLM, and compare accuracy and latency. This would honestly position AtlasKV relative to the RAG approaches it critiques.
- **Discuss the offline preprocessing cost** (time, CPU memory for UMAP + GMM) and practical deployment limits at billion scale.

---

## Score and Decision

**Calibration anchors considered:**

| Anchor | Avg Score | Round | Comparison |
|--------|-----------|-------|------------|
| KBLaM (aLsMzkTej9) | 5.80 | R1/R2 | Direct predecessor; AtlasKV clearly improves on it in data quality, scalability, and results |
| SubgraphRAG (JvkuZZ04O7) | 6.00 | R2 | Different paradigm; AtlasKV is comparably novel with stronger improvement over its predecessor |
| KG-SFT (oMFOKjwaRS) | 5.80 | R2 | Different topic; less relevant |
| Seeking Neural Nuggets (mIEHIcHGOo) | 6.67 | R2 | Different topic; AtlasKV has clearer practical impact |
| Think-on-Graph (nnVO1PvbTv) | 7.00 | R2 | Strong KG+LLM paper with broader evaluation; AtlasKV is slightly below this level due to the scale-evaluation gap |
| Reasoning on Graphs (ZGNWW7xZ6Q) | 7.50 | R2 | Stronger paper with more comprehensive evaluation |
| Knowledge Card (WbWtOYIzIK) | 8.00 | R1 | Stronger paper with broader benchmarks |
| In-context or In-parameter (sl4hOq9wm9) | 5.50 | R1 | Less novel; AtlasKV is clearly stronger |

**Bracket from Round 1:** 5.80–8.00, narrowed to 6.0–7.0 after comparing with KBLaM (5.80, clearly worse) and the 7.5–8.0 anchors (clearly stronger on evaluation breadth).

**Round 2 narrowing:** AtlasKV sits above SubgraphRAG (6.00) and below Think-on-Graph (7.00). The major weakness — no retrieval accuracy evaluation at scale — prevents the paper from reaching the 7.0 level, but the genuine technical advance over KBLaM and the demonstrated memory scalability place it solidly above 6.0. **Final score: 6.5.**

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>