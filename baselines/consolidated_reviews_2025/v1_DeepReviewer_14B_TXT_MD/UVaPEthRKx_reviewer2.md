### Summary

The paper introduces Cuff-KT, a novel method for Real-time Learning Pattern Adjustment (RLPA) in Knowledge Tracing (KT) models. It addresses the challenges of intra- and inter-learner shifts by using a controller and a generator to adapt model parameters without fine-tuning, demonstrating a 7% average increase in AUC across multiple datasets.

### Soundness

2

### Presentation

2

### Contribution

2

### Strengths

1. The paper introduces a novel task, RLPA, which addresses the dynamic nature of learner behavior in educational settings, filling a gap in existing KT research.
2. The proposed Cuff-KT method is tuning-free, fast, and flexible, making it practical for real-world applications.
3. The paper provides a clear and well-structured presentation of the problem, methodology, and experimental results.

### Weaknesses

#### Some Related Works


#### comment

1. The paper lacks a detailed explanation of the theoretical underpinnings of the controller and generator, particularly regarding how they adapt to intra- and inter-learner shifts.
2. The paper does not provide a thorough analysis of the computational complexity and efficiency of Cuff-KT compared to fine-tuning-based methods.
3. The paper could benefit from a more detailed discussion of the limitations of Cuff-KT and potential areas for future research.

### Suggestions

The paper should provide a more detailed explanation of the controller and generator's mechanisms, particularly how they adapt to intra- and inter-learner shifts. The current description lacks the necessary depth to fully understand the adaptive process. For example, the paper mentions that the controller identifies learners with significant changes in knowledge state distribution, but it does not specify the exact metrics or thresholds used to determine these changes. A more rigorous explanation of the mathematical formulation of the controller's decision-making process is needed. Similarly, the generator's method for generating personalized parameters based on real-time samples requires further clarification. The paper should detail the specific algorithms or techniques used to create these parameters, including how the relative relationship between question difficulty and learner ability is quantified and incorporated into the parameter generation process. Without this level of detail, it is difficult to assess the robustness and generalizability of the proposed method.

Furthermore, the paper needs a more thorough analysis of the computational complexity and efficiency of Cuff-KT compared to fine-tuning-based methods. While the paper claims that Cuff-KT is faster and more efficient, it does not provide a detailed breakdown of the computational costs associated with each step of the proposed method. A comparison of the time and space complexity of Cuff-KT with fine-tuning, including the number of parameters updated and the computational overhead of the controller and generator, is necessary. The paper should also discuss the scalability of Cuff-KT, particularly in scenarios with a large number of learners or questions. A quantitative analysis of the computational resources required by Cuff-KT, such as memory usage and processing time, would strengthen the paper's claims of efficiency. This analysis should also consider the impact of different hyperparameter settings on the computational cost of Cuff-KT.

Finally, the paper should include a more detailed discussion of the limitations of Cuff-KT and potential areas for future research. The current discussion is too brief and does not fully address the potential shortcomings of the proposed method. For example, the paper should discuss the sensitivity of Cuff-KT to the quality of the input data and the potential impact of noisy or incomplete data on its performance. It should also explore the limitations of the generator's ability to capture the full complexity of individual learning patterns, particularly in cases where learners exhibit highly irregular or unpredictable behavior. The paper should also consider the potential for Cuff-KT to be integrated with other KT models or learning analytics techniques to further improve its performance. A more comprehensive discussion of these limitations and future directions would enhance the paper's overall impact and provide valuable insights for future research.

### Questions

1. How does Cuff-KT handle the cold-start problem for new learners or questions?
2. Can the authors provide more insights into the choice of hyperparameters for the controller and generator?
3. How does Cuff-KT perform in scenarios with highly irregular or unpredictable learner behavior?

### Rating

5

### Confidence

3

**********
