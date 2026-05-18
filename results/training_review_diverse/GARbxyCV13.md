Now I have all the information needed to produce the consolidated review.

---

## Summary

DINO-WM proposes a simple and effective method for building task-agnostic world models from offline trajectory data by using frozen DINOv2 patch features as the observation encoder and a frame-level causal ViT as the transition model. Planning is performed via MPC with CEM in latent space, using goal images as targets without any reward signal, expert demonstrations, or inverse modeling. The method achieves substantially higher success rates on contact-rich manipulation tasks (PushT: 0.90 vs. 0.32 for the best baseline) and demonstrates generalization to unseen environment configurations.

## Strengths

- **Frozen DINOv2 patch features are a principled design choice for task-agnostic world modeling.** The ablation study (Table 2) cleanly shows that patch-level features massively outperform global feature encoders (R3M, ResNet-18, DINO CLS), especially on manipulation tasks requiring spatial precision. This directly supports the paper's central claim that rich spatial priors from pretrained patch features are a key enabler for offline world modeling.

- **Frame-level causal attention in the transition model is a well-motivated architectural contribution.** The paper distinguishes its frame-level autoregressive prediction (treating all patches of one observation as a whole) from IRIS's token-level prediction, arguing this better captures global temporal structure. The strong empirical results, particularly on multi-step planning tasks, provide circumstantial evidence for this design.

- **Strong empirical results with meaningful headroom over baselines.** On the most demanding tasks (PushT: 0.90 SR vs. 0.32 for IRIS; Rope CD: 0.41 vs. 1.11 for IRIS), DINO-WM shows large and consistent advantages. The generalization results (WallRandom: 0.82 SR vs. 0.76 for DreamerV3) further demonstrate that the approach learns reusable dynamics knowledge.

- **Decoupling the decoder from the dynamics model is pragmatically sound.** Training the decoder independently and only for interpretability means planning never requires pixel reconstruction, reducing computational cost and avoiding the coupling of representation quality to reconstruction objectives.

## Weaknesses

### Major

- **Offline dataset generation is not described.** The paper repeatedly emphasizes that the world model is trained on "offline, pre-collected trajectories" but provides no details about how these trajectories were generated — whether from random actions, a scripted policy, an expert, or a mixture; how many trajectories were used; episode lengths; or state-space coverage. This matters for interpreting the generalization results (e.g., WallRandom: if the training data already contained walls at varying positions, generalization is less surprising) and makes the work difficult to reproduce or build upon. [Verified: Section 4.1 describes the environments but not the data collection process.]

