# Deep Distributed Optimization for Large-Scale Quadratic Programming

- Decision: Accept
- Scores: 6, 3, 5

## Abstract
Quadratic programming (QP) forms a crucial foundation in optimization, encompassing a broad spectrum of domains and serving as the basis for more advanced algorithms. Consequently, as the scale and complexity of modern applications continue to grow, the development of efficient and reliable QP algorithms becomes increasingly vital. In this context, this paper introduces a novel deep learning-aided distributed optimization architecture designed for tackling large-scale QP problems. First, we combine the state-of-the-art Operator Splitting QP (OSQP) method with a consensus approach to derive DistributedQP, a new method tailored for network-structured problems, with convergence guarantees to optimality. Subsequently, we unfold this optimizer into a deep learning framework, leading to DeepDistributedQP, which leverages learned policies to accelerate reaching to desired accuracy within a restricted amount of iterations. Our approach is also theoretically grounded through Probably Approximately Correct (PAC)-Bayes theory, providing generalization bounds on the expected optimality gap for unseen problems. The proposed framework, as well as its centralized version DeepQP, significantly outperform their standard optimization counterparts on a variety of tasks such as randomly generated problems, optimal control, linear regression, transportation networks and others. Notably, DeepDistributedQP demonstrates strong generalization by training on small problems and scaling to solve much larger ones (up to 50K variables and 150K constraints) using the same policy. Moreover, it achieves orders-of-magnitude improvements in wall-clock time compared to OSQP. The certifiable performance guarantees of our approach are also demonstrated, ensuring higher-quality solutions over traditional optimizers.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The authors present an optimization technique for solving quadratic programming problems distributed across multiple compute nodes. The methods use a extend OSQP methodology to a distributed framework which has similarities to a two-block ADMM approach. The authors identify that selecting hyperparameters in this methodology can greatly influence convergence rates. As a result, the authors propose learning the hyperparameters through a deep learning model that has the iterations of the distributed OSQP algorithm embedded as layers.

### Strengths
Using solved QP problems to train the deep learning model, the authors are able to select optimal hyperparameters that greatly improve the convergence for solving new distributed QP problems.

### Weaknesses
A limitation of this approach seems to be the amount of training data required to train the neural network.



### Questions
1.	 Can the authors provide specific details about the dataset size used in each experiment, and comment about how much data would be needed for a user to implement this strategy.
2.	Can the authors discuss if they have separate models for each experiment, or if a single model was used across all problems. If multiple models are used, can the authors comment on the ability of models to generalize to other problems.
3.	Theorem 3 depends on a set of problems drawn from a distribution. Can the authors provide any empirical evidence or discussion on how well the bounds hold for different types of problems?
4.	The authors require knowing the maximum number of iterations, K, apriori. Generally, the maximum number of iterations is quite large with the intention that the optimization solver finds a solution before reaching the limit. Is choosing an appropriate value of K required to construct a deep neural network model that is memory and time efficient? 
5.	In many of the experiments the authors evaluate the optimality gap up to the maximum number of iterations. However, often we care about the number of iterations to reach the optimum. Does this change the methodology implementation?

Some minor points are:
1.	The authors should define some terms like $r$, $\theta$ in equation (10).
2.	Can the authors provide more detail about the known mapping G on page 6, line 282.
3.	Spelling mistake on “non-distrubuted” on page 6 line 290.

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper combines the interpretability of distributed optimization with the strong empirical performance of deep neural networks to enhance optimization efficiency. The authors propose a distributed method for QPs with theoretical convergence guarantees. They then unfold this method into a deep neural network, leveraging it to accelerate QP solutions. The paper includes both theoretical proofs and numerical results to demonstrate effectiveness. The author claim that the proposed approach outperforms conventional optimization softwares.

### Strengths
The mathematical aspects of the paper are technically correct.

