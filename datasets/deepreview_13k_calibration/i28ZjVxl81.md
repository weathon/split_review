# DEALING WITH OUT OF DISTRIBUTION IN PREDICTION PROBLEM

- Decision: Reject
- Avg Score: 2.50
- Scores: 1, 5, 3, 1

## Abstract
The open world assumption in model development means that a model may lack sufficient
information to effectively handle data that is completely different or out of distribution
(OOD). When a model encounters OOD data, its performance can significantly decrease.
Improving the model’s performance in dealing with OOD can be achieved through gener-
alization by adding noise, which can be easily done with deep learning. However, many
advanced machine learning models are resource-intensive and designed to work best with
specialized hardware (GPU), which may not always be available for common users with
hardware limitations. To provide a deep understanding and solution on OOD for gen-
eral user, this study explores detection, evaluation, and prediction tasks within the context
of OOD on tabular datasets using common consumer hardware (CPU). It demonstrates
how users can identify OOD data from available datasets and provide guidance on eval-
uating the OOD selection through simple experiments and visualizations. Furthermore,
the study introduces Tabular Contrast Learning (TCL), a technique specifically designed
for tabular prediction tasks. While achieving better results compared to heavier models,
TCL is more efficient even when trained without specialised hardware, making it useful
for general machine-learning users with computational limitations. This study includes
a comprehensive comparison with existing approaches within their best hardware setting
(GPU) compared with TCL on common hardware (CPU), focusing on both accuracy and
efficiency. The results show that TCL exceeds other models, including gradient boosting
decision trees, contrastive learning, and other deep learning models, on the classification
task.

## Human Reviews

## Human Reviewer 1

### Rating
1

### Rating Number
1

### Confidence
5

### Summary
The paper applies an existing method (Contrastive Federated Learning, or CFL) to tabular data prediction tasks. The authors use 10 toy tabular datasets to evaluate this method and compare with a set of deep learning-based baselines on various classification and regression metrics.

### Strengths
# Overall assessment

In general, the writing in the paper could be improved considerably. The paper is missing references to many relevant works in the tabular prediction literature, and fails to compare to many relevant baselines (most notably, GBDT methods like XGBoost, LightGBM, and CatBoost). The datasets selected for the empirical comparisons are not appropriate for this study, as these datasets do not display distribution shift, while the authors do not use or acknowledge several existing benchmarks for OOD prediction in tabular data.

# Major comments

* Many of the main claims in the abstract lack support or are difficult to verify -- for example, "Addressing OOD data requires extensive fine-tuning and experimental trials" and "Deep learning has been sug-
gested as a solution and has shown significant improvements".

* The paper is missing references to many relevant works, including:
  - Malinin, Andrey, et al. "Shifts 2.0: Extending the dataset of real distributional shifts." arXiv preprint arXiv:2206.15407 (2022). 
  - Gardner, Josh, Zoran Popovic, and Ludwig Schmidt. "Benchmarking distribution shift in tabular data with tableshift." Advances in Neural Information Processing Systems 36 (2024).
  - Liu, Jiashuo, et al. "On the need for a language describing distribution shifts: Illustrations on tabular datasets." Advances in Neural Information Processing Systems 36 (2024).

  All three of the above papers propose benchmarks for OOD-related tabular tasks. These would be much more appropriate than the 10 toy datasets selected for the empirical studies.

* The paper is also missing references to several relevant empirical studies for tabular data, including: 
  - Gardner, Josh, Zoran Popovic, and Ludwig Schmidt. "Subgroup robustness grows on trees: An empirical baseline investigation." Advances in Neural Information Processing Systems 35 (2022): 9939-9954.
  - Grinsztajn, Léo, Edouard Oyallon, and Gaël Varoquaux. "Why do tree-based models still outperform deep learning on typical tabular data?." Advances in neural information processing systems 35 (2022): 507-520.
  - Kadra, Arlind, et al. "Well-tuned simple nets excel on tabular datasets." Advances in neural information processing systems 34 (2021): 23928-23941.

  In particular, the first two studies above suggest that GBDTs are perhaps the most appropriate baseline for this study, but they are omitted from the study completely.

* The paper frames its use of contrastive learning as a novel contribution, however, there are two problems with this:
  1. Contrastive learning has already been widely used for tabular data; See e.g. (Bahri, D., Jiang, H., Tay, Y., & Metzler, D. (2021). Scarf: Self-supervised contrastive learning using random feature corruption. arXiv preprint arXiv:2106.15147.) and the survey of (Rabbani, Shourav B., Ivan V. Medri, and Manar D. Samad. "Attention versus Contrastive Learning of Tabular Data--A Data-centric Benchmarking." arXiv preprint arXiv:2401.04266 (2024).) In particular I would note that its performance has generally not been competitive with strong baselines and adoption of the method has been limited as a result.
  2. The paper simply applies an existing method (Contrastive Federated Learning, or CFL) to tabular data. This is not sufficient for acceptance, given the concerns with the empirical evaluations described above.

# Minor comments

