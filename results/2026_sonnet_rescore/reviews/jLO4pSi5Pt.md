Now I have sufficient detail to write the consolidated review. Let me synthesize everything carefully.

---

## Summary

This paper proposes L-TTA (Long-tailed Test-Time Adaptation), the first TTA framework specifically designed for the long-tailed distribution setting with Vision-Language Models (VLMs). The authors identify two distinct failure modes — text-induced tail erosion and modality-bias amplification — and address them with three co-designed components: Synergistic Prototypes (Deterministic + Exclusionary), Rebalancing Shortcuts with a class re-allocation loss, and Balanced Entropy Minimization (BEM) supported by theoretical propositions. Experiments span 15 datasets across three benchmarks with multiple imbalance ratios, demonstrating consistent gains over 12 baselines in both accuracy and macro-F1.

---

## Strengths

- **Novel Exclusionary Prototype mechanism addresses tail-class feature starvation.** The EP update (Eq. 5) uses a confidence-weighted EMA that ensures every class EP is updated from every incoming sample, not just those predicted as that class. Table 6 confirms practical utility: removing EPs from the full system costs approximately 1.78% macro-F1 on ViT-B/16 and 1.07% on ResNet-50.
- **BEM has genuine theoretical grounding.** Propositions 1 and 2 formally show that standard entropy minimization systematically widens the optimization gap between head and tail classes, and that BEM narrows this gap. Figure 4d provides empirical validation: β=1 outperforms both the class-prior-dominated (β=8) and logit-only (β=0.1) regimes by ~0.85% macro-F1.
- **Rebalancing Shortcuts (RSs) contribute measurable class clustering improvements.** The class re-allocation loss (Eq. 7) is grounded in load-balancing from MoE LLMs. Ablation in Table 6 shows SyP+RS consistently outperforms SyP alone: +1.05% macro-F1 for ViT-B/16, +0.80% for ResNet-50.
- **Robustness to increasing imbalance ratio is demonstrated.** On OOD Average (Table 1), L-TTA's macro-F1 drops only 1.29% from imb=10 to imb=50, versus 4.86% for TDA and 4.72% for DPE, showing the framework handles escalating imbalance far more gracefully than prior work.
- **Efficiency advantage is concrete.** Table 4 shows L-TTA at 1.45h and 1.89GB GPU memory achieves the best harmonic mean on LT-CDB, while WATT requires 27.70h and RLCF 18.30h — a real practical advantage, not just a marginal one.

---

## Weaknesses

### Fatal
None.

### Major

- **No variance reported in any main table.** The paper states 5 runs per experiment but reports no standard deviations in Tables 1–5. Several key margin claims are below 1% (e.g., L-TTA vs. DPE at imb=50 on ImageNet-A: 60.07% vs. 60.21% in accuracy). Without uncertainty estimates, it is impossible to assess whether the claimed consistent improvements are statistically meaningful. This is especially consequential given the paper's framing of its results as systematic, state-of-the-art gains across 15 datasets.

- **Non-i.i.d. TTA baselines (SAR, DELTA, LAME, DA-TTA) are cited but absent from quantitative comparison.** The paper explicitly identifies these as related methods that address class imbalance or non-i.i.d. streams, and Figure 1b shows SAR breaking down on VLMs — but none of these appear in Tables 1–3. Readers cannot determine how much L-TTA improves over methods that at least partially address the same challenge. This gap weakens the "uniqueness of the VLM long-tailed setting" argument, since the claim rests on a single negative demonstration (SAR on Figure 1b) rather than broad comparison.

### Minor

- **The modality-bias amplification claim is supported by only one baseline.** Figure 1b shows SAR on CLIP degrades relative to SAR on a pure visual backbone. However, SAR was designed for vision-only architectures, so the degradation may reflect an architecture mismatch rather than a general VLM-specific phenomenon. Supporting this claim with two or three unimodal non-i.i.d. TTA methods would distinguish a principled failure mode from an SAR-specific artifact.

- **The pseudo-label feedback loop in BEM is unanalyzed.** Section 3.2 states that the class prior π is "continually updated based on the current predicted pseudo-labels." In a long-tailed stream, the model's pseudo-label distribution is systematically biased toward head classes early on — precisely when adaptation matters most. This means BEM's rebalancing term may initially reinforce head-class bias before the pseudo-label estimates stabilize. The paper provides no ablation or analysis comparing estimated pseudo-label prior vs. the true prior, leaving open the question of how much this feedback degrades performance in the early stream.

- **Theoretical account of the EP mechanism does not fully explain its observed effectiveness.** The update rule in Eq. 5 accumulates features from samples confidently predicted as class c* into the EPs of all other classes c ≠ c*. The claim is that these stored "exclusionary" features constitute a useful discriminative signal against future queries from class c. The ablation confirms EPs help, but the paper offers no analysis — diagnostic experiment or otherwise — showing that f(x)·u_c is actually higher for non-class-c queries than for class-c queries, which is the core assumption behind the subtraction in Eq. 8. The mechanism is plausible but its theoretical description functions more as post-hoc rationalization than principled explanation.

### Trivial

