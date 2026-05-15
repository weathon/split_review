Now I have all the information I need. Let me produce the final consolidated review.

## Summary

This paper proposes EquiAV, a framework that integrates single-modal equivariant contrastive learning with audio-visual contrastive learning. The key idea is to learn inter-modal (audio-visual correspondence) and intra-modal (augmentation-related, modality-specific) representations in separate latent spaces — the former using invariant contrastive learning and the latter using equivariant contrastive learning. Extensive ablations validate the framework design, and the method achieves strong results on AudioSet and VGGSound benchmarks.

## Strengths

- **Novel integration of equivariance into audio-visual self-supervised learning.** The paper is the first to apply intra-modal equivariant contrastive learning in an audio-visual setting. The motivation — that strong augmentations can break inter-modal correspondence, but can be harnessed via equivariance in a separate latent space — is well-articulated and clearly distinguished from prior invariant-only approaches.

- **Clean internal ablation validating the core technical claim.** Table 3 provides a direct, controlled comparison between InvAV (intra-modal invariance) and EquiAV (intra-modal equivariance) using the same backbone initialization and training pipeline. EquiAV outperforms InvAV on all metrics (e.g., 14.3 vs. 11.7 V2A retrieval R@1, 48.0 vs. 47.1 AudioSet classification mAP), cleanly demonstrating that the equivariance mechanism itself improves representations beyond an invariant baseline.

- **Systematic ablation of framework variants.** The paper evaluates four distinct architectural variants (Figure 2) and shows that applying equivariance to the inter-modal space actually hurts performance (V2A drops from 11.7 to 8.9) while keeping inter-modal invariant and intra-modal equivariant is optimal. This provides concrete evidence that augmentation-related information and audio-visual correspondence must be learned in separate spaces.

- **Demonstrated robustness to strong augmentations.** Table 4 shows that EquiAV's performance improves monotonically as augmentations are added (AudioSet classification mAP from 47.2 to 48.0), while InvAV degrades (47.1 to 46.2). This supports the claim that equivariance not only avoids the adverse effects of strong augmentations but actively benefits from them.

## Weaknesses

### Fatal

None.

### Major

- **Headline SOTA claims are partially confounded by backbone initialization.** EquiAV initializes both encoders with a self-supervised MAE ViT-B/16 checkpoint, while prior methods (CAV-MAE, MBT, AVMAE, etc.) use different backbones (AST, ResNet, supervised ViT). Table 3 reveals that even the *invariant* baseline InvAV — which uses no equivariance — already achieves 11.7 V2A zero-shot retrieval vs. 3.3 for CAV-MAE, a ~3.5× improvement attributable almost entirely to the MAE backbone. This means the large absolute gap over prior work in Tables 1–2 cannot be cleanly attributed to the equivariance mechanism. The paper's core contribution (equivariance > invariance) is validated internally in Table 3, but the stronger claim of "outperforming existing state-of-the-art methods" would require controlled re-implementations of prior methods with the same MAE backbone, or EquiAV with a weaker backbone. This does not invalidate the paper, but it undermines the headline claim as currently presented.

- **Augmentation parameterization is underspecified, compromising reproducibility.** Section 3.1 states that augmentation information is "encoded into real vectors, denoted as t_a and t_v" that "parameterize how much each augmentation is applied," but it does not specify: (1) the dimensionality of these vectors, (2) how non-parametric or discrete augmentations (e.g., horizontal flip, random resized crop) are mapped to continuous vectors, or (3) how multiple augmentations applied simultaneously are composed into a single vector. Since the augmentation predictors (u_t_a, u_t_v) take these vectors as input, this detail is essential for reproducing the method. Augmentations listed in the paper (RRC, CJ, GB, HF, GS, SA, TS, FR, VF) have disparate parameter spaces, and the paper does not explain how these are unified.

### Minor

- **No error bars or variance estimates are reported.** All results in Tables 1–5 are point estimates without standard deviations or confidence intervals. While single-run evaluation is common practice for large-scale AudioSet benchmarks, the absence of any variance information makes it difficult to assess the robustness of smaller margins (e.g., 55.7 vs. 55.0 on AudioSet-20K A+V classification). The larger gains in zero-shot retrieval are more convincing, but error bars would strengthen confidence throughout.

- **No dedicated limitations section.** The paper concludes without discussing limitations, failure cases, or settings where the method might underperform. For instance, the reliance on MAE initialization means the method inherits any biases or limitations of that pretraining strategy; training from scratch or with different initializations is not explored. Adding a limitations paragraph would improve scientific completeness.

- **Figure 1 does not specify the InvAV configuration or quantify "augmentation level."** The figure is used to motivate the paper, but the caption refers readers to Table 4 for details without specifying which InvAV variant or augmentation configuration is plotted. This makes the figure less self-contained than it should be.

### Trivial

- None of significance.

## Nice-to-Haves

- A controlled experiment where CAV-MAE or another prior method is re-implemented with the same MAE ViT-B/16 backbone used by EquiAV, allowing a clean attribution of gains to the equivariance framework versus backbone choice.
- Qualitative retrieval examples showing cases where EquiAV succeeds and InvAV fails, illustrating the practical value of equivariance.

## Removed Points

These points are flagged to be removed; treat them with caution:

- *"Related work does not discuss prior use of equivariance in multi-modal settings"* — Removed per rule: "DO NOT mention missing related works" since verification is not possible without external sources.
- *Formatting/style nitpicks about Table 1* (cluttered footnotes, spurious "%" signs, unclear columns) — Removed per rule: "REMOVE pure formatting/style nitpicks."
- *Criticism that Figure 1's InvAV configuration is unclear regarding unaugmented inter-modal pairs* — The paper's Equation (Section 2.2, line 67) clearly specifies InvAV uses unaugmented inputs for the inter-modal term. This concern reflects a misreading.
- *Strength Finder's claim about "State-of-the-art performance on multiple downstream tasks"* — This is partially retained in the Strengths section but weakened by the verified backbone confound. It is not fully dropped because the numbers are indeed competitive; the caveat is properly placed in the Weaknesses section.

## Novel Insights

The most interesting finding that emerges across the reviews is the strong empirical case for *separate* latent spaces in multi-modal contrastive learning. Table 3 shows that the choice of where to apply equivariance (intra-modal vs. inter-modal) is not neutral — applying it to the inter-modal space actively harms performance. This suggests a design principle: in multi-modal contrastive learning, augmentation-related variation and cross-modal correspondence should be explicitly disentangled into different representational subspaces. This insight goes beyond the paper's specific application and could inform future multi-modal architectures more broadly.

## Suggestions

1. **Address the backbone confound transparently.** Add an experiment or discussion that controls for backbone choice. For example, pre-train EquiAV using a supervised ImageNet ViT initialization (matching what MBT uses) and compare. Alternatively, re-run CAV-MAE's training pipeline with the same MAE initialization used by EquiAV. Even a discussion quantifying the approximate contribution of the backbone vs. the equivariance mechanism would strengthen the paper.

2. **Fully specify the augmentation parameterization.** Provide the dimensionality of t_a and t_v, a table mapping each augmentation to its parameter encoding (e.g., how horizontal flip — a binary operation — is encoded), and how multi-augmentation compositions are handled. Reference the prior work (Devillers & Lefort, 2023) more precisely to clarify which parts are inherited vs. novel.

3. **Add error bars or multi-seed results** for at least the key comparisons (Tables 3 and 4) to establish statistical robustness.

4. **Include a limitations paragraph** in the final version discussing the reliance on MAE initialization, potential failure cases (e.g., when augmentations are too destructive), and broader applicability to other multi-modal settings.

## Score and Decision

This paper makes a clear and well-motivated contribution: it introduces equivariant intra-modal learning to audio-visual contrastive learning, validates the design through careful ablations, and demonstrates that the approach outperforms an invariant intra-modal baseline under controlled conditions. The main weaknesses are that the headline SOTA claim is partially confounded by a strong backbone initialization (which the paper's clean internal ablation does not fully remedy) and that the augmentation parameterization is underspecified. Neither weakness is fatal — the core framework contribution is validated internally — but both require attention before the paper can be considered fully rigorous.

The paper is a solid empirical contribution to audio-visual self-supervised learning. The experimental methodology could be strengthened with controlled comparisons and reproducibility details, but the core idea is sound and well-supported by the internal ablations.

MY FINAL SCORE: <pineapple>6.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>