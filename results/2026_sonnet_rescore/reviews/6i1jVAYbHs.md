Now I have enough information to write the final consolidated review. Let me synthesize the findings from both reviewers against what the paper actually says.

---

## Summary

AtlasKV proposes a parametric knowledge-injection framework for augmenting LLMs with billion-scale knowledge graphs (KGs) within 20GB VRAM. Its two core contributions are (1) **KG2KV**, which converts KG triples into diverse query-key-value training data using natural relation-to-question rewriting, and (2) **HiKVP**, a hierarchical key-value pruning algorithm that offloads KV pairs to CPU and performs top-k retrieval through a three-layer hierarchy, reducing complexity from O(M) to O(M^(1/3)). The claimed result is that billion-scale KG augmentation is feasible on a single 48GB GPU, with strong OOD generalization that dramatically outperforms KBLaM.

---

## Strengths

1. **Theoretically sound sub-linear complexity reduction.** Table 2 correctly derives that AtlasKV achieves O(C_t·M^(1/3) + N)·N·D time and O(C_m·M^(1/3) + N)·(N+D) memory complexity, versus KBLaM's linear O((M+N)·N·D). The three-step CPU-GPU offloading scheme (Steps 1–3 in §4.2) is mechanically coherent, and the derivation is deferred to Appendix D.

2. **Strong OOD generalization improvement via KGKV training data.** Table 3 demonstrates that AtlasKV trained on ATLAS-Wiki-QKV data massively outperforms KBLaM on the harder OOD sets: e.g., on ATLAS-Pes2o-QKV with 10³ triples, AtlasKV w/o HiKVP achieves 100% Acc@1 versus KBLaM's best 50% (even at 20K steps vs. AtlasKV's 3K steps). These gains are consistent across three OOD evaluation sets and multiple KG sizes.

3. **Quantified data diversity advantage of KG2KV.** Table 1 shows KG2KV produces 7.864% diversity ratio vs. 0.003% for the Synthetic method, with lower average token cost (165.7 vs. 349.9). This directly supports the claim that natural KG triples provide richer query-attribute coverage at lower cost.

4. **HiKVP preserves attention accuracy well.** Table 3 shows that the pruned version (128-64-16) consistently maintains high accuracy: e.g., on ATLAS-CC-QKV with 10³ triples, pruned Acc@1 = 100.0 vs. unpruned 100.0; at 10² triples, 89.1 vs. 96.4, both far above KBLaM's 23.6. The accuracy drop from pruning is modest relative to the baseline gap.

5. **Well-designed ablation on entity mixing.** Table 4 cleanly isolates the contributions of named vs. event entities in KG2KV training data. Removing event entities causes a severe drop (e.g., ATLAS-Pes2o-QKV 10³ triples: Acc@1 falls from 100.0 to 49.0), while removing named entities also degrades performance. This validates the design choice of mixing both entity types.

---

## Weaknesses

### Fatal
None. The core complexity analysis is mathematically correct and the OOD generalization results are real, consistently measured empirical findings.

### Major

- **Figure 4 VRAM curves are almost certainly not fully measured, but are presented as if they are.** The paper states "we compare the GPU memory usage at inference time...across a wide range of KG sizes from 1 to 1B triples" (§5.2), and Figure 4 shows curves extending to 10^9 on the x-axis. However, all experiments were "performed on a single 48GB GPU" (§7 Ethics Statement), and KBLaM already exceeds 40GB at 10^5 triples. It is physically impossible to have directly measured KBLaM's VRAM at 10^6–10^9 triples on that hardware. The curves beyond ~10^5 triples must be derived from the complexity formulas rather than measured. The paper never discloses this. Presenting analytically-derived projections as empirical memory measurements without any clarification is misleading for the paper's headline claim ("billion-scale knowledge graphs in 20GB VRAM"). One sentence clarifying that Figure 4 combines measured data at feasible scales with formula-derived projections at larger scales would resolve this, but as written, the headline empirical claim is not supported by direct measurement.

- **The generation quality evaluation (Figure 5) is never applied to the scalable version of AtlasKV.** Figure 5 (GPTScore) shows only "AtlasKV w/o HiKVP" — i.e., the non-scalable version. The actually-scalable version (AtlasKV with HiKVP) is only evaluated on attention-accuracy proxies in Table 3. The paper therefore simultaneously claims scalability and quality, but demonstrates them only in isolation. Attention accuracy at the 15th layer is a proxy for generation quality; the relationship is not guaranteed when 99.998% of leaf-layer keys are pruned. Without an end-to-end GPTScore evaluation of the HiKVP-enabled system, the co-existence of scalability and quality is unproven.

- **Training data quality and architecture are confounded in all comparisons with KBLaM.** KBLaM is evaluated using Synthetic training data (diversity 0.003%), while AtlasKV uses KGKV data (diversity 7.864%). There is no experiment where KBLaM is trained on KGKV data, making it impossible to distinguish how much of AtlasKV's accuracy advantage comes from the data pipeline versus the attention formulation or training regime. Since KG2KV is itself one of two claimed contributions, the paper's architecture-level contribution (rectangular attention reformulation, HiKVP) is not cleanly isolated.

### Minor

- **Absence of a realistic retrieve-top-k RAG baseline.** The paper compares against ICL, which injects *all* triples into context — a computationally infeasible oracle at scale, not a realistic RAG system. A retrieve-top-k baseline using the same sentence encoder (all-MiniLM-L6-v2) placed in context would be directly comparable in embedding cost and would clarify whether the parametric injection mechanism adds value over simple embedding-based retrieval.

- **The 15th-layer attention metric is not validated across other layers.** The paper defers the rationale for choosing the 15th attention layer to Appendix A.2 (not visible due to parser stripping), and does not show that relative method rankings are stable across layers.

- **Three hierarchical layers are chosen with circular justification.** §4.2 states: "We set the number of layers to be 3, because that is the minimum number of layers to include all of the definitions we need in AtlasKV." No ablation compares 2-layer or 4-layer hierarchy; the choice is design-driven, not empirically motivated.

### Trivial
None worth noting.

---

## Nice-to-Haves

- Run AtlasKV with HiKVP at a genuinely large scale (e.g., 10^6–10^7 triples) and report both actual VRAM measurements and GPTScore. Even 1M triples with direct measurement of both metrics would close the two largest gaps simultaneously and make the headline claim defensible.
- Evaluate KBLaM trained on KGKV data. A single additional row in Table 3 ("KBLaM + KGKV training") would cleanly separate the data-pipeline contribution from the architectural contribution — a two-sentence experiment that would substantially clarify the paper's claims.
- Ablation on number of hierarchical layers (2 vs. 3 vs. 4) and on which attention layer is used for the grounding metric.

---

## Removed Points

*These points are flagged to be removed; treat them with caution.*

- **"The abstract says AtlasKV 'requires no external retrievers' while HiKVP itself performs retrieval."** (Harsh critic, framing critique.) Removed: HiKVP integrates retrieval-like operations inside the attention layer without an *external* retrieval module. The claim is architecturally valid on the paper's own terms.

- **"Diversity ratio counts many rare/semantically overlapping attributes."** (Harsh critic, §4.1 note.) Removed: This is speculation without a concrete anchor — the paper does not make fine-grained claims about attribute quality, only about count-level diversity. The concern may be real in principle but there is no specific section or number in the paper to anchor it.

- **"Evaluation of KG sizes [100–10,000] is several orders of magnitude below claimed capability"** as a standalone weakness. (Harsh critic.) Partially retained and merged into the major weakness about generation quality not being evaluated for the HiKVP-enabled version. As a standalone framing, it overstates the problem because the VRAM curve issue captures the root concern more precisely.

- **Strength Finder: "empirical memory measurements" at 1B triples.** Removed as a strength because, as established above, the Figure 4 curves almost certainly include formula-derived projections at large scales rather than pure measurements. The underlying complexity analysis remains a genuine strength.

---

## Novel Insights

The paper's most insightful observation — validated in Table 4 and discussed in §5.3 — is that combining event entities (semantically complex) with named entities (semantically simpler) in KG2KV training data is necessary for robust learning: named entities alone produce a model that cannot generalize to complex queries, while event entities alone are too difficult to learn from scratch. This "curriculum" intuition about training data composition for attention-based knowledge injection is a concrete, non-obvious finding with implications beyond AtlasKV.

---

## Suggestions

1. In Figure 4, add a footnote or caption line clarifying which portions of each curve are directly measured vs. computed from complexity formulas, and at what KG sizes direct measurement became infeasible. This is a one-sentence fix that addresses the most serious presentational concern.
2. Add a GPTScore curve for AtlasKV with HiKVP (128-64-16) to Figure 5. Given that Table 3 shows the accuracy gap between pruned and unpruned is modest, this experiment is likely to show that HiKVP does not catastrophically degrade generation quality — making it a positive result worth including.
3. Add a row "KBLaM (KGKV training)" to Table 3 to disentangle data vs. architecture contributions.
4. Report wall-clock inference latency alongside VRAM cost, since the sub-linear complexity reduction also reduces latency, and this is a practically important claim that the paper mentions but does not measure.

---

## Evaluation on Key Axes

- **Originality**: Moderate-high. HiKVP's application of hierarchical clustering to KV pruning for attention-based knowledge injection is novel. KG2KV's natural conversion of KG triples is clean and well-motivated. Neither is transformative individually, but together they address a real scalability wall in the KBLaM paradigm.
- **Importance of Research Question**: High. Scaling parametric knowledge injection to billions of triples under a 20GB memory budget is a practically important problem.
- **Claims Supported**: Moderate. The OOD generalization claims are well-supported. The billion-scale memory claims are theoretically sound but empirically unverified at the headline scale. The quality-at-scale claim is unverified for the scalable version.
- **Soundness of Experiments**: Moderate. The OOD evaluation design is good (three hard datasets, multiple KG sizes). The confounding of data and architecture, and the absent end-to-end evaluation of the scalable version, are real methodological gaps.
- **Clarity of Writing**: Good. The method sections are clear and the complexity analysis is presented transparently.
- **Value to Research Community**: Moderate-high. The KG2KV pipeline and diversity analysis are immediately applicable to practitioners; the HiKVP algorithm is a usable technical contribution.

MY FINAL SCORE: <score>4.5</score>
MY FINAL DECISION: <decision>Reject</decision>

<subscores>
<originality>3</originality>
<importance>4</importance>
<claims_supported>2</claims_supported>
<soundness>2</soundness>
<clarity>4</clarity>
<community_value>3</community_value>
</subscores>