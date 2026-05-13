# Local Graph Clustering with Noisy Labels

- Decision: Accept
- Scores: 3, 8, 6, 6

## Abstract
The growing interest in machine learning problems over graphs with additional node information such as texts, images, or labels has popularized methods that require the costly operation of processing the entire graph. Yet, little effort has been made to the development of fast local methods (i.e. without accessing the entire graph) that extract useful information from such data. To that end, we propose a study of local graph clustering using noisy node labels as a proxy for additional node information. In this setting, nodes receive initial binary labels based on cluster affiliation: 1 if they belong to the target cluster and 0 otherwise. Subsequently, a fraction of these labels is flipped. We investigate the benefits of incorporating noisy labels for local graph clustering. By constructing a weighted graph with such labels, we study the performance of graph diffusion-based local clustering method on both the original and the weighted graphs. From a theoretical perspective, we consider recovering an unknown target cluster with a single seed node in a random graph with independent noisy node labels. We provide sufficient conditions on the label noise under which, with high probability, using diffusion in the weighted graph yields a more accurate recovery of the target cluster. This approach proves more effective than using the given labels alone or using diffusion in the label-free original graph. Empirically, we show that reliable node labels can be obtained with just a few samples from an attributed graph. Moreover, utilizing these labels via diffusion in the weighted graph leads to significantly better local clustering performance across several real-world datasets, improving F1 scores by up to 13\%.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper studies the local graph clustering task using noisy node labels. The theoretical justification is provided to investigate the benefits of incorporating noisy labels for local graph clustering. Some empirical results are shown to illustrate the method.

### Strengths
- Graph clustering is a very fundamental problem for graph-related problems, and exploring noisy labels perspective is a very interesting topic.
- The paper is well-organized and easy to be understood.

### Weaknesses
 - About my confusion with the setting of the paper. The setting is local graph clustering or local graph clustering with noisy node labels? If it is local graph clustering, I think this paper tackles the local graph clustering problem with the help of noisy labels. The authors say that they abstract all available sources of additional information as noisy node labels. However, the setting of their experiments does not reflect this point, i.e., they only use the predicted labels as the noisy labels. I did not see any other available sources to transform into noisy labels. If the setting is local graph clustering with noisy node labels, the authors should compare the proposed method with other existing methods that focus on this setting, i.e., node labels should be contained in the compared methods. So the experiments have limitations. I hope the authors clarify the setting and make more comparisons with existing methods. Experiments should be enriched to verify the effectiveness of the method.
- The paper lacks complexity analysis.
- The comparison of the empirical running time of each method should be contained. Hyperparameter analysis is also missed. 
- The analysis and discussion of the empirical results are clearly inadequate.

### Questions
See above.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper studies local graph clustering (identifying a small cluster containing the seed nodes) with noisy node labels. The authors propose a localized algorithm based on flow diffusion on a weighted graph constructed from the noisy labels. For a particular local random model, it is shown that the proposed algorithm yields an accurate recovery of the target cluster with high probability measured by F1 score. The authors also demonstrate through synthetic data as well as several real-world datasets that the approach has better performance compared to using edges or labels alone.

### Strengths
1. The problem of recovering a small cluster with additional noisy labels is new and interesting.
2. The proposed method, though based on a simple modification of flow diffusion, is localized and computationally efficient.
3. The theoretical analysis is sound and convincing. Moreover, it addresses the situation when the F1 score of labels is very low.
4. The experiments further justify the findings and show significant improvements over using only edges or labels.

### Weaknesses
1. Flow diffusion has been studied extensively under various settings in the literature. The current work is a direct application of it.
2. The theoretical analysis is limited to a very simple random graph model in specific parameter regimes, and there is room for stronger arguments (see question 2-5).
3. The choice of several parameters in the algorithm probably requires more investigation and discussion (see question 1). Specifically, the parameter $\epsilon$ which interpolates between using only edges or only labels, needs a more principled approach. The current method relies on a heuristic choice without clear guidance on how it should be adapted to different graph structures or noise levels.

### Questions
1.  As noted by the authors, $\epsilon$ interpolates between two special scenarios that are suitable for different level of label noise. From a theoretical perspective, how should $\epsilon$ be chosen if $a_0$ and $a_1$ are known? Also, is there possibly a way to estimate $\epsilon$ and $\theta^\dagger$ from the graph?
2. The main theorem requires $p = \omega(\frac{\sqrt{\log k}}{\sqrt{k}})$ which produces a dense cluster. Can this condition be relaxed to include less dense clusters?
3. Is there an information-theoretic limit on recovering local graph cluster with noisy labels such that the sharpness of the lower bound on F1 can be evaluated?
4. It would be helpful to compare the current result with these on local graph clustering without labels. In particular, when the labels do not provided any information ($a_0 = a_1 = 1/2$), does the proposed algorithm have improvements over the previous ones?
5. Weighted message passing is another localized algorithm applied to SBM with noisy label information (see [1] and references therein). How does the flow diffusion algorithm and theoretical result compare to it?

[1] Cai, T. T., Liang, T., & Rakhlin, A. (2020). Weighted message passing and minimum energy flow for heterogeneous stochastic block models with side information. The Journal of Machine Learning Research, 21(1), 346-379.

### Soundness
3 good

### Presentation
4 excellent

### Contribution
3 good

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
In this paper, the authors study the local graph clustering problem. They investigate the benefits of incorporating noisy labels for local graph clustering. By constructing a weighted graph with such labels, they study the performance of graph diffusion-based local clustering method on both the original and the weighted graphs. The experimental results demonstrate the effectiveness of the proposed methods.

### Strengths
S1. The problem studied in the paper is important.
S2. The performance of flow diffusion over a random graph model is analyzed.
S3. Empirical experiments are conducted to evaluate the proposed methods.

### Weaknesses
W1. It is unclear whether the proposed method needs to explore the entire graph. Specifically, the introduction states the goal of local graph clustering is to avoid exploring the entire graph, but the paper does not clearly articulate how the proposed method achieves this locality. The description of the algorithm lacks sufficient detail to determine if it requires global graph information or if it can operate using only local neighborhood information.

W2. The relation between the additional node information like texts, images and the proposed methods is unclear. While the paper mentions that such information can be beneficial, it does not explain how this information is incorporated into the proposed label-weighting scheme or the diffusion process. It is not clear how the high-dimensional vector representations of texts or images are converted into the noisy node labels used by the method. The paper needs to provide a concrete mechanism for leveraging this additional information.

W3. Whether the compared methods in the experiment section are comprehensive or not is unclear. The experiments only compare against flow diffusion and Label-based PageRank. It is not clear if these are the most relevant baselines, or if other state-of-the-art local graph clustering methods should also be included. The paper does not provide a strong justification for the choice of these specific methods, and it is unclear if the results would generalize to other methods.

### Questions
Q1. In Section 1, the authors claim that the task of local graph clustering aims to
identify a small cluster of nodes that contains all or most of the seed nodes, without exploring the entire graph. However, it is unclear whether the proposed method needs to explore the entire graph.

Q2. In Section 1, the authors claim that the additional information like texts, images can significantly benefit clustering, but the relation between the additional information and the proposed methods is unclear.

Q3. Only flow diffusion and Label-based PageRank methods are compared in the experiments, it is unclear whether the compared methods in the experiment section are comprehensive or not.

Q4. It is unclear whether the assumption on a_0 and a_1 is practical in real applications.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper proposes a method that leverages noisy node labels for local graph clustering. In this approach, edge weights are defined based on the noisy labels in the graph, giving higher weight to nodes with the same noisy label and lower weight to nodes with different labels. Using this weighted graph, the authors apply a graph diffusion local clustering method called 'flow diffusion' to determine the clustering. The paper includes both theoretical proofs and empirical evidence, demonstrating why this approach improves clustering accuracy compared to applying the flow diffusion method directly to the original graph.

### Strengths
The proposed method for local graph clustering is conceptually simple and easy to implement while apparently being effective. It is also flexible, as it can be combined with different diffusion-based local clustering algorithms. In addition, the authors provide theoretical guarantees for its success under mild conditions.

### Weaknesses
The experimental section lacks a comparison with alternative methods that are not flow-based.

The paper lacks a detailed exploration of the algorithm's sensitivity to hyperparameters. While the robustness to the choice of $\epsilon\in[0.01,0.1]$ is briefly mentioned, there is no reference to the robustness of the source mass of the seed ($\Delta_s$). For the experiments with the synthetic datasets, different $\Delta_s$ values are tested but only the best is provided. The paper would benefit if there was an study on the choice of the hyperparameters.

The discussion regarding Theorem 3.4 is not adequately understandable. See questions for more details.

### Questions
- Regarding the discussions following Theorem 3.4:
  
  - The statement that "as $\gamma$ becomes lager, it generally becomes more
    difficult to accurately recover K [the cluster]" appears counterintuitive. Given that $\gamma\coloneqq \frac{p(k-1)}{q(n-k)}$ signifies the ratio of internal to external connections within a cluster, an increase in $\gamma$ implies more internal connections. This suggests a stronger, more cohesive cluster. Could you elaborate on why higher $\gamma$ values lead to increased difficulty in cluster recovery?
  
  - The assertion that "F1 is lower bounded by a constant as long as $\gamma$ is a constant" raises questions.  What does "$\gamma$ is constant" mean in this context? As far as I understand, the value $\gamma$ is defined for each node and implicitly depends exclusively on the cluster size, $k$, and the edge probabilities, $p$ and $q$. I suggest that this dependence is stress further, since as it is written now, $\gamma$ is apparently a constant by itself. Consequently, I guess that "$\gamma$ constant" means that it has the same value for all nodes (or for all clusters). Nonetheless, the lower bound of F1 would still depend on $a_0$ and $a_1$. Could you clarify why the lower bound of F1 is described as a constant despite potential dependencies on other parameters?
  
  - The statement, "even when the initial labels are deemed fairly accurate based on $a_0$ and $a_1$, e.g. $a_1$ = 1, $a_0$ = 0.99, the F1 score of the labels can still be very low." Could you explain the factors contributing to the low F1 score in this scenario?

- How robust is the proposed method concerning the source mass of the seed ($\Delta_s$)?

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair
