### Summary

The paper introduces ConvINT, a novel semi-structured intention framework that organizes user intentions into four key aspects: situation, emotion, action, and knowledge. The authors propose a Weakly-supervised Reinforced Generation (WeRG) method to efficiently expand ConvINT annotations across large datasets. The framework is evaluated on two conversational datasets, DuRecDial and ESConv, demonstrating its effectiveness in improving downstream tasks such as response generation and task completion.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

1. The paper introduces a novel semi-structured intention framework, ConvINT, which provides a more comprehensive and nuanced understanding of user intentions by organizing them into four key aspects: situation, emotion, action, and knowledge. This framework addresses the limitations of existing structured methods in capturing the complexity of user intentions.
2. The paper proposes a Weakly-supervised Reinforced Generation (WeRG) method to efficiently expand ConvINT annotations across large datasets. The method leverages coarse-to-fine labels and weak supervision signals to generate high-quality ConvINT data, which can be used to enhance downstream tasks.
3. The paper evaluates the proposed ConvINT framework and WeRG method on two conversational datasets, DuRecDial and ESConv. The experimental results demonstrate the effectiveness of the framework in improving downstream tasks such as response generation and task completion.

### Weaknesses

#### Some Related Works


#### comment

1. The paper does not provide a detailed analysis of the computational cost and efficiency of the WeRG method, which is crucial for practical applications. The paper should include a more thorough analysis of the computational resources required for training and inference, including memory usage, training time, and inference time, especially when scaling to larger datasets. This analysis should also consider the impact of different design choices in the WeRG method on computational efficiency.
2. The paper does not discuss the potential biases in the weak supervision signals used to generate ConvINT data. The paper should address how these biases might affect the performance of the proposed method and how they can be mitigated. For example, if the weak supervision signals are derived from a biased dataset, the generated ConvINT data might also be biased, leading to suboptimal performance in downstream tasks. The paper should also discuss the potential for the WeRG method to amplify existing biases.
3. The paper does not provide a detailed comparison with other state-of-the-art methods for intention understanding in conversational AI. The paper should compare the proposed method with other relevant approaches in terms of performance, efficiency, and robustness. This comparison should include a discussion of the advantages and disadvantages of the proposed method compared to existing methods. The paper should also discuss the limitations of the proposed method and suggest future research directions to address these limitations.

### Suggestions

The paper should include a more detailed analysis of the computational cost and efficiency of the WeRG method. This analysis should include a breakdown of the time and memory requirements for each step of the method, such as the weak supervision signal generation, the reinforcement learning training, and the data generation process. The analysis should also consider the impact of different design choices in the WeRG method on computational efficiency, such as the choice of reward function, the number of training epochs, and the size of the training dataset. Furthermore, the paper should discuss the scalability of the method to larger datasets and provide recommendations for optimizing the computational efficiency of the method. This analysis is crucial for assessing the practical applicability of the proposed method in real-world scenarios.

The paper should also address the potential biases in the weak supervision signals used to generate ConvINT data. The authors should discuss the sources of these biases and how they might affect the performance of the proposed method. For example, if the weak supervision signals are derived from a biased dataset, the generated ConvINT data might also be biased, leading to suboptimal performance in downstream tasks. The paper should also discuss the potential for the WeRG method to amplify existing biases. To mitigate these biases, the authors should consider using techniques such as data augmentation, adversarial training, or bias-aware reinforcement learning. The paper should also provide empirical evidence to support the effectiveness of these mitigation strategies.

Finally, the paper should include a more comprehensive comparison with other state-of-the-art methods for intention understanding in conversational AI. This comparison should include a discussion of the performance, efficiency, and robustness of the proposed method compared to existing methods. The paper should also discuss the limitations of the proposed method and suggest future research directions to address these limitations. For example, the paper could compare the proposed method with other semi-structured intention frameworks or with methods that use different types of weak supervision signals. This comparison would help to better position the proposed method within the existing literature and highlight its unique contributions.

### Questions

1. How does the WeRG method handle situations where the weak supervision signals are noisy or incomplete?
2. What are the potential limitations of the proposed ConvINT framework in capturing complex or nuanced user intentions?
3. How does the WeRG method ensure the quality and diversity of the generated ConvINT data?
4. How does the WeRG method handle situations where the user intentions are ambiguous or contradictory?

### Rating

8

### Confidence

4

**********
