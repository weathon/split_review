### Summary

This paper introduces a method for automatically adjusting the distribution of randomized simulator parameters in domain randomization. The method is based on maximizing the entropy of the distribution while ensuring that the policy still achieves a certain level of success. The proposed method is evaluated in simulation and on a real robot.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

- The method is simple to implement and seems to perform well.
- The method is evaluated on a real robot task, which is a nice addition to the usual simulation evaluations.
- The paper is well-written and easy to follow.

### Weaknesses

#### Some Related Works


#### comment

 - The method is evaluated on a limited set of tasks. It would be nice to see it evaluated on a wider range of tasks, especially more complex ones.
- The method relies on a success indicator function, which may be difficult to define for some tasks. It is not clear how sensitive the method is to the choice of this function, and what happens when the success criteria are not well-defined or too strict.
- The paper does not provide a theoretical analysis of the method. It is unclear how the entropy maximization relates to the generalization performance of the learned policy, and what guarantees can be provided about the convergence of the algorithm.

### Suggestions

The paper would benefit from a more thorough evaluation across a wider range of tasks, particularly those that are more complex and involve higher degrees of freedom or more intricate dynamics. For example, tasks involving manipulation of deformable objects, or navigation in cluttered environments with dynamic obstacles, would provide a more robust assessment of the method's capabilities. Furthermore, it would be beneficial to compare the performance of the proposed method against other domain randomization techniques, including those that use adaptive parameter adjustment strategies. This would help to better understand the strengths and weaknesses of the proposed approach in comparison to existing state-of-the-art methods. The current evaluation, while including a real robot experiment, is still limited in the diversity of tasks and environments considered.

Further investigation into the sensitivity of the method to the choice of the success indicator function is needed. The paper should include experiments that systematically vary the success criteria and analyze the impact on the learned policy's performance and generalization ability. It would be useful to explore different types of success functions, such as those based on task completion time, energy efficiency, or other task-specific metrics. Additionally, the paper should discuss the potential limitations of the method when the success criteria are too strict or too lenient, and provide guidelines for selecting appropriate success functions for different types of tasks. A more detailed analysis of the interplay between the success function and the entropy maximization objective would also be valuable.

Finally, while a theoretical analysis may be challenging, some discussion of the method's theoretical properties would be beneficial. For instance, it would be useful to explore the relationship between the entropy of the randomized parameters and the generalization performance of the learned policy. It would also be helpful to provide some insights into the convergence properties of the algorithm, and to discuss the conditions under which the method is expected to perform well. Even a qualitative analysis of the method's behavior, based on existing theoretical results in related areas, would significantly strengthen the paper.

### Questions

- How sensitive is the method to the choice of the success indicator function?
- How does the method compare to other domain randomization techniques that do not use entropy maximization?
- What are the limitations of the method?

### Rating

6: marginally above the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********
