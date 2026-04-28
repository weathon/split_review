# Communication-Efficient Federated Low-Rank Update Algorithm and its Connection to Implicit Regularization

- Decision: Reject
- Avg Score: 4.00
- Scores: 3, 5, 3, 5

## Abstract
\noindent
Federated Learning (FL) faces significant challenges related to communication efficiency and heterogeneity. To address these issues, we explore the potential of using low-rank updates. Our theoretical analysis reveals that client's loss exhibits a higher rank structure (gradients span higher rank subspace of Hessian) compared to the server's loss. Based on this insight, we hypothesize that constraining client-side optimization to a low-rank subspace could provide an implicit regularization effect. Consequently, we propose FedLoRU, a general low-rank update framework for federated learning. Our framework enforces low-rank client-side updates and accumulates these updates to form a higher-rank model. Additionally, variants of FedLoRU can adapt to environments with statistical and model heterogeneity by employing multiple or hierarchical low-rank updates. Experimental results demonstrate that FedLoRU performs comparably to full-rank algorithms and exhibits robustness to heterogeneous and large numbers of clients.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
The paper applies FedLoRU and its variants to impose the local update in a low-rank subspace to achieve implicit regularization.

### Strengths
FedLoRU uses successive low-rank updates for both pre-training and fine-tuning in federated learning and achieves good performance.

### Weaknesses
W1. The novelty is not justified sufficiently.

W2. More discussions and justifications regarding the stable rank metric are needed.

W3. The experiment setup and results are not convincing.

The theoretical analysis reveals a higher-rank nature of Hessian of a smaller dataset, but it may not be regarded as a conclusion for federated learning. The insight only reveals the high-rank nature of small datasets, and it can not conclude constraining to low rank would help to align client updates along major directions and facilitate better aggregation. Therefore the contribution of the theory is limited. Also as the algorithmic convergence wasn't established, the conclusion is not convincing without repeating your experiment to report the variance.

### Questions
Q1. The paper presents FedLoRU and its variants by applying low-rank updates in a federated learning setting. However, the novelty of this proposed method is limited. The idea of using low-rank updates in federated learning has been explored before, and the paper does not provide a compelling argument for why the proposed method outperforms existing approaches. 

Q2. While the paper utilizes the stable rank metric to analyze rank properties between local clients and the central server, the discussion around this metric is lacking. The claim that stable rank "serves as a continuous proxy for rank and is robust" is made without sufficient references or supporting literature. Additionally, more discussion is needed on how this concept is adapted from related fields, and why it is appropriate for the federated learning context.

Q3. Figure 2(a) is difficult to interpret. Both the datasets with 50 and 500 samples show a high stable rank at the 15th epoch, which is counterintuitive and requires further explanation. It would strengthen the paper if the authors could repeat the experiment multiple times and provide clearer insights to support the observed trends.

Q4. The experiment shown in Figure 2(b) does not convincingly support the authors' intuition without a more detailed description. A thorough explanation of the experimental setup and its relation to Theorem 3.2 would significantly improve the clarity and impact of the results.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
To address the issue of communication efficiency and heterogeneity in Federated Learning, this paper proposes the FedLoRU method. This general low-rank update framework enforces low-rank client-side updates and accumulates these updates to form a higher-rank model. The authors provide empirical results to demonstrate that FedLoRU performs better than other algorithms.

### Strengths
1. The proposed method is well-motivated, the paper investigates the rank properties of client and server losses, analytically showing that under stochastic sampling, the rank of the Hessian of the loss function increases with smaller sample sizes.
2. The empirical results show empirical evidence of the higher rank structure of client losses and demonstrate that restricting the rank of local updates aids in implicit regularization.

### Weaknesses
1. In the theorems that are presented, summarizing the main insights of these theorems may be needed since currently they are just written as long paragraphs.
2. In experiments, the least partial client participation ratio is set as 0.5. In more realistic settings, the participation ratio is lower with more clients.
3. The author should consider more baselines, which apply low-rank factorized update models, such as [1].
[1] Nam Hyeon-Woo, Moon Ye-Bin, Tae-Hyun Oh. FedPara: Low-rank Hadamard Product for Communication-Efficient Federated Learning. ICLR 2022.

### Questions
See in weaknesses.

### Soundness
2

### Presentation
2

### Contribution
3

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
This paper reveals that client loss in federated learning has a higher rank structure (in gradients and Hessian subspaces) than the server's loss. Based on this, they propose that restricting client optimization to a low-rank subspace could provide implicit regularization and then introduce FedLoRU, a framework that enforces low-rank updates on the client side and aggregates them into a higher-rank model. Finally, they add another low-rank module pair to adapt to environments with statistical and model heterogeneity.

