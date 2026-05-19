### Summary

The paper proposes SPaR, a method for improving instruction-following in LLMs by generating preference data through tree-search. The authors show that the proposed method is more effective than sampling responses from the model.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

The paper is well-written and easy to follow. The method is intuitive and the results are promising -- the authors show that the proposed method is effective at generating preference data and that it improves performance on instruction-following.

### Weaknesses

#### Some Related Works


#### comment

It is unclear to me what the authors mean when they say that SPaR "does not damage general abilities" (line 375). The reported numbers are higher, but the prompts used for evaluation are the same as the ones used for training. I would enjoy reading an analysis on a held-out set of prompts.

I agree that the method is interesting and the results are promising, but I would have enjoyed a more thorough analysis of the proposed method, for example, by analyzing the depth of the tree search and the number of samples generated per node.

### Suggestions

The claim that SPaR "does not damage general abilities" is not sufficiently supported by the current evaluation. The fact that the evaluation prompts are the same as the training prompts makes it difficult to assess whether the model's improvements are due to genuine generalization or simply memorization. To address this, the authors should evaluate the model on a held-out set of prompts that were not seen during training. This would provide a more robust measure of the model's ability to generalize its instruction-following capabilities to new, unseen tasks. Furthermore, it would be beneficial to analyze the performance of the model on different types of prompts, for example, by categorizing prompts based on their complexity or the type of instruction they require. This would help to identify the specific areas where SPaR is most effective and where it may still struggle.

Regarding the tree search analysis, it would be valuable to explore the impact of different tree search parameters on the quality of the generated preference data. For example, the authors could investigate how the depth of the tree affects the diversity and quality of the negative samples. A deeper tree might lead to more refined negative samples, but it could also increase the risk of overfitting to the specific prompts used for training. Similarly, the number of samples generated per node could also have a significant impact on the performance of the method. A larger number of samples might lead to a more comprehensive exploration of the search space, but it could also increase the computational cost of the method. An analysis of these parameters would provide valuable insights into the trade-offs involved in using tree search for generating preference data and would help to optimize the method for different applications.

Finally, it would be interesting to see a more detailed analysis of the types of errors that the model makes after training with SPaR. Are the errors primarily due to failures to understand the instruction, or are they due to limitations in the model's ability to generate appropriate responses? A qualitative analysis of the model's errors could provide valuable insights into the limitations of the method and could help to guide future research in this area. For example, the authors could categorize the errors based on the type of instruction or the type of response required, and they could analyze the frequency of each type of error. This would help to identify the specific areas where the model needs further improvement.

### Questions

* The authors mention that they use both breadth-first search (BFS) and depth-first search (DFS) for the tree search. Which one is used in the experiments?

### Rating

6

### Confidence

3

**********
