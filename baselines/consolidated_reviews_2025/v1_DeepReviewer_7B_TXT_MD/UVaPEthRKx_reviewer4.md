### Summary

This paper introduces a novel approach to address the real-time learning pattern adjustment (RLPA) problem in Knowledge Tracing (KT). The authors propose a method called Cuff-KT, which consists of a controller and a generator. The controller assigns values to learners based on their distribution changes, while the generator produces personalized parameters for the KT model at different stages or groups, enhancing its adaptability without the need for full retraining. The paper presents experimental results on one classic and two latest datasets, demonstrating that Cuff-KT significantly improves current KT models' performance under both intra- and inter-learner shifts, with an average relative increase of 7% on AUC.

### Soundness

2

### Presentation

3

### Contribution

2

### Strengths

1. The paper is well-structured and easy to follow, with clear explanations of the proposed method and experimental setup.

2. The authors provide a thorough analysis of the experimental results, including ablation studies and comparisons with baseline methods.

3. The paper addresses a relevant and challenging problem in the field of Knowledge Tracing, which has practical implications for improving the accuracy of educational systems.

### Weaknesses

#### Some Related Works


#### comment

1. The paper lacks a detailed explanation of how the controller and generator interact with each other. Specifically, the mechanism by which the controller's output influences the generator's parameter generation is not clearly articulated. The paper should provide a more detailed description of the information flow between these two components, including the specific mathematical operations and transformations involved. Without this clarity, it is difficult to fully understand the proposed method's inner workings and assess its novelty.

2. The paper does not provide sufficient justification for the choice of the specific architecture used for the generator. While the authors mention using a dual-tower model, they do not explain why this particular architecture was chosen over other alternatives, such as a simpler feedforward network or a recurrent model. A more detailed discussion of the design choices and their impact on the model's performance is needed. This should include a comparison with other potential architectures and a rationale for the selected one.

3. The paper does not discuss the computational complexity of the proposed method, particularly in relation to the size of the dataset and the number of learners. The authors should provide an analysis of the time and space requirements of the Cuff-KT method, including a comparison with existing approaches. This analysis should consider the impact of different parameters, such as the number of layers in the generator and the size of the hidden states, on the computational cost. Without this information, it is difficult to assess the practicality of the proposed method for large-scale applications.

### Suggestions

To address the lack of clarity regarding the interaction between the controller and generator, the authors should provide a more detailed explanation of the information flow. This should include a step-by-step description of how the controller's output is used to influence the generator's parameter generation. For example, if the controller outputs a scalar value, how is this value used to modulate the generator's parameters? Are there any specific mathematical operations involved, such as addition, multiplication, or concatenation? Furthermore, the authors should clarify whether the controller's output is a single value or a vector, and how this affects the generator's input. A clear diagram illustrating the data flow between the controller and generator would also be beneficial. This would help readers better understand the proposed method and assess its novelty.

Regarding the choice of the generator's architecture, the authors should provide a more thorough justification for their design decisions. This should include a comparison with other potential architectures, such as simpler feedforward networks or recurrent models, and a discussion of their respective strengths and weaknesses in the context of the proposed method. For example, why was a dual-tower model chosen over a simpler feedforward network? What specific advantages does the dual-tower model offer in terms of capturing the complex relationships between learner behavior and knowledge state? The authors should also discuss the impact of different architectural choices on the model's performance, including the number of layers, the size of the hidden states, and the type of activation functions used. This would help readers understand the rationale behind the chosen architecture and assess its suitability for the proposed task.

Finally, the authors should provide a detailed analysis of the computational complexity of the proposed method. This should include a discussion of the time and space requirements of the Cuff-KT method, as well as a comparison with existing approaches. The analysis should consider the impact of different parameters, such as the number of layers in the generator and the size of the hidden states, on the computational cost. For example, how does the computational cost scale with the size of the dataset and the number of learners? What are the trade-offs between model performance and computational cost? This analysis should also include a discussion of the practical implications of the computational cost, such as the feasibility of using the proposed method for large-scale applications. This would help readers assess the practicality of the proposed method and its potential for real-world deployment.

### Questions

1. How does the proposed method handle the potential for overfitting, especially given that the generator is trained on the same data it is intended to generalize to?

2. What is the computational complexity of the proposed method, particularly in relation to the size of the dataset and the number of learners? How does it compare to existing approaches?

### Rating

6

### Confidence

4

**********
