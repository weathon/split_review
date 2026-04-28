# UNIFYING LONG AND SHORT SPATIO-TEMPORAL FORECASTING WITH SPECTRAL GRAPH NEURAL NETWORKS

- Decision: Reject
- Avg Score: 5.40
- Scores: 5, 8, 3, 5, 6

## Abstract
Multivariate Time Series (MTS) forecasting plays a vital role in various practical applications. Current research in this area is categorized into Spatial-Temporal Forecasting (STF) and Long-term Time Series Forecasting (LTSF). While these tasks share similarities, the methods and benchmarks used differ significantly. Spatio-Temporal Graph Neural Networks (STGNNs) excel at modeling interrelationships in STF tasks but face difficulties with long sequence inputs due to inefficient training. In contrast, LTSF models handle long sequences well but struggle with capturing complex variable interrelationships. This paper proposes the Spectral Spatio-Temporal Graph Neural Network (S2GNN) to address these challenges, unifying short- and long-sequence spatio-temporal forecasting within a single framework. S2GNN leverages spectral GNNs for global feature extraction incorporates an adaptive graph structure to manage varying sequence lengths and adopts a decoupled framework to improve scalability. Additionally, we introduce scale-adaptive node embeddings and cross-correlation embeddings for better differentiation between similar temporal patterns. Extensive experiments on eight public datasets, including both STF and LTSF datasets, demonstrate that S2GNN consistently outperforms state-of-the-art models across diverse prediction tasks. Code is available at \url{https://anonymous.4open.science/r/S2GNN-B21D}.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper presents a method to integrate spatiao-temporal with long-term time series forecasting, tasks which were previously at odds with one another in terms of model capabilities (spatio-temporal models were usually unable to deal with long-term forecasting, while long-term forecasters were inherently incapable of handling complex variable relationships). The authors propose S2GNN (Spectral Spatio-Temporal Graph Neural Network), which unifies both approaches by the following innovations: 

1. Using spectral GNNs with learnable filters
2. Incorporating scale-adaptive node embeddings
3. Utilizing cross-correlation embeddings
4. Adopting an adaptive graph structure

Extensive experiments show SOTA performance over baseline models

### Strengths
1. This paper solves an existing and urgent problem in time series forecasting by combining long-term and spatio-temporal forecasting;
2. It utilizes novel model designs which reduces the length requirement on the input training sequence (is this the purported reason for its utility in LTSF?)
3. Experiments generally show SOTA performance across a variety of metrics, although it is unclear how this model outperforms baselines on LTSF;

### Weaknesses
1. In the methodology section, it is not made explicit where the ability of the model to model long-term time series comes from, and how; specifically, the paper does not clearly articulate how the proposed spectral GNN, scale-adaptive node embeddings, cross-correlation embeddings, and adaptive graph structure collectively enable long-term forecasting capabilities. The description of each component is present, but the explanation of their synergistic effect on long-term forecasting is missing.
2. Correspondingly, in the Experiments section, specifically in Fig. 8(b), visually, the performance of the model on long-term time series does not seem to be much better than baseline models, although the authors claim that the results show smaller fluctuations around the diagonal; the visual comparison does not strongly support the claim of superior long-term forecasting, and the lack of a clear visual advantage raises concerns about the practical significance of the reported numerical improvements.
3. In the Experiments section, to show superiority wrt long-term time series, the authors should compare with models that have been designed to deal with long-term time series; an example could have been the xLSTM; the absence of comparisons with established long-term forecasting models makes it difficult to assess the true contribution of the proposed method in this specific domain. The current baseline selection does not adequately challenge the model's long-term capabilities.
4. Ablation studies also do not quite illustrate which module is particularly responsible for utility on LTSF; the ablation study does not isolate the contribution of each component to long-term forecasting, leaving uncertainty about the specific mechanisms that drive the model's performance in this area. It is unclear if the spectral GNN, embeddings, or adaptive graph structure is the primary driver for long-term forecasting.

### Questions
1. Can the authors point out explicitly which part in the model design is responsible for the good performance on LTSF?
2. Why is the visualization only provided for two other baseline models?
3. Which part (ablation study) is responsible for LSTF?

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
5

### Summary
This paper presents a spatiotemporal graph model composed of learnable graph filters and an MLP-based architecture, addressing the efficiency challenges faced by existing spatiotemporal graph models when processing long-sequence inputs. In addition, the authors propose two feature embedding methods that enhance the model's capability to handle data indistinguishability issues. Moreover, using spectral GNN with learnable filters, the author shows that low-pass and high-pass information must be considered when utilizing the adaptive graph in STF. Experimental results on eight datasets reveal that the model outperforms state-of-the-art models, achieving superior predictive capability while maintaining reasonable training efficiency.

### Strengths
1. The paper provides a comprehensive and clear definition of the studied problems.
2. The paper is well-structured and easy to follow.
3. The use of a spectral GNN framework and a simple MLP-based sequential model ensures that the model remains scalable and efficient, making it applicable to longer input as well as larger datasets.
4. The experiments cover a wide range of public spatial-temporal and long-term time series datasets, showcasing the robustness and effectiveness of the proposed method.
5. The use of learnable filters enhances the interpretability of the model, directly demonstrating that temporal data exhibit both homophily and heterophily.
6. The scalability and efficiency problems are significant and practical for real-world traffic forecasting applications.

### Weaknesses
1. The font is too small in Figures 2, making it hard to read.
2. The paper lacks a comparison with other benchmark models in LTSF, such as the iTransformer[1].
3. The paper lacks evaluation of large-scale spatiotemporal datasets and comparisons with models specifically designed for such datasets, such as BigST[2].

### Questions
See weakness

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
5

### Summary
This paper focuses on **unifying long and short spatio-temporal forecasting**. The main research contribution lies in the design of **input embeddings**, introducing a **scale-adaptive node embedding method** and a **cross-correlation embedding method**. Experiments were conducted on both **STF datasets** and **LTSF datasets**. However, the overall motivation is not clear, the method lacks innovation, and the experiments fail to convincingly demonstrate that the approach is SOTA.

### Strengths
The main drawback of the STF method in the author's motivation is that it requires a lot of computing resources and the model is inefficient when performing LTSF tasks. As far as I know, such a problem does exist. The main research contribution lies in the design of **input embeddings**, introducing a **scale-adaptive node embedding method** and a **cross-correlation embedding method**.

### Weaknesses
The overall motivation is not clear, the method lacks innovation, and the experiments fail to convincingly demonstrate that the approach is SOTA.

**Motivation:** The author's motivation is that performing long-term spatio-temporal forecasting (LTSF) tasks requires substantial computational resources, and the model is inefficient. The author attempts to enhance model efficiency through sample indistinguishability, but the connection between sample indistinguishability and model efficiency is not clearly explained.

**Originality:** The primary contribution lies in the design of embeddings, specifically a **scale-adaptive node embedding method** and a **cross-correlation embedding method**. However, the distinction between these embeddings and temporal or positional embeddings is unclear. As stated in Section 3.1, "This value could be the node’s ID, the time of the day, or the day of the week." if the cross-correlation embedding method is a typical temporal embedding with an added node‘ ID？

**Quality:** The writing quality is average, with several errors (e.g., in the explanation of Equation 2, "Where c is a constant constant," there is a redundant "constant"). The figures are not sufficiently clear, with dimensions that are too small, and the explanations and labels for all figures lack clarity.

### Questions
0.  My main concern is: The size of model does not appear to be related to the embedding design, as it is likely the GNN component that primarily influences model size. So **what is the connection between sample indistinguishability and model efficiency or size?**  Please provide a more detailed explanation of how addressing sample indistinguishability specifically contributes to improved model efficiency or reduced computational requirements.


1. **Please use figures to explain your statement that "existing methods for handling spatial distinguishability cannot adapt to changes in the number of nodes."**
   - 1) Is your model inductive?
   - 2) How does S2GNN handle changes in the number of nodes?
   - 3) What types of node changes are you addressing? If the number of nodes in the test dataset exceeds that of the training dataset, can your model still make predictions accurately? Can it handle cases of missing or additional nodes?

