Here is the final consolidated review:

---

## Summary

VideoDiT proposes a framework for adapting the pre-trained SD3 image diffusion transformer to video generation, with two main contributions: (1) a Distribution-Preserving VAE (DP-VAE) that hybridizes a frozen 2D VAE (for key frames) with a trainable 3D residual VAE plus a distribution-matching regularization term to align the 3D latent distribution with the 2D one; and (2) a parameter-efficient 2D→3D attention conversion via 3D positional embeddings and token reshaping. The paper claims strong data efficiency (10% of data used by prior methods) and reports results on UCF101 video generation and VAE reconstruction benchmarks.

## Strengths

1. **DP-VAE's core design is creative and well-motivated.** The key-frame + residual decomposition inspired by video compression, combined with distribution-matching regularization, directly addresses the tension between 3D VAE compression efficiency and 2D latent-space compatibility. The ablation study (Table 3, Figure 5) convincingly shows that omitting either the 2D key-frame encoding or the regularization causes catastrophic distribution shift — the full DP-VAE is necessary for proper initialization and optimal generation. This is concrete evidence that the method solves the problem it identifies.

2. **Parameter-efficient 2D→3D attention conversion is clearly demonstrated.** The paper compares its "2D→3D" approach against a "2D+3D" alternative (Table 4) and shows similar performance with 2.03B parameters vs. 4.15B — a 51% reduction. This is a clean, quantitative finding that the simple reshaping + 3D positional embeddings strategy is markedly more efficient than prior adaptation approaches.

3. **Systematic ablation studies isolate each component's contribution.** The DP-VAE ablation (Table 3) tests four configurations (no 2D VAE + no reg, 2D VAE + no reg, no 2D VAE + reg, full DP-VAE) with both reconstruction metrics and downstream generation quality, demonstrating that optimal generation requires the full method. The attention ablation fairly compares two architectural choices.

## Weaknesses

### Fatal
None.

### Major

1. **The central data-efficiency claim (10% of prior data) is completely unsubstantiated.** The abstract and introduction state that VideoDiT "achieves comparable or even superior performance while utilizing only approximately 10% of the data employed by existing methods" (line 20). This specific quantitative claim appears nowhere in the experimental section — no table lists training data volumes used by baselines, no controlled experiment varies data quantity, and no citation or comparison supports the 10% figure. A claim this precise — and this prominently positioned in the paper's central selling points — requires direct evidence. Its absence undermines scientific credibility.

2. **Video generation evaluation is insufficient to support the paper's overall claims.** The paper reports only zero-shot FVD (428.52) and IS (33.04) on UCF101. Several problems:
   - UCF101 is a single, limited benchmark with short clips and low text diversity. Modern T2V papers typically evaluate on multiple benchmarks including MSR-VTT and report additional metrics (human evaluation, CLIP-based metrics, temporal consistency).
   - The baselines in Table 2 are not named in the surrounding text — the reader cannot determine which methods are being compared against or whether the comparison is with contemporary alternatives.
   - The paper claims to "excel in both image and video generation" (line 20) but provides no quantitative image generation results (only qualitative examples in Figure 4) and no diversity, prompt-adherence, or temporal consistency metrics.

3. **The VAE reconstruction comparison (Table 1) is not controlled for pre-training advantage.** DP-VAE leverages a frozen 2D VAE from SD3 that was trained on billions of images, while the comparison VAEs (Open-Sora-Plan VAE, OpenSora VAE, CV-VAE) are trained from scratch. Showing better reconstruction under these conditions is expected and does not isolate the contribution of the DP-VAE design itself. The ablation study (Table 3) partially addresses this by testing DP-VAE variants, but a more directly controlled comparison (where the baseline also starts from the same pre-trained 2D VAE) would better isolate the advantage of the key-frame/residual decomposition.

### Minor

1. **The DP-VAE dimensional operation is not fully specified in the main text.** The paper states that z_r is "consistent in dimensionality with z_k" and z = z_k + z_r, but z_k is a 2D tensor from a single key frame while z is subsequently called a "3D latent variable" decoded by a 3D decoder. The broadcast/repetition of z_k along the temporal axis is the natural inference (given the temporal downsample factor of 4) but is never stated explicitly. While a reader can reconstruct this from context, the method section should state this dimensional relationship directly.

2. **The DP-VAE training dataset is underspecified.** The paper trains DP-VAE on "a self-collected, high-quality video dataset" with no details on size, source, or curation. For the diffusion model, 1M videos are "randomly sampled from WebVid-10M" without describing the sampling strategy. These gaps affect reproducibility.

### Trivial

1. **No conclusion section.** The paper ends abruptly after the ablation study with no synthesis of findings, discussion of limitations, failure cases, or future work.

## Nice-to-Haves

- A discussion of whether moment-matching regularization (mean and standard deviation only) is sufficient for full distribution alignment, and what failure modes might arise from imperfect alignment.
- Analysis of inference cost (FLOPS, latency, memory) given the paper's efficiency claims.
- Evaluation of temporal consistency (e.g., CLIP temporal consistency, frame-to-frame variance) as a quantitative measure.

## Removed Points
*These points are from the input reviews and are removed per filtering rules; treat them with caution.*

- **"Paper does not discuss how VideoDiT differs from temporally causal 3D VAE (Yu et al., 2024)"** — REMOVED: The paper *does* discuss this in Section 2.1 (line 32): "However, retraining a 3D VAE often results in an entirely new latent distribution, making it challenging to leverage the original well-trained T2I model's conceptual understanding." The contrast with DP-VAE (distribution preservation) is stated.
- **"The 2D+3D comparison conflates architecture with optimization (freezing vs. updating all weights)"** — REMOVED: While the training strategies differ, the comparison fairly shows that even with more parameters and frozen spatial weights, the 2D+3D method does not outperform the simpler 2D→3D approach. The conclusion about parameter efficiency remains valid.
- **"Paper is structurally incomplete as a research submission (no conclusion)"** — DEMOTED to Trivial. The missing conclusion is a completeness issue, not a methodological gap.

## Novel Insights

None beyond the paper's own contributions. The reviews primarily surface a gap between the paper's genuinely creative core contribution (DP-VAE) and its insufficient experimental support — the ablation study convincingly validates the mechanism, but broader performance claims (10% data efficiency, state-of-the-art video generation) are asserted without commensurate evidence. This is a gap in execution, not a conceptual flaw.

## Suggestions

1. **Remove or substantiate the 10% data-efficiency claim.** Either provide a table comparing training data volumes across methods with appropriate citations, run a controlled data-ablation experiment, or remove the unsupported number from the abstract/introduction.
2. **Expand video generation evaluation to at least one additional benchmark** (e.g., MSR-VTT) and report standard metrics beyond FVD/IS (CLIP score, human preference). Name all baselines in the text.
3. **Clarify the DP-VAE dimensional relationship explicitly** in Section 3.1: state that z_k is broadcast/repeated along the temporal axis before addition with z_r.
4. **Add a controlled VAE comparison** where a standard 3D VAE is initialized from the same pre-trained 2D VAE (without the key-frame/residual decomposition) to isolate the DP-VAE design contribution.
5. **Add a conclusion section** discussing limitations, failure cases, and how the method scales to longer videos.

MY FINAL SCORE: <score>4.0</score>
MY FINAL DECISION: <decision>Reject</decision>