# Can Differentiable Decision Trees Learn Interpretable Reward Functions?

- Decision: Reject
- Scores: 6, 5, 6, 3

## Abstract
There is an increasing interest in learning reward functions that model human
intent and human preferences. However, many frameworks use blackbox learning
methods that, while expressive, are difficult to interpret. We propose and evaluate
a novel approach for learning expressive and interpretable reward functions from
preferences using Differentiable Decision Trees (DDTs). Our experiments across
several domains, including Cartpole, Visual Gridworld environments and Atari
games, provide evidence that that the tree structure of our learned reward function is
useful in determining the extent to which the reward function is aligned with human
preferences. We experimentally demonstrate that using reward DDTs results in
competitive performance when compared with larger capacity deep neural network
reward functions. We also observe that the choice between soft and hard (argmax)
output of reward DDT reveals a tension between wanting highly shaped rewards
to ensure good RL performance, while also wanting simpler, more interpretable
rewards.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
In reinforcement learning from human feedback, the learned reward model is usually a neural model, which is usually not interpretable. This work proposes learning interpretable reward models represented by Differentiable Decision Trees (DDTs). Empirically, DDTs can learn reward models that are useful for RL.

### Strengths
This paper novelly uses DDT to learn and represent a reward model, and shows that the method is effective on CartPole, MNIST, and Atari domains. Using a tree-based reward model is overall an inspiring approach that is under-explored in the literature.

### Weaknesses
The paper started by using learning from human feedback as a motivating example (Fig. 1). However, the domains are all simulated domains. Since rewards in simulated domains are human-designed, it is comparatively simple to learn these reward functions. The experiments do not demonstrate the method's effectiveness in scenarios where the reward function is complex or unknown, which is the primary challenge in learning from human feedback. 

Clarity on the contributions. It would be helpful to clarify which part of the algorithm is exactly the DDT algorithm itself, and which part is its adaption to reward learning. Specifically, the paper does not clearly distinguish between the core DDT method and the modifications made for reward learning. This makes it difficult to assess the novelty and impact of the proposed approach. It is unclear what specific modifications were made to the loss function or the tree structure to accommodate reward learning, rather than just using a standard classification loss.

### Questions
Is it practical to learn interpretable reward functions for more realistic domains, like reinforcement learning from human feedback for large language models?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper proposes to represent the reward function in RL as a decision tree where the nodes and leaves are expressed as neural network layers. At each node, a binary classification is conducted to select which child node to visit. At the leave nodes, a multi-classification module and a regression module are adopted to generate discrete and continuous reward value respectively. This tree structure can provide interpretability in determining which behavior should be rewarded or penalized. The experimental section validates the proposed approach with comparisons with different baselines in multiple benchmarks.

### Strengths
* `Originality`: the idea is original.

* `Quality`: there is no major technical issue.

* `Clarity`: the fundamental ideas in this paper are explained.

### Weaknesses
The idea of inserting nonlinear layers in the tree appears to contradict the purpose of using the tree structure for interoperability. It would be great if the author explained the fundamental difference between this tree and a tree-like neural network. In other words, is it possible to design a neural network that connects the neurons as in the tree and uses ReLUs for branching? If the Author agrees, the author can clarify what are the benefits of using the tree structure instead of NN. Does it reduce complexity, etc.  The author also does not explain how to determine the structure of those trees. Do those trees grow like XGBoost trees? According to the experimental section, the trees are not deep. The baseline NNs are not deep, either. The motivation for trading performance for interoperability is not very strong.

### Questions
Please address my question in the `Weakness` field.

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper delves into the significant issue of learning interpretable reward functions based on human preferences. The authors propose the use of differentiable decision trees (DDT) to model these reward functions and follow the standard reinforcement learning from human feedback (RLHF) pipeline. The paper conducts intriguing experiments across various domains to demonstrate the practicality of these interpretable reward functions in diagnosing misaligned objectives within them.

### Strengths
Integrating structural and interpretability constraints into the RLHF pipeline is of paramount importance due to its diagnostic capabilities for misalignment issues. Although the paper doesn't introduce novel algorithms (it employs standard RLHF with DDT reward functions), its empirical investigations are interesting. The experiments, especially in Cartpole, effectively showcase the aforementioned diagnostic utility.

### Weaknesses
Limited algorithmic novelty.

### Questions
In the related work section, it would be beneficial to discuss research on expert-driven reward design techniques that incorporate structural and interpretability constraints [1, 2, 3]. 

Regarding Table 1, could the performance of the baseline neural network reward be enhanced by using a richer representation such as a high-capacity deep neural network?

References:

[1] Jiang, et al. Temporal-Logic-Based Reward Shaping for Continuing Reinforcement Learning Tasks. 2021.

[2] Devidze, et al. Explicable Reward Design for Reinforcement Learning Agents. 2021.

[3] Icarte, et al. Reward Machines: Exploiting Reward Function Structure in Reinforcement Learning. 2022.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposes to learn more interpretable reward functions by employing differentiable decision trees. The differentiable decision tree allows for explanations of the reward making decision process, therefore enhancing interpretability. Experiments are conducted on cartpole, a new gridworld MNIST environment, and atari.

### Strengths
Strength 1: The idea of improving reward model interpretability is interesting, novel, and timely.

Strength 2: The novel MNIST environment can be of use to the RL community.

Strength 3: The motivation and writing of this paper is quite clear.

### Weaknesses
Weakness 1 (Major): One of my main concerns is the lack of repetition over random seeds. In my understanding, the cartpole environment uses 3 seeds (which is not enough for RL), but the Atari environments seem to use only one seed (and treat the seed as a tunable hyperparameter?). This is a cause for concern regarding the replicability and generalization of the proposed method. In addition, it means it is basically impossible to tell if the results about using a regularizer or soft output are significant. The mean and standard deviation across random seeds for each experiment should be reported.

Weakness 2 (Major): The inability to interpret the decision for breakout is a bit worrying. I think this is an important result that should be discussed in the main paper for clarity.

Weakness 3 (Minor): The synthetic trace method could be explained better, as it seems to be a key part of allowing interpretability in complex environments. But it is only introduced in the experiments section. This makes the experiment section a bit hard to follow. I think that introducing this in the methodology section would make more sense.

### Questions
Question 1: How would the synthetic trace method be applied to the simple environments (cartpole and mnist)?

Question 2: Could this method be applied to text data?

Question 3: Why does the neural network baseline perform poorly for Cartpole? This is surprising since cartpole is a pretty easy task.

### Soundness
2 fair

### Presentation
3 good

### Contribution
3 good
