# Unifying Unsupervised Graph-Level Anomaly Detection and Out-of-Distribution Detection: A Benchmark

- Decision: Accept
- Scores: 6, 6, 6, 8

## Abstract
To build safe and reliable graph machine learning systems, unsupervised graph-level anomaly detection (GLAD) and unsupervised graph-level out-of-distribution (OOD) detection (GLOD) have received significant attention in recent years. Though those two lines of research indeed share the same objective, they have been studied independently in the community due to distinct evaluation setups, creating a gap that hinders the application and evaluation of methods from one to the other. To bridge the gap, in this work, we present a \underline{\textbf{U}}nified \underline{\textbf{B}}enchmark for unsupervised \underline{\textbf{G}}raph-level \underline{\textbf{O}}OD and anoma\underline{\textbf{L}}y \underline{\textbf{D}}etection (\ourmethod), a comprehensive evaluation framework that unifies GLAD and GLOD under the concept of generalized graph-level OOD detection. Our benchmark encompasses 35 datasets spanning four practical anomaly and OOD detection scenarios, facilitating the comparison of 16 representative GLAD/GLOD methods. We conduct multi-dimensional analyses to explore the effectiveness, generalizability, robustness, and efficiency of existing methods, shedding light on their strengths and limitations.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This experimental paper proposes unifying two graph machine learning tasks, graph anomaly detection (GLAD) and graph out-of-distribution detection (GLOD) in the unsupervised setting. The paper applies 35 datasets with different properties (anomaly/out-of-distribution scenarios) and applications. Moreover, the evaluation considered 18 methods proposed for anomaly detection and OOD detection that are evaluated in terms of accuracy, generalization, and efficiency. Some of the major findings in the paper are: (1) GNN-based methods achieve the best results on average even though there is no single best method, (2) the methods often struggle with near-OOD scenarios compared with far-OOD ones. and (3) some of end-to-end (GNN-based) methods are more efficient and accurate than the alternatives.

### Strengths
- The paper is well-written and easy to follow
- The benchmark proposed in the paper contains 35 datasets
- The datasets and implementations are shared as open-source

### Weaknesses
 - The main findings of the paper are mostly expected
- It is not clear why the same methods should solve anomaly detection and out-of-distribution detection
- Most of the datasets are from the same domain

Detailed comments:

These are the main findings quoted from the paper:

1) "The SOTA GLAD/GLOD methods show excellent performance on both tasks"
2) "No universally superior method"
3) "Inconsistent performance in terms of different metrics"
4) "End-to-end methods show consistent superiority over two-step methods"
5) "Near-OOD samples are harder to detect compared to far-OOD samples"
6) "Poor generalizability of several GLAD/GLOD methods in specialized scenarios"
7) "Performance degradation with increasing contamination ratio"
8) "The sensitivity of different methods/datasets can be diverse"
9) "Certain end-to-end methods outperform two-step methods in terms of both performance and computational costs"

The only findings that one could find unexpected are 1 and maybe 9. Finding 3 is expected because of class imbalance. I am not diminishing the effort that the authors have put into running these experiments but the value of an experimental paper is what can be learned from the results. It is unclear how much can be learned from these results.

Regarding the unification of the tasks, I would like to see a more clear formalization than definition 1. One could argue that an anomaly can still be in-distribution (as points can be simply ranked in terms of anomaly scores). On the other hand, an OOD point might not be an anomaly (as there might be many similar points in the test dataset). The setting considered in the experiments seems to assume that the test data points are unseen (besides being unlabelled) but if every point can be observed, the difference between an anomaly and an OOD point should be clear. This setting needs better motivation.

From Table 1, only 8/35 datasets are not molecules. This can bias the findings towards methods that perform well on molecules, which is something not discussed in the paper. 

Minor comments:
- How are the hyperparameters of the methods set without a validation set? I was not able to understand this from Appendix D.

### Questions
1) How do the main findings of the paper contribute to future research on GLAD and/or GLOD?

2) What is the motivation for unifying GLAD and GLOD?

3) How can the findings in the paper be impacted by the dominance of molecular graphs in the benchmark?

4) How are hyperparameters set in the experiments?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This manuscript presents a unified benchmark called UB-GOLD, which aims to unify and benchmark Graph Level Anomaly Detection (GLAD) and Graph lavel OOD detection (GLOD). Specifically, the authors compare the performance of 18 GLAD/GLOD methods on 35 datasets. The performance is investigated in four different dimensions: effectiveness (using three common accuracy metrics), generalisability, robustness, and efficiency (time and memory usage). Based on extensive experiments, the authors provide insightful observations and discuss possible future directions.

### Strengths
1. this manuscript is well written and easy to follow;
2. I believe this is the first work that attempts to unify and benchmark GLAD and GLOD tasks, the findings could be broadly interesting to the graph data mining community;
3. the authors conducted extensive experiments and open-sourced their code base (which I believe is easy to extend), making contributions to future research;

### Weaknesses
## Major Comments

### 1. Unification and Benchmarking of GLAD and GLOD Tasks
As the first work attempting to unify (please indicate the related work if this is not true) and benchmark GLAD (Graph-Level Anomaly Detection) and GLOD (Graph-Level Out-of-Distribution) detection tasks, I believe the authors should dedicate more space and effort to this unification process. Specifically:

- **1.1) Formal Definitions**: It would be beneficial for the authors to formally (with math symbols) define GLAD and GLOD before introducing the concept of "Unsupervised generalized graph-level OOD detection." Providing these definitions upfront would establish clarity and context for readers unfamiliar with these tasks. It is crucial to define the input space, the output space, and the objective function for each task. For example, what constitutes a graph in this context (attributed, un-attributed, directed, etc.)? What is the nature of the anomaly or OOD, and how is it represented in the graph structure or node/edge attributes? A formal definition should also clarify whether the tasks are transductive or inductive.

- **1.2) Relationship Between GLAD and GLOD**: The authors should discuss the relationship between GLAD and GLOD in more depth, as there seems to be room for clarification on whether they perceive OOD detection as a broader concept than anomaly detection. In my view, anomaly detection is a broader concept, as abnormal instances may either (1) exist within the distribution but in low-density regions or (2) represent out-of-distribution instances. Including a specific section comparing and contrasting GLAD and GLOD, with formal definitions and discussions of their conceptual overlap and distinctions, would enhance the unification effort and clarify this relationship. The discussion should also consider the practical implications of treating both tasks under a single umbrella, including potential limitations.

---

### 2. Experimental Details and Completeness
There are some missing details regarding the experiments and results. Adding these would make the manuscript more self-contained, especially as it aims to serve as a benchmark paper.

- **2.1) Definition and Generation of Anomalies/OOD Samples**: To make the manuscript self-contained, please provide details in the appendix on how the anomalies or OOD samples are defined or generated in each dataset. Clear explanations will help readers replicate and understand your experiments.  For example, if anomalies are generated by adding random edges, what is the distribution and density of these added edges? If OOD samples are generated by changing node attributes, what is the nature and magnitude of these changes? The explanation should also include the rationale behind the specific anomaly/OOD generation method.

- **2.2) Completeness of Results in Figures**: In Figure 4, results are only provided for 15 out of 19 methods, with similar omissions in Figures 5 and 6. If these omissions are due to space limitations, including the full results in the appendix would help ensure completeness. Please also add a brief discussion explaining why certain methods were omitted from the main figures, if applicable. The discussion should include a justification for the selection of the 15 methods and why the omitted methods are not as relevant or informative.

- **2.3) Metrics and Additional Results**: In Figures 4 and 5, please specify which metrics are being used. Additionally, including complete results for all metrics in the appendix, along with brief analyses, would make the benchmark more comprehensive and allow for a better understanding of the methods' performances. It is important to include a discussion of why certain metrics are more or less suitable for different scenarios. For example, AUROC might be more suitable when the classes are balanced, while AUPRC might be more appropriate for imbalanced datasets.

---

### 3. Clarification of Experimental Settings and Terminology

- **3.1) Hyperparameter Search**: In the hyperparameter search section, the authors conduct a random search to optimize hyperparameters based on **test set performance**. This approach raises questions regarding practical applicability. Could you clarify if a validation set was used instead of the test set for hyperparameter tuning, or if there was a specific reason for using the test set? Also, discussing the implications of this choice on the generalizability of your results would provide valuable context. This is a critical point, as using test data for hyperparameter tuning can lead to overly optimistic results that do not generalize well to unseen data. The authors should also discuss the potential for overfitting to the specific test set.

- **3.2) Use of the Term "Generalisability"**: The term "generalisability" is typically associated with a model’s performance on unseen data, while the manuscript uses it to describe differences in OOD detection for near- and far-OOD samples. Alternative terms, such as "OOD detection range" or "OOD sensitivity spectrum," may better capture the intended meaning. Clarifying or refining this terminology would enhance reader understanding. The authors should also consider the practical implications of using near- and far-OOD samples, including how these samples are defined and generated, and whether they are representative of real-world scenarios.

---

## Minor Comments and Suggestions

- **4.1) Page 4, Line 084: Typo**: Please correct "28 GLAD and GLOD methods" to "18 GLAD and GLOD methods."

- **4.2) Anomaly Ratio in Table 1**: In Table 1, adding the anomaly ratio for each dataset would make the data overview more informative.

- **4.3) Visualization of CPU and GPU Results in Figure 6**: In Figure 6, consider superimposing the CPU and GPU bars (distinguished by color) to make the visual comparison clearer.

- **4.4) OOD Judge Score Distribution Analysis**: On Page 5, you mention an "OOD Judge Score Distribution Analysis," but this concept was not referenced later in the main text, though it appears in the appendix. Including a reference in the main text would clarify its relevance.

