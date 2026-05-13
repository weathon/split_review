# Investigating Domain Gaps for Indoor 3D Object Detection

- Decision: Reject
- Scores: 5, 3, 6, 5, 6

## Abstract
As a fundamental task for indoor scene understanding, 3D object detection has been extensively studied, and the accuracy on indoor point cloud data has been substantially improved. However, existing researches have been conducted on limited datasets, where the training and testing sets share the same distribution. In this paper, we consider the task of adapting indoor 3D object detectors from one dataset to another, presenting a first benchmark with commonly used ScanNet and SUN RGB-D datasets, as well as our newly proposed large-scale SimRoom and SimHouse datasets by a 3D simulator with far greater number of objects and more precise annotations. Since indoor point cloud datasets are collected and constructed in different ways, the object detectors are likely to overfit to specific factors within each dataset, such as point cloud quality, room layout configuration, style and object size. We conduct experiments across datasets on different adaptation scenarios, analyzing the impact of different domain gaps on 3D object detectors. We observe that through our evaluated domain gap factors, synthetic-to-real adaptation is the most difficult adaptation hurdle to overcome. We also introduce several domain adaptation approaches to improve adaptation performances, providing a first baseline for domain adaptive indoor 3D object detection, hoping that future works may propose detectors with stronger generalization ability across domains.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The paper investigates the challenge of domain adaptation for indoor 3D object detection by introducing new synthetic datasets, SimRoom and SimHouse, and presenting domain adaptation benchmarks across several main scenarios. The paper examines and analyzes factors such as point cloud quality, room layout, synthetic-to-real style, and object size to highlight the issue of domain adaptation for indoor 3D scenes. Additionally, the authors provide baseline results using simple adaptation methods to assess the performance of models trained on one domain and tested on another.

### Strengths
The paper provides a detailed analysis of the impact of domain gaps on model performance. This is useful for understanding specific adaptation challenges and will benefit future work to address these potential issues in real practice. 
Besides showing the challenges, the proposed synthetic datasets, SimRoom and SimHouse, also offer more diverse and scalable data compared to existing real-world datasets, enabling controlled experiments for domain adaptation. 
Overall, this paper presents a novel benchmark specifically for indoor 3D object detection domain adaptation, contributing to the field's progress.

### Weaknesses
The baseline domain adaptation methods implemented are straightforward and lack complexity. Methods like the mean teacher framework and size priors are standard and do not demonstrate significant innovation or exploration of recent advancements in domain adaptation, using such basic adaptation methods might be insufficient to challenge future models. 
In addition, although the paper claims that the synthetic datasets have high-quality annotations, there is a lack of discussion about how faithfully these datasets mimic real-world scenarios. More detailed analysis of data consistency and potential annotation noise could demonstrate the reliability and generalizability of the results.
Also, the paper could provide more information about the consistency and quality assurance processes used in annotating SimRoom and SimHouse. Since the study utilizes the SimRoom and SimHouse with our existing datasets, inconsistencies or errors in labeling between these datasets collected can lead to unreliable benchmarks and misleading conclusions. Further discussion demonstrating the consistency of the data collection and labeling processes for these datasets will be beneficial for establishing the benchmark.

### Questions
It'll be helpful if the authors can provide more details on how data quality and annotation consistency were ensured in the SimRoom and SimHouse datasets.
I hope the authors provide more details about why they chose to implement baseline methods such as few-shot fine-tuning or mean teacher framework for domain adaptation instead of considering more methods, such as adversarial training or self-supervised learning, for stronger comparisons.
Most importantly, I was wondering if the authors have any plans to make SimRoom and SimHouse publicly available.
I appreciate any responses to these questions!

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper explores the task of domain adaptation in the task of indoor 3D object detection by building a new domain adaptation benchmark. The benchmark datasets include the widely-used ScanNet and SUN RGB-D datasets, as well as the newly proposed SimRoom and SimHouse synthetic datasets. SimHouse dataset is generated by sampling large-scale house layouts with ProcTHOR framework originally designed for embodied AI tasks, and SimRoom is generated by splitting SimHouse scenario into different rooms. Four domain adaptation settings are explored, and the experiments show that the synthetic to real domain gap is the most significant domain gap. Extensive experiments are conducted on this benchmark, providing the first baseline for the domain adaptation of indoor 3D object detection.

