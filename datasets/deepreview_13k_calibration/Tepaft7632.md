# MADCluster: Model-agnostic Anomaly Detection with Self-supervised Clustering Network

- Decision: Reject
- Avg Score: 4.80
- Scores: 5, 3, 6, 5, 5

## Abstract
In this paper, we propose MADCluster, a novel model-agnostic anomaly detection framework utilizing self-supervised clustering. MADCluster is applicable to various deep learning architectures and addresses the 'hypersphere collapse' problem inherent in existing deep learning-based anomaly detection methods. The core idea is to cluster normal pattern data into a `single cluster' while simultaneously learning the cluster center and mapping data close to this center. Also, to improve expressiveness and enable effective single clustering, we propose a new 'One-directed Adaptive loss'. The optimization of this loss is mathematically proven. MADCluster consists of three main components: Base Embedder capturing high-dimensional temporal dynamics, Cluster Distance Mapping, and Sequence-wise Clustering for continuous center updates. Its model-agnostic characteristics are achieved by applying various architectures to the Base Embedder. Experiments on four time series benchmark datasets demonstrate that applying MADCluster improves the overall performance of comparative models. In conclusion, the compatibility of MADCluster shows potential for enhancing model performance across various architectures.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper targets on the model-agnostic anomaly detection
for time series and try to addresses the ‘hypersphere collapse’ problem in existing deep learning-based self-supervised clustering anomaly detection methods. The authors introduce learnable cluster center and one-directed adaptive loss to improve the Cluster Distance Mapping module and Sequence-wise Cluster module. The experiments on four time series benchmark datasets showcase that their method can further improve the performance of based model.

### Strengths
1. The paper is well-written and easy to follow.
2. The motivation of learnable cluster center and one-directed adaptive loss is clear and well proved through the experiments.

### Weaknesses
1. The paper does not present sufficient discussion of the reconstruction-based methods, which should be a very important type of methods in time series anomaly detection. More speficially, it seems that the authors can conbine their method with the reconstruction-based methods such as Anomaly Transformer and DCdetector. I wonder how to implement such conbination. Do you only use the network backbones from the Anomaly Transformer or DCdetector, or delivers a reconstruction loss (or even contrastive loss) together with your loss function?
2. There is no ablation study in the paper to demonstrate the independent function of learnable cluster center and one-directed adaptive loss. 
3. Some descriptions are inconsistent. For example, from line 221-225, only the neural network weights W and the cluster center parameters c are learnable. However, from the experiments, the radius R is also learnable. Additionally, it is quite strange to optimize c seperately with equation (6) but use adam to optimze other parameters.
4. The discussion for one-directed adaptive loss function is not so clear and sufficient in the main paper. Even though the detailed explanation is provided in the appendix, the authors are suggested to provide a short but more clear and intuitive explanation about how equation (4) is developed in the main paper.
5. More comparison with the pretrained methods for TS anamoly detection should be discussed, such as TimesNet[1] and FPT[2].

### Questions
1. How to implement your method with reconstruction-based anamaly detection methods?
2. Any ablation study for learnable cluster center and one-directed adaptive loss?
3. It is possbile to implement your method with some pre-trained TS foundation models?

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The authors propose MADCluster, a model-agnostic anomaly detection framework by self-supervised clustering with a one-directed adaptive loss. The authors also address the hypersphere collapse problem for clustering-based anomaly detection methods.

### Strengths
1. The authors propose MADCluster, a model-agnostic anomaly detection framework.
2. The authors propose a one-directed adaptive loss for single clustering.
3. The authors address the hypersphere collapse problem in the clustering-based anomaly detection methods.

### Weaknesses
1. The claimed novelty in this paper is Model-Agnostic. But the authors did not compare with any Model-Agnostic anomaly detection models, such as [1] and [2]. The authors should include these related works in one section, compare these prior works by experiments, and provide a detailed comparison highlighting the key technical differences and innovations compared to these previous works.

    [1] Towards Lightweight, Model-Agnostic and Diversity-Aware Active Anomaly Detection. ICLR 2023.

    [2] Distribution Agnostic Symbolic Representations for Time Series Dimensionality Reduction and Online Anomaly Detection. TKDE 2023.

2. There are no experiments to show or theoretical proof of why updating central coordinates through network parameters can address the hypersphere collapse problem. More experiments or analyses would help demonstrate how or why updating central coordinates prevents hypersphere collapse, for example, using some quantitative metrics and ablation studies to show this effect.

3. The authors argue that they address the hypersphere collapse problem by preventing the all-zero parameter problem. However, the hypersphere collapse problem is not only the all-zero parameter problem but also related to the mode collapse problem, as shown in [3] and [4]. The claim from this paper is not sound. The authors should include these related works in one section, compare these prior works by experiments, and provide a detailed comparison highlighting the key technical differences and innovations of their method.

    [3] Exploring Simple Siamese Representation Learning. CVPR 2021.

    [4] MHCCL: Masked Hierarchical Cluster-Wise Contrastive Learning for Multivariate Time Series. AAAI 2023.

4. The main weakness of this paper is that the authors use the wrong evaluation metrics. The authors use the point adjustment (PA) for evaluation. Many works [5, 6, 7] have demonstrated that PA can lead to faulty performance evaluations, where PA use true labels from the test datasets to adjust the outputs of models, and it is known that using PA can result in state-of-the-art performance even with random scores or random initialized non-trained models [6, 7], making it impossible to conduct a fair comparison and assess the effectiveness of the models. The showed effectiveness in this paper is flawed. The authors should use alternative evaluation metrics, such as original F1, ROC-AUC, PR-AUC, Aff Recall, Precision and F1 [6, 7], instead of PA. The authors should re-run their experiments with these reasonable metrics and discuss how it impacts their results and conclusions.

    [5] Current Time Series Anomaly Detection Benchmarks are Flawed and are Creating the Illusion of Progress. TKDE 2023.

    [6] Drift doesn't Matter: Dynamic Decomposition with Diffusion Reconstruction for Unstable Multivariate Time Series Anomaly Detection. NeurIPS 2023.

    [7] Local Evaluation of Time Series Anomaly Detection Algorithms. KDD 2022.

### Questions
see weaknesses.

### Soundness
1

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper introduces MADCluster, a model-agnostic anomaly detection framework that uses self-supervised clustering. It addresses the "hypersphere collapse" issue in deep learning-based anomaly detection methods by dynamically learning cluster centers to group normal patterns in a single cluster. Experiments on time-series datasets demonstrate that MADCluster enhances the performance of various baseline models, showcasing its flexibility and effectiveness in anomaly detection.

### Strengths
1.MADCluster is easy to adapt to a wide range of neural network architectures and effectively enhances the performance of base models.

2.The framework's dynamic update of cluster centers prevents hypersphere collapse, ensuring a more expressive feature space.

3.The writing of this paper is clear and well-structured.

### Weaknesses
1.The paper lacks a detailed analysis of time and computational costs, particularly a comparison between the original base model and the model combined with MADCluster.

2.The performance improvement observed in advanced methods like DCdetector appears to be less than in simpler methods such as D-RNN. Does this suggest a limitation in the effectiveness of MADCluster when feature quality is already high?

3.It appears that MADCluster is not specifically designed for time-series anomaly detection. Have you explored the generalizability of this method to other domains, such as tabular data or image data?

### Questions
See weakness above.

### Soundness
3

### Presentation
3

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
This paper proposes MADCluster, a model-agnostic framework for anomaly detection that addresses the "hypersphere collapse" issue common in deep anomaly detection methods. MADCluster introduces self-supervised clustering to adaptively learn the cluster center, enabling it to capture normal data patterns in a centralized latent space, thus highlighting deviations as anomalies. The authors present a novel One-directed Adaptive Loss to support clustering into a single cluster, ensuring high intra-cluster similarity for normal data. By combining the Base Embedder, Cluster Distance Mapping, and Sequence-wise Clustering modules, MADCluster achieves adaptability across diverse neural network architectures.

### Strengths
1. The design of MADCluster allows integration with various deep learning models, making it broadly applicable across different network architectures. This adaptability offers potential practical value, as MADCluster may serve as a plug-and-play solution in different anomaly detection contexts.

2. The authors evaluate MADCluster on multiple real-world datasets, demonstrating consistent improvements across diverse models in terms of different metrics. 

3. The authors release the source-code, which improves the reproducibility.

### Weaknesses
1. MADCluster avoids the “hypersphere collapse” problem of traditional one-classification methods by dynamically updating the clustering centers of normal data. However, the reviewer is concerned that when the distribution of normal data is complex or there are multiple local clusters, a single dynamic center may not be sufficient to accurately describe the normal pattern, which may lead to boundary-blurring or false detection. Can the authors discuss this issue?

2. The one-directed adaptive loss proposed in this work is centered on the idea of gradually increasing the threshold to cluster normal data into single clusters, but it has not yet been fully verified whether this design is effective in distinguishing anomalous samples that slightly deviate from the normal clusters. No quantitative or ablative analysis of the performance of this loss function on the model is provided in the paper.

3. In the experimental part, MADCluster is mainly compared with methods such as D-RNN and USAD, but these baseline models do not cover the latest self-supervised or GAN-based anomaly detection methods, which may outperform the traditional methods on multimodal time series data. To ensure the comprehensiveness of the experimental results, it is recommended to introduce the latest baseline models to support the effectiveness of MADCluster.

4. The title of this paper seems to suggest that MADCluster can broadly be applied across various data types. However, the experimental validation is limited to time-series datasets, with no testing on other data types (e.g., structured tabular data, graphs, images). This creates a discrepancy between the title’s generality and the paper’s scope. To better align the title with the paper’s content, 
 the reviewer recommends either specifying the application to time-series data in the title or adding experiments on diverse data types to substantiate the claim of model-agnostic applicability.

### Questions
See weakness.

### Soundness
2

### Presentation
2

### Contribution
3

---

## Human Reviewer 5

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper introduces a model-agnostic anomaly detection approach that incorporates a novel self-supervised clustering step to mitigate hypersphere collapse issues in one-class classification methods. The approach leverages a sequence-wise clustering mechanism that updates the central coordinates of the hypersphere via network parameters, using a one-directional adaptive loss function. The authors provide a mathematical formulation and analysis of the optimization process, showing that it achieves the intended effect. Experimental results on four benchmark datasets and comparisons with 11 baseline methods validate the approach’s effectiveness.

### Strengths
1.	Innovative Loss Function: The paper introduces a novel one-directional adaptive loss function designed to enable distance-based mapping through parameter updates. The authors carefully derive and discuss the impact of this mapping, demonstrating its ability to capture coherent anomalies in similar regions and reduce inconsistent labeling among similar data points. The derivation is thorough and mathematically well-supported, enhancing the approach’s theoretical soundness.
	2.	Extensive Comparative Analysis: The method’s model-agnostic capability is demonstrated by applying it across a variety of deep learning models and comparing results with over ten baselines. The qualitative results indicate that the proposed method learns a more expressive and meaningful representation for hypersphere construction, which strengthens its potential for effective anomaly detection.

### Weaknesses
1.	Limited Innovation Scope: The paper aims to address hypersphere collapse, which is already a well-explored issue in a one-class classification problem (DASVDD, THOC). The clustering-based approach itself is not novel as well (DEC). Although the one-directional adaptive loss function represents an interesting advancement, the extent to which it genuinely enhances anomaly detection is unclear. For example, from Figure 2 it's hard to tell if there is an improved performance in (c) over (b) when distance mapping is employed, as the performance largely depends on the definition of the anomaly. The core idea of using a clustering objective to guide the hypersphere learning is not fundamentally new, and the specific contribution of the proposed loss function needs more rigorous justification beyond the qualitative illustration in Figure 2. The method appears to be an incremental improvement over existing techniques rather than a significant breakthrough.
	2.	Marginal Performance Gains: Table 1 shows consistent improvements for MADCluster over baselines across datasets, but the gains appear marginal (if we compare the best performer with the second best one, for example) and might lack statistical significance. The reported improvements, while consistent, are not substantial enough to demonstrate a clear advantage over existing state-of-the-art methods. The absence of standard deviations makes it difficult to assess the robustness of these results and whether the observed differences are statistically meaningful. The lack of statistical significance testing further weakens the claims of performance improvement, making it hard to ascertain if the gains are due to the method itself or random variations.
	3.	Need for Ablation Study: An ablation study on the F1 scores across different datasets, specifically isolating the contributions of clustering and distance mapping, would offer stronger evidence of each component’s effectiveness. Relying solely on the illustration in Figure 2 limits the understanding of their respective roles in the overall framework. Furthermore, the paper does not explore the sensitivity of the method to the hyperparameter choices, such as the number of clusters or the learning rate for the adaptive loss, which could significantly impact the performance. A thorough ablation study should also include the impact of different initialization strategies for the cluster centers.

### Questions
•	Can you clarify how your approach uniquely addresses hypersphere collapse beyond existing methods? Specifically, what is the key contribution of your one-directional adaptive loss function compared to prior approaches?
	•	How do you define an “anomaly” within the context of your method? Can you provide a clearer explanation of how your distance-based mapping approach influences anomaly detection outcomes?
	•	In Figure 2, it’s challenging to see a distinct improvement from adding distance mapping in subfigure (c) versus (b). Can you provide additional analysis or quantitative comparisons to clarify how the mapping contributes to anomaly coherence and detection accuracy?

### Soundness
3

### Presentation
4

### Contribution
2
