# Hessian-Aware Bayesian Optimization for Decision Making Systems

- Decision: Reject
- Scores: 1, 3, 8, 5, 5

## Abstract
Many approaches for optimizing decision making systems rely on gradient based methods requiring informative feedback from the environment. However, in the case where such feedback is sparse or uninformative, such approaches may result in poor performance. Derivative-free approaches such as Bayesian Optimization mitigate the dependency on the quality of gradient feedback, but are known to scale poorly in the high-dimension setting of complex decision making systems. This problem is exacerbated if the system requires interactions between several actors cooperating to accomplish a shared goal. To address the dimensionality challenge, we propose a compact multi-layered architecture modeling the dynamics of actor interactions through the concept of role. Additionally, we introduce Hessian-aware Bayesian Optimization to efficiently optimize the multi-layered architecture parameterized by a large number of parameters. Experimental results demonstrate that our method (HA-GP-UCB) works effectively on several benchmarks under resource constraints and malformed feedback settings.

## Human Reviews

## Human Reviewer 1

### Rating
1

### Rating Number
1

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
A decision making system determine a sequence of actions to achieve a desired goal.  To solve such a problem, the authors use Bayesian optimization where gradient information is not actively utilized.  In particular, the authors propose Hessian-aware Bayesian optimization to optimize a multi-layer architecture.  Finally, some theoretical and numerical results are reported to show the validity of the proposed methods.

### Strengths
* It solves an interesting problem.

### Weaknesses
 * This paper is hard to follow.  There are too many components but they are not described appropriately.
* Writing and presentation should be improved.  For example, the Introduction section is started by the following sentences: "Decision Making Systems choose sequences of actions to accomplish a goal. Multi-Agent Decision Making Systems choose actions for multiple actors working together towards a shared goal. Multi-Agent Reinforcement Learning (MARL) has emerged as a competitive approach for optimizing Decision Making Systems in the multi-agent settings"  These are three independent sentences.  This part should be re-written.  In addition, a period is missing.  Also, this sentence "We propose the usage of Bayesian Optimization (BO)" is somewhat unnatural.  Please revise it.  There are other cases, but I would not enumerate all of them.  Please revise an article carefully.
* Figures are too small and legends are overlapped with graphs; please see Figures 4 and 5.
* Theoretical results heavily rely on the previous work, in particular (Srinivas et al., 2010).
* I would like to ask about the results in Figure 5.  First off, why do BO results only show current maxima until a particular iteration, i.e., monotonically increasing?  Why are the other results fluctuated?  Also, why do the results at initial iterations differ across algorithms?  It seems unfair to the baseline methods.  Moreover, some baseline methods are better than the proposed methods.  These results seem reasonable.  Why do the authors use Bayesian optimization instead of reinforcement learning in these problems?
* Does Table 1 show the superior performance of your algorithm?  To my understanding, HA-GP-UCB does not outperform some algorithms.

### Questions
* Does Table 1 show the superior performance of your algorithm?  To my understanding, HA-GP-UCB does not outperform some algorithms.

### Soundness
2 fair

### Presentation
1 poor

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper proposed a metamodel based on message-passing neural network  for multi-agent policy search. The MPNN represents a dependency graph between agents, which is claimed to be expressive and compact. A Bayesian optimization algorithm is proposed to learn the graph structure. Using direct queries of Hessian, we can learn the dependency graph using a GP-UCB variant. Experimental results have shown strong performance compared to MARL, HDBO and ablations.

### Strengths
1. The idea of using Bayesian optimization to learn the dependency graph structure is interesting and novel.
2. The multi-agent policy representation is significant.
3. Combination of role assignment and role interaction looks powerful in empirical results.
4. Figures help to understand the contributions.

