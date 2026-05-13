# DAS-GNN: Degree-Aware Spiking Graph Neural Networks for Graph Classification

- Decision: Reject
- Scores: 8, 6, 5

## Abstract
The recent integration of spiking neurons into graph neural networks has been gaining much attraction due to its superior energy efficiency. Especially because the sparse connection among graph nodes fits the nature of the spiking neural networks, spiking graph neural networks are considered strong alternatives to vanilla graph neural networks. However, there is still a large performance gap for graph tasks between the spiking neural networks and artificial neural networks. The gaps are especially large when they are adapted to graph classification tasks, where none of the nodes in the test set graphs are connected to the training set graphs. We diagnose the problem as the existence of neurons under starvation, caused by the sparse connections among the nodes and the neurons. To alleviate the problem, we propose DAS-GNN. Based on a set of observations on spiking neurons on graph classification tasks, we devise several techniques to utilize more neurons to deliver meaningful information to the connected neurons. Experiments on diverse datasets show significant improvements compared to the baselines, demonstrating the effectiveness of the DAS-GNN.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The article introduces DAS-GNN, a novel approach for graph classification task using spiking neural networks. The paper discusses the challenges of applying SNNs for graph classification i.e. varying spike frequency and to overcome these challenge authors proposed a Degree aware group adaptive neurons (DAG) that group neurons based on node degrees, and a Learnable inference base thresholds (LIBT) to reduce sensitivity of DAG to inference thresholds, The proposed method shows significant improvements over baseline approaches and even outperforms traditional ANNs in several cases while maintaining the energy efficiency.

### Strengths
1.In-depth Analysis of Spike Frequency Variation: Significant strength of the work is that authors have thoroughly studied spike frequency variation problem in graph networks along with providing clear visualizations which makes its easier to follow.
2- Ablation studies : The authors conducted component wise ablation studies which helps to understand the method contributing most to performance improvements. The authors have also conducted additional experiments to understand sensitivity to different hyperparameters such as threshold and learning rates.

### Weaknesses
1 - The paper lacks the theoretical justification of why the proposed DAG method provides better performance than other methods.
2-  Simplifying mathematical notations and providing detailed explanations for degree-aware neuron adaptation might make it more accessible to wider audience.Also the model architecture and spiking mechanism needs to be more detailed.

### Questions
1- How would the proposed method scale to very large graph with very skewed degree distributions?
2- Did authors perform any sensitivity for any other hyperparameters?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper proposes degree-aware spiking graph neural networks with adaptive thresholds based on a group of neurons for graph classification. The paper first diagnoses the poor performance as the existence of neurons under starvation caused by the graph structure. Then the paper proposes adaptive threshold among neurons partitioned by degrees, as well as learnable initial threshold and decay rate to reduce the sensitivity. Experiments on several datasets show superior performance of the proposed method and the potential low energy costs.

### Strengths
1. This paper identifies the starvation problem of spiking graph neural networks that causes performance drop when adapting them to graph classification.

2. This paper proposes a novel degree-aware group-adaptive technique to overcome the problem.

3. Experiments show superior performance on several datasets, some outperforming ANNs.

### Weaknesses
1. This paper does not discuss the influence of the proposed method for deployment on potential neuromorphic hardware, while SNNs mainly target those hardware to obtain energy efficiency. The proposed degree-aware group-adaptive neurons require the thresholds to depend on other neurons. Is it plausible for potential neuromorphic hardware? Or will it introduce much more computation for communications between neurons?

2. It is not clear if the energy consumption analysis takes the costs of this adaptive threshold operation (and potential communications between neurons) into account.

### Questions
Some recent works also study SNN for link prediction tasks in graphs besides node-level classification [1], which aims to better leverage the temporal spiking time property of SNNs beyond just the spiking nature. For the proposed method, is only spike rate considered? Is it possible to better leverage these properties of SNNs beyond rate, which are considered important features since the origin of SNNs [2]? These can be discussed.

[1] Temporal Spiking Neural Networks with Synaptic Delay for Graph Reasoning. ICML 2024.

[2] Networks of spiking neurons: the third generation of neural network models. Neural Networks, 1997.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper proposes the starvation problem of spiking neurons, which is widespread in existing spiking graph neural networks. And the paper observes that the spike frequency of neurons is related to the connectivity of the graph and entries in the node feature. Based on these observations, a novel spiking graph representation learning method called DAS-GNN is proposed. DAS-GNN is composed of two modules, degree-aware group adaptive neurons and the learnable inference base threshold. These components are responsible for regulating the threshold voltages of neurons by groups and reducing the influence of the base threshold voltages, respectively. Extensive experiments demonstrate that DAS-GNN outperforms its Artificial Neural Network (ANN) counterparts across some graph classification datasets. These findings highlight the potential of DAS-GNN for energy-saving and accurate graph-based systems.

### Strengths
1. This study proposes interesting observations that the connectivity of the graph will affect the receiving and firing patterns of spiking neurons.

2. The authors carefully design two components, degree-aware group adaptive neurons and the learnable inference base threshold, to effectively balance the predictive performance and the energy consumption.

3. Extensive experimental evaluations are provided, which are informative.

### Weaknesses
1. Some descriptions of neurons and nodes are unclear. In Section 3, neurons are related to the feature dimension. But, in Section 4.2, the paper claims that neurons can be grouped by their degrees.

2. The definition of the "degree group" is vague and the paper lacks more explanations about the groups $N_g$ or grouping strategies.

3. One of my main concerns is the technical quality. In the experiment, the baseline, PGNN, is always considered as a spiking neuron variant, referred to as Parametric Leaky Integrate-and-Fire model (PLIF) in the previous study [1]. However, the other baselines are spiking graph neural networks, which can adopt PLIF models as their spiking neurons. The categorization of baselines is confusing. Besides, the paper lacks details on the settings of these baselines.



### Questions
1. For those graphs following the power-law distribution, simply dividing nodes by their degrees may result in an uneven number of nodes between different groups. How does the grouping strategy proposed in the paper alleviate this issue?

2. In the experiment, the new and relevant spiking graph neural networks [2-3] and spiking neuron variants [4] can be introduced separately as baselines to demonstrate the model's effectiveness. Additionally, the authors should provide architectural details of baselines built from spiking neuron variants.

3. As mentioned in the paper, the real-world graphs tend to exhibit an extremely skewed distribution of degrees. The issue also remains in many large-scale graphs. Providing extra experiment results on node classification tasks would enhance the persuasiveness of the paper.

4. For spiking neural networks, there is a trade-off between the firing rate and the energy consumption. In this paper, the energy consumption of DAS-GNN is not only related to the firing rate but also to the grouping strategies. It would be clearer if the authors could provide the energy consumption (in formula) and further discuss the impact of the aforementioned settings on the energy consumption.

5. As depicted in Figure 5 and Appendix H, PGNN also shows highly diversified spike distributions on MUTAG and ENZYMES datasets. But MUTAG-PGNN-GCN and ENZYMES-PGNN-GAT remain obvious performance gaps compared to other baselines. It would be interesting if the authors could provide further discussions on these unexpected situations.

[1] Wei Fang et al. Incorporating learnable membrane time constant to enhance learning of spiking neural networks. In ICCV. 2021.

[2] Jintang Li et al. A Graph is Worth 1-bit Spikes: When Graph Contrastive Learning Meets Spiking Neural Networks. In ICLR. 2024.

[3] Mingkun Xu et al. Exploiting spiking dynamics with spatial-temporal feature normalization in graph learning. In IJCAI. 2021.

[4] Xingting Yao et al. GLIF: A Unified Gated Leaky Integrate-and-Fire Neuron for Spiking Neural Networks. In NIPS. 2022.

### Soundness
2

### Presentation
2

### Contribution
2
