# FedP3: Federated Personalized and Privacy-friendly Network Pruning under Model Heterogeneity

- Decision: Accept
- Avg Score: 6.00
- Scores: 6, 8, 5, 6, 3, 8

## Abstract
The interest in federated learning has surged in recent research due to its unique ability to train a global model using privacy-secured information held locally on each client. 
This paper pays particular attention to the issue of client-side model heterogeneity, a pervasive challenge in the practical implementation of FL that escalates its complexity. 
Assuming a scenario where each client possesses varied memory storage, processing capabilities and network bandwidth - a phenomenon referred to as system heterogeneity - there is a pressing need to customize a unique model for each client.
In response to this, we present an effective and adaptable federated framework \algname{FedP3}, representing \textbf{Fed}erated \textbf{P}ersonalized and \textbf{P}rivacy-friendly network \textbf{P}runing, tailored for model heterogeneity scenarios.   
Our proposed methodology can incorporate and adapt well-established techniques to its specific instances. We offer a theoretical interpretation of \algname{FedP3} and its locally differential-private variant, \algname{DP-FedP3}, and theoretically validate their efficiencies.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper highlights the growing interest in federated learning (FL) for its privacy-preserving capabilities. It particularly addresses the challenge of client-side model heterogeneity in FL, driven by variations in client resources. Termed "system heterogeneity," this scenario necessitates customizing a unique model for each client. The paper introduces FedP3, a Federated Personalized and Privacy-friendly Network Pruning Framework, designed to address model heterogeneity effectively. FedP3 can adapt established techniques to specific instances, offering a practical solution.

### Strengths
==*== Strengths
+ This work offers an effective and adaptable FL framework FedP3 tailored for model heterogeneity scenarios.
+ The proposed personalized network pruning technique is applicable to diverse scenarios.

### Weaknesses
==*== Weaknesses
- The outcomes of the experiment need to be made more convincing. Specifically, the paper lacks detailed ablation studies demonstrating the impact of individual components of FedP3, such as the global and local pruning strategies, on overall performance. The experimental results should also include a more thorough analysis of the variance in performance across different clients, as well as the impact of varying degrees of data heterogeneity on the effectiveness of the proposed method.
- Limited in-depth comparison with state-of-the-art solutions. The paper does not adequately compare FedP3 with existing personalized federated learning methods that also address model heterogeneity through techniques like adaptive model aggregation or knowledge distillation. The current comparison is insufficient to demonstrate the novelty and advantages of the proposed approach. The paper should include a more detailed comparison with methods that employ similar techniques, such as pruning, to address heterogeneity.
- Privacy analysis and convergence analysis need to be included. Indeed, separating model parameters from the network parameter architecture is intuitively beneficial to FL privacy protection, but whether existing gradient reconstruction attacks or other privacy attacks will challenge this personalization technology has not been fully explored. Therefore, it would be better if the authors could analyze the privacy performance empirically or theoretically. Furthermore, the convergence analysis of the proposed method has not given any explanation. For model heterogeneous scenarios, reviewers expect to see rigorous analysis and discussion of the convergence and stability of this method. The paper should provide a theoretical analysis of the convergence properties of the proposed algorithm, including a discussion of the impact of pruning on convergence rates and stability.
- This paper claims that the proposed personalized pruning technique can well alleviate the system heterogeneity and model heterogeneity problems, but the reviewer has not seen any discussion and numerical results on the system heterogeneity scenario. The paper should include experiments that simulate different client devices with varying computational capabilities and communication bandwidths, demonstrating the effectiveness of FedP3 under realistic system heterogeneity conditions. The current experiments focus primarily on data and model heterogeneity but do not adequately address system heterogeneity.

### Questions
Comments:

-	Privacy analysis and convergence analysis need to be included. Indeed, separating model parameters from the network parameter architecture is intuitively beneficial to FL privacy protection, but whether existing gradient reconstruction attacks or other privacy attacks will challenge this personalization technology has not been fully explored. Therefore, it would be better if the authors could analyze the privacy performance empirically or theoretically.

