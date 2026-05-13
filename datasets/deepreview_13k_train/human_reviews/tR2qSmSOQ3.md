# Improving Offline-to-Online Reinforcement Learning with Q Conditioned State Entropy Exploration

- Decision: Reject
- Scores: 6, 5, 3, 3

## Abstract
Studying how to fine-tune offline reinforcement learning (RL) pre-trained policy is profoundly significant for enhancing the sample efficiency of RL algorithms. However, directly fine-tuning pre-trained policies often results in sub-optimal performance. This is primarily due to the distribution shift between offline pre-training and online fine-tuning stages. Specifically, the distribution shift limits the acquisition of effective online samples, ultimately impacting the online fine-tuning performance. In order to narrow down the distribution shift between offline and online stages, we proposed Q conditioned state entropy (QCSE) as intrinsic reward. Specifically, QCSE maximizes the state entropy of all samples individually, considering their respective Q values. This approach encourages exploration of low-frequency samples while penalizing high-frequency ones, and implicitly achieves State Marginal Matching (SMM), thereby ensuring optimal performance, solving the asymptotic sub-optimality of constraint-based approaches. Additionally, QCSE can seamlessly integrate into various RL algorithms, enhancing online fine-tuning performance. To validate our claim, we conduct extensive experiments, and observe significant improvements with QCSE ( about \textbf{13}\% for CQL and \textbf{8}\% for Cal-QL). Furthermore, we extended experimental tests to other algorithms, affirming the generality of QCSE.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper proposes a new reinforcement learning method called Q-conditioned State Entropy Maximization (QCSE) which aims to improve the performance of offline-to-online RL process. The authors prove that QCSE can achieve State Marginal Matching (SMM), an exploration strategy theoretically ensuring optimal performance. Experiments show that QCSE significantly enhances the performance of existing model-free algorithms like CQL and Cal-QL, with an average improvement of about 13% and 8%. Additionally, QCSE exhibits general applicability to other model-free algorithms such as SAC, IQL, and TD3+BC.

### Strengths
This paper presents a novel approach to offline-to-online reinforcement learning, demonstrating strong originality and significance. The authors provide clear and thorough explanations of their proposed method, making the paper highly readable and understandable.

### Weaknesses
On the novelty factor, contributions are not very significant.

The paper would benefit from a more thorough analysis and discussion of the limitations and potential challenges associated with the proposed framework.

The experimental evaluation should include comparisons with a broader range of state-of-the-art methods to offer a more comprehensive assessment of QCSE's performance.

The theoretical analysis is insufficient and needs strengthening.

### Questions
Could you please provide more clarity on how the hyper-parameter settings, particularly the choice of  λ and the number of k-nearest neighbor (knn) clusters, affect the results? I would appreciate a more detailed explanation of their impact on the performance of QCSE, as the current description is a bit unclear to me.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper explores strategies for optimizing the fine-tuning of pre-trained policies in offline reinforcement learning (RL) to enhance sample efficiency. Traditional fine-tuning methods often fall short due to a distribution mismatch between offline pre-training and subsequent online fine-tuning, which restricts the quality of online sample acquisition and hampers performance. To mitigate this distribution shift, the authors introduce Q-conditioned state entropy (QCSE) as an intrinsic reward mechanism. QCSE maximizes the entropy of individual states based on their respective Q-values, promoting exploration of underrepresented samples while disincentivizing overrepresented ones. This approach implicitly aligns with State Marginal Matching (SMM), resolving the asymptotic limitations often seen in constraint-based techniques. Moreover, QCSE integrates seamlessly with various RL algorithms, leading to significant improvements in online fine-tuning. Experimental results show approximately 13% performance gains for CQL and 8% for Cal-QL, with additional tests confirming QCSE’s versatility across different algorithms.

### Strengths
1. The idea proposed in this paper has a degree of novelty, as it connects the offline-to-online learning problem with exploration mechanisms, leading to a new algorithm. This represents a relatively fresh perspective.

2. The experiments in this paper are quite comprehensive, evaluating the algorithm's effectiveness, modularity, and advancement from multiple perspectives. Additionally, the experiments cover a wide range of tasks, providing robust empirical support for the proposed method.

### Weaknesses
My main concerns about this paper lie in the method description section, where I feel that several key points are not fully explained by the authors.

1. Regarding the interpretation of Equation (1), if the goal is to maximize the right-hand side $J_2$, since the optimal policy’s corresponding $p^*$ is fixed, it’s clear that the scope of $S_2$ should be expanded, rather than "narrowing down the domain $S_2$" as the authors suggest. Meanwhile, to maximize $J_1$, it’s evident that the range of $S_1$ should be reduced, i.e., $p(s)$ over $S_1$ should be decreased to approach $p^*(s)$. Therefore, the overall approach seems to be "increasing exploration in $S_2$ while penalizing exploration in $S_1$." However, this is contrary to the authors’ description in lines 203–209. Could you clarify your reasoning behind the claim of "narrowing down the domain $S_2$" and explain how this aligns with maximizing $J_2$. Additionally, you could  revisit the description in lines 203-209 to ensure consistency with the mathematical formulation.

2. In the "Implementation of QCSE" section, I did not see how the practical algorithm for QCSE was derived from Equation (1). Specifically, what do the $S_1$ and $S_2$ in Equation (1) correspond to here? What role does maximizing the Critic Conditioned State Entropy $H(s|Q)$ in Equation (2) play, and how is it related to Equation (1)? Particularly, if there are indeed issues with the interpretation of Equation (1) mentioned above, does that mean Equation (2) would not hold either? The authors are suggested to provide a step-by-step derivation showing how the practical algorithm in Equation (2) follows from the theoretical formulation in Equation (1). Specifically, could you clarify on how $S_1$ and $S_2$ from Equation (1) are represented in the implementation, and how maximizing $H(s|Q)$ relates to the objectives in Equation (1)?

3. The origin of Equation (3) is also unclear. The authors simply refer to the literature, but they do not explain how (3) is derived from (2), which is not obvious. Therefore, the authors have an obligation to provide the derivation process from (2) to (3).

### Questions
The same as Weaknesses.

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
The paper proposes a new method that estimates Q-conditioned state entropy, to improve offline-to-online RL. Typically, if we train offline agent online, it results in sub-optimal online performance due to limited exploration of effective samples. QCSE introduces an intrinsic reward based on the entropy of states conditioned on Q-values, achieving State Marginal Matching. This approach outperforms previous offline-to-online methods.

### Strengths
- Strong empirical performance.

### Weaknesses
 - There are a number of notations and theoretical arguments that I was not able to fully understand (or wrong):
  - In equation (1), it is said that the state entropy maximization is: 
 $ \max E_{ \mathbf{s} \sim \rho_\pi } \left[ \mathcal{H}_\pi [ \mathbf{s} ] \right] $ 
s.t. 
 $ \pi := \arg \max _ \pi E _ { \tau \sim \pi } [ R( \tau ) ] $ . If $\pi$ is maxmimizing reward as written in constraints, what are we maxmizing in the objective? It seems like the objective is trying to maximize the state entropy, while the constraint is trying to maximize the return. These two objectives are not aligned, and it is unclear how they are optimized simultaneously. The constraint implies that we are choosing a policy that maximizes return, and then among those policies, we are maximizing the state entropy, which is not the typical maximum entropy RL setting.
  - On line 194, it is written: $\max E _ {\mathbf{s} \sim \rho_\pi}[-\log p(\mathbf{s})]$; is $p(x)$ $\rho_\pi(s)$? It is not clear if $p(s)$ refers to the probability density function of the state marginal distribution induced by the policy $\pi$, which is typically denoted as $\rho_\pi(s)$. The notation is ambiguous and should be clarified.
  - The proof of equation (1) seems to be wrong. in equation (4), it is argued that $\rho_\pi \le p^*$ in $\mathcal{S}_2$, but in that case, the inequality should be in the opposite direction. The argument that the state marginal distribution is less than the target distribution in a specific region seems incorrect, and the inequality should be reversed if the goal is to minimize the KL divergence.
  - From the first place, how $ \max E_{ \mathbf{s} \sim \rho_\pi } \left[ \mathcal{H}_\pi [ \mathbf{s} ] \right] $ can be equivalent to KL minimization between $ \rho _ \pi $ and $ p ^ * $? the former converges to maxent distribution (uniform-like), whereas the latter converges to $ p ^ * $. Maximizing state entropy leads to a uniform distribution over states, while minimizing the KL divergence between the state marginal and a target distribution leads to matching that target distribution. These are fundamentally different objectives, and the paper does not adequately explain how they are equivalent.

- While the paper defines critic conditioned state entropy and use it as its key concept, it is very hard to understand intuitively what it is, and the paper does not explain it well. 
  - according to the definition, it seems like, critic conditioned state entropy averages $-\log p(s|Q(s, \pi(\cdot|s)))$ over $\rho _ \pi$. What is $p(s|Q(s, \pi(\cdot|s)))$ indeed? How can a given term depend on the conditioned term? It is unclear what this conditional probability represents. If $Q(s, \pi(\cdot|s))$ is a value, how can we have a probability distribution conditioned on a value? The notation is confusing and lacks a clear explanation.


### Questions
- I was not able to understand the math presented in the paper, as discussed in the weaknesses section. Then, why do we need to consider the so-called critic conditioned state entropy? I agree with the idea that we need exploration for offline-online fine-tuning, and state marginal matching can be one of exploration methods. But for that, we can simply put reward for entropy maximization; how QCSE and VCSE differ from it?
- In the experiments, QCSE adopted algorithms does improve from the baselines, but their performance is still highly correlated to the baselines' performance (e.g., walker2d -medium-replay). Why is there a gap between the theory and the experiment results? Following the papers' arguments, the proposed algorithm does state marginal matching, and shouldn't it lead to an optimal policies?

### Soundness
1

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The paper introduces Q-Conditioned State Entropy Exploration (QCSE), an innovative offline-to-online reinforcement learning (RL) framework aimed at enhancing online fine-tuning of policies trained on offline data. The paper introduces Q-Conditioned State Entropy Exploration (QCSE), an innovative offline-to-online reinforcement learning (RL) framework aimed at enhancing online fine-tuning of policies trained on offline data. The paper introduces Q-Conditioned State Entropy Exploration (QCSE), an innovative offline-to-online reinforcement learning (RL) framework aimed at enhancing online fine-tuning of policies trained on offline data. The paper validates QCSE on several benchmarks, including CQL and Cal-QL algorithms, and demonstrates its effectiveness across various offline-to-online tasks. QCSE shows performance improvements, especially in environments with larger distribution shifts, and offers compatibility with multiple RL algorithms, making it versatile for real-world application

### Strengths
*  By promoting exploration based on Q-conditioned state entropy, the method encourages the agent to explore states that are low-frequency yet potentially valuable. This approach goes beyond traditional exploration strategies, providing a fresh perspective on tackling distribution mismatch.
* The framework’s compatibility with various offline RL algorithms, including CQL and Cal-QL, showcases its versatility. QCSE’s intrinsic reward structure can be integrated into different RL algorithms, making it adaptable for a range of applications beyond the specific benchmarks tested, such as robotics or recommendation systems where offline-to-online RL is critical.

### Weaknesses
 * It seems the online fine-tuning is not efficient enough as several baselines could achieve better performance within 250000 online fine-tuning steps such as BR and ENOTO. And these baselines are missing.
* QCSE’s reliance on entropy maximization and Q-conditioning likely introduces sensitivity to hyperparameter choices, such as size of k-nearest neighbor. The method's performance could be highly dependent on the choice of k, and the paper does not provide sufficient analysis on how to select this parameter effectively. The range of values tested for k-nearest neighbor is also quite limited, and it is unclear if the reported results are robust to a wider range of values. Furthermore, the interaction between the k-nearest neighbor parameter and the underlying offline RL algorithm's hyperparameters is not explored, which could lead to suboptimal performance if not tuned carefully.

### Questions
* A key baseline named ENOTO [1] is missing. In ENOTO, the authors also incorporate exploration techniques into their methods, which should be discussed and compared. Besides, ENOTO could also be combined with different offline RL algorithms. It seems from the curves in Fig.5 and Fig.6 in ENOTO's paper and the Fig.3 of the submitted paper that the proposed method QCSE  is inferior to ENOTO. So what's the advantage of QCSE compared with ENOTO?
*I'm curious whether performance drop could happen when QCSE is applied on medium-expert and expert datasets? These two kinds of datasets are quite nightmare for most offline-to-online RL algorithms. Could QCSE handle them well?


[1] ENOTO: Improving Offline-to-Online Reinforcement Learning with Q-Ensembles. IJCAI 2024.

### Soundness
2

### Presentation
3

### Contribution
2
