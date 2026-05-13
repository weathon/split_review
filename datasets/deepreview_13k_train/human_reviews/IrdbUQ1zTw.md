# Reinforcement Learning-based Layer-wise Aggregation for Personalized Federated Learning

- Decision: Reject
- Scores: 6, 3, 6

## Abstract
A key challenge in Federated Learning (FL) is statistical heterogeneity, which may result in slow convergence and accuracy reduction. To tackle this problem, personalized federated learning (PFL) aims to adapt the global model to the individual data distribution of each client. One approach for this is personalized aggregation, which automatically determines how much each client can benefit from other clients' models. This paper proposes a new PFL method based on two principles: a) shared knowledge and personalized knowledge are reflected in different layers of the network and b) clients with more data should contribute more to shared knowledge, while knowledge transfer from similar clients can boost personalization. Based on these, we propose a Reinforcement Learning-based Layer-wise Aggregation method (pFedRLLA) that applies different mechanisms for different neural network layers. For layers representing shared knowledge, aggregation is carried out based on the size of the local data samples of the client. For layers representing personalized knowledge, a deep reinforcement learning (DRL) agent is used to generate personalized aggregation weights. To ascertain efficiency and scalability, we train a single DRL agent (for all users) that operates on the server-side and takes as input a subset of user models. To further reduce its state-space, we design a multi-head auto-encoder to obtain low-dimensional embeddings of user models. Extensive experiments on benchmark datasets for variable data heterogeneity levels reveal that the proposed algorithm consistently outperforms baselines in terms of both higher accuracy (up to +3.1\%) and faster convergence (a reduction of global rounds by up to 20.5\%).

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper introduces pFedRLLA, a reinforcement learning-based layer-wise aggregation method designed to tackle the challenge of statistical heterogeneity in personalized federated learning. The approach applies different aggregation strategies to different layers of neural networks. The feature extracting layers (body) use weights proportional to the data sizes of the clients, while the heads employ a deep reinforcement learning (DRL) agent to generate personalized aggregation weights. The DRL agent considers compound rewards that take into account both the improvement of validation accuracy and the similarity between clients. Besides, to reduce the state space, a multi-head auto-encoder is utilized to obtain low-dimensional embeddings of user models.

Experimental results on benchmark datasets with varying levels of data heterogeneity demonstrate the effectiveness of the proposed method. It outperforms the baselines in terms of accuracy and convergence speed.

### Strengths
1. This paper presents a novel approach that utilizes reinforcement learning (specifically, DDPG) to tackle the task of learning aggregation weights in the classifier heads. This approach seems to offer a fresh perspective.

2. The proposed method surpasses existing approaches in addressing data heterogeneity in personalized federated learning. The results demonstrate higher accuracy achieved in less time.

### Weaknesses
1.The authors claim that the main novelty lies in the layer-wise design in section 2 (related work). However, the idea of separating the body and head for aggregation is not entirely novel, as seen in approaches like pFedLA, which even achieves a finer-grained layer-wise aggregation using the power of hypernetworks. In comparison, this paper only roughly separates the body and head, and cannot be considered truly layer-wise like pFedLA. Additionally, the idea of separating aggregation for the body and head has also been proposed in FedPAC, with a more detailed mathematical logic. Besides, the weighted averaging based on data volume for body aggregation is trivial and straightforward.

2. Although the experimental results demonstrate the superior performance of the pFedRLLA framework, there is a lack of theoretical analysis explaining why RL-based methods work better. It seems that the paper provides more intuitive reasoning.

3. In terms of clarity, the paper occasionally fails to clearly differentiate between crucial and supplementary information. For instance, the descriptions accompanying the figures and tables, such as Figure 1 and Table 2, are excessively long, while the corresponding text in the main body appears relatively weaker. The steps mentioned below Figure 1 are relatively concise, but the figure description provides excessive detail, also including redundant content.

### Questions
1. In the reward design, the hyperparameter "beta" is not further explained, and it appears that in the code it is simply set as {1, 1, -2}. Regarding the weight allocation for r1, r2, and r3 (the compacts of validation accuracy and similarity), it is unclear if there is a more in-depth consideration. By the way, it would be better to add a negative sign to r3 to maintain consistency with r1 and r2.

2. Will there be any theoretical analysis provided to explain why RL-based methods outperform existing pFed methods? Besides DDPG, have you attempted other RL methods, and why is DDPG the preferred choice?

3. Regarding clarity, there is room for improvement about the issues raised in Weakness3.

### Soundness
3 good

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper provides a personalized federated learning method based on reinforcement learning, which aggregates the local models in a layer-wise manner. In the method, the body part of the model  (i.e., shared knowledge) is aggregated according to the local data size. Also, the head part of the model (i.e., personalized knowledge) is aggregated by using the personalized aggregation weights that are generated by deep reinforcement learning.

### Strengths
The proposed algorithm uses multi-head autoencoder for dimension reduction instead of PCA, which makes it more practical. The source code of the paper is provided.

### Weaknesses
For personalized federated learning, plenty of works have been studied using a variety of learning methods such as knowledge distillation, meta learning, transfer learning, etc., and including reinforcement learning. Considering this, the concept of the paper is not sound and novel, and its contribution seems marginal compared with the conventional federated learning methods with reinforcement learning and multi-armed bandits.

Typically, a lot of experiences is required to learn a DRL policy. In federated learning, is there an enough number of rounds that the DRL policy to be converged? Or, should the DRL policy be trained in advance?

How is the multi-head autoencoder trained when using the proposed algorithm? Is it should be trained in advance? This should be clarified in the paper.

If the DRL policy or autoencoder should be trained in advance, it should be clarified how the dataset for training them can be obtained before applying federated learning.

For a limited number of rounds, it may be doubted that considering accuracy-related rewards (i.e., $r_1$ and $r_2$) will be effective or not. Providing the ablation study of $r_1$, $r_2$, $r_3$ would be helpful to understand the effect of the weights according to the reward structure.

It seems that the reward in Eq. (1d) is structured so that the weights closer to the similarity vector have the smaller reward. Hence, it encourages  the weight of the similar client become smaller. But, in my understanding, the concept of the proposed algorithm should encourage the weight of the similar client become larger for personalization.

It seems that the weights $p_k$'s from the DDPG should be constrained as to be 1 in sum. How is this realized in the algorithm?

### Questions
1. The main concepts of the paper such as layer-wise aggregation, the use of reinforcement learning for model weighting, and dimension reduction have been already considered in federated learning. Please clarify the contribution of the paper compared with the related works, currently, it seems that the contribution is marginal.

2. In a similar context, it is not clear why reinforcement learning is suitable for personalization of federated learning. Learning another deep neural network for DRL agent may incur significant costs. Please justify the rationale of using DRL agent for personalized federated learning.

3. Typically, a lot of experiences is required to learn a DRL policy. In federated learning, is there an enough number of rounds that the DRL policy to be converged? Or, should the DRL policy be trained in advance?

4. How is the multi-head autoencoder trained when using the proposed algorithm? Is it should be trained in advance? This should be clarified in the paper.

5. If the DRL policy or autoencoder should be trained in advance, it should be clarified how the dataset for training them can be obtained before applying federated learning.

6. For a limited number of rounds, it may be doubted that considering accuracy-related rewards (i.e., $r_1$ and $r_2$) will be effective or not. Providing the ablation study of $r_1$, $r_2$, $r_3$ would be helpful to understand the effect of the weights according to the reward structure.

7. It seems that the reward in Eq. (1d) is structured so that the weights closer to the similarity vector have the smaller reward. Hence, it encourages  the weight of the similar client become smaller. But, in my understanding, the concept of the proposed algorithm should encourage the weight of the similar client become larger for personalization.

8. It seems that the weights $p_k$'s from the DDPG should be constrained as to be 1 in sum. How is this realized in the algorithm?

### Soundness
1 poor

### Presentation
3 good

### Contribution
1 poor

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper proposes a reinforcement learning-based layerwise aggregation method (pFedRLLA) that applies different mechanisms for different neural network layers. pFedRLLA leverages different aggregation methods for different layers of neural networks, allowing to learn a better representation while ensuring model personalization. The authors conduct extensive experiments to validate the proposed methods which reach state-of-the-art performance.

### Strengths
- The paper investigates the personalized federated learning problem which is a hot and important topic. Utilizing reinforcement strategy in PFL is also interesting.

- The paper is well-organized and easy to understand. The figures are clear for illustrations.

- The authors conduct extensive experiments to validate the proposed methods which reach state-of-the-art performance.

### Weaknesses
 - The authors adopt $\beta$ as the hyper parameters on different rewards. However, how to properly choose $\beta$? In my opinion, it should be discussed in the paper.

- Some similar paper should be discussed in the main paper, e.g., [1]

- Some information is missing in the main paper, e.g. the name of Alg.2 is missing.

### Questions
Please refer to the weaknesses above

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair
