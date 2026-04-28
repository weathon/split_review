# Lightweight Unsupervised Federated Learning with Pretrained Vision Language Model

- Decision: Reject
- Avg Score: 3.67
- Scores: 3, 5, 3

## Abstract
Federated learning aims to tackle the ``isolated data island" problem, where it trains a collective model from physically isolated clients while safeguarding the privacy of users' data. However, supervised federated learning necessitates that each client labels their data for training, which can be both time-consuming and resource-intensive, and may even be impractical for edge devices. Moreover, the training and transmission of deep models present challenges to the computation and communication capabilities of the clients.
To address these two inherent challenges in supervised federated learning, we propose a novel lightweight unsupervised federated learning approach that leverages unlabeled data on each client to perform lightweight model training and communication by harnessing pretrained vision-language models, such as CLIP. By capitalizing on the zero-shot prediction capability and the well-trained image encoder of the pre-trained CLIP model, we have carefully crafted an efficient and resilient self-training approach. This method refines the initial zero-shot predicted pseudo-labels of unlabeled instances through the sole training of a linear classifier on top of the fixed image encoder. Additionally, to address data heterogeneity within each client, we propose a class-balanced text feature sampling strategy for generating synthetic instances in the feature space to support local training. 
Experiments are conducted on multiple benchmark datasets. The experimental results demonstrate that our proposed method greatly enhances model performance in comparison to CLIP's zero-shot predictions and even outperforms supervised federated learning benchmark methods given limited computational and communication overhead.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This study leverages a pre-trained vision-language model for unsupervised image classification within a federated learning framework. The authors introduce two strategies to enhance the zero-shot prediction capabilities of CLIP. Experiments show that the proposed framework achieves better results compared to conventional supervised federated learning approaches.

### Strengths
1.	Compared to other federated learning scenarios, such as supervised and semi-supervised methods, unsupervised federated learning remains a relatively unexplored domain.
2.	From the ablation study, the proposed two approaches can effectively improve the zero-shot prediction accuracy of CLIP and mitigate the class imbalance problem to some extent.

### Weaknesses
1.	The contributions of this study did not meet the anticipated expectations. The two methods introduced lack novelty. The idea of refining pseudo-labels has been previously explored within the context of self-supervised learning. Additionally, the class-balanced data generation draws parallels with the Synthetic Minority Over-sampling Technique and can be categorized as an oversampling strategy.
2.	While the authors highlight the lightweight nature of their proposed framework, evidence throughout the paper seems insufficient. The sole indication of its lightweight character is the use of a linear classifier during training. However, this isn't a unique aspect as the baseline methods employ the same classifier. The purported lightweight advantage of the proposed framework isn't adequately substantiated. Furthermore, a comprehensive analysis of both computation and communication costs is essential to truly label the framework as lightweight and communication efficient.
3.	More experiments are required, especially for large scale datasets like ImageNet.
4.	There are some typos, like FedBR (Guo et al., 2023b) FedBR (Guo et al., 2023b), tranfer, etc.

### Questions
please respond to the weaknesses

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This work proposed a novel lightweight unsupervised federated learning approach, FSTCBDG, to alleviate the computational and communication costs as well as the human labor of data annotations. The evaluation results illustrated the proposed FSTCBDG significantly outperforms the baseline methods.

### Strengths
1. Developed a lightweight unsupervised federated learning approach based on a single linear layer.

2. Designed a self-training objective for the linear classifier

3. Conducted extensive experiments to show the good performance of the proposed method over the baselines.

### Weaknesses
1. The class prototype augmentation based on Gaussian noise is not novel, since this idea has been used in prior work called PASS [Zhu CVPR 2021]. In addition, some follow-up works like [Zhu CVPR 2022] have pointed out that synthetic data from Gaussian-based augmentation would make some similar classes overlap with each other. Thus, the proposed method in this paper may not work well.

2. It may need to explain why the testing accuracy of baselines drops as the number of communication rounds increases.

3. Why did not compare with the FedUL baseline?

### Questions
Please see the comments above.

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper uses the CLIP image and text encoder for unsupervised learning in FL. Specifically, it uses the image encoder and text features extracted in the server in the client for training. Besides, it also generates data samples on clients to mitigate data imbalance problems.

### Strengths
- The idea is interesting and the Figure 1 illustrates the idea well.
- The paper the generally well-written and easy to follow.
- The proposed method achieves significantly better performance than compared counterparts, especially under heterogeneous data distribution.
- The proposed method only requires a few rounds of communication.

### Weaknesses
 - Some important experimental details are missing. For example, the model architecture used for training the other methods. Specifically, it is unclear if the compared methods use the same backbone and training procedure as the proposed method, which is crucial for a fair comparison. The paper only mentions a linear layer classifier is trained on top of the CLIP image encoder, but does not specify if the baselines also use the same fixed CLIP encoder or if they are trained from scratch.
- The paper mentions computation efficiency in Section 4.2.3, but it seems that the computation saving is mainly from the reduction of the communication round. The paper seems to focus on cross-device FL. It would be useful to further investigate whether the device could fit in the model size of CLIP and has enough memory to use it for inference. The paper should provide a more detailed analysis of the memory footprint and computational cost on the client side, especially considering the use of the CLIP model, even if it is the smallest variant.
- The compared methods are somewhat weak baselines. Some important unsupervised FL baselines and methods are not discussed or compared in the paper, e.g., [1][2][3][4]
    - [1] Collaborative Unsupervised Visual Representation Learning from Decentralized Data. ICCV’21
    - [2] Divergence-aware Federated Self-Supervised Learning. ICLR’22.
    - [3] Orchestra: Unsupervised Federated Learning via Globally Consistent Clustering. ICML’22
    - [4] MocoSFL: Enabling Cross-client Collaborative Self-supervised Learning. ICLR’23
- Some papers mentioning adopting CLIP to FL are not discussed. e.g. [5][6]
    - [5] Fedclip: Fast generalization and personalization for clip in federated learning.
    - [6] When Foundation Model Meets Federated Learning: Motivations, Challenges, and Future Directions.

### Questions
- What is the impact of using different types of backbone?
- What is the impact of training for more local epochs in each round?

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair
