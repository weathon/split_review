Now I have a comprehensive calibration set. Let me write the consolidated review.

## Summary

The paper proposes TbLTA, the first framework for dense long-term action anticipation (LTA) trained exclusively from video transcripts (ordered lists of action labels with no temporal boundaries). It combines a weakly-supervised temporal alignment module (ATBA) to generate pseudo-labels from transcripts, which supervise both a segmentation head and an anticipation decoder. Cross-modal attention with localized masking enriches video features using transcript embeddings, and CTC and CRF losses provide additional sequence-level constraints. Results are reported on Breakfast, 50Salads, and EGTEA.

## Strengths

1. **First transcript-only weakly-supervised LTA framework.** TbLTA establishes a new benchmark in the LTA literature, demonstrating that dense long-term anticipation is feasible without frame-level annotations. This is a genuinely novel problem framing. The deterministic model outperforms all supervised methods on Breakfast at 30% observation (40.28 MoC vs. best supervised ActFusion at 35.79) and achieves a higher average MoC on Breakfast than any supervised method (29.03 vs. 28.45). (Table 1)

2. **Cross-modal attention with local grounding is a well-designed mechanism.** The binary mask from pseudo-labels (Eq. 1-2) restricts each transcript embedding to its temporal neighborhood, followed by a gated residual update. This design is cleanly motivated and the ablation shows a consistent hierarchy: w/o-cross-att < cross-att-simplex < TbLTA, with the full model outperforming w/o-cross-att by ≈5.7 points on Breakfast average. (Table 4)

3. **CRF and CTC components are demonstrated to contribute at long horizons.** Removing the CRF causes large drops at 50% anticipation (e.g., Breakfast Obs 30%: 38.3 → 22.9). CTC removal degrades average accuracy by ≈0.8 on Breakfast and ≈0.6 on 50Salads. These ablations support the architectural design choices. (Table 4, Section 4.3)

4. **Transcript supervision benefits rare-action classes on EGTEA.** TbLTA achieves 60.11 mAP on rare classes vs. 59.70 (Timeception) and 55.10 (Anticipatr), despite underperforming on overall mAP. This suggests transcript-level supervision can mitigate data imbalance — a useful finding. (Table 2)

## Weaknesses

### Major

1. **Ablation study uses the stochastic Top-1 metric rather than the deterministic prediction.** The paper states "All ablations are conducted on both Breakfast and 50Salads, and we report results using the Top-1 MoC metric." The Top-1 metric takes the maximum over multiple stochastic samples, which conflates model quality with sampling luck. For example, removing the CRF on Breakfast at Obs 20%/10% *increases* accuracy from 37.2 to 39.7 under this metric — the paper acknowledges this ("slightly higher on BF") but the overall average arguments still rely on a metric that can be inflated by a single lucky draw. Using the deterministic prediction (reported in Table 1) or the mean over stochastic samples would be more appropriate for component-level attribution. The main comparative results (Table 1) use the appropriate deterministic metric and are not affected, but the ablation evidence is weakened.

2. **The claim of being "competitive with, and occasionally superior to, fully supervised approaches" is unevenly supported across datasets.** On Breakfast this claim holds (deterministic TbLTA avg 29.03 vs. best supervised 28.45). On 50Salads, the deterministic model (avg 20.92) substantially lags the best supervised method (ActFusion, avg 28.39). On EGTEA, the gap is 11+ points on overall mAP (65.37 vs. 76.80). The paper acknowledges the 50Salads limitations but the overall framing overstates the generality of the competitiveness claim. A more differentiated narrative—acknowledging that Breakfast's strong procedural regularity is where the approach works best—would better match the evidence.

### Minor

3. **The CTC loss formulation and its claimed role in constraining future predictions is mechanically unclear.** The paper defines the CTC path π over the observed segment (up to αT frames), yet states "the anticipated segment is constrained to follow the correct symbolic sequence." How a loss on only observed-frame predictions enforces anything about unobserved future frames is not explained. Through parameter sharing the constraint may propagate indirectly, but the text as written suggests a direct mechanism that is not present. This needs clarification.

4. **No ablation that isolates the ATBA alignment module's contribution.** The ablations test removal of CTC, cross-attention, CRF, and duration loss, but there is no baseline that strips down to just ATBA pseudo-labels feeding a minimal decoder. Such a baseline would disentangle whether the reported gains come from the alignment quality or the subsequent architectural components. Without it, the value added by the proposed architecture beyond the borrowed alignment method cannot be cleanly assessed.

5. **Duration prediction is only evaluated indirectly.** The duration loss is claimed to help, but there are no direct metrics on duration prediction quality (e.g., mean absolute error in predicted durations). The paper acknowledges this indirectly ("a major challenge that remains is to correctly estimate future durations") but no quantitative analysis is provided.

### Trivial

6. No error bars or confidence intervals are reported on any results, including the main comparative table. While single-run evaluation is common in this subfield, the stochastic variant's sensitivity to sampling makes uncertainty quantification more relevant here.

## Nice-to-Haves