### Weaknesses
1. The presentation of the paper is poor.
- More background knowledge should be introduced to further clarify the motivations, like the necessity of the JIT compilation. The paper does not adequately explain why JIT compilation is necessary or beneficial in the context of multi-agent policy search. It's unclear what specific resource constraints or performance bottlenecks this addresses. The paper should provide a clear explanation of the problem that JIT compilation solves, and why existing methods are insufficient.
- The notation is extensively abused and many algorithms and notations have no formal definitions (See questions for some of them). The lack of formal definitions for key notations such as the subscripts of $\theta$ (e.g., $\theta_{r,i}$ and $\theta_{g,e}$) and the superscript $D$ in section 4.4 makes it difficult to understand the mathematical formulations. The meaning of superscript $(i)$ in section 4.4 is also unclear, and the mathematical expression for regret $r(t)$ when querying the Hessian is not provided. The paper also does not define $\mathcal U$ in Algorithm 4 or the Max-Cliques operation in the same algorithm.
2. The motivation of one of the main contributions, using Hessian in Bayesian optimization is not very clear. As Bayesian optimization is a black-box function, directly querying Hessian might be very hard. It is unclear how the surrogate Hessian is obtained and what assumptions are made to ensure it is a good approximation of the true Hessian. The paper does not discuss the computational cost of obtaining the surrogate Hessian, which is a critical factor in the practicality of the method. The paper should also discuss the limitations of using a surrogate Hessian and how it might affect the performance of the Bayesian optimization.
3. There are no proofs or lemmas for the theorems.
4. Should add related works of following topics:
- Learning the dependency graph;
- Modeling dependency graph as a MPNN;
- Bayesian optimization to learn the graph structure;

Overall, it is a very interesting paper with possibly strong contributions, but the writing and presentation is very poor and confusing. I suggest the authors to do a very thorough revision during the rebuttal.

### Questions
### Questions regarding the Hessian-award BO:
1. How to observe the surrogate Hessian of the black-box function?
2. What is the motivations of using Hessian in BO? If you already observed Hessian, why not using the gradient descent?
### Questions overall:
3. what do you mean by JIT compilations? The meaning is not clear in the context of multi-agent policy structure. 
4. Why do you use MPNN rather than graph convolution, graph attention or other transformer vi rants? These models should be more expressive.
### Questions about the notations:
- What does the subscripts of $\theta$ means? For example, sometimes you use $\theta_{r,i}$ and some times $\theta_{g,e}$ without any explanations on what are $r,g,i,e$.
- What is super script D in section 4.4? I only see the definition of ``some dimensionality’’. $D$ is a very important dependency terms of regret in the theorem.
- What does the super script ${}^(i)$ mean in section 4.4?
- What is the mathematical expression of regret $r(t)$ of querying Hessian?
- What is $\mathcal U$ in Algorithm 4?
- What is the Max-Cliques operation in Algorithm 4?

### Soundness
2 fair

### Presentation
1 poor

### Contribution
3 good

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper presents a multi-agent reinforcement learning algorithm based on Bayesian optimization. The main contribution of this paper is the idea to incorporate the Hessian information to solve the additive structure of the high dimensional problem as an additive decomposition. Because the value Hessian is unavailable, the system relies on the policy Hessian as a surrogate. The paper includes extensive evaluations and regret bounds.

### Strengths
The main contribution of the paper in terms of the Hessian aware BO is very interesting and could have a very large impact on the community. In fact, I believe that the MARL application could be completely removed and still have a valuable paper, maybe extended to other high dimensional problems with additive structure. I have minimal experience with MARL, but it seems that the approach is competitive in that area as well.
The paper provides an excellent theoretical and empirical analysis.

### Weaknesses
The main weakness of the paper (and it is understandable) is the amount of clutter in the paper. Most figures and tables are impossible to read without zoom. The amount of information provided should be more appropriate to a journal article, although I can see the motivation behind a submission to ICLR instead. However, the paper is clear enough.
Despite reading appendix G, regarding the method presented, it is still unclear to me if H_pi can always be used as a reliable surrogate for H_v, as g might have some 0 (or small) components. In fact, for the optimal policy, shouldn’t it be 0?

### Questions
-Why do you need JIT-compilation? Isn’t it just instantiation with certain parameter values?
-In algorithm 4, do you initialise the parameters with a uniform distribution? In BO literature, it is common to use low discrepancy sequences or sampling procedures.

### Soundness
4 excellent

### Presentation
4 excellent

### Contribution
4 excellent

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper proposes Hessian-aware Bayesian optimization for the multi-agent policy optimization.

### Strengths
The multi-agent policy optimization is interesting setting.

The paper seemingly technically sound, but I currently cannot follow the technical detail because of reason below.

### Weaknesses
Although I'm not familiar with the topic (reinforcement learning with multi-agent), I currently think the paper is not easy to follow for many readers. Even the basic problem setting is difficult to fully understand because of unclear descriptions. The meanings of several key words (abstraction, immutable, compile, and so on) are not clarified in the text, because of which technical description is difficult to understand for those who are not familiar with the topic.

The role affinity function \Lambda^\theta_{r,i} is not clearly defined, and its purpose is unclear. It is not obvious how this function quantifies the affinity of an agent for a specific role, nor what the inputs and outputs of this function are. The description lacks the necessary context to understand its role in the overall algorithm.

The use of 'h' without a subscript in line 4 of Algorithm 4 is confusing. It is unclear what this variable represents, how it is constructed, and why it is used in this specific step. Without a clear definition, it is difficult to understand the purpose of this operation within the algorithm.

The concept of a 'surrogate of Hessian' is not well-defined. The paper does not provide sufficient information on how this surrogate is constructed, what its properties are, and how it relates to the true Hessian. The lack of clarity makes it difficult to assess the validity of the proposed method. Furthermore, the claim that the cumulative regret scales with O(log D) is not adequately justified. The assumption 1 is not intuitive, and its connection to the low-dimensional dependency of the underlying true function is not explained. It is unclear what the parameter p_g represents and how it influences the regret bound.

### Questions
Overall, I feel severe difficulty to understand the paper. I'd appreciate if the authors could provide more elaborated explanation.

What is the definition of the role affinity function \Lambda^\theta_r,i ? What does it indicate?

What is h without subscript in line 4 of Algorithm 4?

What is a surrogate of Hessian? How is it constructed ? 

The authors claim the cumulative regret of the proposed method scale with O(log D). What assumption makes it possible? The implication behind assumption 1 is difficult to find for me. Does it assume some low dimensional essential dependency in the underlying true function?

### Soundness
3 good

### Presentation
1 poor

### Contribution
3 good

---

## Human Reviewer 5

### Rating
5

### Rating Number
5

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper studies the problem of learning good decision-making policies when multiple agents are involved.
This problem traditionally presents several challenges, the biggest of which include reasoning about sparse feedback and unreliable gradient information, and accounting for interactions between agents.
To perform effective optimization with sparse feedback and unreliable gradient information, the authors employ Bayesian optimization (BayesOpt).
However, BayesOpt doesn't scale well to high dimensions, so the paper proposes using an abstraction of role and role interaction to model the agents on a high level, thus significantly simplifying the policy space to search over.
To further aid scaling BayesOpt to the high-dimensional search space, the authors use a surrogate Hessian model to learn an additive structure of the space, which ultimately helps identify good regions within the space.
Experimental results show promising performance of the proposed algorithm.

### Strengths
The problem studied is interesting and important.
The paper motivates the use of the role and role interaction abstraction well, and the proposed affinity score seems like a good way to quantify how suitable each agent is for each role.
Some experiments show really strong performance from the proposed algorithm against a wide range of baselines.

### Weaknesses
There seem to be many components to the algorithm: role abstraction, BayesOpt with the Upper Confidence Bound policy, the Hessian surrogate.
As far as I call tell, the ablation study doesn't give me insights into which components are useful for the final algorithm.
For example, could we use a different optimization algorithm that doesn't rely on gradient information such as DIRECT or evolutionary algorithms?
How much does information about the Hessian help BayesOpt?

I would have liked to see more discussion on the quality of the Hessian surrogate.
My understanding is that Hessian information can be accessed via the JIT compilation of $v(\theta)$.
How good is this surrogate?
What are the situations where this surrogate doesn't offer reliable information?

### Questions
Please see my questions in the Weaknesses section.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
3 good
