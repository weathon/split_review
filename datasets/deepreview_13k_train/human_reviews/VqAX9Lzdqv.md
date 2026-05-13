# Enhancing Interpretability in Deep Reinforcement Learning through Semantic Clustering

- Decision: Reject
- Scores: 5, 6, 5, 6

## Abstract
In this paper, we explore semantic clustering properties of deep reinforcement learning (DRL) to improve its interpretability and deepen our understanding of the internal semantic organization. In this context, semantic clustering refers to the ability of neural networks to cluster inputs based on their semantic similarity in the internal space. We propose a DRL architecture that incorporates a novel semantic clustering module, which includes both feature dimensionality reduction and online clustering. This module integrates seamlessly into the DRL training pipeline, addressing the instability of t-SNE and eliminating the need for extensive manual annotation in the previous semantic analysis methods. Through experiments, we validate the effectiveness of the proposed module and demonstrate its ability to reveal semantic clustering properties within DRL. Furthermore, we introduce new analytical methods that leverage these properties to provide insights into the hierarchical structure of policies and the semantic organization within the feature space. These methods also help identify potential risks within the model, offering a deeper understanding of its limitations and guiding future improvements.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper investigates the semantic clustering properties within deep reinforcement learning to enhance interpretability and understanding of the model's internal semantic organization. Semantic clustering here refers to grouping inputs based on semantic similarity in internal representation. The authors propose a DRL architecture with a semantic clustering module that combines feature dimensionality reduction and online clustering, integrated directly into the training pipeline. Experiments confirm the module’s effectiveness, showing it reveals the semantic structure in DRL and offers analytical tools to understand policy hierarchies and feature space organization, along with identifying model limitations for further improvement.

### Strengths
1.	The paper introduces a new semantic clustering module that provides valuable insights into the internal structure of DRL, improving interpretability by revealing how inputs are organized semantically within the model.
2.	Extensive experiments validate the module’s effectiveness, demonstrating its capability to uncover meaningful semantic clustering within DRL and its potential as a tool for guiding model improvements.

### Weaknesses
1.	The method relies on Euclidean distance to measure similarity for clustering. However, in RL scenarios, minor state variations can lead to significant changes in optimal decisions. How does the proposed method address this issue to ensure meaningful clustering? Specifically, while the paper mentions feature dimensionality reduction, it is unclear how this specifically mitigates the issue of sensitivity to minor state variations, especially when these variations can drastically alter the optimal action. The paper needs to provide a more detailed explanation of how the reduced feature space maintains semantic similarity despite these variations.
2.	In Line 221, what specifically does "online training" refer to? Could you clarify whether this pertains to training the clustering module concurrently with the DRL model or another process? It is crucial to understand the exact training procedure, including whether the clustering module's parameters are updated in tandem with the DRL model's parameters or if it follows a separate update schedule. This lack of clarity makes it difficult to assess the practical implementation and potential impact of the clustering module on the overall DRL training process.
3.	Since the method aims to interpret DRL by clustering state inputs, why not directly use the DRL output as the clustering input? Intuitively, if different states yield similar DRL outputs, they might be more likely to be semantically similar. The paper should discuss the rationale for not using the DRL output (either action probabilities or value function estimates) for clustering, as this could potentially provide a more direct measure of policy similarity. The current approach of clustering based on internal state representations may not directly correlate with the policy's behavior.

### Questions
Please kindly refer to the above weaknesses.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
- This paper aims to better understand the decision making process of DRL via semantic clustering.
- Authors identify the limitations of traditional clustering techniques (mainly t-SNE) and propose a novel semantic clustering module, which incorporates a Feature Dimensionality Reduction (FDR) network and a Vector Quantizer (akin to the module used in VQ-VAE or VQ-GAN) to facilitate online clustering. 
- Experiments and evaluations are carried out on the Procgen benchmark

### Strengths
- The problem this paper aims to tackle is very clearly defined in L53~58.
- The added FDRNet seems relatively simple (not over complicated) and the usage of Vector Quantizer for the purpose of online clustering feels reasonable. 
- Visualizations clearly show the benefits of the proposed clustering method. Specifically, Figure 2 makes the comparison between the proposed FDR + VQ method vs t-SNE. Also, Figure 3 and Table 1 clearly show the different semantics of each cluster.

### Weaknesses
 - In the "Background" paragraph of Section 3, the explanation of Vector Quantized VAEs feels very out of place. A more subtle introduction to VQ is needed. More specifically, at this point in the paper, it is not clear why the audience needs to know about VQ-VAEs. There is no context for it in previous paragraphs, so it seems very out-of-the-blue.
- In L147/148, it is said that "directly clustering such high-dimensional features is challenging, ...". It is a statement that needs to be grounded, even though most people will agree that this is true. Perhaps a quick explanation with a known source would help.   
- Following on the previous point, in L150/151, "instability of t-SNE" should be elaborated on. What are the instabilities of t-SNE, and what causes these issues? It would be a good idea to add a paragraph going into the details of the difficulties of high-dimensional clustering, as well as the limitations of t-SNE. Specifically, the sensitivity of t-SNE to its hyperparameters, such as perplexity, and its tendency to produce different embeddings on different runs, should be discussed. Furthermore, the computational cost of t-SNE, which makes it unsuitable for online clustering, should be mentioned.
- Under Section 3.2 (FDR loss paragraph), the claim "it more effectively captures the nonlinear structure of data and preserves local neighborhood relationships compared to methods like PCA and UMAP" needs to be well grounded. Currently, this is a claim made by the authors without a source or other logical reasoning. For example, while PCA is known to be limited to linear transformations, UMAP is specifically designed for non-linear dimensionality reduction and preserving local structure, so the claim that the proposed method outperforms it needs more justification. The authors should provide a more detailed comparison of the underlying mathematical principles of these methods to support their claims.
- More explanation is needed on the overall pipeline (Figure 1). Especially, on the addition of VQ code (k) with the state feature. The only description is that "k is integrated into the state feature ..." but this is not detailed enough. More details on why this is added back to the state feature, what effects it has, and exactly how the "expansion into a vector" happens should be explained in the text. Specifically, the authors should clarify the dimensionality of the VQ code, how it is transformed into a vector of the same dimensionality as the state feature, and whether this transformation involves a learnable projection or a fixed mapping.

### Questions
There are a few questions in the section above.

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper proposes a novel semantic clustering method for deep reinforcement learning to improve its interpretability.

### Strengths
This paper proposes a semantic clustering module to cluster the state features, which uses vector quantizer to cluster the state features into some clusters.

Experiments provide cluster effectiveness evaluations as well as model and policy analysis.

### Weaknesses
1. The details of the algorithm are not provided. For example, how to integrate the VQ codes with the state features? Will the VQ embedding e_k be used for DRL. The paper needs more mathematical formulas to explain the process how the algorithm performs.

2. The importance of semantic clustering for DRL is not explained. Why clustering the state features can benefit DRL?

3. The enhancement of the interpretability needs to be evaluated and shown in the experiments. Could the method help the system to provide an image or sentence as the explanations of the strategy selection for the users.

4. Are there some baselines used in the experiments? I do not see the baseline section in the manuscript.

### Questions
See the weaknesses above.

### Soundness
1

### Presentation
1

### Contribution
2

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper investigates the semantic clustering properties of deep reinforcement learning (DRL) to enhance interpretability and understanding of internal semantic organization. The authors propose a novel DRL architecture with a semantic clustering module, integrating feature dimensionality reduction and online clustering. This module addresses the instability of t-SNE and reduces the need for manual annotation in previous methods. Experiments validate the module's effectiveness in revealing semantic clustering within DRL and introduce new analytical methods. These methods provide insights into the hierarchical structure of policies and feature space semantic organization, helping identify potential risks and guide future improvements.

### Strengths
1. Nice idea. The paper introduces a novel semantic clustering module within a deep reinforcement learning (DRL) architecture, which is a significant advancement in the field.  

2.  The paper is well-structured and written in a clear, concise manner, making it easy to understand the core contributions and findings of the paper. 

3.  The paper's experimental validation is robust and performs well.

### Weaknesses
1. The explanation of the clustering process lacks clarity. Specifically, it is unclear how the number of clusters, K, is determined in the context of the semantic clustering module and vq-vae. Additionally, the paper does not provide sufficient details on whether experiments were conducted to validate the choice of K or how different values of K might impact the performance and interpretability of the model. A more detailed discussion and experimental validation regarding the determination and impact of K would strengthen the overall contribution of the paper.  
2. Section  4 demonstrates  that  the  paper's  experimental  validation  is  robust  and  yields  promising  results.  However,  the  paper  lacks  a comprehensive  comparison  with  existing  methods in  semantic  clustering  and  DRL interpretability.

### Questions
See weakness.

### Soundness
4

### Presentation
4

### Contribution
4
