Now I have a thorough understanding of the paper and all claims. Let me compose the final consolidated review.

## Summary

This paper proposes DOG (Diffusion-based Outlier Generation), a framework that uses a pre-trained text-to-image diffusion model (Stable Diffusion v1.5) to synthesize surrogate near-OOD outliers from ID data alone. DOG first captures visual semantics via textual inversion to obtain pseudo-words per class, then selects near-OOD textual anchors from WordNet using CLIP similarity, generates images conditioned on these anchors, and fine-tunes the OOD detector with a worst-case OOD regret (WOR) loss. The paper evaluates on CIFAR-10, CIFAR-100, and ImageNet benchmarks.

## Strengths

- **Novel pipeline combining visual and textual modalities for OOD outlier generation**: DOG uses textual inversion to extract visual semantics from ID images and then selects near-OOD text anchors from WordNet, generating synthetic outliers that are closer to the ID boundary. The ablation study (Table 2) confirms that the full method outperforms four alternative diffusion-based synthesis strategies, as well as the synonyms-only variant. This directly supports the claim that combining visual and textual information is crucial for effective surrogate outlier generation.

- **Large performance gains over OE and prior generation-based methods without external OOD data**: On CIFAR-100, DOG reduces average FPR95 by 20.27 compared to conventional OE (Section 4.2). Compared to prior generation methods VOS and NPOS, DOG shows improvements of 50.93 and 27.70 in FPR95. These results are obtained without requiring any external surrogate OOD dataset, addressing a key practical challenge in outlier exposure.

- **Interpretable synthesis through text-space anchor selection**: By transforming outlier generation into text space via CLIP and WordNet, DOG provides a more transparent synthesis process than black-box latent-space sampling used by prior methods. The candidate word selection and filtering steps make the generation process amenable to human analysis.

## Weaknesses

### Fatal
None.

### Major

1. **SOTA claim is potentially contradicted by the paper's own results**: The paper repeatedly claims "state-of-the-art performance" (abstract, Section 1 contributions, Section 4.2). However, DOE (Wang et al., 2023) is included as a baseline in Table 1, and the reviewer reports specific numbers from the table showing DOE outperforms DOG on both CIFAR-10 (FPR95 18.19 vs. 19.89) and CIFAR-100 (FPR95 50.58 vs. 56.26). While the table is embedded as an image and cannot be directly verified from the parsed text, it is notable that the paper's results discussion in Section 4.2 systematically avoids any direct comparison with DOE — it compares DOG against OE, POEM, VOS, and NPOS, but never mentions DOE in the analysis. This selective reporting is problematic regardless of the exact numbers. The authors should either (a) acknowledge where DOE outperforms DOG and contextualize the comparison, or (b) provide justification (e.g., different backbone, experimental conditions) for claiming SOTA over DOE.

2. **Unsubstantiated "dynamic adjustment" claim**: The abstract states that DOG "presents a novel approach for outlier exposure by allowing dynamic adjustment of surrogate outlier data based on the results," and the conclusion repeats this claim. However, the paper never demonstrates any form of dynamic or iterative adjustment — the outlier generation uses fixed hyperparameters (K=1000, η=0.05, λ not even specified, M fixed per dataset), and there is no loop, feedback mechanism, or adaptation based on detection outcomes. This is a clear overclaim that should be removed or supported with experiments.

3. **Missing critical hyperparameter λ, hurting reproducibility**: The anchor filtering step (Eq. 6) depends on a threshold λ that is never specified. The paper states hyperparameters are "selected based on the validation set according to OOD detection performance" (Section 4.1), but does not report the chosen λ value, the range searched, or its sensitivity. Without this, the method cannot be reproduced, and the robustness of the filtering step cannot be assessed. Other details are also missing: the textual inversion optimization (number of steps, learning rate, prompt template) is not specified, the perturbation P and magnitude α for the WOR loss (Eq. 9-10) are referenced only by "following Wang et al. (2023)" without local specification, and the criteria for selecting the K=1000 candidate words from WordNet are not described.

### Minor

4. **No quantitative analysis that generated outliers are genuinely "near-OOD"**: The paper's central motivation is that DOG generates near-OOD data close to ID boundaries. The only support is a t-SNE visualization (Figure 3c), which is purely qualitative. No quantitative metric is provided (e.g., distance to ID centroids in feature space, likelihood under ID density, or comparison of distances across generation strategies). The ablation study shows DOG outperforms other strategies, but this does not isolate the "near-OOD" property as the causal factor. A quantitative analysis would substantially strengthen the claimed insight.

5. **ASH scoring conflates the contribution of outlier generation vs. scoring function**: DOG uses ASH (a strong post-hoc scoring method) for OOD detection, while baselines are evaluated with "their suggested setups" (Section 4.1). This means the comparison in Table 1 mixes the effect of DOG's generated outliers with the effect of using ASH. An ablation experiment using the same scoring function (e.g., MSP or Energy) for all methods would clarify how much performance comes from the generated outliers vs. the scorer. This does not invalidate the results, but it makes the source of improvement less clear than it should be.