- **Baseline adaptation details are insufficiently specified.** The paper compares against IRIS, DreamerV3, TD-MPC2, and AVDC but does not explain how reward-dependent components (DreamerV3's actor-critic and reward predictor, TD-MPC2's reward-conditioned latent learning, IRIS's value functions) were handled in the task-agnostic, reward-free setting. The paper acknowledges that TD-MPC2 scores 0.00 due to "the lack of reward signal," but does not specify whether DreamerV3's planning was done via CEM on its latent representation or via its standard policy, nor whether the baselines' world models were trained from scratch on the same offline data. Without this information, the reader cannot fully separate whether DINO-WM's advantage stems from the frozen DINOv2 encoder, the training procedure, or a mismatch between the baselines' design assumptions and the evaluation protocol. [Verified: Section 3.2 describes baselines at a high level with no adaptation details; the results section (discussion of Table 1) notes the reward issue for TD-MPC2 but no details for other baselines.]

### Minor

- **Planning hyperparameters are not reported.** The paper uses CEM with MPC but does not give the planning horizon, number of CEM iterations, population size, elite fraction, action repeat, or initial action distribution. These choices can significantly affect success rates and are needed both for reproducibility and for judging whether the results are robust. [Verified: Section 3.3 mentions CEM without any hyperparameters.]

- **No error bars or confidence intervals.** The main results tables report point estimates only (50 trials for success rates, 10 for Chamfer distances). Reporting standard errors or confidence intervals would help assess the reliability of the reported advantages, particularly on smaller sample sizes (e.g., 10 trials for rope/granular). [Verified: Tables 1, 2, 3 — no error metrics reported.]

- **Qualitative comparison with AVDC provides limited evidence.** Section 4.5 compares DINO-WM with a diffusion-based generative model only qualitatively, showing a few rollout visualizations. While the paper appropriately frames this as a sanity check, it adds limited weight relative to the quantitative comparisons.

### Trivial

- **The term "zero-shot" could be clarified.** The paper describes DINO-WM as enabling "zero-shot behavioral solutions," which is defensible (the model is not fine-tuned per task) but might be misinterpreted as generalization to entirely unseen environment dynamics rather than unseen goals within a known environment family.

## Nice-to-Haves

- An analysis of *why* patch-level features help — e.g., showing the per-patch prediction error and its correspondence to the spatial regions that need to change during planning — would deepen the paper's core observation.
- A sensitivity analysis of planning hyperparameters (planning horizon, CEM iterations) would strengthen the claim that the latent representation is stable enough for test-time optimization.
- A brief discussion of how the frozen DINOv2 encoder might limit generalization to visually dissimilar environments (real-world images with varying lighting, backgrounds, camera angles) would be helpful, even if only as a limitation.

## Removed Points

These points were raised by reviewers but are removed or downgraded here:

- **Criticism that TD-MPC2's 0.00 score is an "unfair comparison"** — Kept but moved to Major (not removed entirely) since the paper acknowledges the reward issue and the experiment is consistent with the paper's framing of demonstrating why task-specific methods fail in the task-agnostic setting. However, the lack of detail about *how* other baselines were adapted remains a legitimate concern.
- **"No description of baseline adaptation makes comparison invalid"** — The concern is real but does not invalidate the comparison. DINO-WM's dramatic outperformance on manipulation tasks (PushT: 0.90 vs. 0.32) is large enough that even substantial differences in baseline adaptation would not bridge this gap. Downgraded from "Critical" to "Major."

## Novel Insights

The reviews collectively surface an interesting tension: the paper's strongest evidence (DINOv2 patch features beating global features) is simultaneously its most convincingly demonstrated point and the one with the simplest explanation (spatial information matters for manipulation). The deeper insight — and what is less fully explored — is *why* frozen internet-pretrained features specifically benefit offline world modeling in a way that environment-specific learned encoders do not. The fact that the DINO CLS (global) variant underperforms the DINO patch variant by roughly 2× on PushT (0.44 vs. 0.90) while the two variants perform similarly on PointMaze (0.96 vs. 0.98) suggests that the benefit is task-dependent and related to spatial precision requirements. This could motivate future work on understanding when pretrained patch features confer generalization vs. when they are incidental.

## Suggestions

1. **Add a dedicated "Experimental Setup" section** describing: (a) how each offline dataset was generated (source policy, trajectory count, episode length), (b) for each baseline, exactly how it was adapted to the task-agnostic setting (which components were kept/dropped and why), and (c) CEM hyperparameters used for all methods.
2. **Add standard errors** to Tables 1–3, or at minimum report the number of trials and a measure of variance.
3. **Clarify the "zero-shot" claim** with a sentence noting that the model generalizes to unseen goals/configurations within the same environment family, not to entirely novel environment types.
4. **Report the context length hyperparameter H** used in the transition model and any sensitivity to this choice.

## Score and Decision

The paper presents a technically sound and well-motivated method with strong empirical results. The core idea — using frozen pretrained patch features for latent-space world modeling — is clean, the ablation convincingly attributes the gains to the patch-level representation, and the performance margins on manipulation tasks are large and consistent. The weaknesses are primarily omissions in experimental description rather than flaws in the methodology or evidence. These are fully fixable in a camera-ready version.

**Originality:** High. The combination of frozen DINOv2 patch features with frame-level latent prediction and goal-conditioned planning is novel and well-scoped.  
**Quality of claims:** Claims are supported by the evidence, though the missing experimental details make some comparisons harder to fully assess.  
**Soundness:** The methodology is sound. The ablations are informative. No evidence of flawed reasoning.  
**Clarity:** Generally clear, but the missing experimental setup details reduce transparency.  
**Value to community:** The idea of leveraging pretrained visual features for world modeling is likely to be influential and practically useful.

MY FINAL SCORE: <pineapple>7.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>