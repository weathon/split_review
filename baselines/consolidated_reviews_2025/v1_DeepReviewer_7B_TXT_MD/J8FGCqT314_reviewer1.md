### Summary

This paper proposes a new approach to address the performance degradation of Decision Transformer (DT) in stochastic environments. DT, a sequence prediction-based method, has shown strong performance in deterministic tasks but struggles with stochastic ones due to the variance in returns-to-go (RTG) accumulations. The authors identify this variance as a key factor behind DT's reduced performance in stochastic settings. To tackle this, they introduce DT with Temporal Difference via Next-State Guidance (D2T2), which incorporates a novel steering guidance mechanism. This mechanism uses a learned guidance signal derived from temporal difference learning to help DT navigate towards high-reward regions more effectively. The method also eliminates the need for RTG during evaluation, which is a common challenge for DT.

### Soundness

2 fair

### Presentation

2 fair

### Contribution

2 fair

### Strengths

- The paper is well-written and easy to follow. The authors provide a thorough analysis of why DT struggles in stochastic environments, linking it to the variance in RTG accumulations. This analysis is supported by a theoretical framework and empirical evidence, making the problem statement clear and compelling.

- The proposed D2T2 method is a novel approach that integrates temporal difference (TD) learning with DT to address the variance issue. By using a learned steering guidance mechanism, D2T2 helps DT focus on high-reward regions, improving its performance in stochastic tasks. This approach is well-motivated and provides a fresh perspective on enhancing DT's robustness.

- The paper includes extensive experiments across various environments, including stochastic benchmarks and D4RL datasets. The results demonstrate that D2T2 outperforms state-of-the-art (SOTA) methods in stochastic settings, highlighting its effectiveness and potential impact.

- The authors also address the practical challenge of eliminating RTG during evaluation, which is a significant hurdle for DT. By incorporating TD learning, D2T2 provides a more practical solution for evaluating and deploying DT in real-world scenarios.

### Weaknesses

#### Some Related Works


#### comment

 - The paper could benefit from a more detailed discussion of the limitations of the proposed method. For instance, how does D2T2 perform in environments with extremely high levels of stochasticity or very long time horizons? Are there specific types of stochasticity that D2T2 struggles with? Addressing these questions would provide a more comprehensive understanding of the method's applicability and robustness.

- While the paper demonstrates the effectiveness of D2T2, it would be valuable to see a more in-depth analysis of the computational cost associated with the method. How does the training time and inference time of D2T2 compare to that of the original DT and other SOTA methods? Understanding the computational overhead is crucial for assessing the practicality of the approach, especially in resource-constrained environments.

- The paper mentions that D2T2 eliminates the need for RTG during evaluation, which is a significant advantage. However, it would be helpful to understand the sensitivity of D2T2 to the choice of the guidance signal. How does the performance of D2T2 vary with different guidance signals or different hyperparameter settings? A sensitivity analysis would provide insights into the robustness of the method and guide practitioners in selecting appropriate parameters for their specific applications.

- The paper's theoretical analysis provides a good foundation for understanding the variance issue in stochastic environments. However, it would be beneficial to see a more rigorous mathematical treatment of the proposed steering guidance mechanism. How does the learned guidance signal interact with the TD learning process, and what are the convergence properties of the proposed method? A deeper theoretical understanding would strengthen the paper's claims and provide a more solid foundation for future research.

### Suggestions

The paper would benefit from a more thorough investigation into the limitations of the proposed D2T2 method. Specifically, the authors should explore the performance of D2T2 in environments with varying degrees of stochasticity, including scenarios where the stochasticity is not uniformly distributed or where the transition dynamics are highly non-linear. It would be valuable to analyze how the method's performance degrades as the stochasticity increases, and whether there are specific types of stochasticity that pose a greater challenge. For example, does D2T2 struggle more with high-variance rewards or with complex, multi-modal transition distributions? Furthermore, the analysis should consider the impact of long time horizons on the method's performance. Does the accumulation of errors in the guidance signal lead to a significant degradation in performance over extended time periods? Addressing these questions would provide a more complete picture of the method's applicability and robustness in real-world scenarios.

In addition to the limitations, a detailed analysis of the computational cost of D2T2 is essential. The authors should provide a comprehensive comparison of the training time, inference time, and memory requirements of D2T2 with those of the original DT and other state-of-the-art methods. This analysis should include a breakdown of the computational bottlenecks and discuss potential strategies for optimizing the method's efficiency. For example, are there specific components of D2T2 that are computationally expensive, and can these components be replaced or approximated to reduce the overall computational overhead? Furthermore, the authors should investigate the scalability of D2T2 to larger and more complex environments. How does the computational cost of D2T2 scale with the size of the state and action spaces, and how does it compare to other methods in terms of scalability? Understanding these aspects is crucial for assessing the practicality of the approach in real-world applications.

Finally, the paper should include a more rigorous mathematical analysis of the proposed steering guidance mechanism. While the paper provides a good intuitive explanation of the method, a deeper theoretical understanding is needed to fully assess its properties. The authors should provide a formal analysis of how the learned guidance signal interacts with the TD learning process, and what are the convergence properties of the proposed method. For example, under what conditions does the guidance signal converge to the optimal policy, and how does the choice of the guidance signal affect the convergence rate? Furthermore, the authors should investigate the sensitivity of the method to the choice of hyperparameters, such as the learning rate and the discount factor. A sensitivity analysis would provide insights into the robustness of the method and guide practitioners in selecting appropriate parameters for their specific applications. This analysis should also include a discussion of the limitations of the theoretical analysis and potential directions for future research.

### Questions

- How does D2T2 perform in environments with extremely high levels of stochasticity or very long time horizons?

- What is the computational cost of D2T2 compared to the original DT and other SOTA methods?

- How sensitive is D2T2 to the choice of the guidance signal and hyperparameter settings?

- Can the authors provide a more rigorous mathematical analysis of the proposed steering guidance mechanism?

### Rating

5: marginally below the acceptance threshold

### Confidence

4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

**********
