# Zero-shot Generalist Graph Anomaly Detection with Unified Neighborhood Prompts

- Decision: Reject
- Avg Score: 3.75
- Scores: 3, 6, 3, 3

## Abstract
Graph anomaly detection (GAD), which aims to identify nodes in a graph that significantly deviate from normal patterns, plays a crucial role in broad application domains. Existing GAD methods, whether supervised or unsupervised, are one-model-for-one-dataset approaches, \ie, training a separate model for each graph dataset. This limits their applicability in real-world scenarios where training on the target graph data is not possible due to issues like data privacy. To overcome this limitation, we propose a novel zero-shot generalist GAD approach \textbf{UNPrompt} that trains a one-for-all detection model, requiring the training of one GAD model on a single graph dataset and then effectively generalizing to detect anomalies in other graph datasets without any retraining or fine-tuning. The key insight in UNPrompt is that i) the predictability of latent node attributes can serve as a generalized anomaly measure and ii)  highly generalized normal and abnormal graph patterns can be learned via latent node attribute prediction in a properly normalized node attribute space. UNPrompt achieves generalist GAD through two main modules: one module aligns the dimensionality and semantics of node attributes across different graphs via coordinate-wise normalization in a projected space, while another module learns generalized neighborhood prompts that support the use of latent node attribute predictability as an anomaly score across different datasets. Extensive experiments on real-world GAD datasets show that UNPrompt significantly outperforms diverse competing methods under the generalist GAD setting, and it also has strong superiority under the one-model-for-one-dataset setting.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The paper proposes a method for Graph Anomaly Detection (GAD), which aims to identify nodes in a graph that significantly deviate from normal patterns. The GAD framework is trained on one graph and tested on other graphs, addressing a critical challenge in the detection of anomalies in graph-structured data.

### Strengths
1. The focus on graph anomaly detection is timely and relevant, as it addresses an important area within machine learning and data analysis.

2. The approach of training on one graph and testing on others is interesting.

### Weaknesses
1-The authors acknowledge in their rebuttal that the reported baseline results are suboptimal, which undermines the overall findings. They justify their choice of dimensionality by claiming it is heuristic: 'For all datasets used in our paper, the minimum dimensionality is 25 for the Amazon dataset. Therefore, any number that is smaller than 25 can be used as the common dimensionality. In our experiments, we chose a relatively medium size, eight, as the common dimensionality.'  However, this explanation is unconvincing, as the choice of eight seems arbitrary and indistinguishable from random. It is important to note that this hyperparameter has a significant impact on the results (as mentioned in their rebuttal). Furthermore, the authors rely excessively on heuristic-based experimental settings for other baselines, which undermines the credibility of their comparative results.

2- The authors have not thoroughly reviewed the related work, which obscures the clarity of the novelty.

### Questions
Can the authors clarify the specific differences between the "ZERO-SHOT" methodology presented in this paper and established inductive settings in graph neural networks?

### Soundness
2

### Presentation
2

### Contribution
1

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper investigates the zero-shot generalist graph anomaly detection (GAD) problem, aiming to train a one-for-all model that works on all potential datasets. A new method termed UNPrompt with several designs (including prompt tuning, attribute predictability, etc.) is provided. Experiments on both generalist and traditional settings are conducted to show the effectiveness of the proposed method.

### Strengths
1. The research problem of zero-shot generalist GAD is both challenging and intriguing, offering the potential to inspire further innovation within the GAD research community.
2. The proposed method is thoughtfully designed with a balance of sophistication and simplicity, making it accessible for future researchers to build upon.
3. Extensive experiments conducted across diverse scenarios demonstrate the practical effectiveness and versatility of the proposed approach.

### Weaknesses
1. The experimental details are not given clearly in the paper. Which graph datasets are used to train the model (for pre-training and/or prompt tuning)? 
2. In the experiments, only 4 different datasets are used for evaluation (Amazon-all and YelpChi-all can be regarded as an extended version of the original ones). In this case, the generalized ability of the proposed method can't be fully verified. In this case, more datasets from different domains are expected in the experiments.
3. Why coordinate-wise normalization plays a critical role in the performance of UNPrompt? More explanation is expected.

### Questions
The authors are expected to answer the questions listed in Weaknesses. Apart from these, I have the following questions:
1. As ARC (Liu et al 2024) is another generalist GAD method, can you further discuss the difference between UNPrompt and ARC? Is that possible to compare them together (even though their settings are slightly different)?
2. The "attribute predictability" looks similar to the "local affinity" in TAM (Qiao and Pang 2023). In this case, will the performance drop significantly if we replace this design with local affinity?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The authors propose a zero-shot generalist GAD approach, UNPrompt. Specifically, they introduce two components: coordinate-wise normalization to unify node attributes across different graphs, and neighborhood prompt learning, which leverages latent node attribute predictability as an anomaly measure. Experiments show their framework can outperform baselines on datasets included in this paper.

