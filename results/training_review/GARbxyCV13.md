Now I have a thorough understanding of the paper and the reviews. Let me synthesize the final consolidated review.

---

## Summary

This paper proposes DINO-WM, a method that uses frozen, pre-trained DINOv2 patch features as the observation model for offline world modeling. The world model predicts future patch features in latent space using a ViT-based transition model with frame-level causal attention, enabling zero-shot planning via CEM-based model predictive control without pixel reconstruction. The method is evaluated on maze navigation, tabletop pushing, rope manipulation, and granular manipulation, showing strong generalization to unseen environment configurations.

## Strengths

- **Clean and principled architectural design.** The use of frozen DINOv2 patch features as a fixed observation model cleanly decouples perception from dynamics learning (Section 3.1.1). This contrasts with prior world models that learn task-specific encoders from scratch. The decoder is optional and trained separately, eliminating the need for pixel reconstruction during planning — a practical advantage over generative approaches like AVDC.

- **Well-controlled ablation identifies the source of improvement.** Table 2 (encoder ablation) varies only the encoder while keeping the transition model fixed. DINO-WM (patch features) achieves 0.90 success on Push-T vs. 0.44 for DINO CLS (global feature), 0.42 for R3M, and 0.20 for ResNet-18. This convincingly demonstrates that spatial patch-level representations — not architectural confounding — drive the gains on manipulation tasks. The Wall task (0.96 vs. 0.58 for DINO CLS) and Rope (CD 0.41 vs. 0.84) further support this conclusion.

- **Strong generalization to unseen environment configurations.** In WallRandom (Table 3), DINO-WM achieves 82% success vs. 76% for DreamerV3 and 6% for IRIS, despite wall/door positions unseen during training. On GranularRandom (unseen particle counts), DINO-WM's Chamfer Distance (0.63) substantially beats all baselines (next best IRIS: 0.86). These results indicate the method learns generalizable dynamics rather than memorizing specific layouts.

- **High-quality visual predictions without pixel-level training objectives.** Table 4 shows DINO-WM achieves the lowest LPIPS (e.g., Push-T: 0.007 vs. next best 0.039) and highest SSIM across four environments. Figure 3 confirms qualitatively that rollouts are visually near-indistinguishable from ground truth, despite the encoder never being fine-tuned on these environments.

## Weaknesses

### Fatal
None. The paper's core idea is sound and the method contributions are real.

### Major

- **Baseline comparison protocol is inadequately specified, weakening the headline quantitative claims.** The paper compares DINO-WM against DreamerV3, IRIS, and TD-MPC2 — methods that incorporate reward prediction into their world model training (Section 4.2). TD-MPC2 is explicitly designed for reward-based representation learning, and the paper itself notes (Section 4.3) that its failure is due to "lack of reward signal." However, the paper never states whether rewards were provided to any of these baselines during training or planning, nor describes how they were adapted for the offline, reward-free goal-reaching setting. Without this information, the "45% improvement over prior SOTA" claim (from Table 1) is difficult to interpret: it conflates the genuine advantages of DINO-WM with the disadvantage of running baselines outside their intended regime. This issue primarily affects Tables 1 and 3 (generalization), though the encoder ablation (Table 2) and visual quality comparisons (Table 4) are not affected.

- **Missing experimental details that prevent proper assessment of the baselines.** The paper provides no description of: (a) how the offline datasets were constructed (size, coverage, collection policy), (b) whether baselines were trained with or without reward signals, termination conditions, and discount factors that their architectures depend on, (c) how planning was performed for non-DINO-WM methods (same CEM procedure? action space? horizon?), and (d) what hyperparameters were used for baseline training. This lack of transparency makes the entire comparison in Tables 1 and 3 difficult to verify or reproduce.

### Minor

- **The ablation does not test whether other patch-level features (non-DINO) would perform similarly.** Table 2 compares DINO patch features against global features (R3M, ResNet, DINO CLS) with the same transition model — this correctly isolates the encoder effect. However, it does not test alternative patch-level visual features (e.g., from a different ViT checkpoint), so the claim that *DINOv2 specifically* is responsible for the gains (rather than "any spatially-structured patch representation") is not fully supported. This is a scope limitation, not a methodological flaw.

- **Only simulated environments are evaluated.** The paper claims that DINOv2's internet-pretrained priors enable generalization, but all experiments are in simulation with clean RGB renderings. A key test of this claim would be application to real-world video or robotic data without retraining the encoder.

### Trivial

- The paper states (Section 3.1, Eq. 1) that the observation model is parameterized by `enc_θ` and also trained — but Section 3.1.1 says DINOv2 is kept frozen. The notation suggests `θ` includes the encoder parameters, which conflicts with the text stating the encoder is frozen. This minor inconsistency should be clarified.

## Nice-to-Haves

- **Controlled comparison with reward-conditioned baselines.** Running DreamerV3 and IRIS with a reward function (e.g., negative distance to goal) would help separate whether DINO-WM's advantage comes from its representation or from the absence of rewards in the comparison. This is a suggested extension, not a required fix.