- **4.5) "Well-trained GNNs" on Page 5**: On Page 5, the term "well-trained GNNs" is used. If this refers to pre-trained GNNs, please provide a brief explanation for clarity.

### Questions
Please check the weak points.

### Soundness
4

### Presentation
4

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper unifies the unsupervised  graph level ood and anomaly detection as generalized graph level ood detection problem and conduct a comprehensive and unified benchmark. This paper provide some remarkable observation through the comprehensive comparison and analyses.

### Strengths
1. A large amount of datasets are employed to establish the benchmark to fairly compare the mutiple GLAD and GLOD emthods under a unified experimental setting.
2. In addition to the performance, the paper also investigates more characteristics of methods including generalizability, robustness, and efficiency.
3. The comprehensive benchmark and the multiple observations are provided in the experimental analysis to inspire future work.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            
4. There is no clear distinction between the training set and test set in unsupervised GLAD. Leveraging unsupervised graph-level anomaly detection methods for OOD detection is a good point.

### Weaknesses
1. In GLAD, anomalies can be considered as out-of-distribution (OOD) test samples for type 1 and type 2, but further clarification is needed in the paper on how the in-distribution (ID) test samples are constructed. Specifically, the paper should detail the selection criteria for ID samples within each dataset type, including the proportions of different labels and the rationale behind these choices. For instance, in Type I datasets, how are the ID samples selected to ensure they represent the true in-distribution data, and what are the implications of varying test_{ID} to train_{ID} ratios on model evaluation?
2. In an unsupervised setting, does this mean the test set can also be used as the training set? The in-distribution samples in the test set could potentially help improve performance. The paper needs to explicitly clarify whether any data leakage occurs between the training and test sets, especially given the unsupervised nature of the problem. It should also discuss the potential impact of using test set information during training, even unintentionally, and how this could bias the results.
3. From the several observations, we found there are large overlaps between OOD samples,  in addition to the experimental explanation, more specific analysis is needed on this point for particular datasets. The paper needs to provide a more detailed analysis of the overlap, including specific examples of datasets where this overlap is most pronounced and the potential reasons for it. This analysis should go beyond general explanations and delve into the characteristics of the data that might lead to such overlaps.

### Questions
1. What is the difference between near-OOD samples and anomalies if both come from the same dataset?
2. If some OOD samples or anomalies are integrated into the training set as contamination, are they still retained in the test set during inference?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The paper introduces UB-GOLD (Unified Benchmark for unsupervised Graph-level OOD and anomaly Detection), a comprehensive benchmark that unifies two related tasks in graph machine learning: graph-level anomaly detection (GLAD) and graph-level out-of-distribution detection (GLOD). UB-GOLD bridges this gap by providing a unified evaluation across 18 representative methods and 35 datasets, covering various scenarios in anomaly and OOD detection. The benchmark offers a multi-dimensional analysis of methods, assessing their effectiveness, generalizability, robustness, and efficiency, while also providing an open-source codebase to facilitate reproducible research and encourage further exploration.

### Strengths
①The paper makes an original contribution by unifying GLAD and GLOD into a single benchmark, UB-GOLD. This creative combination highlights the conceptual overlap between the two tasks, simplifying evaluation in both areas.

②The paper's experiments evaluate 18 methods on 35 datasets. It offers a multi-dimensional analysis. The breadth of datasets used ensures reliable, real-world applicability, while the open-source codebase.

③UB-GOLD offers insights into detecting near-OOD samples and noisy training data. These findings current limitations in existing methods. What's more, this work focus on generalizability, robustness, and efficiency ensures the benchmark’s practical relevance across different application domains, making it a useful resource in the field.

### Weaknesses
①While the paper provides extensive comparisons across methods, it could benefit from a more in-depth discussion of why certain methods fail in specific scenarios. For instance, understanding the root causes of poor performance under noisy training data or near-OOD conditions.

②Consider adding a more concise summary section that highlights the most important findings from your multi-dimensional analyses. This could be in the form of a bulleted list or a short paragraph at the end of each results subsection to help readers quickly digest key insights.

③In datasets like IC50-Size, the out-of-distribution samples differ primarily in graph structure from the in-distribution ones. It’s unexpected that SSL-D and GK-D methods perform poorly on these datasets. Could the authors offer an explanation for these results?

### Questions
①Performance of SSL-D and GK-D on Graph Structure-Based Datasets: In datasets like IC50-Size, where out-of-distribution samples primarily differ from in-distribution ones in graph structure, SSL-D and GK-D methods show poor performance. Could you provide insights into why these methods struggle with such datasets? Is it related to the specific way these methods handle graph structure?

②Handling Near-OOD Samples: You mention that near-OOD samples are more difficult to detect than far-OOD samples. Could you elaborate on what specific characteristics of near-OOD samples make them harder to distinguish? Do you have any thoughts on how future work could address this issue?

### Soundness
4

### Presentation
3

### Contribution
4
