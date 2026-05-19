- Decision: Reject
- Avg Score: 4.50
- Scores: 3, 5, 5, 5
Now I have a thorough understanding of the paper. Let me synthesize the final review.

## Summary
This paper proposes SBGC, an unsupervised method for heterogeneous change detection that combines self-supervised feature learning (via pseudo-Siamese networks) with bidirectional graph comparison (BGC). SSL extracts features from image patches, BGC exploits graph structures in both modality directions to capture change information, and Otsu thresholding produces the final change map. Experiments on three heterogeneous datasets (Sardinia, Shuguang, California) show SBGC outperforming seven SOTA methods.

## Strengths

- **Quantitative superiority across multiple benchmarks**: SBGC achieves the highest OA and KC on all three datasets (Table 2), outperforming seven SOTA methods including both graph-based (NPSG, INLPG) and deep learning (X-Net, ACE-Net, SRGCAE) approaches. On Sardinia, the KC improvement over the second-best method is 14.38%.

- **Ablation study cleanly validates both contributions**: Table 3 decomposes the method into three conditions (raw pixels + one-way, SSL features + one-way, SSL features + BGC). On Sardinia, SSL alone lifts KC from 0.6479 to 0.7545, and adding BGC further raises it to 0.8740. This decomposition empirically confirms that both proposed components independently contribute.

- **BGC mechanism is well-defined and visually supported**: The bidirectional graph comparison in Section 2.3 defines two complementary difference terms (d_i^X starting from modality X and d_i^Y starting from modality Y), and Figure 5 provides visual evidence that BGC reduces false alarms relative to one-way comparison.

- **Diverse evaluation across modality combinations**: The three datasets cover NIR+multispectral (Sardinia), SAR+multispectral (Shuguang), and multispectral+SAR (California), demonstrating robustness to different sensor pairings.

## Weaknesses

### Fatal
None.

### Major

- **The self-supervised contrastive loss (Eq. 1) is unusually specified and insufficiently justified.** The loss writes:
  \[
  \mathcal{L}_{\mathrm{CL}}^{\chi}=-\sum_{i=1}^{M}\log\frac{d_{\Theta}(z_{x^{i}},p_{x^{i}})}{\sum_{j=1}^{M}d_{\Theta}(z_{x^{j}},p_{x^{j}})}
  \]
  where \(d_\Theta\) is a cosine similarity function. Several concerns arise: (1) Standard contrastive formulations (InfoNCE, SimCLR) use exponentiated cosine similarity with a temperature parameter to guarantee positive, well-behaved denominators — this paper uses raw cosine similarity without exponentiation or temperature. (2) The denominator sums over *all* patches' positive-pair similarities, meaning there is no explicit negative-pair modeling; the loss only normalizes each patch's view-consistency relative to other patches' view-consistency, which differs from standard contrastive learning that explicitly repels different samples. (3) The paper claims to optimize a "contrastive loss function" but does not explain why this non-standard form is suitable for heterogeneous CD or how numerical stability is maintained. While the ablation results suggest the training *does* work empirically, the lack of theoretical justification and implementation detail (exact nature of \(d_\Theta\), whether it's mapped to \([0,1]\), any temperature or stop-gradient usage) makes this a significant gap. **Why it matters**: The SSL pipeline is one of the paper's two core contributions; if the loss is not well-specified, the claim that features are learned via "self-supervised contrastive learning" is incompletely supported.

### Minor

- **Data augmentation is extremely minimal compared to standard SSL practices.** The paper states it "follow[s] the reference augmentations in (Grill et al., 2020)" but only applies horizontal and vertical flipping. Grill et al.'s BYOL uses random cropping, color jitter, blur, and solarization — transformations critical for learning invariant features. Two geometric flips provide limited invariance, and the model could trivially achieve low loss without learning semantically meaningful representations. The choice of weak augmentations is understandable given heterogeneous inputs (some augmentations may harm cross-modality alignment), but the paper neither justifies the deviation from standard SSL practice nor studies the sensitivity to augmentation strength.

- **The Otsu thresholding step may create an uneven comparison.** The paper applies Otsu's method to SBGC's fused difference image to obtain the binary change map. However, it does not specify how the baselines generate their final change maps — whether they use Otsu, their own thresholding, or clustering. If SBGC benefits from Otsu being particularly well-suited to its specific difference-image distribution while baselines use different (possibly suboptimal for their output) procedures, the comparison conflates detector quality with post-processing. The histograms of the difference images are not analyzed to confirm bimodality (Otsu's assumption).

- **The SSL ablation baseline uses raw pixels, which is a weak comparator.** The ablation shows SSL features outperform raw pixels, but this does not isolate the benefit of SSL specifically — any learned feature representation (e.g., from a simple autoencoder, PCA, or random CNN) might outperform raw pixels. A cleaner ablation would compare SSL features to another unsupervised learned representation of similar capacity.

- **No statistical significance or variability reporting.** Results are point estimates from a single run. Given randomness in patch sampling and SSL training, reporting mean±std over multiple runs would strengthen confidence.

- **Fusion of DI^X and DI^Y via simple averaging (Eq. 5) is stated without analysis.** While averaging is a reasonable default, no comparison with alternatives (e.g., min, max, weighted fusion) is provided.

### Trivial

- In line 65, there is a garbled character sequence "FxXM}" that appears to be a rendering artifact.
- The caption in Figure 1 mentions the predictor and branches but the architecture description (line 48) states "The lower branch comprises one encoder, and one predictor, while the upper branch shares the same network architecture, excluding the predictor" — it would be clearer to explicitly state which branch processes which augmented view.

## Nice-to-Haves
- A visualization of learned features (e.g., t-SNE or UMAP) would substantiate the claim that SSL produces "representative and robust" features.
- An analysis of the difference-image histogram confirming Otsu's bimodality assumption for each dataset.
- Comparison of SSL features against other unsupervised feature extractors (e.g., autoencoder) in the ablation.

## Removed Points

These points are flagged to be removed; treat them with caution:

- **"BGC is not truly bidirectional"** (Harsh Critic, Section-by-Section, Eq. 4): The critic claims BGC "computes two differences in the same direction and sums them" and is "not 'bidirectional' in the sense of symmetric comparison across both directions." **Reason for removal**: The critic missed that the paper computes both d_i^X (starting from modality X) AND d_i^Y (starting from modality Y) — Section 2.3 explicitly states "The above step can also be performed to obtain G_y^X for G_y^Y. Similar to d_i^X, we can obtain d_i^Y." This IS a symmetric bidirectional comparison. Factually incorrect.

- **"The SSL loss is 'likely incorrectly specified' and fatal"** (Harsh Critic, Critical Issue 1): The critic asserts the loss is mathematically unsound and that the claimed SSL training "may not optimize what the authors intend." **Reason for downgrade from fatal**: The loss is unusual and under-specified (kept as a Major weakness above), but the empirical results demonstrate the training converges and produces useful features. The critic's comparison to BYOL's loss is irrelevant since BYOL is cited only for augmentations, not the loss function. A non-standard loss is not automatically an incorrect one. The critic's framing as "fatal" is not supported by the evidence on the page.

- **"No analysis of learned features (t-SNE/UMAP)"** (Harsh Critic, Missing Parts): **Reason for removal**: Moved to Nice-to-Haves. This is a desideratum, not a weakness — many CD papers do not provide such analysis.

- **"The improvement might simply come from using any learned feature representation"** (Harsh Critic, Ablation Studies): **Reason for downgrade**: The ablation tests the actual methodological choice (SSL features vs. raw pixels). Requesting a comparison against other learned representations is a reasonable suggestion for strengthening but is not a flaw in the current ablation design, which cleanly tests the paper's claimed contributions.

- **Generic/superficial strengths** (Strength Finder, "Fully unsupervised learning pipeline"): This describes a property of the method (it does not require labels), which is relevant context but not a demonstrated accomplishment beyond what the ablation and main results already show.

## Novel Insights
None beyond the paper's own contributions.

## Suggestions

1. **Clarify the SSL loss** — Specify the exact form of \(d_\Theta(\cdot,\cdot)\) (is it raw cosine similarity in \([-1,1]\) or mapped to \([0,1]\)?). If raw cosine similarity is used, explain why the denominator remains positive and the log is well-defined. Better yet, adopt a standard contrastive formulation (e.g., with exponentiated similarity and temperature parameter) or provide a theoretical justification for the current design. Also clarify whether stop-gradient is used (given the asymmetric architecture with/without predictor, this may be relevant for training stability).

2. **Strengthen the augmentation strategy** — Either expand the augmentation set (e.g., random cropping, which is modality-independent) or explicitly justify why only flips are used and study the sensitivity to augmentation choices.

3. **Control for the thresholding procedure in the comparison** — Either apply Otsu consistently to all methods, or show that the relative ranking is insensitive to the choice of thresholding/clustering method.

4. **Report results over multiple runs** — Given the random components in training (patch ordering, augmentation stochasticity), provide mean and standard deviation over at least 5 runs.

5. **Deepen the SSL ablation** — Compare SSL features against a simple unsupervised alternative (e.g., a randomly initialized encoder of the same architecture, or PCA-based features) to isolate the benefit of SSL specifically.
