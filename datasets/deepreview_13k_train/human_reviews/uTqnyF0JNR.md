# IGL-Bench: Establishing the Comprehensive Benchmark for Imbalanced Graph Learning

- Decision: Accept
- Scores: 8, 8, 6

## Abstract
Deep graph learning has gained grand popularity over the past years due to its versatility and success in representing graph data across a wide range of domains.
However, the pervasive issue of imbalanced graph data distributions, where certain parts exhibit disproportionally abundant data while others remain sparse, undermines the efficacy of conventional graph learning algorithms, leading to biased outcomes. 
To address this challenge, Imbalanced Graph Learning (IGL) has garnered substantial attention, enabling more balanced data distributions and better task performance.
Despite the proliferation of IGL algorithms, the absence of consistent experimental protocols and fair performance comparisons pose a significant barrier to comprehending advancements in this field.
To bridge this gap, we introduce {\fontfamily{lmtt}\fontseries{b}\selectfont IGL-Bench}, a foundational comprehensive benchmark for imbalanced graph learning, embarking on \textbf{16} diverse graph datasets and \textbf{24} distinct IGL algorithms with uniform data processing and splitting strategies. 
Specifically, \modelname~systematically investigates state-of-the-art IGL algorithms in terms of \textit{effectiveness}, \textit{robustness}, and \textit{efficiency} on node-level and graph-level tasks, with the scope of \textit{class-imbalance} and \textit{topology-imbalance}. 
Extensive experiments demonstrate the potential benefits of IGL algorithms on various imbalanced conditions, offering insights and opportunities in the IGL field.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper addresses the gap in graph learning by introducing a benchmark named IGL-Bench for imbalanced graph learning. The benchmark covers 24 algorithms across 17 datasets, tackling node-level and graph-level tasks that are affected by class and topology imbalances. The benchmark includes standardized data processing, evaluation protocols, and metrics across different datasets. Evaluation on effectiveness, robustness, boundary clarity, and efficiency of IGL methods under imbalanced conditions are further carried out. The benchmark findings reveal key insights into the strengths and limitations of current IGL algorithms, particularly around scalability, robustness, and their dependency on graph topology properties.

### Strengths
- Originality: The paper introduces a comprehensive benchmark for IGL to fill the gap in graph learning.
- Quality: Experiments valiadate the quality of the benchmark.
- Clarity: The paper is well written and organized. Easy for general audience to follow.
- Significance: The benchmark provides an easy platform for developing or comparing IGL methods, especially as graph learning expands into real-world, imbalanced datasets.

### Weaknesses
 - Complex visualizations: Certain visualizations, such as multi-metric plots across multiple imbalance ratios, could benefit from clearer explanations to aid interpretability for readers less familiar with the metrics.
- New dataset: No new dataset is introduced in the paper.

### Questions
- Can the authors elaborate on the specific challenges encountered in standardizing data splits and evaluation protocols across such a diverse set of IGL methods?
- How does IGL-Bench handle algorithm hyperparameter tuning, particularly for methods that might be sensitive to different types of imbalance?
- Are there future plans to study the scalability within IGL-Bench, e.g., for larger, more complex graph datasets?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This work presents a benchmark for imbalanced graph learning, encompassing 17 graph datasets and 24 imbalance-handling algorithms, along with a unified data processing pipeline, splitting strategy, and evaluation protocols. The benchmark addresses questions related to effectiveness in handling imbalance, robustness across different imbalance ratios, and efficiency in terms of time and space for both node-level and graph-level tasks. Additionally, an open-source codebase is provided to facilitate reproducible evaluations.

### Strengths
1. Benchmarking imbalanced graph learning is important to track progress in the research community.
2. The four research questions posed are relevant and of interest to the community.
3. The paper is well-written and easy to follow.
4. The experiments are thorough and well-designed. The availability of open-source code enhances reproducibility and accessibility.

### Weaknesses
1. For node-level class-imbalanced algorithms, it would be beneficial to include traditional methods for addressing class imbalance, such as reweighting or PC Softmax [1], to provide a comprehensive comparison. Additionally, reporting per-class F1 scores could offer more insights into model performance across majority and minority classes, enabling a more detailed analysis of effectiveness.

2. Some findings lack depth and do not offer clear insights. For instance, the observation that most algorithms perform poorly on the large-scale ogbn-arXiv dataset is presented without an explanation. It would be valuable to investigate and discuss the reasons for this poor performance, especially through additional experiments.

3. In Section 4.4, which assesses the efficiency of different models, the experiments are conducted on the Cora dataset, the smallest of the datasets used. This setup makes the time and space usage of the algorithms highly dependent on implementation details rather than their inherent algorithmic complexity. While the Appendix includes results for the ogbn-arXiv dataset, they cover only a subset of models, as other models encountered memory limitations. A theoretical analysis of the algorithms' complexities would provide a more meaningful comparison of their efficiency. Relying solely on runtime measurements can be misleading, as they may be influenced by implementation optimizations and do not necessarily reflect the algorithms' underlying efficiency.

4. On the ogbn-arXiv dataset, certain resampling algorithms, such as GraphENS and GraphSHA, run successfully, whereas others, like GraphSMOTE, encounter memory issues. It is unclear whether this is due to differences in algorithmic complexity or specific implementation choices. Given the similarity of these resampling approaches, clarifying whether the issue arises from inherent algorithm characteristics or particular implementation choices would be helpful.

### Questions
See Weakness.

### Soundness
3

### Presentation
3

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
This paper introduces a benchmark for Imbalanced Graph Learning (IGL). IGL-Bench offers a unified framework for evaluating 24 IGL algorithms across 17 datasets, addressing both class- and topology-imbalance at node and graph levels. The authors conduct a rigorous evaluation on effectiveness, robustness, and efficiency, providing a comparative analysis of existing methods. Additionally, the paper presents an open-source package to facilitate reproducible research and encourage further development in the IGL field.

### Strengths
-	The proposed IGL-Bench is well-constructed, it can provide a standardized testbed for future work, encouraging a more consistent evaluation process for IGL.
-	The paper is well-written and easy to follow. The authors' thorough analysis of the benchmarking results leads to interesting insights.

### Weaknesses
Recently, several more general IGL methods have been proposed, which can be used independently or in combination with the IGL techniques discussed in this paper. For instance, [1] based on topological augmentation and automated loss engineering approach [2], both presented at ICML '24, are notable examples. It would be beneficial if IGL-bench could include these recent booster-type methods and provide related discussion.

### Questions
1.	 How does the benchmark incorporate, or plan to incorporate, recent advances in IGL (see weaknesses), and evaluate whether these general approaches improve performance, robustness, and other metrics?
2.	Are there any plans to provide an API reference for IGL-bench? This would significantly enhance usability.

### Soundness
3

### Presentation
3

### Contribution
3
