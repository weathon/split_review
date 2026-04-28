# Graph Neural Networks for Multivariate Time-Series Forecasting via Learning Hierarchical Spatiotemporal Dependencies

- Decision: Reject
- Avg Score: 3.50
- Scores: 3, 3, 5, 3

## Abstract
Multivariate time-series forecasting is one of the essential tasks to draw insights from sequential data. Spatiotemporal Graph Neural Networks (STGNNs) have attracted much attention in this field due to their capability to capture the underlying spatiotemporal dependencies. However, current STGNN solutions still fall short of providing trustworthy predictions due to insufficient modeling of the dependencies and dynamics at different levels. In this paper, we propose a graph neural network model for multivariate time-series forecasting via learning hierarchical spatiotemporal dependencies (HSDGNN). Specifically, we organize variables as nodes in a graph while each node serves as a subgraph consisting of the attributes of variables. Then we design two-level convolutions on the hierarchical graph to model the spatial dependencies with different granularities. The changes in graph topologies are also encoded for strengthening dependency modeling across time and spatial dimensions. We test the proposed model on real-world datasets from different domains. The experimental results demonstrate the superiority of HSDGNN over state-of-the-art baselines in terms of prediction accuracy.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper introduces a GNN-based architecture for multivariate time series forecasting where the relational information among the time series - the graph used by the GNN - is not given, but learned from data. In particular, the proposed method is designed for learning a dynamic graph which is structured into two levels to overcome limitations of previous work.

### Strengths
The ideas of constructing a hierarchical and dynamic graph are interesting and worth exploring. The empirical analysis reports improved performance with respect to the considered baselines.

### Weaknesses
My major concerns are the following:
- Several claims appear unsubstantiated, especially in the fourth paragraph of the introduction. References and/or pieces of evidence to support such claims should be provided. In particular, the claim that 'the temporal correlations regarding the changing spatial dependencies are not well-considered' lacks specific justification. It is not clear what aspect of temporal correlation is being neglected and why this is a significant limitation.
- The technical contribution is limited. The proposed method appears as a minor modification of existing works (e.g., Bai et al., 2020, Han et al., 2021, Weng et al., 2023). The core idea of using a GNN with learned graph structure is not novel, and the specific two-level hierarchical graph, while interesting, seems like an incremental improvement rather than a significant breakthrough. The paper does not adequately explain why this particular hierarchical structure is superior to other potential graph learning approaches.

- I am not fully convinced by the experimental setting. What is the relevance of learning a hierarchical graph in the considered setting where each location (variable in the paper terminology) has only three components? The use of a fully connected graph for attributes, as shown in Fig 9a with edge weights close to 1, suggests that the learned attribute graph is not adding much value. This raises questions about the necessity of the proposed hierarchical structure in the context of these experiments. Could you clarify what is used to replace the IDLM in `HSDGNN_w/o_IDLM` and the dynamic graph in `HSDGNN_w/o_DG`?

Confusing notation
- Sets and tensors appear to be used interchangeably, the tensor dimensionality is rarely provided. For example, it's unclear how the set of nodes is represented as a tensor for computation. The lack of explicit dimensionality makes it difficult to follow the mathematical formulations.
- Sec. 3.1 defines $\mathcal G_s$ as both a set and a graph. This dual definition is confusing and needs to be clarified. The paper should clearly distinguish between the set of nodes/edges and the graph structure.
- Eq. 6: $\mathbf W_{G_1}$ appear undefined, it is not clear what this matrix represents or how it is used in the computation. 
- Eq. 6: notation $\mid \mathbf W_{G_1}$ is undefined. The vertical bar notation is not standard and should be explained or replaced with a more common notation.
- Before Eq. 7: notation $\boldsymbol T_e(\mathbf X)$ is undefined. The paper should define this transformation and its purpose before using it in the equations.

### Questions
I am not fully convinced by the experimental setting. What is the relevance of learning a hierarchical graph in the considered setting where each location (variable in the paper terminology) has only three components? Fig 9a shows that the graph of attributes is a fully connected one, with all edge weights ~1. Could you clarify what is used to replace the IDLM in `HSDGNN_w/o_IDLM` and the dynamic graph in `HSDGNN_w/o_DG`?

Confusing notation
- Sets and tensors appear to be used interchangeably, the tensor dimensionality is rarely provided.
- Sec. 3.1 defines $\mathcal G_s$ as both a set and a graph.
- Eq. 6: $\mathbf W_{G_1}$ appear undefined, 
- Eq. 6: notation $\mid \mathbf W_{G_1}$ is undefined
- Before Eq. 7: notation $\boldsymbol T_e(\mathbf X)$ is undefined

