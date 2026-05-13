# Robust Heterogeneous Graph Neural Network Explainer with Graph Information Bottleneck

- Decision: Reject
- Scores: 3, 3, 3, 3

## Abstract
Explaining the prediction process of Graph Neural Network (GNN) is crucial for enhancing network transparency. However, real-world networks are predominantly heterogeneous and often beset with noise. The presence of intricate relationships in heterogeneous graphs necessitates a consideration of semantics during the explanation process, while mitigating the impact of noise remains unexplored. For GNN explainers heavily reliant on graph structure and raw features, erroneous predictions may lead to misguided explanations under the influence of noise. To address these challenges, we propose a Robust Heterogeneous Graph Neural Network Explainer with Graph Information Bottleneck, named RHGIB. We theoretically analyze the power of different heterogeneous GNN architectures on the propagation of noise information and exploit denoising variational inference. Specifically, we infer the latent distributions of both graph structure and features to alleviate the influence of noise. Subsequently, we incorporate heterogeneous edge types into the generation process of explanatory subgraph and utilize Graph Information Bottleneck framework for optimization, allowing the Explainer to learn heterogeneous semantics while enhancing robustness. Extensive experiments on multiple real-world heterogeneous graph datasets demonstrate the superior performance of RHGIB compared to state-of-the-art baselines.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
This paper proposes a robust heterogeneous graph neural network explainer with graph information bottleneck (RHGIB), which infers the latent distribution of graph structure and features to alleviate the influence of noises, and utilizes the graph information bottleneck to find explanatory subgraph. The authors also theoretically analyze the power of different heterogeneous GNN architectures on the propagation of noise information. Experimental results show the effectiveness of the proposed explainer.

### Strengths
1. The problem studied is interesting and novel. There is no existing work on explaining heterogeneous graph neural networks.

2. Experimental results demonstrate the effectiveness of the proposed method

3. The paper has a theoretical analysis on the noise amplification effect in heterogenous graphs.

### Weaknesses
1. The motivation of doing graph denoising for post-hoc explanation is unclear and unreasonable to me. The post-hoc explainer should truly reflect the important subgraph structure and features that the target GNN relies on for prediction. If noisy edges play an important role in the target GNN’s prediction, the post-hoc explainer should reflect that, which is one purpose of doing post-hoc explanation, i.e., discovering potential issues in the algorithm and data. Doing denoising from the post-hoc explainer perspective would make the explainer unable to explain the target GNN well, especially when the target GNN relies on noisy edges for prediction. I think developing a robust self-explainable heterogenous GNN would be more convincing.

2. Many important details of the methodology about heterogeneous graph neural networks are missing. For example, how do the authors model $p(G|\mathbf{Z})$ for the heterogeneous graph that takes different types and edges and nodes into consideration? How do the authors model $p(\tilde{G|G})$. Currently, the whole methodology is described in a way that almost has nothing to do with heterogeneous graphs.

3. The authors only chose the most basic HGNN architecture which only contains GCN are relational learning modules as the base model. It is unclear why the authors do not adopt more HGNN architectures, especially those meta-path based HGNN, which seems to suffer more from noises. To demonstrate that the proposed explainer is flexible to explain various HGNNs, the authors should conduct experiments on various HGNNs.

4. The related work section should include heterogeneous graph neural networks and more representative and state-of-the-art GNN explainers.

5. In the experiment, it is unclear how the noises are added. Is it adding in the training set, test set or both?

6. The technical novelty is incremental. The idea of using graph information bottleneck for GNN explainer has been studied and the idea of using variational autoencoder for graph denoising is also explored. The paper just did a simple combination of two existing methods.

### Questions
Please see weaknesses.

### Soundness
2

### Presentation
2

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
This paper proposes RHGIB, to address the challenges of explaining heterogeneous graph neural networks with noise. The authors theoretically analyzed the amplification effect of noise in HG, particularly meta-path-based methods; incorporated heterogeneous edge types into the generation of subgraphs and utilize the GIB for optimization. Experiments were conducted on real HGs.

### Strengths
S1: Motivation: there are noise in HG when building the graph. How to explain GNN effectiveness on HG with noise worth to study

S2:  Theoretical analyses the amplification effect of noise in HG with meta-path-based methods

