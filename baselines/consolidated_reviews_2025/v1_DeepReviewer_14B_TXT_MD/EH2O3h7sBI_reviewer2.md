### Summary

This paper introduces a novel approach called Prompt Gradient Projection (PGP) for continual learning, which integrates prompt-tuning with a gradient projection method. The key idea is that prompt-tuning eliminates the need for a task identifier in gradient projection, while gradient projection provides theoretical guarantees against forgetting for prompt-tuning. The authors deduce that achieving an orthogonal condition for the prompt gradient can effectively prevent forgetting through the self-attention mechanism in vision transformers. The condition equations are realized by performing Singular Value Decomposition (SVD) on an element-wise sum space between the input space and the prompt space. The method is validated on diverse datasets, demonstrating its effectiveness in reducing forgetting in various incremental learning settings.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

1. The paper introduces a novel approach called Prompt Gradient Projection (PGP) that combines prompt-tuning with a gradient projection method for continual learning. This integration is innovative as it leverages the strengths of both techniques to address the challenge of forgetting in continual learning scenarios.
2. The authors provide a theoretical basis for their approach by deducing the orthogonal condition of anti-forgetting for prompt gradients. This adds rigor to the proposed method and offers insights into the underlying mechanisms that contribute to its effectiveness.
3. The paper explores the balance between stability and plasticity in the context of gradient projection, providing a new perspective on this trade-off. The authors demonstrate that the essence of gradient projection lies in updating prompts in the orthogonal space of previous tasks, which is a valuable insight.

### Weaknesses

#### Some Related Works


#### comment

1. The paper could benefit from providing more details on the computational complexity of the proposed method, especially regarding the SVD operation. Understanding the computational overhead would help in assessing the practicality of the approach for large-scale applications. Specifically, the paper should discuss the time and memory complexity of the SVD operation in relation to the dimensionality of the input and prompt spaces, and how this scales with the number of tasks. Furthermore, the paper should provide a breakdown of the computational cost associated with other steps in the algorithm, such as the forward and backward passes, to give a complete picture of the computational demands.
2. While the paper demonstrates the effectiveness of the approach on several benchmark datasets, it would be valuable to see comparisons with a broader range of state-of-the-art continual learning methods. This would provide a more comprehensive understanding of the advantages and limitations of the proposed approach. The comparison should include methods that utilize different continual learning strategies, such as regularization-based methods, replay-based methods, and methods that employ architectural modifications. This would help to contextualize the performance of the proposed method relative to the broader landscape of continual learning techniques.
3. The paper primarily focuses on the theoretical aspects and empirical results of the proposed method. However, providing more insights into the practical implementation details and potential challenges in real-world applications would enhance the paper's impact. For example, the paper could discuss the sensitivity of the method to hyperparameter settings, such as the learning rate and the number of prompt tokens, and how these parameters should be tuned for optimal performance. Additionally, the paper could address potential issues related to the stability of the training process and how to mitigate them.

### Suggestions

To address the lack of detail regarding computational complexity, the authors should include a thorough analysis of the time and memory requirements of their method. This should include a breakdown of the computational cost associated with each step of the algorithm, with a particular focus on the SVD operation. The analysis should consider how the computational cost scales with the dimensionality of the input and prompt spaces, as well as the number of tasks. Furthermore, the authors should provide empirical evidence of the computational cost by reporting the training time and memory usage for different experimental settings. This would allow readers to better assess the practicality of the method for large-scale applications. For example, the authors could provide a table showing the training time and memory usage for different datasets and different numbers of tasks, along with the corresponding dimensionalities of the input and prompt spaces. This would provide a more concrete understanding of the computational overhead associated with the proposed method.

To enhance the comparative analysis, the authors should include a more comprehensive comparison with a broader range of state-of-the-art continual learning methods. This should include methods that utilize different continual learning strategies, such as regularization-based methods (e.g., EWC, SI), replay-based methods (e.g., iCaRL, Deep Generative Replay), and methods that employ architectural modifications (e.g., progressive neural networks). The comparison should be performed on the same datasets and using the same evaluation metrics, to ensure a fair comparison. The authors should also provide a detailed discussion of the strengths and weaknesses of the proposed method relative to the other methods, highlighting the specific scenarios where the proposed method performs best. This would provide a more comprehensive understanding of the advantages and limitations of the proposed approach. For example, the authors could include a table showing the performance of the proposed method and other state-of-the-art methods on different datasets, along with a discussion of the trade-offs between accuracy, forgetting, and computational cost.

To improve the practical impact of the paper, the authors should provide more insights into the practical implementation details and potential challenges in real-world applications. This should include a discussion of the sensitivity of the method to hyperparameter settings, such as the learning rate, the number of prompt tokens, and the threshold parameter. The authors should provide guidelines on how to tune these parameters for optimal performance, and discuss the potential issues related to the stability of the training process. Furthermore, the authors should address potential challenges related to the scalability of the method to more complex datasets and tasks. This could include a discussion of the memory requirements for storing the prompt parameters and the computational cost of the SVD operation for large-scale applications. By addressing these practical considerations, the authors can make their method more accessible and useful to the broader research community.

### Questions

1. Can you provide more details on the computational complexity of the SVD operation, especially in the context of large-scale applications?
2. How does the proposed method compare with other state-of-the-art continual learning methods in terms of both accuracy and computational efficiency?
3. Are there any plans to extend the evaluation to more complex datasets or real-world applications to further validate the effectiveness of the approach?

### Rating

6: marginally above the acceptance threshold

### Confidence

4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

**********
