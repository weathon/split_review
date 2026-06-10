## Summary

This paper proposes a test-time adaptation (TTA) framework for image denoising. A Gaussian denoiser is first pre-trained self-supervisedly on 50K ImageNet images (σ=25 noise). For each test image, a "pixel bank" is constructed via non-local self-similarity search (32×32 window, 7×7 patches), from which pseudo-instance pairs are randomly sampled for Noise2Noise fine-tuning. The method adapts to out-of-distribution noise (Poisson, real camera noise) in just 10 iterations, achieving strong PSNR results on Kodak24, McMaster18, PolyU, and SIDD benchmarks compared to single-image denoising baselines.

## Strengths

- **Pixel-bank construction generates substantially more and higher-quality training pairs than prior data-construction methods.** Table 3 directly compares fine-tuning the same pre-trained network with Neighbor2Neighbor's 2×2 subsampling, ZS-N2N's downsampling, and the proposed pixel-bank approach. The proposed method shows the strongest resistance to overfitting across iterations and the highest PSNR. This is supported by the design: prior methods sample from at most 4 images (Noise2Fast) or a 2×2 neighborhood, while the pixel bank searches within a 32×32 window using 7×7 patches, yielding C(20²)^(hw) possible pairs.

- **Strong evidence that a Gaussian pre-trained denoiser can be adapted to OOD noise in remarkably few iterations.** Table 1 shows that a σ=25 Gaussian denoiser fine-tuned with ZS-N2N's data construction for only 10 iterations outperforms ZS-N2N trained from scratch for 2000 iterations on both out-of-distribution Gaussian σ=50 and Poisson λ=10,25 noise. This is a non-trivial empirical finding and the primary evidence for the "deep denoising prior" claim.

- **State-of-the-art results on real-world noise among methods that do not train on domain-specific data.** Table 5 reports the best data-free PSNR on PolyU (38.80 dB) and SIDD-Small (36.47 dB), surpassing dataset-based methods (AP-BSN, LG-BPN, SDAP) on PolyU. The pre-trained model was trained only on synthetic Gaussian σ=25 noise, yet adapts to real camera noise in 10 iterations.

- **Dramatically reduced iteration count without sacrificing model capacity.** The method uses a full-capacity 1.26M-parameter network with only 10 fine-tuning iterations, whereas prior single-image methods require 2000+ iterations (ZS-N2N, DIP) and were forced to shrink networks to 2 layers for speed.

## Weaknesses

### Major

- **Misleading "dataset-free" / "single-image" framing creates an unfair comparison structure.** The paper repeatedly positions itself alongside DIP, Self2Self, and ZS-N2N — methods that start from random initialization and use only the test image — under the label "dataset-free" (Section 4.1: "our method can also be regarded as dataset-free") and "single-image denoising methods" (abstract, contribution list, Table 4 caption). However, the proposed method uses a 1.26M-parameter model pre-trained on **50,000 images from ImageNet** under a specific noise distribution (Gaussian σ=25). The three "single-image" baselines it is compared against inherit no such external data. This does not invalidate the method's engineering contributions, but it means every comparison in Tables 4 and 5 must be interpreted with the pre-training advantage in mind. The paper should either (a) ablate the pre-training contribution (e.g., compare pixel-bank TTA starting from random init vs. pre-trained weights) or (b) reframe honestly as "test-time adaptation from a strong pre-trained model" rather than as a single-image/dataset-free method.

- **The core methodological assumption — that noisy patch matching within a W=32 window yields pairs whose clean content is sufficiently close for Noise2Noise to work — is acknowledged but never validated.** The paper states (Section 3.2) that "when the clean content similarity is high... otherwise, significant errors may be introduced," but provides no quantitative analysis of matching quality, no study of how false-match rate varies with noise level (which degrades patch matching), and no characterization of failure cases (e.g., images with low self-similarity). Since the Noise2Noise theory requires independent noisy observations of the *same* clean pixel, the bias introduced by clean-content mismatch is a fundamental concern. The 1+ dB improvements reported could partially reflect the method learning to exploit this bias rather than genuinely denoising better. A simple experiment using clean images with synthetic noise to quantify the match-error distribution would substantially strengthen the paper.

### Minor

- **SS-TTA is discussed in both the introduction and related work as the closest existing TTA denoising method but is absent from every quantitative comparison table.** SS-TTA (Fahim & Boutellier, 2023) is the most directly related method (test-time adaptation for denoising), and its omission from Tables 4 and 5 is a clear gap. Including SS-TTA would clarify the specific advantage of the proposed pixel-bank construction over SS-TTA's Gaussian noise synthesis approach.

- **The claim that Self2Self's success "is largely due to its ensembling strategy, which often results in overly smooth images" (Section 4.2) is stated as fact without quantitative support.** No perceptual metric (SSIM, LPIPS, or similar) is reported for any method, so this judgment cannot be verified from the data presented. PSNR alone can favor smoother outputs regardless of perceptual quality.

- **No hyperparameter ablation study.** The method has five key hyperparameters (W=32, k=7, M=16, p=20, learning rate) with no analysis of sensitivity to these choices. Given that they control the pixel-bank quality, understanding their impact is important for reproducibility and practical use.

- **The conceptual claim of a "deep denoising prior" is presented as a novel insight, but the paper does not cleanly distinguish it from standard transfer learning.** The central claim — "Gaussian denoisers pre-trained on natural images possess a deep denoising prior, which can be quickly adapted through fine-tuning" — describes a form of transfer learning. While the empirical demonstration that a Gaussian denoiser transfers to Poisson and real noise in 10 iterations is valuable and non-obvious, framing it as a distinct conceptual contribution overstates the novelty relative to the evidence presented. An ablation comparing pre-training on denoising vs. pre-training on an unrelated task (e.g., ImageNet classification) would clarify whether the prior is specific to denoising or generic.

### Trivial

- The ZS-N2N critique in the introduction ("ZS-N2N has already minimized the network to two layers, making further reductions impractical") is imprecise: ZS-N2N's limitations stem from its data construction approach, not from the network being too small. A larger network with ZS-N2N's data construction would also overfit.

## Nice-to-Haves

- A computational cost breakdown showing (a) pixel-bank construction time, (b) fine-tuning time per iteration, and (c) inference time separately, so readers can understand where the budget goes.
- Reporting variance or confidence intervals for the main results.
- Visual examples of failure cases where image self-similarity is low (e.g., images with unique, non-repeating structures).

## Removed Points

*These points were flagged by reviewers but removed after verification against the paper content. Treat them with caution.*

1. **"No comparison against the pre-trained model used without any fine-tuning on the test image."** — Removed as factually incorrect. Table 4 explicitly includes "NB2NB (σ unknown)" and "NB2NB (λ unknown)" rows, which are the pre-trained σ=25 model applied directly to out-of-distribution noise without fine-tuning. The raw pre-trained-only numbers are reported alongside the proposed method's gains.

2. **"The claimed connection to plug-and-play priors does not hold up."** — Removed: the paper mentions PnP (Venkatakrishnan et al., 2013; Ryu et al., 2019) only as contextual motivation in the introduction ("we refrain from considering models trained on large-scale image data solely as denoisers; rather, we interpret them as models that encapsulate rich image priors"). The PnP reference is an analogy, not a technical foundation, and the paper does not claim its mechanism operates through PnP-style optimization.

3. **"The method inherits limitations of NB2NB's self-supervised training, limiting absolute performance."** — Removed as speculative. The paper uses NB2NB's architecture for pre-training, which is a standard choice; whether this ceiling is a meaningful limitation is not established.

4. **"No real-noise comparison against dataset-based methods on SIDD."** — Removed: the paper explicitly explains why (Section 4.3: SIDD-Small is a subset of SIDD-Medium, and dataset-based methods were trained on SIDD-Medium). This is a valid methodological justification.

5. **Various formatting/style nitpicks and speculation about appendix content.** — Removed per hard rules.

## Novel Insights

None beyond the paper's own contributions. The reviews surface the key strengths (pixel-bank construction generates superior training pairs; Gaussian denoisers transfer broadly in few iterations) and the key weaknesses (framing mismatch, missing bias analysis), but do not add a fundamentally new perspective that changes how the contribution should be interpreted.

## Suggestions

1. **Reframe the method honestly** as "test-time adaptation from a pre-trained Gaussian denoiser" rather than as "dataset-free" or "single-image denoising." This does not diminish the pixel-bank contribution but removes the most serious weakness.

2. **Add an ablation isolating the pre-training contribution:** compare pixel-bank TTA starting from (a) random initialization, (b) the pre-trained Gaussian σ=25 model, and (c) a model pre-trained on an unrelated task (e.g., ImageNet classification). This would clarify whether the "deep denoising prior" is specific to denoising pre-training or is generic transfer learning.

3. **Quantify pixel-bank matching quality:** using clean images with synthetic noise, measure how often the non-local search finds genuinely similar clean content and how this degrades with noise level. This would bound the bias introduced by clean-content mismatch in the Noise2Noise pairs.

4. **Include SS-TTA in the main comparison tables** to provide a direct TTA baseline.

5. **Add a hyperparameter sensitivity study** for W, k, M, p, and learning rate.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>