- **K parameter notation is inconsistent between text and implementation.** The main text defines K as "there are K hyper-class vectors," implying an integer count, but the hyperparameter setting reports K=0.3 and Figure 4c shows K on a [0.2, 1.0] scale — suggesting K is a fraction of the total number of classes C. This discrepancy is a reproducibility concern and should be clarified.

---

## Nice-to-Haves

- Including a compact per-class head/tail accuracy breakdown in the main text (currently deferred to appendix) would make the failure-mode-to-component mapping far more convincing — particularly showing EPs specifically benefiting tail classes and BEM specifically reducing head dominance.
- Evaluating at a more extreme imbalance ratio (e.g., imb=100 or imb=200, closer to ImageNet-LT's ~256) would characterize the failure regime and strengthen generalizability claims.
- A diagnostic ablation comparing true class prior vs. pseudo-label prior in BEM would directly address the feedback loop concern and, if the difference is small, constitutes a clear positive result.

---

## Removed Points

*These points are flagged to be removed; treat them with caution.*

- **Harsh Critic — Proposition 2 cannot be verified because proof is in appendix.** The paper does state Proposition 2 with a clear claim (Eq. comparison of gradient gaps). The proof being in the appendix is standard practice and the appendix section is removed by the parser; this is not an author fault. Removed.

- **Harsh Critic — Table 4 WATT memory entry "1.54<×n" is a flaw.** This is a parser artifact, not an author error. The paper states the formatting is an extraction issue. Removed.

- **Harsh Critic — EP ablation costs "~3.22% macro-F1."** This number does not match what is in Table 6. The ViT-B/16 ablation shows the drop from removing EPs is approximately 1.05% (SyP+RS minus DP+RS) before BEM and ~1.78% from the full system. The 3.22% figure is inaccurate. Removed from stated evidence; the underlying concern about EP contribution is addressed via the verified ~1-1.78% figures.

- **Harsh Critic — Missing related work (DA-TTA and DELTA should be compared).** The specific comparisons to these methods are a legitimate gap (kept as Major), but the phrasing demanding specific methods as baselines borders on requesting missing related work commentary. Partially retained as the quantitative comparison gap, but the "missing related work" framing is removed.

- **Strength Finder — "First to address long-tailed TTA for VLMs" as a standalone strength.** This is a framing claim about importance rather than a concrete evidence-backed strength. The fact it is the first is relevant but is captured by other strengths and the summary. Removed as standalone.

---

## Novel Insights

The most genuinely novel architectural insight in this paper is the exclusionary prototype concept: rather than building a prototype solely from instances *of* a class, the method builds a complementary prototype from instances *strongly predicted not to be* that class. This inverts the typical clustering intuition and allows tail-class representations to be populated via head-class traffic — addressing prototype starvation without requiring tail-class samples to appear. The BEM penalty (1 - P̃)^β is a concrete, tunable mechanism that bridges the gap between logit-adjustment (which requires static prior knowledge) and raw entropy minimization (which ignores class imbalance), with a formal theoretical guarantee on gradient gap reduction. Together, these two ideas are more compositionally principled than the typical ensemble-of-existing-TTA-methods approach.

---

## Suggestions

1. **Add standard deviations to main tables or at minimum an appendix table.** Even reporting ±σ on the OOD Average and CDB Average rows would significantly bolster credibility for the borderline (<1%) margins.
2. **Clarify K notation in Section 3.2.** State explicitly whether K is an absolute count or a fraction of C, and add one sentence connecting the text definition to the reported hyperparameter K=0.3.
3. **Broaden the modality-bias amplification evidence.** Demonstrate that at least one additional unimodal TTA method (e.g., LAME or DELTA) also degrades specifically on VLMs under long-tailed conditions, turning Figure 1b's claim into a systematic finding.
4. **Analyze the pseudo-label prior feedback loop in BEM.** A brief ablation (or a bound on the convergence time for π to stabilize) would directly address the circular dependency concern.
5. **Add a diagnostic plot for EP discriminativeness.** Plotting the cosine similarity distribution between class-c EPs and class-c queries vs. non-class-c queries would validate the "exclusionary" intuition with direct evidence.

---

## Assessment on Key Axes

**Originality:** High. The problem formulation (long-tailed TTA for VLMs) is genuinely novel, and all three components contain original design elements. The EP inversion idea is particularly inventive.

**Importance of research question:** High. Long-tailed distributions are pervasive in deployment, and the gap in VLM-specific TTA is real and consequential.

**Claims support:** Moderate. Empirically broad (15 datasets, 3 imbalance ratios, 5 backbones, 5 runs), but the absence of variance estimates and the missing SAR/DELTA/LAME baselines are real credibility gaps. The "modality-bias amplification" framing is somewhat overclaimed.

**Soundness of experiments:** Moderate-high. Ablations are thorough and cover all components; robustness experiments are convincing. The statistical reporting gap is the main concern.

**Clarity of writing:** Good. The three-component design is clearly motivated and connected to identified failure modes; the K notation ambiguity is a minor exception.

**Value to the research community:** High. Establishes a new benchmark configuration, releases code, and provides a method that generalizes across 15 datasets and multiple backbone families.

---

MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>

<subscores>
<originality>4</originality>
<importance>4</importance>
<claims_supported>3</claims_supported>
<soundness>4</soundness>
<clarity>4</clarity>
<community_value>4</community_value>
</subscores>