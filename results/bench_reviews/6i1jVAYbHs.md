Now I have all the information needed. Let me produce the final consolidated review.

## Summary

This paper proposes AtlasKV, a parametric framework for augmenting LLMs with knowledge graphs at billion-triple scale under very low GPU memory (less than 20GB VRAM). Two key innovations are introduced: (1) **KG2KV**, which converts KG triples (head, relation, tail) into high-diversity Q-K-V training data by exploiting the natural structural alignment between triples and attention mechanisms, and (2) **HiKVP** (Hierarchical Key-Value Pruning), which organizes KGKV keys into a 3-level hierarchy and prunes them at inference time to achieve sub-linear time and memory complexity of  \(\mathcal{O}((C_t\sqrt[3]{M}+N)\cdot N \cdot D)\) . Experiments on three OOD datasets (Enron, ATLAS-Pes2o-QKV, ATLAS-CC-QKV) show that AtlasKV substantially outperforms KBLaM on knowledge grounding accuracy (e.g., 90–100% vs. 40–60% ACC@1 at 10³ triples on difficult datasets) while requiring only 3K training steps instead of 20K, and the GPU memory plot indicates flat scaling up to 1B triples.

## Strengths

- **Scalability via sub-linear complexity with empirical memory validation.** Figure 4 demonstrates that AtlasKV's VRAM usage stays below 20GB even at 1B triples, while KBLaM exceeds 40GB at only 100K triples. This is backed by the rigorous complexity analysis in Table 2 (\(\mathcal{O}((C_t\sqrt[3]{M}+N)\cdot N\cdot D)\) vs. KBLaM's linear \(\mathcal{O}((M+N)\cdot N\cdot D)\)), and the hierarchical design is clearly described (Section 4.2, Steps 1–3).

- **Substantial and consistent accuracy gains on hard OOD benchmarks.** On ATLAS-Pes2o-QKV and ATLAS-CC-QKV, AtlasKV achieves 90–100% ACC@1 vs. KBLaM's 40–60% at 10³ triples (Table 3), with improvements of 40–72 percentage points. The gains are consistent across KG sizes from 10³ down to 10⁰ triples and across all three OOD datasets, demonstrating robust generalization.

- **KG2KV's data diversity advantage is well quantified.** Table 1 shows that KG2KV yields 7.864% diversity ratio vs. 0.003% for the synthetic method, with lower average token cost (165.7 vs. 349.9). This explains AtlasKV's strong OOD performance: even on Enron, where KBLaM's training data contains the exact same enquiry attributes, AtlasKV outperforms it because KG2KV's higher diversity enables generalization to unseen query patterns.

- **Training efficiency.** AtlasKV achieves high accuracy in only 3K training steps, compared to 20K for KBLaM (Table 3). For instance, on ATLAS-Pes2o-QKV with 10² triples, AtlasKV w/o HiKVP reaches 92.7% ACC@1 at 3K steps while KBLaM at 20K steps only reaches 25.5%.

- **Ablation study validates the KG2KV entity-type design.** Table 4 confirms that both named entities and event entities contribute to performance, with the full combination outperforming either type alone, supporting the design choice in Section 4.1.

## Weaknesses

### Fatal

None.

### Major

- **Accuracy is not evaluated at the billion-scale the title and abstract emphasize.** The paper claims "billion-scale KGs" and "superior knowledge grounding performance," but knowledge grounding accuracy (Table 3) is only measured for KG sizes up to \(10^3\) triples. While the GPU memory plot (Figure 4) extends to \(10^9\), there is no accuracy or generation quality measurement for \(10^5\), \(10^7\), or \(10^9\) triples. The sub-linear complexity analysis strongly suggests the method should scale, and measuring memory at scale is valuable, but the paper's headline claim bundles scalability *with* effectiveness — and effectiveness at billion-scale remains unsubstantiated. This is the single most important experiment missing from the paper.

### Minor

- **The comparison with KBLaM is confounded by different training data.** AtlasKV is trained on KG2KV-constructed ATLAS-Wiki-QKV data, while KBLaM uses its original synthetic data (Table 3). Because KG2KV is presented as a core contribution of AtlasKV, comparing full systems is valid for evaluating *the complete AtlasKV pipeline*. However, this design means the reported gains cannot be decomposed: it is unclear how much comes from better training data (KG2KV) vs. better attention/pruning mechanics (HiKVP). A controlled experiment training KBLaM on KG2KV data would cleanly isolate the method-level improvement over KBLaM's architecture.

- **HiKVP is not compared against simpler flat top-\(k\) retrieval.** The ablation compares AtlasKV with HiKVP to AtlasKV without HiKVP (which uses all keys), but never to a flat top-\(k\) retrieval from the full key set with the same computational budget. If simple top-\(k\) achieves similar accuracy at similar cost, the hierarchical design adds complexity without clear benefit. The paper also only tests one hyperparameter configuration for HiKVP (128-64-16) in the main results, though different settings are examined in the appendix (Appendix B.4.1).

- **Lack of inference latency breakdown.** Figure 4 reports GPU memory, but there is no corresponding analysis of inference latency (prefill + decoding time) as KG size grows. For a method claiming sub-linear complexity, runtime measurements at multiple scales would strengthen the practical efficiency claims.

### Trivial

- The paper's title and abstract emphasize "billion-scale" but the conclusions about accuracy are drawn from experiments at much smaller KG sizes. Qualifying the scope of accuracy results more explicitly would improve precision.
- The relation between Figure 4 and whether it is empirically measured or computed from theoretical formulas is not explicitly stated. The text says "compare the GPU memory usage at inference time" which implies measurement, but a clear statement would help.

