Now I have a clear picture. Let me synthesize my final review with the calibration comparisons.

**Round 1 Bracket**: Based on the anchors reviewed, this paper sits between AnyBimanual (3.75, rejected — poor baselines, insufficient real-world experiments) and HandsOnVLM (6.33, rejected — similar VLM+hand domain but better baselines). The most comparable anchors are Cross-Embodiment Dexterous Grasping (5.00, accepted — demonstrates cross-embodiment transfer with real quantitative results but limited real-world) and GenBot (5.50, rejected — ambitious multi-component system with insufficient quantitative validation). **Bracket: 4.0–6.0**.

**Round 2 Narrowing**: CrossDex (5.00) actually validates its core cross-embodiment claim with 80% success on seen hands. UniHM claims cross-morphology generalization but provides zero quantitative evidence. UniHM's baseline selection (human body motion models vs. dexterous manipulation systems) is a more serious methodological issue than CrossDex's baseline concerns. However, UniHM has more technical depth (VQ codebook, physics refinement, progressive masking). GenBot (5.50) was rejected for ambition exceeding validation — a pattern UniHM shares. **Final score: 4.5**.

---

## Summary
UniHM proposes a three-stage framework for generating dexterous hand manipulation sequences from open-vocabulary language instructions: (1) a Unified Hand-Dexterous Tokenizer with a shared VQ codebook mapping heterogeneous hand morphologies into a common discrete latent space via staged knowledge distillation; (2) a VLM (Qwen3-0.6B) generating manipulation token sequences conditioned on text, object point clouds, and target trajectories; and (3) a physics-guided dynamic refinement module performing frame-by-frame Gauss-Newton optimization with contact, generative, and temporal priors. Evaluations are reported on DexYCB and OakInk datasets along with real-world results.

## Strengths
- **Physics-guided dynamic refinement is well-formulated**: The three-term energy function (contact, generative prior, temporal smoothness) in Section 3.4 is technically careful — the asymmetric contact penalty (Eq. 12) is continuous and slope-matched at the boundary, and the Gauss-Newton with Levenberg-Marquardt damping (Eq. 17) is a principled fusion. The ablation in Table 4 validates this component contributes meaningfully (MPJPE degrades from 61.40 to 65.78 on seen when removed).
- **Progressive masking curriculum effectively reduces exposure bias**: Training with a schedule that gradually increases mask ratio from 0 to 1 (Eq. 10), so the model transitions from teacher forcing to autoregressive generation, is well-motivated. Table 4 shows it is the single most impactful component — removing it causes MPJPE to jump from 61.40 to 73.41 on seen DexYCB.
- **Consistent quantitative improvements across two datasets**: On both DexYCB and OakInk, across seen and unseen splits, UniHM improves on MPJPE, FOL, FPL, and FID over the compared methods (Tables 1–2). The ablation study (Table 4) cleanly isolates each component's contribution.
- **Decoupled perception-generation architecture is pragmatic**: Separating CLIPort-based perception (trajectory inference, point cloud segmentation) from the VLM-based HOI generation allows the smaller perception module to be fine-tuned independently under distribution shift — a genuine practical advantage.

## Weaknesses

### Fatal
None.

### Major
- **Baseline selection is misaligned with the task, undermining the SOTA claim**: The paper compares against TM2T, MDM, FlowMDM, and MotionGPT3 — all originally designed as human-body motion generation models, not dexterous hand manipulation systems. The paper's own Related Work (Section 2.2) discusses HOIGPT, which generates "long 3D hand-object interaction" sequences from text and is directly relevant, yet HOIGPT does not appear in any experiment. Other discussed systems (DexGraspNet, UniDexGrasp, SemGrasp, AffordDexGrasp) are also absent from comparisons. The strong quantitative margins in Tables 1–2 primarily demonstrate that human-body motion models are a poor fit for dexterous hand manipulation, which is unsurprising and does not establish state-of-the-art status against the relevant literature.
- **Cross-morphology generalization — a claimed core contribution — lacks quantitative empirical validation**: The paper lists the morphology-agnostic codebook as the second of four contributions (Section 1) and describes retargeting to five robot hands (Shadow, Allegro, SVH, Leap, Panda). However, all quantitative results (Tables 1, 2, 4) are on DexYCB and OakInk, which use the MANO hand parameterization. There is no experiment showing reconstruction quality, manipulation accuracy, or token-transfer fidelity across different robot morphologies. The cross-morphology claim is an untested architectural proposal.
- **End-to-end language-to-manipulation performance is never evaluated**: During training (Section 3.3), the VLM receives ground-truth target trajectories and ground-truth object point clouds alongside text. At inference, these are replaced by CLIPort and PointSAM predictions. The paper never reports results using predicted (rather than ground-truth) trajectories and segmentations, nor does it analyze how errors in trajectory prediction or object segmentation propagate to the final hand poses. The quantitative results in Tables 1–2 therefore measure a system with oracle trajectory/object information, not the end-to-end language-conditioned system the paper describes.

### Minor
- **Real-world evaluation lacks reporting detail**: Table 3 presents success rates without specifying trial counts per condition, which physical robot hand was used, what counted as success/failure, whether identical objects were used across methods, or how the baselines were adapted for the physical robot. The absence of these details, combined with very low baseline numbers (0–30%) for most cells, makes it difficult to assess the reliability of the real-world claims.
- **GPT-4o annotation quality is unvalidated**: The auto-annotation procedure (Section 3.1) is described in two sentences. There is no validation of annotation quality, no examples of generated instructions, and no discussion of failure modes. Errors in these automatically generated instructions become part of the training signal for the language-conditioning objective.
- **Diversity metric on DexYCB contradicts the paper's framing**: The paper states "Diversity closer to the ground truth indicates a more reasonable generation." On DexYCB seen, MotionGPT3 achieves 72.51 vs. GT 125.53, while UniHM achieves 39.62 — MotionGPT3 is substantially closer to GT diversity. This inconsistency is not acknowledged or discussed (though on OakInk, UniHM does better on this metric).

### Trivial
- The paper claims "first framework for unified dexterous hand manipulation guided by free-form language commands" (Abstract, Section 1), but HOIGPT (cited in Section 2.2) performs token-based text-to-HOI sequence generation. The primacy claim should be more precisely scoped.

## Nice-to-Haves
- Ablation comparing the VLM backbone (Qwen3-0.6B) against a task-specific transformer trained from scratch to justify the VLM architecture choice.
- Ablation of the unified codebook vs. per-hand codebooks to quantify the cross-morphology benefit.
- Analysis of sequence length effects — does performance degrade with longer manipulation sequences?
- Reporting of CLIPort's standalone trajectory prediction accuracy.

## Removed Points
These points are flagged to be removed, treat them with caution.

- **Harsh Critic: "the paper does not own up to the distributed language-conditioning"** — REMOVED. The paper explicitly describes the training/inference gap in Section 3.3: "Our training and inference pipelines differ by design. During training, we condition the model on ground-truth target trajectories... At inference, a separate CLIPort module estimates these quantities..." The paper is transparent about this architectural choice. However, the related point about missing end-to-end evaluation is retained as a major weakness.
- **Harsh Critic: "'Learning from video' framing is misleading"** — REMOVED as a separate weakness. The paper trains on DexYCB and OakInk, which contain video captures of human-object interaction. The phrasing is somewhat loose but not substantively misleading.
- **Harsh Critic: demanding VLM architecture justification ablation** — MOVED to Nice-to-Haves. The paper states it uses a small model due to data scarcity, which is a reasonable justification. Demanding ablation against every possible simpler architecture is scope overreach.
- **Strength Finder: "first framework" claim** — WEAKENED. Noted as a Trivial weakness since HOIGPT exists and does sequence-level HOI generation from text.
- **Strength Finder: "Learning from video without teleoperation" as unique** — This is not unique to UniHM; many works learn from human video. Kept as supporting context but not highlighted as a primary strength.
- **Harsh Critic: "VLM architecture is unnecessary; why not a task-specific transformer?"** — REMOVED as primarily speculative. The paper states data scarcity motivates the small VLM choice; this is a reasonable engineering decision, not a methodological flaw.

## Novel Insights
The physics-guided refinement module's use of a continuous, slope-matched asymmetric contact penalty (Eq. 12) that smoothly transitions at the object boundary is a technically clean formulation addressing optimizer discontinuity better than simpler threshold-based contact models. This specific design choice, while incremental, is genuinely well-executed and could be useful to practitioners working on contact-rich manipulation optimization.

## Suggestions
- Add HOIGPT as a baseline and compare against at least one dexterous grasp method to situate the contribution in the correct literature and make the SOTA claim meaningful.
- Report end-to-end results using predicted (not ground-truth) trajectories from CLIPort, with error decomposition showing how trajectory errors affect hand-pose quality.
- Provide quantitative cross-morphology transfer results (e.g., reconstruction error on a held-out robot hand after MANO-trained codebook transfer) to support the morphology-agnostic contribution.
- Report trial counts, hardware specs, and success criteria for the real-world evaluation.

## Calibration Anchor Comparison
| Anchor | Avg Score | Round | Comparison |
|--------|-----------|-------|------------|
| AnyBimanual (KLTqeiI7w0) | 3.75 | R1 | Weaker — poor absolute performance, weak baselines. UniHM is clearly stronger. |
| Cross-Dexterous (twIPSx9qHn) | 5.00 | R2 | Most comparable — similar cross-embodiment claims, but CrossDex actually validates its core claim quantitatively. UniHM has more technical depth but weaker validation. |
| GenBot (fZZ4ubttru) | 5.50 | R2 | Similar pattern of ambition exceeding validation. GenBot has more novelty but insufficient quantitative results; rejected at 5.50. |
| CrayonRobo (Aqfwhna1D7) | 5.20 | R2 | Different domain but similar score range. Has stronger baseline comparisons than UniHM. |
| Mani-WM (aVyJwS1fqQ) | 4.67 | R2 | Weaker — a single-component contribution with less technical depth than UniHM. |
| HandsOnVLM (AJQuTFd9es) | 6.33 | R1 | Stronger — more appropriate baselines and better validated, despite being in a similar domain. |
| HAMSTER (h7aQxzKbq6) | 6.00 | R1 | Stronger — fairer baselines, better real-world evaluation, and validated hierarchical design. |

**Round 1 bracket**: 4.0–6.0. **Round 2 narrowing**: Anchors at 4.67–5.50 confirm that UniHM sits in the lower half of this bracket. CrossDex (5.00) is the closest comparator: both have cross-embodiment claims and moderate validation issues, but CrossDex actually demonstrates its core claim quantitatively. UniHM's baseline mismatch and missing end-to-end evaluation pull it slightly below CrossDex. **Final score: 4.5**.

MY FINAL SCORE: <score>4.5</score>
MY FINAL DECISION: <decision>Reject</decision>