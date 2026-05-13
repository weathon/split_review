# Interfering with Interference: Blind Shuffling and Superposition for Better Multi-Model Compression

- Decision: Reject
- Scores: 6, 3, 6, 5

## Abstract
We present two complementary random mechanisms to significantly reduce interference when eliminating cross-model redundancy for efficient multi-model serving: _Layer Shuffling_ and _Task Vector Superposition_. They work together to increase the orthogonality among interfering task vectors, forcing them into self-destruction without requiring any post-training learning or optimization. _Layer Shuffling_ randomly reorders layers of each individual models to reduce the alignment between interfering task vectors. While _Task Vector Superposition_ leverages random orthogonal transformations to decorrelate task vectors further. Together, these techniques drastically minimize interference, yielding improved performance across multiple tasks with effectively zero incremental memory cost when incorporating new models. Their data and model-independent nature also allows for seamless on-the-fly addition or removal of models, without requiring any re-computation, making them highly practical for real-world deployment scenarios.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper introduces two methods, layer shuffling and task vector superposition, aimed at reducing interference between task vectors in multi-model compression scenarios. The proposed methods work by increasing the orthogonality of task vectors, thus minimizing their interference during merging. By leveraging randomization, these methods require no additional training and can be applied across various models and tasks. Experiments on multiple benchmarks, including CLIP, Flan-T5, and GPT-2, demonstrate that this approach can achieve comparable performance to fine-tuned models while reducing storage costs, particularly for real-world deployment scenarios where adding or removing models on the fly is necessary.

### Strengths
* Simplicity and Effectiveness: One of the major strengths of this paper lies in its approach’s simplicity. Layer shuffling and task vector superposition are straightforward yet powerful techniques that effectively reduce interference without needing additional training, optimization, or complex configurations. This simplicity not only enhances the practicality of the approach but also makes it easy to implement and adapt across various multi-model compression tasks, proving that even minimal adjustments can yield significant performance improvements.

* Effective Interference Reduction: The combination of layer shuffling and task vector superposition is innovative in addressing interference by increasing orthogonality among task vectors. This approach allows for a more effective merging process, yielding improved model accuracy without the need for additional optimization or training steps.

* Adaptability and Scalability: The proposed method’s flexibility is a clear strength. Its data and model-independent nature enables seamless additions and removals of models (hot-swapping) without re-computation, a valuable feature for dynamic applications. Moreover, the approach is efficient, doubling the memory footprint while providing significant accuracy improvements.

* Comprehensive Evaluation: The experiments cover a range of benchmarks and tasks, showcasing the model’s capability across various domains, from image classification to text generation. This breadth of evaluation helps establish the generalizability of the method across tasks and model architectures.

### Weaknesses
 * Lack of Detailed Performance Analysis Based on Shuffle/Superposition Levels: It would be useful to analyze the impact of different levels of shuffling and superposition, as these levels could influence task vector similarity and interference differently. Specifically, the paper lacks a systematic exploration of how varying the degree of layer shuffling or the number of task vectors superposed affects the final performance. For instance, does a higher degree of shuffling consistently lead to better orthogonality, or is there a point of diminishing returns? Similarly, how does the performance change when superposing more than two task vectors, and is there an optimal number for different tasks or model architectures? This analysis would provide a clearer picture of optimal interference reduction strategies.
* Clarity Issues in Method Description: Some aspects of the method, such as the merged task vector formation in equation (8), could benefit from further clarification. Specifically, does shuffling task vectors in different layers cause mixing of task vectors across layers, for instance, between k-1 or k+1? The description should explicitly state whether the shuffling operation is confined within each layer or if it allows for cross-layer mixing. If cross-layer mixing is permitted, it's crucial to explain how this affects the layer-specific task vector alignment and whether this mixing is random or follows a specific pattern. Clarifying this would enhance understanding of how the shuffle affects layer-specific task vector alignment.
* Effectiveness Across Tasks: The effectiveness of either TA+Shuffle or STA appears to vary by task, yet the paper does not discuss why some tasks benefit more from specific strategies. For example, it is not clear why TA+Shuffle might be more effective for image classification tasks but less so for text generation, or vice versa. A more in-depth analysis here would provide insights into optimizing methods based on task characteristics. The paper should explore potential correlations between task properties (e.g., data modality, task complexity, or dataset size) and the performance of different interference reduction strategies. This would help in selecting the most appropriate method for a given task.
* Related Work Reference (PEFT): (Maybe, long shot) this paper is related? "Efficient Storage of Fine-Tuned Models via Low-Rank Approximation of Weight Residuals,"
* Minor Formatting Issues: There are some minor formatting errors in the document, such as incorrect Latex punctuation and inconsistent reference formatting. For example, equation 3 is mistakenly referenced in the context of equation 4, and parentheses are missing in certain citations. Additionally, clarifying what the values in parentheses mean in tables, such as in the average (%) and Bits (Gb) columns, would be helpful, as it currently requires reading the text to understand that they refer to relative performance to fine-tuned models.

### Questions
Please see the above.

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
The paper proposes two stochastic mechanisms to improve performance for multi-task model merging by reducing task interference. First, the method takes advantage of the repeating structure of modern neural networks and randomly shuffles the same-module layer across blocks by first showing that the layers are mostly similar in the within-block across tasks. Second, the paper proposes random binary matrices to multiply parameter vectors to further reduce the task vector similarity. During inference, the inverse transforms are applied. The paper performs experiments across diverse benchmarks.

### Strengths
1. The method is intuitive and simple. The motivation for both components is well written and properly ablated.
2. The method is scalable and memory efficient (modulo the duplication of model parameters) given that it only requires the storage of random seeds to retrieve the final model.
3. The experimental results are strong across benchmarks.

### Weaknesses
1. The method has a limitation that is not discussed a lot, apart from the title: it requires the knowledge of the task id during inference. This needs to be underlined during the comparison with methods such as ties and task arithmetic for fairness. This requirement significantly restricts the applicability of the method in scenarios where task identity is not readily available or must be inferred, unlike methods that aim for task-agnostic merging.
2. lack of forward pass time complexity comparison. The proposed method introduces an overhead in the forward pass: layers need to be reshuffled in the correct order, signs need to be restored and the residual needs to be added to the pre-trained weights. Therefore, there should be a study of how much overhead all these operations incur. This is especially important given the potential for increased latency in real-time applications, and a detailed breakdown of the computational cost of each step is needed.
3. Missing baselines: Given the parameter increase and the time complexity overhead, the paper should compare with the compression algorithm of [1]. The absence of a comparison with a method that directly addresses model compression, especially given the parameter duplication inherent in the proposed approach, leaves a gap in the evaluation.
4. The paper solely focuses on small models, base variants on ViT and Flan-T5, but the literature uses ViT-L/14 and T5-XXL regularly. It would also be interesting to check the performance of the method as tasks increase, see 14 and 20 task benchmarks from [1]. It would be interesting to also track the forward pass time metrics in the case of larger models. The lack of evaluation on larger models and a higher number of tasks makes it difficult to assess the scalability and practical relevance of the method in more demanding settings.
5. L268-269: fix references for benchmarks: the vision one for instance comes from Ilharco et al. and not from FusionBench
6. Baselines and their categorization are not explained and the reader cannot understand why PSP ins included given its poor results or what WEMoE and SMILE are on their own category compared to everything else. It would be helpful for the reader to provide a brief description of each method as well as a high level overview of the categories to help the reader understand rather than deferring to the appendix where they are actually not discussed. The current presentation makes it difficult to understand the relative strengths and weaknesses of the baselines and how they relate to the proposed method.
7. Extremely limited Related work: the quality of the paper is heavily undermined by the lack of proper references and discussion over related work. The absence of a comprehensive discussion of relevant literature makes it difficult to place the proposed method within the broader context of model merging and compression techniques.

### Questions
1. why is 5.03 the number of Gb attributed to fine-tuned? shouldn’t it be 8x the pre-trained model?

### Soundness
2

### Presentation
2

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
The paper introduces two methods, Layer Shuffling and Task Vector Superposition, aimed at reducing interference when compressing multiple fine-tuned models into a single multitask model using task vector arithmetic. Layer Shuffling works by randomly reordering layers in each model before merging, reducing alignment between task vectors. Task Vector Superposition applies random orthogonal transformations to further decorrelate task vectors. Both techniques minimize interference and improve performance across tasks. Experiments with CLIP-ViT, Flan-T5, and GPT-2 show that this approach achieves higher accuracy than vanilla task arithmetic and other baseline methods.

### Strengths
- The paper makes an observation that individual task vectors are too similar and successfully uses it to reduce task vector interference, leading to better multitask performance in model compression scenarios.
- Both proposed techniques operate without needing data, allowing flexible model addition or removal without retraining or optimization.
- The method achieves storage reduction compared to keeping individual models.
- The approach is shown to improve performance across diverse domains including image classification, text generation, and text classification.
- The method enables on-the-fly model integration, allowing seamless "hot-swapping" of models.
- The paper is very well written and clearly structured.

### Weaknesses
 - While the paper compares its method to several baseline techniques, it misses comparison with closely related recent works, particularly Guillermo Ortiz-Jimenez et al.'s work (mentioned in the paper) on task vector manipulation for model merging. Including these comparisons would strengthen the submission.
- Although the authors claim minimal memory overhead, additional context matrices and shuffled task vectors nearly double the memory requirement, which may not always justify the marginal performance gains over baselines like SMILE.
- LoRA results show that SMILE achieves a better tradeoff between accuracy and memory than the reported combination of the proposed methods.

### Questions
Q1: Although randomization offers clear advantages like data independence, would a more systematic approach to orthogonalizing task vectors further improve the performance?
Q2: Did you observe any (in-)consistent performance variance due to randomness in shuffling and superposition?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper introduces Layer Shuffling and Task Vector Superposition, two random mechanisms to reduce interference in multi-model compression by increasing orthogonality between task vectors. The methods achieve near-identical accuracy to individual fine-tuned models while reducing storage costs by 4 times and enable seamless hot-swapping of models without recomputation.

### Strengths
- The paper presents a novel approach to multi-model compression through random mechanisms

- The empirical evaluation is conducted across multiple benchmarks to demonstrate the effectiveness of the method

### Weaknesses
 - The current presentation and writing require significant improvements. For instance, the mathematical analysis is overly simplistic and does not warrant extensive explanation. Additionally, the proposed method lacks a rigorous proof demonstrating why Layer Shuffling specifically enhances orthogonality more effectively than other potential random transformations. The paper does not explore the theoretical underpinnings of why shuffling layers, as opposed to other random permutations or transformations, would lead to better task vector orthogonality. This lack of theoretical justification weakens the claims.

- The interaction between Layer Shuffling and Task Vector Superposition isn't thoroughly analyzed as it's unclear whether they're truly complementary or if one method dominates the benefits. The paper does not provide a clear ablation study to isolate the effects of each technique. It's unclear if the observed performance gains are due to a synergistic effect or if one method is simply masking the limitations of the other. A more rigorous analysis of their combined effect is needed.

- The experiments are not convincing because the models used for comparison are generally much smaller, leading to expected inferior performance from competitors. Meanwhile, the authors' model is significantly larger, resulting in better performance, which does not necessarily demonstrate an advantage. The paper does not adequately control for model size when comparing against baseline methods. This makes it difficult to determine if the performance gains are due to the proposed method or simply due to the larger capacity of the models used. The comparison should be made against models of similar size to properly assess the method's effectiveness.

### Questions
see the above weakness part

### Soundness
2

### Presentation
2

### Contribution
2
