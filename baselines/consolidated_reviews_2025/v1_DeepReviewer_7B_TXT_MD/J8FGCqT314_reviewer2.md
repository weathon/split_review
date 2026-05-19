### Summary

This paper proposes a new method called D2T2 to improve the performance of Decision Transformer (DT) in stochastic environments. The authors analyze the performance degradation of DT in stochastic environments and identify the variance of returns-to-go (RTG) accumulation as a key factor. To address this issue, D2T2 incorporates temporal difference (TD) learning to provide a more stable guidance signal for DT, which helps DT to focus on high-reward regions and reduce the variance of RTG. The authors evaluate D2T2 on various stochastic tasks and D4RL benchmarks, and the results show that D2T2 outperforms state-of-the-art offline reinforcement learning methods.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

1. The paper provides a detailed analysis of the performance degradation of DT in stochastic environments and identifies the variance of returns-to-go (RTG) accumulation as a key factor. This analysis is insightful and helps to understand the limitations of DT in stochastic environments.
2. The proposed method D2T2 is simple yet effective. By incorporating temporal difference (TD) learning to provide a more stable guidance signal for DT, D2T2 helps DT to focus on high-reward regions and reduce the variance of RTG. This approach is novel and can be easily integrated into existing DT frameworks.
3. The authors evaluate D2T2 on various stochastic tasks and D4RL benchmarks, and the results show that D2T2 outperforms state-of-the-art offline reinforcement learning methods. The experimental results are comprehensive and demonstrate the effectiveness of D2T2.

### Weaknesses

#### Some Related Works


#### comment

1. The paper could benefit from a more detailed discussion of the limitations of the proposed method. For example, how does D2T2 perform in environments with extremely high levels of stochasticity or very long time horizons? Are there specific types of stochasticity that D2T2 struggles with? Addressing these questions would provide a more comprehensive understanding of the method's applicability and robustness.
2. While the paper demonstrates the effectiveness of D2T2, it would be valuable to see a more in-depth analysis of the computational cost associated with the method. How does the training time and inference time of D2T2 compare to that of the original DT and other SOTA methods? Understanding the computational overhead is crucial for assessing the practicality of the approach, especially in resource-constrained environments.
3. The paper mentions that D2T2 eliminates the need for RTG during evaluation, which is a significant advantage. However, it would be helpful to understand the sensitivity of D2T2 to the choice of the guidance signal. How does the performance of D2T2 vary with different guidance signals or different hyperparameter settings? A sensitivity analysis would provide insights into the robustness of the method and guide practitioners in selecting appropriate parameters for their specific applications.
4. The paper's theoretical analysis provides a good foundation for understanding the variance issue in stochastic environments. However, it would be beneficial to see a more rigorous mathematical treatment of the proposed steering guidance mechanism. How does the learned guidance signal interact with the TD learning process, and what are the convergence properties of the proposed method? A deeper theoretical understanding would strengthen the paper's claims and provide a more solid foundation for future research.

### Suggestions

The paper would benefit from a more thorough investigation into the limitations of the proposed D2T2 method. Specifically, the authors should explore the performance of D2T2 in environments with varying degrees of stochasticity. It would be valuable to analyze how the method's performance degrades as the stochasticity increases, and whether there are specific types of stochasticity that pose a greater challenge. For instance, does D2T2 struggle more with high-variance rewards or with complex, multi-modal transition distributions? Furthermore, the analysis should consider the impact of long time horizons on the method's performance. Does the accumulation of errors in the guidance signal lead to a significant degradation in performance over extended time periods? Addressing these questions would provide a more complete picture of the method's applicability and robustness in real-world scenarios. It would also be beneficial to investigate the sensitivity of D2T2 to the choice of the guidance signal. How does the performance of D2T2 vary with different guidance signals or different hyperparameter settings? A sensitivity analysis would provide insights into the robustness of the method and guide practitioners in selecting appropriate parameters for their specific applications.

In addition to the limitations and sensitivity analysis, a more detailed analysis of the computational cost of D2T2 is necessary. The authors should provide a comprehensive comparison of the training time, inference time, and memory requirements of D2T2 with those of the original DT and other state-of-the-art methods. This analysis should include a breakdown of the computational bottlenecks and discuss potential strategies for optimizing the method's efficiency. For example, are there specific components of D2T2 that are computationally expensive, and can these components be replaced or approximated to reduce the overall computational overhead? Furthermore, the authors should investigate the scalability of D2T2 to larger and more complex environments. How does the computational cost of D2T2 scale with the size of the state and action spaces, and how does it compare to other methods in terms of scalability? Understanding these aspects is crucial for assessing the practicality of the approach in real-world applications.

Finally, the paper would be strengthened by a more rigorous mathematical treatment of the proposed steering guidance mechanism. While the paper provides a good intuitive explanation of the method, a deeper theoretical understanding is needed to fully assess its properties. The authors should provide a formal analysis of how the learned guidance signal interacts with the TD learning process, and what are the convergence properties of the proposed method. For example, under what conditions does the guidance signal converge to the optimal policy, and how does the choice of the guidance signal affect the convergence rate? Furthermore, the authors should investigate the stability of the proposed method and provide theoretical guarantees on its performance. A more rigorous mathematical analysis would strengthen the paper's claims and provide a more solid foundation for future research.

### Questions

See the weaknesses.

### Rating

6: marginally above the acceptance threshold

### Confidence

4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

**********
