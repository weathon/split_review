Now I have sufficient calibration data. Let me compose the final review.

## Summary

This paper proposes augmenting the AIDE hybrid detector for AI-generated image detection with structural semantic features derived from cuboidal partitioning — a hierarchical algorithm that recursively divides an image based on sum-of-squared-error reduction. The structural features are concatenated with AIDE's frozen patchwise and semantic embeddings, and the combined representation is fed into a retrained MLP discriminator. On the GenImage benchmark, the method achieves 89.56% mean accuracy (vs. AIDE's 86.88%), and obtains second-best results on AIGCDetect and Chameleon.

## Strengths

1. **Clear motivation and principled feature design.** The paper correctly identifies a gap in existing detectors: they focus on local patches or global semantics but neglect hierarchical structure. The cuboidal partitioning algorithm (Eqs. 1–3) provides a well-defined, reproducible way to encode structural information, and the integration with AIDE is modular and cleanly described (Section 3.3, Figure 2).

2. **New state-of-the-art on GenImage.** The method surpasses AIDE by 2.68% mean accuracy (89.56% vs. 86.88%) on a large-scale benchmark covering eight diverse generators, achieving the best results on four diffusion models (ADM, GLIDE, VQDM, Wukong in Table 1). This is the paper's strongest quantitative evidence.

3. **Competitive results across multiple benchmarks.** Beyond GenImage, the method is evaluated on AIGCDetect (91.85%, second-best) and Chameleon (second-best in both training scenarios, Table 3). The evaluation covers a wide range of generators (GANs and diffusion models) and difficulty levels, supporting the claim that structural features provide complementary information.

4. **Reproducible methodology.** The structural feature extraction process (cuboidal partitioning, SSE-based gain, cumulative gain curve, compression to 256-D) is specified with sufficient detail to re-implement. Key hyperparameters (N=1024, M=256) and training settings are reported.

## Weaknesses

### Major

1. **The claimed improvement over AIDE is not attributable to structural features without a controlled ablation.** The paper freezes AIDE's patchwise and semantic encoders, then retrains the discriminator MLP from scratch *alongside* the structural module (Section 3.3). The AIDE baseline numbers in Tables 1–3 are taken from the published AIDE paper (Section 4.1: "we rely on the comparison results published in the original papers"). This means the training protocol differs between the baseline and the proposed method in two ways simultaneously: (a) the presence of structural features, and (b) the discriminator retraining procedure. The 2.68% gain on GenImage could be partially or entirely due to retraining the discriminator on the target dataset under a different protocol rather than the structural features themselves. The paper must provide an ablation where the same frozen AIDE encoders are used with a discriminator retrained *without* the structural features to isolate their contribution. This is the single most important missing experiment; without it, the paper's central claim is not adequately supported.

2. **On AIGCDetect, the method is *worse* than the reported AIDE baseline (91.85% vs. 93.02%), and without a re-implemented baseline it is unclear whether this degradation stems from the structural features or the different training protocol.** The paper acknowledges this result and offers a "mixture-of-experts" explanation (Section 4.8), but because the baseline is not retrained under identical conditions, the cause cannot be diagnosed. This undermines the claim that structural features are "highly complementary."

### Minor

3. **No variance or statistical significance reporting.** All results in Tables 1–3 are point estimates. For the small margins on Chameleon (e.g., 58.91% vs. GramNet's 58.94% on ProGAN train), it is unclear whether the differences are meaningful or within the noise of a single run.

4. **No analysis of computational cost.** The cuboidal partitioning algorithm iteratively searches for optimal axis-parallel cuts up to N=1024 splits. The paper does not report inference time per image, FLOPs, or parameter count for the structural module, making it impossible to assess the practical overhead.

5. **Key design choices are not ablated.** The selection of N=1024 splits and M=256 compressed dimensions is stated but not justified with sensitivity experiments. Similarly, the choice of RGB pixel values as the feature vector for SSE computation (Eq. 1 uses "e.g., RGB values") is not discussed — would deeper features capture structural semantics better?

6. **Qualitative analysis is one-sided and lacks mechanistic explanation.** Figure 3 shows 13 cases where AIDE fails and the proposed method succeeds, but no cases of the opposite pattern. Figure 1 shows a face with a highlighted "AI-generated artifacts" region, but the text does not explain how the structural features produced this specific region — it is unclear whether this is a real model output or an illustration.

### Trivial

7. Table 2 has an empty cell for FreDect on SDXL and inconsistent formatting for some baselines.

## Nice-to-Haves

- Analyze which generators benefit most from structural features and characterize why (e.g., GAN vs. diffusion, face vs. scene, high vs. low structural complexity).
- Visualize the cumulative gain curves for real vs. fake image pairs to provide intuitive evidence for the claimed mechanism.
- Report training convergence (learning curves) given the very short training schedules (5 epochs for GenImage, 1 epoch for AIGCDetect).

## Removed Points

- **Criticism about Figure 1 not clarifying whether AIDE's confidence was computed or illustrative:** The paper states "the base AIDE model... incorrectly classifies a generated face as real" but does not claim confidence scores for this figure. This is a minor presentation issue, not a substantive weakness.
- **Criticism about the GELU activation justification being brief:** The paper provides a reasonable justification ("smooth, non-monotonic properties, which are beneficial for stable learning"). The choice of activation function is not central to the paper's contribution.
- **Criticism about the method being "incremental" — this is softened.** The paper explicitly states "first application" of cuboidal partitioning to AIGC detection and correctly cites prior work (Ahmed et al., 2022; Haque et al., 2025). The contribution framing is accurate and not overclaimed relative to what is demonstrated.
- **Strength from Strength Finder about "efficient integration with AIDE" — removed.** The training strategy is standard (freeze + retrain head), not a novel contribution.
- **Strength about "qualitative evidence" in Figure 3 — demoted.** The evidence is suggestive but weakened by cherry-picking (only successful cases shown).
- **Strength about "addressing higher-level structural inconsistencies explicitly" — removed.** This is essentially restating the paper's motivation, not a distinctive strength.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. **Add the critical ablation:** Retrain the AIDE discriminator (frozen patchwise and semantic encoders) *without* the structural features on the GenImage SD v1.4 training set, and compare to the proposed method. This is the single experiment that would resolve the main weakness.
2. **Report all results with confidence intervals** (e.g., over multiple seeds) to establish statistical significance, especially on Chameleon where margins are narrow.
3. **Include a "when structural features help vs. hurt" analysis** by grouping generators by performance delta and discussing common characteristics.
4. **Report inference time** per image for the full pipeline vs. AIDE alone.

## Score and Decision

My round-1 calibration bracketed this paper between the weak AIGC detection anchors (avg ~3.0) and the middle-band method papers (avg 4.0–5.0). Reading the full reviews of closely related papers — SARE (4.00, Reject), Taming the Forensic Singularity (4.50, Reject), RAID (5.00, Reject), and HiDA-Net (5.00, Accept) — provides the following comparisons:

- **vs. SARE (4.00):** SARE had a novel semantic reconstruction approach but its core hypothesis was poorly validated and it lacked robustness analysis. Our paper has a cleaner, better-motivated hypothesis but a more critical missing ablation that directly undermines the main claim. Comparable quality.
- **vs. Taming the Forensic Singularity (4.50):** That paper had stronger technical novelty (hyperbolic framework + discovery of forensic singularity) but suffered from missing ablations and reproducibility issues. Our paper is less novel but more clearly presented; the missing controlled ablation is arguably a more central flaw.
- **vs. RAID (5.00):** RAID had a clever, simple idea with very strong empirical results across 40+ benchmarks. Despite theoretical concerns, the empirical evidence was extensive and convincing. Our paper's empirical evidence is weaker due to the uncontrolled baseline comparison.
- **vs. HiDA-Net (5.00, Accept):** HiDA-Net had a well-justified high-resolution focus, strong ablations, and a new dataset (HiRes-50K). Our paper lacks comparable rigor in its evaluation despite a reasonable core idea.

The missing controlled ablation — comparing against a retrained AIDE baseline without structural features — is the critical weakness. Without it, the 2.68% gain on GenImage cannot be confidently attributed to the structural features. This is a major but not fatal issue (it is fixable with an additional experiment). Given the modest contribution (applying an existing analysis technique to AIGC detection) and the incomplete evaluation, the paper falls below the acceptance threshold but is not fundamentally flawed.

**Round-1 bracket:** Between 4.0 and 5.5.  
**Round-2 narrowing:** Placed near the lower end of this bracket, comparable to SARE (4.00) and slightly below Taming the Forensic Singularity (4.50), due to the more central nature of the missing ablation.

MY FINAL SCORE: <score>4.0</score>
MY FINAL DECISION: <decision>Reject</decision>