# Multi-fidelity Deep Symbolic Optimization

- Decision: Reject
- Scores: 3, 5, 8, 5, 5

## Abstract
Although Symbolic Optimization (SO) can be used to model many challenging problems, the computational cost of evaluating large numbers of candidate solutions is intractable in many real-world domains for existing SO algorithms based on reinforcement learning (RL). While lower-fidelity surrogate models or simulations can be used to speed up solution evaluation, current methods for SO are unaware of the existence of the multiple fidelities and therefore do not natively account for the mismatch between lower and higher fidelities. We propose to explicitly reason over the multiple fidelities. For that, we introduce Multi-Fidelity Markov Decision Processes (MF-MDPs) and propose a whole new family of multi-fidelity SO algorithms that account for multiple fidelities and their associated costs. We conduct experimental evaluation in two challenging SO domains, Symbolic Regression and Antibody Optimization, and show that our methods outperform fidelity-agnostic and fidelity-aware baselines.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper formulates the problem of performing Deep Symbolic Optimization (DSO) using reinforcement learning (RL) when the real black-box objective function is expensive to evaluate, but there are cheaper approximations of the objective function with different fidelities. The goal of the problem is to utilize both the real objective function and multi-fidelity approximations to find a solution that achieves a high value of the original objective function, with a limited budget for evaluations of the real objective function. With the problem formulated as an extended version of MDP with multiple versions of reward functions, the paper proposes a rule-based method to choose the reward function to use for evaluating every sampled token sequence, the main idea being "Elite-Pick", i.e., to only use the real objective function to evaluate token sequences with high potential to produce high objective value. Together with this Elite-Pick sampling rule, an RL approach RSEP, based on the Risk-Seeking Policy Gradient, and its variants are proposed to perform DSO under the problem formulation. The paper provides a brief theoretical analysis of RSEP, mostly on the approximation between the RSEP objective and the standard Risk-Seeking Policy Gradient objective in the limit of infinite exploration. The performances of the proposed RSEP and its variants are evaluated on a symbolic regression task and an antibody optimization task.

### Strengths
* The paper formulates an interesting problem with potential value for real-world applications: to find an efficient way of utilizing multi-fidelity approximations of the real objective function for Symbolic Optimization.

* The paper proposes a rule-based method (Elite-Pick sampling) to select the reward function to use for evaluating each token sequence sampled from the RL policy when there are different versions of the reward function with different fidelities and different associated costs. The method is based on the natural idea of only using the expensive real reward function for the token sequences with a high potential to get a high real reward value, where the potential is decided based on previous low-fidelity evaluations.

### Weaknesses
 * The experiment results as they are now are not sufficient evidence of a performance improvement of RSEP and its variants over the baselines. The main experiment results in Figure 2 and Figure 3 show the objective function value v.s. the number of real objective function evaluations. However, the figures do not show how many low-fidelity evaluations are used for each of the compared methods. For example, **it is possible that the proposed RSEP method and its variants used more low-fidelity evaluations than the Sequential baseline in the experiments, which could also result in RSEP outperforming Sequential, but that would not be a fair comparison**. This seems quite likely to be the case for the experiments on antibody optimization, as the Sequential baseline was trained on only 720 low-fidelity evaluations before switching to only evaluating the real objective function, while Figure 3 shows that the compared methods used over 1000 evaluations of the real objective function. Using only 720 low-fidelity evaluations for Sequential when the low-fidelity evaluations are considered free while doing more evaluations on the expensive real objective function does not make much sense, and this probably indicates that RSEP consumed more evaluations than Sequential. Therefore, it would be more sensible to show the number of low-fidelity evaluations consumed by each of the compared methods as well.

* The problem formulation in the paper considers low-fidelity evaluations as free, no matter what the fidelity is. This does not support the "a whole new family of multi-fidelity SO algorithms that account for multiple fidelities and their associated costs" part of the claim in the abstract. This modeling assumption does not match the application scenarios in reality and causes a problem in the problem formulation because one could just evaluate every possible (exponentially many) token sequence using the low-fidelity approximation at the start of any algorithm. In the case where there are multiple approximations of the real objective function, it seems the zero-cost assumption would make the one approximation with the highest fidelity dominate all other approximations with lower fidelities (more on this in the first question below). As the authors point out in the future work discussion, it would be more reasonable to incorporate the costs of evaluating each fidelity into the problem formulation, where higher fidelity comes with a higher cost.

* Because the error rate is defined as $P(R^0 \ge Q^0_\epsilon, R^1 \le Q^1_\epsilon)$ instead of $P(R^1 \le Q^1_\epsilon | R^0 \ge Q^0_\epsilon)$ in Proposition 2, the first observation (Line 150) is quite trivial and does not provide much deep insight for how good the error rate is. If $\epsilon$ is reduced to a very small value, the absolute error rate will be small but we would probably care more about the conditional error rate given that a sample should pass the quantile under the real objective function. The second observation (Line 151) also only tells one side of the story, as a smaller low-fidelity quantile $Q^1_{\epsilon}$ would reduce the error rate, but at the same time, it would reduce the efficiency of using real objective function evaluations.

### Questions
* Given the current formulation where any approximations of the real objective can be evaluated for free regardless of their fidelity, is there any reason to evaluate a token sequence with a low-fidelity approximation when there is another approximation with a higher fidelity?

* When there are more than one non-zero fidelities such as in the experiment on symbolic regression, does the proposed Elite-Pick sampling randomly choose a non-zero fidelity regardless of their fidelities if the sampled token sequence is not over the $(1-\rho)$ quantile (Line 106 - 107)?

### Soundness
1 poor

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper proposes a symbolic optimization algorithm taking into account the multi-fidelity evaluation, which is based on deep symbolic regression (DSO). In the proposed method, the promising solutions are evaluated on the highest fidelity. The experimental results on symbolic regression and antibody optimization tasks show that the proposed method can exploit the multi-fidelity information and outperform the baseline methods.

### Strengths
- A novel symbolic optimization method considering multi-fidelity evaluation scenarios is proposed.
- The multi-fidelity treatment in the proposed method is simple but effective on the considered tasks.
- The novelty of this paper is to introduce the multi-fidelity situation into RL-based symbolic optimization.

### Weaknesses
 - The paper format is NeurIPS format, not ICLR style.
- The baseline methods compared with the proposed methods are very simple and limited.
- The technical novelty of the multi-fidelity treatment is unclear when comparing the existing techniques used in other algorithms.

### Questions
- Multi-fidelity Bayesian optimization could be a competitive algorithm. Is it possible to compare the performance of the proposed method with multi-fidelity Bayesian optimization methods? Moreover, because the proposed method is based on DSO, multi-fidelity reinforcement learning could also be the baseline.
- Could you elaborate on the technical difference and advantage of the proposed method against the existing multi-fidelity handling methods in Bayesian optimization and reinforcement learning?
- How did the authors decide and tune the hyperparameters of the proposed and baseline methods? How sensitive is the performance of each algorithm for hyperparameter settings?

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper studies Symbolic Optimization (SO) problems under the multi-fidelity setting, where the actual reward is computationally inexpensive, and lower-fidelity surrogate models or simulations can be used to speed up the learning. Instead of performing transfer learning or modifying lower-fidelity models, the authors propose to explicitly reason over the multiple fidelities. Experiments on two SO domains, Symbolic Regression and Antibody Optimization demonstrate the effectiveness of their proposed model.

### Strengths
1.	The authors well formulate Symbolic Optimization (SO) problems under the multi-fidelity setting, which is a quite common scenario in AI applications. The proposed novel multi-fidelity learning framework provides a good new insight.
2.	The studies on the effectiveness of different learning mode with lower-fidelities may open up a new research direction on the critical learning mode.

### Weaknesses
I expect the authors to report the running time of different methods, as calling the low-fidelity estimators also takes time. Moreover, it is beneficial to study the calling of different fidelities during the training time.

### Questions
N/A

### Soundness
3 good

### Presentation
3 good

### Contribution
4 excellent

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper proposes to solve multi-fidelity symbolic regression using trajectory-based policy gradient algorithms. The paper introduces a few notions of MDPs specialized to their use case and propose variants of policy gradient algorithms that incorporate multiple reward functions and adapt to risk sensitive objectives. The paper shows some theoretical analysis and improvements over baseline methods.

### Strengths
The paper studies multi-fidelity symbolic regression using trajectory based policy gradient algorithm, which might be seen as an interesting application of policy gradient algorithm to more grounded applications. The paper also shows some promising empirical gains compared to classic baselines. This might attract and diversify RL community's attention to focus more on application rather than algorithmic research.

### Weaknesses
From the description of the problem setup, it feels that using sampling based optimization approach to solving multi-fidelity symbolic regression is a natural option, and hence it is not clear if the idea is very novel. Multi-objective RL and risk-sensitive RL algorithms have been extensively studied in the literature but it appears that the paper makes little comparison to those.

=== **MF-MDP** ===

The MF-MDP discussed in the paper specializes to the case where all MDPs share the same transition structure, then this is effectively a single MDP with multiple reward functions. What's the benefit of introducing this extra concept of MF-MDP, since it does not seem to benefit algorithmic design in the paper. Also maybe it makes sense to borrow ideas and terminologies from the multi-objective RL literature, instead of introducing an almost identical concept.

=== **Risk sensitive policy gradient** ===

The risk sensitive policy gradient algorithm, previously studied in the RL literature such as Tamar et al, seeks to make use of the Markovian structure in the problem setup to improve the sample efficiency. This is because if we just consider the trajectory based variant of policy graident, the theoretical guarantees have become much simpler (or trivial) to derive (because the problem is effectively one-step now). Have the authors considered making use of more fine-grained structure in the sequential decision problem? From the design of the current algorithms, they are mostly trajectory based and do not leverage the MDP structure.

=== **Experiments** ===

I am not an expert in symbolic regression so cannot comment on the significance of the improvements shown in the paper. The paper does seem to compare with a fair amount of baseline approaches, but I leave to the other reviewers to comment whether such baselines are reasonable.

RSEP-0 does appear to perform the best most of the time compared to other alternatives, but not uniformly, since Fig 5 does show cases where it is under performed. Do we have a sense as to when RSEP-0 underperforms the baseline methods?

For RL experiment, it is typical that the same experiments run multiple times in order to derive the standard deviations across random initializations and optimization. This is especially the case for policy gradient algorithms where variance tends to be high. In Fig 5 no such standard deviation curve is shown.

### Questions
=== **MF-MDP** ===

The MF-MDP discussed in the paper specializes to the case where all MDPs share the same transition structure, then this is effectively a single MDP with multiple reward functions. What's the benefit of introducing this extra concept of MF-MDP, since it does not seem to benefit algorithmic design in the paper. Also maybe it makes sense to borrow ideas and terminologies from the multi-objective RL literature, instead of introducing an almost identical concept.

=== **Risk sensitive policy gradient** ===

The risk sensitive policy gradient algorithm, previously studied in the RL literature such as Tamar et al, seeks to make use of the Markovian structure in the problem setup to improve the sample efficiency. This is because if we just consider the trajectory based variant of policy graident, the theoretical guarantees have become much simpler (or trivial) to derive (because the problem is effectively one-step now). Have the authors considered making use of more fine-grained structure in the sequential decision problem? From the design of the current algorithms, they are mostly trajectory based and do not leverage the MDP structure.

=== **Experiments** ===

I am not an expert in symbolic regression so cannot comment on the significance of the improvements shown in the paper. The paper does seem to compare with a fair amount of baseline approaches, but I leave to the other reviewers to comment whether such baselines are reasonable.

RSEP-0 does appear to perform the best most of the time compared to other alternatives, but not uniformly, since Fig 5 does show cases where it is under performed. Do we have a sense as to when RSEP-0 underperforms the baseline methods?

For RL experiment, it is typical that the same experiments run multiple times in order to derive the standard deviations across random initializations and optimization. This is especially the case for policy gradient algorithms where variance tends to be high. In Fig 5 no such standard deviation curve is shown.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 5

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper studies the problem of symbolic optimization (SO)---which aims to search over sequences of tokens to optimize a black-box reward function---in real-world applications, where the assumption that an inexpensive reward function is available does not hold. The authors introduce Multi-Fidelity Markov Decision Processes (MF-MDPs) and propose a new family of multi-fidelity SO algorithms that account for multiple fidelities and their associated costs. Experiments demonstrate the proposed method outperforms baselines on various benchmarks.

### Strengths
1.	The idea of introducing Multi-Fidelity Markov Decision Processes (MF-MDPs) is interesting.
2.	Experiments demonstrate the proposed method outperforms baselines on various benchmarks.

### Weaknesses
1.	The idea of introducing Multi-Fidelity Markov Decision Processes (MF-MDPs) is interesting. However, the proposed method to solve the MF-MDP is primarily based on some simple sampling and weighting scheme. The authors may want to explain the novelty of the proposed method in detail. Specifically, the paper lacks a rigorous justification for the particular sampling and weighting strategy employed. It's unclear how this approach differs fundamentally from existing multi-fidelity methods in other domains, and the paper does not provide a clear theoretical analysis of its convergence properties or optimality guarantees under different conditions. A more detailed explanation of the algorithm's mechanics and its theoretical underpinnings is needed to fully assess its contribution.
2.	The generality of the proposed method is doubtful, as the proposed method and experiments are primarily based on problems with only two reward fidelities. The paper does not adequately address the challenges that arise when dealing with more than two fidelities. For instance, the method's performance and stability with a larger number of fidelity levels are not explored, and it's unclear how the sampling and weighting would be adapted to handle the increased complexity. The current experimental setup does not provide sufficient evidence to support the claim that the method can be generalized to scenarios with multiple reward fidelities.
3.	The authors may want to explain how to apply their method to problems with multiple (more than three) reward fidelities and transition fidelities in detail. The paper only briefly touches upon the possibility of extending the method to more than two reward fidelities, and it completely ignores the case of multiple transition fidelities. This lack of detail makes it difficult to understand how the method could be applied to more complex real-world problems where both reward and transition functions have multiple fidelity levels. A more thorough discussion of the method's adaptability to these scenarios is needed.
4.	The authors may want to evaluate their method in real-world complex problems with multiple (more than three) reward fidelities and transition fidelities. The experimental evaluation is limited to relatively simple problems and a single real-world application with only two reward fidelities. The paper lacks a comprehensive evaluation of the method's performance on more complex, real-world problems that involve multiple reward and transition fidelities. This lack of empirical evidence makes it difficult to assess the method's practical applicability and its potential to address the challenges posed by complex multi-fidelity problems.

### Questions
Please refer to Weaknesses for my questions.

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair
