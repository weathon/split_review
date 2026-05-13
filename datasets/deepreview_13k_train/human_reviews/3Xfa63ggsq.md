# AlignIQL: Policy Alignment in Implicit Q-Learning through Constrained Optimization

- Decision: Reject
- Scores: 6, 5, 5

## Abstract
Implicit Q-learning (IQL) serves as a strong baseline for offline RL, which never needs to evaluate actions outside of the dataset through quantile regression. However, it is unclear how to recover the implicit policy from the learned implicit Q-function and whether IQL can utilize weighted regression for policy extraction. IDQL reinterprets IQL as an actor-critic method and gets weights of implicit policy, however, this weight only holds for the optimal value function under certain critic loss functions. In this work, we introduce a different way to solve the $\textit{implicit policy-finding problem}$ (IPF) by formulating this problem as an optimization problem. Based on this optimization problem, we further propose two practical algorithms AlignIQL and AlignIQL-hard, which inherit the advantages of decoupling actor from critic in IQL and provide insights into why IQL can use weighted regression for policy extraction. Compared with IQL and IDQL, we find that our method keeps the simplicity of IQL and solves the implicit policy-finding problem.  Experimental results on D4RL datasets show that our method achieves competitive or superior results compared with other SOTA offline RL methods. Especially in complex sparse reward tasks like AntMaze and Adroit, our method outperforms IQL and IDQL by a significant margin.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper considers policy extraction problem, where sometimes in offline RL, existing algorithms only learn value function, and policy extraction problem is to find a policy that coorespond to the policy and does not perform OOD actions. The paper considers distilling policies from value functions learned with IQL algorithm, and propose the implicit policy-finding problem. The solution of the IPF problem leads to the proposed AlignIQL algorithm, from a careful derivation of the IPF formulation. In the experiment, the proposed method is compared with several baselines with competitive performance.

### Strengths
1. The proposed method is derived rigorously.
2. The experiment shows that the proposed method has good empirical performance compared with other baselines on standard benchmarks.

### Weaknesses
1. The formulation aims to use a general regularization function $f$, which is a good attempt. However, the remaining results seems to rely on the case that $f(x) = \log(x)$. Does the derivation of the objective and the resulting algorithm still hold if we use a different regularization function, and how would the choice of $f$ impact the final policy? It is unclear if the theoretical results generalize beyond the logarithmic case, and what conditions are required for other choices of $f$ to be valid.
2. Remark 5.7 seems very hand-wavy. How does the algorithm ensure that the action with the positive advantage is chosen? It does not seem to be reflected in the loss function. The explanation of how the weighting scheme in Eq 15 leads to selecting actions with positive advantage is not sufficiently clear. The connection between the loss function and the desired behavior of selecting actions with high Q-values relative to V is not explicitly shown. 
3. While the result in table 1 looks impressive, I am not sure if this can serve a strong evidence that the proposed method is better than AWR. The proposed method is equipped with diffusion policies, but the IQL (AWR) baseline seem to only use MLP so it might not be a fair comparison. The comparison is not an apples-to-apples comparison due to the different policy architectures used. The advantage of the proposed method might be due to the diffusion policy rather than the core algorithmic contribution.
4. The result in table 1 is missing standard deviation. 
5. The goal of section 6.2 is unclear. What is the baseline that is compared against in this section? The purpose of the experiments in section 6.2 is not clearly stated, and it is difficult to understand what the authors are trying to demonstrate in this section. The comparison is not well-defined, and it is unclear what the baseline is.
6. Some minor issues: a) in eq. 1, is a $\pi(a \mid s)$ missing? b) in eq. 2, where is the $Q_{\theta}$ from? It does not appear eq. 1. c) in eq. 7, the notation $a$ is overloaded in $a' \sim \pi(a \mid s)$.

### Questions
see above

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper proposes AlignIQL (in two versions) to address the implicit policy-finding problem. The authors formulate it as a constrained optimization problem and derive a closed-form solution. The performance of AlignIQL is competitive compared to the baselines.

### Strengths
- This paper introduces a new approach to tackle the implicit policy-finding problem, combining theoretical rigor with practical effectiveness in offline RL.
- The proposed algorithm, AlignIQL, performs well across varied tasks, demonstrating versatility and effectiveness across different offline RL benchmarks.

### Weaknesses
 - While AlignIQL is rigorous, it adds complexity to training by requiring additional multiplier networks and diffusion models, which may increase computational costs and sensitivity to hyperparameters. The scalability of the method is also a concern; can it be extended to image-based tasks?
