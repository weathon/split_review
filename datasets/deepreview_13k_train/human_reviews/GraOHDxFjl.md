# LLaMA Decoder As Vision Transformer

- Decision: Reject
- Scores: 5, 8, 3, 8

## Abstract
This work examines whether decoder-only Transformers such as LLaMA, which were originally designed for large language models (LLMs), can be adapted to the computer vision field. 
We first "LLaMAfy" a standard ViT step-by-step to align with LLaMA's architecture, and find that directly applying a causal mask to the self-attention brings an attention collapse issue, resulting in the failure to the network training. 
We suggest to reposition the class token behind the image tokens with a \textit{post-sequence class token} technique to overcome this challenge, enabling causal self-attention to efficiently capture the entire image's information. 
Additionally, we develop a \textit{soft mask} strategy that gradually introduces a causal mask to the self-attention at the onset of training to facilitate the optimization behavior. 
The tailored model, dubbed as \textit{image LLaMA (iLLaMA)}, is akin to LLaMA in architecture and enables direct supervised learning. 
Its causal self-attention boosts computational efficiency and learns complex representation by elevating attention map ranks.
iLLaMA rivals the performance with its encoder-only counterparts, achieving 75.1\% ImageNet top-1 accuracy with only 5.7M parameters. 
Scaling the model to $\sim$310M and pre-training on ImageNet-21K further enhances the accuracy to 86.0\%. 
Extensive experiments demonstrate iLLaMA's reliable properties: shape-texture bias, calibration, quantization compatibility, ADE20K segmentation and CIFAR transfer learning. 
We hope our study can kindle fresh views to visual architectures in the wave of LLMs and inspire the development of unified multimodal models.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper investigates the potential of using a decoder-only Transformer architecture, specifically LLaMa, as a vision Transformer (ViT) classifier for image processing. The authors propose a model called image LLaMa (iLLaMA), by transforming ViT into LLaMA-like architecture through step-by-step, component-wise modification. During the modification of attention mechanism, the authors discovered the a key issue called "attention collapse" that hampers network training. To mitigate this, they introduce a post-sequence class token and a soft mask strategy to facilitate improved model optimization and performance. The extensive experiments conducted illustrate iLLaMA's effectiveness in various tasks, suggesting it could contribute to standardization in AI models for text and image processing.

### Strengths
- The paper is well-written and clearly structured, making it easy to follow.
- Through extensive ablation studies, the authors effectively demonstrate the impact of each component.

### Weaknesses
 - Unfortunately for the authors, the existence of VisionLLaMA, which shares similar objectives, significantly diminishes the novelty and contribution of this work. While it should be taken into account that these studies were conducted contemporaneously, the paper still shows considerable weaknesses in comparison. Even taking into account the differences outlined in Section 2.2, it is difficult to argue that this work creates additional value. The claimed distinctions do not appear substantial enough to establish its unique contribution to the field.

- Questionable Design Choices:
    - The adoption of causal mode attention appears primarily motivated by mimicking LLaMA's architecture rather than addressing specific technical needs. The purported computational benefits of causal attention seem minimal, as evidenced in Table 2, where the FLOPs reduction is marginal. Furthermore, the requirement for a soft mask strategy (which uses bidirectional attention) to optimize causal attention's effectiveness seems contradictory to the original design intent. The paper's emphasis on decoder-only architecture lacks convincing justification, especially given VisionLLaMA's successful use of an encoder architecture.
- Performance and Efficiency Concerns:
    - The model's claimed superiority relies heavily on larger datasets, IN-21K, making direct comparisons to VisionLLaMA problematic. Under equivalent training datasets and model scale, VisionLLaMA demonstrates superior performance. Moreover, VisionLLaMA achieves better efficiency with fewer parameters than iLLaMA.

### Questions
- Why should we design the decoder-only architecture, unlike the one with encoder architecture like VisionLLaMA?
   - If the objective is to align vision and language modalities within a single architecture, as stated in line 35, the authors should have demonstrated either cross-modal transferability or developed a unified model capable of handling both modalities.

### Soundness
3

### Presentation
3

### Contribution
1

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The paper explores the adaptation of decoder-only Transformers, specifically LLaMA, originally designed for large language models (LLMs), to the field of computer vision.
It proposes post-sequence class token to overcome the attention collapse issue when applying causal mode attention, and introduces a soft mask strategy to improve model training behavior.
The paper presents a novel approach to adapting large language model architectures for computer vision tasks, achieving promising results and opening avenues for future research in unified vision and language models.

