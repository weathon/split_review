# A Topological Perspective on Demystifying GNN-Based Link Prediction Performance

- Decision: Accept
- Scores: 5, 6, 6, 6

## Abstract
Graph Neural Networks (GNNs) have shown great promise in learning node embeddings for link prediction (LP). While numerous studies aim to improve the overall LP performance of GNNs, none have explored its varying performance across different nodes and its underlying reasons. To this end, we aim to demystify which nodes will perform better from the perspective of their local topology. Despite the widespread belief that low-degree nodes exhibit poorer LP performance, our empirical findings provide nuances to this viewpoint and prompt us to propose a better metric, Topological Concentration (TC), based on the intersection of the local subgraph of each node with the ones of its neighbors. We empirically demonstrate that TC has a higher correlation with LP performance than other node-level topological metrics like degree and subgraph density, offering a better way to identify low-performing nodes than using cold-start. With TC, we discover a novel topological distribution shift issue in which newly joined neighbors of a node tend to become less interactive with that node's existing neighbors, compromising the generalizability of node embeddings for LP at testing time. To make the computation of TC scalable, We further propose Approximated Topological Concentration (ATC) and theoretically/empirically justify its efficacy in approximating TC and reducing the computation complexity. Given the positive correlation between node TC and its LP performance, we explore the potential of boosting LP performance via enhancing TC by re-weighting edges in the message-passing and discuss its effectiveness with limitations.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposes a new metric called Topological Concentration (TC) for GNN-based link prediction. The authors also discover a novel topological distribution shift issue and use TC to quantify this shift and its negative impact. They design a message-passing scheme that reweights the edges based on the contribution of the neighbors. They show that this scheme can enhance TC and boost link prediction performance to some extent.

### Strengths
- The paper proposes a novel metric, Topological Concentration (TC), to measure the varying link prediction performance across different nodes.
- It demonstrates the superiority of TC over other node topological properties, such as degree and subgraph density.
- It explores the potential of boosting GNNs’ LP performance by enhancing TC via re-weighting edges in message-passing.

### Weaknesses
 - The writing is unclear and hard to follow. The notations are confusing. The paper uses similar symbols for some concepts, such as ${TC}^{TR}$, ${TC}^{Tr}$, ${Tc}^{Tr}$, which are hard to distinguish. The paper also uses uncommon abbreviations for training and testing sets, such as Tr and Te.
- The motivation of probing the node characteristic for LP is questionable. The paper does not explain why this is a meaningful problem, given that [1] has proven that LP cannot be reduced to two node problems.
- The definition of Topological Concentration is complicated and the rationality is not obvious. The paper uses a complex formula to find the intersection of subgraphs at different hops, but does not justify its choice, such as the exponential decaying coefficients. Why don't you define $\mathcal{H}_i^k$ as $k$-hop neighbors, which is more clear and straightforward?
- The organization is confusing. The paper switches between different topics without clear transitions. For example, it introduces TC in section 3.2, then discusses cold-start nodes and distribution shift in section 3.3, and then returns to TC in section 3.4.
- Obs.2 and Obs. 3 in section 3.3 seem irrelevant for the proposed model and discussion. The paper does not explain how these observations inform the design or evaluation of the edge reweighting strategy.
- The technical novelty is limited. The paper only proposes edge reweighting as a strategy to enhance LP performance, which is a common technique in LP [2,3]. The paper does not compare or contrast its strategy with existing methods.
- The experiment in this paper is weak. You only show the relative gain of GCN/SAGE/NCN with reweighting, but you do not compare with the SOTA LP methods like BUDDY [4]. Your result is not competitive, as you only achieve 54% Hits@50 on Collab. Why do you not include experiments on other OGB datasets like ogbl-ddi and ogbl-ppa?
- The paper lacks ablation studies or case studies to demonstrate the effectiveness of the reweighting strategy. You could also provide some qualitative analysis or visualization to show how the reweighting strategy affects the prediction results.
- The font in every figure is too small to read, and the figures are not well-designed.

### Questions
See Weaknesses.

