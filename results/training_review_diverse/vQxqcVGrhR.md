Now I have all the information I need. Let me synthesize the final review.

---

## Summary

DisEnvisioner proposes a tuning-free, single-image customized generation pipeline that disentangles subject-essential features from subject-irrelevant attributes (pose, background, color tone) via a visual tokenizer (DisVisioner), then enriches the disentangled subject token into multiple granular tokens (EnVisioner) to improve ID consistency. The core idea—explicitly separating then enriching visual tokens—is well-motivated and the two-stage design is logically sound. The method achieves the best text-alignment (C-T=0.315) and lowest internal variance (IV=0.026) on the DreamBooth benchmark, while running in ~2s without test-time tuning.

## Strengths

1. **Explicit disentanglement of subject-essential vs. irrelevant features through spatial-wise tokenization.** Unlike prior tuning-free methods (IP-Adapter, BLIP-Diffusion, ELITE) that use either global image features or implicit subject representations, DisEnvisioner aggregates CLIP image features into two distinct visual tokens via a learned image tokenizer with separate queries. The subject-irrelevant token can be discarded at inference, and attention-map visualizations (Fig. 6, supplementary Fig. S6) confirm that the two tokens attend to genuinely different regions of the image.

2. **Enrichment of the disentangled subject token into multiple granular tokens via separate projectors.** The EnVisioner maps the single subject-essential token into four tokens using dedicated projectors (Eq. 2), boosting ID consistency without re-introducing irrelevant information. The two-stage design is shown to be necessary—single-stage training fails to capture subject features at all (supplementary Fig. S5).

3. **Strong quantitative evidence for editability and robustness to irrelevant factors.** On the DreamBooth benchmark (Table 1), DisEnvisioner achieves the highest CLIP text-alignment (C-T=0.315) and the lowest internal variance (IV=0.026), meaning it follows textual instructions accurately while being minimally influenced by reference-image pose/background. It also achieves the best mean rank (mRank=2.0) across all metrics, including inference speed (1.96 s, comparable to the fastest tuning-free methods).

4. **Introduction of Internal Variance (IV) as an evaluation metric.** IV directly measures the impact of subject-irrelevant factors by computing variance across outputs from the same subject under different environments. This fills a gap in prior evaluation protocols, which focus on ID similarity and text alignment but not on robustness to nuisance variables.

## Weaknesses

### Fatal
None.

### Major

1. **The claimed "orthogonality" guarantee from SoftMax is technically inaccurate.** Section 3.2 states: "This mutual independence and orthogonality are ensured by the SoftMax function applied at spatial dimension within the spatial-wise attention." SoftMax on spatial locations ensures that each query's attention weights sum to 1 over spatial positions; it does **not** enforce orthogonality between different tokens' attention maps, nor does it guarantee that the token feature vectors are orthogonal in embedding space. The model may still learn empirical separation through the training objective and architectural design (separate query initialization, reconstruction loss), but the paper attributes a stronger theoretical property to SoftMax than it provides. This does not invalidate the empirical results, but the description should be corrected.

### Minor

2. **Key ablations lack quantitative metrics.** The ablation on token numbers (Fig. 5) shows only attention maps without reporting C-T, C-I, D-I, or IV for different settings. The ablation of EnVisioner (Fig. 6) shows only a single qualitative example. Without quantitative ablation results, the claim that `n_s=1, n_i=1` is optimal and that EnVisioner provides a measurable boost rests entirely on visual inspection. This is the paper's most significant methodological gap.

