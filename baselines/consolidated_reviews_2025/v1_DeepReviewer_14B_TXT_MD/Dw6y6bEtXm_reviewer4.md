### Summary

The paper introduces a new framework called Physics-Informed Coarse-grained data Learning (PICL) to address the challenges of modeling physical systems with coarse-grained data and limited data acquisition. The PICL framework consists of an encoding module and a transition module, which are trained using a base-training period followed by a two-stage fine-tuning period. The framework integrates data-driven methods with physics-informed objectives to improve the predictive ability of the model. The effectiveness of PICL is demonstrated across modeling various PDE-governed physical systems.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

1. The paper is well-structured and easy to follow. The authors provide a clear overview of the proposed framework and its components.

2. The paper addresses an important problem in modeling physical systems, where coarse-grained data and limited data acquisition are common challenges.

3. The proposed framework, PICL, is a novel approach that integrates data-driven methods with physics-informed objectives to improve the predictive ability of the model.

4. The authors demonstrate the effectiveness of PICL across modeling various PDE-governed physical systems, showing superior predictive ability compared to existing methods.

5. The paper provides a detailed description of the proposed framework, including the encoding module, transition module, and training strategy.

### Weaknesses

#### Some Related Works


#### comment

1. The paper does not provide a detailed analysis of the computational cost of the proposed framework. It would be helpful to understand the computational requirements of PICL and how it compares to existing methods.

2. The paper does not discuss the limitations of the proposed framework. It would be helpful to understand the potential challenges and limitations of PICL and how it can be further improved.

3. The paper does not provide a detailed analysis of the sensitivity of the proposed framework to different hyperparameters. It would be helpful to understand how the performance of PICL is affected by different hyperparameter settings.

### Suggestions

The paper would benefit from a more thorough discussion of the computational demands of the proposed PICL framework. While the authors mention the use of an encoding module and a transition module, a detailed breakdown of the computational complexity of each component, including the number of parameters, FLOPs, and memory requirements, is needed. Furthermore, a comparison of the computational cost of PICL with existing methods, such as FNO and PINNs, should be provided. This comparison should not only focus on training time but also on inference time, which is crucial for real-time applications. It would be beneficial to include a table or graph that shows how the computational cost scales with the input size and the number of training iterations. This analysis should also consider the impact of different hardware configurations on the computational performance of PICL. For example, the authors could provide results for different GPU architectures and memory sizes.

In addition to computational cost, a more detailed discussion of the limitations of the proposed framework is necessary. The authors should discuss the potential challenges of applying PICL to more complex physical systems, such as those with non-linearities or multi-scale phenomena. It would be helpful to understand the sensitivity of PICL to the quality of the coarse-grained data and how it performs when the data is noisy or incomplete. The authors should also discuss the potential for overfitting and how it can be mitigated. Furthermore, the paper should address the limitations of the current implementation of PICL and suggest potential avenues for future research. For example, the authors could discuss the potential for incorporating more advanced neural network architectures or optimization techniques to improve the performance of PICL. A discussion of the limitations of the current approach in terms of the types of PDEs that can be effectively modeled would also be valuable.

Finally, a more detailed analysis of the sensitivity of the proposed framework to different hyperparameters is needed. The authors should provide a systematic study of how the performance of PICL is affected by different hyperparameter settings, such as the learning rate, batch size, and the number of layers in the encoding and transition modules. This analysis should include a discussion of the optimal hyperparameter settings for different physical systems and how these settings can be determined. It would be helpful to provide a sensitivity analysis that shows how the performance of PICL changes as each hyperparameter is varied. This analysis should also consider the interaction between different hyperparameters and how they affect the overall performance of the framework. The authors should also discuss the potential for using automated hyperparameter tuning techniques to optimize the performance of PICL.

### Questions

1. How does the computational cost of the proposed framework compare to existing methods?

2. What are the potential limitations of the proposed framework, and how can it be further improved?

3. How sensitive is the proposed framework to different hyperparameters, and how can the optimal hyperparameter settings be determined?

### Rating

6: marginally above the acceptance threshold

### Confidence

4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

**********
