# Generalization, Expressivity, and Universality of Graph Neural Networks on Attributed Graphs

- Decision: Accept
- Scores: 8, 6, 6, 8

## Abstract
We analyze the universality and generalization of graph neural networks (GNNs) on attributed graphs, i.e., with node attributes. To this end, we propose pseudometrics over the space of all attributed graphs that describe the fine-grained expressivity of GNNs. Namely, GNNs are both Lipschitz continuous with respect to our pseudometrics and can separate attributed graphs that are distant in the metric. Moreover, we prove that the space of all attributed graphs is relatively compact with respect to our metrics. Based on these properties, we prove a universal approximation theorem for GNNs and generalization bounds for GNNs on any data distribution of attributed graphs. The proposed metrics compute the similarity between the structures of attributed  graphs via a hierarchical optimal transport between computation trees. Our work extends and unites previous approaches which either derived theory only for graphs with no attributes, derived compact metrics under which GNNs are continuous but without separation power, or derived metrics under which GNNs are continuous and separate points but the space of graphs is not relatively compact, which prevents universal approximation and generalization analysis.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The authors propose a metric based on optimal transport distances between graph representations.
Under this metric, the authors show the MPNNs are Lipschitz and graph rerpesentations are compact. They establish that GNNs are capable of separating attributed graphs that are distant in the defined metric, leading to a universal approximation theorem and generalization bounds for MPNNs. Building on these, the authors further developed a generalisation theorem.  Empirical results demonstrate the correlation between the new metric and MPNN output.

### Strengths
* The proposed a noval pseudometric for graphs based on iterated degree measures and optimal transport.
* The authors show MPNNs are universal and Lipschitz under this pseudometric.
* The authors show a bidirectional connections between the metric and MPNN output.
* A generalisation theorem is developed based the metric.
* The framework unifies MPNNs on graph and graphon.

### Weaknesses
 * The proposed metric only applies to MPNN/1-WL GNNs, and cannot be used to analyse more powerful GNNs. Specifically, the metric's reliance on iterated degree measures limits its applicability to architectures beyond those captured by the 1-WL test. This prevents analysis of GNNs that incorporate higher-order structural information or more complex message passing schemes, such as k-GNNs or F-MPNNs.
* Related works are insufficiently discussed. In particualr, the proposed metric seems realted to [1][2], but this connection has not been discussed. The relationship between the proposed metric and the Weisfeiler-Lehman distance, particularly as it relates to graph neural networks, needs further clarification. The authors should explicitly address how their metric compares to and differs from the approaches in [1] and [2], especially concerning the use of optimal transport and hierarchical measure representations.
* The metric is expensive to compute, while its complexity is linear to $L$, it is in the order of $n^5$ which hinders its practicality. The computational cost, scaling as $O(n^5)$, makes the metric impractical for large graphs, limiting its utility in real-world scenarios. While the dependence on $L$ is linear, the high polynomial dependence on the number of nodes $n$ is a significant bottleneck.
* The MPNN analysis limits to normalized sum aggregation, which is less commonly used. This choice restricts the scope of the theoretical results, as many practical MPNN implementations use mean or max aggregation. The implications of this choice on the generality of the findings should be discussed.
* There are too many similar notations and symbols, making it difficult to follow. The paper suffers from an overabundance of similar symbols, which makes it challenging to track the different concepts and their relationships. This lack of notational clarity hinders the readability and understanding of the proposed framework.
* The graphon-based approach means the results do not apply to sparse graphs. The reliance on graphon theory limits the applicability of the results to dense graphs, as graphons are not well-suited for representing sparse graphs. This limitation should be explicitly addressed, and the authors should discuss the potential for extending the theory to sparse graph scenarios.
* Emperiments are limited to one small real-world dataset (MUTAG), which makes the results less convincing. The experimental validation is limited by the use of a single, small dataset, which is insufficient to demonstrate the practical relevance and robustness of the proposed metric. The authors should include additional experiments on diverse datasets to support their claims.

