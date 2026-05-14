Now I have enough information to produce the final consolidated review. Let me compose it.

---

## Summary

This paper introduces AtlasKV, a parametric method for augmenting LLMs with knowledge graph triples by converting triples into Q-K-V data (KG2KV) and then injecting them into the LLM's attention layers with a hierarchical key-value pruning algorithm (HiKVP) that achieves sub-linear time and memory complexity. The approach requires only lightweight training (3K steps on 20K samples) and demonstrates superior knowledge grounding accuracy compared to KBLaM on OOD evaluation datasets up to 10⁴ triples, while the memory analysis suggests scalability to billion-scale KGs under 20GB VRAM.

## Strengths

- **KG2KV is a practical and principled data-transformation pipeline.** Converting KG triples into Q-K-V training data by masking entities and rewriting relations as noun phrases is a natural idea that leverages the inherent structure of KGs. Table 1 provides quantitative evidence of improved diversity (7.864% vs 0.003%) and reduced token cost (165.7 vs 349.9) over synthetic data generation used in prior work.

- **HiKVP is a well-motivated hierarchical pruning algorithm with sub-linear complexity.** The three-level clustering (root, inter, leaf) with cluster size S = ⌈∛M⌉ achieves O((C_t∛M + N)·N·D) time and O((C_m∛M + N)·(N + D)) memory complexity, which is theoretically sound and practically significant. The detailed step-by-step description of the pruning pipeline (Section 4.2) is clear and implementable.

- **Strong empirical results against KBLaM across OOD datasets.** Table 3 shows AtlasKV (128-64-16) achieving 90.0% ACC@1 on ATLAS-Pes2o-QKV (10³ triples) versus KBLaM's 40.0% (3e3 steps), and 89.1% vs 21.8% on ATLAS-CC-QKV. These gains are substantial and consistent.

- **Training efficiency is genuinely impressive.** AtlasKV achieves strong performance with only 3K training steps, whereas KBLaM requires 20K steps for comparable results (Table 3). This is a practical advantage.

- **The ablation study (Table 4) validates the importance of jointly using named and event entities in KG2KV.** Removing event entities drops ACC@1 from 92.7% to 49.0% on ATLAS-Pes2o-QKV, providing clear evidence for this design choice.

## Weaknesses

### Fatal

None.

### Major

- **Accuracy is never evaluated at the claimed billion-scale.** The title and abstract claim "billion-scale knowledge graphs," and the central scalability claim is supported by memory measurements (Figure 4), but knowledge grounding accuracy (Table 3) and GPTScore (Figure 5) are only measured up to 10⁴ triples. No evidence is provided that HiKVP maintains retrieval accuracy when M = 10⁶ or 10⁹. Extrapolating from 10⁴ to 10⁹ is unsupported, as the hierarchical pruning ratio (k_R, k_I, k_L = 128-64-16) may not preserve recall at vastly larger scales where cluster-level ambiguity increases. Without accuracy measurements at intermediate scales (e.g., 10⁵, 10⁶), the paper's headline claim is only half-verified.

- **The accuracy comparison with KBLaM is confounded by training data quality.** KBLaM is trained on synthetic data with 0.003% diversity; AtlasKV uses the KG2KV pipeline which produces 7.864% diversity (Table 1). The large accuracy gap shown in Table 3 could be substantially or entirely attributable to the data quality difference rather than the algorithmic contributions (HiKVP, projection heads). A controlled experiment—training KBLaM on KG2KV data or AtlasKV on synthetic data—is necessary to isolate the contribution of the method from the data pipeline. Without this, the paper overclaims the superiority of its algorithmic design.

- **The HiKVP ablation lacks necessary baselines to justify the hierarchical design.** HiKVP is compared only against "AtlasKV w/o HiKVP" (full attention). The paper does not compare against simpler baselines at the same computational budget: (a) flat top-k pruning over all M keys (which would have linear cost but might achieve similar accuracy preservation), (b) random pruning at the same budget, or (c) single-level clustering (only root keys, no hierarchy). Without these, the claim that the *hierarchical* structure is essential for sub-linear scaling while preserving accuracy is unsupported. The paper's derivation of cube-root complexity assumes perfect clustering, but never validates that the actual hierarchical mappings preserve accuracy better than simpler alternatives.

