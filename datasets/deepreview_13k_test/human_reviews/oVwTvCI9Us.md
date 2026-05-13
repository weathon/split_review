# SEPAL: Scalable Feature Learning on Huge Knowledge Graphs

- Decision: Reject
- Scores: 6, 6, 5

## Abstract
Knowledge graphs accumulate information about more and more entities of the world. Much research is conducted to improve embedding models that capture this information and give useful node features in many downstream applications. However, most current methods are hard to scale to large knowledge graphs, partly because GPU memory is too small to hold the embeddings of many entities --YAGO4 has 67M entities. To scale existing embedding models on modest hardware, we introduce SEPAL: Scalable Embedding Propagation Algorithm for Large knowledge graphs.
The key idea of SEPAL to reduce compute is to only optimize embeddings on a core subset of entities, those that come with much more information than others. Then SEPAL propagates these embeddings to the rest of the graph with message passing, but no explicit optimization.
To enable efficient message passing, we break down large graphs into well-connected subgraphs that fit in GPU memory using a new algorithm called BLOCS: Balanced Local Overlapping Connected Subgraphs.
We evaluate SEPAL on five different knowledge graphs for four downstream regression tasks. We show that SEPAL outperforms alternative on downstream tasks, while providing a $43\times$ speedup to its base embedding algorithm.
Moreover, outside the core subgraph, embeddings obtained by message passing are not degraded compared to traditional methods, demonstrating the validity of SEPAL's propagation.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper introduces Scalable Embedding Propagation Algorithm (SEPAL) for scalable and cost-effective training of knowledge graph (KG) embeddings over large KGs with a single GPU. Specifically, SEPAL only optimizes the embeddings for a subset of core entities, and it computes the embeddings for the rest entities with message passing. To address the scalability challenge of message passing over a large KG, it proposes an algorithm called Balanced Local Overlapping Connected Subgraphs (BLOCS) to break the KG into smaller connected subgraphs. Empirical studies demonstrate the effectiveness and efficiency of SEPAL on KGs of up to about 67M entities.

### Strengths
**S1.** The problem formulation and methodology design are well motivated.

**S2.** Empirical studies demonstrate the effectiveness and efficiency of SEPAL for the experiments considered.

**S3.** The paper is easy to follow.

### Weaknesses
**W1.** In order to defend the novelty and principled benefit of core set embedding + embedding propagation, the current discussion and comparison against previous bag-of-entities approaches, particularly NodePiece, is insufficient. Notably, NodePiece also embeds a subset of entities and the authors should discuss how this is different from SEPAL.

**W2.** Current ablation studies are insufficient. This is important in particular as both claimed contributions have counterparts explored in the existing literature, i.e., core entity embedding + embedding propagation vs bag-of-entities approaches like NodePiece and BLOCS vs graph sampling/partition like METIS. The authors should consider respectively fixing one contribution at a time and replacing the other contribution with existing approaches. 

**W3.** The experiment settings considered are kind of different from the established ones without sufficient justification. See the questions below.

### Questions
**Q1.** Did you try evaluation for knowledge graph completion?

**Q2.** Did you try on common KGs like Freebase and Wikidata?

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
2

### Summary
This paper introduces SEPAL  to scale knowledge graph embedding models efficiently on limited hardware resources. SEPAL reduces computational demands by optimizing embeddings only for core subgraphs.   To facilitate efficient message passing, the authors developed BLOCS which partitions large graphs into smaller, well-connected subgraphs that fit within GPU memory. Evaluated on five knowledge graphs across four regression tasks, SEPAL demonstrates speedup over traditional embedding methods and achieves strong performance on downstream tasks.

### Strengths
1.This paper proposes SEPAL, a method designed to reduce computational costs, achieving faster processing times and lower memory usage for knowledge graph embeddings.

2.Although SEPAL generates embeddings from subgraphs, which could be suboptimal, the approach demonstrates strong performance on downstream tasks in experimental evaluations.

### Weaknesses
1.The work presents an interesting approach, though some aspects require further clarification. For instance, how specifically does the model reduce time and memory costs? The proposed method involves constructing core subgraphs and performing message passing on these subsets. In terms of memory, it appears that a substantial portion of memory usage stems from storing embeddings. However, it seems embeddings still need to be allocated for all entities and relations, raising the question of how memory savings are achieved. Regarding time reduction, is it primarily due to message passing on smaller subgraphs? Otherwise, this appears similar to conventional neighborhood-based message passing.

2.In the experimental section, the regression task setup lacks clarity. What specific values are being predicted? Additionally, why not evaluate the method on the knowledge graph completion task, which is a fundamental evaluation for knowledge graph embeddings? Including this evaluation would provide a more comprehensive assessment of the method’s performance.

### Questions
Please refer to the weekness

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
Knowledge graphs accumulate information about relations of entities of the world. Producing high quality knowledge graph embeddings are important to many downstream applications such as knowledge graph completion, knowledge graph based entity retrieval, etc. However, existing methods hardly scale to large knowledge graphs. Works like PyTorch-BigGraph and DGL-KE leverage graph partition and distributed training to scale knowledge graph embedding (KGE) training. This paper tackles the scalability issue of KGE training from a new way. Specifically, it trains knowledge graph embeddings on a core subset of entities, which greatly reduces the computation cost and memory requirements. After training the embeddings of core entities and relations, it propagates these embeddings to the rest of the graph with message passing which does not require further embedding training. The resulting system is called SEPAL (Scalable Embedding Propagation Algorithm for Large knowledge graph).

### Strengths
The paper proposes a new way to train knowledge graph embedding. Instead of training embeddings on the entire KG, it only trains embeddings on a small subset of core entities of a KG, which can reduces the computation cost and memory requirements.

### Weaknesses
The method of constructing the core subgraph cannot guarantee that all the relation types are included in the Core subgraph. Furthermore, there is no explanation of how to select \eta to minimize the training cost while maximize the model quality (embedding quality).

The diffuse step of BLOCS can easily cause the size of a subgraph to grow significantly if the subgraph has some super nodes. How to guarantee the size of subgraph will not exceed the upper bound is not discussed.

The paper claims that the proposed method can easily be adapted to most knowledge-graph embedding method. However, in the evaluation, it only shows the training efficiency and model performance of DistMult model. The performance (system and model) of other KGE models like TransE, RotatE should be presented.

The evaluation only uses YAGO datasets. The author should also include other large scale dataset like Freebase. Both PyTorch-BigGraph and DGL-KE can train KGE on Freebase.

One important task for KGE is knowledge completion. However, the paper does not have any evaluation on KG completion tasks.

The ablation study of how different hyper-parameters, I.e., \eta, m (L259), h (L308) of SEPAL impact KGE training speed and performance is missing.

The execution time breakdown of SEPAL is missing in the evaluation. How many time it takes to produce the core subgraph? How many time it takes to training the KGE on core subgraph? How many time it takes to run BLOCS and how many time it takes to do embedding propagation.

### Questions
How do you define NORMALIZE in section 3.2?
How do you decide K for different datasets? Is it a hyper-parameter?
How does R2 score define?
How do you train the KGE models using PyTordh-BigGraph and DGL-KE, How do you split the training set? Have you included all the entities in Table 5 in the training set?

### Soundness
2

### Presentation
3

### Contribution
2
