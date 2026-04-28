# Learn out of the box: optimizing both diversity and performance in Offline Reinforcement Learning

- Decision: Reject
- Avg Score: 5.75
- Scores: 6, 6, 5, 6

## Abstract
In offline reinforcement learning, most existing methods have focused primarily on optimizing performance, often neglecting the promotion of diverse behaviors. While some approaches generate diverse behaviors from well-constructed, heterogeneous datasets, their effectiveness is significantly reduced when applied to less diverse data. To address this, we introduce a novel intrinsic reward mechanism that encourages behavioral diversity, irrespective of the dataset's heterogeneity. By maximizing the mutual information between actions and policies under each state, our approach enables agents to learn a variety of behaviors, including those not explicitly represented in the data. Although performing out-of-distribution actions can lead to risky outcomes, we mitigate this risk by incorporating the ensemble-diversified actor-critic (EDAC) method to estimate Q-value uncertainty, preventing agents from adopting suboptimal behaviors. Through experiments using the D4RL benchmarks on MuJoCo tasks, we demonstrate that our method achieves behavioral diversity while maintaining performance across environments constructed from both heterogeneous and homogeneous datasets.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper introduces a novel approach to offline reinforcement learning that promotes behavioral diversity through an intrinsic reward mechanism based on maximizing mutual information between actions and policies. The proposed method works effectively with homogeneous datasets, enabling agents to learn varied behaviors beyond those present in the training data. Moreover, the approach also incorporates uncertainty estimation through ensemble-diversified actor-critic (EDAC) to avoid OOD issues, demonstrating strong performance across both heterogeneous and homogeneous D4RL benchmark environments.

### Strengths
1. The proposed method effectively promotes policy diversity across both homogeneous and heterogeneous datasets, addressing a significant limitation in existing approaches.
2. The mutual infomation-based intrinsic reward is technically sound and intuitive.
3. The paper is very well-written and easy to follow.

### Weaknesses
1. I am not sure the illustrative example given in Figure 2 is the best scenario to demonstrate behavioral diversity as the demonstrated policies appear relatively similar despite attempting to showcase distinct behaviors.
2. The empirical evaluation's scope is limited, focusing on only three MuJoCo benchmark tasks, which may not fully validate the method's generalizability. The choice of these specific tasks, while common, does not explore the method's performance across a wider range of environments with varying complexities and action spaces, such as those found in the Atari suite or more complex robotic manipulation tasks. This narrow focus makes it difficult to assess the robustness of the proposed approach.
3. The theoretical transition from path diversity to behavior diversity, while conceptually reasonable, requires more justification, particularly regarding equivalence conditions and underlying assumptions. The paper does not sufficiently detail the conditions under which maximizing path diversity directly translates to meaningful behavioral diversity, especially in complex environments where multiple paths can lead to similar outcomes.

### Questions
1. How does dataset quality impact the method's effectiveness in promoting behavioral diversity?
2. Could the authors provide a comprehensive hyperparameter analysis for $\lambda$ and $N$ to better understand their influence on performance?
3. How might the learned behavioral diversity translate to improved performance in downstream tasks, for example, few-shot adaptation?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper tries to address a limitation in offline RL, where existing methods often focus on optimizing performance at the expense of promoting diverse behaviors. Traditional approaches that rely on well-constructed, heterogeneous datasets struggle with less diverse data. To overcome this, the authors propose a new intrinsic reward mechanism that encourages behavioral diversity regardless of the dataset's heterogeneity. This is achieved by maximizing the mutual information between actions and policies for each state, allowing agents to learn a variety of behaviors, even those not explicitly present in the data. To manage the risks associated with out-of-distribution actions, the authors incorporate the ensemble-diversified actor-critic (EDAC) method to estimate Q-value uncertainty, preventing suboptimal behavior adoption. Experiments using the D4RL benchmarks on MuJoCo tasks show that the proposed method successfully achieves behavioral diversity while maintaining performance across environments with both heterogeneous and homogeneous datasets.

### Strengths
1. The paper introduces a novel intrinsic reward mechanism that encourages behavioral diversity, a significant advancement over existing methods that often overlook this aspect.
2. Although there is some confusion regarding the details of the method, the writing logic used to introduce the approach and model is very clear and easy to follow.

### Weaknesses
There is some confusion about the method for me to understand the paper. Please refer to Questions.

Q1.  How are the heterogeneity and homogeneity of the dataset defined in the context of this study?

Q2. If I understand correctly, In Line205-208, $p^t(s_t|pi)$ is $p(s_t|s_{t-1},a_{t-1})$ and is nothing to do with $\pi$ (since you have specified \tau in $p(\tau|\pi)$, it can decompose to transition probability $p(s_t| s_{t-1}, a_{t-1})$ and $p(a_t|s_t, \pi)$ for t=0,1,...). Based on this, I think there may be some mistakes in the following analysis.

Q3. In practice, how to estimate $p(a_t|s_t)$ in Equation 8?

Q4. Can the experimental results be generalized to tasks with discrete action spaces, such as Atari, representing more complex environments? It would be advantageous if the methods could be validated more broadly.

Q5. The authors employ ensemble training in the experiments. Could we consider incorporating information between the policies to achieve final diversity, as done in [1]?

### Questions
Overall, I have some questions:

Q1.  How are the heterogeneity and homogeneity of the dataset defined in the context of this study?

Q2. If I understand correctly, In Line205-208, $p^t(s_t|pi)$ is $p(s_t|s_{t-1},a_{t-1})$ and is nothing to do with $\pi$ (since you have specified \tau in $p(\tau|\pi)$, it can decompose to transition probability $p(s_t| s_{t-1}, a_{t-1})$ and $p(a_t|s_t, \pi)$ for t=0,1,...). Based on this, I think there may be some mistakes in the following analysis.

Q3. In practice, how to estimate $p(a_t|s_t)$ in Equation 8?


Q4. Can the experimental results be generalized to tasks with discrete action spaces, such as Atari, representing more complex environments? It would be advantageous if the methods could be validated more broadly.

Q5. The authors employ ensemble training in the experiments. Could we consider incorporating information between the policies to achieve final diversity, as done in [1]? 

[1] Wu S et al. Quality-similar diversity via population based reinforcement learning[C]//The Eleventh International Conference on Learning Representations. 2023.

### Soundness
2

### Presentation
3

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
The paper introduces a novel approach to enhance behavioral diversity in offline reinforcement learning without compromising performance, leveraging mutual information to encourage diverse strategies among agents. It employs an Ensemble-Diversified Actor-Critic method to mitigate the risks associated with out-of-distribution actions, ensuring quality alongside diversity. The innovation lies in its intrinsic reward mechanism that maximizes mutual information between actions and policies, promoting a variety of behaviors even in homogeneous datasets.

### Strengths
see questions

### Weaknesses
This paper proposes a new intrinsic reward system that maximizes the mutual information between actions and policies, encouraging behavioral diversity. Through the combination of EDAC method to estimate Q-value uncertainty, the proposed method achieves better performance than other baselines. However, the main concern is that the idea of introducing mutual information in offline RL is also proposed by one previous work [1]. Eq. 5 and 6 of [1] are similar to the objective function in this paper. The authors should claim the difference and novelty compared to [1] and consider involving it as a baseline in experiments.

### Questions
This paper proposes a new intrinsic reward system that maximizes the mutual information between actions and policies, encouraging behavioral diversity. Through the combination of EDAC method to estimate Q-value uncertainty, the proposed method achieves better performance than other baselines. However, the main concern is that the idea of introducing mutual information in offline RL is also proposed by one previous work [1]. Eq. 5 and 6 of [1] are similar to the objective function in this paper. The authors should claim the difference and novelty compared to [1] and consider involving it as a baseline in experiments.

[1] Ma, Xiao, et al. "Mutual Information Regularized Offline Reinforcement Learning." arXiv preprint arXiv:2210.07484 (2022). (accepted by neurips 2024)

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper introduces a novel approach to offline reinforcement learning that enhances behavioral diversity while maintaining performance. Unlike traditional methods that depend on diverse datasets, it maximizes mutual information between actions and policies, enabling agents to learn varied behaviors even from homogeneous data. The approach incorporates an intrinsic reward mechanism and the Ensemble-Diversified Actor-Critic framework to handle out-of-distribution risks. Experimental results on D4RL benchmarks show superior performance and diversity compared to existing methods, making it a promising solution for more robust offline RL applications.

### Strengths
1. Introducing a novel method to enhance behavioral diversity in offline reinforcement learning, addressing limitations of traditional approaches that rely on dataset heterogeneity.
2. Leveraging mutual information, the method enables agents to learn a range of behaviors beyond those present in the dataset.
3. Integrating the EDAC framework helps manage out-of-distribution risks, ensuring that the diversity achieved does not come at the cost of performance.

### Weaknesses
1. The paper lacks clear explanations of some key concepts, leading to ambiguity in how the proposed approach connects to its claims, such as the relevance of the title and certain methodological terms. The phrase 'out of the box' remains vague, failing to specify what 'box' is being referenced, especially in the context of offline RL constraints. The connection between this phrase and the method's ability to learn beyond the dataset is not clearly established.
2. There are insufficient details about the implementation and underlying mechanisms of the method. This makes it challenging for readers to fully understand or replicate the approach. For instance, the method's use of an ensemble of Q-functions (EDAC) is not clearly explained, particularly how it differs from other conservative methods in offline RL. The specific mechanism by which the minimum Q-function is selected for policy updates is also unclear.
3. The comparisons with existing methods are limited, particularly in demonstrating the proposed method's advantages over other high-performance algorithms. Broader benchmarks and more comprehensive comparisons would strengthen the claims. The paper does not adequately explain why the method achieves better diversity and performance than DIVEOFF, given that both methods use mutual information. The distinction in how mutual information is applied is not sufficiently detailed.
4. Some theoretical aspects are not well-justified, leading to questions about the validity and robustness of the approach. Clearer explanations and references to prior work are needed. The paper does not provide a rigorous theoretical derivation for the unique behavior (UB) reward, nor does it sufficiently explain why rewarding policies for behaving differently leads to exploration beyond the dataset. The claim that distant latent vectors can be decoded into similar actions lacks a detailed explanation of the underlying mechanism and its implications for diversity.

