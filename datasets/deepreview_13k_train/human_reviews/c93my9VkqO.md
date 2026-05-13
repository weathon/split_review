# Over 100x Speedup in Relational Deep Learning via Static GNNs and Tabular Distillation

- Decision: Reject
- Scores: 5, 3, 3, 5

## Abstract
Relational databases, organized into tables connected by primary-foreign key relationships, are widely used in industry. Companies leverage this data to build highly accurate, feature-engineered tabular models—often using boosted decision trees—to predict key metrics such as customer transactions and product revenues. However, these models need frequent retraining as new data is introduced, which is both expensive and time-consuming. Despite this, by being the result of extensive engineering effort, they remain difficult to outperform using generalist methods, like Temporal Graph Neural Networks (TGNNs) trained over the same relational data. Rather than attempting to replace tabular models with generalist approaches, we propose to combine the strengths of tabular models and static Graph Neural Networks (GNNs). GNNs offer better speed and scalability than TGNNs, and, as we argue, the primary strength of graph representation learning for these tasks does not lie in modeling temporal dynamics—something highly- engineered tabular models excel at—but in capturing complex relationships within the database, which are hard to featurize. Our approach integrates all predictive embeddings of all tabular models developed for various tasks into a single static GNN framework. Experimental results on the RelBench benchmark show that our approach achieves a performance improvement of up to 33% and an inference speedup of up to 1050x, making it highly suitable for real-time inference.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper introduces TREELGNN, a novel method for addressing relational database (RDB) prediction. TREELGNN combines advanced feature engineering from tabular models with a more efficient static GNN backbone. This approach demonstrates improved performance and computational efficiency compared to the Temporal GNN method when evaluated on RelBench.

### Strengths
1. The paper presents a straightforward yet effective method that shows significant efficiency improvements over Temporal GNNs for RDB prediction tasks.
2. The authors’ approach to modeling tabular features, RDB relationships, and temporal dynamics offers a unique perspective. The framework’s emphasis on feature modeling, while simplifying temporal dynamics, proves effective.
3. The framework is flexible and extendable, supporting a wide selection of tabular models and GNN layers, allowing for more potential configurations.

### Weaknesses
1. The effectiveness of the proposed distillation process is unclear. Distillation generally involves training an additional encoder to transfer information from the tabular model to the main predictive model. However, the analysis does not clarify why this method outperforms directly incorporating feature-engineered results from the tabular models. Specifically, the mechanism by which the softened labels from the tabular model provide a better signal than the raw predictions is not well-explained. It's unclear if the improvement is due to the distillation process itself or simply a different way of weighting the tabular features. (See Question Q1 for more on this.)
2. The distinction between the “time-then-graph” process in TREELGNN and previous TGNN methods is insufficiently explained. The authors mention time-then-graph as a computation-saving approximation for temporal GNNs. However, this concept has already been established in temporal GNN literature (also as the authors cited), as seen with models like TGN [1], which uses memory to store previous information while processing only current events—closely resembling TREELGNN. The paper does not adequately articulate how TREELGNN's approach to time-then-graph differs from existing methods, particularly in terms of how it handles temporal dependencies and feature propagation across time steps. Further comparison would help clarify TREELGNN’s unique contributions in this regard.
3. The paper contains minor typographical errors, such as the misuse of commas and decimal points in tables.

### Questions
1. Could the authors more systematically compare the candidate baselines, such as LIGHTGBM, RDL w.P, RDL w.D, and TREELGNN w.P? Specifically:
- (a) Why might RDL with LIGHTGBM predictions perform worse than LIGHTGBM alone (sometimes markedly worse)?
- (b) What would be the effect of distilling information using the GNN outputs? For instance, if embeddings from the original TGNN or TREELGNN w.P were used to optimize final predictions with LIGHTGBM outputs?
- (c) Performance improvements in classification appear inconsistent across RDL w.P, RDL w.D, and TREELGNN. What might be contributing to this variability?
- (d) Appendix C provides additional experiments on distillation; could the authors elaborate on these experiments and their conclusions?
2. What accounts for the substantial efficiency gains observed? Are they due to TGNNs' inefficient temporal neighbor accesses, or simply fewer neighbors in general? Would restricting TGNN to a similar number of neighbors reduce its computational time as well?
3. A suggestion for presenting results: A pipeline diagram might help provide a clearer overview of the approach. Additionally, organizing the experiment results with a clearer separation between main results and ablation studies might improve clarity, as the current presentation mixes the two.

### Soundness
2

### Presentation
2

### Contribution
3

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
This paper proposes to combine the strengths of tabular models and static GNNs to achieve more efficient predictions on relational databases. The reported predictive and runtime performance are quite significant.

### Strengths
- Strong predictive performance and very strong reported runtime efficiency
- The proposed method is intuitive and easy to understand

### Weaknesses
 - The proposed idea is not novel. There is a long history of combining tree-based models (e.g., XGBoost) with GNNs, including using XGBoost as features for GNNs as is used in this paper; however, the paper fails to discuss this line of related works. For example, Boost then Convolve: Gradient Boosting Meets Graph Neural Networks, accepted to ICLR 2021, also proposed similar ideas, but the paper failed to mention it.
