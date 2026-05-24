Now I have a good calibration. Let me write the consolidated review.

## Summary

The paper proposes SigMap, a multimodal foundation model for wireless localization that combines (1) a cycle-adaptive masking strategy for self-supervised pre-training on CSI data, designed to disrupt periodic shortcuts, and (2) a "map-as-prompt" framework that encodes 3D geographic information via GNNs into lightweight soft prompts for cross-scenario fine-tuning. Experiments on DeepMIMO and WAIR-D ray-tracing datasets show consistent accuracy improvements over baselines in single-BS and multi-BS tasks, with strong parameter efficiency during adaptation.

## Strengths

- **Cycle-adaptive masking yields measurable accuracy gains over fixed masking alternatives (Table 3).** Adaptive masking achieves 0.673 m MAE and 84.5% CDF@1m in multi-BS localization, outperforming grid-only (0.770 m, 80.3%) and strip-only (0.753 m, 75.3%). This controlled ablation directly supports the claim that dynamically disrupting periodic CSI shortcuts improves learned representations.

- **Geographic prompt tuning substantially reduces localization error (Tables 2, 4).** Table 4 shows 3‑D mesh prompts achieve 1.564 m MAE vs. 2.275 m without map (31% reduction) in single-BS. Table 2 shows multi-BS MAE improves from 0.789 m (w/o map) to 0.673 m (w/ map). These results validate the "map-as-prompt" mechanism.

- **Consistent SOTA performance across both single-BS and multi-BS tasks (Tables 1, 2).** SigMap with map surpasses all compared baselines (LWLM, SWiT, CNN, OMP) by large margins — e.g., 34% lower MAE than the best baseline in single-BS (1.564 vs. 2.382 m) and 19% lower in multi-BS (0.673 vs. 0.828 m).

- **Parameter efficiency during fine-tuning is demonstrated (Table 5).** Fine-tuning updates only 0.085 M parameters (0.7% of total) and completes 1000 epochs in 30 minutes. This practical efficiency supports the claim of parameter-efficient cross-scenario adaptation.

## Weaknesses

### Fatal
None.

### Major

- **Claim misalignment: "zero-shot" in the abstract vs. few-shot in the experiments.** The abstract and Section 1.2 claim "strong zero-shot generalization in unseen environments." However, Section 4.5 explicitly describes a protocol where "only the downstream task heads are fine-tuned using limited target samples (approximately 100 instances per scenario)" — this is few-shot fine-tuning, not zero-shot. The paper itself calls this a "few-shot learning setup" (Section 4.5). Using "zero-shot" in the headline claims misrepresents what is actually evaluated and creates a structural disconnect between the paper's central claim and its evidence. This needs to be corrected before the paper can be properly judged.

- **The cycle-adaptive masking algorithm is underspecified, compromising reproducibility.** Equation (6) defines a mask pattern using `d_final`, `j0`, and `w`, but the paper never specifies how `d_final` (the "detected periodicity shift") is computed from the CSI. Section 3.3 mentions "computing shift patterns using cross-correlation analysis," yet neither the cross-correlation operation, the thresholding scheme, nor the mapping from its output to `d_final` is formalized. The ablation (Table 3) additionally omits obvious baselines such as random masking or frequency-band masking that are standard in SSL literature. Without a complete algorithmic description and broader ablations, the novelty and effectiveness of the adaptive masking mechanism cannot be fully assessed.

- **No measures of variance are reported for any result.** The paper states "All results are averaged over 5 independent runs" (Section 4.1) but reports no standard deviations, confidence intervals, or any indicator of variance across those runs. Given that claimed improvements (e.g., 0.673 vs. 0.789 MAE in Table 2, or 1.692 vs. 1.564 in Table 4) are on the order of 8–15%, and given the inherent stochasticity in SSL pre-training and fine-tuning, the reader cannot assess whether these differences are statistically meaningful. This gap weakens every quantitative claim.

- **Baseline training protocol in generalization experiments (Section 4.5) is not described.** The paper states that for SigMap, only the task head is fine-tuned on ~100 target samples while the backbone is frozen. It then compares against LWLM and SigMap w/o map. But the paper never specifies whether LWLM was also pre-trained on source data and fine-tuned on the same 100 samples, or trained from scratch on 100 samples. If the latter, the comparison is unfair and the claimed "53.2% improvement" is uninterpretable.

- **The "NLoS-aware attention mechanism" (Equation 11) is introduced only in the experiments section (Section 4.2) without prior motivation or description in the methodology (Section 3).** The paper states "The key advantage stems from our NLoS-aware attention mechanism" but provides no derivation or connection to the rest of the architecture in the main methodology. This makes it appear as an afterthought and obscures whether it is part of the core contribution or a minor experimental detail.

### Minor

- **Evaluation is limited entirely to simulated data (DeepMIMO, WAIR-D).** While simulation is a legitimate first step and standard in this area, the paper frames the work as solving a practical problem for real 5G/6G systems. No real-world measurements, discussion of measurement noise, hardware impairments, or temporal dynamics are considered. The paper should explicitly acknowledge this limitation and calibrate its significance claims accordingly.

- **Cycle-adaptive masking yields worse RMSE than strip masking (Table 3): 1.099 vs. 0.972.** The paper calls this the "best trade-off" without explaining why worse RMSE is acceptable for localization, where RMSE is the standard error metric. This deserves explicit discussion.

- **The map modality ablation (Table 4) shows 2-D birdview degrades MAE by 8% relative to 3-D mesh, but without error bars it is unclear whether this gap is significant.** The speculation about "replacing the 2-D polygon with a street-level photograph" (Section 4.4) is unsupported and presented without evidence.