### Strengths
1. The paper generated a large-scale synthetic dataset for ablating indoor 3D object detection task, which may help multiple potential tasks for indoor scene understanding.
2. The paper demonstrates extensive experiments to ablate different basic approaches on the newly proposed domain adaptation benchmark.

### Weaknesses
1. This paper does not provide adequate discussions about the applications and importance of the task of domain adaptation in indoor 3D object detection. Moreover, it also doesn't discuss the differences and unique values compared with the task of outdoor domain adaptation of 3D object detection.  
2. It seems that the generation process of the SimRoom / SimHouse dataset is a simple usage of ProcTHOR framework. 
3. For the domain adaptation benchmark, it is also the application of multiple existing approaches, and the technical contribution is limited.

### Questions
1. The authors claim that this is the first baseline for domain adaptive indoor 3D object detection. However, these already exist many papers about domain adaptive outdoor 3D object detection. Hence, it is necessary to compare with domain adaptive outdoor 3D object detection task and highlight the unique values / differences between these two tasks.
2. Typos: 
a) L093: SUN RGB-D -> SUN RGB-D? 
b) L262: static -> statistic
c) L320: out of the scope

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This study introduces novel benchmarks for domain adaptation in indoor 3D object detection, utilizing established datasets (ScanNet and SUN RGB-D) alongside two newly created large-scale synthetic datasets, SimRoom and SimHouse, which contain a greater number of objects and provide highly accurate annotations.The authors systematically examine various domain gaps, including point cloud quality, differences between synthetic and real-world data, room layout, and object size. Cross-dataset experiments reveal that adapting from synthetic to real-world data poses the most significant challenge. To address these challenges, the study evaluates several domain adaptation techniques as baseline methods to improve model performance in cross-domain scenarios. This work lays a foundation for future research aimed at developing robust indoor 3D object detectors capable of generalizing across diverse indoor environments.

### Strengths
This paper focuses on indoor 3D object detection, moving beyond the traditional emphasis on outdoor environments. The authors introduce two larger, novel synthetic datasets to facilitate exploration in this area. Through experiments conducted across multiple adaptation scenarios, they analyze critical factors such as point cloud quality and object size, thoroughly investigating their impact on model adaptability.The structure of the paper is clear, with a rigorous logical flow and fluent expression. The motivation for the study is well-articulated, effectively highlighting the necessity and significance of the research. These contributions provide a substantial foundation for further investigation into domain adaptation in indoor 3D object detection, showcasing notable academic value and practical application potential

### Weaknesses
1.The authors emphasize the low annotation costs associated with their synthetic datasets. However, a comparative analysis of the annotation costs, speeds, and methodologies between their simulation data generation approach and other synthetic data generation techniques, as well as traditional manual annotation methods, would strengthen their argument. Including such an analysis could provide insights into the efficiency and scalability of their approach relative to existing methods, highlighting the practical advantages or limitations of using simulated data.
2.The paper would benefit from a detailed comparison with recent works. For example, the unsupervised domain adaptation method for indoor 3D detection by Wang et al. ([1]) presents an alternative approach that could be discussed alongside the authors' findings. Highlighting the similarities, differences, and potential synergies between these methods would provide valuable context for readers.
Additionally, Lu et al.'s work ([2]), which focuses on open-vocabulary 3D object detection without the need for 3D annotations, offers useful benchmarks. The authors could reference Table 3 from that study, which examines transfer learning effectiveness in indoor 3D detection. Comparing their results with those of Lu et al. would clarify how their methods contribute to the state of the art and identify areas for further exploration.

### Questions
Please refer to the weaknesses section above.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The authors present the first benchmark for domain adaptation in indoor 3D object detection using existing standard datasets (ScanNet, SUN RGB-D) along with new synthetic datasets (SimRoom, SimHouse).

SimRoom and SimHouse are large-scale indoor point cloud datasets with a large number of objects and precise annotation.

These datasets are collected using a 3D simulator following the ProcTHOR.

With four datasets, the authors investigate four different domain adaptation scenarios: high-to-low-quality, low-to-high-quality, synthetic-to-real, and single-to-multiroom.

They evaluate various domain gap factors and observe that synthetic-to-real adaptation is the most challenging.

### Strengths
- The authors provide a thorough analysis of existing datasets, highlighting the differences between them.
Then, they clearly identify factors of challenging domain gaps across datasets.
Based on these investigations, they propose large-scale simulated indoor datasets (SimRoom, SimHouse) to complement existing datasets.

- The creation process of the large-scale dataset is comprehensively defined.
Through low-cost, precise annotation, they build a well-organized dataset.

- Through extensive experiments, the authors present meaningful benchmarks for various domain adaptation scenarios in indoor 3D object detection.

### Weaknesses
 - Unlike datasets collected from real-world environments, synthetic datasets usually differ in texture detail and material realism. 
Also, they have the risk of including simplistic object shapes and monotonous layouts.
These differences are likely significant factors in the large domain gap between synthetic-to-real datasets.
In this paper, the analysis of these differences is unclear, and it would be better to evaluate how well the proposed dataset reflects real-world conditions.

- While the proposed datasets include a large number of scene and object annotations, their significant domain gap from real-world datasets raises questions about their usefulness for various real-world settings.

- Although the dataset creation process is well-described, technical novelty is somewhat limited.
Their proposed framework, Mean Teacher, seems to simply follow previous work without adequately considering the diverse factors of domain gaps.

### Questions
- Did the authors consider experiments to observe domain gaps in the real-to-synthetic (scn2rm) settings?
These experiments could help support the applicability of the proposed dataset.

- How many different designs of each object are included in this synthetic dataset? 
For example, in real-world environments, there is a variety of bed shapes or a diversity of chair designs.
Also, how many different types of room layouts are included?

- Did the authors consider resembling real-world environments when creating the scenes? 
I have some concerns about the potential of this dataset to effectively complement existing datasets and be utilized in various 3D vision tasks.

While this work is well written, I have a few questions, as outlined in the weaknesses and questions. A clarification of the points I mentioned would help me improve my decision.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 5

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper mainly discussed about indoor 3D object detection domain adaptation, which is an underexplored topic. It analyzes the statistics and characteristics of existing indoor datasets and proposes two synthetic datasets, SimRoom and SimHouse. This paper also conducted extensive experiments on different domain adaptation settings across datasets.

### Strengths
1. This paper focuses on an underexplored topic which is of potential.
2. The experiments are comprehensive.
3. This paper also proposes two large-scale synthetic datasets.

### Weaknesses
1. Lack of comparison with 3D-FRONT: A more thorough comparison between proposed SimRoom and SimHouse with 3D-FRONT [1] would be beneficial. 3D-FRONT is also of large quantity and high point cloud quality, with expert-designed room layouts which can potentially narrow the synthetic to real domain gap.

2. The paper lacks comparison with recent syn-to-real domain adaptation work. Specifically, a comparison with the method proposed in [2] would better evaluate the significance of the paper.



### Questions
1. I noticed that there was a recent work [1] which focuses on syn-to-real domain adaptation. A comparison with this paper would better evaluate the significance of the paper.
2. According to the results, the synthetic-to-real domain gaps seem difficult to narrow down without priors of the target dataset. Then is this setting practical?


[1] Wang, Yunsong, Na Zhao, and Gim Hee Lee. "Syn-to-Real Unsupervised Domain Adaptation for Indoor 3D Object Detection." arXiv preprint arXiv:2406.11311 (2024).

### Soundness
2

### Presentation
2

### Contribution
2
