Now I have a clear picture of the paper and the reviewer inputs. Let me compose the final consolidated review.

## Summary

G2Sphere proposes a method that maps 3D geometric inputs (meshes, point clouds, keypoints) to continuous spherical signals by combining an equivariant encoder with a spherical harmonic decoder that outputs Fourier coefficients. The approach supports frequency up-sampling up to L=40, zero-shot super-resolution, and fast single-pass inference (9ms). The method is evaluated across three domains: radar response prediction, aerodynamic drag modeling, and policy learning (behavioral cloning for manipulation and navigation), showing consistent improvements over baselines.

## Strengths

1. **High-frequency spherical signal modeling via frequency up-sampling.** G2Sphere reaches L=40 through frequency up-sampling with trainable spherical non-linearities (TSNL), far exceeding the L≤10 ceiling of prior equivariant GNN architectures for dense geometric inputs (Section 4.2). This translates into visibly sharper predictions on radar signals (Fig. 3) and the lowest MSE on both radar datasets (Table 1).

2. **Zero-shot super-resolution capability.** Because G2Sphere outputs continuous Fourier coefficients, it can be trained on low-resolution (61×21) radar data and evaluated at higher resolution (180×21) without retraining (Fig. 4). This is a structural advantage over fixed-grid baselines (Transformer, Equiformer) that lack this flexibility.

3. **Fast single-pass inference for control.** G2Sphere evaluates the full spherical signal in 9ms (Nvidia Titan), compared to 156ms/action for Diffusion Policy and 44ms for IBC (Table 3). This is enabled by pre-computing spherical harmonic basis functions and avoiding iterative optimization or denoising — a genuine practical advantage for closed-loop control.

4. **Consistent performance across diverse domains.** G2Sphere (or G2S+TSNL) achieves the lowest MSE on all radar and drag tasks (Table 1) and strong results on PushT and PyBullet Drones policy tasks (Table 2), including near-perfect coverage on fixed PushT. The breadth of evaluation across dense (radar) and sparse (drag) spherical signals strengthens the claims of generality.

5. **Superior generalization from sparse training data.** On the drag task, trained on only one (θ,φ) coordinate per object, G2Sphere reconstructs the full drag cone over [-20°,20°] while implicit baselines overfit to the training coordinates (Fig. 5). This demonstrates a concrete advantage of the Fourier-space representation over coordinate-conditioned implicit models.

## Weaknesses

### Major

- **Missing ablation results for the non-equivariant variant (NE-G2S).** Section 5.2 introduces NE-G2S (replacing equivariant MLPs with standard MLPs while retaining the Fourier-space decoder) specifically "to separate the impact of equivariance and representing the output in Fourier space." Yet no quantitative results for NE-G2S appear in the text or are referenced from Table 2. The text then claims that "the addition of equivariance stabilizes training instability leading to more consistent performance" without presenting the comparison that would substantiate this. Since the paper's overall design couples equivariant encoding with Fourier-space decoding, the NE-G2S ablation is critical for attributing improvement to each component. Its absence weakens the core scientific claim.

### Minor

- **Radar output signal is not specified.** The paper never states whether the predicted radar response is complex-valued (amplitude and phase, as would be standard for radar) or real-valued (e.g., radar cross-section magnitude). The grayscale visualizations (Figs. 3, 4) suggest magnitude, but the loss function (MSE) and the architecture's output dimension depend on this choice. This omission affects interpretability of the reported errors.

- **"Operates entirely in Fourier space" overstates the method.** The abstract and Section 2 claim G2Sphere "operates entirely in Fourier space" and contrast this with FNO which "moves back and forth between real and Fourier spaces." However, Section 4.2 (frequency up-sampling) explicitly describes mapping the signal back to real space via IFT for pointwise non-linearities, then transforming back with higher resolution. The method *represents the output* in Fourier space, but the forward pass alternates domains — the same pattern criticized in FNO. This framing should be adjusted for accuracy.

- **Multimodality claim lacks quantitative evidence.** The paper claims G2Sphere "is equally likely to take any of the N-paths" and can control multimodality via maximum frequency (Section 5.2), but the evidence is entirely qualitative: energy landscape visualizations (Fig. 7) and rollout examples (Fig. 8). No quantitative metric (e.g., path-choice entropy, diversity score, per-path success rate with standard errors) is reported. The observation is interesting but the claim of equal likelihood is unsupported.

### Trivial

- The paper uses "embodied" for "energy-based model" (line 130: "EMBs" instead of "EBMs") — a minor typo.

## Nice-to-Haves

- A quantitative evaluation of zero-shot super-resolution (e.g., MSE vs. output resolution) would strengthen the claim beyond the qualitative comparison in Fig. 4.
- An ablation on the maximum frequency L for the radar task (e.g., sweeping L=10,20,30,40) would help justify the choice L=40 and characterize the accuracy-computation tradeoff.
- Confidence intervals or paired significance tests would be informative for the modest improvements on drag (e.g., G2S+TSNL at 0.026 vs. next best at 0.033).

## Removed Points

These points were flagged but are removed from the main review with justification:

- **Harsh Critic: "Fairness and depth of baseline comparisons in policy learning"** — The claim that Diffusion Policy results "seem low relative to published numbers" is speculative and cannot be verified from the paper text (the actual numerical values are in an image table). The concern about hyperparameter tuning effort is a generic criticism that applies to nearly all experimental comparisons without evidence of specific mistuning. Removed.
- **Harsh Critic: "Modest improvement on radar/drag"** — The improvements are indeed modest in absolute terms (e.g., Asym: 0.026 vs. 0.033 MSE), but the paper reports standard errors and the improvement is consistent across datasets. This is a fair observation about effect size but not a weakness of the paper — it accurately reflects what was found. Removed as non-actionable.
- **Harsh Critic: "Generalization to unseen objects is only qualitative"** — The paper explicitly shows a quantitative comparison (the drag cone plots) and discusses the behavior difference between models. The qualitative demonstration is appropriate for illustrating the overfitting pattern. Removed.
- **Strength Finder: "Controllable multimodality via maximum frequency"** — While the idea is interesting, the evidence is qualitative only. This conflicts with the verified weakness that multimodality claims lack quantitative support. Removed on the weakness-prevails-over-strength rule.
- **Strength Finder: "Ablation confirms equivariance improves performance"** — If NE-G2S results are not presented in the table (as the text suggests), this claim is unsupported. Removed pending verification.
- **Strength Finder: Generic strengths about addressing important problems / community value** — These lack specific citations to paper content. Removed.

## Novel Insights

The most interesting observation from the intersection of the reviews is that the paper presents two genuinely distinct contributions — the equivariant encoder and the Fourier-space decoder — but fails to disentangle their relative contributions experimentally. The NE-G2S ablation was designed to do this, making its absence from the results doubly consequential. A separate observation: the paper's strongest practical advantage (9ms inference) comes from a relatively standard engineering choice (pre-computing harmonic bases), while its most novel technical contribution (frequency up-sampling to L=40) is demonstrated only in the radar domain and without ablation. This suggests the method's impact may depend more on the encoder-decoder architecture choice than on the exact frequency up-sampling mechanism used.

## Suggestions

1. **Add NE-G2S results to Table 2** (and ideally to Table 1 as well). This is the single most impactful fix — it would directly quantify how much of G2Sphere's improvement comes from equivariance vs. the Fourier-space decoder, addressing the main evidential gap.
2. **Clarify whether the radar output is complex or real-valued** and, if real, which physical quantity is being predicted (e.g., RCS magnitude). This takes one sentence.
3. **Add a quantitative metric for multimodality** on the N-Paths task (e.g., entropy over path choices across rollouts, or per-path success rate with standard errors). This would turn an interesting qualitative observation into a convincing result.
4. **Adjust the "entirely in Fourier space" language** in the abstract and Section 2 to reflect that the method alternates between Fourier and real space for non-linearities, consistent with Section 4.2.
5. **For the camera-ready version**, consider adding a brief table showing MSE vs. resolution for the zero-shot super-resolution experiment (to quantify what Fig. 4 shows qualitatively).

## Score and Decision

MY FINAL SCORE: <score>7.5</score>
MY FINAL DECISION: <decision>Accept</decision>