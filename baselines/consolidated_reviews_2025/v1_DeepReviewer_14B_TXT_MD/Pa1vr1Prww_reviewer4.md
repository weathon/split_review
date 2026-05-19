### Summary

This paper presents a method for identifying sparse autoencoder features that are involved in in-context learning. The authors present a method for identifying task-execution features, which are features that are causally implicated in the model's in-context learning capabilities. They also present a method for identifying task-detection features, which are features that detect when tasks have been performed. The authors validate their methods through a series of experiments on the Gemma-1 2B model, demonstrating that their methods can identify features that are causally implicated in in-context learning.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

- The paper presents a novel method for identifying sparse autoencoder features that are involved in in-context learning. The method is based on the idea of task vectors, which are vectors that represent the model's knowledge of which task to execute.
- The paper presents a method for identifying task-detection features, which are features that detect when tasks have been performed. This is a novel contribution that has not been explored in previous work.
- The paper presents a comprehensive set of experiments that validate the proposed methods. The experiments demonstrate that the methods can identify features that are causally implicated in in-context learning.
- The paper is well-written and easy to understand.

### Weaknesses

#### Some Related Works


#### comment

 - The paper does not provide a clear explanation of how the task vector cleaning algorithm works. It would be helpful to provide a more detailed explanation of the algorithm, including the specific steps involved and the rationale behind each step.
- The paper does not provide a clear explanation of how the task-detection features are identified. It would be helpful to provide a more detailed explanation of the method, including the specific steps involved and the rationale behind each step.
- The paper does not provide a clear explanation of how the steering experiments are conducted. It would be helpful to provide a more detailed explanation of the experiments, including the specific steps involved and the rationale behind each step.
- The paper does not provide a clear explanation of how the causal analysis is conducted. It would be helpful to provide a more detailed explanation of the analysis, including the specific steps involved and the rationale behind each step.
- The paper does not provide a clear explanation of how the results are interpreted. It would be helpful to provide a more detailed explanation of the results, including the specific steps involved and the rationale behind each step.

### Suggestions

The paper would benefit from a more detailed explanation of the task vector cleaning algorithm. Specifically, the authors should clarify how the initial task vectors are obtained, what specific optimization techniques are used to refine these vectors, and how the stopping criteria are determined. For example, are the task vectors initialized randomly, or are they derived from specific input-output pairs? What is the objective function being optimized during the cleaning process? Is it a loss function that encourages the task vector to be sparse and still effective in inducing the desired task? Providing these details would significantly enhance the reproducibility and understanding of the proposed method. Furthermore, it would be beneficial to include a visualization of the task vector before and after the cleaning process to illustrate the effect of the algorithm.

Regarding the identification of task-detection features, the authors should provide a more detailed explanation of the method. It is unclear how the task-detection features are related to the task-execution features. Are they identified independently, or are they derived from the task-execution features? The authors should clarify the specific criteria used to determine if a feature is a task-detection feature. For example, is it based on the feature's activation pattern in response to specific task-related inputs? What is the threshold for determining if a feature is a task-detection feature? A more detailed explanation of the method, including the specific steps involved and the rationale behind each step, would be beneficial. Additionally, it would be helpful to provide examples of task-detection features for different tasks to illustrate the concept.

Finally, the paper should provide a more detailed explanation of the steering experiments and the causal analysis. For the steering experiments, the authors should clarify how the task-execution features are used to steer the model. Are the features added to the model's activations, or are they used to modify the model's parameters? What is the specific loss function used to evaluate the steering performance? For the causal analysis, the authors should clarify how the causal effects of the task-detection features are measured. Are they using a specific causal inference framework, such as do-calculus? What are the specific interventions performed on the model to measure the causal effects? Providing these details would significantly enhance the reproducibility and understanding of the proposed method. Furthermore, it would be beneficial to include a visualization of the causal relationships between the task-detection features and the task-execution features.

### Questions

- How does the task vector cleaning algorithm work? What are the specific steps involved in the algorithm, and what is the rationale behind each step?
- How are the task-detection features identified? What are the specific steps involved in the method, and what is the rationale behind each step?
- How are the steering experiments conducted? What are the specific steps involved in the experiments, and what is the rationale behind each step?
- How is the causal analysis conducted? What are the specific steps involved in the analysis, and what is the rationale behind each step?
- How are the results interpreted? What are the specific steps involved in the interpretation, and what is the rationale behind each step?

### Rating

6

### Confidence

3

**********
