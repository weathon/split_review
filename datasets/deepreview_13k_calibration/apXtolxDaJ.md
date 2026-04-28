# Adaptive Regularization of Representation Rank as an Implicit Constraint of Bellman Equation

- Decision: Accept
- Avg Score: 6.00
- Scores: 6, 6, 6, 6

## Abstract
Representation rank is an important concept for understanding the role of Neural Networks (NNs) in Deep Reinforcement learning (DRL), which measures the expressive capacity of value networks. Existing studies focus on unboundedly maximizing this rank; nevertheless, that approach would introduce overly complex models in the learning, thus undermining performance. Hence, fine-tuning representation rank presents a challenging and crucial optimization problem. To address this issue, we find a guiding principle for adaptive control of the representation rank. We employ the Bellman equation as a theoretical foundation and derive an upper bound on the cosine similarity of consecutive state-action pairs representations of value networks. We then leverage this upper bound to propose a novel regularizer, namely \underline{BE}llman \underline{E}quation-based automatic rank \underline{R}egularizer (BEER). This regularizer adaptively regularizes the representation rank, thus improving the DRL agent's performance. We first validate the effectiveness of automatic control of rank on illustrative experiments. Then, we scale up BEER to complex continuous control tasks by combining it with the deterministic policy gradient method. Among 12 challenging DeepMind control tasks, BEER outperforms the baselines by a large margin. Besides, BEER demonstrates significant advantages in Q-value approximation.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper proposes a novel method to control the representation rank of neural networks in deep reinforcement learning (DRL), which measures the expressive capacity of value networks. They argue that existing methods either ignore or unboundedly maximize the representation rank, which can lead to overfitting or underfitting problems.

### Strengths
The proposed method is well-founded. The authors establish an upper bound on the cosine similarity between the representations of consecutive state-action pairs, using the Bellman equation1. They demonstrate that this bound indirectly restricts the rank of the representation and offers a criterion for adaptive control.

### Weaknesses
It is recommended to thoroughly investigate the computational overhead of the proposed method.

### Questions
See Weaknesses.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This work studies how to learn a low-rank representation in reinforcement learning (RL). Following several previous works, the authors claimed that RL favors a representation with moderate rank, and they proposed a new regularization method based derived from the Bellman equation. In detail, such a regularization method controls the complexity of the learned representation, and it encourages the rank of the representation to be small empirically. Combined with the regularization method, several baseline methods such as DQN and DDPG outperform existing baselines.

### Strengths
1. The presentation of this paper is clear. 
2. The experiment setup is described very clear. 
3. The literature review is complete.

### Weaknesses
There are several things that can improve the paper. For instance, 
1. On page 4, the definition of $\bar{\phi}(s',a')$ seems not clear since $(s',a')$ serves as both the input of $\bar{\phi}$ and the random variable which is going to be integrated. 
2. On page 5, what is the exact definition of $\mathbb{SG}$? 

I do not quite get why the authors need to design the regularization term as in (12). It seems more natural to me to set the regularization term as in (19), which avoids a calculation of the gradient of an inverse term $1/|\phi(s,a)|$ which might hurt the stability of the optimization process. 

The logic behind the superior performance of BEER is not clear to me. The authors tried to claim that 'representation rank affects the model performance (approximation error), while BEER explicitly controls the rank, thus BEER outperforms other baseline methods'. However, according to figure 2, InFeR has a similar representation rank as BEER, while it performs worse than BEER. Is there any explanation why such a phenomenon happens? Meanwhile, in simpler tasks (Grid World), the rank of BEER is higher than other baselines, while in complex tasks (Lunan radar), the rank of BEER is lower than other baselines. Due to the inconsistency, it is doubtful whether the performance gain is due to the better control of representation rank. If so, it indeed deserves more explanation.

### Questions
See Weaknesses.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper studies an implicit regularization of representation rank in deep RL. The authors draw the intuition between the representation rank and the cosine similarity between adjustment state-action pairs.

### Strengths
- This paper is well written and easy to follow
- The experiment shows a good performance and backup the theoretical insights

### Weaknesses
 - The argument that the cosine similarity of the ** adjustment** state-action pairs $(s, a)$ and $(s', a')$ does not rigorously lead to the rank. This is because one can only control the similarity between limited state-action pairs, instead of all possible state-action pairs. Think of an extreme case that the representation in adjustment state-action pairs is iterating between $(0, 1, 0, \cdots, 0)$ and $(1, 0, 0, \cdots, 0)$, the implicit regularization will fail.
- It seems that in the experiment (Figure 1), the representation rank of the proposed method is dropping. It would be beneficial if the authors can provide some explanation on this


### Questions
- Maximizing the representation rank has always been an important part of the literature. Several theoretical works [1, 2, 3] show that as long as all the representations are in the span of the covariance matrix (i.e. $x \in E[xx^\top], the diversity assumption in [1] or the UniSOFT assumption in [2]), the performance can be improved. It would be beneficial for authors to comment on the relationship between this paper and these theoretical results, e.g. will the cosine similarity be well-bounded under these assumptions?

[1] Papini, Matteo, et al. "Leveraging good representations in linear contextual bandits." International Conference on Machine Learning. PMLR, 2021.
[2] Papini, Matteo, et al. "Reinforcement learning in linear mdps: Constant regret and representation selection." Advances in Neural Information Processing Systems 34 (2021): 16371-16383.
[3] Zhang, Weitong, et al. "Provably efficient representation selection in low-rank Markov decision processes: from online to offline RL." Uncertainty in Artificial Intelligence. PMLR, 2023.

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper studies an important issue of representation rank in deep reinforcement learning (DRL).  To tackle this problem, the authors propose BEER, which leverages the Bellman equation to derive an upper bound on the cosine similarity between consecutive state-action pair representations. This bound is then used as a regularizer to adaptively control the representation rank during training. The empirical studies on DeepMind control tasks validate the high efficiency of the proposed algorithm.

### Strengths
The paper is well written and easy to follow. The proposed adaptive regularization is new and effective.

The empirical results clearly validate the high efficiency of BEER, which is impressive. Since I am not an expert in this specific area and haven't followed this line of recent literature, I will refer to others reviewers' opinions on the experiments.

### Weaknesses
I have some minor questions:

1. The authors intuitively explained the intrinsic similarity between the cosine similarity and the representation rank with examples. I am curious about if there is some formal statement or proof on this topic, since it serves as a very important property of your paper. There is some parameter in the definition of the representation rank (e.g. $\epsilon$) in Definition 1, but I didn't see it in the following discussion.

2. When the authors transform the constraint in Eqn. (11) to the penalty regularizer with ReLU in Eqn.(12), is there any theoretical support for this transformation? And also is there any theoretical analysis on how to choose the value of $\beta$? I check the ablation study on this hyperparameter on Appendix, but I feel its choice is still quite important but unclear in practice.

For the Eqn. (5), should the $\phi$ be $\Phi$?

### Questions
Please refer to the above Weaknesses section.

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair
