Now I have all the information needed. Let me produce the final consolidated review.

---

## Summary

This paper proposes DOG (Diffusion-based Outlier Generation), a framework that uses a pre-trained text-to-image diffusion model (Stable Diffusion) to generate surrogate near-OOD images from only in-distribution (ID) data for fine-tuning OOD detectors. The key idea is to first capture visual semantics from ID images into pseudo-words via textual inversion (Gal et al., 2022), then use those pseudo-words along with CLIP similarity to select text anchors near the ID boundary, and finally condition the diffusion model on those anchors to synthesize near-OOD images. The detector is then fine-tuned with the generated outliers using a worst-case OOD regret (WOR) loss from Wang et al. (2023). The method shows strong empirical performance on CIFAR-10/100 and ImageNet benchmarks.

## Strengths

1. **Novel use of text-to-image diffusion models for surrogate OOD generation**: DOG generates entire images (not latent features) conditioned on both visual semantics (via textual inversion) and textual class information, producing near-OOD data without requiring external outlier datasets. This directly addresses a key bottleneck in outlier exposure methods — the difficulty of collecting appropriate surrogate data. (Abstract, Section 3.1.1–3.1.2)

2. **Multi-modal conditioning outperforms single-modality alternatives**: The ablation study (Table 2, strategies a–e) systematically shows that combining textual inversion with text-based anchor selection outperforms alternatives using only visual perturbations, only text perturbations, or only synonym-based generation. This provides direct empirical support for the core design choice. (Section 4.3, Table 2)

3. **Strong empirical results across multiple benchmarks**: On CIFAR-10, CIFAR-100, and ImageNet, DOG achieves best or near-best FPR95 and AUROC compared to a comprehensive set of baselines including OE, POEM, VOS, NPOS, and DOE. The gains over standard OE are substantial (e.g., 20.27 FPR95 reduction on CIFAR-100). (Table 1, Section 4.2)

4. **Systematic ablation of hyperparameter M**: The paper analyzes the impact of the number of generated outliers per anchor (M), showing that performance stabilizes when M is approximately equal to or greater than the per-class size of ID data. (Figure 3a–b, Section 4.3)

## Weaknesses

### Fatal
None.

### Major

1. **Unsupported "dynamic adjustment" claim**. The abstract and conclusion state that DOG "enables dynamically adjusting the surrogate outlier data based on the OOD detection results" and "allowing dynamic adjustment of surrogate outlier data based on the results." However, the methodology (Section 3.1–3.2, Algorithm 1) describes a one-pass outlier generation process followed by a fixed fine-tuning phase. There is no iterative loop, no feedback from the detector back to the outlier generator, and no mechanism that revisits generation based on intermediate detection results. The WOR loss perturbs the *model* (θ+αP) but does not regenerate or adjust the *outlier data*. This is a discrepancy between what the paper advertises and what it demonstrates. Removing or honestly qualifying this claim would strengthen the paper. (Abstract, lines 4–5; Conclusion, lines 233–234 vs. Sections 3.1–3.2)

### Minor

2. **Pseudo-word optimization (textual inversion) is underspecified for reproducibility**. Equation (4) defines s_y as an argmin over an expectation involving the diffusion denoising network, but the paper provides no details about: the number of optimization steps, learning rate, whether the pseudo-word is a continuous learnable embedding or a discrete token, the prompt template, how many diffusion timesteps t are sampled, or how many latent samples are drawn per image. The paper cites Gal et al. (2022) but does not state whether it follows that exact protocol or adapts it. Since the downstream candidate selection and outlier generation depend entirely on these pseudo-words, this is a non-trivial gap. (Section 3.1.1, Eq. 4; Section 4.1 experimental details)

3. **WOR loss implementation details are incomplete**. The paper defines the WOR objective (Eqs. 8–10) by citing Wang et al. (2023) and stating that "P is the perturbation introduced by Wang et al. (2023)." It does not specify what form the perturbation P takes (e.g., layer-wise vs. global, structured vs. random), how α is chosen, or how the perturbation is applied during optimization. Algorithm 1's fine-tuning step merely says "Update the network parameters with training objective L(f_θ; D_ID^Train, D_out)" without indicating that this includes the WOR-style perturbation. Since the fine-tuning stage is half the framework, this undermines reproducibility. (Section 3.2, Eqs. 8–10, Algorithm 1)

