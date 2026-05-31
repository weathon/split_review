## Human Reviewer 1

### Summary
### 1. Research Problem

*  Existing Spiking Transformer models underperform compared to their ANN counterparts, primarily due to limitations in the spiking self-attention (SSA) mechanism which lacks effective attention localization.

*  SSA requires explicit storage of large attention matrices (such as QK and KV), resulting in significant memory overhead, especially during inference on resource-constrained hardware.

*  Without the softmax operation, SSA generates nearly uniform attention distributions, losing the ability to focus on spatially relevant regions, which is critical in visual tasks.


### 2. Proposed Method

* LRF-SSA (Local Receptive Field Self-Attention):

  * Enhances SSA by incorporating multi-scale dilated convolutions that introduce spatial bias through local receptive fields.
  * Adjusts attention weights to favor nearby tokens, improving local modeling capability while preserving spike-driven characteristics.
  * The attention weights are computed as a convex combination of SSA attention and a local convolutional kernel:
    α_lrf-ssa = (1 - λ) * α_ssa + λ * r_ij

* LRF-Dyn (Local Receptive Field with Neural Dynamics):

  * Reformulates attention using principles of spiking neuron dynamics, simulating membrane potential updates and dendritic processing.
  * Avoids explicit computation and storage of QK or KV matrices by using accumulated membrane states, reducing memory complexity.
  * The attention computation becomes a charge–fire–reset-like process that aligns with the biological plausibility of SNNs.


### 3. Theoretical Contributions

* Entropy-based attention analysis:

  * Demonstrates that LRF-SSA produces lower-entropy attention distributions than SSA, which better reflect the selective nature of softmax-based VSA.

* Expected receptive field radius: Introduces a formal measure of attention locality and proves that LRF-SSA reduces the average receptive field size compared to SSA, while remaining closer to the behavior of VSA.

* Neural dynamics formulation of attention: Establishes an equivalence between spiking attention and dynamic state updates in multi-dendritic neurons, paving the way for biologically grounded attention mechanisms.

* Memory and computation complexity: Reduces inference-time memory from O(d²) to O(kd), with k representing the number of dendritic branches, offering theoretical scalability for edge deployment.


### 4. Experimental Results

* Image classification (ImageNet-1k): LRF-SSA improves top-1 accuracy by up to 1.24% with negligible parameter increase (<0.2M). LRF-Dyn achieves similar or slightly reduced accuracy (within 0.1%) while cutting memory usage to O(kd).

* Semantic segmentation (ADE20K): LRF-SSA improves mIoU by 2.6% and LRF-Dyn by 1.8% over the SSA baseline, showing stronger spatial discrimination with fewer parameters than attention-free baselines like ResNet.

* Ablation studies (CIFAR-100): Performance scales with number of convolution kernels (larger Ω yields higher accuracy), validating the contribution of local spatial modeling.

### Strengths
* The paper introduces a novel perspective on spiking self-attention by recasting attention as a neural dynamic process, drawing from the charge–fire–reset behavior of biological neurons. This is a conceptually original contribution that bridges the gap between algorithmic attention mechanisms and neurophysiological processes.

  * The integration of localized receptive fields into spike-based self-attention (LRF-SSA) is a creative fusion of biologically inspired modeling and modern deep learning practice. It departs from the conventional global attention view in SNNs and enables spatial bias without softmax.

  * The work removes a critical limitation in existing spiking Transformers by eliminating the need for explicit QK/KV matrix storage, allowing for scalable inference on neuromorphic or memory-limited hardware—an underexplored but increasingly relevant design constraint.

  * The experimental content is detailed and clear, and the effectiveness of the method is verified on different tasks.

### Weaknesses
* Limited theoretical depth for LRF-Dyn: While the paper presents a compelling neuro-dynamic approximation of self-attention, the theoretical treatment of LRF-Dyn remains less rigorous than that of LRF-SSA. Specifically, the membrane potential update formulation lacks an explicit connection to the global attention weighting mechanism it replaces.


* Experiments limited to static vision benchmarks: Despite the motivation from real-time and neuromorphic computing, the evaluation is restricted to frame-based, static datasets (ImageNet-1k and ADE20K). These benchmarks do not fully capture the event-driven potential or energy-efficiency implications of spiking systems. The paper would benefit from experiments on neuromorphic datasets (e.g., N-Caltech101, DVS Gesture, or N-Cars) to substantiate claims of biological plausibility and resource efficiency.

* Experimental performance improvement is limited.

### Questions
* Can the authors provide a more rigorous theoretical analysis of LRF-Dyn? Specifically, is there a formal approximation bound or information-preserving guarantee that connects LRF-Dyn to standard attention mechanisms?

* How does the proposed method handle long-range temporal dependencies inherent to spiking inputs? Would LRF-Dyn remain effective in tasks requiring fine-grained temporal precision, such as DVS-based continuous input streams?

* Have the authors considered evaluating the method on neuromorphic datasets?

*  Does the LRF-Dyn formulation introduce stability issues during training, such as exploding or vanishing membrane potentials? Can the authors provide convergence plots or empirical analysis to support its robustness?

* Please add some missing citations, eg:  https://arxiv.org/abs/2311.09376

### Soundness
3

### Presentation
3

### Contribution
3

### Rating
6

### Confidence
4

---

## Human Reviewer 2

### Summary
This paper addresses the issue of unfocused global attention and high memory overhead in spiking transformers. To resolve these problems, this paper proposes Local Receptive Field Spiking Self-Attention (LRF-SSA), which strengthens local attention by assigning higher weights to spatially adjacent positions. Building on LRF-SSA, the paper also introduces LRF-Dyn, a method that eliminates the need for explicit attention-matrix storage and reduces memory overhead.

### Strengths
1. Theoretical analyses are provided to support the proposed LRF-SSA mechanism.
2. The proposed LRF-Dyn maintains performance comparable to LRF-SSA while reducing memory requirements during inference.

### Weaknesses
1. The motivation behind LRF-SSA requires further validation. The paper points out a mismatch in attention patterns between SSA and VSA: as shown in Fig. 1(a) and Fig. 2, VSA emphasizes local relations, while SSA exhibits unfocused global attention. However, this lack of local attention in SSA is a result of its inherent limitations rather than the root cause of its shortcomings. Therefore, enhancing local attention may not fundamentally resolve the issue. In fact, this issue stems from information loss due to the binary nature of spikes in SSA. Previous research [1] has identified this problem and proposed solutions that effectively focus on key features. As a result, the motivation for this paper needs reconsideration and further validation.
2. The proposed method achieves only marginal accuracy improvements on the ImageNet-1k classification task, particularly on the state-of-the-art architecture QKFormer, where the accuracy gain is less than 0.5%.

[1] Xiao, Y., et al. (2025). Rethinking Spiking Self-Attention Mechanism: Implementing a-XNOR Similarity Calculation in Spiking Transformers. Proceedings of the Computer Vision and Pattern Recognition Conference.

### Questions
Please compare existing methods and explain why LRF is more effective than these approaches in addressing the limitations of SSA.

### Soundness
1

### Presentation
2

### Contribution
2

### Rating
2

### Confidence
5

---

## Human Reviewer 3

### Summary
This paper addresses two critical challenges in existing SNN-Transformer architectures: the degradation of local receptive fields and high inference memory cost. The authors present empirical evidence through visualization and statistical analysis, and further propose LRF-Attn and LRF-Dyn to effectively address these issues. Experimental results on both image classification and segmentation tasks demonstrate consistent performance gains, indicating the method’s effectiveness and generality.

### Strengths
1. The paper identifies key limitations in existing SNN-Transformer architectures and substantiates these claims through comprehensive empirical observations and quantitative analyses, making the motivation convincing.
2. Extensive experiments are conducted on recent state-of-the-art Transformer architectures, showing consistent and notable improvements in both image classification and segmentation tasks.
3. The authors provide an analysis of the local receptive field degradation in SNNs from both receptive field radius and information entropy perspectives, and convincingly demonstrate the effectiveness of the proposed approach.

### Weaknesses
1. The adoption of multi-dendritic neurons increases training complexity, potentially leading to higher computational costs on large-scale datasets such as ImageNet.
2. The presentation of inference memory requirements could be improved. Providing a tabular summary for LRF-Attn and LRF-Dyn would make the comparison clearer and more intuitive.

### Questions
1. While the authors have validated the proposed module on mainstream image classification and segmentation tasks, it would be valuable to examine whether comparable effectiveness can be achieved on more challenging NLP tasks [1].
2. Does the proposed LRF-Dyn introduce additional training overhead compared to mainstream CNN-based SNNs [2] and Transformer-based SNNs [3]?
3. Is the local receptive field essential to the effectiveness of the LRF-Dyn method? The authors are encouraged to include experiments to verify this.
[1] Spikelm: Towards general spike-driven language modeling via elastic bi-spiking mechanisms, ICML 2024.
[2] Deep residual learning in spiking neural networks, NeurIPS 2021.
[3] Scaling spike-driven transformer with efficient spike firing approximation training, T-PAMI 2025.

### Soundness
3

### Presentation
3

### Contribution
3

### Rating
6

### Confidence
5

---

## Human Reviewer 4

### Summary
This paper tackles two critical limitations in Spiking Transformers: the performance gap compared to their Artificial Neural Network (ANN) counterparts and excessive memory overhead. The authors argue these issues stem from the unfocused global attention of Spiking Self Attention (SSA) and the high cost of storing attention matrices. Inspired by biological visual neurons, they introduce LRF-Dyn, a novel method that enhances SSA by integrating a Localized Receptive Field (LRF) mechanism. This addition enables the model to focus on neighboring regions, thereby improving its local modeling capabilities. Furthermore, LRF-Dyn reformulates the attention computation to approximate the charge–fire–reset dynamics of spiking neurons, which significantly reduces memory requirements during inference. Extensive experiments confirm that LRF-Dyn successfully lowers memory overhead while delivering substantial performance gains on visual tasks, establishing it as a key advancement for creating more practical and energy-efficient Spiking Transformers.

### Strengths
This paper demonstrates significant strengths across all key dimensions. Its originality is high, stemming from a novel problem analysis that pinpoints the lack of local modeling and high memory cost in Spiking Self Attention (SSA) as key barriers . The proposed LRF-Dyn method is a creative and well-motivated solution, uniquely integrating a Localized Receptive Field (LRF) mechanism to enhance local feature capture and, more innovatively, reformulating the attention mechanism to mimic neuronal dynamics, thereby reducing memory overhead. The quality of the work is excellent, substantiated by a solid theoretical foundation, including theorems that formally prove LRF-SSA preserves the desirable local attention and low-entropy properties of standard attention mechanisms . These theoretical claims are rigorously supported by extensive experiments that confirm both performance improvements and reduced memory consumption. The paper is presented with outstanding clarity, logically progressing from a well-defined problem to a tailored solution, with concepts effectively illustrated through figures and formal proofs. Finally, the significance of this work is substantial; by directly tackling the critical performance and efficiency bottlenecks of Spiking Transformers, it provides a practical and effective component that could accelerate the deployment of energy-efficient vision models on resource-constrained edge and neuromorphic hardware.

### Weaknesses
1. To substantiate the claimed benefits of the proposed method, such as the reduction in memory overhead, the authors should provide concrete quantitative data, for instance, measurements of energy consumption and inference latency.
2. To further justify the necessity of multi-dendritic neurons, the authors are encouraged to include comparisons under identical conditions with other spiking neuron (e.g., LIF, ALIF or DH-LIF) that serve as the core neurons in LRF-Dyn.
3. Given that LRF-Dyn exhibits more complex dynamical behavior, the authors should consider providing an algorithmic description or pseudocode to facilitate a clearer understanding of the proposed method.

### Questions
1. Under identical configurations, how does LRF-Dyn perform when employing different spiking neuron such as LIF, ALIF or DH-LIF?
2. Can the proposed module maintain its effectiveness and generality when evaluated on additional neuromorphic datasets, such as CIFAR10DVS?
3. How does the number of dendrites affect the model's performance and results?

### Soundness
3

### Presentation
3

### Contribution
3

### Rating
6

### Confidence
5