# FeedSign: Full-parameter Federated Fine-tuning of Large Models with Extremely Low Communication Overhead of One Bit

- Decision: Reject
- Avg Score: 5.25
- Scores: 5, 5, 5, 6

## Abstract
Federated fine-tuning (FFT) aims to fine-tune a pre-trained model with private data from distributed clients by exchanging models rather than data under the orchestration of a parameter server (PS). However, as large models are acing in almost every machine learning task, the communication overhead and memory demand are surging accordingly, hindering the practical deployment on consumer devices. To overcome the bottleneck forged by the growing communication overhead of federated learning and lower the high memory demand of large model fine-tuning, we propose FeedSign, an FFT algorithm where a client uploads its update model and downloads the global model of any size using exactly $1$ bit per step, while the memory demand is squeezed to the amount needed for inference. This is realized by utilizing zeroth-order (ZO) optimizers on large models and shared pseudo-random number generators (PRNG) across devices to split the gradient estimate from the clients to 1) a direction corresponding to a designated random seed and 2) a binary vote from the client indicating whether the seed-corresponding direction grants a local loss descent, which is the only information the clients should convey to the PS. We conduct theoretical analysis on FeedSign and show that it converges at an exponential rate $\mathcal{O}(e^{-t})$, where $t$ is the number of elapsed steps, the same rate as in first-order (FO) methods can attain in big $\mathcal{O}$ notation. Moreover, it is also found that FeedSign enjoys good robustness against data heterogeneity and Byzantine attacks. We conduct extensive experiments on models across different structures and sizes (11M to 13B) and found that the proposed method performs better or closely, depending on scenarios, compared to its ZO and FO counterparts albeit an orders-of-magnitude lower communication overhead. We also discuss some interesting advantages as byproducts guaranteed by the minimalistic design of FeedSign.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This work studies Federated fine-tuning (FFT) realized by utilizing zeroth-order (ZO) optimizers. By using shared pseudo-random number generators (PRNG) across devices, the authors suggest to compress the transmitted gradients using 1-bit; which is in turn robust, as a result of the associated low-influence per-client. A convergence analysis is provided, demonstrating exponential rate similarly to the first-order (FO) methods. An experimental stay and a discussion are further presented, where the latter extends the proposed algorithm into a differentially private one.

### Strengths
Quality & Clarity:
- The paper is well written and presented.
- The provided convergence analysis supports the validation of the presented algorithm. 
- The discussion section is comprehensive. 
- The reference to ZO-FedSGD is clear and easy- to-follow.

### Weaknesses
Originality & Significance:
- Compressed FL has been extensively studied in literature. Specifically, the idea of clients voting via 1-bit compression and shared source-of-randomness; its differentially private version; and its implied associated robustness due to the implicit low-influence of its clients; have all already been presented in: 1) Lang, Natalie, et al. "CPA: Compressed private aggregation for scalable federated learning over massive networks." ICASSP 2023-2023 IEEE International Conference on Acoustics, Speech and Signal Processing (ICASSP). IEEE, 2023, and in 2) Lang, Natalie, et al. "Compressed private aggregation for scalable and robust federated learning over massive networks." arXiv preprint arXiv:2308.00540 (2023).‏
- The setting of both works 1) and 2) is the conventional FL with FO optimization, rather than the less adopted FFT and ZO, respectively. While the shift to FFT and ZO is a change in optimization approach, it does not fundamentally alter the core challenge of compressed communication in FL, which is already addressed by the cited works. The core idea of using 1-bit compression with shared randomness for robustness is not novel in this context.
- Moreover, as reflect from Algorithm 1 and lines 46-47; FFT does not change the implementation and associated challenges of regular FL, having the latter not-restricted to models of a certain size. The paper does not convincingly demonstrate how the proposed method overcomes the limitations of existing FL methods, especially in the context of large models, given that the core algorithmic structure remains largely unchanged. The use of ZO optimization, while reducing computational cost, does not inherently solve the communication bottleneck that the proposed method aims to address, as the core idea of 1-bit compression is already explored in the context of FO optimization.

### Questions
1. In lines 85-87: "However, we show that the per-step uplink and downlink communication overhead can be further reduced to 1 bit per step regardless of model size with little performance loss but numerous surprising benefits...". According to you Algorithm 1, only your uplink communication is being compressed. Additionally, in "numerous surprising benefits" the use of "numerous" may be too exaggerating. 
2. In lines 187-188: "However, to the best of our knowledge, efforts toward communication efficiency, data heterogeneity, and Byzantine resilience on FL are separated, motivating this work.". How does you method supports data heterogeneity?
3. In line 227: "...perturb its model in the same direction." What do you mean by that?
4. In line: "FeedSign left the sampling of random seeds to the PS...". Is this left of sampling is unique to FeedSign or can also be implemented in ZO-FedSGD?
5. What is 'D' in eq. (16)?
6. In lines 315-318: "...the only means of damaging convergence of FFT due to the binary voting scheme in FeedSign is to always send a reversed sign to PS." Does sending a constant sign (regardless of the true value) is also a possibility?

### Soundness
3

### Presentation
3

### Contribution
1

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper proposes FeedSign and ZO-FedSGD as two methods to fine tune large models in an FL setting with communication efficiency. They utilize zeroth-order gradient estimation to also reduce the computational complexity in the edge devices. In the ZO-FedSGD method, each client samples a seed and computes the gradient estimator coefficient and shares the seed and the coefficient with the server (64 bits per round). In the FeedSign method, the seed is shared by the server to all clients, and clients compute their gradient estimator coefficient for that seed and send the sign of that estimator to the server (1 bit per round). In Theorem 1, they proved that the method converges with exponential rate O(e^{-t}). They evaluate the method's performance under different models and datasets for different tasks. Also the differential private version of FeedSign (DP-FeedSign) is proposed in theorem 2.

### Strengths
The paper introduces a novel approach to minimizing communication overhead in fine-tuning large models by communicating only one bit per round, regardless of model size, structure, or task. This method combines communication efficiency with the computational efficiency of a zeroth-order gradient estimator in each client, which reduces memory requirements by estimating gradients through inference rather than backpropagation. The methods for both ZO-FedSGD and FeedSign are detailed in Algorithm 1. For the FeedSign method, which employs a voting mechanism, robustness against Byzantine attacks is achieved.
The exponential convergence rate O(e^{-t}) is proved in Theorem 1, and a comprehensive set of experiments is provided for various model architectures (ResNet, ViT, RoBERTa, OPT) and scales (ranging from 11M to 13B parameters).
The paper addresses the critical challenge of communication in federated learning by reducing communication overhead to one bit per round for FeedSign and 64 bits for ZO-FedSGD. It also tackles computational limitations in edge devices through the use of a zeroth-order gradient estimator. The method scales effectively to very large models (up to 13B parameters) and offers additional benefits, such as enhanced parameter security and privacy guarantees as byproducts.

### Weaknesses
1- The ZO-FedSGD method is a distributed version of a zeroth-order algorithm, similar to MeZO, and is referenced in other forms in some citations within the paper. However, it does not appear to be the main contribution of the paper; instead, FeedSign is presented as the primary contribution, which is theoretically and practically distinct from previous work.

2- The assumption that FeedSign is unbiased is fundamentally inaccurate. In FeedSign, only the sign of $p$ is transmitted and aggregated, which would only yield unbiasedness if all $p$ values were uniformly $+1$ or $-1$. Since this is not the case, Lemma 1 holds only for ZO-FedSGD and does not apply to FeedSign. Consequently, it cannot be used in Theorem 1, and the proof of convergence for FeedSign in Theorem 1 should be revised.

3- In the experimental section, Table 1 shows instances where FeedSign or ZO-FedSGD achieve better accuracy than the centralized version, which seems improbable under the same scenario, as a decentralized version typically cannot surpass the accuracy of its centralized counterpart. If different scenarios were used for fine-tuning, this should be specified in the section, along with a rationale for selecting particular scenarios for the experiments.

### Questions
1- Your method clearly introduces bias in gradient estimation by using only signs. Have you analyzed how this bias affects the convergence compared to unbiased ZO-FedSGD? Why does FeedSign still work well despite being biased?
2- Is there any theoretical bound on the bias of the method?
3- Is there any theoretical prove for the convergence of the FeedSign considering its a biased estimation of the gradient?

### Soundness
1

### Presentation
2

### Contribution
3

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper introduces FeedSign, a federated fine-tuning framework that employs zeroth-order (ZO) optimizers and pseudo-random number generators, aiming to reduce communication overhead from 64 bits to 1 bit per communication round. While this technical innovation represents a noteworthy advancement in communication per round, the practical relevance of such a reduction remains debatable, particularly given the existing sufficiency of bandwidth for 64 bits. Furthermore, FeedSign does not demonstrate a clear performance advantage over existing frameworks such as FwdLLM and FedKSeed, which undermines its overall contribution.

### Strengths
1 The motivation of this paper is well shown. 
2 Detailed proof is given.

### Weaknesses
1 Lack of convergence speed analysis. The paper lacks a comprehensive analysis of the convergence speed, which is critical as it seems to be the tradeoff between FeedSign and conventional methods (like FedAvg). Adding a direct comparison can better validate the proposed method.