* More detail should be provided on the datasets in the main text (note that I suggest completely changing the datasets to more appropriate distribution shift datasets). In particular, the authors should explain why these generic tabular datasets (e.g. Adult, California Housing) are appropriate for studying the very specific task of OOD detection. Some descriptive statustucs about the datasets would also be useful.

# Typos etc.

* The paper is quite difficult to read in places due to grammatical issues. I would suggest having a native English speaker proofread the manuscript, or using a grammar checking tool.
* Definition 4: "eucledian"

### Weaknesses
 # Overall assessment

In general, the writing in the paper could be improved considerably. The paper is missing references to many relevant works in the tabular prediction literature, and fails to compare to many relevant baselines (most notably, GBDT methods like XGBoost, LightGBM, and CatBoost). The datasets selected for the empirical comparisons are not appropriate for this study, as these datasets do not display distribution shift, while the authors do not use or acknowledge several existing benchmarks for OOD prediction in tabular data.

# Major comments

* Many of the main claims in the abstract lack support or are difficult to verify -- for example, "Addressing OOD data requires extensive fine-tuning and experimental trials" and "Deep learning has been sug-
gested as a solution and has shown significant improvements".

* The paper is missing references to many relevant works, including:
  - Malinin, Andrey, et al. "Shifts 2.0: Extending the dataset of real distributional shifts." arXiv preprint arXiv:2206.15407 (2022).
  - Gardner, Josh, Zoran Popovic, and Ludwig Schmidt. "Benchmarking distribution shift in tabular data with tableshift." Advances in Neural Information Processing Systems 36 (2024).
  - Liu, Jiashuo, et al. "On the need for a language describing distribution shifts: Illustrations on tabular datasets." Advances in Neural Information Processing Systems 36 (2024).

  All three of the above papers propose benchmarks for OOD-related tabular tasks. These would be much more appropriate than the 10 toy datasets selected for the empirical studies.

* The paper is also missing references to several relevant empirical studies for tabular data, including:
  - Gardner, Josh, Zoran Popovic, and Ludwig Schmidt. "Subgroup robustness grows on trees: An empirical baseline investigation." Advances in Neural Information Processing Systems 35 (2022): 9939-9954.
  - Grinsztajn, Léo, Edouard Oyallon, and Gaël Varoquaux. "Why do tree-based models still outperform deep learning on typical tabular data?." Advances in neural information processing systems 35 (2022): 507-520.
  - Kadra, Arlind, et al. "Well-tuned simple nets excel on tabular datasets." Advances in neural information processing systems 34 (2021): 23928-23941.

  In particular, the first two studies above suggest that GBDTs are perhaps the most appropriate baseline for this study, but they are omitted from the study completely.

* The paper frames its use of contrastive learning as a novel contribution, however, there are two problems with this:
  1. Contrastive learning has already been widely used for tabular data; See e.g. (Bahri, D., Jiang, H., Tay, Y., & Metzler, D. (2021). Scarf: Self-supervised contrastive learning using random feature corruption. arXiv preprint arXiv:2106.15147.) and the survey of (Rabbani, Shourav B., Ivan V. Medri, and Manar D. Samad. "Attention versus Contrastive Learning of Tabular Data--A Data-centric Benchmarking." arXiv preprint arXiv:2401.04266 (2024).) In particular I would note that its performance has generally not been competitive with strong baselines and adoption of the method has been limited as a result.
  2. The paper simply applies an existing method (Contrastive Federated Learning, or CFL) to tabular data. This is not sufficient for acceptance, given the concerns with the empirical evaluations described above.

# Minor comments

* More detail should be provided on the datasets in the main text (note that I suggest completely changing the datasets to more appropriate distribution shift datasets). In particular, the authors should explain why these generic tabular datasets (e.g. Adult, California Housing) are appropriate for studying the very specific task of OOD detection. Some descriptive statustucs about the datasets would also be useful.

# Typos etc.

* The paper is quite difficult to read in places due to grammatical issues. I would suggest having a native English speaker proofread the manuscript, or using a grammar checking tool.
* Definition 4: "eucledian"

### Questions
See above.

### Soundness
2

### Presentation
3

### Contribution
1

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This study focuses on detecting and predicting OOD data in tabular datasets. It provides methods for identifying OOD data, guidance on evaluating OOD selections, and introduces Tabular Contrast Learning (TCL), a technique optimized for tabular predictions. 
TCL seems to be more computationally efficient than baseline models, making it suitable for general users with limited computational power. The study also compares TCL with existing approaches, emphasizing both accuracy and efficiency.

### Strengths
+ Multiple Dataset and Models

+ Impressing Experiments and Results

The manuscript tackles an important challenge in machine learning by focusing on out-of-distribution (OOD) data handling for tabular datasets, and introduces Tabular Contrast Learning (TCL) as a novel solution. This is a well-defined problem with significant practical implications, especially for general users with computational limitations. The authors have provided a clear motivation for their work, particularly in making OOD detection and handling accessible without high-end hardware requirements. The proposed TCL method appears promising for addressing efficiency and accuracy in tabular OOD tasks.

