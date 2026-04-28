# There is More to Graphs than Meets the Eye: Learning Universal Features with Self-supervision

- Decision: Reject
- Avg Score: 3.50
- Scores: 5, 3, 3, 3

## Abstract
We study the problem of learning features through self-supervision that are generalisable to multiple graphs. State-of-the-art graph self-supervision restricts training to only one graph, resulting in graph-specific models that are incompatible with different but related graphs. We hypothesize that training with more than one graph that belong to the same family can improve the quality of the learnt representations. However, learning universal features from disparate node/edge features in different graphs is non-trivial. To address this challenge, we first homogenise the disparate features with graph-specific encoders that transform the features into a common space. A universal representation learning module then learns generalisable features on this common space. We show that compared to traditional self-supervision with one graph, our approach results in (1) better performance on downstream node classification, (2) learning features that can be re-used for unseen graphs of the same family, (3) more efficient training and (4) compact yet generalisable models. We also show ability of the proposed framework to deliver these benefits for relatively larger graphs. In this paper, we present a principled way to design foundation graph models that learn from more than one graph in an end-to-end manner, while bridging the gap between self-supervised and supervised performance.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The manuscript proposes a generic framework designed for universal representation learning on graphs with different input features. By leveraging multiple graphs of a family, the proposed method can improve the quality of
learned representations, similar to multi-task learning. Experiments show that the method outperforms traditional SSL counterparts and obtains comparable results with supervised learning on some datasets.

### Strengths
1. Overall, the paper is well-written and easy to follow.
2. The paper studies an interesting research question of how to utilize knowledge contained in different graphs. As we know, graph datasets usually come with different node/edge features, which significantly hinders the study of transfer learning and foundation models. The authors adopt a simple approach to map the raw features from different domains into one shared feature space, and then train a shared graph encoder on top of the universal space. The pipeline makes sense to me and shows some promising results.
3. The framework seems to show some transferability. For example, when trained on [CoraFull, Cora-ML, DBLP, Citeseer, PubMed] and adapted on Arxiv, the result is better than performing SSL only on Arxiv itself. This demonstrates that training a shared graph encoder given a universal feature space can indeed help transfer learning.
4. In section 8.5, the authors show that including graphs with a larger domain gap negatively affects the quality of the universal embeddings. This finding is consistent with my understanding and it'll be better if the authors conduct more experiments to further demonstrate it.

### Weaknesses
1. The authors only implement the framework with one specific graph encoder, i.e., NAGphormer. The results will be much more convincing with more backbones included. Specifically, the lack of experiments with established GNN architectures like GCN, GAT, or GraphSAGE makes it difficult to assess the generalizability of the proposed framework. The current results might be specific to the transformer-based architecture used.
2. Similarly, they only use one pretext objective for SSL and test with one downstream task, i.e., SSNC. The paper would benefit from exploring a wider range of self-supervised learning objectives, such as contrastive learning or masked node prediction, and evaluating the learned representations on diverse downstream tasks beyond node classification, such as graph classification or link prediction. This narrow scope limits the conclusions that can be drawn about the universality of the learned representations.
3. The experiments lack details, and no code is available. The absence of crucial details, such as the specific data splits used for training, validation, and testing, makes it difficult to reproduce the results. The lack of code further hinders reproducibility and makes it challenging for other researchers to build upon this work. The description of the PairSim objective is also insufficient, lacking the precise mathematical formulation and implementation details.
4. The results for node classification seem inconsistent with prior work. For example, even a simple 2-layer GCN can achieve over 70% accuracy on Arxiv, yet the supervised baseline in the manuscript is only 61%. The authors must explain the gap between the results reported in the manuscript and the ones commonly found in related literature. This discrepancy raises concerns about the experimental setup and the validity of the reported results.
5. The results in Table 1 show a significant gap between the supervised baseline and SSL methods for some datasets, which is not typical in conventional graph-ssl literature, e.g., DGI[1]. This raises questions about the effectiveness of the chosen SSL method and the experimental setup.

### Questions
1. What's the data split used in the experiments? I looked everywhere but found nothing. The results for node classification seem weird to me, e.g., even a simple 2-layer GCN can achieve over 70% accuracy on Arxiv, yet the supervised baseline in the manuscript is only 61%. The authors must explain the gap between the results reported in the manuscript and the ones commonly found in related literature.
2. How to do the self-supervised learning (PairSim)? How to define the 'similar' or 'dissimilar' nodes without label information? Please add the equation of the training objective to the revised version.
3. The results in Table 1 are strange. In conventional graph-ssl literature, e.g., DGI[1], the performance of supervised GCN and SSL variants is close. However, in Table 1, there is a significant gap between the supervised baseline and SSL methods for some datasets. 
4. Why add an additional data augmentation step before feeding into the linear layers? The authors should conduct an ablation study to show the effect of such graph-aware augmentation. 
5. If the authors want to claim transferability (so-called Adaptability in the manuscript) of their framework, more experimental results and analysis should be included. Only the result on Arxiv is not convincing enough.
Overall, this paper is interesting in its research question, and the overall framework also makes sense to me. However, many technical details are missing and reproducibility is limited.  

Reference:
[1] Veličković, Petar, et al. "Deep graph infomax."

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper proposes to learn universal feature representations to facilitate cross-graph self-supervised learning. The model consists of two modules: the graph-specific module projects node features of different graphs to the same space; and then the universal representation learning module gets the features as input and share parameters for graph learning. The authors claim it can be a good way to train foundation graph models.

### Strengths
(1) The paper presents a very simple concept which tends to contribute more on the engineering side but useful in practice.
(2) The writing and organization is generally clear.
(3)  Comparatively comprehensive experiments on efficacy, efficiency and scalability

### Weaknesses
1. The major concern is about the novelty. The method is too straightforward and we do not see enough insights here. 
2. There are some ambiguity about the setting of universal multi-graph SSL. For the pre-training tasks on molecule graphs such as Rong et al. (2020), they are also training on multiple graphs. However the paper actually differs from these papers since it implicitly assumes that the have graphs with node attributes from different domains or with different dimensions. It is generally suitable for those big graphs with node-level/edge-level downstream tasks. But the authors do not make this point very clear.
3. In the experiments, the choice of the self-supervision task in our study is guided by the downstream task. That also looks too heuristic or too specific, because in many cases pretraining is used to train a foundation model which can be generalizable to many different tasks.

### Questions
Please refer to weakness.

### Soundness
3 good

### Presentation
3 good

### Contribution
1 poor

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper introduces a novel concept and explores a new problem domain - Universal self-supervised learning on graphs. In the case of other modalities such as images and natural language, models pre-trained on large datasets tend to generalize well to other datasets. However, achieving similar generalizations for graph data is notoriously challenging. This paper aims to address this challenge through universal self-supervisions, which involve training an Encoder model on various datasets and pretext tasks to obtain universal embeddings. Empirical results demonstrate that the proposed approach bridges the gap between self-supervised and supervised performance.

### Strengths
- The research problem is intriguing and holds practical significance.
- The authors provide a comprehensive definition of the concepts used in this paper, such as 'universal self-supervision'.
- The proposed framework is straightforward and easy to comprehend.

### Weaknesses
 - Concerns about graph-specific encoders: Regarding the alignment of feature dimensions across different graph datasets using a graph-specific encoder, it raises the question of how the proposed method generalizes to new, unseen datasets when there is no learned graph-specific encoder available. Since the aim of this paper is to learn universal node embeddings, it would be interesting to explore how the approach adapts to new datasets where a graph-specific encoder has not been learned.

**Concerns about the experiments**:
 
- The experimental setup used in this paper appears to be unconventional. Firstly, the authors explicitly choose NAGhormer as the encoder, which avoids direct comparisons with traditional self-supervised methods based on message-passing GNNs. However, NAGhormer does not seem to be the primary contribution of this paper. I recommend that the authors consider conducting experiments with a GCN-based encoder and compare their approach with standard graph-specific self-supervised models, such as contrastive methods.
- Furthermore, in the experimental section, the authors claim to use PairSim as a self-supervised task. While I am well-acquainted with self-supervised learning on graphs, such as contrastive methods and graph autoencoders, I am not familiar with PairSim. It is crucial that the authors provide a detailed explanation of the self-supervised task they use, preferably in the form of an objective function. They should also clarify why they chose this particular task, and if a different task (such as contrastive learning) were adopted, what impact it would have on the experimental results.
- Lastly, the experimental results provided by the authors are not particularly convincing. The results in Table 1 appear to be rather perplexing, as the authors did not clarify the dataset splits, which, to my knowledge, do not align with the common splits used for the corresponding baselines. Furthermore, the authors claim that their proposed method narrows the performance gap between self-supervised and supervised models, but the experimental results do not seem to support this claim. I would suggest that the authors reconsider conducting experiments under more widely adopted self-supervised settings, such as those used in contrastive learning and masked graph autoencoder methods. The lack of clarity regarding the dataset splits and the unusual performance values reported for node classification tasks raise concerns about the experimental rigor and the authors' familiarity with standard evaluation protocols for these datasets.

### Questions
Please see the Weaknesses part.

### Soundness
2 fair

### Presentation
2 fair

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
This work studies a framework for learning universal representations from multiple graphs through self-supervision, for node classification tasks. The proposed framework consists of graph-specific encoders that homogenize the distinct node features with different sizes and the universal encode that learns generic features from the homogenized features across different graphs. The framework is evaluated on node classification tasks with benchmark citation graphs, and the authors show the performance and efficiency improvements of the proposed method (namely U-SSL) over the self-supervised learning on individual graphs.

### Strengths
* This paper addresses the important and novel problem of learning universal representations across different graphs for node classification tasks.
* The proposed framework, consisting of graph-specific and universal encoders, is intuitive and easy to understand/implement. 
* This paper is generally well-written.

### Weaknesses
There are some weaknesses in the experimental setups and results, as follows:
* The authors consider only the citation graphs to validate the effectiveness of the proposed universal representation learning framework. In this vein, the proposed method may not be generalizable to more complex networks, such as social networks or code graphs. Specifically, the inherent structural differences and diverse feature sets present in social networks or code graphs might not be adequately captured by a framework optimized for citation graphs. For instance, social networks often exhibit community structures and dynamic interactions, while code graphs involve complex relationships between code entities. The absence of experiments on these types of networks leaves a gap in understanding the framework's broader applicability.
* For the citation graphs that are mainly considered in this paper, the authors may not have to use graph-specific encoders to homogenize the features from different graphs. In particular, for citation graphs, we can use the abstract of each paper to generate initial node features, and subsequently we can use the shared vocabulary or a certain method that can encode abstracts in a unified manner (e.g., using LMs to embed them), which means the proposed graph-specific encoders may not be worthwhile to use. The use of pre-trained language models, for example, could provide a more semantically rich and uniform feature representation across different citation graphs, potentially negating the need for graph-specific encoders.
* In Table 1 and Table 2, if the performances of the proposed U-SSL are lower than the performances of the baseline full fine-tuning methods, while these baselines are more efficient than the proposed U-SSL, what are the advantages that we can grab from using the proposed U-SSL? This raises concerns about the practical utility of U-SSL, especially when considering the trade-off between performance and efficiency. A clearer articulation of the scenarios where U-SSL would be preferred over more efficient baselines is needed.

Also, there is a weakness in the generability of the proposed method, as follows:
* The proposed method seems applicable to only the graphs with features, while real-world graphs sometimes do not have initial node features. This limitation significantly restricts the applicability of the proposed framework to a subset of real-world scenarios where node features are readily available or can be easily engineered.

### Questions
* Do you use the same backbone model for baseline, SSL, and U-SSL methods?
* When reporting the main results (Table 1), I am wondering why not include the OGBN-arxiv dataset during pre-training, and rather show the results with pre-training on all datasets including the OGBN-arxiv dataset as the extra. I assume that if similar citation networks are used more during pre-training of the proposed U-SSL, the downstream performance may be further increased.

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair
