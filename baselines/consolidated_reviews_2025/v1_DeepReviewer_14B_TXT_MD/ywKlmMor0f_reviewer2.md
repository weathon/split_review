### Summary

This paper introduces MMA, a benchmark specifically designed to evaluate the ability of MLLMs to handle ambiguous queries. The benchmark consists of 261 textual contexts and questions with ambiguous meanings, categorized into lexical, syntactic, and semantic ambiguities. Each ambiguous question is paired with two images that suggest different scenarios, leading to different correct answers. The authors evaluate 24 MLLMs, including both proprietary and open-source models, and find that these models often fail to effectively integrate visual information to resolve textual ambiguities. The paper highlights the limitations of current MLLMs in handling ambiguity and suggests areas for future improvement.

### Soundness

2

### Presentation

3

### Contribution

3

### Strengths

1. The paper introduces MMA, the first benchmark specifically designed to evaluate MLLMs' ability to handle ambiguous queries using visual information. This is a novel contribution to the field, as previous benchmarks have not focused on this specific aspect of MLLM performance.
2. The paper is well-organized and easy to follow. The authors clearly explain the different types of ambiguities and provide examples for each category. The experimental setup is also well-described, and the results are presented in a clear and concise manner.
3. The paper provides a comprehensive evaluation of 24 MLLMs, including both proprietary and open-source models. This allows for a thorough comparison of the performance of different models on the MMA benchmark.

### Weaknesses

#### Some Related Works


#### comment

1. The paper does not provide a detailed analysis of why MLLMs perform poorly on the MMA benchmark. While the authors suggest that this may be due to the models' inability to effectively integrate visual information, they do not provide any evidence to support this claim. A more detailed analysis of the models' behavior on the benchmark would be helpful in understanding the underlying reasons for their poor performance.
2. The paper does not discuss the limitations of the MMA benchmark. For example, the benchmark may not be representative of all types of ambiguities, and the images used in the benchmark may not be realistic or diverse enough. A discussion of these limitations would help to put the results of the paper in context.
3. The paper does not provide any suggestions for how to improve the performance of MLLMs on the MMA benchmark. While the authors suggest that future work should focus on developing models that can better integrate visual information, they do not provide any specific ideas for how to achieve this.

### Suggestions

The paper would benefit from a more in-depth analysis of the failure modes of the MLLMs on the MMA benchmark. Specifically, it is crucial to investigate whether the models are failing to recognize the ambiguity in the text, or if they are failing to correctly associate the visual information with the appropriate interpretation of the text. For example, a detailed error analysis could categorize instances where the model chooses the incorrect answer due to a misinterpretation of the visual context, versus instances where the model fails to resolve the textual ambiguity even when presented with the correct visual context. This could involve examining the attention maps of the models to see which parts of the image are being attended to when making a decision, or analyzing the internal representations of the models to see how they are encoding the ambiguous text and the visual information. Such an analysis would provide a more nuanced understanding of the limitations of current MLLMs in handling ambiguous queries.

Furthermore, the paper should address the limitations of the MMA benchmark more thoroughly. While the authors acknowledge that the benchmark may not be exhaustive, a more detailed discussion of the types of ambiguities that are not covered by the benchmark would be beneficial. For instance, the benchmark could be expanded to include more complex forms of syntactic ambiguity, such as those involving nested structures or long-range dependencies. Additionally, the diversity of the images could be improved by including images with more complex scenes, varying lighting conditions, and different viewpoints. The authors could also consider including images that are intentionally misleading or ambiguous, to further challenge the models' ability to integrate visual and textual information. A more detailed discussion of these limitations would help to put the results of the paper in context and would provide a roadmap for future research.

Finally, the paper should provide more concrete suggestions for how to improve the performance of MLLMs on the MMA benchmark. While the authors suggest that future work should focus on developing models that can better integrate visual information, they do not provide any specific ideas for how to achieve this. For example, the authors could explore the use of attention mechanisms that are specifically designed to handle ambiguous queries, or they could investigate the use of multi-modal pre-training techniques that explicitly encourage the model to integrate visual and textual information. Another approach could be to incorporate external knowledge sources to help resolve ambiguities. For example, a model could use a knowledge graph to disambiguate the meaning of a word based on the context provided by the image. These are just a few examples of how the paper could provide more concrete suggestions for future research.

### Questions

1. Can you provide more details on how the images were selected or generated for the benchmark? Were the images manually selected or generated using a specific algorithm? How did you ensure that the images accurately represented the different interpretations of the ambiguities?
2. Can you provide more details on the error consistency rate? How was this metric calculated, and what does it tell us about the models' ability to handle ambiguities? It would be helpful to see some examples of cases where the models showed high error consistency rates, as well as cases where the models showed low error consistency rates.
3. Can you provide more details on the performance gap between proprietary and open-source models? What are the key differences between these models that may explain their different performance on the MMA benchmark? It would be helpful to see a more detailed comparison of the architectures and training procedures of the different models.

### Rating

5

### Confidence

4

**********
