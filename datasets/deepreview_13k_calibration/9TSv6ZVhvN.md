# Improving Accelerated Federated Learning with Compression and Importance Sampling

- Decision: Reject
- Avg Score: 4.67
- Scores: 3, 8, 3

## Abstract
Federated Learning is a collaborative training framework that leverages heterogeneous data distributed across a vast number of clients. Since it is practically infeasible to request and process all clients during the aggregation step, partial participation must be supported. In this setting, the communication between the server and clients poses a major bottleneck. To reduce communication loads, there are two main approaches: compression and local steps. Recent work by~\citet{ProxSkip} introduced the new \algname{ProxSkip} method, which achieves an accelerated rate using the local steps technique. Follow-up works successfully combined local steps acceleration with partial participation \citep{grudzien2023can, condat2023tamuna} and gradient compression \citep{condat2022provably}. In this paper, we finally present a complete method for Federated Learning that incorporates all necessary ingredients: Local Training, Compression, and Partial Participation. We obtain state-of-the-art convergence guarantees in the considered setting. Moreover, we analyze the general sampling framework for partial participation and derive an importance sampling scheme, which leads to even better performance. We experimentally demonstrate the advantages of the proposed method in practice.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
Per the authors and reviewing the history of optimization methods on FL, this paper combines three techniques that help with the communication burden in FL rounds: Local training, Compression, and Partial Participation.

### Strengths
- The paper introduces different algorithmic and theoretical tools for the final solution. I.e., if FL was a setting targeting convex problems mostly, the fact that the paper presents and exploits dual spaces + new theoretical tools like AB Inequality is a plus.

### Weaknesses
 - From an optimization perspective, assuming the logistic regression as an experimental setting is ok, but this is a machine learning venue; it has been a norm to consider more difficult objectives to test the hypotheses. It is a weakness not to consider a setting similar to what most of the FL algorithms are tested in.

- Similarly to the experimental case, providing theory in the convex case, given that FL is mainly applied in nonconvex settings with neural networks, could be improved. While the reviewer appreciates that there is a continuation of works (from specific research groups) that aim to cover every possible problem setting (as summarized in Table 1 of the paper), the current work (theoretically and practically) cannot be readily appreciated (and put among other works) on nonconvex neural networks FL setting.

- I might have missed it, but the difference between this work (along with the accompanying difficulties in completing the algorithm and proof) and the 5GCS is not clear from the text. Table 1 claims that that work did not satisfy the CC column. However, how difficult was it to complete the CC column on top of the work of 5GCS? What were the challenges? What was the amount of additional difficulty in completing this work? Was it incremental or substantial?

- The paper does not explain why assumptions 2,3,4 should hold in practice and under which conditions. They are hard to digest and read like proof, enabling assumptions

Overall, This reads like rigorous work. Yet, this score is due to the lack of generalizability of the results to more FL settings, lack of experimental results on FL scenarios, and lack of proper description of (differences with) prior work.

### Questions
See above.

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper proposed a Federated learning framework that combines the state-of-art techniques in Federated learning. Thorough theoretical results upon smooth and strongly convex objectives are presented.

### Strengths
1. The paper gives an excellent review of existing techniques from different perspectives of FL. The motivation of the paper is well-presented.
2. The theoretical part looks sound and solid.

### Weaknesses
1. The work focuses only on strong convex and smooth cases. How does it perform (theoretically) in convex / non-convex cases?

2. The authors are encouraged to give more detailed comparisons to existing approaches on convergence and communication cost.

3. It will be interesting to see how well the proposed algorithms perform empirically.

### Questions
See weaknesses

### Soundness
4 excellent

### Presentation
4 excellent

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper studied the communication problem in the federated learning. The authors proposed a local training strategy which combine the communication compression and importance client sampling. The authors provided theoretical analysis to validate their proposed methods.

### Strengths
The authors introduced an innovative federated training method that integrates client importance sampling. Additionally, the paper offers a thorough and comprehensive theoretical analysis of their approach.

### Weaknesses
The paper appears to encompass a broad range of topics, making it challenging to follow. The theoretical analysis is primarily confined to strongly convex scenarios, which may not be applicable to intricate models such as deep neural networks (DNNs). Moreover, the simplicity of the numerical experiments detracts from their overall persuasiveness. I would suggest to reorganize the presentation and include more experiments.

In Algorithm 1&2 line 7, the local optimization problem is solved within K iterations. However, most optimization problems cannot be solved exactly within a limited number of iterations. The paper does not adequately address how the precision of the sub-problem solution affects the global convergence. The theoretical results should consider the impact of this approximation error on the overall convergence rate.

The paper claims that the proposed 5GCS-AB algorithm handles data heterogeneity through importance sampling (IS). However, the algorithm does not explicitly detail how IS is set up based on the specific characteristics of data heterogeneity. The connection between the heterogeneity of the data and the IS mechanism is not clearly established. The paper only considers the smoothness constant as the source of heterogeneity, neglecting other factors such as the heterogeneity in the data distribution itself, which can affect the location of the solution.

Assumption 2 is not sufficiently clear. While the authors claim it encompasses a broad range of sampling schemes, they do not provide concrete examples or a clear explanation of how to verify if a given sampling scheme satisfies this assumption. The paper needs to provide more examples and a more detailed explanation of how to achieve this assumption in practice.

The current study and analysis are limited to the strongly convex case. Most real-world problems, especially in the context of federated learning, are non-convex. This significantly limits the practical applicability and contribution of the paper.

### Questions
1. In Algorithm 1&2 line 7, what if we can not optimize the problem in K iteration? How would the optimization error on  Eq(4) or Eq(6)  affect the final convergence? Has this be considered in Theorem 4.1 or 5.1?

2. How will the client's data heterogeneity affect the convergence as well as the sampling mechanism?

3. The assumption 2 seems not to be very clear. Can you explain how to achieve it in the algorithm? 

4. The client sampling mechanism seems to be unclear. Is it informative? Which information is leveraged for the sampling? 

5. Could the results be extended to non-convex cases? I would suggest to both include analysis and experiment on non-convex learning problems.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair
