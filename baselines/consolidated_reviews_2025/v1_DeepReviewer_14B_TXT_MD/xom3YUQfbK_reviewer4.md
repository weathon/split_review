### Summary

The authors propose a framework to compare two models trained on the same dataset by capturing and verbalizing their differences. The framework works by serializing a representative sample of input instances (from the dataset) and the corresponding model outputs in a JSON format. The serialization, along with a task description, is passed to the LLM through a zero-shot-based prompt. The LLM then analyzes the patterns from the serialization, captures the inconsistencies in the predictions between the two models, and summarizes them in human-understandable texts.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

The authors propose a novel framework to compare two models trained on the same dataset by capturing and verbalizing their differences. The authors also propose a novel protocol to evaluate the verbalization of the framework. The authors also perform extensive experiments on different datasets and models to validate the effectiveness of the framework.

### Weaknesses

#### Some Related Works


#### comment

The authors only evaluate the framework on tabular data, which may limit the generalizability of the framework to other types of data. The authors should consider evaluating the framework on other types of data, such as image, text, or audio data, to demonstrate its effectiveness in different domains. Specifically, the framework's reliance on JSON serialization of input instances and model outputs may not be directly applicable to non-tabular data, where the input representation and model outputs are often more complex and high-dimensional. For instance, image data would require a method to serialize pixel values or feature maps, and text data would need a way to represent token embeddings or attention weights. The current framework does not address these challenges, which could significantly impact its performance and applicability in other domains. Furthermore, the evaluation metric, which relies on an external LLM to infer the second model's output, may introduce biases or inconsistencies depending on the complexity of the task and the quality of the LLM's reasoning capabilities. This could lead to an overestimation of the framework's performance, especially in scenarios where the LLM struggles to accurately infer the model's behavior.

### Suggestions

To enhance the generalizability of the proposed framework, the authors should explore methods for adapting the JSON serialization process to handle non-tabular data. For image data, this could involve incorporating techniques such as feature extraction using pre-trained convolutional neural networks (CNNs) and serializing the resulting feature maps. For text data, the authors could consider using transformer-based models to generate contextualized word embeddings and serialize these embeddings along with attention weights. The framework should also be evaluated on tasks that involve more complex model outputs, such as bounding boxes for object detection or sequence predictions for natural language processing. This would provide a more comprehensive assessment of the framework's ability to capture and verbalize differences between models across diverse domains. Furthermore, the authors should investigate alternative evaluation metrics that are less reliant on the reasoning capabilities of external LLMs. This could involve using metrics that directly compare the model outputs or employing human evaluators to assess the quality of the verbalizations. This would help to mitigate potential biases and provide a more robust evaluation of the framework's performance. 

Additionally, the authors should consider the computational cost associated with the framework, especially when dealing with large datasets or complex models. The process of serializing input instances and model outputs, along with the LLM-based analysis, could be computationally expensive. The authors should explore techniques for optimizing the framework's performance, such as using more efficient serialization methods or employing techniques for reducing the computational burden of LLM inference. This would make the framework more practical for real-world applications. The authors should also investigate the sensitivity of the framework to different LLMs and prompt variations. The performance of the framework may be influenced by the choice of LLM and the specific prompt used to elicit the verbalizations. The authors should conduct a thorough analysis of these factors to ensure the robustness and reliability of the framework. This analysis should include a comparison of different LLMs and prompt variations, as well as an investigation of the impact of these factors on the quality of the verbalizations.

Finally, the authors should provide a more detailed analysis of the types of differences that the framework is able to capture and verbalize. It would be beneficial to understand the limitations of the framework in terms of the types of model differences it can effectively identify. For example, the framework may be more effective at capturing differences in model predictions on specific input instances, but less effective at capturing differences in model architectures or training procedures. The authors should provide a more detailed analysis of these limitations and discuss potential avenues for future research to address them. This would provide a more complete understanding of the framework's capabilities and limitations, and guide future research in this area.

### Questions

1. How does the framework handle cases where the two models being compared have very different performance levels? Does it generate different verbalizations for pairs of models with varying levels of performance difference?
2. How does the framework handle cases where the two models being compared have different types of errors? Does it generate different verbalizations for pairs of models with varying types of errors?
3. How does the framework handle cases where the two models being compared have different levels of confidence in their predictions? Does it generate different verbalizations for pairs of models with varying levels of confidence?
4. How does the framework handle cases where the two models being compared have different levels of interpretability? Does it generate different verbalizations for pairs of models with varying levels of interpretability?
5. How does the framework handle cases where the two models being compared have different levels of complexity? Does it generate different verbalizations for pairs of models with varying levels of complexity?

### Rating

6

### Confidence

4

**********
