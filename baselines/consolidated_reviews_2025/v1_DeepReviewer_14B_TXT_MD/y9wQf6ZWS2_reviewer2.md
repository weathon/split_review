### Summary

This paper proposes a new Q-learning algorithm, called RegQ, that converges when linear function approximation is used. The stability is established using a recent analysis tool based on switching system models. Moreover, the authors experimentally show that RegQ converges in environments where Q-learning with linear function approximation has known to diverge.

### Soundness

3 good

### Presentation

3 good

### Contribution

2 fair

### Strengths

The paper is well written and the authors provide a new single time-scale Q-learning algorithm with linear function approximation. They also prove the convergence of the proposed algorithm based on the O.D.E approach together with the switching system model. The authors experimentally show that the proposed algorithm performs faster than other two timescale Q-learning algorithms in the selected environments.

### Weaknesses

#### Some Related Works


#### comment

The novelty of the paper is not high. The proposed algorithm is very similar to the algorithm in Diddigi et al., 2019, and the difference is that the former one applies the regularization to Q-function while the latter one applies the regularization to V-function. However, the authors do not discuss this similarity and do not show the difference in terms of performance. The paper lacks a thorough comparison to existing methods, particularly those employing similar regularization techniques. The experimental section is limited, with no comparison to other algorithms on the Mountain Car environment, which is a standard benchmark. The theoretical analysis, while present, does not offer significant new insights compared to existing convergence proofs for regularized reinforcement learning algorithms. The assumptions made, particularly Assumption 2.2, are quite restrictive and limit the applicability of the proposed method. The assumption of a positive state-action visit distribution is also a strong assumption that is not always realistic in practice.

### Suggestions

The authors should provide a more detailed comparison of their approach to existing methods, especially those that use regularization techniques. A thorough analysis of the differences between applying regularization to the Q-function versus the V-function is needed. This should include a theoretical discussion of the implications of each approach, as well as empirical evidence to support the claims. Specifically, the authors should investigate whether the proposed method offers any advantages over existing methods in terms of convergence speed, sample complexity, or robustness to hyperparameter settings. The experimental section should be expanded to include a wider range of environments and a comparison to other state-of-the-art algorithms. The Mountain Car environment, while simple, is a standard benchmark and should be included in the evaluation. The authors should also consider more complex environments to demonstrate the scalability of their approach. Furthermore, the authors should provide a more detailed analysis of the sensitivity of their algorithm to the choice of the regularization parameter. This should include both theoretical considerations and empirical results. The authors should also discuss the limitations of their approach and the potential for future work. 

The theoretical analysis could be strengthened by providing a more detailed explanation of the assumptions and their implications. The authors should discuss the limitations of Assumption 2.2 and explore potential ways to relax this assumption. The assumption of a positive state-action visit distribution is also a strong assumption that is not always realistic in practice. The authors should discuss the implications of this assumption and explore potential ways to address this limitation. The authors should also provide a more detailed explanation of the convergence proof and highlight the key differences between their approach and existing convergence proofs for regularized reinforcement learning algorithms. The authors should also discuss the limitations of their theoretical analysis and the potential for future work. 

Finally, the authors should clarify the practical implications of their work. While the theoretical analysis is important, it is also crucial to demonstrate the practical relevance of the proposed algorithm. The authors should discuss the potential applications of their approach and the challenges that need to be addressed to make it more practical. The authors should also provide a more detailed discussion of the computational complexity of their algorithm and compare it to other existing methods. The authors should also discuss the potential for future work, such as extending their approach to other types of function approximation or exploring the use of different regularization techniques.

### Questions

1. What is the novelty of the proposed algorithm compared to the existing works?
2. How does the proposed algorithm perform compared to other algorithms?
3. What are the limitations of the proposed algorithm and what are the potential directions for future research?

### Rating

3: reject, not good enough

### Confidence

4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

**********
