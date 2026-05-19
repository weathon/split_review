- Decision: Reject
- Avg Score: 5.25
- Scores: 6, 5, 5, 5
Now let me produce the final review.

## Summary

This paper introduces DiffSDA, a diffusion-based autoencoder for unsupervised sequential disentanglement of static (time-invariant) and dynamic (time-varying) factors in high-resolution video. The model extends diffusion autoencoders to the sequential setting with a probabilistic prior that does not assume independence between static and dynamic factors, and uses an EDM sampler with a latent diffusion front-end for computational efficiency (63 NFEs vs. thousands for DDIM-based approaches). The paper also introduces a new evaluation protocol for real-world sequential disentanglement, including unsupervised swap metrics (AED/AKD), zero-shot cross-dataset tests, and PCA-based multifactor exploration. Results on CelebV-HQ, VoxCeleb, TaiChi-HD, and TIMIT show qualitative and quantitative improvements over VAE-based baselines SPYL and DBSE.

## Strengths

- **Novel dependent prior modeling (Sec. 4.1, Eq. 4)**: Unlike prior VAE-based sequential disentanglement works (Bai et al., 2021; Naiman et al., 2023) that assume independent static and dynamic factors, DiffSDA models them with a joint, dependent distribution. This enables non-autoregressive parallel sampling and avoids the restrictive independence assumption. The design is principled and clearly motivated.
- **Efficient decoder via EDM + LDM (Sec. 4.2)**: The paper adapts the EDM sampling framework to the sequential setting, requiring only 63 network function evaluations during inference (vs. thousands for DDIM-based DiffAEs), and integrates a latent diffusion module (LDM) to process high-resolution video at practical compute. This is a genuine engineering contribution that directly addresses a key bottleneck in applying diffusion autoencoders to video.
- **New real-world evaluation protocol (Sec. 5.1–5.3)**: The paper introduces AED and AKD metrics from the animation domain for unsupervised swap evaluation on real-world data, along with zero-shot cross-dataset evaluation and PCA-based multifactor exploration. These are absent from prior sequential disentanglement benchmarks and represent a useful contribution that could standardize evaluation in this area.
- **Strong qualitative evidence across multiple datasets**: Figure 3 shows DiffSDA producing high-resolution, semantically correct swaps on CelebV-HQ, VoxCeleb, and TaiChi-HD, while SPYL produces visibly blurry outputs and fails to transfer dynamics. Figure 1 (middle) shows compelling zero-shot results where the model trained on VoxCeleb adapts to MUG and even hallucinates plausible body pose details. These qualitative results directly support the claim that the method works on real-world, high-resolution data.
- **Modality-agnostic design validated on audio (Sec. 5.5)**: The model adapts to the TIMIT speech dataset by replacing the U-Net with an MLP, and achieves 42.29% dynamic EER — an 11% improvement over DBSE. This demonstrates generality beyond the video domain.

## Weaknesses

### Fatal
None.

### Major

- **Swap metrics (AED, AKD) are partially confounded with generative quality**: The AED (average Euclidean distance between latent representations) and AKD (average keypoint distance) used for quantitative swap evaluation measure feature-level similarity between a swapped reconstruction and the original. When comparing across methods with very different generative capabilities — DiffSDA produces sharp, high-resolution outputs while SPYL/DBSE produce blurry ones — lower AED/AKD may partly reflect better reconstruction quality rather than better disentanglement. The paper does not include an ablation that controls for the backbone's generative strength (e.g., a sequential DiffAE without the static/dynamic factorization) to separate disentanglement improvements from generation quality improvements. This weakens the quantitative disentanglement comparison, though the qualitative results provide complementary support.

- **Claimed advantage of dependent priors is not empirically validated**: Section 4.1 motivates the dependent static/dynamic prior with three reasons (expressiveness, efficiency, causality), but no ablation study compares this choice against an independent-prior variant. The paper asserts that dependence improves expressivity and enables parallel sampling, yet provides no controlled experiment measuring what the dependence actually buys in practice. This is a notable gap given that the dependent modeling is presented as a core contribution.

### Minor

- **Quantitative results lack variance/confidence intervals**: Tables 1, 2, and 3 report point estimates without error bars, making it impossible to assess whether the observed improvements are statistically significant. This is standard to include for benchmarking results, especially given that some differences (e.g., AED on TaiChi-HD) are small.

### Trivial
None.

## Nice-to-Haves

- An ablation using a non-disentangled diffusion backbone (e.g., a sequential DiffAE with a single shared latent rather than separate static/dynamic factors) would help isolate whether the swap improvements come from the disentanglement mechanism or from the diffusion backbone's superior generation.
- Reporting compute cost (training time, GPU-hours) would help readers assess the practical trade-off between DiffSDA and lighter baselines, given that diffusion models are typically more expensive to train.

## Removed Points

- **"Comparison is fundamentally unfair because baselines are VAE-based and not adapted for high-res"**: This is removed because testing published baselines as-is on standard benchmarks is normal practice across ML. The paper's core claim is that existing methods fail on real-world data while DiffSDA succeeds — showing that gap is the whole point, not an unfair comparison. The confound concern (above) is the valid residue of this criticism and is retained as a Major weakness.
- **"Lacks hyperparameters, training compute, VQ-VAE specifics"**: Removed per the instruction that the parser strips appendix content, and these details are standard for appendix deferral. The paper references App. C for dataset preprocessing details; the original submission likely contains these.
- **"Missing statistical significance"**: Demoted to Minor (it is a real but addressable gap, not a major flaw).

## Novel Insights

The harsh critic usefully identifies a genuine confound in the swap metrics — that AED/AKD measure feature-level similarity between swapped reconstructions and originals, which conflates generative quality with disentanglement. This is a meaningful methodological observation. However, the reviewer overstates its severity: the paper includes reconstruction metrics (Table 2) that independently show the baselines' failure, and the qualitative comparisons (Fig. 3) directly confirm that the baselines produce poor swaps. No genuinely novel insight emerges beyond the interplay between these observations and the paper's own contributions.

## Suggestions

1. **Add a controlled ablation**: Train a sequential DiffAE variant that removes the static/dynamic factorization but retains the same diffusion backbone and sampling procedure. Comparing its swap metrics against DiffSDA would cleanly separate the contribution of the disentanglement mechanism from the contribution of the diffusion backbone.
2. **Add an ablation comparing dependent vs. independent priors**: Since the dependent prior is a claimed advantage over VAE-based work, an experiment showing what degrades when independence is enforced would substantially strengthen the claim.
3. **Report variances or confidence intervals** for the key quantitative metrics (Tables 1, 2, 3) to establish statistical significance.
4. **Clarify how baselines were evaluated**: State explicitly whether SPYL and DBSE were retrained on the new datasets or evaluated using pre-trained checkpoints, and if retrained, under what protocol. This preempts concerns about fairness.
