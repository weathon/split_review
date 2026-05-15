Now I have a thorough understanding of the paper and verified all claims. Let me construct the final consolidated review.

## Summary

This paper tackles the problem of generalizable AI-generated image detection. The authors first demonstrate through systematic analysis that different types of low-level features (e.g., NPR, DnCNN, NoisePrint) exhibit complementary generalization strengths across different forgery types (GANs vs. diffusion models). They then propose the Adaptive Low-level Experts Injection (ALEI) framework, which fuses multiple low-level information modalities with RGB input via three key components: LoRA-based expert modules with cross-low-level attention, a low-level information interaction adapter, and a dynamic feature selection mechanism. Evaluated on three benchmarks, the method achieves consistent improvements over prior state-of-the-art approaches.

## Strengths

1. **Empirical demonstration of complementary low-level feature behavior**: Section 3.1 systematically evaluates 6 low-level features across 16 forgery types and shows that NPR excels on StyleGAN-based forgeries while DnCNN and NoisePrint perform better on diffusion-model outputs (Fig. 1). This insight is genuinely novel and well-supported, providing a clear motivation for multi-modal fusion that distinguishes this work from prior single-extractor methods (LNP, NPR, etc.).

2. **Adaptive fusion via Dynamic Feature Selection (DFS)**: The DFS module (Section 4.4) learns to weight modality features per image rather than using static concatenation/averaging. The ablation (Table 5) confirms DFS contributes positively on its own, and the t-SNE visualization (Fig. 4) provides direct evidence that the router selects different features for different forgery types (e.g., BigGAN vs. Stable Diffusion), validating the adaptive behavior.

3. **Cross-Low-level Attention layer for intermediate fusion**: Unlike simple early or late fusion (shown to be suboptimal in Section 3.2), the proposed cross-attention mechanism (Eq. 2) integrates features from different low-level experts within each transformer block while preserving modality-specific characteristics. The ablation (Table 5) demonstrates that combining all components yields a +12.5% Acc. improvement over the late-fusion baseline using the same inputs.

4. **Consistently strong empirical results**: The method achieves SOTA on AIGCDetectBenchmark (Table 1, +3.44% over prior best), GANGenDetectionBenchmark (Table 2, +2.1% Acc. over NPR), and UniversalFakeDetect for diffusion models (Table 3, +2.0% Acc. over NPR), with gains across both GAN and diffusion test sets. These results support the claim of improved generalization.

5. **Thorough ablation isolating each component's contribution**: Tables 4 and 5 systematically ablate low-level feature combinations and each architectural component (LoRA Expert, Cross-Low-level Attention, Low-level Information Adapter, Dynamic Feature Selection), providing transparent evidence for design choices.

## Weaknesses

### Fatal
None.

### Major

1. **Potential data leakage from pre-trained low-level feature extractors**: The paper uses NPR, DnCNN, and NoisePrint as fixed pre-trained feature extractors but never discloses their training data or verifies independence from the test generator families (StyleGAN, BigGAN, ADM, Stable Diffusion, etc.). NPR (Tan et al., 2023a) was designed to detect GAN upsampling artifacts, DnCNN-based methods (Corvi et al., 2023) have been used for GAN detection, and NoisePrint (Guillaro et al., 2023) is trained via contrastive learning on manipulated images. If any of these extractors were exposed to the same generator families used for evaluation, then the low-level features they produce may already encode discriminative patterns specific to those generators, creating an indirect leakage pathway. This concern is **not fatal** because: (a) the extractors are used as fixed pre-processing—the paper's trainable components (LoRA experts, fusion, DFS) demonstrably improve over simple fusion of the *same* inputs, so the relative contribution of the framework itself remains valid; (b) this issue applies broadly to any work using pre-trained forensic feature extractors. However, the paper should discuss this limitation and ideally verify independence or bound its impact.

### Minor

2. **Qualitative-only motivation for the fusion design (Section 3.2)**: The analysis motivating why simple fusion is insufficient relies entirely on a radar chart (Fig. 1) without quantitative results or statistical significance. While this section serves as motivation rather than core evaluation, the paper would be strengthened by reporting numerical accuracy values for the early/late fusion baselines to substantiate the claim that "simple fusion mechanisms prove inadequate."

