Now I have all the information I need. Let me write the final consolidated review.

## Summary

UniHM proposes a framework for generating sequential dexterous hand manipulation trajectories from open-vocabulary language instructions. The system combines a unified VQ-VAE codebook shared across five hand morphologies (Shadow, Allegro, SVH, Leap, Panda hands), a compact VLM (Qwen3-0.6B) with a progressive masking curriculum, a CLIPort-based perception module for trajectory planning, and a physics-guided dynamic refinement step. Training uses only existing human-object interaction datasets (DexYCB, OakInk) with GPT-4o-annotated language, avoiding expensive teleoperation data collection.

## Strengths

1. **First sequential (non-static) framework for language-conditioned dexterous hand manipulation.** Prior language-guided methods (SemGrasp, AffordDexGrasp, DexGYS) generate only static grasp poses. UniHM produces full manipulation sequences (grab, pick&place, pull&push, open&close), as demonstrated by the real-world task evaluation in Table 3 and the multi-step metrics (FOL, FPL measuring end-effector trajectories) in Tables 1–2. This is a genuine advance over the static-pose state of the art.

2. **Morphology-agnostic shared codebook with cross-hand distillation.** The paper introduces a VQ-VAE codebook with per-hand encoders/decoders aligned via knowledge distillation (Eq. 3), enabling direct token reuse across five robot hands via Eq. 6. This architectural novelty is well-motivated: it goes beyond single-morphology tokenizers used in MotionGPT and HOIGPT. The retargeting pipeline in Section 3.1 and Figure 2 credibly describes how MANO poses are mapped to each robot hand.

3. **Physics-guided dynamic refinement with ablation support.** The frame-wise Gauss-Newton optimization (Section 3.4) combining contact energy, generative prior, and temporal smoothness is clearly specified. Table 4 provides causal evidence that this module matters: removing it degrades MPJPE from 61.40 to 65.78 on seen DexYCB and from 63.56 to 65.39 on unseen, establishing that the refinement contributes meaningfully to the reported results.

4. **Consistent SOTA results across two datasets and multiple metrics.** UniHM outperforms all four baselines (TM2T, MDM, FlowMDM, MotionGPT) on both DexYCB and OakInk under both seen and unseen splits, across MPJPE, FOL, FPL, FID, and Diversity. The margins are substantial — e.g., on DexYCB unseen, MPJPE of 63.56 vs. the next best 77.93 (MotionGPT). The improvement is consistent across all conditions, which is stronger evidence than an isolated win.

5. **Real-world transfer without teleoperation data.** Table 3 shows that UniHM achieves 55–65% success rates on seen tasks and 35–60% on unseen tasks using a physical dexterous hand, compared to 0–30% for baselines. This validates that the simulation-trained pipeline transfers to hardware, supporting the paper's "generalization without teleoperation" claim.

## Weaknesses

### Fatal
None.

### Major

1. **Baseline adaptation and comparison protocol are underspecified.** The paper compares against TM2T, MDM, FlowMDM, and MotionGPT — models originally designed for full-body skeleton motion, not dexterous hands. Section 4.3 states only that the authors "post-process their outputs with our physics-guided refinement to ensure a fair comparison," but it never specifies:
   - How these models were adapted to produce hand-specific outputs (do they generate MANO parameters? joint angles? 3D positions?).
   - Whether the baselines were trained on the same data splits and language annotations, or whether they were applied zero-shot from pretrained checkpoints.
   - The output representation used for metric computation.

   This is consequential because MotionGPT's VQ tokenizer was trained on full-body motion (HumanML3D), and MDM/FlowMDM generate 3D joint positions with different kinematic topologies than a hand. Without this documentation, the reader cannot assess whether the comparison is controlled fairly. The paper should train these baselines on the same retargeted hand-motion data with the same train/test splits and document the adaptation procedure.

2. **No direct evaluation of the unified tokenizer's cross-morphology capabilities.** The shared codebook and cross-hand token reuse (Eq. 6) are presented as core contributions (Section 3.2), yet the paper never reports:
   - Reconstruction error (MPJPE or similar) of the tokenizer itself.
   - Codebook usage statistics (e.g., perplexity, active code percentage).
   - Cross-hand translation accuracy — e.g., encoding a pose from hand A and decoding on hand B, then measuring how well the output matches the retargeted ground truth.
   - Ablation comparing the unified codebook against training separate per-hand codebooks.

   Tables 1–2 evaluate the full pipeline; they cannot isolate whether the cross-morphology codebook works as claimed. The ablation study (Table 4) omits any tokenizer-specific variant. This gap weakens the evidence for a central architectural claim.

### Minor

3. **Diversity gap on DexYCB is notable and undiscussed.** On DexYCB seen, UniHM achieves Diversity 39.62 while GT is 125.53 and MotionGPT reaches 72.51. The ablation (Table 4) reveals that removing masked training *increases* diversity to 73.09 (surpassing MotionGPT), which strongly suggests that the progressive masking curriculum suppresses output variability. The paper acknowledges that "diversity closer to GT is better" but does not analyze why UniHM underperforms a baseline on this axis, nor discuss whether the masking-diversity trade-off is a concern for real-world deployment. A brief discussion of this trade-off would strengthen the paper.

4. **Real-world evaluation lacks detail.** Table 3 reports success rates for four task types without specifying: the number of trials per condition (are these percentages from 10, 20, or 100 trials?), the hardware used (which robot arm, which dexterous hand model, which controller/setup), the definition of success for each task type, or any measure of variance or confidence intervals. The success rates themselves (e.g., 65% for seen Grab, 60% for unseen Grab) are modest and their interpretability depends heavily on these missing details. The paper should specify the experimental protocol in the main paper or appendix.

5. **Ground-truth space for error metrics is not explicitly defined.** The paper computes MPJPE, FOL, and FPL against a "GT" row in Tables 1–2, but never states whether these are computed against original MANO hand poses or against the retargeted robot-hand poses (after Dex-Retargeting). Since the model operates in robot-hand joint space and the training data is retargeted, the natural interpretation is that metrics are computed against retargeted poses — but this should be stated explicitly.

6. **No quality assessment of GPT-4o language annotations.** Section 3.1 describes using GPT-4o to generate open-vocabulary instructions from keyframes, but provides no human evaluation, agreement measure, or even examples of generated instructions. Since the VLM is trained to condition on these annotations, their quality directly affects the trained model's language understanding. A small human evaluation or annotation examples would help.

### Trivial
None.

## Nice-to-Haves
- An ablation comparing the unified codebook against per-hand codebooks would strengthen the cross-morphology claim.
- Reporting tokenizer reconstruction error (e.g., MPJPE between original and reconstructed hand poses) would help isolate tokenizer performance from the full pipeline.
- An analysis of failure modes (e.g., which tasks/objects cause failures in the real-world experiments) would improve the paper's thoroughness.

## Removed Points

The following points from the harsh critic are removed (with justifications):

- **"Evaluation metrics are computed against unclear ground truth" treated as fatal flaw** — The paper trains on retargeted data, so the natural GT is the retargeted robot poses. This is a clarity issue (addressed as Minor #5 above), not a structural flaw that invalidates the results.
- **"CLIPort not designed for dexterous manipulation trajectories"** — The paper uses CLIPort for SE(3) *trajectory planning*, not for dexterous manipulation itself. The dexterous manipulation is handled by the VLM + unified tokenizer. This criticism misunderstands the architecture.
- **"Standard deviations suspiciously small"** — Speculative. Std values like 61.40±1.93 for MPJPE are plausible for a deterministic Gauss-Newton optimization with a learned prior; no evidence suggests misconduct.
- **"Error cascade from decoupled training"** — Speculative concern without evidence from the paper.
- **"Claims generalization without teleoperation but trains on DexYCB/OakInk"** — DexYCB and OakInk *are* human-interaction (not teleoperation) datasets. The criticism misunderstands the paper's data paradigm.
- **"Missing related works"** — Cannot verify; the parser strips references.
- **"Physics refinement is overclaimed / not novel"** — The refinement is well-specified (Eq. 11–18) and its benefit is quantified via ablation (Table 4). Whether it is "novel" is a judgment call, but the module is clearly described and empirically validated.
- **Formatting/typo nitpicks** — Parser artifacts, not author errors.
- **Missing appendix content** — The parser strips the appendix from all papers.

## Novel Insights

None beyond the paper's own contributions. The core insight — that a shared VQ-VAE codebook with per-hand encoders/decoders enables cross-morphology transfer for VLM-based dexterous manipulation — is the paper's own. The reviews surface useful documentation gaps but do not reveal fundamentally new observations about the method or problem.

## Suggestions

1. **Document baseline adaptation thoroughly.** For each baseline, specify: (a) whether it was trained from scratch or fine-tuned, (b) the output representation (MANO parameters? joint angles? 3D positions?), (c) data splits and language annotations used, (d) any architectural modifications to handle hand-only motion.

2. **Report tokenizer metrics.** Add reconstruction error (MPJPE between original and reconstructed), codebook usage (perplexity, % active codes), and cross-hand translation accuracy for each of the five robot hands. This would directly validate the cross-morphology claim.

3. **Discuss the diversity-masking trade-off.** Show how varying the masking schedule affects diversity and MPJPE, and explain whether the current schedule is Pareto-optimal or if there is a better operating point.

4. **Provide real-world experiment details.** Add the number of trials, hardware specifications, success criteria, and variance across runs for the real-world evaluation.

5. **Explicitly state the GT metric space.** Add a sentence to Section 4.2 clarifying that MPJPE, FOL, and FPL are computed against the retargeted robot-hand ground truth (or the original MANO poses, whichever is used).

## Score and Decision

**Score calibration details:**

| Anchor | Path | Avg Score | Round | Comparison |
|--------|------|-----------|-------|------------|
| Generative Simulation for Dexterous Hands | 6oDiWrtk2e.md | 3.00 | R1 | Weaker contribution; speculative pipeline without real-world validation |
| SIGHT | ff3gboFkss.md | 3.00 | R1 | Similar task but lower quality of evidence |
| Tele-Catch | WacpfqlmhI.md | 2.50 | R1 | Narrower scope (dynamic catching only); weaker |
| One-shot Robot Manipulation | cz6SbHgGEn.md | 3.00 | R1 | Different sub-area; comparable quality level |
| **SynHLMA** | EzJowEZ1UJ.md | **5.50** | R1/R2 | Most directly comparable (language-conditioned HOI sequence generation). UniHM has more architectural novelty and real-world experiments but similar documentation gaps. **Comparable.** |
| **UniHand** | upUl6hMYwy.md | **5.33** | R1/R2 | Unified hand motion model with claim-evaluation mismatch. UniHM's claims match its evidence better. **Slightly stronger.** |
| **XDex** | VJqfoHU4Op.md | **4.50** | R1 | Cross-embodiment grasping with major documentation issues. UniHM is clearly stronger. |
| **DexNDM** | 80vjyj5o7l.md | **6.00** | R1 | Dexterous in-hand rotation with strong sim-to-real. Different sub-problem but similar rigor. UniHM has more missing documentation. **Weaker.** |
| VLBiMan | he86smZzRk.md | 5.50 | R2 | Bimanual manipulation from one-shot demo. Comparable overall quality. |
| VLA Pretraining | nmW77spR1I.md | 5.50 | R2 | Larger-scale VLA for dexterous manipulation. Rejected due to clarity issues; UniHM is better presented. |
| Vision-Language-Action Pretraining | nmW77spR1I.md | 5.50 | R2 | Similar VLA+hand paradigm. UniHM has stronger component validation. |
| EgoHandICL | nwjy9BeorI.md | 6.00 | R3 | Hand reconstruction, different task. Stronger evaluation. |
| InfBaGel | TeyHNq4WlI.md | 6.00 | R3 | HOI generation with iterative refinement. Stronger evaluation documentation. |

**Round 1 bracket:** 4.0 – 7.0 (based on weak anchors at 2.5–3.0 and strong anchors at 8.0 pulling from very different domains).

**Round 2 narrowing:** The closest topical anchors (SynHLMA 5.50, UniHand 5.33, XDex 4.50) and adjacent VLA papers (VLBiMan 5.50, VLA Pretraining 5.50) cluster between 5.0 and 6.0. UniHM is comparable to or slightly above SynHLMA (accepted papers at this score tend to have stronger evaluations) but below InfBaGel (6.00) and EgoHandICL (6.00) which have more complete evaluations.

**Final score: 5.5.** The paper makes a genuine contribution (first sequential dexterous manipulation from free-form language, with a thoughtfully designed architecture and consistent empirical improvement) but has clear documentation gaps that prevent full trust in the results. These gaps are addressable and do not invalidate the core claims, so acceptance is warranted.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Accept</decision>