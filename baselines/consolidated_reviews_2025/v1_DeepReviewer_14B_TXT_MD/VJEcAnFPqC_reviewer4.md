### Summary

This paper studies stepwise inference in Transformers using a synthetic graph navigation task. The authors find that stepwise inference can improve the model's performance, especially when the training data contains paths that are shorter than the test paths. They also observe a tradeoff between diversity and accuracy in the model's output, as well as a simplicity bias towards shorter paths. The authors also analyze the model's failure modes and the mechanistic basis of the learned algorithm.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

- The paper is well-written and easy to follow.
- The proposed synthetic task is a good abstraction of stepwise inference and allows for controlled experiments.
- The paper provides a detailed analysis of the model's behavior and the underlying mechanisms.
- The paper makes several interesting observations, such as the diversity-accuracy tradeoff and the simplicity bias.

### Weaknesses

#### Some Related Works


#### comment

 - The paper does not provide a clear explanation of how the proposed task relates to real-world stepwise inference problems.
- The paper does not compare the proposed method to other stepwise inference methods or to other models.
- The paper does not discuss the limitations of the proposed method or the potential for future work.

### Suggestions

The paper would benefit from a more thorough discussion of the connection between the synthetic graph navigation task and real-world stepwise inference problems. While the authors claim the task captures the essence of multi-step reasoning, they should provide concrete examples of how this translates to practical applications. For instance, how does the graph structure and node traversal in their task relate to the steps involved in solving a complex reasoning problem in natural language processing? A more detailed explanation, perhaps with a specific example, would greatly enhance the paper's impact and clarify the relevance of the proposed task. Furthermore, the authors should consider discussing the limitations of their task in capturing the full complexity of real-world scenarios, such as the presence of noise, ambiguity, or the need for external knowledge.

To strengthen the paper's contribution, the authors should include a more comprehensive comparison of their method with existing stepwise inference techniques. While the authors mention that their work is primarily focused on understanding the mechanisms of stepwise inference, a comparison with other methods would provide valuable context and highlight the advantages and disadvantages of their approach. This comparison should not be limited to just performance metrics, but also include an analysis of the computational complexity, memory requirements, and the interpretability of the different methods. For example, how does the proposed method compare to chain-of-thought prompting or other methods that explicitly guide the model through intermediate steps? A detailed comparison would help position the proposed method within the broader landscape of stepwise inference techniques and provide a more complete picture of its strengths and weaknesses.

Finally, the paper should include a more detailed discussion of the limitations of the proposed method and the potential avenues for future work. While the authors touch upon some limitations, they should delve deeper into the specific challenges that their method faces. For example, how does the method perform when the graph structure is more complex or when the task requires more sophisticated reasoning? What are the computational bottlenecks of the proposed approach, and how can they be addressed? Furthermore, the authors should discuss potential future research directions, such as exploring different graph structures, incorporating external knowledge, or applying the method to other types of stepwise inference problems. A more thorough discussion of these aspects would provide a more complete and balanced view of the proposed method and its potential impact.

### Questions

- How does the proposed task relate to real-world stepwise inference problems?
- How does the proposed method compare to other stepwise inference methods or to other models?
- What are the limitations of the proposed method, and what are the potential avenues for future work?

### Rating

6: marginally above the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********