- The authors do not explain the use of diffusion modeling in the methods section.
- The performance of AlignIQL raises some concerns:
    - The authors argue that MuJoCo tasks are already saturated for offline RL, which I agree with. However, AlignIQL's performance is also considerably worse than Diffusion QL and even worse than IQL in 4 out of 9 tasks. Given that AlignIQL consumes more computational resources, this discrepancy is problematic.
    - There is a significant performance difference between the authors' version and the original IDQL paper, which further leaves the reader uncertain about the supposed improvements in AlignIQL's performance.
    - The results were obtained using inconsistent hyperparameters, yet the authors under-analyze the ablation study and hyperparameter sensitivity.
    - The authors state, “Figure 2 shows that as training time increases, the performance of AlignIQL with different N converges to the same value, which shows that AlignIQL is insensitive to N.” This conclusion is not obvious from Figure 2. A clearer approach would be to report the mean and standard deviation of these scores.
    - The optimization techniques may risk overfitting in AntMaze environments with sparse rewards, potentially reducing generalization to new scenarios. More testing on sparse reward tasks would benefit this submission.
- In this submission, "policy alignment" is defined differently from its use in language models. A more formal definition of “policy alignment” should be provided, or the authors could consider renaming it.
- A minor issue: multiple duplicate references appear in the bibliography (e.g., lines 568-573). Additionally, lines 916-917 may contain editing errors.

### Questions
See Weaknesses

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The paper introduces AlignIQL, a novel approach to extracting implicit policies in offline reinforcement learning by formulating the implicit policy-finding problem as a constrained optimization problem. AlignIQL and its variant AlignIQL-hard leverage policy alignment constraints to ensure that the extracted policy reflects the learned Q-function while maintaining the advantages of decoupling the actor and critic in Implicit Q-Learning (IQL). The authors demonstrate that their method achieves competitive or superior performance on D4RL datasets, particularly excelling in complex sparse reward tasks like AntMaze and Adroit, while also being more robust to hyperparameter variations than existing methods. Additionally, the study provides theoretical insights into the conditions under which weighted regression can be effectively utilized for policy extraction in IQL. Overall, the proposed algorithms contribute to a better understanding of the bottlenecks in IQL-style methods and offer a more effective means for implicit policy extraction in offline reinforcement learning.

### Strengths
- The introduction of AlignIQL as a constrained optimization approach represents a significant advancement in offline reinforcement learning, providing a fresh perspective on implicit policy extraction.
- The empirical results demonstrate that AlignIQL and its variant achieve competitive performance across a variety of D4RL benchmarks, particularly in challenging tasks with sparse rewards, indicating the effectiveness of the proposed methods.
- Theoretical Insights: The paper offers valuable theoretical analysis regarding the use of weighted regression for policy extraction, enhancing the understanding of the underlying mechanisms that contribute to the success of IQL methods.
- By incorporating policy alignment constraints, the approach ensures that the extracted policies are both effective and representative of the learned Q-function, leading to improved stability and reliability in offline settings.
- AlignIQL shows increased robustness to variations in hyperparameters compared to existing methods, which is crucial for practical applications where tuning can be challenging.

### Weaknesses
 - While the experiments demonstrate competitive performance on specific D4RL benchmarks, the applicability of AlignIQL to other domains or more diverse environments may not be fully established, limiting its generalizability.
- The proposed framework may introduce additional complexity in implementation compared to existing methods, which could deter practitioners who seek simpler solutions for offline reinforcement learning.
- Although the paper includes comparisons with several baseline methods, it may benefit from a more comprehensive analysis against a broader range of state-of-the-art algorithms to fully contextualize its contributions.
- The performance improvements may be contingent on the quality of the dataset used, raising concerns about the approach’s robustness in real-world scenarios where data can be noisy or incomplete.
- The computational requirements for training AlignIQL could be higher than those of simpler methods, potentially limiting its scalability for larger-scale applications or real-time scenarios.

### Questions
- How does AlignIQL perform in real-world environments with noisy or incomplete datasets? The paper evaluates performance on D4RL benchmarks, but it would be interesting to see how the method handles imperfect data.
- What are the key factors that affect the alignment between the Q-values and the learned policy in AlignIQL? Understanding the sensitivity of the method to different alignment parameters could help clarify its robustness.
- How does the computational complexity of AlignIQL compare to other state-of-the-art offline reinforcement learning methods in terms of training time and resource usage? This would help evaluate the method’s scalability for larger or more complex tasks.
- Is the approach compatible with more advanced neural network architectures, such as transformers, for offline reinforcement learning? Could integrating more modern architectures improve its performance?
- What are the potential limitations of applying AlignIQL to tasks outside of continuous control, such as discrete action spaces or hierarchical tasks? This could provide insight into the method’s broader applicability.

### Soundness
3

### Presentation
3

### Contribution
3
