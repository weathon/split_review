# A Mathematics-Inspired Learning-to-Optimize Framework for Decentralized Optimization

- Decision: Reject
- Avg Score: 4.50
- Scores: 3, 6, 6, 3

## Abstract
Most decentralized optimization algorithms are handcrafted. While endowed with strong theoretical guarantees, these algorithms generally target a broad class of problems, thereby not being adaptive or customized to specific problem features. This paper studies data-driven decentralized algorithms trained to exploit problem features to boost convergence. Existing learning-to-optimize methods typically suffer from poor generalization or prohibitively vast search spaces. In addition, they face more challenges in decentralized settings where nodes must reach consensus through neighborhood communications without global information. To resolve these challenges, this paper first derives the necessary conditions that successful decentralized algorithmic rules need to satisfy to achieve both optimality and consensus. Based on these conditions, we propose a novel **M**athematics-**i**nspired **L**earning-to-**o**ptimize framework for **D**ecentralized **o**ptimization (**MiLoDo**). Empirical results demonstrate that MiLoDo-trained algorithms outperform handcrafted algorithms and exhibit strong generalizations. Algorithms learned via MiLoDo in 100 iterations perform robustly when running 100,000 iterations during inferences. Moreover, MiLoDo-trained algorithms on synthetic datasets perform well on problems involving real data, higher dimensions, and different loss functions.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
This paper proposes distributed algorithm called MiLoDo that solve consensus-type problems. Some simulations are run to demonstrate the speed of convergence.

### Strengths
- Distributed optimization is an important problem. 
- This paper is fairly easy to read and the methods seem to make sense. 
- A number of simulations are done.

### Weaknesses
 - It seems that not much in the paper is new? A lot of the tricks are standard in distributed optimization, for example, variable duplicating to create equality constraints are used in ADMM. 
- I'm also not sure what mathematical-inspired means. The methods are follow standard approaches. 
- I would suggest that the paper do a better job in describing what is different between the material in the paper and existing work out there.

### Questions
- The update rules in this paper is similar to tuning the step size in iterative algorithms. There are a lot of different methods for tuning these step sizes, it would be useful to compare against some of these.

### Soundness
2

### Presentation
2

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
This paper introduces a new approach to learning-to-optimize for distributed optimization. The core contribution is a new parameterization of the optimizer update rule which is motivated by theoretical conditions that any update rule must satisfy for convergence. This is an elegant approach leading to a new method, MiLoDo, that exhibits superior empirical convergence behavior compared to prior work in the literature on small test problems (LASSO, logistic regression, MLP/MNIST, and ResNet/CIFAR).

### Strengths
1. The paper is well-written and easy to follow.
2. The contributions are well-situated with respect to the recent literatures on learned optimizers and decentralized optimization.
3. The motivation for the parameterization introduced in equations (12)--(14) as well as the implementation in (22)--(24) is sound and interesting.
4. Thorough experiments with small problems illustrate the promise of this approach.
5. That MiLoDo generalizes to many more iterations than the learned optimizer was trained on is impressive.

### Weaknesses
 1. The motivation to use decentralized optimizers remains somewhat unclear, and there doesn't appear to be a well-known widely-adopted implementation today. This may change in the future, especially as some companies talk about training models across data centers. However, without that, the overall motivation for this contribution remains limited.
 2. The experimental results focus on smaller problems, the largest being a ResNet trained on CIFAR. These are all problems that can be easily solved today in a centralized manner with very modest/accessible compute resources. The empirical results would be much stronger if they demonstrated that the same trends hold at scales where distributed/decentralized training is necessary.
 3. Some experimental details are unclear; for example is the same 5-stage MiLoDo training procedure used for all workloads, including MLP and ResNet? How sensitive is MiLoDo training to this procedure? The MiLoDo training setup for MNIST and CIFAR is also less convincing, given that the meta-training is done using (subsets of) the same dataset that evaluation is performed on. It would be much more convincing to see results on neural network training where there is clear separation between training ("optimizees") and the workload used to evaluate the learned optimizer.

