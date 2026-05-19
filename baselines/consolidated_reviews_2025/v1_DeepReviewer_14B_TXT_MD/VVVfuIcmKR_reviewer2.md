### Summary

This paper presents a novel approach to using CLIP for intra-modal tasks, such as image-to-image retrieval. The authors propose a method that transforms features from one modality (e.g., images) into the other (e.g., text) to leverage CLIP's inter-modal alignment capabilities. They introduce Optimization-based Textual Inversion (OTI) and Optimization-based Visual Inversion (OVI), which map features from their native modality into the complementary modality without requiring additional training data or adapters. Through extensive experiments on more than fifteen datasets, the authors demonstrate that this inter-modal approach significantly outperforms traditional intra-modal methods.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

1. The paper addresses an important limitation in how CLIP is typically used for intra-modal tasks, highlighting the issue of intra-modal misalignment.
2. The proposed approach is well-motivated and grounded in a clear understanding of CLIP's inter-modal strengths.
3. The experiments are thorough, covering multiple datasets and tasks, and the results consistently show performance improvements.

### Weaknesses

#### Some Related Works


#### comment

1. The proposed method requires an optimization step for each query, which may be too slow for large-scale retrieval tasks. The iterative optimization, even if performed only once per query image, introduces a significant computational overhead, especially when considering the need to compare against a large gallery of images. This could limit the practical applicability of the method in real-world scenarios where speed is crucial.
2. The need to optimize pseudo-word tokens or pseudo-patches could be seen as an additional complexity that might limit the method's practicality. The process of optimizing these pseudo-tokens or patches, while avoiding external data dependence, adds a layer of complexity that might be difficult to implement and tune in practice. The choice of the number of pseudo-tokens or patches and their initialization could also impact the performance and require careful consideration.

### Suggestions

The authors should explore methods to reduce the computational cost of the optimization process. One potential direction is to investigate techniques for faster convergence of the optimization, such as using more efficient optimization algorithms or employing techniques like early stopping. Another approach could be to pre-compute and cache the inverted features for the gallery images, which would eliminate the need for optimization during the retrieval phase. This would significantly speed up the retrieval process, making it more practical for large-scale applications. Furthermore, exploring the use of approximate nearest neighbor search algorithms could also help to reduce the search space and improve the efficiency of the retrieval process.

To address the complexity of optimizing pseudo-word tokens or pseudo-patches, the authors could investigate alternative methods for mapping features between modalities that do not require iterative optimization. For example, they could explore the use of a learnable linear transformation or a small neural network trained to map image features to text features and vice versa. This would eliminate the need for optimizing pseudo-tokens or patches for each query, simplifying the method and making it more practical. The authors could also explore the possibility of using a fixed set of pseudo-tokens or patches that are learned once and then used for all queries, reducing the computational overhead. The choice of the number of pseudo-tokens or patches and their initialization could also be explored more thoroughly, perhaps by using a hyperparameter search or by analyzing the sensitivity of the method to these parameters.

Finally, the authors should provide a more detailed analysis of the computational cost of their method, including the time required for optimization and the memory requirements. This would help to better understand the practical limitations of the method and to identify areas where further improvements are needed. A comparison with other state-of-the-art methods in terms of both performance and computational cost would also be beneficial. This would allow the reader to better assess the trade-offs between performance and efficiency and to determine the suitability of the method for different applications.

### Questions

1. How does the computational cost of the proposed method compare to other state-of-the-art approaches in image-to-image retrieval?
2. Are there any potential ways to reduce the computational cost of modality inversion, perhaps by optimizing fewer steps or using more efficient optimization techniques?
3. How sensitive is the performance of the proposed method to the choice of the number of pseudo-word tokens or pseudo-patches?

### Rating

6

### Confidence

3

**********