### Questions
1. The proposed metric considers attributed graphs, but in Fig 2, why is the alignment worsen when added attributes? 
2. Can the results be used to analyse more power GNNs? e.g. k-GNN, F-MPNN, etc
3. Unifying graph and graphon MPNN means you have to assume normalised sum aggregation, can this assumption be removed?
4. If not considering graphons, can this results apply to sparse graphs?
5. How is the metric related to the metric in "Weisfeiler-lehman meets gromov-Wasserstein."?
6. Why do you use Unbalance OT instead of OT?

### Soundness
4

### Presentation
2

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
This paper develops a comprehensive theoretical framework that enhances the understanding of generalization, expressivity, and universality in Graph Neural Networks (GNNs) when applied to attributed graphs (graphs with node features). The central contribution is the introduction of a new metric, the Tree Mover’s Distance (TMD), designed to precisely measure the similarity between graphs by capturing both their structural and attribute-based characteristics. Key findings of this paper include the design of TMD,  the universal approximation of GNNs, and the analysis of the expressivity of GNNs.

### Strengths
1. The theoretical analysis is solid and thorough.
2. This work enhances the understanding of GNNs. The work introduces a new framework that unifies generalization and expressivity theories for attributed graphs, a notable achievement in GNN research.
3. The idea of introducing OT to this problem is quite novel and fancy.

### Weaknesses
1.  While the paper provides some empirical results, the evaluation could be expanded to offer deeper insights into practical applications and better demonstrate the efficacy of the proposed method. Have the authors considered evaluating TMD on additional graph classification benchmarks beyond MUTAG? Comparing TMD against other graph similarity metrics on tasks like graph matching or clustering could also strengthen the empirical evaluation. Furthermore, could the authors provide more detailed explanations of the experimental settings and parameter choices？

2. In Table 1, it would be helpful to clarify the organization and naming of the columns, as the label “Accuracy” appears to represent results across multiple methods. Providing a clearer breakdown of the results, along with an analysis that contextualizes each method’s performance, would enhance understanding. For example, if the statistics below MUTAG represent accuracy scores, they suggest that TMD does not significantly outperform some existing methods, such as Chen et al. (2022)’s  d^{(3)}_{WL} . A discussion of how TMD compares to these methods and whether additional datasets were considered may add further depth to the results.

3.  Structuring the manuscript to more prominently summarize the major findings and their impact would improve readability. Perhaps revise the contribution part in the introduction to better summarize the major findings. Also, perhaps adding a section to state the broader impact of these findings more clearly and how each finding advances the field of GNN theory to better illustrate the importance of this work. 

4. The methods primarily focus on dense graphs, as noted in the conclusion that “sparse graphs are always considered close to the empty graph under our metrics.” A further explanation of this limitation—specifically, why sparse graphs exhibit this behavior under TMD—would benefit the reader. Additionally, a discussion of whether this limitation affects the method’s generality and its potential applications to sparse graph domains would strengthen the paper.

### Questions
1.  While the paper provides some empirical results, the evaluation could be expanded to offer deeper insights into practical applications and better demonstrate the efficacy of the proposed method. Have the authors considered evaluating TMD on additional graph classification benchmarks beyond MUTAG? Comparing TMD against other graph similarity metrics on tasks like graph matching or clustering could also strengthen the empirical evaluation. Furthermore, could the authors provide more detailed explanations of the experimental settings and parameter choices？

2. In Table 1, it would be helpful to clarify the organization and naming of the columns, as the label “Accuracy” appears to represent results across multiple methods. Providing a clearer breakdown of the results, along with an analysis that contextualizes each method’s performance, would enhance understanding. For example, if the statistics below MUTAG represent accuracy scores, they suggest that TMD does not significantly outperform some existing methods, such as Chen et al. (2022)’s  d^{(3)}_{WL} . A discussion of how TMD compares to these methods and whether additional datasets were considered may add further depth to the results.

