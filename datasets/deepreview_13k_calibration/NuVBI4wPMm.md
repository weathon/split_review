# Decoupled Graph Energy-based Model for Node Out-of-Distribution Detection on Heterophilic Graphs

- Decision: Accept
- Avg Score: 6.50
- Scores: 6, 8, 6, 6

## Abstract
Despite extensive research efforts focused on Out-of-Distribution (OOD) detection on images, OOD detection on nodes in graph learning remains underexplored. The dependence among graph nodes hinders the trivial adaptation of existing approaches on images that assume inputs to be i.i.d. sampled, since many unique features and challenges specific to graphs are not considered, such as the heterophily issue. Recently, GNNSafe, which considers node dependence, adapted energy-based detection to the graph domain with state-of-the-art performance, however, it has two serious issues: 1) it derives node energy from classification logits without specifically tailored training for modeling data distribution, making it less effective at recognizing OOD data; 2) it highly relies on energy propagation, which is based on homophily assumption and will cause significant performance degradation on heterophilic graphs, where the node tends to have dissimilar distribution with its neighbors. To address the above issues, we suggest training Energy-based Models (EBMs) by Maximum Likelihood Estimation (MLE) to enhance data distribution modeling and removing energy propagation to overcome the heterophily issues. However, training EBMs via MLE requires performing Markov Chain Monte Carlo (MCMC) sampling on both node feature and node neighbors, which is challenging due to the node interdependence and discrete graph topology. To tackle the sampling challenge, we introduce Decoupled Graph Energy-based Model (DeGEM), which decomposes the learning process into two parts—a graph encoder that leverages topology information for node representations and an energy head that operates in latent space. Additionally, we propose a Multi-Hop Graph encoder (MH) and Energy Readout (ERo) to enhance node representation learning, Conditional Energy (CE) for improved EBM training, and Recurrent Update for the graph encoder and energy head to promote each other. This approach avoids sampling adjacency matrices and removes the need for energy propagation to extract graph topology information. Extensive experiments validate that DeGEM, without OOD exposure during training, surpasses previous state-of-the-art methods, achieving an average AUROC improvement of 6.71% on *homophilic* graphs and 20.29% on *heterophilic* graphs, and even outperform methods trained with OOD exposure. Our code is available at the anonymous link: [https://anonymous.4open.science/r/DeGEM\_ICLR2025\_rebuttal-B801/README.md](https://anonymous.4open.science/r/DeGEM\_ICLR2025\_rebuttal-B801/README.md).

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper studies out-of-distribution detection on graph data. The authors argue that existing models for this problem derives node-wise energy function that ignores the inter-dependence among node instances for uncertainty modeling and relies on homophily assumption for energy propagation. To address these limitations, the authors propose a new energy-based model as well as a new training scheme that can address graph heterophily and enables effective training of the energy model. Experiments on benchmark datasets show the consistent improvements of the proposed model over state-of-the-arts.

### Strengths
1. The paper is well motivated and studies an important problem in graph learning

2. The proposed model seems reasonable and sound

3. The experiment results are promising and solid

### Weaknesses
1. The argument that existing works on out-of-distribution detection resort to energy function independent for each node is arguably not true. There is a recent paper [1] that considers Dirichlet energy and extends the node-wise energy-based modeling for accommodating the neighborhood information in the graph.

2. The proposed model is computationally expensive, and more justification on the necessity of the proposed components that complex the model is needed. Particularly, compared to GNNSafe and other peer models, the additional computational cost of the proposed method seems considerably large, that questions the practical efficacy and scalability of the model in large datasets.

### Questions
1. Is there any intuition why the proposed model can address graph heterophily?

2. What is the computational complexity of the training algorithm and how does it compare with the other models?

3. What is the time/memory costs of the model and how does it compare with the other models?

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
This paper, titled “Decoupled Graph Energy-based Model for Node Out-of-Distribution Detection on Heterophilic Graphs,” presents a new model, DeGEM, aimed at detecting Out-of-Distribution (OOD) data in nodes on heterophilic graphs. By decoupling the graph encoder from the energy head, DeGEM addresses challenges in traditional methods, such as reliance on homophily assumptions and the complexity of MCMC sampling in graph structures. Experimental results show that, even without exposure to OOD data, DeGEM outperforms state-of-the-art models on both homophilic and heterophilic graphs.

### Strengths
1.The DeGEM model enhances OOD detection performance on graphs by decoupling the graph encoder and energy head, which helps avoid the performance degradation seen on heterophilic graphs due to homophily assumptions. This design demonstrates strong generalizability.

2.By moving MCMC sampling to the latent space, DeGEM reduces computational complexity, avoiding direct sampling on graph structures and achieving good scalability.

3.The paper conducts extensive experiments on both homophilic and heterophilic graphs, showing performance improvements across different graph types, which illustrates the model’s practical potential.

4.DeGEM enables effective OOD detection without the need for OOD data during training, making it highly valuable for real-world applications where unsupervised adaptability is crucial.

### Weaknesses
1.Although the decoupled design reduces dependency on graph structure and improves computational efficiency, the introduction of multiple components (such as GCL, conditional energy, and recurrent updates) adds complexity to the model structure. I suggest that key components be simplified in future versions.

2.While the paper includes some ablation studies, it does not discuss independent contributions from specific components such as the Multi-Hop encoder, Energy Readout, and Conditional Energy modules. Further independent testing of these components is recommended for future research.

### Questions
1.Although the decoupled design reduces dependency on graph structure and improves computational efficiency, could the introduction of multiple components (such as GCL, conditional energy, and recurrent updates) make the model structure overly complex? Could future versions simplify key components to reduce implementation difficulty?

2.While the paper includes some ablation studies, why were independent tests not conducted for specific modules like the Multi-Hop encoder, Energy Readout, and Conditional Energy? Could future research add such independent testing to more comprehensively assess the contributions of each component?

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
2

### Summary
The paper proposes a Decoupled Graph Energy-based Model (DeGEM) for detecting out-of-distribution (OOD) nodes on graphs, specifically addressing challenges on heterophilic graphs where existing models struggle. Extensive experiments validate DeGEM's superior performance, highlighting its robustness and scalability.

### Strengths
1. The paper is easy to follow.

2. OOD node detection is an important topic in the graph machine learning literature.

3. The model design is technically novel.

4. The performance of the proposed model surpasses that of the existing baseline methods.

### Weaknesses
1. More detailed explanations are needed regarding the state-of-the-art performance on homophilic graph datasets. The paper introduces specific components designed to address the heterophily phenomenon in graph datasets, which lead to their effectiveness on heterophilic datasets. However, it remains unclear why these components are also beneficial for homophilic data. Providing a rationale or theoretical basis for this performance would strengthen the paper's quality.

2. Given the paper’s focus on heterophilic graphs, it would be helpful to include experiments that analyze how varying levels of heterophily affect model performance. This could be similar to Figure 2 in [1], which explores performance across different heterophily levels, offering valuable insights into the model's adaptability.

### Questions
It appears that the uncertainty estimation methods proposed in previous GNN literature [1, 2] could also be applied for OOD node detection. Would it be possible for the authors to consider including these methods as baselines?

[1] Huang, Kexin, et al. "Uncertainty quantification over graph with conformalized graph neural networks." Advances in Neural Information Processing Systems 36.

[2] Hart, Russell, et al. "Improvements on Uncertainty Quantification for Node Classification via Distance Based Regularization." Advances in Neural Information Processing Systems 36.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This work proposes a method named DeGEM for graph OOD node detection, which can overcome the heterophily issue and the computational challenges.

### Strengths
- This work seems to be theoretically solid and technically sound.
- Extensive experiments show that the proposed method has a promising performance.
- The authors provided the source code in Supplementary Material, facilitating good reproducibility of this work.

### Weaknesses
 - In Abstract, the authors argue that GNNSafe has significant performance degradation on heterophilic graphs. However, there is a recent work [1] that has similar consideration.
- In Introduction, the authors only analyze the limitation of one recent graph OOD method named GNNSafe. However, as discussed in Section 5, there are many existing graph OOD methods. What are the fundamental research challenges that cannot be addressed by these existing methods?
- There are some minors. For example, the text font in tables is too small. It would be better to provide all the source scripts as well as the used datasets and give the anonymous repo link in the text.

### Questions
Please see the weaknesses listed above.

### Soundness
3

### Presentation
2

### Contribution
2
