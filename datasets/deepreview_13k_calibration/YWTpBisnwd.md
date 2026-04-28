# Enhancing Graph Self-Supervised Learning with Graph Interplay

- Decision: Reject
- Avg Score: 4.80
- Scores: 6, 5, 5, 5, 3

## Abstract
Graph self-supervised learning (GSSL) has emerged as a compelling framework for extracting informative representations from graph-structured data without extensive reliance on labeled inputs. 
In this study, we introduce Graph Interplay (\textsc{GIP}), an innovative and versatile approach that significantly enhances the performance equipped with various existing GSSL methods.
To this end, \textsc{GIP} advocates direct graph-level communications by introducing random inter-graph edges within standard batches. 
Against \textsc{GIP}'s simplicity, we further theoretically show that \textsc{GIP} essentially performs a principled manifold separation via combining inter-graph message passing and GSSL, bringing about more structured embedding manifolds and thus benefits a series of downstream tasks.
Our empirical study demonstrates that \textsc{GIP} surpasses the performance of prevailing GSSL methods across multiple benchmarks by significant margins, highlighting its potential as a breakthrough approach. 
Besides, \textsc{GIP} can be readily integrated into a series of GSSL methods and consistently offers additional performance gain.
This advancement not only amplifies the capability of GSSL but also potentially sets the stage for a novel graph learning paradigm in a broader sense.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper proposes a brand-new data augmentation, GIP, to address the limitations of current Graph Contrastive Learning augmentations which overlook the characteristics of graph. Specifically, GIP performs inter-graph edge adding instead of the common practice of edge adding or dropping within each graph, successfully improving manifold separation. The proposed method exhibits significant performance gain over existing GCL methods on TU datasets and OGB datasets. The paper provides valuable insights into future GCL augmentation designs that is more suitable for the nature of graph-structured data.

### Strengths
Novelty: the main contribution of the paper is to investigate inter-graph augmentation in GCL for the first time, which is simple, effective and flexible. This paper is likely to be a ground-breaking work that provides a new perspective to the GCL community.
Quality: the writing is easy to follow; the experimental results are extensive and impressive; the authors support their idea by theoretical analysis.
Reproducibility: I confirm that the authors have provided detailed code to reproduce the results.

### Weaknesses
1. Motivation: I do admit that inter-graph augmentation sounds interesting, but I think the motivation behind is still obscure due to the brief demonstration explaining it. The authors argued that conventional GCL augmentations overlook the characteristics of graph. While in GIP, edges between atoms of different molecules are added, which is still hard to interpret. The following questions arise: 1) How do the authors define “the peculiar and critical characteristics of graph data” in a more specific way, and how existing GCL augmentations violate it? 2) Upon the answer to Q1, how does GIP capture these characteristics?
2. Theoretical Proof: I’ve roughly checked the proof in the paper while finding it a bit confusing. For instance, to the best of my knowledge, the mathematical part before Eq.44 tries to tell that “An ideal coefficient learnt by an SSL model is better than coefficients of any other SSL models” which seems to be trivial and unnecessary; but the subsequent sentence “Since $f^{opt}$ represents the ideal case for GIP” is not a formal and valid proof that connects GIP to the context. Moreover, the augmentation of GIP is not involved in the proof. In conclusion, I assume that the theoretical part needs clarification to support the manifold separation assumption, which is the key theory of inter-graph augmentation in GIP.

### Questions
Besides the clarification of your theoretical analysis, why are some of the experimental results so high, even reaching 99% accuracy? Is there any explanation or insights? Or are there potential data leakage?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The goal of the paper is to broadens the contextual landscape within which the learning model operates. And this paper proposes a graph interplaly (GIP) framework, which encourages inter-graph connectivity fro enriched learning experiences by interconnecting graphs within learning batches. Meanwhile, the paper theoretically show the GIP could perform manifold separation via inter-graph message passing.

### Strengths
Pros:
1. The paper tries to broaden the contextual landscape within which the learning model operates and proposes a new graph interplay framework.
2. The framework is simple and easy to follow. The paper also provide the theory analysis to show that GIP essentially performs a principled manifold separation via combining intergraph message passing.
3. As the paper claims, the proposed framework can be readily integrated into a GSSL framework.

### Weaknesses
Cons:
1. Is it p a hyper-parameter of the framework? Why create enhanced views of the graph through the stochastic inter-graph edges? Could use the fully-connected graph with different edge weights to instead?
2. The paper construct inter-graph within a batch? Is it the batch size an important hyper-parameter? How the batch size impact the model performance?
3. There are also some related work about inter-graph construction, the model should highlight the difference and the improvement compared with these methods (i.e., Semi-Supervised Graph Classification: A Hierarchical Graph Perspective).
4. It is better to review the related works about inter-graph construction in the related work section.
5. The model is focused on the graph classfication. Could the framework has the improved performance on the other graph tasks, i.e., node classfication, or other settings like semi-supervised graph learning.
6. It is suggested to give the complexity analysis about the framework, i.e., time and space complexity analysis.

### Questions
Please see the above weaknesses.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
This work introduces a framework called Graph Interplay (GIP) to enhance Graph Self-Supervised Learning (GSSL) by allowing direct communication between graphs. GIP adds random inter-graph edges within a batch, enabling graphs to share information and improve representation learning. This interaction facilitates better separation of data manifolds, enhancing downstream task performance across benchmarks. Empirical results demonstrate that GIP integrates seamlessly with various GSSL methods, achieving significant performance gains.

### Strengths
1. The paper is well written, clearly showing the model framework. 

2. Theoretical analysis based on manifold separation is sound.

3. The empirical results on graph classification demonstrate the effectiveness of the proposed model.

### Weaknesses
1. The model treats batched graphs as super-nodes within a larger graph structure, employing a node-level contrastive objective to learn individual representations. While this approach is straightforward and potentially powerful, the technique of pooling graphs or subgraphs into super-nodes is not novel. Furthermore, the paper does not adequately address the computational overhead of introducing these inter-graph connections, especially as the number of graphs in a batch increases. The increased edge density could lead to significant memory and time costs, which are not discussed in the manuscript.
2. The paper does not clearly delineate how the GIP mechanism integrates with existing GSSL models. For instance, in the context of GRACE, it is unclear whether feature or edge perturbations should still be applied to the generated views after adding inter-graph connections. Does the graph augmentation method, such as diffusion used in MVGRL, still apply to the views within the GIP framework? If not, could combining GIP's augmentation with those used in the backbone GSSL models potentially enhance performance further? The manuscript lacks a clear ablation study to demonstrate the necessity of both GIP and the original GSSL augmentations.
3. In Line 53, the text states that the approach is 'tailored to respect and leverage the unique attributes of graph structures,' and Line 49 mentions 'non-uniformity, varying connectivity of different nodes, and the complexity of their relational linkages.' However, the manuscript does not clearly delineate how GIP preserves these characteristics. The introduction of random inter-graph edges could potentially disrupt the original graph structures, leading to a loss of the very properties the authors claim to preserve. It would be beneficial for the authors to provide both theoretical and empirical analysis to substantiate this claim, including an analysis of how the inter-graph edges affect the original graph properties, such as degree distribution and clustering coefficients.

### Questions
Please see the questions above.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper presents a novel augmentation method for graph-level tasks by considering other graphs in the dataset. 
The authors introduce a method to generate new edges between graphs, effectively creating an interplay between them. 
This approach leads to a significant performance improvement on several benchmark datasets.

### Strengths
1. The paper is well-written and readable.
2. The method achieves significant performance gains on several benchmark datasets.
3. Extensive ablation study provides valuable insights into the effectiveness of different components of the proposed method.
4. The paper can empower GSSLs focusing on node-level tasks in graph-level tasks.