S3: Utilizes the Graph Information Bottleneck framework for optimization, enabling the explainer to handle irregularities introduced by structural noise.

### Weaknesses
C1: For graph learning with HG, meta-path-based algorithms in one of the key technique. But how to select meta-path is important. Meta-paths are usually given by domain experts. As shown in the methdology and theoretical analyses, the proposed is robust to noise with meta-path-based methods. Would the theorem be applied for non-meta-path methods? For example, for node classification, a simple GCN/GAT on the target node layer/domain without meta-path is a straightforward baseline. How is the effect of noise for a simple GNN without meta-path?

C2: The methodology section could be more concise and easier to follow.

C3: How does the proposed handle feature noise in addition to structural noise? The paper seems to focus primarily on structural noise.

C4: The paper does not explore the generalizability of RHGIB to other graph tasks except for node classification, such as link prediction or graph classification as mentioned in introduction.

C5: The main contribution of this paper is on robustness on HG with noise. However, there is no experiments on specific investigation of the robustness. For example, a synthetic HG with community structure can be generated with existing graph generator (groundtruth is know for the synthetic graphs), such as  Stochastic Block Model (SBM), Girvan-Newman Algorithm, and Caveman Graph Generator. Noise can be added by random deleting/adding edges. How would the proposed explain a GNN node clustering ability for the two HGs (one is noise-free, the other is with noise)?

### Questions
Please see weaknesses

### Soundness
3

### Presentation
2

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
This paper presents a PHGIB model aimed at mitigating the impact of noise on the graph explanation results. Specifically, the authors theoretically demonstrate how noise affects the information propagation process in heterogeneous graphs. Furthermore, they utilize noise-variational inference to alleviate its effects and combine these results with a graph information bottleneck to optimize the heterogeneous subgraph generation process for robust explanations.

### Strengths
S1: This paper primarily addresses the impact of noise in real-world heterogeneous graphs on graph interpretability. The model proposed by the authors features a unique denoising variational graph encoder, which can effectively integrate denoising strategies into a variational inference framework. Additionally, the authors combine edge-type information with an attention mechanism used during generation; this can enhance the capture of semantic information in heterogeneous graphs.

S2: The proposed method is supported by a theoretical foundation, which is based on validated techniques, and a theoretical analysis of the improved method is provided. The authors also present relevant experiments to validate their approach.

S3: The organization of the paper is well-structured, and the description of the methods is logically coherent.

### Weaknesses
W1. The authors have not conducted a comprehensive review of related works. Although the paper states that there are no existing robust heterogeneous explainers, it introduces a related method and claims to validate the robustness of the model. However, similar studies, such as "Counterfactual Learning on Heterogeneous Graphs with Greedy Perturbation" and "On the Robustness of Post-hoc GNN Explainers to Label Noise," are not mentioned. Furthermore, the authors do not discuss other papers related to heterogeneous graph explainers or clarify the differences between their method and existing ones, which limits the demonstration of the originality of their work.

W2. The authors only utilize MAE and RMSE as metrics to evaluate the interpretability of the extracted subgraphs, while related literature typically includes additional classification-related evaluation metrics to assess model performance comprehensively. Specifically, metrics such as precision, recall, F1-score, and AUC, which are commonly used in classification tasks, are absent. This omission makes it difficult to assess the quality of the explanations in terms of their ability to support accurate predictions.

W3. In the baseline design, the authors only select general graph explanation methods and do not include interpretable methods specifically for heterogeneous graphs, which fails to effectively demonstrate the advantages of their work. The selected baselines, such as those designed for homogeneous graphs, may not be directly comparable to the proposed method, which is tailored for heterogeneous graphs. This makes it challenging to isolate the benefits of the proposed approach over existing heterogeneous graph explanation techniques.

W4. Although the authors provide visualization results in the case study to demonstrate the effectiveness of their explanations, they do not present results from other explainers, which diminishes the credibility and superiority of their proposed model. Without a comparative visualization, it is difficult to ascertain whether the proposed method provides more insightful or accurate explanations than existing techniques.

W5. The experiments described in the paper are based on artificially added noise values, which only demonstrate some robustness of the model but do not validate its generalization capability. Furthermore, these noise values are limited to edge perturbations, while the introduction also states that node features can be distorted by noise; thus, the experiments should consider including noise that accounts for this assumption. The lack of experiments involving node feature noise limits the assessment of the model's robustness in more realistic scenarios.

### Questions
Q1. How can it be proven that the statistical features and distributions of graph data are affected by existing noise? Since the main goal of the paper is to eliminate noise present in real-world data, the authors only provide results where noise has been added to edges in the real dataset. How can these experimental results effectively reflect the noise in the real world? Is it possible to elaborate on the specific impacts of noise on the statistical features of graph data and provide related experiments or theoretical support to demonstrate the model's ability to effectively remove noise from real-world data?

Q2. In Proof of THEOREM 1, why the method based on neighbor aggregation does not consider the influence of node v_j's neighbors on node v_i? This could affect the effectiveness of neighbor aggregation, and it is suggested that the authors provide a detailed explanation of the rationale behind this assumption and discuss the interactions between nodes during the aggregation process.

Q3. Regarding hyperparameter analysis, the Lagrange multiplier is used to control the extent of graph information compression. As stated in the paper, studies on "Graph Structure Learning with Variational Information Bottleneck" indicate that excessive or insufficient compression should degrade the model's performance. However, the authors' experimental results show that RHGIB is insensitive to these constraints, raising concerns about whether the model adequately captures patterns in the data. It is recommended that the authors carefully examine the model architecture and hyperparameter settings to further validate the model's effectiveness and robustness, ensuring that it can fully leverage the data's features.

### Soundness
1

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
This paper proposes a robust heterogeneous GNN explainer based on the graph information bottleneck (RHGIB) to identify the critical subgraph which decides the prediction. RHGIB consists of a denoising variational inference process and a relation-aware explanation generator. The denoising variational inference deduces the statistic characteristics of the graphs and provides the robust edge representations. The relation-aware explanation generator introduces the heterogeneous edge type to constrains the explanation subgraph optimization. Experiments on three public heterogeneous graph datasets demonstrate the superiority of RHGIB. The ablation study and the fidelity-sparsity analysis further present insights of the proposed method.

### Strengths
1. This work provides solid proofs to the denoising variational inference process and the GIB optimization, and the 
theorem of heterogeneous graph noise amplification effect is meaningful.
2. The focus of explanation on heterogeneous graphs and heterogeneous GNNs is intriguing and practical.
3. The superiority of RHGIB is sufficiently demonstrated by the extensive experiments.

### Weaknesses
1. The contribution of this work needs more elaborations, since the framework of RHGIB is highly similar to the baseline V-InfoR, consisting of a robust feature encoder and a GIB-based explainer. The novelty of combining these two existing components is not sufficiently justified, and the specific modifications to adapt them for heterogeneous graphs require more detailed explanation.
2. The manuscript overlooks the main distinction of the proposed denoising variational inference against the standard variational inference and the target of Formula (4) needs more explanations from my perspective. Specifically, the motivation for introducing a transformation of the distribution in the denoising process is unclear. The paper should elaborate on how this transformation differs from standard variational inference and why it is necessary for handling noisy heterogeneous graphs. The connection between the theoretical proof of noise amplification and the specific form of Formula (4) is also missing.
3. The case study in Section 5.6 is not convincing. The significance of <Paper-5558> to predict <Author-1034> is opaque and the same issue persists in the second example . The explanations provided for the selected subgraphs are superficial and lack a deeper analysis of the underlying relationships and reasoning behind the model's prediction. The case study should provide more concrete evidence that the identified subgraphs are indeed critical for the prediction.
4. The writing and organization of this manuscript can be further polished up. Moreover, Figure 1 in introduction is too rough and lacks of insights. The figure should provide a more detailed and illustrative overview of the proposed method and its advantages over existing approaches.

### Questions
1. If the edge representations are directly sampled from the variational distribution? The forward process deserves detailed introduction.
2. Elaboration on the denoising variational inference is recommended, especially for the motivation of Formula (4).
3. How to acquire the edge type embedding $r_{\phi(e)}$ is missing in the manuscript.
4. The reasonability of adopting MAE and RMSE to evaluate the classification task should be clarified.

### Soundness
3

### Presentation
2

### Contribution
2
