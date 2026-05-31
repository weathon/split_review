## Human Reviewer 1

### Summary
This paper proposes Vision Filter (ViF), a novel vision backbone that replaces Transformer self-attention with a Fourier Neural Filter (FNF). Built upon the Fourier Neural Operator (FNO), FNF introduces adaptive modulation and selective activation to dynamically couple spatial and frequency-domain representations, addressing FNO’s limitations in modeling high-frequency local details. Experiments on classification, detection, and segmentation show that ViF achieves competitive or superior performance to Swin Transformer, ConvNeXt, and VMamba while maintaining quasi-linear complexity.

### Strengths
1. The paper provides a clear theoretical motivation.
2. The introduced adaptive modulation and selective activation mechanisms effectively mitigate the over-smoothing and bandwidth bottleneck issues of conventional FNOs.
3. Experiments on classification, detection, and segmentation tasks demonstrate consistent improvements over strong baselines such as ConvNeXt, Swin, and VMamba, confirming the model’s effectiveness and generality.

### Weaknesses
1. The ablation study is relatively limited, providing insufficient analysis of the independent contributions of the two key FNF submodules. A more detailed exploration of how each component individually influences performance would strengthen the empirical validation.
2. The paper lacks interpretability analysis. Although the authors claim that adaptive modulation adaptively scales different frequency components in the spectral domain, the explanation remains purely mathematical without concrete visualization or empirical evidence. It is unclear how the modulation behaves across different images or tasks and whether any consistent adaptation patterns exist.
3. The comparison with recent state-of-the-art methods are missing, such as MLLA and OverLoCK.
4. In Table 3, the performance improvement under the Mask R-CNN 3× MS schedule is marginal. The paper does not discuss possible reasons for this weak gain.

### Questions
See weaknesses.

### Soundness
3

### Presentation
3

### Contribution
3

### Rating
6

### Confidence
3

---

## Human Reviewer 2

### Summary
This manuscript proposes a novel visual backbone network called Vision Filter (ViF). Its innovation lies in the introduction of a core component, the Fourier Neural Filter (FNF). Building on the Fourier Neural Operator (FNO), FNF introduces an input-dependent adaptive integral kernel. Through selective activation and adaptive modulation, it establishes a dynamic information flow between the frequency and time domains, addressing the bandwidth bottleneck and over-smoothing issues inherent in FNO. ViF outperforms current mainstream Transformer, Mamba, and Fourier-based models on ImageNet-1K image classification, COCO object detection, and ADE20K semantic segmentation tasks, while maintaining high computational efficiency.

### Strengths
1.The manuscript 's motivation is sound, and it clearly identifies the limitations of FNO, such as bandwidth bottlenecks and over-smoothing.
2.This manuscript introduces an input-dependent integral kernel into the Fourier operator, constructing a unified time-frequency representation space, which is quite innovative.
3.An obvious advantage of this method is computational efficiency. Compared with Transformer-type models, it has lower computational complexity and is more advantageous than Mamba-type models in spatial structure modeling.
4.This manuscript achieves state-of-the-art or competitive results on multiple mainstream vision tasks, particularly on ImageNet-1K, significantly outperforming similar Fourier methods (such as GFNet).

### Weaknesses
1.Although FNF solves some of the shortcomings of FNO, its core idea is still based on the traditional framework of "frequency domain processing + time domain supplementation". It does not propose a new visual representation learning paradigm, which weakens the innovation of this article.
2.Although ViF performs well on ImageNet-1K, its improvement on COCO and ADE20K compared to models such as ViM is relatively small (e.g., mAP increases by 0.2-0.4), failing to significantly widen the gap.
3.ViF only tested three small and medium-sized variants, ViF-T/S/B, and did not evaluate the performance of larger models, such as those of ViT-L/16, on larger datasets.
4.Definition 7 mentions that adaptive modulation is achieved through the amplitude-sensitive weighting function \(\|z\|\) and learnable parameters \(\alpha\) and \(\beta\), but does not give the range of \(\alpha\) and \(\beta\) and whether they are adjusted with training iterations.

### Questions
As mentioned above.

### Soundness
3

### Presentation
3

### Contribution
3

### Rating
4

### Confidence
4

---

## Human Reviewer 3

### Summary
This paper proposes a theoretically sound and empirically validated vision backbone that bridges local and global modeling through the frequency domain, offering an alternative to attention-based and state-space models. The FNF formulation is well-motivated and results across benchmarks substantiate its benefits.

### Strengths
1.The paper presents a theoretically grounded extension of the Fourier Neural Operator (FNO), introducing an input-dependent integral kernel that enables adaptive and dynamic coupling between the spatial (time) and frequency domains.
2. The proposed Vision Filter (ViF) integrates both local convolutional和global frequency operations within a single framework.
3. Results in Figure 1 demonstrate that ViF achieves a more favorable accuracy–throughput trade-off compared to both Transformer and Mamba-based counterparts, showing practical efficiency for high-resolution image processing.