### Soundness
3 good

### Presentation
2 fair

### Contribution
3 good

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The authors identify a gap in understanding how different nodes in a graph achieve varying LP performance. They propose the Topological Concentration (TC) and its scalable version, Approximated Topological Concentration (ATC) metrics, which offer a more accurate measurement of the correlation between local subgraph structure and LP performance compared to traditional node degrees. Surprisingly, the paper reveals a counterintuitive observation that LP performance does not consistently increase with node degree, challenging conventional wisdom. Additionally, the paper uncovers a Topological Distribution Shift (TDS) issue, which impacts LP generalizability and highlights the importance of TC in understanding node-level LP performance. The authors propose TC-inspired message-passing techniques to enhance LP performance by focusing on well-connected neighbors within a node's computational tree. Overall, this research contributes valuable insights into LP performance variation and cold-start issues in GNNs, with potential implications for improving network dynamics and LP strategies.

### Strengths
* The paper's introduction of the Topological Concentration (TC) and Approximated Topological Concentration (ATC) metrics provides a new and innovative approach to addressing the variation in Link Prediction (LP) performance within Graph Neural Networks (GNNs). 

* The paper's observation that LP performance does not consistently increase with node degree challenges existing assumptions in the field. This counterintuitive finding sparks curiosity and adds an element of novelty to the research.

* The paper proposed a new method to improve model's link prediction performances based on their TC and show empirical results.

### Weaknesses
 * Discussion of the time complexity is not so good. The adjacent matrix are based on each layer's embedding, so the time consumption will be larger. Experiments on this are needed.
* Subgraph-based methods as baselines are not so complete.

### Questions
* Can you measure the time complexity through experiments? I guess the time consumption will not be so close to the original method.

* NCN already explicitly accounts for this common neighbor signal in its decoder, the performance gains from our strategy are relatively modest. So why don't you choose another subgraph-based method because I'm curious what's your strategy's effect on subgraph-based methods that don't explicitly use common neighbor signals. 

* How to get the performances of link prediction of nodes with different TC? I mean one link has two nodes. For example for the results for nodes'TC in \[0,0.2\), does every link includes two nodes in that domain or just one node is enough?


* Have you tried to make TC^{Tr} closer to TC^{VAL}, if wanting to make model more generalizing to prediciting test links. Because we may assume validation set has the same distribution of test set.
* In Figure 7(a), why the curve of training original graph has several fast down of performances?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposes a metric "Topological Concentration" (TC) as a new measure for Link Prediction (LP) in GNNs.
TP is basically the intersection of the subgraphs of extremal nodes $i$ ans $j$ of an edge $(i,j)$. A concept very similar
to the common-neighbors heuristic. The authors claim "With TC, newly joined neighbors of a node tend to become less 
interactive with that node’s existing neighbors, compromising the generalizability of node embeddings for LP at the testing time". 

There is empirical evidence that GNNs perform better on high-degree nodes than on low-degree nodes. However, the authors 
observe that this is not the case in LP. TC seems to find better correlations with LP performance (again, as common neighbors). 
TC also inspires a new message-passing strategy considering well-connected neighbors. 

The authors highlight the good properties of their measure and propose how to compute it efficiently. ATC (approximated topological 
concentration) relies on powers-hops of the transition matrix. This is $O(Kd(|E| + |V|))$, where $K$ is the maximum hop. 

The experiments show that TC boosts the performance of LP in several basic baselines. No comparisons with subgraph-based baselines.

### Strengths
* Formalization of an intuition (common neighbors and subgraph-based methods for LP). 
* Nice empirical study on the properties of TC. 
* ATC is efficient.

### Weaknesses
 * No comparison with state-of-the-art subgraph-based methods (e.g. subgraph sketching).

 * The ATC heavily depends on the powers of the transition matrix. In this regard, how do you fix $K$? Large values of $K$ lead to a matrix with constant rows (ergodicity theorem).
* What are the computational advantages wrt subgraph-sketching, if any?
* What is the expected gain in performance wrt to state-of-the-art LP methods beyond the common-neighbors heuristic?

### Questions
* The ATC heavily depends on the powers of the transition matrix. In this regard, how do you fix $K$? Large values of $K$ lead to a matrix with constant rows (ergodicity theorem). 
* What are the computational advantages wrt subgraph-sketching, if any? 
* What is the expected gain in performance wrt to state-of-the-art LP methods beyond the common-neighbors heuristic?

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper proposes a novel metric called Topological Concentration (TC) to demythify the varying performance of Graph Neural Networks (GNNs) in link prediction across different nodes. The authors demonstrate that TC has a higher correlation with link prediction performance than other node-level topological metrics like degree and subgraph density. They also uncover a novel Topological Distribution Shift (TDS) issue and propose an Approximated Topological Concentration (ATC) to address the computational complexity of TC. The paper concludes by exploring the potential of boosting link prediction performance via enhancing TC.

### Strengths
- The paper introduces a new metric, Topological Concentration (TC), which provides a better characterization of node link prediction performance in GNNs than traditional metrics like degree and subgraph density.
- The authors uncover a novel Topological Distribution Shift (TDS) issue and demonstrate its negative impact on link prediction performance at the node and graph levels.
- The paper proposes an Approximated Topological Concentration (ATC) to address the computational complexity of TC, while maintaining high correlations to link prediction performance.
- The authors explore the potential of boosting link prediction performance by enhancing TC through edge reweighting in message-passing and discuss its efficacy and limitations.

### Weaknesses
 - The paper could benefit from a more comprehensive evaluation of the proposed methods on a wider range of datasets and benchmark tasks. This would help to establish the generalizability and robustness of the proposed techniques across different domains and problem settings. Specifically, the current evaluation seems limited to relatively small datasets; testing on larger, more complex graphs, such as those with millions of nodes and edges, would be crucial to assess scalability. Furthermore, the paper should include a more diverse set of graph types, including those with varying densities and structural properties, to ensure the method is not overly tailored to specific graph characteristics.

- The theoretical analysis of the relationship between TC and link prediction performance could be further strengthened with additional mathematical proofs or rigorous analysis. Providing a more solid theoretical foundation would increase the credibility and impact of the proposed methods. The current justification relies primarily on empirical correlations, which, while suggestive, do not provide a deep understanding of why TC is effective. A more formal analysis, perhaps using tools from spectral graph theory or information theory, could provide a more robust theoretical underpinning. For instance, it would be beneficial to explore the connection between TC and the eigenvalues of the graph Laplacian or the entropy of node neighborhoods.

- The paper could discuss the limitations and potential biases of the proposed evaluation metrics, such as TC and ATC. Addressing these concerns would help to ensure that the results are reliable and that the methods are not overly sensitive to specific aspects of the data. For example, it is unclear how TC and ATC might be affected by homophily or heterophily in the graph. A discussion of these potential biases, along with strategies to mitigate them, would strengthen the paper. Moreover, the paper should clarify the sensitivity of TC and ATC to different choices of hyperparameters, such as the dimensionality of the node embeddings and the number of message-passing steps.

- The paper could provide a more in-depth analysis of the cold-start problem and its relationship with the proposed metrics, as well as discuss potential strategies for addressing this issue. The current discussion of cold-start nodes is somewhat superficial. A more detailed analysis of how TC and ATC perform on nodes with very few connections, and how this performance compares to other methods designed specifically for cold-start scenarios, would be valuable. Furthermore, the paper should explore whether the proposed edge reweighting strategy is effective for cold-start nodes, or if additional techniques are needed.

### Questions
- Could you please provide more details on the implementation of the Approximated Topological Concentration (ATC) and its theoretical justification for approximating TC? This would help to better understand the rationale behind the proposed method and its potential advantages over other approaches.

- How do the proposed methods compare to other state-of-the-art link prediction techniques in terms of performance and computational efficiency? 

- What does the "cold-start" nodes mean? Please clarify the definition and implications of cold-start nodes in the context of link prediction. This would help to better understand the relevance and importance of addressing the cold-start problem in the proposed methods.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good
