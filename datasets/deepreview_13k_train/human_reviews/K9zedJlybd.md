# Implicit degree bias in the link prediction task

- Decision: Reject
- Scores: 6, 6, 5, 5, 8, 6

## Abstract
Link prediction---a task of distinguishing actual hidden edges from random unconnected node pairs---is one of the quintessential tasks in graph machine learning.
Despite being widely accepted as a universal benchmark and a downstream task for representation learning, the validity of the link prediction benchmark itself has been rarely questioned.
Here, we show that the common edge sampling procedure in the link prediction task has an implicit bias toward high-degree nodes and produces a highly skewed evaluation that favors methods overly dependent on node degree, to the extent that a ``null'' link prediction method based solely on node degree can yield nearly optimal performance.
We propose a degree-corrected link prediction task that offers a more reasonable assessment that aligns better with the performance in the recommendation task.
Finally, we demonstrate that the degree-corrected benchmark can more effectively train graph machine-learning models by reducing overfitting to node degrees and facilitating the learning of relevant structures in graphs.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper is focused on the link prediction task and it shows how the sampling procedure applied in the evaluation of link prediction methods is biased towards high degree nodes. More specifically, the selection of random negative pairs to be distinguished against positive pairs leads to negative pairs connecting lower-degree nodes compared with the positive ones. This issue is analyzed both empirically and theoretically. To address the issue, the paper proposes a degree-correlated sampling procedure that generates negative pairs that have similar degrees as positive ones. Using this new benchmark provides a different ranking of link prediction approaches, most notably with preferential attachment achieving significantly worse results compared with GNN-based methods.

### Strengths
- The paper addresses an important issue in the evaluation of link prediction methods.
- The paper is clear and easy to follow.
- The paper applies multiple datasets and methods to support its hypothesis.

### Weaknesses
 - The definition of unbiased distribution used in the paper needs better justification
- The focus on node degree is a bit narrow given all the possible structural properties that might be biased in negative samples
- The paper does not consider state-of-the-art link prediction methods like BUDDY and NCN.

Detailed comments:

First, I need to disclose that I reviewed this paper earlier, and the authors have improved the paper significantly based on previous reviews. Still, there are some points that I believe could be better addressed:

1) Unbiased distribution: based on the paper, the unbiased degree distribution for disconnected test pairs (no class) should be the same as the one for connected test pairs (yes class). I am still not convinced why that should be the case and how the degree can still be a useful feature in this setting (as mentioned in the paper). For instance, if the proposed sampling algorithm is applied to a Barabasi-Albert graph, how would link prediction algorithms perform? Shouldn't the PA algorithm perform well in this case even if samples are unbiased?

2) Other types of bias: the paper focuses on degree bias but one could expect any connectivity-based metric to also produce a similar bias. The authors also mention shortest paths but there could be many others.

3) Link prediction methods: the proposed link prediction methods are not state-of-the-art, as shown in the papers below:

Chamberlain et al. Graph Neural Networks for Link Prediction with Subgraph Sketching.

Wang et al. Neural Common Neighbor with Completion for Link Prediction.

### Questions
1) What is the motivation for the proposed unbiased degree distribution?

2) What other similar sources of bias could affect link prediction performance? Could the proposed approach be generalized?

3) Why state-of-the-art link prediction algorithms were not considered in the experiments?

### Soundness
2

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
Observing existing link prediction models often sample partial negative edges for evaluation; this paper hypothesized that this sampled evaluation includes degree bias and would cause the link predictor model to over-fit to capture node degree signal in making a prediction. After empirical and theoretical analysis, this paper successfully demonstrates the degree of bias, proposes a degree unbiased negative sampling method, and demonstrates that the newly proposed benchmark would result in different rankings for some link prediction models and better align with recommender systems.

### Strengths
(1) This paper investigates a widely used technique for evaluating link prediction performance. The sampling bias discovered in this technique has never been systematically investigated before.

(2) This paper provides a rigorous justification, not only in terms of theoretical analysis (e.g., derived the relationship between the degree distribution and the PA link prediction AUCROC) but also empirically analyzed the performance.

(3) this paper also demonstrates several implications of using degree-corrected benchmarks, one for aligning with recommendation tasks (which is more aligned with real-world applications) and one for learning community structure.

### Weaknesses
(1) When empirically demonstrating the relationship between the degree bias and link prediction performance, this paper only leverages the preferential attachment model, which might limit the generalizability of some observations drawn in the Figure. See Question 1 for more details.

(2) Throughout the analysis, the paper does not leverage any advanced machine learning model for link prediction, such as the more recently proposed BUDDY [1] and NCN [2]. Since both explicitly model the structures into the link prediction decision-making, it will be interesting to see how their performance relates to the degree distribution. Furthermore, the largest graph used in this paper only has up to 100,000 nodes. It might be better to include a further larger graph such as citation2. Moreover, it would be more important to investigate the degree of bias for very large networks since, on small networks, it is very easy to conduct full negative edge link prediction. See question (5) for more suggestions.

[1] Chamberlain, Benjamin Paul, et al. "Graph neural networks for link prediction with subgraph sketching." arXiv preprint arXiv:2209.15486 (2022).
[2] Wang, Xiyuan, Haotong Yang, and Muhan Zhang. "Neural common neighbor with completion for link prediction." arXiv preprint arXiv:2302.00890 (2023).
[3] Hu, Weihua, et al. "Open graph benchmark: Datasets for machine learning on graphs." Advances in neural information processing systems 33 (2020): 22118-22133.

(3) The motivation of the section 3.3 is unclear. If it aims to show that the proposed benchmark captures a lower node degree, would it be better to directly demonstrate that the learned node embedding can lead to better degree prediction performance? If it is to show the benchmark capture more salient graph structures, I wonder if there is any application where the link prediction performance requires capturing the substructures.

### Questions
(1) In addition to the PA model that only belongs to the heuristic-based method, I am wondering whether we can design a more explicit method using degree, for example, designing an MLP based on only the node degree and train the model for link prediction compared with designing an MLP not based on degree and train the model for link prediction, and compare their performance. Experimenting with this way could further demonstrate such a degree of bias, which could also be captured by the learning-based method.

(2) Since we will split the original edges into training/validation/testing and we will remove testing edges in both message-passing and setup of supervision edges for training, so we also change our graph and I am wondering whether such graph change would cause the heterogeneity also change? Since following the same logic, for high-degree nodes, their neighboring edges are more easily selected as testing edges and removed

(3) In Figure D, the author attributes the advantages of the PA model over others to its explicit ability to capture degree signals. However, I’m curious about models that outperform PA. What are these models, and do they also capture degree signals? It might be better to analyze those better than PA and derive insights on whether they can capture degree signals.

(4) There are some other references discussing the degree-related bias:
 [1] Wang, Yu, and Tyler Derr. "Degree-related bias in link prediction." 2022 IEEE International Conference on Data Mining Workshops (ICDMW). IEEE, 2022.
 [2] Subramonian, Arjun, Jian Kang, and Yizhou Sun. "Theoretical and Empirical Insights into the Origins of Degree Bias in Graph Neural Networks." arXiv preprint arXiv:2404.03139 (2024).

(5) I am wondering, specifically for large-scale networks, such as the ones with nodes beyond 100,000 nodes, what would the conclusion be? I noticed from Table 2,3,4, currently the most large network is Collab (232865), which is still far less than the number of nodes in the real-world large social network. I am wondering, for those networks, whether the observed degree bias still exists. Since, for small-scale networks, we can very easily conduct full negative edge analysis rather than sample negative edges, it is essential to analyze the large-scale social network.

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This work highlights how the "standard" setup for link prediction task in graph machine learning suffers from a sampling degree bias. This bias, as shown, disproportionately affects nodes with high degrees, making node degree a dominant factor in determining link presence, irrespective of actual structural features. The authors validate their claims through empirical evaluation of a wide range of datasets and some theoretical analysis on networks with a log-normal degree distribution. They show that a naive method that just considers the degree of nodes to make a prediction performs really well in the old setup and incrementally proposes a modification to the existing setup to counter this sampling bias.

### Strengths
1. Originality: This work identifies and addresses an under-examined issue in graph machine learning benchmarks - implicit degree bias in sampling in the "standard" link prediction benchmark. By identifying and correcting this bias, the authors contribute a novel perspective on the evaluation methodologies that underpin graph-based tasks. This originality lies in highlighting how benchmark designs can inadvertently favor certain features, like node degree, thus affecting model evaluation in unintended ways. The proposed degree-corrected benchmark, although quite simple, offers an approach for mitigating this bias.

2. Quality: The paper provides a thorough analysis of degree bias, including both theoretical insights (in a specific setting) and empirical validation. The experiments span a range of datasets and link prediction methods, offering a well-rounded evaluation of the proposed benchmark's effectiveness.

3. Clarity: The paper generally communicates its objectives, findings, and implications well, especially in its discussion of degree bias and its impact on link prediction tasks. The premise is clear from the very start and is easy to read and follow, although some figures are quite hard to follow. The discussion section is well written and properly acknowledges pitfalls and potential scope in the future.

4. Significance: This work has some implications for the evaluations in this field. With the potential bias identified, newer methods that do not evaluate in any already special configurations of the link prediction benchmarks can adopt this.

### Weaknesses
Let me preface by appreciating the thorough limitations discussed in the Discussion section. Although they are acknowledged and defended to some extent, I still feel that some of the explanations are not convincing enough, and hence, you might find me mentioning a couple of them down below.

W1. The authors overgeneralize the impact of their proposed benchmark. While the described setup was the most followed one, in recent times, other works tend to adopt different sampling schemes and experimental setups [3] [4]. While this work touches on an important issue with the legacy benchmarks, I wonder how relevant they are currently.

W2. Despite highlighting degree bias, the paper fails to thoroughly compare with recent works that address similar benchmarking biases. Relevant works, such as those by [1] [2], which tackle degree-related bias, are absent. This lack of engagement with the broader literature makes the contribution feel isolated rather than a comprehensive advancement in benchmark design.

W3. Hyperparameter tuning for GNNs is missing, which is paramount while benchmarking multiple methods. While the authors mention standard settings, there is no indication that they optimized parameters for the degree-corrected benchmark. I find the results brittle as it is common knowledge that most of the GNN-based methods are very sensitive to the hyperparameters, which, when properly tuned, could result in a completely different set of results. Another weakness on the same line of reasoning is that while the authors test on 96 graphs, most of their discussions are centered around the insights from artificial datasets, rendering the depth of the dataset choices valuable only to some extent.

W4. The choice of only four GNNs among 26 total methods seems outdated, as classical link prediction methods are now less commonly used. Incorporating a more diverse set of GNN models, including more recent architectures like Graph Transformers and rewiring-infused GNNs, would better reflect the benchmark’s utility in current graph machine learning applications. These advanced GNNs, which are often the most commonly used ones in practice now, are completely missing from the evaluations, leaving a gap in the assessment of the benchmark's relevance to modern techniques.


### Questions
Q1. Can the authors clarify the hyperparameter choices for GNNs? Specifically, were parameters optimized for each benchmark setting, and if so, did tuning impact performance rankings? If no such tuning was done, I'm skeptical about the validity of the results.

Q2. What about testing in the inductive setting, where the growth of the network might deviate from its expected behavior?

Q3. Given that the degree-corrected benchmark produces substantial performance shifts, can the authors clarify how this effect arises purely from changing the negative edge sampling process?

Q4. How does the degree-corrected benchmark compare to alternative methods for addressing biases, such as distance-aware benchmarks or methods using degree-aware sampling? Although this is mentioned in the Discussions section, no result has been presented to back this up.

Q5. Could the authors provide additional evidence on the potential overfitting to large-degree nodes within the degree-corrected benchmark? Quantifying this effect with metrics like clustering or centrality could clarify the approach’s limitations.

Q6. Why is Section 2.5 (assuming no degree assortativity) relevant here, given that real-world graphs often exhibit assortative mixing? How does this assumption affect the applicability of your results to real-world graphs?

Q7. Upon simple searches online, I could find other works that alleviate the degree-induced or centrality-induced in GNNs. How do you think this benchmark will complement it? [1] [2]

Q8. I think this sort of study in the Knowledge Graph datasets would be a significant contribution, too, since link prediction is much more prevalent and often complex tasks (such as complex query answering) can be broken down into multiple link prediction tasks naively. The effects, I'm assuming, might be much more profound there. There are similar studies in that domain [3] [4].

[1] Jian Kang, Yan Zhu, Yinglong Xia, Jiebo Luo, and Hanghang Tong. 2022. RawlsGCN: Towards Rawlsian Difference Principle on Graph Convolutional Network. In Proceedings of the ACM Web Conference 2022 (WWW '22).

[2] Arun, Arvindh, et al. "CAFIN: Centrality Aware Fairness Inducing IN-Processing for Unsupervised Representation Learning on Graphs." ECAI 2023.

[3] Kamigaito, Hidetaka, and Katsuhiko Hayashi. "Comprehensive analysis of negative sampling in knowledge graph representation learning." International Conference on Machine Learning. PMLR, 2022.

[4] Madushanka, Tiroshan, and Ryutaro Ichise. "Negative Sampling in Knowledge Graph Representation Learning: A Review." arXiv preprint arXiv:2402.19195 (2024).

### Soundness
3

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
5

### Summary
Real-world graphs are sparse and have a heavy-tailed degree distribution. Thus, when measuring performance on link prediction, one should not randomly sample a bunch of edges (positive examples) and non-edges (negative examples). The paper presents a degree-corrected link prediction benchmark, where the non-edge samples have the same degree bias as edges.  The paper shows how the degree-corrected sampling learns better community structure.

### Strengths
The paper talks about an important problem and is well-written. The proposed solution is reasonable for graphs with no attributes.

### Weaknesses
The problem highlighted is well-known. For example, here are two recent works:

[1] Xie He et al. (2024). Link prediction accuracy on real-world networks under non-uniform missing-edge patterns. PLoS One, 18;19(7):e0306883. https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0306883

[2] Ayan Chatterjee et al. (2023). Improving the generalizability of protein-ligand binding predictions with AI-Bind. Nature Communications, 14, Article number: 1989. https://doi.org/10.1038/s41467-023-37572-z

### Questions
Xie He et a. [1] showed that one must consider the data collection process and application domain for link prediction. Are you suggesting that the degree-corrected sampling benchmark should be used for all graphs regardless of the application domain or the data collection process?

[1] Xie He et al. (2024). Link prediction accuracy on real-world networks under non-uniform missing-edge patterns. PLoS One, 18;19(7):e0306883. https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0306883

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 5

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper critically examines the standard link prediction benchmark in graph machine learning, revealing an inherent degree bias that favors methods overly dependent on node degree. The authors propose a degree-corrected link prediction task to address this bias, demonstrating its improved alignment with real-world recommendation tasks and its ability to train graph machine learning models more effectively.

### Strengths
1. The paper is well-structured and clearly articulates the problem, proposed solution, and implications.
2. The figures and their captions do very well to illustrate the problem and approach
3. The findings have broad implications for graph machine learning, and could potentially influence future benchmark designs and model evaluations.

### Weaknesses
1. The paper focuses primarily on undirected, unweighted graphs. It's unclear how the findings generalize to other graph types (e.g., directed, weighted). Specifically, the proposed degree correction method relies on sampling negative edges based on node degree distributions. In directed graphs, the in-degree and out-degree distributions are distinct, and it's not immediately obvious how to combine or treat these distributions for negative sampling. Similarly, in weighted graphs, the concept of degree is extended to weighted degree, and the paper does not discuss how the proposed method would account for the distribution of these weighted degrees, or how the edge weights would influence the negative sampling process.
2. The practical implications for existing graph machine learning models and their reported performances are not extensively discussed. While the paper demonstrates the degree bias in standard link prediction benchmarks, it does not provide a clear path for how existing models trained on these biased benchmarks should be re-evaluated or adapted. The paper should discuss the potential impact of this degree bias on the performance of existing models, and how the proposed degree-corrected benchmark could be used to retrain or fine-tune these models.

### Questions
1. Any intuition on how the degree-corrected benchmark would perform on directed or weighted graphs?
2. Elaborating on how the degree-corrected benchmark might be integrated into existing graph machine learning frameworks and evaluation pipelines would benefit the paper.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 6

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper illustrates the presence of an implicit bias toward high-degree nodes in the usual link prediction benchmark for graphs, potentially favoring prediction methods based on node degree (e.g. preferential attachment).

Then, authors propose a straightforward yet effective idea to address this issue by sampling negative edges with the same biased distribution as positive ones. This novel benchmark is shown to align better with link recommendation tasks. Moreover, the degree-corrected benchmark allows for training unsupervised GNN models that better capture graph structure.

### Strengths
The paper provides a detailed analysis of the standard benchmark for link prediction, revealing a bias in positive edge sampling that can lead to misleading experimental outcomes. The proposed solution is very straightforward, not very original, but effective across the experiments. While the exploration of biases in link prediction is not a new concept, the paper's contribution to improving current benchmarks for more reliable and fair results represents a valuable advancement. The clarity of the paper is generally good, particularly in the introductory sections, while there is room for improvement in the description of experiments. I have also appreciated the theoretical analyses and the amount of supplementary results reported, which ensure the overall quality of the work.

### Weaknesses
I have noticed two main weaknesses. First, aspects of the exposition lack clarity. Specifically, in Section 3.2, where authors explore the alignment with recommendation tasks, the task description is somewhat vague, and the section would benefit from a substantial revision to improve coherence and integration with the rest of the paper. The connection between link prediction and recommendation is not clearly established, making it difficult to understand the motivation for this analysis. The specific recommendation task being addressed is not well-defined, and the evaluation metrics are missing, hindering a proper assessment of the results. Second, the impact of biased negative sampling during GNN training seems underexplored in the experiments. In fact, Section 3.3 demonstrates a positive effect when graph models are trained with bias-corrected sampling, suggesting that improved community learning is due to the reduced overfitting to node degrees. However, other factors could also contribute to this improvement. For example, the reduction of distance bias, which is a consequence of degree-corrected sampling, could also play a role, as it removes easily distinguishable negative examples, potentially leading to more robust structure learning. To clarify the sources of enhancement in community detection with degree-corrected sampling, authors should include additional experiments or more detailed discussions. I elaborate further on these issues and other minor concerns in the question box below.

### Questions
(1) Section 3.2 provides a vague and unclear intuition about recommendation tasks. I strongly recommend revising this section, possibly incorporating some of the information already included in the appendix. Specifically, authors should include a clear definition of the recommendation task objective, metrics used for evaluation, and an explanation of why alignment between link prediction and recommendation is important. For instance, I wonder why not directly using link recommendation instead of a new link prediction benchmark if already the first one is less biased?   
Additionally, as a minor comment, the results presented in Figure 2B are not easy to interpret. In particular, I do not understand why using a different color for grey and orange distributions and which part of the graph highlights the alignment with recommendation tasks. Improving the clarity with a more detailed caption and/or adding labels to the picture is important for understanding the results more deeply. Moreover, the figure should be clearly referenced in the corresponding paragraph where it is discussed.

(2) Section 3.3 demonstrates notable improvements in community learning when degree-corrected sampling is applied during GNN training, suggesting that node degree overfitting is the primary factor in performance loss for community detection. However, other factors may also contribute to this improvement. For example, as mentioned in the final discussion, correcting for degree bias also reduces distance bias, making link prediction more challenging by removing easily distinguishable negative examples and thereby promoting more robust structure learning. Authors should explore more in depth this possibility, proving evidence that reduction in node degree overfitting, beyond the elimination of other possible biases, is the main reason for enhanced community learning. At this purpose, adding in Figure 3 the results with a "distance-unbiased" benchmark can be an important comparison, or alternatively, explaining why the use of the degree-corrected benchmark should be preferred to reduce distance bias (e.g., computationally faster?).

(3) Related to the previous question, Section 3.3 mentions that GNNs are trained using either the original and degree-corrected link prediction benchmarks and tested on community detection. Have you also evaluated how link prediction performance is affected —across both the standard and degree-corrected benchmarks— when training is conducted without the bias?

(4) Figures 3B and 3D show an overall improvement in learning community structure when using the degree-corrected benchmark. However, the performance gain with GAT appears minimal. Do you have any insights or hypotheses as to why this might be the case?

(5) Given that in the degree-corrected benchmark, negative sampling follows the same degree bias as positive edges, can you provide any theoretical guarantee, empirical evidence, or link to other works, showing that the pairs involving low-degree nodes (mostly neglected during sampling) have a minor impact on prediction accuracy?

### Soundness
3

### Presentation
3

### Contribution
3
