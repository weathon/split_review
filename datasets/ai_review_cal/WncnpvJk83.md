- Decision: Accept
- Avg Score: 6.50
- Scores: 6, 6, 8, 6
Now I have all the information I need. Let me synthesize the final review.

## Summary

GMValuator proposes to reframe data valuation for generative models as an efficient similarity-matching problem. The method uses Product Quantization for fast recall of candidate training samples, perceptual similarity metrics (LPIPS/DreamSim) for re-ranking, and MANIQA-based image quality assessment to calibrate contribution scores. It is evaluated on three generative architectures (GAN, β-VAE, Diffusion) across multiple datasets and compared against VAE-TracIn and IF4GAN.

## Strengths

- **First training-free, model-agnostic data valuation method for generative models.** The paper demonstrates GMValuator on GAN, β-VAE, and Diffusion models without requiring retraining, Hessian computation, or model-specific modifications. This is a genuinely novel capability compared to existing methods (VAE-TracIn is VAE-specific, IF4GAN is GAN-specific).

- **Substantial efficiency gains over existing attribution methods.** Table 4 shows GMValuator (No-Rerank) is ~192× faster than VAE-TracIn on MNIST (0.250 s vs. 47.945 s per generated sample) and ~7× faster than IF4GAN for data valuation on noise MNIST (2,137 s vs. 14,543 s). Even the more expensive DreamSim variant is competitive, and the speed-accuracy trade-off is explicitly discussed.

- **Quality calibration addresses a genuine limitation.** The paper identifies that without calibration, low-quality generated images receive the same total contribution scores as high-quality ones (Figure 2). Introducing MANIQA-based weighting (Eq. 5) is a principled response to this issue, absent in prior work.

- **Consistently outperforms baselines on class and attribute alignment tests.** On the identical class test (Table 2), GMValuator (DreamSim) achieves 88.78% vs. 72.00% for VAE-TracIn on MNIST, and 77.94% vs. 6.28% on CIFAR-10. On attribute alignment (Table 3), DreamSim achieves ≥96% on "Hat," ≥95% on "Eyeglasses," and ≥98% on "Gender" for k=5.

## Weaknesses

### Fatal

None.

### Major

- **The evaluation does not establish that perceptual similarity measures causal data contribution.** The paper's central assumption (Sec. 3.1: "similarity between training data and generated data characterizes the contribution of the training data to the generated data") is stated but not validated. Criterion C1 (identical class) and C2 (identical attributes) test whether the method retrieves training samples that *look like* the generated sample — this is a necessary check for any similarity-based method but is nearly tautological given the design: any nearest-neighbor method in a class-discriminative embedding space will satisfy these criteria by construction. A method that measures similarity will naturally retrieve similar-looking images, so C1/C2 verify the similarity matching works, not that similarity equals contribution. The one non-tautological criterion (C3, data cleansing) tests a downstream application but lacks quantitative rigor (see Minor below). The paper would need either (a) data removal experiments that retrain the model after removing top/bottom-ranked contributors and measure degradation in generation quality, or (b) experiments on synthetic data with known contribution structure, to bridge this gap between similarity and causation.

### Minor

- **C3 (data cleansing) evaluation lacks quantitative rigor.** The results (Figure 3) are presented as a scatter plot with no AUC, mean rank, precision@k, error bars, or statistical test. The y-axis label ("ranking of values from high to low") is ambiguous. This makes it difficult to assess the significance of the reported advantage over IF4GAN.

- **No ablation on the quality calibration component.** The MANIQA-based weighting (Eq. 5) is introduced as a key contribution, but the paper never reports results *without* it. The reader cannot assess whether this weighting improves or degrades performance on C1–C4, nor whether the specific functional form (q⸳softmax) is justified over alternatives.

- **No ablation or recall analysis for the Product Quantization recall phase.** The paper does not report recall@k (i.e., what fraction of true top-k nearest neighbors are retrieved by PQ vs. exact search). Without this, the speed-quality trade-off of the PQ step is unquantified, and it is unclear whether the recall phase introduces significant error that the re-ranking phase cannot correct.