### Strengths
S1. The paper is easy to follow. 

S2. The authors propose a zero-shot generalist GAD approach including two main components, Coordinate-wise Normalization and neighborhood prompt learning. 

S3. Experiments show their framework can outperform baselines on datasets included in this paper.

### Weaknesses
W1. The Coordinate-wise Normalization component is hardly considered as a contribution in this paper. As stated in the paper, the authors simply follow the previous work in the related areas to apply the Coordinate-wise Normalization, so the authors need to explain the differences between their design and framework from others. Otherwise, this component can only be considered as an implementation, not a contribution. 

W2. The Latent Node Attribute Predictability is similar to Local Affinitiy in TAM. This anomalous score function shares a similar form of Local Affinitiy in TAM. Although the authors provide a comparison in Figure 3(b), they need to further explain the result. To be specific, changing the objective function in an unsupervised learning framework but not tuning hyperparameters carefully is hard to lead to optimal results. The authors need to illustrate whether they use the same hyperparameters as Latent Node Attribute Predictability for Local Affinitiy or they fine-tune optimal hyperparameters for Local Affinitiy in the comparison. 
W3. The Neighborhood Prompting Learning follows the previous framework. Graph prompt learning has been utilized in several downstream applications, but the authors still follow the typical design of it. They need to further explain the differences between their design and other graph prompt learning frameworks to show their contributions. Otherwise, this key component can have the same issue as W1. 

W4. The setting of the hyperparameters is not explained well. For example, for the unsupervised setting of UNPrompt, the authors use the "40th percentile of the normal scores" as the threshold to generate pseudo labels. However, the real anomalous rate is far less than this, which leads to many false pseudo-labels in this setting. They need to explain why they chose such a hyperparameter. Besides, they only provide the hyperparameter sensitivity of the number of prompts. It would be better to include the analysis of other hyperparameters. 

W5. The datasets and baselines are not diverse enough. For datasets, the authors only include "social networks" and "co-review", which may share similar structural information. It would be better to include financial networks, like T-Finance[1]. For baselines, the most recent supervised work included in this paper is GHRN and unsupervised work is TAM, but XGBGraph[1] and GADAM[2] are two novel works in this area, separately. In addition, since Coordinate-wise Normalization is a very common design when compared with baselines, it would be better to include such a technique for baseline models.

### Questions
Q1. Can the pre-trained model use a different dataset other than Facebook to train and still get good performance? 

Q2. Can the framework be used for large-scale datasets, like Elliptic[1]? 

Q3. Can UNPrompt still outperform other baselines after they use the Coordinate-wise Normalization technique? 


Reference: 

1. Jianheng Tang, Fengrui Hua, Ziqi Gao, Peilin Zhao, Jia Li. GADBench: Revisiting and Benchmarking Supervised Graph Anomaly Detection. NeurIPS 2023. 
2. Jingyan Chen, Guanghui Zhu, Chunfeng Yuan, Yihua Huang. Boosting Graph Anomaly Detection with Adaptive Message Passing. ICLR 2024.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper proposes a novel zero-shot generalist Graph Anomaly Detection (GAD) approach called UNPrompt, which aims to train a unified detection model. The approach achieves generalist GAD through two key modules: the first module aligns the dimensionality and semantics of node attributes across different graphs by employing coordinate-wise normalization in a projected space. The second module focuses on learning generalized neighborhood prompts that leverage the predictability of latent node attributes as an anomaly score across various datasets.

### Strengths
1. The experiments are detailed and demonstrate strong performance.
2. The paper is well-organized.
3. The work addresses a novel problem in a new context: zero-shot Graph Anomaly Detection (GAD).

### Weaknesses
1. The theoretical innovation is insufficient. The concept of Neighborhood Prompting appears to encompass an all-in-one method in [1], and the method of coordinate-wise normalization is not novel. The paper does not sufficiently address the unique challenges associated with applying these methods to GAD.
2. The consideration of graph anomalies is inadequate. The evaluation focuses primarily on graph uniformity or high node connectivity as criteria for determining anomalies, while neglecting the importance of attribute features.
3. The writing needs improvement; the paper contains too many lengthy sentences, making it difficult to read and understand.
4. No code provided

### Questions
1. What are the unique challenges of prompt learning in Graph Anomaly Detection (GAD)?
2.  In Formula 2, the mean value will also be large when the difference in features between the two datasets is large. So, how can the two data be projected to the same space?
3. How are potential negative values from Formula 2 handled?
4. Formulas 4 and 5 suggest that the authors only consider graph uniformity or high node connectivity as criteria for determining anomalies. This design seems somewhat superficial, as anomalous nodes may also be related to node attributes.
5. Does Neighborhood Prompting involve learning a prompt for each node's neighbours? If the added prompts alter the neighbour features of *x*, could this affect the detection of anomalies?

### Soundness
3

### Presentation
2

### Contribution
1