- **The ICL baseline in Figure 4's memory comparison appears inconsistent with the paper's own characterization of ICL.** The paper states that ICL with "more than 100 triples... over 48GB VRAM is required" (Section 5.2, Figure 5 discussion), yet Figure 4's caption describes ICL as staying below 20GB even at 10⁹ triples. This contradiction suggests that the ICL in Figure 4 may use a fundamentally different setup (possibly only storing KG embeddings rather than all triples in the context), making the comparison with AtlasKV's parametric approach misleading or at minimum poorly explained. The paper does not clarify what memory cost is being measured for ICL in Figure 4 versus what is described in the text.

### Minor

- **Missing ablation of the relation rewriting step.** The ablation study (Table 4) removes named or event entities but does not ablate the rewriting of relations into noun phrases (e.g., using raw relation strings as keys without rewriting). Since the rewriting step is a key part of KG2KV's claimed benefit (line 116 states it is "more beneficial than simple combinations"), its contribution should be isolated.

- **The OOD evaluation datasets from the ATLAS family may share latent distributions.** While ATLAS-Wiki (training), ATLAS-CC, and ATLAS-Pes2o (evaluation) come from different source documents, they originate from the same KG extraction pipeline and may share entity/relation distributions. Only Enron is truly from a different domain. The large improvements on ATLAS-CC and ATLAS-Pes2o may partly reflect data similarity rather than pure generalization.

- **No comparison with scalable graph RAG methods or CAG.** The paper mentions E² GraphRAG, LinearRAG, and CAG in related work but does not compare against them. While these follow a different (non-parametric) paradigm, including at least one comparison would strengthen the claim of superiority over the broader RAG landscape. The paper's positioning as a "parametric alternative to RAG" makes this comparison relevant.

- **GPT-4o as an automatic evaluator** has known biases (LLMs may score answers favorably when they match their own parametric knowledge). The paper uses 5 random seeds and standard error, which is standard practice, but no human evaluation or inter-annotator agreement is reported.

### Trivial

None.

## Nice-to-Haves

- Reporting the computational cost of offline preprocessing (UMAP+GMM clustering on billions of keys, LLM-based relation rewriting) would help practitioners assess the end-to-end practicality.
- Inference latency per query token as a function of KG size, in addition to memory, would strengthen the scalability analysis.
- Evaluation on a truly external KG (e.g., a Wikidata subset) would test generalization beyond the ATLAS family.

## Removed Points

- **Criticism that the 7.864% vs 0.003% diversity ratio is "likely an artifact"** — REMOVED. The comparison is between KG2KV (extracted from real KGs with millions of distinct relations) and the synthetic method from KBLaM (which uses fixed templates). The diversity gap is the *intended benefit* of KG2KV, not an artifact.
- **Criticism that Figure 4's memory comparison is "fundamentally misleading"** — PARTIALLY REMOVED. The ICL memory inconsistency is retained as a significant concern (moved to Major weaknesses). However, the stronger claim that the plot "cannot support the paper's core scalability claim" is softened: the memory savings of AtlasKV vs. KBLaM at scale are consistent with the complexity analysis and are a genuine contribution, even if the ICL comparison is questionable.
- **Claim that the paper miscomputes ICL's memory** — This cannot be fully verified from text alone. The inconsistency between the paper's text and the figure caption is flagged above, but the reviewer's stronger claim about "impossible" memory values is treated as a concern rather than a confirmed error.
- **Generic formatting/style nitpicks** — REMOVED per instructions.
- **Complaint about missing proofs in Appendix C (equivalence to rectangular attention)** — REMOVED per instructions (parser strips appendix).

## Novel Insights

None beyond the paper's own contributions. The reviews surface a recurring pattern in parametric KG-augmentation papers: the experimental design conflates data representation quality with algorithmic effectiveness, making it hard to attribute gains to the method versus the data. This paper is a clear example — the KG2KV pipeline likely accounts for much of the improvement over KBLaM, but the paper attributes it to AtlasKV as a whole. A cleaner experimental separation (training both methods on identical data) would resolve this.

## Suggestions

