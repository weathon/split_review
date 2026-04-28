# Understanding Community Bias Amplification in Graph Representation Learning

- Decision: Reject
- Avg Score: 5.00
- Scores: 6, 6, 3

## Abstract
In this work, we discover a phenomenon of community bias amplification in graph representation learning, which refers to the exacerbation of performance bias between different classes by graph representation learning. We conduct an in-depth theoretical study of this phenomenon from a novel spectral perspective. 
Our analysis suggests that structural bias between communities results in varying local convergence speeds for node embeddings. This phenomenon leads to bias amplification in the classification results of downstream tasks. Based on the theoretical insights, we propose random graph coarsening, which is proved to be effective in dealing with the above issue. Finally, we propose a novel graph contrastive learning model called Random Graph Coarsening Contrastive Learning (\ourmodel), which utilizes random coarsening as data augmentation and mitigates community bias by contrasting the coarsened graph with the original graph. Extensive experiments on various datasets demonstrate the advantage of our method when dealing with community bias amplification.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper identifies a problem in graph representation learning on graphs with community structures. When the communities have different strengths (e.g., edge densities), the representations of nodes from different communities convergence at different speeds. In the resulting representations, this may lead the representations of nodes from weaker communities to be further apart, which may result in poor classification results on these classes downstream. 
The paper introduces a contrastive learning approach using random graph coarsening to ameliorate this issue.
Experiments show that this learning model outperforms existing representation learning methods.

### Strengths
The paper is well written, with only few language errors and typos.

The problem that is identified is interesting and subtle.

The proposed solution seems elegant.

### Weaknesses
It took me quite a while into reading the paper before I understood what was actually meant with this community bias. I think the introduction of this bias can be made a bit more concrete to improve this.

The message passing operator $\hat{A}$ is mentioned but not introduced properly. Is this supposed to be the renormalized version of $\tilde{A}$ that is shown in (1) or should it be something else?

The performance in the experiments are measured by the Accuracy and Macro-F1 measure. Both of these methods have biases w.r.t. class sizes [1,2]. I understand why you use Accuracy, as you also use this to motivate the community bias, but perhaps you could replace Macro-F1 by the Matthew's coefficient.

### Questions
Consider removing "Understanding" from the title, as it sounds a bit generic and makes the title seem less strong.

Instead of using this contrastive learning approach, can't we just cluster the obtained representations by a density-based clustering method like DBSCAN? The problem of different clusterings having different densities doesn't seem like a new problem in clustering.

It would be interesting to compare the performance of these representation learning methods to community detection methods like the Louvain algorithm [1] or Bayesian community detection methods [2]. This latter method also addresses the issue of different communities having different densities, but does so in a statistical framework.

[1] Blondel, V. D., Guillaume, J. L., Lambiotte, R., & Lefebvre, E. (2008). Fast unfolding of communities in large networks. Journal of statistical mechanics: theory and experiment, 2008(10), P10008.
[2] Zhang, L., & Peixoto, T. P. (2020). Statistical inference of assortative community structures. Physical Review Research, 2(4), 043271.

### Soundness
3 good

### Presentation
3 good

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
In this paper, the authors explore a phenomenon called "community bias amplification" in graph representation learning. This phenomenon refers to the exacerbation of performance bias between different classes by graph representation learning methods. The researchers conduct a thorough theoretical investigation of this phenomenon, approaching it from a novel spectral perspective. Their analysis reveals that the structural bias between communities leads to varying local convergence speeds for node embeddings, resulting in biased classification outcomes in downstream tasks. To address this issue, the authors propose a solution called random graph coarsening. This technique is demonstrated to be effective in mitigating the problem of bias amplification. Furthermore, the authors introduce a novel graph contrastive learning model named Random Graph Coarsening Contrastive Learning (RGCCL). This model utilizes random graph coarsening as a form of data augmentation and alleviates community bias by contrasting the coarsened graph with the original graph. Extensive experiments conducted on various datasets highlight the effectiveness of their proposed method in addressing community bias amplification in graph representation learning tasks.

### Strengths
- The problem of community bias amplification in GRL is very interesting and has not been extensively studied before.

- The analysis is theoretically sound with appropriate discussion and remarks.

- Experiments on several benchmark graphs show the effectiveness (better node representations) and efficiency (less memory usage) of the proposed method.

### Weaknesses
 - One of the research questions has not been answered in a good way, i.e., why community bias amplification exists in existing GCL method? Although some theoretical analyses have been provided in this paper, they are based on general (and simplified) graphs and it is not clear why there is such bias in GCL methods.

- How to quantitatively measure the (community) bias amplification is not clear in the experiments. More analysis should be conducted to better illustrate why the proposed method is able to mitigate the issue of bias amplification. For example, some measures [1] can be used for the quantitative analysis.

### Questions
- What are the answers to the first research question, i.e., why community bias amplification exists in existing GCL method?

- It is possible to give some quantitative analysis on how the proposed method can mitigate the issue of community bias amplification rather than simply comparing the performance between different classes/communities?

- Discussion on extending this key idea to general GRL. I asked this question because the theoretical analysis is general enough on any GRL methods.

### Soundness
3 good

### Presentation
2 fair

### Contribution
3 good

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
For the graph learning, this paper discovers the phenomenon which this paper calls community bias amplification. This paper provides theoretical analysis on this phenomenon. Using this theoretical insights, this paper proposes a graph learning algorithm to mitigate this bias. The experimental results show that the proposed method outperforms the existing ones.

### Strengths
A problem this paper focuses on is interesting. Seeing Fig.1, it is convincing that a bias between classes surely exists, and this itself is novel as far as I believe, at least in the GNN realm.

### Weaknesses
1. I do not agree with the authors claim on where the bias comes from. 
The datasets for illustrative examples in Fig.1 contain the independent components. 
Oono and Suzuki (2020) and its earlier work [1] shed a light on the phenomenon over-smoothing -- if we stack layers, the stacked adjacency matrix is dominant by the eigenspace associated with the largest eigenvalues. In the Cora and Citeseer cases, that space is a set of indicate vectors of independent components. 
Also, the claim is this worsens the performance, which is understandable, since the only this eigenspace of the independent components are too simplified as an underlying structure. 
However, the underlying graph structure does not necessarily correspond to the classes, while of course graph structure and the classes are loosely related. 
If they are, we observe somewhat comparative performance only using the graph of Cora and Citeseer, but we do not observe such performance by conducting for example the simple spectral clustering on graph. 
Thus, the community amplification bias of the underlying graphs is not the primal reason why we observe the unfairness of Fig. 1. 
Instead, I believe that the bias is more nuanced -- hope to see what is the dominant.


2. Also, even if the community bias were primal reason, the argument of Eq. (3) is weak since they only compare the value of the eigenvalues of two clusters. Also, how the example of Appendix A reflects the Cora and Citeceer dataset? Do we observe such things in the real datasets? How do you argue that?

### Questions
How do you defend that the community amplification bias of the underlying graph is the primal reason we observe an unfairness between classes? As stated in the weakness section, I feel like there exists some gap between them.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair
