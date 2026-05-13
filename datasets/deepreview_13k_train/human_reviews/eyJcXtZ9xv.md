# Modeling Spatiotemporal Heterogeneity in Earth Science Machine Learning: An End-to-End Approach

- Decision: Reject
- Scores: 6, 3, 3, 3

## Abstract
In Earth sciences, unobserved factors often lead to spatially nonstationary distributions, causing relationships between features and targets to vary across locations. Traditional tabular machine learning methods struggle to effectively model this spatial heterogeneity. While approaches like Geographically Weighted Regression (GWR) capture local variations, they often miss global patterns, overfit local noise, and lack the ability to model temporal changes in spatial heterogeneity. Our research aims to model spatiotemporal heterogeneity. To achieve this, we propose an end-to-end approach that fits the entire dataset to capture global patterns, while designing the model as a conditional generative framework to learn sparse spatial heterogeneity, mitigating overfitting through localized condition sharing. Our method involves four key steps: constructing a spatiotemporal graph, encoding tabular features, aggregating spatial heterogeneity node embeddings via graph convolutions, and decoding with spatial condition vectors for location-specific predictions. We validate our approach by predicting vegetation gross primary productivity (GPP) using global climate and land cover data (2001–2020). Trained on 50M samples and tested on 2.8M, our model achieves an RMSE of 0.836, outperforming GWR (2.149), LightGBM (1.063) and TabNet (0.944). Visual analysis of the learned node embeddings reveals clear spatial heterogeneity patterns and their temporal dynamics.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper proposes a novel graph neural network-based method to model spatiotemporal heterogeneity in Earth science data. It incorporates a Spatiotemporal Conditional Graph (STCG) to integrate both spatial and temporal data, capturing environmental changes dynamically. A dual attention mechanism within a transformer architecture enhances the model's ability to handle complex dependencies across time and features. The effectiveness of the proposed method is demonstrated using real-world data sets.

### Strengths
- The entire modeling process, from data preprocessing to final prediction, is optimized end-to-end. This unified approach ensures that the model learns generalized features across the entire dataset, which helps in enhancing predictive accuracy.
- The manuscript is well-written.
- Although the proposed approach is simple and a combination of several elements, the way it is combined is reasonable and practically useful.
- The effectiveness of the proposed method is demonstrated using real-world data sets.

### Weaknesses
The technical contribution of the proposed method is incremental. There have been proposed many deep learning methods for spatiotemporal modeling, such as graph neural networks and Transformers. The proposed method is a combination of graph neural networks and self-attention models. The experimental results are not convincing. Comparison with deep learning methods for spatiotemporal data is needed to clarify the effectiveness of the proposed method.
Although the authors describe that the proposed method is an end-to-end approach, there are many components that are not trained in an end-to-end fashion; i.e., clustering of spatial regions, graph construction, initial node embedding, and edge weight calculations.

### Questions
- I did not understand how the cluster center C in section 3.1 is used in the architecture. Could you please explain in detail?
- The edge weight is calculated based on Euclidean distance, but is it necessary to use other geometric distances when considering a spherical surface like the earth?
- Is it possible to do a detailed analysis of the prediction results? For example, do the errors differ from region to region? Are local and global dynamics really captured? Are there any areas where the error is locally larger?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
This paper introduces a novel end-to-end framework for modeling spatiotemporal heterogeneity in Earth science data using a conditional generative approach. The authors propose a model that leverages GNNs and transformer-based encoding to handle spatial and temporal dependencies simultaneously. Through the Climate2GPP dataset, the method demonstrates superior performance over established techniques such as GWR, LightGBM, and TabNet in predicting GPP.

### Strengths
The topic is interesting. The visualization of results is clear and well-designed. Applying the proposed method to a large-scale dataset is both challenging and impactful.

### Weaknesses
+ 1. In line 175, the authors project geographic coordinates onto a three-dimensional unit sphere. For a large number of nodes, this could lead to computational overhead, especially considering the need to compute distances between all pairs of nodes in this space. Additionally, this projection assumes the Earth is a perfect sphere, but in reality, the Earth is a slightly flattened ellipsoid. Therefore, spherical projection may introduce some inaccuracies in certain cases, particularly when dealing with long-range spatial dependencies. Moreover, this method cannot effectively capture true geodesic distances, which are crucial for accurate spatial modeling on the Earth's surface.

---

+ 2. In line 185, the authors use the node2vec embedding method to calculate initial node representations. From my past experience, this algorithm has a certain time cost, especially for a large number of nodes and edges, as it requires multiple random walks for each node. I remain skeptical about its time complexity, and the use of node2vec initialization seems to contradict the end-to-end approach mentioned by the authors in the abstract, as it introduces a pre-processing step that is not jointly optimized with the rest of the model.

---

+ 3. In Section 3.2, the entire spatio-temporal conditional encoding process is not novel, as it can be found in various spatio-temporal graph learning methods [1, 2]. Specifically, the use of graph neural networks to encode spatial dependencies and recurrent networks to capture temporal dynamics is a common practice. However, the authors have entirely neglected to cite relevant work, which makes it difficult to assess the novelty of their approach.

---

+ 4. In Section 3.3, the table representation aggregation process is also not novel, as it essentially amounts to a simple application of linear attention. Considering there are many alternatives[3, 4], such as kernel-based attention or sparse attention mechanisms, the authors have not explained why they chose this approach, nor have they provided any justification for its suitability in the context of their problem. The lack of ablation studies further hinders the evaluation of this design choice.

