I have all the information I need. Let me compose the final consolidated review.

## Summary

The paper proposes AtlasKV, a parametric framework for augmenting LLMs with knowledge graphs (KGs). It introduces two components: (1) **KG2KV**, a pipeline that converts KG triples into query-key-value training data with higher diversity and lower token cost than prior synthetic approaches, and (2) **HiKVP**, a hierarchical key-value pruning algorithm that reduces inference-time memory and time complexity from linear to sub-linear in the number of triples. Experiments show large accuracy gains over KBLaM on OOD benchmarks and memory scaling below 20GB VRAM even at 1B triples.

## Strengths

- **Novel and well-motivated combination of data and algorithmic contributions.** The KG2KV insight — that KG triples can be naturally decomposed into Q-K-V structures analogous to attention vectors — is elegant. The diversity ratio (7.864% vs 0.003%) and token cost (165.7 vs 349.9) improvements over the synthetic baseline in Table 1 concretely demonstrate the data quality advantage.

- **Sub-linear complexity with clear analysis.** Table 2 formalizes the complexity reduction from O((M+N)·N·D) (KBLaM) to O((C_t ∛M + N)·N·D) (AtlasKV) for time and similarly for memory. Figure 4 validates this empirically: AtlasKV stays near 20GB across 10⁴–10⁹ triples while KBLaM exceeds 40GB by 10⁵ triples. The 3-layer hierarchical clustering design (with cluster size S = ⌈∛M⌉) is a principled architectural choice.

- **Substantial accuracy gains on OOD benchmarks.** Table 3 reports very large improvements on the harder ATLAS-Pes2o-QKV and ATLAS-CC-QKV datasets (e.g., 16.4→92.7 ACC@1 at 10² triples on Pes2o). The ablation in Table 4 cleanly demonstrates that mixing both named and event entities in KG2KV is critical for good performance. The GPT-4o relevance scoring (Figure 5) provides a complementary quality signal beyond exact-match accuracy.

## Weaknesses

### Major

1. **Main accuracy comparison is confounded by training data differences.** AtlasKV is trained on KG2KV data (ATLAS-Wiki-QKV) while KBLaM is trained on its original Synthetic data. A controlled experiment — training KBLaM on the same KG2KV data, or AtlasKV on Synthetic data — is missing. This means the reported gains (e.g., 25.5→92.7 ACC@1 on ATLAS-Pes2o-QKV at 10² triples) may be driven entirely by data quality differences rather than AtlasKV's architectural innovations (the trained heads and equivalence attention formulation). The paper implicitly attributes the gains to data diversity ("This is mainly due to the diversity of the enquiry attributes in ATLAS-Wiki-QKV"), but the overall framing positions AtlasKV as a superior *method*. Without the control experiment, the method-level contribution over KBLaM's architecture is unsubstantiated.

