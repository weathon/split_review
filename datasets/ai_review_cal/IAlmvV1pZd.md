- Decision: Reject
- Avg Score: 3.50
- Scores: 3, 5, 3, 3
Now I have a thorough understanding of the paper and can verify claims against the actual text. Let me produce the consolidated review.

## Summary

L-MBOP-E proposes two innovations for model-based offline planning: (1) a latent dynamics model (encoder-decoder + dynamics) trained jointly to reduce compounding errors from limited offline data, and (2) a Thompson Sampling mechanism that selects between the behavior-cloned (BC) policy and an extrinsic policy during MPC rollouts, aiming to avoid overly conservative planning. Experiments on D4RL and DMC tasks compare against MBOP and MOPP.

## Strengths

- **Latent dynamics model benefit is isolated and validated.** The ablation (Section 5.2) compares L-MBOP (latent model, no extrinsic policy) against standard MBOP on the hopper-medium task. This is a clean, fair comparison that controls for the extrinsic policy variable, and the paper reports that L-MBOP substantially outperforms MBOP. Figure 2b further shows L-MBOP-E with 50k samples outperforming MBOP with 1M samples, demonstrating improved data efficiency.

- **Thompson Sampling mechanism is shown to correctly identify the better policy.** Figure 3a systematically varies dataset quality (random, medium, medium-expert) and extrinsic policy quality, and reports the converged Thompson Sampling probability p_t. On random datasets where the BC policy is poor, p_t converges near 0 (favoring the extrinsic policy); on high-quality datasets with a poor extrinsic policy, p_t converges near 1 (favoring BC). This directly validates that the mechanism works as intended. The comparison L-MBOP-E vs L-MBOP (both with the same latent model, differing only in whether the extrinsic policy + Thompson Sampling is used) further isolates this benefit.

- **Comprehensive ablations.** The paper systematically varies latent dimension size (Figure 2a, dimension 3–19), dataset size (Figure 2b, 20k–1M), extrinsic policy quality (Figure 3b, low to expert), and the variance scaling factor σ_M (Figure 3c, 0.2–2.0). These ablations provide evidence that the design choices matter and that performance is reasonably robust to hyperparameter settings.

- **Transparency about the extrinsic policy.** The paper explicitly states in Section 5.1: "For convenience, the extrinsic policy is obtained as a variant by training a policy using SAC on the same task until it performs reasonably well as the BC policy." It also discusses (in the abstract and Section 4) that in practice the extrinsic policy could come from meta-learning or a related task. This transparency allows readers to assess the limitation rather than conceal it.

## Weaknesses

### Fatal
None.

### Major

- **The main comparison (L-MBOP-E vs MBOP/MOPP) is not apples-to-apples, undermining the "state-of-the-art" claim for the full system.**  
  The L-MBOP-E results in Table 1 use an extrinsic policy trained via SAC on the *same task* through online interaction (Section 5.1: "training a policy using SAC on the same task"). Neither MBOP nor MOPP has access to any such online-trained policy. While the paper frames this as "for convenience" and discusses offline-available alternatives (meta-learning, related task), the experiments never test those alternatives — they rely on a same-task online oracle. This means the headline improvements in Table 1 may partly reflect the quality of the extra policy rather than the latent model or Thompson Sampling mechanism. The paper's claim of "significantly outperforming state-of-the-art model-based offline planning algorithms" is therefore not properly supported by the evidence presented for the full system.  
  **Crucially, this does NOT invalidate the controlled ablations** (L-MBOP vs MBOP, L-MBOP-E vs L-MBOP), which are fair and support the individual contributions.

### Minor

- **The paper does not specify how \(Q_c\) is obtained.** Algorithm 1 (line 156–157) uses \(Q_c(z_H,a)\) to compute the terminal value \(V_c\) for rollouts that follow the extrinsic policy, but nowhere does the paper explain how \(Q_c\) is learned — whether from offline data (which may poorly estimate returns for the extrinsic policy's OOD actions) or from the extrinsic policy's own online experience (which would further break the offline framing). This is a missing implementation detail that affects reproducibility and interpretation.

- **Zero-shot adaptation claims are partially overstated.** The paper presents "zero-shot task adaptation" (Section 5.3) but the strongest results come from the New-Q variant, which retrains the Q-function on the new reward — this is not zero-shot. The New-Reward variant (genuinely zero-shot, no retraining) does show improvement over MBOP, which is legitimate, but the paper does not control for whether MBOP could also simply replace the reward function in its model rollouts. Without that controlled comparison, the zero-shot advantage over MBOP is not cleanly attributable to L-MBOP-E's design.

- **Thompson Sampling operates on model-predicted returns, but the reliability of these estimates is not directly analyzed.** The policy selection mechanism depends on cumulative returns from rollouts in the learned latent model. The paper provides indirect evidence that it works correctly (Figure 3a, showing convergence to the right policy), but does not analyze the correlation between model-predicted and true-environment returns for the two policies, especially in OOD regions where model error could be higher. A direct analysis would strengthen the claim that the mechanism is reliable.

- **The ablation comparing MBOP to L-MBOP does not control for model capacity.** The latent model uses an encoder-decoder architecture that may have more parameters than the standard dynamics model used by MBOP. The paper does not discuss whether the improvement could partially stem from increased model capacity rather than the latent representation itself.

### Trivial
None.

## Nice-to-Haves

- Report results with standard deviations over multiple seeds. Offline RL results can be high-variance, and many papers in this area report multi-seed statistics.
- Show that MBOP with the same reward replacement cannot achieve the same zero-shot improvement, to isolate the benefit of L-MBOP-E's latent model.
- Analyze the correlation between model-predicted rollout returns and true environment returns for both policies, to directly validate the Thompson Sampling signal.

## Removed Points

- **"Any improvement could trivially come from the online-trained policy itself" (Harsh Critic).** This characterization is too strong because the controlled ablation L-MBOP (no extrinsic policy) vs MBOP isolates the latent model contribution on fair terms. The unfairness only applies to the full-system comparison. The point is retained in the Major weakness above but without the "trivial" framing.  
- **"Without standard deviations, the reliability of these gains is uncertain" — REMOVED as generic.** Many offline RL papers report single-run normalized scores on established benchmarks; this is community-standard practice and not a specific flaw of this paper. Moved to Nice-to-Haves.  
- **"The zero-shot section overstates the contribution of L-MBOP-E" — REFRAMED.** The paper does present New-Reward as the zero-shot variant and New-Q as an additional improvement. The overstatement is limited to the uncontrolled MBOP comparison and the "zero-shot" label for New-Q, which are already captured as Minor weaknesses.  
- **Strength Finder: "Consistent state-of-the-art results across diverse tasks" — WEAKENED.** The strength finder reports this without noting the fairness issue. The controlled ablations are valid; the full-system SOTA claim is not. The strength is retained but qualified in the review.  
- **Strength Finder: "Zero-shot task adaptation is demonstrated" — QUALIFIED.** The evidence is partial; the weakness about uncontrolled comparison and New-Q not being zero-shot is noted.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. **Redesign the main experimental comparison.** Either replace the same-task SAC policy with a genuinely offline-compatible extrinsic policy (e.g., trained on a different task's offline data, or via meta-learning from multiple datasets) and compare against baselines that also have access to that same auxiliary data, or restructure the claims so that the "state-of-the-art" label applies only to the L-MBOP variant (latent model alone) with the full L-MBOP-E presented as a method that assumes availability of an additional policy.
2. **Clarify how \(Q_c\) is learned.** State explicitly whether it is trained on offline data, online data from the extrinsic policy's experience, or some other source. If it is trained on offline data, discuss whether the value estimates are reliable for the extrinsic policy's OOD actions, and provide supporting analysis.
3. **In the zero-shot experiment**, include a variant of MBOP that also replaces the reward function in its model rollouts (and optionally retrains its Q-function on the new reward). This would isolate whether the benefit comes from the model-based planning framework generally or from L-MBOP-E's specific design choices.
