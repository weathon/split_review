## Summary

This paper proposes the Adaptive Low-level Experts Injection (ALEI) framework for generalizable AI-generated image detection. The key idea is to fuse multiple types of low-level information (NPR, DnCNN, NoisePrint) with RGB features using a ViT-based architecture with per-modality LoRA experts, cross-low-level attention, a low-level information interaction adapter, and dynamic feature selection. The method achieves SOTA results across three benchmarks (AIGCDetect, GANGenDetection, UniversalFakeDetect) when trained only on ProGAN data.

## Strengths

- **Systematic empirical analysis of low-level features (Section 3)**: The paper evaluates six low-level features across 16 forgery types and demonstrates that different features excel on different generators (NPR on GANs, DnCNN/NoisePrint on diffusion models). This is supported by a radar chart (Fig. 1) and t-SNE visualizations (Fig. 4), and provides concrete justification for multi-feature fusion rather than relying on any single low-level signal.

- **Demonstration that simple fusion is insufficient (Section 3.2)**: The authors test early and late fusion strategies and show they underperform, providing direct experimental motivation for the proposed architecture rather than asserting the need without evidence.

- **Complete ablation study (Table 5)**: Each component (LoRA experts, cross-low-level attention, low-level information adapter, dynamic feature selection) is ablated and shown to contribute positively (+12.5% Acc. total). This granularity is rare and gives confidence that the design choices are non-redundant.

- **Consistent SOTA results across diverse benchmarks (Tables 1–3)**: The method outperforms prior work on AIGCDetectBenchmark (+3.44%), GANGenDetectionBenchmark (+2.1%), and UniversalFakeDetectBenchmark (+2.0% over NPR, +3.4% over FAFormer on diffusion data). These gains are from a model trained only on ProGAN, demonstrating genuine generalization.

## Weaknesses

### Major

- **The central claim — that *diverse* low-level features drive the gains — is not disentangled from increased model capacity.** The baselines (LNP, NPR, LGrad, DIRE, etc.) each use a single low-level feature with a lighter architecture. ALEI runs four parallel streams through a ViT-L backbone with additional LoRA experts, cross-attention layers, an interaction adapter, and a router with multiple classification heads — substantially more parameters. The paper does not control for this: if one took the single best low-level feature (e.g., NPR) and scaled up the model to roughly the same total parameter count, would similar gains appear? A control experiment where all four "modalities" use the same low-level feature (e.g., NPR repeated four times with independent LoRA experts) is needed to attribute the improvement to feature *diversity* rather than architectural capacity. This is the paper's most important unaddressed question.

### Minor

- **The "adaptive" nature of the dynamic feature selection is asserted but under-validated.** Fig. 4 (rightmost column) shows bar charts of feature selection distributions across forgery types, which is helpful. However, there is no quantitative analysis: How often does the router assign non-trivial weight to more than one modality? How much does the routing distribution vary across forgery types vs. across individual samples of the same type? Does the entropy regularization loss actually prevent collapse to a single modality? The paper's headline framing makes adaptivity a core contribution, so the evidence should be commensurate.

- **No variance or statistical significance reporting.** The paper reports Acc. and A.P. as point estimates without standard deviations or multiple runs. For claimed improvements of 2–3.4%, variance could affect the ranking. This is the single most impactful missing piece in the experimental section.

- **No comparison of computational cost.** ALEI processes four parallel streams through a ViT-L backbone with LoRA adapters, cross-attention at every block, a ResNet50-based encoder, and injector/extractor modules. The paper reports no FLOPs, parameter count, inference time, or GPU memory — making it impossible to assess whether the accuracy gains come at a proportional or disproportionate cost relative to single-feature baselines.

- **Citation errors (lines 199 and 205).** In the SOTA Methods list (line 185), NPR is correctly cited as (Tan et al., 2023a) and FAFormer as (Liu et al., 2023a). But in the GANGenDetection discussion (line 199), NPR is cited as (Liu et al., 2023a), and in the UniversalFakeDetect discussion (line 205), the citations for NPR and FAFormer are swapped. While minor, these are factual errors in the body text.

- **CNNDetectionBenchmark listed as a testing dataset (line 183) but no results table is shown.** The paper lists it alongside three other benchmarks for which results are reported (Tables 1–3), but no corresponding table appears for CNNDetectionBenchmark. If results are in the appendix (stripped during parsing), the main text should reference them.

- **Two-stage training procedure (Section 4.5) is described but not motivated.** The paper first trains LoRA experts and encoders, then loads these weights and trains the fusion module. There is no discussion of why end-to-end training was not used, or whether the two-stage approach could cause the LoRA experts to overfit to the classification task without the context of the fusion mechanism.

### Trivial

- The citation error noted above (lines 199, 205) should be corrected.

## Nice-to-Haves

- **Model-capacity control experiment**: Run ALEI with all four "modalities" set to the same low-level feature (e.g., NPR repeated four times with independent LoRA experts). If performance drops vs. the diverse-feature version, this directly attributes the gain to feature diversity rather than capacity.
- **Quantify router behavior**: Report average routing entropy across the test set, variance of routing weights across forgery types, and a confusion-matrix-style visualization of which features are preferred for which forgery types.
- **Limitations paragraph**: Acknowledge the framework's computational overhead relative to single-feature methods, the dependency on the specific choice of low-level features, and the lack of evaluation on in-the-wild post-processed images (JPEG compression, resizing).
- **Discussion of failure cases**: Every ablation shows monotonic improvement; identifying forgery types or conditions where multi-feature fusion hurts would strengthen the narrative.

## Removed Points

*These points were flagged by a reviewer but are not included as weaknesses in the main review. They are listed here for completeness, but should be treated with caution.*

1. **"How many transformer blocks have cross-low-level attention?"** — The paper defines features indexed by block number (i = 0,1,...,N) and notes the cross-attention layer is applied "in the original output section" of each block. This is sufficiently clear from context; the concern reflects a misreading.
2. **"Low-level interaction adapter — for what input?"** — The paper states: "utilize the first two blocks of ResNet50... to project the low-level information C1, C2, ..., CM into D dimensions." This is unambiguous.
3. **"No failure case discussion"** — A reasonable suggestion but not a weakness; moved to Nice-to-Haves.
4. **Pure formatting/style nitpicks** — Removed as parser artifacts.
5. **Generic complaints about missing appendix content** — The parser strips supplementary material from all papers; these are not author omissions.

## Novel Insights

None beyond the paper's own contributions. The reviewer inputs did not surface any genuinely novel synthesis or observation that the paper itself does not provide.

## Suggestions

- Add a control experiment using repeated identical features (e.g., NPR×4) to disentangle feature diversity from model capacity.
- Report router metrics (average entropy, per-forgery-type weight distributions, variance across samples) to substantiate the "adaptive" claim.
- Add standard deviations or confidence intervals to all main results (Tables 1–3).
- Report parameter count and inference time for ALEI vs. key baselines.
- Fix the swapped citations for NPR and FAFormer (lines 199, 205).
- Add a brief motivation for the two-stage training procedure.

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>