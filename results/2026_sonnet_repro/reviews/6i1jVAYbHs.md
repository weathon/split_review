**Round 1 bracket: 4.0–6.5.** KBLaM (the direct predecessor) scored 5.80. AtlasKV is technically more ambitious but has notable evaluation gaps. Let me narrow within this range.Now I have enough information to write the final consolidated review. Let me synthesize everything from the paper reading and calibration.

---

## Summary

AtlasKV proposes a parametric knowledge injection framework that extends the KBLaM paradigm to billion-scale knowledge graphs (KGs). Its two core contributions are: (1) **KG2KV**, a pipeline that naturally converts KG triples into Q-K-V training data with substantially higher diversity than prior synthetic data generation; and (2) **HiKVP**, a three-layer hierarchical key-value pruning algorithm that reduces inference memory complexity from linear O(M) to sub-linear O(M^(1/3)), enabling augmentation of LLMs with up to 1B triples within 20GB VRAM. The paper demonstrates meaningful OOD generalization improvements over KBLaM across three evaluation datasets and validates HiKVP's attention-level accuracy at KG sizes up to 10³ triples.

---

## Strengths

- **Sound sub-linear complexity analysis (Table 2, Section 4.2):** The three-step HiKVP derivation correctly achieves O(C_m · M^(1/3)) memory complexity. The step from Step 1 (root keys: M^(1/3) vectors on GPU) to Step 2 (inter-layer keys: k_R · M^(1/3)) to Step 3 (leaf-level values: k_L vectors) is mechanically correct and clearly explained. This is a genuine algorithmic contribution over KBLaM's linear complexity.

- **Dramatic OOD generalization improvements via KG2KV (Table 3):** AtlasKV trained on KGKV data achieves 100% Acc@1 at 10³ triples on ATLAS-Pes2o-QKV versus KBLaM's best 50% at 20K training steps (vs. AtlasKV's 3K). On ATLAS-CC-QKV (the hardest dataset), the Acc@1 improvement over KBLaM reaches 49-71 percentage points across scales. These results strongly support the KG2KV contribution.

- **Validated data quality improvements (Table 1):** KG2KV achieves a diversity ratio of 7.864% versus 0.003% for the Synthetic method, with lower average token cost (165.7 vs. 349.9). These are concrete, quantified improvements that directly explain the generalization gains.

