## Summary

This paper proposes Transition-aware weighted Denoising Score Matching (TDSM), the first principled method for training conditional diffusion models under label noise. It proves that the noisy-label conditional score is a convex combination of clean-label conditional scores with instance-wise, time-dependent weights, and derives a modified training objective whose minimizer provably recovers the clean conditional score under an invertible transition matrix. Experiments across MNIST, CIFAR-10/100, and Clothing-1M with synthetic and real label noise show substantial and consistent improvements on conditional generation metrics (CW-FID, CAS, CW-Density, CW-Coverage).

## Strengths

1. **First formal treatment of noisy labels in diffusion models**: Theorem 1 establishes the linear decomposition of noisy-label conditional scores into clean-label conditional scores via transition-aware weights, and Theorem 2 guarantees that the TDSM minimizer recovers the clean conditional score. This is the first work to theoretically and empirically address label noise specifically for diffusion models, going beyond prior GAN-based approaches that rely on simpler class-prior weighting.

2. **Strong and consistent conditional metric gains**: In Table 1, TDSM substantially outperforms the DSM baseline on every conditional metric across all datasets and noise settings. For example, on CIFAR-10 with 40% symmetric noise, CW-FID drops from 30.45 to 15.92 and CAS rises from 47.21% to 62.28%. The improvement grows with noise rate, confirming the method targets the right problem. These gains are not marginal — they are practically meaningful.

3. **Ablation isolating the key contribution**: Table 4 cleanly separates the effect of instance- and time-dependent weights (TDSM) from time/instance-independent transition matrix weighting (**S**-DSM) and from the naive baseline (DSM). TDSM outperforms **S**-DSM on conditional metrics (e.g., CW-FID 15.92 vs. 16.26), confirming that the instance- and time-dependence — the paper's core theoretical insight — is empirically necessary, not just a mathematical curiosity.

4. **Orthogonality to existing label correction methods**: Table 5 shows that TDSM applied on top of corrected labels from VolMinNet or DISC yields further improvement. This demonstrates that TDSM addresses a distinct source of noise (score-matching bias) not handled by classifier-based corrections, and that the two paradigms are complementary.

5. **Real-world validation**: On Clothing-1M (1M images, 61.54% label accuracy), TDSM improves FID from 6.67 to 4.94 and CAS from 46.52% to 47.79%, demonstrating effectiveness beyond synthetic noise settings.

## Weaknesses

### Fatal

None.

### Major

None.

### Minor

1. **Overclaimed unconditional performance in the conclusion**: The conclusion states that TDSM "outperform[s] baseline models in both conditional and unconditional performance." The body text is more careful ("in most cases," line 280), and the data bear this out: unconditional metrics on CIFAR-100 under symmetric noise degrade noticeably (e.g., FID 2.96→4.26 at 20%, 3.36→6.85 at 40%). The same pattern appears on CIFAR-10 FID under symmetric noise (2.00→2.06, 2.07→2.43). This does not weaken the contribution — the paper's strength is in conditional generation, and a trade-off is entirely plausible — but the conclusion should honestly reflect that unconditional improvements are dataset- and setting-dependent, not uniform. The abstract and conclusion should be revised to match the paper's own more measured in-text claims.

2. **Clothing-1M transition matrix estimated from clean subset**: The paper estimates the transition matrix using the 25K clean labeled subset of Clothing-1M (line 353). While the ablation in Table 4 on CIFAR-10 shows that an estimated matrix (via VolMinNet without clean data) works comparably to the true matrix, this experiment is not repeated on Clothing-1M. The reliance on clean data for real-world deployment is a limitation that should be acknowledged and ideally addressed with noise-only estimation results on Clothing-1M.

### Trivial

1. **Gradient flow through non-dominant terms**: Algorithm 1 detach()es gradients for non-dominant weight terms (those below threshold τ) and only backpropagates through the noisy-label class output. The paper mentions this reduces memory but does not discuss whether it could lead to undertraining for rare or hard classes whose weights rarely exceed τ. This is unlikely to be a serious problem given the ablation on τ in the appendix, but a brief discussion would be helpful.

## Nice-to-Haves

- **Comparison with robust-classifier-guided sampling**: A natural alternative is to train a standard conditional diffusion model on noisy labels and use an off-the-shelf noise-robust classifier for classifier guidance at sampling time. This would provide a useful point of reference for understanding whether TDSM's training-side fix is complementary to or supersedes a sampling-side fix. The paper discusses guidance in the appendix but does not compare against this baseline.
- **Analysis of unconditional degradation on CIFAR-100**: The paper could strengthen its own narrative by investigating why unconditional FID degrades more on CIFAR-100 than CIFAR-10 — e.g., whether weight estimation becomes noisier with 100 classes, or whether the convex combination approximation introduces systematic errors in high-class-count settings. A qualitative analysis (e.g., visualizing weight distributions) would deepen understanding of the method's limitations.

## Removed Points

- **Criticism about theoretical guarantees relying on idealized assumptions** (the minimizer uniqueness, sufficient capacity): These are standard idealizations used throughout the score-matching literature and are not specific weaknesses of this paper. The paper appropriately provides practical ablation (Table 4) showing the method works with estimated components. This point applies to essentially every theory-motivated ML paper and is not a meaningful discriminator.
- **Criticism about missing theory on failure modes** (classifier collapse at high noise levels): The paper addresses invertibility (lines 142–143) and provides empirical validation. The requested depth of failure-mode analysis exceeds what is standard for a conference paper of this type.
- **Generic strength from Strength Finder** (e.g., "improvement on clean benchmark datasets" — the paper's Table 2 on clean data is a side finding, not a core contribution, and the critic notes some metrics degrade on clean CIFAR-100 FID, so this strength conflicts with verified weaknesses).

## Novel Insights

The harsh critic's observation that the unconditional–conditional trade-off may be inherent — that shifting the learning objective to prioritize conditional alignment through a weighted convex combination of scores could hurt unconditional distributional fidelity — is a genuinely insightful point that goes beyond what the paper discusses. If correct, it suggests fundamental architectural or objective-level changes may be needed to improve both simultaneously, rather than simply tuning the weighting scheme. The paper would benefit from explicitly engaging with this hypothesis. None beyond the paper's own contributions.

## Suggestions

1. Revise the conclusion and abstract to accurately reflect that conditional metrics improve robustly while unconditional metrics improve in most (but not all) settings, with the largest unconditional degradations occurring on CIFAR-100 symmetric noise.
2. Add a brief discussion of the unconditional–conditional trade-off, including a hypothesis about why CIFAR-100 (100 classes) shows larger unconditional degradation than CIFAR-10 (10 classes).
3. Either replicate the estimated-transition-matrix experiment on Clothing-1M, or clearly state the reliance on clean data as a limitation and discuss when practitioners can and cannot rely on such a subset being available.
4. Include at least one comparison with a robust-classifier-guided sampling baseline in the main paper or appendix to contextualize the complexity/benefit trade-off.

## Score and Decision

MY FINAL SCORE: <pineapple>7.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>