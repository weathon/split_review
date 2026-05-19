### Summary

The paper introduces OmniSep, a novel framework for sound separation that leverages omni-modal queries, including text, images, and audio, to isolate clean soundtracks from complex audio mixtures. The key contributions are the Query-Mixup strategy, which blends query features from different modalities during training, and the introduction of negative queries to eliminate undesired sounds. The paper also proposes Query-Aug, a retrieval-augmented approach for open-vocabulary sound separation. Experimental results on MUSIC and VGGSOUND datasets demonstrate that OmniSep achieves state-of-the-art performance across various sound separation tasks.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

1. OmniSep is the first model to handle omni-modal queries for sound separation, unifying text, image, and audio queries into a single framework.
2. The introduction of negative queries is a novel approach that enhances the flexibility of sound separation by allowing the model to filter out specific sounds.
3. The Query-Aug method enables open-vocabulary sound separation, which is a significant advancement over previous methods that relied on predefined class labels.
4. The paper provides extensive experimental results and ablation studies that validate the effectiveness of the proposed methods.

### Weaknesses

#### Some Related Works


#### comment

1. The paper does not provide a detailed analysis of the computational complexity of the proposed methods, particularly the Query-Mixup and Query-Aug strategies. This makes it difficult to assess the practicality of the approach for real-time applications. Specifically, the paper lacks a breakdown of the FLOPs and memory requirements for each component of the model, such as the query processing, the separation network, and the augmentation process. Without this information, it's hard to understand the bottlenecks and potential for optimization.
2. The reliance on ImageBind as the Query-Net means that the performance of OmniSep is inherently tied to the capabilities of ImageBind. Any limitations or biases in ImageBind could propagate to OmniSep. For example, if ImageBind struggles with certain types of images or text descriptions, the corresponding sound separation performance might be negatively affected. Furthermore, the fixed nature of the pre-trained ImageBind model prevents the model from adapting to the specific nuances of the sound separation task, potentially limiting its overall performance.
3. The Query-Aug method relies on retrieving similar in-domain class queries, which might not always be effective for truly out-of-domain or novel queries. The effectiveness of this approach depends on the quality and coverage of the query set. If the query set does not adequately represent the diversity of possible sound descriptions, the model's ability to generalize to unseen queries will be limited. Additionally, the similarity metric used for retrieval might not capture all relevant semantic relationships between queries, leading to suboptimal query augmentation.

### Suggestions

To address the lack of computational complexity analysis, the authors should provide a detailed breakdown of the FLOPs and memory requirements for each component of the OmniSep model, including the query processing, separation network, and augmentation process. This analysis should be performed for different input modalities (text, image, audio) and different query augmentation strategies. Furthermore, the authors should compare the computational cost of OmniSep with other state-of-the-art sound separation models to provide a clear understanding of its practicality for real-time applications. This analysis should also consider the impact of batch size and sequence length on the computational cost. The authors should also explore potential optimization techniques to reduce the computational overhead of the proposed methods, such as model pruning or quantization.

To mitigate the reliance on ImageBind, the authors should explore alternative query networks that are specifically designed for sound separation tasks. This could involve training a query network from scratch using a large dataset of audio queries and their corresponding sound separations. Alternatively, a lightweight adaptation of ImageBind could be explored, where the pre-trained weights are fine-tuned on the sound separation task. This would allow the model to leverage the general knowledge captured by ImageBind while also adapting to the specific requirements of the task. Furthermore, the authors should investigate the impact of different query network architectures on the overall performance of OmniSep. The authors should also explore methods to incorporate domain-specific knowledge into the query network to improve its ability to extract relevant features for sound separation.

To improve the effectiveness of the Query-Aug method, the authors should focus on developing more robust and comprehensive query sets. This could involve incorporating a wider range of text descriptions, including both common and rare sound categories, as well as more abstract and nuanced descriptions. Additionally, exploring different similarity metrics for query retrieval could lead to more accurate and relevant query augmentation. For example, using a metric that captures semantic similarity rather than just lexical similarity could improve the model's ability to generalize to unseen queries. Furthermore, the Query-Aug method could be extended to incorporate other modalities, such as images or audio, to provide a more comprehensive representation of the query. This would allow the model to leverage the strengths of different modalities and improve its ability to handle complex and diverse queries. The authors should also investigate the impact of the size and diversity of the query set on the performance of the Query-Aug method.

### Questions

1. How does the performance of OmniSep scale with the complexity of the audio mixture? Are there any limitations in terms of the number of sound sources or the level of noise?
2. Can the authors provide more details on the training process, such as the number of epochs, batch size, and learning rate? How sensitive is the model to these hyperparameters?
3. How does the model handle ambiguous queries, where the desired sound is not clearly defined? Are there any mechanisms in place to resolve such ambiguities?
4. What are the potential real-world applications of OmniSep, and how can the model be adapted for specific use cases?

### Rating

6

### Confidence

3

**********
