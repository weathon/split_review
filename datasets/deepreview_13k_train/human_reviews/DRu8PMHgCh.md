# FedTrans: Client-Transparent Utility Estimation for Robust Federated Learning

- Decision: Accept
- Scores: 6, 6, 6

## Abstract
Federated Learning (FL) is an important privacy-preserving learning paradigm that plays an important role in the Intelligent Internet of Things. Training a global model in FL, however, is vulnerable to the noise in the heterogeneous data across the clients. In this paper, we introduce **FedTrans**, a novel client-transparent client utility estimation method designed to guide client selection for noisy scenarios, mitigating performance degradation problems. To estimate the client utility, we propose a Bayesian framework that models client utility and its relationships with the weight parameters and the performance of local models. We then introduce a variational inference algorithm to effectively infer client utility, given only a small amount of auxiliary data. Our evaluation demonstrates that leveraging FedTrans as a guide for client selection can lead to a better accuracy performance (up to 7.8\%), ensuring robustness in noisy scenarios.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper considers the problem of performance degradation caused by the presence of noisy clients in federated learning. In order to mitigate this degradation, the paper proposes a client selection policy based on  FedTrans, a Bayesian framework for client utility estimation. The paper constructs a probabilistic graphic model determining the relationship between the client utility, the round reputation matrix, the round informativeness, and some other parameters of the problem (e.g., clients models weights, discriminator model weights, and prior distributions parameters). The paper uses Variational Expectation Maximization to infer the parameters of this probabilistic graphical model. Finally, the paper conducts numerical experiments on FEMNIST and CIFAR-10 datasets with different types and levels of noise. The numerical experiments lead to the following conclusions: 1) FedTrans outperforms other methods. 2) Other methods cannot take advantage for small auxiliary dataset, as opposed to FedTrans. 3) Combining both the round-reputation matrix and the discriminator model is crucial for FedTrans to achieve good performance. 4) The performance of FedTrans is robust to variation in the size of the auxiliary dataset, however, the performance drops if the auxiliary dataset is scarce.

### Strengths
- The paper effectively motivates the problem of performance degradation under the presence of noisy clients. 
- The paper clearly justifies the feasibility of accessing an auxiliary dataset.  
- The definition of the probabilistic graphical model, and the execution of Variational EM are overall correct. 
- The proposed method does not require the clients to perform any additional computation. 
- The numerical experiments, although being restricted to only two datasets, are fair, and evaluate all the important aspects of the proposed approach.

### Weaknesses
 - The paper relies on the availability of an auxiliary public dataset at the server.
- The clarity of the probabilistic graphical model explanation is lacking, and the rationale behind the modeling choices is not consistently elaborated upon.
    -  It is unclear what "the top-layer" means. Specifically, it's not clear which layer is being referred to, and what makes it the most discriminative for utility inference.
    - $x_j$ is obtained using $W_{i, j}$.  It raises the question of why the paper opts not to employ $x_{i, j}$ instead, which would explicitly denote the round-dependent nature of the client's model weights.
    - Further clarification is needed to justify (5). The connection between the round informativeness and the observed entries in the round reputation matrix is not clearly established.
- I am surprised by the drop of DivFL and FedCorr after the fine-tuning. My guess is that the fine-tuning employed a large learning rate, or a large number of epochs.
- Figure 6 highlights a limitation of the proposed method: relying solely on the round-reputation or the discriminator model results in inferior performance compared to alternative methods. It is plausible that the superior performance of FedTrans stems from its stacking of two learning methods, rather than an inherent advantage in its approach to client utility estimation.
- The evaluation criteria is unclear. Are the reported results evaluated only on "good" (i.e., mot noisy) clients, or on all the clients. It is important to clarify if the reported accuracy is on the clean clients, or if the noisy clients are included in the evaluation.
- Similar to most robust federated learning approaches, FedTrans might raise fairness concerns, as it may eliminate benign clients from the training if their local data distribution is very different from the majority of clients. The paper does not address the potential for the method to unfairly exclude clients with diverse data characteristics.
- Other minor issues:
    - The conclusions of Figure 1 might be due to a poor choice of the learning rate. It is important to verify that the conclusions are robust to different learning rates.
    - I am not sure that Figure 1 brings any significant value to the paper. My understanding is that the main conclusion obtained from Figure is that it is important to select reliable clients for training the global model. This conclusion is obvious.
    - In the first sentence in Section 1; lives -> live.
    - what is the meaning of "without loss of generality" in Section 1. Does it mean that the same results hold if we vary the flip rate? The statement is vague and needs further clarification.
    - As opposed to the paper claim, I think that the calibration/computation of the weights $p_j$ in (1) is crucial. Please, note that $p_j$ in (1) is different from $p_j$ used in Appendix B. The paper seems to downplay the importance of these weights, which are critical for the aggregation process.
    - I think that $\Theta$ is missing in the probabilistic graphical model depicted in Figure 3. The absence of the global model parameters in the graphical model is a significant oversight.

