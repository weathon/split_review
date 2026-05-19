### Summary

This paper proposes a new Q-learning algorithm called RegQ, which converges when linear function approximation is used. The authors prove that simply adding an appropriate regularization term ensures the convergence of the algorithm. The stability of RegQ is established using a recent analysis tool based on switching system models. The authors also experimentally show that RegQ converges in environments where Q-learning with linear function approximation is known to diverge.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

1. The authors propose a practical Q-learning algorithm called regularized Q-learning (RegQ), which guarantees convergence under linear function approximation.
2. The authors prove the convergence of the proposed algorithm based on the O.D.E approach together with the switching system model.
3. The authors experimentally show that their algorithm performs faster than other two timescale Q-learning algorithms.

### Weaknesses

#### Some Related Works


#### comment

1. The authors should provide more details on the experimental setup, including the specific environments used and the evaluation metrics. It is not clear how the performance of RegQ is compared to other algorithms, and what are the specific advantages of RegQ in these comparisons. For example, what are the learning curves like, and how does the final performance compare to the optimal policy? The lack of detail makes it difficult to assess the practical significance of the proposed method.
2. The authors should discuss the limitations of their approach and potential directions for future research. For instance, how does the performance of RegQ scale with the size of the state and action spaces? Are there specific types of environments where RegQ is expected to perform poorly? A more thorough discussion of these limitations would provide a more balanced view of the proposed method.

### Suggestions

To address the lack of detail in the experimental setup, the authors should include a comprehensive description of the environments used, including the state and action spaces, the reward functions, and the transition dynamics. They should also clearly specify the evaluation metrics used, such as average reward, cumulative reward, or convergence speed. Furthermore, the authors should provide a detailed comparison of RegQ with other algorithms, including learning curves and final performance metrics. This comparison should not only focus on convergence speed but also on the quality of the learned policy. For example, the authors could compare the learned Q-values with the optimal Q-values to quantify the suboptimality of the learned policy. This would provide a more complete picture of the performance of RegQ and its advantages over existing methods. The authors should also include a discussion of the hyperparameter tuning process, including the range of values explored and the method used to select the optimal hyperparameters.

Regarding the limitations of the approach, the authors should discuss the computational complexity of RegQ, particularly in relation to the size of the state and action spaces. They should also analyze the sensitivity of the algorithm to the choice of the regularization parameter and provide guidelines for selecting this parameter. Furthermore, the authors should explore the potential limitations of RegQ in environments with sparse rewards or delayed feedback. A discussion of these limitations would provide a more balanced view of the proposed method and help guide future research. For example, the authors could investigate the use of more sophisticated regularization techniques or explore the application of RegQ to other types of reinforcement learning problems, such as those with continuous state and action spaces.

Finally, the authors should consider including a more detailed analysis of the theoretical properties of RegQ. While the paper provides a convergence proof, it would be beneficial to explore the rate of convergence and the conditions under which the algorithm is guaranteed to converge to the optimal policy. This analysis could provide a deeper understanding of the algorithm's behavior and help identify potential areas for improvement. The authors could also investigate the robustness of RegQ to noise in the environment or to errors in the function approximation. This would provide a more comprehensive assessment of the algorithm's practical applicability.

### Questions

1. Can the authors provide more details on the experimental setup, including the specific environments used and the evaluation metrics?
2. Can the authors discuss the limitations of their approach and potential directions for future research?

### Rating

6: marginally above the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********
