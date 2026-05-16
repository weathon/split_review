Now I have a thorough understanding of the paper. Let me produce the final consolidated review.

## Summary
The paper applies discrete diffusion models (D3PMs) to non-deterministic semantic segmentation tasks. It unifies medical image ambiguity segmentation (LIDC tumor dataset) and future prediction (car simulator, Cityscapes) under a single generative framework. The key technical contributions are (1) adapting D3PMs for segmentation by embedding discrete labels and concatenating conditioning inputs into the U-Net, and (2) an auto-regressive diffusion scheme that uses predicted segmentations as inputs for multi-step future forecasting. Experiments across all three tasks show consistent gains over a matched deterministic architecture and competitive or superior performance against domain-specific methods (Hierarchical Probabilistic U-Net on LIDC, VQ-VAE+Transformer on the simulator, Lin et al. on Cityscapes).

## Strengths
1. **First application of discrete diffusion to uncertainty modeling in semantic segmentation** — The paper correctly identifies that prior work on ambiguous segmentation uses either VAEs (Kohl et al., 2019; Baumgartner et al., 2019) or continuous diffusion (Rahman et al., 2023). Adapting D3PMs to this setting, with its natural fit to discrete segmentation masks, is a genuine novelty (abstract, §1, §2).

2. **Auto-regressive diffusion framework for future forecasting** — The paper introduces a scheme (§3.3) that rolls out multi-step predictions using only previous segmentation maps as conditioning, enabling mid-term forecasting (t+9 on Cityscapes). While Chen et al. (2022a) used auto-regressive discrete diffusion for panoptic segmentation, this present work targets ambiguous future prediction, which is a distinct and meaningful extension.

3. **Consistent empirical improvement over deterministic baselines** — Across all three tasks, the diffusion model outperforms an architecture-matched deterministic model. The car simulator results are particularly striking: FDE 0.25 vs 3.48, miss rate 0.7% vs 52% (Table 2). This cleanly demonstrates that generative modeling is necessary for these ambiguous tasks.

4. **Motivating toy example clearly isolates the failure of deterministic models** — The rectangle world dataset (§3.4, Figure 2) shows in a controlled setting that a deterministic model collapses to only half the categories while the diffusion model captures all four equally-probable modes. This concisely validates the paper's core motivation.

5. **Computational efficiency** — The diffusion model uses only 10 diffusion steps and is ≈5× faster per sample than the Transformer baseline (9.2ms vs 49.1ms on V100, Table 2) on the car simulator, while achieving better accuracy.

## Weaknesses

### Fatal
None.

### Major
1. **Best-of-N evaluation creates an asymmetric comparison.** On the car simulator (§4.2.2), the diffusion model selects the trajectory with the lowest FDE out of 10 samples, while the deterministic model is allowed only a single output. On Cityscapes (§4.3.2), the diffusion model's mIoU is the best over N samples (1, 10, 100). This inflates the generative model's reported performance relative to deterministic competitors—the metric partly measures coverage rather than average sample quality. The paper provides motivation for this choice (capturing the true scenario from multiple possibilities, §4.3.2), and it does report 1-sample results on Cityscapes (Table 3), which is helpful. However, on the simulator, no average-sample metric is reported at all. The claim that the diffusion model "performs best" on the simulator (Table 2 caption) is partly driven by this asymmetry, since the main fair comparison is between the two generative models (diffusion and Transformer), both of which benefit from multiple samples.

2. **No comparison to simpler generative models (VAE, continuous diffusion) on any task.** The paper's framing implies that the *discrete diffusion* framework specifically brings value, yet no experiment isolates this. On the rectangle world (§3.4), a VAE or continuous diffusion model would likely also capture multiple modes. On LIDC, the paper compares to HPU (a VAE) but not to the more directly comparable continuous diffusion method of Rahman et al. (2023), which the paper cites. Without such baselines, the evidence supports the weaker claim that *stochastic sampling helps* —which any generative model could provide—rather than the claimed contribution that *discrete diffusion* is the right framework.

3. **No ablation on the number of diffusion steps.** The paper uses only T=10 steps for all experiments and states that "more steps did not bring significant quality improvements" (§4) without showing any supporting data. Standard D3PMs often benefit from more steps, and T=10 is unusually low. Without an ablation (e.g., T=1, 5, 10, 50, 100 on LIDC validation), it is plausible that the model's performance is dominated by the conditioning architecture rather than the diffusion denoising process. If T=1 performed similarly, the paper's framing as a diffusion model would be misleading.

### Minor
1. **The car simulator has very structured, low-variance uncertainty.** Each car has at most 4 possible routes, determined by intersection geometry (§4.2.1). The paper claims this "clearly showcase[s] the ability… to handle complex distributions," but the distribution is a small discrete set. Real-world future prediction involves continuous, high-dimensional uncertainty (positions, interactions). The simulator is informative as a controlled test but the paper should be more measured in extrapolating from it.

2. **No statistical significance reported for LIDC results.** The improvement over HPU on the full test set is 1% (Table 1). Without confidence intervals or significance testing, it is unclear whether this difference is meaningful, especially since the deterministic model already matches HPU on subset B.

3. **Conditioning architecture details are underspecified.** Section 3.3 says segmentation maps are "project[ed] into a continuous vector space of dimension E with an embedding layer" without specifying whether this is a learned lookup table or linear projection, or what E is. The specific number of previous frames used as conditioning is given in §4.3.1 for Cityscapes, but the general description in §3.3 is vague. These details matter for reproducibility.

4. **The only future direction discussed (§5) is forcing diversity in sampling.** Important limitations such as the information loss from using segmentation-only inputs, the computational cost of multi-sample inference, and the lack of temporal consistency in the auto-regressive scheme are not discussed.

### Trivial
None.

## Nice-to-Haves
- An ensemble comparison: train N deterministic models and take the best prediction, to isolate whether stochastic sampling is the key advantage over deterministic single-shot inference.
- Reporting average sample performance (mean FDE/mIoU across samples) alongside best-of-N on the simulator and Cityscapes for full transparency.
- A VAE baseline on the rectangle world to confirm that the discrete diffusion framework specifically, rather than generative modeling in general, provides the benefit.

## Removed Points
These points are flagged to be removed; treat them with caution.
- **"The contribution is incremental / novelty overstated"** — The critic claims the method is a "textbook recap of D3PM." While §3.1 reviews standard D3PM background (which is standard practice), the actual adaptation in §3.3 (embedding discrete labels, conditioning via concatenation, softmax output) and the auto-regursive scheme constitute a genuine application-level contribution. The paper clearly delineates its novelty in §1 and §2; it does not claim algorithmic innovation beyond the application to uncertain segmentation.
- **"Conflates aleatoric and epistemic uncertainty"** — The paper intentionally treats both as instances of non-deterministic prediction where a single output is insufficient. The method models the posterior distribution regardless of the uncertainty's source, so this distinction is not needed for the paper's claims.
- **"Binary deterministic transition rules" on simulator make it "not very informative"** — The simulator is one of three experiments. The paper also evaluates on real-world Cityscapes. The simulator is a controlled diagnostic test; the paper does not claim it alone proves real-world applicability.
- **"§3.3 underspecified: how is noisy segmentation embedded?"** — The paper says "embedding layer," which is standard terminology for a learnable lookup table. The specific conditioning configurations are described in §4.3.1 (e.g., {S_{t-6}, S_{t-3}, S_{t}}). The level of specification is typical for a conference paper.
- **"Missing baselines on LIDC (Baumgartner et al., Bhat et al., Rahman et al.)"** — The paper compares to the SOTA HPU (Table 1) and outperforms it. Adding every follow-up VAE baseline would strengthen but is not required to support the paper's claims. The paper does cite these works in §2.
- **"The paper should also cover Y / additional tasks"** — These are scope-creep demands outside the paper's stated goals.
- **"§4.1.2: deterministic model matches HPU on subset B, interesting but not discussed"** — The paper does discuss this: "This suggests that the HPU does not generate enough variations that properly cover the predictions of the physicians" (§4.1.2). The discussion is present and reasonable.
- **"Reproducibility requires more detail (hyperparameters)"** — Implementation details (learning rate, batch size, optimizer, noise schedule parameters) are standard content for the appendix, which the parser strips from these submissions.

## Novel Insights
None beyond the paper's own contributions.

## Suggestions
1. Add an ablation study varying the number of diffusion steps (T=1, 5, 10, 50, 100) on at least the LIDC validation set, reporting mIoU and generation time. This would directly address the concern that the model may not be leveraging the diffusion process.
2. On the car simulator, report the mean FDE across all 10 samples (not just the lowest) alongside the best-of-N metric. This gives a complete picture of distribution quality vs. coverage.
3. Add a continuous diffusion baseline (e.g., Rahman et al. 2023's method) on LIDC to show whether discrete diffusion provides specific advantages over continuous diffusion for segmentation ambiguity.
4. Disclose the embedding dimension E, and clarify whether the embedding layer is a learned lookup table or a linear projection.

## Score and Decision

This paper tackles a well-motivated problem and demonstrates that discrete diffusion models can effectively capture uncertainty in segmentation tasks across diverse domains (medical, autonomous driving). The experiments are multi-faceted and consistently show that generative modeling beats deterministic prediction. However, two structural issues (asymmetric best-of-N evaluation, no comparison to simpler generative models, and no ablation on diffusion steps) weaken the core claim that *discrete diffusion specifically* provides the benefit, as opposed to stochastic sampling generically. The evaluation is otherwise solid and the writing is clear. These issues are addressable in revision but reduce the strength of the contribution as presented.

MY FINAL SCORE: <pineapple>5.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>