- **Analysis of latent space geometry.** The planning cost uses MSE in DINOv2 feature space. Visualizing the latent space (e.g., what goals are "close" under the MSE metric) would help validate this design choice.

- **Failure case analysis.** DINO-WM achieves 98% on PointMaze and 90% on Push-T. Understanding the 2% and 10% failure modes (dynamics error? planning horizon? CEM getting stuck?) would strengthen the paper.

## Removed Points

- "TD-MPC2 scores 0.00 on all tasks, including simple environments like PointMaze where random actions have non-zero success probability... 0.00 is not credible." — **Removed**: The paper explicitly explains (line 188) that TD-MPC2's failure is due to missing reward signal, not random action performance. For a D4RL U-shaped maze, reaching an arbitrary goal from a random start via a poorly learned latent space plausibly yields 0.00 success. The critic misunderstands the failure mode.

- "DreamerV3 achieves 1.00 on Wall but 0.04 on Push-T — a gap too large to be explained by task difficulty alone." — **Removed**: This gap is entirely explainable by task difficulty. Wall is a simple 2D navigation task (go through a known door) while Push-T requires precise contact-rich manipulation over 25 steps. DreamerV3's world model is known to struggle with precise object interactions.

- "The paper does not engage with recent work on using DINO features for control (e.g., DINO-based policies), which would help contextualize DINO-WM." — **Removed**: Per hard rules, we do not mention missing related works.

- "The contribution of DINOv2 patch features is not isolated" (as stated in the critic's formulation claiming it's an evidential gap). — **Weakened to Minor**: Table 2 actually DOES isolate the encoder (same transition model, different encoders). The critic's claim that the paper should also "plug DINOv2 features into DreamerV3's or IRIS's architecture" is a different question — it probes architectural interaction rather than isolating the encoder contribution. The existing ablation is informative but could be extended.

- Several generic "deeper analysis" suggestions (t-SNE visualizations, nearest-neighbor retrieval) — **Moved to Nice-to-Haves**.

- Comment about decoder comparison being unfair because baselines train decoder jointly — **Removed**: The paper's decoder is only used for *visualization* (Section 3.1.3), not for planning. The LPIPS/SSIM comparison simply measures reconstruction quality from latents, not planning performance. This is a valid comparison of decoder capability.

## Novel Insights

The most interesting observation from these reviews is the tension between the paper's genuine architectural contribution (frozen patch-level pretrained features for offline dynamics) and the weakness of its evaluation protocol. The reviewers' criticisms about baseline fairness have merit, but they also reveal something subtle: the paper's strongest evidence is actually *not* the Table 1 comparison against DreamerV3/IRIS/TD-MPC2, but rather the controlled ablation in Table 2. That ablation, which keeps the transition model fixed and only varies the encoder, shows a 2×+ improvement of patch features over global features. This is a cleaner experiment and should be the centerpiece of the paper's evidence for its claims. The noisy baseline comparison against reward-based methods is a distraction that weakens rather than strengthens the paper.

## Suggestions

1. **Clarify the baseline evaluation protocol.** State explicitly whether rewards were provided to DreamerV3, IRIS, and TD-MPC2. If rewards were not provided (which appears to be the case), acknowledge this limitation transparently and reframe the comparison as "our method versus prior methods evaluated in a setting for which they were not designed" — or, better, add a controlled comparison where reward-based methods receive a reward signal.

2. **Restructure the evidence hierarchy.** Move the encoder ablation (Table 2) more prominently into the main results, and clearly separate the "fair" comparisons (same architecture, different encoders) from the "apples-to-oranges" comparisons (DINO-WM vs. reward-based methods). Consider relegating TD-MPC2 to an ablation or removing it entirely, since the paper acknowledges it fails without rewards.

3. **Add experimental details.** Include dataset statistics (number of trajectories, coverage), training hyperparameters for each baseline, planning configuration (CEM iterations, population size, horizon), and the exact procedure for adapting each baseline to the offline planning setting. This is essential for reproducibility.

4. **Consider testing alternative patch-level features.** Even a single comparison against patch features from a non-DINO ViT (e.g., MAE, CLIP ViT) would substantially strengthen the claim that DINOv2's particular representation matters.

5. **Clarify the notation inconsistency** between the observation model having learned parameters `θ` (Eq. 1) and the text stating DINOv2 is frozen (Section 3.1.1).

## Score and Decision

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Weak Accept</orange>

**Rationale**: The paper introduces a clean and well-motivated method with convincing ablation evidence (Table 2) and impressive generalization results (Table 3). The core idea — using frozen pretrained patch features for offline world modeling — is a genuine contribution that advances the state of the art in task-agnostic world modeling. However, the experimental evaluation is undermined by the weak baseline comparison protocol against reward-based methods without adequate specification of how they were adapted. The headline quantitative claims (45% improvement) are not well-supported. The paper would benefit from a major revision to the evaluation section, but the method itself is sound enough to warrant publication with revisions. The score reflects a positive assessment of the core contribution tempered by concerns about the evaluation rigor.