### Questions
1. The phrase 'out of the box' in the title is not clearly connected to specific concepts or points within the paper. The authors should clarify what 'box' refers to in the context of their method. 
2. Regarding the abstract, after reviewing the full paper, I found that the comparison between heterogeneous and less diverse datasets is not explicitly addressed in the methodology or experiments. The claimed effectiveness of the approach across different data types has not been adequately substantiated. Could the authors specify which datasets are considered heterogeneous and which are less diverse, and clarify this distinction in the methodology or experiment sections?
3. How important is diversity for reinforcement learning, particularly in offline RL? What are the main benefits of promoting diversity in this context? The authors should elaborate more on the significance and implications of this aspect in their research.
4. What distinguishes the current mutual information-based approach from other methods, including the baseline approaches like DIVEOFF, CLUE, and SORL? The authors mention that DIVEOFF also maximizes mutual information, so why does their method achieve better diversity while balancing performance? What is the underlying reason for this difference?
5. Regarding Figure 1, the comparison between the proposed method and SORL does not show a significant difference. In my view, their diversity levels appear quite similar. Could the authors provide another example where the distinction between the methods is more pronounced?
6. Why does the approach adopt an ensemble method (EDAC) to avoid over-estimation? How does this compare to other techniques like conservative Q-learning or conservative policy gradient methods? What are the advantages of using EDAC over these alternatives?
7. The paper states, "However, a challenge arises when the dataset is homogeneous, or when distant latent vectors are decoded into similar actions." What exactly does it mean for distant vectors to be decoded into similar actions? Could the authors provide a more detailed explanation of this concept?
8. The paper states, "Agents are rewarded for behaving differently from each other during training, providing direct guidance that allows policies to learn behaviors even beyond the dataset distribution." Why does the proposed method enable learning behaviors beyond the dataset distribution? How does this approach differ from importance sampling-based methods, and why did the authors choose not to use importance sampling?
9. The estimation formula $p\left(a_t \mid s_t\right)=\sum_{i=1}^M p\left(a_t \mid s_t, \pi^i\right) p\left(\pi^i\right)$ on page 5 is intriguing, but can it truly provide an accurate estimate of $p\left(a_t \mid s_t\right)$? Are there any potential issues with bias or high variance in this approach? The same concern applies to the formula $p^t\left(s_t\right)=\sum_{i=1}^M p^t\left(s_t \mid \pi^i\right) p\left(\pi^i\right)$. Could the authors explain the rationale behind using these estimations? If this method is derived from existing research, it would be helpful to cite those sources and provide further clarification.
10. In Inequation (8), is the second term of $U_{\text{Path}}^{\pi_{\theta}^i}(\tau) = \sum_{t=0}^{T} \log \left( \frac{p(a_t \mid s_t, \pi^i)}{p(a_t \mid s_t)} \right) + \sum_{t=0}^{T} \log \left( \frac{p^t(s_t \mid \pi^i)}{p^t(s_t)} \right)$ always positive? It is not clear to me why this inequation holds. Could the authors provide further explanation?
11. To which part of the paper does Figure 2 correspond? The authors did not clearly indicate this connection.
12. In Algorithm 1, how is the policy update in line 8 implemented? Did you use the policy gradient theorem? The authors should provide more details on how the policies are updated.
13. The notation $\phi(\pi_i) = E_{s \sim \pi_i, P}[s]$ is used to evaluate state diversity, while $\phi(\pi_i) = E_{s \sim \pi_i, P}[a]$ is used to assess action diversity. However, it appears that the same notation $\phi(\pi_i)$ is being used for two different values. Could the authors clarify this?
14. In Table 4, the performance of the EDAC method appears to be better than that of the proposed approach. Under what conditions should we choose the proposed method for its diversity benefits, despite the lower performance compared to EDAC? Is there a standard metric or conventional score to evaluate this trade-off between diversity and performance?
15. I noticed that the proposed method appears to outperform DIVEOFF, SORL, and CLUE in both performance and diversity. Could the authors also evaluate the diversity of other high-performance algorithms, such as EDAC, CQL, and IQL? Furthermore, are the observed differences in actions genuinely due to enhanced diversity, or could they be attributed to insufficient training of the policies (e.g., SORL), which may have been limited to a single, suboptimal policy?
16. Is this method applicable only to offline learning? If not, please consider discussing its potential for online scenarios in the future work section.

### Soundness
2

### Presentation
3

### Contribution
2