### Strengths
This paper reveals that client loss in federated learning has a higher rank structure (in gradients and Hessian subspaces) than the server's loss.
 Based on this, they propose that restricting client optimization to a low-rank subspace could provide implicit regularization. They then introduce FedLoRU, a framework that enforces low-rank updates on the client side and aggregates them into a higher-rank model. Finally, they add another low-rank module pair to adapt to environments with statistical and model heterogeneity.

### Weaknesses
The novelty is limited, there is no close connectiong between the analysis and the algorithm. I think this algorithm is a federated version of ReLoRA if we consider on the non-personalized version, aggregating low-rank modules for higher rank training.

There is no theoretical analysis for the algorithm. It's fully heuristic. When we consider the personalized strategy this paper studied, I don't know what kind of solution will this algoritm converge to. Will the introduced L, U fully concel out the A, B modules and make this algorithm fully consider local loss? The author didn't provide the reasonability of their strategy.

According to my understanding, this algorithm is still a full parameter training algorithm as it initializes W every $\tau$ step. So the comparison to LoRA is unfair. On the other hand, there are numerous algorithms for conventional federated learning. If you want to highlight your algorithm's advantage, you should compare your algorithm with the conventional algorithm, rather than just beatting LoRA.

You can't accurately solve argmin_{A,B} f. This step is computation-heavy even if you use an \epsilon-approixition. This step is actually one step of full LoRA tuning.  Therefore, this algorithm is not suitable for LLM fine-tuning.

What I want to emphasize is that you need to do a series of LoRA, and then merge AB into W sequentially, which sacrifices the flexibility of LoRA. LoRA separating adapter and the frozen pre-trained model, which thus can be adapted to multiple tasks in parallel.  Concretely, for each task, LoRA only needs to store {A, B}. Your algorithm needs to store the parameters with the size of the full model. I think it is inefficient.

Overall, compared with the conventional algorithm, this paper lacks theoretical justification.  Compared with LoRA, this work sacrifices flexibility and extensibility.

### Questions
Please refer to the limitation.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper studies communication-efficient low-rank update framework for federated learning. 

It provides theoretical asymptotic analysis for the rank structures of the Hessian at server side and client side, which motivates the design of FedLoRU algorithm. Generalizations of FedLoRU under statistical and model heterogeneity, namely pFedLoRU and mFedLoRU, are also presented. Finally, the authors conduct experiments on computer vision pre-training and language model fine-tuning tasks to demonstrate the performance of FedLoRU and its generalizations.

### Strengths
* The paper provides rigorous theoretical analysis on the Hessian rank structures, establishing interesting asymptotic results within a mathematically general framework.
* The proposed algorithm achieves performance comparable or superior to other known methods in experiments, while significantly reducing the communication overhead by low-rank updates.
* The presentation of this paper is well-organized and the motivation and methodology are clear to follow.

### Weaknesses
 * Although the authors provide some Hessian rank structure analysis, the design of FedLoRU can be better supported from the theoretical side. For example, some convergence guarantees, since low-rank updates lead to loss of information compared to full-rank updates and may hurt the optimization. Specifically, it's unclear how the low-rank constraint affects the convergence rate and whether it introduces any bias in the optimization process. A more rigorous analysis of the trade-off between communication efficiency and convergence would be beneficial.
* The title mentions "its connection to implicit regularization", but I was not able to spot sufficient discussion on implicit regularization of FedLoRU; also please see a conceptual question below. The paper should more explicitly connect the low-rank update mechanism to the concept of implicit regularization, perhaps by showing how it biases the solution towards a simpler, more generalizable model. The current discussion lacks a clear explanation of this connection.
* The design of FedLoRU seems a straightforward extension to federated setting of existing methods for low-rank matrix accumulation such as ReLoRA [1]. The novelty of the approach in the context of federated learning needs to be more clearly articulated, beyond simply applying an existing low-rank update technique to a federated setting. A deeper discussion on the specific challenges and benefits of using low-rank updates in federated learning is needed.
* This is not a major weakness but more evaluations on LLM fine-tuning could be done, as most of the experiment details are devoted to computer vision tasks on small datasets. The paper would benefit from more extensive experiments on large language models, which are a key area of interest in federated learning. This would help to demonstrate the practical applicability and scalability of the proposed method.

### Questions
* The title mentions "its connection to implicit regularization". To my knowledge, implicit regularization refers to the phenomenon that optimizers without explicit regularization, such as SGD, prefer regularized solutions [1]. However, FedLoRU explicitly works in a specific rank-$r$ space. Could the authors please explain in what sense is FedLoRU connected to implicit regularization?
* The theory part analyzes the rank structures of *loss Hessians* at server and client side. At the same time, FedLoRU proposes to perform low-rank updates on the model's *weight matrices*. Could the authors please explain the connection between the rank structure of loss Hessians and weight matrices?

[1] Ziwei Ji and Matus Telgarsky. Gradient descent aligns the layers of deep linear networks. arXiv preprint arXiv:1810.02032, 2018.

### Soundness
2

### Presentation
3

### Contribution
2
