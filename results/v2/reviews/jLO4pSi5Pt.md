Now I have all the information needed. Let me synthesize the final review.

## Calibration Anchor Summary

**Round 1:**
- **RwiUmrEHgR** (3.00) — rejected; cost-sensitive loss for long-tailed classification. Topic-related but much weaker paper.
- **pdzHpQbGrn** (2.50) — rejected; active test-time prompt learning, weak evaluation.
- **WM5G2NWSYC** (2.00) — rejected; projected subnetworks, very weak.
- **yD2JMeKumt / DOTA** (6.00, Round1-mid) — rejected; TTA for VLMs with distribution estimation. Had missing-baseline issues. L-TTA is comparable or stronger on most dimensions.
- **b20VK2GnSs** (7.00, Round1-mid) — accepted; concept drift for MLLMs. Had significant clarity/experimental issues. L-TTA is slightly weaker in some aspects.
- **iEFMwP5wng** (5.50, Round1-weakness) — rejected; agreement-on-the-line for TTA. Different topic, moderate quality.
- **TPZRq4FALB** (8.00, Round1-high) — accepted; multi-modal TTA reliability. Significantly stronger paper.
- **PxL35zAxvT** (4.67, Round1-weakness) — rejected; TTA with auxiliary tasks.
- **eXrUdcxfCw** (4.80, Round1-weakness) — rejected; continual TTA prototypes.
- **6yJuDK1DsK** (4.50, Round1-weakness) — rejected; lifelong TTA.

**Round 2:**
- **k9NYnsC4Mq** (5.67) — rejected; VLM continual learning.
- **eE2PXlNydB** (6.00) — accepted; compositional zero-shot learning with prototypes. Different task, similar technical area.
- **KNtcoAM5Gy / BaFTA** (5.50) — rejected; backprop-free TTA for VLMs. Had insufficient ablation. L-TTA is clearly stronger.
- **lF9QXpfNHm / ROSITA** (4.67) — rejected; open-world TTA.
- **75PhjtbBdr / ML-TTA** (6.25) — accepted; multi-label TTA with BEM. A reviewer raised the same "baselines not designed for this setting" concern and it was still accepted. L-TTA has more thorough evaluation.
- **ZuYvrjh2od** (5.00) — rejected; benchmark evaluation.

**Round‑1 bracket:** [5.5, 7.0]. The paper is clearly above the 3.5−4.67 cluster (which had major methodological issues and thin evaluation). It sits near DOTA (6.00, rejected) but I assess L-TTA is stronger due to better ablations, more datasets, and clearer component design. The Multi-label TTA paper (6.25, accepted) had the same "baselines-not-adapted" concern yet was accepted, suggesting the field accepts this limitation for papers establishing a new problem variant.

**Final calibration:** Comparing against the 6.25 (accepted) and 6.00 (rejected) anchors — L-TTA is consistently more thorough than DOTA (more datasets, better component analysis, theoretical grounding, efficiency study). It is comparable to the 6.25 ML-TTA paper in rigor but evaluates across far more settings (15 datasets vs 3). The concept drift paper at 7.00 had a stronger novelty claim (new dataset + theory) but had significant presentation/confounding issues. L-TTA's main gap is the absence of LT-adapted baselines, a weakness shared by the accepted 6.25 anchor and that did not prevent its acceptance. I therefore place L-TTA at **6.5**.

---

## Summary

This paper introduces L-TTA, the first systematic study and method for Long-Tailed Test-Time Adaptation of Vision-Language Models (VLMs). The method comprises three co-designed components — Synergistic Prototypes (SyPs), Rebalancing Shortcuts (RSs), and Balanced Entropy Minimization (BEM) — that collectively enrich tail-class representations, dynamically rebalance prototypes, and correct the head-class bias of standard entropy minimization. Experiments across 15 datasets under three imbalance ratios (10, 20, 50) show consistent improvements in both accuracy and macro-F1 over 12+ existing TTA methods.

## Strengths

- **Novel problem formulation and failure-mode analysis.** The paper is the first to identify and formalize the unique challenges of LT-TTA for VLMs, specifically "Text-induced Tail Erosion" and "Modality-bias Amplification" (Sec. 1, Fig. 1b). This goes beyond a simple combination of existing TTA and long-tailed techniques and provides genuine insight into why prior methods fail under long-tailed test distributions.

