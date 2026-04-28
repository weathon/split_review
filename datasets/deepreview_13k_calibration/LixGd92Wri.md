# GDL-DS: A Benchmark for Geometric Deep Learning under Distribution Shifts

- Decision: Reject
- Avg Score: 5.67
- Scores: 6, 3, 8

## Abstract
Geometric deep learning (GDL) has gained significant attention in various scientific fields, chiefly for its proficiency in modeling data with intricate geometric structures. Yet, very few works have delved into its capability of tackling the distribution shift problem, a prevalent challenge in many relevant applications. To bridge this gap, we propose GDL-DS, a comprehensive benchmark designed for evaluating the performance of GDL models in scenarios with distribution shifts. Our evaluation datasets cover diverse scientific domains from particle physics and material science to biochemistry, and encapsulates a broad spectrum of distribution shifts including conditional, covariate, and concept shifts. 
Furthermore, we study three levels of information access from the out-of-distribution (OOD) testing data, including no OOD information, only OOD features without labels, and OOD features with a few labels. 
Overall, our benchmark results in 30 different experiment settings, and evaluates 3 GDL backbones and 11 learning algorithms in each setting. A thorough analysis of the evaluation results is provided, poised to illuminate insights for DGL researchers and domain practitioners who are to use DGL in their applications.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper effectively addresses the challenge of evaluation of deep learning models generalization abilities under distribution shift in geometric deep learning (point cloud data). It categorizes various sources of distribution shift between training and testing domains and introduces a new benchmark dataset spanning three distinct domains: particle collision physics, chemistry, and material science. The paper further evaluates multiple models, drawing conclusions and recommendations regarding which methods generalize better in specific scenarios

### Strengths
The introduction of a new benchmark dataset that spans different domains and types of distribution shifts is a noteworthy contribution. This dataset allows for a more nuanced comparison of deep learning methods based on the specific type of shift, making it practically significant and important for the research community.

The paper's coverage of various scientific fields, including particle collision physics, chemistry, and material science, broadens its applicability and relevance, potentially opening up opportunities for interdisciplinary research.

The paper is clearly written and technically sound.

### Weaknesses
It's crucial to include detailed information about the characteristics of the new benchmark datasets and of the already existing datasets. Providing information on data size and other characteristics would enhance the reader's understanding of the datasets' properties and its applicability.



### Questions
n/a

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
The paper presents a OOD benchmark for geometric deep learning in science. The authors curate datasets from 3 scientific domains, identify several shifts in each dataset, and conduct 3 OOD splits for each shift. Then each setting is used to evaluate 3 GDL backbones and several OOD methods.

### Strengths
1. The paper focuses a a very compelling topic. OOD datasets and benchmarks for geometric deep learning in science are innovative and meaningful research.

2. The paper presentation includes rich contents, with tables and figures well organized.

3. The selected data presents practical tasks. The conducted experiments look correct and sufficient experimental analyses are given.

### Weaknesses
1. The use of critical terms should be better considered. Concept drift is a well-established term in the study of causality and distribution shift. As defined in [1], which the authors also cited, the only constraint for concept drift is "changes in $p(y|X)$". To avoid any confusions to readers, this conventional definition should be followed without modifications like $P(Y|X_c)$. Similarly for the definition of covariate shift. If the authors attempt to define a more specific kind of shift, another term should be used.

2. The causal statements are problematic.
    - The statement that $X$ consists of two disjoint parts and $X_i ⊥Y |X_c$ does not hold. A easy violation would be $X_c →Y →X_i$. Intrinsically, $Y$ is often a property of the input and therefore $X$ cannot be divided into two disjoint parts that are causal/independent, but there would exist a part of $X$ that is statistically associated with $Y$ while non-causal to $Y$. A classic example is the PIIF and FIIF causal modeling, such as the analysis in [2].
    - Following the above point, even for $X → Y$, $P(Y|X)P(X) = P(Y|X_c)P(X)$ does not hold. For $X → Y$, there can be a case where $P_S(Y |X_i)\neq P_T (Y |X_i)$, which will also result in a "conditional shift". It is also included by the definition of concept shift. Constraining $Y → X$ does not seem like a necessity for conditional shift.
    - Overall, as the foundation of the whole paper, 3.1 appears to be logically unclear and farraginous and needs major corrections.

