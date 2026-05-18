Now I have all the information I need. Let me draft the final consolidated review.

---

## Summary

This paper proposes rRCM (Robust Representation Consistency Model), a two-stage training approach for certified robustness against ℓ₂-norm adversarial perturbations. In pre-training, the model aligns representations of temporally adjacent points along noise-perturbed trajectories via contrastive learning on pairs constructed from the same clean image with identical noise at different noise levels. During fine-tuning, a classification head is trained with additional consistency regularization across independently-noised samples. The method achieves state-of-the-art certified accuracy (5.3% average improvement over diffusion-based methods on ImageNet) while reducing inference cost by 85× compared to purification-based diffusion approaches.

## Strengths

1. **State-of-the-art certified accuracy with a wide margin.** Table 1 shows rRCM-B-Deep surpasses the best diffusion-based method (DDS) by 5.3% on average across radii on ImageNet, with gains up to 11.6% at larger radii (r=1.0: 26.6% vs. 15.0%). On CIFAR-10 (Table 2), rRCM-B outperforms DDS at every radius (e.g., +6.4% at r=0.5). These results are clearly documented and the evaluation follows standard certification protocols (500 images, 99.9% confidence, 100k smoothing noises).

2. **Dramatic inference cost reduction while improving accuracy.** The paper reports an average 85× reduction in inference latency over diffusion-based methods. Concrete numbers in Table 1 show rRCM-B certifies a sample in 53s versus 52min 20s for DensePure and 28min 4s for DiffSmooth — a genuine and practically meaningful improvement.

3. **Novel training paradigm unifying denoising and classification.** The method reformulates the generative denoising task into a discriminative consistency-alignment problem in latent space (Section 3), enabling one-step denoising-then-classification. This eliminates the separate purification + majority-voting pipeline required by prior diffusion-based approaches, which is architecturally non-trivial.

4. **Strong scalability.** Section 4.3 and Figures 3-4 demonstrate consistent certified accuracy improvements with increasing model parameters (rRCM-S → rRCM-B → rRCM-B-Deep) and training batch size, with no signs of saturation — suggesting further gains are possible with more resources.

## Weaknesses

### Major

1. **PF ODE trajectory framing does not match the implementation.** The paper's core narrative (Sections 1, 3.1) claims to leverage the *deterministic PF ODE trajectories* of diffusion models, repeatedly emphasizing that points on the same PF ODE trajectory share unique semantics. However, the actual positive pair construction (Section 3.3) uses the approximation $x_{t_{n-1}} = x_{t_n} + (t_{n-1} - t_n)\epsilon$, which yields $x_0 + t_{n-1}\epsilon$ — simply a noisier version of the same image with the same noise direction. These points lie on the same *forward SDE* path (a straight line in noise direction), not on the PF ODE trajectory (which requires the score function for reverse steps and is curved for non-Gaussian data). While the paper acknowledges this approximation ("leaving further exploration of pre-trained score models to future research"), the surrounding narrative consistently presents the method as exploiting PF ODE structure. This disconnect means the claimed theoretical grounding (contribution item 1: "first to exploit the advantages of the structured noise schedule of diffusion models") is materially overstated. The method itself is a reasonable empirical approach — aligning representations of correlated-noise pairs at different noise levels — but it is not what the paper advertises it to be theoretically. This weakens the claimed novelty relative to methods that train on noisy samples (e.g., Jeong & Shin 2020), which also use multiple noise levels but without the contrastive pre-training framework.

2. **Experimental comparisons do not isolate the pre-training contribution.** The paper compares rRCM against diffusion-based methods (DDS, DensePure, DiffSmooth) using a ViT classifier with 81.35% clean accuracy trained via standard supervised learning. However, rRCM receives extensive contrastive pre-training (600k steps, batch size 4096 on ImageNet) before fine-tuning. Without a baseline that uses the same compute budget with standard contrastive pre-training (e.g., MoCo-v3 followed by the same fine-tuning), it is impossible to tell whether the gains come from the noise-specific pair construction or simply from having a better base representation after heavy pre-training. The paper mentions a comparison with MoCo-v3 in Figure 5 but does not provide quantitative certified accuracy results from that ablation. This confound is the primary barrier to attributing the method's strong results to the proposed mechanism rather than to increased training compute.

### Minor

3. **Correlated noise in pre-training vs. independent noise in certification.** During pre-training, positive pairs use the *same* noise vector $\epsilon$, learning invariance to noise magnitude but not noise direction. During certification, each sample receives *independently* drawn noise (per the randomized smoothing protocol). The fine-tuning stage (Equation 9) partially addresses this by enforcing consistency between two independent noisy versions at the same noise level, but the pre-training may provide a suboptimal inductive bias. The paper acknowledges the discrepancy (Section 3.3) but provides no analysis (e.g., ablating same-$\epsilon$ vs. independent-$\epsilon$ pre-training) to justify the design choice or demonstrate its impact.

