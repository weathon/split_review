# Mixture of Experts Made Personalized: Federated Prompt Learning for Vision-Language Models

- Decision: Accept
- Avg Score: 5.75
- Scores: 6, 5, 6, 6

## Abstract
Prompt learning for pre-trained Vision-Language Models (VLMs) like CLIP has demonstrated potent applicability across diverse downstream tasks.
This lightweight approach has quickly gained traction from federated learning (FL) researchers who seek to efficiently adapt VLMs to heterogeneous scenarios.
However, current federated prompt learning methods are habitually restricted to the traditional FL paradigm, where the participating clients are generally only allowed to download a single globally aggregated model from the server. While justifiable for training full-sized models under federated settings, in this work, we argue that this paradigm is ill-suited for lightweight prompts. By facilitating the clients to download multiple pre-aggregated prompts as fixed non-local experts, we propose \textbf{P}ersonalized \textbf{Fed}erated \textbf{M}ixture of \textbf{A}daptive \textbf{P}rompts (\ct{\textbf{pFedMoAP}}), a novel FL framework that personalizes the prompt learning process through the lens of Mixture of Experts (MoE). \ppp \ implements a local attention-based gating network that learns to generate enhanced text features for better alignment with local image data on the client, benefiting from both local and downloaded non-local adaptive prompt experts. The non-local experts are sparsely selected from a server-maintained pool, fostering collaborative learning across clients.% thanks to the prompt's lightweight property. 
To evaluate the proposed algorithm, we conduct extensive experiments across 9 datasets under various heterogeneous federated settings. The results show that \ppp \ consistently outperforms the state-of-the-art alternatives, underscoring its efficacy in personalizing prompt learning for CLIP within the federated learning paradigm.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
This paper introduces pFedMoAP that enables effective federated prompt learning for vision-language models like CLIP. The key innovation is allowing clients to download multiple pre-aggregated prompts as fixed non-local experts rather than being restricted to a single globally aggregated model.

### Strengths
1.	The method is novel which allows the client download prompts from others.
2.	The experiments are extensive and show good performance.

### Weaknesses
1.	It is very similar to the prompt learning framework. How does your method differ from the classic prompt learning framework if you can directly access prompts from other clients?
2.	I noticed that similar work, like pFedPrompt, conducted experiments on large-scale datasets like UCF-101 or ImageNet. Would the scale of the dataset influence the performance?

### Questions
Refer to the weakness part.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper proposes a lightweight federated prompt learning framework to personalize the prompt learning process through the lens of mixture of experts (MoE). An attention-based gating network is also introduced to achieve efficient cross-client knowledge sharing. Experiments indicate that the proposed **pFedMoAP** performs better than state-of-the-art methods.

### Strengths
1. Implementing prompt learning into the distributed environment is an important topic for FL applications due to its efficiency in computation and communication.

2. The proposed learning framework is simple and effective.

### Weaknesses
1. The quality of the writing is poor. The expression of the paper is somehow obscure, and not concise enough. Besides, there are many typos in the paper, e.g.,  lacking space between two adjacent words in Line 27, Line 198, Lin 415, and Line 469. 

2. The novelty is limited. The **pFedMoAP** seems like a naive combination of PromptFL and MoE. Although the selected non-local experts will be updated in each communication round, the intuition behind it is also not explained well, leading to weak convincingness. 

3. it is unclear why the attention-based gate network does not need to be uploaded to the server for aggregation. Please clarify.

4. I think the ablation study of the paper is not enough. 
- To study the effectiveness of MoE-based textual feature enhancement mechanism, the authors should add experiments under different values of $K$ to confirm performance changes.

- The author implements a dimension reduction operation in Section 3.3, please add experiments to show whether the performance will be influenced.   

- How about a larger number of clients, e.g., 100 or more?

### Questions
1. In Section 4.1 **Implementation details.**, for CIFAR10&CIFAR100, why the participation rate is 10%? Does it mean only one client will be selected to join the training process in each communication round?

### Soundness
2

### Presentation
1

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
This paper proposes a Mixture of Experts (MoE) approach for prompt-based federated learning, employing a local attention-based gating network to refine text features for better alignment with local image data. It also highlights the lightweight design of the prompt, exploring a configuration where the prompt is updated directly by other clients rather than relying on an aggregated prompt from the server.

### Strengths
1. The integration of the MoE method into prompt-based federated learning is an innovative concept.

2. The paper is well-organized and effectively communicates its main contributions. The methodology is clearly explained, particularly regarding the incorporation of the MoE approach in the federated learning context.

### Weaknesses
1. While this approach utilizes inter-client sharing, it could expose prompt updates directly to other clients, which may lead to privacy concerns as prompt updates could be tracked, making the model susceptible to certain attack algorithms. 

2. In the related work section in the appendix (Line 783), the authors mentioned that previous work utilized inter-client sharing prior to aggregation. However, these works allow prompt aggregation in the server and do not share local prompts with other clients. This sentence is somewhat unclear; please provide a clearer version to avoid misunderstandings. 

3. The paper claims that the MoE-based method can leverage prompts from other clients. Please provide experimental evidence to show whether your method’s effectiveness is sensitive to the total number of clients and the value of $K$. 

4. Some related works are encouraged to be properly cited in Related work. For example, personalized federated learning [a,b] and prompt-based federated Learning [c]. 

[a] Li, et al, FedTP: Federated Learning by Transformer Personalization, TNNLS 2023. 

[b] Cai, et al, Fed-CO2: Cooperation of Online and Offline Models for Severe Data Heterogeneity in Federated Learning, NeurIPS 2023. 

[c] Pan et al, Federated Learning from Vision-Language Foundation Models: Theoretical Analysis and Method, NeurIPS 2024.

### Questions
Please refer to the weakness.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This work introduces a new paradigm in federated prompt learning for pre-trained Vision-Language Models (VLMs) such as CLIP, challenging the traditional restriction that clients are limited to downloading a single globally aggregated model. This shift is particularly beneficial for lightweight prompts, enabling more flexible and effective knowledge sharing among clients.

### Strengths
1. pFedMoAP proposes a novel framework that personalizes the prompt learning process by allowing clients to download multiple pre-aggregated prompts as fixed non-local experts. This leverages the concept of Mixture of Experts, where a local attention-based gating network is implemented to generate enhanced text features that better align with the local image data on the client side.

2. By facilitating a many-expert scenario (e.g., 10 experts) per client with negligible communication overhead, pFedMoAP achieves efficient and effective personalization. This approach overcomes the limitations of having too many or too few experts, which can lead to high communication costs or suboptimal performance, respectively.

3. The algorithm consistently outperforms existing work across various heterogeneous federated settings, as demonstrated through extensive experiments on 9 datasets.

### Weaknesses
1. Determining which prompt experts should be included in the pool and when to update or replace them requires careful management. If the selection process is not optimal, it could lead to suboptimal performance. Additionally, maintaining a diverse and up-to-date pool of experts is crucial but can be complex. The paper lacks a detailed analysis of the sensitivity of performance to the expert pool composition. For example, how does the performance vary with the number of experts, the diversity of their training data, and the frequency of updates? Without this analysis, it is difficult to assess the robustness of the proposed method under different conditions.

2. The local attention-based gating network, while designed to be efficient, may still introduce optimization challenges. Ensuring that this network converges to a solution that effectively combines local and non-local prompts is not trivial, especially when dealing with heterogeneous data distributions. The paper does not provide sufficient detail on the training procedure of this gating network. Specifically, what are the learning rates, batch sizes, and optimization algorithms used? How is the network initialized, and what regularization techniques are employed to prevent overfitting? These details are crucial for reproducibility and for understanding the stability of the training process.

2.  As the number of clients increases, managing a dynamic pool of prompt experts and maintaining efficient communication between the server and all clients can become more challenging. The complexity of coordinating updates and ensuring that each client receives the most relevant prompts could grow significantly. The paper does not address the scalability of the proposed approach with respect to the number of clients. How does the communication overhead scale with the number of clients? What are the computational costs associated with maintaining the expert pool on the server side? These are important considerations for practical deployment in large-scale federated learning scenarios.

### Questions
Please see weaknesses.

### Soundness
3

### Presentation
2

### Contribution
2
