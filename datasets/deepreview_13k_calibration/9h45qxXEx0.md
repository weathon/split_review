# Debiasing Federated Learning with Correlated Client Participation

- Decision: Accept
- Avg Score: 6.75
- Scores: 8, 8, 6, 5

## Abstract
In cross-device federated learning (FL) with millions of mobile clients, only a small subset of clients participate in training in every communication round, and Federated Averaging (FedAvg) is the most popular algorithm in practice.  Existing analyses of FedAvg usually assume the participating clients are independently sampled in each round from a uniform distribution, which does not reflect real-world scenarios. This paper introduces a theoretical framework that models client participation in FL as a Markov chain to study optimization convergence when clients have non-uniform and correlated participation across rounds. 
We apply this framework to analyze a more general and practical pattern: every client must wait a minimum number of $R$ rounds (minimum separation) before re-participating. We theoretically prove and empirically observe that increasing minimum separation reduces the bias induced by intrinsic non-uniformity of client availability in cross-device FL systems. 
Furthermore, we develop an effective debiasing algorithm for FedAvg that provably converges to the unbiased optimal solution under arbitrary minimum separation and unknown client availability distribution.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper studied the federated learning problem with partial client participation. In particular, it focused on the case where there is minimum separate between clients in terms of minimum rounds. The authors formulated the client participation process as a R-th order Markov chain and characterize the marginal stationary distribution of clients to be sampled. The authors proposed a debiasing FedAvg based on the estimation of this marginal stationary distribution and provided the convergence analysis of the proposed algorithm as well as the original FedAvg algorithm. There are several very interesting observations of this paper. The performance of the proposed algorithm is also verified using simulations.

### Strengths
1. The authors formulates the client participation process as a R-th order Markov chain. 

2. The authors proposed the debiasing FedAvg algorithm based on the estimation of marginal stationary distribution of clients to be sampled. 

3. The authors provided the convergence analysis of both FedAvg (to indicate the problem) and the proposed algorithm which can converge.

### Weaknesses
1. The paper is not well written and there are some notations not explained, e.g., $\tau_{mix}$ (is it the mixing time?) and $p_e$, although the paper presented quite a few interesting ideas. Specifically, the definition of $\tau_{mix}$ is crucial for understanding the convergence rate, and it's not immediately clear how it relates to the Markov chain parameters. The lack of a clear definition early on makes it difficult to follow the theoretical arguments. Similarly, $p_e$ appears to be a client-specific probability, but its precise meaning and how it's derived from the Markov chain are not explicitly stated, leading to ambiguity in the algorithm's implementation and analysis.

2. The authors discussed quite a few limitations of the proposed approach and its proofs. These seem the weaknesses of the paper. For example, the reliance on a specific form of the Markov chain and the assumptions made for the convergence analysis (e.g., smoothness and strong convexity) may limit the applicability of the proposed method in more complex scenarios. The discussion of these limitations, while honest, highlights the need for further research to address these constraints.

### Questions
1. The algorithm is based on GD instead of SGD. If SGD was used, will there be any challenges?

2. I suggest the authors put the proof of Proposition 1 in the appendix.

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper proposes a theoretical framework that models client participation in FL as a Markov chain, enabling the study of optimization convergence when clients exhibit non-uniform and correlated participation across rounds. The authors find that FL algorithms converge with asymptotic bias, which can be mitigated by increasing the minimum separation $R$. Additionally, they propose a debiasing algorithm for FedAvg, providing both theoretical and empirical performance guarantees for this approach.

### Strengths
1. The authors introduce a theoretical framework that models client participation in FL as a Markov chain, allowing the study of optimization convergence when when each client must wait at least $R$ rounds before participating again and has its own availability probability.
2. Through both theoretical and empirical results, the authors find that due to non-uniformity and time correlation effects, FL algorithms converge with asymptotic bias, which can be reduced by increasing the minimum separation $R$. 
3. To achieve unbiased solutions, the authors propose a debiasing algorithm for FedAvg, with performance guarantees provided through both theoretical analysis and empirical evaluation.

### Weaknesses
1. The authors restrict the choices of $R$ to range from $0$ to $M-1$. However, the theoretical analysis only considers cases where $R$ ranges from $0$ to $M-2$. It would be beneficial to include the results for $R=M-1$. Specifically, the analysis relies on the Markov chain being aperiodic to guarantee a unique stationary distribution, and this condition is not met when $R=M-1$, leading to a potential gap in the theoretical framework's completeness. The absence of analysis for the $R=M-1$ case limits the applicability of the theoretical results.
2. In the experiments, the authors simplify the algorithm by partitioning the $N$ clients into $M$ groups, with exactly one group selected in each round. This setup does not align with the more complex proposed algorithm, which allows for any subset of clients to be sampled as long as the minimum separation constraint is met, and is insufficient for a comprehensive evaluation of its performance. The experimental setup simplifies the client selection process, potentially masking the effects of the proposed minimum separation constraint and limiting the generalizability of the empirical findings.
3. The experiments are only conducted on synthetic dataset and MNIST dataset, which is relatively simple. More complex datasets (e.g., CIFAR-100, Shakespeare) and tasks (e.g., NLP) are recommended for a more comprehensive evaluation of the proposed algorithm's performance. The limited diversity in datasets and tasks raises concerns about the robustness and general applicability of the proposed method, particularly in more challenging real-world scenarios.

### Questions
1. Theorem 2 holds only under specific requirements. What about more general settings that relax these requirements?
2. The authors claim that each client can maintain its own specific $R_i$. In this more general setting, Theorems 1 and 3 hold without modification, while Theorem 2 becomes more challenging. What modifications would be needed to obtain Theorem 2?

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
3

### Summary
This paper finds that traditional FL algorithms like FedAvg assume clients participate independently and uniformly, which is unrealistic in practical applications. It addresses the bias in FL due to non-uniform and time-correlated client participation. The authors introduce a Markov chain model to simulate the sequential and dependent nature of client participation, where each client waits a minimum number of rounds before participating again. A debiasing algorithm for FedAvg is proposed to improve convergence and ensure unbiased model updates. Empirical results also demonstrate that Debiasing FedAvg effectively reduces bias during training.

### Strengths
1. The authors find common FL assumption that clients participate independently and uniformly is unrealistic.
2. The paper frames client participation as a Markov process, capturing real-world constraints and interdependencies among clients.
3. The paper proposes Debiasing FedAvg converging to an unbiased solution with theoretical analysis.
4. Experiments on both synthetic and real datasets validate the algorithm’s effectiveness.

### Weaknesses
1. The paper claims that a larger minimum separation $R$ reduces bias. However, it lacks a discussion of how $R$ affects the server's model performance on the test set empirically and how to choose the best $R$. Specifically, while the paper focuses on reducing training bias, it does not adequately explore the trade-off between bias reduction and generalization performance. A larger $R$ might reduce bias in training but could also lead to slower convergence or poorer generalization if fewer clients are involved in each round, which is not discussed.
2. The paper assumes a uniform minimum separation for all clients, which may not reflect real-world situations. This assumption simplifies the analysis but might limit the applicability of the proposed method in scenarios where clients have varying participation patterns or resource constraints. For example, some clients might be more frequently available than others, and imposing a uniform minimum separation could be overly restrictive for those clients.

### Questions
1. If there is extreme heterogeneity among clients, how might a larger minimum separation $R$ impact the model's performance?

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
Existing federated learning algorithms assume clients are sampled uniformly at random at each iteration which does not reflect the real scenario. In this paper, the authors assume that each client requires a minimum separation of R rounds between sampling. Then they model client selection as a Markov chain to theoretically analyze the setting and propose a debiasing algorithm with provable guarantees.

### Strengths
- Motivation: the minimum separation in federated learning is reasonable to analyze.
- Literature review is thorough.

### Weaknesses
 - The FL setting is not rigorous. In line 121, authors use $p_i$ to capture the willingness to be sampled at each iteration which means a client may not join the training for arbitrarily long amount of iterations (with small probability). However, in line 128~129, it is claimed that "the cyclic participation corresponds to the case, R = N / B − 1", which means in the last round of the cycle, all of the remaining B clients will definitely be sampled. So the setting is not consistent. Besides, forcing clients to join cross-device federated learning is not practical.

- As has been mentioned in the "Limitations" section, the theoretical results do not enjoy linear scalability.

- I am not very convinced that Markov-chain Model is necessary to analyze the problem. The algorithm 1 essentially only try to estimate p_i and then inversely scale 1/pi to gradients in order to have uniform weight to all clients. 

- The presentation of the paper can be improved.

### Questions
Are Markov-chain model really necessary to analyze this problem?

### Soundness
2

### Presentation
2

### Contribution
2