2. **Accuracy at billion-scale is not evaluated.** The paper's headline claim is "augmenting LLMs with billion-scale knowledge graphs." The memory claim is validated up to 10⁹ triples (Figure 4), but the knowledge grounding accuracy is only measured for KGs of size 10⁰–10³ triples (Table 3). There is a six-orders-of-magnitude gap between the tested scale and the claimed scale. While HiKVP's theoretical analysis suggests it preserves relevant keys via hierarchical pruning, and accuracy at 10³ triples is maintained, the actual behavior at 10⁶–10⁹ triples (where hierarchical pruning's loss of relevant keys could compound) is not empirically verified. The paper would be stronger with a scaling experiment measuring recall@k of the pruned set against the full set as M grows, or accuracy on a held-out test set at 10⁴ or 10⁵ triples.

### Minor

3. **Memory comparison with ICL in Figure 4 is unclear.** ICL's memory curve appears flat at ~20GB across 10⁴–10⁹ triples, but ICL should require memory that grows with context length (number of triples × tokens per triple). The flat curve suggests either (a) ICL is shown without injecting any KG triples (i.e., just the base LLM), which would make the comparison not apples-to-apples, or (b) the measurements reflect a fixed small context. The caption and text do not clarify what each curve measures. The most important comparison (AtlasKV vs KBLaM) is still interpretable — KBLaM rises sharply while AtlasKV stays flat — but the ICL/zero-shot baselines' behavior needs explanation.

4. **No wall-clock latency measurement.** HiKVP involves multiple round-trips between CPU and GPU (offloading and uploading hierarchical layers). The paper reports only asymptotic complexity. A latency comparison against KBLaM for, say, 10³–10⁵ triples would confirm that the CPU-GPU transfers do not become a practical bottleneck.

5. **HiKVP's recall at scale is not characterized.** The algorithm prunes via top-k selection at each of the 3 hierarchical layers. The paper does not measure what fraction of ground-truth relevant keys survive the pruning cascade as M grows. This is important because errors in the root-layer pruning propagate downward and are irrecoverable.

### Trivial

6. Figure 4's y-axis starts at 20GB, which visually compresses differences between methods at the lower end. A broken-axis plot or a table with numerical memory values at selected points (10⁴, 10⁶, 10⁹) would be more informative.

## Nice-to-Haves

- Evaluating on a broader set of base LLMs (beyond LLaMA3.1-8B-Instruct) would strengthen generalizability claims.
- A comparison with CAG (Chan et al., 2025) on both memory and accuracy, since it is mentioned in related work as a caching-based parametric method.
- The relation rewriting step in KG2KV uses an LLM; an analysis of rewriting accuracy or a comparison with simpler alternatives (e.g., direct concatenation of relation and entity strings) would help quantify this design choice.

## Removed Points

- *"The paper does not compare against E² GraphRAG / LinearRAG"* — These are non-parametric RAG methods and out of scope for a parametric augmentation paper; removing as scope creep.
- *"KG2KV diversity ratio (7.864% vs 0.003%) compares different source documents"* — The comparison is between KG2KV on Wiki data and Synthetic on Wikipedia documents, but both methods start from the same underlying knowledge domain; the diversity ratio advantage is a genuine property of the pipeline design, not a confound.
- *"Analysis of relation rewriting accuracy is only in appendix"* — The paper explicitly references Appendix B.2 for this analysis; removing as the appendix exists in the original submission.
- *"Figure 4 may be measuring LLM base memory without context for ICL"* — This is a valid concern (retained as Weakness 3 above), but the harsh critic's stronger claim that "the plot is not apples-to-apples" is demoted from a central fatal criticism to a minor clarity issue, since the primary AtlasKV-vs-KBLaM comparison remains interpretable.
- *Several generic strengths from the Strength Finder* — Generic statements about "addressing an important problem" removed as they lack specific, verifiable evidence.

## Novel Insights

None beyond the paper's own contributions. The reviewer analyses surface primarily methodological concerns (experimental design confounds, evaluation scope) rather than revealing new conceptual insights about the material.

## Suggestions

1. **Run the controlled comparison.** Train KBLaM on ATLAS-Wiki-QKV data and report ACC@1/ACC@5 on the same OOD test sets. If AtlasKV's architecture still outperforms KBLaM on the same data, the method-level claim is established. If not, reframe the contribution honestly: KG2KV is a data pipeline that improves KBLaM-class methods, with HiKVP providing the scalability benefit.

2. **Add a recall-at-scale experiment.** Measure the recall of the HiKVP-pruned key set (relative to the full set) for queries at KG sizes of 10⁴, 10⁵, 10⁶ triples. This would bridge the gap between the theoretical complexity analysis and the accuracy experiments.

3. **Clarify Figure 4.** Explicitly state what each curve measures (e.g., whether ICL includes any injected knowledge), and add a small table with numerical memory values at representative points.

4. **Report latency.** A simple wall-clock time comparison against KBLaM for the same KG sizes would address the CPU-GPU transfer concern.

## Score and Decision

**Bracket pass (Round 1):** I queried three bands for papers on similar topics. Weak anchors (score < 3.5) clustered around 2.5–3.0 (papers on KG construction or simple LLM+KG integration with limited novelty). Middle anchors (3.5–7.5) included:
- **sl4hOq9wm9** (5.50, Reject) — "Knowledge Augmentation: In-context or In-parameter?" — in-parameter injection via LoRA, limited novelty, confounded evaluation.
- **aLsMzkTej9** (5.80, Accept) — KBLaM — direct predecessor, similar paradigm with rectangular attention.
- **mIEHIcHGOo** (6.67, Accept) — parametric knowledge transfer between LLMs.
- **PTcMzQgKmn** (6.25, Accept) — HiP — hierarchical pruning for attention.

Strong anchors (score > 7.5) included well-known KG+LLM reasoning papers (Think-on-Graph, ~8.0).

**Round 1 bracket:** [5.0, 7.0]

**Narrowing pass (Round 2):** I pulled more anchors inside this bracket, focusing on the most topically relevant papers. KBLaM (5.80) is the most directly comparable anchor — same paradigm, similar evaluation scope, accepted. AtlasKV has stronger technical contributions (data pipeline + hierarchical pruning vs. just rectangular attention) but also has the confounded comparison issue that KBLaM did not have (KBLaM's comparison with ICL used the same knowledge base format, so the comparison was cleaner).

**Final score:** 5.8 / 10

**Decision rationale:** AtlasKV proposes a genuinely interesting framework with two clear innovations (KG2KV and HiKVP) and provides substantial evidence of memory scalability. However, the main accuracy comparison is confounded by data differences, making it impossible to attribute the reported gains to the architectural innovations versus the data pipeline. The billion-scale accuracy claim also lacks direct empirical support. These weaknesses are significant enough that the paper sits at a moderate score comparable to its predecessor (KBLaM at 5.80), rather than reaching the 6.5+ range associated with cleaner evaluations. The contributions are real but the evidence for the method-level claims is incomplete.

MY FINAL SCORE: <score>5.8</score>
MY FINAL DECISION: <decision>Reject</decision>