3.  Structuring the manuscript to more prominently summarize the major findings and their impact would improve readability. Perhaps revise the contribution part in the introduction to better summarize the major findings. Also, perhaps adding a section to state the broader impact of these findings more clearly and how each finding advances the field of GNN theory to better illustrate the importance of this work. 

4. The methods primarily focus on dense graphs, as noted in the conclusion that “sparse graphs are always considered close to the empty graph under our metrics.” A further explanation of this limitation—specifically, why sparse graphs exhibit this behavior under TMD—would benefit the reader. Additionally, a discussion of whether this limitation affects the method’s generality and its potential applications to sparse graph domains would strengthen the paper.

### Soundness
4

### Presentation
2

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
This paper theoretically shows that the closeness of two graphs by MPNNs can be represented by the proposed metrics based on Wasserstein Distance. This work also shows the existence of MPNNs that can separate two graphs with non-zero distance and can approximate any functions over the space of graphs. A bound of generalization gap is also provided for MPNNs with milder assumptions.

### Strengths
1. The theoretical analysis is solid and strong. Especially, this work tries to provide an analysis that is as universal as possible with the fewest assumptions. 
2. The discussion of MPNNs and tree mover's distance in Section 4 is interesting and novel to me.

### Weaknesses
1. The presentation is a bit strange. The main results in Section 5 appear too late on almost page 9 in the main body of the paper. Moreover, the universal approximation and the generalization bound seem independent of the previous analysis of graph/graphon distances. It is better to move Section 5 earlier and elaborate more about the connections with previous sections. 

2. Section 5 is not insightful enough. For example, although Theorem 7 makes contributions by requiring fewer assumptions, experiments in Figure 3 show that the generalization error is still related to the covering number and the Lipschitz constant, which is unsurprising and known in generalization theory. 

3. Some references on the generalization error of MPNNs are missing. 

Oono, K. and Suzuki, T. Optimization and generalization analysis of transduction through gradient boosting and application to multi-scale graph neural networks. Neurips 2020.

Li et al., 2022. Generalization guarantee of training graph convolutional networks with graph topology sampling. ICML 2022.

Tang et al., 2023. Towards understanding the generalization of graph neural networks. ICML 2023.

### Questions
1. Can your theoretical analysis extend to the node classification problem?

2. Is Theorem 7 related to any distance metric proposed in Sections 3 and 4? If not, can the analysis in Sections 3 and 4 be used to derive a generalization bound?

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The present manuscript studies the approximation and generalization capabilities of message passing GNNs on attributed graphs under the lens of  proposed pseudometrics, based on the Wasserstein distance between distributions of computation tree analogs over graphons. It is demonstrated that such a pseudo metric leads to the characterization of a topology that allows to prove that message passing GNNs are universal approximations over attributed graphons, which are the fine-grained version of attributed graphs. Furthermore,  bounds on the generalization capability are provided exploiting the compactness and the lipschitzness of the retrieved topology. The theoretical findings are supported by an extensive experimental framework.

### Strengths
This manuscript provides a solid theoretical analysis of message passing GNNs under the framework of attributed graphons. The framework studies many properties, from universal approximation to generalization capabilities, therefore yielding a comprehensive overview of message passing GNNs that integrates in several ways the contribution already present in literature.

### Weaknesses
It is not explained why GINs and GraphConvs where chosen for the empirical evaluation, among the large class of message passing GNNs present in literature. I would suggest to discuss whether GIN and GraphConv are representative of different types of MPNNs, or if they have properties that make them particularly suitable for evaluating the theoretical results. 

A (short) discussion of the results of the empirical evaluation over the generalization bound is missing. I would suggest to discuss how closely the empirical results align with the theoretical bound, also considering the statistical nature of the task, or if there are any unexpected patterns or discrepancies that needs some careful consideration and warrant further investigation.

### Questions
Can the authors provide a motivation for the choice of GINs and GraphConvs for the empirical evaluation?
Can the authors provide a short discussion of the results of the empirical evaluation over the generalization bound?

### Soundness
4

### Presentation
3

### Contribution
4
