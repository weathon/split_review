# Memory Efficient Transformer Adapter for Dense Predictions

- Decision: Accept
- Avg Score: 6.00
- Scores: 6, 6, 6

## Abstract
While current Vision Transformer (ViT) adapter methods have shown promising accuracy, their inference speed is implicitly hindered by inefficient memory access operations, e.g., standard normalization and frequent reshaping. In this work, we propose META, a simple and fast ViT adapter that can improve the model's memory efficiency and decrease memory time consumption by reducing the inefficient memory access operations. Our method features a memory-efficient adapter block that enables the common sharing of layer normalization between the self-attention and feed-forward network layers, thereby reducing the model's reliance on normalization operations. Within the proposed block, the cross-shaped self-attention is employed to reduce the model's frequent reshaping operations. Moreover, we augment the adapter block with a lightweight convolutional branch that can enhance local inductive biases, particularly beneficial for the dense prediction tasks, e.g., object detection, instance segmentation, and semantic segmentation. The adapter block is finally formulated in a cascaded manner to compute diverse head features, thereby enriching the variety of feature representations. Empirically, extensive evaluations on multiple representative datasets validate that META substantially enhances the predicted quality, while achieving a new state-of-the-art accuracy-efficiency trade-off. Theoretically, we demonstrate that META exhibits superior generalization capability and stronger adaptability.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper proposes META, an efficient ViT Adapter that enhances ViT in dense prediction tasks. The adapter block MEA provides the local bias required for image tasks to ViT by introducing conv branches, and significantly reduces memory time consumption by minimizing reshape operations on tensors in the adapter. In classic dense prediction tasks such as Object Detection, Instance Segmentation, and Semantic Segmentation, META outperforms previous adapter methods in terms of fewer parameters and lower memory consumption. Ablation experiments were conducted to verify the effectiveness of the three modules in the MEA block and the improvement of the model with the MEA cascade.

### Strengths
1. The method proposed in this work is simple but effective, achieving higher performance and efficiency in various classic detection and segmentation frameworks.
2. The paper provides clear and understandable descriptions of the details of each module in the MEA block, with the design purposes of each module being clear and effective.

### Weaknesses
1. There is still space on the main text pages, but the implementation parameters of the model are not clarified, such as the number of cascades. Different designs of each size are also not specified.

### Questions
1. In Table 2 and Table 3, models of different sizes have the same Memory Consumption (MC). What specific quantity does MC describe, and what measurements lead to this phenomenon?
2. For different sizes of variants of META, are there differences in the implementation details?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper explores the limitations of Vision Transformer (ViT) adapters in dense prediction tasks, particularly focusing on the issues of memory inefficiency and slow inference speed caused by frequent reshaping operations and normalization steps. The paper proposes a novel ViT adapter named META, which introduces a memory-efficient adapter block that enables the sharing of normalization layers between the self-attention layer and the feed-forward layer. Furthermore, a lightweight convolutional branch is added to enhance the adapter block. Ultimately, this design achieves a reduction in memory access overhead.

### Strengths
This paper presents a simple and fast ViT adapter named META, which addresses the critical yet underexplored issue of memory inefficiency. The quality of this paper is supported by theoretical foundations and empirical validations across various tasks and datasets, demonstrating that META outperforms state-of-the-art models in terms of accuracy and memory usage. The paper is structured clearly, with detailed architectural descriptions and clear explanations of the proposed motivation.

### Weaknesses
In the Atte Branch discussed in this paper, the adoption of the cross-shaped self-attention (CSA) mechanism is a pivotal factor in effectively reducing the frequent reshaping operations of the model. However, the current analysis lacks an in-depth comparison and discussion between CSA and other efficient attention mechanisms, failing to fully elaborate on why the selection of CSA achieves the current experimental results. Specifically, the paper does not explore the trade-offs between CSA and alternatives like linear attention or low-rank approximations in terms of computational cost, memory footprint, and impact on accuracy for the specific dense prediction tasks considered. A more rigorous justification for choosing CSA over other options is needed, including a discussion of the potential limitations of CSA in different scenarios.

The ablation analysis in this paper are currently limited to the results of instance segmentation on the MS-COCO dataset, whereas your previous experimental work also encompassed the tasks of object detection and semantic segmentation. Therefore, the current ablation analysis regarding the components of the proposed module has certain limitations in terms of generalization. To more comprehensively evaluate the effectiveness and universality of the module components, I recommend conducting corresponding experimental validations for all three tasks of object detection, instance segmentation, and semantic segmentation, thereby ensuring the accuracy and applicability of the conclusions obtained. The current analysis does not sufficiently demonstrate the robustness of the proposed method across different dense prediction tasks.

In this paper, there is an inconsistency in the presentation, specifically between Formula (1) and part (a) of Figure 2, which do not align accurately. Although you have explained later in the text that the channel concatenation step for Fsp and Fvit is omitted in the formula, this omission may still lead to misunderstandings among readers. To ensure clarity and accuracy of the content, we recommend that the two should correctly correspond to each other.

### Questions
In your experimental section, you have conducted in-depth explorations of the three tasks: object detection, instance segmentation, and semantic segmentation. To more intuitively demonstrate the specific improvements brought by your model in handling these tasks, are there any relevant visualization results to support this?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper proposes a Memory-Efficient Transformer Adapter, termed META, which reduces memory access costs by sharing layer normalization across multiple modules and substituting standard self-attention with cross-shaped self-attention. Meanwhile, META divides the feature map into smaller parts along the channel dimension and processes these smaller features sequentially. Thereby further reducing memory requirements. Experiment results in object detection and instance segmentation indicate that META achieves better accuracies.

### Strengths
1. META introduces a cross-shaped self-attention mechanism and a cascaded process, both of which are grounded in the principles of dividing the entire feature into multiple smaller features to reduce memory costs.
2. META incorporates local inductive biases by introducing convolutions into the FFN and an additional lightweight convolutional branch. This enables META to achieve better performance in extensive experimental evaluations.

### Weaknesses
1. Insufficient Motivation (1): META claims that the inference speed of previous adapters is hindered by inefficient memory access operations such as normalization and frequent reshaping, but it lacks experimental analysis to support this claim. It is recommended to provide a detailed breakdown of inference time to show the proportion of time consumed by inefficient memory access operations in META and previous methods, specifically detailing the time spent on normalization, reshaping, and attention calculations. This analysis should quantify the actual overhead of these operations to justify the proposed optimizations.
2. Insufficient Motivation (2): META aims to decrease memory access costs by reducing frequent reshaping operations. However, I do not observe any reduction. First, the input for attention and layer normalization is $x\in R^{B\times L\times C}$, where B, L, and C denote the batch size, number of tokens, and channels, respectively. In contrast, the convolution accepts input in the format $x\in R^{B\times C\times H\times W}$. The MEA block mixes many convolutions, layer normalization, and attention. This may result in multiple tensor reshaping operations. Second, the cross-shaped self-attention mechanism divides the features into non-overlapping horizontal/vertical stripes, further compounding the need for tensor reshaping operations. I conjecture that the observed lower memory access costs during experiments are due to the segmentation of the entire feature into multiple smaller features, instead of reducing tensor reshaping operations. I'd like to see a thorough analysis of memory costs associated with each operation in META and previous approaches, including a detailed breakdown of the number of reshaping operations and memory footprint for each component. This will help clarify where the memory saving comes from.
3. The results of the ablation study presented in Table 4 indicate that convolutional layers are primarily responsible for the observed improvements (FFN also includes MLP composed of two 3x3 convolutional layers). This raises the question: to what extent does the Attention Branch contribute to these improvements? Consider conducting an additional ablation study that includes the ViT-B along with the FFN Branch, maintaining the same configuration as described in Line 435, but excluding the Attn Branch. This would isolate the impact of the attention mechanism.
4. The proposed META is relatively sophisticated and comprises numerous layers (e.g., the cascaded injector includes 16 layers), making it less practical for low-performance hardware. On which hardware do you measure FPS? It is recommended to compare META with other methods on less powerful GPUs such as the V100, rather than A100 or H100. This would provide a more realistic evaluation of its applicability in resource-constrained environments.
5. In Table S3, how do you compare other efficient attention methods? Do you only replace the attention mechanism in the ViT-adapter with other attention mechanisms? Please provide further details regarding the experimental setup, including the specific configurations and training parameters used for each compared method. This will ensure the validity and reproducibility of the comparisons.
6. Other minor comments.
Line 150：The spatial prior requires clarification, is the spatial prior module utilized here identical to that in the ViT-adapter [1]?  
Line 96: TDE Transformer, DeiT is more frequently used.  
Line 182: The term "which" appears to ambiguously refer to the prior module rather than the MEA block; it would be beneficial to provide clarification.
Line 188: In Equation 1, "Concat" is a widely recognized abbreviation for concatenation.
Line 199: "Attn" is a more commonly accepted abbreviation for attention compared to "Atte".  
Line 223: Should "respectively" be replaced with "sequentially"?  
Line 166 Table S2 in Supplementary Materials: Do you mean separate normalization for different modules? The use of "common" may introduce ambiguity.

### Questions
Please see weakness section. After the rebuttal, I have addressed many of my concerns and now support the acceptance of the paper.

### Soundness
2

### Presentation
2

### Contribution
3