2. **As most TSF benchmarks achieve good performance within 10 epochs, why does your model require so many epochs, as shown in Figure 2?** Additionally, could you explain why the graph structure appears stable and lacks significant variation? Is it possible that this is simply the result of model convergence?

3. **As stated in Section 3.1, "This value could be the node’s ID, the time of the day, or the day of the week," is the cross-correlation embedding method just a typical temporal embedding with an added node ID?** Please provide a more detailed comparison between the proposed embedding methods and existing temporal/positional embeddings, highlighting the key differences and advantages. This would help clarify the novelty of S2GNN.

4. **I don't see any components designed specifically to optimize both short- and long-term TSF tasks.** Could you concisely explain why your model qualifies as a unified model for both short- and long-term TSF?

5. **The chosen baselines are not previous SOTA, which limits the credibility of your experimental comparisons.** Please add recent SOTA baselines, e.g. itransformer, forecastgrapher.

### Soundness
1

### Presentation
1

### Contribution
1

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The authors aimed to achieve efficient learning for GNNs to process both short- and long-term spatial-temporal dependencies for forecasting tasks. To achieve so, they proposed S2GNN, introducing learnable filters to process these dependencies.

### Strengths
1.	The addressed problem, achieving efficient learning while simultaneously capturing spatial-temporal information, is important.
2.	The experiments are comprehensive, including multiple datasets for comparisons with SOTAs, ablation study, efficiency study etc.

