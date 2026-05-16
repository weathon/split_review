Now let me compile my final review.

## Summary
2-3 sentence summary of the paper's contribution.

The paper proposes DOG, a framework that uses a pre-trained text-to-image diffusion model (Stable Diffusion) to generate near-OOD surrogate outliers from in-distribution data alone, by combining visual semantics (via textual inversion) with explicit textual category information (via WordNet candidate selection and CLIP-based anchoring). These synthetic outliers are used to fine-tune an OOD detector. The method achieves strong empirical results on CIFAR-10, CIFAR-100, and ImageNet benchmarks.

## Strengths
- **Novel diffusion-based, bi-modal synthesis of near-OOD outliers**: DOG is the first framework to use a large-scale text-to-image diffusion model to generate surrogate outliers by combining visual semantics (via textual inversion, Eq. 4) with explicit textual category information (Section 3.1.2). This differs fundamentally from prior GAN-based (ConfGAN) or latent-space sampling approaches (VOS, NPOS).
- **Strong empirical results on multiple benchmarks**: On CIFAR-100 (Table 1), DOG improves average FPR95 by 20.27 over standard OE and by 50.93 over VOS, with corresponding AUROC gains of 5.14 and 27.70. These improvements are large and consistent across multiple OOD test sets.
- **Ablation study confirms design choices outperform alternatives**: Table 2 shows DOG beats five alternative diffusion-based synthesis strategies (noise injection, interpolation, synonym-based generation), demonstrating that the combination of textual inversion and candidate-word anchoring is critical to the method's effectiveness.
- **Addresses a practical limitation of Outlier Exposure (OE)**: DOG eliminates the need to collect external surrogate OOD datasets, a well-known difficulty in OE (Section 2). The method generates outliers using ID data alone, which is validated in Algorithm 1 and Section 3.1.
- **T-SNE visualization confirms near-OOD positioning**: Figure 3(c) shows synthetic outliers lie near the boundary of ID embeddings, supporting the claim that they constitute near-OOD data that improves generalization.

## Weaknesses

### Fatal
None.

### Major
- **Unsubstantiated "dynamic adjustment" claim**: The abstract states that DOG "presents a novel approach for outlier exposure by allowing dynamic adjustment of surrogate outlier data based on the results," and the conclusion repeats this. However, the methodology (Section 3, Algorithm 1) describes only a fixed, one-shot generation procedure — textual inversion → candidate selection → anchor filtering → image generation → fine-tuning — with no iterative or adaptive component. No experiment demonstrates any dynamic adjustment. This is a significant mismatch between claimed contribution and actual content. The authors should either remove this claim or provide a mechanism and experimental validation.
- **Potential data leakage from the diffusion model not discussed**: DOG uses Stable Diffusion v1.5, trained on the LAION-5B dataset, which very likely contains images from standard OOD test sets used in evaluation (e.g., Textures, Places365, SUN, iNaturalist). If the generative model can produce images resembling these test distributions, detection accuracy could be artificially inflated. The paper does not acknowledge or attempt to control for this confound. A simple check (e.g., measuring CLIP similarity between generated outliers and OOD test samples) would help assess the risk. This is not a fatal flaw but needs discussion.

### Minor
- **Missing error bars / variance reporting**: Table 1 reports only point estimates. Given the stochasticity of diffusion sampling and fine-tuning, performance can vary across runs. Without multiple seeds or confidence intervals, the robustness of the reported improvements cannot be assessed.
- **Threshold λ never specified**: The anchor selection criterion (Eq. 6) uses a threshold λ that "is the given threshold," but no value is reported in the experimental details (Section 4.1) and no ablation is provided. This parameter crucially determines which candidate words become anchors; its omission harms reproducibility.
- **Textual inversion hyperparameters omitted**: The textual inversion optimization (Section 3.1.1, Eq. 4) is described at a high level, but critical hyperparameters (learning rate, number of optimization steps, prompt template) are not reported.
- **η=0.05 without ablation or justification**: The percentile tolerance η (Eq. 6) is set to 0.05 without any sensitivity analysis or rationale for why this value is appropriate.
- **Baseline comparison lacks sufficient detail**: The paper states "We adopt their suggested setups but unify the backbones for fairness" (Section 4.1), but does not specify whether baseline numbers were obtained by re-running methods under identical conditions or taken from original papers. Given the very large margins reported (e.g., 20.27 FPR95 improvement on CIFAR-100), the reader needs to know how baselines were produced.
- **Ablation strategies use fixed, not optimized, hyperparameters**: The alternative synthesis strategies in Table 2 use single configurations (e.g., noise level α=0.3, β∈{0.3,...,0.7}) without tuning. While reasonable defaults, this limits the conclusiveness of the comparison.

