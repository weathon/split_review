# MeFBO: A Moreau Envelope Based First-Order Stochastic Gradient Method for Nonconvex Federated Bilevel Optimization

- Decision: Reject
- Avg Score: 4.75
- Scores: 5, 5, 6, 3

## Abstract
Federated Bilevel Optimization (FBO) enables training machine learning models with nested structures across distributed devices while preserving data privacy. However, current FBO methods often impose restrictive assumptions, particularly the requirement of strong convexity in the lower-level objective. To overcome this limitation, we propose a first-order stochastic gradient method for general FBO problems, leveraging a Moreau envelope-based min-max optimization reformulation to handle potentially non-convex lower-level objectives. Unlike implicit gradient methods, our approach eliminates the need for second-order derivative information. We also establish rigorous theoretical guarantees for convergence rate and communication complexity, demonstrating linear speedup as the number of devices increases. Numerical experiments validate the effectiveness and efficiency of our method, showing comparable or superior performances in challenging scenarios, including federated loss function tuning on imbalanced datasets and federated hyper-representation.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The paper concerns Federated Bilevel Optimization (FBO) under weaker conditions than previous work provided. It proposes a Moreau envelope-based min-max reformulation and develops a first-order stochastic gradient method for the general FBO problem. The paper then provides a convergence and complexity analysis, establishing a theoretical guarantee of convergence and communication complexity.  Numerical experiments are performed under various conditions, including federated loss function tuning on unbalanced datasets and federated hyper-representation, which demonstrate faster convergence and superior performance.

### Strengths
1.	Compared to previous learning algorithms for solving bilevel optimization, the proposed algorithm is developed under weaker assumptions of upper- and lower-level objectives, and hessian-free, giving an advantage in communication and computational efficiency in Federated Learning. 
2.	The theoretical work contains two major novelties: (1). The convergence and complexity analysis is developed, releasing restrictive assumptions required in previous work; (2). The results obtained clarify the relationship between step size, number of participants, number of local iterations and convergence. 
3.	Extensive experimental results on challenging settings demonstrate the efficiency of the proposed algorithm.

### Weaknesses
1.	There is a lack of technical novelty, as the analysis is based on previous work that leverages the Moreau envelope and hessian-free approach. For the theoretical part, it is unclear whether the complexity caused by the boundedness of the data heterogeneity introduces additional novelty beyond previous work. As a result, the proposed method seems like a combination of existing works.
2.	It lacks non-asymptotic analysis / numerical evaluations to demonstrate how the level of data heterogeneity affects convergence and robustness. Specifically, while the experiments include both i.i.d. and non-i.i.d. datasets, there is no systematic study on how varying degrees of non-i.i.d. data impact the algorithm's performance. The experiments do not isolate the effect of data heterogeneity, making it difficult to assess the algorithm's robustness under different levels of data imbalance.
3.	The number of tuning parameters is relatively large in my opinion (local update rounds, server learning rates, client learning rates, penalty parameter, and proximal parameter). It could not be easy to choose those parameters in real applications, which affects the efficiency of the algorithm. 
4.	It is recommended to list some examples of bilevel optimization that fit the assumptions of the upper and lower objectives, which will strengthen the motivation of this work.

### Questions
1.	The author states that the theoretical analysis is more complex compared to Liu et al. (2024) due to the bounds of client drifts. Could authors give intuitions on the proof, especially on the complexity caused by the client drifts? 
2.	Could authors comment on the impact of the level of data heterogeneity on the convergence and robustness? 
3.	Could authors provide guidance on the choice of the tuning parameter in algorithm 1?

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
4

### Summary
This paper studies the Federated Bilevel Optimization (FBO) problem and puts forward a first-order method without the requirement of lower-level function strong convexity. Besides, it also provides theoretical analysis and sufficient experimental results to show the advantages of their method.

### Strengths
1. This paper has some interesting experimental observations on the previous FBO methods, such as the sensitivity. 
2. There are solid experiments.

### Weaknesses
1. The presentation of this paper is confusing in some places. The important question that this paper asks on the first page involves both privacy and communication issues. Yet, there is no focus on privacy, which makes the question confusing to readers. Besides, there is a mismatch in the description of the work by Xiao & Ji (2023). In line 40, it is described as an AID-based method, and an ITD-based method in line 132. 
2. I suggest that the authors mention the comparison between the two convergence measures in this paper (line 310) for the following reasons. First, it could allow readers to have a more smooth understanding. More importantly, it helps compare the sample complexity and communication costs. 
3. In the convergence analysis, in eq (109), there is an expectation of the hypergradient on the left-hand side, which should be wrong. I guess it should be the expectation of the hypergradient norm. Meanwhile, it raises another question. Do authors compare the communication cost with previous works? If they do, previous works establish communication cost comparisons when the hypergradient norm square is small. So could authors please provide a more detailed comparison on it?
4. Lastly, the novelty of this paper is limited. In terms of communication, the result (current version) in Corollary does not have a big improvement over SimFBO. Admittedly, this paper is hessian-free and relaxes the assumption of strong convexity. However, it directly benefits from the Moreau envelope proposed by Liu et al. (2024). Please correct me if I missed anything.