6. **Ablation differences are small and statistical significance is unreported**: In the ablation study (Table 2), strategy (e) (synonyms only) performs very close to the full DOG method — on CIFAR-10, FPR95 of 20.13 vs. 19.89; on CIFAR-100, 54.72 vs. 56.26 (synonyms actually better). The paper claims DOG "achieves better results than all the above strategies" but the differences are marginal and no statistical significance tests or multiple-run error bars are reported for any experiment, including the main Table 1.

7. **No discussion of limitations or computational cost**: The paper does not discuss any limitations — the dependence on Stable Diffusion v1.5, computational cost (GPU hours for textual inversion, image generation, and fine-tuning), potential biases from WordNet, or sensitivity to the choice of η and the percentile filtering. This omission makes it harder to assess practical applicability.

### Trivial
None.

## Nice-to-Haves

- **Scoring-controlled ablation**: Re-run the main evaluation with a single common scoring function (e.g., Energy or MSP) for all methods, including DOG, to isolate the contribution of generated outliers.
- **Direct comparison with DOE using ASH**: Since DOE is the closest competitor, evaluating DOE with ASH as well would show whether DOG's advantage (if any) holds under the same scoring.
- **Quantitative near-OOD analysis**: Measure feature-space distances between generated outliers and ID data across generation strategies.
- **Hyperparameter sensitivity analysis**: Report how λ, η, K, and M affect OOD detection performance.
- **Runtime/cost reporting**: Provide GPU hours for each stage (textual inversion, image generation, fine-tuning).

## Removed Points

- **"Unfair baseline comparisons — VOS/NPOS are post-hoc methods"**: The reviewer claims VOS and NPOS are post-hoc methods. This is factually incorrect. VOS (Du et al., 2022) generates virtual outliers in feature space and uses them to train the classifier with an energy-based loss. NPOS (Tao et al., 2023) uses normalizing flows to generate outliers and fine-tunes the model. Both involve training/adaptation and are appropriately classified as fine-tuning methods in the paper (Section 4.1). The paper also separately lists post-hoc methods (MSP, Free Energy, ASH, Mahalanobis, KNN OOD) under a distinct category.

- **"Figure 1 generated examples look unrealistic (blurry, artifacts)"**: This is a subjective visual quality judgment about generated images. The images serve as illustrative examples of the synthesis approach; their photorealistic quality is not central to the paper's claims about OOD detection performance. Subjective aesthetic criticism is not a substantive weakness.

- **"Figure 3 curves are noisy and not convincing"**: The curves in Figures 3(a)-(b) show the expected trend (performance improving or stabilizing as M increases). The reviewer's claim of erratic behavior is a subjective interpretation of normal experimental variation.

- **"The paper overstates the difficulty of collecting OOD data — many OE works use 80 Million Tiny Images"**: The paper's claim about collection difficulty is a general motivation that applies to many practical settings. The availability of one specific dataset does not invalidate the general challenge.

- **"P and α not given for WOR loss"**: The paper explicitly states "following Wang et al. (2023)" and "P is the perturbation introduced by Wang et al. (2023)." This is standard practice when building on prior work — the details are available in the cited publication.

- **"VOS and NPOS evaluations suspicious/unfair"**: The reviewer questions VOS/NPOS reported numbers as "quite poor" but offers no evidence of mis-evaluation. The paper states it unifies backbones for fairness. Speculative claims about unfair evaluation without evidence are not substantive.

## Novel Insights

The most revealing finding from the review process is the tension between the paper's ambitious claims ("SOTA," "dynamic adjustment") and the actual experimental evidence. The ablation study (Table 2) is actually the paper's strongest contribution — it systematically compares five alternative generation strategies and shows that combining visual semantics (via textual inversion) with textual class information yields the best results. However, the paper front-loads broad SOTA claims in the abstract and introduction while failing to directly engage with the strongest competitor (DOE) in the results discussion. This pattern — strong methodological contribution paired with overstated claims and selective reporting — is the paper's central weakness. The core idea is genuinely novel and the within-method ablation is convincing, but the cross-method comparisons are less thoroughly validated.

## Suggestions

1. **Temper the SOTA claim**: If DOE outperforms DOG on some benchmarks, acknowledge this explicitly and discuss why (e.g., DOE's WOR loss may provide different regularization, or the comparison may involve different settings). Avoid blanket "state-of-the-art" claims.
2. **Specify λ and other missing hyperparameters**: Report the λ value used (or the range searched) and the textual inversion optimization details (steps, learning rate, prompt template).
3. **Remove or support the "dynamic adjustment" claim**: Either add an experiment showing iterative refinement of the generated outlier set, or remove this language from the abstract and conclusion.
4. **Add a scoring-controlled ablation**: Run all main baselines and DOG with the same scoring function to disentangle generation effects from scoring effects.
5. **Add quantitative near-OOD analysis**: Compute feature-space distances between generated outliers and ID data, and compare across generation strategies to substantiate the "near-OOD" claim.
6. **Report error bars or multiple runs**: The main tables and ablation results lack any indication of variance. At minimum, report results over multiple random seeds.

## Score and Decision

MY FINAL SCORE: <pineapple>5.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>