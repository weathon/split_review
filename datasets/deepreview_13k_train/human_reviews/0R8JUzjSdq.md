# LEMMA-RCA: A Large Multi-modal Multi-domain Dataset for Root Cause Analysis

- Decision: Reject
- Scores: 5, 6, 5, 5

## Abstract
Root cause analysis (RCA) is crucial for enhancing the reliability and performance of complex systems. However, progress in this field has been hindered by the lack of large-scale, open-source datasets tailored for RCA. To bridge this gap, we introduce LEMMA-RCA, a large dataset designed for diverse RCA tasks across multiple domains and modalities. LEMMA-RCA features various real-world fault scenarios from IT and OT operation systems, encompassing microservices, water distribution, and water treatment systems, with hundreds of system entities involved. We evaluate the quality of LEMMA-RCA by testing the performance of eight baseline methods on this dataset under various settings, including offline and online modes as well as single and multiple modalities. Our experimental results demonstrate the high quality of LEMMA-RCA. The dataset is publicly available at \url{https://lemma-rca.io/}.
\nop{Dataset and Benchmark accepted papers of previous years: \href{https://datasets-benchmarks-proceedings.neurips.cc/paper/2021}{2021}, \href{https://nips.cc/virtual/2022/events/datasets-benchmarks-2022}{2022}, \href{https://neurips.cc/virtual/2023/events/datasets-benchmarks-2023}{2023}.

I do not see papers in the previous three years with keywords: AIOps, Root Cause Analysis, Microservice. However the following papers/resources may be relevant.

\begin{itemize}
    \item \href{https://arxiv.org/pdf/2208.03938.pdf}{Constructing Large-Scale Real-World Benchmark Datasets for AIOps}
    \item \href{https://arxiv.org/pdf/2310.07637v3.
}

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper introduces Lemma-RCA, a dataset designed for root cause analysis. Lemma-RCA has distinctive and appreciable characteristics like large-scale, multi-modal nature and spans two domains: IT and OT. It includes test logs and time-series data, capturing KPI metrics across several interconnected pods over more than 100,000 timestamps. Notably, the dataset provides ground-truth annotations for both the exact fault occurrence times and the root cause components. This level of detail makes Lemma-RCA a valuable resource for advancing research in RCA.

### Strengths
- Lemma-RCA is a large, multi-model and multi-domain dataset that includes data from both IT and OT domains. It has over 100,000 timestamps across several connected pods, with a rich mix of test logs and time-series data. This dataset will be valuable for testing and improving future RCA methods.

- Unlike most other datasets, Lemma-RCA provides exact ground-truth labels, showing both when faults happened and the specific components responsible. 

- The paper builds on past studies that highlight using causal structure-based methods for RCA. The authors compare Lemma-RCA with causal discovery methods and other recent RCA models.

- **Clarity and Presentation**: The paper is well-organized, with clear visuals and a smooth flow that makes it easy to understand in a single read.

### Weaknesses
 **Missing Dependency Graph**: A key limitation of Lemma-RCA is the absence of a dependency graph, which prior datasets like PetShop provided as a causal graph. This dependency graph is critical for RCA, as it allows more direct evaluations of causal discovery methods. The paper seems to already hint the partial dependency graph in Figure 1(a). I wonder if the authors could add the full dependency graph along with the datasets.

**Insufficient Explanation of Baseline Approaches:** The paper does not include explanations of the baseline approaches used, even in the appendix. Although prior work is cited, providing brief descriptions of each benchmarked approach, particularly the high-performing REASON method, would enhance the reader’s understanding of the comparative results.


**Limited Explanation of Experimental Results**: The experimental results focus primarily on causal discovery approaches, but they lack in-depth analysis of why these methods failed. The authors' insights and intuition about why each method achieved the numbers reported in the table could significantly enhance the understanding of the experiment section. For instance, suppose we assume that the dependency graph is the true causal graph as in PetShop. Then can the authors establish how far the PC's predicted causal graph is from the true dependency graph. This would at least give us a sense of the causal discovery performance and put the RCA results in context. For instance, if the causal discovery performance is very poor, there is no meaning in expecting the methds like PC, GOLEM, etc. to perform better in predicting root causes. Additionally, one interesting experiment to run would be evaluating the causal graph based baselines on the true dependency graph, instead of the one inferred from observational data by PC.

**Choice of Baseline Algorithms:** Given that the dataset is timestamped, it cannot be assumed that each record is i.i.d. Some causal discovery methods, like those in the Tigramite package (https://jakobrunge.github.io/tigramite/), are tailored for time-series data. It is unclear why the authors chose standard PC over these alternatives, which may be more suitable for time-dependent causal discovery.


Finally, some important prior RCA works appear to be missing among the benchmarked methods. For example, the paper by Pham et al. (2024) on BARO highlights that inaccurate RCA predictions can result when a method fails to learn the correct causal graph. Including such approaches would provide a more thorough baseline comparison and strengthen the evaluation.

### Questions
1. Could the authors consider including the dependency graph? Having this graph like in petshop seems like a deal breaker to me.

2. Could the authors benchmark the baselines using the dependency graph instead of the causal graph inferred by the PC?

3. For the CIRCA method as well, could the authors provide results based on the dependency graph?

4. The experiments section needs more and a systematic explanation on why each method performed better or worse.

### Soundness
2

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
In this paper, the authors proposed a new dataset with both metrics and log collected for the root cause analysis task. In addition, 8 existing RCA methods are evaluated on this dataset. The proposed datasets could be a good addition for evaluation of RCA methods for later research. However, it is not very clear what the benefit of including log modal data is. Existing methods work quite well on these datasets with only metrics modal.

### Strengths
1. New multi-modal datasets are collected for RCA problem.
2. Eight existing RCA methods are evaluated on the proposed datasets.

### Weaknesses
1. The description of the data collection is insufficient. See Q1.
2. Some subsets of the datasets are from existing work and have been evaluated before. They should not be seen as the contribution of this work. See Q2.
3. The proposed IT ops datasets seems to be less challenging for existing works. See Q3.

### Questions
1. The authors claimed that the proposed datasets contain real system faults. If I understand correctly, the authors developed two microservice platforms and deployed them in production and collected the real system faults for 8 days when users are using these platforms. It is a bit surprising that so many faults happened in 8 days. Moreover, in the faults description section, it seems that these faults are simulated (e.g., External Storage Failure) to mimic the real world scenario. Could the authors clarify this?
2. It seems that SWaT and WADI are from existing work. The authors applied some anomaly detection algorithms on them to transform discrete labels into continuous ones. It is not clear why this is necessary. Moreover, SWat and WADI are already evaluated for RCA in the REASON (Wang et al. KDD2023) paper.  Since this is a dataset paper, including existing datasets into the proposed one should not be seen as the contribution. 
3. From experiments on existing methods, it seems that two IT ops datasets are not very challenging. For instance, REASON performs quite well in terms of PR@k, MRR and MAP@k on both of them with only the metrics data. What is the difference between the proposed datasets compared with existing ones, e.g., AIOps data in REASON and the popular train ticket datasets? When new datasets are proposed, they are expected to be more challenging, where current methods are failed on them. If current method can handle the proposed well with only metric modal, what is the meaning of including log modal?
4. The authors conducted some preprocessing to convert logs to time series for evaluation. But the open-sourced datasets do contain all the original logs, right?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper presents LEMMA-RCA, a large-scale, multi-modal, and multi-domain dataset specifically designed for Root Cause Analysis (RCA) in complex systems. The dataset includes real-world fault cases from IT and OT operational systems, covering microservices, water treatment, and distribution systems to support a wide range of RCA tasks. To validate the effectiveness of LEMMA-RCA, the authors evaluated various RCA methods on this dataset, demonstrating its diversity and utility across offline and online settings as well as single and multi-modal data scenarios.

### Strengths
(1)	LEMMA-RCA is the first public dataset specifically designed for root cause analysis, covering two domains—IT and OT. 
(2)	The paper thoroughly tests multiple existing RCA methods on LEMMA-RCA, demonstrating the dataset’s quality and multi-modal value.
(3)	By making LEMMA-RCA freely accessible, the paper lowers research barriers, encouraging collaboration between academia and industry and enhancing the generalizability and practical impact of RCA methodologies.

### Weaknesses
(1)	One contribution of this study is the introduction of LEMMA-RCA, the first multi-domain dataset for RCA. However, the dataset includes only IT and OT domains, which appear to be a simple combination of two unrelated domains, thus raising questions about the solidity of this contribution. Additionally, the limited data collection period, such as the 11 days for the OT system, may not capture long-term trends, potentially limiting its applicability to broader fault analysis scenarios.
(2)	The figures in this study are unclear, heavily relying on screenshots. 
(3)	The experimental analysis tables lack consistency in reporting, with varying decimal places and an absence of standard deviation reporting.
(4) The experimental results presented are not standardized. For example, in Table 3, row 452 uses percentages, while other rows presented as three decimal place; results in part of row 423 are still not standardized.
(5) The lack of reported standard deviations undermines the credibility of the experimental results, which are unreliable.
(6) The analysis indicates that the task data is time-series data; however, algorithms such as PC, Notears, and CORAL are not designed for time-series data. Therefore, comparing them on this dataset is not meaningful.

### Questions
(1)	The author should provide more valuable data rather than simply assembling data. Additionally, it is not clarified whether these platforms the data come from are sufficiently representative to ensure the quality of the data and the data collection period appears to be rather short, making it difficult to establish whether the dataset adequately captures a wide range of fault patterns and system behaviors.
(2)	The experiments designed by the authors do not seem sufficient to demonstrate the value of the dataset. I suggest that the authors select several widely recognized RCA methods with known performance differences and analyze whether these methods exhibit similar performance distinctions on this dataset.
(3)	The author can pay more attention to the readability of the figures in the paper and the normalization of the experimental results.

### Soundness
2

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
3

### Summary
The paper presents Lemma-RCA, a novel dataset and benchmark designed for root cause analysis (RCA). This dataset includes four sub-datasets: two from IT environments and two from OT environments, offering a large-scale, multi-modality dataset (with both KPI and log data) that captures real-world system faults. The authors validate the dataset’s quality by testing it with eight baseline models across offline single-/multi-modality and online single-modality settings.

### Strengths
- The dataset is open-source, multi-modal, and well-suited to RCA, making it both timely and relevant.
- The authors have provided a thorough review of existing baseline approaches.

### Weaknesses
 - The dataset description could be more accessible to a broader audience, as suggested in the questions below.
- Reproducibility is limited due to insufficient implementation details for the baseline models.
- The statement “We evaluate the quality of LEMMA-RCA by testing the performance of eight baselines” seems to overstate the implications of the baseline tests. While I acknowledge the dataset’s quality through expert inspection and validation, I don’t think the baseline comparisons alone can determine the relative quality of datasets. I recommend revising similar statements.

### Questions
1. **Clarification:**
- The current data collection section seems tailored for domain experts and could benefit from clarification for a general audience. For instance, what do "IT" and "OT" refer to? Are "Prometheus" and "ElasticSearch" tools or companies? Clarifying the meanings of such terms would improve the accessibility. 
- Figure 2(a) would benefit from a more detailed explanation in its caption.
- In Figure 3, what is the KPI being referenced? Should it be assumed that all KPIs in this figure relate to system latency? Please specify the y-axis further.
- How were the root causes $V_a$  for each system fault $a$ labeled? The authors  may include a section in the paper detailing their labeling methodology.
2. **Evaluation Metrics:** The evaluation metrics appear to be sample-independent. Why did the authors not consider sample-dependent metrics? For example, over a 10-day system run yielding 1000 faults, the accuracy of the prediction algorithm could be tested against the actual root cause labels.

3. **Data Quality Claims:** The authors suggest high data quality based on baseline comparisons. This conclusion seems somewhat overstated, as the main insight from these experiments appears to be that "MRR performance improves when considering two modalities jointly."

**Comment on Missing Data:** While the authors view missing data as a limitation, I consider it a realistic aspect of real-world data, which poses a meaningful challenge rather than a flaw.

### Soundness
2

### Presentation
2

### Contribution
3
