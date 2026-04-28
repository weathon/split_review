# CSP: An Efficient Baseline for Learning on Large-Scale Structured Data

- Decision: Reject
- Avg Score: 3.50
- Scores: 5, 1, 3, 5

## Abstract
Last decade has seen the emergence of numerous methods for learning on graphs, particularly Graph Neural Networks (GNNs). These methods, however, are often not directly applicable to more complex structures like bipartite graphs (equivalent to hypergraphs), which represent interactions among two entity types (e.g., a user liking a movie). This paper proposes Convolutional Signal Propagation (CSP), a non-parametric simple and scalable method that natively operates on bipartite graphs (hypergraphs) and can be implemented with just a few lines of code. After defining CSP, we demonstrate its relationship with well-established methods like label propagation, Naive Bayes, and Hypergraph Convolutional Networks. We evaluate CSP against several reference methods on real-world datasets from multiple domains, focusing on retrieval and classification tasks. Our results show that CSP offers competitive performance while maintaining low computational complexity, making it an ideal first choice as a baseline for hypergraph node classification and retrieval. Moreover, despite operating on hypergraphs, CSP achieves good results in tasks typically not associated with hypergraphs, such as natural language processing.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
In this paper, the authors introduce Convolutional Signal Propagation (CSP), which is a simple and efficient algorithm for learning on large-scale structured data represented as hypergraphs or bipartite graphs. CSP is formulated as an iterative averaging process that propagates signals over hypergraph structure. Authors also analyse the proposed CSP, establishing connections between CSP and label propagation, niave bayes, and one-layer HNN. Experimental results for the tasks of node classification, and retrieval tasks are produced which show that CSP maintains very low computational complexity while achieving decent success. Authors present CSP as a important first choice baseline for learning on hypergraphs and large-scale structured data.

### Strengths
1. The CSP algorithm is simple and can be implemented with just a few lines of code, making it computationally efficient. 
2. The paper evaluates CSP on a diverse set of real world datasets related to various domains, which show the broad applicability of the proposed method.
3. Despite simplicity, the empirical results show that CSP achieves good performance compared to more complex baseline methods on tasks node classification, and retrieval. 
4. Authors also discussed several possible extensions for the basic CSP method.

### Weaknesses
1. The proposed CSP is simple, but it does not show any advantages over a simpler Naive-bayes classifier. For node classification task, Naive Bayes is better suited as a baseline than CSP. Specifically, while CSP is computationally efficient, its performance is not consistently superior to Naive Bayes, particularly on the node classification tasks. The core issue is that CSP's signal propagation mechanism, which relies on iterative averaging, does not inherently provide a more discriminative representation than the probabilistic approach of Naive Bayes, which directly models class conditional probabilities. This is especially evident in scenarios where feature independence assumptions of Naive Bayes hold reasonably well.

2. A simpler baseline is more beneficial on large scale datasets, because running a complex algorithm on small datasets is not that expensive. Among the datasets considered for evaluation DBLP, movie-RA and movie-TA are large-scale. CSP does not achieve better results on large scale datasets for both classification and retrieval tasks. CSP only achieves better results on small scale datasets, this raises the question of whether CSP is needed at all while a simpler Naive Bayes might just do the job. The claim that CSP is a good baseline for large-scale data is not fully supported by the results. The performance of CSP on large datasets like DBLP is not better than Naive Bayes, and in some cases, it is worse. This undermines the argument that CSP is a universally good baseline, especially when simpler methods perform equally well or better on the very datasets where its efficiency should shine.

3. Authors also do not compare with simpler GNNs, which I think should be added in the evaluation. The absence of comparisons with simpler Graph Neural Networks (GNNs) is a notable gap. While hypergraphs are different from standard graphs, there are established methods for converting hypergraphs to graphs, which would allow for a more comprehensive evaluation. This is important because GNNs have demonstrated strong performance in various graph-based learning tasks, and comparing against them would provide a more complete picture of the strengths and weaknesses of CSP. Specifically, even a simple GNN like Graph Convolutional Network (GCN) could serve as a relevant comparison point, especially since it also performs message passing, albeit on a different graph structure.

4. Authors discuss about various possible extensions to the basic CSP, but are not included in experimentation. I do not completely understand the reasoning behind this, but including them in experimental evaluation will strengthen the paper. The lack of experimental validation for the proposed extensions is a missed opportunity. While the core contribution is the simplicity of CSP, exploring the potential benefits of these extensions would provide a more complete understanding of the method's capabilities. Without empirical evidence, the extensions remain speculative, and it is difficult to assess their practical value.

### Questions
I have addressed my concerns in the weakness section, I do not have any specific questions.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
1

### Rating Number
1

### Confidence
5

### Summary
This paper extends classic Zhu Gharmani (2003) label propagation to hyper-graphs in a fairly straightforward manner.  Experiments are performed on the quality of the proposed algorithm on some small (and contrieved) hypergraph datasets.  Although they don't contain many recent baselines, the proposed method is still beat by baselines frequently (including naive bayes).

### Strengths
+ well principled extension of classic idea
+ clearly written

### Weaknesses
 - experimental results are on simple datasets and use very simple baselines.  still the proposed method doesn't seem that compelling
- the hypergraph formalization seems excessively complicated for simple recommendation problems studied
- zhu and gharmani is so old that it has doubtlessly been extended to hyper-graphs;  there absolutely must be more related work in this area

### Questions
See weaknesses.  Unfortunately there realistically isn't much that could convince me of this paper's novelty or merits.

The related work, discussion, and baselines should focus more on the existing work on LP and hypergraphs (Henne 2015, Villian, etc).  Many more papers in this vein are not compared with, including:

- Hypergraph Propagation and Community Selection for Objects Retrieval (2021)
- Hypergraph Label Propagation Network (2020)
- Wasserstein Soft Label Propagation on Hypergraphs (2018)

.... and doubtlessly many more.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper introduces Convolutional Signal Processing (CSP), a simple, nonparametric, and scalable baseline for hypergraphs. It further examines the relationship between CSP and previously established baselines, such as Hypergraph Convolution, Label Propagation, and Naive Bayes. The method is validated on both classification and retrieval tasks.

### Strengths
* Paper is well written and easy to follow.

* The proposed method is simple and scalable.

### Weaknesses
 * The authors observe that their proposed method resembles a simplified form of Hypergraph Convolution, where learnable weights are replaced by identity matrices. This extension is straightforward and lacks novelty. To strengthen the contribution, a clean empirical analysis or theoretical analysis could clarify the advantages of this design choice over standard hypergraph convolutional methods. Such an addition would enhance the novelty of the approach and provide insights into the specific benefits and trade-offs introduced by this simplification.


* Inconsistent evaluation compared to prior work: previous studies [1, 2] typically employ a 50%/25%/25% train/validation/test split, whereas CSP uses a 90%/10% train/test split. The authors should either align their evaluation with a similar evaluation split in [1, 2] or provide a clear justification for their choice of the 90%/10% split. Additionally, it would be beneficial for the authors to specify whether the recommended hyper-parameters in Hypergraph Convolution were used for the baseline methods and detail the specific settings employed for each baseline. 


* Retrieval tasks report only P@100; however, it would be more informative to also report NDCG@K (K=1/10/20). The authors should provide a rationale for their choice of P@100, explaining why this metric was selected over others.
CSP can only support binary labels. What are some implications of this limitation for real-world applications? Were any extensions considered to support multi-class problems?


* Missing baseline comparisons with MLP and Label Propagation. Including these baselines might offer additional insights into performance and advantages of CSP.

---

### Questions
See weaknesses.

Typo: Line 157: consists in a  → consists of a

### Soundness
1

### Presentation
2

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
The paper introduces Convolutional Signal Propagation (CSP), a simple non-parametric method designed for learning on hypergraphs and bipartite graphs. 

The authors present CSP as an efficient baseline for hypergraph node classification and retrieval tasks, achieving competitive performance with lower computational complexity.

CSP operates natively on these complex structures and is compared with well-known methods such as label propagation, Naive Bayes, and Hypergraph Convolutional Networks.

### Strengths
1. The motivation to propose a simple non-parametric method as a robust baseline for learning on hypergraphs, both with and without vertex features is strong.
2. The paper is well-structured and provides intuitive explanations of the problem, the method, and its applications. The formal presentation of CSP is enhanced with toy examples and implementation details.

### Weaknesses
1. The paper lacks a detailed discussion and in-depth comparison with several existing methods [a, b, c]. The significance of CSP as a baseline can be greatly enhanced through empirical evaluation against existing methods. Such an evaluation considers multiple metrics, such as accuracy, training times, and memory usage, as well as the tradeoffs among these across all datasets. Specifically, the paper should include a comparison with methods that demonstrate scalability on large graphs [a], as well as recent generalisations of neural networks on graphs and hypergraphs [b, c].
2. The core idea of CSP is already present [d] in the literature on hypergraph learning. Adding a unique enhancement, such as theoretical analysis, into the non-parametric CSP would strengthen the originality of the idea.  For instance, it could be the case that the non-parametric nature of CSP makes it more robust to overfitting and hence easier to generalise to unseen data. A more detailed analysis of the method's convergence properties and its relationship to other propagation methods would also be beneficial.
3. The academic datasets used in the paper (Cora, Citeseer, Pubmed, DBLP) include vertex features suitable for processing with (hyper)graph neural networks. Therefore, it is necessary to include hypergraph neural networks as competitors to demonstrate the effectiveness of CSP. The method HGCN is used as a competitor but including more recent methods such as [b] and [c] would strengthen the significance of CSP. It is important to evaluate the performance of CSP against these methods, particularly in scenarios where vertex features are abundant and can be effectively utilized by neural network architectures.
4. In datasets lacking vertex features, it is necessary to compare against non-neural methods for hypergraph learning [e, f]. Specifically, both [e] and [f] propose non-trivial methods for classifying nodes on hypergraphs, making them essential baselines for the task of node classification. The paper should include a comparative analysis of CSP against these methods to demonstrate its effectiveness in scenarios where vertex features are absent or limited.
5. The paper briefly introduces several potential extensions of CSP, such as alternative normalisations and generalisations of label propagation, but does not evaluate these variants experimentally. Including experimental results for these extensions would strengthen the paper by demonstrating the practical value of the proposed variations and providing a more comprehensive understanding of CSP's potential. The impact of different normalization schemes on the performance of CSP should be investigated, and the results should be included in the paper.

### Questions
1. Was an analysis conducted on the tradeoffs between accuracy, training time, and memory usage? How did these tradeoffs compare to existing methods, such as LightHGNN [a]? Understanding these aspects would clarify the efficiency and practicality of CSP in different scenarios.
2. How does CSP offer a unique contribution compared to the existing work on hypergraph learning [d]? Were there unique aspects that were not covered in the existing literature?
3. Was the inclusion of recent generalisations of hypergraph neural networks [b, c] considered in the experiments as competitors? How did these methods perform in comparison to CSP within the context of the datasets utilised with vertex features?
4. For datasets lacking vertex features, how did CSP compare to non-neural hypergraph learning methods [e, f]?

### Soundness
2

### Presentation
3

### Contribution
2