### Questions
1. For Lines 82--93, are there references that could be cited to support the last three challenges mentioned, especially "weak generalization"?
2. Is there stronger motivation that can be provided for where decentralized (learned) optimization is being applied or will be useful in practice? Similarly, can motivation be provided for decentralized LASSO or logistic regression tasks?
3. Could consistent notation be used throughout the paper? In Sections 2 and 3 the learnable update rule is denoted $\bf{g}$, while in Section 4 $\bf{g}$ is used for subgradients of the regularization term and the learned update rule is $\bf{m}$.
4. I'm confused how the generalization to problems with higher problem dimension works. From Section 4.2 I understand that the update rule is implemented as an LSTM, for which I would have thought the shapes of its weights depended on the problem dimension. Can you please explain?
5. The formulation and derivation of MiLoDo in Section 4.1 is written with $p_i^k$, $p_{i,j,1}^k$ and $p_{i,j,2}^k$ that are memoryless, while in Section 4.2 we see these are implemented with LSTMs, i.e., RNNs that have memory/state across iterations. That this helps or is useful is not surprising since it is known that optimizers with memory/momentum are important for efficient convergence of decentralized optimization (see, e.g., EXTRA, DIGing, SlowMo). How do we reconcile this important difference between Sections 4.1 and 4.2? Is memory helpful/sufficient, but not necessary according to the theory? Do the theoretical claims also apply to this implementation with LSTMs?
6. Any intuition about the loss spike/instability (in $F(x)$) observed in Fig 7 around iteration 500?
7. The experiments illustrate the effectiveness and capabilities of trained MiLoDo optimizers. It would be good to also include some illustration and discussion about the process of training MiLoDo optimizers to provide more intuition and support for the five-stage procedure.
8. I appreciated the inclusion of runtimes and transparency about MiLoDo and learned optimizers requiring more computation per update. Please include more information about the system on which timing experiments were run for results in Table 1. It is impossible to interpret these times without knowing more about the system setup.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper addresses the learning to optimize problem in the decentralized setting. The current learning to optimize algorithms suffer from big search space and poor generalization. The paper considers the mathematical conditions requires in the decentralized system to achieve consensus and optimality and proposed MiLoDo. For a fixed network with individually trained agents, MiLoDo demonstrated robust performance with generalization properties for both synthetic and real data.

### Strengths
The MiLoDo framework provides insights on the necessary mathematical conditions for ensuring consensus and optimality in decentralized training, which could be of separate interest.

This work bridges the L2O literature with decentralized optimization techniques, the problem formulation is intuitive and the simplification on parameters as well as reductions in parameter search space works well in practice.

I have not checked the technical details of the proof in the paper's appendix, but the analytical results in the main paper seem to be intuitive and aligns with the existing literature in the decentralized optimization literature.

### Weaknesses
Perhaps one of the most important aspects of decentralized optimization and training over a network, as noted in papers such as EXTRA and various gradient tracking approaches, is to address the data and/or function heterogeneity across agents. In the numerical experiments, especially for MNIST and CIFAR-10, the data seems to be evenly split across agents. When the loss functions are similar across the decentralized network, the system essentially reduces to a SVRG problem, where the consensus and optimality questions are, in a sense, trivial. This paper would benefit from additional experiments regarding the impact of data heterogeneity in the framework. The actual notion of generalization should also be discussed regarding whether MiLoDo can generalize across various degrees of heterogeneity. I will base my opinion on the acceptance of this paper on how the authors address this question in their rebuttal.

As the authors have mentioned, the current MiLoDo framework requires a fixed network with fully synchronized updates. This assumption is difficult to satisfy for many current applications of decentralized optimization tasks. 

MiLoDo requires a set of parameters to be learned for all connections among agents, which suggests that the worst-case complexity of the problem is O(n^2) with respect to network size. This scaling is undesirable for large-scale applications.

Despite the mathematical inspiration behind MiLoDo, the framework did not directly address the impact of network structure e.g. the connectivity of the decentralized network, with the only assumption that the graph is strongly connected.

Currently each agent in the MiLoDo framework is required to learn individual parameters, which are specific to the agents. A more concise and elegant solution would be training one set of parameters which can be used for all agents in the network. Though this might not satisfy the mathematical conditions noted in the papers, some discussions would be appreciated.

### Questions
Please see the weaknesses.

### Soundness
3

### Presentation
3

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
This paper proposes an approach to extend the Learning to Optimize framework to the decentralized setting. The authors compared the trained model with many commonly used decentralized optimization approaches using empirical evaluations.

### Strengths
The effort of extending Learning to Optimize framework to the decentralized setting is interesting.

### Weaknesses
1. The comparison with existing decentralized optimization results are not fair. It is commonly known that existing decentralized optimization algorithms are sensitive to parameters such as learning rate. How did you select learning rate for these existing decentralized optimization algorithms? If these existing algorithms were to given the best parameters, then their performance cannot be beaten by the proposed algorithm, which uses essentially the same algorithmic structure.

2. It is well known that exiting decentralized algorithms are sensitive to parameters like learning rate, it seems much easier to learn the learning rate, than to conduct the learning proposed here.

### Questions
see weakness.

### Soundness
2

### Presentation
2

### Contribution
2