### Trivial
- The "cross-correlation" terminology in Section 3.3 likely refers to autocorrelation when analyzing periodicity within a single CSI sample; this should be clarified.

## Nice-to-Haves
- Provide visualizations of learned mask patterns or reconstruction examples to build intuition for what the cycle-adaptive masking actually learns.
- Report computational cost (GNN inference time/memory) for the prompt generation step across different map sizes.
- Ablate the number of GCN layers (currently 2), the number of prompt tokens (currently 1), and the impact of positional encoding for the prompt token.

## Removed Points

*These points are flagged to be removed; treat them with caution.*

- **Criticism that the 2-layer GCN may limit receptive field.** This is speculative; the paper does not claim to handle large-scale scenes and provides no evidence that 2 layers are insufficient. No concrete failure is identified. → **Removed as speculative.**

- **Criticism about positional encoding for the prompt token.** The paper states positional encoding is added to the full sequence including the prompt token (Section 3.4). The reviewer's question is reasonable but amounts to a curiosity rather than a demonstrated weakness. → **Removed as not a concrete weakness.**

- **Criticism that global mean pooling loses spatial information.** This is an architectural design choice; pooling the graph representation into a single prompt vector is intentional. → **Removed as not a weakness; it is a design decision.**

- **Criticism about missing related work on general prompt-tuning methods.** As per instructions, I cannot mention missing related works. → **Removed.**

- **Strength claiming "zero-shot generalization."** The strength is reworded in the main review to reflect the actual few-shot setup. → **Removed and replaced with corrected language.**

- **Generic/superficial strengths** (e.g., "the paper addresses an important problem," "this paper is well-written") from the Strength Finder. → **Removed as generic.**

## Novel Insights

The harsh review's most valuable observation is the structural misalignment between the abstract's "zero-shot" framing and the paper's actual few-shot evaluation protocol — this is not a minor phrasing issue but a systemic overclaim that runs through the title claim ("cross-scenario" used interchangeably with "zero-shot") and conclusion. A second genuinely useful synthesis is that the paper claims three distinct contributions (cycle-adaptive masking, map-as-prompt, parameter-efficient generalization) but the evaluative support is uneven: the map prompt and parameter efficiency are well-supported by controlled ablations, while the adaptive masking contribution rests on an underspecified algorithm and a narrow set of masking baselines. The paper would benefit from a structural separation of these contributions so that a reviewer can assess each on its own merits.

None beyond the paper's own contributions.

## Suggestions

1. **Correct the "zero-shot" language throughout.** Replace "zero-shot generalization" with "few-shot generalization" or "cross-scenario generalization with limited fine-tuning." If true zero-shot results exist (backbone frozen, no target labels), report them separately.
2. **Fully specify the cycle-adaptive masking algorithm** — provide the cross-correlation computation, the threshold used to determine `d_final`, and the mask width `w`. Add random masking and frequency-masking baselines to Table 3.
3. **Report standard deviations** for all main tables (Tables 1–4 and the generalization table).
4. **Clarify how LWLM was trained in the generalization experiments** (Section 4.5). State whether it was trained from scratch on 100 samples or pre-trained and fine-tuned on 100 samples.
5. **Move the NLoS-aware attention mechanism (Equation 11) into Section 3** with proper motivation and connection to the architecture.
6. **Add a limitations section** acknowledging simulation-only validation and the need for real-world evaluation.

## Score and Decision

**Calibration procedure:**

**Round 1 — Bracketing:** Three parallel queries on "wireless localization foundation model self-supervised learning" with score filters (< 3.5, 3.5–7.5, > 7.5). Low-band anchors (avg 3.0–3.33): ECG foundation model, wearable sensing foundation model, remote sensing robustness benchmark. Mid-band anchors (avg 5.25–7.0): Wi-GATr wireless simulation (7.0), RelCon motion foundation model (6.75), MeshMask (6.33), FECCT (6.25). High-band anchors (avg 8.0): long-sequence model fairness, cross-entropy theory. **Initial bracket: [4, 6.5]** — the paper is clearly above weak anchors (3.0–3.33) and clearly below strong anchors (7.0+).

**Round 2 — Narrowing:** Two queries targeting the 3.5–6.5 range. Retrieved Presto (4.75), MeshMask (6.33), FECCT (6.25), and self-supervised object detection (5.25). Read Presto (4.75, Reject) and MeshMask (6.33, Accept) in full. **Narrowed bracket: [4.75, 6.33].**

**Anchor comparisons:**
- *Presto (4.75, Reject)*: Applied MAE to remote sensing; concerns about limited novelty, weak baselines, small performance gains. SigMap has stronger differentiation (novel adaptive masking, map prompts) and larger performance gains, but has more critical issues (claim misalignment, no error bars, underspecified algorithm). **SigMap is comparable or slightly stronger.**
- *MeshMask (6.33, Accept)*: Masked pre-training for CFD; clear methodology, extensive experiments on 7 datasets. SigMap has similar masked-modeling-plus-domain-knowledge concept but weaker evaluation rigor (no error bars, simulation-only, unclear baselines). **SigMap is clearly weaker.**
- *FECCT (6.25, Accept)*: Foundation model for error correction codes; mixed reviews, accepted despite limited code-length validation. SigMap has similar foundational-model ambitions but more evaluation gaps. **SigMap is weaker.**

**Final score: 5.0** — Positioned below MeshMask (6.33) and FECCT (6.25) due to the zero-shot claim misalignment, missing error bars, and algorithmic underspecification, but above Presto (4.75) because the contributions are more substantive and the performance gains are larger.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>