### Weaknesses
However, it would benefit from a more detailed comparison with recent advancements in tabular contrastive learning. Notably, two works could provide relevant baselines and enhance the context for TCL.
- Best of Both Worlds: Multimodal Contrastive Learning With Tabular and Imaging Data, CVPR23
- TabContrast: A Local-Global Level Method for Tabular Contrastive Learning, NIPS23


- Why is the Contrastive Federated Learning (CFL) reference in an anonymized link?
- Why does the title miss some keywords like Tabular Contrastive Learning?
- Why is there no experiment for baseline models running on CPU (Apple) to fairly compare with your TCL?

### Questions
- Why is the Contrastive Federated Learning (CFL) reference in an anonymized link?
- Why does the title miss some keywords like Tabular Contrastive Learning?
- Why is there no experiment for baseline models running on CPU (Apple) to fairly compare with your TCL?

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
The article presents a method called tabular contrast learning (TCL) aimed at improving model performance on tabular datasets, particularly in the context of Out-of-Distribution (OOD) tabular data. The authors highlight TCL's efficiency in reducing computational costs and its potential for deployment in resource-limited environments. The paper discusses the model's training process and experimental results across 10 datasets.

### Strengths
1. The research addresses an important issue in machine learning—handling OOD data, which is crucial for ensuring model reliability and robustness.
2. TCL demonstrates a very efficient approach that reduces computational costs, making it viable for deployment in environments with limited resources.

### Weaknesses
1. The experimental results are not particularly impressive. While TCL shows high efficiency, it only achieved optimal performance on three datasets compared to FT-T and ResNet.
2. The paper lacks a comprehensive comparison of methods. It would benefit from including comparisons with GBDT methods (e.g., CatBoost[1], XGBoost[2]), other state-of-the-art deep learning models (e.g., TabR[3], ExcelFormer[4], Trompt[5]), and alternative self-supervised learning algorithms (e.g., Scarf[6], VIME[7]) besides SubTab.
3. More details should be included in the paper, such as the specific structure of TCL, the downstream classifier used, hyperparameters of the comparison methods, and whether experiments were conducted multiple times to present average results.
4. The experiment comparing dot product and Euclidean distance indicates that dot product is more efficient on the hardware they used. However, this work does not discuss how using these two distance metrics impacts the performance of TCL and how significant the computational time for distance calculation is within the entire TCL process.

### Questions
1. See weaknesses
2. What criteria did the authors use to select different detectors for OOD detection across various datasets? 
3. Authors may want to assess the performance of TCL using the recently published benchmark, TabRed [1], which is a Benchmark of Tabular Machine Learning in-the-Wild with Real-World Industry-Grade Tabular Datasets.

[1] Ivan Rubachev, Nikolay Kartashev, Yury Gorishniy, Artem Babenko: TabReD: A Benchmark of Tabular Machine Learning in-the-Wild.

### Soundness
1

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
1

### Rating Number
1

### Confidence
4

### Summary
This paper tackles the OOD issue for tabular data by using a framework consisting of contrastive learning. To separate in-domain and out-of-domain samples for experiments, the authors adopt OpenMax and Temperature Scaling with manually assigning the thresholds. The proposed TCL shows higher speed-accuracy trade-off scores, which was only trained on a CPU.

### Strengths
1. The proposed method is easy to understand, with a clear problem statement and definition.
2. Simaltaneously considering the OOD problem with efficiency may be an interesting direction, especially in the realm of large-scale models.

### Weaknesses
Generally, this paper requires extensive improvements in terms of motivations, related works, proposed method, as well as the experiments. Detailed comments are provided below:

1. The paper presentation should be improved. In the abstract, for instance, the issues in existing OOD works do not appear novel. Extensive fine-tuning and experimental trials are not unique to this specific OOD problem but relate to many general issues. The authors need to outline issues more specific to the OOD problem.
2. The review of related works requires significant improvement. There is a substantial body of existing work on OOD in tabular domains; however, the authors only discuss two methods in Sec. 2.1 and one other in L38, with the most recent paper referenced from 2017. The authors should put more effort into the literature review, for example, [1].
3. The proposed TCL employs a common strategy: contrastive learning with two views generated from a sample for self-supervised learning, followed by a head for classification/regression. This framework has been used in various contrastive learning-based tabular models, such as SubTab, which modifies contrastive targets with slicing techniques for tabular structures. The performance is not superior to the selected baselines, which limits both the novelty and effectiveness of the proposed approach.
4. The selected baselines are based on the work of Gorishniy et al., 2021, which was published in 2021. Since then, many advanced tabular prediction models have emerged and should be included in this paper, such as those summarized in [2]. Note that some of these models serve as tabular foundation models and may not experience the OOD issues described in this paper.
5. The authors used CPU(s) to train their model but used an H100 GPU for the baselines, which is confusing. I didn't see any specific design element that would make the proposed method more efficient; on the contrary, matrix augmentation appears to require more computational resources. Although Table 4 presents training durations, it is unclear how this table was created. For example, is the parameter space the same across all models?

### Questions
Please see above comments.

### Soundness
1

### Presentation
1

### Contribution
1