- **HiKVP preserves grounding accuracy under aggressive pruning (Table 3):** The pruned AtlasKV (128-64-16) maintains strong Acc@1 across all three OOD datasets (e.g., ATLAS-CC-QKV at 10² triples: 89.1% pruned vs. 96.4% unpruned, still far above KBLaM's 23.6%). This demonstrates that hierarchical pruning does not catastrophically degrade grounding accuracy at the attention level.

- **Well-executed ablation on entity types (Table 4):** The comparison of full KG2KV vs. named-entity-only vs. event-entity-only variants clearly validates the design choice of combining both entity types. Removing event entities causes severe accuracy drops (e.g., ATLAS-Pes2o-QKV at 10³ triples: 72.7% → 34.5%), while removing named entities hurts early-scale performance.

---

## Weaknesses

### Fatal
None.

### Major

- **The 1B-triple headline claim is not empirically validated at the quality level.** The paper's title, abstract, and Figure 1 center on "billion-scale KGs in 20GB VRAM." Figure 4 shows a VRAM curve extending to 10^9 triples, but the caption ("GPU memory usage comparison across various KG sizes from 1 to 1B triples") does not state whether the values at large scales are directly measured or extrapolated from the O(M^(1/3)) formula. All experiments were run on a single 48GB GPU. Meanwhile, quality evaluation (Table 3, Figure 5) only reaches 10³–10⁴ triples — five to six orders of magnitude below the claimed scale. The paper simultaneously claims scalability and quality, but only demonstrates them at scales separated by many orders of magnitude. Whether Figure 4's curve is a measurement or an analytical projection is the single most important clarification the paper needs.

- **HiKVP and generation quality are never evaluated together.** Figure 5 (GPTScore, the paper's only end-to-end quality metric) evaluates exclusively "AtlasKV w/o HiKVP." Table 3 evaluates the HiKVP-enabled version only on attention accuracy (Top-1/5 at layer 15), a proxy metric. The scalable version that actually realizes the billion-scale claim is never shown to produce high-quality answers. Given that HiKVP prunes 99.98% of leaf-layer keys (e.g., k_L=16 out of M=10⁵), generation quality degradation — beyond what the attention proxy captures — is a genuine unverified concern.

- **The AtlasKV vs. KBLaM accuracy comparison confounds training data and architecture.** AtlasKV is trained on KGKV data (7.864% diversity) while KBLaM is trained on Synthetic data (0.003% diversity). There is no experiment in which KBLaM is trained on KGKV data. The dramatic accuracy improvements in Table 3 cannot be attributed to the attention formulation vs. the data pipeline in isolation. Since KG2KV is itself one of the paper's two primary contributions, this confound is not an error — but it means the paper's architectural novelty (the attention formulation itself) is never cleanly isolated.

### Minor

- **Three-layer hierarchy choice is circularly justified.** Section 4.2 states: "We select 3 layers because that is the minimum number of layers to include all of the definitions we need in AtlasKV." This is a design decision justified by the design itself, not by ablation or principled analysis. An ablation comparing 2-layer, 3-layer, and 4-layer hierarchies would significantly strengthen this choice.

- **Knowledge grounding proxy is single-layer and unexplained.** Table 3's Top-1/5 accuracy is computed from averaged post-softmax attention scores "at the 15th layer due to the reason described in Appendix A.2." The appendix is stripped, and the paper does not report whether the same relative ordering between methods holds at other layers. The robustness of this proxy to layer choice is unverified.

- **GPTScore evaluation is noisy and small-scale relative to the claims.** Figure 5 evaluates generation quality at 10²–10⁴ triples using 5 seeds × 5 generations. The standard error bands are visible. This scale is 5–7 orders of magnitude below the headline claim, and the small sample size makes the signal noisy.

### Trivial
None that the filtering rules would retain.

---

## Nice-to-Haves

- **A measured VRAM experiment at ≥10⁶ triples with HiKVP enabled**: Even demonstrating VRAM ≤20GB and stable GPTScore at 1M triples (vs. theoretical extrapolation to 1B) would substantially strengthen the paper's central claim.

- **GPTScore evaluation for AtlasKV (128-64-16)**: Adding the HiKVP-enabled version to Figure 5 at scales up to 10⁴ triples would close the most important gap — demonstrating that scalability and generation quality co-exist.

- **KBLaM trained on KGKV data** (one additional row in Table 3): This single experiment would cleanly isolate the contribution of the attention architecture from the data pipeline.

- **Inference latency benchmarks**: CPU-to-GPU transfer at each attention layer during HiKVP inference may introduce non-trivial latency. A wall-clock comparison against KBLaM and ICL would complete the efficiency picture.

- **A practical top-k RAG baseline**: A retrieve-top-k system using the same sentence encoder (all-MiniLM-L6-v2) placed in context at matched retrieval budget would clarify whether parametric injection adds value over the embedding model's retrieval ability at moderate scales.

---

## Removed Points

*These points are flagged to be removed; treat them with caution.*

1. **"Abstract says no external retrievers but HiKVP does nearest-neighbor-style lookups"** — REMOVED. The sentence encoder is used offline to precompute KV embeddings before inference; HiKVP's hierarchical search is an internal attention computation, not an external retrieval pipeline at query time. The distinction is architecturally meaningful.

2. **"Diversity ratio counts many semantically overlapping relation types that don't contribute to OOD generalization"** — REMOVED. This is speculative with no concrete anchor in the paper. There is no evidence that the relations are semantically redundant.

3. **"Missing retrieve-top-k RAG baseline is the most critical gap"** — DEMOTED to nice-to-have. The paper is explicitly a parametric method paper; the relevant comparison class is the parametric paradigm (KBLaM) and the oracle non-parametric bound (ICL with all triples). A top-k RAG baseline would strengthen but is not required for the core contribution.

4. **"The paper cannot be accepted"** from the harsh critic's assessment overweighting of the confounded comparison — SOFTENED. The confound is real but does not invalidate the contribution: the paper's contribution is *the system* (KG2KV + HiKVP), and the system as a whole does outperform KBLaM by a very large margin. The architectural question is scientifically interesting but not a fatal invalidation.

5. **Strength: "Comprehensive evaluation across multiple datasets"** from the Strength Finder — KEPT. The three OOD evaluation datasets (Enron, ATLAS-CC-QKV, ATLAS-Pes2o-QKV) at four KG sizes with two metrics genuinely goes beyond a single narrow benchmark.

---

## Novel Insights

The structural observation that KG triples (h, r, t) map naturally onto Q-K-V semantics — with the query drawn from questioning prefixes of the key, the key encoding the unmasked entity and relation, and the value encoding the masked entity — provides a principled and elegant motivation for parametric knowledge injection via existing attention layers. This triple-to-QKV decomposition is more principled than prior synthetic approaches with fixed human-defined schemas. The empirical finding from the ablation (Table 4) that *both* named entities (simpler, easier to learn from) and event entities (semantically complex, necessary for generalization) are required — with event entities providing a form of curriculum complexity that enables the attention heads to generalize to novel relation types — is a counterintuitive and potentially broadly applicable insight about training data design for parametric knowledge injection.

---

## Suggestions

1. **One sentence in Figure 4's caption or main text clarifying whether the VRAM curve at >10⁵ triples is directly measured or analytically derived** from the O(M^(1/3)) formula. This single clarification determines the paper's primary empirical claim status.

2. **Add AtlasKV (128-64-16) to Figure 5.** Even at 10⁴ triples, this would directly test whether the scalable configuration generates high-quality answers. If the GPTScore drop relative to the unpruned version is small, the paper's headline claim becomes substantially more credible.

3. **Add a "KBLaM trained on KGKV" row in Table 3.** This is the single most informative ablation the paper could add without new infrastructure: it directly isolates whether the accuracy improvement comes from data quality or architecture.

4. **Report end-to-end inference latency** (prefill + generation time per query) for HiKVP at representative KG sizes. The CPU↔GPU transfer at each attention layer is a non-trivial overhead in practice.

---

## Score and Decision

**Anchors retrieved:**

| Path | Avg Score | Round | Comparison |
|------|-----------|-------|------------|
| aLsMzkTej9.md (KBLaM) | 5.80 | R1 | Direct predecessor; AtlasKV is more ambitious but has larger evaluation gaps |
| sl4hOq9wm9.md (In-context or In-parameter) | 5.50 | R1 | Rejected; AtlasKV has more genuine novelty |
| mIEHIcHGOo.md (Neural Nuggets) | 6.67 | R1 | Accepted; well-evaluated parametric knowledge transfer; AtlasKV weaker on evaluation |
| pG820nmDvy.md (Huge Context on Tiny GPUs) | 4.67 | R2 | Rejected; similar issue of large-scale claims without full empirical support; AtlasKV is more complete |
| dSneEp59yX.md (Cascading KV Cache) | 6.00 | R2 | Accepted; clean methodology, measured results; AtlasKV lacks comparably measured experiments at claimed scale |
| z1ohBxWeL2.md (SwiftKV) | 5.50 | R2 | Rejected; efficiency-focused KV cache paper with similar completeness level |
| Hjk1tWIdvL.md (HASA) | 5.00 | R2 | Rejected; hierarchical attention efficiency with similar empirical scope |
| 22OTbutug9.md (RA-DIT) | 6.25 | R2 | Accepted; retrieval-augmented instruction tuning with cleaner evaluation |

**Round 1 bracket: 4.0–6.5**

**Round 2 narrowing:** AtlasKV is clearly stronger than "Huge Context on Tiny GPUs" (4.67) — it has well-defined OOD accuracy metrics, a clean complexity analysis, and ablations. It sits below KBLaM (5.80) due to the evaluation gaps that are central, not peripheral, to its headline claim: the scalable version (HiKVP) is never shown to produce high-quality answers, and the VRAM curve at 1B triples is of ambiguous provenance. The paper lands close to "Cascading KV Cache" (6.0) in ambition but below it in empirical completeness. Among rejected papers, it sits above "In-context or In-parameter?" (5.50) and "SwiftKV" (5.50) due to stronger and more novel contributions, but the evaluation gaps make acceptance hard to justify.

**Final score: 5.0. Decision: Reject.**

The paper makes real, technically sound contributions (sub-linear complexity, KG2KV data pipeline, strong OOD results), but its headline claim — billion-scale augmentation with maintained quality — is never jointly demonstrated. The three improvements suggested (Figure 4 clarification, HiKVP+GPTScore, KBLaM-on-KGKV ablation) are not major experiments; they are targeted additions that would transform this into a clear acceptance.

---

**Originality:** Moderate-to-high. The sub-linear KV hierarchical pruning for knowledge injection is novel; KG2KV's triple-to-QKV mapping is an elegant insight.

**Importance of research question:** High. Scaling parametric knowledge injection beyond thousands of triples is a real and important bottleneck.

**Claims vs. support:** The internal results are well-supported; the headline "1B triples" claim is supported only at the VRAM level with ambiguous measurement provenance.

**Soundness of experiments:** The experiments that exist are well-executed; the gaps are in what is missing (HiKVP generation quality, scale of actual empirical evaluation).

**Clarity of writing:** Good. The paper is well-organized and clearly written.

**Value to research community:** High if the evaluation gaps are closed; moderate as-is.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>