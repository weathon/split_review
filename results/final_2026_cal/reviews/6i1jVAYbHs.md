Now I have enough information to produce the final consolidated review.

## Summary

This paper proposes AtlasKV, a parametric framework for augmenting LLMs with billion-scale knowledge graphs. It introduces two key components: (1) KG2KV, a pipeline that converts KG triples into QKV-formatted training data, and (2) HiKVP, a hierarchical key-value pruning algorithm that achieves sub-linear memory complexity during inference. Experiments show AtlasKV maintains a ~20GB GPU memory footprint across KG sizes from 10^4 to 10^9 triples, while achieving strong OOD knowledge grounding accuracy compared to KBLaM and other baselines.

## Strengths

1. **Sub-linear memory scaling demonstrated both empirically and theoretically**: Figure 4 shows AtlasKV maintaining a flat ~20GB GPU memory footprint from 10^4 to 10^9 triples, while KBLaM exceeds 40GB at just 10^5 triples. The complexity analysis in Table 2 formally derives O((C_t ∛M + N)·N·D) time and O((C_m ∛M + N)·(N+D)) memory for AtlasKV, versus KBLaM's linear O((M+N)·N·D). This core scalability claim is well-supported.

2. **Strong knowledge grounding accuracy on hard OOD datasets**: Table 3 reports AtlasKV achieving 90.0% ACC@1 on ATLAS-Pes2o-QKV at 10^3 triples (vs. KBLaM's 40.0%) and 89.1% on ATLAS-CC-QKV at 10^2 triples (vs. 21.8%). These large margins hold consistently across KG sizes and datasets, even with HiKVP pruning active.

3. **KG2KV data pipeline independently validated**: Table 1 shows KG2KV achieves 7.864% diversity ratio (unique enquiry attributes / total triples) vs. the synthetic method's 0.003%, with lower token cost (165.7 vs. 349.9). This quantifies a concrete data-quality advantage that is separable from the attention/architecture contributions.

4. **Ablation study validates entity-type design choices**: Table 4 shows that removing either event entities or named entities from KG2KV degrades ACC@1 substantially (e.g., from 92.7% to 49.0% on ATLAS-Pes2o-QKV at 10^2 triples when named entities are removed), confirming both entity types contribute meaningfully.

5. **Clear algorithmic description of HiKVP**: Section 4.2 provides a concrete three-step pruning pipeline (Equations 8–11, Figure 3) with precise operations at each layer (root → inter → leaf), including the offloading/uploading pattern and top-k selection. This makes the algorithm reproducible.

## Weaknesses

### Major

1. **Accuracy comparison against KBLaM confounded by different training data**: The headline accuracy comparison (Table 3) pits AtlasKV (trained on ATLAS-Wiki-QKV via KG2KV) against KBLaM (trained on its original synthetic dataset). These differ in both the method and the training distribution. The paper attributes AtlasKV's large gains to "diverse enquiry attributes" from KG2KV — but a controlled experiment (e.g., KBLaM trained on the same ATLAS-Wiki-QKV data, or AtlasKV trained on synthetic data) is absent. Without this control, one cannot determine how much of the +50–70 point gains come from the KG2KV data pipeline versus the attention formulation or HiKVP. The KG2KV data quality is independently validated (Table 1), which partially mitigates this concern, but the claim that "AtlasKV as a method outperforms KBLaM" conflates method and data contributions. Disentangling these would require the controlled comparison.

2. **No inference wall-clock time or latency measurements**: The paper prominently claims sub-linear *time* complexity (Table 2) and discusses efficiency throughout, but only measures GPU memory usage (Figure 4). The HiKVP pipeline involves multiple rounds of CPU↔GPU data transfer (upload root keys → compute → offload → upload inter keys → compute → offload → upload leaf keys and values). The cost of these transfers, plus attention computation at each hierarchy level, is never measured as wall-clock time, tokens-per-second, or per-query latency. The practical efficiency story is incomplete without such data, especially since the time complexity derivation is relegated to the (stripped) appendix.

### Minor

3. **Offline preprocessing cost is not discussed**: HiKVP requires building a three-level hierarchical structure over all KG keys via UMAP dimensionality reduction and GMM clustering *before* inference. KG2KV requires relation rewriting via an LLM for each triple. For billion-scale KGs, these are substantial one-time costs. The paper focuses solely on inference-time efficiency and does not acknowledge or quantify these offline costs. This does not invalidate the inference contribution, but the framing of "efficiency" should be qualified.

4. **Apparent inconsistency between Figure 4 and text regarding ICL memory usage**: The text states that ICL "when there are more than 100 triples in a KG, over 48GB VRAM is required" (Section 5.2, GPTScore paragraph), but the Figure 4 caption describes ICL as "staying below 20GB" across all KG sizes from 10^4 to 10^9. The paper should clarify whether the Figure 4 ICL line represents a feasible operating regime (e.g., with a very small retrieved subset), or whether this is a different measurement setup. As presented, the two statements are contradictory.

5. **HiKVP construction detail underspecified**: The paper states "Each key vector in a higher layer is the pooling of the key vectors in the lower layer" but does not specify the pooling operation (mean, max, attention-weighted, learned?). UMAP and GMM hyperparameters (number of neighbors, min distance, number of components) are also not reported. These details may reside in the appendix, but should ideally be available in the main text for reproducibility.

### Trivial

6. The synthetic method's diversity ratio of 0.003% (Table 1) — the paper should report the raw count of unique enquiry attributes alongside the percentage for clarity.

## Nice-to-Haves

- A controlled experiment training KBLaM on the same ATLAS-Wiki-QKV data (or a subset) would cleanly distinguish the method contribution from the data contribution and significantly strengthen the paper.
- Reporting wall-clock latency per query across KG sizes would substantiate the time-complexity claims.
- A brief discussion of offline preprocessing cost (clustering time, relation rewriting API calls) would improve the paper's honesty about total deployment cost.

## Removed Points

- **Criticism about Section 3.2 complexity claim being "stated without derivation"**: The derivation is cited to Appendix D, which is standard practice. The paper clearly states the complexity and references the appendix.
- **Criticism about "ICL, KBLaM, and RAG baselines" being unfair because of asymmetry**: The asymmetry (e.g., ICL using all triples as context vs AtlasKV using sub-linear pruning) is a standard way to demonstrate the advantage of the proposed method. The baselines are run in their standard configurations.
- **Criticism about "missing related works"**: Not verifiable from the paper itself.
- **Formatting/style nitpicks about ethics/reproducibility sections**: These are appropriate in length and content.
- **Claim that "the comparison is not controlling for query diversity generation" regarding prefix augmentation**: The paper explicitly describes how query prefixes work and compares diversity ratios in Table 1. This is adequately addressed.

## Novel Insights

The key insight that emerges from the harsh and supportive reviews together is that AtlasKV's contribution is really two relatively independent pieces — a data pipeline (KG2KV) and an algorithmic efficiency technique (HiKVP) — but the evaluation design conflates them. The memory scaling result (Figure 4) cleanly validates HiKVP; the accuracy result (Table 3) validates the combined system. A reader interested in adopting the method needs to know: does HiKVP by itself hurt accuracy much (compared to AtlasKV w/o HiKVP, the gap is modest, ~5-10 points), and would KBLaM trained on KG2KV data narrow the gap? The paper's construction of two distinct OOD datasets from the ATLAS family and its clear ablation on entity types are well-executed and informative.

## Suggestions

1. Run KBLaM on the ATLAS-Wiki-QKV training data to isolate the method effect from the data effect in the accuracy comparison.
2. Add a table showing wall-clock time per query or tokens-per-second across KG sizes (10^2 to 10^6) for AtlasKV, AtlasKV w/o HiKVP, and KBLaM.
3. Clarify the ICL memory usage in Figure 4 — either explain the measurement setup or fix the inconsistency.
4. Specify the pooling operation used for hierarchical key construction and UMAP/GMM hyperparameters.
5. Add a limitations paragraph discussing the offline costs of hierarchical clustering and relation rewriting.

## Score and Decision

### Calibration Report

**Round 1 (Bracketing):**
- Low band (avg<3.5): Queried "parametric knowledge augmentation for LLMs with knowledge graphs" → anchors at 3.00 (Reject), 3.33 (Reject). These papers had limited novelty or flawed evaluation.
- Middle band (3.5–7.5): Queried "scalable knowledge graph integration LLM attention memory" → anchors at 4.50 (Reject), 5.00 (Accept Poster), 5.00 (Accept Poster), 6.50 (Accept Poster). The 5.0 papers had clear contributions with some evaluation gaps.
- High band (avg>7.5): Queried "large language model knowledge grounding hierarchical retrieval" → anchors at 8.0 (Accept Oral/Poster). These were on unrelated topics (multi-turn conversation, embodied navigation).

**Initial bracket**: between 4.5 and 6.5.

**Round 2 (Narrowing within bracket):**
- Queried "parametric knowledge augmentation attention memory LLM knowledge graph" (4.5–6.0) → anchors including MLP Memory (5.0, Accept Poster), KG reasoning LM (5.0, Accept Poster), Pretraining with hierarchical memories (4.80, Accept Poster)
- Queried "hierarchical retrieval pruning key value LLM scalable" (5.5–7.5) → LinearRAG (6.0, Accept Poster), ThinKV (6.0, Accept Oral), LMLM (6.5, Accept Poster)

**Comparison to specific anchors:**
- vs. MLP Memory (5.0, Accept Poster): MLP Memory had evaluation gaps (missing kNN-LM comparison, training cost unquantified) similar to AtlasKV's gaps. AtlasKV has a stronger algorithmic contribution (HiKVP) but similar evaluation limitations. Comparable quality.
- vs. LinearRAG (6.0, Accept Poster): LinearRAG had cleaner evaluation including latency/token-cost metrics, unanimous 6s. AtlasKV is weaker on evaluation completeness (no latency, confounded comparison). Below LinearRAG.
- vs. Ground-Truth Subgraphs (3.33, Reject): That paper was rejected primarily due to limited novelty (similar framework already existed). AtlasKV has stronger novelty in its algorithmic contribution.

**Final score: 5.0** — The paper has a genuine technical contribution (KG2KV + HiKVP) with strong empirical memory scaling and accuracy results, but the evaluation has two significant gaps: the confounded head-to-head comparison with KBLaM and the missing latency benchmarks. These prevent it from reaching the 6.0 level but the contributions are clearly above the 3–4 range.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Accept</decision>