### Trivial
- Algorithm 1's loop nesting (lines 2–10) has an ambiguous structure that mixes candidate selection and diffusion sampling in an unclear way — a minor presentation issue.

## Nice-to-Haves
- Computational cost analysis (GPU-hours) would help assess practical feasibility.
- Sensitivity analysis for K (candidate count) and λ would strengthen the method's characterization.
- A limitations paragraph discussing failure cases (e.g., classes with ambiguous visual semantics, WordNet limitations) would improve credibility.
- An ablation comparing standard OE loss vs. the model-perturbed DOE loss (Eq. 9) would isolate the contribution of the generated data from the training objective.

## Removed Points
These points are flagged to be removed; treat them with caution.
- **"Using only ID data" is contradictory (Harsh Critic, Section-by-Section)**: The critic claims the paper contradicts itself by saying "using only ID data" while relying on external models (diffusion model, CLIP, WordNet). This is a misunderstanding: "using only ID data" means no external OOD *datasets* are needed — a standard phrasing in the OE literature. The external models are pre-trained and fixed. Removed as factually incorrect.
- **ImageNet results missing from main text (Harsh Critic)**: The critic says ImageNet results are mentioned only in passing without a table. The text states "We also evaluate all methods on the ImageNet dataset, with our method DOG achieving the best performance.1" — the superscript "1" is a footnote reference to an appendix table that was stripped by the parser. Removed per rule that parser-stripped appendix content should not be penalized.
- **Algorithm 1 structural issues (Harsh Critic)**: The critic claims "the nesting is ambiguous." The algorithm is conceptually clear despite minor formatting artifacts. Removed as a formatting nitpick.
- **"No systematic study of M's interaction with model capacity" (Harsh Critic)**: The paper studies M on both CIFAR-10 and CIFAR-100 (two different dataset complexities) in Figures 3(a,b). The analysis is adequate for the scope. Removed as an overreach.

## Novel Insights
The harsh critic's most insightful point is the "dynamic adjustment" overclaim — a genuine gap between the paper's framing and its method. This is not a minor wording issue; the abstract and conclusion both present this as a key property of DOG, yet no mechanism or experiment supports it. This kind of overclaiming in high-level framing undermines reader trust even when the underlying technical contribution is solid. The data leakage concern is also well-taken and represents a blind spot common in papers leveraging large-scale pre-trained generative models for OOD detection — the community should develop norms for verifying that synthetic training data does not accidentally resemble test OOD distributions.

## Suggestions
1. Remove or substantiate the "dynamic adjustment" claim. If it refers to adjusting λ or M post-hoc, make this explicit and show an experiment; otherwise delete the claim entirely.
2. Add a data leakage analysis: compute maximum CLIP similarity between generated outliers and OOD test images, or hold out a set of OOD datasets whose images are known to be absent from LAION-5B.
3. Report λ (the anchor threshold) and provide an ablation over its values.
4. Add error bars (multiple seeds) to at least the main results table.
5. Clarify whether baselines were re-run or numbers were cited, and if re-run, describe the protocol.
6. Report textual inversion hyperparameters (learning rate, steps, prompt template).

## Score and Decision

The paper proposes a genuinely novel and well-motivated approach, and the empirical results on CIFAR benchmarks are strong. However, the combination of an unsubstantiated core framing claim ("dynamic adjustment"), an unaddressed data leakage confound, missing error bars, and an unspecified key parameter (λ) means the paper does not yet meet the standard for acceptance. The contribution is real, but the evidence as presented is not fully rigorous. I encourage the authors to address these issues in a revision.

MY FINAL SCORE: <pineapple>5.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>