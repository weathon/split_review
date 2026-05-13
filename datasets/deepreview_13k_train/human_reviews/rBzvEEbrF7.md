# Q-GaLore: Quantized GaLore with INT4 Projection and Layer-Adaptive Low-Rank Gradients

- Decision: Reject
- Scores: 6, 5, 6, 3

## Abstract
Training Large Language Models (LLMs) is memory-intensive due to the large number of parameters and associated optimization states. GaLore \cite{zhao2024galore}, a recent method, reduces memory usage by projecting weight gradients into a low-rank subspace without compromising performance. However, GaLore relies on time-consuming Singular Value Decomposition (SVD) operations to identify the subspace, and the frequent subspace updates lead to significant training time overhead. Moreover, GaLore offers minimal improvements in accuracy and efficiency compared to LoRA in more accessible fine-tuning scenarios. To address these limitations, we introduce \textbf{\OURS{}}, a novel approach that substantially reduces memory usage by combining quantization and low-rank projection, surpassing the benefits of GaLore. Our method is based on two key observations: (i) the gradient subspace exhibits diverse properties, with some layers converging early in training while others are subject to frequent changes; (ii) the projection matrices are highly resilient to low-bit quantization. Leveraging these insights, \OURS{} adaptively updates the gradient subspace based on its convergence statistics, achieving comparable performance while significantly reducing the number of SVD operations. We maintain the projection matrices in INT4 format for aggressive memory conservation and preserve weights in INT8 format, incorporating stochastic rounding to capture accumulated gradient information. This approach enables a high-precision training trajectory using only low-precision weights. We demonstrate that \OURS{} achieves highly competitive pre-training and fine-tuning performance with exceptional memory efficiency. \textit{At pre-training}, \OURS{} facilitates training a \textbf{LLaMA-7B} model from scratch on a single NVIDIA RTX 4060 Ti with only \textbf{16 GB memory}, showcasing its exceptional memory efficiency and practicality. \textit{At fine-tuning}, it reduces memory consumption by \textbf{up to 50\%} compared to LoRA and GaLore, while consistently outperforming QLoRA (by \textbf{up to 5.19} on MMLU) at the same memory cost.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper improves the memory and compute efficiency of GaLore with a combination of aggressive quantization and lazy layerwise subspace exploration techniques. Authors motivate these techniques by thoughtfully designed empirical analyses (e.g., layerwise gradient subspace analysis), and validate its effectiveness through diverse experiments. Notably, Q-GaLore reduces memory consumption by up to 50% and saves over 32 hours for training a 7B model compared to the baselines like LoRA and GaLore.

### Strengths
This paper is tackling the important problem of democratizing the large-scale ML training given the limited compute resources. To achieve this goal, authors have performed insightful analyses, upon which they carefully develop quantization and layerwise adaptive SVD computations. Finally, authors have demonstrated the effectiveness of Q-GaLore in extensive empirical experiments, encompassing language model pertaining and fine-tuning.

### Weaknesses
In Table 1, it seems that the performance gap between GaLore and Q-GaLore tends to increase as the model size increases. While it still outperforms LoRA, I personally believe the 0.5 perplexity difference is not negligible. In addition, some hyperparameters like 0.4 cosine similarity threshold looks somewhat arbitrary, and it's unclear how important these hyperparameters are in the final performance.

Noting that the performance degradation starts at 350M, I believe it's possible that the effectiveness of Q-GaLore decreases with larger models.

While the author noted that the absolute perplexity difference decreased at 1B (compared to 350M), I want to point out that the loss scale generally decreases as the model size increases following the scaling laws. I am not sure about the best way to measure the performance degradation across different model scales, but my concern 1 still remains valid.

### Questions
See above.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper propose Q-GaLore to reduce the memory footprint when training LLMs. Q-GaLore is build upon GaLore and further quantize weights and projection matrix into lower precision to improve the performance. Q-GaLore adaptively update the subspace to reduce the overhead correspond to SVD decomposition. This approach achieve better training performance compared with other low-rank training methods and significantly reduce the memory requirement on pretraining of Llama-1B and fine-tuning on 7B scale models.

### Strengths
1. Q-GaLore achieves substantial memory reduction compared to the original Galore paper by applying 8-bit quantization to model weights and 4-bit quantization to the projection matrix. 
2. Q-GaLore reduces training time associated with Singular Value Decomposition (SVD) by decreasing the frequency of SVD updates for layers where the low-rank subspace remains relatively stable over time, which is well-motivated.

### Weaknesses
1. "pre-training a LLaMA 7B with single batch size" is very strange in Section 1. Discussing the motivation in the fine-tuning scenario is a better choice.
2. The modifications on GaLore framework is relatively incremental (for the quantization section).
3.  How the quantization of weight and projection matrices contribute to the degradation of the models? Which factor contributes more to the performance degradation? For example, the comparison of (FP16 weight, FP16 projection) - (FP16 weight, INT8 projection) - (FP16 weight, INT4 Projection) - (INT8 weight, FP16 projection) - (INT8 weight, INT8 Projection) - (INT8 weight, INT4 Projection) will help to understand how each component and the choice of quantization bit-width affect the final performance.

### Questions
See Weakness Part.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This work proposes Q-GaLore, a memory-efficient training method based on GaLore. Q-GaLore further reduces the memory footprint by quantizing the model weights to 8-bit and the low-rank gradient terms to 4-bit. Q-GaLore also adaptively reduces the number of SVD operations on gradients throughout the training process. This work also performs experiments to decompose the memory footprint which verifies the efficacy of Q-GaLore.

### Strengths
Q-GaLore enhances GaLore with quantization.
- Q-GaLore havles the memory footprint of weights by quantizing weights to 8-bit.
- Q-GaLore adaptively reduces the frequency of the computation-intensive SVD operation on gradients (projection matrices), based on the enlightening observations that there are layers with diminishing gradients. 
- The memory footprint breakdown clarifies the improvement of Q-GaLore.

### Weaknesses
 - Limited novelty with increased complexity. This work mainly applies quantization to GaLore with adaptively reduced SVD operations on projection matrices. However, it introduces more hyper-parameters to tune, such as the threshold for determining update intervals.
- A lack of end-to-end latency/time evaluation. Q-GaLore introduces extra operations like the dequantization and the calculation of cosine similarity of projection matrices. The extra cost of these operations, in terms of latency and computation, remains unclear compared to the baselines.  If possible, please consider a breakdown of time spent on different operations including the new ones introduced by Q-GaLore.
- Insufficient and vague evaluation on fine-tuning/training experiments.
  - No description of hyper-parameters like learning rates, training epochs, and batche sizes.
  - If the trained model performance heavily depends on the threshold of cosine similarity, a discussion on the threshold selection is necessary. If not, relevant experiments and a recommend value can be provided.

### Questions
1.  In line 201, how is the "*cosine similarity across matrices*" defined? Why not use other ways of measuring distances between matrices like Frobenius norm? Usually the cosine similarity measures the similarity between **two vectors** of an inner product space. Are the matrices flattened? If so, along which dimension? 
2. In line 315, the statement "*no baseline involves quantization and all data are maintained in BF16 format*" is confusing, since in the QLoRA baseline weights are quantized. Please clarify this statement or correct it if it's inaccurate.
3. In Tab 1, for the 60M model, why the LoRA (ReLoRA) uses the the same amount of memory (0.36GB) as full fine-tuning? Similarly, for the 130M model, LoRA takes up more memory (0.80GB) than full fine-tuning (0.76G). 
4. In Tab 1, if QLoRA is added as a baseline (QLoRA was included in Tab 2 as a baseline), how much memory is consumed and what is the perplexity? As Q-GoLore adopts quantization, comparing to QLoRA can be reasonable to evaluate memory efficiency.
5. In Tab 1, 2, and 3, how hyper-parameters are determined? Since different methods may have different optimal hyper-params like learning rate.
6. As stated in the weakness. Does the trained model performance heavily depend on the threshold for determining update intervals of projection matrices? If so, how do users determine the value for given a model and a task? If not, what is the recommended value?
7. In line 472, the time cost is reduced by over 32 hours. What is the total time of training in this case?

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
The paper proposes a method to accelerate the GaLore, which is time-consuming and memory-intensive. It cleverly utilizes observed behaviors to reduce the time and memory required for GaLore. The structure of the paper is clear, and the experiments are thorough.

### Strengths
1. The paper proposes an acceleration method to address the time and memory requirements of the GaLore process. It cleverly observes an early stopping phenomenon in some layers during GaLore training, which reduces the number of SVD decompositions needed. Additionally, the paper employs quantization to lower memory usage.
2. The structure of the paper is clear, making it easy to understand.
3. The experiments are comprehensive.

### Weaknesses
1. The paper emphasizes reducing memory usage during the GaLore process. However, the main source of memory consumption in GaLore seems to be the need for SVD on large matrices, which currently only supports 32-bit precision. Without reducing the dimensionality of the decomposition matrices, the proposed method does not seem to genuinely reduce memory requirements. The memory footprint of storing the full U, S, and V matrices during SVD, even if temporary, is substantial, and it's not clear how the proposed quantization addresses this specific bottleneck. The paper needs to clarify whether the quantization is applied to these intermediate SVD matrices or only to the final projection matrix.
2. The proposed adaptive lazy update is interesting, but it lacks further explanation. For instance, why does this phenomenon occur, and what is its relationship with different depths and types of layers? It's unclear what specific properties of the layers or the training process cause the observed early stopping behavior. The paper should provide a more detailed analysis of the gradient subspace changes and their correlation with layer depth and function. Furthermore, it is not clear if this behavior is consistent across different model architectures or training datasets.

### Questions
1. I do not fully understand how the memory requirement is reduced. The memory bottleneck of GaLore seems to be the 32-bit decomposition of large matrices. Could you provide further clarification? If clarified well, I will improve my score.
2. Could you provide a more in-depth explanation of the adaptive lazy update, such as the reasons behind it or its behavior across different layers and matrices? Does this phenomenon occur with different training datasets? Is the lazy matrix the same for the same model under different training datasets?
3. Could the authors provide a more intuitive comparison of the time required to demonstrate the effectiveness of the acceleration?

### Soundness
3

### Presentation
4

### Contribution
2
