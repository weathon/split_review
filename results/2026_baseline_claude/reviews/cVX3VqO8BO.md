## Summary

UniHM is a unified framework for dexterous hand manipulation guided by open-vocabulary language instructions. The system combines three components: (1) a morphology-agnostic VQ-VAE tokenizer that maps heterogeneous hand morphologies to a shared discrete codebook via knowledge distillation; (2) a small VLM (Qwen3-0.6B) trained on human-object interaction (HOI) video data for language-conditioned token sequence generation; and (3) a physics-guided dynamic refinement module using Gauss-Newton optimization with contact, generative, and temporal priors. The system is evaluated on DexYCB and OakInk benchmarks as well as real-world robot trials.

---

## Strengths

- **Meaningful problem formulation and training paradigm.** The goal of eliminating teleoperation data dependency by learning from human video is practically important and well-motivated. Training solely on HOI data and showing generalization to robot hands is a useful proof-of-concept.

- **Well-formulated physics refinement.** The Gauss-Newton energy minimization (Section 3.4) is mathematically rigorous: the asymmetric penalty in Eq. 12, the LM-damped normal equations in Eq. 17–18, and the causal frame-by-frame structure are all sound design choices. The ablation in Table 4 confirms the module's positive impact on MPJPE, FOL, FPL, and FID.

- **Morphology-agnostic codebook design.** The knowledge distillation step (Eq. 3) that aligns new encoder latent spaces to the reference before VQ-VAE fine-tuning is a sensible solution to the gradient discontinuity problem. The pose translation formula (Eq. 6) is clean and elegant.

- **Comprehensive ablation.** Table 4 isolates the three main design choices (depth input, masked training curriculum, physical refinement), and the results consistently validate each component. The progressive masking from teacher-forcing to full masking is a principled exposure-bias mitigation strategy.

---

## Weaknesses

### Fatal
None.

### Major

1. **Primary claimed contribution lacks quantitative evaluation.** The Unified Hand-Dexterous Tokenizer and its cross-morphology transfer (Eq. 6) are presented as the central technical contribution, and the system claims to support five dexterous robot hands (Shadow, Allegro, SVH, Leap, Panda). Yet Tables 1–4 are evaluated exclusively on human hand (MANO) datasets (DexYCB, OakInk). No reconstruction error, retargeting quality metric, or cross-morphology transfer accuracy is reported for any robot hand morphology. The real-world evaluation in Table 3 shows robot arm grasps qualitatively (Fig. 3), but without per-morphology quantitative breakdown. The paper's strongest claimed advantage—unified cross-hand generalization—is thus not quantitatively substantiated.

2. **Inappropriate or under-specified baselines.** The four comparative methods (TM2T, MDM, FlowMDM, MotionGPT3) are whole-body human motion generation models. The paper does not specify whether these methods were retrained on DexYCB/OakInk or adapted in any way to the dexterous hand domain, making the comparison hard to interpret. More directly relevant baselines (e.g., SemGrasp, Multi-GraspLLM, DexGYS) exist in the language-guided dexterous grasping space, yet none appear in the comparison tables. While these produce only static poses and may not be perfectly comparable, their absence weakens the "state-of-the-art" claim in this specific domain.

3. **Real-world evaluation is underspecified.** Table 3 reports success rates without: (a) the number of trials per condition, (b) the specific robot hardware, (c) what constitutes "seen" vs. "unseen" in deployment (whether new objects, new instructions, or both), and (d) confidence intervals or standard deviations over trials. The "Dex-Retargeting" postprocessing used for the real-world baselines is not described in enough detail to be reproducible. Qualitative results are referenced ("Fig.D2") but only available in an appendix.

### Minor

1. **Diversity disadvantage on DexYCB.** On DexYCB (Table 1), the GT diversity is 125.53 and UniHM's diversity (39.62 seen, 42.70 unseen) is substantially below MotionGPT3 (72.51 seen, 75.84 unseen). The paper does not discuss why this divergence is acceptable and whether it reflects mode collapse in the VQ codebook or the autoregressive generation.

2. **CLIPort adaptation unclear.** CLIPort was designed for top-down 2D pick-and-place. Its use here to produce SE(3) target trajectories $\mathcal{T}_{\text{tar}} \in \text{SE}(3)^K$ is non-trivial, but Section 3.3 does not describe how CLIPort is modified for 3D dexterous manipulation, making this component difficult to reproduce.

3. **No ablation over model scale.** The paper justifies choosing Qwen3-0.6B because of data scarcity but provides no comparison to larger models (e.g., 1.5B, 7B) even with limited data. Given the small model size, it is unclear whether the bottleneck is model capacity or data volume.

### Trivial

- The FID numbers for OakInk (200–337 range) are orders of magnitude larger than DexYCB (30–55 range), suggesting the feature spaces used are different; this difference is not explained or harmonized.
- The paper states FID comparisons are "fair" because baselines are post-processed with UniHM's own refinement, but for some metrics (especially MPJPE) this may inadvertently mix the effects of the generation and refinement modules.

---

## Nice-to-Haves

- A cross-morphology reconstruction experiment: train the tokenizer on MANO, transfer to Shadow/Allegro/Leap, and report per-joint reconstruction error for each, to directly quantify the codebook's morphology-agnostic claim.
- A runtime analysis showing the per-frame inference latency of the full pipeline (CLIPort + VLM + Gauss-Newton refinement) and whether it supports real-time or near-real-time operation.
- A data-scaling experiment showing how performance on DexYCB/OakInk changes as the amount of HOI training data varies, to better support the "learning from video" narrative.

---

## Novel Insights

The most genuinely novel insight is the combination of pre-alignment via knowledge distillation (Eq. 3) with subsequent VQ-VAE fine-tuning to achieve morphology-agnostic codebook sharing across kinematically heterogeneous robot hands. This sidesteps the gradient discontinuity inherent in straight-through VQ training and makes incremental addition of new morphologies practical without retraining the full codebook. The modular inference design—where only CLIPort adapts to distribution shift while the HOI generator remains frozen—is also an interesting data-efficient deployment strategy that could be of general utility.

---

## Suggestions

- Add a cross-morphology transfer evaluation table: for each of the five supported robot hands, report VQ reconstruction error (MPJPE equivalent) before and after the distillation step, to demonstrate the tokenizer's core claim.
- Retrain MDM, FlowMDM, and MotionGPT3 on DexYCB/OakInk hand data and report those numbers explicitly, or substitute one baseline that is native to the dexterous manipulation setting.
- Expand Table 3 with trial counts, standard deviations, and a description of test objects and conditions.
- Discuss and analyze the low diversity of UniHM on DexYCB (39.62 vs. GT 125.53); consider whether codebook size K or the temperature at generation time can be tuned to recover diversity.

---

## Score and Decision

UniHM addresses a practically meaningful problem and has three technically reasonable components. The physics refinement and distillation-based tokenizer training are the strongest parts of the paper. However, the primary claimed contribution—cross-morphology unified tokenization—lacks quantitative evaluation, the baselines are body-motion methods not native to the hand domain, and the real-world experiments are not described with enough rigor to be reproducible or fully trusted. These gaps collectively prevent confident acceptance.

MY FINAL SCORE: <score>4</score>
MY FINAL DECISION: <decision>Reject</decision>