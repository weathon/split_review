# Differentiable Distance Between Hierarchically-Structured Data

- Decision: Reject
- Scores: 3, 5, 5, 3

## Abstract
Many machine learning algorithms solving various problems are available for
metric spaces. While there are plenty of distances for vector spaces, much
less exists for structured data (rooted heterogeneous trees) stored in popular
formats like JSON, XML, ProtoBuffer, MessagePack, etc. This paper
introduces the Hierarchically-structured Tree Distance (HTD) designed
especially for these data. The HTD distance is modular with differentiable
parameters weighting the importance of different sub-spaces. This allows
the distance to be tailored to a given dataset and task, such as classification,
clustering, and anomaly detection. The extensive experimental comparison
shows that distance-based algorithms with the proposed HTD distance
are competitive to state-of-the-art methods based on neural networks with
orders of magnitude more parameters. Furthermore, we show that HTD is
more suited to analyze heterogeneous Graph Neural Networks than Tree
Mover’s Distance.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The paper studies hierarichically structured data and introduces a tree-distance with differentiable parameters weighting the importance of different subspaces. The paper presents experimental evidence that their approach achieves similar performance to SOTA methods based on neural networks while having orders of magnitude fewer parameters, and also has some benefits for heterogeneous Graph Neural Networks compared to prior methods.

The paper is motivated by the fact that there are many structured data formats such as JSON/XML/Protobuffer but not a good way of defining a reasonable notion of distance between them, which is in contrast with what happens when we deal with more standard objects like vectors in Euclidean space.

This paper proposes a particular distance called HTD distance, which exploits the recursive nature of the previously-mentioned data formats. The ultimate goal is to have a modular construction by combining potentially different metrics on different levels of the given tree. HTD has weight parameters, which control importance on different parts, is differentiable, and requires orders of magnitude fewer parameters than neural networks with similar guarantees (based on experiments). The authors perform a series of experiments with supervised learning, ianomaly detection, heterogenous GNNs,  clustering and UMAP for visualization.

### Strengths
+the paper studies a natural problem on hierarchies which is how to define suitable metrics that are differentiable and modular. 

+the authors present some natural candidate and apply it to different types of hierarchical data

+the authors present experimental results showcasing properties of their proposed metrics and benefits over prior methods.

### Weaknesses
-the theory is very straightforward in this paper. In fact, the two theorems stated as Th1 and Th2 could be obserations or propositions as they follow from the basic definitions.

-there have been recently approaches to define differentiable objectives suitable for doing optimization over trees and hierarchies, especially to deal with problems on relational data coming from networks (e.g. facebook or other social networks) with the goal of performing hierarchical clustering. The first such works were 1) Nickel et al. "Poincaré embeddings for learning hierarchical representations" and later 2) "Hyperbolic graph neural networks" of Nickel et al. and later the works of 3) Chami et al. "Hyperbolic graph convolutional neural networks" and 4) "From Trees to Continuous Embeddings and Back: Hyperbolic Hierarchical Clustering" and of 5) Monath et al. "Gradient-based hierarchical clustering using continuous representations of trees in hyperbolic space" have dealt with similar questions. I am surprised the authors do not cite such works as the problem of optimization over trees was addressed using differentiable methods in all of these works.

-omission of discussion for use of hyperbolic techniques and hyperbolic spaces in the present paper which is known to be suitable for hierarchical relations, much more than euclidean spaces.

### Questions
-Please I would like to hear the authors discussi the related works on Hyperbolic spaces for dealing with hierarchical data and Hierarchical clustering, where data also have latent tree structure. The goal here is to compare different trees and assign a loss to each so that lower loss means better tree for the dataset. The approaches there are also differentiable so how do you compare with them?

-For your metrics, is there any hope to prove something about the quality of the metric found?

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
This paper presents the Hierarchically-structured Tree Distance (HTD), a novel metric for structured data in formats like JSON and XML. Designed for rooted heterogeneous trees, HTD is modular and differentiable, allowing it to adapt to tasks like classification, clustering, and anomaly detection. Experiments show that HTD-based algorithms perform competitively with neural network methods while using far fewer parameters and are more effective for analyzing heterogeneous Graph Neural Networks than the Tree Mover’s Distance.

### Strengths
1. The paper is overall well-written and easy to follow.
2. This paper demonstrates theoretical superiority, as shown in Table 1.

### Weaknesses
1. The authors demonstrate the effectiveness mainly on distance-based tasks, which shows better performance compare to other distance-based method but does not appear comparable to GNN classifiers.

2. I am also concerned about the contribution and scope of this paper; however, I acknowledge that I am not an expert and am open to other opinions.

3. Although some limitations are mentioned in the submission (e.g., in the caption of Table 4), there is no comprehensive discussion of the proposed method's limitations. Specifically, the paper lacks a discussion on the sensitivity of the HTD metric to the choice of weights for individual sub-trees. The impact of these weights on the overall distance calculation and the potential for instability or bias is not explored. Furthermore, the computational complexity, while mentioned, is not thoroughly analyzed in the context of real-world applications with large, complex tree structures. The paper should also address the limitations of the bag distance calculation, particularly when dealing with highly diverse or large sets of sub-trees.

### Questions
see weakness

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
3

### Summary
This paper introduces the Hierarchically Structured Tree Distance (HTD), a metric designed to measure distances between tree-structured data commonly stored in formats like JSON and XML. HTD effectively represents message passing in heterogeneous graph neural networks (GNNs). Experimental results show that this distance metric is capable of addressing various machine learning tasks, including classification, visualization, and clustering.

### Strengths
- The paper is well-written.
- The proposed HTD generalizes the tree mover’s distance, making it applicable to both heterogeneous graphs and tree-structured data.
- Extensive experiments conducted across multiple tasks—classification, clustering, and anomaly detection—show HTD's superiority over state-of-the-art methods for tree-structured data.

### Weaknesses
I have several concerns regarding the novelty of the proposed distance:
- HTD appears to be a straightforward extension of the tree mover’s distance, replacing the optimal transport (OT) distance with the Hausdorff and Chamfer distances, which may introduce cheaper computational complexity.
- It is unclear why HTD outperforms the tree mover’s distance on homogeneous graph datasets, such as MUTAG and BZR, as shown in Table 3.
- Even on heterogeneous datasets, it seems feasible to apply the tree mover’s distance by constructing separate computational trees for each node type in the graph. So we can improve the performance of tree mover's distance on heterogeneous datasets like MUTAG and BZR.
- Similar to the tree mover’s distance, HTD does not meet the criteria for defining a valid kernel for tree-structured data, as it is not conditionally negative definite.
- Including standard deviations (STD) in the results of Tables 3 and 4 would be beneficial, as the variances are large; for instance, the STD of accuracy values for MUTAG and BZR might be around 5.

### Questions
See the weaknesses above.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
The paper introduces hierarchically-structured tree distance (HTD) between HS-Trees.

### Strengths
The authors introduce a new distance for hierarchically-structured trees based on Leaves, Bags, and Dicts.

### Weaknesses
- The motivation and explanation of the use of HS-trees and their distance are unclear in the introduction. The authors first say that the properties of HT-Trees are used in existing work. Then, in the next paragraph, the authors mention that the distance on HS-Trees has been studied very little. Among the properties used in previous work, were there HS-Tress distance?
- In the introduction and background, it’s unclear if the term HS-Trees is from previous work or if the term is first given by the authors. In addition, the background of HS-Trees, sample, and schema are very confusing. It would be clearer if the authors could provide an example of what they are here. Moreover, it’s unclear how bags are assumed to be “permutation invariant; therefore, the position has to be encoded through position encoding” and how the “universal approximation theorem for HS-Trees has been proved in Pevny & Kovarik (2019).”
- The authors mention the motivation of the work is “measuring the distance between samples emerging from popular data storage formats (e.g., JSON, XML, and ProtoBuffer)”. However, in the experiment section, there is no application in such data format. It is misleading to use the data storage formats as motivation in the introduction, but there is no related experiment
- In Section 2.1, it is unclear if the authors are trying to claim that GNNs are “hierarchically-structure data”. In the context of GNN, it’s hard to see what sample, schema, and even HS-Trees are.
- The authors claim that the proposed distance is differentiable, however, there is no theoretical proof
- The term Leaves is commonly used in tree structure data. It will be important to differentiate the difference between common tree structures and HS trees. In addition, it’s unclear how and why the definition of Leaves in Section 3. 1 is outside of the scope
- There is no proof for Theorem 1. The justification right after Theorem 1 is hard to follow.
- It is hard to link the relation between Eq. (5) and the distance in Table 2, even with the brief introduction in Appendix B. A simple proof or derivation could have helped to understand the connection.
- It’s unclear what the relation between HTD and TMD is.  A simple proof or derivation could have helped to understand the connection.
- The README.md files in the provided link to the code are not sufficient to reproduce the HTD and experimental results.
- The experimental setup is unclear in the main texts. It’s unclear what the actual classification tasks and anomaly detection are. Also, while Appendix A includes the implementation details, there is no reference in the main text link to the appendix. In addition, in Appendix A, the authors claim that the experiments are repeated five times, and there is no variance or standard deviation reported in the performance in the main text.
- It’s unclear what the colors represent in Figure 3. It’s unclear why and what “—” represents in Tables 3-5.
- The paper needs more proofreading: i) additional ) in line 029, ii) line 250 missing a period and there is an additional ), iii) notation is very hard to follow; a notation is given with confusing comma

## Minor
- There if no reference and introduction when the Mutagenesis dataset is first mentioned in line 317

### Questions
- Only until Figure 2 the authors demonstrate examples of Schema. However, the sample 1 and sample 2 are essentially trees, it still remains unclear how HS-Trees to GNN in Section 2.1. Could the author provide an illustrative figure to show the relation?
- The font size is a bit bigger than usual?

### Soundness
2

### Presentation
1

### Contribution
2