### Strengths
1. The paper innovatively adapts the decoder-only Transformer architecture from large language models (LLMs) to the computer vision domain, demonstrating the potential for unified architectures across modalities.
2. It introduces a post-sequence class token (PS [cls]) technique to address the attention collapse issue in causal self-attention, which is crucial for the effective training of the proposed iLLaMA model.
3. The soft mask strategy developed in the paper gradually introduces causal masking during training, which improves optimization behavior and mitigates underfitting concerns.
4. iLLaMA achieves competitive performance compared to encoder-only models on ImageNet with significantly fewer parameters, showcasing efficiency and effectiveness.
5. The paper provides a comprehensive evaluation of iLLaMA, including not only accuracy but also calibration, shape-texture bias, quantization compatibility, and transfer learning performance, demonstrating its robustness across various practical metrics.
6. The proposed model scales well with increased model capacity and dataset size, achieving state-of-the-art performance on ImageNet with minimal parameters, highlighting its scalability.

### Weaknesses
1. While the paper discusses the potential of unified architectures for language and vision models, it does not explore multimodal tasks that involve both text and images. This is a significant limitation since multimodal capabilities are crucial for assessing the true potential of unified models.

### Questions
1. Will you plan to release the code ?

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
The paper introduces iLLaMA, an adaptation of the LLaMA decoder model to function as a Vision Transformer (ViT) for image classification. iLLaMA addresses the inherent challenges of causal self-attention in image tasks by introducing the post-sequence class token (PS [cls]) and a soft mask strategy. These techniques enhance iLLaMA’s stability and performance, yielding competitive results on ImageNet with relatively few parameters. The paper validates iLLaMA’s capabilities across various tasks, such as calibration, shape-texture bias, and quantization compatibility, positioning it as a streamlined alternative to encoder-only models for visual processing.

### Strengths
1. Architectural Alignment: Adapting LLaMA’s decoder architecture to image classification, the authors propose a novel integration that demonstrates the feasibility of using language-model structures for visual tasks.

2. Training Techniques: The introduction of PS [cls] and a soft mask to address the attention collapse issue in causal attention is well-motivated and effective in stabilizing training.

3.Extensive Validation: The model is evaluated on multiple properties, including calibration and shape-texture bias, showing robust performance across different visual tasks.

### Weaknesses
1. Limited Scope in Multimodal Tasks: Although aligned with LLaMA’s architecture, iLLaMA primarily focuses on vision tasks, and the paper does not explore its application to more complex multimodal scenarios. The absence of experiments involving joint image and text processing limits the assessment of its true potential as a unified architecture, especially given the stated motivation of aligning with language models.

2. Limited Performance Improvement Over ViT: Although iLLaMA introduces novel adaptations for causal attention in visual tasks, the model does not show a substantial performance enhancement compared to ViT on key benchmarks. This raises questions about the practical gains of adapting a decoder-only architecture for image classification. The reported results indicate that iLLaMA achieves comparable, but not superior, performance to ViT, which undermines the practical benefits of the proposed approach.

3.Computational Demands in Soft Masking: While effective, the soft mask strategy could still present some overhead in training time for larger models, which may limit scalability. Although the authors claim the soft mask is computationally light, the additional operations, even if minimal, may still introduce a non-negligible overhead when scaling to larger models and datasets, especially when compared to a fixed mask.

### Questions
1. How does iLLaMA’s causal self-attention compare to traditional bi-directional attention in fine-grained object detection tasks, where spatial dependencies might be critical?

2. Would incorporating an explicit multimodal training objective enhance iLLaMA’s ability to handle both image and language tasks in a unified model?

3. Why should we incur additional costs to adapt a decoder-only architecture for image encoding when encoder-only and decoder-only architectures share the same attention method? This clarification could help readers understand the trade-offs of aligning image models with language-model structures, particularly if the benefits of causal attention are marginal compared to bi-directional approaches in vision tasks.

### Soundness
2

### Presentation
2

### Contribution
1

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
In this paper, the authors present a novel approach for adapting Large Language Model (LLM) architectures to the visual modality. They introduce the Patch Selection [CLS] (PS [CLS]) technique to address the issue of attention collapse commonly observed in vision transformers. This technique enhances the model's ability to focus on salient image regions by refining the attention mechanism within the transformer architecture. To validate their methodology, the authors pre-train iLLaMA, an adaptation of the LLaMA model tailored for image processing, on the ImageNet dataset. They conduct extensive experiments to benchmark iLLaMA's performance across various datasets. The results demonstrate that iLLaMA, equipped with the PS [CLS] technique, achieves superior performance compared to existing models, thereby showcasing the effectiveness of their proposed approach in advancing computer vision tasks.

### Strengths
The paper presents a novel methodology for integrating Large Language Model (LLM) architectures into the visual modality, addressing significant challenges in the process. The authors introduce the Patch Selection [CLS] (PS [CLS]) technique, which effectively mitigates the issue of attention collapse commonly observed in vision transformers. This problem arises when the attention mechanism disproportionately focuses on certain regions, leading to suboptimal feature representation. The PS [CLS] technique enhances the model's ability to attend to diverse and informative regions of an image by refining the attention distribution across patches.

To empirically validate their approach, the authors adapt the LLaMA model—a powerful LLM known for its capabilities in language understanding—for image processing tasks, resulting in the iLLaMA model. They pre-train iLLaMA on the extensive ImageNet dataset to ensure robust feature learning. The model is then evaluated across multiple benchmark datasets, where it demonstrates superior performance compared to existing state-of-the-art models. The experiments cover various aspects of computer vision tasks, including image classification, object detection, and segmentation, showcasing the versatility and effectiveness of the proposed approach.

The paper's architectural novelty lies in the seamless integration of LLM architectures with vision transformers through the PS [CLS] technique. This integration allows the model to leverage the strengths of LLMs—such as advanced sequence modeling and contextual understanding—in processing visual data. The authors provide a comprehensive analysis of the model's architecture, detailing how the PS [CLS] technique operates within the transformer framework to enhance attention mechanisms.

### Weaknesses
Despite the paper's substantial novelty and the thorough explanation of the architectural innovations, there is a noticeable gap in the empirical evaluation section. Specifically, the paper does not include comparative experiments with newer methods such as Extended LSTMs, MAMBA, or QK-normalized architectures. These models represent significant advancements in the field and are known for their effectiveness in handling complex visual tasks.

The omission of these comparisons makes it challenging to fully assess the strength and generalizability of the proposed iLLaMA model. Without empirical evidence demonstrating how iLLaMA performs relative to these cutting-edge architectures, it's difficult to quantify its advantages or identify potential areas where it may fall short. Including experiments that benchmark iLLaMA against these models would provide a more comprehensive understanding of its performance and robustness.

i feel there should be substantial Experiment of how the behavior of method changes if one to choose the like Mixture of Exparts or Mixtures of base.

### Questions
Despite the paper's significant novelty and the innovative concept of utilizing Large Language Models (LLMs) as pre-trained vision learners, there are several areas that would benefit from further clarification and additional experimentation:

Clarification on Attention Collapse: The paper addresses the issue of attention collapse within vision transformers, but it would be beneficial to elaborate on this phenomenon. Specifically, is attention collapse analogous to mode collapse in statistical machine learning, where a model generates limited diversity in outputs despite diverse inputs? A detailed explanation would help readers, especially those new to this area, understand how attention collapse affects model performance and how the proposed Patch Selection [CLS] (PS [CLS]) technique mitigates this issue.

Transparency of Experimental Results: Regarding Table 6, it is not entirely clear whether all the experimental results were obtained directly by the authors or if some results were sourced from existing literature. Clarifying which results are original and which are replicated or cited from other works would enhance the credibility of the empirical evaluation. This transparency is crucial for readers to accurately assess the contributions and validity of the experimental comparisons.

Visualization of Attention Maps: Although the authors demonstrate significant improvements over previous baselines like Vision Transformers (ViT) and ResNet, the attention maps presented in Figure 12 of the supplementary material appear faded in the case of iLLaMA. This raises questions about the model's ability to focus on salient image regions. Providing clearer visualizations or explaining why the attention maps are less pronounced would help in understanding the effectiveness of the PS [CLS] technique in enhancing the attention mechanism within the model.

While the paper excels in presenting architectural innovations and is well-articulated with self-explanatory diagrams, addressing these questions would substantially strengthen its contributions. Additionally, incorporating empirical experiments with newer architectures such as Extended LSTMs, MAMBA, or QK-Normalized architectures could provide a more comprehensive evaluation. These comparisons would help in assessing the true strengths and limitations of iLLaMA relative to cutting-edge models in the field.

By providing detailed answers to these queries and expanding the empirical analysis, the paper would improve in both clarity and scientific rigor. The novelty of repurposing LLMs as pre-trained vision learners is a significant leap forward, and addressing these points would further solidify the paper's impact. I encourage the authors to consider these suggestions, as they would enhance the overall quality and reception of the work.

### Soundness
3

### Presentation
4

### Contribution
3
