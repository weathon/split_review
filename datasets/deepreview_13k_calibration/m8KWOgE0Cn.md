# FENDA-FL: Personalized Federated Learning on Heterogeneous Clinical Datasets

- Decision: Reject
- Avg Score: 3.50
- Scores: 3, 5, 3, 3

## Abstract
Federated learning (FL) is increasingly being recognized as a key approach to overcoming the data silos that so frequently obstruct the training and deployment of machine-learning models in clinical settings. This work contributes to a growing body of FL research specifically focused on clinical applications along three important directions. First, an extension of the FENDA method (Kim et al., 2016) to the FL setting is proposed. Experiments conducted on the FLamby benchmarks (du Terrail et al., 2022a) and GEMINI datasets (Verma et al., 2017) show that the approach is robust to heterogeneous clinical data and often outperforms existing global and personalized FL techniques. Further, the experimental results represent substantive improvements over the original FLamby benchmarks and expand such benchmarks to include evaluation of personalized FL methods. Finally, we advocate for a comprehensive checkpointing and evaluation framework for FL to better reflect practical settings and provide multiple baselines for comparison.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The authors introduce FENDA-FL, an adaptation of the Frustratingly Easy Neural Domain Adaptation (FENDA) method for FL, focusing on the personalized FL paradigm where each participant trains a model tailored to their local data distribution. The effectiveness of FENDA-FL is demonstrated through comprehensive experiments using various clinically relevant datasets, including a subset from the FLamby benchmark and tasks from the GEMINI datasets.

### Strengths
- The application of the FENDA method, originally used for domain adaptation, to Federated Learning (FL) is effective, aligning domain-agnostic features with FL's global components and domain-specific traits with local elements.

### Weaknesses
 - While adapting FENDA's concept to the FL scenario required some modifications, the application of FENDA in this methodology appears overly incremental. The approach of combining features to utilize both global and local information, as opposed to APFL's method of aggregating logits, is not particularly novel. The feature concatenation, while different from APFL's logit aggregation, still represents a relatively straightforward combination of information, and the benefits of this specific approach over other potential fusion methods are not thoroughly explored.
- The methodological contribution to the ICLR community unclear. The application of FENDA to federated learning is straightforward, "federated checkpointing" is conceptually a combination early stopping with federated learning. The paper does not sufficiently articulate the novelty of combining these existing concepts. The idea of checkpointing based on a validation set is a common practice, and the federated aspect adds a layer of complexity but does not fundamentally change the core idea.
- The paper lacks a thorough ablation study on federated checkpointing methods. Additionally, while it benefits from not restricting the network architectures between global and local feature extractors, it would have been informative to show performance variations with the use of diverse network architectures. The absence of experiments exploring different architectural choices for the global and local feature extractors limits the understanding of how these design choices impact performance. For example, the effect of varying the depth or width of these networks, or the use of different types of layers (e.g., convolutional vs. fully connected), is not investigated.
- The paper could greatly improve the visibility of performance differences between methodologies in its figures. Currently, the color-coding for each method is not distinct enough, and the representation of all performances via bar graphs makes it challenging to discern if the differences, including standard deviations, are statistically significant. In terms of visibility, it falls significantly short. The use of bar graphs to represent performance, especially when standard deviations are present, makes it difficult to visually assess the statistical significance of the differences between methods. The lack of clear visual distinction between methods further compounds this issue.

### Questions
Please see the weaknesses

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
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This work expands on the federated learning space in clinincal domain by extending the FENDA method (a domain adaptation method) to federated learning, while showing improvements on the FLamby benchmark.

### Strengths
- Clear presentation, well written paper. 
- Appropriate comparison of baselines on the FLamby benchmark.
- Extensive analysis of multiple other baselines

### Weaknesses
 - It would be nicer to also see a table of the results, rather than a visual representation due to the number of settings. Minor comment: The color choices for the bar graphs seem to represent goodness, with red being worse and blue being better; however, the different colors are a little jarring and could cause confusion.
- The performance benefit compared to APFL shown in Fig. 2 is not very clear, also in Fig. 3, a similar obersvation can be made for FedAVG and APFL

### Questions
- The idea of using domain adaptation seems like a natural pairing with FL. Can the authors include a discussion on the inherent differences / relationships between these 2 fields for better context? Google scholar reveals some papers such as https://arxiv.org/abs/1911.02054 and https://arxiv.org/abs/1912.06733 which may be relevant.
- Is it possible to release a version of the code that works for open-source datasets?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This paper adapts the FENDA method to the federated setting. The central concept involves maintaining both local feature extractors and global feature extractors for each client, with the central server utilizing Fedavg to aggregate the weights of the global feature extractors from each client. The paper rigorously assesses the proposed method using benchmarks and real-world tasks, enhancing evaluation robustness by conscientiously selecting checkpoints based on cross-validation and employing additional baseline comparisons.

### Strengths
- The method is comprehensible and straightforward.
- The experiments meticulously evaluate the proposed method by selecting the appropriate checkpoints, which are convincing and robust. The real-world clinical scenarios are well-suited for federated learning.

### Weaknesses
This paper addresses the challenge of personalized federated learning using heterogeneous local datasets; however, the mechanism is not thoroughly explained. The proposed method draws inspiration from domain adaptation, where distribution shifts naturally occur. In this paper, local clients have datasets sampled from various distributions. The question arises: What types of distribution shifts (such as feature shifts or label shifts) can the proposed method effectively handle?

### Questions
Please describe the mechanism of the proposed method in detail and elucidate its effectiveness in addressing different types of distribution shifts, particularly in the context of client dataset heterogeneity.

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
In this study, the authors introduce a federated domain adaptation model designed to train personalized FL models. The model in question is an adaptation of the FENDA domain adaptation method, leveraging both a global feature extractor and a local feature extractor to adapt data across different domains. Evaluations of the model have been conducted on an FL benchmark dataset as well as a real-world clinical dataset.

### Strengths
The experimental design is thorough, and the paper is well-written and easy to follow.

### Weaknesses
My major concern is a significant oversight in this work, which is the absence of discussions of an important line of related works - federated domain adaptation/generalization. This topic is closely related to the central topic of this paper. There are many advanced techniques for federated domain adaptation/generalization in recent years, for examples [1-2] and numerous other contributions in this domain. Yet, the authors seem to have omitted any discussion contrasting their proposed model with these works, nor have they incorporated them as baseline models for comparison. The decision to utilize the FENDA model, which appears potentially outdated in the domain adaptation field, raises concerns. Without comparing the proposed model against current SOTA methods in the field of federated domain adaptation, it is hard to assert that the domain adaptation strategy showcased here represents the state-of-the-art in FL. The lack of comparison to these methods makes it difficult to ascertain the true novelty and effectiveness of the proposed approach, especially given that the chosen FENDA model is not the most recent in the domain adaptation literature.

### Questions
Please address the weaknesses above.

### Soundness
1 poor

### Presentation
3 good

### Contribution
1 poor
