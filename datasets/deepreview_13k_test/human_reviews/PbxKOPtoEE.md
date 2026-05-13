# Neural Logical Index for Fast Knowledge Graph Complex Query Answering

- Decision: Reject
- Scores: 8, 5, 6, 5

## Abstract
Complex query answering (CQA) over knowledge graphs is a crucial multi-hop reasoning task aimed at addressing first-order logical queries within large and incomplete knowledge graphs. Direct traversal search methods rely solely on graph topology and often miss answers due to the incompleteness of the graph, thus neural models have been proposed to generalize the neglected answers from observed facts. There are primarily two lines of research tackling the challenges of CQA. Query embedding models learn representations for complex queries, offering fast speed but often providing only generic performance. In contrast,  neural symbolic search methods deliver better performance, although they tend to be computationally more expensive. In this paper, we propose an efficient and scalable search framework that combines the precision of symbolic methods with the speed of embedding techniques. Our model utilizes embedding methods to compute Neural Logical Indices (NLI) to reduce the search domain for each variable in advance, followed by an approximate symbolic search for fine ranking. The search is precise for tree-structured queries and approximates cyclic queries (which are NP-complete) in quadratic complexity concerning the search domain, matching the complexity of tree-form queries. Experiments on various CQA benchmarks show that our framework reduces computation by 90% with a minimal performance loss, alleviating both efficiency and scalability issues.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper proposes a novel framework called Neural Logical Index for Search Approximately (NLISA) to tackle the problem of complex query answering over large and incomplete knowledge graphs. The framework leverages the speed of embedding-based methods and the precision of symbolic search methods by reducing the search domain using neural logical indices computed via embedding techniques. This allows for an efficient and scalable approximate search mechanism, particularly for cyclic queries which are traditionally NP-complete. Experiments on various benchmarks demonstrate that the proposed method achieves significant computation reduction with minimal performance loss.

### Strengths
1. The combination of embedding-based and symbolic search methods in a novel framework that reduces the search domain using neural logical indices is a creative approach to the existing challenges in complex query answering.
2. The method is well-designed with details on how the neural logical indices are computed using local and global constraints strategies. The framework is theoretically grounded and empirically evaluated on multiple benchmarks.
3. The paper is well-structured and clearly explains the motivation, approach, and results. Definitions, figures, and tables are used effectively to aid comprehension.
4. The proposed method addresses the critical issues of efficiency and scalability in symbolic search methods, demonstrating its potential for real-world applications involving large knowledge graphs.

### Weaknesses
This work is solid. Maybe the authors could discuss more about the caching issue mentioned in appendix line 797, which is suggested to be presented in the main body of the paper if the issue really exists.

### Questions
Section 3.2 Why to choose hypernetwork? How sensitive are the results to the choice of embedding model used for computing the neural logical indices? Would different embedding techniques lead to significant variations in performance? The embedding model seems to be related to the caching issue.

### Soundness
4

### Presentation
4

### Contribution
4

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper introduces a new knowledge graph complex query answering method called NLISA, featured by computationally fast. It is a neural-symbolic framework with local and global constraints. Experiments on the benchmarks show that the NLISA framework could reduce computation by 90% with a minimal performance loss.

### Strengths
1. This paper studies an important problem of fast knowledge graph complex query answering, which could benefit the development of the knowledge graph complex query answering methods. 
2. The proposed fast knowledge graph complex query answering method is efficient that could reduce the computation by 90%.

### Weaknesses
1. The main method is hard to understand. After reading, I find it is not clear how the neural logical indices are achieved. 
2. Some method and experiment details are missing(refer to question 3 and 4 ). 
3. Though the NLISA is efficient but the complex query answering performances of NLISA are suboptimal. Table 1 shows the NLISA(local) is more efficient that achieves the best efficiency results. But most of the task performance of NLISA(local) in Table 2 are worse than FIT method. Especially the AVG(P) results on FB15k datasets is significantly worse.

### Questions
1. In Figure2, should the query graph represent the query “Fine someone who is married to a person who graduated from the same institution”? Since the in the triples (x1, Graduate, y) and (x1, Graduate, x2), the head entity refers to the same variable x1. 
2. The $\top$ in Equation (3) and (4) is hard to understand. Does the $\top$ represents operations between the truth values?  How should we interpret the Equation (3) and (4)? 
3. What are the entity embedding and relation embedding from equation in line 244 from? is it pre-trained by some methods? 
4. How the hyper-network are train? What data are used for the training?

### Soundness
3

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
3

### Summary
This paper addresses the limitations of current approaches to complex query answering, particularly query embedding and neural symbolic search methods. While query embedding methods offer speed, they often suffer from lower performance. Conversely, neural symbolic search methods achieve strong performance but are computationally demanding.
The proposed approach seeks to combine the strengths of both methods, aiming to provide high performance with efficiency. It does this by leveraging surrounding constraints for each query variable to reduce the search space. In one strategy, termed local constraints, embedding models determine constraints via relation tail prediction, based on the variable's connection to the relation. In another strategy, called global constraints, a broader set of constraints is applied across the entire query to further limit the domain.
The resulting framework, Neural Logical Index for Search Approximately (NLISA), can handle both tree and cyclic queries in a scalable way. Extensive experiments across multiple CQA datasets demonstrate NLISA's effectiveness and efficiency compared to several baseline models.

### Strengths
– The problem targeted in this paper (enhance the scalability of CQA methods while obtaining a good performance) is a valid and an important ongoing problem existing in the literature of CQAs. 

– the paper is well written in terms of motivation and problem statement.

– The proposed approach can handle several query types including cyclic ones where many previous works did not handle.

### Weaknesses
– In general, the local version of the model obtain lower performance than state of the art models. For example, on FB15K, the results are very low (approx 55) comparing to other models which obtain approx 72. Thus the scalability is obtained with the cost of substantial performance loss for local model. 

– while the paper is written well in terms of problem statement and motivation, the technical details of the approach requires further and better explanation. Moreover, some acronyms should be defined before the first usage to improve the clarity of the paper, e.g., EFO1.

– Scalability remains a significant challenge in the embedding and complex query answering (CQA) domains. Even studies that claim to improve scalability often use only small datasets for evaluation. Given years of advancements in model development, it is expected that models claiming improved scalability would be trained and tested on large-scale datasets. However, most datasets used in this field are quite small. In this paper, even the largest dataset, used to demonstrate model scalability, contains only 400,000 entities—far fewer than real-world knowledge graphs, which often have over 90 million entities.

### Questions
Why GNN-QE is not included in table 1?

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper addresses the challenge of efficiently answering complex queries over large and incomplete knowledge graphs (KGs). The authors propose a novel framework that combines the speed of embedding methods with the precision of symbolic search approaches. Their method introduces Neural Logical Indices (NLI) to preemptively reduce the search domain using embedding-based techniques. The framework approximates cyclic queries in quadratic complexity, achieving significant efficiency gains with minimal performance loss. Experiments across multiple benchmarks demonstrate the scalability and performance of their approach.

### Strengths
1. The method reduces computation costs by 90%, significantly improving efficiency with minimal performance loss.
2. It is scalable to larger knowledge graphs, handling orders of magnitude more entities than traditional methods.
3. The introduction of Neural Logical Indices effectively narrows the search domain, making symbolic computation more feasible.
4. It achieves a good balance between the precision of symbolic search and the speed of embedding methods for tree-form queries.

### Weaknesses
1. Even with the efficiency improvements, the framework incurs some performance loss when handling more complex cyclic queries. This limitation could affect use cases where high accuracy on intricate query patterns is essential.
2. The method’s dependency on embedding-based approaches may limit its adaptability and generalizability across different query types or diverse knowledge graph structures. Variability in embedding quality could impact overall performance and effectiveness.
3. The integration of local and global constraints in the framework adds a layer of implementation complexity. This could present challenges during practical deployment, requiring sophisticated engineering and optimization efforts to ensure seamless functionality.
4. While the framework achieves competitive results, it still falls short of the performance of state-of-the-art models in certain scenarios. This performance gap indicates room for further refinement, particularly in enhancing the handling of complex and cyclic queries to match or surpass the best-performing methods available.

### Questions
See the Weaknesses.

### Soundness
3

### Presentation
3

### Contribution
2
