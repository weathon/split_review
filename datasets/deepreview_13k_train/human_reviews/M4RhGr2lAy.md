# Fairness-Aware Graph Learning: A Benchmark

- Decision: Reject
- Scores: 5, 5, 3, 3, 6

## Abstract
Fairness-aware graph learning has gained increasing attention in recent years. Nevertheless, there lacks a comprehensive benchmark to evaluate and compare different fairness-aware graph learning methods, which blocks practitioners from choosing appropriate ones for broader real-world applications. In this paper, we present an extensive benchmark on ten representative fairness-aware graph learning methods. Specifically, we design a systematic evaluation protocol and conduct experiments on seven real-world datasets to evaluate these methods from multiple perspectives, including group fairness, individual fairness, the balance between different fairness criteria, and computational efficiency. Our in-depth analysis reveals key insights into the strengths and limitations of existing methods. Additionally, we provide practical guidance for applying fairness-aware graph learning methods in applications. To the best of our knowledge, this work serves as an initial step towards comprehensively understanding representative fairness-aware graph learning methods to facilitate future advancements in this area.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper provided a comprehensive protocol to evaluate the performance of fairness-aware graph learning methods. Extensive experiments on seven real-world attributed graph datasets with ten fairness-aware graph learning methods were conducted to induce in-depth analysis for the benchmark results.

### Strengths
1. This paper provided a comprehensive benchmark over ten very recent fairness-aware graph learning methods, including both group fairness and individual fairness. A clear timeline and categorization were provided to help the presentation of the whole study.
2. Extensive experiments on seven datasets and ten methods were conducted and were well organized to answer the four research questions. Various metrics in utility, group fairness and individual fairness were compared.
3. In Section 4, the results in the tables were further partially compared in figures to discuss the limitations and strengths of different methods, which validated the findings of the authors.
4. Practical guidance was provided for users to help choose the most appropriate fairness-aware graph learning methods.

### Weaknesses
 1. The discussion mostly focused on stating the observations that different methods have different performances on different metrics. However, a more in-depth discussion of why these methods have different advantages could be added. E.g., how do different objective functions in the methods benefit certain fairness notions? For instance, methods that directly minimize a fairness metric might perform well on that specific metric but could suffer in overall utility, while methods that use adversarial training might achieve a better balance but with higher variance. This should be explored further.
2. For a benchmark study of fair graph learning, how do you choose the datasets for testing? What is the group density in the graphs? Are the groups balanced or not? These details could be clarified to justify the diverse choice of datasets for evaluation. The selection criteria should be more transparent, and the implications of imbalanced groups on the performance of different methods should be discussed. For example, how do methods perform when the protected group is a small minority or a large majority?
3. What are the connections and the comparison within different group fairness metrics, within different individual fairness metrics, and between them? Can you provide more explanations in Section 4.3? For example, how does statistical parity difference relate to equal opportunity difference, and when might one be more appropriate than the other? Similarly, how do different individual fairness metrics capture different aspects of individual fairness, and what are their trade-offs?
4. Although the authors studied efficiency in Section 4.4, it is not well discussed as a factor in their practical guidance. The practical guidance should explicitly consider the computational cost of different methods, especially when dealing with large-scale graphs. The trade-off between fairness, utility, and efficiency should be discussed in the context of practical applications.

### Questions
1. I did not find the newly constructed datasets AMiner-S and AMinder-L in the supplemental materials, which I think may count for part of the contributions of this work. Am I missing something?
2. In lines 334-335 you mentioned "neither DeepWalk nor GNN yields top-ranked performance under utility". Where does this statement come from? DeepWalk achieves an even worse ranking in utility than fairness.
3. In Figure 3, what do dots of different colors stand for?

### Soundness
3

### Presentation
4

### Contribution
2

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This work addresses the pressing issue of fairness in graph learning by providing a comprehensive evaluation of ten fairness-aware graph learning methods. The authors propose an experimental setup to evaluate these methods across seven real-world datasets, focusing on group fairness, individual fairness, the balance between fairness and utility, and computational efficiency. Their systematic approach aims to offer guidance to practitioners for selecting appropriate fairness-aware methods in real-world applications.

### Strengths
1. Originality: Although the motivation and the idea to do this kind of study have been attempted in the past, as pointed out by the authors, they also make a clear distinction of how their approach is different.

2. Quality: The empirical evaluation is extensive, spanning several datasets and including multiple fairness and utility metrics. Common checkmarks for benchmark works like hyperparameter tuning, reporting across multiple runs, etc., are taken care of.

3. Clarity: Key objectives and methods are introduced clearly, and the premise is set clearly without any confusion on the objective of the work. The work is very easy to read and follow, and the figures and the metrics reported are well explained.

4. Significance: Fairness in machine learning on graphs is a growing area of importance, and this benchmark offers a much-needed reference point for comparing fairness-aware graph methods. While there are more definitions of fairness in this domain, this work covers the most widely used settings.

### Weaknesses
W1. The paper implies that this benchmark is a comprehensive evaluation of fairness-aware methods, yet it evaluates only a subset of fairness criteria. There are prior works that cover more inherent fairness issues in GNNs that do not depend upon the node characteristics [1,2], and the evaluation of such methods would have also been a great addition. Specifically, methods addressing structural biases or those that consider the propagation of bias through the graph structure are absent from the evaluation.

W2. While the benchmark includes a selection of ten methods, the paper does not sufficiently discuss recent advancements in fairness-aware graph learning, such as methods that address intersectional biases or temporal fairness. This limits the relevance of the benchmark for contemporary applications and makes it appear somewhat outdated in the rapidly evolving fairness landscape. The evaluation lacks methods that consider the dynamic nature of graphs and how fairness evolves over time, which is crucial in many real-world scenarios.

W3. Experimental details are insufficiently described. Important aspects such as hyperparameter search ranges, validation criteria, and dataset preprocessing steps are either missing or vaguely specified. While Figure 3 conveys some parts of it, the exact ranges specified and the final hyperparameters used would be helpful for reproducibility. The absence of specific details makes it difficult to reproduce the results and assess the robustness of the findings.

W4. The benchmarking focuses mainly on fairness-aware graph neural networks (GNNs) and shallow embeddings but lacks methods that might employ fairness-enhancing architectures or hybrid models. Expanding this range would make the benchmark more relevant and impactful. The current selection does not include methods that combine graph learning with adversarial training or other techniques to enhance fairness.

W5. The benchmark briefly touches on computational efficiency but does not thoroughly investigate the scalability of these fairness-aware methods on large-scale graph datasets. Given that scalability is a crucial consideration for real-world applications, particularly in social networks or knowledge graphs, this is a notable omission. The evaluation should include a more detailed analysis of the computational cost and memory requirements of each method on varying graph sizes.

W6. While the findings validate existing assumptions in the field, they don't offer novel insights beyond what practitioners would already understand through experience. The results largely confirm known trade-offs between fairness and utility, without providing new perspectives or actionable recommendations.

### Questions
Q1. Can the authors clarify the hyperparameter tuning process? Specifically, were grid search ranges adjusted for each dataset, and how were optimal settings chosen? What were the search ranges, and how were they decided upon?

Q2. The dataset selection includes only node classification tasks. Can the authors comment on the applicability of this benchmark for link prediction or other graph-based tasks?

Q3. More realistic scenarios that often have hybrid fairness objectives have not been tested; what would be the performance of these methods in those settings?

Q4. How does the benchmark account for potential variations in fairness definitions across different domains, especially when the impact of bias may differ (e.g., financial vs. social networks)?

Q5. It would be interesting to see the GNN methods running without (or with random) node attributes since the claim that the "absence of bias brought by node attributes" is mentioned in two places in the text without any supporting evidence.

Q6. The confidence intervals in Figure 2 overlap a lot, which is why I'm unsure about the statistical validity of the claims. Can the authors verify the significance of the results presented?

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
5

### Summary
In this paper, the authors aim to establish a benchmark for fairness-aware graph learning to guide practical applications by evaluating the trade-off between fairness and performance of multiple graph learning methods. To this end, the authors propose a set of evaluation protocols covering group fairness and individual fairness metrics, summarize and test the fairness and performance of ten representative fairness graph learning methods on seven real-world datasets, provide systematic experimental results and analyses demonstrating their trade-offs between fairness and utility, as well as constructing a reliable and quantitative basis for a benchmark for fairness graph learning.

### Strengths
●	The authors address an interesting and timely topic that is absolutely relevant to ICLR.

●	The authors tested these methods on seven real-world datasets, including datasets from different domains such as social networks and finance.

### Weaknesses
●	The novelty of this paper is limited, as the systematic evaluation approach proposed does not significantly improve upon existing methods. The authors primarily use visual comparisons, i.e., plotting accuracy and fairness or presenting them separately in tables or bar charts. This approach is still unable to effectively illustrate the trade-off between performance and fairness for fair GNN.
●	The comparison of fair graph methods are some of the early works. The authors omitting newer approaches such as Graphair [1] and FairSAD [2], which should be included for a more comprehensive comparison.
[1] Ling, Hongyi, et al. "Learning fair graph representations via automated data augmentations." International Conference on Learning Representations (ICLR). 2023.
[2] Zhu, Yuchang, et al. "Fair Graph Representation Learning via Sensitive Attribute Disentanglement." Proceedings of the ACM on Web Conference 2024. 2024.
●	The discussion of experimental results lacks depth and context. The authors mostly describe the numerical scores shown in the result table without interpreting their significance. For example, in RO2, three individual fairness metrics are used to assess model fairness, yet the authors do not discuss the rationale for choosing multiple metrics, the potential conflicts among them, or how to interpret whether the metric values indicate good or poor performance.

### Questions
please refer the weakness.

### Soundness
2

### Presentation
2

### Contribution
1

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The authors compare equity approaches up to 2022 through four dimensions: group fairness, individual fairness, fairness-performance trade-offs, and performance-efficiency trade-offs. They provide a more comprehensive comparison of the methods and an extensive overview of the approaches available prior to 2022.

### Strengths
The authors successfully reproduced the pre-2022 methods and conducted experiments using the corresponding performance indicators.

### Weaknesses
Defining the Balance Between Fairness Guidelines: The paper should clarify how the balance between different fairness guidelines is defined. If the balance is understood as a trade-off between fairness and performance, it is important to explain why existing related works are not utilized as baselines in the experiments [1], [2].

Unique Evaluation Metrics: The paper needs to specify whether it proposes a unique evaluation rubric for assessing fairness. If it relies solely on original metrics, it should highlight how this approach differs from current research that employs multiple baseline comparisons.

Comprehensiveness and Novelty of Fairness Perception Methods: The proposed fairness perception graph learning methods must be evaluated for their comprehensiveness and novelty to determine their potential contributions to the field. Notably, the article only includes methods up to 2022 and lacks discussion of methods from 2023 and 2024 [3], [4], [5].

Significance of Comparing Fairness Types: The significance of comparing individual and group fairness across different approaches should be addressed, especially in light of the established trade-off between these two types of fairness.

Interpretation of Figure 4: The paper should provide guidance on how to interpret the blurred trade-off represented in Figure 4. It should also discuss the insights this figure provides regarding the balance between different fairness metrics.

Interpretation of Figure 5: As fairness-aware graph learning methods, the metrics used for the baselines in Figure 5 should include fairness metrics. The absence of these metrics needs to be justified.

Avoidance of Baseline Comparisons: The authors fail to adequately address concerns about the lack of meaningful and relevant baseline comparisons. Instead of providing sufficient evidence to support their claims, they avoid comparing their method to state-of-the-art approaches, leaving the evaluation incomplete and unconvincing.

Undefined "the most widely used and impactful works": The claim of broader applicability is neither defined nor substantiated. Other fairness methods can also operate across multiple datasets, yet the authors neglect to clarify why their approach is more widely applicable or to conduct direct comparisons with closely related fairness techniques.

Performance Deficiency: The proposed method demonstrates significant gaps in both utility and fairness metrics compared to stronger existing methods. This discrepancy undermines the claim of improved performance and calls into question the practical advantages of the proposed framework.

### Questions
How do the methods developed after 2023 perform on these benchmarks?

There has been substantial research on the trade-off between fairness and performance; why has this not been considered in the current study?

What is the contribution of comparing efficiency? When evaluating efficiency, why is performance the only metric taken into account?

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 5

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
This paper presents benchmarking results for fairness corrections to graph learning algorithms. They investigate multiple aspects of 10 baseline methods on node classification tasks.

### Strengths
The paper is very well-written and well-organized. The paper tackles a useful problem, benchmarking fairness approaches for graph learning algorithms, which to my knowledge has not been done.

### Weaknesses
There are some key weaknesses:

1. The paper only covers node classification, limiting its impact and informativeness.

2. The paper claims to "design a systematic evaluation protocol", but this amounts only to running 10 baselines on standard fairness datasets for graph algorithms. As best I can tell, there is not a novel architecture/system design that the benchmarking experiments depend on.

3. There are some confusions about the results that I point out in my questions.

### Questions
Small typo in RQ1: $\Delta_{\text{Utility}}$ should not be called a fairness metric.

RQ3 is written somewhat confusingly -- its not clear what this RQ is investigating. I also don't know what "Utility" is in Figure 4. Can this be elaborated?

Finding 1 (the answer to RQ1) reads "This verifies the natural advantage of GNNs in achieving both accurate and fair predictions owing to their superior fitting ability", suggesting that GNNs best balance group fairness and accuracy. But Finding 3 (the answer to RQ3) suggests DeepWalk-based methods balance all three metrics the best. Combined with the fact that "Utility" from Finding 3 does not seem to be AUC-ROC, this makes these two findings hard to reconcile and compare. How can a practitioner make decisions based on these findings?

L482: This part should be specific that GNNs only exceed at balancing utility & *group* fairness, not overall fairness.

L483: Where do you show that "FairGNN maintains better trade-off between all three fairness metrics"?

S5 should have a disclaimer that these recommendations only hold for node classification.

### Soundness
3

### Presentation
4

### Contribution
3
