Now I have all the verification I need. Let me produce the final consolidated review.

---

## Summary

This paper presents an empirical comparison of Vision Transformers (ViT B/32) against five CNN architectures (ResNet-50, VGG-16, Inception-v3, MobileNet-v2, EfficientNet-B0) on face identification and verification tasks. Experiments span five datasets (VGG Face 2, LFW, ROF, SCface, UPM-GTI-Face) targeting occlusions, distance variation, and surveillance conditions. The paper reports that ViT consistently outperforms CNNs across nearly all settings — with the most striking result being that at 30 meters on UPM-GTI-Face, ViT maintains AUC 0.63 while all CNNs drop to near-random (~0.5). ViT also achieves competitive inference speed (only 23.81% slower than MobileNet despite 7× more parameters).

## Strengths

- **Multi-dataset evaluation targeting realistic face-recognition challenges**: The paper tests across five datasets that specifically isolate occlusions (masks, sunglasses in ROF and UPM-GTI-Face), variable camera quality (SCface with five surveillance cameras), and distances from 3 to 30 meters (UPM-GTI-Face). This design goes well beyond standard LFW evaluation and provides meaningful stress tests.

- **ViT's robustness to distance degradation is convincingly demonstrated**: At 30 meters on the UPM-GTI-Face unmasked scenario, ViT achieves AUC 0.63 while all five CNNs score ~0.5 (random). This is a non-trivial finding — the gap is large, consistent across distances beyond 12 meters (Figure 6a), and supports the paper's central claim about ViT's superior embedding resilience under severe distance variation.

- **Competitive inference speed with supportive evidence**: ViT processes a batch of 256 images only 23.81% slower than MobileNet (the fastest CNN), despite having over 7× the parameters (Table 2). This supports the claim that ViT offers a favorable accuracy–speed trade-off for real-time applications.

- **Transparent and reproducible experimental setup**: The paper documents hardware (Intel i9-13900K, two RTX 4090s, 128 GB RAM), software (TensorFlow, data parallelization), fixed seeds, and provides a public code repository. This enables direct reproduction and verification.

- **Honest reporting of overfitting behavior**: The paper notes that ViT's validation accuracy (99.81%) exceeds its training accuracy (98.86%), indicating underfitting rather than overfitting, while CNNs show early overfitting signs at training conclusion (Section 3.3). This observation is concrete and informs the deployment narrative.

## Weaknesses

### Fatal

None.

### Major

- **All models trained under a single hyperparameter configuration without any robustness check.** The paper uses one fixed recipe (image size 224, batch size 256, 25 epochs, Adam lr=0.0001, no learning rate schedule) for all six architectures. The paper acknowledges (Section 3) that "networks might indeed perform optimally with distinct hyperparameter settings," yet draws strong conclusions about ViT superiority from this single configuration. ViTs typically benefit from different optimizers (AdamW), schedules (cosine decay, warmup), and longer training; CNNs can respond differently to learning rate and optimizer choices. Without demonstrating that the ranking holds under a reasonable range of hyperparameters — or at minimum showing each model received comparable tuning effort — the core claim of ViT superiority is under-supported. The 30m distance result is impressive, but even there, one cannot rule out that the gap would shrink or disappear under a configuration more favorable to CNNs. This is the paper's central methodological weakness.

- **Memory footprint advantage is claimed but never empirically measured.** The abstract states that ViTs present "a smaller memory footprint," and Section 2.1 makes a theoretical argument about activation map storage. However, no GPU memory usage is measured or reported anywhere in the paper. Parameter counts are given (Table 2), but GPU memory during training — the actual claimed advantage — is not. The conclusion hedges ("holds the potential to facilitate"), but the abstract presents it as an experimental finding. A single table showing peak GPU memory during training (e.g., with the same batch size for all models, or scaling batch size to fit memory budgets) would directly support or refine this claim. As it stands, the claim is unverifiable.

### Minor

- **No confidence intervals, error bars, or variability measures are reported** for any evaluation metric (accuracy, AUC, EER). This is especially relevant for the small UPM-GTI-Face dataset (484 images, 11 subjects), where the VGG exception may reflect sampling variability. The paper dismisses the VGG exception as a "non-reproducible anomaly" without any statistical justification (e.g., bootstrap confidence intervals, significance test).

- **No details on data augmentation.** Face recognition pipelines commonly use alignment, cropping, flip, and color jitter. The paper does not mention whether any augmentation was applied, and if so, whether it differed by model. Since augmentation can interact differently with CNN inductive biases vs. ViT self-attention, this omission creates an unaccounted variable.

- **ImageNet pre-training asymmetry is not discussed.** All models are initialized from ImageNet pre-training. ViTs are known to depend heavily on large-scale pre-training to learn local representations, while CNNs can often be trained from scratch more effectively. This asymmetry could inflate ViT's relative performance and is worth at least a limitations discussion.

- **Inference time is reported for a single batch without multiple trials or throughput metrics.** Table 2 shows inference time per batch of 256 images as a single point value. No mention of number of runs, standard deviation, or whether data loading time is excluded. Throughput (images/second) or multiple trials would strengthen the comparison.

- **Only one ViT variant (B/32) and one variant per CNN family are evaluated.** This is acceptable for a focused comparison, but the conclusions about "Vision Transformers" (plural) are drawn from a single representative. Different patch sizes and ViT scales may behave differently on face tasks.

- **No learning rate schedule used.** The paper specifies a fixed learning rate (0.0001) with no decay, warmup, or scheduling. This is suboptimal for ViTs, which commonly use cosine decay and linear warmup, and may differentially penalize architectures with different optimization landscapes.

### Trivial

- None that survive filtering (parser artifacts, style nitpicks, etc., removed per instructions).

## Nice-to-Haves

- A hyperparameter sensitivity experiment (e.g., sweep learning rate × optimizer × training length on one representative dataset) showing rank stability would dramatically strengthen the paper.
- Measuring peak GPU memory during training (e.g., with `nvidia-smi` or TensorFlow memory hooks) for each model at the same batch size would validate or qualify the memory footprint claim.
- The isolated VGG exception on masked UPM-GTI-Face could be better explained (e.g., does VGG's smaller effective receptive field interact favorably with small masked face crops?).

## Removed Points

These points were raised by reviewers but removed after verification against the paper:

- **"LFW results are near-saturated and add little"** → The paper itself acknowledges this (Section 3.4: "the LFW dataset, being an older dataset, does not pose a substantial challenge"). The authors correctly use LFW as a sanity check. Not a weakness.
- **Generic formatting/style nitpicks, missing appendix concerns** → Parser artifacts, not author errors.
- **Missing related works** → Cannot verify without external sources; outside scope.

## Novel Insights

The most notable insight from comparing these reviews is that the paper's core empirical finding — ViT maintains discriminative embeddings at distances where CNNs collapse to random — is robust enough to survive the methodological concerns. Even if hyperparameter tuning narrowed the gap, the 30-meter result (AUC 0.63 vs. ~0.5) is so large that it would likely persist. However, the paper's weakness is not in any single experimental result but in the framing: it presents itself as a "comprehensive comparison" that justifies a general claim of ViT superiority, when the actual evidence is more consistent with "ViT performed best under one specific training configuration we tested." The former requires robustness checks the paper lacks; the latter is what the data actually supports.

## Suggestions

1. Add a hyperparameter sensitivity analysis — even a limited sweep (e.g., two learning rates × Adam vs. SGD × 50 epochs) on a representative subset — and show that the ranking of architectures is stable.
2. Measure and report peak GPU memory usage during training for each model at the same batch size.
3. Add bootstrap confidence intervals for AUC/EER on the smaller datasets (UPM-GTI-Face, SCface subsets) to quantify variability.
4. Report data augmentation details, or explicitly state that none was used.
5. Report inference time over multiple runs (e.g., mean ± std over 10 trials) rather than a single measurement.
6. Discuss the potential confound of ImageNet pre-training favoring ViTs in the limitations section.
7. Soften the abstract's claim about memory footprint — change "presenting a smaller memory footprint" to "theoretically offering a smaller memory footprint" or provide the measurement to back it up.

## Score and Decision

This paper tackles a relevant and timely question, assembles a diverse set of evaluation datasets, and produces genuinely interesting results — particularly ViT's maintained performance at 30 meters where CNNs collapse. The experimental design is transparent and reproducible, and the honest reporting of the VGG exception adds credibility. However, the paper's central weakness is structural: as a comparative study claiming superiority of one architecture class, it relies on a single, untested hyperparameter configuration with no robustness checks, and it makes an unsubstantiated claim about memory footprint in the abstract. These are not minor omissions — they directly affect the believability of the paper's main conclusions. The experiments are well-executed for what they are, but the conclusions go beyond what the evidence supports. With additional experiments addressing hyperparameter sensitivity and memory measurement, the paper could become a useful empirical contribution. In its current form, the gap between the claims and the evidence is too wide.

MY FINAL SCORE: <pineapple>5.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>