1. **Run accuracy experiments at intermediate scales (10⁵–10⁶ triples)** to demonstrate that HiKVP preserves retrieval accuracy as M grows. Without this, the "billion-scale" claim in the title is premature.
2. **Control for data quality**: train KBLaM on the same KG2KV training data and/or train AtlasKV on synthetic data. This will isolate whether the accuracy gains come from the method or from better training data.
3. **Add ablation baselines for HiKVP**: flat top-k pruning (at the same final k_L budget), random pruning, and single-level clustering. This will justify why the three-level hierarchy is necessary.
4. **Clarify the ICL setup in Figure 4** and resolve the contradiction between the text (ICL >48GB for 100+ triples) and the figure (ICL below 20GB at 10⁹). If embeddings rather than raw triples are being compared, state this explicitly.
5. **Report end-to-end inference latency** alongside memory, as the sub-linear time complexity is a core claim.
6. **Evaluate on at least one KG outside the ATLAS family** (e.g., Wikidata subset) to demonstrate domain-independence.

## Score and Decision

### Calibration Anchors

| Path | Avg Score | Comparison to AtlasKV |
|------|-----------|----------------------|
| `/home/wg25r/review_agent/human_reviews_2026/VKGTGGcwl6.md` (LLMs Get Lost In Multi-Turn Conversation) | 8.00 (Oral) | Stronger evaluation with comprehensive, well-controlled experiments that fully support all claims. AtlasKV has a larger evidential gap. |
| `/home/wg25r/review_agent/human_reviews_2026/9gw03JpKK4.md` (Gaia2 Benchmark) | 8.00 (Oral) | Rigorously benchmarked with diverse models and thorough analysis. AtlasKV's evaluation is less comprehensive. |
| `/home/wg25r/review_agent/human_reviews_2026/cvztBvlglK.md` (LMLM Pre-training) | 6.50 (Poster) | Similar topic (parametric knowledge handling). LMLM's core claims are better supported by experiments despite some limitations. AtlasKV's accuracy-at-scale gap is more severe. |
| `/home/wg25r/review_agent/human_reviews_2026/6Qc6sO1jh9.md` (Knowledgeable-R1) | 5.50 (Poster) | Both have identifiable evaluation gaps. Knowledgeable-R1's experiments are more thorough for its specific claims. AtlasKV has a stronger core idea but weaker overall evidence. |
| `/home/wg25r/review_agent/human_reviews_2026/1SMdxRtLBp.md` (MLP Memory) | 5.00 (Poster) | Comparable level: both have interesting ideas with some evaluation gaps. MLP Memory's missing baseline comparison mirrors AtlasKV's confounded comparison. |
| `/home/wg25r/review_agent/human_reviews_2026/XOu5z16cbY.md` (Hierarchical Memories Pretraining) | 4.80 (Poster) | Both use hierarchical structures for knowledge. AtlasKV has a clearer methodological contribution but similar evaluation weaknesses (unfair comparison in one baseline, insufficient ablations). |
| `/home/wg25r/review_agent/human_reviews_2026/idtEFFfWcI.md` (PARR) | 4.00 (Reject) | PARR had limited novelty and marginal gains. AtlasKV's contribution is stronger, and its empirical results vs. KBLaM are clearly positive. |
| `/home/wg25r/review_agent/human_reviews_2026/vm8TSA37Na.md` (GG-Explore) | 4.00 (Withdrawn) | Similar topic (KG-augmented LLMs). GG-Explore had pipeline complexity without strong justification. AtlasKV has a cleaner approach and better results. |
| `/home/wg25r/review_agent/human_reviews_2026/zbNWwHLJFw.md` (EfficientLLM) | 2.00 (Withdrawn) | Fundamentally flawed. AtlasKV is clearly stronger in every dimension. |

**Comparative reasoning:** AtlasKV sits between the 4–5 and 5.5–6.5 bands. Its core ideas (KG2KV, HiKVP) are genuinely novel and the empirical results against KBLaM are solid. However, the evaluation has significant gaps that prevent the strongest claims from being fully supported: accuracy is never measured at scale, the KBLaM comparison is confounded by data quality, the HiKVP ablation lacks basic baselines, and the ICL memory comparison is inconsistent with the paper's own text. Papers scoring in the 5.5–6.5 range (e.g., Knowledgeable-R1 at 5.5, LMLM at 6.5) have cleaner evaluations that better support their specific claims. Lower-scoring papers (4–5) tend to have similar evaluation gaps. Given the genuine contribution combined with notable evidential gaps, the appropriate score is **5.0**.

MY FINAL SCORE: <pineapple>5.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>