### Questions
- Could you, please, discuss the fairness implication of FedTrans? 
- Could you, please, clarify if the evaluation r2eports the performance of benign clients only, or includes the performance of noisy clients?
- Could you, please, report the success rate of FedTrans in detecting the noisy clients?

### Soundness
3 good

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
In this paper, the authors propose a novel Bayesian method designed to achieve robust aggregation on the server side within the framework of federated learning, effectively addressing the challenges posed by heterogeneous and noisy data. Central to this methodology is the use of a small yet pristine and balanced dataset, which resides on the server side and plays a crucial role in approximating the utility of each client. The experiment results validate the efficacy of the proposed approach, showcasing its potential practical benefits.

### Strengths
1. The paper addresses a significant issue in the federated learning (FL) environment, presenting a clear and well-founded motivation.
 
2. The clarity and simplicity of the writing style make the content accessible and easy to understand.

### Weaknesses
1. The novelty of this paper appears somewhat limited. There have been extensive prior studies on federated learning focused on client utility. It would be beneficial if the author could provide further clarification regarding the unique contributions of this work.

2. The proposed method appears to have a high dependence on the server dataset, which significantly limits its potential use cases. This limitation substantially reduces the generality of the proposed method.

3. While the authors do provide a convergence analysis in the appendix, it lacks a proper derivation of the convergence rate. In comparison to random sampling, the theoretical advantages of the proposed method remain unknown.

4. The proposed method introduces additional computational overhead per round, which could potentially increase the time required for each round when compared to the baseline methods.

### Questions
See the weakness above.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
* This paper proposes a Bayesian framework to estimate the client utility on different levels of noisy data. 

* Two metrics, i.e., weight-based utility estimation, and performance-based utilization estimation are applied into the Bayesian framework. 
For the first metric, last-layer weights are trained on a server-owned clean auxiliary dataset/and the noisy dataset is provided as a label. For the second metric, the inference results over the selected model in the auxilliary dataset are used for labeling.

### Strengths
* The paper is very well-written and the motivation for proposing a utility estimation method is clear. 

* The addressed problem is important and addresses the pain in the deployment of federated learning.  

* The method looks technically solid, and the formulation/description is concise but rigorous, but I couldn't check their correctness because of a lack of background in the Bayesian framework.   

* The experiment is also comprehensive, which demonstrates the effectiveness of the utility estimation. Ablation study and analysis of different simulation settings are also provided.

### Weaknesses
 * The Bayesian inference part is difficult to read through for readers without related knowledge. The authors may want to  introduce the framework of EM updates in the Appendix for readers without such background,

* The authors may discuss and contrast their Bayesian-based solution and multi-arm bandit-based client selection framework,  (Lai et al,2021), (Huang et al,2020), (Xia et al,2020)， as both frameworks aim to balance exploration and exploitation by providing some label signal for the client selection process. The current discussion is limited to the high-level differences, but a more detailed analysis of the similarities and differences in terms of mathematical formulations and assumptions is needed. Specifically, the authors should address how their method handles the exploration-exploitation trade-off, which is a core component of multi-armed bandit approaches. It would also be beneficial to discuss the computational complexity of their Bayesian approach compared to the typically more lightweight multi-armed bandit methods.


* Minor: the margin of the headers of Section 4 and Section 5 are modified. It is suggested the authors obey the author's guidelines and keep the original format. 

### Questions
As I am not so familiar with the EM framework, I am wondering why the weight-based utility estimation is only involved in the M step, while the performance utilization estimation is involved in the E step. Is that because the performance-based utility label is binary?

It is shown on page 6 that Algorithm 1 is run in each round of the federated learning process. Will the discriminator weight be inherited from that obtained in the previous round? Will utility inference become more accurate when rounds in the federated learning process increase? If so, can the authors demonstrate how the utility curve evolves with the rounds go?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good