---

+ 5. In line 266, the details of the decoder are completely missing. If space constraints were an issue, they should have been discussed in the appendix. However, it is clear the authors are not restricted by space here. The absence of decoder details makes it difficult to understand the complete architecture and assess its potential impact on the results.

---

+ 6. There is a lack of empirical experiments related to efficiency. The authors should provide a detailed analysis of the computational cost of their method, including training time, inference time, and memory usage, especially when compared to baseline methods. This is crucial for evaluating the practical applicability of the proposed approach.

### Questions
1.	Will the dataset and code used in this study be made publicly available? 

2.	The study uses data from 2001-2019 for training and data from 2020 for testing. Given the significant environmental and impacts of COVID-19 in 2020, is it possible that this anomaly could affect the model’s predictions?

### Soundness
2

### Presentation
2

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
This paper proposes a graph neural network-based method for modeling spatiotemporal data. In the experiments, the proposed method achieved the better performance than the existing tabular machine learning, tabular deep learning methods, and geographically weighted regression.

### Strengths
Proposed a new method for earth science.
Experiments with global data.

### Weaknesses
The technical contribution of the proposed method is incremental. There have been proposed many deep learning methods for spatiotemporal modeling, such as graph neural networks and Transformers. The proposed method is a combination of graph neural networks and self-attention models. The experimental results are not convincing. Comparison with deep learning methods for spatiotemporal data is needed to clarify the effectiveness of the proposed method.
Although the authors describe that the proposed method is an end-to-end approach, there are many components that are not trained in an end-to-end fashion; i.e., clustering of spatial regions, graph construction, initial node embedding, and edge weight calculations.

### Questions
What is the main contributions of this paper compared with the existing deep learning methods for spatiotemporal data?

### Soundness
2

### Presentation
3

### Contribution
1

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
In this paper, the authors propose a conditional generative model with local parameter sharing to replace explicit geographic and temporal weighting models. This reduces the risk of overfitting caused by dense spatio-temporal weights and improves performance in Earth Sciences Forecasting.

### Strengths
+ 1. The goal of this paper is to address an important real-world problem: achieving spatio-temporal forecasting from Earth science-related data. This research problem is meaningful because spatio-temporal forecasting in Earth sciences help humans understand the dynamic changes in the Earth's systems and can be applied to important areas such as agriculture and social activities.

---

+ 2. The core idea of the paper is to avoid the overfitting problem caused by global dense spatio-temporal weights by proposing a conditional generative model with local parameter sharing.

---

+ 3. The authors' writing is clear and easy to understand.

### Weaknesses
+ 1. In line 175, the authors project geographic coordinates onto a three-dimensional unit sphere. For a large number of nodes, this could lead to computational overhead. Additionally, this projection assumes the Earth is a perfect sphere, but in reality, the Earth is a slightly flattened ellipsoid. Therefore, spherical projection may introduce some inaccuracies in certain cases. Moreover, this method cannot effectively capture true geodesic distances.

---

+ 2. In line 185, the authors use the node2vec embedding method to calculate initial node representations. From my past experience, this algorithm has a certain time cost, especially for a large number of nodes. I remain skeptical about its time complexity, and the use of node2vec initialization seems to contradict the end-to-end approach mentioned by the authors in the abstract.

---

+ 3. In Section 3.2, the entire spatio-temporal conditional encoding process is not novel, as it can be found in various spatio-temporal graph learning methods [1, 2]. However, the authors have entirely neglected to cite relevant work.

---

+ 4. In Section 3.3, the table representation aggregation process is also not novel, as it essentially amounts to a simple application of linear attention. Considering there are many alternatives[3, 4], the authors have not explained why they chose this approach.

---

+ 5. In line 266, the details of the decoder are completely missing. If space constraints were an issue, they should have been discussed in the appendix. However, it is clear the authors are not restricted by space here.

---

+ 6. There is a lack of empirical experiments related to efficiency.

---
[1] Wu, Zonghan, et al. "Graph wavenet for deep spatial-temporal graph modeling." IJCAI 2019.
[2] Bai, Lei, et al. "Adaptive graph convolutional recurrent network for traffic forecasting." NIPS 2020.
[3] Shen, Zhuoran, et al. "Efficient attention: Attention with linear complexities."  CVPR 2021.
[4] Wang, Sinong, et al. "Linformer: Self-attention with linear complexity." arXiv 2020.

### Questions
+ 1. In line 42, the statement that the spatial distribution of missing variables being non-stationary implies that the relationship between the remaining features and the target variable changes with spatial location seems logically flawed to me. In my view, the spatial distribution of variables with spatiotemporal associations is generally non-stationary, regardless of whether data is missing or not.

---

+ 2. Why do the authors not summarize their main contributions at the end of the introduction, but instead scatter them throughout the paper? This makes it difficult to quickly identify their core contributions.

---

+ 3. I don’t quite understand Figure 3. Why is there such a large difference between GNNWR and GTWR compared to the other two figures? Shouldn’t spatial heterogeneity result in clear color separations across different regions? From this perspective, the GWR figure seems to capture this better.

---

+ 4. What is the time complexity of the proposed method?

### Soundness
1

### Presentation
2

### Contribution
2
