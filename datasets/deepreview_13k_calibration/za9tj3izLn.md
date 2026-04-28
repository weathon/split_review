# A Unified View on Neural Message Passing with Opinion Dynamics for Social Networks

- Decision: Reject
- Avg Score: 4.33
- Scores: 5, 3, 5

## Abstract
Social networks represent a common form of interconnected data frequently depicted as graphs within the domain of deep learning-based inference. These communities inherently form dynamic systems, achieving stability through continuous internal communications and opinion exchanges among social actors along their social ties. In contrast, neural message passing in deep learning provides a clear and intuitive mathematical framework for understanding information propagation and aggregation among connected nodes in graphs. Node representations are dynamically updated by considering both the connectivity and status of neighboring nodes. This research harmonizes concepts from sociometry and neural message passing to analyze and infer the behavior of dynamic systems. Drawing inspiration from opinion dynamics in sociology, we propose \odnet, a novel message passing scheme incorporating bounded confidence, to refine the influence weight of local nodes for message propagation. We adjust the similarity cutoffs of bounded confidence and influence weights of \odnet~and define opinion exchange rules that align with the characteristics of social network graphs. We show that \odnet~enhances prediction performance across various graph types and alleviates oversmoothing issues. Furthermore, our approach surpasses conventional baselines in graph representation learning and proves its practical significance in analyzing real-world co-occurrence networks of metabolic genes. Remarkably, our method simplifies complex social network graphs solely by leveraging knowledge of interaction frequencies among entities within the system. It accurately identifies internal communities and the roles of genes in different metabolic pathways, including opinion leaders, bridge communicators, and isolators.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposes to integrate the dynamics of opinion defined in some opinion dynamics models such as Degroot model and the Hegeselmann and Krausse model to propose new aggregation equations for GNNs. The authors then combine these dynamics with the Neural ODE paper to train the parameters of the resulting model. The authors report improvement over node prediction tasks, and other tasks over baseline GNNs.

A key contribution of the paper is the design of the phi function which can incorporate homophily and heterophily. However they also introduce two new parameters. While their significance has been explained, how to set those parameters is still not intuitively clear. Specifically, on an unknown graph we may not have any idea about the nature of interactions that led to the graph.

Another contribution seems to be the integration of the whole model into the neural ODE framework for learning. However, the authors assume familiarity of the reader with this framework. It is very difficult judge the added complexity due to this addition. The authors also do not report training times and depth to which these networks and baseline models can be trained. Also, what about other GNN tasks e.g. link-prediction.

The author should also compare and contrast the role of other literature on learning of opinion dynamics models using neural networks:
Okawa, Maya, and Tomoharu Iwata. "Predicting opinion dynamics via sociologically-informed neural networks." In Proceedings of the 28th ACM SIGKDD Conference on Knowledge Discovery and Data Mining, pp. 1306-1316. 2022.

### Strengths
The design of aggregation function phi.
Experimental results on node prediction.

### Weaknesses
Limited scope of experimentation. Only node classification problem is addressed. Also the reason for good results is not sufficiently explored. The authors claim that their method addresses over-smoothing, but do not provide sufficient analysis of the spectral properties of the learned graph Laplacian, or how the proposed dynamics affect the eigenvalues. A more detailed analysis of the learned representations and their relation to the graph structure is needed. Missing literature review. A large class of methods in opinion dynamics has not been referred. Also, it is not clear why some of the other referred collective dynamics references are not effective. The authors should provide a more thorough comparison with other methods that combine dynamics and neural networks. Also, the overall contribution seems limited. The introduction of two new parameters in the phi function, while explained, lacks clear guidance on how to set them for different graph structures, especially when the nature of interactions is unknown. The paper also lacks a discussion of the computational complexity of the proposed method, particularly in relation to the Neural ODE solver, and how it scales with graph size. Finally, the paper does not discuss the sensitivity of the model to the choice of ODE solver and its parameters.

### Questions
None.

### Soundness
3 good

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper proposes a new message passing scheme for Graph Neural Networks, inspired by the Hegselmann-Krause (HK) opinion dynamics model. It is claimed that the proposed model, ODNet, resolves the oversmoothing issue of GNNs. Experiments show that ODNet significantly outperforms selected GNN baselines on popular benchmarks such as Cora, Citeseer, Pubmed.

### Strengths
1. To study the connection between opinion dynamics and neural message passing scheme is an interesting idea.
2. Experiments show that ODNet has some edge compared to traditional GNNs, Figure 2 also provides an example on which ODNet significantly alleviates oversmoothing.

### Weaknesses
1. It still remains very unclear to me why opinion dynamics can be used to design Graph Neural Networks. Opinion dynamics describe some hypothesized laws that humans might apply when exchanging opinions with others in a social network. GNNs are a class of neural architectures for the sake of capturing graph signals and make accurate predictions. I can clearly see that both of them are passing messages on the graph structure, with each node aggregating information from neighboring nodes in each iteration. However, the high-level similarity in their working mechanism does not explain why GNNs should do message passing following the way how humans exchange opinions. The paper's title, "A Unified View on Neural Message Passing with Opinion Dynamics for Social Networks", further exacerbates this concern, as the work primarily adapts the Hegselmann-Krause (HK) model for oversmoothing, which hardly qualifies as a unified view.

2. Eq. (6) (7) requires O(n^2) complexity to compute in each iteration of message passing, which abandons one of the most important characteristics of GNNs in leverage graph sparsity. Can the authors justify why this is a good choice, as well as the numerical comparison of ODNet's time complexity with other baselines? The authors claim that the method is "practically meaningful", yet they completely sacrifice graph sparsity, a critical aspect for scalability in real-world applications. This trade-off needs more justification, especially given the existence of large-scale graph datasets where sparsity is essential for computational feasibility.

3. The baselines used in experiments are outdated. Most GNN architectures are at least 3-5 years ago.

4. The readability of some key parts of the paper is extremely concerning. I find it very hard to understand, for example, the second paragraph on page 2 ("The opinion dynamics-inspired ...") and the paragraph of "Clustering and Oversmoothing in Herterophilious Dynamics" on page 4. Can the authors explain these two paragraphs in simpler language? For the former, why do microbial communities and metabolic genes suddenly appear in the context of social networks and opinion dynamics; for the latter, are the authors claiming that HK model does better on oversmoothing? I am extremely confused why so many things, "clustering", "oversmoothing", "heterophily", and "dirichlet energy", all show up together when none of them has been mentioned or eve hinted in the previous paragraph. The inclusion of gene co-occurrence networks as a type of social network is also confusing and requires more justification, as the connection is not immediately obvious.

### Questions
See weaknesses.

### Soundness
1 poor

### Presentation
1 poor

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper introduces a method called ODNET that combines sociological concepts from social networks with message passing. It incorporates the concept of bounded confidence, dynamically adjusting the influence weight on target nodes based on their similarity between the target node and their neighbor nodes, which could better simulate the propagation and aggregation of information in graph structures. And the results shows that ODNET outperforms other graph neural network models in node classification tasks and decreases the over-smooth problem.  Furthermore, this method has also been successfully applied to various types of graphs in this paper, including heterophilic graphs, homophilic graphs, and hypergraphs. Lastly, through ODNET, it becomes possible to explain the internal information exchange within networks and the roles of genes in different metabolic pathways.

### Strengths
1.	This paper introduces a novel MP framework ODNET which employs the influence function with bounded confidence.
2.	The ODNET method outperforming other baseline GNN models including heterophilic graphs and homophilic graphs. And the ODNET is generalized into hypergraphs.
3.	The ODNET decreases the over-smooth problem in GNN models and explains the internal information exchange within networks and the roles of genes.

### Weaknesses
1.	The structure of the paper is not very clear. There are minor symbol errors in the text.
2.	The example of social network architecture simplification is discussing about the microbial comparison between the Mariana Trench and Mount Everest networks, which is not adequately explained that the connection to social networks is unclear.
3.	This method is not very innovational that it combines the mathematical models from sociology to update node representation in MP.

### Questions
Why the microbial comparison between the Mariana Trench and Mount Everest networks is put into social network architecture simplification? Is it possible to make it clear how to identify opinion leaders, bridge communicators and isolators through ODNET?

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair
