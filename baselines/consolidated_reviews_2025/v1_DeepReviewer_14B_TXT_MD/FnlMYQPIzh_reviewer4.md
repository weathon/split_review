### Summary

This paper introduces ConvINT, a semi-structured intention framework for conversational understanding, which organizes user intentions into four key aspects: situation, emotion, action, and knowledge. To facilitate the efficient adoption of this framework, the authors propose a Weakly-supervised Reinforced Generation (WeRG) method that scales ConvINT annotations across large datasets with high quality. Experimental results demonstrate that integrating ConvINT with WeRG markedly improves LLMs’ ability to comprehend user intentions, yielding significant gains in downstream tasks such as response generation and task completion.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

1. The proposed ConvINT framework provides a more holistic and fine-grained understanding of user intentions by organizing them into four key aspects: situation, emotion, action, and knowledge. This is a novel approach that goes beyond traditional structured or unstructured representations of user intentions.
2. The authors introduce a Weakly-supervised Reinforced Generation (WeRG) method that scales ConvINT annotations across large datasets with high quality. This is a practical solution to the challenge of annotating large amounts of data for training LLMs.
3. The paper is well-written and easy to follow. The authors provide a clear explanation of the ConvINT framework and the WeRG method, and they present their experimental results in a clear and concise manner.

### Weaknesses

#### Some Related Works


#### comment

1. The paper does not provide a detailed analysis of the computational resources required for training and inference using the proposed ConvINT framework and WeRG method. This information is crucial for assessing the practicality of the proposed approach in real-world applications.
2. The paper could benefit from a more in-depth discussion of the limitations of the proposed ConvINT framework and the WeRG method. For example, how do these methods perform in scenarios with highly ambiguous or context-dependent user intentions? Are there specific types of conversations or domains where the proposed methods might struggle?
3. The evaluation of the WeRG method primarily focuses on the quality of the generated ConvINT data. While this is important, the paper could also explore the efficiency and scalability of the WeRG method in more detail. How does the performance of WeRG scale with the size of the dataset and the complexity of the conversations? Are there any computational bottlenecks or practical challenges in deploying WeRG for very large datasets?

### Suggestions

The paper would benefit from a more thorough analysis of the computational demands of the proposed approach. Specifically, the authors should provide a detailed breakdown of the training time, memory usage, and inference latency for both the ConvINT framework and the WeRG method. This should include a discussion of how these resources scale with the size of the training dataset and the complexity of the conversational context. For instance, what is the impact of increasing the number of training examples on the training time and memory requirements? Furthermore, it would be valuable to understand the computational cost of generating annotations using WeRG, and how this cost compares to alternative annotation methods. This analysis should also consider the hardware requirements, such as GPU memory and CPU cores, needed to effectively utilize the proposed approach. Without this information, it is difficult to assess the practical feasibility of deploying the proposed method in real-world scenarios.

In addition to computational considerations, the paper should also delve deeper into the limitations of the ConvINT framework and the WeRG method. The authors should explore scenarios where the proposed methods might struggle, such as conversations with highly ambiguous or context-dependent user intentions. For example, how does the framework handle situations where the user's emotion is subtle or implicit? What happens when the user's action is not clearly defined or when the knowledge required to understand the conversation is not readily available? A more detailed analysis of these edge cases would provide a more complete picture of the strengths and weaknesses of the proposed approach. Furthermore, the authors should investigate the performance of the proposed methods across different domains and types of conversations. Are there specific types of conversations or domains where the proposed methods perform poorly? Understanding these limitations is crucial for identifying areas for future improvement and for guiding the application of the proposed methods in real-world scenarios.

Finally, the evaluation of the WeRG method should be expanded to include a more comprehensive analysis of its efficiency and scalability. The authors should investigate how the performance of WeRG scales with the size of the dataset and the complexity of the conversations. For example, how does the training time and annotation quality change as the dataset size increases? Are there any computational bottlenecks or practical challenges in deploying WeRG for very large datasets? Furthermore, the authors should explore the impact of different hyperparameter settings on the performance of WeRG. A more thorough analysis of these factors would provide a more complete understanding of the practical limitations of the WeRG method and would help guide its application in real-world scenarios. This analysis should also include a discussion of the trade-offs between annotation quality and computational cost, which is crucial for practical deployment.

### Questions

1. How does the proposed ConvINT framework and WeRG method compare to other state-of-the-art methods for conversational understanding in terms of computational resources required for training and inference?
2. What are the limitations of the proposed ConvINT framework and WeRG method, and how do they perform in scenarios with highly ambiguous or context-dependent user intentions?
3. How does the performance of the WeRG method scale with the size of the dataset and the complexity of the conversations? Are there any computational bottlenecks or practical challenges in deploying WeRG for very large datasets?

### Rating

6

### Confidence

4

**********
