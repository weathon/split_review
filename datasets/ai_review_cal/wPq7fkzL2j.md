- Decision: Reject
- Avg Score: 4.50
- Scores: 5, 5, 3, 5
Now I have a thorough understanding of the paper and the reviewer claims. Let me produce the consolidated review.

## Summary

This paper introduces Self-Paced Augmentations (SPAug), a method that dynamically adjusts the augmentation intensity per training sample based on its current loss value. For each sample, SPAug blends the original and augmented images with a sample-specific coefficient *mᵢ* (controlled by binary, polynomial, or learnable mapping functions from the loss). The method requires only a few lines of code on top of any uniform augmentation policy. Experiments on CIFAR-10/100-C and ImageNet-C with AugMix, AutoAugment, and RandomAugment show consistent improvement in corrupted error (0.5–1.8% absolute) while maintaining clean accuracy. A toy experiment (Table 1) cleanly demonstrates why per-sample adaptation is beneficial.

## Strengths

- **Minimal integration overhead, concretely demonstrated**: The paper shows that SPAug with the binary mapping function adds only 5 lines of code to existing training loops (Algorithm 1, Section 3.2). This is a verifiable and practical advantage over prior adaptive methods requiring separate policy networks or meta-learning loops.

- **Consistent corrupted-error gains without clean accuracy degradation**: Across three augmentation policies (AugMix, AutoAugment, RandomAugment), two CIFAR architectures (WRN-40-2, WRN-28-10), and ImageNet (ResNet-50), SPAug-Learnable consistently reduces corrupted error while keeping clean error essentially unchanged. For example, on CIFAR-100-C with AugMix+JSD (WRN-28-10), corrupted error drops from 8.7% to 7.0% with identical clean accuracy (Table 2). On ImageNet-C (ResNet-50), C-Err drops from 74.35% to 72.54% with equal clean error (23.1%) (Table 3).

- **Compelling toy experiment validates the core intuition**: Table 1 shows a smooth U-shaped curve where intermediate threshold τ (0.1–0.2) outperforms both τ=0 (no augmentation) and τ=∞ (uniform augmentation) on CIFAR-100, with up to 3.5% absolute improvement in corrupted error. This directly supports the claim that per-sample loss-based intensity adaptation is beneficial.

- **Scalability demonstrated on ImageNet**: Table 3 provides ImageNet-scale results (270 epochs, ResNet-50), showing that the method works beyond small-scale benchmarks without added complexity.

- **Visualization of per-sample adaptation dynamics**: Figures 4 and 5 illustrate how augmentation intensity varies across easy/medium/hard samples over the course of training, making the mechanism transparent and interpretable.

## Weaknesses

### Fatal
None.

### Major

1. **No experimental comparison against prior adaptive augmentation methods (AdaAug, MetaAugment) — structural gap**.  
   Section 2.2 discusses AdaAug (Cheung & Yeung, 2021) and MetaAugment (Zhou et al., 2021), both of which adjust augmentation per sample/class and are positioned as more complex alternatives. The paper claims SPAug is simpler with "little to no computational overhead" and easier integration. Yet **no experimental comparison** against these methods is provided on any benchmark (CIFAR-C, ImageNet-C). Without this comparison, the novelty claim is uncalibrated: it is impossible to tell whether SPAug advances the state of the art or simply matches prior adaptive methods with a different mechanism. This is the single most important gap and substantially weakens the paper's empirical contribution.

2. **Overclaimed scope: Adversarial Training results are promised but absent**.  
   The introduction (Section 1) and experimental setup (Section 4.1) explicitly list "Adversarial Training" as one of the base policies SPAug is integrated with and tested on. However, no adversarial training results appear anywhere in the paper — Sections 4.3–4.5 cover only AugMix, AutoAugment, and RandomAugment. This is a clear mismatch between the stated experimental scope and the evidence provided. The claim of broad applicability is partially unsupported.

### Minor