4. **Clean accuracy not reported.** The paper reports only certified accuracy at various radii $r$. While $r=0$ certified accuracy captures performance on unperturbed images under the smoothing procedure, standard (non-smoothed) clean accuracy of rRCM models is not stated. This makes it difficult to assess whether robustness gains come at a cost to standard performance, and is a standard omission in the certified robustness literature that the paper could easily address.

5. **Missing ablation studies.** Key design choices are not ablated: (a) the consistency loss vs. contrastive loss terms in Equation 7, (b) the effect of the EMA rate choices (0 vs. 0.99), (c) placement of losses on encoder vs. projector outputs (the paper mentions training instability but provides no evidence), and (d) fine-tuning regularization coefficients ($\eta_1$, $\eta_2$). While early experiments are mentioned, systematic ablation would strengthen confidence in the design.

### Trivial

None.

## Nice-to-Haves

- Using a pre-trained score model to generate proper PF ODE trajectory points during pre-training (acknowledged as future work in Section 3.3) would align the implementation with the claimed theoretical framing.
- Reframing the method as using forward-SDE pairs rather than PF ODE trajectories, with a simpler justification centered on the value of same-noise-different-magnitude positive pairs for downstream robustness, would more honestly represent what is done.
- Confidence intervals or variance estimates for certified accuracy across multiple certification runs would quantify the stability of the reported numbers.
- Comparison against newer certified defenses from 2024–2025 (if applicable given the submission timeline) would help position the work.

## Removed Points

These points are flagged to be removed; treat them with caution:

- **Novelty over existing work (Jeong & Shin 2020, Zhai et al. 2020).** The reviewer claimed training on multiple noise levels is not new. However, the paper's claim is about using a *structured noise schedule* (the full diffusion noise schedule with many time steps from EDM, not just one or two certification noise levels) combined with contrastive learning on same-noise-direction pairs. The paper cites these works and acknowledges the similarity of the fine-tuning consistency term (Equation 9) to Jeong & Shin (2020). The criticism conflates multi-level training with the paper's specific design.
- **Statistical uncertainty (missing confidence intervals).** Certified accuracy in randomized smoothing is standardly reported as a single number following the Cohen et al. (2019) protocol. Each individual certification already involves statistical testing at 99.9% confidence. Requesting confidence intervals for the aggregate accuracy over the 500-image subset is not standard practice in this literature.
- **Comparison with more recent work (2024–2025).** Without knowing the paper's submission date, this is an unfair ask. The paper cites works up to Li et al. (2024) and Jeong & Shin (2024).
- **General formatting/style nitpicks and suggestions about adding appendix proofs or missing references** — these reflect parser artifacts, not author errors.

## Novel Insights

None beyond the paper's own contributions. The reviews do not surface a genuinely novel perspective that the paper itself does not already articulate. The key tension between the PF ODE framing and the forward-SDE implementation is well-identified by the Harsh Critic but is fundamentally a mismatch between the paper's narrative and its execution rather than an insight that opens a new research direction.

## Suggestions

1. **Correct the PF ODE narrative.** Either (a) use a pre-trained score model to generate actual PF ODE trajectory points (and demonstrate this improves results), or (b) drop the PF ODE framing entirely and reframe the pre-training as aligning representations of forward-SDE pairs (same-image, same-noise-direction, different-magnitude). Option (b) is more practical and honest — the justification would be: "correlated-noise pairs at different noise levels provide a useful inductive bias for downstream certified robustness." If choosing (b), provide a clear comparison showing that same-$\epsilon$ pairs outperform independent-$\epsilon$ and single-level baselines.

2. **Add a controlled ablation for pre-training.** Compare rRCM pre-training against standard contrastive pre-training (MoCo-v3) using the same batch size, steps, and data augmentation, followed by the identical fine-tuning procedure. Report certified accuracy for both. This is the single most important experiment to substantiate the claimed contribution.

3. **Report clean accuracy** of rRCM models and baseline classifiers to contextualize robustness-accuracy trade-offs.

4. **Add ablation studies** for the two loss terms in Equation 7, EMA rates, and fine-tuning hyperparameters ($\eta_1$, $\eta_2$) to substantiate design choices.

5. **Analyze the same-$\epsilon$ vs. independent-$\epsilon$ design choice** in pre-training by including a comparison between these two variants while keeping all other factors constant.

## Score and Decision

The paper presents a genuinely effective two-stage training method for certified robustness with strong empirical results and practically meaningful inference speedups. However, the central theoretical claim is overstated (the PF ODE trajectory motivation does not match the implementation), and the experimental evaluation lacks a controlled ablation that isolates the contribution of the noise-specific pre-treatment from the effect of additional compute. These are substantial weaknesses, but they primarily affect attribution and framing rather than invalidating the empirical findings. With honest reframing and targeted ablation experiments, the paper's contributions would be clearly valuable to the community.

MY FINAL SCORE: <pineapple>5.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>