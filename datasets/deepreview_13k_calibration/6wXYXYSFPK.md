# From Molecules to Mixtures: Learning Representations of Olfactory Mixture Similarity using Inductive Biases

- Decision: Reject
- Avg Score: 5.67
- Scores: 6, 6, 5

## Abstract
Olfaction---how molecules are perceived as odors to humans---remains poorly understood. Recently, the primary odor map (POM) was introduced to digitize the olfactory properties of single compounds. However, smells in real life are not pure single molecules, but are complex mixtures of molecules, whose representations remain relatively underexplored. In this work, we introduce POMMix, extending the POM to represent mixtures. Our representation builds upon the symmetries of the problem space in a hierarchical manner: (1) graph neural networks for building molecular embeddings, (2) attention mechanisms for aggregating molecular representations into mixture representations, and (3) cosine prediction heads to encode olfactory perceptual distance in the mixture embedding space. POMMix achieves state-of-the-art predictive performance across multiple datasets. We also evaluate the generalizability of the representation on multiple splits when applied to unseen molecules and mixture sizes. Our work advances the effort to digitize olfaction, and highlights the synergy of domain expertise and deep learning in crafting expressive representations in low-data regimes.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The authors report POMMIX, an approach to extend principal odor maps to mixtures. For this, they derive embeddings using a GNN and then use attention to aggregate those embeddings. Since they focus on a contrastive task, they use cosine predictive heads. 
They show that their approach outperforms various baselines.

### Strengths
- The paper is very well written and the methodology is clearly described 
- The authors also carefully described their hyperparameter optimization 
- It also seems as if the authors were careful in building baselines
- Dealing with mixtures is an important problem in chemistry that is often ignored - many people focus on predicting the properties of pure compounds as this is simpler
- The analysis of the "White noise hypothesis" is a nice case study

### Weaknesses
 - The methodology the authors proposed seems to be well-suited to address the task, but there seem to be no major innovations. Using GNN-derived embeddings and aggregating them via attention has been done before, e.g., in https://arxiv.org/pdf/2312.16473
- The attention maps are interesting, but I found it difficult to gain insights from them. Also the discussion in the paper is mainly focussed on general observations as number of interactions increasing with the number of components. 

Overall, it is an interesting applied ML paper that nicely shows how ML can be applied to an exciting chemistry problem. There is little advancement in the ML methodology.

### Questions
- Perhaps it goes beyond the scope of the work but I wonder if the performance of such models might not be improved a lot with MixUp-like augmentation techniques. 
- Could one obtain more chemical insights from the attention-map analysis by analyzing, for instance, how often certain functional groups/scaffolds interact with each other?

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
In the paper, the authors introduce POMMIX, which is an extending framework of the POM to represent mixtures. The POMMIX framework includes the POM model pretrained with mono-molecular data, CHEMIX attention model and  a cosine distance prediction head. Experiments on the mixture dataset show the empirical performance of the method.

### Strengths
1. The presentation of the method is very clear and easy to understand.
2. Many details of the experiments are provided, including the dataset and the schematic of the POMMIX model.

### Weaknesses
1. I think ablation study about different POM network architecture is necessary.  Since the GraphNets architecture is not the current SOTA architecture, I think using other architecture may improve the performance, e.g. [1].


### Questions
See the weaknesses part above.

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
This work presents POMMIX, a novel model for representing molecular mixtures, leveraging hierarchical design to capture the underlying symmetries in the mixture space. The approach comprises three key components: (1) graph neural networks for generating robust molecular embeddings, (2) attention mechanisms for effectively aggregating these molecular embeddings into comprehensive mixture representations, and (3) cosine similarity-based prediction heads to encode perceptual distances in the mixture embedding space, aligning with olfactory perception.

### Strengths
POMMIX’s hierarchical architecture captures the structural complexity of molecular mixtures by integrating graph neural networks, attention mechanisms, and cosine-based prediction heads, enabling acquisition of mixture representations. By encoding perceptual distances in the embedding space through cosine prediction heads, POMMIX aligns mixture embeddings with olfactory perceptual similarities, a novel enhancement for sensory science applications. The model consistently demonstrates high predictive accuracy across multiple datasets, highlighting its robustness and generalizability for a range of mixture-related tasks, from olfactory perception to chemical property prediction. Additionally, POMMIX’s modular framework allows it to be readily adapted to various molecular mixture tasks, making it a flexible tool for predictive modeling and exploratory analysis in molecular science.

### Weaknesses
This work has some limitations that highlight areas for future improvement in POMMIX. First, its performance is highly dependent on the quality and diversity of the training data; limited or biased data can hinder generalization, especially in underrepresented molecular categories. Specifically, the model's reliance on graph neural networks (GNNs) for molecular embeddings might not capture all relevant chemical features, particularly for molecules with complex or unusual structures, leading to potential biases if these are not well-represented in the training set. Additionally, POMMIX’s hierarchical architecture—combining graph neural networks and attention mechanisms—is computationally intensive, posing scalability challenges for very large datasets or deployment in resource-limited settings. The computational cost of GNNs, especially with larger graphs representing complex molecules, combined with the quadratic complexity of attention mechanisms, could limit the model’s applicability to large-scale mixture datasets. The model’s high capacity for capturing complex representations also increases the risk of overfitting, particularly with smaller or highly correlated datasets, which could impact generalization to new data. This is especially concerning given the relatively limited size of available olfactory datasets, making the model potentially prone to memorizing training data rather than learning generalizable patterns.

While innovative in its structure, POMMIX’s individual components could benefit from further exploration. For instance, alternative embedding techniques, such as chemical language models, could be evaluated alongside graph-based approaches to potentially enhance performance. The current reliance on GNNs might limit the model's ability to capture subtle nuances in molecular structure and interactions that could be better represented by other methods. An ablation study comparing the contributions of each pipeline component would provide valuable insights into optimizing and refining POMMIX’s architecture. Without a clear understanding of the individual contributions of the GNN, attention mechanism, and cosine-based prediction head, it is difficult to pinpoint areas for improvement or to justify the complexity of the current architecture.

### Questions
How does POMMIX handle biases or gaps in training data, particularly for underrepresented molecular categories? Would augmenting the data or introducing data-driven regularization improve generalization?

What steps could be taken to reduce overfitting, particularly for smaller or highly correlated datasets? Would techniques such as dropout, regularization, or data augmentation improve model robustness?

Have other embedding strategies, such as chemical language models, been considered as alternatives to graph-based methods? Would a hybrid approach provide any advantages, and how might the performance of different embeddings compare within the POMMIX framework?

Has an ablation study been conducted to evaluate the individual contributions of POMMIX’s components (graph neural networks, attention mechanisms, cosine prediction heads)? How would understanding the effectiveness of each component inform future improvements?

### Soundness
2

### Presentation
3

### Contribution
2
