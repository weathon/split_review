Now I have all the information needed to verify each claim. Let me write the final consolidated review.

## Summary

This paper investigates the generalization problem in AI-generated image detection. Through empirical analysis of six low-level features across 16 forgery types, the authors demonstrate that different low-level features exhibit complementary generalization strengths and that naive fusion (early/late) is insufficient. They propose the Adaptive Low-level Experts Injection (ALEI) framework, which uses LoRA experts for each modality, cross-low-level attention for feature fusion, a low-level information interaction adapter to preserve features through deep layers, and dynamic feature selection for per-image adaptive classification. Trained on only four ProGAN categories, ALEI achieves SOTA results (+3.44% on AIGCDetectBenchmark, +2.1% on GANGenDetection, +2.0% on UniversalFakeDetect) across multiple unseen GAN and diffusion test sets.

## Strengths

1. **Clear empirical motivation grounded in analysis**: Section 3.1 and Figure 1 demonstrate that different low-level features (NPR, DnCNN, NoisePrint, etc.) have complementary generalization patterns — NPR excels on StyleGAN/BigGAN, while DnCNN and NoisePrint perform better on diffusion models. This provides a concrete, data-driven rationale for fusing multiple low-level cues rather than relying on a single one.

2. **Novel adaptive fusion framework with validated components**: The ALEI framework integrates four components (LoRA Experts, Cross-Low-level Attention, Low-level Information Interaction Adapter, Dynamic Feature Selection) in a principled manner. Table 5 systematically ablates each component, showing that even after controlling for the LoRA experts (LE), the fusion components CLA, LIIA, and DFS each contribute measurable gains (+1.7%, +0.6%, +1.7% respectively), confirming their individual utility.

3. **Strong and consistent SOTA results across multiple benchmarks**: The method outperforms prior methods by clear margins on three different benchmarks covering 16+ unseen forgery types from both GAN and diffusion families, all while training on only ProGAN data. This provides strong evidence that the adaptive fusion design transfers well.

4. **Dynamic Feature Selection provides interpretable per-image adaptation**: Figure 4 and Section 4.4 show that the router learns to weight different low-level features differently depending on the forgery type (e.g., relying more on Image+NPR for StyleGAN/BigGAN, and DnCNN+NoisePrint for ADM/Stable Diffusion), giving both adaptive behavior and a degree of interpretability.

## Weaknesses

### Fatal
None.

### Major

1. **Uneven late-fusion baseline in the ablation study conflates capacity with fusion design**. The ablation baseline (Table 5, first row: 77.3% Acc.) uses a frozen backbone with only the FC layer fine-tuned, while the late fusion described in Section 3.2 uses LoRA-trained backbones. The first component added (LE/LoRA Experts) jumps to 85.8% (+8.5%), partly reflecting the introduction of additional trainable parameters — not just per-modality expert design. The subsequent gains from CLA, LIIA, and DFS (+4.0% combined) cleanly isolate the fusion architecture. To fully substantiate the claim that the fusion design itself drives performance, the paper should include a stronger baseline that matches ALEI's total trainable parameters using a simpler fusion strategy (e.g., concatenated tokens with end-to-end LoRA but no cross-attention/adapter/router). This would isolate the benefit of the adaptive fusion mechanism from the benefit of simply having more capacity.

### Minor

2. **Choice of three low-level features lacks sufficient justification**. The paper evaluates six features in Section 3 but then restricts to NPR, DnCNN, and NoisePrint citing "superior performance" and "Occam's Razor" (line 83). Table 4 shows performance with 1, 2, and 3 features but does not include results with all six, or a systematic analysis showing the excluded features (SRM, Bayar, LNP) are redundant rather than simply set aside. If the excluded features provide complementary signal for certain forgery types, the reported performance may not be the best achievable. An ablation showing "adding LNP/SRM/Bayar to the three-feature set yields X%" would resolve this.

3. **Training procedure underspecified**. Section 4.5 describes two-stage training: first train LoRA experts and the low-level encoder, then load these weights and train the fusion module. It does not state whether the pre-trained LoRA experts and low-level encoder are **frozen or fine-tuned** in the second stage. This is critical for reproducibility and for understanding whether stage 1 is merely initialization or provides fixed feature extractors.

4. **Section 3 analysis lacks numerical values**. The key motivation for the entire framework rests on Figure 1 (radar chart), which is difficult to read precisely. The claims about which features work best for which forgery types and the quantitative gap between individual features and fusion strategies would be substantially stronger with a companion table reporting accuracy numbers.

5. **Low-level encoder initialization not specified**. Section 4.3 states the adapter uses "the first two blocks of ResNet50" but does not state whether these are pretrained (e.g., on ImageNet) or randomly initialized. This matters because pretrained vs. random initialization affects both performance and comparability with other methods that use pretrained backbones.

6. **Router generalization claim could be better supported**. Figure 4 shows dynamic feature selection weights on test data, but the router is trained only on ProGAN. Showing sensible weights on test data does not guarantee the router has learned a generalizable selection strategy — it could be overfitted to ProGAN and coincidentally produce reasonable weights. Comparing router behavior on training vs. test data, or showing router decisions on OOD examples, would strengthen the claim.

7. **DIRE-D included in benchmark averages despite different training distribution**. The paper acknowledges DIRE-D is trained on ADM rather than ProGAN (line 185), but still includes it in aggregate comparisons. While common in the field, mixing training distributions in averaged results is methodologically imprecise and should either be separated or explicitly discussed.

### Trivial

8. The number of attention heads is specified (4) for the cross-low-level attention, but the Q/K/V dimensionality is not explicitly stated.

9. The low-level interaction adapter is described as operating "for each modality feature of the i-th block" without specifying the set of blocks (all N blocks? a subset?) where it is applied.

## Nice-to-Haves

- A matched-capacity simple-fusion baseline (same number of LoRA parameters, same end-to-end training, but simple concatenation + classifier head) would strengthen the central claim that the fusion architecture — not just capacity — drives the +12.5% improvement.
- An ablation with all six low-level features would either justify the three-feature restriction or uncover additional gains.
- Comparing router selection weights on training data vs. test data (not just showing test weights) would clarify whether the router generalizes or overfits.

## Removed Points

These points are flagged to be removed, treat them with caution:
- **Title typo ("AI-generateted")**: Parser artifact. The original submission does not have this issue.
- **"Results tables as images, should be machine-readable"**: Formatting nitpick. Tables embedded as images in PDFs is standard practice for complex table formatting.
- **"Section 3 analysis only radar chart without numbers"**: This was kept as a minor weakness (item #4 above) because it is a substantive evidential concern, not a formatting issue. Retained with appropriate severity.
- **"Cross-attention/adapter dimensionality not specified"**: Already captured more succinctly in trivial items #8-9.

## Novel Insights

None beyond the paper's own contributions. The reviews confirm that the paper's main insight — that different low-level features are complementary across forgery types and require adaptive fusion — is both novel and well-grounded. The harsh critic's observation about the baseline capacity confound is a methodological critique, not an insight the paper itself missed.

## Suggestions

1. Add a matched-capacity baseline: train end-to-end LoRA on all modalities with simple concatenation + classifier (no cross-attention, no adapter, no router). This isolates the benefit of the adaptive fusion architecture.
2. Specify which parameters are frozen vs. fine-tuned in stage 2 of training.
3. Add a small table to Section 3 with numerical accuracy values for each of the 6 features on the 16 forgery types (or aggregated categories).
4. Either include results with all six low-level features, or provide a clear redundancy analysis showing the three excluded features offer no marginal benefit.
5. Specify whether the ResNet50 blocks in the low-level adapter are pretrained or randomly initialized.

## Score and Decision

The paper presents a well-motivated, technically sound, and empirically strong framework for AI-generated image detection. The core idea — that different low-level cues are complementary and require adaptive fusion — is validated through both analysis and extensive experiments. The weaknesses identified are addressable and do not threaten the paper's central contributions. The method is an original combination of existing techniques (LoRA, cross-attention, adapters, mixture-of-experts routing) applied to a well-defined problem, and the results are convincingly state-of-the-art.

MY FINAL SCORE: <pineapple>7.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>