3. Contribution overclaimed and related works not well addressed. In the comparison with existing benchmarks, the authors claim no existing OOD benchmarks consider conditional shift, which is not true. OoD-Bench, GDS, and GOOD all include the Cmnist dataset, which is clearly conditional shift. GOOD also constructed conditional shift for each dataset. Also, though benchmarks like WILDS do not use test labeled/unlabeled data for algorithm learning, these OOD info are available. Therefore, Table 1 gas multiple overclaiming issues, and the authors should treat existing works properly.

4. Experimental setting not fair. Some methods are trained solely on the Train-ID dataset, while DA algorithms are trained on both Train-ID and OOD input data, and TLs also learn labeled Train-OOD data. This does not seem like a fair setting since different methods are trained on even different numbers of data samples. Given that the analyses are conducted based on comparing all these methods together, a fair evaluation setting is certainly needed.

5. Baselines out-of-date. These years many new OOD methods including new sota have been proposed. The benchmark should include more recent methods as baselines. For learning algorithms the sota methods on the Wilds leaderboard should be considered. For graph OOD methods, many recent methods can easily outperform DIR. Also, geometric methods specifically developed for scientific tasks should be considered.

6. The benchmark includes only 3 datasets. Though more than one shift is identified for each dataset, this number seems a bit few for a benchmark. Given that the datasets are not newly collected, possibly more discussions on contributions like curating 3D coordinate can make up for the overall contribution.

### Questions
See Weaknesses

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper addresses the challenge of distribution shifts in Geometric Deep Learning (GDL), a topic that has seen limited research focus despite GDL's prominence in various scientific applications. The authors introduce GDL-DS, a comprehensive benchmark designed to evaluate the performance of GDL models across scenarios that encounter distribution shifts. They provide a comprehensive evolution on several datasets from different fields; particle physics, materials science, and biochemistry, and categorize distribution shifts into three types: conditional, covariate, and concept shifts. Furthermore, they explore three levels of out-of-distribution (OOD) information access and evaluate multiple GDL backbones and learning algorithms. The benchmark consists of 30 experiment settings, and the findings provide valuable insights for researchers and practitioners in the GDL domain.

### Strengths
- The paper presents a comprehensive benchmark for GDL models, covering a spectrum of scientific domains and distribution shifts. Such a benchmark fills an existing gap in the literature.

- The authors leverage the causality inherent in scientific applications to classify distribution shifts into conditional, covariate, and concept shifts, providing a clearer understanding of the challenges faced.

- By exploring three distinct levels of OOD information, the paper offers a nuanced understanding of the impact of OOD data on model performance, addressing disparities in previous works.

- The paper conducts a myriad of experiments, with 30 different settings, evaluating various GDL backbones and learning algorithms, ensuring a robust and holistic evaluation.

- The results yield key takeaways that can guide the selection of practical solutions based on the availability of OOD data, serving as a valuable resource for researchers and practitioners.

### Weaknesses
Given the disparities in previous benchmarking studies across various domains,, there's a compelling case to expand this benchmark study to encompass both CV and NLP tasks to provide a holistic and unified perspective on performances across diverse tasks.

### Questions
- How do the findings of this study compare with earlier research on CV and NLP tasks concerning distribution shifts?

- What is the rationale behind the choice of the considered GL backbones? Would incorporating more diverse GDL backbones or learning algorithms significantly alter the conclusions drawn from this study?

### Soundness
4 excellent

### Presentation
4 excellent

### Contribution
4 excellent
