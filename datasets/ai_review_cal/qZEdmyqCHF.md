- Decision: Accept
- Avg Score: 6.00
- Scores: 6, 6, 6, 6, 6
Now I have a thorough understanding of the paper. Let me produce the consolidated review.

## Summary

This paper proposes DeFT, a two-stage finetuning framework for domain-generalizable semantic segmentation. The key idea is to decouple encoder and decoder updates during finetuning to prevent co-adaptation and overfitting to the source domain. In the first stage, the decoder is warmed up with a frozen pretrained encoder. In the second stage, two parallel encoder-decoder pathways are used, each pairing a gradient-updated "usual component" (UC) with a "generalized component" (GC) updated via exponential moving average biased toward initialization. The final model combines the two GCs (EMA encoder + EMA decoder). Experiments on five datasets with two backbone variants show consistent improvements over joint finetuning.

## Strengths

- **Empirical diagnosis of joint finetuning's harm (Figure 1):** The paper directly measures source-domain and target-domain loss trajectories during finetuning, showing that joint finetuning causes the target loss to rise while the source loss drops. This concrete finding motivates the decoupling approach and is a self-contained contribution regardless of absolute performance numbers.

- **Decoupled finetuning with biased EMA demonstrably reduces parameter distance (Eq. 2, Figure 3):** The method is formalized cleanly, and the paper measures L2 norm, MARS norm, and operator norm of parameter changes after training. DeFT consistently yields smaller distances from initialization than joint finetuning, linking the method to well-known generalization bound arguments (Nagarajan & Kolter, 2019; Gouk et al., 2021).

- **Controlled internal ablation (Table 6) shows each component contributes additively:** The paper isolates the contributions of removing the auxiliary encoder loss, data augmentation, decoder warm-up, and the DeFT framework itself — all under the same training pipeline. DeFT adds the largest single gain (e.g., +4.8 mIoU on Cityscapes over the best joint-finetuning variant), providing strong controlled evidence for the method's core claim.

- **Design-choice ablations validate the proposed mechanism (Tables 7, 8):** Table 7 shows that combining both GCs (EMA encoder + EMA decoder) outperforms any configuration involving a UC. Table 8 shows that higher EMA coefficient β (keeping GCs closer to initialization) monotonically improves performance, confirming that the EMA's bias toward initialization is causally beneficial.

- **Orthogonality with explicit distance regularization (Table 3):** DeFT outperforms joint finetuning even when the latter is augmented with an explicit distance penalty, and the two approaches can be combined for further gains. This shows that DeFT's benefit is not simply distance reduction.

## Weaknesses

### Fatal
None.

### Major

- **Uncontrolled SOTA comparison undermines headline performance claims.** Tables 4 and 5 compare DeFT with ten prior methods (IBN-Net, DRPC, WildNet, SHADE, PASTA, etc.) but do not state whether these baselines were re-implemented under the same training conditions (same optimizer, augmentation schedule, learning rate schedule, etc.). The paper only describes DeFT's own training setup. Many prior methods use different training recipes — some include auxiliary losses that DeFT explicitly removes ("We exclude the auxiliary cross-entropy loss... as it degrades OOD generalization capability"), others use different augmentation policies. If the numbers are simply tabulated from original papers, the comparison confounds method improvements with training-pipeline differences. The paper's narrative ("outperformed previous work by large margins") overstates the evidence available from this comparison. **Mitigating factor:** The controlled internal ablation (Table 6) provides the strongest evidence for the method's value and is not affected by this issue. The core claim — that decoupled finetuning improves over joint finetuning — stands on the internal experiments. However, the SOTA framing needs to be caveated or the comparisons need to be properly controlled.

### Minor

- **Missing comparison with single-pathway EMA or weight-averaging baselines.** The paper's related work discusses SWA (Izmailov et al., 2018), Model Soups (Wortsman et al., 2022a), and WiSE-FT (Wortsman et al., 2022b), but never compares DeFT against a baseline that applies EMA or SWA to an ordinary jointly-finetuned model. Such a baseline would isolate whether the improvement comes from the *decoupled two-pathway design* or merely from the EMA/weight-averaging itself, which is known to improve OOD generalization. Table 3 compares against distance regularization but that is not the same as weight averaging. This is the single most informative missing comparison for validating the claimed mechanism.