### Weaknesses
1. The paper does not evaluate ViF on larger datasets (e.g., ImageNet-22K, LAION) or with pretraining strategies such as self-supervised learning (MAE, BEiT). As such, the scalability and transferability of ViF remain uncertain compared to modern foundation models.
2. The ablation study (Table 5) confirms that each module contributes to performance, but lacks deeper interpretability or visualization (e.g., frequency response maps, energy spectrum analysis). More qualitative analysis could help clarify how ViF balances local and global representations in practice.
3. Although the authors cite GFNet and AFNO, the distinction between ViF’s adaptive gating mechanism and prior dynamic spectral filters could be elaborated further.

### Questions
1.The manuscript seems only to swap the entire Multi-Head Attention block in ViT for the proposed FNF module, but never compares the two under an otherwise identical architecture. An ablation is recommended that exchanges only the attention mechanism.
2.Although the authors claim “quasi-linear complexity”, only FLOPs are reported. No end-to-end latency, throughput, or peak-memory measurements versus Swin, VMamba or GFNet on the same GPU/CPU are provided.
3.FNF introduces several new hyper-parameters (α, β in adaptive modulation, number of Fourier modes, kernel size of local convolutions, etc.). The manuscript gives a single setting without any hyper-parameter sensitivity analysis. It is indiscernible whether the performance gains are statistically robust or an artefact of ad-hoc tuning.
4.The claim that “directional scanning inevitably leads to spatial disruption” in Mamba-based models is not substantiated. The manuscript neither quantifies the degree of spatial-information loss nor compares patch-order robustness between Mamba and the proposed FNF. It is necessary to compare Acc of Mamba and FNF after random patch-shuffling to quantify patch-order robustness.
5.The implicit periodic extension inherent in FFT introduces spectral leakage and degrades the accuracy of the frequency-domain filtering operation when the input dimension is not a power of two or when the image contains strong edges. This work has not examined whether the proposed FNF module suffers from such boundary artefacts, nor has it evaluated remedies such as windowing or reflection padding. A systematic comparison of cyclic, symmetric and zero-padding schemes is required to determine the susceptibility of FNF to spectral leakage and its consequent impact on dense prediction tasks.

### Soundness
3

### Presentation
3

### Contribution
3

### Rating
4

### Confidence
4

---

## Human Reviewer 4

### Summary
This paper proposes a new generic vision backbone called Vision Filter (ViF) , built upon a novel Fourier Neural Filter (FNF) module. The authors argue that while the Fourier Neural Operator (FNO) is promising for its global modeling capabilities and quasi-linear complexity , it suffers from an "over-smoothing" effect and a "bandwidth bottleneck," making it difficult to capture local, high-frequency patterns. To address this, the FNF module introduces two key components: 1) Adaptive Modulation (AM) in the frequency domain to enhance sensitivity to high-frequency components , and 2) Selective Activation (SA) to balance local time-domain and global frequency-domain information flow. This design creates an input-dependent integral kernel. Extensive experiments on image classification (ImageNet-1K) , object detection (COCO) , and semantic segmentation (ADE20K) demonstrate that ViF outperforms existing SOTA Transformer- and Mamba-based backbones.

### Strengths
1. The authors introduce an adaptive kernel that effectively couples time- and frequency-domain information, providing theoretical novelty.
2. The paper demonstrates strong empirical performance across multiple visual benchmarks and model scales.
3. The authors conduct comprehensive ablation studies that clearly quantify the contribution of each component (AM, SA, LC).
4. The proposed ViF achieves a favorable balance between model complexity and performance, offering quasi-linear computational efficiency.

### Weaknesses
1. The paper lacks experiments exploring the scalability of ViF on larger datasets such as ImageNet-22K or LAION.
2. The authors do not evaluate ViF under self-supervised or foundation model pre-training settings, which limits its generalization claims. I believe this is crucial for vision backbone models.
3. The paper lacks detailed frequency-domain visualizations (e.g., spectral activation maps) to empirically support its frequency modeling claims.
4. The improvements over strong Mamba variants on dense prediction tasks are relatively marginal compared to the architectural complexity.
5. The authors have not released any implementation code at submission time, reducing reproducibility.

### Questions
In addition to the above weaknesses, I also have several questions and suggestions for the authors:
1. Could ViF be integrated into existing architectures (e.g., ConvNeXt or BEiT) as a modular replacement, and what challenges might arise?
2. Does the proposed FNF introduce any implicit bias toward certain frequency bands, and how is this mitigated?
3. Are there plans to extend FNF to video or multimodal vision tasks?
4. Could the authors provide additional visualization results illustrating spectral activations or learned frequency responses?

### Soundness
3

### Presentation
2

### Contribution
3

### Rating
6

### Confidence
4