Now I have a clear picture of the calibration landscape. Let me write the final consolidated review.

---

## Summary

This paper introduces the task of **Free-Form HOI generation** — moving beyond the grasp-centric paradigm that dominates prior work to generate diverse interactions including pushing, poking, rotating, etc. The authors contribute three tightly coupled elements: (i) **WildO2**, a dataset of 4,414 3D hand-object interaction samples (92 intents, 610 objects) reconstructed from internet videos with multi-level semantic annotations; (ii) **TOUCH**, a three-stage framework combining contact map prediction (CVAEs), multi-level conditioned diffusion with coarse-to-fine text/geometry injection, and cycle-consistency-based physical refinement; (iii) quantitative evidence that TOUCH outperforms adapted grasping baselines (ContactGen, Text2HOI) across contact accuracy, physical plausibility, diversity, and semantic consistency.

## Strengths

- **Novel and well-motivated problem formulation.** The paper convincingly identifies that existing HOI generation is locked into a grasp-centric paradigm and defines free-form HOI generation as a distinct task. This reframing is timely and opens a genuine new direction (Sec. 1, Fig. 1).

- **WildO2 dataset with practical automated pipeline.** The O2HOI frame-pairing strategy (object-only + interaction frame from the same video) cleverly bypasses the occlusion problem that plagues in-the-wild 3D reconstruction, using mask transfer rather than error-prone inpainting. The resulting dataset covers 92 intents and 610 object categories with multi-level annotations (SSC, DSC, contact maps, 17-part hand segmentation) — a resource the field currently lacks (Sec. 3).

- **Well-designed three-stage framework with strong ablations.** The architectural decomposition — separate contact prediction CVAEs → multi-level conditioned diffusion → cycle-consistency refinement — is logical and each component's contribution is validated. The ablation study (Table 2) is carefully done, including the astute observation that low penetration values can be misleading when the hand fails to contact the object (Sec. 5.3). The coarse-to-fine injection design (Eq. 4–5) where global context conditions early transformer blocks and local contact features condition later blocks is principled.

- **Consistent quantitative superiority across all metric categories.** Table 1 shows TOUCH outperforming both baselines on every reported metric: contact accuracy (P-IoU 0.776 vs. 0.620/0.711), physical plausibility (MPVPE 2.97mm vs. 5.46/4.69mm), diversity (Ent 2.93, CS 5.40), and semantic consistency (P-FID 4.13 vs. 6.08/15.72). The margins on MPVPE and P-FID are especially substantial.

- **Out-of-domain generalization on Objaverse.** The method plausibly generates interactions for CAD models never seen during training and for verbs outside the annotated intent set (Fig. 7). This goes beyond what the adapted grasping baselines can do and demonstrates genuine generalization capability.

- **Semantic force control.** The analysis showing 22–25% larger contact area for "firm" vs. "gentle" prompts (Sec. 5.4.3, Fig. 9) provides concrete evidence that the model learns nuanced semantic distinctions beyond surface-level text conditioning.

## Weaknesses

### Fatal
None.

### Major

1. **User study is too small for reliable conclusions.** The perceptual score (PS) is based on only 10 participants. For a generation task where perceptual quality and semantic faithfulness are central, 10 raters is insufficient to establish statistical significance, especially given natural variance in how users judge hand-object interactions. No inter-rater agreement is reported. The trend (8.8 vs. 6.3/7.5) is suggestive but not definitive.

2. **Force-related semantic analysis lacks error bars and significance testing.** The paper claims "a 22-25% larger average contact area for 'firm/tight' interactions" (Sec. 5.4.3), but this figure is presented as a single statistic without confidence intervals, standard deviations, or a statistical test. This is the paper's best quantitative evidence for nuanced semantic control, so the lack of uncertainty quantification is a meaningful gap.

### Minor

3. **VLM-based evaluation protocol is underspecified.** Table 1 reports a "VLM" score (7.1 vs. 4.8/6.5), but the main text does not state which VLM was used for evaluation, the prompt template, how the score is computed, or how many trials were run. While P-FID already provides a standard semantic consistency metric, the VLM score would be more interpretable with these details.

4. **Dataset bias from 55% reconstruction success rate is not analyzed.** The pipeline only succeeds for 55% of source clips (Fig. 3a, with 31% "Pore Estimation Failure" and 9% other errors). The paper does not analyze whether certain object categories, action types, or hand configurations are systematically more likely to fail. This makes it difficult to assess whether WildO2 is biased toward "easier" interactions.

5. **Baseline post-processing module is not described.** The paper augments adapted baselines with "an optimization-based post-processing module to correct hand poses" (Sec. 5.2) but provides no details about this module. Since the baselines would otherwise fail on this task, the reader cannot assess whether the post-processing is comparable across methods or whether it advantages/disadvantages any approach.

6. **Architectural specifics missing.** The number of transformer layers, attention heads, and hidden dimensions in the diffusion model are not stated. The paper reports "N_inj = 8 blocks" but not the per-block configuration.

### Trivial

7. **No failure case visualization.** The paper shows only successful generations. A figure showing typical failure modes (e.g., residual penetration the refiner could not resolve, implausible hand orientations) would aid future work.

## Nice-to-Haves

- A paired test set varying a single semantic dimension (e.g., "push bottle" vs. "lift bottle" on the same object) with quantitative comparison of the resulting contact maps would directly quantify semantic control.
- Larger user study (≥25 participants) with separate ratings for physical plausibility and semantic faithfulness, plus inter-rater agreement statistics.
- Class-wise breakdown of dataset reconstruction success rate by object category and action type to characterize potential bias.

## Removed Points

*The following points from the inputs were removed with justification:*

- **"Missing related works"** — Per instructions, unrelated works cannot be confirmed as missing without external knowledge.
- **"Independent CVAEs produce inconsistent contact maps"** — The paper explicitly acknowledges this and the refinement stage is designed to address it. Not a weakness, it's a design choice with a mitigation strategy.
- **"The baseline comparison only shows adapted grasping models is weak"** — The paper's ablation study (Table 2) already provides what the critic asks for: removal of specific components (contact maps, multi-level text, etc.) to isolate their value. The critic's desired "vanilla diffusion" baseline is effectively the ablation minus all conditioning components, which the paper partially covers.
- **"Missing appendix details"** — The parser strips appendices; per instructions, weaknesses about missing appendix content are removed.
- **"Reproducibility nitpick about hyperparameters"** — Hyperparameters (1000 epochs, Adam, 1e-4 LR, batch 128) are stated. Further granularity (optimizer details for CVAEs and refiner) is reasonable to ask but is a minor detail.
- **Weakness 3 from harsh critic about "methodological gap"** — The core criticism is that adapted grasping models are weak baselines. This is partially valid, but the paper's ablations (Table 2) serve as self-baselines. The criticism also conflates the valid concern about post-processing details (addressed as Minor issue #5) with a broader methodological gap claim.

## Novel Insights

The most interesting observation across the reviews is that the paper's strongest evidence for semantic control comes from an unexpected place: the force-expression analysis (Sec. 5.4.3), where the model learns to map "firm" vs. "gentle" language to measurably different contact geometries despite no explicit modeling of physical forces. This emergent behavior is both impressive and underexploited — it could be turned into a more rigorous evaluation paradigm by constructing paired prompts that differ only on a single semantic dimension and measuring the resulting contact-map divergence. The harsh critic's suggestion of a "paired test set" would transform this qualitative insight into a systematic benchmark.

## Suggestions

1. **Before the deadline:** Add a paragraph specifying the VLM evaluation protocol (which VLM, prompt template, scoring method). Report reconstruction failure rates by object category in the dataset section to address the bias concern.
2. **For a stronger paper:** Add a systematic paired-prompt experiment where the same object is described with two different intents (e.g., "push bottle" vs. "lift bottle") and report contact-map IoU between conditions. Add error bars to the force-contact-area analysis. Increase the user study to ≥25 participants with inter-rater agreement.
3. **For future work:** Extend to temporal dynamics (noted as a limitation). Release the dataset and code to maximize community impact — WildO2 could become a standard benchmark for free-form HOI generation.

---

## Score and Decision

**Round 1 bracketing:** Similar papers exist across the weak (2.5–3.0), middle (5.0–6.0), and strong (8.0) bands. The most relevant anchors are clustered in the 5.0–6.0 range: CLUTCH (5.00, accepted), SesaHand (5.00, accepted), SynHLMA (5.50, rejected), InfBaGel (6.00, accepted). TOUCH is clearly above the 3.0 weak band and below the 8.0 strong band, placing initial bracket at 5.0–7.0.

**Round 2 narrowing:** The narrowest relevant band is 5.5–6.5. Within this: TOUCH is stronger than CLUTCH (5.00), which omits object interaction entirely and had dataset quality concerns. TOUCH is comparable to but slightly stronger than InfBaGel (6.00), which has a similar technical scope but less thorough ablations. TOUCH is stronger than SynHLMA (5.50, rejected), which used simulation data rather than real in-the-wild data. SpatialHand (6.00, accepted) is on a different task (2D image manipulation) but similar in technical execution quality. TOUCH sits above all 5.0 anchors and is comparable to or above the 6.0 anchors, placing it at **6.5**.

**Final score rationale:** The paper makes genuine contributions (new task, new dataset with practical automated pipeline, well-designed three-stage method with strong empirical results). The weaknesses are real but addressable — none invalidate the core claims. The paper is clearly above the acceptance threshold for a venue like ICLR. The score of 6.5 reflects a solid paper with clear contributions that could be strengthened around semantic evaluation rigor and dataset bias characterization.

**Calibration anchors used across rounds:**
| Paper | Avg Score | Round | Comparison to TOUCH |
|-------|-----------|-------|---------------------|
| CLUTCH (W7YRskO47j) | 5.00 | 1/2 | Weaker — skips object interaction entirely |
| SesaHand (sKMgGQQy7g) | 5.00 | 2 | Different task (hand image gen for reconstruction) |
| SynHLMA (EzJowEZ1UJ) | 5.50 | 1/2 | Weaker — simulation-based data, evaluation less thorough |
| UniHand (upUl6hMYwy) | 5.33 | 2 | Weaker — claimed unification but evaluated only estimation |
| InfBaGel (TeyHNq4WlI) | 6.00 | 1/2 | Similar — comparable technical level, TOUCH has more thorough ablations |
| SpatialHand (VpsqfCac2B) | 6.00 | 2 | Different task (2D image manipulation), similar execution quality |
| ff3gboFkss | 3.00 | 1 | Much weaker — low-quality paper |
| JT6hR0sNXZ | 2.50 | 1 | Much weaker |
| tiQaO3f1QB | 2.67 | 1 | Much weaker |
| kI27Niy4xY | 8.00 | 1 | Stronger — oral-level paper, not comparable task |

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>