-	Furthermore, the convergence analysis of the proposed method has not given any explanation. For model heterogeneous scenarios, reviewers expect to see rigorous analysis and discussion of the convergence and stability of this method.

-	This paper claims that the proposed personalized pruning technique can well alleviate the system heterogeneity and model heterogeneity problems, but the reviewer has not seen any discussion and numerical results on the system heterogeneity scenario.

-	Limited in-depth comparison with state-of-the-art solutions. In fact, personalized pruning technique is not the first time to be applied to FL to solve efficiency and heterogeneity problems. The following literature needs to be included in the baseline solutions and explain the differences and connections between this paper and them.

[1] Zhou X, Jia Q, Xie R. NestFL: efficient federated learning through progressive model pruning in heterogeneous edge computing[C]//Proceedings of the 28th Annual International Conference on Mobile Computing And Networking. 2022: 817-819.

[2] Li A, Sun J, Li P, et al. Hermes: an efficient federated learning framework for heterogeneous mobile clients[C]//Proceedings of the 27th Annual International Conference on Mobile Computing and Networking. 2021: 420-437.

[3] Pase F, Isik B, Gunduz D, et al. Efficient federated random subnetwork training[C]//Workshop on Federated Learning: Recent Advances and New Challenges (in Conjunction with NeurIPS 2022). 2022.

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
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The appeal of Federated learning lies in its privacy-aware model training using data held locally on clients. However, the issue of varied client capacities, termed system heterogeneity, complicates its implementation. This paper proposes the FedP3 framework, emphasizing federated, personalized, and privacy-friendly network pruning, to cater to such diverse client scenarios.

### Strengths
1.	The proposed system comprehensively considers a holistic management of heterogeneity, i.e., it effectively manages both data and model disparities. It supports data distribution among clients, class-wise or Dirichlet non-iid. Moreover, it accommodates variance in the models between the server-client and among individual clients.
2.	The proposed methods are inspiring for real-world scenarios, including dual pruning that supports both global pruning (from server to client) and local pruning by individual clients; few-layer communication from the clients to the server after local training. 
3.	Experiments validate that the proposed FedP3 is both effective and adaptable. It paves the way for personalized and privacy-conscious pruning in a heterogeneous federated setting.

### Weaknesses
1.	Few-layer communication can also significantly reduce communication costs and save bandwidth, a detailed numerical analysis would help. Specifically, it would be beneficial to quantify the reduction in the number of parameters transmitted and the corresponding impact on bandwidth usage, considering different network architectures and layer configurations. This analysis should also account for the overhead associated with transmitting layer indices or masks, which could offset some of the gains.
2.	The results on various FL aggregation strategies shall be considered for completeness. It is important to evaluate how FedP3 performs with different aggregation methods beyond simple averaging, such as FedProx or SCAFFOLD, as these methods can have a significant impact on convergence and performance, especially in heterogeneous settings. The interaction between the pruning strategy and these aggregation methods should be explored.
3.	Hyperparameter tuning part is not so crystal. More explanation is needed on how to choose and tune the hyperparameter (maybe via grid-search?) to deliver the best possible results for each model. The paper should detail the search space for each hyperparameter, the specific optimization algorithm used (if any), and the criteria used to select the optimal values. It should also discuss the sensitivity of the results to different hyperparameter settings.
4.	Broader Literature Review is expected. While this work focuses primarily on the discussion and analysis of the most relevant and typical works, this approach might overlook other pertinent past research that holds tangential relevance to their study. For example, research on dynamic pruning or adaptive communication strategies could provide valuable context and comparison points.

### Questions
1. How much the few-layer communication can save communication costs and bandwidth?
2. How the other FL aggregation strategies work in combination with FedP3?
3. How to choose and tune the hyperparameter?

### Soundness
4 excellent

### Presentation
3 good

### Contribution
4 excellent

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper focus on the problem of federated learning with model heterogeneity among clients and designs an algorithm that (1) allows each client only to perform training on a small subnetwork and (2) incorporates model pruning between server and clients to meet the different memory and communication constraints of individual clients. For subnetwork selection, the paper allows each client to train a randomly selected subset of layers of the global model. For model pruning, the paper explores two approaches: uniform pruning and uniform-ordered dropout. Finally, for aggregation of clients' updates, the paper explores simple averaging, weighted averaging (with the weight proportional to the number of layers each client trains), and attention averaging.

### Strengths
- The problem of designing FL algorithms under model heterogeneity is well-motivated from practice. 
- The paper introduces the new ingredient of subnetwork pruning between the server and the clients and investigates the effect of pruning strategies and pruning ratio on the performance of FL.
- The authors performed necessary ablation studies for the proposed algorithm, such as different subnetwork selections, data heterogeneity levels, sizes of total networks, and aggregation methods.

### Weaknesses
 - There is a discrepancy between the experiment setting and the motivation problem setting in the introduction.
  - The experiment setting does not reflect the heterogeneity of memory and communication constraints between clients, even though this is a major motivation mentioned in the introduction. Specifically, in all experiments, different clients train subnetworks roughly the same size. 
  - The subnetwork is not significantly smaller than the global model. For the ResNet-18 experiments, the subnetwork of each client appears to be at least around half the scale of the global model. This differs from the interesting scenario mentioned in the introduction, where each subnetwork is significantly smaller than the global model.
- Lack of baselines for interpreting the significance of the proposed algorithm. One baseline that is not mentioned is an approach that performs model pruning on the global model first and then performs standard FL on the pruned smaller model. This is for understanding the necessity of personalized model pruning among clients.
- Algorithm descriptions sometimes need more clarity; see question 3 for more details.

### Questions
1. Could the authors comment on whether the algorithm would perform well if the subnetworks trained by individual clients are significantly smaller than the global model? Table 2 shows that the algorithm performs poorly when each client only trains one layer.
2. Could the authors comment on an alternative approach of global model pruning + standard FL on the pruned model?
3. Several parts of the algorithm could be clarified more.
   - Figure 1 shows that each client still needs to store a large proportion of the unpruned global model. Is that correct?
   - In Algorithm 1, the pruned weights $P_i(W_t^l)$ are not used anywhere later.
   - In eq (2), the objective function $h$ does not appear to be defined for the problem considered in this paper.

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This paper focuses on addressing the model heterogeneity problem in federated learning. Concretely, it proposes an adaptable federated framework that leverages the personalized pruning technique in a privacy-preserving way. Experiments show that FedP3 can deal with data and model heterogeneity and adapt to various pruning strategies.

### Strengths
1. An interesting network pruning-based pipeline is proposed. In this pipeline, the size of training parameters can be personalized for each client.

2. Various local pruning and global aggregation strategies are developed, which present high flexibility of the proposed framework. 

3. Limitations of this paper including theoretical analysis and LLMs aspects are well discussed.

### Weaknesses
1. The relation between privacy-friendly property and network pruning is implicit. It is better to provide a detailed illustration of the reason why existing pruning-based FL methods have privacy concerns. This can help readers to better understand the motivation of the privacy-preserving part. 

2. The authors have emphasized the possibility of utilizing the proposed method in LLMs-based scenarios but there is a lack of related experiments supporting that point. Only shallow neural networks and ResNet are considered in the experimental part.

3. To show the improved communication efficiency as mentioned in the 5th paragraph of the Introduction, it is better to provide some quantitive results on the number of communicated parameters. 

4. The presentation of the paper should be further enhanced and some parts should be reorganized. For example, the training goal and variable notation should be given in the Preliminary or Methodology section rather than the Introduction section. 

