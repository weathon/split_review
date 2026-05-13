# Temporal Heterogeneous Graph Generation with Privacy, Utility, and Efficiency

- Decision: Accept
- Scores: 8, 8, 6

## Abstract
Nowadays, Temporal Heterogeneous Graphs attract much research and industrial attention for building the next-generation Relational Deep Learning Models and Applications, due to their informative structures and features. While providing timely and precise services like personalized recommendations and question answering, this rich information also introduces extra exposure risk for each node in the graph, because the distinctive local topology, the abundant heterogeneous features, and the time dimension of the graph data are more prone to exposing sensitive information and narrow down the scope of victim candidates, which calls for well-defined protection techniques on graphs. To this end, we propose a **T**emporal **He**terogeneous Graph Generator balancing **P**rivacy, **U**tility, and E**ff**iciency, named **THePUff**. More specifically, we first propose a differential privacy algorithm to perturb the input temporal heterogeneous graph for protecting privacy, and then utilize both the perturbed graph and the original one in a generative adversarial setting for THePUff to learn and generate privacy-guaranteed and utility-preserved graph data in an efficient manner. We further propose 6 new metrics in the temporal setting to measure heterogeneous graph utility and privacy. Finally, based on temporal heterogeneous graph datasets with up to 1 million nodes and 20 million edges, the experiments show that THePUff generates utilizable temporal heterogeneous graphs with privacy protected, compared with state-of-the-art baselines.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The paper proposes a differentially private method to generate temporal heterogeneous graphs. The method first perturbs the input temporal heterogeneous graph for privacy protection. A generative adversarial network is trained using the perturbed graph and the original graph to generate large-scale and privacy-utility-adversary graph. The paper proposes six metrics to evaluate the graphs.

### Strengths
1. The paper is well written and easy to follow. 
1. The problem of privately generating temporal heterogeneous graphs is interesting and relevant. 
1. The paper introduces six novel metrics to the temporal and heterogeneous nature of graphs, allowing for more precise evaluation of the generated graphs.

### Weaknesses
1. The details on hyperparameters are missing. 
1. Attack experiments can be thoroughly evaluated on all the datasets.

### Questions
1. Though the graphs are evaluated on the proposed metrics, it seems a good idea to see and understand their performances on some specific tasks.  
1. What is the motivation for performing only the node signature structural query?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The introduces THEPUFF, a framework for generating temporal heterogeneous graphs that balances privacy, utility, and efficiency. THEPUFF employs a differential privacy algorithm to perturb input graphs, protecting privacy, and then uses a generative adversarial setting to learn and produce synthetic graph data that preserves both privacy and utility. The authors propose six new metrics to measure the utility and privacy of the generated graphs in a temporal setting. Extensive experiments on large-scale datasets demonstrate THEPUFF's ability to generate utilizable graphs with protected privacy compared to state-of-the-art baselines. The framework includes a privacy-preserving graph sample for distribution, an adversarial generative model for fitting the distribution, and an assembler for aggregating generated walks into a final graph. THEPUFF's effectiveness is validated through comprehensive evaluations and attacker experiments, showing it generates graphs with lower successful attack probabilities, indicating stronger privacy protection. The paper concludes that THEPUFF is the first work to address temporal heterogeneous graph generation with guaranteed privacy.

### Strengths
1. The paper addresses a significant gap in the field by proposing a method for generating temporal heterogeneous graphs with a focus on privacy preservation, which is increasingly important in data-sensitive applications.
2. THEPUFF is designed to balance three key aspects: privacy, utility, and efficiency, which are often competing considerations in data generation tasks. This balance is achieved through a sophisticated approach that includes differential privacy algorithms and generative adversarial networks (GANs).
3. The paper provides a thorough experimental evaluation using multiple real-world datasets, demonstrating THEPUFF's effectiveness and scalability compared to baselines using various metrics. 
4. The paper is generally good written and easy to follow.

### Weaknesses
1. As far as I am concerned, the key challenge in generating temporal graphs lies in the potential privacy leak in the temporal sense. The paper does not emphasize enough how such a challenge is tackled in the proposed method.
2. The paper carried out comparative experiments against baselines like EDGE (Chen et al. 2023), while excluding other state-of-the-art baselines like DISCO (Xu et al. 2024). Justifications should be provided to the choice of baselines. 
3. Some technical details are missing, like the functional form of D_priv, which hampers a smooth understanding of the paper.

### Questions
1. How is D_priv calculated in the proposed method? Any parameters involved? How does the parameter setting impact the performance of the proposed method?
2. How does the paper handle the potential privacy leak via temporal relevance in the graph when designing the proposed method? Is this taken care of in the GAN part or the assembly part?
3. Can the paper provide more experimental results against DISCO (Xu et al. 2024), even in small-scale graphs? This could benefit the understanding of the pros and cons of different approaches.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper introduces an innovative model, THEPUFF, for temporal heterogeneous graph generation that balances privacy protection and data utility. By leveraging adversarial learning and differential privacy perturbation, THEPUFF effectively safeguards privacy while preserving usability, with comprehensive experiments demonstrating its robustness and utility. Suggestions for improvement include clarifying methodological details, adding comparative experiments with existing methods, incorporating additional attack tests, and providing efficiency analysis. Overall, THEPUFF shows strong practical potential and innovation, and further optimization could make significant contributions to privacy protection in relational data.

### Strengths
1. The use of adversarial learning and differential privacy perturbation is well-justified, and the paper provides six metrics to comprehensively evaluate the model’s effectiveness in privacy and utility preservation.
2. The model is designed for applications that require scalable, privacy-sensitive graph data generation, with potential uses in recommendation systems, question answering, and beyond.
3. Extensive experiments, including attack simulations, ablation studies, and parameter analyses, validate the robustness and practicality of the model across diverse scenarios.

### Weaknesses
1. The introduction references social networks and citation networks as examples, but does not provide specific data or case studies to illustrate the severity of the issues and their potential impacts, making the discussion appear abstract.
2. While THEPUFF claims efficiency, the paper lacks explicit efficiency metrics or runtime comparisons, which would substantiate this claim and assess scalability
3. The model’s privacy resilience could be more comprehensively assessed by testing against a broader range of privacy attacks, such as structural or attribute inference attacks.

### Questions
See the weaknesses above

### Soundness
3

### Presentation
3

### Contribution
2
