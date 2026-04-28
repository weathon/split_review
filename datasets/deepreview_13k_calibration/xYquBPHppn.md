# A VARIATIONAL FRAMEWORK FOR GRAPH GENERATION WITH FINE-GRAINED TOPOLOGICAL CONTROL

- Decision: Reject
- Avg Score: 4.25
- Scores: 5, 3, 6, 3

## Abstract
Controlled graph generation is the process of generating graphs that satisfy specific topological properties (or attributes). Fine-grained control over graph properties allows for customizing generated graphs to precise specifications, which is essential for understanding and modeling complex networks. Existing approaches can only satisfy a few topological properties such as number of nodes or edges in output graphs. This paper introduces CGRAPHGEN, a novel conditional variational autoencoder that, unlike existing approaches, uses graph adjacency matrix during training, along with the desired graph properties, for improved decoder tuning and precise graph generation, while relying only on attributes during inference. In addition, CGRAPHGEN implements an effective scheduling technique to integrate representations from both adjacency matrix and attribute distributions for precise control. Experiments on five real-world datasets show the efficacy of CGRAPHGEN compared to baselines, which we attribute to its use of adjacency matrix during training and effective integration of representations, which aligns graphs and their attributes in the latent space effectively and results in better control.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
The paper introduces CGRAPHGEN, a novel framework for controlled graph generation that allows for fine-grained control over graph topological properties. The authors propose a conditional variational autoencoder (VAE) that, unlike previous approaches, utilizes both the graph adjacency matrix and attribute vectors during training for improved decoder tuning and relies only on attributes during inference. This enables CGRAPHGEN to generate graphs that closely match the specified structural attributes.

### Strengths
1. The method utilizes a conditional VAE that integrates information from both the adjacency matrix and attribute vectors during training, resulting in more precise graph generation.

2. The scalability of the method is quite good. The method can be used to generate large-scale graphs, which is quite competitive compared to other auto-regression models. 

3. The paper is well-written and easy to understand.

### Weaknesses
1. The baselines and the datasets are quite simple. The authors are recommended to compare with more recent graph conditional generation methods. e.g. [1] [2] [3]

2. it is unclear how the hyper-parameters are defined. In Figure 5, the performance seems quite stable for different gamma, e.g. there's a drop when gamma = 0.8 on arxiv dataset. "When γ increases and more information is drawn from the prior pθ, the generation error increases." is not always true.

3. No theoretical analysis of how the proposed method can reduce the generation error better than other baseline methods.

### Questions
Please refer to the Weaknesses.

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
The paper focuses on controlled graph generation that generates graphs satisfying specific topological attributes. It introduces a new scheduling technique, MIXTURE-SCHEDULER, to combines desired attributes with adjacency matrix representations during training for precise graph generation, and it then uses only attributes during inference. Experiments demonstrate that generated graphs have better aligned attributes.

### Strengths
1. mixing the attributes and graph representation in latent space for VAE is somehow new for controlled generation. 
2.  the results for controlled graph generation is seemingly good regarding attribute alignment.

### Weaknesses
1. The biggest concern is the paper lacks of a rigorous deduction for the VAE model and learning objective. For most VAEs, we generally start from the miminization of log likelihood and use variational inference to factorize it. However, the formulations in this paper are very heuristic. We do not know whether the mixing of attributes and graph representation is valid. Mixing the prior with posterior looks also weird to me. What I expect should be starting something like $P(G|c) = \int_{Z_G, Z_c} P(G|Z_G, Z_c, c)P(Z_G|\theta, c) P(Z_c|c) dZ_G dZ_c$. The paper does not clearly define the joint distribution being modeled, nor does it provide a clear derivation of the ELBO that justifies the proposed loss function. The mixing of latent spaces, especially the way the prior and posterior are combined, lacks theoretical justification and appears to be an ad-hoc design choice. The lack of a proper probabilistic framework makes it difficult to assess the validity of the approach.
2. It seems the graph encoder/decoder can only deal with adjacency matrix, but how about graphs with node features? The paper does not discuss how node features, which are common in many real-world graph datasets, would be incorporated into the model. The current architecture appears limited to graphs represented solely by their adjacency matrices, which restricts its applicability.
3. The evaluation only measures the attributes, but the validness of the graph in many domains is also important (e.g. for molecules). The evaluation focuses solely on attribute alignment, neglecting other crucial aspects of graph generation, such as structural validity and domain-specific constraints. For example, in molecular graph generation, it is essential to ensure that generated graphs represent valid chemical structures, which is not considered in the current evaluation.

### Questions
What is d(Z_c) in Eq. (6)? There is no explanation for this notation.

### Soundness
1

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
This paper proposes a conditional variational autoencoder for graph generation with fine-grained topological control. The proposed model incorporates a scheduling technique to integrate representations from both the adjacency matrix and attribute distribution to enable fine-grained control.

### Strengths
1. This paper proposes a new setting for the controlled graph generation task, which is highlighted by the injection of fine-grained topological control.
2. The proposed method seems technically sound to me.

### Weaknesses
1. The number of baseline models compared in the experiments appears to be limited.
2. I'm not sure if it's reasonable to use only the MAD metric to evaluate the generation results based on various topological attributes.

### Questions
Please refer to the Weaknesses.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
The paper proposes CGRAPHGEN, a novel conditional variational autoencoder framework for generating graphs with fine-grained control over topological attributes. The framework introduces a MIXTURE-SCHEDULER, a scheduling technique to combine structural and attribute-based latent representations. Experiments on multiple datasets show that CGRAPHGEN outperforms baseline models.

### Strengths
- The model offers flexibility in controlling multiple structural properties (e.g., graph density, connectivity, clustering coefficient), enabling accurate graph generation across various domains.
- The mixture-scheduler seems to be novel and it smoothly integrates prior and posterior distributions, improving the quality and stability of generated graphs.

### Weaknesses
 - The proposed model doesn't seem to be much of an improvement compared to GraphVAE-like models. The condition architecture is very common in generative models, and feature/attribute based conditional graph generation seems to be a common trick in most methods. Therefore, I think the proposed model may lack enough novelty.
- Lack of baselines. I have noticed this paper include the diffusion-based model (EDGE), why not other SOTA graph generative models like DruM, DIGress and so on. For graph generation, I think it is more convincing to compare these models or at least other vae-based models. As far as I know, I believe these models can also incorporate the attribute feature to achieve conditional graph generation.
- For the mixture-scheduler part, I don't really understand the meaning of regarding the time $t$ as epoch in the training stage. From Figure 4(b), it seems there is no clear effect on whatever the $\beta(t)$ is.
- In your ablation, I find the experiments with masked only one attribute, is there any flexibility attributes choice?

### Questions
- Is there any code for the proposed model?
- Have you tried other more complex neural network architecture?

### Soundness
3

### Presentation
3

### Contribution
2