2 Performance Comparison Deficits: Despite its lower communication cost, FeedSign does not surpass ZO-FedSGD in several performance metrics across different experiments. The marginal reduction of 63 bits in communication cost per round is not adequately justified as a significant advantage over the existing methods, especially when FeedSign does not exhibit faster convergence. This could result in an increased number of communication rounds, negating its low bandwidth benefits. Figure 2 underscores this issue, showing that ZO-FedSGD can achieve faster convergence speed.

3 Vague Claims of Superiority: The paper claims that FeedSign offers “numerous surprising benefits” over its predecessors. However, these benefits are not well-defined or substantiated beyond the reduced communication requirement, making these claims appear overstated. The advantages over the frameworks in [1], [2], and [3] are ambiguously presented and lack clear support. The contribution should be strengthened.

4 Limited Client Participation: The experimental setup with only five participating clients raises questions about the scalability and generalizability of FeedSign. Testing with a larger client pool could provide more robust insights into the framework’s performance across diverse federated environments.

### Questions
See Weakness.

### Soundness
3

### Presentation
2

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
This paper presents FeedSign, a federated fine-tuning (FFT) method that significantly reduces communication overhead for large models, requiring just one bit per step. Unlike conventional FFT, which demands high memory and communication, FeedSign uses zeroth-order optimization and a shared random generator to let clients signal only a binary vote indicating local model improvement. This keeps memory demands low and is compatible with a range of device constraints. FeedSign converges at rates similar to first-order methods and is robust against data heterogeneity and Byzantine attacks, performing on par with or better than other FFT methods across model sizes up to 13 billion parameters.

### Strengths
* Strong experimental results: the considered experimental setups are diverse and feature strong baselines, and the results of the proposed methods seem to be on par or better than the considered baselines. 
* The idea of communication one bit of information is quite simple and could be used in practice.

### Weaknesses
 * **Byzantine Resilience.** The paper could explore a broader range of Byzantine attacks and defenses, since “Byzantine resilience” refers to the ability of tolerating arbitrary corruptions. While robustness to basic Byzantine failures (Section 4.3) is a positive outcome, the method’s effectiveness against specific attacks (e.g., label flipping, gradient noise injection) is unclear. For instance, Allouah et al. (2023) explored representative defenses and attacks that might be relevant here, and integrating or testing such techniques could enhance FeedSign’s security profile. The current evaluation only considers a scenario where Byzantine clients send random bits, which is a very limited form of attack. More sophisticated attacks, such as those that strategically manipulate the sign bit based on local data or model state, should be considered to thoroughly assess the method's robustness. Furthermore, the paper does not discuss the potential impact of coordinated Byzantine attacks, where multiple malicious clients collude to disrupt the learning process. 

* **Novelty Consideration.** Although FeedSign introduces an efficient mechanism for communication reduction, the reliance on sign-based updates and zeroth-order optimization is not entirely novel. Techniques like sign-SGD have been previously studied for Byzantine-resilient federated learning (Li et al. 2019), and zeroth-order methods are known in federated contexts. While FeedSign’s combination of these ideas is compelling, the novelty could be highlighted more by contrasting its specific contributions with these prior works in-depth. The paper should explicitly differentiate its approach from existing sign-based methods, particularly in how it applies the one-bit communication strategy to the entire gradient update rather than individual gradient components. The novelty argument would be strengthened by a more detailed comparison with these existing techniques, highlighting the unique aspects of FeedSign's approach and its advantages.

* **Practical Relevance of Assumptions.** Assumption 2, in particular, appears to impose conditions that may not align with realistic settings. Further analysis or empirical evaluation showing how sensitive FeedSign’s performance is to deviations from this assumption would clarify the applicability of the theoretical results. The assumption that the Hessian matrix has a low effective rank is not always valid in practical scenarios, especially with complex models and non-convex loss landscapes. The paper needs to provide more justification for this assumption, possibly through empirical evidence or theoretical arguments that demonstrate its applicability in the context of federated fine-tuning. It is also important to discuss the potential impact of violating this assumption on the convergence and performance of FeedSign.

### Questions
1. Could the authors clarify how FeedSign would handle more advanced Byzantine attack scenarios beyond "random" faults? Are there defenses that could be integrated into FeedSign to enhance robustness without substantially increasing communication costs?

2. The reliance on Assumption 2 for theoretical guarantees may limit FeedSign’s applicability in real-world data distributions. Could the authors provide empirical insights or adjustments to make this assumption more practical?

3. Since FeedSign’s communication relies on PRNG and zeroth-order methods, do these choices introduce any potential issues with reproducibility or variance in results across different clients, and if so, how might they be mitigated?

### Soundness
3

### Presentation
2

### Contribution
2