### Weaknesses
The primary concern revolves around the novelty of the unfolded network. 
A similar approach can be found in [1], which also predicts parameters for ADMM in conventional OSQP using reinforcement learning, where this work seems to be a straightforward substitution of tuning efforts with basic MLPs. 
This also raises questions about the fairness and completeness of the experiments, as the authors only compare their method against OSQP without considering other learning-based frameworks that could potentially yield better performance. Specifically, the lack of comparison to other learning-based optimization methods, especially those that also leverage deep learning for parameter tuning in iterative solvers, is a significant oversight. The paper would benefit from a more comprehensive experimental evaluation that includes these relevant baselines. Additionally, the presentation in Section 6 is somewhat difficult to follow. For example, the implementation of the performance metrics is not clearly explained, and it would be helpful for the authors to provide more details on how improvements are quantified. Another minor issue is that some notations are quite confusing and not adequately introduced

### Questions
Questions:
In addtion to those mentioned in weakness, there are some specifc questions regarding this paper.
1. What does r^k_i in Figure 1 and subsection **Learning feedback policies** represent? This notation is not defined elsewhere in the paper. Additionally, a complete update formulation would greatly aid in understanding the unfolding process.
1. The author mentions that distributed methods are effective for large-scale decision-making; however, the tested problems are relatively small. Can the authors discuss the feasibility of extending the numerical results to larger problem sizes?
3. The specific number of layers used in the neural network is not mentioned. From the description, I assume it corresponds to $K$. Do these layers share the same weights? Additionally, how does DEEPDISTRQP perform with varying numbers of layers?
4. Why does Figure 6 use the relative optimality gap as a metric, while other figures utilize the absolute optimality gap? What is the rationale behind this choice?

### Soundness
3

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
5

### Summary
This paper proposes two frameworks -- Distributed Quadratic Programming (DistributedQP) and Deep Distributed Quadratic Programming (DeepDistributedQP). The former combines the state-of-the-art operator splitting method in optimization with distributed optimization, and the latter further introduces deep neural networks into the framework. The authors theoretically prove the convergence guarantees and the generalization bounds of the algorithms. Some numerical simulations are provided to empirically verify the effectiveness of the algorithms.

### Strengths
1. The organization of the paper is clear -- the authors first introduce distributed version of operator splitting, and then combine explain how to incorporate deep learning techniques into the proposed framework to solve optimization problems more effectively.

2. The theoretical proof is well-structured and easy to follow.

### Weaknesses
Major:

1. (Lack of Motivation) In DEEPDISTRQP framework, the authors aimed to combine distributed optimization, in particular distributed quadratic programming, with deep learning. However, it lacks motivation of why one should study this type of problems. It is true that distributed QP part has the advantage of interpretability, while the deep learning part has stronger generalization capabilities. However, the experiments are only limited to relatively small-scale problems like optimal control, portfolio optimization, etc. It is unclear if this framework can handle large-scale deep learning problems effectively, and thus a optimization journal, instead of a machine learning conference, might be a better fit for this paper. The paper does not adequately explain the specific scenarios where the proposed combination of distributed QP and deep learning provides a distinct advantage over existing methods, especially considering the computational overhead introduced by the deep learning component. For example, in what specific applications would the interpretability of the QP component be crucial, and how does the deep learning component enhance the solution quality or efficiency in those cases, compared to using either method alone?

2. (Lack of Novelty) The design of the frameworks as well as the theoretical analysis are more like a combination of existing techniques, such as local and global updates, primal dual updates, the generalization bounds, etc. It is unclear if there is any novelty of simply combining these techniques, especially provided that the experiments are only conducted on some simple ones. The paper does not clearly articulate how the combination of these techniques leads to a novel approach with unique properties or benefits. The theoretical analysis, while well-structured, seems to follow standard approaches for convergence and generalization, and it's unclear what new insights are gained from this particular combination.

3. (Unfair Comparison in Experiments) All figures of the experiments section have the iteration number as the horizontal axis, and the curves showcase better performance of DeepDistributedQP. However, different model architectures have different per-iteration complexities, and thus it is unfair to simply plot the optimality gap vs iteration numbers. The comparison lacks a fair assessment of computational cost, as the deep learning components likely introduce significant overhead per iteration compared to the standard distributed QP method. A more appropriate comparison would involve plotting the optimality gap against wall-clock time or computational cost, which would provide a more realistic evaluation of the practical performance of the proposed method.

Minor:

1. The term 'OSQP' is first introduced in the abstract without additional context. It is unclear what OS is for the audience outside of optimization community.

### Questions
I am wondering if the authors could explain the motivation and the novelty of this paper.

### Soundness
3

### Presentation
3

### Contribution
1
