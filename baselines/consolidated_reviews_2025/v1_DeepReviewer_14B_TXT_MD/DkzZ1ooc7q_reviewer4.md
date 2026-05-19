### Summary

This paper proposes a novel framework OmniSep for omni-modality sound separation. The authors introduce a Query-Mixup strategy to blend query features from different modalities during training, enabling the model to optimize multiple modalities concurrently. They also introduce negative queries to eliminate undesired sounds and a retrieval-augmented approach Query-Aug for open-vocabulary sound separation. The model achieves state-of-the-art performance on various sound separation tasks.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

1. The introduction of the Query-Mixup strategy is a novel approach to handling multi-modal queries in sound separation.
2. The negative query concept is innovative and enhances the flexibility of sound separation.
3. The Query-Aug method addresses the challenge of open-vocabulary sound separation, making the model more practical.
4. The paper is well-structured and clearly explains the proposed methods and their significance.

### Weaknesses

#### Some Related Works


#### comment

1. The paper lacks a detailed analysis of the computational complexity and efficiency of the proposed methods. It would be beneficial to understand the trade-offs between performance and computational resources.
2. The reliance on ImageBind as the Query-Net means that the performance of OmniSep is inherently tied to the capabilities of ImageBind. Any limitations or biases in ImageBind could propagate to OmniSep.
3. The Query-Aug method relies on retrieving similar in-domain class queries, which might not always be effective for truly out-of-domain or novel queries. The effectiveness of this approach depends on the quality and coverage of the query set.

### Suggestions

The paper should include a more thorough analysis of the computational demands of the proposed OmniSep framework. Specifically, the authors should provide a breakdown of the computational cost associated with each component of the model, such as the Query-Net, the separation network, and the Query-Augmentation process. This analysis should include metrics such as FLOPs, parameter counts, and memory usage, as well as the inference time for different query modalities. Furthermore, it would be beneficial to compare the computational efficiency of OmniSep with other state-of-the-art sound separation models. This would allow readers to better understand the practical implications of using the proposed method and to assess the trade-offs between performance and computational resources. For example, the authors could provide a table showing the inference time for different query types (text, image, audio) and different audio lengths, which would be very helpful for practical applications.

To address the dependence on ImageBind, the authors should explore alternative query networks or investigate methods to mitigate the impact of ImageBind's limitations. One approach could be to fine-tune ImageBind specifically for the sound separation task, which might improve its performance and reduce the propagation of biases. Another option would be to explore other pre-trained models that are more robust or better suited for this task. Additionally, the authors could investigate methods to make the model more robust to variations in the quality of the query features. For example, they could explore techniques such as data augmentation or adversarial training to improve the model's ability to handle noisy or ambiguous queries. This would make the model more reliable and practical for real-world applications where query quality may vary.

The authors should also provide a more detailed analysis of the Query-Aug method's performance on out-of-domain queries. This analysis should include a quantitative evaluation of the model's ability to generalize to novel queries that are not present in the training set. The authors should also investigate the impact of the size and diversity of the query set on the performance of the Query-Aug method. It would be beneficial to explore different strategies for selecting the most relevant queries from the query set, as well as methods to improve the quality of the retrieved queries. For example, the authors could explore using a more sophisticated similarity metric or incorporating contextual information into the query retrieval process. This would help to ensure that the model can effectively handle a wide range of queries and generalize to new sound separation tasks.

### Questions

1. How does the model perform on sound separation tasks involving sounds or scenarios not well-represented in the VGGSOUND and MUSIC datasets? Are there any specific limitations observed in such cases?
2. What are the potential challenges and solutions for scaling up the training data for OmniSep? How can the model be made more generalizable to a wider range of real-world audio events?
3. How does the performance of OmniSep compare to other state-of-the-art sound separation models on a broader range of datasets and tasks? Are there any specific areas where OmniSep excels or falls short?

### Rating

6

### Confidence

3

**********