- **Well-motivated, multi-component design with clear ablation evidence.** Each of the three components (SyPs, RSs, BEM) targets a specific identified failure mode. The Exclusionary Prototype update (Eq. 5) is a novel mechanism that uses prediction gaps as EMA weights to capture inter-class feature associations. The component ablation (Table 6) cleanly demonstrates that each component contributes positively and that the full system consistently outperforms any subset (e.g., SyP+RS+BEM → 71.30% vs. DP-only → 68.68% on ViT-B/16).

- **Extensive and well-designed experimental evaluation.** The paper evaluates across 15 diverse datasets (OOD variants, fine-grained domains, corrupted data), 3 imbalance ratios, 2 backbones, and 4 additional larger backbones (ViT-L, ViT-H, SigLIP, MetaCLIP). Results are reported with both accuracy and macro-F1, and 5-run averages are provided. The systematic inclusion of head/tail accuracy (deferred to appendix) and efficiency metrics (Table 4) strengthens the evaluation.

- **Theoretical grounding of the loss objective.** Propositions 1 and 2 formally characterize how standard EM widens the gradient gap between head and tail classes and how BEM reduces this gap. While the proofs are deferred to the appendix, the framing provides a principled motivation for the proposed loss modification.

- **Practically useful efficiency profile.** L-TTA (1.45h, 1.89GB on ImageNet at imb=10) is substantially more efficient than several competitive methods (RLCF: 18.3h, WATT: 27.7h) while achieving the highest harmonic mean performance (67.20 on LT-CDB). The claim of a favorable performance-efficiency trade-off is empirically supported.

## Weaknesses

### Fatal
None.

### Major

1. **Missing comparison against LT-adapted versions of standard baselines.** The paper compares L-TTA against 12+ TTA methods in their original (balanced-set) form under long-tailed test distributions. While this establishes that *existing unmodified* methods degrade under LT, it does not address a natural question: would a simple LT-aware modification of a baseline (e.g., TPT with logit adjustment, TDA with class-weighted entropy minimization) close the gap? The paper argues theoretically (Sec. 3.2) that logit adjustment may fail under EM's dynamics, but this argument is not validated experimentally. Since the paper frames its contribution as providing the *first* solution to LT-TTA and presents its specific components as essential (via ablation), the evaluation would be substantially stronger with at least 2–3 LT-adapted baselines. This is the single most significant gap in an otherwise thorough experimental study. (Not a fatal flaw — the paper's core claims about outperforming existing methods are supported — but a clear limitation that weakens the comparative narrative.)

### Minor

2. **No limitations section.** The paper lacks an explicit discussion of limitations. Several are worth acknowledging: EMA-based prototypes depend on stream order and batch size; the RS module's architectural choices (number of hyper-class vectors, cross-attention design) introduce unexplored scaling properties; and the synthetic long-tailed construction from datasets with small original class sizes may produce shallow tails in some cases.

3. **Unclear connection between the text-bias motivation and visual prototype solution.** The paper identifies "Text-induced Tail Erosion" as a failure mode (text embeddings carry pre-training biases) but proposes visual prototypes (SyPs) as the corrective mechanism. The paper does not explicitly analyze *which* of the two terms in the final logit (text similarity vs. prototype affinity) is responsible for counteracting the text-specific component of erosion. An ablation that compares text-only, prototype-only, and combined predictions on classes where CLIP is known to have strong text bias would clarify the mechanism.

4. **Missing ablation of the entropy threshold θ for DP updates.** The DP update (Eq. 4) uses a threshold θ that is itself updated via EMA, but there is no analysis of sensitivity to the initial θ value or the momentum of its update.

5. **Synthetic benchmark construction could be better characterized.** The paper notes that for datasets with small original class sizes, "if the calculated cardinality is less than the class cardinality itself, we simply keep that class unchanged" — meaning some datasets may have fewer classes actually shrunk than intended. Reporting the actual number of classes modified per dataset would help readers assess the difficulty of the constructed task.

### Trivial
None beyond what was filtered to Removed Points.