## Nice-to-Haves

- **Flat top-\(k\) baseline for HiKVP:** A comparison against single-level top-\(k\) retrieval from all keys, matched for computational budget, would directly justify the hierarchical design.
- **Data-controlled KBLaM experiment:** Training KBLaM on the same KG2KV data used for AtlasKV would isolate method effects from data effects.
- **Sensitivity analysis of HiKVP hyperparameters:** Evaluating more configurations of \(k_R, k_I, k_L\) with accuracy and runtime would demonstrate robustness.
- **End-to-end downstream task evaluation** (e.g., QA) on a standard benchmark with a large KG would complement the knowledge grounding accuracy measure.

## Removed Points

*These points are flagged to be removed, treat them with caution*

- Harsh critic's claim that "HiKVP *is* a retrieval pipeline and thus inherits retriever-like limitations, contrary to the 'no external retrievers' claim." — The paper claims no need for an *external* retriever module, which is accurate since HiKVP operates within the attention mechanism. This is a semantic distinction, not a factual error.
- Harsh critic's claim that "the 'Synthetic' method is not defined" and "diversity ratio" metric concerns. — The synthetic method is referenced (used in KBLaM) and the diversity ratio is clearly defined as "number of unique enquiry attributes divided by the total number of triples." The criticism is not grounded in the paper's actual content.
- Harsh critic's claim that Table 1 comparison "could be driven by superficial differences in how enquiry attributes are counted." — This is speculative and unsupported by evidence in the review.
- Strength Finder's generic claim about "training efficiency" being a separate strength — This is actually well-supported by Table 3 data, so kept. No generic strengths to remove.

## Novel Insights

The reviewers surface an interesting gap between how the paper frames its contribution and what it actually validates. The headline "billion-scale" claim rests on two legs: memory scalability (which is validated) and grounding accuracy at scale (which is not). This mismatch is common in systems papers that propose a theoretical complexity improvement — the paper would benefit from either explicit accuracy measurements at larger scales (even \(10^5\) or \(10^6\) triples with sampled ground truth) or sharper scoping language that separates "scalable" (memory) from "accurate at scale" (accuracy). The KG2KV contribution is arguably the stronger and better-validated part of the paper, whereas HiKVP's novelty over simpler pruning methods requires more rigorous baselining.

## Suggestions

1. **Add accuracy results at larger KG sizes.** Even evaluating at  \(10^5\) or \(10^6\) triples with ground-truth subsampling would significantly strengthen the billion-scale claim.
2. **Run a controlled KBLaM experiment.** Train KBLaM on the KG2KV training data (or AtlasKV on synthetic data) to isolate method from data effects.
3. **Compare HiKVP against flat top-\(k\) retrieval** from all keys under matched computational budgets.
4. **Report inference latency** (prefill + decoding) across KG sizes to complement the memory plot.
5. **Explicitly state** whether the memory measurements in Figure 4 are empirical or derived from the complexity formulas.

## Score and Decision

**Score calibration against anchors:**

* **Low-scoring anchor (avg 3.00, Reject):** *Combining-on-Graph (xgrG17OC3Q)* — Rejected for limited novelty and narrow evaluation. AtlasKV has substantially stronger novelty (two novel components, KG2KV+HiKVP) and more thorough evaluation (3 OOD datasets, ablation, scalability analysis). Clearly stronger.
* **Low-scoring anchor (avg 3.00, Reject):** *IntuitiveGraphLLM (91jL62CQF1)* — Negligible performance gains over baselines. AtlasKV's gains (40–72% improvements over KBLaM) are far larger and more convincing.
* **Medium-scoring anchor (avg 4.00, Reject):** *PARR (idtEFFfWcI)* — Rejected despite decent novelty for heavy compute cost and marginal improvements. AtlasKV's efficiency advantage is core to its contribution, and its accuracy gains over baselines are much larger, making it the stronger paper.
* **Medium-scoring anchor (avg 5.00, Accept Poster):** *PARoG (g6XnP7Sgui)* — Accepted with similar evaluation quality. AtlasKV has more novel methodological components (KG2KV data conversion, HiKVP pruning) whereas PARoG's contribution is more architectural. AtlasKV is slightly stronger in novelty but has the missing billion-scale accuracy gap.
* **High-scoring anchor (avg 6.50, Accept Poster):** *LMLM (cvztBvlglK)* — A pre-training paradigm paper with foundational novelty and thorough evaluations. AtlasKV is less ambitious (fine-tuning, not pre-training) but has clearer practical wins. LMLM is more thoroughly validated across dimensions.
* **High-scoring anchor (avg 7.00, Accept Poster):** *Fast-dLLM (3Z3Is6hnOT)* — Training-free acceleration with thorough ablations and strong speedup numbers. AtlasKV has comparable experimental breadth but lacks the same level of thorough sensitivity analysis.

**Judgment:** AtlasKV makes two well-motivated, clearly explained contributions (KG2KV and HiKVP) with strong empirical results at tested KG sizes, clear memory scalability evidence, and consistent OOD gains. The primary weakness — missing accuracy evaluation at billion-scale — is significant and prevents the paper from being a strong accept. However, it does not invalidate the core contributions, which are validated at the scales where ground truth is practical. The confounded KBLaM comparison and lack of flat top-\(k\) baseline for HiKVP are addressable concerns. Relative to the calibration anchors, the paper sits between the 5.0 band (accepted with moderate concerns) and the 6.5 band (stronger acceptance). Given the novel components and strong results at tested scales, but tempered by the missing large-scale accuracy experiment, a score of **5.5** and **Accept (Poster)** is appropriate.

MY FINAL SCORE: <pineapple>5.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>