- The premise of this paper, that TGNNs are mainly trained over the same relational data, is wrong/questionable. If we check the related works cited in this paper, we can find that many existing works do not use a TGNN but use the static GNN that is also used in this paper. Even for the paper that this paper frequently refers to and compares against (Robinson et al.,2024), they did not claim they are using a TGNN either.
- The major claim, that there is a 100x speed-up, is questionable. To make convincing claims on runtime efficiency boost, the paper should have defined the relevant settings and metrics clearly; however, the paper failed to do so. Some of the questions/concerns include: (1) Does the tree-based model (LightGBM) component count as the training/inference time? (2) If so, why not report the training and inference time of LightGBM? Its predictive performance has been reported, but its runtime is missing. (3) What is the definition of epoch here? The mini-batch definition of a temporal GNN and a static GNN could be quite different. (4) Instead of reporting runtime per epoch which is unclear, why not report the complete end-to-end training/inference time for all the methods? (5) Based on the appendix (by the way, according to ICLR guidelines, the appendix should be attached with the submission, but this paper apparently did not follow the guideline), the number of parameters of temporal GNN is orders of magnitude large than static GNN. For example, for rel-hm the RDL has 100x more parameters than the proposed method, which is not a fair comparison for arguments on runtime.
- Following the above-mentioned concerns, explicitly claiming the over 100x speedup in the title is not appropriate and could be misleading.
- The implementation of the baseline is also very vague. After checking, the RDL was originally a position paper. There are many variants of RDL, including GraphSAGE and ID-GNN versions. The paper does not mention which version of RDL they use in all the comparisons. Moreover, all the numbers in this paper are not the same as the reported number of RDL and the baseline LightGBM. The authors could better explain how the numbers are obtained.

### Questions
- Across all the experiments, it seems that the predictive performance between LightGBM and proposed TreeLGNN is quite marginal, in some cases, such as rel-hm or rel-stack, LightGBM is actually better. Is GNN really helpful for the RDB prediction tasks if efficiency is the major focus? Could the author report the inference/training speed up from LightGBM and over the proposed TreeLGNN?

- There are many relational databases that are not dynamic, why does this work focus on the temporal aspect of RDB prediction tasks? For static RDB prediction tasks, I suppose the proposed method will actually be slower. Here, the baseline will also be a vanilla static GNN, and the proposed TreeLGNN will have an additional LightGBM preprocessing module.

### Soundness
2

### Presentation
1

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
The paper proposes TREELGNN, which combines LightGBM with GNN. 
Basically, the authors consider the graph at time $t$ as a static graph. And then they use the LIGHTGBM-distilled embeddings as node features and use GNN to learn the entity relations. The goal is to predict the result at $t+1$.
The authors conduct experiments on four tasks in RelBench. The performance is on par, but the training and inference time is much faster as compared to RDL.

### Strengths
The GNN + LIGHTGBM-distilled embeddings produces much faster training time and inference time, while having slightly better performance on the tasks.

### Weaknesses
1. The authors only evaluate their proposed model on one benchmark, RelBench. Moreover, it only compared to 4 out of the 30 tasks from Relbench. It also lacks experiments on link prediction tasks. 
2. The idea lacks innovation. RDL already uses deep learning models like resnet for node feature encoder. This paper only changes the encoding strategy from deep learning models to lightgbm. The rest of the architecture follows the design in RDL
3. Using embeddings from pre-trained model will obviously outperform RelBench on speed. This is because the feature encoders in RDL are trained alongside the GNN. So not training the encoder will for sure improve the training/inference time.

### Questions
Suggestion:
1. Compare across different tasks in RelBench.
2. The datasets the authors use are fairly small. Consider running experiments on large scale datasets.
3. Consider using other tree-based models than LightGBM.

### Soundness
2

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
4

### Summary
This paper suggests combining the strengths of tabular models with static Graph Neural Networks (GNNs) to improve performance and speed in predicting key metrics from relational databases. By integrating predictive embeddings from tabular models into a unified GNN framework, the approach achieves up to a 33% performance boost and a remarkable 1050x speedup in inference, making it highly suitable for real-time applications.

### Strengths
- **Research Topic.** The studied problem is interesting and practically important for relational deep learning.

- **Writing.** The paper is well-organized and written in a clear, logical manner, moving seamlessly from problem introduction to method presentation, experiments, and results.

### Weaknesses
 - **Applicability.** The method introduced in this article is limited to application on time series data. Enhancements to enable its application on broader datasets while maintaining substantial time savings would be advantageous.

- **Experimental Baselines.** The paper is suggested to compare experimental results with more baselines, such as XGBoost and static and temporal GNN methods. Only 2 baselines make the experimental section not so convincing.

- **Experimental Datasets.** Only a few part of RelBench is used, and it would be better if more datasets are evaluated on.

- **Experimental Results.** The paper is suggested to compare the time usage with LightGBM, for TREeLGNN can not always outperforms LightGBM.

### Questions
- What is the meaning of TREeLGNN?

- In Figure 1, the word "articles" should be "products", and this mistake appears in Section 2.2.

- Figure 2 is not so clear, which needs more explanation.

### Soundness
2

### Presentation
2

### Contribution
2
