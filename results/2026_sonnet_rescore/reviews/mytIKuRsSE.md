Now I have enough information to write the final consolidated review. Let me verify the key factual claims from the harsh critic against the actual paper data.

**Critical verification**: The harsh critic claims "RULE without TTR achieves H@1 = 94.0, while the best baseline (MEAformer) achieves 94.7" — but from Table 2, for 50% DNC ICEWS-WIKI All-attributes, MEAformer achieves H@1 = 91.9 (not 94.7). RULE w/o TTR (Table 3) achieves H@1 = 94.0. So 94.0 > 91.9: the training-time RULE *does* beat the best baseline even in this setting. The harsh critic's pivotal factual assertion is wrong, which substantially changes the severity of that concern.

---

## Summary

This paper identifies and studies Dual-level Noisy Correspondence (DNC) in Multi-Modal Entity Alignment (MMEA) — a practical problem where both intra-entity (entity-attribute) and inter-graph (entity-entity, attribute-attribute) correspondences contain annotation noise. To address DNC, the authors propose RULE, a framework that estimates correspondence reliability using a two-fold principle (uncertainty + consensus), applies reliability-aware robust training losses (DRL) and attribute fusion (DRF), and supplements training-time robustness with a Test-time Correspondence Reasoning (TTR) module powered by a large vision-language model. Extensive experiments on five benchmarks against seven state-of-the-art methods demonstrate consistent and often substantial improvements across multiple noise levels.

---

## Strengths

- **Empirically grounded problem motivation**: The paper demonstrates that real-world MMEA benchmarks contain over 50% noisy correspondences (Appendix B, Introduction) and shows via Fig. 1(b) that both vanilla adaptive fusion and concatenation degrade significantly under inter-graph and intra-entity NC, while RULE does not. This directly establishes the practical importance of DNC.

- **Reliability estimation effectively separates clean from noisy pairs**: The combination of Dempster-Shafer-based uncertainty (Eqs. 2–3) and consensus (Eq. 5) yields reliability scores (Eq. 1) that demonstrably distinguish clean and noisy pairs. Fig. 3(b) shows clean pairs concentrating in high-reliability regions and noisy pairs in low-reliability regions, and Fig. 4 shows the three subsets (S_U, S_I, S_C) forming distinct clusters in uncertainty-consensus space. This validates the core reliability estimation mechanism.

- **Strong and robust empirical results**: RULE outperforms all seven baselines across all five benchmarks and three noise levels (Tables 1–2). At the hardest tested setting (50% DNC, Non-name), RULE achieves H@1 = 58.2 vs. the next best 43.9 (HHREA) on ICEWS-WIKI. Critically, from Table 3, RULE *without* TTR achieves H@1 = 56.5 (Non-name) and 94.0 (All-attributes) under 50% DNC on ICEWS-WIKI, both exceeding the best baselines (43.9 and 91.9 respectively), confirming the training-time contributions are independently meaningful.

- **Informative ablation**: Table 3 isolates each component: removing DRL collapses H@1 from 58.2 to 31.6 (Non-name); removing DRF drops it to 50.4; removing TTR yields 56.5. The combination of uncertainty and consensus principles (vs. either alone) is also tested, showing both components are necessary.

- **Qualitative validation of DRF**: Fig. 5 shows that artificially injected noise in an attribute is reflected by low reliability weights, while clean attributes retain high weights, directly supporting the DRF design rationale.

---

## Weaknesses

### Fatal
None.

### Major

- **TTR asymmetry not transparently disclosed in main tables**: The full "Ours" row in Tables 1–2 incorporates Qwen2.5-VL-72B-Instruct (Section 3.1), while no baseline receives access to an equivalent MLLM. The paper states "for fair comparisons, we adopt the same backbone (i.e., CLIP) for all baselines and our method" (Section 3.2), but this refers only to the attribute encoders, not the 72B inference-time VLM. While RULE w/o TTR *does* exceed the best baseline in all tested settings (from Table 3), presenting the full system in main comparison tables without a separate "w/o TTR" row conflates two distinct capabilities (a learned alignment model vs. that model augmented with frontier VLM reasoning) and makes it difficult for readers to assess the true contribution of the training-time components vs. the VLM augmentation. A "w/o TTR" row should appear alongside baselines in Tables 1–2.

- **No runtime or cost analysis for TTR**: The TTR module queries a 72B VLM for inference over candidate entity pairs. On benchmarks like ICEWS-WIKI and DBP15K, this incurs significant cost. The paper provides no per-query timing, total inference time, or any discussion of scalability. Without this, the practical usability of the full RULE system cannot be assessed.

### Minor

- **Assumption 1 is unverified beyond qualitative evidence**: The inference-time consensus estimator relies on Assumption 1 — that an attribute correctly associated with an entity has non-negative marginal contribution to the similarity value function (Eq. 7). This assumption is stated but neither proved nor directly empirically validated (e.g., by measuring what fraction of greedy π* selections match the ground-truth clean subset in synthetic experiments where ground truth is known). The qualitative distribution plots (Figs. 3–5) provide indirect support but do not constitute a direct test.

- **Ablation limited to one dataset and one noise level**: Table 3 ablates on ICEWS-WIKI 50% DNC only. Component interactions (especially DRL + DRF) may behave differently at lower noise levels or on DBP15K, where inherent DNC rates differ. An ablation on at least one additional noise level or dataset would improve confidence in the robustness of each component's contribution.

