## Summary
The paper extends Haim et al. (2022)'s KKT-based training data reconstruction to a transfer-learning setting: an MLP classifier $\phi$ is trained on top of frozen embeddings from a foundation model $F$ (ViT, DINO, DINOv2, CLIP), and reconstruction proceeds by (a) recovering candidate embeddings via the KKT loss and (b) inverting them back to images using DIP-based inversion (or Karlo for CLIP). It also introduces an agglomerative-clustering step that selects representatives from thousands of candidates, removing the need for ground-truth training embeddings to identify "good" reconstructions.

## Strengths
- **Embedding-space adaptation of Haim 2022 is a clean decomposition** that lifts prior reconstruction work from MNIST/CIFAR-resolution toy MLPs to 224×224 images via several modern backbones (Fig. 3, Fig. 5).
- **The diagnostic plots in Fig. 5** correlate per-sample reconstruction quality (cosine similarity in embedding space) with proximity to the decision margin across all eight classifiers, which matches the KKT theory and provides a principled, model-agnostic summary metric.
- **Multiclass extension demonstrated empirically** (Fig. 4) at 4-class iNaturalist (96%) and 10-class Food101 (84%), so the approach is not strictly tied to binary tasks.
- **The clustering idea (Sec. 5)** is a genuinely useful pragmatic contribution: it removes the unrealistic assumption of ground-truth embedding access used in §3.3 and prior works, by showing visually similar reconstructions cluster together so that inverting only ~45 representatives suffices.
- **Candid limitations in §6**: failure on linear probes, dependence on weight decay, and the explicit observation that $F^{-1}(F(s))$ is sometimes closer to $F^{-1}(\hat{x})$ than $s$ is — i.e., inversion, not reconstruction, is the bottleneck — is a useful diagnostic for the field.

## Weaknesses

### Fatal
None. The core claim — KKT-based reconstruction recovers training-margin embeddings from $\phi$ trained on top of frozen $F$ — is supported by the per-sample correlation in Fig. 5, which is computed in the embedding space the method actually optimizes (not in image space) and so is not undermined by inversion-quality concerns.

### Major
- **No null/class-conditional baseline rules out "class-prototype" generation, especially for CLIP+Karlo.** Karlo is a text-conditional diffusion generator; with only 50 images per (binary-mixed) class and a strong class-conditional generator, plausibly recognizable images could arise from any embedding pointing into the right semantic region of CLIP space. The paper concedes (§6) "$F^{-1}(\hat{x})$ are sometimes more similar to $F^{-1}(F(s))$ than to $s$." A baseline that inverts class-mean embeddings, held-out same-class embeddings, or random Gaussian samples in class space is needed to show that the recovered images are closer to the *specific* training samples than to generic class exemplars. Without it, the privacy-leakage claim is weakened, particularly for CLIP.
- **Selection in §3.3 uses oracle access to true training embeddings.** "Pair each training embedding with its nearest reconstructed candidate and select the top 40" is, as the paper admits in §3.3 last paragraph, not realistic — and that motivates §5. But the headline qualitative grids in Fig. 3 / Fig. 4 are produced under the oracle protocol, while the only training-set-free results are the smaller Fig. 6. The framing should make this distinction sharper, and the main quantitative comparison (Fig. 5) is also computed against ground-truth $F(s)$.
- **Clustering sensitivity is evaluated on a different setting than the headline.** The maxclust analysis (Fig. 6, "good rec" count via SSIM>0.4) is run on a CIFAR-10 model from prior work, not on any of the embedding-space DINO/CLIP models that motivate the paper. SSIM>0.4 is a fairly loose bar and the paper provides no false-positive analysis (clusters whose representative is plausible but not a training image). Since clustering is Contribution 3, it should be quantitatively evaluated in the actual setting.
- **Gap between "real-world transfer learning" framing and the actual setup.** §6 candidly admits the method requires (i) homogeneous MLPs (not linear probes — the dominant TL protocol), (ii) weight decay, (iii) zero training error, (iv) no full fine-tuning, and the experiments use $n=100$ binary tasks. The abstract's "real-world scenarios" and the medical-data motivation in the intro are not matched by these constraints; the contribution is more accurately framed as "MLP-on-frozen-features with WD," not transfer learning broadly.

### Minor
- **No quantitative image-space identification metric** (e.g., LPIPS/SSIM/re-ID rate of nearest reconstruction vs. nearest *non-training* same-class image) for the headline backbones. The current cosine-similarity metric is in the same embedding space the optimization targets, making the success criterion partially circular for the privacy claim.
- **Cosine-similarity inversion is magnitude-invariant**, which combined with DIP could collapse distinct candidates onto similar images and is plausibly partly responsible for the clustering behavior. A short discussion would clarify whether clusters reflect reconstruction structure or inversion structure.
- **No scaling curve in $n$** beyond $n=100$, so the threat model's dependence on training-set size is unbounded by experiment.
- **Sensitivity to weight-decay strength** is acknowledged but not quantified — at what WD does the attack degrade to chance?

### Trivial
- §4 paragraph ending "...e.g., same class)." appears to have a dropped sentence fragment.
- The "Pretrained Backbones" itemized list in §4 only lists ViT explicitly, with DINO/DINOv2/CLIP appearing implicitly via figures and table headers; an enumeration would aid readability.

## Nice-to-Haves
- A linear-probe variant of the attack (since linear probing is the most common transfer-learning protocol and is what the framing implicitly promises).
- Failure-mode visualizations: high-cosine-similarity candidates whose inversions match a *different* training image of the same class, to clarify whether memorization is per-individual or per-prototype.
- A class-conditional generation baseline using Karlo conditioned only on the class label (no embedding from $\phi$) to put an upper bound on what the inverter alone can produce.

## Removed Points
*These points are flagged to be removed; treat them with caution.*

- **"Karlo / DALL-E-style generator availability" doubts** — the paper cites Karlo; existence/availability concerns about cited tools are out of scope per review rules.
- **Harsh critic's request for membership-inference / model-stealing baselines and prior-work coverage in §2** — removed as missing-related-work concerns the reviewer cannot independently verify.
- **Strength Finder's "robust evaluation across diverse backbones"** — kept but slightly weakened: it is robust *across backbones* but always within the same restrictive $\phi$ regime, so framing it as broad robustness would conflict with the major weakness about scope.
- **Strength Finder's "per-sample similarity plots confirm KKT theory" framing** — kept, but the harsh critic's tautology concern (the metric is what's optimized) is also valid; the plot is still informative because it shows correlation with *margin distance*, not just with the optimized objective.

## Novel Insights
None beyond the paper's own contributions. The most useful original observation — that inversion, not KKT reconstruction, is the dominant bottleneck (Fig. 7 / §6) — is the paper's own.

## Suggestions
- Add a class-conditional generation null baseline, especially for CLIP+Karlo: invert class-mean embeddings and held-out same-class embeddings, and compare to the proposed method using a pixel/perceptual metric.
- Report a per-image identification rate (nearest reconstruction vs. nearest non-training same-class image under LPIPS or a re-ID network) on at least one (backbone, dataset) pair.
- Run the maxclust sensitivity / precision-recall study on the actual DINO-Food101 setting used in Fig. 4, not only on CIFAR-10.
- Sweep $n \in \{100, 500, 1000, 5000\}$ and weight-decay strength to chart the boundary of the threat model.
- Tighten the abstract/intro framing: "MLP classifiers on frozen transformer embeddings, with weight decay" rather than "real-world transfer learning," and explicitly disclaim linear probes / fine-tuning.
- Make clear in the captions of Fig. 3 / Fig. 5 that pairing uses ground-truth training embeddings; the clustering experiment in §5 / Fig. 6 is the only training-set-free result.

## Evaluation by axis
- **Originality**: Moderate. The method is a composition of three known ingredients (Haim KKT reconstruction, DIP-based model inversion, agglomerative clustering). The composition is sensible; the clustering selection is the most original piece.
- **Importance of the question**: High. Whether transfer-learned models leak training samples is genuinely interesting for privacy.
- **Soundness of claims**: Mixed. The embedding-space reconstruction claim is well-supported by Fig. 5; the *image-space* recovery claim and the broad "transfer learning in practice" claim are not, due to the missing null baseline and the restrictive setup.
- **Soundness of experiments**: Mostly qualitative; a quantitative identification rate and a class-conditional baseline are missing; the clustering ablation is run on a different setting from the main results.
- **Clarity**: Generally good; method and limitations are clearly described.
- **Value to the community**: Real. The pragmatic insights (clustering for selection, inversion as the bottleneck, candid failure modes for linear probes / no-WD) will be useful for follow-up work on attacks and defenses.

## Score and Decision
The paper makes a real, if narrow, contribution: it scales KKT-based reconstruction up to embedding-space transfer learning with modern foundation backbones, and it offers a pragmatic clustering selection step that removes the prior dependence on training-set access. The main claims are partially supported (embedding-space recovery is well-evidenced) and partially overstated (image-space "memorization recovery" is not separated from class-conditional generation, and the "real-world transfer learning" framing exceeds what the constrained MLP/WD setup demonstrates). These are addressable in revision but materially weaken the headline message in the current version.

MY FINAL SCORE: <pineapple>5.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>