3. **Learnable SPAug formulation (Eq. 4) is insufficiently motivated and uses a non-differentiable Sign term**.  
   The regularization loss in Equation (4) includes a `Sign` function, making the objective non-smooth in *mᵢ*. The paper does not analyze whether this causes gradient oscillations or dependence on batch composition. The description of the two-case optimization ("easy" vs. "hard") effectively recreates a binary decision, undercutting the claimed advantage of continuous learnable parameters. The paper would benefit from either a smooth alternative or an ablation showing that the sign-based update is more effective than a simpler continuous regularizer.

4. **No ablation on the polynomial exponent *t* or analysis of τ sensitivity in main experiments**.  
   The toy experiment (Table 1) does ablate τ for binary SPAug, which is commendable. However, the polynomial mapping function (Eq. 3) has an additional hyperparameter *t* (shape parameter) that is never ablated or discussed. The threshold τ is also not varied in the main AugMix/AutoAugment experiments. Understanding the sensitivity of these hyperparameters is important for practical adoption.

5. **Computational overhead is claimed but not quantified**.  
   The paper repeatedly states SPAug has "negligible" or "little to no computational overhead" but provides no wall-clock time measurements, GPU memory figures, or throughput comparisons. A concrete measurement would support the practical-utility claim.

### Trivial
None.

## Nice-to-Haves

- A brief limitations paragraph discussing cases where loss might not be a reliable easiness proxy (e.g., very small datasets, noisy labels, regression tasks) would improve intellectual honesty.
- The paper could explicitly state that per-sample *mᵢ* storage (e.g., ~5 MB for ImageNet) is negligible — this is currently implicit.

## Removed Points

- **Lack of error bars in tables (harsh critic point #2)**: The experimental setup (Section 4.1) states "All experiments are repeated three times, and average classification error and standard deviation are reported." Table 3 visibly shows ±0.1. The remaining tables (1, 2, 4, 5) are embedded images in the extracted text and cannot be fully verified from this rendering; the critic's claim about their absence cannot be confirmed or refuted from the available material. This point is moved here rather than retained as a standalone weakness, because the paper explicitly claims to report standard deviations, and a proper verification would require viewing the original PDF images.
- **Strength about "Compatibility with diverse augmentation policies" including Adversarial Training**: This claimed strength is partially invalid because adversarial training results are absent. The strength holds for AugMix, AutoAugment, and RandomAugment, but the adversarial training component is dropped.
- **"Memory and speed overhead" mention by harsh critic as missing part**: This is already covered as weakness #5 above.
- **Criticism about "pure formatting/style nitpicks"**: The harsh critic mentions presentation issues but these are generic and not concretely anchored, so removed per instructions.
- **Strength Finder's generic or unsupported strengths**: All retained strengths are concrete and evidence-backed. Generic strengths (e.g., "this paper addresses an important problem") are dropped.

## Novel Insights

None beyond the paper's own contributions. The reviews raise the important point that the paper's positioning against prior adaptive methods is aspirational rather than empirically grounded, but this is an observation about a gap, not a synthesis that transcends what the paper says.

## Suggestions

1. **(Required) Add experimental comparison against AdaAug and MetaAugment on CIFAR-10/100-C and ImageNet-C** using matching architectures (WRN-28-10, ResNet-50). This is essential to validate the contribution and support the claims of simplicity and effectiveness.
2. **(Required) Either include the Adversarial Training results promised in the introduction and Section 4.1, or remove those claims from the scope.** A small-scale experiment (e.g., PGD-AT on CIFAR-10 with SPAug) would suffice.
3. **(Recommended) Clarify the learnable formulation in Section 3.2**: either replace the non-differentiable `Sign` term with a smooth alternative (e.g., λ·σ(mᵢ) for easy samples and −λ·σ(mᵢ) for hard samples, defined via batch threshold) or provide an ablation showing the current formulation does not cause optimization instability.
4. **(Recommended) Add an ablation on the polynomial exponent *t* and show sensitivity of τ** for at least one main experiment (e.g., CIFAR-100 with AugMix).
5. **(Nice-to-have) Report wall-clock training time or throughput** for SPAug vs. uniform baselines to substantiate the "negligible overhead" claim.
