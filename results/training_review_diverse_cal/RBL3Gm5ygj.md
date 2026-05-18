Now I have a thorough understanding of the paper and the reviews. Let me compose the final consolidated review.

---

## Summary

This paper presents MM-SAM, an extension of the Segment Anything Model (SAM) to multi-modal sensor data. It introduces two key designs: **Unsupervised Cross-Modal Transfer (UCMT)** that aligns non-RGB embeddings with SAM's RGB latent space via an L2 unification loss, and **Weakly-supervised Multi-Modal Fusion (WMMF)** with a Selective Fusion Gate (SFG) that adaptively weights modalities at the patch level. Both modules are parameter-efficient (adding 492.9K–9.7M parameters to SAM's 91M) and label-efficient (requiring no mask annotations). Evaluated on seven datasets across eight modalities (thermal, depth, LiDAR, HSI, MS-LiDAR, SAR, DSM), MM-SAM consistently improves over SAM baselines by large margins, e.g., RGB+Thermal fusion achieves 75.9 mIoU on MFNet vs. SAM RGB's 68.2.

## Strengths

1. **Effective cross-modal adaptation via embedding alignment.** The UCMT loss aligns non-RGB embeddings with SAM's RGB space using only lightweight trainable components. Results are striking: thermal improves from 64.5 to 72.3 mIoU on MFNet, depth from 68.1 to 77.2 on SUN RGB-D, LiDAR from 60.1 to 68.7 on SemanticKITTI (Table 2). This validates the core idea that SAM's latent space can be shared across sensor modalities.

2. **Adaptive multi-modal fusion through Selective Fusion Gate (SFG).** The patch-wise weighted fusion mechanism (Eq. 2) dynamically adjusts modality contributions based on scene content. Figure 5 provides compelling visual evidence: under glare from car headlights, SFG assigns higher weight to the thermal modality, leading to correct segmentation. Fusion consistently outperforms the best single modality across all datasets (e.g., RGB+Thermal 75.9 vs. Thermal 72.3 on MFNet; RGB+Depth 81.2 vs. Depth 77.2 on SUN RGB-D; RGB+LiDAR 69.9 vs. LiDAR 68.7 on SemanticKITTI).

3. **Parameter-efficient and label-efficient adaptation.** Table 1 shows total added parameters range from 492.9K to 9.7M depending on input channels — a tiny fraction of SAM's 91M parameters. The entire pipeline is trained without mask annotations: UCMT uses unlabeled modality pairs, and WMMF uses pseudo-labels from geometric prompts. This is a practical contribution for deploying SAM with new sensor suites.

4. **Broad applicability across diverse sensor types.** Evaluations span 7 datasets and 8 modalities (thermal, depth, LiDAR, HSI, MS-LiDAR, SAR, DSM) across both time-synchronized and time-asynchronized settings. The method scales to high-dimensional inputs (48-channel HSI at 9.7M parameters) and multiple modalities simultaneously (RGB+HSI+MS-LiDAR achieving 89.3 IoU on DFC2018, the best among all combinations).

5. **Scalable to non-RGB fusion and zero-shot transfer.** MM-SAM can fuse two non-RGB modalities (HSI+MS-LiDAR: 86.5 IoU) without RGB at inference time, expanding deployment to sensor suites without RGB cameras. Zero-shot experiments (MFNet→FreiburgThermal, SUN RGB-D→NYU/B3DO) show consistent improvements over SAM, indicating learned representations transfer across domains.

6. **Ablations on PEFT methods and backbones.** MM-SAM is evaluated with three PEFT methods (LoRA, AdapterFormer, VPT) and three ViT backbones (B, L, H), showing consistent improvements over SAM across all configurations. This demonstrates the framework's robustness to architectural choices.

## Weaknesses

### Fatal
None.

### Major

1. **Missing ablations that isolate the contributions of the two core components.** The paper's central claim is that UCMT and WMMF (with SFG) are the *designs* driving improvements, but neither component is ablated against a simpler alternative:
   - **UCMT without the unification loss:** The reviewer reasonably asks: if you simply train a new patch embedding for each non-RGB modality (adjusting input channels, fine-tuning with LoRA) *without* the L2 alignment loss $L_U$, how much performance do you retain? The unification loss is presented as a key contribution, but the paper never measures its marginal benefit. Since the patch embedding is already being trained from scratch, it is plausible that simply adapting the input layer accounts for most of the gain.
   - **SFG vs. simple fusion alternatives:** Does the learned per-patch weighted combination outperform a simple learned linear projection of concatenated/averaged embeddings? The selective gate is the core of WMMF, but no comparison against a trivial fusion baseline is provided.
   
   Without these ablations, the reader cannot tell whether the two named "designs" are responsible for the measured improvements, or whether the gains come from more basic input adaptation and feature concatenation. This is the most significant weakness in the paper.

2. **Pseudo-label training quality is unanalyzed.** WMMF trains the SFG using pseudo-labels derived from the model's own single-modality predictions (self-training). This risks confirmation bias: the fusion module learns to match a target that may be noisy, particularly in regions where both single-modality predictions are uncertain. The paper provides no quantitative analysis of pseudo-label quality — no oracle upper bounds, no confidence threshold analysis, no pixel-level agreement rates between single-modality predictions and the fused pseudo-label. The visual example in Figure 5 is illustrative but insufficient to characterize this across the dataset.

### Minor

1. **Small-scale evaluation on time-asynchronous datasets.** DFC2018 has only 12 training images and 2 test images; ISPRS Potsdam uses 32 training and 6 test images. Results on such tiny test sets are fragile — a single image's quirks can shift aggregate metrics noticeably — and no error bars are provided. The paper should either report variance across splits or explicitly frame these as proof-of-concept results.

2. **No comparison to non-SAM multi-modal segmentation methods.** While the paper's framing is about extending SAM, comparing to a lightweight non-foundation multi-modal segmentation baseline (e.g., a simple fusion network trained from scratch) on at least one dataset would help contextualize the value that SAM's pretrained representations bring. Without this, the claim of "superior multi-modal segmentation" is only verified against SAM variants, not against the broader segmentation literature.

3. **L2 unification loss chosen without ablating alternatives.** The L2 loss forces non-RGB embeddings to exactly match RGB embeddings. This may discard modality-specific structure that could still be compatible with SAM's prompt encoder and mask decoder. An ablation comparing L2 against contrastive or cosine alignment losses would strengthen the contribution.

4. **Limited discussion of failure cases.** The Limitations section mentions computational cost and the need for paired RGB training data, but does not discuss scenarios where MM-SAM *worsens* results relative to using RGB alone or where the SFG weights are suboptimal. For a method that claims adaptive robustness, acknowledging failure modes would strengthen credibility.

### Trivial

1. The Limitations section could be expanded to discuss whether the SFG correctly downweights modalities under severe misalignment or occlusion, beyond the one success case shown in Figure 5.

## Nice-to-Haves

- **More challenging zero-shot transfer.** The MFNet→FreiburgThermal transfer is between two thermal road-scene datasets. A cross-domain zero-shot experiment (e.g., thermal autonomous driving → indoor depth) would be more convincing, though the positive results shown are already a useful signal.
- **Error bars for small-dataset results.** Cross-validation or repeated train/test splits for DFC2018 and ISPRS Potsdam would help assess statistical significance.
- **Oracle bound for pseudo-label training.** Reporting an upper bound (training SFG with ground-truth masks on a small subset) would clarify the gap between the pseudo-label approach and fully supervised fusion.

## Removed Points

- *"Reproducibility details missing (prompts per image, batch size, learning rate, SFG architecture)"* — These details are standard in the appendix, which was stripped by the parser. The paper states details are provided in supplementary material. Removed per the rule about missing appendix content.
- *"The paper should compare to SAM-Adapter and other SAM domain adaptations"* — The paper's scope is multi-modal *sensor suites* (fusion of heterogeneous sensors), not single-modality domain adaptation. SAM-Adapter et al. address a different problem (adapting SAM to a single non-RGB domain). The paper discusses these works in Related Works. Removed as scope creep.
- *"Zero-shot results should include more diverse transfer"* — This is a suggestion for expansion, not a weakness. The zero-shot experiments provided are already positive evidence. Moved to Nice-to-Haves.
- *"The paper should compare against fully supervised segmentation methods"* — The paper's contribution is an *extension of SAM*, not a new general-purpose segmentation architecture. Comparing to non-SAM methods would evaluate a different claim. Removed per the rule about evaluating against the wrong class of expectations.

## Novel Insights

The most interesting observation emerging from the reviews is the tension between the paper's ambitious scope (7 datasets, 8 modalities, zero-shot, multi-modal fusion) and the relatively thin experimental validation of its *specific design choices*. The paper convincingly shows that *something* in the MM-SAM pipeline works well across diverse settings, but it does not isolate *which parts* drive the gains. This is a common pattern in systems papers that propose a full pipeline: the whole works, but the attribution of credit to individual components remains uncertain. A sharper insight is that the unification loss strategy — forcing non-RGB embeddings to exactly match RGB embeddings in SAM's latent space — is so simple that one might expect it to fail, yet the empirical results suggest SAM's latent space is surprisingly accommodating of cross-modal alignment. This robustness of SAM's latent space to non-RGB inputs (after lightweight adaptation) is itself an interesting finding that the paper could emphasize more.

## Suggestions

1. **Add the two critical ablations.** The most impactful improvement would be to compare (a) UCMT with vs. without the unification loss (i.e., just training the patch embedding and LoRA adapters), and (b) SFG against a simple learned linear fusion (concatenation + projection or weighted averaging). If the proposed components outperform these simpler alternatives, the contributions are substantially validated; if not, the claims need to be adjusted.

2. **Analyze pseudo-label quality quantitatively.** For at least one dataset, report the agreement rate between single-modality predictions and the fused pseudo-label, show the distribution of fusion weights, and compare against an oracle bound where SFG is trained with ground-truth masks.

3. **Add error bars or cross-validation** for the small asynchronous datasets (DFC2018, ISPRS Potsdam) to indicate whether the improvements are statistically robust.

4. **Add a qualitative failure case** to balance the success case in Figure 5 — showing when SFG weights are suboptimal would increase trust in the method's claimed adaptivity.

## Score and Decision

The paper presents a well-motivated, practical extension of SAM to multi-modal sensor data with consistent gains across a broad set of modalities and datasets. The core weakness is that the two named design contributions (unification loss and selective fusion gate) are not ablated against simpler alternatives, making it difficult to attribute the observed improvements to the specific designs rather than basic input adaptation. This is a significant gap but not a fatal flaw — the overall pipeline works, and the missing ablations are well-scoped experiments that could be added. The contributions are real, the evaluation is broad, and the practical impact (label-efficient, parameter-efficient adaptation of SAM to new sensor types) is clear. I recommend acceptance conditional on the authors addressing the missing ablations.

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>