- **Interaction between injected and inherent noise unaddressed**: ICEWS benchmarks reportedly contain ~50% inherent DNC. Injecting another 50% may produce effective corruption rates that differ qualitatively from either natural or synthetic noise distributions. The paper does not report the effective total NC rate, making it difficult to interpret results in the 50% injected DNC condition for ICEWS datasets.

### Trivial
- The three-level DNC framing (entity-attribute, entity-entity, attribute-attribute) implies three independent noise sources, but Section 2.1 shows that attribute-attribute NC is fully derived from entity-attribute and entity-entity NC (y^m_ij = 1 iff h^m_i = 1, h̃^m_j = 1, and y_ij = 1). Making this dependency explicit in the main text would avoid potential misreading of the DNC framing.

---

## Nice-to-Haves

- Reporting what fraction of greedy π* subsets (Eq. 7) recover the correct clean correspondence subset in synthetic experiments would directly validate Assumption 1 and is achievable within the paper's experimental setup.
- Presenting RULE w/o TTR as a separate row in the main comparison tables (Tables 1–2) — in addition to the ablation Table 3 — would make the contribution breakdown immediately transparent to readers and strengthen the presentation of the training-time contribution.
- A brief discussion of TTR's computational overhead and suggestions for how it might be approximated or batched for large-scale deployment would improve the paper's practical utility.

---

## Removed Points

*These points are flagged to be removed; treat them with caution.*

- **Harsh Critic Issue 1 (stated as fatal): "RULE w/o TTR does not beat the best baseline in All-attributes 50% DNC"** — FACTUALLY INCORRECT. The critic claims MEAformer achieves H@1 = 94.7 in this setting, but Table 2 shows MEAformer achieves H@1 = 91.9 for 50% DNC ICEWS-WIKI All-attributes. RULE w/o TTR achieves 94.0 (Table 3), which exceeds 91.9. The training-time RULE beats the best baseline even without TTR. This removes the "structural problem" characterization. The asymmetry remains a transparency concern (see Major) but is not fatal.

- **Harsh Critic: Detailed noise-rate characterization for Appendix B** — The paper's 50% DNC prevalence claim is supported in Appendix B. Under the Hard Rules, criticisms about missing appendix or supplementary content are removed, as the parser strips these sections.

- **Strength Finder: "first methods to enhance test-time robustness for the MMEA task"** — The paper's claim of novelty here is self-asserted and cannot be verified without external references. Retained only as the training-time contributions' novelty is well-supported; the "first" framing is left to the authors.

- **Strength Finder generic strength: "addresses an important problem"** — Removed as too generic per filtering rules. The importance is captured concretely via the empirical DNC prevalence evidence (which is retained).

---

## Novel Insights

The paper's most original contribution is the inference-time consensus estimator: using a greedy marginal-contribution strategy (Eq. 7) to estimate ground-truth correspondences when labels are unavailable at test time, then computing a proxy consensus score to weight attributes during fusion. This bridges training-time reliability learning and test-time adaptation in a way that does not require any additional supervision. The key insight — that attributes with positive marginal contribution to entity-level similarity likely correspond to correct entity-attribute associations — is a novel connection between the cooperative game theory literature (Shapley/marginal contributions) and the noisy correspondence problem in multi-modal alignment. Whether this assumption holds robustly across entities with very few attributes or all-noisy attribute sets remains an open empirical question worth future investigation.

---

## Suggestions

1. Add a "w/o TTR" row to Tables 1–2 alongside baselines to make the contribution split between training-time learning and VLM-augmented inference transparent to readers without requiring them to cross-reference Table 3.
2. Report per-query and total TTR inference time (e.g., GPU-hours on ICEWS-WIKI) to help readers assess the practical overhead of the 72B MLLM component.
3. In the synthetic noise experiments (where clean subsets are known), measure the precision/recall of the greedy π* selection (Eq. 7) against the true clean attribute subset. This would directly validate Assumption 1 and convert it from an assumption to an empirically supported claim.
4. Report effective combined NC rates (inherent + injected) when testing on ICEWS benchmarks to clarify the experimental conditions.

---

## Score and Decision

**Originality**: The DNC problem formulation and the two-fold reliability principle (uncertainty + consensus) are novel in the MMEA literature. The inference-time consensus estimator is a creative solution. **4/5**

**Importance**: Noisy correspondences are prevalent in real MMKGs, and existing methods assume clean correspondence. Addressing this gap has clear practical relevance. **4/5**

**Claims supported**: The main claim — that RULE is robust against dual-level NC — is well-supported by Tables 1–2 and by the ablation in Table 3 which confirms that training-time RULE alone (w/o TTR) beats all baselines. Minor gaps around Assumption 1 and limited ablation breadth. **4/5**

**Soundness**: The Dempster-Shafer uncertainty formulation and DRL loss design are technically principled. The DRF coupling is coherent. The 72B MLLM asymmetry is a transparency issue; the underlying methodology is sound. **4/5**

**Clarity**: Well-structured, with clear problem formulation, method description, and ablation. The main transparency gap (TTR not separated in main tables) mildly detracts. **4/5**

**Community value**: Strong: provides both a problem formulation and a solution framework with open experimental settings that others can build on. **4/5**

The paper makes a genuine and well-supported contribution: it identifies a practically important problem, proposes a principled method, and validates it convincingly. The main issues (TTR transparency, runtime analysis) are addressable in revision and do not undermine the core results.

MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>

<subscores>
<originality>4</originality>
<importance>4</importance>
<claims_supported>4</claims_supported>
<soundness>4</soundness>
<clarity>4</clarity>
<community_value>4</community_value>
</subscores>