### Weaknesses
1.  Motivation is unclear. I think the main motivation should be achieving efficient learning and meanwhile capturing the spatial-temporal information. However, the authors discuss a lot regarding the challenges in sample indistinguishability, which really confuse me. The authors should explain, why you adopted sample indistinguishability? what is its function in achieving training efficiency? Additionally, why adaptive graph structure is used? Still, what is its function in achieving training efficiency?
2.  Contribution is insufficient and not novel enough. The contributions include scale-adaptive node embeddings and cross-correlation embeddings. (I don’t think the adaptive adjacent matrix is a contribution, because it just employs a trainable weight to each node.) I appreciate the contribution of the scale-adaptive node embeddings, which is interesting, although I don’t see its connection with RIP. But the contribution is not enough for ICLR. Regarding the cross-correlation embeddings, I don’t see how it can help to achieve more efficient learning to process both short and long term dependencies.
3.  Writing is quite poor. The manuscript does not sound logical. For example, the authors discuss a lot the pros of spatial GNN and the cons of spectral GNN, and then they adopted spectral GNN in this work. I dont think this is logical.

### Questions
See above

### Soundness
2

### Presentation
1

### Contribution
2

---

## Human Reviewer 5

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper introduces a novel model, the Spectral Spatio-Temporal Graph Neural Network (S2GNN), aimed at unifying short-term and long-term multivariate time series forecasting. Current research in this area is primarily divided into Spatio-Temporal Forecasting (STF) and Long-term Time Series Forecasting (LTSF), which differ significantly in methods and benchmarks. S2GNN leverages the strengths of spectral graph neural networks and incorporates an adaptive graph structure to efficiently handle varying sequence lengths. By introducing scale-adaptive node embeddings and cross-correlation embeddings, S2GNN demonstrates superior performance across multiple public datasets, outperforming state-of-the-art models.

### Strengths
1  The proposed S2GNN model effectively combines the advantages of short-term and long-term forecasting, addressing a significant gap between STF and LTSF research.
2  Extensive experiments on eight public datasets show that S2GNN consistently outperforms existing models, indicating strong generalization capabilities.
3  The use of an adaptive graph structure and learnable filters allows the model to flexibly accommodate different input lengths, enhancing its expressiveness.
4  The paper clearly outlines the model's construction and its components' functionality, making it accessible for other researchers to understand and replicate.

### Weaknesses
1  While S2GNN performs well across various datasets, its computational complexity may pose challenges in training on larger datasets. Specifically, the adaptive graph structure and the spectral graph convolutions, while powerful, can be computationally expensive, especially with increasing node counts and sequence lengths. The paper does not provide a detailed analysis of the model's scalability, which is a crucial factor for real-world applications.
2  Despite introducing learnable filters, the internal mechanisms and decision-making processes of the model lack sufficient interpretability, which may affect trust in practical applications. The paper does not delve into which features the model prioritizes or how the adaptive graph structure evolves during training. This lack of transparency makes it difficult to understand the model's behavior and debug potential issues. Furthermore, the spectral domain operations, while mathematically sound, often lack intuitive explanations, making it harder to grasp the model's reasoning.
3  The selection of baseline models for comparison is somewhat limited, potentially failing to fully showcase the advantages of S2GNN. While the paper compares against several existing models, it does not include more recent and advanced architectures, particularly those that have shown strong performance in long-term forecasting. This makes it difficult to assess the true novelty and superiority of S2GNN.

### Questions
NAN

### Soundness
3

### Presentation
2

### Contribution
2