### Soundness
2 fair

### Presentation
1 poor

### Contribution
1 poor

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper introduces a hierarchical spatial-temporal dependency graph neural networks (HSDGNN) for multi-variate time series forecasting. The proposed HSDGNN has two levels. At the first level, for each multi-variate time series collected at a sensory station, HSDGNN learns the dependencies (graph) of different variates, and then use a GRU to model temporal dynamics of each station. At the second level, HSDGNN learns a dynamic spatial-temporal graph among different sensory stations and then use another GRU to model the temporal dynamics of the entire graph. The model is evaluated on several benchmark datasets and the proposed method could outperform baselines.

### Strengths
1. The proposed model is technically sound. The graph learning, spatial modeling and temporal modeling are based on prior works, and thus the proposed HSDGNN should have a good performance.
2. The writing of the paper is clear and easy to follow.
3. The code is provided.

### Weaknesses
1. The contribution of this paper is somewhat incremental. The proposed method is kind of simple combination of existing methods [1][2][3]. The core idea of using a hierarchical approach with graph neural networks and recurrent units is not novel, and the specific implementation appears to be a straightforward application of these existing techniques. The paper lacks a strong justification for why this particular combination is significantly better than other possible combinations or existing approaches.
2. According to the results of ablation study (Table 3), it seems that IDLM (the intra graph) is less effective. The performance of the full model HSDGNN and the ablated version HSDGNN_w/o_IDLM does not have a significant difference. The ablation study does not provide sufficient evidence to support the necessity of the IDLM module, raising questions about its practical value and the overall complexity it adds to the model. The performance gain from IDLM is marginal, suggesting that the model might be over-parameterized.
3. How will your model perform if you simply replace IDML with some other simple static graphs (e.g., the graph constructed by Pearson Correlation or other prior knowledge)? The paper does not explore alternative methods for capturing intra-variable dependencies, such as using static graphs based on domain knowledge or statistical measures. This lack of comparison makes it difficult to assess the true contribution of the learned dynamic graph and whether the added complexity is justified.

### Questions
Please refer to weaknesses.

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper primarily improves two main shortcomings of previous STGNN models: 1) the lack of consideration of dependencies among attributes of variables. 2) insufficient consideration of the temporal correlations in dynamic spatial dependencies.
To address these two shortcomings, this paper proposes a model called HSDGNN for multivariate time-series forecasting problems. HSDGNN captures the spatiotemporal dependencies among variables at two levels: attribute and variable. It also utilizes an additional temporal learning module to capture the temporal correlations among dynamic graph topologies.
Experiments demonstrate that the proposed model achieves performance improvement compared to the state-of-the-art STGNN models, without increasing the model size.

### Strengths
1.	Originality:
This paper explicitly establishes dependencies for each attribute of the variable, which is a departure from previous work that either combines multiple attributes together or does not consider the dependencies between attributes. This paper provides a valuable reference for future research in this area.
2.	Quality:
2.1	The paper's experiments are thorough and comprehensive. It demonstrates superior performance compared to the state-of-the-art STGNN models. Furthermore, the experiments confirm that while improving performance, the proposed model does not significantly increase training and testing time, as well as the model size.
2.2	The ablation experiments are well-executed, demonstrating the necessity of each module and providing reasonable explanations for the experiment results.
2.3	In the ablation experiments, HSDGNN_w/o_MF outperformed DDGCRN, showcasing the superiority of the model framework. Furthermore, incorporating the remaining attributes resulted in even higher performance, underscoring the importance of establishing attribute dependencies.
2.4	The model exhibits remarkable stability, as its performance does not significantly fluctuate with parameter variations.
3.	Clarity:
Overall, the paper is clearly written and well organized. Figure 2 clearly illustrates the overall workflow and the functions of each module in the model.
4.	Significance:
In my view, the major contribution of this paper is the modeling of attribute dependencies among variables, which introduces a fresh perspective and a good direction for future research. Future work can conduct more in-depth research on how to better explore the dependencies between attributes.

### Weaknesses
1.	In this paper, only the main attribute (traffic flow) is predicted, and the other attributes served as auxiliary attributes for the prediction of the main attribute. If only the main attribute is predicted, the other attributes can be considered as providing additional useful information for the prediction of the main attribute. However, this does not necessarily reflect the presence of inherent dependencies between attributes, as each attribute can be treated as the main attribute. The current experimental setup does not fully justify the claim that the model captures inherent dependencies between attributes, as the model is only evaluated on the prediction of a single, designated 'main' attribute. This setup could be interpreted as simply leveraging additional features to improve the prediction of the main attribute, rather than demonstrating a true understanding of inter-attribute relationships.
2.	In Figure 2, the Intra-dependency Tensor (I) should be a 3x3 grid instead of a 4x4 grid.
3.	In Appendix A.2, HSDGNN is incorrectly written as MSDGNN.