3. **Underspecified extraction pipelines for low-level features**: The paper does not specify the exact computation pipeline for each low-level feature extractor (e.g., for NPR: which checkpoint, pre-processing, normalization; for DnCNN: is the feature the denoised image or the residual noise map; for NoisePrint: which layer's output). While citing the original papers is standard, the lack of specification makes it difficult to reproduce results or assess whether gains come from careful engineering of the extractors versus the fusion framework itself.

4. **ResNet50 adapter initialization unspecified**: The Low-level Information Adapter (Section 4.3) uses the first two blocks of ResNet50, but the paper does not state whether these are ImageNet-pretrained or randomly initialized and trained from scratch. If pretrained, there is a domain mismatch between ImageNet and low-level feature maps (noise residuals, upsampling artifacts).

5. **No discussion of limitations or computational cost**: The conclusion (Section 6) is a summary without any discussion of limitations, failure cases, computational overhead, or sensitivity to the choice of low-level extractors. Including these would strengthen the paper's scientific rigor.

### Trivial

6. **t-SNE bar chart (Fig. 4, rightmost column) unclear**: The bar chart showing feature selection distribution is small and lacks a clear axis label—it is not immediately obvious whether the bar height represents frequency of selection, average weight, or another metric across the test set.

## Nice-to-Haves

- A quantitative analysis of the DFS router weights (e.g., average weight vector per test generator) to directly validate that the router learns to select NPR for GAN-type forgeries and DnCNN/NoisePrint for diffusion-type forgeries, as the t-SNE visualization suggests.
- An experiment showing performance with all 6 low-level features (rather than the selected 3) to quantify the marginal benefit of adding more modalities and test whether the fusion framework scales.
- Visualization of the extracted low-level feature maps (NPR residual, DnCNN noise, NoisePrint) for a few sample images to help readers interpret what information each modality provides.

## Removed Points

These points are flagged to be removed; treat them with caution:

- **"Missing simple fusion baseline in ablation (Table 5)"** — REMOVED (misreading). The reviewer claimed the baseline "w/o all (Image only)" uses only RGB images. However, the paper's text explicitly states: "compared to using only low-level information and Image as input, followed by late fusion and fine-tuning the fully connected layer." This IS the simple fusion baseline using all the same multi-modal inputs. The criticism is factually incorrect.

- **"Baseline numbers from different splits"** — REMOVED (generic concern). The claim that "some baselines may have been evaluated on different splits" is a generic concern applicable to virtually all benchmark comparisons. The paper cites specific papers for baseline numbers, which is standard practice.

- **"Selection of only 3 features using Occam's Razor is hand-wavy"** — REMOVED (scope creep). The paper tested 6 features empirically and chose the 3 best performers. This is a standard, reasonable methodology, not a weakness.

- **"Missing related works"** — REMOVED per instructions (cannot confirm existence of missing references).

## Novel Insights

The key insight emerging from the reviews is that the paper's central claim—that different low-level features are complementary across generator types and that adaptive fusion outperforms simple fusion—is well-supported by the ablation study (Table 5), which shows a +12.5% improvement over the late-fusion baseline using the *same* multi-modal inputs. However, the unresolved question about feature extractor independence means the absolute performance numbers should be interpreted with some caution, even though the relative comparisons within the paper's own framework remain valid. The DFS router visualization (Fig. 4) provides direct behavioral evidence that the adaptive mechanism works as intended, which is a stronger form of validation than many fusion methods provide.

## Suggestions

1. **Address the data leakage concern directly**: In a camera-ready version, state the training data and methodology for each low-level extractor (NPR, DnCNN, NoisePrint) and explicitly verify whether any were trained on the generator families used for evaluation. If overlap exists, bound its impact by removing that extractor and reporting the change in results, or use independently trained versions. At minimum, add a paragraph discussing this limitation.

2. **Add a table with numerical accuracy values for the early/late fusion analysis in Section 3.2** to provide quantitative support for the claim that simple fusion is insufficient.

3. **Specify exact extraction pipelines**: Provide model checkpoints, pre-processing steps, normalization, and the specific output representation used for each low-level feature type (NPR, DnCNN, NoisePrint). State whether the ResNet50 blocks in the adapter are pretrained on ImageNet or randomly initialized.

4. **Add limitations discussion**: Include a paragraph on limitations, failure cases, and computational cost in the conclusion.

## Score and Decision

The paper makes a genuine contribution: it identifies complementary generalization behavior across different low-level features and designs a principled adaptive fusion framework that consistently outperforms prior methods. The most serious issue (potential data leakage from pre-trained extractors) is a transparency gap rather than a fatal flaw, since the relative comparisons in the ablation—which demonstrate the framework's advantage over simple fusion of the same inputs—remain valid. The paper would benefit from addressing the reproducibility gaps and adding a limitations discussion, but the core contributions are solid.

MY FINAL SCORE: <pineapple>7.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>