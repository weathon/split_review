# ARC-RL: Self-Evolution Continual Reinforcement Learning via Action Representation Space

- Decision: Reject
- Scores: 3, 3, 6, 3

## Abstract
Continual Reinforcement Learning (CRL) is a powerful tool that enables agents to learn a sequence of tasks, accumulating knowledge learned in the past and using it for problemsolving or future task learning. However, existing CRL methods all assume that the agent’s capabilities remain static within dynamic environments, which doesn’t reflect realworld scenarios where capabilities evolve. This paper introduces *Self-Evolution Continual Reinforcement Learning* (SE-CRL), a new and realistic problem where the agent’s action space continually changes. It presents a significant challenge for RL agents: How can policy generalization across different action spaces be achieved? Inspired by the cortical functions that lead to consistent human behavior, we propose an **A**ction **R**epresentation **C**ontinual **R**einforcement **L**earning framework (ARC-RL) to address this challenge. Our framework builds a representation space for actions by self-supervised learning on transitions, decoupling the agent’s policy from the specific action space. For a new action space, the decoder of the action representation is expanded or masked for adaptation and regularized fine-tuned to improve the stability of the policy. Furthermore, we release a benchmark based on MiniGrid to validate the effectiveness of methods for SE-CRL. Experimental results demonstrate that our framework significantly outperforms popular CRL methods by generalizing the policy across different action spaces.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The paper proposes Action Representation Continual Reinforcement Learning (ARC-RL), a method for adapting the agent when its action space is changing from one task to another. The idea is to train (fine-tune) an encoder and a decoder pair at the beginning of the task using a self-supervised learning objective in order to learn the action representation space. Then, the decoder maps this space into the action set that is currently available to the agent. The authors perform experiments on the empty grid environment in the MiniGrid framework and the bigfish environment in the Procgen environment to demonstrate the usefulness of the proposed approach.

### Strengths
* The problem that the paper considers is very important in continual reinforcement learning, especially in cases when skills are built and added to the agent’s base action set in a continual manner (although this is not explored in the paper).
* Albeit not novel, the idea of learning action representation space using self-supervised learning objectives is a very simple idea and yields many useful benefits for training deep neural networks.
* The regularized fine-tuning trick, which combines the ideas from elastic weight consolidation and the self-supervised learning objective is new. It is also useful in continual RL to retain past learnings in order to adapt faster when the past is reencountered.

### Weaknesses
 * The first major weakness of the paper is in the claims it is making, especially in the novelty contribution:
    * The proposed approach for learning the action representation using the self-supervised learning objective is not new. There are many works in this literature including the one that the paper cites that learns the action representation space [1]. The application of this technique to continual reinforcement learning is not novel either. [2], which is by the same author as [1], proposes a very close approach to the one introduced in this paper. The algorithm is well-studied theoretically in their case. I encourage the authors to check [2] and the papers that cite it in order to better place the proposed approach within the existing literature. It is also crucial to use the method introduced in [2] as a baseline to better understand the benefits of the proposed approach. The paper fails to adequately distinguish its approach from these existing methods, particularly in terms of the specific self-supervised learning objective used and how it interacts with the continual learning setting. The novelty of the specific combination of self-supervised learning and elastic weight consolidation (EWC) is not sufficiently highlighted, leading to a perception of incremental contribution.
    * The problem of changing action spaces in continual reinforcement learning is not new either as the paper claims to be. [2] and [3] have discussed this as a subproblem within RL and the proposed SE-CRL’s description perfectly fits well with those. The paper does not adequately position its contribution within this existing body of work, failing to clearly articulate the specific nuances of the problem it addresses and how it differs from prior formulations.

* The experiments are performed on very basic environments and the conclusions drawn from them do not match the plots presented in Fig 4 and Fig 5:
   * In Fig 4, for ARC-RL, the agent reaches optimal performance on tasks 2 and 3 when it is trained on task 1. No further boost in performance is observed when new actions are added to the action set. This raises the question of whether the agent is making use of new available actions in order to improve its policy. The lack of performance improvement with additional actions suggests that the learned action representation might not be effectively leveraging the expanded action space, which is a critical flaw in the proposed approach. The experiments do not provide sufficient evidence that the method can effectively adapt to new actions.
    * In Fig 5, on task 2, the performance of ARC-RL decreases when the agent is trained on it, perhaps because the action space is reduced from seven to five. But the performance doesn’t drop when the agent’s action space is further reduced to three; it stays the same. This is a very strange behaviour. The inconsistent performance behavior with reduced action spaces raises serious concerns about the robustness and reliability of the proposed method. The lack of a clear explanation for this behavior undermines the validity of the experimental results.
    * The environments used are too simple and are not well-designed to support the method. Besides, in Sec 2.2, four categories are introduced when the action space changes, but only two of them are used to demonstrate the applicability of the proposed approach experimentally. The experimental setup lacks the complexity needed to demonstrate the effectiveness of the proposed method in realistic scenarios. The limited scope of the experiments raises concerns about the generalizability of the findings.
    * There is no description of the baselines used or how the hyperparameters in them are tuned. Besides, some of the baselines don’t offer much value in terms of understanding the results of ARC-RL. I suggest the authors include: (a) a baseline that uses all the actions; and (b) the method proposed in [2]. The lack of detailed information about the baselines and their hyperparameter tuning makes it difficult to assess the validity of the experimental results. The absence of a strong baseline like the method in [2] further weakens the empirical evaluation.

### Questions
**Decision:**

The paper is not discussed well within the existing literature. The experiments are simple and the conclusions from them don’t match the performance curves. Therefore, I recommend a clear rejection.

**Areas of improvement:**

* In the introduction, the paper says “[...] assumes that the agent’s capabilities remain static [...]”. This is incorrect! It is the opposite case. In CRL, the desiderata of the agent is to have continuous adaptation as discussed in some foundation papers in CRL, e.g., [4] and [5].
* The paper should provide a summary of the task description in the main paper. It is unclear how the actions are changing from one task to another.

**Questions:**

* How does the zero-shot generalization metric (forward transfer) relate to the jump-start objective that is commonly used in CRL papers (e.g., [4] and [6])?
* What does the double union symbol denote in Sec 3.2 (just before Eq. 4)?
* In the caption of Fig 2, the paper says “After the action space changes, the number of actions changes, while the probability distribution is relatively stable.” What does this sentence mean?

**References:**

[1] Chandak, Yash, et al. "Learning action representations for reinforcement learning." International conference on machine learning. PMLR, 2019.

[2] Chandak, Yash, et al. "Lifelong learning with a changing action set." Proceedings of the AAAI Conference on Artificial Intelligence. Vol. 34. No. 04. 2020.

[3] Khetarpal, Khimya, et al. "Towards continual reinforcement learning: A review and perspectives." Journal of Artificial Intelligence Research 75 (2022): 1401-1476.

[4] Anand, Nishanth, and Doina Precup. "Prediction and control in continual reinforcement learning." Advances in Neural Information Processing Systems 36 (2024).

[5] Abel, David, et al. "A definition of continual reinforcement learning." Advances in Neural Information Processing Systems 36 (2024).

[6] Taylor, Matthew E., and Peter Stone. "Transfer learning for reinforcement learning domains: A survey." Journal of Machine Learning Research 10.7 (2009).

### Soundness
2

### Presentation
3

### Contribution
1

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The authors introduces a novel framework for continual reinforcement learning (CRL) where the agent's action space evolves over time. The authors propose ARC-RL, which leverages self-supervised learning to build an action representation space, allowing the agent's policy to adapt to changes in the action space without catastrophic forgetting. The paper claims to make significant contributions to the field of CRL by addressing the challenge of policy generalization across different action spaces.

### Strengths
- The setting of continual learning in tasks with varying action spaces is interesting and valuable for research.
- The writing is very clear, making it easy for readers to understand main context.

### Weaknesses
 - The experimental validation is limited, with only a few scenarios tested. The authors only evaluated contraction and expansion in Minigrid and contraction in the Procgen Fish environment. It would be beneficial to construct 4-5 discrete action space scenarios, including other environments in Minigrid and Procgen benchmarks, as well as 2-3 continuous action space scenarios, such as Ant with varying leg counts (4, 6, or 8 legs).
- The proposed regularization method shows minimal impact, as evidenced by Table 1. Specifically, the regularization term seems to have little effect on the forgetting and forward transfer metrics, which are crucial for evaluating continual learning methods. The lack of a clear benefit from the regularization raises questions about its necessity and effectiveness.
- While I appreciate the simplicity of the overall method, it  does not demonstrate significant performance improvements over the baseline. The reported improvements are marginal, especially in simpler environments, suggesting that the method's ability to generalize across different action spaces may be limited.
-  Lack of discussion on related work in continual learning and continual reinforcement learning.

### Questions
In Section 2.2, the paper states that the only difference between tasks is the action space. However, the transition function is defined as 
$\mathcal{S} \times \mathcal {A} \rightarrow \Delta(\mathcal{S})$, and thus, when the action space changes, the transition function also changes.  It seems that the oversight of the potential changes in the transition function between tasks has led to the limited improvements of the current method.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The authors have introduced a new problem in reinforcement learning called Self-Evolution Continual Reinforcement Learning (SE-CRL), which focuses on the change only in action space. They have formally defined this problem and proposed a novel approach, ARC-RL, to address it. Furthermore, the authors have developed a benchmark to evaluate and test the SE-CRL problem.

### Strengths
The authors have formalized the proposed SE-CRL problem with a well-defined problem statement that is both precise and standardized. 

The schematic diagrams and experimental result presentation are clear and easy to understand. 

The ARC-RL method proposed in the paper has clear and comprehensible formulas.

### Weaknesses
1). Wei Ding's paper [1]  also addresses the issue of changes in the action space, and it also extends the state space. The problem discussed in this paper, which involves changes only in the action space, can be considered a subset of the problem described above. The authors claim that this paper is the first to address the problem of changes in the action space, but I believe this statement may not be entirely accurate. The issue of robustness in robotic algorithms under action space changes has already been extensively studied.

2). In this paper, "Although a general policy can be obtained using the union of all action spaces, the previous global optimum may become a local one that does not fit the new action space." The claim made in the paper regarding the potential of an expanded action space to discover more optimal solutions is not clearly supported by Figure 4 or other results. The current presentation of the results does not adequately demonstrate how an expanded action space contributes to improved performance or enables superior solutions. It is recommended to either provide additional evidence or analysis that explicitly illustrates this claim or revise the statement to better align with the presented data.

3). Minor issue: "new neurons are initialized randomly". It should be parameters or weights that are initialized.

### Questions
1). Can you explain why the performance of some algorithms (FT, IND) in Figure 4 is degraded with action expansion? In action expansion setting, 

2). Was 0-3M in Figure 4b trained during this period? Do you use the checkpoint load of task1 to perform the test? Why is the purple curve so different? Is it a difference between training and testing?

3). The same with figure 4c, only 6-9M were trained, and what did 0-6M do? The FT?

4). The authors propose a relatively complex algorithm to address the issue of aligning policy with action space changes. However, there are simpler approaches, such as directly adding or masking the output layer neurons of the actor and only training the last layer of the actor when transferring across tasks. I did not find a formal definition of methods like Fine-Tuning (FT) and Mask in the text. Are these methods referring to what I described?

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper addresses the issue of varying action set in the same domains. 
The proposed approach involves learning action representation through exploration and using the action representation to enhance reinforcement learning.
Then, the method combines the reconstruction loss and the EWC loss for Continual Learning to train encoder-decoder network.
The method is evaluated in one MiniGrid environment(Empty) and one Procgen environment(Bigfish).

### Strengths
1, This paper pushes in an interesting direction:  generalizing policy to new action set by action representation.

2, The proposed method is justified and explained very clearly.

3, Source code is included.

### Weaknesses
1, Novelty. Using encoder-decoder framework and reconstruction loss to learn action representation have been discussed in many prior work([1],[3]). This raises major concern regarding the novelty of Eq.6 as the loss just combines it with Elastic Weight Consolidation loss from continual learning.


2, Overly Simple Experiment. The method is only evaluated in one MiniGrid environment(Empty) and one Procgen environment(Bigfish). More experiments could enhance the paper.


3, Related work. This paper is missing several works that are closely related to this paper. The authors appear to have missed the rich body of literature on varying action set and learning action relations/representations.

The list is not by any means exhaustive:

[1] Jain A, Szot A, Lim J. Generalization to New Actions in Reinforcement Learning[C]//International Conference on Machine Learning. PMLR, 2020: 4661-4672.

[2] Chandak Y, Theocharous G, Nota C, et al. Lifelong learning with a changing action set[C]//Proceedings of the AAAI Conference on Artificial Intelligence. 2020, 34(04): 3373-3380.

[3] Jain A, Kosaka N, Kim K M, et al. Know your action set: Learning action relations for reinforcement learning[C]//International Conference on Learning Representations. 2021.

[4] Tennenholtz G, Mannor S. The natural language of actions[C]//International Conference on Machine Learning. PMLR, 2019: 6196-6205.

[5] Farquhar G, Gustafson L, Lin Z, et al. Growing action spaces[C]//International Conference on Machine Learning. PMLR, 2020: 3040-3051.

### Questions
1, The experimental setting in Figure 4 and Figure 5 need more detailed explanation. I think the notation of exploration stage and learning stage is necessary. Meanwhile, how does the action set change in the experiment? The authors appear to train policy in task 1, task 2 and task 3 sequentially but should provide more detailed explanation.

2, I am curious to know why the decoder map action representation e to the action probability of any action space. Why not map action representation to the action just like [Yash Chandak et al. Learning action representations for reinforcement learning.]

### Soundness
1

### Presentation
3

### Contribution
1
