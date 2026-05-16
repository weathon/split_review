Here is the final consolidated review.

---

## Summary

DiNO-Diffusion proposes a self-supervised method for training latent diffusion models that conditions image generation on frozen DiNO image embeddings rather than text or class labels. By eliminating the annotation requirement, the authors train on 868k unlabelled chest X-ray images from 21 public datasets. The resulting model achieves FID 4.7, yields up to 20% AUC improvement when used for data augmentation in small-data regimes, and enables zero-shot lung segmentation (84.4% Dice) — all without any manual annotation during DM training.

## Strengths

- **Self-supervised conditioning eliminates the annotation bottleneck.** The method trains on 868k unlabelled CXR images (Section 2.1, 2.3) by conditioning on DiNO global tokens. This directly addresses a core challenge in medical imaging where annotated datasets are scarce and inconsistent.

- **Demonstrated downstream improvements across multiple tasks.** Data augmentation with synthetic images improves classifier AUC by up to 20% in small-data regimes (N=50, Table 1, Section 3.2). Zero-shot lung segmentation achieves 84.4% Dice on the combined dataset, outperforming vanilla SD 1.5 (80.3%) with lower variance (Table 2, Section 3.4). The paper notes this is the first application of zero-shot segmentation to a medical diffusion model.

- **Large-scale unlabelled training corpus.** The compilation of 868k images from 21 sources without label curation (Section 2.1) exceeds the scale of prior medical DMs that rely on smaller annotated datasets (e.g., RoentGen's 300k MIMIC images with captions).

- **Clean experimental design.** Five-fold cross-validation with held-out test sets, label balancing, and careful separation of training data (all non-MIMIC) from evaluation data (MIMIC for classification/quality, JSRT/Montgomery/Shenzhen for segmentation). Multiple data regimes (N=50 to 5000) and real-to-synthetic ratios (1:1 to 1:50) provide a thorough characterization.

- **Clear, self-critical discussion.** The paper openly acknowledges when the interpolation strategy degrades performance in high-data regimes (Section 4) and discusses the circular dependency limitation of image-conditioned models.

## Weaknesses

### Fatal
None.

### Major

- **Missing comparison to text-conditioned medical DMs.** The paper frames self-supervised conditioning as an alternative to text conditioning but provides no direct comparison to a text-conditioned DM (e.g., RoentGen or an equivalent) on any of the three evaluation tasks. A text-conditioned model trained on MIMIC (with its ~300k report-paired images) would provide a critical reference point for FID, classification benefits, and segmentation quality. Without this baseline, the reader cannot assess whether self-supervised conditioning yields comparable, better, or worse outcomes than a model using even weakly aligned text annotations. This gap is structural: the evaluation protocol does not test the paper's central framing.

### Minor

- **Unsubstantiated privacy-preservation claim.** The abstract states DiNO-Diffusion "hold[s] potential for privacy preservation," the discussion claims it "demonstrated that synthetic data can replace real data while preserving privacy," and the conclusions list "privacy preservation" as a demonstrated result. In reality, no privacy metric is computed — no membership inference, reconstruction risk, or distance-to-nearest-neighbor analysis. Synthetic images are generated from embeddings of real training images, so whether they actually protect patient privacy is unknown. This overclaim does not undermine the core method, but it should be toned down to "potential" or supported with analysis.

- **Confounded segmentation baseline.** The zero-shot segmentation comparison pits DiNO-Diffusion (trained on 868k CXR images) against vanilla SD 1.5 (trained on LAION-2B natural images). This confounds two factors: (i) medical-domain training vs. natural-domain training, and (ii) DiNO conditioning vs. text conditioning. The reported 4–10% Dice improvement cannot be cleanly attributed to the DiNO conditioning mechanism. An unconditional LDM or a text-conditioned LDM trained on the same medical data would be needed to disentangle these factors. (That said, the improvement over SD is still a meaningful existence proof — it shows a model trained with self-supervised conditioning on unlabelled medical data outperforms a general-domain model.)

- **Data leakage in segmentation test sets.** The training set (Section 2.1) includes "every openly accessible CXR dataset minus MIMIC-CXR," and the listed sources include JSRT, Montgomery, and Shenzhen — the same datasets used for segmentation evaluation. While the DiffSeg method uses internal UNet features (not labels) and FID is computed on MIMIC (held out), the use of test-set images during DM training is a potential leakage that should be acknowledged.

- **No analysis of synthetic image diversity/novelty.** The paper reports large AUC improvements from synthetic data augmentation but provides no analysis (e.g., LPIPS, precision/recall, or embedding-space coverage) to verify that synthetic images provide semantically meaningful variety rather than low-level augmentation effects. The concern is especially relevant for the reconstruction strategy, where images are generated from embeddings of real training samples.

- **FID reported without context.** The FID scores of 4.7 (DiNOv1) and 6.4 (DiNOv2) are presented without comparison to prior work. RoentGen reports FID ~4.3 on MIMIC using a similar feature extractor; citing this would help readers calibrate the results. Confidence intervals or standard deviations for FID would also be helpful, as FID is known to be noisy with single values.

### Trivial

- **"Agnostic to medical imaging modality" is overstated.** Only chest X-ray is tested. The paper's claim (Introduction, line 31) of modality agnosticism is not supported by evidence. The softer statement in the abstract ("can be easily adapted") is more appropriate.

- **Segmentation checkpoint inconsistency noted but unexplored.** The paper observes that the optimal checkpoint for segmentation (Section 3.4) is "significantly earlier" than the one with lowest FID (Section 3.1) but does not discuss implications. This is an interesting finding worth a brief comment.

## Nice-to-Haves

- A text-conditioned LDM trained on MIMIC-CXR (or comparable data) as a baseline for all three evaluation tasks.
- Privacy analysis: at minimum, distance-to-nearest-neighbor between synthetic and real images in embedding space, or a membership inference attack.
- Ablation: an unconditional LDM trained on the same medical data to quantify the benefit of DiNO conditioning vs. simply training on more domain data.
- Diversity analysis (LPIPS, recall) for synthetic images, particularly for the reconstruction strategy where overfitting is a concern.

## Removed Points

- *Criticism that the training data (MIMIC-CXR) has free-text reports making a text-conditioned baseline "feasible on the same training data."* This is factually incorrect: the paper explicitly states (Section 2.1) that the **training set excludes MIMIC-CXR entirely**. The training data (868k images from non-MIMIC sources) do not have standardized text reports. A text-conditioned model trained on the same 868k images is **not** feasible without additional annotation. The corrected criticism (kept above) is that a text-conditioned model trained on MIMIC (~300k report-paired images) should still be compared.

- *"Weakness about missing appendix / missing appendix content."* The parser strips appendix content; these exist in the original submission.

- *Formatting/style nitpicks and grammar issues.* These are parser artifacts, not author errors.

- *Generic strengths from the Strength Finder that lack specific evidence (e.g., "addressed an important problem" without concrete support) have been dropped.*

## Novel Insights

The reviews surface an insightful tension: the paper's main strength (self-supervised conditioning enabling training on 868k unlabelled images) is also the source of its main evaluation gap. Because the training data has no text, a direct like-for-like comparison to text-conditioned models is structurally impossible on the same data. This means the paper is effectively arguing for a different *data regime* (unlabelled at scale) rather than a strictly better *conditioning mechanism*. The segmentation result — where DiNO-Diffusion outperforms vanilla SD despite SD being trained on vastly more (natural) data — is the strongest evidence that domain-specific self-supervised training matters, but the attribution to DiNO conditioning specifically remains entangled with domain adaptation. The privacy overclaim is a separate, avoidable weakness: the paper's actual evidence (classifiers trained on synthetic-only data achieve reasonable AUC) supports "data replacement potential" but not "privacy preservation" without further analysis.

## Suggestions

1. **Add a text-conditioned baseline trained on MIMIC-CXR** (replicating RoentGen's setup) for FID and classification comparisons. This is the single most impactful addition and would directly address the main structural weakness.
2. **Remove or soften privacy claims** — either add a privacy analysis (membership inference, nearest-neighbor distance) or replace "privacy preservation" with "data replacement potential" throughout.
3. **Acknowledge the data leakage** that segmentation test images were in the DM training set and explain why this does/does not affect the DiffSeg results.
4. **Add an unconditional LDM trained on the same medical data** as a controlled ablation for the segmentation experiment.
5. **Report FID with confidence intervals or across seeds** and cite RoentGen's FID for context.

## Score and Decision

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>