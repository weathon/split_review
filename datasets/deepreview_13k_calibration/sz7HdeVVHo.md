# Structure-preserving contrastive learning for spatial time series

- Decision: Reject
- Avg Score: 5.25
- Scores: 6, 5, 5, 5

## Abstract
Informative representations enhance model performance and generalisability in downstream tasks. However, learning self-supervised representations for spatially characterised time series, like traffic interactions, poses challenges as it requires maintaining fine-grained similarity relations in the latent space. In this study, we incorporate two structure-preserving regularisers for the contrastive learning of spatial time series: one regulariser preserves the topology of similarities between instances, and the other preserves the graph geometry of similarities across spatial and temporal dimensions. To balance contrastive learning and structure preservation, we propose a dynamic mechanism that adaptively weighs the trade-off and stabilises training. We conduct experiments on multivariate time series classification, as well as macroscopic and microscopic traffic prediction. For all three tasks, our approach preserves the structures of similarity relations more effectively and improves state-of-the-art task performances. This approach can be applied to an arbitrary encoder and is particularly beneficial for time series with spatial or geographical features. Our code is attached as supplementary material, which will be made openly available with all resulting data after review.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper proposes a time series contrastive learning loss with topology-preserving or graph-geometry preserving regularization. I appreciate the sufficient experiment made by the authors, but the novelty and originality of this paper are unclear.

### Strengths
- The proposed method can enhance SOTA performance on various datasets.
- The writing is good, and the paper is easy to follow.

### Weaknesses
 - About novelty. The idea of measuring topology similarity or preserving graph geometry has been extensively studied in existing literatures. What is the key insight of this paper that is different from existing works? Specifically, while the paper claims to use these techniques for time series, the core idea of preserving structural relationships through contrastive learning is not fundamentally new. The novelty claim would be stronger with a more detailed explanation of how the specific characteristics of time series data necessitate a different approach compared to image or other data types where these techniques have been applied.
- About originality. As described in Sec3.2 and Sec3.3, the proposed method adopts many existing technics, including TS2Vec loss, SoftCLT loss and topology-preserving loss. What is the origin idea or content of this work? The paper combines these existing techniques, but it lacks a clear, original contribution in terms of novel loss functions, architectural designs, or theoretical insights. The adaptive balancing mechanism is mentioned, but its novelty and impact are not fully justified. The paper needs to clearly articulate what specific problem it solves that existing methods fail to address and how the proposed method uniquely achieves this.

### Questions
See Weaknesses.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper extends time series contrastive learning by incorporating two structure-preserving regularisers: one preserves the topology of similarities between instances, and the other preserves the graph geometry of similarities across spatial and temporal dimensions. And, the proposed method preserves the structures of similarity relations more effectively and improves state-of-the-art task performances for all three tasks.

### Strengths
1. The topic of time series analysis is important to the ICLR community.

2. The proposed Structure-preserving contrastive learning is novel, which can enhance model performance and generalisability in downstream tasks.

3. The presentation is good and the experimental evaluation is adequate.

### Weaknesses
1. In terms of experimental evaluation, this paper does not analyze the efficiency of the proposed method, making the evaluation of the model incomplete.

2. In the experimental part, the ablation experiment of key modules in the model is not carried out, which makes the effectiveness of the designed module difficult to be verified.

3. In traffic prediction evaluation, some important baseline models in the field of traffic prediction were not used, making the performance comparison experiments less convincing.

### Questions
1. The UEA datasets this paper used omit the two largest, InsectWingbeat and PenDigits, due to limited computation resources. Does this mean that the proposed method has limitations when dealing with large datasets?

2. See Weaknesses.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The paper aims to improve contrastive learning for spatiotemporal data. Building upon existing time series self-supervised representation learning methods, namely TS2Vec and SoftCLT, the paper adds two structure-preserving regularisers to the pre-training process. The topology-preserving loss 
$\mathcal{L}\_{topo}$
is borrowed from Topological Autoencoders by Moor et al., 2020, while the graph-geometry-preserving loss 
$\mathcal{L}\_{GGeo}$
is borrowed from Graph Geometry-Preserving Autoencoders by Lim et al., 2024.

The paper then applies six combinations of pre-training losses on the UEA datasets by Bagnall et al., 2018 and two traffic prediction datasets. In all datasets, it is evident that adding structure-preserving regularizers improves prediction performance.

### Strengths
The question that the paper is asking is very important. Applying self-supervised representation learning techniques to multivariate time series is relatively unexplored. Many previous works focus on improving encoder architecture, and the techniques introduced in this paper are general and applicable to all deep learning models in this field.

The paper brings concepts from autoencoder regularization techniques to time series contrastive learning, forcing the distance of samples in the input space and latent space to be similar. This bridge of ideas is creative and original. The paper also introduces the background information very well, allowing the readers to fully understand the motivation behind these regularizers and how they can be used in spatiotemporal data. The overall framework is intuitive.

The paper also runs extensive experiments on two datasets, comparing the effect of using only contrastive losses and using them with the structure-preserving regularizers.

### Weaknesses
 * **Experimental design**: 
   * The paper lacks the "No Pre-training" baseline on the UEA datasets (this setting is included in the traffic prediction datasets). The baseline method should use only the vanilla models (i.e. models without constrastive loss or regularizers). It is unclear why the authors chose to use an RBF-kernel SVM for classification on the UEA datasets, as opposed to a simple linear decoder, which would be more consistent with the traffic prediction experiments and allow for a direct comparison with a no pre-training baseline using the same encoder architecture. This makes it difficult to isolate the effect of the proposed regularizers.
   * The paper does not include the training configurations (e.g. hardware specs, the GPUs/CPUs used during training, the training time, and the training/validation/test data splits ratio
    * The paper does not discuss if contrastive pre-training decreases overall training time, which is important in practice. To address this, the paper could include a plot with training time as the x-axis, test accuracy on the y-axis, and 2 curves showing 1. finetuning from scratch 2. finetuning from pre-training. For instance, see Figure 5. in Masked Autoencoders As Spatiotemporal Learners by Feichtenhofer et al., 2022.
    * Since the paper is examining the effect of contrastive learning and structure regularizers in the latent space, more baseline models should be tested in combination such as DCRNN, STGCN, Graph WaveNet, etc. These models are important spatiotemporal forecasting models that can provide more evidence for the effectiveness of the method.

* **Writing clarity**:
    * The term $r_{\eta}$ is only explained to "regularisation against overfitting of the dynamic weights", but is not further mentioned in the methods section or hyperparameter search. 
    * It is difficult to understand what the bold and underlining mean in Tables 5, 6, 7. Perhaps adding a detailed caption for the tables helps.
    * There is no explanation on why "No-Pretraining" has the best structure preserving metrics on traffic prediction. This is counter-intuitive since the baseline does not force the distance between samples in the original and latent space to be similar. Furthermore, the paper should clarify whether the structure preservation metrics are calculated on the training, validation, or test set, as this could affect the interpretation of the results.
    * In Table 1, maybe explain the abbreviations of batch size and learning rate in the caption or footnote.
    * Lines 468-472 are hard to understand without giving specific measures for improvement e.g. using GGeo + TS2Vec improved performance by x%. It is impossible to know in "These methods are also those showing sub-optimal performances in prediction", what "These methods" are specifically. The paper should provide rephrase the paragraph by giving specific improvement examples and analyzing the results in more detail. 

* **Typos**
    * Line 84-85 SOTA abbreviation should be in the introduction at the first mention
    * Line 423-424 whereas it does when together with preserving similarity structure >> whereas it does when used together with preserving similarity structure

### Questions
* What are the details of the model used for fine-tuning, which model is used for traffic prediction?
* For the evaluation metrics (e.g. dRMSE), how are the distances measured in datasets with spatial features vs. without spatial features? Do you account for the edge distances between connected nodes? Are they the same when calculating the structure regularizer losses (e.g. $\boldsymbol{A}$ in equation 7)?
* The graph structures in many of these datasets are static, i.e. the graph doesn’t change over time, is it still appropriate to use structure-preserving regularizers from these graph autoencoders?
* What do the colors of the nodes in Figure A1. represent? Are they the classes of the samples? Are the latent representations obtained during pre-training or after fine-tuning?
* The paper leaves many questions unanswered. The goal here is to examine the effectiveness of structure-preserving regularizers in spatiotemporal data contrastive learning, yet the paper only shows prediction improvements without explaining why one regularize works better than the other. For example, if $\mathcal{L}\_{topo}$ performs better than $\mathcal{L}\_{GGeo}$ on macroscopic traffic prediction, what does this tell us about the dataset and the loss function? Under what circumstances would $\mathcal{L}_\{GGeo}$ do better than $\mathcal{L}\_{topo}$? This could be better answered by evaluating them on the same topology dataset such as the Sphere or the Swiss Roll dataset to interpret the results better and understand the self-supervised representations. There is also no explanation on why TS2Vec performs better than SoftCLT in certain scenarios.

### Soundness
2

### Presentation
2

### Contribution
3

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This article investigates structure-preserving flow prediction models, emphasizing the balance between data-driven approaches and simulation-based methods. The authors present a novel model that aims to enhance the accuracy of flow predictions by leveraging a combination of node-level and edge-level features. The proposed method is built on existing frameworks but introduces modifications to improve performance in predicting flow across graphs.
Specifically, it describes the methodology in detail, outlining how the model integrates various features such as topological, geographical, and temporal data to optimize flow predictions. It employs a two-step approach: first, it analyzes the historical flow data to identify patterns, and second, it applies simulation techniques to predict future flows based on these identified patterns. The theoretical foundation is supported by mathematical formulations that establish the relationships between flow, costs, and node attributes.

### Strengths
1 The paper provides a robust theoretical analysis, detailing the mechanics of flow prediction models. It includes mathematical derivations that clarify the relationships between various graph features and flow dynamics.
2 The proposed model incorporates a unique combination of simulation techniques and feature extraction from node and edge data. This method aims to closely approximate actual flow while maintaining computational efficiency.
3 The experiments are well-structured, comparing the proposed method against existing approaches. The results demonstrate the effectiveness of the model in various scenarios, showing improvements in prediction accuracy.

### Weaknesses
1 Despite the improvements made, the overall approach does not significantly advance the field of flow prediction. The methods employed largely build upon established techniques without introducing truly innovative concepts or frameworks. Specifically, the core methodology appears to be an incremental improvement over existing graph-based flow prediction models, lacking a novel theoretical contribution or a significant departure from current practices. The modifications to feature integration and simulation techniques, while potentially effective, do not represent a paradigm shift in how flow prediction is approached.
2 The scope of the datasets used in the experiments is somewhat restricted. This limitation may impact the generalizability of the results, raising questions about how well the method would perform in diverse real-world scenarios. The datasets appear to be limited in terms of size and variety, potentially not capturing the full complexity of real-world flow dynamics. For example, the experiments do not seem to include datasets with highly irregular or unpredictable flow patterns, which could expose limitations in the model's robustness.

### Questions
The novelty of this paper primarily lies in its enhancements to pre-existing methodologies. While the authors make contributions to the understanding of flow prediction, these modifications do not represent a big enough step forward in the field. Many of the techniques discussed are already prevalent in the literature, lacking the introduction of new paradigms or theoretical frameworks.

### Soundness
3

### Presentation
2

### Contribution
1