## Nice-to-Haves
- An experiment that degrades the text encoder (e.g., by adding noise to text embeddings) to directly test whether the visual prototypes compensate for text bias.
- Ablation of the initial θ value and EMA momentum for the DP update threshold.
- Reporting the number of classes actually modified when constructing the long-tailed versions of fine-grained datasets.

## Removed Points
- **"Invalid baseline comparisons (structural)" at the "fatal" level**: Demoted from structural/fatal to a Major weakness (point #1 above). The critic's framing that "L-TTA's specific components are *necessary*" overstates the paper's actual claim. The paper claims L-TTA *outperforms existing methods*, not that its designs are provably necessary. The missing LT-adapted baselines is a real gap but not a structural flaw invalidating all comparisons. However, the concern is valid and significant enough to remain as a Major weakness.
- **"Method classification and Rebalancing Shortcuts complexity (structural)"**: Moved here. The paper honestly describes RS as "cross-attention with shared hyper-class vectors" (Eq. 6). Calling them "shortcuts" is a mild framing preference, not a factual error. The structural complexity is fully disclosed.
- **"Coherence between motivation and mechanism (evidential)"**: The paper explains that SyPs "accumulate multi-modal semantics beyond text embeddings" to mitigate text bias. This is conceptually clear even if not separately analyzed. Demoted to Minor (point #3 above) rather than being a separate Major weakness.
- **"Efficiency claim contradicted by data"**: Removed. The paper claims L-TTA "keeps the trade-off between performance and efficiency," which is supported by the data: L-TTA achieves HM 67.20 vs. TDA 64.51 and DPE 66.31, at 1.45h/1.89G vs. TDA 0.91h/0.89G and DPE 1.38h/1.81G. Slightly higher cost for meaningfully better performance *is* a trade-off, not a contradiction.
- **"\\ and - entries without explanation"**: Removed. Table 4's caption explicitly states: "\\ means the model fails to provide valid outputs. - means the model did not finish within time budget." The explanation is present.
- **"Missing appendix/proofs"**: Removed. These exist in the original submission; the parser strips appendix content.
- **Strength Finder's generic strengths about "problem importance," "novel method," "well-written"**: Removed per filtering rules. Only specific, evidence-anchored strengths are retained.

## Novel Insights
The paper's identification of "Text-induced Tail Erosion" (certain classes, termed "rich classes," maintain high accuracy irrespective of head/tail status due to pre-training biases in text embeddings) provides a genuinely new lens on why long-tailed distributions are particularly challenging for VLMs — the text modality introduces an independent source of bias beyond the standard label-frequency imbalance. The Exclusionary Prototype design (Eq. 5), which uses the gap between the top prediction and each class prediction as an EMA weight to store improbable features for *all* classes, is a clever departure from prior prototype-caching approaches (like TDA's negative cache) that only store features for the predicted class.

## Suggestions

1. **(Critical for revision)** Add at least 2–3 LT-adapted baselines: (a) TPT with logit adjustment ($\log \pi$ added to logits before softmax in the entropy step), (b) TDA or DPE with class-weighted entropy minimization using predicted class counts. If these fail to match L-TTA's performance, the comparative claims are substantially strengthened. If they perform comparably, the narrative should be adjusted accordingly.
2. Add a limitations section acknowledging the method's dependence on stream order, unexplored scaling of RS hyperparameters, and the synthetic nature of the LT construction.
3. Include an ablation analyzing the contribution of the text-similarity term vs. prototype-affinity term in Eq. 8, particularly for classes where CLIP exhibits strong text bias.
4. Report the number of classes actually modified by the exponential-decay sampling for each dataset to clarify task difficulty.
5. Add an ablation of the initial θ value and EMA momentum for the DP threshold update.

## Score and Decision

**Originality:** 4/5 — First to study LT-TTA for VLMs with genuinely novel failure-mode analysis.
**Importance:** 4/5 — Addresses a realistic and underexplored problem.
**Claims support:** 3/5 — Well-supported overall but weakened by missing LT-adapted baselines.
**Soundness:** 3.5/5 — Robust experiments and ablations but one significant evaluation gap.
**Writing:** 4/5 — Clear, well-structured, though missing a limitations section.
**Value to community:** 4/5 — Provides a new benchmark, baselines, and a strong method.

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>