5. Lack of empirical comparison with existing FL methods that also address model heterogeneity problem. 

6. To solve the model heterogeneity problem, some existing work needs to be discussed, e.g. Knowledge Distillation-based FL [1],  Prototype-based FL [2], and NAS-based FL.

### Questions
1. Please refer to weakness.

2. How to conduct federated training of LLMs based on the proposed method?

3: In the algorithm, predefined pruning mechanisms are assigned for each client. Is this a common operation in FL under model heterogeneity issues? Are there any previous works conducting similar operations?

4: There are multiple pruning and averaging strategies that can be adopted in the proposed FedP3. For a specific case, how to select the most appropriate strategy? 

5. In practice, what if we set several types of models to tackle various heterogeneous devices? Can you set a baseline algorithm to test it?

### Soundness
4 excellent

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 5

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The authors present a "privacy-preserving" pruning mechanism that is tailored for heterogeneous clients/devices. In this approach, only a part of the model is transmitted to the server, saving resources and enhancing privacy.

### Strengths
- The paper is well written, presented and easy to understand. 
- Tackling device heterogeneity on federated learning is an important problem
- Model pruning and submode research is an important step towards addressing device heterogeneity and our ability to train larger models with federated learning

### Weaknesses
The main weaknesses of this paper are:
- The authors claim that this method is "privacy-preserving" and designed to maximise privacy overall. At the same time, there is no evaluation at all wrt to privacy (either analytical or through some empirical attacks). Furthermore, the privacy aspect is not discussed, practically assuming that fewer layers sent -> more privacy. While there might be some correlation there, I would expect these claims to be backed up with some thorough evaluation/analysis. Specifically, the paper lacks any formal privacy analysis, such as differential privacy guarantees or empirical evaluations against membership inference attacks. The claim that sending fewer layers inherently provides more privacy is not sufficiently justified and requires a more rigorous treatment.

- Similarly, the authors claim that resources are saved (energy, memory, cpu)  and larger models can be trained. But there is no evaluation wrt to any such savings. There are no numerical results wrt to any energy savings, the memory consumption savings, understanding how wide can the heterogeneity can we have wrt to device capabilities. Finally, It would be great to have a thorough study on the convergence speed. The paper needs to quantify the resource savings, providing concrete metrics for energy consumption, memory footprint, and CPU usage under various pruning configurations and heterogeneous device capabilities. Furthermore, the convergence analysis should include a comparison with standard federated learning algorithms under similar conditions.

- Finally, given that there are a number of sub-model FL training methods proposed (the authors cite a few), it would be great if the evaluation could be expanded to compare with the state of the art.

### Questions
Please see my comments above.

### Soundness
2 fair

### Presentation
4 excellent

### Contribution
2 fair

---

## Human Reviewer 6

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
Federated learning has gained attention for its capability to train global models while maintaining local data privacy. This paper delves into the challenge of client-side model heterogeneity, exacerbated by differences in clients' memory, processing, and network capabilities (system heterogeneity). The proposed FedP3 framework can well address these challenges.

### Strengths
- Adaptable Design: FedP3 caters to model diversity by allowing personalization based on each client's specific capacities, including computational, memory, and communication constraints.
- Novel Dual-Pruning Strategy: FedP3 integrates a dual-pruning approach. This encompasses both global pruning (server to client) and local pruning executed by individual clients.
- Strong Privacy Commitment: FedP3 prioritizes user privacy. The design ensures that full client data is kept confidential as only the selected layers are transmitted from the client to the server post-local training.

### Weaknesses
 - Absence of Theoretical Insights: This work seems lacks a strong theoretical foundation or interpretation.
- More Ablations: The current model does not explore all potential ablations, for instance, different data aggregation techniques.

### Questions
Please refer to the weaknesses.

### Soundness
3 good

### Presentation
3 good

### Contribution
4 excellent