4. **Experimental protocol clarity is insufficient**. The paper states "We adopt their suggested setups but unify the backbones for fairness" and "We adopt the ASH scoring...in OOD detection," but it does not explicitly state: (a) which baselines were retrained in the same environment vs. numbers quoted from prior work, (b) whether all methods were evaluated using the *same* scoring function (ASH) or each with its originally reported one, and (c) whether the training configurations (learning rates, epochs, data augmentations) were standardized across methods or each used its own original settings. This ambiguity weakens confidence in the reported state-of-the-art claims, especially given the large margins (e.g., 50.93 FPR95 improvement over VOS on CIFAR-100). (Section 4.1 — Baseline Methods and Experimental Details)

### Trivial

5. **Equation (6) notation is ambiguous**. The expression `min_{(x,y)∈D_ID^Train} percentile_η[sim(...)]` is unclear: the min appears to be over (x,y) pairs, but the percentile is then applied — it is not obvious whether the percentile is taken over the similarities *after* the min or whether the min is over the percentile values. The accompanying text partially clarifies the intent, but rewriting the equation would eliminate confusion. (Section 3.1.2, Eq. 6)

6. **Computational cost is not reported**. Generating thousands of images per dataset with Stable Diffusion v1.5 is expensive. The paper does not mention GPU hours, generation time, or memory requirements, making it difficult to assess practical deployability. (Section 4.1)

## Nice-to-Haves

- An analysis of how many anchors survive the second filter (C_λ) for each dataset, and whether any class has zero surviving anchors (which would mean no outliers generated for that class).
- A comparison of visual diversity / plausibility of DOG-generated outliers vs. text-only synonym-generated outliers, beyond T-SNE embeddings.
- An ablation comparing the standard OE loss with the WOR loss to isolate the benefit of the added complexity.
- A discussion of trade-offs between generating whole images (as DOG does) vs. generating outliers in penultimate feature space (as VOS/NPOS do).

## Removed Points

- **"Evaluation metric tables are missing from the parsed text"** — This is a PDF parsing artifact, not an author error. The original submission contains these tables.
- **Strength Finder's point about "Dynamic adjustment capability via worst-case OOD regret"** — This claimed strength conflicts with the verified weakness (Point 1 above). The WOR loss perturbs the model weights, not the outlier data. There is no mechanism to "adapt surrogate outlier data to the current model state." Removed due to conflict with a verified weakness.
- **"The comparison to VOS and NPOS should note that those methods operate on penultimate features"** — This is a discussion point about framing, not a weakness of the paper.
- **Criticism that gains come "simply from having a richer starting point" rather than visual details** — The paper's ablation (strategy e vs. DOG) already controls for this; the paper's interpretation is reasonable.
- **Generic strengths** from the Strength Finder that were generic or superficial were filtered out.

## Novel Insights

None beyond the paper's own contributions. The reviewer inputs did not surface any genuinely novel observation about the paper that goes substantially beyond what the authors themselves state.

## Suggestions

1. Remove or substantially qualify the "dynamic adjustment" claim throughout the paper. Present DOG as a static one-pass outlier generation method, which is still a novel and valuable contribution.
2. Add a reproducibility appendix specifying textual inversion hyperparameters: number of optimization steps, learning rate, pseudo-word embedding type (discrete token vs. continuous vector), prompt template, number of diffusion timesteps sampled per image, and number of latent samples per image.
3. Clarify the WOR implementation: describe what P is (layer-wise noise, adversarial perturbation, etc.), how α is set, and how the perturbed loss is integrated during training.
4. State explicitly: which baselines were retrained vs. quoted, whether ASH scoring was applied uniformly to all methods, and whether training hyperparameters were standardized.
5. Report GPU hours or wall-clock time for outlier generation and fine-tuning.
6. Rewrite Equation (6) to disambiguate the min and percentile operations — e.g., by using clearer notation or additional parentheses.
7. Report the distribution of |C_λ| across classes for each dataset to demonstrate coverage.

## Score and Decision

This paper proposes a creative and timely idea — using text-to-image diffusion models conditioned on both visual pseudo-words and text anchors to generate near-OOD images. The empirical results are strong and the ablation study supports the design choices. However, the paper suffers from an overclaim (the "dynamic adjustment" language), several reproducibility gaps (textual inversion details, WOR implementation), and insufficiently documented experimental protocols. These issues are addressable, but in the current form weaken the contribution. The core idea is genuinely novel and the results are impressive enough that a revised version could be a strong accept.

MY FINAL SCORE: <pineapple>5.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>