- **No details on PQ parameters.** Codebook size, number of subvectors, and other PQ hyperparameters that affect both speed and accuracy are not reported, hindering reproducibility.

- **Hardware table (Table 1) has CPU/GPU labels swapped.** The row labeled "CPU" lists an RTX 3080 GPU, and the row labeled "GPU" lists CPU specifications. This is clearly a formatting inversion.

- **No sensitivity analysis for k (number of top contributors).** The paper uses k = 5/10/15 for C2 and k = 30/50/100 for C1 but does not analyze how the valuation ranking changes with k or what guides the choice of these values.

- **Comparison with VAE-TracIn on CIFAR-10 is uneven.** The paper acknowledges that VAE-TracIn underfits on CIFAR-10 (its 6.28% result vs. 77.94% for GMValuator). While this is disclosed, the CIFAR-10 comparison does not provide a fair assessment of VAE-TracIn's capabilities and inflates the apparent gap between methods.

### Trivial

- Hardware table (Table 1) labels are inverted (CPU ↔ GPU).
- Line 99 contains a commented-out `%Here d is Wasserstein distance` that conflicts with the clear statement on line 139 that Wasserstein distance is not used.

## Nice-to-Haves

- A data removal experiment (remove top-k vs. bottom-k contributors, retrain, measure FID/class-conditional accuracy change) would substantially strengthen the evidence linking similarity scores to actual contribution.
- Reporting recall@k for the PQ recall phase against exact search on a manageable subset would clarify the speed-accuracy trade-off.
- Results with and without MANIQA quality weighting would clarify whether this component is beneficial.

## Removed Points

*These points are flagged to be removed; treat them with caution.*

- **"Wasserstein distance inconsistency" (Harsh Critic, Sec. 3.2).** The critic claims the paper says "Here d is Wasserstein distance" then later contradicts this. The cited text (`%Here d is Wasserstein distance...`) is a LaTeX comment on line 99 and would not appear in the compiled PDF. The paper consistently states on line 139 that Wasserstein distance is not used. This criticism is based on a parser artifact.
- **"The first" claim is too strong.** This is standard academic phrasing; the paper acknowledges concurrent work (LAVA) and the claim is scoped to model-agnostic, training-free methods for generative models, which is supportable.
- **"Missing related works."** As per instructions, I cannot confirm the existence of missing citations.
- **"T-SNE experiment is confusing."** The description is somewhat unclear but the experimental logic (split a class, train on one subset, verify generated data overlaps more with training subset) is conceptually sound.
- **"88% on MNIST should be close to 100%."** This asks why a similarity-based method doesn't achieve perfection; it conflates "imperfect" with "invalid" and does not threaten any core claim.

## Novel Insights

The harsh critic's most valuable observation is that the paper conflates two distinct quantities — perceptual similarity and causal training contribution — and evaluates only the former as evidence of the latter. This exposes a recurring problem in the data valuation literature: methods developed for discriminative models (Shapley value, influence functions) have well-defined causal interpretations (marginal contribution to loss/accuracy), but transferring the "valuation" framing to generative models introduces an ambiguity where "contribution" can mean either "looks like" or "causally caused." The paper would benefit from explicitly acknowledging this distinction and repositioning its contribution as an efficient similarity-based *attribution* method — a practical tool for tracing generations back to similar training samples — rather than a method that measures causal training impact.

## Suggestions

1. Add a data removal experiment (or synthetic-data experiment with known ground-truth contribution structure) to provide evidence linking similarity scores to actual contribution.
2. Add ablation studies for both the quality calibration (with/without MANIQA weighting) and the PQ recall phase (recall@k vs. exact search).
3. Add quantitative metrics (AUC, mean rank, or similar) with error bars to the C3 experiment.
4. Correct the hardware table label inversion and ensure all commented-out LaTeX lines are removed from the camera-ready version.
5. Report PQ hyperparameters (codebook size, number of subvectors) for reproducibility.