3. **No statistical uncertainty reported for any metric.** All quantitative results (Table 1, user study) are point estimates without confidence intervals, standard deviations, or significance tests. The evaluation uses 158,000 generated images (40 inferences × 25 prompts × 158 images), so the estimates are likely stable, but the paper does not demonstrate this. Given that the differences on C-I and D-I between DisEnvisioner and several baselines are modest (e.g., C-I 0.828 vs. BLIP-Diffusion's 0.785), variance across subjects would help confirm robustness.

4. **The "augmentation set" applied to reference images before CLIP encoding is not specified.** Section 3.2 mentions that the reference image is transformed "using an augmentation set" to prevent the model from merely duplicating the subject, but no list of augmentations is provided. This is a reproducibility gap.

5. **The mRank weighting, while justified, is presented without a simpler baseline comparison.** The paper halves the weight of C-I and D-I because they are "two sub-indicators of image-alignment." This is a defensible choice, but showing the unweighted mean rank alongside the weighted one would make the overall comparison more transparent. (For the record: even with equal weights, DisEnvisioner's mean rank of 2.0 still beats IP-Adapter's 2.8, so this does not affect the relative ranking—but the reviewer's concern about clarity is reasonable.)

6. **No limitations section.** The paper would benefit from a brief discussion of known limitations: reliance on bounding-box annotations for training, potential failure cases (small/occluded subjects, subjects that blend with background), and the fact that the disentanglement is learned empirically rather than guaranteed by the architecture.

### Trivial
- The paper uses "mutually independent and orthogonal" language that conflates two different concepts (statistical independence ≠ vector orthogonality) in describing the token features.

## Nice-to-Haves
- A direct quantitative comparison (e.g., Pareto plot of C-T vs. C-I) that visualizes the editability–identity trade-off across methods would be more informative than collapsing everything into a single mRank.
- Reporting variance across the 30 DreamBooth subjects (e.g., per-subject C-I with error bars) would strengthen the statistical credibility of the comparisons.
- A user study with raw-score distributions (not just normalized sums) would make the human evaluation fully interpretable.

## Removed Points

*These points are flagged to be removed; treat them with caution.*

1. **"mRank weighting is arbitrary; IP-Adapter would win with equal weights."** — Factually incorrect. Computing a simple unweighted mean rank (all weights = 1.0) gives DisEnvisioner 2.0 vs. IP-Adapter 2.8. DisEnvisioner still leads with or without the 0.5 weighting. The paper's justification (C-I and D-I are two sub-indicators of the same construct) is also reasonable.

2. **"User study results appear inconsistent with described procedure."** — The reviewer misread the text. The paper says "scores for **other** methods are frequently identical" (emphasis added), meaning the non-DisEnvisioner baselines cluster together. If DisEnvisioner consistently gets 4/5 while the rest get 3/5, normalization to sum=1 produces exactly the observed pattern (DEn at ~0.21, others at ~0.15–0.18). The description and numbers are consistent.

3. **"The BLIP-2 claim in Section 2.2 is not empirically demonstrated."** — This is a motivation argument, not a claimed result. The paper does not need to experimentally validate every statement about why prior methods are limited. The motivation is supported by qualitative comparisons in Fig. 1.

4. **"Missing related works"** — Not verifiable without external sources; do not assume omission.

5. **Various formatting/style nitpicks** — Parser artifacts, not author errors.

## Novel Insights

The reviews surface a useful meta-point about evaluation methodology in customized generation: the field currently relies on aggregate rankings that can obscure trade-offs between editability and identity preservation. The harsh critic's concern about mRank weighting (even though the specific arithmetic was mistaken) underscores that the community would benefit from per-metric Pareto analyses rather than single-number composites. None of the other insights go beyond what the paper itself articulates about the importance of explicit disentanglement of subject-essential features.

## Suggestions

1. **Correct the orthogonality language.** Replace the claim that SoftMax "ensures" mutual independence and orthogonality with an honest description: the architecture encourages separation through separate query initialization (random vs. class-name embeddings), the reconstruction objective, and the spatial-wise cross-attention mechanism that forces each query to attend to different spatial regions. Remove the overclaimed theoretical guarantee.

2. **Add quantitative ablation tables.** Report C-T, C-I, D-I, and IV for (a) different `(n_s, n_i)` configurations and (b) w/ vs. w/o EnVisioner. This would substantially strengthen the empirical validation of design choices.

3. **Report per-subject variance** (e.g., standard deviation or 95% CI across the 30 DreamBooth subjects) for all metrics in Table 1. This is feasible from the existing 158,000 generated images.

4. **Specify the augmentation set** used on reference images during DisVisioner training (e.g., random cropping, color jitter, etc.).

5. **Add a brief limitations paragraph** covering the training-data requirement (bounding-box annotations), potential failure cases, and the empirical (rather than theoretically guaranteed) nature of the disentanglement.

## Score and Decision

The paper proposes a clearly motivated, well-structured method that achieves demonstrably best editability and robustness while maintaining competitive ID consistency, all without fine-tuning at test time. The identified weaknesses are addressable and do not undermine the core contribution. The orthogonality overstatement and missing quantitative ablations are real issues but fall short of fatal.

**Score: 7.0**

**Decision: Accept**

MY FINAL SCORE: <pineapple>7.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>