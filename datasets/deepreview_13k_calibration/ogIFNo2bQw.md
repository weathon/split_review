# BiCompFL: Stochastic Federated Learning with Bi-Directional Compression

- Decision: Reject
- Avg Score: 4.80
- Scores: 5, 5, 3, 6, 5

## Abstract
Communication is a prominent bottleneck in federated learning (FL). State-of-the-art accuracy performance under limited uplink communications from the clients to the federator is achieved by stochastic FL approaches. It has been recently shown that leveraging side information in the form of a prior distribution at the federator can drastically reduce the uplink communication cost in stochastic FL. Here, the latest global model distribution serves as a natural prior since it can be shared with the clients under ideal downlink communication from the federator to the clients. Nevertheless, downlink communication is often limited in practical settings, and bi-directional compression must be considered to reduce the overall communication cost. The extension of existing stochastic FL solutions to bi-directional compression is non-trivial due to the lack of a globally shared common prior distribution at each iteration. In this paper, we propose BiCompFL, which employs importance sampling to send samples from the updated local models in the uplink, and the aggregated global model in the downlink by carefully choosing common prior distributions as side-information. We theoretically study the communication cost by a new analysis of importance sampling that refines known results, and exposes the interplay between uplink and downlink communication costs. We also show through numerical experiments that BiCompFL enables multi-fold savings in communication cost compared to the state-of-the-art.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This work is about communication-efficient FL that leverages side information to transmit samples from the desired distribution through importance sampling. Unlike in most FL works, this paper assumes that downlink communication is also bandwidth-constrained. Convergence analysis is given and experimental results on accuracy versus total bits required validate the method.

### Strengths
The results are strong and practical merits are high.

### Weaknesses
In a nutshell, the proposed idea is to bring in a bidirectional element to FedPM of Isik et al. 2023. Probabilistic mask training, synchronized randomness and importance sampling are all from the existing work of Isik et al. 2023 and 2024. The only significant new element seems to be the introduction of downlink cost (as described by the n_DL dependent term in the first equation of section 5) in the analysis and performance evaluation. Thus, overall novelty is not high. 

Also, the authors would be overestimating the downlink communication cost in wireless scenarios since downlink is achieved by broadcasting and the effective bandwidth requirement should be reduced by the factor n. In this case, the effect of including downlink cost would be marginal, questioning the relative merits of the proposed approach.

### Questions
About the total communication cost in bits per parameter in Fig. 1, how is the uplink/downlink cost combined? As said above, does the overall cost reflect the difference in the bandwidth requirement for broadcasting vs separate one-to-one links?

Maximum accuracy is higher with the compressed schemes than FedAvg in Fig. 2? How is this so?

I would like to hear authors' response to novelty issue raised above.

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
This paper proposes2 algorithms for bi-directional version of the work of ISIK et. al.  The first algorithm assumes that globally shared randomness is available, and the second is for the case when only a private random key between each client and the central federator is available. The authors provide experiments showing improvements in the communication bandwidth for the same performance. Some analysis is also provided.

### Strengths
The improvements in the communication bandwidth, for the same performance and theoretical analysis.

### Weaknesses
Modification of Isik et. al which by itself is more of a narrow problem in Federated learning. There exists lots of proposals in this direction, so the paper while novel is not highly original. For instance, the paper by Philippenko et. al, Avdiukhin et. al, etc. This paper results are good, but I am not sure if it is good enough for a competitive venue like ICLR.

What is the justification for |q_j - p_j| being uniformly bounded? It does not seem like a mild assumption to me.

### Questions
What is the justification for |q_j - p_j| being uniformly bounded? It does not seem like a mild assumption to me.

### Soundness
4

### Presentation
4

### Contribution
3

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
The paper discusses bi-directional compression schemes in a federated learning framework assuming global and private common randomness in the model.

### Strengths
The attempt to study the shared randomness in a FL setting seems interesting.

### Weaknesses
The are some issues with the paper:

- An important issue is that, given this paper considers various schemes within a system model that includes shared common randomness, the performance of previous algorithms like FedAvg should also be re-evaluated under the assumption of shared randomness, with results reported in the paper for comparison. Specifically, it is unclear whether the improvement shown in Fig. 2 arises from the availability of shared randomness or from the algorithm itself. If the improvement is primarily due to the former, the comparison may not be entirely fair.

- Another important issue with the paper is that the results presented in Fig. 2 and Theorem 1 should account for the size of the common randomness. There is no discussion on whether this size is sufficiently large or if specific assumptions are being made about it.

- Section 3 primarily focuses on the mathematical details of the algorithm, with limited emphasis on the intuition behind it. To improve clarity, these mathematical details should be moved to the appendix, allowing this section to concentrate on explaining the intuition and comparing the algorithm with previous approaches.

### Questions
Can the authors refine the previous schemes' performances assuming the availability of shared randomness in the system model?

### Soundness
2

### Presentation
1

### Contribution
2

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The manuscript considers federated learning under uplink and downlink communication constraints. Several distributed learning strategies based on importance sampling are proposed. The strategies are designed under varying assumptions on the availability of shared common randomness between the server and clients. Theoretical guarantees are provided on the convergence rate of the sampled parameter distribution to that of the target distribution, as a function of the number of samples generated in uplink and downlink operations, which in turn determines the communication rate. Extensive empirical results are provided to compare the performance of the proposed strategies with existing federated learning methods, including those specifically designed for communication-constrained learning scenarios.

### Strengths
- The manuscript is well-written. There are few typographical errors if any, and the presentation is easy to follow.
- The topic is of interest to the community, communication constraints, especially in the uplink direction, are a significant roadblock in the implementation of federated learning mechanisms. 
- The application of importance sampling, and the several variations considered in the work, is novel in the context of federated learning to my knowledge.
- The theoretical analysis is sound and I have verified the proof steps to extent possible by the limited review time. 
- The literature review is comprehensive and covers many of the relevant works. 
- The empirical evaluations are comprehensive and provide performance comparisons with a range of existing methods in several different scenarios and benchmark datasets.

### Weaknesses
 - The computational and storage complexity of the proposed strategies should be evaluated and discussed. A main motivation of the work is the communication-constrained nature of many federate learning scenarios. For instance, in scenarios where clients comprise of mobile edge devices, uplink communication rate may be constrained. However, in such scenarios, the computation and storage complexity of the clients is also limited. As a result, in addition to communication cost, the computation and storage cost need to be considered. Specifically, the importance sampling operations, while reducing communication, might introduce a non-negligible computational overhead at the client side, which should be quantified and compared to existing methods.
- Note that a main motivation of federated learning is to avoid sharing the client's datasets with the server and with other clients due to privacy considerations. The proposed methods, especially Algorithm 2 which considers global randomness, require that the server share each of the client's updates with other clients. This may not be desirable due to privacy related considerations. The privacy implications of sharing client updates, even without explicit client identifiers, should be analyzed in more detail, considering potential information leakage about individual client data distributions.
- The experiments consider only 10 clients. It is not clear to the reviewer if some of the proposed methods would scale to larger numbers of clients. Specifically, in Algorithm 3, the clients have different estimates of the global model, since the exact model is not shared with the clients, and it is only estimated in the downlink using important sampling. This may cause the model to not converge when the number of clients is large. The heterogeneity in client model estimates, especially with a large number of clients, could lead to instability and divergence, which needs further investigation through theoretical analysis or experimental demonstrations with a larger client base.


### Questions
- Following the first comment in the weaknesses section, please clarify the storage cost and computational cost, compared to existing state-of-the art. 
- Following the third comment in the weaknesses section, please comment on the convergence of the model for larger number of clients. Theoretical guarantees or experimental demonstrations of convergence for larger numbers of clients would strengthen the results.  
- The empirical results show significant improvements in terms of total communication cost and communication cost per parameter for a fixed number of epochs. However, it is not clear if the prior methods converge at the same pace as the current method. That is, if the previous methods converge faster, then they may not need to be trained for the same number of epochs yielding a better communication cost. An experimental result showing the accuracy vs epoch curve of the proposed methods vs benchmarks would clarify this question. 
- The plots combine the uplink and downlink communication costs, however, these would not always be of similar importance in practice. Please comment on or provide experimental results on the UL and DL costs separately.
- In the plots for total communication cost per parameter, it is unclear whether the total is per epoch or over all training epochs. 
- Minor Comment: In line 824 on Page 16, the Bernoulli parameter $\frac{(L+1)(p+\eta_\delta)}{n_{IS}}$ could theoretically be greater than one, e.g, by taking $L=n_{IS}-1$, $n_{IS}$ small enoguh, and $\eta_{\delta}$ and $p$ large enough. It appears that there needs to be additional constraints on $n_{IS}$ and $p$ to avoid this.

### Soundness
4

### Presentation
4

### Contribution
4

---

## Human Reviewer 5

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper addresses a critical challenge in Federated Learning (FL) — the communication bottleneck that arises due to the extensive data exchange between clients and the federator. Specifically, the authors introduce **BICOMPFL**, a novel federated learning framework aimed at reducing communication costs in both uplink (clients to federator) and downlink (federator to clients) transmissions. BICOMPFL employs bi-directional stochastic compression by leveraging importance sampling and utilizing carefully chosen prior distributions as side information to transmit model updates efficiently. The framework presents two variants: **BICOMPFL-GR (Global Shared Randomness)**, which assumes a globally shared randomness source enabling synchronized sampling across all clients, and **BICOMPFL-PR (Private Shared Randomness)**, which operates with only private shared randomness between each client and the federator, addressing scenarios where global shared randomness is infeasible.