### Weaknesses
1. It may be debatable that the motivation for capturing "interplay" between graphs is not fully aligned with the method, which introduces arbitrary edges between graphs. 
Even if the authors have provided extensive experiments, I think the results do not focus on aligning the motivation and implementations.
Also, there is no special consideration to differentiate inter-graph edges with intra-graph edges. This raises concerns about the validity of the "interplay" concept. 
It would be better to explain how the random inter-edges improve meaningful interactions between graphs in the introduction or experiment sections.
Personally, I guess the role of interplay in the SSL process is to facilitate better learning of the invariant information (i.e., the intra-graph edges) by comparing the edges with inter-graph edges rather than capturing the relationships among graphs.
However, I am willing to authors refute my opinion and show that SSL can capture relationships with inter-graph edges.


2.  There are some typos and grammatical errors throughout the paper.

### Questions
1. In Theorem 1, the authors claim that equation (45) holds due to equation (46). However, it is unclear why the similarity between $f^{(1)}$ and $f^{(2)}$ guarantees the similarity between these functions and $f^\text{sopt}$. Since $f$ maps graphs from various manifolds, it might be challenging to ensure that the learning process converges to $f^\text{sopt}$. If f gets stuck in a local optimum, equation (45) might not hold, invalidating Theorem 1. Could the authors please clarify this point?

2. Is there any study that explains the proposed graph-interplay 'actually' captures the interaction between graphs?
For example, It would be better to explain the importance of inter-graph edges compared to intra-graph edges using GNN-explaining techniques such as [1].

3. It is observable that an inter-graph edge exists between nodes and does not have a notable difference compared to intra-graph edges.
Are there some reasons to design inter-graph edges in this way, instead of providing them with different semantics (e.g., learn inter-graph edge embeddings, learn important inter-graph edges with attention mechanisms)? 

[1] Edge-Level Explanations for Graph Neural Networks by Extending Explainability Methods for Convolutional Neural Networks

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 5

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The authors focus on graph self-supervised learning, and propose a new augmentation technique, called Graph Interplay (GIP). GIP is to randomly link nodes belonging to different graphs in the same batch. The unimaginable results may show the potential of this newly self-supervised augmentation.

### Strengths
1. The proposed GIP augmentation is simple and intuitive, friendly for following research.
2. The quality of writing is easy to follow.

### Weaknesses
1. Potential to violate double-blind policy. In the repo for code, "environment.yml" file contains the following information "prefix: /home/zhaoxinjian/miniconda3/envs/sgnn", where "zhaoxinjian" implies one of authors.
2. The results shown in Table 1 is too unimaginable to convince. In IMDB-MULTI, GRACE+GIP and BGRL+GIP nearly double the baselines performances. For BGRL+GIP for IMDB-BINARY and GRACE+GIP for PROTENINS, the performances are 99.80$\pm$0.40 and 99.40$\pm$0.85, which approach 100 but baselines are far away from 100. Inversely, GIP does not bring so huge improvement over datasets in Table 2, although the task is still graph classification. I strongly suggest authors to double check if there is a leakage in Table 1.
3. The motivation of this paper is not clear. The authors argue other GSSLs overlook "peculiar and critical characteristics" of graph data. What are "peculiar and critical characteristics"? Why can they not capture these characteristics? Why can this paper realize this point? For example, DropEdge can capture the "varying connectivity of different nodes". Such motivation is so general that can be used for other papers.

### Questions
1. The theoretical result is strange. Intuitively, randomly connecting two graphs will involve more noisy edges than beneficial edges, since it's more possible to connect graphs from different distributions. In this case, the MI should be decreased, rather increased. In proof, the authors only assume a very specific scenario, where each graph only absorbs graphs within the same class and totally ignore the influence from other classes (Eq. 38). This setting is oversimplified and unreasonable.

### Soundness
1

### Presentation
3

### Contribution
2
