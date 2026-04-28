# IGTO: Individual Global Transform Optimization for Multi-Agent Reinforcement Learning

- Decision: Reject
- Avg Score: 6.00
- Scores: 6, 5, 6, 5, 8

## Abstract
The rigorous equivalency of individual-global actions is accustomedly assumed for  Centralized Training with Decentralized Execution (CTDE) in Multi-Agent Reinforcement Learning (MARL), wherever Individual-Global-Max (IGM) or Individual-Global-Optimal (IGO) it is. To release the restriction, in this work, we pose an individual-global action-transformed condition, named individual-global-Transform-Optimal (IGTO), to permit inconsistent individual-global actions while guaranteeing the equivalency of their policy distributions. Conditioned by IGTO, accordingly, we design a Individual-Global Normalized Transformation (IGNT) rule, which could be seamlessly implanted into many existing CTDE-based algorithms. Theoretically, we prove that individual-global policies can converge to the optimum under this rule. Empirically, we integrate IGNT into Multi-agent Actor-Critic (named IGNT-MAC) as well as various MARL algorithms, then test on StarCraft Multi-Agent Challenge (SMAC) and Multi-Agent Particle Environment (MPE). Extensive experiments demonstrate that our method can achieve remarkable improvement over the existing MARL baselines.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposes an Individual-Global Normalized Transformation (IGNT) rule that maps a sample from a simple density i.e., Gaussian policy. In this way, the restriction of IGO is released and the global value function is able to represent complex situations. Experimental results show that the proposed method outperforms many state of the art baselines.

### Strengths
See questions

### Weaknesses
This paper provides a simple but powerful method to release the restriction of IGO. By mapping the action to a distribution, the global value network can perform much better than multiple baselines. Theoretical analysis is also sound and provides the guarantee of convergence. The paper is interesting and easy to follow. However, I still have some concerns:

1. The proposed method is similar to the normalization of actions, which is widely used in many methods as a trick to improve performance. What is the difference between the proposed method and the widely-used normalization?

2. In the paper, the soft objective function is adopted. It seems that the proposed method can also apply to the normal objective function. Could authors explain why they must be combined? Since there is no ablation study to show the performance without the soft objective function, it is hard to say why the performance improved.

typos: a Individual-Global Normalized Transformation (IGNT) rule that map ..... -> an .... that maps .....;

### Questions
This paper provides a simple but powerful method to release the restriction of IGO. By mapping the action to a distribution, the global value network can perform much better than multiple baselines. Theoretical analysis is also sound and provides the guarantee of convergence. The paper is interesting and easy to follow. However, I still have some concerns:

1. The proposed method is similar to the normalization of actions, which is widely used in many methods as a trick to improve performance. What is the difference between the proposed method and the widely-used normalization?

2. In the paper, the soft objective function is adopted. It seems that the proposed method can also apply to the normal objective function. Could authors explain why they must be combined? Since there is no ablation study to show the performance without the soft objective function, it is hard to say why the performance improved.


typos: a Individual-Global Normalized Transformation (IGNT) rule that map ..... -> an .... that maps .....;

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
The authors try to release the restriction that the optimal joint actions should
be consistent with the optimal individual behaviors. They propose the Individual-Global-Transform-Optimal condition, IGTO, which transforms the joint action via a bijection function. The authors claim that individual-global policies can converge to the optimum under this condition. The proposed method is easy to implement and can be integrated into many existing MARL methods seamlessly.

### Strengths
+ The paper is well-organized.
+ The experiments are extensive. IGNT achieves strong performance gains in many tasks compared with the backbone algorithm. The experiment settings and hyper-parameters are detailed. I think it is easy to reproduce the results.

### Weaknesses
First, is it really a restriction that the optimal joint actions should
be consistent with the optimal individual behaviors? I think it is a natural fact and can be satisfied in all environments. Can you propose a case (maybe matrix games) where the optimal joint action is inconsistent with the optimal individual actions, and perform experiments on it to show that your method can achieve the optimum as claimed?

The condition that is Jacobian determinant is 1 is derived by the change of variable formula. However, the formula requires that the Jacobian exists. In discrete action space, the function is not differentiable. Can you give us a numerical case with discrete action space to show the original actions, the transformed actions, the bijection function, and the Jacobian determinant? It would be helpful to understand your algorithm.

Moreover, without considering the Jacobian determinant, the function F is bijection. Does it really increase the representation abilities or release the restriction of individual actions? I cannot see the meaning of transforming the actions using a bijection function. Specifically, if the transformation is applied to the action probabilities, the Jacobian determinant condition becomes even more critical, as it directly impacts the probability density and the validity of the change of variable. The paper does not adequately address how the transformation interacts with the underlying probability distributions, and whether the bijection is still meaningful when applied to probability vectors rather than discrete actions themselves. Furthermore, the proof of Theorem 1 seems to assume a continuous action space, and it is unclear how it applies to the discrete action space, even when using a probability vector representation.

### Questions
See Weaknesses.

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
This paper presents an individual-global action-transformed condition named IGTO, which releases the IGM or IGO restriction. To achieve this, it designs a bijective function for each agent to convert actions and proves that the converted actions can converge to the optimal policy. This method can be seamlessly implanted into many CTDE-based algorithms.

### Strengths
1. This paper attempts to find a solution to the optimal action of multi-agent from a new perspective, which is interesting.

2. IGNT is suitable for discrete and continuous actions and can be used in many agent reinforcement learning methods.

### Weaknesses
1. The motivation of this work is not clearly presented. Why do we need transformed actions? What are the benefits brought by this new method? The paper does not adequately explain the limitations of existing methods that necessitate the introduction of transformed actions. Specifically, it is unclear what specific scenarios or agent behaviors are poorly handled by IGM or IGO, and how the proposed transformation addresses these issues. The paper should provide a more detailed explanation of the problem being solved and the advantages of the proposed approach over existing methods.

2. The experiments of this method are not convincing. More IGM methods such as QPLEX [ICLR 21], WQMIX [NeurIPS 21], ResQ [NeurIPS 22], etc. could be added to prove the effect of this work. The experimental evaluation lacks a comprehensive comparison with state-of-the-art IGM-based methods. The current experiments do not provide sufficient evidence to demonstrate the superiority of the proposed approach. It is necessary to include a broader range of baseline methods to establish the effectiveness of the proposed method.

3. This paper provides a proof of improvement for the policy-based method, however, the proof of the value decomposition method is not yet clear. The theoretical analysis is incomplete, as it only focuses on policy-based methods. The paper needs to provide a more rigorous theoretical justification for the application of the proposed method to value decomposition methods. The current analysis does not adequately address the challenges and complexities associated with value-based approaches.

### Questions
1.  IGM or IGO strictly requires the optimal joint actions to be consistent with the optimal individual behaviors, which may lead to unsatisfied performance in some complicated environments. Could you describe a scenario where the IGM or IGO conditions could lead to poor performance? 

2. A closely related work is missing. ResQ [1] is a decomposition-based MARL method which learn a value decomposition by using a nonlinear function. 

3. For the discrete or continuous action space of an agent, how to ensure that all actions converted by the bijective function f_i are valid, and they should include all actions in the raw action space. It is unclear to me how it ensures this condition.

4. In value-based decomposition MARL methods，Do $Q_{jt}^* (\tilde{u} |\tau)$ and $[Q_i^* ( \tilde{u}_i|\tau)]$ satisfy IGM condition ? Can the author provide the complete training procedure based on value decomposition such as QMIX.

References

[1] ResQ: A Residual Q Function-based Approach for Multi-Agent Reinforcement Learning Value Factorization, NeurIPS 2022

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper introduces a new condition called Individual-Global Transform-Optimal (IGTO) to allow inconsistent individual-global actions while ensuring the equivalency of their policy distributions in Multi-Agent Reinforcement Learning (MARL). The authors propose a rule called Individual-Global Normalized Transformation (IGNT) to satisfy the IGTO constraint and integrate it into existing MARL algorithms. Theoretical proofs show that individual-global policies can converge to the optimum under the IGNT rule. The authors demonstrate the proposed method effectiveness through experiments on StarCraft Multi-Agent Challenge (SMAC) and Multi-Agent Particle Environment (MPE).

### Strengths
- Proposes the Individual-Global Normalized Transformation (IGNT) rule, which can be seamlessly integrated into existing MARL algorithms, offering a practical solution to satisfy the IGTO condition

- Providing detailed explanations and proofs in the appendix, enhancing the transparency and reproducibility of the proposed approach

### Weaknesses
 - This work is less novelty, by adding the normalized transformation to FOP. The majority of the proofs are similar to FOP.
- IGNT is more suitable for policy-based methods. However, chosen baselines are almost value-based methods. Especially, MADDPG in MPE is ignored.
- Lack of motivation about why we need the normalized transformation, especially if the transformation is invertible. 
- Lack of ablation about the chosen transformation function. For example, an Identity matrix, which $|G_i| = 1$ can be chosen, so that after transformation, actions are the same.

### Questions
- Could you provide an example of the normalized transformation? Especially, since the action is discrete in SMAC, u_i is an index of one action.
- It is unclear to me about how to adapt IGNT to value-based decomposition MARL methods, e.g., QMIX. If incorporating individual policy networks and target policy networks for each agent into QMIX, the ablation study should include such modifications.
- Why FOP cannot learn well in 3s_vs_5z? FOP can reach around 70% win-rate in their original paper in MMM2.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 5

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper introduces the Individual-Global Transform-Optimal (IGTO) condition, allowing for inconsistent individual-global actions while ensuring equivalent policy distributions. The authors also develop the Individual-Global Normalized Transformation (IGNT) rule, which can be integrated into existing CTDE-based algorithms and helps achieve optimum convergence of individual-global policies. Extensive experiments demonstrate the effectiveness of the proposed method.

### Strengths
1.	This paper proposes the IGTO condition, which alleviates the limitations of the IGM condition.
2.	The paper presents a novel method for obtaining individual transformed policy improvement through global joint policy optimization in the centralized training procedure.
3.	The methods are designed with theoretical guarantees, and the experiments provide evidence of their effectiveness.

### Weaknesses
Overall, this is a good paper and I have not found significant weakness yet.
I would lean towards accepting this paper. Meanwhile, I will also pay attention to the opinions and discussions of other reviewers.

There are some typos such as Eq.14.
Some symbols in the definitions lack explanations, making it difficult to understand such as Eq.5.

### Questions
1.	IGTO is based on Theorem 1 where the transformation is performed sequentially. Whether the order will influence the final results?
2.	From Eq.13, the joint policy is restricted to some set of intractable policies. Whether this global operation may lead to the suboptimal results of individual policies.
3.	How the method will perform in more complex scenarios in SC2 such as corridor, 6h_vs_8z?

### Soundness
4 excellent

### Presentation
4 excellent

### Contribution
4 excellent
