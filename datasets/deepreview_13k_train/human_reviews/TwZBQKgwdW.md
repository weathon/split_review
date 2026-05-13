# NTK-DFL: Enhancing Decentralized Federated Learning in Heterogeneous Settings via Neural Tangent Kernel

- Decision: Reject
- Scores: 5, 6, 5, 5

## Abstract
Decentralized federated learning (DFL) is a collaborative machine learning framework for training a model across participants without a central server or raw data exchange. DFL faces challenges due to statistical heterogeneity, as participants often possess different data distributions reflecting local environments and user behaviors. Recent work has shown that the neural tangent kernel (NTK) approach, when applied to federated learning in a centralized framework, can lead to
improved performance. The NTK-based update mechanism is more expressive than typical gradient descent methods, enabling more efficient convergence and better handling of data heterogeneity. We propose an approach leveraging the NTK to train client models in the decentralized setting, while introducing a synergy between NTK-based evolution and model averaging. This synergy exploits inter-model variance and improves both accuracy and convergence in heterogeneous settings. Our model averaging technique significantly enhances performance, boosting accuracy by at least 10\% compared to the mean local model accuracy. Empirical results demonstrate that~our approach consistently achieves higher accuracy than baselines in highly heterogeneous settings, where other approaches often underperform. Additionally, it reaches target performance in 4.6 times fewer communication rounds. We validate our approach across multiple datasets, network topologies, and heterogeneity settings to ensure robustness and generalizability.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper proposes a novel framework for decentralized federated learning (DFL) that leverages a Neural Tangent Kernel (NTK)-based update mechanism instead of typical gradient descent methods. Specifically, clients send labels and Jacobians to their neighbors, who then use tools from NTK to obtain the trained neural network instead of relying on gradient descent. The paper provides empirical results validating that this approach significantly outperforms previous baselines in highly heterogeneous settings, achieving 4.6 times fewer communication rounds.

### Strengths
- The idea of using the NTK paradigm for DFL without gradient descent is both interesting and novel.
- This paper contributes a practical algorithm for DFL.

### Weaknesses
 - The proposed method requires clients to share their respective Jacobians, true labels, and function evaluations with their neighbors. This seems to violate the privacy-preserving feature of FL. More discussion is needed.
- The experiments were only validated on simple datasets (MNIST, Fashion-MNIST, and EMNIST); it is necessary to test on more complex datasets, such as CIFAR-100.
- The notations could be improved to make the method and algorithm clearer.

### Questions
1. The derivative notation should be: $\boldsymbol{J}_{i, j}^{(k)} \equiv\big[\nabla _{\bar{w}_j} \boldsymbol{f} (\mathbf{X}_i; \overline{\boldsymbol{w}} _j^{(k)}) \big]^{\top} \Rightarrow$ 

$
\boldsymbol{J}_{i, j}^{(k)} \equiv\big[\nabla _{w} \boldsymbol{f}(\mathbf{X}_i ; \overline{\boldsymbol{w}}_j^{(k)})\big]^{\top}
$

2. The expression “A global or aggregated model may take the form $\boldsymbol{w}=\frac{1}{M} \sum _{i=1}^M N_i \boldsymbol{w}_i$” should be revised to: $\boldsymbol{w}=\frac{1}{N} \sum _{i=1}^M N_i \boldsymbol{w}_i$, where $N=\sum _{i=1}^M N_i.$

3. Consider simplifying the set of clients using the notation $\mathcal{C}=${$1,..i,..M$} instead of $\mathcal{C}=${$C_1,...C_M$}. This way, subsequent neighborhoods can be expressed as $\mathcal{N}_i^{(k)}= ${$ j \mid(i, j) \in E^{(k)}$ }, making later expressions more concise.



4. The true label $Y_i$ in Figure 1 does not match the definition $\mathbf{Y}_i$ in the main text.

5. Given the definition of the aggregated model as $\boldsymbol{w}=\frac{1}{N} \sum_{i=1}^M N_i \boldsymbol{w}_i$, Eq. (1) should be modified to:
   $
   \overline{\boldsymbol{w}}_i^{(k)}=\frac{1}{N_i+\sum _{j \in \mathcal{N}_i^{(k)}}N_j}(N_i\boldsymbol{w}_i^{(k)}+\sum _{j \in \mathcal{N}_i^{(k)}} N_j\boldsymbol{w}_j^{(k)}).
   $

6. It is currently unclear how NTK-DFL differs from the previous work by Yue et al. (2022); it seems to extend their work to decentralized FL. It would be helpful for the paper to add more discussion on the unique aspects of NTK-DFL in the context of DFL.

7. NTK-DFL requires each client to share local true labels, function evaluations, Jacobians, and other information with their neighbors. This appears to contradict the fundamental privacy-preserving features of FL. More discussion on privacy protection is recommended.

### Soundness
2

### Presentation
2

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper introduce Neural Tangent Kernal into Decentralized Federated Learning, method of which is called NTK-DFL. The corresponding framework, NTK-DFL weight evolving method, empirically works on 3 common vision datasets in federated learning literatures.

### Strengths
- Presentation is easy to read.
- Straightforward motivation and clear validation: NTK works well in Centralized FL; it's not used in Decentralized FL yet; a vanilla method NTK-DFL is proposed; it empirically works well.
- Experimental results about comparison and ablation seem good.

