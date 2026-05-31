## Summary

The paper identifies and addresses *Dual-level Noisy Correspondence* (DNC) in Multi-Modal Entity Alignment (MMEA): misalignments in both intra-entity (entity-attribute) correspondences and inter-graph (entity-entity and attribute-attribute) correspondences. The proposed RULE framework estimates correspondence reliability via a two-fold principle (uncertainty from Dempster-Shafer Theory and a consensus measure), uses this reliability during training through a Dually Robust Learning (DRL) loss and Dually Robust Fusion (DRF), and adds a test-time correspondence reasoning (TTR) module powered by a large multimodal LLM (Qwen2.5-VL-72B) with Chain-of-Thought prompting. Experiments on five benchmarks across three noise settings demonstrate consistent improvements over seven SOTA baselines.

---

## Strengths

- **Well-motivated, novel problem framing.** The DNC problem is practically important—>50% of ICEWS benchmarks contain inherent noisy correspondences—and the paper is among the first to address it systematically at both the intra-entity and inter-graph levels simultaneously. The formal problem setup in §2.1 cleanly distinguishes the three types of noisy correspondence.
- **Principled reliability estimation.** Grounding uncertainty in Dempster-Shafer / Subjective Logic and pairing it with a consensus measure (Eq. 5) is theoretically motivated. Theorem 1 formally justifies why uncertainty alone is insufficient, motivating the two-fold design. The adaptive thresholding in Eq. 8 (calibrated on true positive pairs) is a clean self-supervised mechanism.
- **Comprehensive ablation study.** Table 3 isolates each component (DRL, DRF, Uncertainty-only, Consensus-only, TTR), confirming each contributes positive gains. The margin for the training-time core (w/o TTR: 56.5 vs. best baseline 42.4 on Non-name 50% DNC) demonstrates that the base approach is independently effective regardless of the MLLM module.
- **Strong empirical results across diverse settings.** RULE consistently outperforms all seven baselines across five datasets, three noise levels, and two evaluation protocols, with particularly large margins on the challenging ICEWS benchmarks (e.g., 58.2 vs. 43.9 at 50% DNC on ICEWS-WIKI Non-name). Fig. 3(a) shows slower degradation as noise increases from 0 to 70%, which is compelling.
- **Reliability visualization is interpretable.** Fig. 3(b) and Fig. 5 show that estimated reliability cleanly separates clean/noisy pairs and correctly suppresses corrupted attributes during fusion, providing strong qualitative validation.

---

## Weaknesses

### Fatal
None.

### Major

1. **Unfair test-time comparison via TTR.** The main results tables include gains from TTR, which invokes Qwen2.5-VL-72B-Instruct at inference time. No baseline uses an MLLM of comparable scale. While the ablation shows RULE without TTR still outperforms baselines in the Non-name setting, the All-attributes 50% DNC case in Table 3 reveals that w/o TTR (H@1 = 94.0) barely exceeds MEAformer (91.9) by 2.1 points, whereas the default with TTR (97.7) creates a 5.8-point gap. The paper should either (a) include a baseline augmented with the same MLLM or (b) present w/o-TTR numbers prominently in the main tables alongside the MLLM-augmented numbers, so the reader can clearly attribute gains.

2. **No computational cost analysis.** TTR queries Qwen2.5-VL-72B for each entity pair under consideration. MMEA datasets can involve thousands of entities. The paper provides no inference time, FLOPs, or API call count comparison, making it impossible to assess practical deployability relative to baselines. For a test-time module built around a 72B parameter model, this is a significant omission.

3. **Assumption 1 is unvalidated.** The greedy marginal contribution strategy (Eq. 7), used to identify reliable intra-entity correspondences at inference time, rests entirely on Assumption 1 ("if x_i^m is correctly associated, then Δ ≥ 0"). This is stated as an assumption without empirical or theoretical justification. If it fails for common attribute types (e.g., uninformative structural triples), the entire DRF reliability estimate at test time is unreliable.

### Minor

1. **Circular reliance on noisy labels during training.** The consensus c_i in Eq. 5 directly uses the annotated (potentially noisy) correspondence y_i during training, even though the goal is to identify which labeled correspondences are noisy. The paper proposes using the greedy estimate only during inference; a brief discussion of how this circularity is bounded or managed during training would strengthen the method.

2. **Ablation scope is narrow.** Table 3 reports only ICEWS-WIKI under the 50% DNC setting. Given the large performance variation across datasets (e.g., ICEWS-WIKI vs. DBP15K have very different noise profiles), ablations on at least one DBP15K dataset would better support the general applicability of the component design.

3. **TTR "MLLM Enhance" baseline is unclear.** In Table 3, "MLLM Enhance" (56.6) performs nearly identically to "w/o TTR" (56.5) in the Non-name setting, implying the MLLM alone adds almost nothing. The paper attributes the gain of Full TTR (58.2) to combining rethinking scores with prior similarity, but the explanation in §3.3 is brief and could be more precisely quantified or analyzed.

### Trivial
None beyond the hard rules.

---

## Nice-to-Haves

- A wall-clock time / throughput comparison between RULE (with and without TTR) and at least one fast baseline would greatly aid practitioners.
- An experiment showing RULE generalized to a third MMKG setup (e.g., DBP-FB) would reinforce robustness claims.

---

## Novel Insights

The paper's most genuinely novel insight is the identification and formalization of *dual-level* noisy correspondence as a unified problem, combined with the observation that test-time noise (seemingly similar but actually distinct attributes) requires a qualitatively different treatment from training-time noise. The use of evidence accumulation from Subjective Logic to compute uncertainty directly from cross-graph similarities—without any auxiliary clean set or two-network scheme—is a clean and practical adaptation of principled uncertainty quantification to the entity alignment setting. The observation (Theorem 1) that low uncertainty does not imply correctly concentrated belief motivates the consensus complement, which is a subtle but important point missing from most prior noisy-label learning frameworks.

---

## Suggestions

1. Report "Ours w/o TTR" as a separate row in Tables 1 and 2 alongside the full RULE. This lets readers accurately assess the contribution of the training-time design versus the MLLM-augmented inference.
2. Add a cost table (query count × MLLM inference time per entity) and compare against total baseline training+inference cost to contextualize the TTR overhead.
3. Empirically validate Assumption 1 on a held-out entity set by measuring how often Δ < 0 for known clean attributes, as a sanity check for the greedy strategy.
4. Extend Table 3 ablations to at least one DBP15K dataset to confirm component contributions generalize beyond ICEWS-WIKI.

---

## Score and Decision

The paper introduces a well-motivated new problem, provides a principled and effective framework, and supports claims with comprehensive experiments and ablations. The main concern—unfair comparison due to the 72B MLLM in TTR—is partially mitigated by ablations demonstrating that the training-time core independently beats baselines by wide margins in most settings. The lack of computational cost reporting and the unvalidated Assumption 1 are notable gaps, but do not invalidate the core claims. The work is a solid contribution to the MMEA and noisy-correspondence learning communities.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>