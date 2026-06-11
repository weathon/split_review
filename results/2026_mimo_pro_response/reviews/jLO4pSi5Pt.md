Now I have enough data for calibration. Let me finalize my assessment.

**Round 1 Bracket Analysis:**

Key anchors retrieved across all bands:
- **Strong reject (score ~1.0):** Off-topic/survey papers. Clearly not comparable.
- **Weak reject (2.0-3.5):** Active TTA prompt learning (2.50), LVLM continual learning (2.50). Our paper is much stronger.
- **Borderline reject (4.0-5.5):** BLG long-tailed VLM (4.67), Demystifying LT in LVLMs (4.40), ROSITA open-world TTA (4.67). These have relevant ideas but weaker evaluation and execution.
- **Borderline accept (5.5-7.5):** DOTA (6.00, rejected, all 6s — unclear method, questionable human feedback eval), Multi-Label TTA with BEM (6.25, accepted, only 3 datasets), RLCF TTA with CLIP Reward (6.67, accepted, incremental), DeYO Entropy is not Enough (7.00, accepted, novel observation + new metric), Adapting MLLM to Concept Drift (7.00, accepted, novel framework + new dataset but experimental concerns).
- **Strong accept (7.5-8.5):** READ Multi-modal TTA (8.00, all 8s — novel problem, new benchmarks, innovative paradigm).

**Initial bracket: 6.5 to 7.5.**

Our paper is clearly stronger than DOTA (6.00) — which has an unclear method and weaker evaluation. It's stronger than Multi-Label BEM (6.25) — only 3 datasets, less thorough. It's stronger than RLCF (6.67) — more novelty, more extensive evaluation. It's comparable to DeYO (7.00) and Concept Drift (7.00) — but with much more extensive evaluation (15 datasets vs 3-5). It's below READ (8.00) — which had all 8s, cleaner narrative, and new benchmarks.

L-TTA has stronger experimental evaluation than most anchors at 7.0, but the K parameter inconsistency and bootstrap feedback concern are real issues. I'll settle on **7.0**.

---

## Summary
This paper proposes L-TTA, the first framework for Test-Time Adaptation under long-tailed distributions for Vision-Language Models (VLMs). It introduces three co-designed components — Synergistic Prototypes (SyPs with Deterministic + Exclusionary Prototypes), Rebalancing Shortcuts (RSs with a class re-allocation loss), and Balanced Entropy Minimization (BEM) — and demonstrates consistent improvements across 15 datasets, 3 benchmark types, multiple imbalance ratios, and multiple backbones.

## Strengths
- **Novel and practically relevant problem formulation.** The paper is the first to study TTA under long-tailed distributions for VLMs, identifying two VLM-specific failure modes (Text-induced Tail Erosion and Modality-bias Amplification). Table 1 shows existing SOTA methods suffer significant macro-F1 degradation as imbalance worsens (e.g., DPE drops from 57.57 to 55.43 macro-F1 on OOD Average as imb goes from 10 to 50), while L-TTA degrades by only 1.29%.

- **Extensive, consistent empirical gains.** L-TTA achieves best results across all three imbalance ratios on the OOD Benchmark (Table 1: 61.18% macro-F1 at imb=10 vs nearest competitor DPE at 57.57%), 10 of 11 datasets on the Cross-Domain Benchmark (Table 2: 2.20% macro-F1 improvement over DPE), and the Corruption Benchmark (Table 3: 2.87% accuracy and 2.64% macro-F1 average gains). Cross-backbone results on 4 additional architectures (Table 5) further confirm generalization.

- **Principled, well-ablated component design.** Each component targets a specific failure mode. Table 6 systematically isolates DP, EP, RS, and BEM across RN50 and ViT-B/16, showing coherent incremental gains. The Exclusionary Prototype mechanism (Eq. 5) is a creative design that updates all classes at every step, distinct from TDA's negative cache.

- **Theoretical grounding.** Propositions 1 and 2 formalize why standard EM disfavors tail classes and how BEM reduces the head-tail optimization gap, with proofs deferred to the appendix. This provides a rigorous foundation beyond empirical tuning.

- **Excellent efficiency-performance trade-off.** Table 4 shows L-TTA requires only 1.45h runtime and 1.89G memory — comparable to lightweight methods like TDA (0.91h/0.89G) and DPE (1.38h/1.81G) while significantly outperforming them, as L-TTA avoids gradient propagation through the visual encoder.

## Weaknesses

### Fatal
None

### Major
- **K parameter ambiguity and inconsistency.** In Section 3.2 (line 112), K is defined as the *number* of hyper-class vectors: "assume there are K hyper-class vectors q = {q_j}_{j=1}^K." Yet the implementation (line 208) sets K = 0.3, and the ablation (line 334) varies K from 0.1 to 1 — fractional values that are nonsensical as counts, strongly implying K is a ratio relative to the number of classes C. This is never explicitly stated. Moreover, the implementation uses K = 0.3 while the ablation concludes K = 0.2 "yields the best performance," an inconsistency that undermines reproducibility. The paper needs to explicitly define K as a ratio, specify how the integer number of hyper-class vectors is computed, and reconcile the reported default with the ablation recommendation.

- **BEM's pseudo-label-based class prior bootstrap issue is unacknowledged.** Line 138 states the class prior π is "continually updated based on the current predicted pseudo-labels." Since TTA is a one-epoch streaming process, early-stage bias toward head classes propagates into the estimated class distribution, which feeds back into BEM's loss. Given that Proposition 1 explicitly establishes that standard EM amplifies head-class confidence, the pseudo-label-based prior estimation should inherit this bias. The paper never discusses this bootstrapping concern or compares against using the true (known) class distribution as the prior. This analysis would directly validate the most novel aspect of BEM.

### Minor
- **Entirely synthetic long-tailed evaluation.** All evaluations create long-tailed distributions by subsampling balanced datasets into exponential decay curves (line 206). This is standard for controlled experiments, but means all test distributions are structurally simple with the head/tail split always at the 20th percentile. At least one naturally imbalanced dataset would strengthen the claim that advantages transfer to real-world settings.

- **Modality-bias Amplification evidence is thin.** Figure 1(b.2) shows only a single method (SAR) on a single backbone to support a failure mode that motivates a major design choice.

- **No limitations discussion.** The paper does not discuss failure cases or conditions under which L-TTA might struggle (e.g., extremely small datasets, very large class counts). A limitations section would add credibility.

### Trivial
- **Head/tail accuracy breakdowns missing from main text.** For a paper specifically about long-tailed performance, the main tables only show overall accuracy and macro-F1. Including at least the OOD benchmark head/tail breakdown in the main text would directly validate that improvements come from tail classes.

## Nice-to-Haves
- Visualize which classes attend to which hyper-class vectors to verify meaningful clustering from the CRA loss.
- Compare BEM against using fixed uniform priors or known true cardinalities as an ablation condition.
- Include results on additional corruption types beyond Gaussian noise in the main text (16 other types are in Appendix J).

## Removed Points
These points are flagged to be removed, treat them with caution:
- The harsh critic's concern about EP counters incrementing for all classes regardless of appearance is not a real issue — the φ_c weighting in Eq. 5 naturally handles this by diluting contributions when a class is not predicted.
- The informal nature of Propositions 1 and 2 ("with certain measurements") is noted but acceptable given that proofs are in the appendix.
- Formatting/style concerns are parser artifacts, not paper issues.

## Novel Insights
The identification of two VLM-specific failure modes under long-tailed TTA (Text-induced Tail Erosion and Modality-bias Amplification) is genuinely novel and motivates a well-designed solution. The theoretical insight that standard EM's gradient dynamics specifically disfavor tail classes (Proposition 1), and that simple logit-adjustment-style rebalancing can backfire for EM loss unlike for cross-entropy, is a useful contribution that could inform future TTA method design beyond this specific setting.

## Suggestions
- Explicitly define K as a ratio and report the actual integer hyper-class count per dataset. Reconcile K = 0.3 (implementation) with K = 0.2 (ablation recommendation).
- Add a plot showing how the pseudo-label-derived class prior evolves over the TTA stream compared against the true distribution, to directly validate or address the bootstrap concern.
- Include head/tail accuracy breakdowns in the main text for at least the OOD benchmark.
- Add a brief limitations paragraph to the conclusion.

## Calibration Anchors

| Anchor | Path | Avg Score | Round | Comparison |
|--------|------|-----------|-------|------------|
| DOTA: Distributional TTA of VLMs | yD2JMeKumt | 6.00 | 1 | TTA for VLMs with unclear method and questionable human feedback eval; L-TTA is more thorough with clearer method |
| Multi-Label TTA with BEM | 75PhjtbBdr | 6.25 | 1 | TTA with entropy minimization, only 3 datasets; L-TTA has far more extensive evaluation |
| RLCF: TTA with CLIP Reward | kIP0duasBb | 6.67 | 1 | TTA for VLMs, incremental contribution; L-TTA has broader novelty and evaluation |
| DeYO: Entropy is not Enough for TTA | 9w3iw8wDuE | 7.00 | 1 | Novel TTA observation + new confidence metric, comparable depth; L-TTA has more datasets but slightly more presentation issues |
| Adapting MLLM to Concept Drift | b20VK2GnSs | 7.00 | 1 | Novel framework for long-tailed VLM with experimental concerns; L-TTA has stronger evaluation rigor |
| READ: Multi-modal TTA against Reliability Bias | TPZRq4FALB | 8.00 | 1 | All 8s, novel problem + new benchmarks + innovative paradigm; L-TTA has more datasets but more issues to address |

**Round 1 bracket: 6.5–7.5.** The paper clearly exceeds the 6.0–6.5 range (DOTA, Multi-Label BEM, RLCF) due to more extensive evaluation and stronger novelty. It sits alongside DeYO and Concept Drift at 7.0, with stronger evaluation but slightly more addressable issues. It falls below READ (8.0) due to the K parameter inconsistency and unaddressed bootstrap concern. Final score: **7.0**.

MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>