### Weaknesses
 - Privacy concerned. In the 3rd step of proposed framework NTK-DFL, ground truth label are exchanged among clients, which would lead to more serious bad impacts. This potention privacy leakage breaks the claim made in Line 45-48. More discussion about privacy preserving should be considered. Specifically, the direct sharing of labels exposes sensitive information and makes the system vulnerable to various attacks, such as membership inference attacks, where an adversary could determine if a particular data point was used in training. The paper needs to address how this direct sharing of labels can be mitigated, and what are the implications of this for the privacy of the clients' data.
- Additional overhead. centralized federated learning system do have a heavy bandwidth issue on the path from clients to the server. However, the additional ones in NTK-DFL exchanged on the entire network system is far larger than that of centralized federated learning system. Further analyses on network overhead should be involved and make the paper more solid. The paper should provide a more detailed analysis of the communication overhead, including the size of the Jacobian matrices being exchanged, and how this scales with the number of clients, the size of the model, and the dimensionality of the input data. It should also consider the impact of this overhead on the overall training time and resource consumption.
- The content and the main claim are supported by the experiment. However, more experiments will be considered for higher rating. More detailed ablation study, analyses on overhead through the whole DFL system and NTK on other network topologies and protocols (e.g., multi-server) are recommended. The current experiments do not fully explore the parameter space of the proposed method. For example, the impact of different levels of data heterogeneity, the effect of varying the number of neighbors, and the performance of the method on more complex datasets should be investigated. Additionally, the paper should provide a more thorough analysis of the convergence behavior of the method under different conditions.

### Questions
- How to prevent privacy data leakage in NTK-DFL's 3rd step? Is there any technique to enhance this? For example more discussion on differential privacy.
- What's the comparison to other methods about network overhead? Is there a comparison of total bytes transferred per round for NTK-DFL v.s. centralized approaches, or an analysis of how the overhead scales with number of clients and model size.
-  How about other network topologies and protocols in DFL?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This work proposes an approach leveraging the NTK to train client models in the decentralized setting while introducing a synergy between NTK-based evolution and model averaging. It exploits intermodel variance and improves both accuracy and convergence in heterogeneous settings. The empirical results show the proposed approach consistently achieves higher accuracy than baselines in highly heterogeneous settings and reaches target performance in fewer communication rounds with multiple datasets, network topologies, and heterogeneity settings.

### Strengths
1.The experiments demonstrate that the proposed method is useful.
2.The study with NTK approach on decentralized FL is meaningful.

### Weaknesses
1. A significant concern revolves around the novelty of the proposed method. It seems that the proposed method may appear to be an extension of NTK from FL to DFL with some effective trick methods. It is essential for the authors to underscore their distinctive contributions in a more prominent manner. Specifically, the paper lacks a clear explanation of how the proposed approach fundamentally differs from existing NTK-based federated learning methods, beyond simply applying it in a decentralized setting. The core algorithmic differences and the specific challenges addressed by the proposed method in the decentralized context are not sufficiently highlighted.
2. In terms of experimental baselines, it is recommended that the authors include the most recent decentralized federated learning method (DFedSAM (Shi et al. (2023)) for a comprehensive comparison. This will enhance the paper's completeness and relevance in the context of the current state of the field. The absence of a comparison against a state-of-the-art decentralized method makes it difficult to assess the true performance gains of the proposed approach. The paper should also clarify why other decentralized methods were not considered.
3.The analysis in line 310-325 “Gains Due to Final Model Aggregation” is not clear enough. Where is the 10% in line 318 and 15% in line 321? The paper needs to explicitly reference the figures where these values can be observed. The current description lacks sufficient detail, making it hard to verify the claims made about the performance gains from model aggregation. The analysis should also explain why these gains are observed and what factors contribute to them.

### Questions
1.See the weakness above.

### Soundness
3

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
The paper proposes to leverage the Neural Tangent Kernel (NTK) to guide decentralized federated learning. More specifically, in each communication round, clients send their weights to neighbors and ask neighbors to calculate the Jacobian on neighbors' datasets. Then, clients receive the Jacobian from neighbors, and construct the empirical NTK matrix with the data from all neighbors. Next, each client updates the weights with reconstructed NTK. The proposed method NTK-DFL is shown to outperform standard DFL algorithms on heterogeneous datasets.

### Strengths
The paper is motivated by an important problem in decentralized federated learning: heterogeneity. The idea to reconstruct empirical NTK from neighbors is novel and interesting. Experiments also show great potential of the NTK-DFL in tacking heterogeneous datasets.

### Weaknesses
 - My major concern is the communication overhead of NTK-DFL. Conventional decentralized gradient descent only communicates gradients with neighbors, so the communication cost is $O(d)$. However, NTK-DFL needs to communicate Jacobian with the cost of $O(N_i\times d)$, where $N_i$ is the number of data in one client. This approach does not seem scalable to big datasets. Authors mentioned Jacobian batching in line 216. It would be interesting to see the trade-off between communication cost and performance for different batch sizes.

- The presentation of weight evolution can be made clearer. It seems negative signs are missing in the exponents in (4).



### Questions
- How are implement (4) and (5) implemented in practice? To exactly calculate the exponential map, eigen-decomposition on $\tilde{N}_i\times\tilde{N}_i$ matrix $H$ is needed. It would be better to explicitly present the implementation in practice.

- Can authors also present the communication cost in terms of bits rather than communication rounds?

- Can the method scale to larger scale problems like TinyImagenet?

### Soundness
2

### Presentation
2

### Contribution
3
