### Summary

This paper proposes a new domain randomization method, DORAEMON, which maximizes the entropy of the training distribution while retaining generalization capabilities. The proposed method is validated on several simulation tasks and one real-world task.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

1. The idea is simple and easy to implement.
2. The paper is well-written and easy to understand.
3. The proposed method is validated on several simulation tasks and one real-world task.

### Weaknesses

#### Some Related Works


#### comment

1. The real-world task is a pushing task, which is relatively simple. It would be better to evaluate the proposed method on more complex tasks, such as object manipulation or locomotion tasks. The current evaluation lacks the complexity to fully demonstrate the method's robustness and generalizability to diverse real-world scenarios. Specifically, the pushing task, while useful as a starting point, does not capture the intricacies of tasks involving articulated objects, dynamic environments, or more intricate contact dynamics. 
2. The paper does not discuss the limitations of the proposed method. For example, how does the method perform when the environment is very different from the training environment? What are the computational costs of the method? The absence of a discussion on the method's limitations makes it difficult to assess its practical applicability and potential failure modes. For instance, it is unclear how the method would behave if the real-world environment exhibits significant variations in parameters such as friction, mass, or sensor noise compared to the simulation environment. Furthermore, the computational overhead of the proposed method, especially in terms of memory and time, is not quantified, which is crucial for practical deployment.

### Suggestions

To strengthen the paper, the authors should consider evaluating the proposed method on more complex robotic tasks. For example, object manipulation tasks involving grasping, lifting, and placing objects with varying shapes and sizes would provide a more comprehensive assessment of the method's capabilities. Additionally, locomotion tasks, such as walking or running on different terrains, would further demonstrate the method's robustness to dynamic environments and complex contact dynamics. These tasks would not only provide a more rigorous evaluation but also highlight the method's potential for real-world applications. Furthermore, the evaluation should include a detailed analysis of the method's performance under different levels of environmental variation, such as changes in friction, mass, and sensor noise. This would provide a better understanding of the method's limitations and its ability to generalize to unseen environments.

In addition to more complex tasks, the authors should provide a thorough discussion of the method's limitations. This should include an analysis of the method's sensitivity to hyperparameter settings, its computational costs, and its performance under extreme environmental variations. For example, the authors could investigate how the method's performance degrades as the difference between the training and testing environments increases. They could also analyze the computational overhead of the method in terms of memory usage and training time, and compare it to other domain randomization techniques. This would provide a more complete picture of the method's strengths and weaknesses and help potential users understand its practical limitations. The authors should also consider providing guidelines for selecting appropriate hyperparameter values for different tasks and environments.

Finally, the authors should consider including a more detailed analysis of the method's failure modes. This would involve identifying specific scenarios where the method fails to generalize or performs poorly. For example, the authors could investigate whether the method struggles with tasks that require precise control or those that involve complex contact interactions. By understanding the method's failure modes, the authors can provide valuable insights into its limitations and suggest potential directions for future research. This analysis should also include a discussion of how the method's performance is affected by the choice of the success indicator function and the probability of success, as these parameters can significantly impact the method's behavior.

### Questions

1. How does the proposed method perform on more complex tasks?
2. What are the limitations of the proposed method?
3. How does the proposed method perform when the environment is very different from the training environment?
4. What are the computational costs of the method?

### Rating

6: marginally above the acceptance threshold

### Confidence

4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

**********
