# A Comprehensive Graph Pooling Benchmark: Effectiveness, Robustness and Generalizability

- Decision: Reject
- Scores: 3, 8, 5, 3

## Abstract
Graph pooling has gained attention for its ability to obtain effective node and graph representations for various downstream tasks. Despite the recent surge in graph pooling approaches, there is a lack of standardized experimental settings and fair benchmarks to evaluate their performance. To address this issue, we have constructed a comprehensive benchmark that includes 17 graph pooling methods and 28 different graph datasets. This benchmark systematically assesses the performance of graph pooling methods in three dimensions, i.e., effectiveness, robustness, and generalizability. We first evaluate the performance of these graph pooling approaches across different tasks including graph classification, graph regression and node classification. Then, we investigate their performance under potential noise attacks and out-of-distribution shifts in real-world scenarios. We also involve detailed efficiency analysis, backbone analysis, parameter analysis and visualization to provide more evidence. Extensive experiments validate the strong capability and applicability of graph pooling approaches in various scenarios, which can provide valuable insights and guidance for deep geometric learning research.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
This paper presents a comprehensive benchmark for evaluating graph pooling methods. It covers 17 pooling techniques and tests their performance across 28 graph datasets in three tasks, including graph classification, graph regression, and node classification. The study focuses on three key areas: effectiveness, robustness under edge and feature noises, and generalizability under out-of-distribution shifts. Additionally, the paper provides analyses of computational efficiency, backbone variations, parameter sensitivity, and visualization of different baselines. The authors emphasize that their open-source benchmark is intended to standardize the evaluation of graph pooling techniques, facilitate reproducibility, and guide future research in deep geometric learning.

### Strengths
1.	Comprehensive benchmark. The paper provides a novel and publicly available benchmark, which comprehensively includes 17 state-of-the-art graph pooling methods, 28 diverse datasets, and 3 graph learning tasks on both graph and node levels. The comprehensiveness helps set a new standard for evaluating graph pooling methods.

2.	Diverse evaluation criteria. The authors evaluate different graph pooling methods from three diverse dimensions: effectiveness, robustness, and generalizability, which provide a comprehensive view of the strengths and weaknesses of different methods.

### Weaknesses
1.	Lack of novelty. The findings, especially those presented in the introduction section, are straightforward and naïve, lacking novel insights into graph pooling methods that can guide future research. (1) The author lists six observations in the introduction part, some of which are too specific (e.g. the third point) and should only be mentioned in the corresponding experiment sections. (2) The findings in this paper are simple empirical observations of the experiment results but fail to provide valuable insights that can guide future research. For example, the authors simply observe that node clustering pooling methods outperform node dropping pooling methods in terms of robustness and generalizability, but no underlying explanations are given. (3) Some of the findings are also well-known, such as the high computational cost of node clustering pooling methods [1].

2.	Questionable or inconsistent claims. (1) The authors claim that node clustering pooling methods outperform node dropping pooling methods in terms of robustness, whereas Table 5 shows that node dropping pooling methods achieve the best results in 8 different settings, compared to node clustering methods that only achieve the best results in 5 settings. (2) The authors claim that node clustering pooling methods outperform node dropping pooling methods in terms of generalizability, but Table 5 (node classification under distribution shifts) only includes node dropping pooling methods. (3) The 4th finding in the introduction is not mentioned or verified in the corresponding experiment section. (4) The 1st finding in the introduction partially overlaps with the 6th finding.

### Questions
1.	What does Rank in Tables 2, 3, and 4 mean? Please explain it in the paper.
2.	What does feature masking mean? Please explain it in the paper.
3.	KMISPool and ParsPool do not demonstrate the best overall performance on Cornell, please double-check the first claim made in section 4.2 Performance on Node Classification.
4.	For the visualization, would it be possible to add more numeric metrics to support the claim? E.g., the overlap ratio.
5.	Would it be possible to include experiments of node pooling methods on node classification tasks under distribution shifts to validate the findings of the paper?
6.	Would it be possible to address the concerns mentioned above? Please at least consider rewriting the findings in the introduction to make them consistent with the claims in the experiment sections and the conclusion.

### Soundness
2

### Presentation
3

### Contribution
1

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
The paper benchmarks 17 state-of-the-art approaches and 28 different graph datasets used in graph pooling for graph-level and node-level tasks. The existing methods are evaluated based on their effectiveness, robustness, and generalizability, where valuable discussions/observations are provided for their performance.

### Strengths
- The paper provides a comprehensive literature overview for graph pooling.

- Open source codes reimplementing the existing methods with commonly used datasets are valuable assets, which might allow fairer performance comparisons in future works.

- The work provides remarkable observations for the performances of existing works with respect to their effectiveness, robustness, and generalizability.

- The paper is written well and easy to follow.

### Weaknesses
- For graph-level tasks, the Authors seem to only use GCN as the GNN backbone. More advanced GNN designs, like GIN, can also be incorporated here.

- Additional analyses for the effect of graph structure (homophilic vs. heterophilic) on existing works' performance can provide further insights. For such an analysis, synthetic graphs may be generated with different structural properties.

### Questions
Please see weaknesses.

### Soundness
3

### Presentation
3

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
In summary, this paper provides a comprehensive evaluation of 17 graph pooling methods using 28 different datasets across three tasks. This paper evaluates these methods from the perspectives of performance, robustness, and generalizability.

### Strengths
- The paper makes a significant effort to evaluate these methods, offering a fair comparison for future studies.

- It includes the generalization and robustness aspects that have been overlooked in previous evaluations.

### Weaknesses
- This paper still lacks the additional suggestions and directions for the future development of graph learning methods. Which directions and challenges should be considered when designing new methods?

- Besides, it does not sufficiently explore the relationship between graph characteristics and the selection of graph learning methods, which is crucial for a comprehensive evaluation benchmark.

### Questions
Please check the weaknesses.

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
4

### Summary
This paper presents a comprehensive graph pooling benchmark, which incorporates 17 state-of-the-art graph pooling approaches and 28 diverse datasets across graph classification, graph regression, and node classification. Experiments from three perspectives, i.e., effectiveness, robustness, and generalizability were conducted to compare collected methods with each other.

### Strengths
1.	This paper presents a collection of 17 graph pooling methods over 28 different graph datasets, and the authors claim to be the first work of benchmarking.

### Weaknesses
1.	Further experiments should be conducted for hyperparameter sensitivity to enable fair comparison.
2.	Experiments on robustness against noise, specifically Tabel 5 and 6, were not conducted on all datasets. The same problem exists in experiments on generalization ability.
3.	The biggest weakness of this paper is that it only presents baseline results of existing methods, lacking new insights for researchers who are already familiar with this field, or a code framework that newcomers can use to quickly develop their own insights.

### Questions
4.	The taxonomy of graph pooling methods in lines 46-47, is it originally proposed in this paper?
5.	What is the ‘Feature map’ in line 106?
6.	Line 107 ‘In this work, we focus on hierarchical pooling approaches’. Does it mean this benchmark only contains hierarchical pooling approaches? According to a recent survey, the graph pooling community is obviously more than hierarchical pooling approaches.
7.	Lines 125-126 ‘during the connection’ should be ‘during the pooling process’ ?
8.	Lines 125-126 Why is the ‘connection component’ necessary? Dropping and clustering nodes, according to your taxonomy, can affect the topology too.
9.	Lines 209-210 ‘We perform a hyperparameter search for all pooling methods; detailed information can be found in Appendix E’. However, Appendix E does not provide any details on how the hyperparameter search was conducted. Further experiments should be conducted for hyperparameter sensitivity to enable fair comparison, or at least performance reported in the original paper VS in your paper.
10.	Experiments on robustness against noise, specifically Tabel 5 and 6, were not conducted on all datasets. Why are these datasets selected while the others are not?
11.	The analysis of why method A performs well while method B does not on certain tasks and scenarios is quite disorganized. I suggest organizing it into a table like a survey paper and presenting each method’s design, along with an analysis of its strengths and weaknesses, in a separate section.
12.	See weakness 3. I suggest synthesizing the code you’ve collected and standardizing the input, output, and evaluation protocols.

[1] Liu C, Zhan Y, Wu J, et al. Graph Pooling for Graph Neural Networks: Progress, Challenges, and Opportunities. IJCAI 23

### Soundness
3

### Presentation
2

### Contribution
1