- **No variance reporting across runs.** The paper reports only point estimates (mIoU) without standard deviations or confidence intervals. Given stochastic elements (random initialization, data augmentation ordering, sampling), single-run results make it impossible to assess whether the reported margins are statistically significant. This is especially relevant for the external comparisons (Tables 4, 5) where margins are 1–3 points for some settings.

- **Limited analysis of what UCs learn versus GCs.** The EMA coefficient β = 0.9999 is extremely high, meaning the GCs remain heavily biased toward initialization throughout the 40K iterations. Table 8 confirms that higher β works better. However, the paper does not analyze what the UCs actually contribute beyond the warm-up initialization, nor how the cross-update interaction between UC and GC drives learning. The mechanism (UC learns domain-specific residuals; GC slowly incorporates them via heavily-biased EMA) is plausible but underspecified. Some trajectory analysis (e.g., per-layer parameter change, gradient norms across pathways) would strengthen the paper's explanation of how DeFT works.

### Trivial
None.

## Nice-to-Haves

- A discussion of the computational cost of maintaining two parallel encoder-decoder pathways (double the memory and compute of standard finetuning) would help practitioners assess the trade-off.
- Re-implementing at least two strong prior methods (e.g., SHADE, PASTA) under the unified pipeline used for Table 6 would convert the uncontrolled external comparison into a fair one and solidify the performance claims.

## Removed Points

These points from the reviewers are flagged to be removed; treat them with caution:

- **"No code is provided / reproducibility concern":** Removed per instruction — the appendix (including code links if any) is stripped by the parser; this is an artifact, not an author omission.
- **"Results with ViT backbones are missing":** Scope creep. The paper clearly specifies DeepLabV3+ with ResNet backbones as its experimental scope. Requesting transformer-based architectures goes beyond the stated scope.
- **"The generalization bound argument is hand-wavy":** The paper explicitly frames §3.4 as "empirical justification" and acknowledges the bound discussion is qualitative. For an empirical paper this is acceptable, and the critic's phrasing overstates the issue. The paper does not claim to derive new bounds.
- **Strength about "State-of-the-art results across multiple domain shifts":** This strength disagrees with the verified weakness about uncontrolled comparison. The results exist as reported, but the strength label ("SOTA") is disputed by the uncontrolled comparison issue, so it is removed from the strengths list.
- **"Computational cost of training two pathways is not discussed":** A valid practical observation but not a weakness in the technical contribution; moved to nice-to-haves.
- **Strength about "The paper addressed an important problem":** Generic/superficial without specific evidence anchor.

## Novel Insights

None beyond the paper's own contributions. The reviewer inputs did not surface a perspective not already present in the paper.

However, one cross-review observation worth noting: **the strong dependence on a near-1.0 EMA coefficient (β=0.9999) together with the short warm-up (2K–8K iterations) suggests that DeFT's GCs are essentially the warm-up model with tiny perturbations.** Table 8 shows that pushing β closer to 1.0 monotonically helps, which raises an interesting question about the optimal stopping point for the EMA trajectory — could the same performance be achieved by simply freezing the warm-up model and only training the UCs? Table 1 shows that freezing entirely hurts (as the critic noted), so the small EMA-driven updates do matter, but the paper does not explore how large these updates need to be or whether a simpler interpolation (like WiSE-FT) at the end of training would suffice. This tension between "GCs barely change" and "GC changes are essential" is the most interesting unresolved question the reviews surface.

## Suggestions

1. Add a controlled baseline: after warm-up, jointly finetune with the exact same pipeline as DeFT but apply EMA (or SWA over the trajectory) to a single model, then evaluate that EMA model. This isolates whether the decoupled two-pathway design matters beyond weight averaging.
2. Re-implement at least 2 prior methods under the paper's exact training pipeline and re-run the comparisons in Tables 4 and 5, or alternatively, add a clear caveat to the SOTA claims stating that comparisons are with published numbers.
3. Report standard deviations over at least 3 random seeds for the main results and key ablations.
4. Add a trajectory analysis (e.g., t-SNE of GC vs. UC weights over time, or per-layer distance from initialization) to clarify what the UCs learn beyond the warm-up initialization.
