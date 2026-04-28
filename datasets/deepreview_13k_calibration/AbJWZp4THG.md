# Efficient Adaptive Federated Optimization

- Decision: Reject
- Avg Score: 5.00
- Scores: 8, 3, 3, 6

## Abstract
Adaptive optimization plays a pivotal role in federated learning, where simultaneous server and client-side adaptivity have been shown to be essential for maximizing its performance. However, the scalability of jointly adaptive systems is often constrained by limited resources in communication and memory. In this paper, we introduce a class of efficient adaptive algorithms, named $FedAda^2$, designed specifically for large-scale, cross-device federated environments. $FedAda^2$ optimizes communication efficiency by avoiding the transfer of preconditioners between the server and clients, while simultaneously utilizing memory-efficient adaptive optimizers on the client-side to reduce extra on-device memory cost. Theoretically, we demonstrate that $FedAda^2$ achieves the same convergence rates for general, non-convex objectives as its more resource-intensive counterparts that directly integrate joint adaptivity. Empirically, we showcase the benefits of joint adaptivity and the effectiveness of $FedAda^2$ on both image and text datasets.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
The paper proposes the algorithm FedAda^2 as a strategy for jointly training adaptive optimizers for both the client and server, but also saving on memory and communication costs via a modification in  standard client and server optimization. Usually the preconditioners for the adaptive optimizers are communicated between the clients and server (server aggregates a bunch of client preconditioner matrices, server sends them back). Under FedAda, the server does not send the preconditioners back to the client. Authors have determined that not sending the preconditioners to the client results in very little degradation of performance, but better memory costs and communication costs (don't need to store preconditioners on clients/no need to send them)/ The preconditioners are initialized on the client for local epochs. The authors provide convergence guarantees and demonstrate that their method is superior on CIFAR-100, DP-StackOverflow, and GLD-23K against FedAdaGrad, FedAvg, FedAdam, and other baselines.

### Strengths
-Writing is easily understandable and well cited

-Figures are relevant and well-explained.

-Strong related works and literature survey.

-Convergence is in $\mathcal{O}(1/\sqrt{T})$ which is respectable and requires non-aggressive assumptions. 

-Clear motivation behind the algorithm, and appears to be relatively novel. 

-Good results against baselines (the authors run the same type of experimental settings as [1])

[1] Reddi, S., Charles, Z., Zaheer, M., Garrett, Z., Rush, K., Konečný, J., ... & McMahan, H. B. (2020). Adaptive federated optimization. arXiv preprint arXiv:2003.00295.

### Weaknesses
 -Experimental results feel like there could be a little more, the authors run CIFAR-100, GLD-23-K, DP Stackoverflow (logistic regression), but their chief comparison [1] runs Stackoverflow NWP, Shakespeare, some EMNIST stuff (all classification tasks). I would be curious to see how FedAda^2 compares on these untested datasets.
.
-The authors mention several other adaptive federated optimization frameworks (MIME, FedOPT) that seem to be doing something similar, but no mention or comparison afterwards. The authors could expand and compare their results against these techniques. It is unclear if this work is a significant improvement in the wider landscape of adaptive federated optimization. 

- No empirical evidence or experiments for memory reductions (they use SM3 algorithm which demonstrates excellent performance in [2], and rely on their theoretical work to show it is an improved memory cost). I would personally like to see more concrete memory metrics.

### Questions
See weaknesses

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
The paper first discusses the importance of adaptive methods on the client side of Federated Learning in terms of heavy-tail. Then it proposes a method that does not require a communication Preconditioner and gives its convergence guarantee in the non-convex case. Experimentally it is shown that their method has a little saving on communication overhead.

### Strengths
1.The paper provides the importance of adaptive methods on the client side of the argument.

2.The paper provides the FedAda framework to avoid passing Preconditioner and use more memory-efficient adaptive methods on the client side and provides a proof of convergence.

### Weaknesses
1.The thesis is not well structured around the core contribution points **AVOID extra communication cost** and **REDUCE on-device memory** for discussion and experimentation, as shown below:

(1) What exactly is the main impact of Section 3 on the main contribution of the paper? Section 3 seems to only show that client-side adaptation is important and has little impact on the topic of the paper, please explain to Section 3 what specific impact or direct effect HEAVY-TAILED DISTRIBUTION has on the additional communication overhead and on-device memory? The connection between the heavy-tailed analysis and the proposed techniques for reducing communication and memory is not clearly established. It is unclear how the theoretical analysis of heavy-tailed gradients directly informs the design choices in the proposed method. The paper should clarify how the properties of heavy-tailed distributions necessitate the specific adaptive methods used, and how these methods lead to reduced communication and memory footprints.

(2) The theory is not analyzed around the core contribution points.Convergence analysis is necessary to some extent, but not very critical in terms of communication overhead and MEMORY. The paper uses SM3 to reduce the memory required in training, and should theoretically or experimentally analyze how much the communication overhead and memory can be reduced relative to other algorithms? The theoretical analysis focuses on convergence but lacks a detailed analysis of the communication and memory costs. While convergence is important, the paper's main contribution is framed around reducing communication and memory. The analysis should explicitly quantify the reduction in communication overhead and memory usage achieved by the proposed method compared to existing approaches, both theoretically and empirically. The paper should provide a clear theoretical analysis of the memory footprint of SM3 in the context of the proposed method, and compare it to other adaptive optimization techniques.

2. The paper doesn't seem to propose a substantial solution, what is the difference between this method and using the adaptive method directly on the client side if the preconditioner is not transmitted during the communication process? It appears that the adaptive optimization method is simply switched to save training memory overhead on the client side. Can the authors provide a theory to refute this? The paper does not clearly articulate the novelty of the proposed approach compared to simply using adaptive optimization methods on the client side without transmitting preconditioners. It is not clear what unique aspects of the proposed method contribute to the reduction of communication and memory costs beyond the basic idea of not transmitting preconditioners. The paper should provide a theoretical justification for why the proposed method is more effective than a naive implementation of adaptive optimization on the client side.

3. Does using an adaptive optimization update on the client side just drop faster, and what is the difference between using a simple SGD on the client side for more rounds of training? The paper does not adequately address the trade-offs between using adaptive optimization methods and simply using SGD with more training rounds. While adaptive methods might converge faster, the paper should provide an analysis of the communication and memory costs associated with both approaches. It should compare the performance of the proposed method with SGD, considering both convergence speed and final performance, and analyze the trade-offs between using adaptive methods versus more rounds of SGD in terms of communication costs and memory usage.

### Questions
Based on the weakness, I have following questions/suggestions.

1. How the heavy-tailed analysis motivates or informs the specific techniques you propose to reduce communication and memory usage.

2. Could you please  provide quantitative comparisons of communication overhead and memory usage between your method and baselines, either theoretically or through additional experiments.

3. Could you please clearly articulate the novelty of your approach compared to simply using adaptive methods on the client side without preconditioner transmission. Specifically, you can highlight any unique aspects of your method beyond just switching optimizers, and explain how these contribute to the overall goals of reducing communication and memory costs.

4. Could you please provide empirical comparisons between your method and SGD with more training rounds, focusing on both convergence speed and final performance, and give an analysis of the trade-offs between using adaptive methods versus more rounds of SGD in terms of communication costs and memory usage?

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper highlights the importance of adaptivity in the FL framework, and propose a FedAda2 paradigm to implement the advantages of both global and local adaptivity, reduce communication bits through Zero Local Preconditioner Initialization, while allowing local clients to use different adaptive optimizers. The author provides both theoretical analysis and empirical research to validate the effectiveness of the framework.

After the review, several issues remain, including conflicts in the assumptions made in the analysis, the relatively low technical contribution of the proposed methods, and the potential training divergence caused by naive aggregation. Additionally, the experimental results are not presented clearly, making it difficult to see the performance improvements of the framework in the chosen settings.

### Strengths
1. Discussing the advantages of adaptive methods in long-tailed data is very interesting, as it highlights why we should use adaptive learning rates in FL.

2. The paper is well organized, making the reading relatively easy.

### Weaknesses
1. Some statements in the introduction are inaccurate. For example, "To the very best of our knowledge, there are no known convergence results on joint adaptive federated optimization in the general convex or non-convex setting". Is the joint adaptive federated optimization a special setup? Based on the analysis of Reddi et al., most papers seem to provide convergence analysis in either convex or non-convex settings. I don’t understand what scenario this refers to, as there is no corresponding explanatory content in the context.

2. After proposing the gradient condition under the long-tailed data distribution in Definition 1, the authors later adopt the assumption of Lipschitz continuity to constrain the bounded gradient in subsequent proofs. These two assumptions seem to conflict with each other. The authors do not carefully address the inconsistency between the assumptions. This could lead to another issue: whether an function satisfying Lipschitz continuity would still experience divergence during training with long-tailed data? I believe this is important. The current version lacks discussions about their relationships, which fails to demonstrate the advantages and significance of local adaptivity.

3. Zero Local Preconditioner Initialization is proposed to save communication bits. However, previous works seem to have already achieved this without the need to additional communications. [1] has been pointed out that using local historical preconditioner can also achieve good convergence and performance in experiments. This approach does not require knowledge of the global preconditioner. If the proposed technique is merely intended to reduce communication, its contribution is insignificant.

4. [1] also mentions a critical issue: when using a local adaptive optimizer, performing adaptive learning rate based on the local preconditioner might lead to divergence. They provide an example to illustrate the issue of divergence, attributing the cause of the divergence to the inconsistency of the local preconditioner. It is worth noting that pure global adaptivity does not have this issue, as local nodes use simple SGD. However, since the FedAda2 method proposed in this paper introduces local adaptivity, computing a simple average at the global server may encounter divergence issues. Specifically, the calculation of $\Delta_t$ could potentially approach infinity in some bad case. This leads to the conclusion that the framework presented in this paper seems unreliable.

5. The experimental improvements appear to be minimal. I do not see any significant enhancement in accuracy reflected in the figures. Can authors provide the table comparison of the test accuracy? In certain results, the performance of FedAda2 seems even worse. In most cases, it overlaps with other baselines, making it difficult for me to accurately discern its experimental effectiveness.

### Questions
The discussion on long-tailed data of the paper is quite interesting. However, the latter part regarding the proposed solution and its explanatory analysis seems to have issues; for details, please refer to the weaknesses section. In the experimental part, it is challenging to differentiate the performance improvements of the proposed framework. Currently, the main issues include the feasibility and effectiveness of the proposed solution. The current solution may lead to divergence due to its naive aggregation approach, and the techniques aimed at saving communication in the analysis do not seem very significant.

### Soundness
1

### Presentation
3

### Contribution
1

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This work considers efficient adaptive optimization in FL and proposes FedAda2 to optimize communication efficiency and memory costs. The theoretical and empirical results demonstrate the benefits of FedAda2.

### Strengths
1) This work proposes the algorithm FedAda2 to avoid extra communication costs and reduce the memory cost on device.

2) This work provides comprehensive convergence analysis to show the importance of client adaptivity and also proves the convergence of FedAda2 for general non-convex function.

### Weaknesses
1) The appendix is missing, and it is hard to check the experimental setup and convergence analyses.

2) The theoretical analysis in Section 3 is mainly for online strongly-convex functions, which limits their contribution for most real-world applications. Specifically, the strong convexity assumption is quite restrictive and doesn't align with the non-convex nature of neural networks typically used in federated learning. This makes the theoretical results less relevant to the practical application of the proposed method.

3) The current manuscript lacks a clear, concise comparison of the communication costs and memory costs between FedAda2 and existing algorithms. A table summarizing these costs would significantly increase the readability and impact of the paper. Without this, it's difficult to quickly assess the practical benefits of FedAda2.

4) The baselines in experiments seem to be confusing; it is better to distinguish existing methods and FedAda2 with ablations. The current experimental setup does not clearly isolate the effects of the different components of FedAda2, making it hard to understand the contribution of each design choice.

### Questions
1) As the abstract mentioned that this algorithm is designed for large-scale, cross-device federated environments, I wonder what the number of clients in total and per round in the experiments are.

2) On DP stackoverflow task, FedAda2 achieves worse performance than Joint Adap. w/o Precond. Commu. What are comparisons between their (and also other baselines') memory costs?

### Soundness
3

### Presentation
2

### Contribution
3
