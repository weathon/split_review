## Summary

UniHM proposes a framework for generating sequential dexterous hand manipulation trajectories conditioned on open-vocabulary language instructions and RGB-D images. It combines (1) a VQ-VAE tokenizer with a shared codebook across five hand morphologies, (2) a Qwen3-0.6B VLM fine-tuned with a progressive masking curriculum to generate token sequences, and (3) a physics-guided post-refinement optimizer for feasibility. Training uses only existing HOI datasets without teleoperation data, and evaluation spans DexYCB, OakInk, and real-world robot trials.

## Strengths

- **Cross-morphology unified codebook via knowledge distillation.** The staged training approach (Section 3.2) where new hand encoders are aligned to a reference encoder via Eq. 3 before full VQ-VAE training is a practical solution to the non-differentiable VQ bottleneck. This enables a single codebook to serve five distinct hand morphologies, and the pose translation mechanism in Eq. 6 is clean.

- **Learning from human HOI video without teleoperation data.** The paper demonstrates that a model trained solely on DexYCB and OakInk (human-object interaction datasets) can produce real-world executable trajectories on robot hardware (Table 3), without expensive teleoperation data collection. This is a practically significant result.

- **Asymmetric contact penalty in physics refinement is principled.** Eq. 12 uses a smooth function that is quadratic for penetration (d≥0) and exponential for separation (d<0), which properly penalizes interpenetration while softly encouraging contact. The ablation in Table 4 confirms removing physical refinement degrades MPJPE from 61.40→65.78 on seen DexYCB.

- **Decoupled perception-vs-generation architecture.** By separating scene perception (CLIPort) from HOI generation (VLM), the system can adapt to distribution shifts by fine-tuning only the smaller CLIPort module while keeping the VLM fixed (Section 3.3, Inference Stage). This is a practical design choice for real-world deployment.

## Weaknesses

### Fatal
None.

### Major

- **Missing comparison against the most relevant baseline: HOIGPT.** The paper's Related Work (Section 2.2) cites HOIGPT as a method that "extends token-based generation to long 3D hand-object interaction, learning a bidirectional mapping between text and HOI sequences." Yet the experimental comparison (Tables 1–3) includes only full-body motion generators (TM2T, MDM, FlowMDM, MotionGPT3) adapted to hand data. HOIGPT is the closest existing method to UniHM's task (text-conditioned hand-object interaction sequences), and its absence makes the "state-of-the-art" claim unsubstantiated. While most other cited methods (SemGrasp, DexGraspNet, etc.) produce only static grasps and are not directly comparable for sequence evaluation, HOIGPT is a sequence-level method that should have been included.

- **Cross-hand generalization claim is untested.** The paper claims "direct token reuse and transfer across robotic and anthropomorphic hands" (Section 1) as a core contribution. However, all experiments train on all five hand morphologies simultaneously (via retargeting of MANO data) and evaluate within those same morphologies. No experiment tests transfer to a held-out hand — e.g., training on 4 hands and testing on the 5th. The unified codebook's generalization to unseen morphologies is asserted but not demonstrated. This is particularly notable because even a simple "leave-one-hand-out" experiment would directly validate the claim.

- **Training/inference gap is not decomposed.** During training, the VLM receives ground-truth target trajectories and object point clouds. At inference, these are estimated by CLIPort and PointSAM (Section 3.3). This gap is acknowledged but never measured — when real-world success rates are 35–65% (Table 3), we cannot tell whether failures come from the VLM's generation quality, CLIPort's trajectory estimation, or PointSAM's segmentation. An oracle-perception condition (injecting ground truth at inference) is needed to isolate the generation module's performance.

### Minor

- **Real-world evaluation is underspecified.** Table 3 reports success rates without specifying which dexterous hand was used on the robot, number of trials per condition, specific objects tested, or variance across trials. Without these details, it is difficult to assess whether success rates of 35–65% are meaningful or how they compare to simple scripted baselines.

- **No reconstruction fidelity reported for the tokenizer.** The unified codebook is central to the method, but the paper reports no reconstruction error per hand morphology (Section 3.2). If the VQ-VAE introduces large reconstruction errors, the downstream VLM cannot compensate. This information is critical for understanding pipeline bottlenecks.

- **GPT-4o annotation quality is not analyzed.** Section 3.1 describes using GPT-4o to generate five instructions per sequence from keyframes, but no human evaluation or quality check of these annotations is reported. It is unclear whether the VLM learns grounded manipulation semantics or exploits biases in GPT-4o-generated language.

- **OakInk vs. DexYCB FID discrepancy unexplained.** FID values on OakInk (e.g., TM2T: 311.90 seen) are an order of magnitude larger than on DexYCB (TM2T: 54.83 seen). This warrants explanation — whether due to sequence length, data complexity, or a normalization issue.

### Trivial
None.

## Nice-to-Haves

- A held-out hand transfer experiment (train on 4 morphologies, test on the 5th) would directly validate the core cross-hand generalization claim.
- Reporting reconstruction error per hand morphology for the VQ-VAE tokenizer would help diagnose information loss in the pipeline.
- Decomposing the training/inference gap via oracle-perception evaluation would clarify where the bottleneck lies.
- Specifying trial counts, the hand used, and object set for real-world experiments.

## Removed Points

These points are flagged to be removed; treat them with caution:

- **Table 1 "data reporting errors" (standard deviations larger than means).** The suspicious values (e.g., 85.33 ± 341) are parser artifacts caused by broken LaTeX `$` delimiters in the extracted text — Tables 2 and 4 in the same paper show proper decimal-point formatting for the same types of values. Per the hard rules, formatting/parser artifacts are not author errors and are removed.

- **VLM architecture underspecified / missing hyperparameters (learning rate, batch size).** Per hard rules, undisclosed hyperparameters and trivial implementation details are categorized as nitpicks to remove.

- **Criticism about FID/Diversity metric definitions.** The critic questions what "Inception features" are used for FID and what Diversity measures — these are generic concerns applicable to any motion generation paper using standard metrics and do not identify a concrete error specific to this paper.

- **Strength Finder claim about "non-overlapping confidence intervals."** The paper reports standard deviations (±), not confidence intervals. The Strength Finder misinterpreted these. Removed from strengths.

- **Strength Finder claim about being "first" to demonstrate sequential dexterous manipulation.** Given that HOIGPT is cited in the paper as doing text-to-HOI sequences, this novelty claim is contestable. Removed as it conflicts with verified weaknesses.

- **Strength Finder claim about "consistent and large-margin SOTA results" as a core strength.** This depends on the baseline comparison being appropriate, which is a verified weakness. Removed due to conflict.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. Include HOIGPT as a baseline in both quantitative and real-world experiments. If adaptation is non-trivial, explain why and provide the best approximation you can.
2. Add a held-out hand experiment: train on four of the five hand morphologies and evaluate on the fifth, measuring MPJPE/FOL/FPL/FID for the unseen hand.
3. Report oracle-perception results (ground-truth trajectories and point clouds at inference) to isolate generation quality from perception errors.
4. Specify trial counts, the robot hand used, object lists, and variance for real-world experiments in Table 3.
5. Report VQ-VAE reconstruction error per hand morphology.

---

**Calibration Anchors Referenced:**

| Paper | Avg Score | Round | Comparison |
|---|---|---|---|
| Pseudo-Tactile Grasping (xcHIiZr3DT) | 2.50 | R1 | Much weaker — simulation-only, narrow scope |
| Early Fusion VLA (KBSHR4h8XV) | 3.33 | R1 | Weaker — limited real-world, thin evaluation |
| Goal-Conditioned Masking (sXF5P4N7e8) | 3.00 | R1 | Weaker — simulation-only grasping |
| Appear→Motion (wl1Kup6oES) | 3.00 | R1 | Weaker — representation learning, no dexterous hand |
| GCML (30SmPrfBMA) | 4.75 | R2 | Weaker — motion quality issues, no real-world |
| Mani-WM (aVyJwS1fqQ) | 4.67 | R2 | Weaker — world model, no dexterous manipulation |
| Video2Policy (RhfYIJux9d) | 5.50 | R2 | Similar pipeline complexity but no real-world eval; UniHM slightly stronger |
| Cross-Embodiment Dex Grasping (twIPSx9qHn) | 5.00 | R1 | Very similar topic; validated cross-hand transfer but weaker real-world; comparable quality |
| HandsOnVLM (AJQuTFd9es) | 6.33 | R1 | Stronger — more thorough hand trajectory prediction eval |
| HAMSTER (h7aQxzKbq6) | 6.00 | R2 | Stronger — more rigorous real-world baseline comparisons |

**Bracketing:**
- **Round 1 bracket:** 4.0–6.0 (above weak anchors at 2.5–3.3, below strong anchors at 7.5+)
- **Round 2 narrowing:** The paper is between GCML (4.75) and Cross-Embodiment (5.00). It is stronger than GCML (real-world results vs. simulated-only motion quality issues) but slightly weaker than Cross-Embodiment (which at least validates its cross-hand transfer claim via actual zero-shot experiments, whereas UniHM's comparable claim is untested).

MY FINAL SCORE: <score>4.5</score>
MY FINAL DECISION: <decision>Reject</decision>