### Questions
Please check the weaknesses.

### Soundness
2

### Presentation
2

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
The author(s) developed FedBO, an algorithm that solves the federated bilevel optimization problems without assuming the lower-level objective to be strongly convex. On the theoretical side, the convergence properties of FedBO is studied; on the practical side, FedBO shows superior performance against baselines on some toy learning tasks based on the MNIST datasets.

### Strengths
- The paper is well-written, related work are well-addressed to my knowledge;
- The author(s) studied MeFBO both theoretically and empirically.

### Weaknesses
 - The motivation of MeFBO is ok but not very convincing to me:
    - The paper relaxs the LL-convexity assumption, which feels like the author(s) developed a new algorithm in a slightly different setting using existing analytical tools;
    - The hessian-vector product computation is not very expensive using existing auto-differentiation framework such as PyTorch, so the motivation for avoiding Hessian-vector product is only partially convincing.
- Experiments are based on the tiny MNIST dataset. I understand that the paper is not really motivated from applications in practice, but the experiments can still be improved. For example, the author(s) could use larger dataset and maybe include some other more interesting learning tasks.

### Questions
- Is it really technically challenging to relax the LL-convexity assumption? Or is the analysis based on simple combination of existing proof templates?
- Is bilevel optimization really being used in pratical federated learning applications? Or is it just a interesting topic from the theoretical side?

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
This work aims to solve the federated bilevel optimization problem using the first-order based method. The theoretical analyses for the approximation problem of the federated bilevel optimization problem are provided in this work. Experiments on hyper-parameter optimization tasks are conducted to evaluate the proposed approach.

### Strengths
1. A method based on Moreau envelope is proposed for federated bilevel optimization problem.

2. Some theoretical analyses are provided for the proposed method.

### Weaknesses
I find it difficult to appreciate this work due to the following key reasons.

(W.1.) In the proposed method, the exterior penalty approach is employed to approximate the original constrained optimization problem (2) into the unconstrained optimization problem (4). However, how can you ensure that the optimal solution obtained from the approximation problem (4) is also optimal for the original problem (2)? Furthermore, I found that the convergence rate is related to reaching a stationary point for the approximation problem (4). The stationary point in (2) may deviate from the one in (4).

(W.2.) The main problem studied in this work is not interesting (at least to me). The first-order gradient method for nonconvex distributed centralized (federated) problems was already studied two years ago [1]. Additionally, I did not find any comparisons related to this work in the manuscript.

(W.3.) I have some concerns about the complexity of the proposed algorithm. In each communication round, the algorithm requires solving an additional projection problem as described in Eq. (12). In bilevel deep learning, the variables are often high-dimensional, which increases the complexity of solving the optimization problem.

(W.4.) The experimental results are not sufficiently convincing due to the following reasons: 

(W.4.1) Only the MNIST dataset is used to evaluate the proposed method. Could you conduct experiments on larger-scale datasets? 

(W.4.2) The evaluation is limited to hyper-parameter optimization tasks. It is unclear if the proposed method is applicable to other bilevel optimization tasks, such as meta-learning in [2] or neural architecture search (NAS) in [3]. Could you provide additional experimental results on these tasks? 

(W.4.3) The experiments are conducted on 2- or 3-layer multi-layer perceptrons, raising concerns about the method’s efficiency when applied to models with more parameters. This point is also related to W.3, as larger-scale models may significantly impact the efficiency of the proposed algorithm.

Besides the key concerns, I also have lots of concerns as follows.

(W.5.) Additional comparisons of the convergence rate between the proposed method and existing distributed centralized (federated) bilevel methods should be included to demonstrate the superiority of the proposed approach.

(W.6.) The readability of this work is poor, as it contains numerous notations, some of which lack sufficient explanations. For instance, the exact meaning of $\nabla_1$ and $\nabla_2$ in Eq. (9) is not clearly defined.

(W.7.) In the experiment, the author claims that MeFBO outperforms other methods in both i.i.d. and non-i.i.d. settings. I would appreciate it if the authors could provide more detailed explanations and discussions on these results.

### Questions
I have lots of questions about this work, please refer to the Weaknesses.

### Soundness
1

### Presentation
2

### Contribution
1