- Report the ablation using deterministic or mean-over-samples MoC rather than (or in addition to) stochastic Top-1.
- Include a minimal baseline: ATBA pseudo-labels + a simple frame-classification decoder, to factor out alignment quality from architectural contributions.
- Provide TAS metrics (frame accuracy, edit score, segmental F1) on the observed segment to validate pseudo-label quality directly, complementing the referenced Table 3 (IAS).

## Removed Points

These points are flagged to be removed; treat them with caution.

- **Harsh Critic Point 1 (no TAS evaluation of pseudo-labels):** The paper references Table 3 (IAS) in Section 4.3, which appears to report segmentation metrics. This table was stripped by the PDF parser. Per the review guidelines, missing content due to parser artifacts should not be treated as a paper weakness. If Table 3 does not contain standard TAS metrics (frame accuracy, edit score, segmental F1), this concern could be re-raised, but the current evidence suggests the paper does include some segmentation evaluation.

- **Harsh Critic Point about missing related work and formatting/style nitpicks:** Removed per guidelines (no external verification, parser artifacts).

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. Re-run the ablation study using the deterministic prediction or the mean over stochastic samples rather than the Top-1 maximum. This would provide a cleaner attribution of each component's contribution.
2. Add a baseline: ATBA pseudo-labels + a simple frame-level classifier (without the proposed cross-attention, CRF, or specialized decoder) to isolate the alignment module's contribution from the architectural innovations.
3. Provide direct duration prediction metrics (e.g., per-class mean duration error) to substantiate the value of the duration loss.
4. Tone down the "competitive" framing for 50Salads and EGTEA; the paper's contribution is already significant as the first transcript-only LTA approach, and the Breakfast results alone justify the claim.

## Score and Decision

**Calibration protocol summary:**

**Round 1 bracket:** 4.0–6.0. Based on topic-anchored queries: the LTA mid-band papers (AntGPT 6.25, VSNLS 6.00) are stronger papers with cleaner evaluation; the rejected mid-band papers (Actions-to-Action 4.40, Weakly Supervised Skill Understanding 4.75) share evaluation rigor gaps. Weakness-anchored queries: papers with pseudo-label quality concerns scored 3.5–4.25; papers with ablation metric concerns scored 5.33. The paper under review has a stronger contribution than the low-band anchors but shares some evaluation weaknesses with the mid-band rejections.

**Round 2 narrowing:** Inside the 4.0–6.5 bracket, the paper sits between the rejected mid-band papers (~4.4–4.75) and the accepted weakly-supervised paper VSNLS (6.00). TbLTA has a clearer problem-scope contribution than the mid-band rejections but lacks the evaluation thoroughness of VSNLS.

**What the low-band anchors and weakness-anchored hits failed at:** They had insufficiently validated pseudo-labels, overclaimed results relative to evidence, or used evaluation methodologies that conflated measurement noise with model quality. The paper under review shares the ablation-metric concern (weakness-anchored hits at 5.33) and the partial overclaiming (low-band rejections). These shared failure modes prevent the score from rising above the mid-range.

**Anchor list:**
- `2HdZPEQUig` (3.00, R1-topic-low) — Weak object-centric video paper; not comparable.
- `MSxCBXD5C8` (3.00, R1-topic-low) — Anomaly recognition; not comparable.
- `Bb21JPnhhr` (6.25, R1-topic-mid, R2) — AntGPT, fully-supervised LTA with LLMs. Clear accept. Stronger than TbLTA.
- `f3CdjpPkSq` (6.50, R1-topic-mid) — Action Sequence Augmentation, fully-supervised. Stronger than TbLTA.
- `dl34rOnbqJ` (4.40, R1-topic-mid, R2-weakness) — Actions-to-Action, rejected. Shared incremental-contribution concerns. Comparable or slightly weaker than TbLTA.
- `GQgPj1H4pO` (6.00, R1-topic-mid, R2) — VSNLS, weakly-supervised VidSGG. Accepted. Cleaner evaluation than TbLTA.
- `HCoSsULNxG` (4.75, R2) — Weakly Supervised Skill Understanding, rejected. Shared evaluation-rigor gaps. Comparable to TbLTA.
- `Uj2Wjv0pMY` (4.33, R2) — Procedural error detection; not directly comparable.
- `HEXtydywnE` (6.00, R2) — LASER, neuro-symbolic scene graphs. Not comparable.
- `DE2RMJVjgI` (4.25, R1-weakness) — Pseudo-label paper, rejected. Shared pseudo-label validation concerns.
- `PageLgQlXz` (4.00, R1-weakness) — Pseudo-label refinement paper, rejected. Not directly comparable.
- `o8SPZJaJyj` (4.00, R1-weakness) — Domain adaptation for TAD, rejected. Not comparable.
- `JDd46WodYf` (5.67, R2) — Active Procedure Planning, rejected. Comparable methodology gaps.
- `RflvsSxM0u` (4.50, R2) — Trajectory prediction, not comparable.
- `jLnygpRFYm` (6.00, R2-weakness) — Stochastic locations in MIM, not comparable.
- `YfZMfrpEnl` (5.33, R2-weakness) — Stochastic ViT, not comparable.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>