### Strengths
- While existing research predominantly concentrates on optimizing uplink communication in FL, this paper broadens the scope by simultaneously addressing both uplink and downlink communication bottlenecks. 
- Integrating bi-directional stochastic compression through importance sampling, showcases a creative combination of existing techniques tailored to a new problem formulation. Developing two distinct variants—**BICOMPFL-GR (Global Shared Randomness)** and **BICOMPFL-PR (Private Shared Randomness)**—demonstrates originality in catering to different practical scenarios.
- The paper extends and refines existing theories on importance sampling, particularly for Bernoulli distributions. 
- The paper provides a theoretical analysis of the proposed framework focusing on an upper bound on communication costs and the interplay between uplink and downlink efficiencies. 
- The introduction of adaptive block allocation strategies, including both fixed and adaptive average allocations, demonstrates a thoughtful approach to optimizing model parameter partitioning based on KL-divergence metrics.
- The authors conduct comprehensive numerical experiments across multiple datasets (MNIST, Fashion-MNIST, CIFAR-10) and neural network architectures (LeNet-5, 4CNN, 6CNN), showcasing the versatility and robustness of BICOMPFL.
- The empirical findings consistently demonstrate multi-fold reductions in communication costs compared to state-of-the-art FL methods, without compromising model accuracy.

### Weaknesses
 - The paper builds upon existing frameworks such as FedPM (Isik et al., 2023) and KLMS (Isik et al., 2024), integrating them into a bi-directional compression strategy. However, the novelty of combining these specific techniques with importance sampling and adaptive block allocation makes the technical novelty somehow limited.
- The theoretical analysis is limited to showing a bound on the cost of downlink transmission. The paper lacks a proper convergence analysis of the proposed algorithm as opposed to [1] and [2].

[1] Constantin Philippenko and Aymeric Dieuleveut. Bidirectional compression in heterogeneous settings for distributed or federated learning with partial participation: tight convergence guarantees. arXiv preprint arXiv:2006.14591, 2020.

[2] Constantin Philippenko and Aymeric Dieuleveut. Preserved central model for faster bidirectional compression in distributed settings. Advances in Neural Information Processing Systems, 34: 2387–2399, 2021.

- The empirical evaluation is confined to well-known datasets (MNIST, Fashion-MNIST, CIFAR-10) and relatively simple CNN architectures (LeNet-5, 4CNN, 6CNN). While these are standard benchmarks, they may not fully demonstrate the framework's effectiveness in more complex or large-scale real-world scenarios.
- While the paper mentions that global shared randomness does not incur additional communication costs, in practice, initializing and maintaining shared randomness (especially as the number of clients scales) may introduce hidden overheads.
- The theoretical results focus on Bernoulli distributions, which may limit the applicability of the analysis to more complex model parameter distributions encountered in practical deep learning models.
- The paper does not extensively explore how sensitive BICOMPFL is to various hyperparameters, such as the number of importance samples (nIS), block sizes (B), or the choice of priors (p).
- The proposed importance sampling and adaptive block allocation strategies may have implications for the energy consumption and computational load on client devices, which is particularly important in edge or mobile FL applications.

### Questions
-	Can the theoretical analysis be extended beyond Bernoulli distributions to more complex parameter distributions? 
-	Why are the authors not comparing their method to [1] and [2] in the simulation setting? Also, a similar convergence analysis to these references is missing from the paper.

[1] Constantin Philippenko and Aymeric Dieuleveut. Bidirectional compression in heterogeneous settings for distributed or federated learning with partial participation: tight convergence guarantees. arXiv preprint arXiv:2006.14591, 2020.

[2] Constantin Philippenko and Aymeric Dieuleveut. Preserved central model for faster bidirectional compression in distributed settings. Advances in Neural Information Processing Systems, 34: 2387–2399, 2021.

-	The current experiments are limited to MNIST, Fashion-MNIST, and CIFAR-10 with relatively simple CNN architectures. Consider evaluating BICOMPFL on larger and more diverse datasets, such as ImageNet, or involving more complex models like ResNet or Transformers. 
-	How feasible is the assumption of shared randomness in large-scale or decentralized FL environments? In practical deployments with numerous clients, maintaining global shared randomness can be challenging.
-	What are the computational and energy overheads associated with importance sampling and adaptive block allocation in BICOMPFL? Especially for clients with limited computational resources, these overheads could impact the feasibility of deployment.
-	How does BICOMPFL perform as the number of clients and the size of the model increase? The current number of clients is somehow very small.
-	How sensitive is BICOMPFL to the choice of hyperparameters, such as the number of importance samples (nIS), block sizes (B), and priors (p)?

### Soundness
3

### Presentation
3

### Contribution
2