### Questions
1.	For weakness1. Although the ablation experiments suggest that considering only the performance of the main attribute can surpass that of DDGCRN, this only demonstrates the superiority of the model architecture. Therefore, I hope the authors can provide the prediction results and ablation experiments for the other attributes (occupancy, speed).
2.	In long-term prediction, is the horizon of input also 12? If the horizon of input is 12, why are the values of PEMSD8 in Figure7 and Figure6 slightly different under the first 12 timestamps? If the horizon of input is not 12, can author indicate horizon of input of HSDGNN and DDGCRN for long-term prediction performance in the paper? 
3.	I am not sure whether the horizon of input of HSDGNN and DDGCRN is the same in long-term prediction. If not, can the author modify the experiment to compare the performance of HSDGNN and DDGCRN under the same horizon of input?

### Soundness
3 good

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
The paper introduces HSDGNN, a neural network architecture for multivariate time series forecasting. HSDGNN propagates representations along both nodes and features using dynamic adjacency matrices, which can be considered analogous to spatial attention scores. The model uses static learnable embeddings for both time steps and nodes and other operators to condition the forecasts. Empirical results show performance competitive w.r.t. the state of the art.

### Strengths
* Decent empirical results.
* The ablation study is appreciated.
* Figures do a good job of clarifying aspects of the method.

### Weaknesses
The methodological novelty of the paper is quite limited and the selected datasets appear inappropriate.

* The main novelty of the paper consists of combining intra and inter-node graph convolutions on a dynamically learned adjacency matrix (with no constraint on the sparsity), which can be seen as a matrix of dynamic attention coefficients. However, several methods perform attention across different dimensions (e.g., [1]) and there's little novelty in the mechanism used to learn such matrices end-to-end. The use of a dynamic adjacency matrix, while presented as a core contribution, is essentially a form of attention mechanism applied across nodes and features, which has been explored in prior works. The paper does not sufficiently articulate how their specific implementation of this dynamic adjacency matrix learning offers a significant advancement over existing attention-based approaches.
* The architecture appears overly complicated compared to alternatives from the literature and such complexity is poorly justified (see minor comments). The justification for the specific combination of modules is weak, and the paper does not provide a clear explanation of why this particular architecture is superior to simpler alternatives. The number of learnable parameters and the computational cost associated with the proposed architecture are not adequately addressed, especially given the marginal performance gains observed in the experiments.
* The considered datasets have at most 3 channels which does not justify modeling intra-channel dependencies with a graph. As shown by the ablation study in Tab. 2, removing the intra-dependency learning module results in a decrease in performance that is not statistically significant by considering the reported standard deviations. The use of graph convolutions to model intra-channel dependencies seems excessive for datasets with such a limited number of channels. The ablation study further suggests that this module contributes minimally to the overall performance, raising questions about its necessity and the rationale behind its inclusion.
* Empirical results on the existing traffic datasets are worse than those of much simpler baselines such as [2], which consists of a simple MLP with spatial and temporal embeddings. The fact that a basic MLP model achieves comparable or even superior results on the traffic datasets indicates a potential issue with the proposed model's ability to capture the underlying patterns in these datasets. This raises concerns about the model's effectiveness and the appropriateness of the chosen evaluation benchmarks.

Minor comments:

* Several claims are not supported by appropriate evidence. For example, in the introduction: "These methods can provide acceptable results depending on circumstances, but they may also introduce a higher degree of uncertainty, which can impact the reliability of predictions"; it is not clear what uncertainty the sentence is referring to and, at same time, how the introduced method should reduce uncertainty. The paper lacks specific examples or references to support the claim about increased uncertainty in existing methods. The connection between the proposed method and reduced uncertainty is not clearly established or quantified.
* "Even so, the temporal correlations regarding the changing spatial dependencies are not well-considered, which makes these methods ineffective in learning from dynamic graph topologies." There are a few papers that learn dynamic adjacency matrices using a mechanism similar to the one used here (e.g., [3]), but it is not clear how HSDGNN should be better than the current approaches. The paper fails to adequately differentiate its approach from existing methods that also model dynamic dependencies. The specific advantages of the proposed method over these existing approaches are not clearly articulated or supported by empirical evidence.

### Questions
Please clarify the novelty of the proposed method and justify this choice of benchmarks.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
1 poor
